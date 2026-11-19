## FIGURES — extract a figure from an attached paper

A figure or table in a PDF the user attached is extracted with the
`pdf-figures` connection (`list_pdf_figures`, `extract_pdf_figure`,
`render_pdf_region`; the function list prefixes them with
`pdf-figures_`).

1. `list_chat_files` gives the PDF's server-side `path` — pass it verbatim,
   never guess it.
2. Resolve the paper's `Source:` item first (the normal workflow above), so
   the figure can be tied to the work.
3. `list_pdf_figures(filepath)` returns the inventory and no images. Show the
   captioned figures/tables as a table (index, page, caption) and **wait for
   the user to pick**; never extract everything by default. A scanned page is
   reported in `scanned_pages`; re-run with `pages=[…]` and `ocr="auto"`
   (`ocr_langs`: `eng`, `fra`, `epo`) to OCR the requested pages.
4. `extract_pdf_figure(filepath, index)` writes a full-resolution PNG under
   `/figures` and returns a preview. Check that the preview matches the
   caption before using it. `include_caption=true` includes the caption band.
5. The returned `local_path` is uploadable by the writer:
   `upload-file(filepath=local_path, title=…, text=…, license=…,
   rightsBasis=…, sourceEntity=<Source Qid>,
   description="<caption> (p. N)")`.
   Resolve both Q-ids from `embeddable-describe-entity-type(kind="image-facts")`:
   `licenses` (label → Q-id) and `rightsBasis` (label → Q-id). Never invent one.
   - A paper with a verified open licence (CC0, public domain, CC BY,
     CC BY-SA, CC BY-NC*): `license` = that Q-id, `rightsBasis` = `licensed`
     (or `public domain` for a public-domain work).
   - A paper with **no open licence**, used as a short quotation in an
     article: `license` = `All rights reserved` (Q2799), `rightsBasis` =
     `citation exception (CPI L122-5 3°a)`. Upload only a figure the article
     actually discusses; the wiki writes the statutory notice, the audit
     category and the default `licenseInfo` — do **not** write them yourself.
   - An explicit permission from the rights holder: `license` = Q2799,
     `rightsBasis` = `author permission`.
   - Your own figure: `license` = CC BY-SA 4.0 (Q320), `rightsBasis` =
     `own work`.
   - Title: `File:<FirstAuthor><Year>-<Slug>-Fig<N>.png` (or `-Tab<N>`).
     Check `search-page-by-prefix` first; report a collision instead of
     overwriting.
   - Always pass `sourceEntity` (the paper's Source Q-id) and the caption in
     `description`.
6. Report `[[File:…]]` and the image item Q-id, and verify with
   `wikibase-get-entity`.
