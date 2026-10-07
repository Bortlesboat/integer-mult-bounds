# Proof dependency audit

The frozen-network parameter substitutions pass the numerical and asymptotic
dependency audit against commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
No contradiction was found in the reviewed main proof chain. This is a first
mathematical review, not independent verification of every algorithmic lemma.
The unconditional multiplication theorem remains unvalidated in this project.

## Frozen network patch

The recommended patch uses

\[
\epsilon=c=2^{-51},\quad
\lambda=1-3\cdot2^{-102},\quad
\lambda'=1-2^{-101},\quad
\kappa=2^{-153}.
\]

It keeps h, both networks, tau, sigma, beta, delta, C1, input precision p = 6b,
all numerical error thresholds, and the seven cost terms fixed.
The weaker 2^-154 patch retains the user's proposed lambda and lambda prime.

The upstream `prop:simultaneous-layer` explicitly allows new positive rational
c, epsilon, lambda and lambda prime under its stated inequalities. Consequently
the frozen substitutions do not need a generalized version of that proposition.

Two previously displayed numerical estimates become false after substitution:

- `tau(1+2c) < 1-31*2^-55`. Its new value is exactly `1-2^-100`.
- `g4 > 2^-51`. Its new value is `2^-51 - 2^-101`, which is greater than `2^-52`.

Both are corrected in the patches. The exact integer-root comparison in setup
is also updated from exponent `2^75` to `2^51`. Thus “every displayed inequality
still holds” should mean the underlying constraint system, not every old
parameter-specific estimate.

## Parameter dependency ledger

Paths in this table are relative to `upstream/build/sections/`. Labels are the
upstream LaTeX labels, so they remain useful if line numbers change.

| Source and anchor | Dependency | Disposition |
| --- | --- | --- |
| `03-motifs.tex`, `eq:explicit-motif-exponents` | tau and sigma from finite rank deficits | Unchanged by frozen patches; counts reproduced exactly. |
| `04-swap.tex`, `prop:power-interchange` | s/W < m^tau, tau > 0 | Unchanged. Recurrence divided by logical volume has coefficient s/W. |
| `05-layers.tex`, `lem:packed-selected-bit-rectangle` | K/log p -> infinity; r dominates polynomials; d <= p | epsilon*c > 0 and epsilon < 1 retain all three. |
| `05-layers.tex`, “Unrolling the recurrence” | tau(1+2c) < lambda; sigma < lambda; max(lambda, sigma+(1-sigma)/2) < lambda prime | All slacks checked exactly. Strict gaps absorb geometric sums and the number of groups. |
| `05-layers.tex`, “An explicit guard-width bound” | C1 = 20; epsilon*C1 < 1 | Original counts reproduce nu = 11. New epsilon still gives d^20 = o(p). C0 is unchanged. |
| `05-layers.tex`, `prop:simultaneous-layer` | Fixed rational parameters, uniform comparison bands | Quantifiers already permit both frozen substitutions. A common cutoff may increase. |
| `06-transforms.tex`, `lem:synthetic-transform-cost` | 1 <= K <= ell-1; d*ell = O(p); r superpolynomial | 1-epsilon-epsilon*c > 0 yields K=o(ell); input size construction gives the other requirements. |
| `06-transforms.tex`, `lem:signed-ring-product` | r < 2^p and O(p)-bit components | Unchanged; the existing O(N log N) multiplier is used, so there is no recursive appeal to the proposed result. |
| `07-resampling.tex`, `lem:no-sort-resampling` | delta in (0,1/8), alpha < sqrt(p), theta > p/alpha^4, coprime s,t | delta is unchanged; the source-size calculation retains all hypotheses. |
| `07-resampling.tex`, `lem:tensor-resampling` | Polynomial per-line setup dominated by r; d polynomial in p | Retained for fixed 0 < epsilon < 1. |
| `08-assembly.tex`, `eq:sizes` | d = Theta(p^epsilon), K = Theta(p^(epsilon*c)), ell = Theta(p^(1-epsilon)) | Floors affect constants only beyond a common cutoff. |
| `08-assembly.tex`, `eq:gamma` and prime lengths | epsilon < 1/12; 1-2*epsilon > 0 | alpha exponent < 1/2; gamma exponent <= 2/3; prime intervals eventually contain enough primes. |
| `08-assembly.tex`, setup example | Rational-power computation must match new epsilon | Explicit fixed integer exponent updated. Trial division remains n^o(1). |
| `08-assembly.tex`, `eq:final-error` | gamma = o(b), T < 2^b, p = 6b | Retained. Final rounding error remains eventually below 1/2. |
| `08-assembly.tex`, `eq:margin-list` | Seven normalized costs | New minima certified exactly; all >= 2*kappa. |
| `08-assembly.tex`, exceptional-stream total | p^A visits and p^A' * 2^-K -> 0 | A and A' remain fixed; epsilon*c > 0 suffices even for extremely small exponents. |
| `09-exact-arithmetic.tex`, downstream corollary | 0 < kappa < 1 | No parameter-specific literal needs changing; not a dependency of multiplication. |
| `10-transposition.tex`, downstream corollary | log log n = o((log n)^(1-kappa)) | Retained; not a dependency of multiplication. |
| `11-grouped-rectangles.tex`, grouped variant | Same packed-gadget growth assumptions | Unchanged; the main layer uses the rectangular version directly. |

## Review of unchanged proof mechanisms

### Finite networks and rank accounting

The scalar cancellation coefficients reduce to intersection sizes 0, 1, 2, 3.
The forward schedule restores arbitrary auxiliary values; the three bank updates
give the signed swap. Neighbor counts are checked by independent enumeration
for small h, including both ordered intersection rules.

The subspace proof assigns common frames at every gate. Comparable nondegenerate
labels give rank equal to residual dimension. The rational interface must include
the extra N ranks caused by changing the X-source projection to its negative;
the checker includes this term. The complex deficit is instead 2N-2Lc.

The binary phase argument uses weight additivity modulo four on orthogonal
vectors and odd weights of an orthonormal basis. The endpoint tensor weight
is 27. The supplied manuscript's scalar corrections distinguish the sign on
one role from a tensor of signs across columns; this distinction is necessary.
These symbolic arguments were reviewed, but the enormous concrete matrices and
all their bases have not been generated or independently machine-checked.

### Tape movement and recursion

The elementary operations work with implicit addresses, a fixed number of
collapsed fields, and complete Cartesian ranges. They do not charge unit cost
for arbitrary wide arithmetic. Controlled-shift setup is amortized against
the complete target range; descriptor polynomials are charged against a stream
or a polynomial record, as appropriate.

At a recursion node, all W roles, including scratch roles, are supplied by
existing rows. Each child has logical volume V/W. The manuscript's parking
schedule charges copying and restoring the parent's volume as node overhead,
with a fixed number of child calls. The parked ancestors are not swept on
every return. The normalization by W is the critical implementation assertion
to validate independently; finite identity tests cannot establish its time bound.

### Packed selected-bit operation

The eight-update scalar identity is checked exhaustively for control bits and
integers u,w in [-16,16]. Packed modular updates are checked on 4,500 deterministic
sampled triples over K = 6, 8, 10, f = 2, 3, 4 and every selected offset.
The checks include inversion, agreement with the intended XOR off the bad set,
and invariance of the bad set. Both good and bad addresses are exercised.

The proof uses bijectivity plus agreement outside an invariant set to justify
repairing only that set. The scan and radix-sort costs include the full record
payload and destination keys. Independent verification should preserve those
charges and the complete-range invariant after row splitting.

### Transform layout and precision

The forward transform retains bit-reversed frequency order and a positional
layout; pointwise multiplication respects their common record permutation.
The reverse transform consumes this order. Both transforms are normalized, so
the final scale M is required. The polynomial quotient introduces a negacyclic
wrap, which the coefficient twist cancels.

Signed coefficient packing was tested against direct polynomial convolution,
including negative coefficients. The source proof's centered extraction and
sign-extension carry identities were reviewed. This test is not an implementation
of the source's entire fixed-tape packing procedure.

The three source transforms produce convolution divided by S^2. Both factors
of S in assembly are required and were checked in the algebraic normalization.
The error bound includes the amplified ring error and the 2^gamma resampling
scale. Increasing epsilon within the certified bounds retains gamma=o(b).

### External analytic interfaces

The [45-page Harvey–van der Hoeven manuscript](https://www.texmacs.org/joris/nlogn/nlogn.pdf)
was consulted for the numerical map statements in Lemmas 4.8, 4.9 and 4.12,
the retained permutations in Proposition 4.7, and the prime-interval bound in
Lemma 5.1. Their displayed statements match the cited uses checked here.
This review did not reprove those analytic lemmas or audit every implementation
detail of their numerical routines. The source's removal of the two sorting
permutations and its replacement by the chirp identity remain part of the
algorithmic dependency chain to review independently.

## Network changes and optimization

For h = 100, the exact deficits certify a = 2^-42 using log(m) < 14. This changes
the explicitly fixed exponents in the end of `03-motifs.tex`, `04-swap.tex`,
`prop:simultaneous-layer`, and the assembly choices. The review patch
`patches/same-network-129.patch` makes these changes and adds an exact Taylor
partial-sum certificate for the logarithm comparison.

For h = 46, the exact counts and the guard exponent C1 = 20 are certified.
The rational form is nondegenerate (its exceptional eigenvalue is -37/9);
triple norms and the tensor weight 27 are unchanged; h > 6 preserves the spare
coordinates used to prove nonalternation. Both losses satisfy L < N/2.
The review patch `patches/h46-111.patch` updates six source files, including
all network counts, the exceptional eigenvalue, both loss ratios, the recurrence
comparison, and the guard-count constants. The symbolic construction dependencies
listed above survive at h = 46. The original algorithmic interfaces still need
independent validation; updating these constants is not a substitute for that.

The logarithm search uses exact rational intervals, not floating-point scores.
It separates h = 46 from every other admissible h in [7,199]. For h >= 200,
the bit-network bound a(h) < 1/(3*zb*m-1) excludes the infinite tail. The result
is restricted to the common-exponent counting problem. Separate tau and sigma,
alternative tensor depths, and alternative networks can change the optimum.

## Rational saving, variable beta, and strict final slack

The additional patches `h46-109.patch`, `h46-108.patch`, and
`h46-rational.patch` all use a = 9/500000000000. Exact logarithm enclosures
certify log(97336) < 5743/500, and each rank deficit exceeds a*(5743/500).
The inequality exp(-x) > 1-x therefore certifies both recurrence exponents.
The finite network and C1 = 20 are the same as in the h = 46 patch.

Every occurrence of the stopping parameter beta was checked in the source.
The indexed beta_j in Gaussian resampling is a different variable.
In `05-layers.tex`, the two assignments beta = 1/2 are replaced by a fixed
rational 0 < beta < 1 in the 108 and rational patches. The proof extends as follows:

- At an internal node e >= d^beta, K <= d^c <= e^(c/beta). The packed
  overhead is still O(e^lambda) under its stated strict inequality.
- At a leaf u < d^beta, the summed cost is bounded by
  e^sigma * d^(beta*(1-sigma)). A strict lambda-prime bound absorbs the
  logarithmic number of pieces.
- The initial row preprocessing is O(V log d) independently of beta.
  Row divisibility was arranged for the larger depth ceil(log_m d), which
  remains an upper bound; every leaf still has e <= d. Thus neither padding,
  the V/W child-volume argument, nor the guard-depth estimate changes.
- If beta = u/v, the stopping test compares integer powers e^v < d^u.
  These fixed powers take polynomial descriptor work, absorbed by r as before.
  They require no new growing collection of tapes or advice.

The assembly patches use G = min(g_i) and rho = G-kappa > 0. For every
fixed C, (log p)^C <= p^rho eventually, so p^(1-G) times the logarithmic
factor is at most p^(1-kappa). No factor-of-two slack is required.
The default checker retains the original half-margin requirement; the new
patches explicitly select strict-gap validation and, where needed, generalized
beta validation. Equality G = kappa is rejected.

For the strongest witness, beta = 999/1000, epsilon = 999a/1000,
c = 998a/1000, lambda-prime = 1-ac, and lambda is the midpoint between
lambda-prime and (1-a)*(1+c/beta). Exact arithmetic gives
G = 5.814515664e-33 > kappa = 5.8e-33. All seven margins and all recorded
asymptotic side conditions pass. The source's integer-root setup example is
updated to d^500000000000000 <= b^8991.

For the parameter ceiling put a = 1-tau. Positivity of g4 forces epsilon < a.
If c < a then ac < a^2. Otherwise beta < 1 and the packed-overhead condition
force 1-lambda-prime < a^2. Therefore min(g2,g3) < a^3, irrespective of sigma.
The bit-network saving alone is maximized at h = 46 by a separate exact
interval search, including the infinite h >= 200 tail. Its cubed upper
endpoint is below 5.838e-33 and below 2^-107. The present rational witness
exceeds 99% of that upper endpoint. This ceiling concerns only the stated
rank bounds, admissible h family, and seven-margin accounting. It does not
exclude improvements to the rank estimates, networks, or cost analysis.

## Validation of the new patches

`make verify` passes 20 tests, exact certificate regeneration, pinned-source
hash checks, and application checks for all seven alternative patches.
`make note` builds the updated seven-page research note without warnings.
All three new patched manuscripts also compile in disposable review copies
with Tectonic after commenting out the original three pdfTeX-only metadata
commands (`pdfinfoomitdate`, `pdftrailerid`, and `pdfsuppressptexinfo`). Those
preview-only edits are absent from the research patches. The manuscript
previews report two small overfull boxes in unchanged prose; the modified
parameter displays compile without layout warnings. These compilation checks
validate document construction, not the mathematical theorem.

## What remains before an unconditional claim

1. Independently validate the network rank interfaces and the fixed-tape
   recurrences, preferably as formal lemmas with explicit computational models.
2. Complete an independent review of the Gaussian-resampling implementation
   contracts and their composition with the retained permutations.
3. Independently review the h = 46 and a = 2^-42 patches, especially the finite
   subspace argument and its implications for the concrete recursive procedures.
4. Have a reviewer who did not produce this audit examine the conditional note
   and the underlying manuscript before making a public running-time claim.

The pinned formalization catalogue has no entry matching family 109 or this
manuscript title. This says what the catalogue lists; it is not a proof that no
related formalization exists elsewhere.
