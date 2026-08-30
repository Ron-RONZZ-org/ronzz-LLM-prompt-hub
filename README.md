# AI-prompts — shared prompts for ronzz.ORG

Home for the team's AI prompts, organised by user scenario — plus the organisation-wide **opencode** agent configuration, built from the same shared snippets.

## Layout

| Path | What it is | |---|---| | `src/fundamentals/` | Shared behaviour fragments + org policy (`org-context.md`, `credential-policy.md`, `forge-posture.md`, …). Define each rule here, once. Not standalone prompts. | | `src/fundamentals/coding/` | Software-development snippets (git, worktree, forge ops, testing, …) — reusable by any LLM code client, not just opencode. | | `src/<scenario>-prompts/` | Scenario prompts (`Help-Contributing.md`, system prompts, …). The files people actually work with. | | `src/opencode/` | **Sources for the opencode agent config**: `AGENTS.md`, `agents/copilot.md`, `opencode.jsonc`, plugins, proxy. Built (with the same `{{include:}}` mechanism) into `dist/opencode/`. | | `dist/` | **Generated** flat prompts (`*.prompt.md`) **and** the generated opencode config tree (`opencode/`). Never hand-edit — rebuilt with `build-prompts.py`. | | `build-prompts.py` | The build script (pure stdlib Python, no dependencies). | | `README.md` | This file. | | `AGENTS.md` | Repo conventions for agents/contributors working in this repo. |

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

### Open WebUI (llm.ronzz.org) — open question

Whether the same snippet-based approach can power an Open WebUI prompt/model collection is **not yet decided**. Open WebUI has no include mechanism and prompts are attached per-chat/model, so the design space differs from the opencode config tree. Tracked as a future extension of this repo; contributions welcome.

## Contributor conventions

- NEVER edit `dist/`; edit the source, then rebuild
- NEVER copy-paste a rule from `src/fundamentals/` into a scenario file — `{{include:}} it
- keep `src/fundamentals/` entries generic; no scenario-specific claims
- don't put credentials in prompts — reference their storage location instead
- when changing the opencode tree (`src/opencode/`), rebuild and verify:   `python3 build-prompts.py --check`
