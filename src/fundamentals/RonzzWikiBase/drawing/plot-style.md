## PLOT STYLE — ronzz.ORG scientific figures

Reference figures (follow them):

- [[File:Social-Loafing-Expectancy-Value-95CI.svg]] — grouped dot-and-whisker, two series, `n` labels.
- [[File:Teger-Pruitt-1967-Group-Risk-Shift-Mean-95CI.svg]] — bars with 95 % CI, zero line, `p` values.

### Canvas, type, colour

- White background; no frame, shadow, gradient, 3-D effect, or chartjunk.
- Serif only: `'Times New Roman', Times, 'Liberation Serif', serif`.
- Ink `#1a1a1a`; secondary `#4a4a4a`; grid `#dcdcdc`; zero/reference line `#333333`.
- Series palette in order: `#1f4e79` navy, `#b45309` amber, `#c55a11` orange, `#2e7d6f` teal, `#909090` grey. Pair colour with a marker or hatch so the figure survives greyscale.
- Keep text as text (`svg.fonttype = "none"`) and emit explicit `font-family`/`font-size` CSS. matplotlib writes a `font:` shorthand that some SVG renderers ignore; see TOOL WORKFLOW.
- Type sizes in points: title 12.5, axis labels 11, tick labels 10, annotations 8.5–9.5. At most three sizes per figure.

### Axes and grid

- Left and bottom spines only, 0.8 pt; ticks outward.
- Horizontal major grid only, `#dcdcdc`, 0.6 pt. No vertical grid; a vertical guide `#f0f0f0` may separate groups.
- Axis labels carry units. Use the typographic minus `−` (U+2212).
- Draw a zero/reference line `#333333`, 1.3 pt, when values can be negative.

### Statistical marks

- Means: a filled circle marker 5–6 pt with a white stroke, or a bar from zero.
- 95 % CI: whisker 2.1–2.6 pt; cap 5–6 pt.
- Dot-and-whisker for means; bars for magnitudes; line + ribbon for continuous series.
- Error bars are 95 % CI unless the caption says otherwise. Compute with `scipy.stats.t.ppf(0.975, df)`; `df = n − 1` for one sample, Welch–Satterthwaite for two samples.
- Bars start at zero; never truncate a bar axis. Do not connect categorical means with a line unless the categories are ordered.
- No error bar on a single observation; write `n = 1`.

### Title, notes, provenance

- Default title: `{plot content} (based on {Author (Year)})`, one line. Example: `Mean maximum number of uses identified, by instrumentality and evaluation (based on Shepperd & Taylor (1999))`.
- `n = …` under each category or point, grey, brief.
- `p` values italic under the category label, only when computed; give the test and `df` in the notes.
- Notes: one line. Example: `Bars: mean; whiskers: 95 % CI (t, df = 9); n = 10 per condition.`
- Footer, grey `#4a4a4a`, 8–9 pt, below the plot:
  1. `Data source: {APA 7 reference with DOI}`.
  2. `RonzzWikiBase: {the Source: page URL you resolved}`. Never invent a Q-id, page title, or URL. If the source has no `Source:` page, ask the user to create it with the Bibliographer.
- **A user instruction overrides this section.** If the user says the caption lives on the wiki page, omit the in-figure title and footer; do not debate it.
- Add `<title>` and `role="img"`/`aria-label` with the title and a one-sentence description.

### Size and output

- Single panel 720×375 or 800×584 pt; grouped 800×584 pt. Keep margins consistent; control them with `fig.subplots_adjust`, not `bbox_inches="tight"`.
- Save a PNG preview at 200 dpi and the SVG under `UPLOAD_DIR`; list both in `files_to_save`. Upload only the SVG unless the user asks for another format.
