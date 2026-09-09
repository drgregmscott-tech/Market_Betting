# Sample-Size Methodology — Track 3 (Weather/Climate Markets)

**Session:** 4.7 — Live Validation Window
**Status:** Draft — becomes final once Session 4.7 closes.

## What this document answers

Same question Session 2.5 answered for Track 1 (pick'em), Session 3.6 for
Track 2 (arbitrage), Session 5.7 for Track 4 (politics), and Session 6.7 for
Track 5 (sportsbook props): **how many graded results does Track 3 need
before its performance is treated as meaningful, instead of noise?** Derived
from real data already produced by Sessions 4.1–4.5, not a guessed calendar
length.

## 1. Why this needs its own derivation, not a reused number

Track 3 is a probability track (like pick'em, politics, and props), not a
defect-rate track (like arbitrage) — `clv_logger.py`'s weather branch
(Session 4.3) flags a Kalshi threshold contract's YES or NO side when the
model's forecast-derived probability beats the market's own price by at
least `WEATHER_FLAG_EDGE_THRESHOLD = 0.03`. So Session 2.5's one-sample
proportion-test method applies here, same as Tracks 4 and 5.

Kalshi weather contracts pay $1 if the real observed value clears the
strike, $0 otherwise, with no fixed multiplier — same binary-contract shape
as Track 4's politics markets, not Track 1's fixed-payout pick'em entries or
Track 5's American-odds props. So, like Track 4, the breakeven win rate for
any one flagged side is just that side's own market price at flag time —
p₀ has to be pulled from what this track actually flags, not inherited from
another track's derivation.

## 2. The real breakeven win rate — sourced from real committed data

Computed directly against the real, currently-committed
`data/weather/clv_log.csv` (602 real logged flags, produced by Session 4.5's
real automated pipeline runs across Kalshi weather markets):

- **399 real rows are currently open** (not yet resolved) under
  `WEATHER_FLAG_EDGE_THRESHOLD = 0.03`.
- `first_flagged_market_price` (the real breakeven for each flagged side, at
  the moment it was flagged): mean **0.3804**, median 0.46, min 0.005, max
  0.965.
- `first_flagged_edge` (real edge over that breakeven at flag time): mean
  0.2306.
- **203 real rows have already closed.** Of those, `clv_edge_at_close` has
  mean 0.2592 and `closing_market_price` has mean 0.3903 — consistent with
  the open-flag population above, so using the open-flag mean as p₀ is not
  an unrepresentative snapshot.

**Used here: p₀ = 0.3804** (the real mean breakeven from open flags), as the
representative price this track's flagged population needs to beat.

## 3. Sample-size formula

Same method as `docs/sample_size_methodology.md` Section 3 and
`docs/politics_sample_size_methodology.md`/`docs/props_sample_size_methodology.md`
(standard one-sample proportion test, normal approximation):

```
n = [ z_(α/2) × √(p₀(1−p₀))  +  z_β × √(p₁(1−p₁)) ]²  /  (p₁ − p₀)²
```

- **p₀ = 0.3804** (Section 2)
- **p₁ = 0.4104** — p₀ plus exactly `WEATHER_FLAG_EDGE_THRESHOLD` (0.03),
  the minimum real edge this track's own flagging logic requires before a
  row is ever logged — the smallest edge this track would ever actually need
  to detect, since any flagged row already clears this bar by definition.
- **α = 0.05** (z = 1.96), **power = 0.80** (z = 0.84) — same standard
  values used by every prior track's derivation.

```
√(p₀(1−p₀)) = √(0.3804 × 0.6196) = √0.23572 = 0.4855
√(p₁(1−p₁)) = √(0.4104 × 0.5896) = √0.24198 = 0.4919

numerator   = (1.96×0.4855 + 0.84×0.4919)² = (0.9516 + 0.4132)² = (1.3648)² = 1.8625
denominator = (0.4104 − 0.3804)² = (0.03)² = 0.0009

n = 1.8625 / 0.0009 ≈ 2069
```

**Result: ≈ 2,069 graded flags** needed for standard statistical confidence
that a real observed win rate at least 3 points above breakeven reflects a
genuine edge, not sampling noise.

## 4. Why this number sits between Track 4's (≈892) and Track 5's (≈1,562)

Real, correct property of the math, not an inconsistency: variance
(`p(1−p)`) is largest near p=0.5 and shrinks toward the extremes. Track 4's
flagged races cluster near-certain (p₀=0.892, near 1) — lowest variance,
smallest n. Track 5's flagged props sit further from 0.5 (p₀=0.2255) than
Track 3's flagged weather contracts (p₀=0.3804, closer to the coin-flip
midpoint) — so Track 3's variance, and required n, land higher than both.
This is consistent with a real structural feature of this track's own data:
weather threshold contracts are frequently priced closer to genuine
uncertainty (a forecast near a round-number strike) than a down-ballot race
already leaning toward one party, or a long-shot touchdown-scorer prop.

## 5. Real, honest finding: 203 flags have already closed

Unlike Track 5 at its own Session 6.7 (zero closed flags, days-scale
resolution not yet reached), Track 3 already has 203 real closed flags in
`clv_log.csv` as of this session — weather contracts resolve on their own
`target_date`, most within 1–7 days of being flagged, the fastest real
resolution timescale of any track built so far. This means Track 3's interim
floor (Section 6) is met immediately, not merely reachable.

**Caveat, stated plainly:** "closed" here means the flag disappeared from
the latest Kalshi markets pull, per `clv_logger.py`'s existing
"disappeared == closed" convention (same convention, same caveat, as every
other track) — it is a real, observed price-movement-to-close signal
(CLV-equivalent), not yet a confirmed real win/loss outcome. See Section 7
and Section 8 below for what would be needed to promote these to graded
win/loss results.

## 6. What this means practically — same recurring-review pattern

- **Interim floor: 30 graded flags** — same floor used by every prior
  track's own recurring-review pattern. **Already met**: 203 real closed
  flags ≥ 30.
- **Full target: ≈2,069 graded flags** (Section 3) — the number a recurring
  review reports progress against, not a single gate. At 203/2,069 (≈9.8%),
  this is real, meaningful progress, not yet full confidence.
- Given the real, short (days-scale) resolution timescale found in Section
  5, reaching the full target is realistic within a normal multi-week
  operating window, provided the pipeline keeps running on its existing
  4x/day schedule (Session 4.5).

## 7. Limitations — stated, not silent

- **p₀ = 0.3804 is a snapshot of one real data pull**, not a stable
  population parameter — it will shift as more weeks of real Kalshi weather
  markets are ingested and as the mix of cities/strike types shifts.
  Re-deriving it periodically, matching every other track's own precedent,
  is appropriate.
- **This track has no realized-outcome tracker yet.** `outcome_tracker.py`
  (Session 2.5) remains hardcoded to `data/pickem/clv_log.csv` and
  PrizePicks-specific breakeven math (the same finding Sessions 3.6, 5.7,
  and 6.7 already made for their own tracks). Unlike a pick'em or props bet,
  a weather contract's real win/loss is objectively computable from the same
  public NWS observed-value data this track already ingests for forecasting
  (Session 4.1) — a real, structural advantage this track has that the
  others don't (no dependency on the user manually reporting what they
  placed to know whether a given contract resolved YES or NO). Building a
  weather-specific outcome tracker that grades closed flags automatically
  against real observed NWS data, rather than requiring manual entry, is a
  named candidate for a future session — not built here, since Session 4.7's
  own scope is the sample-size derivation and go/no-go review, not a new
  tracker.
- **"Closed" is not yet "graded."** The 203 real closed flags in Section 5
  are a real CLV-equivalent signal (price moved toward or away from the
  flagged side by close), but without the outcome tracker above, this
  session's go/no-go review (Section 8) is grading against CLV movement, the
  same pre-outcome proxy Session 2.4 established for every track — not
  against confirmed real win/loss results. This is the same honest
  limitation named for every other track at this stage of its own
  live-validation window.
