**CRITICAL: Never use `git checkout`, `git switch`, `git stash`, or any command that changes the current branch or stashes work in the main checkout.**

There are often **multiple AI coding agents running concurrently** on a machine (e.g. via a serve+attach model). If one agent switches branches or stashes work, it **silently disrupts every other agent** attached to the same repo — they find themselves on a different branch or with work suddenly stashed, with no warning.

**Safe operations** (do not affect other agents):
- Read-only git commands: `status`, `diff`, `log`, `branch --list`
- Committing to the current branch: `add`, `commit`, `push`, `pull`
- Restoring files: `git checkout -- <file>`, `git restore <file>`

**Forbidden operations** (use worktree instead):
- `git checkout <branch>` — switches current branch
- `git checkout -b <name>` — creates and switches branch
- `git switch <branch>` — modern branch switching
- `git stash`, `git stash push`, `git stash pop` — hides/restores work in progress

**Workflow for branch work:**
1. Create an isolated worktree: `git worktree add /path/to/worktree <branch>`
2. Change to the worktree directory and work there (keeps your full session context)
3. When done, change back to the main repo and clean up: `git worktree remove /path/to/worktree`

**Cleanup:**
- **Delete worktree branches immediately after the PR is merged** — delaying even one session makes it hard to distinguish "work not merged" from "work already merged, branch not cleaned up."
- **Do not create temporary branches outside the worktree system** (`temp-fix`, `temp-rebase`, etc.). If a temp branch is unavoidable, delete it as soon as the equivalent PR is submitted — not later.
- **`git branch --merged main` is unreliable with squash/rebase merges.** The branch commits get a different hash after squash. Always verify content, not commit ancestry.
- **Never use `rm -rf` on a worktree directory.** This orphans the active session and can cause data loss or corruption. Always use the sanctioned worktree cleanup tooling — it validates safety first, preserves session continuity, and defers directory removal.
- **A failed `git worktree remove` leaves a half-removed state.** Removal deregisters the worktree *before* deleting the directory — a permission failure on root-owned files leaves the directory present but unregistered. Verify with `git worktree list` + `git branch --list`, then `sudo git worktree remove` (handles the root-owned files), or remove the leftover directory + `git worktree prune`.
