### Resolve the agents before the source

- **Pasted author list** — pass `authorNames` to `embeddable-add-citation-source`, never `authors`. The first call writes nothing and returns the batch resolution (`authorConfirmationRequired=1`); confirm each name, then call again with `authorDecisions` (and optional `authorDetails`) to create/reuse the Persons and the Source in one write. Use `embeddable-resolve-authors` for a read-only preflight of the same list. A name prefixed with `ORG:` is a collective row (e.g. `ORG:Wikimedia Foundation`); use semicolons when the organisation name contains a comma.
- **Individual author** — use `local.authors[]` from the work result. A non-null `qid` with `exact=true` can be reused. A non-null `qid` with `exact=false` is a suggestion: confirm its authority ID or ask the user before using it; never bind a fuzzy same-name person silently. If no candidate exists, create the person with `embeddable-add-semantic-entity` (kind=person), passing given/family names, every authority ID the record carries (`orcid`, `viafId`, `isni`, `wikidataId`, `openalexAuthorId`), and `affiliatedWith` when known.
- **Group of humans** — a fixed research group may be a `Collective:` of class `group of humans` (Q8) whose members are `Person:` items; use `memberNames` / `memberDecisions` on `embeddable-add-semantic-entity`, or pass the member Q-ids in `members`. Do not create a group item for an ordinary author list.
- Publisher: use `local.publisher`. If unresolved, search `kind=entity` or create a collective (`embeddable-add-semantic-entity`, kind=collective, `collectiveClass=Q1730` for a publisher) and use its Q-id.
- Journal (scholarly article): use `local.journal`. If unresolved, find the existing periodical item or create it (`collectiveClass=Q1731`), then use its Q-id.
- `authors`, `publisher` and `journal` are item IDs, never names. A pasted name list goes in `authorNames`, never in `authors`.

### Create or update the source

- Pass `classKey`, `title`, the resolved `authors` Q-ids (or `authorNames` + `authorDecisions`), the `publisher`/`journal` Q-ids, `year`, `doi`/`isbn`/`openalexWorkId`/`pubmedId`, `url`, `language` and any other field the record provides.
- Child classes need a parent (`parent`, comma-separated if several): webpage → website, youtube-video → youtube-channel, book-excerpt → book, law → legislation.
- A create matching an existing item returns `duplicate` + `duplicateOf`: reuse that item; do not set `confirmDuplicate`.
- A label collision returns `collision` + `collisionOf`: use `collisionAction=reuse` only when it is the same work; `delete` and `duplicate` need explicit user approval.
- A PDF/EPUB supplied by the user or downloaded for the work: attach it as the access file in the same call (`accessFile`), per ACCESS FILES below.

### Verify and report

Verify each created or updated item with `wikibase-get-entity`: the class and the key statements (authors, publisher/journal, year, identifiers). Then format the citation with `citation-get-citation`.

Report the table and the citation snippets. List anything unresolved (a missing author, an unknown publisher) explicitly rather than silently dropping it.
