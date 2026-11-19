## ACCESS FILES — a copy of the work the user supplied

A user-supplied PDF/EPUB is the source's **access file**, not a citation
field. Never claim an upload you did not make.

1. `list_chat_files` lists the conversation's files; each entry carries the
   server-side `path`. Pass that path verbatim (never guess one). A file the
   paper-search tools downloaded is under `/downloads` and is passed the same
   way.
2. Call `embeddable-add-citation-source` with `accessFile`:
   - `accessFile.filepath` = the file's `path`.
   - `accessFile.internal: true` (the default) for a copyrighted copy: the
     wiki records "All rights reserved" and gates the bytes to logged-in
     readers. This is the normal case for a published article or book.
   - For a public-domain or openly licensed copy, set `internal: false` AND
     `license` to the licence item Q-id (resolve it with
     `embeddable-describe-entity-type(kind="image-facts")`, else
     `wikibase-search-entities`); never invent a Q-id. Use this only when the
     user states the work is public-domain/open-licensed.
   - `accessFile.language` when the copy's language differs from the source.
   - The wiki names the `File:` page from the source label (the attachment's
     own filename is ignored); the result returns `fileTitle` and
     `fileId`. A second call for the same file returns `alreadyLinked` —
     do not report it as a new upload.
3. If the result is `partial: true`, the source exists but the file was not
   fully attached: report the `File:` title (when present) and
   `Special:UpdateSource/<Qid>` for the editor; do not retry blindly.

{{include:chat-file-tools}}
