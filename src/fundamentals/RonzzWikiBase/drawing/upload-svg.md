## UPLOAD TO RONZZWIKIBASE

Upload only after the user validates the figure.

1. **Get the path.** `files[].path` from `execute_code` (the file must be under
   `UPLOAD_DIR` and listed in `files_to_save`). Never guess a path.
2. **Check the title.** `search-page-by-prefix` / `get-file-info` on
   `File:<Kebab-case>.svg`. An existing file means a revision, not a duplicate.
3. **Resolve the licence.** Own figures are CC BY-SA 4.0 (`Q320`).
   `embeddable-describe-entity-type(kind="image-facts")` returns the label → Q-id
   map; `wikibase-search-entities` is the fallback. Never invent a Q-id.
   {{include:licence-requirements}}
4. **Upload.** `upload-file(filepath=…, title="File:<Kebab-case>.svg",
   text=<File page text>, license="Q320", author=<author named in this prompt>,
   description=…)`.
   - The Veramiko models use `Rong Martin-Siebler ZHOU and Veramiko AI`;
     `/svg-ronzzwikibase` uses `Rong Martin-Siebler ZHOU and RonzzWikiCowriter AI`.
   - Existing figure: `update-file` with the same title. Facts only:
     `update-file(factsOnly=true, …)`.
   - Omit `sourceUrl` for a self-made figure; the File page is the origin.
5. **File page text.** One-sentence description; the source reference (for a
   plot: APA 7 with DOI and the `Source:` page link; for an illustration: the
   source, or `own work`); `== Licensing ==` and `{{CC BY-SA 4.0}}`.
6. **Reply** with `[[File:<Name>.svg]]` and nothing else after the upload.

Titles are kebab-case and descriptive: `File:Social-Loafing-Expectancy-Value-95CI.svg`,
not `File:figure1.svg`.
