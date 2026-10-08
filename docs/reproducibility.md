# Reproducing the current result

Run from the repository root with Python 3.11+, a C++ compiler supporting
C++17 and unsigned 128-bit integers (GCC or Clang), Git, and Make.
No third-party Python package or network access is required for verification.

```sh
make structured-bulk-verify
```

This incremental target checks the selected additions:

- Regenerates the original-envelope bit producers needed for the new h36
  rank histogram and h30 fixed-basis profile. The unchanged h32 positive
  producer counts are matched to the preceding verified certificate.
- Reconstructs the h30 physical transition multiset, computes its exact
  modular pivot profiles, and checks the bounded-minor CRT certificate.
  This is deterministic exactness, not random sampling.
- Regenerates the mixed-center complex producers `(h,d)=(30,19)` and `(40,35)`;
  the first is used on two tensor axes. Checks supports, scalar coefficients,
  binary frames, carrier counts and complete histograms.
- Reconstructs both full recursive child lists and certifies their moments,
  the semantic precision induction, product row stock, seven assembly margins
  and all 47 strict inequalities with exact arithmetic.

The h30 profile computation is the largest new check and may take several
minutes. It stores many 30-by-30 modular matrices. Intermediate graphs and
executables are temporary by default; `--work-dir PATH` preserves them:

```sh
python3 scripts/structured_bulk_producer.py --work-dir /tmp/structured-bulk-producers
```

`make verify` runs this target and all inherited checks. Unchanged historical
producers and regression suites are not rerun for the incremental target.
For arithmetic alone, use `make structured-bulk-certificate`.

## Proof and dependencies

The current proof is supplied as [LaTeX source](../notes/structured-bulk-note.tex).
This submission does not include a compiled PDF. Optional local compilation
is available with `make structured-bulk-note`, using pdfLaTeX by default or
`TEX_ENGINE=tectonic`.

The [adopted proof sources](../references/semantic-bulk/README.md)
include the selected PR #23, PR #21 and RaD arguments, their original notices,
and a hash manifest. Generic simultaneous basis existence and the analytic
interfaces are written proofs, separate from the finite checks.

[SOURCES.json](../SOURCES.json) pins the source commits, archive and immediate
parent. Original archives, alternate constructions and exploratory files are
kept outside the submission. The [historical manuscript patch](../PATCHING.md)
remains the inherited #10 result.
