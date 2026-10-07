# A sharper exponent for integer multiplication

**Research draft by Douglas Colkitt — conditional on the underlying manuscript.**

This repository improves the parameters and axis-routing schedule in OpenAI's
[*Integer multiplication below n log n*](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integer-multiplication-below-n-log-n-September-23-2026)
(result family #109). Subject to its algorithmic interfaces and the construction
changes audited here, the strongest supplied bound is

$$
T(n)=O\!\left(n(\log n)^{1-\kappa}\right),\qquad
\boxed{\kappa=2^{-78}\approx3.309\times10^{-24}}.
$$

The computational model is the manuscript's fixed finite-alphabet Turing machine
with a fixed finite number of one-dimensional tapes. The original manuscript
uses `kappa = 2^-182`. The new witness increases the exponent saving by about
570 million times over our earlier parameter-only witness `kappa = 5.8e-33`.
These are asymptotic exponent comparisons, not measured practical speedups.

**[Read the routing note (PDF)](artifacts/nonadjacent-axis-note.pdf)** ·
[Review the 2^-78 patch](patches/h46-nonadjacent-78.patch) ·
[Inspect the routing audit](docs/nonadjacent-axis-audit.md) ·
[Reproduce the checks](docs/reproducibility.md)

## What changes

The new routing schedules use direct nonadjacent swaps already supported by
the manuscript. CRT axis reversal needs floor(d/2) field interchanges; exposing
and restoring all resampling axes needs at most 2(d-1). This replaces the
original O(d^2) count of adjacent moves by O(d) full-field interchanges.
The finite network and numerical operations remain the same as in our earlier
h = 46 construction. The exact sequence of data-movement operations changes.

The normalized layout cost improves from `d^2(1 + ell^tau)` to
`d(1 + ell^tau)`. Its exponent margin therefore becomes

$$
g_4=(1-\tau)(1-\epsilon),
$$

which permits a fixed dimension exponent `epsilon = 1/40`. With
`a = 9/500000000000`, the other choices are

$$
\tau=\sigma=1-a,\quad \beta=\frac12,\quad c=\frac a2,\quad
\lambda=1-\frac{3a^2}{4},\quad \lambda'=1-\frac{a^2}{2},\quad
\delta=\frac1{16},\quad C_1=20.
$$

Exact rational arithmetic gives

$$
\min_i g_i=\frac{a^2}{80}=4.05\times10^{-24}>2^{-78}.
$$

The [routing audit](docs/nonadjacent-axis-audit.md) checks coordinate order,
padding, coefficient records, fixed tapes, descriptor costs, precision, and
all remaining parameter dependencies. The routing change itself uses primitives
already present in the source. With OpenAI's original network and recurrence
exponents unchanged, it also supports the simpler bound **kappa = 2^-107**.

## The earlier parameter-only result and its ceiling

Our [first note](artifacts/parameter-note.pdf) gives `kappa = 5.8e-33` under
the original layout cost accounting. Within the stated network-counting
family and those cost inequalities, it establishes `kappa < 5.838e-33`, even
allowing variable `beta` and unequal `tau` and `sigma`. The exact search covers
every admissible integer h, using a decreasing bound for the infinite tail.

That ceiling remains valid for its stated assumptions. The original layout
cost forced `epsilon < a`, yielding a cubic constraint `kappa < a^3`.
The new schedules improve that cost and remove the restriction. With a fixed
epsilon, the supplied saving instead scales quadratically in a. We do not
claim that quadratic dependence is unavoidable or that 2^-78 is optimal for
the revised accounting.

## What has been checked

| Component | Status |
| --- | --- |
| Parameter inequalities and logarithm bounds | Exact rational certificates |
| Network-counting search and its infinite tail | Exact rational certificates |
| Nonadjacent routing, parameter dependencies, and earlier variable-beta extension | Written mathematical audits |
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

To rebuild the routing PDF, install Tectonic and run `make audit-note`;
`make note` rebuilds the earlier parameter-only note. The first run may
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
| [h46-rational](patches/h46-rational.patch) | `5.8e-33` | Strongest supplied parameter-only witness |
| [nonadjacent-layout](patches/nonadjacent-layout.patch) | Original parameters retained | Routing proof and revised layout cost only |
| [frozen-nonadjacent-107](patches/frozen-nonadjacent-107.patch) | `2^-107` | Direct routing, original network and recurrence exponents |
| **[h46-nonadjacent-78](patches/h46-nonadjacent-78.patch)** | **`2^-78`** | **Direct routing with the h = 46 network** |

Machine-readable results are in [parameters.json](certificates/parameters.json), [network-search.json](certificates/network-search.json), and
[nonadjacent-axis.json](certificates/nonadjacent-axis.json). The first note also gives
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
