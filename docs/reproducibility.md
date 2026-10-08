# Reproducing the current result

Run from the repository root with Python 3.11+, a C++17 compiler, Git, and Make.
No third-party Python package or network access is required for verification.

```sh
make endpoint-gauge-verify
```

This regenerates the new binary and complex scalar producers at `(32,30,40)`,
checks their supports, frame assignments, carrier matchings and complete rank
histograms, and compares them with the selected input data. The bit construction
uses the retained ordinary paired base threshold; the complex construction uses
threshold two. These are distinct producers with distinct counts and losses.

The exact certificate reconstructs both recursive call lists, encloses both
characteristic moments with rational arithmetic, checks the updated precision
guard, and evaluates 29 strict constraints and seven assembly margins. Small
exact algebra checks cover alternating and signed residuals and endpoint phase
normalization. Basis checks cover coordinate prescriptions and both A5 trees;
remaining generic-minor and interface arguments are in the proof.

`make verify` runs the new checks together with all inherited producers, tests
and historical patch checks. Unchanged inherited checks need not be repeated
when validating only this extension.

Large intermediate graph and label files are temporary. To retain them:

```sh
python3 scripts/endpoint_gauge_producer.py --work-dir /tmp/endpoint-gauge-producers
```

Portable sources are in `scripts/endpoint_gauge/`, with inherited helpers in
`scripts/partial_swap/` and the retained circuit modules. The selected counts
are in `certificates/endpoint-gauge-bit-axes.json` and
`certificates/endpoint-gauge-complex-input.json`.

For exact arithmetic alone:

```sh
make endpoint-gauge-certificate
```

The certificate uses exact rational numbers. Rounded prose values are
explanatory. On a committed checkout, generated artifacts can be checked with
`git diff --exit-code -- certificates patches`.

## Proof PDF

```sh
make endpoint-gauge-note
# Alternatively:
make endpoint-gauge-note TEX_ENGINE=tectonic
```

The target produces `artifacts/endpoint-gauge-note.pdf`; the default engine is
pdfLaTeX. PDF bytes can differ across TeX environments. The standalone note is
the current proof. The [combined manuscript patch](../PATCHING.md) remains
the inherited #10 result.

## Provenance

[SOURCES.json](../SOURCES.json) records the new archive hash, parent commit,
and retained source pins. The original archive and exploratory alternatives
are preserved outside this submission. Copyright notices, licenses and the
Gaussian scaling correction are retained. The GitHub workflow runs the full
`make verify` target and checks certificate/patch reproducibility.
