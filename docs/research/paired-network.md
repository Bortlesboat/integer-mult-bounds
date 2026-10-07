# Conditional kappa = 2^-59

The new witness reaches **2^-59**, a factor **128/13 ≈ 9.85** above the
preceding 13*2^-66 result. It combines a smaller finite bit circuit with two
changes in the downstream proof. The computational model and the unchanged
upstream interfaces remain assumptions.

- [Proof note (PDF)](../../artifacts/paired-note.pdf)
- [Proof source](../../notes/paired-note.tex)
- [Independent upstream patch](../../patches/h50-paired-59.patch)
- [Exact certificate](../../certificates/paired-network.json)

## 1. Pair the vertices and retain their internal weights

The local side problem sums all input pairs avoiding two target points.
Partition the ground points into pairs. Aggregate cross-block edges into
coarse edges and put internal edges into coarse vertex weights. Recurse on
this weighted graph, carrying the vertex weights with it. A prefix/suffix
routine supplies the terms from the unexcluded vertex of each target block.
The remaining cross edge completes the output. These regions are disjoint.

Keeping internal weights inside the recursion removes a separate exclusion
circuit at each level. This is a change to the finite sum circuit, not merely
parameter selection. At n=49 it uses 9,813 additions and 1,176 outputs.
Cross-common-point sharing then gives, at h=50:

    global additions = 450394
    partial outputs = 58800
    side roles per invocation = 509194.

The previous circuit at the same h=50 would use 694,495 roles. The new circuit
saves about 26.7% of them. Every retained sum still has a common point, so its
source-indicator span is positive definite. Forward source spans and reverse
orthogonal complements supply the frames without additional rank loss.

We retain the complete first/third-stage auxiliary matching and the original
central losses. Both motifs now use h=50 and m=125000. The complex motif uses
its original construction at this ground size; its circuit is not otherwise
changed. The new bit counts and deficit are

    W = 406321422080000
    s = 50790175992864000000
    Wm-s = 1767136000000
    eta_b = 23/661055000.

The rational log bound log(m)<11737/1000 supports a_b=296/10^11. The complex
counts support a_c=1/10^11. Positivity of the complex deficit and the retained
construction's spare-coordinate requirements are also satisfied at h=50.

## 2. Use the actual stopping depth in the guard estimate

The old guard replaced the recurrence A(e)<=s*A(e/m)+E by repeated
multiplication by s+E and allowed a full log_m(d) levels. Both are conservative.
Here the retained complex network satisfies 2<=s<m^5. Stopping below d^beta
means at most (1-beta)*log_m(d)+1 internal levels. Keeping E additive gives

    A(e) <= s*(8+E)*d^(5-4*beta) <= 9*(s+E)^2*d^(7/5)

for beta>=9/10. There are at most 2*m*sqrt(d) base-m pieces. Including
preprocessing and final shifts, the original constant C0=128*m*(s+E)^2
therefore supports **guard width C0*d^2**, replacing C0*d^20.

This uses the complex coefficient-depth recurrence. The new bit circuit only
permutes complete encodings during address swaps and does not introduce
coefficient arithmetic into that recurrence.

## 3. Choose the Gaussian width to meet the interface directly

The resampling interface requires alpha^4*theta_i>p. With p=6*b and
 theta_i>1/(4*d), the choice

    alpha = ceil((32*d*b)^(1/4))

already gives alpha^4*theta_i>8*b>p. The old expression used 12*d^2*b.
The smaller width changes the Gaussian cost exponent from
3/4+delta+3*epsilon/2 to **3/4+delta+5*epsilon/4**.

The scale exponent gamma=2*d*alpha^2 now satisfies
 gamma<46*b^(1/2+3*epsilon/2). Thus epsilon<1/3 is sufficient for gamma=o(b);
the old convenient epsilon<1/12 bound is unnecessary. For the selected
epsilon=199/1000, b>=2^40 guarantees gamma<=b/4, preserving the original
rounding argument with a revised fixed cutoff. Prime selection and all
resampling hypotheses are checked again; the analytic resampling lemma is
unchanged.

## Exact final parameters

    tau = 1 - 296/10^11
    sigma = 1 - 1/10^11
    beta = 999/1000
    epsilon = 199/1000
    delta = 1/10000
    C1 = 2
    c = beta*a_b
    lambda = 1 - (1+beta)*a_b^2/2
    lambda-prime = 1 - beta*a_b^2.

All revised constraints are strict, and the exact minimum margin is

    G = epsilon*beta*a_b^2
      = 272158569/156250000000000000000000000
      > 2^-59.

The ratio G/(2^-59) is approximately 1.00408789. The certificate uses exact
fractions, not that decimal. This fixed positive gap absorbs logarithmic
factors. The proof patch updates the finite interfaces, guard argument,
Gaussian setup, cost table, seven margins, integer setup comparisons, and
explicit rounding cutoff together.

The arithmetic checker requires explicit selection of the new guard and
assembly models. The old checks retain their original constraints; this is
not accomplished by silently weakening the existing certificate.

## What happened to the earlier ceiling?

The former bound a^2/(20*(1-a)) retained C1=20 and hence epsilon<1/20.
That guard constraint has now been replaced by a proved stronger estimate.
For this graph and the revised Gaussian inequalities, the analogous necessary
bound is a^2/(5*(1-a)), because the Gaussian margin forces epsilon<1/5.
The certificate encloses it and puts it below 2^-58. This is a scoped bound
on these counts and inequalities, not on other finite networks or algorithms.

## Bounded search decisions

The first recursive whole-map circuit used 503,482 roles at h=46 before a
frame audit. That was only a small reduction, so it was not promoted to a
proof. Direct global greedy factoring gave 4,156 additions at h=12, 13,182
at h=16, and 30,309 at h=20, with worsening additions per output. We stopped
that route before a costly h=46 run. These are candidate counts, not lower
bounds or certified frame constructions.

Those experiments are reproducible with
`scripts/experiments/intersection_circuit.py` and
`scripts/experiments/intersection_greedy.py`. The latter intentionally defaults
to the bounded small sizes. The successful paired circuit and its proof are
independent of those failed screens.

## Verification boundary

Exact support comparisons check all local coefficients and the entire merged
graph. Both frame directions are checked on every compiled physical role.
Small full input-basis tests include arbitrary dirty scratch in forward and
reversed invocations; complete small three-stage tests check bank exchange.
Further tests cover nonzero vertex weights, the unrolled depth recurrence,
model-selection failures, the h=50 matching, and every changed proof interface.

The written arguments supply the general rational-frame, stopped-depth, and
Gaussian-scaling proofs. Neither these finite checks nor successful compilation
independently verifies the complete upstream multiplication theorem.
