## Class notes

`embeddable-describe-entity-type` with `kind='citation-source'` returns the current class list and the fields each class exposes. Call it before the first create or update in a chat, and again whenever a create is rejected with an unexpected field.
- `website` and `webpage` are URL-first: pass the URL to `embeddable-authority-search` with the class to fetch the page metadata.
- `transcript`, `text` and `law` have no external authority: create them from the user's fields; the authority search returns a warning for them.
- A book excerpt requires its parent book; a YouTube video requires its channel; a legal provision requires its legislation. `parent` accepts a comma-separated list when the child belongs to several parents.
- The human workflow for the same steps is documented at https://wikibase.ronzz.org/wiki/Help:Contributing/import.
