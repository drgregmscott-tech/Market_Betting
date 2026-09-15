# Underdog Cross-Sport Pricing Gap Investigation

**Session:** 2.31
**Status:** Complete (2026-09-15) — measurement only, no model change.
**Script:** `scripts/calibration/investigate_underdog_pricing_gap.py`

## What this document answers

Session 2.26's real grading run found Underdog's real win rate sits below
the 57.74% breakeven in every sport tested (MLB 46.4%, NFL 49.5%, both
n well past the 20-leg floor), while PrizePicks is comfortably profitable
in both (66.9% / 69.4%). Worse, Underdog's real win rate **falls** as the
model's own stated edge **rises** — an inverted relationship a uniform
sigma/overconfidence rescale (this project's Session 2.22 fix) cannot
correct, because that fix only corrects same-direction, wrong-magnitude
overconfidence, not a sign-flipped relationship between edge and outcome.

This document answers: what is actually causing the inversion, is it a
data bug or a real model/information gap, and what — if anything — should
this project do about Underdog flags right now.

## Part A — id-stability check (data-integrity, ruled out)

`over_under_lines[].id` (Underdog's `source_line_id`) is the only real
per-flag identifier this pipeline reuses across the life of a flag. If
Underdog silently reused an id for a different real prop, a flag's
recorded price/edge could belong to one prop while its later grading
belongs to another — a real explanation for a nonsense-looking result.

Checked directly against 4 real, full production Underdog pulls
(`data/pickem/raw/underdog_20260911T172815Z.json` through
`underdog_20260912T100543Z.json`, ~14,300 `over_under_lines` rows each,
spanning ~17 real hours on 2026-09-11/12): **8,339 real ids were present
in all 4 snapshots. Zero of them changed (appearance_id, stat,
stat_value) across any snapshot.** Underdog's ids are stable over a real
flag's lifetime.

**Conclusion: id-stability is clean.** Combined with the two checks
Session 2.26 already ran (no sign/side flip in
`implied_prob_over_underdog()`; Underdog flags caught with a *shorter*
median lead time, 7.3h, than PrizePicks', 13.7h — the opposite of what
staleness would predict) and this session's own `payout_multiplier`
cross-check against Underdog's separate `decimal_price`/`american_price`
field on a real 14,273-line pull (mean abs diff 0.49%, zero lines >5%
apart), **every cheap data-integrity explanation has now been checked and
ruled out.** This is not a data bug.

## Part B — real information-gap analysis

Real join: `data/pickem/clv_log.csv` (per-flag price/timing —
`first_flagged_at`, `game_start_time`, `first_flagged_edge`,
`first_flagged_implied_prob`) to `data/pickem/outcome_log.csv` (real
graded `result`) on `flag_id`, restricted to Underdog win/loss rows.
**10,380 real graded legs** (MLB 9,456 / NFL 924) had usable edge and
timing data (43 rows with a negative computed lead time — flag logged
after game start, a real but separate data-quality question — were
dropped before this analysis; not in scope here). Overall real Underdog
win rate on this joined set: **46.8%**, matching Session 2.26's number.

### B1 — the inversion, reproduced directly

| edge bucket | n | win% | avg implied prob |
|---|---:|---:|---:|
| 0.00–0.10 | 4,187 | 47.9% | 0.4843 |
| 0.10–0.20 | 3,839 | 47.6% | 0.4585 |
| 0.20–0.30 | 1,653 | 46.1% | 0.4366 |
| 0.30–0.40 | 518 | 38.0% | 0.3965 |
| 0.40+ | 183 | 33.3% | 0.3760 |

Confirmed independently, same shape as Session 2.26's report. Splitting
by sport: MLB alone shows the same monotonic fall (47.8% → 27.6%,
n=3,884 → n=145). NFL alone is noisier at the top end (its 0.40+ bucket
is only n=38, below this project's 20-leg-per-cut floor is cleared but
barely — a single-sport read here is not trustworthy) but its 0.30–0.40
bucket (n=51) also dips to 31.4%, consistent with the same pattern, not
NFL-specific.

### B2 — lead-time x edge cross-tab (the key test)

The inversion was tested against the hypothesis that it's driven by real
news moving Underdog's price after the model's stat blend was computed —
if so, it should concentrate in long-lead-time flags and disappear at
short lead times. It does not:

| lead time | 0.00–0.10 win% (n) | 0.30–0.40 win% (n) | 0.40+ win% (n) |
|---|---:|---:|---:|
| 0–3h (short) | 50.1% (955) | 38.0% (108) | 29.7% (37) |
| 3–8h (medium) | 46.9% (1,291) | 39.8% (161) | 29.2% (48) |
| 8–16h (long) | 47.4% (1,095) | 38.0% (129) | 26.2% (42) |
| 16h+ (very long) | 47.8% (846) | 35.8% (120) | 44.6% (56) |

The drop from the lowest to the 0.30–0.40 edge bucket is present at
**every** lead-time bucket, including the shortest (0–3h, where there is
minimal real time for post-flag news to move Underdog's price before the
model's own blend was already current). **This rules out lead-time /
staleness as the driver of the inversion** — it is not "the model was
right when it looked and the world changed after." The 16h+ bucket's
0.40+ row (44.6%, n=56) is the one cell that doesn't fit the pattern as
cleanly, but n=56 split across 4 lead buckets and 5 edge buckets each
(20 cells) means several cells this thin should be expected to wobble;
it does not change the pattern at the 0.00–0.10/0.30–0.40 cells, which
are all well past the 20-leg floor.

### B3 — the inversion is concentrated on skewed ("chalk") lines, not high edge per se

Bucketing by how far Underdog's own implied probability sits from a
coin flip:

| skew bucket | n | win% | avg edge |
|---|---:|---:|---:|
| near-coinflip (\|p−0.5\|<0.05) | 2,582 | 51.8% | +0.1423 |
| mild skew (0.05–0.15) | 4,823 | 49.9% | +0.1348 |
| chalk / heavy skew (≥0.15) | 2,975 | 37.2% | +0.1551 |

**Restricting to near-coinflip Underdog lines only and re-running the
same edge-bucket cut (B3d) makes the inversion mostly disappear:**

| edge bucket (near-coinflip lines only) | n | win% |
|---|---:|---:|
| 0.00–0.10 | 1,023 | 50.4% |
| 0.10–0.20 | 964 | 52.3% |
| 0.20–0.30 | 433 | 53.8% |
| 0.30–0.40 | 121 | 51.2% |
| 0.40+ | 41 | 56.1% |

Win rate is flat-to-slightly-rising with edge here — the opposite shape
from the pooled result — though every point in this restricted cut still
sits under the 57.74% breakeven (the 0.40+ row, n=41, is the closest at
56.1%, but that n is thin enough to not be trusted on its own). The
correlation between the model's stated edge and Underdog's own price skew
is weak but positive (+0.0591) — not the main mechanism — but the B3/B3d
split shows skew, not edge magnitude itself, is what actually separates
the good cells from the bad ones: **the model's confidence and
Underdog's own price confidence point the same direction on chalk lines,
and Underdog is right far more often (37.2% real win rate against the
model's own "you should take the other side" signal).**

### Stat-type check: platform comparison rules out a stat-specific model bug

`RBIs` stood out as Underdog's single worst stat type (33.2%, n=1,697,
avg edge +0.18 — a real, large group, not a thin one). Checked directly
whether this is a general model weakness on RBIs (which would show up on
PrizePicks too) or something specific to how Underdog prices RBIs:

- PrizePicks RBIs: **75.95% win rate (n=341)**
- Underdog RBIs: **33.06% win rate (n=1,706)**

Same stat, same underlying model estimate methodology, opposite real
result by platform. **This rules out "the model is bad at RBIs" as an
explanation** — the model's RBIs estimate is fine against PrizePicks'
price; it is Underdog's own RBIs price specifically that is hard to beat.

## Conclusion — root cause

Not a data-integrity issue (Part A, plus Session 2.26's and this
session's earlier checks, all clean). It is a **genuine, platform-level
informational gap concentrated on skewed lines**: Underdog's own per-side
price on lines it has already moved away from a coin flip (chalk/favorite
lines) reflects real information — likely lineup, weather, recent
matchup, or market-flow signal — that this project's season-average +
recent-form blend does not have and does not react to, regardless of how
much real time passed between flag and game start (B2 rules out
staleness as the mechanism). On lines Underdog has NOT moved away from a
coin flip, the model's edge signal does not show the same inverted
relationship (B3/B3d) — the informational gap is a property of Underdog's
own skewed pricing, not of the model's edge number in general.

## Decision

1. **Underdog is not usable as a blanket flag source in any sport right
   now.** MLB 46.4% / NFL 49.5% aggregate, both below breakeven, both on
   samples well past this project's 20-leg floor (n=9,499 / n=924).
2. **No Underdog segment currently clears breakeven with a trustworthy
   sample.** The closest candidate — near-coinflip lines (\|implied_prob
   − 0.5\| < 0.05) — sits at 50–54% across every edge bucket with n≥121,
   still under the 57.74% breakeven; its only bucket that crosses toward
   breakeven (56.1%) is n=41, too thin to act on per this project's own
   sample-size standard (`docs/props_sample_size_methodology.md` Section
   6's 20-leg interim floor is cleared, but this is nowhere near the
   ~900–3,700-leg full-confidence range that methodology derives for
   comparable breakeven levels elsewhere in this project). **Restricting
   Underdog to near-coinflip lines only is the one lead worth tracking as
   more legs grade in — it is not yet an actionable segment.**
3. **The existing Session 2.26 "Below breakeven" frontend badge
   (`frontend/app.js`'s `classifySportStatus()`) is sufficient as-is.**
   It already reads real per-sport/per-platform performance from
   `outcome_log.csv` and marks Underdog `underperforming` in both
   validated sports; nothing in this investigation's findings changes
   what the frontend should tell a user today. No frontend change is
   proposed by this session, matching its own explicit scope (measurement
   only).
4. **A real, scopeable fix exists but is out of scope here, per this
   session's own card:** test whether gating/down-weighting Underdog
   flags by `|implied_prob − 0.5|` (i.e. only trusting Underdog edges on
   near-coinflip lines, or applying a skew-dependent discount to
   Underdog's stated edge) recovers a usable segment once more legs have
   graded past the near-coinflip cut's current thin n. This is a model
   change (touches how Underdog edges get sized/filtered) and belongs in
   its own follow-up session, not this investigation.

## Limitations

- This investigation's B2/B3 buckets are real cuts of a real, fixed
  10,380-leg sample, not independently re-collected data — the same
  underlying rows appear across B1/B2/B3, so these are correlated views
  of one dataset, not independent confirmations.
- NFL-only reads throughout this document are on thin samples (924 total,
  down to 38–56 in individual cells) — every NFL-specific number here
  should be read as directionally consistent with MLB's much larger
  sample, not as independent proof on its own.
- The near-coinflip segment's apparent lack of inversion (B3d) is the
  most actionable finding in this document but is itself only ~2,582
  legs total, thinning further once split by edge bucket — worth
  re-running this script's B3d cut specifically as more Underdog legs
  grade in before treating it as a real, tradeable segment.
