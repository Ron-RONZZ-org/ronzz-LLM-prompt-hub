RonzzWikiBase runs the Diagrams extension: a text-heavy or structural diagram
belongs in the page **as wikitext**, not as an uploaded image. The tags are
`<uml>`, `<graphviz>`, `<mscgen>` and `<mermaid>` — **not** `<plantuml>`,
which is unregistered and renders as literal text. Usage reference:
https://wikibase.ronzz.org/wiki/Help:Contributing/diagrams.

| Tag | Renders | Where |
| --- | --- | --- |
| `<uml>…</uml>` | PlantUML (sequence, class, state, activity, component, …; `type=` selects another dialect) | server-side, cached SVG |
| `<graphviz>…</graphviz>` | GraphViz (`renderer` = `dot` (default), `neato`, `fdp`, `sfdp`, `circo`, `twopi`, `osage`) | server-side, cached SVG |
| `<mscgen>…</mscgen>` | Message sequence charts | server-side, cached SVG |
| `<mermaid>…</mermaid>` | Mermaid | client-side (blank in print/export) |

Default output is SVG; add `format="png"` only when a raster is explicitly
required. `<mermaid>` runs in the reader's browser and is empty in print and
static export, so prefer `<uml>` unless Mermaid syntax is specifically wanted.

**PlantUML specifics**

- `<uml>` (default `type="uml"`) covers sequence, class, state, activity,
  component, object, use-case, deployment and timing diagrams. For another
  dialect set `type`, which becomes the `@start<type>` directive:
  `type="mindmap"`, `type="salt"`, `type="gantt"`, `type="wbs"`,
  `type="json"`, `type="yaml"`, `type="ditaa"`, …
- The usual `@startuml` / `@enduml` directives are optional — the extension
  adds them. Omit them and let `type` do the wrapping.
- PlantUML runs in its **SANDBOX** security profile: `!include` of local files
  and URLs is disabled. The bundled stdlib works (`!include <C4/C4_Context>`,
  `!theme bluegray`, …); the diagram must otherwise be self-contained.

{{include:format/plantuml}}

- A tag that fails to render leaves an error span on the page, so **validate
  before publishing**: call `validate_uml(diagram_type="plantuml", code=…)`
  (`graphviz`, `mscgen`, `mermaid` for the other tags) with the exact code you
  are about to publish, fix every reported error, and re-validate until clean.
  On the wiki, `parse-wikitext` over the final page text is the last check that
  the tag renders instead of erroring.
- `list_diagram_types` reports which `diagram_type` values and output formats
  the renderer backend supports — call it when unsure.

**Delivering a diagram**

- **In a wiki page** → write the tag with `update-page` (fetch the page first
  and pass its `latestId`) or with `create-page` for a new page. Do not upload
  a file the tag renders.
- **As a page snippet** → when you cannot or should not edit the page, reply
  with the tag wikitext.
- A tool-rendered preview is optional; the tag is the deliverable, not the
  preview image.
