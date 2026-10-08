# Current contracts and research status

Updated October 7, 2026. Author: Douglas Colkitt. All results remain conditional
on the pinned upstream algorithmic interfaces and the identified written
extensions. Nothing here asserts formal or independent verification.

## Current and earlier results

| State | Exponent saving kappa | Artifacts |
| --- | --- | --- |
| Earlier published baseline | `2^-59` | [paired note](../../artifacts/paired-note.pdf), [patch](../../patches/h50-paired-59.patch) |
| Published compact-control checkpoint | `83/10^12 > 2^-34` | [note](../../artifacts/compact-control-note.pdf), [certificate](../../certificates/compact-control-layer.json), [patch](../../patches/compact-control-34.patch) |
| Integrated follow-up, pending publication | `2^-31` | [note](../../artifacts/complex-compression-note.pdf), [certificate](../../certificates/complex-compression.json), [patch](../../patches/complex-compression-31.patch) |

The latest witness increases kappa by approximately 5.61 times over the exact
preceding witness; the dyadic comparison `2^-34` to `2^-31` is eightfold.
These compare exponent savings, not practical runtime. All earlier certificates,
patches and the pinned upstream source remain unchanged.

## What changed and what is retained

The [complex-network construction](complex-compression.md) uses weighted
rectangles for disjoint triples, shared sums for intersection-two triples,
and binary phase frames valid in both signed directions. Transparent computation
restores arbitrary auxiliary inputs. A matching shares the complete first/third
auxiliary banks. At `h_c=26`, it has

    m_c = 17576, W_c = 7082222160000,
    s_c = 124477130005280000,
    a_c = 1-sigma = 5/10^9.

The bit network remains `h_b=50`, `m_b=125000`, with
`a_b=1-tau=296/10^11`. Thus the complex interface now has the larger saving.
The bit interface is the bottleneck.

The retained compact-control construction moves compact dirty fields instead
of spaced windows, at cost `O(V*((f log p)^tau+1))`. It reserves two front
fields and one back field from existing address coordinates, preserves complete
ranges in every recursive child, restores arbitrary values, and charges
exceptional-address repair at every node. All three movement/layout/guard
proof sources are embedded verbatim in the new patch.

## Exact current parameters and bottleneck

The certificate uses

    epsilon = 199/1000, c = 1,
    beta = 1/100, zeta = 1/1000, delta = 1/10000,
    C1 = 4961/1000,
    lambda = 1-293/10^11,
    lambda' = 1-29/10^10,
    kappa = 2^-31.

The internal, leaf and reservation exponents are

    chi = tau+(1-beta)*max(sigma-tau,0) = tau,
    leaf = sigma+beta*(1-sigma),
    reserve = max(1-c,0) = 0.

All required comparisons are strict. The seven assembly margins have minimum

    G = g3 = 5771/10^13 = 5.771e-10 > 2^-31.

The explicit new scalar-operation count fits the generalized guard's node
charge `E=64*(W_c+m_c+1)^3`. The guard still has
`C1=5-4*beta+zeta`, and `epsilon*C1=987239/1000000<1`.
Reserved-axis processing costs `O(V log p)` for `c=1`.

The old quadratic restriction from `K^tau` is absent. With the **retained
certified bit exponent and Gaussian assembly inequality**, the current scoped
ceiling is `kappa<a_b/5=5.92e-10<2^-30`. This is not an all-network limitation.
The new complex saving provides numerical headroom for `2^-30` if a stronger
bit construction is supplied; that is not another established witness.

## Verification boundary

The [integration review guide](complex-compression-review.md) identifies each
new obligation and its tests. General arguments are supplied in:

- [compressed complex construction](../../notes/complex-compression.tex);
- [movement and deterministic repair](../../notes/compact-control-movement.tex);
- [reservations, row splitting and recurrence](../../notes/compact-control-layout.tex);
- [generalized guard](../../notes/compact-control-guard.tex).

The new certificate records all four source hashes. The combined patch applies
directly to the pinned original and includes the full retained refinements.
It updates every complex constant, the exponent ordering, scalar guard charge,
final parameters and derived powers. It preserves the legacy wide-slot lemma
for the appendix and retains the corrected local exceptional-stream sum.

Finite tests check exact signed scalar maps with independent dirty variables,
rectangle partitions, binary residual bases, phase identities, matching,
parameter inequalities and source integration. They do not simulate the entire
multiplication machine or replace independent proof review. The retained
compact-control arguments have the same review dependencies as before.

Completion checks passed: 176 tests, 18 patch-application checks, exact
certificate/patch regeneration, and both note and manuscript builds.

Reproduce with `make verify` and `make complex-note`. See the
[reproduction instructions](../reproducibility.md) for applying the patch and
building a manuscript preview without changing the pinned source.

## Next research priority

The complex construction is integrated. The next improvement should target
the bit finite network, especially methods transferable from the new circuit
compression or a new topology. More complex-network tuning alone cannot cross
the present bit/Gaussian ceiling. Independent review remains valuable for both
the new phase-frame transfer and the retained compact-control tape proof.

The previous [joint-frame obstruction](joint-frame-audit.md) remains scoped to
its fixed-boundary, grouped-gate model. Older research pages retain their
chronology; use this page when interpreting superseded targets and barriers.
