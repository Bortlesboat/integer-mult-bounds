# Sharing across common-point groups

The new conditional witness is **kappa = 13 * 2^-66**, a factor **13/8**
above 2^-63. It uses 531,870 side roles instead of 577,576. This is a modest
refinement; no exponent in the 50s is established.

The more useful development is a general reverse-frame argument. If U_z is
the nondegenerate source span at a forward node, assign its orthogonal
complement to that node in the reversed computation. Forward inclusion
U_z <= U_w becomes reverse inclusion U_w^perp <= U_z^perp. Output
orthogonality supplies the starting target line, and the original input
ends at exactly its source-line complement. Reachable-target spans no longer
need a common point or a positivity argument.

This does not remove the need to prove nondegeneracy of every source span.
In this construction each retained sum comes from an original common-point
circuit, so the old positive-definiteness proof still applies. The ambient
form is nondegenerate at h=46. Equal scalar values by themselves would not
justify merging arbitrary gates or simultaneously occupied physical slots.

See the [proof note](../../notes/shared-point-note.tex),
[PDF](../../artifacts/shared-point-note.pdf),
[full source patch](../../patches/h46-shared-point.patch), and
[exact certificate](../../certificates/shared-point-network.json).

## Construction and validation

Identify equal inputs and equal intermediate supports across the 46 copies of
the pair-exclusion circuit. A sum occurring in different groups i and j must
be a pair-star: every source triple contains both points. Its fixed pair and
variable vertices determine its support exactly. Keep the first decomposition,
prune unused nodes, and compile the reversible roles afresh.

There are 486,330 additions and 45,540 designated partial outputs, so the
c+q embedding uses 531,870 roles. All three partial outputs for a physical
target are injected into that target. Since neighbors have a unique common
point, the combined side matrix remains the intersection-one matrix.

Every addition and output is checked exactly using local pair coordinates;
the checker expands a shared pair-star into the receiving group's coordinates.
It checks both directions of frame nesting on every compiled role. Independent
small global expansions check all coefficients, and full input-basis tests
check forward and reversed invocations with arbitrary dirty scratch. A complete
small three-stage model checks bank exchange with shared auxiliary banks.

At h=46, the exact counts are

    W = 252137288620800
    s = 24542034552800107200
    Wm-s = 572394081600
    eta = 27/1157655136.

The certificate supports a_b = 203/10^11, with the complex saving unchanged.
The retained parameter recipe has strict minimum margin

    G = 17661/10^23 > 13/2^66.

These checks support the written transfer proof. The upstream multiplication
algorithm and its unchanged interfaces remain assumptions.

## Bounded probes and where to spend the next effort

Straight cross-group sharing removes 45,706 additions, about 7.9% of the old
side roles. It is worthwhile but does not fundamentally change the circuit's
size. Exact logarithm enclosures put the downstream ceiling for **this
particular graph** below 2^-62. This is not a bound on future graphs.

An independent greedy circuit experiment repeatedly factors the input-node
pair used together in the most outputs, using only disjoint-support additions.
It gives 11,474 additions per common point versus the present local circuit's
11,566: less than 1% better. Every output support passes exact comparison.
Run `python3 scripts/experiments/exclusion_greedy.py` to reproduce it. It is
an exploratory alternative, not part of the certified network. Its failure
to make a large gain proves no lower bound.

Other quick local probes of aligned splits and chaining unchanged input values
through nested later consumers also produced small changes. They have not
been promoted into the certified construction. Continued tuning of these
choices does not currently justify a large search budget.

For a concrete next target, retain h=46, the central losses, and the current
parameter recipe. An eligible graph with **at most 158,353 side roles** would
support a_b=6.4e-9 and kappa=2^-59. This sufficient budget follows by exact
comparison of D/(W*m) with a_b*(5743/500); it is recorded in the certificate.
It requires roughly a 3.36-fold reduction from the current role count.

The next architectural search should therefore consider sharing computations
that combine contributions from different common points, or a substantially
smaller reversible implementation of the whole intersection-one map. The
complement-frame lemma allows such a search to focus its frame audit on source
spans. New mixed source spans may be indefinite or degenerate, so their
nondegeneracy must be checked before a scalar circuit is credited as a network.
The immediate screen should be the side-role count and added rank loss; only
candidates with a material saving merit the full upstream patch audit.

Follow-up: the [paired-network result](paired-network.md) reaches 2^-59 by
changing both the finite circuit and the guard/Gaussian estimates. The ceiling
above retains the older downstream inequalities and does not apply to that
combination.
