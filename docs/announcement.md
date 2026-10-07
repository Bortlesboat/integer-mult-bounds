# Draft Twitter announcement

Suggested four-post thread. This is draft copy, not a record of publication.

**1/4**

We've pushed our conditional improvement to OpenAI's integer multiplication result (#109) further:

T(n) = O(n (log n)^(1 − κ)), with κ = 2^-78.

That's about 570 million times our previous exponent saving of 5.8e-33—not a practical speedup claim.

**2/4**

The key: the manuscript already supports nonadjacent axis swaps. Using them directly reduces layout routing from O(d²) to O(d) swaps, while preserving the network and arithmetic. A small scheduling change unlocks much stronger parameters.

**3/4**

Our earlier ceiling applied to the original routing estimates. Improving those estimates removes the constraint that made the exponent saving cubic in the network saving. The new witness scales quadratically; we haven't established a new ceiling.

**4/4**

The bound remains conditional on the upstream algorithmic interfaces. Notes, exact certificates, source patches, and the routing audit are public. Developed with OpenAI Codex; independent review welcome.

https://github.com/CrocSwap/integer-mult-bounds

## Claim boundaries

- The headline is a conditional asymptotic bound, not an independently proved
  upstream theorem or a measured runtime improvement.
- The finite network and numerical operations are retained from our h = 46
  construction; the sequence of data-movement operations changes.
- The earlier ceiling remains valid under its stated cost assumptions. It is
  not a lower bound for integer multiplication or the revised routing schedule.
- No priority or optimality claim is made for the new witness.

Author: Douglas Colkitt. See the [routing note](../artifacts/nonadjacent-axis-note.pdf)
and [audit](nonadjacent-axis-audit.md) for the precise statements.
