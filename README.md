# AI-prompts — shared prompts for ronzz.ORG

Home for the team's AI prompts, organised by user scenario — plus the organisation-wide **opencode** agent configuration, built from the same shared snippets.

## Layout

| Path | What it is | |---|---| | `src/fundamentals/` | Shared behaviour fragments + org policy (`org-context.md`, `credential-policy.md`, `forge-posture.md`, …). Define each rule here, once. Not standalone prompts. | | `src/fundamentals/coding/` | Software-development snippets (git, worktree, forge ops, testing, …) — reusable by any LLM code client, not just opencode. | | `src/<scenario>-prompts/` | Scenario prompts (`Help-Contributing.md`, system prompts, …). The files people actually work with. | | `src/system-prompt/` | **System prompts** for Open WebUI custom Models. Each file's YAML frontmatter declares the model (`name`, `description`, `tags`, `base_model`, `tool_ids`); the body is the system prompt. | | `src/opencode/` | **Sources for the opencode agent config**: `AGENTS.md`, `agents/copilot.md`, `opencode.jsonc`, plugins, proxy. Built (with the same `{{include:}}` mechanism) into `dist/opencode/`. | | `dist/` | **Generated** flat prompts (`*.prompt.md`) **and** the generated opencode config tree (`opencode/`). Never hand-edit — rebuilt with `build-prompts.py`. | | `build-prompts.py` | The build script (pure stdlib Python, no dependencies). | | `sync-owui.py` | Pushes `dist/` to Open WebUI — see [Open WebUI](#open-webui-llmronzzorg) below. | | `README.md` | This file. | | `AGENTS.md` | Repo conventions for agents/contributors working in this repo. |

## Writing prompts

All fundamental style directives, (e.g., "do not guess"), live as `md` snippets in `src/fundamentals/`. Those style directives can then be included in any prompt files via `{{include:}}`.

```markdown
{{include:do-not-guess}}        # expands into src/fundamentals/do-not-guess.md in dist/ on compile
{{include:wikibase/wikirules}}  # expands into src/fundamentals/wikibase/wikirules.md in dist/ on compile
```

> nested includes are allowed (`style.md` may itself include `do-not-guess.md`) > directives inside ```` ``` ```` fenced code blocks are **not** expanded > to show a *literal* `{{include:…}}` in a prompt (meta-prompts!), write > `{{!include:…}}` — the `!` escapes it

The opencode config tree (`src/opencode/`) uses the same directives: e.g. `src/opencode/AGENTS.md` includes `{{include:org-context}}`, so the organisation context is written once and reused by every prompt that needs it.

## Building

```bash
python3 build-prompts.py            # rebuild all prompts into dist/
python3 build-prompts.py --check    # exit 1 if dist/ is stale (CI / pre-commit)
python3 build-prompts.py -f some-prompt.md    # rebuild only matching source files
```

After editing any source `.md` file, **rebuild** so `dist/` reflects the change. Every generated prompt carries a header saying so; `--check` is the enforcement tool (wire it into a `pre-commit` hook or GitHub Action if this folder becomes a git repo).

The build **auto-formats** markdown before expansion, so contributors don't have to: trailing whitespace is stripped, blank-line runs collapse to a single blank line, and (in prompt files) list nesting is normalized to 2-space steps while stray indentation on plain paragraphs is dedented. Fenced code blocks, blockquotes and YAML frontmatter are preserved; `src/opencode/` markdown keeps its indentation byte-for-byte (frontmatter and minified lines there are semantically meaningful).

The opencode config tree (`dist/opencode/`) is generated too, but carries **no** generated header (agent files must start with their frontmatter, and `AGENTS.md` feeds the model's system prompt). The files keep their exact names so they can be symlinked directly.

## Consumption

The expanded flat text prompts in `dist/` can be copy&pasted everywhere!

### opencode (recommended desktop coding client)

`dist/opencode/` IS a complete opencode config directory (`AGENTS.md`, `agents/`, `opencode.jsonc`, `plugins/`). Link your global config to it — every `git pull` of this repo updates your agent config:

```bash
# one-time setup — everyone at ronzz.ORG is on Linux
git clone https://forgejo.ronzz.org/ronzz-org/ronzz-LLM-prompt-hub.git ~/ronzz-LLM-prompt-hub
ln -s ~/ronzz-LLM-prompt-hub/dist/opencode ~/.config/opencode

# per-user bits (gitignored, never committed):
mkdir -p ~/.config/opencode/.secrets
#   brave-api-key        — Brave Search API key (mcp-daemon plugin reads it)
#   context7-api-key     — Context7 API key (context7-mcp-proxy.mjs reads it)

# plugin dependencies (only if you use the worktree/notify plugins):
cd ~/.config/opencode && npm install   # creates node_modules/, gitignored

# mediawiki MCP credentials (SeedBot@MCP bot password):
mkdir -p ~/.config/mediawiki-mcp
#   ~/.config/mediawiki-mcp/ronzz-wikibase.json — see RonzzIT:Runbook/WikiWriterMCP
```

Personal overrides (providers, your own MCP servers, model choices) go in a project-level `.opencode/opencode.jsonc`, which opencode merges over the global config. Secrets never belong in this repo — see `src/fundamentals/credential-policy.md`.

### Open WebUI (llm.ronzz.org)

`sync-owui.py` pushes `dist/` to the ronzz.ORG Open WebUI instance ("Veramiko",
`llm.ronzz.org`). The mapping is by location under `dist/`:

| Source | Open WebUI |
| --- | --- |
| `dist/system-prompt/*.prompt.md` (i.e. `src/system-prompt/`) | a custom **Model**; its YAML frontmatter sets `name`, `description`, `tags`, `base_model`, `tool_ids`, and the body becomes the system prompt (code interpreter + web search enabled by default) |
| every other `dist/**/*.prompt.md` | a **Prompt** — the `/slash` command inserted into the chat composer |

```bash
OWUI_API_KEY=sk-… python3 sync-owui.py --dry-run   # preview the changes
OWUI_API_KEY=sk-… python3 sync-owui.py             # rebuild dist/ and apply
```

Every item the sync writes is tagged `meta.managed_by = "ronzz-LLM-prompt-hub"`.
Managed items are updated in place, and **hard-deleted** when their source is
removed from the repo. Hand-made items are never deleted; an item whose
id/command collides with a repo item is *adopted* (updated and tagged), never
duplicated. `--no-prune` (add/update only) and `--no-build` are also available.

`OWUI_API_KEY` is an **admin** API key — enable it once at *Admin → Settings →
Authentication → Enable API Keys*, then copy the key from *Account → API Keys*.
It is a secret: never commit it (see `src/fundamentals/credential-policy.md`).

**Automation.** The repo is push-mirrored to
`github.com/Ron-RONZZ-org/ronzz-LLM-prompt-hub`; `.github/workflows/sync-owui.yml`
runs the sync on every push to `main` (using the repository secret
`OWUI_API_KEY`). Pushing to Forgejo therefore updates the instance within a
minute. The workflow **rebuilds `dist/` from `src/` first**, so a commit that
forgot to run `build-prompts.py` still publishes the right content — it only
emits a warning, since the committed `dist/` (which `dist/opencode/` consumers
symlink) would have drifted.

## Contributor conventions

- NEVER edit `dist/`; edit the source, then rebuild
- NEVER copy-paste a rule from `src/fundamentals/` into a scenario file — `{{include:}} it
- keep `src/fundamentals/` entries generic; no scenario-specific claims
- don't put credentials in prompts — reference their storage location instead
- when changing the opencode tree (`src/opencode/`), rebuild and verify:   `python3 build-prompts.py --check`

## Prompt hub: adding prompts and models {#prompt_hub_adding_prompts_and_models}

## Veramiko auto-sync

This repository is synced by CI on its Github mirror to Veramiko as custom Models and slash-command prompts.

Deployment facts:

[RonzzIT:Deployment/OpenWebUI](https://wikibase.ronzz.org/wiki/RonzzIT:Deployment/OpenWebUI#Prompt_hub_sync_(ronzz-LLM-prompt-hub))

### Where to put a prompt {#where_to_put_a_prompt}

Work in the repo\'s `src/` tree. `build-prompts.py` expands
`{{include:…}}` directives into `dist/`, and the sync publishes `dist/`:

  Location                   Becomes in Open WebUI
  -------------------------- ----------------------------------------------------------------
  `src/system-prompt/*.md`   a custom **Model** (system prompt + metadata)
  any other `src/**/*.md`    a **Prompt** --- a `/slash` command
  `src/fundamentals/**`      nothing --- reusable fragments, pulled in with `{{include:…}}`
  `src/opencode/**`          nothing --- the opencode config tree

The model id / prompt command is the **file name**, lower-cased with
runs of non-alphanumerics turned into `-`:
`src/oneliners/writing/proofread.md` → `/proofread`;
`src/system-prompt/veramiko-science.md` → model `veramiko-science`.
Commands are flat (a nested file still yields a flat command) and must
be unique across the repo --- the sync fails loudly on a collision.

### Slash-command prompts {#slash_command_prompts}

Plain markdown. The text is what gets inserted when a user types
`/name`. Open WebUI\'s own `{{variable}}` placeholders are supported
(the user fills them in).

``` markdown
## TASK

Proofread the article. Preserve the author's language and writing style.

## Article

{{article}}
```

### System prompts → custom Models {#system_prompts_custom_models}

A file under `src/system-prompt/` becomes a custom Model: the body
(after the frontmatter) is its system prompt, and the YAML frontmatter
declares the metadata.

  Frontmatter key       Default                 Meaning
  --------------------- ----------------------- -----------------------------------------------------------------------------------------------
  `name`                the file name           display name in the model picker
  `description`         none                    one-line description shown under the name
  `tags`                `[]`                    list, e.g. `[Science, Research]` --- groups the model in the picker
  `base_model`          `deepseek-flash`        the upstream model the custom model wraps
  `tool_ids`            `[]`                    MCP tool servers to attach, e.g. `[server:mcp:mediawiki-mcp]` (the ids shown in the Admin UI)
  `profile_image_url`   `/static/favicon.png`   avatar

Every generated model has the **code interpreter** and **web search**
switched on by default. The frontmatter is metadata only --- it is
stripped from the system prompt; unknown keys are ignored.

Example --- `src/system-prompt/veramiko-science.md`:

``` markdown
---
name: Veramiko Science
description: Scientific research assistant — literature review, analysis, drafting, and citation.
tags: [Science, Research]
base_model: deepseek-flash
---

You are "Veramiko", a scientific research assistant.
```

### Publish

After editing the repo:

``` bash
python3 build-prompts.py            # rebuild dist/
python3 build-prompts.py --check    # exit 0 = dist/ consistent with src/
git add -A && git commit -m "feat: …" && git push
```

CI rebuilds `dist/` itself, so a forgotten build only raises a warning
--- it does not block publication. The instance is updated within \~2
minutes of the push. **Delete** a prompt by deleting its source file;
the next sync removes it. **Preview** the changes first with:

``` bash
OWUI_API_KEY=$(cat .secrets/owui-api-key) python3 sync-owui.py --dry-run
```

**Do not** create a prompt or model by hand in the Admin UI: the sync
only manages what it published (items tagged `meta.managed_by`), so a
hand-made item is never updated or removed --- and if its name matches a
repo item, the sync adopts (overwrites) it.
