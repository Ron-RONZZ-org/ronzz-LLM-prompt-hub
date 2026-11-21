## The one rule: resolve before create

Never create an item when an existing one matches.

1. `wikibase-search-entities` by label.
2. `wikibase-query` by authority ID (Wikidata, ORCID, VIAF, ISNI, DOI, ISBN, OpenAlex). Get the property IDs from `embeddable-describe-entity-type`; do not guess them.
3. `embeddable-authority-search` to fetch the authority record when the user gives a DOI, ISBN, ORCID, URL or title.

If a match exists, reuse or enrich it through the add tools' `qid` update path. Do not duplicate.
