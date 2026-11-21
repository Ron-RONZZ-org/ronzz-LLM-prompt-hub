Named things that recur — persons, collectives, citation sources, quotations, code snippets, and important or general-form mathematical expressions — are stored as Wikibase **items** with Q-ids. A page pulls the item's data at view time, so editing the item updates every page that uses it.

### The three workflows

1. **Mention an entity** (author, organisation, band, …): `wikibase-search-entities` by label → reuse the match, or create it with `embeddable-add-semantic-entity` (`kind`: person | software | collective | fictional-character | other) → mention it as `[[<its sitelinked page>|<mention text>]]`.
   - A source's `authors`, `publisher` and `journal` fields are **item ids**: resolve or create the Person/Collective first and pass its Q-id.
   - A pasted author list goes in `authorNames`, not `authors`: the first call writes nothing and returns the batch resolution; confirm each name, then call again with `authorDecisions`.
   - Prefix a collective author with `ORG:`. A fixed research group is a `Collective:` of class `group of humans` with `members` Persons.
2. **Cite a source** (book, article, website, film, …): search → reuse, or create it with `embeddable-add-citation-source` → cite it inline as `<ref>{{#cite:Qxx}}</ref>`.
   - Child classes need a `parent`: webpage → website, youtube-video → youtube-channel, book-excerpt → book, law → legislation.
   - A user-supplied PDF/EPUB is the source's **access file**: read its path from `list_chat_files` and pass `accessFile={filepath, internal: true}` to `embeddable-add-citation-source`. Internal use is the default ("All rights reserved"); a public copy needs the user's licence Q-id. If the result is `partial: true`, report the `File:` title and `Special:UpdateSource/<Qid>` instead of retrying.
   - For a bulk bibliography, hand off to the Veramiko Bibliographer (DOI/ISBN/ORCID lookup + batch author resolution).
3. **Embed content** (quotation, code snippet): search first (they are shared items) → reuse, or create it with `embeddable-add-special-content` (`kind`: quotation | code-snippet) → embed it as `{{#content:Qxx}}`.

### The rules behind them

- **Reuse before create** — never create an item that already exists.
- **Never invent a Q-id or a property id.** Confirm with `wikibase-search-entities` / `wikibase-get-entity`; ask `embeddable-describe-entity-type` for a class's exact fields and resolved property ids.
- **If the entity already exists, always reuse it.**
- **One concept per item**; do not create a second item for the same thing.
