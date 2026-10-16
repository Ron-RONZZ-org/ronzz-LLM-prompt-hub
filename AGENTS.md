# ronzz-LLM-prompt-hub — repo conventions

This repo is the shared prompt hub for ronzz.ORG. It holds two kinds of content:

- **Prompt sources** (`src/<scenario>-prompts/`, `src/system-prompt/`, `src/oneliners/`, …) — expanded by `build-prompts.py` into flat, copy-paste-ready prompts in `dist/*.prompt.md`.
- **The opencode config tree** (`src/opencode/`) — expanded into `dist/opencode/`, which users symlink as `~/.config/opencode`. `dist/opencode/AGENTS.md` is the org-wide system instruction for coding agents.
- **Open WebUI models** (`src/system-prompt/`) — each file becomes a custom Model on `llm.ronzz.org`; its YAML frontmatter declares the model, the body is the system prompt. Pushed by `sync-owui.py` (see `CONTRIBUTING.md`).
- **Prompt store website** (`site/`) — an Astro site that renders `dist/` into a searchable browsable store, deployed to GitHub Pages by `.github/workflows/pages.yml`. Docs in `CONTRIBUTING.md`; end users should read `USERGUIDE.md`.

## Working in this repo

- **Organization context & policy**: `src/fundamentals/org-context.md`, `src/fundamentals/credential-policy.md`, `src/fundamentals/forge-posture.md` — extend these, never duplicate their content into a prompt.
- **Software-dev conventions**: `src/fundamentals/coding/` (git, worktree, forge ops, testing, …) — shared by any LLM code client; keep them client-agnostic.
- **NEVER edit `dist/`** — edit the source under `src/`, then rebuild: `python3 build-prompts.py`.
- After any change, run `python3 build-prompts.py --check` to confirm `dist/` is consistent.
- **NEVER edit generated site output** — `_site/`, `site/src/data/`, `site/public/search-index.json` are build artifacts; the source is `dist/` + the root markdown docs + `site/src/`.
- Follow the conventions in `CONTRIBUTING.md` (contributor conventions section).

See `https://wikibase.ronzz.org/wiki/RonzzIT:Main` for ronzz.ORG IT docs.
