## TASK

Turn the data below into one publication-quality statistical plot in the
ronzz.ORG house style. Present it, iterate until the user is satisfied, and on
validation upload the SVG to RonzzWikiBase and reply with `[[File:<name>.svg]]`.

## SCOPE

- This command is for **data plots**: distributions, means with 95 % CI, bars,
  dot-and-whisker, series with a CI ribbon, grouped comparisons.
- For an icon or vector illustration, use `/svg-ronzzwikibase`.
- For a UML/PlantUML/GraphViz/Mermaid diagram, use
  `/make-mediawiki-plantuml-diagram`.
- Never invent a data point, a mean, a CI, a `p` value, or an `n`. If the data
  is missing a column, unit, or sample size, ask one short question.

## DATA

{{data}}

## NOTES

{{notes}}

{{include:chat-file-tools}}

{{include:RonzzWikiBase/drawing/plot-style}}

{{include:RonzzWikiBase/drawing/plot-recipes}}

{{include:RonzzWikiBase/drawing/plot-tools}}

## OUTPUT

Present the raster with one short sentence. On validation, upload the SVG per
UPLOAD TO RONZZWIKIBASE and reply with `[[File:<name>.svg]]` and nothing else.
If `execute_code` is unavailable, stop and say the request must be resent once
it is back.
