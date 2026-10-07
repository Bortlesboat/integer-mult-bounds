# A sharper exponent for integer multiplication

**Research draft by Douglas Colkitt — conditional on the underlying manuscript.**

This repository gives a parameter improvement to OpenAI's
[*Integer multiplication below n log n*](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integer-multiplication-below-n-log-n-September-23-2026)
(result family #109). Subject to its algorithmic interfaces and the construction
changes audited here, the improved bound is

$$
T(n)=O\!\left(n(\log n)^{1-\kappa}\right),\qquad
\boxed{\kappa=\frac{29}{5\cdot10^{33}}=5.8\times10^{-33}}.
$$

The computational model is the manuscript's fixed finite-alphabet Turing machine
with a fixed finite number of one-dimensional tapes. The original manuscript
uses `kappa = 2^-182`; our exponent saving lies between `2^-108` and `2^-107`.
This is an asymptotic exponent improvement, not a measured practical speedup.

**[Read the research note (PDF)](artifacts/parameter-note.pdf)** ·
[Review the parameter-only patch](patches/h46-rational.patch) ·
[Inspect the proof audit](docs/audit.md) ·
[Reproduce the checks](docs/reproducibility.md)

## What changes

The construction keeps the manuscript's conceptual algorithm and changes four
ingredients: its finite-network parameter to `h = 46`, its common recurrence
saving to `a = 9/500000000000`, its stopping exponent to `beta = 999/1000`,
and its final absorption argument to use any fixed positive margin.

The remaining explicit choices are

$$
\epsilon=\frac{999a}{1000},\quad c=\frac{998a}{1000},\quad
\tau=\sigma=1-a,\quad \lambda'=1-ac,\quad
\lambda=\frac{\lambda'+(1-a)(1+c/\beta)}{2}.
$$

Exact rational arithmetic gives

$$
\min_i g_i=5.814515664\times10^{-33}>\kappa.
$$

The [note, Sections 7–8](artifacts/parameter-note.pdf) proves the variable-stopping
extension, checks the witness, and explains the limit of further tuning.

## How much room remains?

Within the stated network-counting family and seven-margin cost accounting,
we establish `kappa < 5.838e-33`, even allowing variable `beta` and unequal
`tau` and `sigma`. The supplied witness exceeds 99% of this upper bound.
The search covers every admissible integer `h`, using exact logarithm intervals
for `h < 200` and a decreasing bound for the infinite tail.

This ceiling limits what these estimates can certify. It is not a lower bound
for integer multiplication or an obstruction to other finite networks or
sharper cost analyses. See the [scope and derivation](docs/audit.md#rational-saving-variable-beta-and-strict-final-slack).

## Follow-up audit: nonadjacent axis routing

A separate [routing audit](docs/nonadjacent-axis-audit.md) changes the layout
cost assumption behind the parameter-only ceiling above. The source already
provides nonadjacent swaps, allowing O(d) field interchanges for CRT reversal
and axis exposure instead of O(d^2) adjacent moves. With the other dependencies
audited, exact witnesses support **kappa = 2^-78** using h = 46, or **2^-107**
with the original network and recurrence exponents unchanged.

Read the [follow-up note](artifacts/nonadjacent-axis-note.pdf),
[routing-only patch](patches/nonadjacent-layout.patch), or
[combined 2^-78 patch](patches/h46-nonadjacent-78.patch). These bounds remain
conditional on the upstream algorithmic interfaces. The earlier note and
its ceiling are retained as results about the original cost accounting.
The follow-up does not claim optimality for the revised accounting.

## What has been checked

| Component | Status |
| --- | --- |
| Parameter inequalities and logarithm bounds | Exact rational certificates |
| Network-counting search and its infinite tail | Exact rational certificates |
| Variable stopping exponent and parameter dependencies | Written mathematical audit |
| Selected finite identities | Exhaustive small cases and deterministic sampled tests |
| Source patch application | All ten alternatives checked |
| Full upstream multiplication theorem | Assumed; not independently established here |

The scripts do not constitute a formal proof of the complete algorithm. This
repository contains no full multiplication-machine implementation or Lean
formalization of the claimed bound. Independent review is welcome, especially
of the finite-network interfaces and fixed-tape recurrence. See
[the audit's remaining work](docs/audit.md#what-remains-before-an-unconditional-claim).

## Reproduce

From the repository root, with Python 3.11 or newer, Git, and Make:

```sh
make verify
```

The mathematical checks use the Python standard library and bundled source;
no package installation or network access is needed. The command regenerates
the certificates and patches, runs the tests, verifies upstream hashes, and
checks each patch against the pinned manuscript. On a clean checkout, generated
files should have no changes:

```sh
git diff --exit-code -- certificates patches
```

To rebuild the PDF, install Tectonic and run `make note`. Its first run may
download TeX resources. See [reproducibility details](docs/reproducibility.md)
for individual commands and how to apply a patch in a disposable copy.
[GitHub Actions](.github/workflows/verify.yml) runs the numerical and patch checks.

## Alternative patches

Each patch applies independently to the unmodified pinned source.

| Patch | Certified conditional saving | Scope |
| --- | --- | --- |
| [frozen-154](patches/frozen-154.patch) | `2^-154` | Original network and recurrence exponents |
| [balanced-153](patches/balanced-153.patch) | `2^-153` | Balanced assembly parameters |
| [same-network-129](patches/same-network-129.patch) | `2^-129` | Original network, sharper recurrence comparison |
| [h46-111](patches/h46-111.patch) | `2^-111` | Smaller network, dyadic parameters |
| [h46-109](patches/h46-109.patch) | `2^-109` | Rational recurrence saving, strict final margin |
| [h46-108](patches/h46-108.patch) | `2^-108` | Variable stopping exponent |
| **[h46-rational](patches/h46-rational.patch)** | **`5.8e-33`** | **Strongest parameter-only witness** |

Machine-readable results are in [parameters.json](certificates/parameters.json)
and [network-search.json](certificates/network-search.json). The note also gives
a closed-form supremum for the earlier fixed-`beta` parameter problem.

## Attribution, citation, and license

Author: **Douglas Colkitt**. The research, implementation, and drafting were
performed with assistance from OpenAI Codex. This assistance is not independent
review or endorsement by OpenAI. No priority claim is made.

The original manuscript is by OpenAI. Its source is pinned at commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, with URLs and SHA-256 hashes in
[upstream/manifest.json](upstream/manifest.json). The files under `upstream/`
are preserved unchanged; modifications are distributed as separate patches.

Use [CITATION.cff](CITATION.cff) for this project and also cite the
[upstream manuscript](upstream/README.md) when discussing the multiplication
bound. Until a release is archived, include the repository commit you used.

Licensed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) for attribution and
[CONTRIBUTING.md](CONTRIBUTING.md) for review and contribution guidance.
