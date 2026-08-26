# ronzz-LLM-prompt-hub — repo conventions

This repo is the shared prompt hub for ronzz.ORG. It holds two kinds of content:

- **Prompt sources** (`src/<scenario>-prompts/`, `src/personas/`, `src/oneliners/`, …) — expanded by `build-prompts.py` into flat, copy-paste-ready prompts in `dist/*.prompt.md`.
- **The opencode config tree** (`src/opencode/`) — expanded into `dist/opencode/`, which users symlink as `~/.config/opencode`. `dist/opencode/AGENTS.md` is the org-wide system instruction for coding agents.

## Working in this repo

- **Organization context & policy**: `src/fundamentals/org-context.md`, `src/fundamentals/credential-policy.md`, `src/fundamentals/gh-over-forge.md` — extend these, never duplicate their content into a prompt.
- **NEVER edit `dist/`** — edit the source under `src/`, then rebuild: `python3 build-prompts.py`.
- After any change, run `python3 build-prompts.py --check` to confirm `dist/` is consistent.
- Follow the conventions in `README.md` (contributor conventions section).

See `https://wikibase.ronzz.org/wiki/RonzzIT:Main` for ronzz.ORG IT docs.
