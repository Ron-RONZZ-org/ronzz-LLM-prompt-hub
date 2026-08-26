Follow the client's conventions (exploration, memory, testing). In addition:

- WHILE coding
  - do not reinvent the wheel, use `import`.
  - external libraries: choose carefully
    - must: FOSS, clearly documented, actively maintained
    - preferred: efficient, lightweight
  - readability is key
    - each function must be sensibly named, do one simple thing, be comprehensible without extensive comments
  - **if you spot unrelated pre-existing issues (efficiency, security concern, bug)**
    - fix them if code intent is clear and risk is low
    - if risk is high/complex: if your task is not impacted, continue and inform user when finished; if impacted, STOP and inform user
  - do not take shortcuts
    - implement long-term stable options
    - code should always raise errors requiring user attention with specific error type and clear error message
    - silent swallow/generic errors forbidden
    - define custom error classes in one centralised location (see Error Discipline)
  - **For cross-cutting changes touching 20+ files, prefer scripted refactors over manual edits.** Use `rg` to identify all affected locations, read the exact lines, then apply changes consistently. For mechanical changes (renames, import path updates, env var removals), consider a codemod to avoid whitespace mismatches and inconsistent application.
  - **Check the tool's own CLI before designing abstractions.** Run `tool --help` and `tool subcommand --help` early. The fastest documentation is often in the terminal — and may reveal primitives that eliminate entire layers of complexity before you build them.
  - **For third-party software that misbehaves, read the official documentation before the first iteration.** When a component doesn't behave as expected, locate and read its official docs (project site, README, `--help`, its issue tracker) *before* changing anything — not after failed attempts. Only then iterate; if the docs don't cover the case, escalate to the source.

- AFTER implementation
  - if TEST FAILED, REPAIR CODE, NOT SKIP TEST
    - if the problem is in the repo, pre-existing or not, fix it
    - if the problem is elsewhere (external library), ASK user how to proceed
