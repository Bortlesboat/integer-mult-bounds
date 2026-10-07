# Overlapping incidence circuits: conditional kappa = 2^-67

The bit network's individual neighbor channels can be replaced by rectangle
circuits. A rectangle with a source triples and b target triples uses a+b-1
scratch roles, instead of ab. Its new middle gate has a common nondegenerate
frame and introduces no decreasing edge. First/third-stage sharing then
applies to all side and central roles. The old complex network is unchanged.

This gives a conditional 2^-67 witness at h=46, a 256-fold increase in kappa
over the local 2^-75 witness. It is a new finite scalar circuit with new
frame assignments, not just a tighter count of the old circuit. The unchanged
upstream multiplication machinery remains a dependency.

## Rectangle partition

Neighbors have a unique common point i. Remove it; their remaining pairs are
disjoint subsets of the other 45 points. Partition this ordered pair
disjointness relation into rectangles S times T. In every rectangle, every
source pair is disjoint from every target pair. Add i back to obtain the
triple families. Each neighbor appears exactly once; there is no cancellation
or assumption about a covering being a partition.

`scripts/incidence_rectangles.py` constructs these partitions recursively.
On n points, D(a,b) denotes disjoint a-subsets against b-subsets, a,b<=2.
If either size is zero, one complete rectangle suffices. Otherwise available
choices are singleton-row rectangles, singleton-column rectangles, or a split
into l and n-l points. A split separates the relation by the source and
target cardinalities in its left half. Each case is a Cartesian product of
two smaller disjointness relations, hence of their rectangles.

For a partition let (C,L,R) be its number of rectangles, sum of source-family
sizes, and sum of target-family sizes. Tensor products multiply each of the
three counts; disjoint cases add them. The cost is L+R-C. Weighted recursive
costs alpha*L+beta*R-C account for multiplication by a complete factor. When
both factors are nontrivial they are D(1,1); the implementation tries each
factor's unweighted selected plan, row stars and column stars. Every split
size is tried. This restricted search supplies a construction, not a claim
of optimality among all partitions.

At n=45 the selected partition has

    C=2759, L=27278, R=27534, L+R-C=52053.

An independent exhaustive enumeration verifies that its rectangles contain
each of the 893,970 ordered disjoint pairs exactly once. Across all 46 common
points, each invocation uses R_side=46*52053=2,394,438 side roles, compared
with 41,122,620 individual neighbor roles in the original invocation.

## An invertible rectangle mixer

For a rectangle with a sources and b targets, use a+b-1 roles. The input
slots and output slots overlap at one pivot. Define an invertible linear map
L by adding all other input slots into the pivot, then adding that pivot to
all other output slots. All operations are over GF(2). Its output-by-input
submatrix is all ones, and its inverse reverses the two steps.

Let V copy each source value into its input slot; let J add each output slot
to its target. Write G for the old central gather and R for its scatter.
For every rectangle simultaneously, a forward invocation has this schedule:

| Time | Operation | Physical frame, suppressing Q |
| --- | --- | --- |
| 0 | L on side scratch | B tensor F |
| 1 | J to Y | B tensor F |
| 2 | inverse L | B tensor F |
| 3 | R to Y | B tensor F |
| 4 | V from X | (B tensor F) orthogonal-sum (P tensor line(t_X)) |
| 5 | G from X | A tensor F |
| 6 | R to Y | B tensor F |
| 7 | L on side scratch | (B tensor F) orthogonal-sum (P tensor U) |
| 8 | J to Y | (B tensor F) orthogonal-sum (P tensor t_Y-perp) |
| 9 | inverse L | A tensor F |
| 10 | G from X | A tensor F |
| 11 | V from X | A tensor F |

The source frame at time 4 and target frame at time 8 are grouped separately
by data triple. L is grouped by rectangle. Every wire touching a particular
gate has its displayed common frame. The earlier side injection now uses
B tensor F, rather than the old B tensor line(t_Y); the data-wire growth to
this larger early label is monotone and causes no extra backward rank.

If the initial side vector is z, the first three operations add JLz to Y
and restore z. Copy changes z to z+Vx. The middle L and injection add
JL(z+Vx); the two dirty-scratch terms cancel. The final inverse L and copy
restore z. Center operations contribute RGx and restore every center. Thus
the net map is Y+= (JLV+RG)X = Y+X, since the rectangles partition exactly
the intersection-one correction. No scratch is assumed initially zero.

## Why the middle frame is legal

Retain the original rational form on F=Q^h, I-J/9. For a forward rectangle,
let U be the span of its physical X triple indicators. They all contain the
same common point i, and every physical Y triple in the rectangle is a
neighbor of every such X triple. Therefore

    line(t_X) subset U subset t_Y-perp.

U is nondegenerate. Indeed, for any vector u in the span of triples containing
i, sum_j u_j=3u_i, so

    <u,u> = sum_{j != i} u_j^2.

This is positive for nonzero rational u: if the outside coordinates vanish,
the displayed linear relation also forces u_i=0. Thus U is positive definite
even though the ambient form is indefinite at h=46. Its inclusions above
have nondegenerate orthogonal residuals.

The original decomposition A=B orthogonal-sum P and future factor Q are
unchanged. Input-only side roles follow low -> X-line -> U -> full; output-only
roles follow low -> U -> Y-perp -> full; the pivot follows both. All changes
are nested. Data X grows from its original incoming label to X-line and then
full. Data Y grows from its incoming label to low and then Y-perp. Their
stage boundaries are exactly the original ones.

## Reverse invocation at stage 2

Reverse the scalar schedule and invert its operations, using logical source
Y and target X. Its chronological operations and frames are:

    V(low), G(low), L(low), J(X-line), inverse L(U), R(full),
    G(low), V(Y-perp), R(full), L(full), J(full), inverse L(full).

Here U is the span of the physical X indicators, now the rectangle's logical
target family. It is again nondegenerate and orthogonal to all physical Y
indicators in that rectangle. The physical X/Y frame transitions therefore
remain the same as in a forward stage. The only decreasing central edge is
full -> low, between times 5 and 6. In a forward stage it is between times
5 and 6 as well. Each loses dimension h, after including the rank-one tensor
factors P and Q. No side edge decreases in either schedule.

Consequently the original data endpoints, scalar bank exchange, and loss
L_total=3v^2h^2 are retained. The original source-rank correction remains N.

## Sharing whole auxiliary banks between stages 1 and 3

Use the existing even-h triple permutation pi with |A intersect pi(A)|=1.
Match the entire auxiliary bank in the stage-1 invocation with fixed triples
(A,B) to the bank in the stage-3 invocation with fixed triples (B,pi(A)),
keeping its local role index. This is a bijection and both invocations restore
every arbitrary scratch value. It identifies no simultaneous roles.

Every auxiliary role's first gate now has label B_stage tensor F tensor Q,
and its last gate has label A_stage tensor F tensor Q. In a joined pair,

    E = F tensor line(t_A) tensor line(t_B),
    H = line(t_B tensor t_pi(A))-perp tensor F.

The pairing t_A perpendicular t_pi(A) proves E subset H. Both labels are
nondegenerate. Replacing E -> F^3 and 0 -> H by E -> H saves exactly m rank
per removed role and creates no decreasing edge. This includes central roles,
unlike the prior side-only sharing patch. All remaining auxiliary endpoints
are still 0 and I_m, and the completed scalar permutation fixes every role.

## Counts and downstream certificate

At h=46, v=C(46,3), N=v^3 and m=h^3. The new counts are

    W = 2N + 2v^2(R_side+h),
    s = Wm-N+6v^2h^2,
    eta = (N-6v^2h^2)/(Wm).

Take a=46/10^11 and keep the old complex saving a_c=9/500000000000.
Exact logarithm enclosure proves eta>a log(m), so the bit recurrence supports
tau=1-a. The existing nonadjacent-axis parameter recipe gives

    epsilon=1/21, beta=9/10, c=9a/10,
    lambda=1-19a^2/20, lambda'=1-9a^2/10, sigma=1-a_c,
    min_j g_j=3a^2/70=1587/175000000000000000000000 > 2^-67.

All strict layer inequalities pass. The label dimension stays 46^3 for both
networks; no distinct-dimension transfer assumption is needed. The rational
frame bases, side mixers, and additional gates are fixed finite data, so they
change only finite compilation constants in the original interchange
interface. The complex network and its arithmetic guard analysis are unchanged.

`scripts/incidence_network.py` writes the exact count and parameter certificate.
Tests check the complete linear map of small forward and inverse invocations
on every input basis vector; a three-stage h=6 simulation checks bank exchange
and restoration with shared, arbitrary scratch. Further tests check the
rectangle partition, mixer, subspace norm identity, and sharing inclusion.
These tests support the written argument; they do not independently validate
the upstream algorithm. No practical speedup or global optimality is claimed.
