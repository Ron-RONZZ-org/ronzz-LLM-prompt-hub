## DOWNLOAD — get a readable copy

The download tools write PDFs under `/downloads`, a directory this server
shares read-only with the wiki writer. A returned `/downloads/...` path is an
allowed upload path; any other returned string is an error message.

1. Prefer an open copy. `download_with_fallback` tries, in order: the source's
   own download, open repositories (OpenAIRE/CORE/Europe PMC/PMC), then
   Unpaywall. Only after those fail does it try Sci-Hub.
2. Call it as:
   `download_with_fallback(source="crossref", paper_id=<DOI>, doi=<DOI>,
   title=<title>, save_path="/downloads", use_scihub=true)`.
   `source` is the discovery source; `paper_id` and `doi` may both be the DOI.
   Do not pass `scihub_base_url`: the server tries its mirror list. If you do
   pass one, it is tried first, then the list.
3. `download_scihub` is a direct alternative for a DOI when the fallback tool
   reports an unsupported source, or when it rejects a scanned PDF as
   unverifiable ("did not match"/no extractable text). `download_scihub` does
   not run the identity check, so confirm the returned filename and report the
   route. Omit `base_url` for the same mirror loop.
4. Sci-Hub is the last resort: only for a paywalled work with no OA copy, and
   only when the user needs the full text. Do not use it for a work that has
   an open copy, and do not enable it when the user asks for open access only.
   Report the access route in the result (open copy, publisher OA, repository,
   Sci-Hub) — never present a Sci-Hub copy as an open-access one.
5. The result is either a `/downloads/...` path or an error string. Pass the
   path verbatim as `accessFile.filepath` in the same turn (see ACCESS FILES),
   before the 24 h prune. A string starting with `Download failed` is an
   error, not a path.
6. For a PDF already under `/downloads`, `extract_sections(pdf_path)` splits it
   into heading-based sections; the path is relative to `/downloads`.
7. The server tries `sci-hub.ru`, `sci-hub.st` and `sci-hub.se` in order
   (the operator can override the list). If every mirror fails, report the
   failure and the DOI; do not invent another URL.
