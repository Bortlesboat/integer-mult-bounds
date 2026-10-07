# Draft routing-improvement release

Repository: [CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds)

Suggested description:

> Conditional exponent improvements for integer multiplication, with exact rational certificates, source patches, and proof dependency audits.

Suggested release title: **Direct axis routing: conditional exponent saving 2^-78**

## Release body

This research draft improves the axis-routing schedule in OpenAI's
*Integer multiplication below n log n*. Its strongest supplied witness is
`kappa = 2^-78` in `O(n (log n)^(1-kappa))`, for the manuscript's
fixed-alphabet, fixed-tape Turing-machine model.

Direct nonadjacent swaps reduce the number of layout interchanges from O(d²)
to O(d). The revised cost permits a fixed dimension exponent, removing the
cubic constraint behind our earlier parameter-only ceiling. The finite
network and numerical operations are retained from our h = 46 construction.

New artifacts:

- A routing research note and dependency audit.
- An exact rational certificate for the 2^-78 witness, plus a 2^-107 witness
  using the original network and recurrence exponents.
- Three independent source patches, including a routing-only alternative.
- Finite checks of coordinate permutations, padding, coefficient records,
  CRT order, and parameter constraints.

The earlier parameter-only note, certificates, and seven patches remain
available. Its ceiling applies to the original cost accounting. No ceiling
or optimality claim is established for the revised accounting.

The full upstream multiplication theorem remains an assumption. The exponent
comparison does not imply a practical speedup. Independent review is welcome.

Author: Douglas Colkitt, with assistance from OpenAI Codex. Apache-2.0 licensed.

## Publication details

Attach `artifacts/nonadjacent-axis-note.pdf` if publishing a release. Add a
release version and date to citation metadata when a release is actually
published. This draft does not create a GitHub release or post an announcement.
Suggested thread: [announcement.md](announcement.md).
