ronzz.ORG is migrating from GitHub to Forgejo — GitHub is legacy, Forgejo is the future and the **source of truth**.

- **Forgejo** (forgejo.ronzz.org) is the primary forge: new repos live here; issues, PRs, and releases go through the web UI or the Forgejo REST API (`curl` against `https://forgejo.ronzz.org/api/v1/`). `git` push/pull/clone work identically via the git remote.
- **GitHub** (orgs `Ron-RONZZ-org` / `Rong-Zhou-FR`) is a legacy mirror: repos are mirrored there for **CI** (GitHub Actions — Forgejo has no CI runner) and to **accept external issues/PR contributions**. Use the `gh` CLI for GitHub-side work only; never inline markdown bodies — write the body to a file, then `--body-file`.
- When a repo exists on both forges, **Forgejo is the source of truth**; GitHub hosts CI and the external-contribution surface.
- Migration is gradual: existing GitHub repos move over to Forgejo one at a time.
