## RECIPES — known-good starting points

Each snippet is a complete `render_diagram(diagram_type="tikz", …)` `code` argument. Change the content, keep the preamble lines.

### Annotated function plot (pgfplots + units)

```latex
\usepackage{siunitx}
\begin{tikzpicture}
\begin{axis}[width=8cm,height=5cm,xlabel={$t$ (\si{\second})},
  ylabel={$v$ (\si{\metre\per\second})},grid=major]
\addplot[thick,blue,domain=0:5,samples=60]{2*x};
\end{axis}
\end{tikzpicture}
```

### Free-body diagram

```latex
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[font=\small,>=Stealth]
\fill[gray!15] (-0.5,0) -- (5.5,0) -- (5.5,-0.4) -- (-0.5,-0.4) -- cycle;
\draw[thick] (0,0) -- (5,0);
\draw[thick,rotate around={20:(2.5,0.55)}] (0.7,0.55) rectangle (4.3,1.1);
\draw[->,very thick,red] (2.5,0.8) -- ++(0,-1.6) node[below]{$m\vec{g}$};
\draw[->,very thick,blue] (2.5,0.8) -- ++(1.8,0) node[right]{$\vec{N}$};
\draw[->,very thick,orange] (2.5,0.8) -- ++(-1.4,-0.5) node[left]{$\vec{f}$};
\end{tikzpicture}
```

### Ray optics (thin lens)

```latex
\begin{tikzpicture}[font=\small]
\draw[thick] (0,-1.6) -- (0,1.6);
\draw[->] (-5,0) -- (5,0) node[right]{optical axis};
\foreach \y in {-1.2,-0.6,0.6,1.2} \draw[->,red] (-5,\y) -- (0,\y);
\foreach \y in {-1.2,-0.6,0.6,1.2} \draw[->,red] (0,\y) -- (3.2,0);
\fill (3.2,0) circle (2pt) node[below]{$F'$};
\end{tikzpicture}
```

### Circuit (circuitikz)

```latex
\usepackage{circuitikz}
\begin{circuitikz}[font=\small]
\draw (0,0) to[battery1, l=$V$] (0,2) to[R=$R_1$] (2,2) to[C=$C$] (2,0) -- (0,0);
\draw (2,2) to[L=$L$, *-*] (4,2) -- (4,0) -- (2,0);
\end{circuitikz}
```

### Chemistry: structure scheme and reaction equation

```latex
\usepackage{chemfig}
\usepackage{mhchem}
\begin{tikzpicture}[font=\small]
\node at (0,0) {\chemfig{*6(-=-(-OH)=-=)}};
\node at (4,0) {\chemfig{*6(-=-(-NO_2)=-=)}};
\draw[->,thick] (1.1,0) -- node[above]{HNO$_3$} (2.9,0);
\node at (2,-1.6) {$\ce{C6H5OH + HNO3 -> C6H4(NO2)OH + H2O}$};
\end{tikzpicture}
```

### Feynman vertex (tikz-feynhand, not tikz-feynman)

```latex
\usepackage{tikz-feynhand}
\begin{tikzpicture}[font=\small]
\begin{feynhand}
\vertex (a) at (-1.5,0) {\(e^-\)};
\vertex (b) at (1.5,0) {\(e^-\)};
\vertex (c) at (0,1.2) {\(\gamma\)};
\propag[fer] (a) to (c);
\propag[fer] (c) to (b);
\end{feynhand}
\end{tikzpicture}
```

### Molecular orbital diagram (modiagram)

`\atom` takes `[name]{left|right}{configuration}`; each shell is `n l = electrons ; pairing`.

```latex
\usepackage{modiagram}
\begin{MOdiagram}
\atom[O]{left}{1s=2;pair,2s=2;pair,2p=3}
\end{MOdiagram}
```

### Data figure (matplotlib, in `execute_code`)

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

matplotlib.rcParams["text.usetex"] = True  # LaTeX is installed in the sandbox
x = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(4, 2.6))
ax.plot(x, np.sin(x), label=r"$\sin x$")
ax.set_xlabel(r"$x$ / rad")
ax.set_ylabel(r"$y$")
ax.legend(frameon=False)
fig.tight_layout()

out = Path(UPLOAD_DIR)  # defined by the interpreter preamble
png, svg = out / "sine.png", out / "sine.svg"
fig.savefig(png, dpi=200)
fig.savefig(svg, format="svg")
print(png, svg)
```

Then pass `files_to_save=[str(png), str(svg)]` on the same `execute_code` call.
