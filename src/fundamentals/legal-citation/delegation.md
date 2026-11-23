## Saving a citation on RonzzWikiBase

Your answer still comes from your jurisdiction's legal source. You do **not**
get the wiki write tools; the citation agent does.

When the user asks to save, cite, or create a citable item for a specific law
article on RonzzWikiBase, delegate:

```
delegate_task(
  agent="veramiko-jurist-citation",
  mode="session",
  task="Cite <law> <article> on RonzzWikiBase",
  context=<the exact tool output + the law/article you are citing>
)
```

Give the agent the **verbatim tool output** (the exact text returned by your
legal MCP tool), not a summary or your paraphrase. The agent validates the
article against the corpus; a summary cannot be validated.

Do not call `law-search`, `law-get` or `law-cite` yourself. The wiki tools are
scoped to the citation agent until the corpus proves reliable.
