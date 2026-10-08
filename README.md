# A sharper exponent for integer multiplication

**Research draft by Douglas Colkitt — conditional on the underlying manuscript
and the written extensions supplied here.**

This draft improves OpenAI's
[*Integer multiplication below n log n*](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integer-multiplication-below-n-log-n-September-23-2026)
(result family #109). In its fixed finite-alphabet Turing-machine model with a
fixed number of one-dimensional tapes, the strongest supplied witness is

$$
T(n)=O\!\left(n(\log n)^{1-\kappa}\right),\qquad
\boxed{\kappa=2^{-31}\approx4.6566\times10^{-10}}.
$$

This integrated follow-up increases the exponent saving by approximately
**5.61 times** over the preceding `83/10^12 > 2^-34` witness. Comparing the
simpler dyadic statements gives `2^-31 / 2^-34 = 8`. The original manuscript
uses `2^-182`. These compare asymptotic exponents, not practical runtimes.

**[Read the complex-network proof note (PDF)](artifacts/complex-compression-note.pdf)** ·
[Review the combined source patch](patches/complex-compression-31.patch) ·
[Inspect the exact certificate](certificates/complex-compression.json) ·
[Review guide and dependencies](docs/research/complex-compression-review.md)

This is a research claim supported by written proofs and reproducible checks.
The complete upstream theorem is assumed; the new arguments have not received
independent mathematical review or formal verification.

## What changed

The preceding compact-control construction removed the movement penalty for
spaced windows. This follow-up improves the **complex finite network** used
inside that construction, keeping the bit network and compact-control proofs.

Weighted rectangle circuits compress the disjoint-triple correction, while
shared sums compress the intersection-two correction. Compatible binary
phase frames, signed arithmetic and a transparent computation schedule preserve
arbitrary auxiliary inputs. A matching reuses complete first/third-stage
auxiliary banks without additional residual loss.

At `h_c=26`, the complex saving is certified at `a_c=5e-9`, exceeding the
retained bit saving `a_b=2.96e-9`. The combined patch integrates the new
network, separate arities, scalar-operation guard charge, recurrence and
final parameter witness. Its exact minimum assembly margin is

$$
G_* = \frac{5771}{10^{13}} = 5.771\times10^{-10}>2^{-31}.
$$

The **bit interface now limits the result**. With that certified bit saving
and the retained Gaussian assembly constraint, `kappa<a_b/5=5.92e-10<2^-30`.
This is a scoped ceiling for the retained choices, not for other networks or
integer multiplication in general. The new complex construction already
supplies headroom for a stronger bit network.

The preceding [compact-control note](artifacts/compact-control-note.pdf) and
[patch](patches/compact-control-34.patch) remain unchanged.

## Evidence and scope

| Component | Evidence |
| --- | --- |
| Parameters, logarithm enclosures, final margins | Exact rational certificate |
| Dirty-control identities, inverses and repair | Finite exhaustive cases and seeded tests |
| Wider-control tape bound, reservations and recursion | Written general proofs |
| Compressed complex circuit, binary phase frames and precision guard | Written proofs, exact scalar tests and accounting |
| Source integration | Combined patch, reference checks and manuscript build |
| Full upstream multiplication theorem | Assumed |
| Independent review / full formalization | Not supplied |

The [review guide](docs/research/complex-compression-review.md) identifies the new
proof obligations and their tests. [Current research status](docs/research/current-status.md)
is authoritative when older notes describe superseded barriers or hypothetical
witnesses. The earlier artifacts remain available and unchanged.

## Reproduce

With Python 3.11 or newer, Git and Make, run from the repository root:

```sh
make verify
git diff --exit-code -- certificates patches
```

No third-party Python packages or network access are needed for these checks.
They regenerate the certificates and patches, run the tests, verify upstream
hashes, and check each patch against the pinned manuscript. The second command
checks exact regeneration on a clean checkout.

With Tectonic installed, rebuild the latest note using:

```sh
make complex-note
```

The output is `artifacts/complex-compression-note.pdf`. The first PDF build may
download TeX resources. See [reproducibility instructions](docs/reproducibility.md)
for applying the combined patch in a disposable copy and building older notes.
[GitHub Actions](.github/workflows/verify.yml) runs the arithmetic and patch checks.
Passing tests does not establish the complete multiplication theorem; this
repository contains no full multiplication-machine implementation.

## Witnesses and independent patches

Each patch applies independently to the **unmodified** pinned source; they are
alternatives, not a sequence to apply together. The
[result history](docs/research/result-history.md) records the earlier mechanisms
and scoped ceilings.

| Patch | Conditional saving | Scope |
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
| [h46-nonadjacent-78](patches/h46-nonadjacent-78.patch) | `2^-78` | Direct routing with the h = 46 network |
| [h46-nonadjacent-76](patches/h46-nonadjacent-76.patch) | `2^-76` | Direct routing with tuned dimension and stopping parameters |
| [h46-shared-side-75](patches/h46-shared-side-75.patch) | `2^-75` | Stage-1/stage-3 side-role sharing, routing, and parameter tuning |
| [h46-incidence-67](patches/h46-incidence-67.patch) | `2^-67` | Rectangle incidence circuits, full auxiliary sharing, routing, and parameter tuning |
| [h46-dag-63](patches/h46-dag-63.patch) | `2^-63` | Shared intermediate sums and reversible role allocation |
| [h46-shared-point](patches/h46-shared-point.patch) | `13*2^-66` | Cross-group sharing |
| [h50-paired-59](patches/h50-paired-59.patch) | `2^-59` | Paired sums, stopped guard and tighter Gaussian setup |
| **[compact-control-34](patches/compact-control-34.patch)** | **`83/10^12 > 2^-34`** | **Compact controls, complete reservations, local repair and separate complex arity** |
| **[complex-compression-31](patches/complex-compression-31.patch)** | **`2^-31`** | **Weighted complex circuits, binary phase frames and complete auxiliary sharing** |

## Attribution, citation, and license

Author: **Douglas Colkitt**. Research, implementation and drafting were performed
with assistance from OpenAI Codex. The compact-control proposal originated
with a separate research agent; the supplied note develops its tape, layout,
repair and assembly arguments. AI assistance is not independent review or
endorsement by OpenAI. No priority or unrestricted optimality claim is made.

The original manuscript is by OpenAI, pinned at commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Source URLs and SHA-256 hashes are in
[upstream/manifest.json](upstream/manifest.json). Files under `upstream/` remain
unchanged; modifications are supplied as separate patches.

Use [CITATION.cff](CITATION.cff) and also cite the
[upstream manuscript](upstream/README.md). Until a release is archived, include
the repository commit used. Licensed under [Apache-2.0](LICENSE); see
[NOTICE](NOTICE) and [CONTRIBUTING.md](CONTRIBUTING.md).
