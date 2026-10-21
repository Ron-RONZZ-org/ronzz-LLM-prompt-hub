## METHOD — programmatic first (mandatory when tools are available)
Generate the SVG with a script (Python + svgwrite/ElementTree/plain string builder) rather than writing markup by hand. The script must:
1. Declare all sizes as multiples of a base unit `u` (see SIZING CONTRACT). No absolute pixel font-sizes anywhere.
2. Compute every label's bounding box (assume advance width ≈ 0.55 × font-size per character for serif) and assert no two labels overlap; assert the span check; assert the collision check. Fail loudly if any assertion breaks.
3. Emit the SVG from the computed geometry.
4. Print `u`, each font-size, and the span-check value to stdout for verification.
If no code execution is available, write out the same numbers by hand.

## SIZING CONTRACT
- `viewBox` must be {20–40} primary font-sizes across its smaller dimension. Derive canvas size from this, not the other way round.
- Base unit `u` = {natural atom of this diagram: tick spacing / node height / band width / shortest labeled segment / row pitch / grid cell / (smaller canvas dimension ÷ 30)}.
- Font sizes (all same serif family, e.g. Times New Roman):
  - Primary labels (axis numbers, node labels, data values): 0.40 u
  - Secondary labels (axis names, title, legend): 0.35 u
  - Tertiary labels (annotations, callouts): 0.30 u
- Strokes: axes/ticks 0.010 u · connectors 0.07 u · guides 0.07 u · dash pattern 0.015 u · marker radius 0.10 u.
- Font family must be identical for every text element; font sizes must come only from the tiers above (no ad-hoc sizes).

## LAYOUT CONTRACT
- Every label on a shared baseline uses the identical `y`.
- If labels would collide, move the offenders to an additional row at the SAME font size — never shrink them, never let them overlap.
- Collision check per row: `font-size ≤ L / (N · (0.55·n + 0.2))`, where L = row length, N = label count, n = chars per label. If it fails, drop minor ticks, stagger rows, or extend the axis.
- Every annotation/point must have the required guides (e.g. dashed lines to both axes) drawn before labels, with labels placed just outside the point/label.


## BASE IMAGE / OVERLAY — when the user supplies artwork

If the user attaches an image and asks for labels, arrows, axes or annotations **on top of it**, that image is the artwork. Do **not** redraw, trace or vectorise it.

1. Read the attachment from `UPLOAD_DIR` (the interpreter's upload folder), using the file name the user attached. If it is not there, stop and ask the user to re-attach it; do not reconstruct the artwork from the prompt text.
2. Embed it unchanged in the SVG. For a raster base:

   ```python
   import base64
   data = base64.b64encode((Path(UPLOAD_DIR) / "base.png").read_bytes()).decode()
   # <image href="data:image/png;base64,{data}" x="0" y="0" width="W" height="H"/>
   ```

   Set the SVG `viewBox` from the image's own `width`/`height` (or scale both by the same factor). A raster base stays a raster.
3. Add only the requested labels and guides as text/line elements, positioned from the base image's dimensions. If you cannot inspect the image, ask the user for the positions instead of guessing.
4. Keep it a single self-contained SVG. The embedded image makes the file large; that is expected.
5. For a vector base (SVG), read its XML and reuse its coordinate system; do not trace it either.

## OUTPUT
- Single self-contained SVG (inline `<style>` preferred; classes for `label`, `plabel`, `axis`, `tick`, `dashed`, `point`).
  - proper contrast with background
- Valid XML, closed tags, quoted attributes, no truncated output.
