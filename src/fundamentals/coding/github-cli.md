#### GitHub mirror (`gh`)

`gh` is used **only** for the GitHub mirror of a Forgejo project — GitHub Actions and external contributions. `tea` cannot talk to GitHub and `gh` cannot talk to Forgejo, so the two never substitute for each other. Forgejo issues/PRs stay on `tea` (see above).

**Mandatory rules:**

- **File-based bodies, always** — write the body to a file, then `gh issue create --body-file /tmp/body.md` (or `gh pr create --body-file`). Never inline markdown in a shell one-liner.
- **Labels must exist** before `--add-label` — create them first with `gh label create`.
- **Sub-issues and blocked-by are GraphQL-only** — `gh issue edit` cannot set them.

**GraphQL for relationships.** Resolve node IDs first, then mutate:

```bash
gh api graphql -f query='
query {
  repository(owner: "OWNER", name: "REPO") {
    issueN: issue(number: N) { id }
  }
}' --jq '.data.repository'
```

```bash
# sub-issue: parent <- child
gh api graphql -f query='
mutation {
  addSubIssue(input: {
    issueId: "PARENT_NODE_ID",
    subIssueId: "CHILD_NODE_ID"
  }) { subIssue { id } }
}'

# blocked-by: issueId is blocked by blockingIssueId
gh api graphql -f query='
mutation {
  addBlockedBy(input: {
    issueId: "BLOCKED_ISSUE_NODE_ID",
    blockingIssueId: "BLOCKING_ISSUE_NODE_ID"
  }) { clientMutationId }
}'
```

**Triggering CI workflows** (the GitHub mirror is where CI runs):

```bash
gh workflow list
gh workflow run ci.yml -f scope=unit
gh workflow run ci.yml -f scope=unit,build
# common scopes: unit, integration, build, e2e (comma-separated)
```

When the wiki or the mirror's issue tracker is the target, say which forge you are operating on. Full pattern reference (issue CRUD, file bodies, schema introspection, pitfalls): the `AGENTS-gh-cli.md` file shipped alongside this config.
