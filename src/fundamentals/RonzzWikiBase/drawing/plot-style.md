## PLOT STYLE — ronzz.ORG scientific figures

Reference figures (follow them):

- [[File:Social-Loafing-Expectancy-Value-95CI.svg]] — grouped dot-and-whisker, two series, `n` labels.
- [[File:Teger-Pruitt-1967-Group-Risk-Shift-Mean-95CI.svg]] — bars with 95 % CI, zero line, `p` values.

### Canvas, type, colour

- White background; no frame, shadow, gradient, 3-D effect, or chartjunk.
- Serif only: `'Times New Roman', Times, 'Liberation Serif', serif`.
- Ink `#1a1a1a`; secondary `#4a4a4a`; grid `#dcdcdc`; zero/reference line `#333333`.
- Series palette in order: `#1f4e79` navy, `#b45309` amber, `#c55a11` orange, `#2e7d6f` teal, `#909090` grey. Never a rainbow. Pair colour with a marker or hatch so the figure survives greyscale.
- Keep text as text in the SVG (`svg.fonttype = "none"`); one serif family; at most three sizes per figure. Title 10.5–14 px, axis labels 10.5–14 px, tick labels 12–16 px, annotations 9–12 px.

### Axes and grid

- Left and bottom spines only, 0.5–1.0 pt, square caps. Ticks outward; no minor labels.
- Horizontal major grid only, `#dcdcdc`, 0.4–0.6 pt. No vertical grid; a vertical guide `#f0f0f0` may separate groups.
- Axis labels carry units. Use the typographic minus `−`, not `-`.
- Draw a zero/reference line `#333333`, 1.2–1.4 pt, when values can be negative.

### Statistical marks

- Mean: filled circle, radius 0.28–0.32 % of canvas width, white stroke 0.5–0.9 pt; or a bar from zero.
- 95 % CI: vertical whisker in the series colour, 2.1–2.6 pt; caps 1.7× the marker diameter, same thickness.
- Dot-and-whisker for means; bars for magnitudes; line + ribbon for continuous series.
- Error bars are 95 % CI unless the caption says otherwise. Compute with `scipy.stats.t.ppf(0.975, df)`; `df = n − 1` for one sample, Welch–Satterthwaite for two samples.
- Bars start at zero; draw the zero line when values can be negative. Never truncate a bar axis.
- No error bar on a single observation; write `n = 1`.
- Do not connect categorical means with a line unless the categories are ordered.

### Title, notes, provenance

- Title: `{plot content} (based on {Author (Year)})`. One line; wrap only if unavoidable. Example: `Mean maximum number of uses identified, by instrumentality and evaluation (based on Shepperd & Taylor (1999))`.
- `n = …` under each category or point, grey, brief.
- `p` values italic under the category label, only when computed; give the test and `df` in the notes.
- Notes: as brief as possible. One line for the method, for example `Bars: mean; whiskers: 95 % CI (t, df = 9); n = 10 per condition.` No paragraphs.
- Footer, grey `#4a4a4a`, 9–12 px, below the plot:
  1. `Data source: {APA 7 reference with DOI}`. Example: `Data source: Shepperd, J. A., & Taylor, K. M. (1999). Social loafing and expectancy-value theory. Personality and Social Psychology Bulletin, 25(9), 1147–1158. https://doi.org/10.1177/01461672992512008`
  2. `RonzzWikiBase: {Source: page URL}`. Resolve the citation source; never invent a Q-id, page title, or URL. If the source has no `Source:` page, ask the user to create it with the Bibliographer before uploading.
- If the user did not supply a citable source, ask for it before uploading. A plot with no source is incomplete.
- Add `<title>` and `role="img"`/`aria-label` with the title and a one-sentence description.

### Size and output

- Single panel 720×375 or 800×584; grouped 800×584. Keep margins consistent.
- Save a PNG preview (200 dpi) and the SVG artifact under `UPLOAD_DIR`; list both in `files_to_save`. Upload only the SVG.
