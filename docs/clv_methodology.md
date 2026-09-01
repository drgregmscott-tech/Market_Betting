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
| `line_moved` | Whether `closing_line` differs from `first_flagged_line` |
| `clv_edge_at_close` | `first_flagged_model_prob − closing_implied_prob` — the literal pick'em-analog CLV number |

A parallel, timestamped snapshot is also written to
`data/pickem/clv_snapshots/` on every run, matching Session 2.2's
snapshot-plus-latest pattern, so the log's state at any past run can be
recovered even after later runs overwrite `clv_log.csv`.

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
