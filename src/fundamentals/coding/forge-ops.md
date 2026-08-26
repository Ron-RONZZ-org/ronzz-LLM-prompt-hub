{{include:coding/tea-usage}}

**Operational rules:**

- **Always use file-based bodies** — `tea issues create --description-file body.md` on Forgejo, `gh issue create --body-file` on GitHub. Never inline markdown in a shell one-liner.
- **Labels must exist before use** — manage them with `tea labels` (or the web UI).
- **REST API fallback** (scripting where tea cannot do the job): write the JSON body to a file, then POST it with `curl`. Never inline markdown in a shell one-liner:
  ```bash
  # requires a Forgejo access token (PAT) — ask the user for one, never invent credentials
  cat > /tmp/issue.json <<'JSON'
  { "title": "…", "body": "…" }
  JSON
  curl -sf -X POST https://forgejo.ronzz.org/api/v1/repos/ronzz-org/<repo>/issues \
       -H "Authorization: token <PAT>" -H "Content-Type: application/json" -d @/tmp/issue.json
  ```
- **Issue relationships (blocked-by, sub-issues)**: use the web UI, or the REST API endpoint `POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies` with `{"depends_on": [<issue-index>]}` in the body (confirm the exact shape in the Forgejo API docs).
- **Forgejo has no CI runner** — CI runs on the GitHub mirror via GitHub Actions; use `gh` against `github.com` for those workflows (`gh workflow list`, `gh workflow run ci.yml -f scope=…`).
