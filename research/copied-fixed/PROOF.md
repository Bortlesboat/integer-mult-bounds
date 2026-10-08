# Weighted carrier matching with exact recovery of every data block

Conditional witness, prepared locally on 8 October 2026 with OpenAI Codex assistance.

Under the base theorem and the retained analytic and fixed finite-alphabet,
fixed multitape interfaces, the construction below gives

\[
T(n)=O\bigl(n(\log n)^{1-\kappa}\bigr),\qquad
\boxed{\kappa=\frac{82012589}{2000000000000}=0.0000410062945>2^{-15}.}
\]

This is **6.6292252%** above icekylinx's PR #36 witness,
**0.0268189%** above our published PR #43 witness, and
**0.00000477975%** above Rohan Arun's contemporaneous PR #44 witness
4.100629254e-5. The increment over #44 is small: 1.96e-12 in kappa.
The power-of-two corollary remains 2^-15; 2^-14 is not reached.
These compare asymptotic exponent savings, not running times. Finite
certification does not formally verify the full multiplication theorem.

## Increment and provenance

Use the weighted carrier matching published by Rohan Arun in PR #44,
at commit 061414a529f1123668872db44d737e362fbe066f, with Anthropic Claude
assistance. Its binary carrier-use lists are pinned and fully replayed.
The floating-point discovery optimizer is retained for attribution only;
no optimizer result, optimality claim or floating-point value is trusted
by the certificate. Both scalar graphs use support-right summation trees.
At h=25 this changes PR #43's input-order left association; h=23 is unchanged.

The additional saving comes from removing all ten conservative data-corner
fallbacks in #44. PR #40/#42 had already resolved these primary-prime
failures by a second-prime test. This composition uses a separate exact
rational elimination of all ten pairs, proving every ordered pivot and
required zero directly. Each of the two macros per pair replaces 38
singletons by blocks of widths 21 and 17. Globally the child multiplicities
change by -760 at width 1, +20 at width 21, and +20 at width 17, with
no change in total rank, physical roles, copies or overhead interfaces.

An exact lower moment bound excludes the complete #44 network at the new
bit saving; the new network's exact upper moment is below one. This is a
finite-construction improvement, rather than parameter tuning alone.
The novelty claimed here is this checked composition and rational recovery,
not the weighted matching or the already known possibility of recovering
these ten pairs. No global optimality claim is made.

## What changes, and what is reused

Use RaD / hipotures's PR #41 alternating pair order: in the h-point graph,
form consecutive pairs excluding the common point, reverse the pair list
for odd common points, and append leftover points. At both h=23 and h=25, sort summands
by decreasing (support size, support bitmask) before left association. These are deterministic changes to
the scalar computation DAG. `changed_graph.py` is a minimal specialization
of the pinned PR #41 producer and its linked RaD checkpoint. The h23 scalar hash is unchanged from PR #41/#43; the h25 specialization
has the new scalar hash recorded in `scalar-25.json`. No sampled search statistic
is a certificate input.

Use the **original envelope labels**, both fixed local bases I+J, and our
pinned PR #44 weighted matching. Original labels have the
explicit low-rank projector formula from icekylinx PR #32 and Dominik
Scholz PR #35. The pinned selected carriers satisfy every legality check; all selected uses are independently
recounted. Both complete fixed profiles are recomputed from these changed
DAGs and actual matching uses, rather than substituting PR #40's profiles.

Retain icekylinx PR #36's copied centers, paid endpoint correction and
complex circuit. Use James Chang PR #34 / Rohan Arun PR #37's reversed
dimensions (23,25) and balanced transfer. Rohan Arun PR #39/#40 supplies
the modular data-corner method and the contemporaneous both-fixed baseline.
For all 4,073,300 actual triple pairs our full data profile is **9 singletons
+21+17+481**. The primary prime certifies 4,073,290 pairs and direct rational
elimination certifies the remaining ten. Every pair and every paid endpoint
is included.

An exact lower moment bound rejects the complete PR #40 network and the
stronger published PR #41 generic alternating network at our new bit
saving. The improvement therefore changes the finite construction; it is
not merely a tighter choice of assembly parameters.

## Scalar identity, labels, and restored scratch

Index source lines by triples of an h-point set and use rational address
metric \(G_h=I-J/9\). Triple indicators have norm two and inner product
\(|S\cap T|-1\). The changed, independently replayed exclusion producer and point totals implement
the scalar identity \([|S\cap T|=1]+|S\cap T|=[S=T]\) over bit payloads.
Its source injection, reversible mixer, and scatter satisfy \(JLV=I\).
For arbitrary old auxiliary vector z, the chronological word
\(L,J,L^{-1},V,L,J,L^{-1},V\) scatters
\(JLz+JL(z+Vx)=x\) and restores z. The payload field is \(\mathbb F_2\);
the address projectors are over \(\mathbb Q\), subsequently reduced modulo
an eligible odd prime. These two fields must not be identified.

For common core C and cover M, the original envelope is

\[
E(C,M)=\{x:\operatorname{supp}x\subseteq M,
 x_i=t\ (i\in C),\ \sum_i x_i=3t\}.
\]

An addition has c=|C| in {1,2} and dimension |M|-c. Every envelope lies
in \(U_i=\{x:\sum_jx_j=3x_i\}\) for some i in C, where
\(x^tG_hx=\sum_{j\ne i}x_j^2\); hence it is nondegenerate. Every operand
and matched continuation has nested envelopes. Side outputs omit the two
non-common coordinates of the target triple and are orthogonal to that line.
Retained totals have envelope \(U_i\), of rank h-1.

The full generator checks these properties. A separate dense-bitset pass
expands every addition into global triple supports, checks disjointness and
every output, and independently replays the actual matched use records.
Matching joins an addition's carrier to a later compatible operand/output use.
Each donor and recipient use occurs at most once. Designated output-use
carriers remain distinct terminals: no center copy bypasses a later producer
consumer. This is the compiler's retained terminal contract.

| h | triples v | additions c | output uses q | matches | roles R | loss ell |
|---|---:|---:|---:|---:|---:|---:|
| 25 | 2300 | 49119 | 6925 | 7565 | 48479 | 600 |
| 23 | 1771 | 37098 | 5336 | 5749 | 36685 | 506 |

Here \(R=c+q-\mathrm{matches}\), \(\ell=h(h-1)\).

A separate physical compiler, adapted with attribution from PR #41,
constructs every role trajectory directly from binary DAG and selected
use records. Original rational envelope bases replace positive-label
inputs. It checks all input/output coefficients, frame containments,
terminal-role uniqueness, reverse-complement incidences and the copied
rank histogram. Its actual XOR word is then applied to the **complete
formal basis** of inputs, outputs and all dirty auxiliaries: 40,227 basis
vectors at h=23 and 53,079 at h=25, with 312,842 and 413,392 elementary
operations respectively. Both forward and reverse-complement words give
the required shear and restore every auxiliary exactly. This is full
finite linear verification over F2, not random dirty-state sampling.
The rational address projectors and their compiled contiguous profiles
are checked separately below.


PR #36's copied-center identity is valid for these original labels. In a
forward invocation, replace an original center's path U→0→F by a paid
rank-r transform U→0 on a copy, supplying all read-only scatter uses, and
the original's direct U→F path of rank h-r. In the reverse complementary
invocation, the original goes 0→U-perp; its paid transformed copy goes
U-perp→F for the early reads. Both schedules deliver precisely the old
read value and the old cleanup value. Arbitrary dirty auxiliaries therefore
still cancel. Every copy is a complete existing role stream of volume V/W;
copy, read, erase and parking are charged linear passes on fixed work tapes.
There is no new independent row index. In both directions r=h-1, so each
center replaces one full h-block by a singleton and **retains** its
transformed-copy profile. Its rank mass drops by h-1, not by 2(h-1).

The two scalar shears give \((x,y)\mapsto(y,x+y)\). With PR #36's data
and auxiliary frames, their outputs are \(A=Fy,B=Fx+Ey\), where
\(F=D_I,T=D_U,E=D_{I-U}=TF\), and U is the tensor product of two triple
lines. Retain A, transform a copy by the rank-one T, and XOR it into B.
The result is \((Fy,Fx)\). Undoing the bank exchange gives full interchange
on the data; every restored auxiliary has endpoint product F. All N paid
rank-one endpoint corrections are separate from the center copies.

## One fixed compatible basis

With physical coordinate \(i=b\alpha+\beta\), use
\(K=T_2(I_a\otimes L_b)\), where
\(T_2(x\otimes e_\beta)=M_\beta L_ax\otimes e_\beta\).
Use the actual controlled permutations certified by the imported PR #34
all-weight geometry, transferred by PR #37. At a=23,b=25 the first and
last d=47 row and inverse-column labels are
R=[0,...,22;22;0,...,22], C=[0,...,22;0;0,...,22].
The 25 completed permutations are explicitly checked.

For each source triple indicator t and normalized dual phi,
L_ht=t+3*1 and phi L_h^{-1}=t^t/2-5*1^t/[3(h+1)].
All coordinates are nonzero. The first-h/last-h corner of each local tensor
residual is a nonzero diagonal row/column scaling of its full conjugated
local matrix. It contains its entire rank, so the entire ordered local
profile transfers. `geometry()` checks the actual contractions, auxiliary
restrictions, and physical offsets. The auxiliary exterior profiles are
(23,529) and (25,525); data growth profiles are (1,21) and (1,23).

The null projector of (I-P) tensor (I-Q) has rank d=a+b-1=47.
Its image consists of u tensor v+p tensor w modulo (cp,-cv).
After dividing row evaluations by nonzero p_r v_beta, the first-d
restrictions form a bipartite incidence tree on a+b vertices. So do the
last-d dual restrictions. Leaf elimination proves both have rank d.
Their product is therefore an invertible null corner for every fixed
source pair, regardless of whether our modular test succeeds.

The rescaled null-corner entry is
x_{R_i}[R_i=C_j]+y_{i mod b}[i mod b=(m-d+j) mod b]-1,
where x=1/(p*xi), y=1/(v*nu). At I+J these values are
x_in=3(h+1)/(2(3(h+1)-10)), x_out=-(h+1)/5.
The imported exact all-weight rank cuts prove the zeros for the prescribed
ordered pivots. Our C++ replay then tests every actual source pair modulo
the trial-division-proved prime 1000003. A nonzero pivot proves rational
nonvanishing. Arithmetic in that sweep is entirely integral with 64-bit
products bounded by prime squared. For each of the ten failures,
`data_recovery.py` starts again from the rational corner entries and
performs exact Fraction elimination through all 47 prescribed pivots.
Every pivot is nonzero and all 346 required ordered zeros hold for each
pair. The certificate includes all 470 rational pivot values. The row and
column restrictions are explicitly compared with the inherited geometry.
A residue zero therefore does not become a rational-zero assertion.

All 47 prescribed pivots succeed on 4,073,290 pairs. The two contiguous
blocks occupy rows 1..21 / columns 553..573 and rows 28..44 / columns
530..546. The remaining nine pivots are singletons. The exact rational
recovery certifies the same two contiguous blocks for the ten other pairs.
In all cases the
large-projector Schur identity supplies the middle block 47..527 of width
481. No separated pivots are gathered and no source pair is discarded.
The full producer independently regenerates and compares every record;
checks of saved counts alone are not the nonvanishing proof.

## Exact internal pivot certificates

Put O=M\C, n=|O|, c=|C|, s=3-c, d=s²+(c-1)n,
\(w=\mathbf1_C+3\mathbf1\), \(z=3(h+1)\mathbf1_C-10\mathbf1\).
For the conjugated envelope projector A, the inherited explicit formula is

\[
3(h+1)d(A-\Delta_O)
=s\mathbf1_Oz^t+3(h+1)s w\mathbf1_O^t+n wz^t
-3(h+1)(c-1)\mathbf1_O\mathbf1_O^t.
\]

One derivation starts with columns \(e_j+\mathbf1_C/(3-c)\), j in O.
Their Gram matrix is \(I+(c-1)J/(3-c)^2\); its inverse and conjugation
by I+J give the formula. `audit.py` independently checks the defining
properties: image contained in E, identity on an E basis, and self-adjointness
in \(G'=I-(9h+19)J/[9(h+1)^2]\). It checks all 90 core/cover size cases
at both dimensions. Since I+J and G commute with coordinate permutations,
these canonical cases cover every core/cover arrangement. Source triple
projectors are separately normalized and checked exactly.

Every actual transition is a 0/1 diagonal mask plus a correction of rank
at most two (single frame, complement, same-core difference), three
(source growth), or four (core-two to core-one growth). These exhaust the
checked nested incidences. For c=1 the correction is a sum with column
span generated by w and the outside indicator; a same-core difference
has the same form with the difference of outside indicators. For c=2,

\[
A=\Delta_O+\frac{wz^t}{3(h+1)}
-\frac{(w-\mathbf1_O)(z-3(h+1)\mathbf1_O)^t}{3(h+1)(n+1)}.
\]

The constant rank-one term cancels in same-core differences, leaving two
rank-one terms. Nested masks have only 0/1 differences. The source-growth
and changing-core bounds follow by adding correction ranks.

Let \(Z=3h-7\), \(B_0=(4h-2)Z+27(h+1)\),
\(D=3(h+1)(h-1)^2\), \(B=2(h-1)B_0\).
Each constituent denominator is 3(h+1)d with d≤h-1; for source lines d=2.
The actual common denominator of two terms is ≤D and each multiplier
is ≤h-1. Every correction numerator is therefore bounded by B.
For correction rank r, any square minor, times its actual common denominator
to power r, is an integer of absolute value at most

\[
\mathcal B_r=\sum_{j=0}^r\binom hj j!B^jD^{r-j}.
\]

Expansion by correction columns proves this: terms with more than r such
columns vanish; mask columns fix their rows. Use \(p_1=2^{61}-1\) for
rank-two cases and \(p_1p_2p_3\), with \(p_2=2^{31}-1,p_3=2^{19}-1\),
for the other cases. Lucas–Lehmer verifies primality and all denominators
are invertible. The exact bounds are:

| h | B₂ | B₃ | B₄ |
|---|---:|---:|---:|
| 23 | 38218181861376 | 219993996697351151616 | 1206074983422622280129445888 |
| 25 | 75405344477184 | 613343016893987684352 | 4772090401825349199521120256 |

Both B₂ values are below p₁; B₃ and B₄ are below
\(p_1p_2p_3=2596143476298333157846630848266239\).
Thus each northeast-corner rank over Q equals the maximum of its modular
ranks: an alleged larger minor vanishing at all selected primes must be
zero by the strict numerator bound. Nonzero modular minors are nonzero
over Q. This certifies zeros as well as nonzeros, without a probabilistic
rank assumption. Consecutive increasing pivots are compiled by the retained
lower-triangular partial-swap conjugation into one contiguous recursive call.

The profiler reconstructs 68,229 distinct matrices at h=23 and 91,834 at
h=25. Of these, 5,555 and 7,179 respectively use all three primes; no
modular profiles disagree. The checked-in complete block lists have old
rank masses 844767 and 1213175. Subtract h full h-blocks and add h
singletons for copied centers; the new masses are 844261 and 1212575.

## Complete cost and exact witness

Put \(N=v_av_b=4073300\), \(B_a=v_bR_a=84375500\),
\(B_b=v_aR_b=85856309\), \(W=2N+B_a+B_b=178378409\),
\(L=v_b\ell_a+v_a\ell_b=2226400\), m=575.
The disjoint classes are:

| Class | Multiplicity | Recursive widths |
|---|---:|---|
| First auxiliary exterior | B_a | 23,529 |
| Second auxiliary exterior | B_b | 25,525 |
| Every data macro | 2*4073300 | 9 singletons,21,17,481 |
| h=25 internals | v_a | Complete certified copied fixed profile |
| h=23 internals | v_b | Complete certified copied fixed profile |
| h=25 data growth | 2N | 1,23 |
| h=23 data growth | 2N | 1,21 |
| Paid endpoint correction | N | 1 |

Their weighted rank is exactly
\(s=Wm-N+L=102565738275\); the deficit is 1846900.
Every width is at most 529<m. Every copied transform is included once,
and every original role still undergoes full interchange. Node overhead
is linear in current volume, under the inherited complete-row, remainder,
spectator, ordered-affine and fixed-tape contracts.

For \(a_b=410079761/10000000000000\), the checker proves

\[
\sum_t\frac{n_t t}{Wm}\exp(a_b\log(m/t))<1-3.4558\cdot10^{-14}.
\]

It range-reduces logarithms to [1,2], uses the 32-term atanh series with
its explicit geometric tail, and rounds outward with integer arithmetic.
For 0≤u<1 it uses
\(e^u\le1+u+u^2/[2(1-u/3)]\); the factorial inequality
\(k!\ge2\cdot3^{k-2}\) for k≥2 proves this bound.
The first four exponential terms give a rigorous lower bound. Those lower
bounds reject the old PR #36 profile and the complete PR #40--#44 profiles
at this new saving. These are scoped
checks, not global optimality claims.

The complete-row induction therefore gives bit exponent τ=1-a_b.
The complex network is unchanged from PR #36, with saving 717/10^7,
including every copied-center inverse phase and paid endpoint correction.
Its scalar charge is G=4793351472, and its semantic envelope remains
\(E=64(W_c+m_c+G+1)^3\); the completed-child guard is C₁=1.
The largest bit child stays 529 and the reduced W still has 28 bits, so
the bit halving degree is 9,
the complex degree is 20, and product row stock p^2000 still suffices.

The balanced assembly is an additional inherited physical construction,
not an algebraic deletion of the old prefix cost. Process each long FFT
axis's extra top bit individually, then use common named low-coordinate
groups of widths K_j in [K,2K). The resulting extra work is O(T p d),
with saving 1-epsilon. The complete axis-major/group-major permutation and
its inverse use the paid arbitrary-coordinate router; global bulk gathers
and inverses retain margin a_b. Whole active, control, row and spectator
fields stay complete. FFT level/twiddle order and forward/inverse alignment
are retained. The imported PR #34 assembly proof and RaD reports specify
the router, bulk Gaussian map, phase-cell inverse and all-size tape costs.
Their hypotheses remain required; see `references/copied-fixed/pr34/`.

Use eta=10^-12, beta=1/20, q=a_b(1-2 eta), c=q+eta/4,
epsilon=(1-eta)/(1+q), lambda=(1-a_b+1-q)/2,
lambda'=1-q, g=epsilon*q, r=(g+1-epsilon)/2, delta=eta/8.
All 47 strict constraints hold. The seven margins are

\[
1-\epsilon,\ a_b,\ g,\ a_b,
\min(1-\epsilon-\delta,r-\delta),\ 1-\epsilon-\delta,\ \epsilon.
\]

Their minimum is g, the first is g+eta, and

\[
g-\kappa=\frac{147321738734203716270751}
{10000410079760999179840478000000000000}>1.4731\cdot10^{-14}.
\]

The geometric requirement is still positive:
1-epsilon(1+c)=eta-epsilon*eta/4>3 eta/4; it is not itself a cost margin
in this balanced physical layout. Negative controls reject the old prefix,
old nonlinear guard, and old separate exposure charges at these parameters.
Exact cutoff checks retain padding across whole intervals, product row
stock, and the additional prime/native-setup/recovery thresholds. These
strict positive gaps absorb fixed polylogarithms. The paper's fixed-machine
extension below an eventual cutoff gives the claimed conditional exponent.

## Review boundary and attribution

The weakest steps requiring expert mathematical review are the inherited
ordered-affine partial-swap compiler and its fixed-tape cost, copied-stream
parking and complete spectators at every recursive call, the balanced positional-layout transfer, the translation
from fixed local pivot profiles into the common ambient basis, and the
semantic/bulk Gaussian and exact-recovery interfaces. The finite checks
support those arguments; they do not replace them. The common eligible
address prime and full all-size machine are specified by the retained
existence/setup arguments, not materialized here. The optional Lean extension was not implemented; no Lean build or full
formal verification is claimed.

Direct construction credits: **Rohan Arun, PR #44, with Anthropic Claude
assistance** (weighted carrier matching, pinned links and profiler); **RaD / hipotures, PR #41** (changed scalar
DAGs, alternating point order, and independent role-compiler checker), **icekylinx, PR #36** (copied centers, complex
network, assembly integration), **Dominik Scholz, PR #35** (two fixed factors,
tree argument, dimension-specific CRT method), **icekylinx, PR #32**
(fixed I+J projectors/profiler), **Zhihao Chen / jacklightChen, PR #29**
(compatible two-stage tensor construction), **Aurel Prosz / Paureel**
(two-stage topology and paid endpoint copy), **Swapnil Jain** (linked
two-stage development), **Rohan Arun, PR #25/#31** (first data block and
ordered corner methods), and **Dominik Scholz, PR #33** (dimension adaptation).

Retained interfaces: **icekylinx, PR #10/#18/#24**; **Zhihao Chen,
PR #7/#16/#21/#23**; **RaD / hipotures, PR #20** and its pinned semantic,
routing, Gaussian inverse and bulk work; **eumemic, PR #3/#5/#6/#13**;
**Bortlesboat / Andrew Barnes, PR #2**; **dleen / David Leen, PR #4**;
**Douglas Colkitt**, **OpenAI**, and **David Harvey and Joris van der Hoeven**.
The reversed geometry is credited to **James Chang / jamesyc, PR #34**
and **Rohan Arun, PR #37**. **Rohan Arun, PR #39/#40/#42** supplies the
modular data-corner method and contemporaneous both-fixed comparison.
**Dominik Scholz, PR #38** independently composed both fixed factors with
copied centers. The balanced physical assembly and its arithmetic are imported from PR #34/#37,
with the RaD source reports preserved.
All original notices, licenses and assistance disclosures are retained.

Source pins are in `SOURCE.json`. Run `make copied-fixed-verify` for full
new producer, independent algebra and exact-certificate checks, and
`make verify` for the integrated repository suite. This increment targets PR #43 commit
`c0fbfd3cc4fd6e95cef54ab307dfb50c69dd96f6`; its full inherited base is pinned
PR #36 commit `11817ccacb564bb7f98789c20dc11d3fece207e3`.
