# Bounded finite-network investigation

Started 2026-10-07 14:24 UTC; completed 15:18 UTC. The authorized window allowed
work until approximately 17:23 UTC, with an earlier stop if the bounded avenues
were resolved. The planned screens are resolved. Existing conditional 2^-76 artifacts are
preserved. All work remains local for review; no research changes were pushed.

## Outcome and scope

The investigation found a **conditional 2^-75 witness**. First- and third-stage
side roles can be paired so their frame transition is nested. Sharing those
roles removes one third of the side scratch infrastructure without reducing
the absolute rank deficit. This changes a network hypothesis of the earlier
fixed-network tuning bound.

The other completed work consists of family-specific bounds, finite tests,
and a ranked [next-step roadmap](next-steps.md). No exponent in the 60s or 50s
has been proved. No candidate was promoted on wire counts alone: scalar
restoration, common gate frames, endpoint identities and rational edge ranks
were checked before substituting the final parameters.

## Baseline and target selection

Re-read the scalar motif, subspace-label and bit-interface contracts in the
pinned `03-motifs.tex`. Side wires account for about 99.975% of bit-network
roles at h=46. The old bit saving is approximately 1.80054e-11.
Prioritize the bit/swap network and retain the existing complex network.
Meaningful next targets are 2^-70 and 2^-60, with smaller structural gains
retained if the proof is economical and transferable.

## Completed bounded work

| Avenue | Result | Scope |
| --- | --- | --- |
| Shared binary source hierarchy | Even a free implementation cannot reach 2^-70 under current downstream constraints | Original unshared stages and central losses; one hierarchy |
| Thinning triples | Cannot beat the full h=46 bit family | Original ambient dimension, centers and per-edge side roles |
| Unequal tensor factors | (46,46,46) remains uniquely best | Original complete-triple construction; exact finite search and infinite tail |
| Higher odd subset sizes | Favorable sampled models score worse than triples | Bounded exploratory scores, not a feasibility or all-h theorem |
| Reuse with at least one added backward dimension per deleted role | Worsens the deficit ratio | Fixed N,m and the stated loss hypothesis |
| Matched stage-1/stage-3 side sharing | Preserves the absolute deficit and supports 2^-75 | Explicit matching, written frame proof and exact parameters |
| Direct-sum low-dimensional labels | Local orthogonality holds, but existing interstage nesting fails | Explicit proposed substitution only |

Proofs and numerical checks are in [network-screens.md](network-screens.md).
The unequal-factor search checks 3,898,895 unordered triples and bounds the
infinite tail. These results do not exclude arbitrary overlapping incidence
circuits, new representations, or larger composite primitives.

## The surviving construction

For h=46, pair ground points and construct an explicit permutation pi of all
15,180 triples with |T intersect pi(T)|=1. It defines a bijection between the
first- and third-stage side roles. Each earlier invocation restores the reused
scratch value before the later invocation begins.

The critical connecting labels are

    E = F tensor line(t_A) tensor line(t_B),
    H = line(t_S tensor t_pi(A))^perp tensor line(t_B).

Orthogonality in the middle factor gives E subset H. Replacing the two old
scratch endpoint edges by this edge removes exactly m units of edge rank per
deleted role. No new decreasing edge appears; all-role endpoint identities
and the scalar bank exchange are retained.

The exact counts are

    removed roles R = 9475984020888000,
    W_new = 18958995769111200,
    s_new = 1845392811609813681600,
    eta_new = 9/29015910268.

The certified bit saving increases to a_b=27/10^12. The complex saving remains
a_c=9/500000000000. With epsilon=1/21, beta=9/10 and the tuned quadratic
recipe, the minimum margin is 3a_b^2/70 > 2^-75. The separate conditions
involving sigma pass. The recurrence refinement that assumed sigma<=tau is
not used.

Deliverables:

- [Standalone proof](../../notes/stage-reuse-note.tex) and [PDF](../../artifacts/stage-reuse-note.pdf).
- [Independent source patch](../../patches/h46-shared-side-75.patch).
- [Count and parameter certificate](../../certificates/stage-reuse.json).
- Matching, rational projection, complete small-network scalar, and patch tests.

## Independent agent input and follow-up target

The supplied agent independently proposed the already completed d^2-to-d
layout change. The remaining square instead comes from c=O(1-tau) in packed
movement. Its suggestions about incidence layers, smaller label spaces and
joint primitives helped focus the follow-up models.

The next-step document gives a specific higher-rank label target: 2,024
nondegenerate rational two-planes in dimension 24 with prescribed orthogonality.
The transfer counts and downstream arithmetic would support 2^-59 **if those
planes were constructed**. They have not been constructed or shown to exist.
`certificates/block-label-target.json` is explicitly an unrealized design
target, not another multiplication result. The corresponding script checks the
arithmetic implication and does not claim feasibility.

A short literature check found the fractional Haemers block-matrix framework
relevant to that search. The [Bukh–Cox paper](https://arxiv.org/pdf/1802.00476)
does not supply the required symmetric rational representation. No external
theorem from that survey is needed for the checked 2^-75 construction.

## Validation and stopping decision

`make verify` passes: all **46 tests**, all **twelve alternative patches**, and
the pinned upstream hash checks. The run regenerates the arithmetic and search
artifacts. The stage-sharing note compiles without warnings. A disposable
full patched-manuscript preview compiles with only two inherited overfull-box
warnings. The pdfTeX-only metadata commands were disabled solely in that
preview, not in the mathematical patch.

The research certificates and stage-sharing patch regenerate byte-for-byte,
local document links pass, and `git diff --check` passes. The bounded
investigation stops after these final artifact consistency checks. The
cheap planned screens are resolved and a concrete conditional improvement is
packaged. Constructing new block labels or searching general incidence circuits
is a distinct next research attempt; an unused portion of the time window is
not a reason to start an unbounded search.

## Subsequent authorized incidence-circuit attempt

After the rank-two screens, the overlapping-incidence route produced a
[conditional 2^-67 construction](incidence-network.md). It replaces each
neighbor rectangle by an invertible mixer on a+b-1 roles, changes the early
side frame to the common B tensor F label, and inserts a nondegenerate middle
frame between the physical source lines and target orthogonal complements.
The middle span is positive definite because all triples contain a common
point. Both the forward and reversed invocation introduce no extra backward
rank. The new early label also permits sharing complete auxiliary banks,
including central roles, between stages 1 and 3.

The target h=46 partition is checked on all 893,970 ordered disjoint pair
instances. Side roles per invocation drop from 41,122,620 to 2,394,438.
The bit saving a=46/10^11 gives exact minimum margin
1587/175000000000000000000000 > 2^-67. This is a new circuit and new frame
schedule, outside the earlier unchanged-trajectory bounds.

Validation now includes 67 tests and 13 independent patches, a warning-free
standalone note, and a full patched-manuscript build with the same two
inherited layout warnings. No commit or push was made in this attempt.

## Shared-computation follow-up

The next authorized attempt first expanded the rectangle product-plan pool.
It reduced roles per common point from 52,053 to 51,131, only 1.8%; exhaustive
enumeration checked the selected partition. An exact edge-efficiency bound
also excludes 2^-60 for independent common-point rectangles at fixed h=46,
under the retained central losses and downstream constraints. This justified
stopping the partition search rather than optimizing an inadequate family.

The [shared-sum graph](shared-computation.md) then produced conditional
2^-63. A deterministic recursive circuit computes all disjoint-pair sums
using 11,566 binary additions and 990 outputs at local size 45. Every addition
has disjoint input supports. Its reversible embedding uses c+q=12,556 roles
per common point, hence 577,576 side roles per invocation. Source-support
spans provide the middle forward frames; reachable-target spans provide the
middle reverse frames. All are nondegenerate because each local circuit's
labels share a common point. No additional backward rank is introduced.

Exact comparison supports a=187/10^11 and minimum margin
104907/700000000000000000000000 > 2^-63. The old complex primitive and full
first/third-stage auxiliary sharing are retained. The new circuit's output
map and both compiled support-frame directions are checked at the target
size. Small invocations are checked on every data and scratch input basis
vector, and the full small three-stage circuit restores its shared scratch.

All 73 tests and 14 alternative patch checks pass. The standalone note builds
without warnings; the full patched manuscript builds with the same two
inherited layout warnings. The 2^-67 artifacts are preserved. No commit or
push was made, and no exponent in the 50s is claimed.
