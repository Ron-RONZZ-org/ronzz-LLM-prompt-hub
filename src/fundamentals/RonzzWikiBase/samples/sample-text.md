```wikitext
[[Category:Inner product space]]
'''Orthogonality''' generalises perpendicularity to an [[inner product space]].

== Mathematical definition ==

Let $V$ be an [[inner product space]].

If for $u,v\in V$ 

$$\langle \vec u , \vec v  \rangle=0$$

Then $\vec u,\vec v$ are '''orthogonal''' to each other.

$\vec u \bot \vec v $ denotes this orthogonality.

== Application ==

=== Orthogonal decomposition ===

Given vectors $\vec u,\vec v \in V$ and $\vec v \neq 0$, $\vec u$ can be uniquely decomposed into two pieces: one parallel to $\vec v$ and one orthogonal to $\vec v$. This is called an '''orthogonal decomposition'''.

In mathematical terms:

$$\vec u=\vec u_ 1+\vec u_ 2,$$

Where $\vec u_ 1=a \vec v , a \in \mathbb{F}; \vec u _2\bot \vec v $

'''Derivation:'''

$$
\because \vec u  = \vec u _1 +\vec u_ 2 \\
\therefore \vec u _2= \vec u -\vec u_ 1= \vec u -a\vec v \\
\because \vec u _2 \bot \vec v  \\
\therefore \langle \vec u _2, \vec v  \rangle = \langle \vec u - a\vec v, \vec v  \rangle = \langle \vec u , \vec v  \rangle - a \left\| \vec v  \right\|^2 = \vec 0 \\
\text{Solve for }a,a = \frac{\langle \vec u , \vec v  \rangle}{\left\| \vec v  \right\|^2} \\
\text{Substitute back into }\vec u_ 1=a \vec v, \vec u _2= \vec u -a\vec v, \\
u=\frac{\langle \vec u , \vec v  \rangle}{\| \vec v  \|^2} \vec v  + \left( \vec u -\frac{\langle \vec u , \vec v  \rangle}{\| \vec v  \|^2} \vec v  \right)
$$

== Properties ==

=== $\vec 0$ is orthogonal to every $\vec v$ ===

$$
\forall \vec v  \in \vec v , \vec 0 \bot \vec v 
$$

{{Hidden proof}}
Recall [[Vector_space#Mathematical_definition|the properties of a \vec v ector space by definition]]. By additive identity, 

$$
\vec 0 +\vec 0 = \vec 0
$$

Therefore,

$$
\langle \vec 0, \vec u  \rangle = \langle \vec 0+\vec 0, \vec u \rangle
$$

Recall the [[inner product|properties of the inner product by definition]], by linearity in the 1st slot,

$$
\langle \vec 0+\vec 0, \vec u \rangle = \langle\vec 0, \vec u  \rangle+\langle \vec 0, \vec u \rangle
$$

Subtracting $\langle \vec 0, \vec u \rangle$ from both sides gives

$$
\langle \vec 0, \vec u  \rangle=0.
$$
{{End hidden}}

=== Generalised Pythagorean theorem === 

''If'' $u,v\in V; \vec u \bot \vec v $, then $\| \cdot \|$ defined by $\| \vec v  \|:=\sqrt{\langle \vec v , \vec v  \rangle}$ obeys

$$\| \vec u + \vec v  \|^2 = \| \vec u  \|^2 + \| \vec v  \|^2.$$

{{Hidden proof}}
By definition,

$$
\| \vec u + \vec v  \|^2 = \langle \vec u + \vec v , \vec u + \vec v  \rangle
$$

Recall the [[inner product|properties of the inner product by definition]]:

By linearity in the 1st slot,

$$
\langle \vec u + \vec v , \vec u + \vec v  \rangle = \langle \vec u , \vec u + \vec v  \rangle + \langle \vec v , \vec u + \vec v  \rangle
$$

By conjugate symmetry,

$$
\langle \vec u , \vec u + \vec v  \rangle + \langle \vec u , \vec u + \vec v  \rangle = \overline{\langle \vec u + \vec v , \vec u  \rangle} + \overline{\langle \vec u + \vec v , \vec v  \rangle}
$$

Again by linearity in the first slot,

$$
\overline{\langle \vec u + \vec v , \vec u  \rangle} + \overline{\langle \vec u + \vec v , \vec v  \rangle}=\overline{\langle \vec u , \vec u  \rangle} + \overline{\langle \vec v , \vec u  \rangle} + \overline{\langle \vec u , \vec v  \rangle} + \overline{\langle \vec v , \vec v  \rangle}
$$

Again by conjugate symmetry,

$$
\overline{\langle \vec u , \vec u  \rangle} + \overline{\langle \vec v , \vec u  \rangle} + \overline{\langle \vec u , \vec v  \rangle} + \overline{\langle \vec v , \vec v  \rangle} = \langle \vec u , \vec u  \rangle + \langle \vec u , \vec v  \rangle + \langle \vec v , \vec u  \rangle + \langle \vec v , \vec v  \rangle
$$

since $u,v\in \vec v ; \vec u \bot \vec v $:

$$
\langle \vec u , \vec v  \rangle=0;\langle \vec v , \vec u  \rangle=0
$$

By definition

$$
\langle \vec u , \vec u  \rangle=\left\| \vec u  \right\|^2;\langle \vec v , \vec v  \rangle=\left\| \vec v  \right\|^2
$$

Hence

$$\| \vec u + \vec v  \|^2 = \| \vec u  \|^2 + \| \vec v  \|^2.$$
{{End hidden}}
```
