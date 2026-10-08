# Community contributions

Thank you to everyone contributing proofs, constructions, parameter improvements,
independent implementations, checks, corrections and unsuccessful searches with
useful conclusions. Parallel work, small improvements and results later superseded
remain part of this project's research record. A contribution need not win the
headline to deserve acknowledgement.

This record accompanies the conditional **2^-30 checkpoint**, following the last
published exact witness **83/10^12 > 2^-34**. It covers submissions available on
October 8, 2026, including earlier work on the 2^-59 family and newer claims beyond
this checkpoint. It is not a ranking of contributors or a determination of priority.
Descriptions below summarize the submitted work; inclusion does not imply that a
PR's mathematics has been independently verified or its code incorporated.

## The 2^-34 to 2^-30 interval

The local complex-compression checkpoint was committed at `1c09a58` on October 8
at 01:10 UTC. eumemic's related complex construction in [#3](https://github.com/CrocSwap/integer-mult-bounds/pull/3)
was submitted at 02:23 UTC, and Rohan Arun's [#8](https://github.com/CrocSwap/integer-mult-bounds/pull/8)
provides another geometric complex candidate. These parallel contributions deserve
recognition alongside the local implementation. dleen's [#4](https://github.com/CrocSwap/integer-mult-bounds/pull/4)
adds retained totals and sharing; eumemic's [#5](https://github.com/CrocSwap/integer-mult-bounds/pull/5)
and [#6](https://github.com/CrocSwap/integer-mult-bounds/pull/6) claim stronger savings
through resampling and circuit changes. They were submitted before this release,
but are not dependencies silently imported into its proof.

Zhihao Chen's [#7](https://github.com/CrocSwap/integer-mult-bounds/pull/7) predates
this checkpoint's ternary implementation and contains the same F3 five-subset
motif, rational form and fixed-alphabet direction, with a different producer and
a stronger claimed bound. The checkpoint explicitly makes no priority claim for
that motif. Rohan Arun's [#9](https://github.com/CrocSwap/integer-mult-bounds/pull/9)
then refines its templates. Their submissions are credited even though this
checkpoint retains its separately checked producer and conservative assembly.

## Contributors and submitted work

Names follow the authors' supplied attribution where available; otherwise GitHub
handles are used. PR links preserve the full descriptions, co-credits and review
history. The [snapshot](docs/research/contribution-snapshot.json) pins every listed
submission, including closed PRs. The [review index](docs/research/contribution-review.md)
tracks acceptance separately.

| Contributor | Submissions | Contribution described in submissions |
| --- | --- | --- |
| Aurel Prosz (Paureel) | [#1](https://github.com/CrocSwap/integer-mult-bounds/pull/1) | Parameter refinement and a scoped fixed-exponent supremum; later two-stage topology and paid endpoint-copy work are credited by the incoming integration chain. |
| Bortlesboat | [#2](https://github.com/CrocSwap/integer-mult-bounds/pull/2) | Aligned pair groups and exact producer/frame checks; this supplies an ingredient used by later submissions. |
| eumemic | [#3](https://github.com/CrocSwap/integer-mult-bounds/pull/3), [#5](https://github.com/CrocSwap/integer-mult-bounds/pull/5), [#6](https://github.com/CrocSwap/integer-mult-bounds/pull/6), [#13](https://github.com/CrocSwap/integer-mult-bounds/pull/13), [#15](https://github.com/CrocSwap/integer-mult-bounds/pull/15) | Parallel complex-network compression, Gaussian resampling, cheaper centers, auxiliary source frames and later producer/batching refinements. |
| dleen | [#4](https://github.com/CrocSwap/integer-mult-bounds/pull/4) | Composition of shared exclusions, retained totals and stage sharing, with additional complex-network headroom. |
| Zhihao Chen (jacklightChen) | [#7](https://github.com/CrocSwap/integer-mult-bounds/pull/7), [#16](https://github.com/CrocSwap/integer-mult-bounds/pull/16), [#21](https://github.com/CrocSwap/integer-mult-bounds/pull/21), [#23](https://github.com/CrocSwap/integer-mult-bounds/pull/23), [#29](https://github.com/CrocSwap/integer-mult-bounds/pull/29) | Ternary five-subset construction, nested controlled bases, translated frames, semantic/bulk assembly and two-stage integration. |
| Rohan Arun (rohanarun) | [#8](https://github.com/CrocSwap/integer-mult-bounds/pull/8), [#9](https://github.com/CrocSwap/integer-mult-bounds/pull/9), [#11](https://github.com/CrocSwap/integer-mult-bounds/pull/11), [#12](https://github.com/CrocSwap/integer-mult-bounds/pull/12), [#14](https://github.com/CrocSwap/integer-mult-bounds/pull/14), [#17](https://github.com/CrocSwap/integer-mult-bounds/pull/17), [#19](https://github.com/CrocSwap/integer-mult-bounds/pull/19), [#25](https://github.com/CrocSwap/integer-mult-bounds/pull/25), [#28](https://github.com/CrocSwap/integer-mult-bounds/pull/28), [#31](https://github.com/CrocSwap/integer-mult-bounds/pull/31), [#37](https://github.com/CrocSwap/integer-mult-bounds/pull/37), [#39](https://github.com/CrocSwap/integer-mult-bounds/pull/39) | Parallel geometric complex construction; ternary template and matching work; dimension, corner and composition refinements; exact checks and review packages. |
| icekylinx | [#10](https://github.com/CrocSwap/integer-mult-bounds/pull/10), [#18](https://github.com/CrocSwap/integer-mult-bounds/pull/18), [#24](https://github.com/CrocSwap/integer-mult-bounds/pull/24), [#32](https://github.com/CrocSwap/integer-mult-bounds/pull/32), [#36](https://github.com/CrocSwap/integer-mult-bounds/pull/36) | Recursive batching, partial swaps, endpoint gauges, structured projector blocks and copied retained-center schedules. |
| RaD project (hipotures) | [#20](https://github.com/CrocSwap/integer-mult-bounds/pull/20) | Attributed research record and semantic precision, routing, phase-cell inverse and bulk-transfer work used by subsequent submissions. |
| Dominik Scholz (DominikScholz) | [#22](https://github.com/CrocSwap/integer-mult-bounds/pull/22), [#27](https://github.com/CrocSwap/integer-mult-bounds/pull/27), [#30](https://github.com/CrocSwap/integer-mult-bounds/pull/30), [#33](https://github.com/CrocSwap/integer-mult-bounds/pull/33), [#35](https://github.com/CrocSwap/integer-mult-bounds/pull/35), [#38](https://github.com/CrocSwap/integer-mult-bounds/pull/38) | Parameter and interface composition, near-balanced geometry, smaller two-stage dimensions and fixed local bases. |
| princezuda | [#26](https://github.com/CrocSwap/integer-mult-bounds/pull/26) | Lean certificate-check contribution; its formalized scope remains to be reviewed separately from the multiplication theorem. |
| James Chang (jamesyc) | [#34](https://github.com/CrocSwap/integer-mult-bounds/pull/34) | Reversed two-stage geometry, exact controls and balanced assembly. |

The incoming two-stage work also credits **Swapnil Jain** for linked two-stage
batching development, alongside Aurel Prosz's topology and endpoint correction;
see [#29](https://github.com/CrocSwap/integer-mult-bounds/pull/29) and
[#36](https://github.com/CrocSwap/integer-mult-bounds/pull/36) for their pinned
external sources. This acknowledgement does not imply those sources have yet
been imported or audited here.

Closed [#11](https://github.com/CrocSwap/integer-mult-bounds/pull/11) records
matching/prime-power generalizations and bounded negative screens without a new
headline. Closed [#30](https://github.com/CrocSwap/integer-mult-bounds/pull/30)
preserves a concurrent near-balanced construction overtaken by another submitted
bound. Both remain credited. Review, replication, bug reports and documented
negative results are also welcome contributions.

## Attribution as integration proceeds

- Keep original authorship, licenses, source pins and substantial AI-assistance
  disclosures when importing code or proofs.
- Credit an idea's supplied source as well as the person who checks, improves or
  integrates it. Preserve explicit predecessor credits rather than crediting only
  the final PR in a chain.
- Record incorporated results, parallel work and pending review distinctly.
  A merged file is not a claim of external mathematical acceptance.
- Retain acknowledgements when a bound is superseded, a PR closes, or a duplicate
  implementation is not imported. Do not infer joint authorship of a proof from
  a general acknowledgement.
- Corrections to names, contribution descriptions, omitted work and source links
  are welcome through an issue or PR. This is a dated record, not an exhaustive
  account of everyone who has helped outside the repository.

Douglas Colkitt's local research and integration work used OpenAI Codex.
The original manuscript and the underlying Harvey–van der Hoeven analytic work
retain their existing attribution. Contributor-specific AI disclosures and
licenses remain attached to their original submissions; acknowledgement here
neither replaces those notices nor asserts independent human review.

## Submissions received after the checkpoint snapshot

Rohan Arun's [#40](https://github.com/CrocSwap/integer-mult-bounds/pull/40)
extends the fixed-basis copied-corner work. It is queued separately; the current
integration pass remains pinned to #39 so its review has a stable target.
This addition does not rewrite the checkpoint's original 39-PR snapshot.
