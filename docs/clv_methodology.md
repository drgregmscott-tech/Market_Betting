# CLV-Equivalent Calibration Logging — Methodology (Session 2.4)

## What this document is

This explains what `scripts/calibration/clv_logger.py` measures, why it
measures it that way, and what it does not yet measure. It exists so a
future session — or a fresh read of this project cold — does not have to
re-derive the reasoning from the code itself.

## The problem this session solves

Per ROADMAP.md's "Rule for every session," a track's estimation model is not
considered validated until it is logging a real, pre-outcome
price-vs-benchmark comparison on every flagged opportunity — not just
producing plausible-looking numbers. Session 2.3 built the model. This
session builds the logging layer that lets a future session judge, honestly,
whether the model's confidence lines up with anything real, well before any
bet resolves.

## Why this isn't the same thing as sportsbook CLV

Real Closing Line Value compares the price you got when you bet against that
same market's price right before it closes. The assumption: if the market
moves toward your side after you take it, you were early and right. That
assumption depends on the market repricing continuously against real money
flow — which is exactly what PrizePicks and Underdog do **not** do. Session
0.1's research is explicit: these are "static, non-repricing lines." So this
project cannot just port sportsbook CLV over unchanged and call it done — a
platform's own line failing to move toward the model's side would not be
real evidence the model was wrong, because the platform mostly doesn't move
lines at all, right or wrong.

## The two benchmarks actually logged

**1. Cross-platform consensus (primary).** At the moment a prop is flagged,
the logger checks whether the same real-world prop — same player, same
underlying stat (matched via `resolved_stat_key`, a Session 2.4 addition to
`pickem_model.py` — see that file's docstring), same game — is also priced
on the other platform at that same moment. If so, that platform's own
implied probability is logged as an independent second opinion. This is the
closest thing this project has to a sharp-book benchmark for pick'em
platforms, in the absence of a real one.

**2. Own-line movement to close (secondary).** Because Session 2.2's
ingestion pipeline is designed to run hourly, the logger re-checks every
open flag on every subsequent run. Once a flagged prop's `source_line_id`
stops appearing under its own platform, the last line and implied
probability seen before it disappeared are frozen as its "closing" values —
the literal pick'em analog of a closing line, for whatever it turns out to
be worth. This is logged, not assumed to be meaningful; the whole point of
tracking it alongside the consensus benchmark is to let a future session
(2.5 onward, once real graded outcomes exist) check which — if either —
actually correlates with the model being right.

Both benchmarks are recorded side by side on every row, explicitly labeled,
rather than blended into a single number, so nothing is silently favored
ahead of real evidence.

## What "the platform's own implied probability" means for PrizePicks —
## clarified during Session 2.5, a real correction, recorded here

PrizePicks' rows use a flat 50% as "the platform's own implied probability"
throughout this document and in `pickem_model.py`. **This 50% is a flagging
sensitivity threshold, not a claim about PrizePicks' real breakeven win
rate.** Session 2.5 derived the actual real breakeven for a specific,
common entry type (a 2-pick Power Play: √(1/3) ≈ 57.7%, from PrizePicks'
own published 3x payout — see `sample_size_methodology.md`, Section 2) and
this surfaced a real point of confusion worth stating plainly: 50% and
57.7% are answering two different questions, and neither should be
mistaken for the other.

- **50% (used here, in `clv_logger.py` and `pickem_model.py`) answers:**
  "is this prop interesting enough to flag and log at all?" At the moment
  a prop is flagged, no entry type has been chosen yet — the same flagged
  leg could end up in a 2-pick, 3-pick, 4-pick, or Flex entry, each with
  its **own, different** real breakeven. A single flat number was needed
  at this stage regardless, and 50% (maximum flagging sensitivity) was the
  explicit, stated placeholder chosen — not a claim that PrizePicks is
  priced like a coin flip.
- **57.7% (used only in `sample_size_methodology.md`) answers:** "for one
  specific, named entry type actually played, what real win rate is
  needed to break even?" This number is entry-type-specific and only
  becomes the right question once a specific entry type is chosen — which
  happens downstream of flagging, at the point a flagged leg is actually
  sized into a real entry. **That real breakeven economics work is Session
  2.6's job (Bankroll & Sizing Logic), not Session 2.3's or 2.4's** — this
  is noted here so a future session doesn't try to retrofit 57.7% (or any
  other single entry type's breakeven) into the flagging/CLV layer, where
  no single number is correct across every possible entry type a flag
  could end up in.

No code changed as a result of this clarification — `FLAG_EDGE_THRESHOLD`
and the flat-50% PrizePicks assumption in `pickem_model.py` are unchanged.
This section exists solely to close the ambiguity between the two numbers,
which had genuinely caused confusion (see SESSION_LOG.md, Session 2.5
entry) before being resolved.

## What counts as "flagged" — a stated, unvalidated threshold

`FLAG_EDGE_THRESHOLD = 0.03` in `clv_logger.py`. A prop is logged only when
the model's probability is at least 3 percentage points away from the
platform's own implied probability, on whichever side has the edge. This
number is a placeholder, not a researched figure — no graded outcome data
exists yet to derive a real number from, which is exactly what this
calibration loop exists to eventually produce. It was chosen loosely enough
to generate a meaningful number of real flags for this session's own testing
and for the real live data Session 2.4 will run against, without flagging
nearly everything the model can estimate at all (a threshold of 0 would do
that, and would validate nothing). Re-deriving this threshold from real
graded results belongs to Session 8.3 (Ongoing Recalibration Cadence), not
this session.

## Log schema (`data/pickem/clv_log.csv`)

One row per flagged opportunity, created the first time it clears the
threshold and updated on every later run while still open:

| Column | Meaning |
|---|---|
| `flag_id` | `platform + "\|" + source_line_id` — stable key across runs |
| `flagged_side` | `over` or `under` — whichever side cleared the threshold |
| `first_flagged_*` | Line, model probability, implied probability, and edge at the moment this was first flagged — frozen forever after |
| `consensus_available` | Whether the other platform had a matching prop at flag time |
| `consensus_*` | The other platform's line/implied probability/edge at that same moment, if available |
| `last_seen_*` | Updated every run the prop is still present — the most current line/probability while open |
| `status` | `open` while still appearing in ingestion runs, `closed` once it stops appearing |
| `closing_*` | Frozen from `last_seen_*` at the moment `status` flips to `closed` |
| `line_moved` | **(Session 2.19 fix — see that section below.)** Whether `closing_implied_prob` differs from `first_flagged_implied_prob` — i.e. whether the real PRICE signal moved, not whether the point line (`closing_line` vs `first_flagged_line`) did. `None` for PrizePicks rows (not applicable — see below). |
| `clv_edge_at_close` | `first_flagged_model_prob − closing_implied_prob` for Underdog. **`None` for PrizePicks** (Session 2.19 fix — see below; this used to be a tautological, always-"positive" number, not real evidence) |

A parallel, timestamped snapshot is also written to
`data/pickem/clv_snapshots/` on every run, matching Session 2.2's
snapshot-plus-latest pattern, so the log's state at any past run can be
recovered even after later runs overwrite `clv_log.csv`.

## Session 2.19 — fixing the tautological PrizePicks CLV-at-close metric

**The real finding, checked live 2026-09-14.** Every one of PrizePicks'
10,750 closed flags in `data/pickem/clv_log.csv` showed `clv_edge_at_close`
byte-identical to `first_flagged_edge`, producing a reported "100%
positive-edge rate" that is not real evidence of anything. Root cause:
`closing_implied_prob` for a PrizePicks row is always
`PRIZEPICKS_ASSUMED_IMPLIED_PROB` — a flat, constant 0.5 defined in
`pickem_model.py` (see "What 'the platform's own implied probability' means
for PrizePicks," above). It is not derived from a real, moving market price
at all; it is the **same** constant already used to compute
`first_flagged_edge`. Since a flag can only be created once its edge already
clears the 3% threshold, every closed PrizePicks flag was mathematically
guaranteed to show a "positive" CLV at close, regardless of whether the
model was actually any good. This is a tautology, not a validation signal.

**The decision (not just a code change).** There is no fix that makes this
number real — PrizePicks does not publish a per-side price that could move,
so there is nothing for `closing_implied_prob` to differ from. Going
forward, `clv_edge_at_close` and `line_moved` are reported as **not
available** (`None`) for every closed PrizePicks flag, rather than a
fabricated or misleadingly "real-looking" number. Session 2.18's real-outcome
grading (`data/pickem/outcome_log.csv`) is PrizePicks' real validation
signal now — CLV was never meant to be the last word, only a pre-outcome
stand-in until real graded outcomes existed.

**The second, independent bug this surfaced: Underdog's `line_moved` was
comparing the wrong field.** It compared `closing_line` to
`first_flagged_line` — the point stat threshold (e.g. "74.5 receiving
yards"), which a platform essentially never revises once posted. But the
real price signal `clv_edge_at_close` is actually computed from is the
**implied probability**, derived from Underdog's real, independently-moving
per-side payout multipliers. Checked live: comparing the wrong field made it
look like Underdog's line almost never moved (0 of 9,885 closed flags showed
`line_moved=True`). Comparing the right field (`closing_implied_prob` vs
`first_flagged_implied_prob`) found the real number: **672 of 9,885 closed
Underdog flags (≈6.8%) show a genuine implied-probability move between
first-flag and close.** That is a real, if modest, rate of real price
movement — the mechanism is sound, it was just measuring the wrong thing.
`data/pickem/clv_log.csv` was backfilled once, in place, to correct both
bugs on every already-closed historical row (10,750 PrizePicks rows'
`clv_edge_at_close`/`line_moved` set to `None`; 9,178 Underdog rows'
`line_moved` recomputed against the real implied-probability field) — not
just fixed going forward, since the frontend reads this file directly and
old rows would otherwise keep showing the old, wrong numbers indefinitely.

**Frontend impact.** The Pick'em tab's "Average CLV edge" and "Positive-edge
rate" stats (`frontend/app.js`) already filter to rows where
`clv_edge_at_close` is not null before averaging — so once PrizePicks rows
report `None`, they silently and correctly drop out of those two stats on
their own, leaving only Underdog's real signal. The "Closed & graded" count
was decoupled from that same filtered set so it still shows the true total
closed-flag count across both platforms, with a caption clarifying that the
CLV average/hit-rate reflect Underdog only.

## What this script does not do yet (stated gap, not silent)

- **No real outcomes.** This is a pre-outcome signal only. Realized-outcome
  tracking (did the bet actually win) is Session 2.5's separate log
  (`outcome_log.csv`), tied back to this log's `flag_id` by a future
  session, not built here.
- **Consensus matching requires an exact `resolved_stat_key` match.** If a
  stat resolves on one platform but not the other (e.g. an unmapped
  `stat_type` string on just one side), no consensus match is found even if
  the same real prop exists on both platforms — a missed match, not a wrong
  one, which was the deliberate tradeoff (see `clv_logger.py` docstring).
- **Game-lock detection is inferred, not confirmed.** A prop is treated as
  "closed" simply because it stopped appearing in a run. Session 2.1/2.2
  never enumerated every real `status` value either platform can return, so
  a prop pulled for some other reason would look the same as a locked one
  in this log.
- **Not yet wired into automation.** This script is run manually, after each
  manual `pickem_model.py` run, for now. Automation is Session 2.7.
