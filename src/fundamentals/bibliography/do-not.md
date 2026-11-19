## Do not

- Do not invent metadata, identifiers or Q-ids. If a field is unknown, leave it blank and say so.
- Do not create an item that already exists under another label: search the authority ID first.
- Do not use `confirmDuplicate` to force a create; it produces a second item for the same work.
- Do not edit article prose. Return the citation snippet; the editor or RonzzWikiCowriter inserts it.
- Do not pass a name string to `authors`, `publisher` or `journal`: those fields are Q-ids. A pasted author list goes in `authorNames`; resolve or create the entities first.
- Do not bind a fuzzy author match (`exact=false`) without confirmation.
- Do not leave a group of humans labeled as a hand-written author list; its label is generated from its `members` (P82).
- Do not publish a user's copy of a copyrighted work as a public access file, and do not pass a `license` for an internal-use copy (it is recorded as "All rights reserved").
- Do not upload a figure from a paper whose licence is not a verified open licence unless `rightsBasis` is the citation-exception item and the article discusses that figure.
- Do not write `licenseInfo`, `{{Citation exception}}` or a category for a rights-basis upload: the wiki adds them from the rights basis.
- Do not extract every figure of a paper without the user's selection, and do not invent a caption, page number or figure index.
