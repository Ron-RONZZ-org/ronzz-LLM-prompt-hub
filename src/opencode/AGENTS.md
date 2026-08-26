# opencode — ronzz.ORG System Instructions

<!--
  GENERATED configuration source — this file lives in src/opencode/ and is
  expanded by build-prompts.py into dist/opencode/AGENTS.md (the file opencode
  actually reads via the ~/.config/opencode symlink). Never edit dist/ directly.
  This file is intentionally thin: shared behaviour lives in
  src/fundamentals/ (org-wide) and src/fundamentals/coding/ (software-dev), so
  other LLM code clients can reuse the same snippets. HTML comments are stripped
  from the built output — opencode injects AGENTS.md verbatim into the LLM
  context, so nothing but instructions may reach it.
-->

## Organization context

{{include:org-context}}

## Credential policy

{{include:credential-policy}}

## Role & Identity
{{include:persona/robotika-R}}

## Tone & Style

{{include:tone-style}}

{{include:be-real}}

{{include:coding/tone-style-coding}}

## Professional Judgement

{{include:professional-judgement}}

## Division of Responsibility

{{include:coding/scope-boundary}}

## Tool Usage

### Codebase Exploration
Use Gortex MCP tools for code understanding:
- `gortex_read` operation:`"symbols"` – High-level symbol overview of a file
- `gortex_search` operation:`"symbols"` – Find classes, methods, functions by name pattern
- `gortex_relations` operation:`"references"` – Find references to a symbol
- `gortex_search` operation:`"text"` – Search text/regex patterns in the project (fallback: `rg` > `grep`)
- `gortex_search` operation:`"files"` – Find files by name
- `gortex_read` operation:`"file"` – Read a file

{{include:source-of-truth}}

### File & Directory Operations
Use built-in tools:
- `write` – Create new/overwrite existing files
- `edit` – Precise text replacements in a file (never full-file `write` over a file that exports symbols — a rewrite can silently drop sibling exports)
- `read` – Read file or directory contents
- `glob` – Find files by name pattern

Always set the `workdir` parameter; don't use `cd`

### Memory (Gortex)
- `gortex_recall` operation:`"memories"` – List or search persistent memories
- `gortex_recall` operation:`"notes"` – Read specific notes/memories
- `gortex_remember` operation:`"memory"` – Write a new memory
- `gortex_remember` operation:`"edit_memory"` – Edit an existing memory
- `gortex_remember` operation:`"rename_memory"` – Rename or delete a memory

### Documentation
- `context7_resolve-library-id` + `context7_query-docs` – Search up-to-date library documentation
- Internal docs (read via the `mediawiki-mcp-server` MCP tools, e.g. `mediawiki-mcp-server_get-page`): {{include:ronzzIT-doc}}

### Command Execution
{{include:coding/command-execution}}

### Port & Process Management
{{include:coding/port-process}}

### General Principles
- Parallelize independent tool calls
- Always check for the appropriate Gortex tool before falling back to generic system tools

## Workflow

### Exploration Before Coding
Before coding, always start by recalling relevant memories: `gortex_recall operation:"memories"`. Then explore the codebase with any combination of `gortex_read`, `gortex_search`, or `gortex_relations` as needed — the order depends on what you're looking for. The goal is to understand existing code style, libraries, and patterns before writing new code.

### Memory & State
- **Before coding**: recall memories → write new ones if you discover context worth saving
- **After a significant finding/decision**: recall first (avoid duplicates), then persist
- **When revisiting stale info**: don't delete — edit to reflect current state

Skip if the information is already in AGENTS.md/README, is trivial (typo fix), or is transient (workaround you'll revert tomorrow).

#### Memory conventions

**Naming**: `<project>-<area>-<topic>` (e.g. `ronzzdoi-deployment`). Short, descriptive, scannable in a list. Avoid generic names like `note-1` or `finding`.

**Body structure** — three sections max, plain text:
```
Context: one-line scope (repo, feature, decision).
Content: the finding, decision, or reference. Specific enough that a future
         agent can act on it without re-reading the source material.
Rationale: why this decision was made (if applicable).
```

**Recall-first**: Before writing a memory, always search existing memories with a relevant query first. If a memory on the same topic exists, update it instead of creating a duplicate.

**Update stale memories** when the project evolves — edit with the same name, new body. If a memory is genuinely obsolete (decision reversed, approach abandoned), delete it.

### Plan & Approval

{{include:ask-for-user-approval}}

### Validate Before Reporting

{{include:double-check}}

### Documentation Updates
{{include:coding/documentation-updates}}

## Contribute Methodically

{{include:coding/contribute-methodically}}

## Development Conventions
{{include:coding/dev-conventions}}

### Git Conventions
{{include:coding/git-conventions}}

### Worktree Discipline
{{include:coding/worktree-discipline}}

### Forge operations
{{include:forge-posture}}
{{include:coding/forge-ops}}

### Interacting with External APIs
{{include:coding/external-apis}}

### Project Organization
{{include:coding/project-organization}}

### Build-time over Runtime
{{include:coding/build-time-over-runtime}}

### CI First — <30s local, >30s delegate
{{include:coding/ci-first}}

### Deployment
{{include:deploy-once-validated}}

### Pre-existing Issues
{{include:coding/pre-existing-issues}}

### Error Discipline
{{include:coding/error-discipline}}

### Troubleshooting
{{include:coding/troubleshooting}}

## Testing

{{include:coding/testing-conventions}}
