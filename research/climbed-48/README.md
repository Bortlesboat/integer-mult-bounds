# Hill-climbed orders on PR #48's exclusion graphs

Under the inherited analytic and fixed finite-alphabet multitape hypotheses,

$$T(n)=O(n(\log n)^{1-\kappa}),\qquad
\kappa=\frac{4129418696}{10^{14}}=4.129418696\times10^{-5}>2^{-15}.$$

This is **0.26206% above PR #48** (`411862541/10^13`) and **0.13469% above PR #49** (`4123863984/10^14`). The bit saving is
`4129589225/10^14`.

## Idea

PR #48 reordered the leave-one-out `vector()` construction and kept 403 more
carriers. PR #47 showed that climbing summand orders removes roles. These act
on different calls, so they stack. Starting from PR #48's exact orders, we
pin adjacent-swap bits for both `total()` calls (`tbits`) and `vector()`
calls (`vbits`), and climb greedily with the exact optimal carrier matching
in the loop. With all bits zero, PR #48's DAGs are reproduced
byte-for-byte.

| | PR #48 | PR #49 | This |
|---|---:|---:|---:|
| h=23 roles R (matched) | 36,432 | 36,382 (6,077) | **36,297 (6,202)**, 21+13 swaps |
| h=25 roles R (matched) | 48,329 | 48,255 (7,809) | **48,201 (7,903)**, 12+21 swaps |
| Width W | 177,530,859 | 177,284,805 | **176,993,671** |

Everything else is PR #48, unchanged:
- RaD's point order and original-envelope labels
- both fixed I+J bases
- copied centers and paid endpoint corrections
- reversed data corners with exact recovery of all ten fallbacks
- the complex layer and the balanced assembly

## Checks

- `producer.py` replays both dimensions with PR #48's own checkers, imported
  unchanged:
  - scalar identity
  - dense global-bitset audit
  - independent recount of every matched use
  - the complete physical timeline and dirty basis in both orientations

  The profiler reads the pinned matching and asserts that every edge is
  admissible. CRT disagreements are zero.
- `witness.py`:
  - exact moment at the new bit saving
  - all 47 constraints and seven margins
  - the next bit-saving and κ grid points are rejected
  - the PR #40–#48 child lists are excluded at the new bit saving by exact
    lower bounds

```sh
make climbed-48-verify
```

A greedy finite search is not a claim of global optimality.

**Validation status:** the focused producer replay, the exact certificate and
5 tests pass. A full `make verify` has not been run yet. On Linux/GCC, use
`CXX="c++ -include algorithm"`.

## Attribution

Chafik Boukhalfa (PR #43/#46/#48: compositions, reordered exclusion sums,
checkers, exact data recovery). RaD / hipotures (PR #41). icekylinx, James
Chang, Dominik Scholz, Zhihao Chen, Aurel Prosz / Paureel, Swapnil Jain,
eumemic, Douglas Colkitt, OpenAI, Harvey–van der Hoeven, and all retained
predecessors. Optimal matching (PR #44), climbed orders (PR #47, PR #49 by Rohan Arun).
Multi-threaded parallel climbing on PR #48/#49 DAG orders and certified bound
κ = 4.129418696e-5 by Rohan Gupta with Google DeepMind Antigravity assistance.
