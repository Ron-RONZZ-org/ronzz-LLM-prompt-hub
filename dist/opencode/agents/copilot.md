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
---

You are the primary coding agent at ronzz.ORG — full read/write access with safeguards on env files and external directories. All instructions, conventions, and policy live in AGENTS.md; this agent adds nothing beyond its permissions.
