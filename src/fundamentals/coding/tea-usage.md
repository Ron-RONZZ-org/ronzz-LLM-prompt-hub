Common Forgejo operations with `tea` (Gitea's official CLI, works with Forgejo instances). Login once with `tea login add`; tea reads the repo in `$PWD` from its git remote:

```bash
tea issues                        # list open issues (--state all|open|closed)
tea issue 42                      # view an issue
tea issues create --title "…" --description-file /tmp/body.md
tea issues close 42               # close (--comment "…" adds one)
tea pulls                         # list PRs; tea pulls checkout 128; tea pulls merge 128
tea labels                        # list/manage labels
tea releases                      # list/manage releases
tea comment 42 "…"                # comment on an issue/PR
tea open 42                       # open in the web UI
```

Installation is the user's job — never install it yourself.
