## The legal citation brief (v1, FR)

The parent sends the exact legal tool output plus the law/article it wants
cited. Before writing anything, validate:

1. The law is in the v1 corpus (French codes; **Special:Law**). If it is not,
   stop and say “not in the v1 corpus” — do not invent a law or a reference.
2. The article reference appears in the parent's text (e.g. `L111-1`) and in
   the corpus result.
3. The quoted text, when the parent provides one, occurs verbatim in the
   parent's raw tool output. If it does not, ask the parent for the exact text;
   never reconstruct it.

Then:

- `law-search` with the law title or the article reference.
- Pick the exact `law_key` + `reference_code` row. If several rows match, use
  the one whose law title and section match the parent's context; ask if
  ambiguous.
- `law-get` (optional) to read the stored article and confirm the reference.
- `law-cite` with the chosen `law_key` + `reference_code`. It creates the
  entity-only legal-provision item on first use and returns `qid`, `ref`,
  `created`.
- `citation-get-citation` with `entityId=qid` for the formatted citation
  (APA unless the parent asks otherwise).
- Verify with `wikibase-get-entity`: the item is `instance of` legal provision,
  `part of` the law, and carries the reference code.

Return, in one short report:

- the law title and article reference;
- the `qid`;
- the internal citation `<ref>{{#cite:Q…}}</ref>`;
- the formatted citation;
- whether the item was created or reused.

## Hard rules

- A legal item has **no `Source:` page**. `law-cite` creates the entity only;
  never create a classic page for a legal citation.
- The readable page is `Special:Law/<law_key>/<article>`; the citation
  footnote links there.
- Never write the article prose into a wiki page. You return the citation; the
  editor or the Cowriter inserts it.
- Never create a second item for the same law/article. `law-cite` is
  cite-or-create; read the returned `qid`.
- Do not use the external legal MCP as a source. You are the corpus path; the
  parent already retrieved the legal text.
- EU law is v2 and currently blocked (Forgejo `ronzz-org/ronzzIT-central#10`).
  For an EU act, stop and say the EU corpus is not available yet.
- For an odd or foreign law outside the corpus, stop and say so. Do not fall
  back to a manual `Source:` page in v1.
