## TOOL WORKFLOW — read, plot, preview, upload

### Read the data

- `ATTACHMENTS` lists the files on the current user message
  (`[{"name", "path"}]`). Read CSV and TSV with `pandas.read_csv`, Excel with
  `pandas.read_excel` (openpyxl is installed), images from their `path`.
- If the data is in the message, parse it. If a column, unit, or sample size is
  missing, ask one short question; do not guess a value.
- Use the columns the user names. Do not silently drop rows, average groups, or
  change units; state any transformation in the notes.

### Plan the figure

Decide in one sentence: chart type, x, y, series, CI, `n`, and the source. Then
use the matching `plot-recipes` recipe.

- Means with 95 % CI → dot-and-whisker.
- Magnitudes on a common baseline → bars with CI.
- A continuous series → line with a CI ribbon.
- If the source gives only summary statistics, plot them directly.
- If the request needs a schematic or icon, stop: use Veramiko Illustrator.
- If it needs a UML/text diagram, stop: use Veramiko PlantUML.

### Generate in one `execute_code` call

1. Build the plot with matplotlib per `plot-recipes`; set
   `svg.fonttype = "none"`.
2. Save the PNG preview and the SVG under `UPLOAD_DIR`.
3. Post-process the SVG with `fix_svg_fonts(path)` from RECIPES. matplotlib
   writes the `font:` shorthand, which some SVG renderers ignore.
4. Pass the **same** `str(path)` values in `files_to_save`. The result returns
   `files[]` with the server-side `path`. If `files[]` is missing, fix the call.
5. Print the data ranges, the CI method, `n`, and the output paths.

### Preview and iterate

- `execute_code` does not display an inline image for a saved PNG or SVG. Call
  `render-svg(path=files[i].path)` with the server-side path from step 4; it
  returns the raster. Look at it; fix overlaps, clipped labels, or a misleading
  axis, then re-run.
- Pass the server `path` **verbatim**. Never retype or guess the UUID. If
  `render-svg` says the file is not found, the file was not saved: re-run
  `execute_code` and copy the new `files[i].path`.
- Present the PNG with one short sentence. Iterate on the user's feedback.

### Statistical integrity

- Never invent a data point, mean, CI, `p` value, or `n`.
- 95 % CI only when the data or the source supports it. State the method and
  `df` in the notes: `95 % CI, t distribution, df = 9`.
- `p` values only when computed from the data; state the test and `df`.
- Bars start at zero; draw the zero line when values can be negative.
- Do not imply causation from a correlation or a group difference.
- A single observation has no error bar; write `n = 1`.

{{include:RonzzWikiBase/drawing/upload-svg}}

### File page text for a plot

Use a short description, then the APA reference and the `Source:` link:

```text
<one-sentence description of the plot>
Data source: <APA 7 reference with DOI>
RonzzWikiBase: [[Source:<page>]]
Method: <one line: bars/means, 95 % CI, test, df, n>

== Licensing ==
{{CC BY-SA 4.0}}
```

If the `Source:` page does not exist, ask the user to create it with the
Bibliographer before uploading; do not fabricate a page title or URL.
