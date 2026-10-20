---
description: Full-access AI coding pair with safeguards on env files and external directories
mode: primary
permission:
  doom_loop: ask
  read:
    "*": allow
    "*.env": allow
    "*.env.*": allow
    "*.env.example": allow
  edit: allow
  write: allow
  glob: allow
  grep: allow
  webfetch: allow
  question: allow
  todowrite: allow
  list: allow
  browser: allow
  browser_clean: allow
  browser_health: allow
  browser_start: allow
  browser_snapshot: allow
  browser_click: allow
  browser_type: allow
  codesearch: deny
  plan_enter:
    "*": allow
  plan_exit:
    "*": allow
  # MCP fine-grained control
  context7_*: allow
  gortex_*: allow

  # DENY: Use specialized agents for these
  mcp_hugging_face_*: deny
  mcp_github*: deny
  task:
    githubber: allow
    huggingfacer: allow
    architect: ask
    refactorer: allow
    reviewer: allow
    debugger: allow
    tester: allow
    explore: allow
    expert: ask
---

{{include:follow-AGENTS.md}}
