# Shared intermediate sums: conditional kappa = 2^-63

The new circuit shares intermediate sums across outputs rather than allocating
separate scratch for every rectangle. At h=46 it uses **577,576 side roles per
invocation**, versus 2,394,438 in the 2^-67 circuit. The absolute rank deficit
is unchanged. This supports conditional kappa=2^-63, a 16-fold increase in
the certified exponent saving. The complex network and upstream assumptions
are retained. No exponent in the 50s or practical speedup is established.

The proof is in [the note](../../notes/dag-note.tex), including its
[construction fragment](../../notes/dag-construction.tex). The independent
[source patch](../../patches/h46-dag-63.patch) applies to the pinned upstream
source and includes routing and parameter changes.

## The short partition screen

Enriching the D(1,1) factor choices with plans chosen at additional integer
weights improves the per-common-point rectangle count from 52,053 roles to
51,131, about 1.8%. It is not worth further broad tuning when the shared-sum
circuit uses only 12,556 roles at the same local size.

There is also a rigorous bound for independent common-point rectangles at
h=46, with the retained central losses and downstream inequalities. If a
rectangle has a source pairs and b target pairs, the unions of their point
supports are disjoint. For some k, therefore a<=C(k,2), b<=C(45-k,2).
The efficiency ab/(a+b-1) increases with either variable. Exact maximization
over k gives efficiency at most 121 neighbor edges per scratch role.
Consequently the 46 local relations require at least

    46*893970/121 = 3738420/11

side roles per invocation. The exact logarithm enclosure and necessary bound
kappa<a^2/(20(1-a)) put this restricted family's upper bound below 2^-60
(approximately 2^-60.826). This is a fixed-h bound, not a bound on the new
shared-sum graph, all finite networks, or other downstream arguments.
`certificates/incidence-partition-screen.json` records the arithmetic.

## A circuit for deleting two vertices

For each common point i, index the other 45 points naturally. Inputs x_ab are
the source triples {i,a,b}. The desired output for {i,c,d} is the sum of all
x_ab whose pair avoids {c,d}. The construction uses only additions with
disjoint input supports, so no unwanted source paths are hidden by cancellation.

The routine splits a point set in half. It recursively computes pair-input
sums excluding zero, one, or two vertices inside each half. Cross pairs form
a matrix. Row totals and column totals supply exclusions on one side; applying
leave-one-out sums along rows and then columns supplies simultaneous row/column
exclusions. Finally, the left-left, right-right and cross contributions are
combined. Their input regions are disjoint.

The vector leave-two-out routine uses the same divide-and-conquer principle;
leave-one-out alone uses prefix and suffix sums. Identical formal sums are
interned by their source-support bit sets, and unused nodes are removed.
The implementation is deterministic and uses no floating-point search.

At n=45 the active graph has 990 inputs, 990 outputs, and 11,566 binary
addition nodes. All 990 output support sets are compared with their exact
disjoint-pair definitions, checking both the 893,970 nonzero coefficients and
every required zero. This is a whole-linear-map check, not a sample of values.

## Reversible role allocation

For each node, create one outgoing edge for each later use and designated
output. Input nodes receive a source slot and fan it out. An addition node
uses its two incoming roles, adds the second into the first, and uses the
first as the pivot for one outgoing edge. Additional outgoing edges receive
fresh roles containing copies of the pivot. Other incoming roles retire.
Each node's gate is an invertible gather-and-fanout mixer.

If there are c additions and q outputs, there are 2c+q outgoing uses in total.
Reusing one incoming role at each addition subtracts c, giving **c+q roles**.
Every physical role follows a directed path; branching creates separate roles.
Identity input gates are allowed, making the early and late frame assignments
uniform even for a source with only one outgoing use.

Let L denote the product of node mixers, V the source copy and J the output
injection. Use the already audited 12-operation schedule

    L, J, inverse L, R, V, G, R, L, J, inverse L, G, V.

For arbitrary initial scratch z, the early and late contributions are JLz
and JL(z+Vx). They cancel to leave JLVx. Final cleanup restores z, and the
original center operations restore their scratch as well. The full map is
the original bank shear, since the side relation cancels exactly the
intersection-one entries of the central incidence map.

## Why sharing costs no additional rank

In the middle forward L, label a gate by the span of all physical source
indicators reaching that node. Support inclusion along an edge implies span
inclusion, so physical roles move through nested frames. Every source triple
in one local circuit contains the common point i. Consequently every vector
u in any such span satisfies sum(u)=3*u_i and

    <u,u>_(I-J/9) = sum_{j != i} u_j^2.

The span is positive definite and hence nondegenerate, even though the whole
rational ambient form is indefinite. At an output it lies in the target's
orthogonal complement because every contributing source is a neighbor.

The reversed second stage has a different assignment: a gate receives the
span of all physical X targets reachable from that node. These descendant
sets grow when the graph is traversed backward. They also consist of triples
containing i, so the same nondegeneracy proof applies. At an original source,
all reachable targets are neighbors, providing the required final inclusion
in the physical Y orthogonal complement.

The embedding checker follows every compiled role in both directions and
checks all support inclusions. This also checks that pivot reuse or fanout
does not silently identify simultaneous roles. The written span argument
supplies the rational interpretation of those set inclusions.

Early mixer gates use the common low frame B tensor F and late cleanup gates
the full frame A tensor F. The original data-stage boundaries are unchanged.
Thus only the original central returns decrease rank: total loss remains
3v^2h^2. Full first/third-stage auxiliary sharing applies as in the rectangle
construction, including centers, with the same nested joining frames.

## Counts, parameters, and verification

Each invocation has 46*(11566+990)=577576 side roles. At h=46,

    W = 273201575169600,
    s = 26592347948314104000,
    Wm-s = 572394081600,
    eta = 27/1254369032.

Exact comparison supports bit saving a=187/10^11. The unchanged complex
saving is a_c=9/500000000000. With the previous parameter recipe,

    min_j g_j = 3a^2/70
              = 104907/700000000000000000000000 > 2^-63.

All strict layer inequalities pass. No change to the label dimension,
computational model, complex precision analysis, numerical maps, or rounding
is needed. Gate counts and rational frame bases remain fixed finite constants.

The reproducible artifacts are `scripts/exclusion_circuit.py`,
`scripts/dag_network.py`, and `certificates/dag-network.json`. Small forward
and reversed invocations are checked on every input basis vector, including
every scratch input. A complete small three-stage model also checks bank
exchange with the shared auxiliary banks. These checks do not independently
validate the full upstream multiplication theorem.

The next search can work directly on cancellation-free addition graphs and
use this transfer lemma, provided each local graph retains the common-point
property and all required source-target support constraints. Sharing across
different common points requires a new nondegeneracy audit, particularly for
the reversed-stage reachable-target spans; equal scalar sums alone do not
justify that extension.

Follow-up: the [cross-group sharing audit](cross-point-sharing.md) proves that
orthogonal complements of forward source spans can supply the reversed frames.
This removes the separate common-point condition on reachable-target spans and
supports the next conditional refinement.
