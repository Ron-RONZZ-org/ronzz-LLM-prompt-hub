### Katex math requirements

- Use $...$/$$...$$ delimiters
 - $$ should occupy its own line
- Avoid using $'$ for for particular value of a variable to avoid ambiguity
  - use $_1$, $_2$...
- Use $\dot{}$, $\ddot{}$, ... for derivatives

GOOD:
```
$$
\Phi(\mathbf r_1)=-G\int\frac{\rho(\mathbf r)}{|\mathbf r_1-\mathbf r|}d^3r_1
$$

$\ddot{\mathbf r}=-G(M+m)\frac{\mathbf r}{r^3}$
```

BAD:
```
$$\Phi(\mathbf r)
=-G\int\frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}d^3r'$$
```

- Use $\vec u$ for vectors and $\mathbf{M}$ for matrices, not simply $u$ or $M$ for clarity

- Use ${}$

GOOD:
```
\mathbf{r}
```

BAD:
```
\mathbf r
```

- Use cases for parallel equations

GOOD:
```
$$
\begin{cases}
\ddot{\mathbf{r}}_m=-GM\frac{\mathbf{r}}{r^3} \text{ (1)/m} \\
\ddot{\mathbf{r}}_M=+Gm\frac{\mathbf{r}}{r^3} \text{ (2)/M}
\end{cases}
$$
```

BAD:
```
$$
\ddot{\mathbf{r}}_m=-GM\frac{\mathbf{r}}{r^3} \text{ (1)/m} \\
\ddot{\mathbf{r}}_M=+Gm\frac{\mathbf{r}}{r^3} \text{ (2)/M}
$$

- Use symbolic language whenever possible

GOOD:
```
$$\exists a \in B$$
```

BAD:
```
There exists $a$ in $B$
```

- to emphasise multiple variables all have a value $a$, use , to separate the variables

GOOD:
```
$$
c_1, c_2, \cdots, c_n = 0.
$$

BAD:
```
c_1 = c_2 = \cdots = c_n = 0.
```
- strip any $\boxed$

- leave a blank line between explanatory text and katex

GOOD:
```
Let $j=\pi(i)$,

$$
\prod_{i=1}^n b_{\pi(i),\sigma(i)}
=
\prod_{j=1}^n b_{j,\rho(j)}.
$$
```

BAD:
```
Let $j=\pi(i)$,
$$
\prod_{i=1}^n b_{\pi(i),\sigma(i)}
=
\prod_{j=1}^n b_{j,\rho(j)}.
$$
```
