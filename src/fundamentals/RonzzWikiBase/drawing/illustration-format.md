## FORMAT FIRST — decide what the figure is made of

Before choosing a tool, decide the medium:

1. **Text-heavy or structural diagram** — software architecture, class,
   sequence, state, activity, component, ER, flowcharts, message-sequence
   charts, mind maps, dependency or network graphs. Prefer the wiki's native
   tags: `<uml>` (PlantUML), `<graphviz>` or `<mscgen>`; `<mermaid>` only when
   Mermaid syntax is specifically requested. They render server-side from page
   text, stay editable in page history and diffs, and print correctly. An
   uploaded SVG for one of these is the exception, not the default.
2. **Graphic no tag can express** — textbook schematics (free body, rays,
   circuits, geometry, chemistry structures or reactions, orbitals, Feynman
   vertices), data plots, annotated images, or a layout no diagram DSL
   produces. Draw them as **SVG** with the right library: TikZ for schematics,
   `circuitikz`, `chemfig`, `modiagram`, `tikz-feynhand` for their domains,
   matplotlib for data, hand-authored SVG when no library fits.
3. **An asset that must exist as a file** — a figure reused across pages,
   embedded in chat, or destined for an external document. Render it, then
   upload it as `File:…`.

Then choose the tool from TOOL CHOICE. For the native-tag route, write and
validate the tag per RONZZWIKIBASE TEXT DIAGRAMS.
