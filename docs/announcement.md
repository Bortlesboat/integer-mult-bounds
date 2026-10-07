# Draft announcement

I have prepared a reproducible parameter improvement to OpenAI's integer
multiplication manuscript (#109). Conditional on its algorithmic interfaces
and the audited construction changes, the bound becomes

$$
T(n)=O\!\left(n(\log n)^{1-\kappa}\right),\qquad
\kappa=5.8\times10^{-33},
$$

with `2^-108 < kappa < 2^-107`, compared with the manuscript's `2^-182`.
The improvement uses a smaller instance of the same finite-network
construction, sharper rational parameters, and a generalized recursion
stopping threshold. It does not require a new conceptual multiplication
algorithm.

The repository includes a research note, exact rational certificates,
patches against a pinned upstream revision, and a dependency audit. It also
bounds the stated parameter family's ceiling by `kappa < 5.838e-33`; the
supplied witness exceeds 99% of that bound.

This is an asymptotic exponent improvement, not a practical performance claim
or an independent proof of the underlying multiplication theorem. I welcome
independent mathematical review, especially of the network interfaces and
fixed-tape recurrence. The work was prepared with assistance from OpenAI Codex.

— Douglas Colkitt

[Repository](https://github.com/CrocSwap/integer-mult-bounds) ·
[Research note](https://github.com/CrocSwap/integer-mult-bounds/blob/main/artifacts/parameter-note.pdf)
