# Sample-Size Methodology — Track 5 (Sportsbook Player Props)

**Session:** 6.7 — Live Validation Window
**Status:** Draft — becomes final once Session 6.7 closes.

## What this document answers

Same question Session 2.5 answered for Track 1, Session 3.6 for Track 3
(arbitrage), and Session 5.7 for Track 4 (politics): **how many graded
results does Track 5 need before its performance is treated as meaningful,
instead of noise?** Derived from real data already produced by Sessions
6.1–6.6, not a guessed calendar length.

## 1. Why this needs its own derivation, not a reused number

Track 5 is a probability track (like pick'em and politics), not a
defect-rate track (like arbitrage) — `clv_logger.py`'s props branch
(Session 6.3) flags a player/stat/side combination when the field-vig-
normalized model probability beats the platform's own no-vig implied
probability by at least `PROPS_FLAG_EDGE_THRESHOLD = 0.03`. So Session
2.5's one-sample proportion-test method applies here, same as Track 4.

Track 1's p₀ (0.5774) does not transfer — that came from PrizePicks'
fixed 3x/2-pick payout multiplier. Track 4's p₀ (0.892) does not transfer
either — that came from Kalshi/Polymarket's own real flagged-race prices,
a structurally different market. DraftKings/FanDuel player props are
priced in American odds per side, with no fixed payout multiplier — the
breakeven win rate for any one flagged side is just that side's own
no-vig implied probability (Session 6.1/6.2's
`american_odds_to_implied_probability()`). A representative p₀ has to be
pulled from what this track actually flags, same principle as Track 4.

## 2. The real breakeven win rate — sourced from real committed data

Computed directly against the real, currently-committed
`data/sportsbook_props/clv_log.csv` (230 real open flags, produced by
Sessions 6.5/6.6's real pipeline runs across DraftKings and FanDuel):

- **230 real rows are currently flagged** under `PROPS_FLAG_EDGE_THRESHOLD
  = 0.03`.
- `first_flagged_market_price` (the real breakeven for each flagged side):
  mean **0.2255**, median 0.1182, min 0.0055, max 0.5717.
- `first_flagged_edge` (real edge over that breakeven at flag time): mean
  0.2750, median 0.2022 — noticeably larger than Track 1/4's typical
  flagged edges, a real property of this track's data, not a modeling
  error (see Section 4).

**Used here: p₀ = 0.2255** (the real mean breakeven), as the
representative price this track's flagged population needs to beat.

## 3. Sample-size formula

Same method as `docs/sample_size_methodology.md` Section 3 (standard
one-sample proportion test, normal approximation):

```
n = [ z_(α/2) × √(p₀(1−p₀))  +  z_β × √(p₁(1−p₁)) ]²  /  (p₁ − p₀)²
```

- **p₀ = 0.2255** (Section 2)
- **p₁ = 0.2555** — p₀ plus exactly `PROPS_FLAG_EDGE_THRESHOLD` (0.03),
  the minimum real edge this track's own flagging logic requires before a
  row is ever logged. Chosen the same way Track 1/4's p₁ was — a real,
  discernible edge, not an arbitrarily large one — and specifically the
  *smallest* edge this track would ever actually need to detect, since
  any flagged row already clears this bar by definition.
- **α = 0.05** (z = 1.96), **power = 0.80** (z = 0.84) — same standard
  values used by every prior track's derivation.

```
√(p₀(1−p₀)) = √(0.2255 × 0.7745) = √0.17467 = 0.4179
√(p₁(1−p₁)) = √(0.2555 × 0.7445) = √0.19022 = 0.4362

numerator   = (1.96×0.4179 + 0.84×0.4362)² = (0.8191+0.3664)² = (1.1855)² = 1.4053
denominator = (0.2555 − 0.2255)² = (0.03)² = 0.0009

n = 1.4053 / 0.0009 ≈ 1562
```

**Result: ≈ 1,562 graded flags** needed for standard statistical
confidence that a real observed win rate at least 3 points above breakeven
reflects a genuine edge, not sampling noise.

## 4. Why this number sits between Track 1's (≈3,725) and Track 4's (≈892)

Real, correct property of the math, not an inconsistency: variance
(`p(1-p)`) is largest near p=0.5 and shrinks toward the extremes. Track
1's flagged legs cluster near a coin flip (p₀=0.577, close to 0.5) —
highest variance, largest n. Track 4's flagged races cluster near-certain
(p₀=0.892, near 1) — lowest variance, smallest n. Track 5's real p₀
(0.2255) sits closer to an extreme than Track 1 but not as close as Track
4, landing its required n in between. This also explains why this track's
real flagged edges (mean 0.275) run larger than the other two tracks': a
model probability meaningfully above a low-probability breakeven (e.g.
0.50 vs. 0.23) is a proportionally much bigger edge-in-odds-terms move
than the same absolute distance would be near 0.5 or near 1 — a real
structural feature of American-odds-priced long-shot-heavy prop markets
(this track's 230 real flags skew toward touchdown-scorer and similar
long-shot markets, per `data/sportsbook_props/clv_log.csv`'s real
`prop_category` column), not evidence the model is unusually confident.

## 5. Real, honest finding: zero graded flags exist yet

All 230 real flags currently in `clv_log.csv` show `status == "open"` —
none have reached `closing_market_price`/`clv_edge_at_close` yet. This is
expected, not a defect: these are real NFL props tied to specific real
games (`game_start_time` values cluster around 2026-09-10, the current
week's slate), and `clv_logger.py` only marks a row closed once it
disappears from the platform's own latest pull (the same "disappeared ==
closed" convention Track 1/4 use), which happens once a game locks or the
market is taken down — not before. Unlike Track 4's ~55-day race
timescale, this track's real resolution timescale is short (days, not
months) — the first real closed flags are expected within the current
NFL week, once Session 6.5's 3-hour-cadence pipeline runs across a game's
actual kickoff.

## 6. What this means practically — same recurring-review pattern

- **Interim floor: 30 graded flags** — same floor used by every prior
  track's own Section 6/recurring-review pattern. Below this, no
  directional read is reported as meaningful.
- **Full target: ≈1,562 graded flags** (Section 3) — the number a
  recurring review reports progress against, not a single gate.
- Given the real, short (days-scale) resolution timescale found in
  Section 5, this track's interim floor is realistically reachable within
  the current NFL season, unlike Track 4's multi-cycle timescale — a real,
  favorable difference worth stating plainly rather than assuming every
  track's live-validation window behaves the same way.

## 7. Limitations — stated, not silent

- **p₀ = 0.2255 is a snapshot of one real data pull**, not a stable
  population parameter — it will shift as more weeks of real NFL props are
  ingested and as the mix of prop categories (touchdown scorer vs. yardage
  totals vs. other markets) shifts. Re-deriving it periodically, matching
  Track 1/4's own precedent, is appropriate.
- **This track has no realized-outcome tracker yet** — `outcome_tracker.py`
  (Session 2.5) remains hardcoded to `data/pickem/clv_log.csv` and
  PrizePicks-specific breakeven math (the same finding Sessions 3.6 and
  5.7 already made for their own tracks). Building a props-specific
  version is deferred until at least one real flag has actually closed
  with a real graded win/loss outcome to test it against — building it
  blind would risk the same false-confidence problem Session 2.4's
  Decision #6 already named once for this project.
- **`implied_prob_includes_field_vig` is True for 102 of the 230 real
  flags (44%)** — per Session 6.4, these rows' underlying no-vig
  probability is a coarser estimate than the 128 rows where the field's
  own vig could be fully backed out. This document does not split p₀ by
  that flag (v1 scope, same reasoning as Session 6.6's decision to keep
  it a per-row badge rather than a separate track); a future recalibration
  pass could test whether the two groups' real hit rates actually differ.
