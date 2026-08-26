ronzz.ORG is migrating from GitHub to Forgejo — GitHub is legacy, Forgejo is the future and the **source of truth**.

- **Forgejo** (forgejo.ronzz.org) is the primary forge: new repos live here; issues, PRs, labels, and releases go through the `tea` CLI (usage below).
- **GitHub** (account `Ron-RONZZ-org`) is a legacy mirror: repos are mirrored there for **CI** (GitHub Actions — our Forgejo has no CI runner yet) and to **accept external issues/PR contributions**.
- When a repo exists on both forges, **Forgejo is normally the source of truth**;
  - however, beware of contributors accidentally pushing to Github and makes Forgejo fall behind
- Migration is gradual: existing GitHub repos move over to Forgejo one at a time.
