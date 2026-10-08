# Lean check of the κ = 83/10¹² certificate

Lean 4 (v4.21.0) + Mathlib. Machine-checks the arithmetic in
`certificates/compact-control-layer.json` and `certificates/paired-network.json`.

```
cd formal/lean
lake exe cache get   # prebuilt Mathlib
lake build
```

`KappaCheck/CrocSwap.lean` proves:

- complex network, h = 25: counts, `L_c < N`, η_c, and `s_c/W_c < 15625^σ` with 1-σ = 418/10¹²;
- paired bit network, h = 50, given R = 509194 side roles: counts, η_b,
  `log 125000 < 11.737`, and `s_b/W_b < 125000^τ` with 1-τ = 296/10¹¹;
- guard constants (E, B, `s_c < m^5`, `s_c(8+E) ≤ 9B²`, C1, C0);
- all 31 constraint slacks, the recurrence exponents, margins g1–g7,
  min = g3 = 333833/(4·10¹⁵) and `2^-34 < κ < g3`;
- the repair density bound `≤ 5/(128 p³)` for every p ≥ 2;
- the per-level bounds behind `internal = τ+(1-β)max(σ-τ,0)` and `leaf = σ+β(1-σ)`;
- the scoped ceiling at its exact value: κ < U ≈ 8.3695980744e-11 for every
  admissible parameter choice with the h = 25 complex motif. Their witness meets
  every hypothesis, and Lean refutes the enclosure against U·(1 - 10⁻²⁴).

Everything depends only on `propext`, `Classical.choice` and `Quot.sound`:
no `sorry`, no `native_decide`.

Not covered: the written tape constructions, the circuit producing R, and the
upstream theorem. `Network.lean` and `Certificates.lean` are shared helpers
(network count formulas and a generic exponent certificate).
