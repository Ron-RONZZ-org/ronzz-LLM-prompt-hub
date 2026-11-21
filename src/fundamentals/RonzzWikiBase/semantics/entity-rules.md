## Entity rules

- **One concept per item** — merge duplicates instead of creating near-copies.
- **Reuse properties** — propose a new one only when nothing fits; datatype is forever, so double-check it before creating.
- **English labels are mandatory**; other languages are welcome (content language: `en`).
- **Never invent a Q-id or a P-id** — resolve it with `wikibase-search-entities` / `wikibase-get-entity`, or ask `embeddable-describe-entity-type`.
- **Cite every factual statement** (house rule 3): a statement without a reference is incomplete.
- **One item per page**: a classic page's sitelinked item is its semantic identity; do not create a second item for the same page.
