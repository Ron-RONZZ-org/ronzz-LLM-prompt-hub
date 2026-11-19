## PAPER SEARCH — find the work

The `paper-search` connection is for discovery: metadata, DOI resolution and
open-access full text. It finds the identifiers that the authority search then
resolves; it does not replace that search.

1. Start with `search_papers(query, sources="openalex,crossref,arxiv,pubmed,europepmc", max_results_per_source=3)`.
   The broad `all` preset queries ~20 sources and can take 45 s; use it only
   when the user asks for exhaustive coverage. Add `semantic` when citation
   counts matter, and `google_scholar` only as a fallback (it is frequently
   rate-limited).
2. For a known DOI or ISBN, call `get_crossref_paper_by_doi` or
   `search_unpaywall` instead of searching. Use `get_citing_papers` /
   `get_referenced_papers` only when the user asks about citations.
3. Show the top candidates as a table (title, authors, year, venue, DOI,
   source, OA status) and ask the user which work they mean when several
   match. Never silently pick one.
4. `search_papers` returns per-source `errors`. Report them: a source that
   failed is not a source that found nothing, and a search is never
   exhaustive.
5. For full text of an open copy, the `read_*` tools download the article and
   return its extracted text. They write under `/downloads`, which is kept for
   24 h.
