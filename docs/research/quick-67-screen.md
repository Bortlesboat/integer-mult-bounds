# A bounded screen for a quick 2^-67 certificate

Historical screen: a subsequent [changed incidence circuit](incidence-network.md)
does establish conditional 2^-67. It changes the gates and frames, outside
the unchanged-trajectory pooling scope audited here.

The current conditional certificate remains 2^-75. No 2^-67 certificate
was found. With the current recipe G=3a^2/70, a bit saving a=4e-10 would
suffice for 2^-67; this is about 14.8 times the certified a=2.7e-11.

Two scoped obstructions make further parameter and scratch-pooling work
unpromising for this milestone. They do not exclude new finite networks.

## Pooling the original scratch trajectories

Keep the complete-triple scalar circuit and every rational gate label fixed.
Write v=binomial(h,3), N=v^3, m=h^3, z=3 binomial(h-3,2),
A=v^2(vz+h), W=2N+3A, and D=N-6v^2h^2. There are A auxiliary
trajectories in each of three invocations. The original relative rank deficit
is D/(Wm). We allow these trajectories to share physical roles sequentially.

For nondegenerate subspaces E,H, their orthogonal projections satisfy

    rank(P_H-P_E)=dim E+dim H-2 dim(E intersect H).

Indeed their difference has kernel (E intersect H) direct-sum
(E-perp intersect H-perp). This argument does not assume a definite form
or a nondegenerate intersection. Joining a trajectory ending at E to one
starting at H replaces two endpoint edges by one. It saves
m-2 delta rank, where delta=dim E-dim(E intersect H)>=0. Thus the role
count falls by one and the absolute deficit falls by 2 delta.

Only a stage-1 to stage-3 join can have delta=0. A stage-j tail is
F^j tensor Q, of dimension h^j. A stage-k head is contained in the center
head, of dimension h^k-h. This excludes containment whenever j>=k.
For 1 to 2, the new head excludes a nonzero line in the first factor,
whereas the old tail contains the whole first factor. For 2 to 3, the
new head excludes a nonzero tensor line in the first two factors, whereas
the old tail contains their whole tensor product. These cases also have
delta>=1. The existing stage-sharing construction exhibits zero-penalty
1 to 3 joins.

Consequently at most A joins have zero penalty. If Z<=A such joins and B
positive-penalty joins are made, the new ratio is at most

    (D-2B)/(m(W-Z-B)) <= D/(m(W-A)).

The second inequality follows from D<2(W-A). This grants all center and
side sharing, including hypothetical matchings, so it is an optimistic upper
bound. At h=46 it improves the current role count by less than one part per
million. It cannot supply another full bit of exponent improvement.

The exact log-enclosure search over 39<=h<200 has its maximum at h=46.
For h<=38 the deficit is nonpositive. For h>=200, the bounds
eta<1/(2zm) and log(m)>1 give a<1/(2zm-1); this decreasing tail is below
the finite maximum. Substituting the upper enclosure into the necessary
downstream bound kappa<a^2/(20(1-a)) gives kappa<2^-74, hence <2^-67.

This is a bound on pooling unchanged auxiliary trajectories, not on new
gates, new labels, overlapping aggregation, or arbitrary scalar circuits.

## Other easy label models

The [block-label audit](block-label-feasibility.md) bounds the entire
positive-definite ambient family, even allowing all h and all label ranks,
under the stated shared-side counts. Its optimistic downstream upper bound
is about 2^-67.574, below 2^-67. The unrestricted indefinite rational
problem is still open. Numerical failures do not establish nonexistence.

The economical next step is a genuinely different algebraic label or circuit
construction aimed at the 50s, rather than a separate extended search for 67.
The unrealized two-plane target and its explicit missing hypothesis are
recorded in [the roadmap](next-steps.md).

Reproduce the pooling arithmetic with `python3 scripts/audit_scratch_pooling.py`.
Its output is `certificates/scratch-pooling-audit.json`; the symbolic scope
and containment arguments above remain mathematical proof obligations, not
claims of automated theorem proving.
