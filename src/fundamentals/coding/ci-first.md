Before running any build or test that will take **>30 seconds**, check if the repo's GitHub mirror has CI workflows that can do it on GitHub runners instead:

```bash
gh workflow list   # only in a repo with a GitHub mirror
```

| Runtime | What to do | |---------|-----------| | **<30s** (format check, single-package unit test, interactive debug) | Fine to run locally | | **>30s** (full build, integration tests, E2E, multi-package suite) | Use the mirror's CI (`gh workflow run <name> -f scope=...`) or **propose new CI for user approval** if none exists |

Rationale: every minute of heavy compute you run locally is a minute this machine is at OOM risk and unavailable for other sessions. GitHub runners are free for public repos and cheap for private ones — use them.
