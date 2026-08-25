# AI-prompts — shared prompts for ronzz.ORG

Home for the team's AI prompts, organised by user scenario. 

## Layout

| Path | What it is |
|---|---|
| `src/fundamentals/` | Shared behaviour fragments (`do-not-guess.md`, `verify-before-claiming.md`, …). Define each rule here, once. Not standalone prompts. |
| `src/<scenario>-prompts/` | Scenario prompts (`Help-Contributing.md`, system prompts, …). The files people actually work with. |
| `dist/` | **Generated** flat prompts (`*.prompt.md`). Never hand-edit — rebuilt with `build-prompts.py`. |
| `build-prompts.py` | The build script (pure stdlib Python, no dependencies). |
| `README.md` | This file. |

## Writing prompts

All fundamental style directives, (e.g., "do not guess"), live as `md` snippets in `src/fundamentals/`. Those style directives can then be included in any prompt files via `{{include:}}`.

```markdown
{{include:do-not-guess}}        # expands into src/fundamentals/do-not-guess.md in dist/ on compile
{{include:wikibase/wikirules}}  # expands into src/fundamentals/wikibase/wikirules.md in dist/ on compile
```

> nested includes are allowed (`style.md` may itself include `do-not-guess.md`)
> directives inside ```` ``` ```` fenced code blocks are **not** expanded
> to show a *literal* `{{include:…}}` in a prompt (meta-prompts!), write
  `{{!include:…}}` — the `!` escapes it

## Building

```bash
python3 build-prompts.py            # rebuild all prompts into dist/
python3 build-prompts.py --check    # exit 1 if dist/ is stale (CI / pre-commit)
python3 build-prompts.py -f some-prompt.md    # rebuild only matching source files
```

After editing any source `.md` file, **rebuild** so `dist/` reflects the change.
Every generated file carries a header saying so; `--check` is the enforcement
tool (wire it into a `pre-commit` hook or GitHub Action if this folder becomes
a git repo).

## Consumption

The expanded flat text prompts in `dist/` can be copy&pasted everywhere!

## Contributor conventions

- NEVER edit `dist/`; edit the source, then rebuild
- NEVER copy-paste a rule from `src/fundamentals/` into a scenario file — `{{include:}} it
- keep `src/fundamentals/` entries generic; no scenario-specific claims
- don't put credentials in prompts — reference their storage location instead
