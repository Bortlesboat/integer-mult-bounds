# Draft initial GitHub release

Repository: [CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds)

Suggested description:

> Conditional exponent improvement for integer multiplication, with exact rational certificates, source patches, and a proof dependency audit.

Suggested release title: **Initial research draft: conditional exponent saving 5.8e-33**

## Release body

This research draft gives a conditional parameter improvement to OpenAI's
*Integer multiplication below n log n*. Its strongest supplied witness is
`kappa = 29/(5 * 10^33) = 5.8e-33` in `O(n (log n)^(1-kappa))`, for the
manuscript's fixed-alphabet, fixed-tape Turing-machine model.

Included artifacts:

- A research note with the parameter substitution and variable-beta argument.
- Seven alternative patches against an immutable upstream revision.
- Exact rational certificates and a network search with an infinite-tail bound.
- A dependency audit that separates checked implications from assumed interfaces.
- Automated numerical, finite-identity, source-integrity, and patch checks.

The stated network-counting and seven-margin family has a certified ceiling
below `5.838e-33`. This restricts the current estimates, not other algorithms.
The full upstream multiplication theorem remains an assumption.

Author: Douglas Colkitt, with assistance from OpenAI Codex. Apache-2.0 licensed.

## Publication details

Attach `artifacts/parameter-note.pdf` to the release. The repository URL is recorded in `CITATION.cff`; add a release version and
date when a release is actually published. A DOI can be added later if an archived release receives one.

The preparation itself does not create a remote repository, publish a release,
or claim independent review. The short public announcement is drafted in
[announcement.md](announcement.md).
