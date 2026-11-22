## RECIPES — matplotlib in `execute_code`

Use one `execute_code` call. Write the PNG preview and the SVG artifact under
`UPLOAD_DIR`, and pass both in `files_to_save`.

### Shared setup

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

INK, MUTED, GRID = "#1a1a1a", "#4a4a4a", "#dcdcdc"
PALETTE = ["#1f4e79", "#b45309", "#c55a11", "#2e7d6f", "#909090"]
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "Liberation Serif", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "text.color": INK,
    "axes.labelcolor": INK,
    "axes.edgecolor": INK,
    "axes.linewidth": 0.8,
    "xtick.color": INK,
    "ytick.color": INK,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "grid.linestyle": "-",
    "svg.fonttype": "none",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})
```

### 95 % CI helper

```python
from scipy.stats import t

def ci95(mean, sd, n):
    half = t.ppf(0.975, n - 1) * sd / np.sqrt(n)
    return mean - half, mean + half
```

If the source gives the CI bounds and `n`, plot them directly; do not recompute
from a guessed standard deviation.

### Grouped dot-and-whisker

```python
groups = ["High", "Low", "Control"]
series = ["Evaluation", "No evaluation"]
means = np.array([[28.40, 28.40], [37.90, 21.11], [28.40, 20.00]])
lo = np.array([[22.08, 24.51], [28.68, 15.09], [20.93, 15.18]])
hi = np.array([[34.72, 32.29], [47.12, 27.13], [35.87, 24.82]])
ns = np.array([[17, 16], [16, 17], [19, 18]])

fig, ax = plt.subplots(figsize=(800 / 72, 584 / 72))
x = np.arange(len(groups))
offsets = (np.arange(len(series)) - (len(series) - 1) / 2) * 0.18
for i, group in enumerate(groups):
    ax.axvline(i, color="#f0f0f0", lw=0.6, zorder=0)
for j, label in enumerate(series):
    xs = x + offsets[j]
    ax.errorbar(
        xs, means[:, j], yerr=[means[:, j] - lo[:, j], hi[:, j] - means[:, j]],
        fmt="o", ms=5, mfc=PALETTE[j], mec="white", mew=0.8,
        ecolor=PALETTE[j], elinewidth=2.2, capsize=5, capthick=2.2,
        label=label, zorder=3,
    )
    for xi, n in zip(xs, ns[:, j]):
        ax.text(xi, -0.055, f"n = {n}", transform=ax.get_xaxis_transform(),
                ha="center", va="top", fontsize=9.5, color=MUTED)

ax.set_xticks(x, groups)
ax.set_xlim(-0.55, len(groups) - 0.45)
ax.set_ylim(0, 50)
ax.set_xlabel("Instrumentality", fontsize=12, labelpad=24)
ax.set_ylabel("Mean maximum number of uses identified", fontsize=12)
ax.set_title("Mean maximum number of uses identified, by instrumentality and evaluation "
             "(based on Shepperd & Taylor (1999))", loc="left", fontsize=12.5, pad=12)
ax.legend(frameon=False, loc="upper left", fontsize=10)
fig.subplots_adjust(left=0.12, right=0.98, top=0.90, bottom=0.28)
```

### Bars with 95 % CI

```python
conditions = ["I\nDiscussion, 4 and 5", "II\nDiscussion, 3",
              "III\nInformation exchange", "Control\nno discussion"]
means = np.array([6.15, 0.86, 1.91, 0.04])
lo = np.array([4.10, -1.05, 1.30, -0.05])
hi = np.array([8.20, 2.75, 2.50, 0.13])
pvals = ["p = .00013", "p = .457", "p = .0206", "reference"]

fig, ax = plt.subplots(figsize=(720 / 72, 375 / 72))
x = np.arange(len(conditions))
colors = [PALETTE[i % len(PALETTE)] for i in range(len(conditions))]
ax.bar(x, means, width=0.6, color=colors, zorder=2)
ax.errorbar(x, means, yerr=[means - lo, hi - means], fmt="none",
            ecolor=INK, elinewidth=2.1, capsize=6, capthick=2.1, zorder=3)
ax.hlines(means, x - 0.3, x + 0.3, color=INK, lw=2.1, zorder=3)
ax.axhline(0, color="#333333", lw=1.3, zorder=1)
for xi, p in zip(x, pvals):
    ax.text(xi, -0.20, p, transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=8.5, style="italic", color=MUTED)

ax.set_xticks(x, conditions)
ax.set_ylabel("Mean shift", fontsize=11)
ax.set_title("Mean shift in group risk taking, by condition "
             "(based on Teger & Pruitt (1967))", loc="left", fontsize=11, pad=12)
fig.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.32)
```

### Line with 95 % CI ribbon

```python
x = np.linspace(0, 10, 100)
mean = np.sin(x)
lo, hi = mean - 0.15, mean + 0.15

fig, ax = plt.subplots(figsize=(720 / 72, 375 / 72))
ax.fill_between(x, lo, hi, color=PALETTE[0], alpha=0.18, linewidth=0)
ax.plot(x, mean, color=PALETTE[0], lw=1.6)
ax.set_xlabel("$t$ / s")
ax.set_ylabel("$y$")
ax.set_title("Example series (based on Author (Year))", loc="left", fontsize=11, pad=12)
fig.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.30)
```

### Footer

```python
import textwrap
footer = textwrap.fill(
    "Data source: Shepperd, J. A., & Taylor, K. M. (1999). Social loafing and "
    "expectancy-value theory. Personality and Social Psychology Bulletin, 25(9), "
    "1147-1158. https://doi.org/10.1177/01461672992512008", width=105)
footer += "\nRonzzWikiBase: https://wikibase.ronzz.org/wiki/Source:Shepperd-Taylor-1999"
fig.text(0.01, 0.01, footer, ha="left", va="bottom", fontsize=8.5, color=MUTED)
```

Keep the notes above the footer as short as possible; put full method details on
the File page, not in the figure.

### Saving

```python
out = Path(UPLOAD_DIR)
png, svg = out / "plot.png", out / "plot.svg"
fig.savefig(png, dpi=200)
fig.savefig(svg, format="svg")
print(png, svg)
```

Place the footer before saving. Do **not** pass `bbox_inches="tight"` when you
want the exact 800×584 or 720×375 canvas; control the margins with
`fig.subplots_adjust` instead.

Then call `execute_code` with `files_to_save=[str(png), str(svg)]`.
