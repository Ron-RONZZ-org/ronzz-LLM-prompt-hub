### IMPORTANT: think of reader

- primary reader: non-math-major engineers looking to consolidate their math
- academic register
- concise language
- minimise technical jargons
- focus on core concept and basic applications
- do not try to include everything

### Show, don't tell

- demonstrate with math, not words
  - NO blabla about what readers can see for themselves in the math demonstrations.
  - NO empty metacomments

#### GOOD

```wikitext
== Mathematical definition ==

Let $V$ be a vector space over $\mathbb{F}$.

Map

$$
\begin{aligned} 
\langle \cdot, \cdot \rangle : V \times V \to \mathbb{F}\\
\quad (u, v) \mapsto \langle u, v \rangle
\end{aligned}
$$

is an '''inner product''' on $V$ if 4 conditions are satisfied:

* '''Linearity in the 1st slot''': $\forall (u, v, w \in V, a \in \mathbb{F}), \langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$ and $\langle au, v \rangle = a \langle u, v \rangle$
* '''Definiteness''': $\langle v, v \rangle = 0 \iff v = \vec 0$.
* '''Positivity''': $\forall v \in V, v \neq \vec 0, \langle v, v \rangle > 0$
* '''Conjugate symmetry''': $\forall u, v \in V, \langle u, v \rangle = \overline{\langle v, u \rangle}$.

<blockquote>
Recall:

$$\forall x\in\mathbb{R},\; x=\overline{x}$$

Hence, for real vector spaces, conjugate symmetry of an inner product becomes actual symmetry.
</blockquote>

<blockquote>
'''Warning''': confusingly, the convention in physics is often the exact opposite: an inner product is linear in the second slot and anti-linear in the first slot.
</blockquote>
```

#### BAD

```wikitext
Most laws of nature are stated as rules about how quantities change, so differential equations appear throughout science and engineering: the swinging of a pendulum, the cooling of a hot drink, the growth of a population, and the discharge of a capacitor are all described by differential equations. This article explains what a differential equation is and how equations are classified, then works through the most common exact methods of solution, each illustrated by a concrete numerical example that needs no background knowledge beyond school algebra. It treats '''ordinary differential equations''' (ODEs), in which the unknown function depends on a single independent variable, in the most detail, and gives shorter accounts of '''partial differential equations''' (PDEs) and of the numerical, series, and qualitative methods used when no exact formula exists.
```

(full of useless ramble and metacomments)

### show derivation

- multiplication/division of both sides, algebraic manipulation, etc.

### discuss case-by-case

- do not confound different cases meriting different solution approaches/having different properties together

#### GOOD

- discuss differential equations in general in a page (definition/classification/general solution strategies: algebraic manipulation/numerical solution), then link to separate pages discussing ordinary differential equations and partial differential equations (definitions), which then links to pages discussing first order ordinary differential equation (general form, specific solution methods unique to 1st order ODE), 2nd order ...

### definition > example

- always begin discussion with abstract general-case definitions
- then provide concrete examples

### Do NOT duplicate

- When a topic is already treated in a separate article, simply link to that article. No extra explanation.

### Good examples to imitate

- https://wikibase.ronzz.org/wiki/Ring_(mathematical_concept)
- https://wikibase.ronzz.org/wiki/Vector_space


