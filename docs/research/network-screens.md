# Scoped bounds for finite-network searches

These are conditional counting bounds and rejection criteria, not general
lower bounds on integer multiplication. They retain the source's three-stage
bit network unless an explicit modification is stated. Write

    v = C(h,3), z = 3 C(h-3,2), N = v^3, m = h^3,
    W = 2v^3 + 3v^2(vz+h), L = 3v^2 h^2,
    D = N-2L, eta = D/(Wm), a = -log(1-eta)/log(m).

The original network has a positive deficit exactly when v > 6h^2, which
requires h >= 39. The rational form is nonsingular throughout this range.
Exact logarithm enclosures select h=46 among 39 <= h < 200. For h >= 200,

    a < 1/(3 z m - 1),

a decreasing bound already below the h=46 lower enclosure. This bit-only
search includes h=39; it does not unnecessarily impose the complex network's
positivity condition on a prospective bit construction.

## One shared binary aggregation hierarchy

Suppose a binary tree partitions the source triples. Each target receives the
maximal tree subtrees contained entirely in its neighbor set. A target with z
neighbors saves one channel for each internal tree node contained in that set.
Summing over targets, the saving is the sum of the common-neighbor counts of
the internal nodes. Each internal node contains two distinct triples.

If those triples have intersection size k in {0,1,2}, put q=h-6+k. Their
common-neighbor count is

    k C(q,2) + (3-k)^2 q.

The first term selects one point of their intersection and two outside their
union. The second selects one point from each difference and one outside.
For h >= 39 the maximum is (h-4)^2. Thus every such hierarchy uses at least

    vz - (v-1)(h-4)^2

side channels per invocation. At h=46 the lower bound is 14,346,864 channels;
the possible reduction is less than 2.867-fold. Uniformly in admissible h,

    z / (z-(h-4)^2) = 3(h-3)/(h-1) < 3.

Even if hierarchy overhead is free and the original L does not increase,
the total W stays greater than W_original/3, so eta_new < 3 eta_original.
For 0 < eta < 1/10, (1-eta)^4 < 1-3eta. Consequently a_new < 4 a_original.
Using the all-h h=46 maximum and the current downstream necessary inequality

    kappa < a_new^2 / (20(1-a_new)),

the exact certificate excludes kappa=2^-70 for this hierarchy family.

This bound assumes unshared stages and the original central losses. It does
not cover arbitrary overlapping incidence factorizations, cancellations,
simultaneous improvements to other components, or general finite circuits.

## Thinning the triple family

Let an arbitrary subfamily have v triples on h points, point degrees d_i and
pair degrees d_ij. Let E1 count ordered distinct pairs intersecting in one
point. Double counting gives

    E1 = sum_i d_i^2 - 2 sum_{i<j} d_ij^2 + 3v.

Since sum d_i=3v, sum d_ij=3v, and d_ij <= h-2,

    E1 >= 9v^2/h - 6vh + 15v.

Keep the h-dimensional label space, h central roles per invocation, three
tensor stages, and one side role per ordered neighbor edge. The scalar
identity and neighboring-label orthogonality restrict to such a subfamily.
Its optimistic deficit bound is

    eta <= (v-6h^2) / [h^3 ((27/h)v^2 + (47-18h)v + 3h)].

It is enough to consider 6h^2 < v <= C(h,3). With A=27/h, B=6h^2,
C=47-18h and D0=3h, the derivative numerator of (v-B)/(Av^2+Cv+D0) is

    -Av^2 + 2ABv + BC + D0.

This decreases for v>B. Exact checks show it remains positive at v=C(h,3)
for every h from 39 through 59. At that endpoint the edge bound is attained
by the full triple family. Hence thinning cannot help in this range.

For h>=60, the edge bound gives E1/v > 8v/h. Therefore

    eta < (v-6h^2)/(24v^2h^2) <= 1/(576h^4).

Also log(h^3)>10. The resulting a < 1/[10(576h^4-1)] is already below
the full h=46 saving at h=60 and decreases afterward. No such subfamily
beats the original full h=46 construction. This does not cover a reduced
ambient label dimension or a new gate schedule.

## Unequal complete-triple factors

For ground sizes h_1,h_2,h_3, put v_i=C(h_i,3), z_i=3C(h_i-3,2). The same
unshared construction has

    N = product v_i, m = product h_i,
    W = N(2+sum z_i) + sum (N/v_i)h_i,
    L = sum (N/v_i)h_i^2.

Positivity forces 2 sum h_i^2/v_i < 1. Since h_i^2/v_i > 6/h_i, each
h_i>=15 and sum 1/h_i<1/12. The arithmetic-geometric mean inequality on
the reciprocals implies m>36^3, so log m>10.

An exact search covers all 3,898,895 unordered triples with 15<=h_i<300.
Integer comparisons reject all but 1,099 of the positive-deficit cases
before logarithm enclosure is needed. The unique best tuple is (46,46,46).
The runner-up is (46,46,47).

For H=max h_i>=300, use m>=225H and W>=N z(H). Then

    eta < 1/(225H z(H)),
    a < 1/[10(225H z(H)-1)].

This decreases and is below the h=46 lower enclosure already at H=300.
Thus unequal factors do not improve this original counting family. The claim
does not apply to the new stage-sharing family, whose role counts differ.

## Scratch reuse must include rank loss

Fix N and m and write D=N-2L. If deleting r roles introduces at least r
additional backward dimensions, the new relative deficit is at most
(D-2r)/[(W-r)m]. For D<=2W,

    (D-2r)/(W-r) <= D/W.

At h=46, D/W=18/894191, much smaller than 2. A one-dimensional reset per
deleted role therefore outweighs its benefit. The criterion applies only
after proving that a proposed reuse scheme incurs the stated loss.

The [stage-sharing construction](../../notes/stage-reuse-note.tex) escapes
this criterion: a matched stage-1/stage-3 transition is nested and adds zero
backward dimension. It removes Nz roles, preserves D, and supports 2^-75.

## A smaller orthogonal representation is not sufficient by itself

There is a tempting low-dimensional substitute for the tensor representation.
For a=(A,B,C), concatenate the three indicator vectors to obtain u_a in Q^(3h),
with form I-(7/81)J. Its span has dimension 3h-2. Each u_a has norm 2; two
labels differing in one coordinate with intersection one are orthogonal.
Thus it solves the local graph-orthogonality problem in far less than h^3
dimensions.

It fails the existing stage schedule. After the first-stage central gate,
the X label must contain

    V_1(T,C) = span {u_(R,T,C): R is any triple}.

At a second-stage side channel to target (A,S,C), where |T intersect S|=1,

    <u_(R,T,C), u_(A,S,C)> = |R intersect A| - 3.

This is nonzero for R!=A. Hence V_1(T,C) is not contained in the final
target orthogonal complement. The original monotone copy-to-side path cannot
be retained. A lower-dimensional representation must therefore come with new
compatible stage frames or an explicit affordable loss budget. This example
rejects a direct substitution, not all lower-dimensional representations.

## Exploratory higher odd subset sizes

The variants script also screens subset sizes 5,7,...,15 with h<500. It
hypothesizes a favorable label dimension C(h,t)-C(h,t-1), t=(k-1)/2, counts
all odd-intersection neighbors, and retains h central roles. This is an
optimistic numerical model, not a proved feasible family. Floating-point
scores select a candidate; only that candidate's score is then enclosed
exactly. No all-h bound or exact optimality claim follows from this screen.

Even these favorable sampled scores are poor: the selected k=5 case has
saving about 8.71e-15, versus 1.80e-11 for the original triple construction;
the larger sampled subset sizes score still lower. That does not justify
spending this investigation's budget on their missing frame constructions.

## Reproduction and proof boundary

`scripts/research_networks.py` writes `certificates/network-research.json`;
`scripts/search_network_variants.py` writes `certificates/network-variants.json`.
Both are included in `make verify`. The accompanying tests independently
enumerate common neighbors, check the subfamily edge identity, compare tree
channel counts, specialize unequal counts to the original formula, and exhibit
the direct-sum nesting failure.

The proofs above justify the families and tail bounds. Finite arithmetic
checks certify their numerical consequences, not the correctness of every
underlying algorithmic interface.
