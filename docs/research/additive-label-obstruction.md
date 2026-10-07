# Point-additive labels cannot improve the dimension per label

This bounded follow-up to the rank-two feasibility audit allows arbitrary
point matrices, indefinite forms, and local changes of label basis. It still
cannot produce the proposed dimension-24, rank-two labels at h=24. This is a
restriction on one explicit ansatz, not a general impossibility theorem.

## Statement

For every triple T of [h], let A_T and B_T be r-by-k rational matrices with

    A_T = A_0 + sum_{i in T} A_i.

The B_T are unrestricted. Assume A_S^T B_T=0 whenever |S intersect T|=1,
and every diagonal block A_T^T B_T is invertible. For h>=6,

    r >= kh       if h != 9,
    r >= k(h-1)   if h = 9.

Invertible changes of basis separately at each label do not evade the claim:
they can be undone without changing any required zero or diagonal rank.
Taking B_T=H A_T covers any rational symmetric ambient form H, including
indefinite forms. The one-sided statement is stronger: B_T need not depend
additively on T or arise from a symmetric form at all.

At h=24,k=2 this forces r>=48. In the proposed hyperbolic split model,
if either paired-vector family is point-additive, its scalar ambient dimension
must be at least 24; the hoped-for dimension 12 is excluded.

## Neighbor hyperplane

Fix T. Write q_S for the indicator vector of S. The q_S with |S intersect
T|=1 span the hyperplane annihilated by w_T=3q_T-1.

To see the dimension, differences of neighbors with the same outside pair
give the two independent coordinate differences inside T. Differences with
the same inside point give all coordinate differences outside T: there are
at least three outside points, so a shared third point permits each such
difference. These spaces have dimensions 2 and h-4. One neighbor indicator
has nonzero coordinate sum and supplies another independent direction.
Thus the dimension is h-1. Every neighbor has dot product 2-1-1=0 with
w_T, completing the identification over Q.

## Factorization forced by the zero constraints

Absorb A_0/3 into each point matrix. Fix T and put D_i=A_i^T B_T. Every
matrix entry of (D_1,...,D_h) annihilates the neighbor hyperplane. Hence

    D_i = (3*1_{i in T}-1) C_T

for some k-by-k matrix C_T. Summing over i in S gives

    A_S^T B_T = 3(|S intersect T|-1) C_T.

On the diagonal this is 6C_T, so C_T is invertible. If G is the scalar
matrix G_ST=|S intersect T|-1, the full block fitting matrix consequently is

    M = 3 (G tensor I_k) diag(C_T).

It has rank k rank(G), and also rank at most r from its assumed factorization.
No point-permutation symmetry was assumed; the zero constraints imposed this
form themselves.

Let Q be the triple-by-point incidence matrix. It has column rank h: triple
differences give all point differences, and one triple has nonzero sum. Since
Q 1=3*1,

    G = Q (I-J/9) Q^T.

The middle matrix has eigenvalues 1 on the zero-sum subspace and 1-h/9 on
the constant line. Full column rank of Q preserves its rank on multiplication
by Q and Q^T. Therefore rank(G)=h, except rank(G)=h-1 at h=9.

The exception at h=9 is real but does not rescue the proposed network:
even its favorable ratio r/k=8 has v=84 < 6*h*(r/k)=432, giving a
nonpositive network deficit under the current transfer counts.

## Consequence for the search

Changing point weights, adding a constant offset, mixing coordinates, choosing
an indefinite form, or varying local bases cannot help if the label frames
remain point-additive on even one side. Pair-dependent or higher-order
features, a different combinatorial family, or a changed scalar circuit are
needed to escape this ansatz.

This closes a cheap symmetry-breaking attempt. It does not establish that
arbitrary rank-two labels exist or that they are impossible. The conditional
multiplication certificate remains 2^-75.

Reproduce with `python3 scripts/audit_additive_labels.py`. Independent rational
elimination tests include the exceptional h=9 case and nonsymmetric invertible
block column factors. Modular ranks used in the certificate are only lower
bounds for integer matrices over Q, paired with exact rational upper bounds.
