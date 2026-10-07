# Feasibility audit of the proposed 2^-59 route

October 7, 2026. **No exponent in the 50s has been established.** The strongest
checked multiplication bound in this repository remains conditional 2^-75.
The rank-two target is still open in its unrestricted indefinite rational form.

This audit rules out several tempting restricted models and supplies a bounded
numerical probe. It is not a nonexistence proof for the desired representation.

## Target and outcomes

The proposed representation assigns a nondegenerate two-plane U_T to every
triple T of [24], inside a 24-dimensional rational space with a nondegenerate
symmetric bilinear form. Neighboring triples, with intersection size one,
must receive orthogonal planes. The conditional counting and parameter
implication remains in [the target certificate](../../certificates/block-label-target.json).

| Restricted model | Exact finding |
| --- | --- |
| Gram blocks depend only on intersection size | Minimum rank 48, excluding rank 24 |
| Positive-definite ambient form | Rank at least 37 at h=24,k=2 |
| Positive-definite ambient form, arbitrary h and label rank k | Current shared-side construction and downstream constraints cannot reach 2^-67 |
| Planes supported only on their triple's coordinates, original form I-J/9 | No such plane assignment |
| Characteristic-two block fitting matrix | Rank at least 169 at h=24,k=2 |
| Arbitrary indefinite rational representation | Unresolved |

The positive-definite restriction is on the **ambient form**. Positive planes
inside an indefinite ambient space are not excluded by that argument.

## Intersection-only block kernels

Write B_t(S,T)=C(|S intersect T|,t), for t=0,1,2,3. A block kernel depending
only on intersection size has a unique expansion

    M = sum_{t=0}^3 B_t tensor C_t,

where the C_t are 2x2 matrices. The four Johnson levels have dimensions

    1, h-1, C(h,2)-h, C(h,3)-C(h,2).

On level j the eigenvalue of B_t is zero for j>t, and otherwise is

    C(3-j,t-j) C(h-t-j,3-t).

These identities follow by lifting coefficients on j-subsets whose sums on
(j-1)-subsets vanish. The nested incidence spaces have successive dimensions
C(h,j)-C(h,j-1); counting the t-subsets in a fixed intersection gives the
displayed action. Equivalently, disjoint-pair differences generate the harmonic
levels. The tests independently verify this action on explicit integer
harmonics in small cases.

At h=24, the last two multiplicities are 252 and 1748. If rank(M)<48, its
level-3 block must vanish, forcing C_3=0, and its level-2 block must vanish,
forcing C_2=0. Thus M(S,T)=C_0+|S intersect T|C_1. The neighbor zero condition
gives C_0=-C_1. The diagonal block is 2C_1 and must be invertible. Consequently

    M = [|S intersect T|-1] tensor C_1

has rank 24*2=48, a contradiction. Rank 48 is attained by duplicating the
old representation. This excludes arbitrary intersection-only block kernels,
not just scalar multiples selected in advance.

This is a restriction on the Gram blocks in a common choice of block bases.
It does not exclude all group-equivariant subspace constructions: nontrivial
actions on the internal block coordinates can fall outside this model.

## Positive-definite geometry: an all-ranks screen

Let H be the triple graph with adjacency at intersection size one. Its
adjacency matrix is B_1-2B_2+3I. The nonconstant eigenvalues are

    (h-4)(h-9)/2, 11-2h, 3,

and its degree is z=3C(h-3,2). Write -s for its least eigenvalue and v=C(h,3).
The matrix

    Y = t I + b A_H - J,
    b = v/(z+s), t = v s/(z+s),

is positive semidefinite: it vanishes on the constant eigenspace, and all
other eigenvalues are t+b*lambda >= 0.

Now assume the ambient form is positive definite, so we may use Euclidean
orthogonal projections P_T onto the k-dimensional labels. The matrix

    X(S,T) = tr(P_S P_T)/(v k)

is positive semidefinite, has trace one, and is zero on edges of H. Hence
0<=tr(YX)=t-sum X(S,T). On the other hand, Q=sum P_T has trace vk, and
tr(Q^2)>=(vk)^2/r by Cauchy-Schwarz on its eigenvalues. Combining these gives

    r/k >= v/t = (z+s)/s =: x(h).

At h=24 the adjacency eigenvalues are 630,150,-37,3. Thus

    r/k >= 667/37, and for k=2, r>=37.

No external optimization software is needed for this bound. It is an
explicit positive-semidefinite dual certificate, checked with rational numbers.

For arbitrary h and k in the stated three-stage construction, put y=r/k.
The shared-side role count is W=2v^3+2v^3z+3v^2h, and the relative deficit is

    eta = v^2 (v-6hy)/(W y^3).

Positivity requires v>6hy. On that interval eta decreases with y. Also
log(r^3)>=log(y^3). We can therefore bound every positive-definite candidate
optimistically by replacing y with x(h) and allowing k=1 even when the bound
is nonintegral or unattainable.

Exact log enclosures for 6<=h<200 select h=35 as the maximum of this optimistic
bound, with saving less than approximately 3.017e-10. Odd ground sizes are
included as a favorable relaxation, regardless of the explicit even-h matching.
For h>=200, x(h)>h/2, W>2v^3z, and log(r^3)>1 give

    a = -log(1-eta)/log(r^3) < 4/(z h^3-4).

This decreases and is already below the finite maximum at h=200. Finally,
the current necessary downstream inequality

    kappa < a^2/[20(1-a)]

puts the entire optimistic positive-definite family below 2^-67. This is not
a bound on indefinite labels, changed scalar circuits, reduced central losses,
or different downstream cost accounting.

## Why coordinate-local two-planes fail

Assume U_T is contained in the three coordinate positions indexed by T, with
the original form I-J/9. For neighboring triples S,T sharing coordinate i,
the pairing between their three-dimensional coordinate spaces has matrix

    K = E_ii - J/9.

It has rank two. Its left kernel is the line spanned by the difference of
the two coordinates of S other than i; its right kernel is the analogous
line for T. If a two-plane in S is orthogonal to a two-plane in T, it must
contain the left kernel: otherwise the pairing restricted to that plane has
rank two, leaving only a one-dimensional kernel in T, too small for U_T.

For each i in S there is a neighboring triple intersecting S exactly at i.
Thus U_S contains all three coordinate differences and is exactly the
zero-sum plane on S. But the zero-sum planes of neighboring triples are not
orthogonal: vectors e_i-e_j and e_i-e_l have pairing one. Contradiction.
This rules out the natural sparse-coordinate extension without relying on a
solver or a positivity assumption on the ambient form.

## Characteristic two is a bad discovery field for this target

Let M be any block fitting matrix over characteristic two, with invertible
kxk diagonal blocks and zero blocks at intersection-one neighbors. Let
A(S,T)=|S intersect T| modulo 2, the scalar incidence Gram matrix, of rank
at most h. Blockwise multiplication of M by A leaves only its diagonal
blocks: off-diagonal intersections are 0,1,2; A vanishes at 0 and 2, while M
vanishes at 1. The resulting matrix has rank vk.

Expressing A as a sum of h outer products expresses the product matrix as a
sum of h row/column-scaled copies of M. Consequently

    vk <= h rank(M).

At h=24,k=2, rank(M)>=ceil(4048/24)=169. This excludes the proposed rank 24
over characteristic two. It also excludes a rational solution whose entries
reduce regularly modulo two and whose diagonal blocks remain invertible.
It does **not** exclude a rational solution with essential bad reduction at
two. The original rational triple Gram matrix illustrates why this matters:
its diagonal is two, which disappears on reduction.

Thus a GF(2) search with nondegenerate diagonal blocks would be searching an
impossible model. Odd-characteristic solutions would still require verified
rational lifts before promotion.

## Bounded numerical probe

`scripts/experiments/block_completion.py` alternates the affine constraints
(zero neighbor blocks and prescribed 2x2 diagonal blocks) with symmetric
rank truncation. It keeps the eigenvalues of largest absolute magnitude, so
it permits indefinite ambient forms. The tested diagonal blocks are I_2 and
diag(1,-1); heterogeneous signatures are not searched.

The first run checked (h,r)=(8,14),(10,16),(12,20), two signatures, and two
seeds, with 200 iterations per case. None converged. Best maximum entrywise
constraint errors ranged from about 0.118 to 0.967, far from a candidate.
The exact duplicated representation supplies known feasible controls at
h=8,r=16. A subsequent [exact small construction](small-block-control.md)
also supplies h=8,r=14 for both tested signatures: thus two of the failed
parameter cases are known to be feasible. Floating-point failure here is
demonstrably a search failure, not a nonexistence result. This probe is not
included in the mathematical certificate or routine verification target.

To reproduce the optional probe:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  uv run --with numpy==2.5.3 python scripts/experiments/block_completion.py
```

Results are written under `build/`, not promoted into theorem certificates.
There is no justification from these runs for a large dense search at h=24.

## Research decision and references

The first feasibility pass has not produced a route to the 50s. It does show
that the easy models do not contain the target. The remaining candidate must
escape intersection-only Gram blocks, coordinate locality, and a
positive-definite ambient form, and must have essential bad reduction at two.
These are meaningful algebraic requirements, not merely numerical tuning.

A focused next attempt could use mixed-signature labels and a symmetry group
smaller than the full point-permutation group. A hyperbolic split model can
also be built from paired vectors a_T,b_T in dimension d with a_T^T b_T=1
and both cross pairings zero at neighbors: the vectors (a_T,0),(0,b_T) are
nondegenerate two-planes in dimension 2d. For the current target d=12. This
is another unconstructed sufficient condition, not evidence that the target
is feasible. A new attempt should have its own bounded algebraic ansatz.

The general block/paired-vector fitting framework is described in
[Bukh and Cox, Section 2](https://arxiv.org/pdf/1802.00476).
Nearby minimum-rank results must be checked against their definitions:
[Hu and Tang](https://arxiv.org/pdf/2607.06480) prescribe nonzero entries on
every allowed off-diagonal edge, which our fitting problem does not require.
Their lower bound therefore does not directly rule out this target.

Exact arithmetic is in `scripts/audit_block_labels.py` and
`certificates/block-label-audit.json`; independent finite checks are in
`tests/test_block_label_audit.py`. The checked 2^-75 result is unchanged.
