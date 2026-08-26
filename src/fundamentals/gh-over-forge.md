ronzz.ORG works with both GitHub and Forgejo:

- **GitHub** is the primary forge: use the `gh` CLI for issues, pull requests, labels, and workflows. Never inline markdown bodies — write the body to a file, then `--body-file`.
- **Forgejo** (forgejo.ronzz.org) hosts internal-only repos. `git` push/pull/clone work identically via the git remote; issues, PRs, and releases go through the web UI (or the `tea` CLI). There is no CI runner on Forgejo — repos that need CI are mirrored to GitHub, where GitHub Actions runs.
- When a repo exists on both forges, GitHub is the source of truth for issues/PRs/CI.
