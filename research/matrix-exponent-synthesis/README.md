# Strict parameter refinement above PR #58

The new conditional saving is
`kappa = 59384196136667/1250000000000000000 = 4.75073569093336e-5`,
strictly above PR #58's `475073569/10000000000000 = 4.75073569e-5`
and its old scoped limit `1187740349/25001187740349`.
The improvement is `9.3336e-15`. It uses finer certified bit saving
`475096139655209/10000000000000000000` and positive backoff `h=1e-18`.
This is a parameter refinement of the same network. Matrix/parity constructions
and all-cardinality matching certificates are additional research tools, with
the precise applicability and remaining physical-child obstruction in the paper.

# Matrix circuits, parity arithmetic and certified exponent search

This package is the local review edition of Alejandro Zarzuelo Urdiales's
matrix/parity synthesis. The paper source is `matrix-exponent-synthesis.tex`.
The candidate's exact current witness, benchmark pin and verification status
are in `candidate/README.md`, `candidate/arithmetic.json` and its receipts.
Read those current files before claiming a numerical frontier result.

The exact 2,208-product matrix circuit is a mixed-input commutative scalar
schedule. It is not tensor rank 2,208 or an uncharged replacement for a linear
interchange child. The conditional exponent witness comes from a PR #58 inherited
bit-network profile. Known Dumas-Pernet-Sedoglavic, Rosowski, Gaussian
three-product and matching-duality ingredients retain their prior-work credit.

## Reproduce the arithmetic and certificate checks

Requirements: Python 3.11+ standard library and Lean 4.31.0 with bundled Std.
The original matrix proof archive uses its separate pinned Mathlib/Lean
4.33.1 toolchain; its historical CI evidence is included, and is not described
as a fresh local recompilation here.

```
lake build
python run_checks.py --work work/recheck
```

Use a fresh work directory for another run: some independent audit receipts
intentionally refuse to overwrite existing evidence. No SciPy, compiler or
network is needed for these delivered arithmetic checks and dual replays.
The matching discovery helpers use SciPy; discovery is excluded from the
trusted integer/rational certificate replay.

The current refinement uses PR #58 construction commit
`bc2f7ed4c20dc18898305ab17165c0c995cbb804` (current PR head adds a
validation receipt only). Run `python candidate/verify_refinement.py --upstream
/path/to/pinned/pr58` for fresh parameter arithmetic. This does not replay the
inherited physical graph, wrapped words or data sweep. Those checks are reused
from PR #58, as stated in its public completion receipt.

The 171 standalone theorem endpoints combine the unchanged, previously checked
matrix/parity/search toolkit with 11 fresh concrete frontier theorems and the
four generic rational-interface theorems. Historical matrix and catalogue
receipts are background evidence; they are not fresh PR #58 network validation.
The paper source is supplied without a newly compiled PDF.

## Concrete interfaces

`gaussian_matrix.multiply16` evaluates the pinned flat certificate on 256-entry
canonical Gaussian matrices. `hierarchical_gaussian_matrix.multiply16_hierarchical`
retains the actual 48-by-46 DAG sharing. Both align inputs to Pi tag E and return
canonical values on the mathematically necessary product tag 2E. All final
coordinate numerators divide by eight exactly. The shared reference schedule
uses 57,696 component additions rather than the flat interpreter's 193,568;
alignment, normalization and physical tape costs remain separately charged.

`LateQuotient.lean` proves exact recovery modulo 2^p from a denominator-cleared
numerator computed modulo 2^(p+3). `SharpQuotient.lean` proves the numerator-only
precision boundary. `CommutingPhases.lean` proves raw XOR-phase commutation
with equal charged denominator tags and a gauge incompatibility witness.
Exact operator tests also show that mixed linear forms can leave the eligible
phase-child class despite staying inside a commutative operator algebra.

## Search certificates and formal boundaries

The typed catalogue rejects unsupported coefficient domains, mixed leaves
used as block-stable outers, false rank claims and unpaid lifted arithmetic.
Its minima are minima in the supplied finite catalogue, not global records.

`catalogue/MATCHING_SEARCH.md` documents two exact certificate objectives.
The original objective has a maximum-cardinality penalty. The new complete
fixed-target feasibility slack includes external roles and changes in wire
normalization, uses zero-cost private unmatched columns, and permits every
cardinality. Integer primal/dual equality proves the recorded quantized
fixed-DAG optimum; rational intervals bound remaining true-cost regret.
Neither assertion proves global network or exponent optimality.

`MatchingDual.lean` proves generic exact weak duality and optimality from
explicit edge, row and column-partition contracts. `FeasibilityNormalForm.lean`
proves the all-cardinality bookkeeping identity. The finite graph/source binding
is independently checked by Python. `RefinedFrontierCertificate.lean` derives the
actual rounded moment envelope and checks the 47 slacks and strict benchmark
comparisons. `FiniteRationalChecks.lean` states the enclosure contracts; the full
transcendental and physical interface scope is stated in the paper and candidate
receipts. `AuditAll.lean` prints dependencies for every standalone theorem.

There are no omitted proofs, new project axioms or native decision shortcuts.
The full multiplication theorem remains conditional on inherited analytic,
ordered-affine compiler, fixed-tape, setup, recovery and eventual-threshold
arguments. Neither finite replay nor the new Lean modules implies peer review
or measured hardware speed.

## Provenance

Alejandro Zarzuelo Urdiales is the author and human developer. His earlier
Archivara exploration and July matrix generalization were developed personally
with multiple AI tools, most recently GPT-6.1 as recorded by the author. The
current synthesis, proofs, implementations and search involved substantial
OpenAI Codex assistance. The actual matrix source and 45-endpoint proof evidence
are pinned at `alejandrozu/openmath-2026-judging`, commit
`7203497dc990e47c2391bff1b9863408d817faeb`, with proof edition
`9e13c89a51a62958ced9ebdf16da31f5e2fb3cdd`.

Community credit and source/license notices are retained in the candidate
README and source manifests. New material follows the destination's Apache-2.0
license; copied original source/evidence retains its attribution and scope.
