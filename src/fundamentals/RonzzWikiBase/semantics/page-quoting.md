## Quoting statements in page text

Page text is a **view**; the item is the store. Quote a value with the Wikibase client functions:

| Need | Wikitext |
| --- | --- |
| Rich value (keeps markup) | `{{#statements:<property>}}` |
| Plain text (prose, table cell) | `{{#property:<property>}}` |
| An infobox row only when data exists | `{{#statement-row:<Label>|<property>}}` |
| An explicit item | `{{#statements:<property>|from=Qxx}}` |

- `<property>` may be a **label** (`number of deaths`) or a **P-id** (`P1120`). Labels are resolved by the WikibaseClient property-label resolver; prefer the label for readability and the P-id when the label is ambiguous or changes.
- Without `from=`, the item sitelinked to the current page is used.
- On an Item page, **Copy claim** gives the exact snippet (rich, plain, explicit-item) — nobody types a property id by hand.
- Common facts belong in a **template** (`Template:Event`, `Template:Person`, …): the template holds the rows and the article transcludes it.
- Property labels are a **public interface**: rename one only with a fix pass (or use the P-id form in pages).
