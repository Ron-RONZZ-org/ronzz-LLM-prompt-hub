After any structural or UI change, update the relevant documentation to match the current state. Do not defer this — stale docs are worse than no docs.

**What counts as a structural/UI change:**
- New or renamed commands, subcommands, or command paths
- New or renamed modules, packages, or files
- Changed file layout or directory structure
- New or modified UI components, routes, or interactive behavior
- Changed configuration options, environment variables, or CLI flags
- Changed API endpoints, parameters, or return shapes

**What to update:**

| Documentation | When | |---|---| | Project `README.md` | New feature, changed workflow, different install steps | | Module `AGENTS.md` (each module) | Module structure, interface, or behavior changed | | Root `AGENTS.md` | Project-wide conventions, architecture, or module list changed | | Command description (`commands/*.md`) | Command behavior, flags, or arguments changed | | Help text / `--help` output | CLI flags or subcommands changed | | In-code docstrings / JSDoc | Function signatures, return types, or behavior changed |

**Workflow:**
1. **Before implementing**, note which docs may need updates (grep for mentions of the code you're changing)
2. **After implementing**, update all affected documentation in the same commit (or same batch of commits). If the change is large enough to warrant separate doc commits, that's fine — but docs must be committed before the branch is complete.
3. **Verify** — run `rg` to check for stale references to old names, paths, or patterns. A mention of a deleted command or renamed module is a bug.

For ronzz.ORG internal documentation, follow:
- {{include:writing/RonzzWikiBase/writing-style-guide}}
- {{include:ronzzIT-convention}}
