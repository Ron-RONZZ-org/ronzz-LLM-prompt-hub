## RECIPES — vector illustrations

### Monochrome icon (24×24)

Use a 24-unit grid, a 1-unit padding, 2-unit strokes, round caps and joins, and
`currentColor` so the icon inherits the page colour.

```python
import xml.etree.ElementTree as ET
from pathlib import Path

SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
root = ET.Element(f"{{{SVG}}}svg", {
    "viewBox": "0 0 24 24", "width": "24", "height": "24",
    "role": "img", "aria-label": "Document with a plus sign",
})
ET.SubElement(root, "title").text = "Document with a plus sign"
style = ET.SubElement(root, "style")
style.text = (
    ".line{fill:none;stroke:currentColor;stroke-width:2;"
    "stroke-linecap:round;stroke-linejoin:round}"
)
ET.SubElement(root, "path", {"class": "line",
    "d": "M6 3h9l4 4v14H6z M15 3v4h4 M12 12v6 M9 15h6"})
out = Path(UPLOAD_DIR) / "document-add.svg"
ET.ElementTree(root).write(out, encoding="utf-8", xml_declaration=True)
print(out)
```

- Snap coordinates to 0.5 units; keep the drawing inside a 1-unit padding.
- Do not add text to an icon; the accessible name goes in `<title>`.
- Do not scale stroke widths with the canvas; keep them at 2 units on a 24-unit
  grid, 3–4 units on a 64-unit grid.

### Pictogram or illustration

- Use a 64×64 or 128×128 grid for a pictogram; 800×600 or a square for an
  illustration.
- Use flat fills from a small palette (`#1f4e79`, `#b45309`, `#2e7d6f`, `#909090`)
  or a single ink colour; no gradients, shadows, or 3-D effects unless requested.
- Build repeated elements from one shape and a loop; do not copy coordinates by
  hand.
- Keep a margin of at least 5 % of the canvas on every side.

### Annotated image overlay

The supplied image is the artwork; do not redraw or trace it.

1. Find the file in `ATTACHMENTS` by name. If it is missing, ask the user to
   re-attach it.
2. Read its pixel size with `PIL.Image.open(path).size`; set the SVG `viewBox` to
   `0 0 width height` (or scale both by the same factor).
3. Embed the bytes as a data URI:

   ```python
   import base64
   data = base64.b64encode(Path(path).read_bytes()).decode()
   # <image href="data:image/png;base64,{data}" x="0" y="0" width="{w}" height="{h}"/>
   ```

4. Add only the requested labels, arrows, or axes; place them from the image
   dimensions. If you cannot inspect the image, ask for the positions.

### Audit before presenting

- Every element lies inside the viewBox; no clipped stroke or label.
- Labels do not overlap each other or the artwork; use a leader line when a
  label must sit away from its target.
- Text is real text, not paths; the file is valid XML with closed tags.
- The SVG is self-contained; no external font, image, or stylesheet.
- Save the final file under `UPLOAD_DIR` and pass it in `files_to_save`.
