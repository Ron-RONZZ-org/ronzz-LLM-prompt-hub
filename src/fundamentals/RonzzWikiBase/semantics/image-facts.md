## Image facts on upload

`upload-file` / `upload-file-from-url` accept the image's semantic facts; on this wiki they create or reuse the sitelinked `image`-class item, so the `File:` page renders them.

- `license` — the licence item's Q-id. Get the wiki's label → Q-id map from `embeddable-describe-entity-type(kind="image-facts")`; `wikibase-search-entities` is the fallback. Never invent a Q-id.
- `author` — free-text attribution.
- `description` — a short description.
- `licenseInfo` — attribution or terms text the licence requires.
- `sourceUrl` — **only** for an image that came from an external source (web page, repository, Commons `File:` page). Omit it for a figure you generated: the `File:` page is its origin.
- `rightsBasis` — the legal ground for a non-free reproduction (citation exception, author permission, own work). The wiki adds the notice and the default license info.
- **Revision**: `update-file` / `update-file-from-url` replace the facts you pass and keep blank ones; `factsOnly: true` changes facts without new bytes; `clear: [...]` removes a fact.
- **Commons**: `image-search` → `upload-file-from-url`, passing the returned licence/author/credit and the Commons file-page URL as `sourceUrl`.
