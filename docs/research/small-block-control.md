# An exact small rank-two witness and a search control

For h=8 there are valid rational two-plane labels in dimension 14. This
beats duplicating the old eight-dimensional representation, but gives a
negative network deficit and no improvement to kappa. It is useful as a
control for numerical discovery: the earlier alternating-projection runs
failed on precisely this feasible size for both uniform signatures.

Index the eight points by the vectors of F_2^3. Every three distinct points
lie in a unique affine plane. Color their triple by the plane's nonzero
normal vector; there are seven possible normals. A color class consists of
the four triples in each of two parallel, disjoint four-point planes.
Two triples of the same color therefore intersect in zero, two, or three
points, never one. This is a proper seven-coloring of the neighbor graph.

In Q^14 assign color c the coordinate plane spanned by e_(2c),e_(2c+1).
Different colors are orthogonal under any diagonal form. Every label is
nondegenerate if all diagonal entries are nonzero. Thus one may choose a
positive-definite form, seven split blocks, or heterogeneous label signatures.
The finite field is used only to index the coloring; the label construction
is over the rationals and requires no lifting assertion.

The scalar seven-color Gram matrix has rank seven, so doubling gives rank
14. The ambient dimension per label is seven instead of eight. Nevertheless
the transfer inequality requires v>6h(r/k). Here

    v=56 < 6*8*7=336.

Consequently this construction cannot support a positive deficit under the
current network counts. Nor does the coloring give a method of reaching the
h=24 target. It demonstrates that non-additive frames can outperform the
old dimensions at a small size, not that this improvement scales.

The matching scalar GF(2) incidence matrix has diagonal one and zeros between
distinct triples of the same color. Its rank is at most h. Hence every color
class has at most h members, and any proper coloring uses at least v/h colors.
More generally, any coordinate-subspace labeling with k coordinates per
label has r*h >= v*k: for each coordinate, its labels form a color class
of size at most h. Therefore any such labeling has

    v <= h*(r/k),

incompatible with the positive-deficit requirement v>6h(r/k). This argument
holds for arbitrary diagonal signs. Pure coloring and coordinate allocation
can never solve the current network target, even when they improve r/k at
a small size. Non-coordinate geometry is essential for this approach.

The same obstruction covers all pairwise commuting label projections, without
assuming a coordinate basis in advance. Commuting rational idempotents have
a simultaneous decomposition into joint zero/one eigenspaces. If neighboring
labels shared a nonzero joint eigenspace, their projections would have a
nonzero product, contrary to their orthogonality. Each joint eigenspace is
therefore used by an independent set of at most h labels. Counting dimensions
again gives vk<=hr. Any successful label construction under these transfer
counts must have noncommuting projections.

The exact witness and all 840 neighboring-pair checks are in
`scripts/small_block_witness.py` and `certificates/small-block-witness.json`.
The tests additionally form the coordinate pairings explicitly with positive,
split, and negative label signatures.
