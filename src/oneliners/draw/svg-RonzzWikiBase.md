## TASK

Draw an SVG illustration or icon based on the prompt.

This command is for true vector illustrations. For a data plot, use
`/illustrate-data`; for a UML/PlantUML/GraphViz/Mermaid diagram, use
`/make-mediawiki-plantuml-diagram`.

When done, present the SVG to the user. No extra explanations. Iterate until the
user is satisfied.

On validation, upload to RonzzWikiBase and reply uniquely with:

[[File:{file-name}]]

Author: `Rong Martin-Siebler ZHOU and RonzzWikiCowriter AI` (use
`Veramiko AI` when the model is a Veramiko model).

## STAGING — file → wiki

1. In one `execute_code` call, write the final SVG to
   `Path(UPLOAD_DIR) / "<file-name>.svg"` and pass that path in `files_to_save`.
   `UPLOAD_DIR` is provided by the interpreter; do not guess a server path.
2. Take `files[0].path` from the result and pass it verbatim as `filepath` to
   `upload-file`.
3. If the result has no `files[]`, fix the `execute_code` call: the file must be
   written under `UPLOAD_DIR` and listed in `files_to_save`.
4. If `execute_code` returns an error or a traceback, read it and fix the call.
   Never retry an identical failing call.

{{include:RonzzWikiBase/drawing/upload-svg}}

## PREVIEW — inspect without polluting the wiki

Before presenting the SVG, call `render-svg` with the final SVG source. It returns
the raster and any warnings. Look at it, compare it with the request, fix what is
wrong, and render again. Present only after the rendering matches the request.

After the upload, `get-file-content` with `format="both"` on the `File:` title
returns the stored raster and the SVG XML for a final check.

{{include:drawing/svg}}

## Prompt

{{to-illustrate}}
