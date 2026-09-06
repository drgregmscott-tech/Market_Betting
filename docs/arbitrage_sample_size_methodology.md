# Arbitrage Sample-Size Methodology (Session 3.6)

## Why this document exists

Session 2.5 derived pick'em's sample-size threshold (3,725 graded legs) from
real math: a known payout structure has a known breakeven win rate, so a
standard statistical calculation tells you exactly how many graded legs are
needed before a win rate means anything. Arbitrage has no such formula --
there is no win probability to size against (Session 3.3's own docstring:
"there is no win/loss probability to plug into Kelly at all"). This document
works out, honestly, what an equivalent number *can* mean for arbitrage, and
where it comes from.

## The real question this session answers

Session 3.6's roadmap card asks: are the detector's flagged opportunities
real and executable, not stale or a matching error? This is a **defect-rate
question about the detection code**, not a statistical-edge question about
a betting strategy. The right tool for "how many clean trials until I'm
confident a process's defect rate is low" is not Session 2.5's win-rate
math -- it's the standard statistical convention used for exactly this
situation, worked out below.

## Step 1 -- the detector has three distinct mechanisms, not one

Confirmed directly from `scripts/arbitrage/detector.py` and
`scripts/ingestion/venue_matcher.py` (not assumed):

1. **`single_venue`** (`detect_single_venue_mispricing`) -- one venue's own
   YES + NO price doesn't sum to $1. No cross-venue matching at all.
2. **`cross_venue` / `elections_wide`** (`_find_elections_matches`) --
   down-ballot Elections markets matched Kalshi<->Polymarket via Session
   3.4's district-code logic.
3. **`cross_venue` / `bucketed`** (`_find_bucketed_matches`) -- everything
   else (currently Climate/Commodities), matched via a coarser time-bucket
   comparison.

These are three separate code paths with separate failure modes. A bug in
one (see below) says nothing about the reliability of the other two, so
each needs its own sample, not one combined count.

## Step 2 -- we already have a real, measured defect rate for one path

Session 3.4's first live automated run of the `elections_wide` path
produced 10 real flags, of which **9 were confirmed false positives**
(cross-state matches like Kalshi's WA-08 vs. Polymarket's IN-08) -- a 90%
observed defect rate, before the district-code fix. This is not a
hypothetical worst case; it is what this specific system actually did on
its first real run. Any sample-size target that would still consider "1 or
2 clean examples" sufficient evidence of a fix is not taking that real
history seriously.

## Step 3 -- the objective method: rule-of-three sampling

Standard convention for zero-failure attribute sampling: observing `n`
consecutive clean (non-defective) trials with zero failures gives ~95%
confidence that the true failure rate is below `p`, where

```
n ≈ 3 / p
```

This is the same category of real, named statistical tool Session 2.5 used
(real math, not an invented number), applied to a defect-rate question
instead of a win-rate question.

| Target confidence that residual fault rate is below... | n needed |
|---|---|
| 50% | 6 |
| 20% | 15 |
| 10% | 30 |
| 5% | 60 |

Given Session 3.4's own measured 90% pre-fix defect rate, "confident the
true rate is now below 10%" (n=30) is the honest bar -- not the smallest
number on the table, and not the largest.

## The full-confidence target

**30 confirmed-clean, distinct real opportunities per mechanism (90 total
across all three)** is this project's real, documented "high confidence"
target for arbitrage -- the direct equivalent of pick'em's 3,725-leg
threshold. It is derived from Step 3's math applied to Step 2's real
measured defect rate, not chosen because it sounded reasonable.

## Why this session does not wait for that number

At the real observed flag frequency as of this session (one distinct
opportunity in the `elections_wide` path over ~6 hours of live running; zero
ever observed in the other two mechanisms across all 4 real runs to date),
reaching 30 per mechanism could take weeks, and for the two mechanisms that
have never fired at all, it is not yet known whether they are rare or
broken. Blocking this session's close on the full target would repeat the
exact mistake this project already corrected in Sessions 2.1, 2.2, and 2.4:
importing a rigor level the current real data cannot support without an
unreasonable wait.

## The interim floor (agreed directly with the user, 2026-09-06)

Session 3.6 closes its "minimum sample size" checklist item once, for
**each of the three mechanisms**, either:
- at least 1 genuine, confirmed-executable distinct opportunity has been
  observed, **or**
- a real, stated observation window has passed with zero candidates,
  documented as a legitimate finding ("this mechanism may simply fire
  rarely against current market conditions") rather than treated as a
  blocker.

This interim floor is explicitly a judgment call, not a derived number --
named as such, same posture as `KELLY_FRACTION` or `EXECUTION_RISK_BUFFER`
elsewhere in this project. The 30-per-mechanism target above remains the
real, documented bar for actual high confidence, and is carried forward as
an ongoing recurring review (same pattern as Session 2.5's
`weekly_review.py` for pick'em), not something this session is expected to
reach on its own.

## Tooling

`scripts/calibration/arbitrage_flag_tracker.py` implements the
deduplication and per-mechanism progress tracking described here. See that
script's own docstring for the exact identity rule used to recognize the
same real opportunity across runs where the detector's venue-a/venue-b
labeling flips.
