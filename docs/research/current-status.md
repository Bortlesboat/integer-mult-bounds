# Current result

The conditional saving is `kappa = 119723/20000000000 = 5.98615e-6`.
The [proof](../../artifacts/endpoint-gauge-note.pdf) inherits the partial-swap
construction at `f2ab41aebad47861caf6316282c1793e5513845e`, which extends
[PR #10](https://github.com/CrocSwap/integer-mult-bounds/pull/10).

Complementary auxiliary endpoint gauges merge the middle-stage entrance and
exit, preserving rank budget `Wm-2N+2L`. The selected bit and complex producers
both use `(32,30,40)` with separate counts. The rational controlled basis
supplies the bit profiles, while a binary quadratic-phase normal form supports
all nondegenerate complex residuals, including alternating ones.

The [certificate](../../certificates/endpoint-gauge-network.json) records exact
moments, the updated precision guard, finite basis combinatorics and assembly.
The [producer checker](../../scripts/endpoint_gauge_producer.py) rebuilds the
new graphs, frames, carrier matchings and internal histograms. Generic basis
existence and the tape/analytic interfaces remain written proof obligations.

The earlier [partial-swap proof](../../artifacts/partial-swap-note.pdf),
[#10 proof](../../artifacts/batched-23-note.pdf) and
[patch](../../patches/batched-23.patch) remain baseline references, including
the Gaussian scaling correction. Older research pages describe earlier results.
