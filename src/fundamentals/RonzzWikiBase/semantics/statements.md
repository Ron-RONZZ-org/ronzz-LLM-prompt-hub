## Statements

A statement is **property → value**, optionally with qualifiers and references.

- **Property** carries the semantics: use an item value when an item exists (a source's `authors`, `publisher` and `journal` are item ids, not strings).
- **Qualifiers** narrow the value without changing the property — a participant's `role`, a date's `circa`, an amount's unit or point in time.
- **References** carry provenance: at least one `Source:` item per factual statement (`source`, the Wikidata P248-aligned property), not a bare URL when a Source item exists.
- **Rank**: a curated value is `preferred`; imported or provisional values are `normal`. Never silently replace a preferred value.
- **Uncertainty is data**: mark `circa` / `presumably` with a qualifier instead of writing a guessed precise value.
- **No invented vocabulary**: a value the vocabulary cannot express is a proposal to the human, never a new property invented on the spot.
