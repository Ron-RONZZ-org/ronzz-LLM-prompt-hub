Before running any test suite that takes >30s locally, check if the repo's GitHub mirror has CI:

```bash
gh workflow list
```

- If a CI workflow covers your scope, trigger it and wait for results.
- Only run locally what CI cannot: rapid iteration during development (<30s), single-file unit tests, interactive debugging.

### Test Coverage Requirements
Every feature or fix that touches BOTH the backend and frontend MUST have tests at ALL applicable layers:

| Layer | Tool | Scope | When required | |-------|------|-------|---------------| | **Backend unit tests** | `pytest` | Handler logic, validation, DB operations, error conditions | Any new/modified Python function, class, or API route | | **E2E GUI tests** | Playwright `.mjs` in `tests/` | DOM rendering: tab opens, panel content, form fields, keyboard nav, selection mode | Any new command, UI component, route, or interactive feature | | **Component tests** | Vitest in `web/src/__tests__/` | Isolated component behavior: rendering, props, callbacks, validation display | Complex or shared Svelte components (DynamicForm, MultiEntryField, list tabs, dialogs) |

#### Minimum assertion quality for E2E GUI tests
- **Not**: Just `assert(!text.includes("Error"))` (cheap — only checks the app didn't crash)
- **Must**: assert a tab actually rendered (e.g. `assertTabOpened("Expected Title")`)
- **Must**: assert form fields exist when a command is incomplete
- **Must**: Track console errors and FAIL on any unhandled JS exception
- **Should**: Assert specific DOM elements (tab bar, role attributes, CSS classes, button text)
- **Should**: Test keyboard navigation (open multi-tab, switch, close)
- **Should**: Test empty states, form validation, and selection mode
- **Treat the test suite as code under review**: when an assertion fails, verify the helper's output shape and regex capture before blaming the code under test.
- **No masking fallback branches**: helpers that resolve the outcome via a fallback let the wrong path pass — assert explicitly which branch was taken.

#### Match test depth to tool size
- For small CLI tools (<500 lines), `--help`/`--dry-run` smoke tests and structural ripgrep (`rg`) checks catch more real bugs than mock-based unit tests. Shell scripts with `set -euo pipefail` already catch undefined variables and early exits — a simple live run or dry-run often suffices.
- Reserve elaborate test frameworks for tools with complex data transformations, multi-layer architectures, or public APIs where subtle regressions matter.

### Running Tests from Git Worktrees
- **Never create a `.venv` inside a worktree.** All worktrees share the original checkout's `.venv`.
- **The same applies to `node_modules`** — worktrees do NOT share `node_modules` with the parent repo. Check `ls node_modules/` first. If empty, use the parent's `node_modules` via `NODE_PATH`, or install inside the worktree if you'll be working there for multiple sessions. `npx` in an empty worktree will try to install packages from scratch — don't let it.
- **Use the parent checkout's Python** — never bare `pytest`, `uv run pytest`, or any worktree-local Python:   ```bash   PYTHONPATH=src /path/to/parent/.venv/bin/python -m pytest tests/...   ```
- **Do NOT use `uv run pytest`** from a worktree — `uv run` may resolve the wrong virtual environment.
- **When test collection fails at import time**, check **`conftest.py`'s `autouse=True` fixtures** first. An autouse fixture that imports from sibling modules pulls in the entire module tree at collection time. Fix: make the deep dependency lazy (import inside the function body rather than at module level).
- **If you install a missing dependency to unblock tests**, check for unintended side effects first. Use `pip install <pkg> --dry-run` to preview what else would be modified. Consider whether the dependency is genuinely required or whether the test fixture should not depend on it in the first place.

### User-Simulation Testing
Test the end program as a user would — verify the front-end (GUI/CLI/TUI) works, not just the backend. Do **not** test directly via the backend API alone.

> **This is the FINAL manual verification step.** Before running user-simulation, ensure automated tests exist at all three layers as specified in Test Coverage Requirements. User-simulation is meant to catch what automated tests miss, not to replace them. If your user-simulation flow addresses existing test gaps and can be automated, append it to the automated test suite.

#### Reporting
When reporting back user-simulation test results, use this table format:

| what exact I have done | what results I expect to get | what results I got | what are my conclusions | |------------------------|------------------------------|--------------------|-------------------------|

#### Data isolation
- Do **not** pollute the production database — test on a COPY
- If test credentials are required, look for `.dev` files
- **Clone the data directory before any test run.** This guarantees you can restore the original state regardless of what happens during testing:   ```bash   cp -r ~/.local/share/<app>/ ~/tmp/<app>-backup/
  # ... run tests, which modify the live data ...
  rm -rf ~/.local/share/<app>/   mv ~/tmp/<app>-backup/ ~/.local/share/<app>/   ```   The `~/tmp/` directory (your home, private) is used instead of `/tmp/` (world-readable on some systems).
- **If the app supports a custom database path** (check CLI flags or config), use a temp file instead — no clone needed.

#### Cleanup
After testing is complete, clean up all processes and resources you created:

- **Kill servers you started** — If you saved the PID on start, kill by PID file. If you didn't record the PID, fall back to `fuser -k <port>/tcp`.
- **Restore backed-up data** — If you cloned a data directory for testing, restore it. Data isolation is worthless without cleanup.
- **Remove temp files** — Delete any test databases, temp directories, or artifacts created during testing.

If in doubt about whether a process is yours to kill, see Maintain Standards.

### Browser Testing Guide
**PREFER automated E2E test scripts over the interactive browser tool.** Use an interactive browser only as a last resort when an E2E script cannot reproduce the issue and you need to manually inspect the UI.

#### Automated E2E Workflow
1. **Discover** — Find existing E2E test files in the project:
   - Glob for `**/*e2e*`, `**/*spec*`, `**/*test*`, `**/playwright*`
   - Check common directories: `tests/`, `e2e/`, `cypress/`, `playwright/`
   - Check `package.json` scripts for `test:e2e`, `e2e`, `playwright`, `cypress`
2. **Check Playwright browsers** — Before attempting installs, check what's cached:    ```bash    npx playwright install --list    ```    Globally cached browsers live at `~/.cache/ms-playwright/<browser>-<revision>/`. Point test scripts at the cached binary — no need to re-install.
3. **Pre-warm Vite cache** (Vite projects only) — Vite compiles modules on first request, which can trigger OOM kills on memory-constrained systems. Fetch the page via `curl` to trigger initial compilation before Playwright. Monitor `dmesg -T` for OOM killer messages if the dev server crashes without error logs.
4. **Assess** — Read found test files. Are they relevant to the change? Do their selectors/locators still match the current UI?
5. **Run via CI when possible** — If the repo's GitHub mirror has CI with E2E coverage, trigger it and wait for results. If CI is unavailable or the test needs interactive debugging, run locally.
6. **Write or update tests** (when no CI or when adding new coverage): if tests exist but selectors are stale, **update the test file** to match the current UI, then run. If no relevant tests exist, write a new automated test file, add it to the project, run it, and commit it alongside code changes.

#### Verify Test Selectors Match Current UI
Before assuming test failures are your fault, snapshot the page and check that locators (CSS selectors, aria-labels, class names, command paths) haven't gone stale. Common rot: `<input>` → `<textarea>`, `.popup-panel` → tab-based result rendering, command paths that changed. Systematic checklist:
1. Snapshot the page → see if the expected element exists in the DOM at all
2. If the locator is missing, ripgrep (`rg`) the source for the actual class/aria-label
3. Update the test selector to match the current UI
4. Re-run the test

#### Capture Browser Console Errors
```js
page.on("pageerror", (err) => console.log("  [BROWSER ERROR]", err.message));
```
Add a handler and log errors during test runs: Console errors (especially `TypeError: Cannot read properties of undefined`) often indicate real code bugs, not test problems. Fix them even if tests pass. Note: this only catches unhandled exceptions, not `console.warn`/`console.error` calls inside try/catch — add a `page.on("console", ...)` handler for those if needed.

**Read the full Playwright error output before debugging.** When a locator fails, the error message often identifies the OBSCURING element directly (e.g. `"<div class=\"modal-overlay\">…</div> intercepts pointer events"`). Investigate WHAT is obscuring the element before debugging WHY the expected element didn't appear. A leftover modal from a prior test is a common cause; dismissing it may be the entire fix.
