# Sample-Size Methodology — Track 4 (Down-Ballot Politics)

**Session:** 5.7 — Live Validation Window
**Status:** Draft — becomes final once Session 5.7 closes.

## What this document answers

Same question Session 2.5 answered for Track 1 and Session 3.6 answered for
Track 3 (arbitrage): **how many graded results does Track 4 need before its
performance is treated as meaningful, instead of noise?** This document
derives that number using real data already produced by Sessions 5.1–5.5,
not a guessed calendar length.

## 1. Why this needs its own derivation, not a reused number

Track 4 is a probability track (like pick'em), not a defect-rate track
(like arbitrage) — `clv_logger.py`'s `build_politics_candidates()` (Session
5.3) flags a race/party/venue combination when the model's corrected
probability beats the venue's raw market price by at least
`POLITICS_FLAG_EDGE_THRESHOLD = 0.03`. So Session 2.5's one-sample
proportion-test method applies here, not Session 3.6's rule-of-three method.

But Track 1's own p₀ (0.5774) does **not** transfer: that number came from
PrizePicks' fixed 3x, 2-pick payout multiplier. Kalshi/Polymarket contracts
have no such fixed multiplier — each is a $1-payout binary contract bought
at its own market price, so **the breakeven win rate for any one flag is
just that flag's own market price** (buy at $0.90, need to win ≥90% of the
time to break even). A fixed single p₀ has to be a real, representative
number pulled from what this track actually flags, not assumed.

## 2. The real breakeven win rate — sourced from real committed data

Computed directly against the real, currently-committed
`data/politics/estimates/politics_estimates_latest.csv` (867 real race/party
rows, pulled from live Kalshi/Polymarket/ElectIndex data by Session 5.5's
orchestrator), applying the exact same filter `clv_logger.py` uses
(`model_status == "estimated"` and `edge_vs_raw >= 0.03`), across both
venues and both parties:

- **415 real rows would be flagged** under current data and threshold.
- Market price (real breakeven) of those rows: mean **0.892**, median
  **0.935**, min 0.565, max 0.962.

**This is a real, expected shape for this track, not a bug:** down-ballot
races Session 5.1 ingested are heavily lopsided (most seats are not
competitive), so most of the model's real disagreements-with-the-market are
small nudges on already-high-confidence races, not close calls. **Used
here: p₀ = 0.892** (the real mean), as the representative breakeven this
track's flagged population needs to beat.

## 3. Sample-size formula

Same method as `docs/sample_size_methodology.md` Section 3 (standard
one-sample proportion test, normal approximation):

```
n = [ z_(α/2) × √(p₀(1−p₀))  +  z_β × √(p₁(1−p₁)) ]²  /  (p₁ − p₀)²
```

- **p₀ = 0.892** (Section 2)
- **p₁ = 0.92** — a real, discernible edge (2.8 points above breakeven),
  chosen the same way Track 1's p₁=0.60 was: large enough to matter, small
  enough that a v1 model with no incumbency/fundraising/scandal adjustment
  (a named gap — see `politics_model.py`'s own docstring) isn't held to an
  unrealistic bar
- **α = 0.05** (z = 1.96), **power = 0.80** (z = 0.84) — same standard
  values Session 2.5 used

```
√(p₀(1−p₀)) = √(0.892 × 0.108) = √0.09634 = 0.3104
√(p₁(1−p₁)) = √(0.92 × 0.08)   = √0.0736  = 0.2713

numerator   = (1.96×0.3104 + 0.84×0.2713)² = (0.6084+0.2279)² = (0.8363)² = 0.6994
denominator = (0.92 − 0.892)² = (0.028)² = 0.000784

n = 0.6994 / 0.000784 ≈ 892
```

**Result: ≈ 892 graded flags** (a real race/party/venue combination that has
reached final resolution) needed for standard statistical confidence that a
92% real win rate reflects a genuine edge over an 89.2% breakeven, not
sampling noise.

## 4. Why this number is smaller than Track 1's (≈3,725), and what that means

This is a real, correct property of the math, not a sign the two tracks are
being held to different standards: variance (`p(1-p)`) shrinks as p
approaches 1, so a track whose flags cluster near-certain outcomes needs
fewer graded trials to detect the same absolute-point edge. **The
trade-off, stated plainly:** a smaller n here does not mean this track's
edge is easier to trust — it means confirming or rejecting a small edge on
already-lopsided races is a smaller statistical lift than confirming one on
a pick'em leg near a coin flip. Whether a 2.8-point edge on a 89%-favorite
race is *economically* worth flagging at all (the payout on a $0.89
contract that wins is only ≈12 cents on the dollar) is a separate, sizing-
layer question — not addressed by this document, and a real candidate for
Session 8.3's recalibration work once Session 5.4's sizing logic has real
graded data to check against.

## 5. Real, honest finding: zero graded flags exist yet

**Race resolution timescale makes "reached" a slow question by nature.**
The real committed estimates data (Section 2) shows `hours_to_resolution`
in the **thousands** (≈1,331 hours ≈ 55 days, as of the most recent real
run) — these are real down-ballot races that will not resolve for weeks or
months. No flag logged today can be graded for a real win/loss outcome
until its race actually happens. This mirrors Session 3.6's arbitrage
finding (real data takes real time to accumulate) but for a different
underlying reason (event timescale, not defect-rate accumulation).

**A second, separate finding, not yet explained:** as of this session,
`data/politics/clv_log.csv` does not exist anywhere in this repo's tracked
history, even though `politics_pipeline.yml` (Session 5.5) has run at least
5 times against real data since 2026-09-07 (per the real timestamped files
already committed under `data/politics/normalized/` and
`data/politics/estimates/`) and Session 5.5's own sandbox validation run
proved the CLV-logging stage works end-to-end (414 real newly-flagged
rows). Either the scheduled/dispatched GitHub Actions runs have not yet
reached the CLV-logging stage successfully, or something about that
environment differs from the sandbox in a way that has not yet surfaced.
**This needs a direct check of the real run logs on GitHub's Actions tab
for `politics_pipeline.yml`** before this session's sample-size checklist
item can be assessed at all — see SESSION_LOG.md's Session 5.7 entry, Open
items.

## 6. What this means practically — same recurring-review pattern

Once `clv_log.csv` exists and is accumulating real closed (resolved) flags:

- **Interim floor: 30 graded flags** (same floor used by Track 1's Section
  6 and this project's established pattern) — below this, no directional
  read is reported as meaningful.
- **Full target: ≈892 graded flags** (Section 3) — the number a recurring
  review reports progress against, not a single gate.
- Given the ~55-day-plus real resolution timescale found in Section 5, this
  track's full target is realistically a multi-election-cycle project, not
  a multi-week one. This is stated here as an honest expectation, not
  hidden inside a generic "keep collecting data" note.

## 7. Limitations — stated, not silent

- **p₀ = 0.892 is a snapshot of one real data pull**, not a stable
  population parameter — it will shift as more races are ingested and as
  competitive (closer to 50/50) races enter or leave the flagged set.
  Re-deriving it periodically (matching Track 1's own Section 6 pattern) is
  appropriate rather than treating this document's number as permanently
  fixed.
- **This track has no realized-outcome tracker yet** — `outcome_tracker.py`
  (Session 2.5) is hardcoded to `data/pickem/clv_log.csv` and PrizePicks-
  specific breakeven math (confirmed directly, same finding Session 3.6
  made for arbitrage). Building a politics-specific version is deferred
  until real resolved races exist to test it against — building it blind,
  before any race has actually resolved, would risk the same false-
  confidence problem Session 2.4's Decision #6 already named once for this
  project.
