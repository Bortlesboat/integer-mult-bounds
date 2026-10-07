# Audit: nonadjacent axis routing

**October 7, 2026 — conditional mathematical audit by Douglas Colkitt, with
assistance from OpenAI Codex.** The audit supports replacing the manuscript's
quadratic count of axis moves by a linear count, using primitives already
stated and proved in the pinned source. This changes a hypothesis of the
published cubic ceiling; it does not contradict that ceiling.

The resulting checked witness is **kappa = 2^-78** with the h = 46 network.
A second witness gives **kappa = 2^-107** with the original h = 100 network,
original tau = sigma = 1 - 2^-50, and beta = 1/2 unchanged. Both depend on the
upstream algorithmic interfaces. This is not an independent verification of
those interfaces or an executable implementation of the complete machine.

## Source-level finding

`lem:chunk-swap` in `04-swap.tex` explicitly accepts the address shape
`[P] x [2^u] x [G] x [2^u] x [B]` with arbitrary positive P, G, and B.
It exchanges the two equal-width fields in O(V u^tau), including shape
processing, workspace cleanup, and padding. The paragraph immediately after
its proof already gives the nonadjacent unequal-width construction:

```
long field first:  e x G y -> e y G x -> y G e x
long field last:   x G e y -> e x G y -> e y G x
```

Here x and y have equal bit width and e is one bit. Each case uses one
completed chunk interchange and one single-bit move, so widths ell and
ell-1 cost O(V (1 + ell^tau)). No new swap lemma, network, or variable-beta
extension is required by the routing change.

The gap G represents all intervening axes. B includes the full coefficient
record. Moving the extra bit preserves the order of all other positions;
record contents and their internal bit order survive every completed field
interchange. When the equal-width pieces are empty, the swap is the identity.
Actual asymptotic applications already have ell >= 2.

## CRT conversion and its inverse

Before the forward CRT updates, the padded physical axes are ordered
`(a_d, ..., a_1)`. Exchange positions j and d+1-j for j = 1,...,floor(d/2).
These disjoint endpoint swaps reverse the list exactly, using floor(d/2)
full-field interchanges. Axis names and widths move with their fields.

The resulting order is exactly `(a_1, ..., a_d)`, which is the order used by
the original triangular CRT proof. The update order remains d,d-1,...,1.
Every lower-index control still precedes the target and is still an original
digit when its offset is computed. The inverse recovers digits in order
1,...,d, then applies the inverse reversal before deleting padding.

The padding insertion and deletion enumerations are unchanged. Temporary
bit-field arrangements need not preserve the original physical validity mask;
the completed coordinate permutation carries the mask to its corresponding
named-coordinate mask. No coefficients are interpreted or discarded during
the temporary swap operations.

The d controlled rotations remain O(d V). The reversal and its inverse now
cost O(V d (1 + ell^tau)). No arithmetic term is removed from this accounting.

## Resampling: expose, process, restore

For each axis i, in the original axis-processing order:

1. Swap the whole field for i with the innermost axis, if they differ.
2. Apply exactly the original line algorithm along coordinate i, in increasing
   numerical order of that coordinate.
3. Undo that field interchange before moving to the next axis.

There are at most 2(d-1) field interchanges per tensor map. The other axes need
not retain their original physical order while a line is processed: their
names, sizes, and validity bounds travel with the fields. The line routine
only requires that its target coordinate be innermost and its other named
coordinate values be fixed. These conditions hold.

The full padded box stays allocated. Expansion reads s_i inputs and writes
all t_i outputs on valid lines. Compression reads t_i inputs and writes s_i
outputs followed by zeros. Other lines remain zero, using the same named-axis
validity predicate as upstream. Restoring the original field order after each
axis makes composition identical to the original tensor map, with the same
axis-processing order and truncations. Contraction norms and numerical error
bounds are therefore unchanged; no commutation of approximate maps is assumed.

## Fixed tapes, descriptors, and volume

Each primitive takes a fixed number of collapsed address lengths. Arbitrarily
many spectator axes become their product G. Since every t_i >= 2,
d <= log_2 T. The axis list (including names and validity bounds), record-width
description, and collapsed lengths have size polynomial in log(2V). Preparing
one call by ordinary integer arithmetic is therefore polynomial in log(2V),
which is O(V). This pays for list scans and updates at every interchange.

Lists and counters are stored data, not additional heads. All interchanges run
sequentially and reuse the fixed work tapes of the source primitives. Their
cleanup is already included. The list of all swaps can be generated from the
axis counters; no unbounded collection of simultaneous streams is introduced.
The volume V refers to the same complete padded box and complete records as
in the original cost calculation.

## Dependency and exponent audit

| Dependency | Result |
| --- | --- |
| `04-swap.tex`, `lem:chunk-swap` and following paragraph | Reused unchanged; the required nonadjacent width-mismatch schedule is explicit. |
| `07-resampling.tex`, `lem:tensor-resampling` | Exposure/restoration count changes from O(d^2) to at most 2(d-1). Numerical maps and errors are unchanged. |
| `08-assembly.tex`, CRT map Phi | Reversal uses floor(d/2) swaps; control order and inverse are unchanged. |
| Assembly cost table | Layout term changes from d^2(1+ell^tau) to d(1+ell^tau). |
| Fixed-parameter constraint | epsilon*(2-tau) < 1-tau becomes epsilon*(1-tau) < 1-tau. |
| Fourth margin | g4 = 1-tau-epsilon*(2-tau) becomes (1-tau)*(1-epsilon). |
| Other six margins | Unchanged formulas. |
| alpha and gamma definitions | Their analytic d^2 factors remain; none are replaced by d. |
| Prime-interval and setup bounds | Their d^2 factors remain; 1-2*epsilon = 19/20 > 0. |
| Guard width | epsilon*C1 = (1/40)*20 = 1/2 < 1, so d^20 = Theta(p^(1/2)) = o(p). |
| Resampling accuracy | alpha = Theta(p^(21/80)); gamma = O(p^(11/20)) = o(p). |
| Packed-gadget repair | epsilon*c > 0, hence K/log(p) -> infinity and polynomial(p)*2^-K -> 0. |
| Layout chunk size | 1-epsilon-epsilon*c > 0, hence K = o(ell). |
| Record length/setup | r = 2^Theta(p^(39/40)) still dominates every fixed polynomial. |
| Input dimensions and prime search | d = Theta(p^(1/40)) -> infinity; setup remains n^o(1). |
| Explicit integer-root calculation | Replaced with d^40 <= b. |
| Final absorption | G = min g_i > kappa, so rho = G-kappa > 0 absorbs all fixed logarithmic factors. |

With a = 1-tau = 1-sigma, choose

```
epsilon = 1/40, c = a/2, beta = 1/2,
lambda = 1 - 3a^2/4, lambda-prime = 1 - a^2/2,
delta = 1/16, C1 = 20.
```

Then g2 = g3 = a^2/80, g4 = 39a/40, g5 = 3/20, g6 = 73/80,
g7 = 1/40, and g1 > 1/2. All side conditions pass exactly.

For h = 46 and a = 9/500000000000, G = 4.05e-24 > 2^-78.
For the original h = 100 and a = 2^-50, G = 2^-100/80 > 2^-107.
The old layout constraint rejects both witnesses: using these epsilon choices
without changing the implementation would be invalid.

## Artifacts and checks

- [Standalone audit note](../artifacts/nonadjacent-axis-note.pdf)
- [Routing-only patch](../patches/nonadjacent-layout.patch): two source files;
  retains the original headline and network choices.
- [Original network and 2^-107](../patches/frozen-nonadjacent-107.patch): four files;
  no finite-network or layer-exponent changes.
- [h = 46 and 2^-78](../patches/h46-nonadjacent-78.patch): seven files;
  retains the previously audited h = 46 network and beta = 1/2.
- [Exact certificate](../certificates/nonadjacent-axis.json)
- [Finite schedule model](../scripts/nonadjacent.py) and
  [tests](../tests/test_nonadjacent.py)

All patches are independent alternatives against the immutable upstream source.
`make verify` regenerates every artifact and runs 27 tests and ten patch checks.
`make audit-note` builds this four-page follow-up note without warnings; the original
note remains separate. All three patched manuscripts also compile in disposable
Tectonic previews after disabling the same three pdfTeX-only metadata commands
as in the earlier audit. Their two small overfull-box warnings are in unchanged
source paragraphs, and no new layout warnings appear.

The new tests compare primitive schedules with independent tuple-coordinate
oracles, cover all width patterns and axis positions in stated finite ranges,
check reversal and inversion, preserve distinct multiword payloads, compare
padded expansion/compression with exact tensor-product sums for every axis
processing order in a small example, and compare the complete padded CRT map
with its algebraic exponent oracle. These test correctness of finite examples;
the asymptotic count and tape bound are the written proof plus upstream lemmas.

## Remaining review boundary

No obstruction was found in this audit. The outstanding independent review
should concentrate on the two changed schedules and the substitution of the
new margin into all uses of the layout bound. The upstream swap implementation,
finite-network interfaces, and analytic reductions retain the same conditional
status as before. Neither the finite tests nor the certificates independently
prove those interfaces. This audit does not claim optimality for the improved
layout accounting.
