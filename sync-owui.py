#!/usr/bin/env python3
"""sync-owui.py — push this repo's prompts to an Open WebUI instance.

Mapping
-------
* ``dist/system-prompt/**/*.prompt.md`` become Open WebUI **custom Models**.
  Their YAML frontmatter carries the model metadata (``name``, ``description``,
  ``tags``, ``base_model``, ``tool_ids``); the rest of the file is the model's
  system prompt.
* every other ``dist/**/*.prompt.md`` becomes an Open WebUI **Prompt** — the
  ``/slash`` commands inserted into the chat composer. The command is derived
  from the file name.

Ownership
---------
Every item this script writes is tagged ``meta.managed_by = "ronzz-LLM-prompt-hub"``.
On the next run the sync updates those items, and hard-deletes the managed
items that no longer exist in the repo. Hand-made items are never deleted. An
item whose id/command collides with a repo item is *adopted* (updated and
tagged), never duplicated.

Configuration (environment)
---------------------------
    OWUI_URL         base URL            (default: https://llm.ronzz.org)
    OWUI_API_KEY     admin API key       (required)
    OWUI_BASE_MODEL  default base model  (default: deepseek-flash)

Usage
-----
    python3 sync-owui.py --dry-run    # show what would change, write nothing
    python3 sync-owui.py              # rebuild dist/, then sync
    python3 sync-owui.py --no-build   # skip the build-prompts.py rebuild
    python3 sync-owui.py --no-prune   # never delete (add/update only)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SYSTEM_DIST = DIST / "system-prompt"

MANAGE_TAG = "ronzz-LLM-prompt-hub"
DEFAULT_OWUI_URL = "https://llm.ronzz.org"
DEFAULT_BASE_MODEL = "deepseek-flash"
DEFAULT_IMAGE = "/static/favicon.png"

# Visible to every logged-in user (principal_type "user" + wildcard id).
PUBLIC_READ = [{"principal_type": "user", "principal_id": "*", "permission": "read"}]

# Features switched on by default when the model is opened in the composer.
DEFAULT_FEATURE_IDS = ["code_interpreter", "web_search"]

# Capability gates — mirrors the hand-made ronzz models already on the instance.
CAPABILITIES = {
    "file_context": True,
    "vision": True,
    "file_upload": True,
    "web_search": True,
    "image_generation": True,
    "code_interpreter": True,
    "terminal": True,
    "citations": True,
    "status_updates": True,
    "memory": True,
    "builtin_tools": True,
}

PROMPT_SUFFIX = ".prompt.md"
# The build prepends two HTML comment lines (generated marker + source path)
# followed by a blank line.
HEADER_RE = re.compile(r"\A(?:\s*<!--.*?-->)+[ \t\r\n]*", re.DOTALL)
# Optional YAML frontmatter block at the head of a source file.
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
SLUG_RE = re.compile(r"[^A-Za-z0-9_-]+")


class SyncError(Exception):
    """Fatal sync error (bad input, API failure, collision)."""


# --- built-file parsing ---------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a leading YAML frontmatter block from the body.

    Supports the flat subset this repo uses: ``key: value`` and
    ``key: [a, b]`` (inline lists). Values stay strings except inline lists.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise SyncError(f"bad frontmatter line (expected 'key: value'): {raw!r}")
        key, _, value = line.partition(":")
        meta[key.strip()] = _parse_scalar(value.strip())
    return meta, text[match.end():]


def _parse_scalar(value: str):
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(item.strip()) for item in inner.split(",") if item.strip()]
    return _unquote(value)


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


def read_built(path: Path) -> tuple[dict, str]:
    """Return (frontmatter, body) for a built ``*.prompt.md`` file."""
    text = HEADER_RE.sub("", path.read_text(encoding="utf-8"))
    frontmatter, body = parse_frontmatter(text)
    return frontmatter, body.strip("\n") + "\n"


def slugify(stem: str) -> str:
    slug = SLUG_RE.sub("-", stem).strip("-").lower()
    if not slug:
        raise SyncError(f"cannot derive a command/id from {stem!r}")
    return slug


# --- desired state --------------------------------------------------------


def collect_models() -> dict[str, dict]:
    """Desired Open WebUI models, keyed by model id."""
    items: list[tuple[str, dict]] = []
    if SYSTEM_DIST.is_dir():
        for path in sorted(SYSTEM_DIST.rglob(f"*{PROMPT_SUFFIX}")):
            stem = path.name[: -len(PROMPT_SUFFIX)]
            model_id = slugify(stem)
            frontmatter, body = read_built(path)
            name = frontmatter.get("name") or stem
            meta = {
                "managed_by": MANAGE_TAG,
                "profile_image_url": frontmatter.get("profile_image_url", DEFAULT_IMAGE),
                "description": frontmatter.get("description"),
                "tags": [{"name": tag} for tag in frontmatter.get("tags", [])],
                "toolIds": frontmatter.get("tool_ids", []),
                "defaultFeatureIds": DEFAULT_FEATURE_IDS,
                "capabilities": CAPABILITIES,
            }
            items.append((model_id, {
                "form": {
                    "id": model_id,
                    "base_model_id": frontmatter.get("base_model") or DEFAULT_BASE_MODEL,
                    "name": name,
                    "meta": meta,
                    "params": {"system": body},
                    "access_grants": PUBLIC_READ,
                    "is_active": True,
                },
                "source": path.relative_to(ROOT),
            }))
    return _unique(items, "model id")


def collect_prompts() -> dict[str, dict]:
    """Desired Open WebUI prompts (slash commands), keyed by command."""
    items: list[tuple[str, dict]] = []
    for path in sorted(DIST.rglob(f"*{PROMPT_SUFFIX}")):
        if SYSTEM_DIST in path.parents:
            continue
        stem = path.name[: -len(PROMPT_SUFFIX)]
        command = slugify(stem)
        _, body = read_built(path)
        items.append((command, {
            "form": {
                "command": command,
                "name": stem,
                "content": body,
                "meta": {
                    "managed_by": MANAGE_TAG,
                    "source": str(path.relative_to(ROOT)),
                },
                "access_grants": PUBLIC_READ,
            },
            "source": path.relative_to(ROOT),
        }))
    return _unique(items, "command")


def _unique(items: list[tuple[str, dict]], what: str) -> dict[str, dict]:
    """Build a keyed mapping, failing loudly on a collision."""
    result: dict[str, dict] = {}
    for key, entry in items:
        if key in result:
            raise SyncError(
                f"{what} {key!r} is produced by both "
                f"{result[key]['source']} and {entry['source']} — rename one"
            )
        result[key] = entry
    return result


# --- OWUI client ----------------------------------------------------------


class OWUI:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def _request(self, method: str, path: str, body: dict | None = None):
        url = f"{self.base_url}{path}"
        data = json.dumps(body).encode() if body is not None else None
        request = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise SyncError(f"{method} {path} -> HTTP {exc.code}: {detail[:500]}") from exc
        except urllib.error.URLError as exc:
            raise SyncError(f"{method} {path} -> network error: {exc.reason}") from exc
        return json.loads(raw) if raw else None

    def list_models(self) -> dict[str, dict]:
        return {model["id"]: model for model in self._request("GET", "/api/v1/models/all")}

    def list_prompts(self) -> dict[str, dict]:
        return {prompt["command"]: prompt for prompt in self._request("GET", "/api/v1/prompts/")}


# --- diffing --------------------------------------------------------------


def _meta(obj: dict) -> dict:
    return obj.get("meta") or {}


def _managed(obj: dict) -> bool:
    return _meta(obj).get("managed_by") == MANAGE_TAG


def _tags_as_names(value) -> list[str]:
    names = []
    for tag in value or []:
        if isinstance(tag, dict):
            names.append(tag.get("name"))
        else:
            names.append(tag)
    return names


def model_changed(current: dict, desired: dict) -> bool:
    if current.get("name") != desired["name"]:
        return True
    if current.get("base_model_id") != desired["base_model_id"]:
        return True
    if (current.get("params") or {}).get("system") != desired["params"]["system"]:
        return True
    current_meta, desired_meta = _meta(current), desired["meta"]
    if current_meta.get("description") != desired_meta["description"]:
        return True
    if _tags_as_names(current_meta.get("tags")) != _tags_as_names(desired_meta["tags"]):
        return True
    if sorted(current_meta.get("toolIds") or []) != sorted(desired_meta["toolIds"]):
        return True
    if sorted(current_meta.get("defaultFeatureIds") or []) != sorted(DEFAULT_FEATURE_IDS):
        return True
    return False


def prompt_changed(current: dict, desired: dict) -> bool:
    if current.get("name") != desired["name"]:
        return True
    if (current.get("content") or "") != desired["content"]:
        return True
    return not _managed(current)


# --- application ----------------------------------------------------------


def sync_models(client: OWUI, desired: dict[str, dict], *, dry_run: bool, prune: bool) -> None:
    current = client.list_models()
    for model_id, entry in desired.items():
        form = entry["form"]
        existing = current.get(model_id)
        if existing is None:
            print(f"  + create model {model_id}  ({entry['source']})")
            if not dry_run:
                client._request("POST", "/api/v1/models/create", form)
        elif _managed(existing) and not model_changed(existing, form):
            print(f"  = model {model_id} unchanged")
        else:
            verb = "update" if _managed(existing) else "ADOPT"
            print(f"  ~ {verb} model {model_id}  ({entry['source']})")
            if not dry_run:
                client._request("POST", "/api/v1/models/model/update", form)
    if not prune:
        return
    for model_id, existing in current.items():
        if _managed(existing) and model_id not in desired:
            print(f"  - delete model {model_id}  (removed from repo)")
            if not dry_run:
                client._request("POST", "/api/v1/models/model/delete", {"id": model_id})


def sync_prompts(client: OWUI, desired: dict[str, dict], *, dry_run: bool, prune: bool) -> None:
    current = client.list_prompts()
    for command, entry in desired.items():
        form = entry["form"]
        existing = current.get(command)
        if existing is None:
            print(f"  + create prompt /{command}  ({entry['source']})")
            if not dry_run:
                client._request("POST", "/api/v1/prompts/create", form)
        elif _managed(existing) and not prompt_changed(existing, form):
            print(f"  = prompt /{command} unchanged")
        else:
            verb = "update" if _managed(existing) else "ADOPT"
            print(f"  ~ {verb} prompt /{command}  ({entry['source']})")
            if not dry_run:
                client._request("POST", f"/api/v1/prompts/id/{existing['id']}/update", form)
    if not prune:
        return
    for command, existing in current.items():
        if _managed(existing) and command not in desired:
            print(f"  - delete prompt /{command}  (removed from repo)")
            if not dry_run:
                client._request("DELETE", f"/api/v1/prompts/id/{existing['id']}/delete")


# --- entry point ----------------------------------------------------------


def rebuild_dist() -> None:
    print("Rebuilding dist/ ...")
    result = subprocess.run(
        [sys.executable, str(ROOT / "build-prompts.py")],
        cwd=ROOT,
        check=False,
    )
    if result.returncode != 0:
        raise SyncError("build-prompts.py failed — fix the build before syncing")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Push this repo's prompts to an Open WebUI instance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would change without writing anything")
    parser.add_argument("--no-build", action="store_true",
                        help="do not rebuild dist/ before syncing")
    parser.add_argument("--no-prune", action="store_true",
                        help="never delete managed items (add/update only)")
    args = parser.parse_args(argv)

    base_url = os.environ.get("OWUI_URL", DEFAULT_OWUI_URL)
    api_key = os.environ.get("OWUI_API_KEY")
    if not api_key:
        print("error: OWUI_API_KEY is not set (admin API key for the instance)", file=sys.stderr)
        return 2

    try:
        if not args.no_build:
            rebuild_dist()
        desired_models = collect_models()
        desired_prompts = collect_prompts()
    except SyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    mode = "DRY RUN — no changes will be written" if args.dry_run else "applying"
    print(f"\nTarget: {base_url}  ({mode})")
    print(f"Desired: {len(desired_models)} models, {len(desired_prompts)} prompts\n")

    client = OWUI(base_url, api_key)
    try:
        print("Models:")
        sync_models(client, desired_models, dry_run=args.dry_run, prune=not args.no_prune)
        print("\nPrompts:")
        sync_prompts(client, desired_prompts, dry_run=args.dry_run, prune=not args.no_prune)
    except SyncError as exc:
        print(f"\nerror: {exc}", file=sys.stderr)
        return 1

    print("\nDone." + ("  (dry run — nothing written)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
