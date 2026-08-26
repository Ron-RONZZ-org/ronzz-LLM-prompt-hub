ronzz.ORG is migrating from GitHub to Forgejo — GitHub is legacy, Forgejo is the future and the **source of truth**.

- **Forgejo** (forgejo.ronzz.org) is the primary forge: new repos live here; issues, PRs, labels, and releases go through the `tea` CLI (usage below).
- **GitHub** (orgs `Ron-RONZZ-org` / `Rong-Zhou-FR`) is a legacy mirror: repos are mirrored there for **CI** (GitHub Actions — Forgejo has no CI runner) and to **accept external issues/PR contributions**.
- When a repo exists on both forges, **Forgejo is the source of truth**; GitHub hosts CI and the external-contribution surface.
- Migration is gradual: existing GitHub repos move over to Forgejo one at a time.
