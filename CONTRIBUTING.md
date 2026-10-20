# Contributing to the ronzz.ORG prompt library

Technical guide for adding, editing, building, and publishing prompts.

Just want to *use* the prompts? See **[USERGUIDE.md](USERGUIDE.md)** instead.

## Repository layout

| Path | Content |
| --- | --- |
| `src/fundamentals/` | Shared behaviour fragments + org policy (`org-context.md`, `credential-policy.md`, `forge-posture.md`, …). Define each rule here, once. Not standalone prompts. |
| `src/fundamentals/coding/` | Software-development snippets (git, worktree, forge ops, testing, …) — reusable by any LLM code client, not just opencode. |
| `src/<scenario>-prompts/` | Scenario prompts (`Help-Contributing.md`, system prompts, …). The files people actually work with. |
| `src/system-prompt/` | **System prompts** for Open WebUI custom Models. Each file's YAML frontmatter declares the model (`name`, `description`, `tags`, `base_model`, `tool_ids`); the body is the system prompt. |
| `src/opencode/` | **Sources for the opencode agent config**: `AGENTS.md`, `agents/copilot.md`, `opencode.jsonc`, plugins, proxy. Built (with the same `{{include:}}` mechanism) into `dist/opencode/`. |
| `dist/` | **Generated** flat prompts (`*.prompt.md`) **and** the generated opencode config tree (`opencode/`). Never hand-edit — rebuilt with `build-prompts.py`. |
| `build-prompts.py` | The build script (pure stdlib Python, no dependencies). |
| `sync-owui.py` | Pushes `dist/` to Open WebUI — see [Publishing](#publishing-open-webui) below. |
| `AGENTS.md` | Repo conventions for agents/contributors. |

`src/fundamentals/` is **not** published on its own: fragments exist only to be
pulled into prompt files with `{{include:}}`.

## Writing prompts

### Shared snippets and `{{include:}}`

All fundamental style directives (e.g. "do not guess") live as `md` snippets in
`src/fundamentals/`. Include them in any prompt file:

```markdown
{{include:do-not-guess}}        # expands into src/fundamentals/do-not-guess.md in dist/ on compile
{{include:wikibase/wikirules}}  # expands into src/fundamentals/wikibase/wikirules.md in dist/ on compile
```

- Include paths are relative to `src/fundamentals/`; the `.md` extension is added
  automatically.
- Nested includes are allowed (`style.md` may itself include `do-not-guess.md`).
- Directives inside fenced code blocks are **not** expanded.
- To show a *literal* `{{include:…}}` in a prompt (meta-prompts!), write
  `{{!include:…}}` — the `!` escapes it.
- **Never copy-paste a rule out of `src/fundamentals/` into a scenario file.**
  Include it, so the rule has a single source of truth instead of a million orphaned duplicates.

### System prompts → Open WebUI Models

A file under `src/system-prompt/` becomes a custom **Model** on
`llm.ronzz.org`. Its YAML frontmatter must be a **flat subset** —
`key: value` or `key: [a, b]`, nothing nested — because `sync-owui.py` parses it
with a minimal reader, not a full YAML engine:

```yaml
---
name: Veramiko Science
description: Scientific research assistant — literature review, analysis, drafting, and citation.
tags: [Science, Research]
base_model: deepseek-flash
tool_ids: [server:mcp:mediawiki-mcp]
---
```

| Key | Effect |
| --- | --- |
| `name` | Display name of the model in Open WebUI. |
| `description` | Model description shown in the model picker. |
| `tags` | List; shown as model tags. |
| `base_model` | Underlying model (default `deepseek-flash`). |
| `tool_ids` | MCP/tool servers the model may call. |
| `profile_image_url` | Avatar (defaults to the instance favicon). |

The rest of the file (after the frontmatter) becomes the model's system prompt.
Code interpreter and web search are switched on by default.

### Filenames become slash commands

Every other `dist/**/*.prompt.md` becomes an Open WebUI **slash-command
Prompt**. The command is the **slugified filename stem**: lowercased, with every
run of non-alphanumeric characters collapsed to `-`. For example,
`I-will-sudo.prompt.md` → `/i-will-sudo`.

- Keep filenames descriptive and unique — two files with the same basename (in
  different folders) produce the same command, and the sync **fails loudly** on
  a collision, so rename one.
- The same slug rule derives the **model id** for system prompts.

### Placeholders

Prompts can carry fill-in markers such as `{{article}}` or `{{article_topic}}`. They
are passed through by `build-prompts.py` as literal text for the user/end-client to replace.

See the [official OpenWeb UI guide](https://docs.openwebui.com/features/workspace/prompts/#variables) for usage.

> `{{article topic}}` does not work. No spaces allowed in variables (upstream Open WebUI constraint).

## Building

```bash
python3 build-prompts.py            # rebuild all prompts into dist/ (never deletes)
python3 build-prompts.py --check    # exit 1 if dist/ is stale (CI / pre-commit)
python3 build-prompts.py --prune    # also delete dist/ files whose source is gone
python3 build-prompts.py --self-test  # verify the pruning policy
python3 build-prompts.py -f some-prompt.md    # rebuild only matching source files
```

After editing any source `.md` file, **rebuild** so `dist/` reflects the change.
Every generated prompt carries a header saying so; `--check` is the enforcement
tool.

A plain build **never deletes** anything: files in `dist/` with no matching
source are reported as a warning and left in place; pass `--prune` to remove
them. `dist/opencode/` is a live config directory once symlinked as
`~/.config/opencode` — `node_modules/`, `.secrets/` and package lockfiles live
there and are never treated as build output. `--self-test` asserts that
invariant (run it after touching the pruner).

The build **auto-formats** markdown before expansion, so contributors don't have
to: trailing whitespace is stripped, blank-line runs collapse to a single blank
line, and (in prompt files) list nesting is normalized to 2-space steps while
stray indentation on plain paragraphs is dedented. Fenced code blocks,
blockquotes and YAML frontmatter are preserved; `src/opencode/` markdown keeps
its indentation byte-for-byte (frontmatter and minified lines there are
semantically meaningful).

HTML comments (`<!-- … -->`) in any source file are for contributors only — they
are stripped before expansion and never reach `dist/`.

The opencode config tree (`dist/opencode/`) is generated too, but carries **no**
generated header (agent files must start with their frontmatter, and `AGENTS.md`
feeds the model's system prompt). The files keep their exact names so they can be
symlinked directly.

## Publishing

### Open WebUI (`llm.ronzz.org`) {#publishing-open-webui}

`sync-owui.py` pushes `dist/` to the ronzz.ORG Open WebUI instance ("Veramiko",
`llm.ronzz.org`). The mapping is by location under `dist/`:

| Source | Open WebUI |
| --- | --- |
| `dist/system-prompt/*.prompt.md` (i.e. `src/system-prompt/`) | a custom **Model** (frontmatter sets metadata; body is the system prompt) |
| every other `dist/**/*.prompt.md` | a **Prompt** — the `/slash` command inserted into the chat composer |

```bash
OWUI_API_KEY=sk-… python3 sync-owui.py --dry-run   # preview the changes
OWUI_API_KEY=sk-… python3 sync-owui.py             # rebuild dist/ and apply

# the admin key is kept locally and gitignored:
OWUI_API_KEY=$(cat .secrets/owui-api-key) python3 sync-owui.py --dry-run
```

Deployment reference: [RonzzIT:Deployment/OpenWebUI → Prompt hub sync](https://wikibase.ronzz.org/wiki/RonzzIT:Deployment/OpenWebUI#Prompt_hub_sync_(ronzz-LLM-prompt-hub)).

Every item the sync writes is tagged `meta.managed_by = "ronzz-LLM-prompt-hub"`.
Managed items are updated in place, and **hard-deleted** when their source is
removed — so **delete a prompt by deleting its source file**. Hand-made items
are never deleted; an item whose id/command collides with a repo item is
*adopted* (updated and tagged), never duplicated. `--no-prune` (add/update only)
and `--no-build` are also available.

**Do not create prompts or models by hand in the Admin UI** — the sync only
manages what it published, so a hand-made item is never updated or removed.

`OWUI_API_KEY` is an **admin** API key — enable it once at *Admin → Settings →
Authentication → Enable API Keys*, then copy the key from *Account → API Keys*.
It is a secret: never commit it (see `src/fundamentals/credential-policy.md`).

#### CI constraints — `.github/workflows/sync-owui.yml`

The repo is push-mirrored to `github.com/Ron-RONZZ-org/ronzz-LLM-prompt-hub`.
On every push to `main` the workflow:

1. warns (non-fatally) if the committed `dist/` is stale,
2. **rebuilds `dist/` from `src/`** — a commit that forgot to run
   `build-prompts.py` still publishes the right content,
3. runs the sync against `llm.ronzz.org` using the repository secret
   `OWUI_API_KEY`.

Pushing to Forgejo therefore updates the instance within ~2 minutes. What this
means when you write a prompt:

- **Frontmatter must stay flat** — the sync parses it with a minimal reader, so
  nested YAML breaks the run.
- **Command/model ids are derived from filenames** and must be unique across the
  whole `dist/` prompt tree.
- The **committed `dist/`** still matters: `dist/opencode/` consumers symlink it,
  so run the build and commit the result even though CI rebuilds anyway.

### Prompt store website (GitHub Pages)

`dist/` is also rendered into a browsable, searchable **prompt store** and
published to GitHub Pages from the push mirror:
<https://prompts.ronzz.org/>.

- **Generator** — `site/` is an [Astro](https://astro.build) project.
  `site/scripts/prepare-content.mjs` reads `dist/**/*.prompt.md` (plus
  `USERGUIDE.md` and `CONTRIBUTING.md`), strips the generated header and YAML
  frontmatter — the same normalisation `sync-owui.py` applies — and emits
  `site/src/data/*.json` plus a client-side `search-index.json`. Astro then
  renders the home page (title, search box, tiles), `/userguide`,
  `/contributing`, `/themes` (a tree of every prompt), and one page per prompt
  (`/prompts/<path>`) with the prompt shown in a bordered box, a
  **Rendered/Source** toggle, and a **Copy** button that yields exactly the text
  Open WebUI receives. A search box also sits in the site header on every page
  (the home page keeps its larger hero search), and `/themes` adds an inline
  filter box.
- **Deployment** — `.github/workflows/pages.yml` rebuilds `dist/`, runs
  `npm ci && npm run build` inside `site/`, and deploys `_site/` with
  `actions/deploy-pages`. The repository must have Pages set to build from
  **GitHub Actions** (Settings → Pages → Source).
- **Local preview** — requires Node 24.18.0 (pinned in `.nvmrc`; npm refuses
  other versions via `engine-strict`):
  ```bash
  nvm use                               # reads .nvmrc
  cd site && npm ci && npm run build    # writes ../_site
  cd site && npm run dev                # dev server, live reload
  ```
- **Domain** — served at <https://prompts.ronzz.org>. `site` and `base` are set
  in `site/astro.config.mjs`, the domain is declared in `site/public/CNAME`, and
  the same domain must be set in the repo's Pages settings. DNS is a Cloudflare
  `CNAME` for `prompts` → `ron-ronzz-org.github.io` (grey cloud, so GitHub can
  issue its own TLS certificate) — see `RonzzIT:Runbook/Cloudflare`.

## Contributor conventions

- NEVER edit `dist/`; edit the source, then rebuild.
- NEVER copy-paste a rule from `src/fundamentals/` into a scenario file —
  `{{include:}}` it.
- Keep `src/fundamentals/` entries generic; no scenario-specific claims.
- Don't put credentials in prompts — reference their storage location instead.
- When changing the opencode tree (`src/opencode/`), rebuild and verify:
  `python3 build-prompts.py --check`.
- Run `python3 build-prompts.py --check` before you commit.

## Checklist — adding a new prompt

1. Create `src/<scenario>-prompts/<Descriptive-Name>.md` (a unique filename
   becomes a unique slash command).
2. Reuse shared rules with `{{include:…}}` instead of copying them.
3. For a system prompt, put it under `src/system-prompt/` with flat frontmatter.
4. Run `python3 build-prompts.py` and commit the rebuilt `dist/`.
5. Verify: `python3 build-prompts.py --check`.
6. Push to Forgejo `main`; the mirror CI publishes it to Open WebUI and the
   prompt store.
