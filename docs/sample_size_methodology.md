# Sample-Size Methodology — Track 1 (Fixed-Line Pick'em Platforms)

**Session:** 2.5 — Sample-Size Thresholds & Realized-Outcome Tracking
**Status:** Draft for review — becomes final once Session 2.5 closes.

## What this document answers

Every later go/no-go checkpoint in this project (Sessions 2.9, 3.6, 4.7, 5.7,
6.7, and Phase 7.0) depends on one question: **how many graded results does
this track need before its performance is treated as meaningful, instead of
noise?** This document derives that number for Track 1, using real data from
Sessions 2.1–2.4 and a standard statistical method — not an arbitrarily chosen
calendar length or entry count.

This document does **not** set a threshold for "how many flags should we log"
(Session 2.4 already produced that — 3,205 flags in ~17 hours; logging volume
is not the bottleneck). It sets a threshold for **graded outcomes**: bets the
user actually placed and reported through the outcome tracker (this session),
where the real result (won/lost) is now known.

---

## 1. Why a win-rate test, not a CLV test

Session 2.4 built two pre-outcome benchmarks (cross-platform consensus,
own-line movement to close). Those are proxies — real signal, but not the
real thing. The real thing is: **did the flagged picks actually win more
often than they needed to, to be worth making?** That is a win-rate
question with a known statistical answer, so this document uses a standard
one-sample proportion test (comparing the track's real win rate against its
real breakeven win rate), the same category of test used throughout sports
betting and DFS performance evaluation.

> **Correction, Session 2.57 (read this before Sections 2-5).** Two inputs
> below were wrong, and the 3,725 figure was re-checked on real data with
> `scripts/calibration/report_sample_size_check.py`.
>
> 1. **Payout.** PrizePicks does not pay 3x for a 2-pick. Measured in the
>    user's app: all-Standard 2/3/4/5/6-pick = 2 / 4.75 / 9 / 19 / 36.5x, so
>    the per-leg breakeven is 0.7071 / 0.5949 / 0.5774 / 0.5549 / 0.5491.
>    (0.5774 is now the 4-pick number, by coincidence.)
> 2. **Reference entry.** At a true leg win rate near 0.60, the entry size
>    with the best bankroll growth (Kelly log-growth, equal independent legs)
>    is 6-pick (0.577% per entry vs 0.556% for 5-pick); 5-pick wins from
>    about 0.62 up. A 3-pick barely grows at 0.60 (0.009%) and a 2-pick never
>    does. Code now uses the **5-pick, 0.5549**: almost as good as the 6-pick
>    and it wins about 7.8% of entries, not 4.7%.
> 3. **Independence.** Legs from one game are correlated. Measured design
>    effect (real variance / independent-leg variance) for PrizePicks
>    Standard: **3.49** (171 games, 32.8 legs per game, game-clustered).
>    5,603 graded legs carry the information of about 1,600 independent legs.
> 4. **Re-derived threshold.** Detect a true 60% against 0.5549 (5% false
>    positive, 80% power): 946 independent legs x 3.49 = **about 3,300
>    real legs, about 100 games**. The 3,725 figure was derived the wrong
>    way (wrong hurdle, independence assumed) but lands within 13% of this,
>    so it is **kept**. Read it as real, game-clustered legs. Count games,
>    not only legs: adding legs from games already counted adds little.
>    A 6-pick reference needs about 2,600 legs (79 games); a 3-pick reference
>    cannot test a 60% target at all (it needs about 250,000 legs).
> 5. **Pooled numbers hide big differences.** On real graded legs (game-
>    clustered 95% interval): MLB 51.9% [49.7, 54.0] is below even the 6-pick
>    hurdle; NFL 69.1% [65.9, 72.4] is above it but rests on only 16 games;
>    unders 62.5% [59.1, 65.8] are above, overs 52.2% [49.2, 55.1] are below
>    the 5-pick hurdle. The pooled 56.2% [53.8, 58.6] is inconclusive. Judge
>    by sport and side, not only pooled.
>
> The original text below is kept as written for history.

## 2. The real breakeven win rate — sourced, not assumed

Track 1's estimation model (Session 2.3) flags individual over/under legs.
Those legs get combined by the user into an entry (2–6 picks) on PrizePicks
or Underdog. The breakeven win rate depends on the entry's real payout
structure, which is public and fixed.

**Used here: PrizePicks' standard 2-pick Power Play.** A Power Play requires
every leg in the entry to hit; PrizePicks' own published standard payout for
a 2-pick Power Play is **3x** the entry amount (source: PrizePicks' own
payout page and third-party payout-calculator sites cross-referencing it,
current as of mid-2026). For a 2-leg, all-or-nothing entry to break even
over many entries, the **per-leg win probability (p)** must satisfy:

```
p² × 3x = 1x     (entry must return, on average, at least what was staked)
p² = 1/3
p = √(1/3) ≈ 0.5774
```

**Real breakeven per-leg win rate: ≈ 57.7%.** This is the number Track 1's
flagged legs must beat, on average, over a real sample, for a 2-pick Power
Play strategy to be worth playing. This is intentionally the standard,
most-commonly-played entry size (per the payout research: 2-pick and 3-pick
Power Plays are the most commonly recommended entry type for exactly this
reason — highest per-leg breakeven tolerance of any entry size). Larger
entries (4-, 5-, 6-pick) and Flex Play have different, generally *higher*
breakeven requirements per leg, and are treated as a stated, separate case —
see Section 5 (Limitations).

## 3. Sample-size formula

Standard one-sample test of a proportion against a fixed benchmark, using a
normal approximation (the same method underlying most sports-betting
"how many bets do I need to know if I'm actually winning" calculators):

```
n = [ z_(α/2) × √(p₀(1−p₀))  +  z_β × √(p₁(1−p₁)) ]²  /  (p₁ − p₀)²
```

Where:
- **p₀** = real breakeven win rate = 0.5774 (Section 2)
- **p₁** = the true win rate this track needs to demonstrate to be worth
  running — set at **0.60** (a 2.3-percentage-point real edge over
  breakeven; see Section 4 for why this number, not a bigger or smaller one)
- **α = 0.05** (standard 5% false-positive tolerance — z = 1.96)
- **power = 0.80** (standard 80% chance of correctly detecting a real edge
  if one exists — z = 0.84)

```
√(p₀(1−p₀)) = √(0.5774 × 0.4226) = √0.2440 = 0.4940
√(p₁(1−p₁)) = √(0.60 × 0.40)     = √0.2400 = 0.4899

numerator   = (1.96 × 0.4940 + 0.84 × 0.4899)² = (0.9682 + 0.4115)² = (1.3797)² = 1.9036
denominator = (0.60 − 0.5774)² = (0.0226)² = 0.000511

n = 1.9036 / 0.000511 ≈ 3,725
```

**Result: ≈ 3,725 graded individual legs** needed to say, with standard
statistical confidence, that a true 60% win rate is real and not a lucky
run at the 57.7% breakeven line.

## 4. Why p₁ = 0.60, not a bigger or smaller number

This is a real judgment call, stated explicitly rather than hidden in the
formula. 0.60 was chosen because:
- It represents a real, discernible edge (2.3 points above breakeven) — not
  so small that the project would need tens of thousands of graded legs
  before Session 2.9 could ever close (a threshold like p₁ = 0.585 pushes
  n into the tens of thousands — impractical for a v1 track to reach in a
  reasonable number of sessions).
- It is not so large that it sets an unrealistically easy bar — Session
  2.3's own model has no opponent/injury/pace adjustments yet (a named, v1
  gap), so demanding a large edge from a deliberately simple model would be
  demanding more than v1 was built to deliver.
- **This is a placeholder in the same sense Session 2.4's `FLAG_EDGE_THRESHOLD
  = 0.03` was a placeholder** — a reasoned starting point, not a proven
  number. Revisiting it against real graded results is Session 8.3's job
  (Ongoing Recalibration Cadence), same as the flag threshold.

## 5. Limitations — stated, not silent

- **This n (≈3,725) is per-leg, not per-entry.** A single 2-pick entry
  produces 2 graded legs once it resolves. At that rate, ≈3,725 graded legs
  requires roughly 1,860 real 2-pick entries placed and reported — a real,
  large number, stated plainly rather than glossed over. Section 6 discusses
  what this means in practice.
- **This threshold assumes every graded leg is independent.** In practice,
  two legs from the same 2-pick entry share the same bet-sizing decision
  (the user chose to play them together), which is a reasonable
  approximation for a win-rate test on individual legs, but not a perfect
  one. Noted here as a real simplification, not corrected in this session.
- **Different entry sizes and Flex Play have different real breakeven
  rates**, not calculated here. If the user's real usage pattern shifts
  toward 3-pick, 4-pick, or Flex entries, this document's p₀ = 0.5774 no
  longer applies cleanly, and the threshold should be recalculated using
  that entry type's real published multiplier. Flagged here as a gap for a
  future session (or an update to this document) once real usage data
  exists.
- **This is Track 1's own threshold, not a universal one.** Cross-venue
  arbitrage (Phase 3), weather markets (Phase 4), and the other tracks each
  need this same exercise repeated with their own real breakeven math
  (arbitrage has no win-rate concept at all — it needs a different
  methodology entirely, deferred to Session 3.6's own card).

## 6. What this means practically — recurring review, not a single gate

**Decision, made directly with the user during this session:** ≈3,725
graded legs is a large number relative to what one person can place and
report by hand in a short window — treating it as a single gate (nothing
reviewed or acted on until the full number is reached) would leave the
project with no real feedback loop for a very long time. Instead, this
project adopts a **recurring weekly review**, run indefinitely, not a
one-time checkpoint:

- **Interim floor: 30 graded legs.** Below this, even a directional read
  isn't reported as meaningful — this mirrors Session 2.4's own "15+ flags"
  minimum-before-reporting-anything standard, applied here to graded
  outcomes instead of raw flags.
- **Above 30 graded legs, every weekly review reports a real number**,
  always shown next to two fixed reference points: the 57.7% breakeven
  (Section 2) and progress toward the 3,725 full-strength threshold
  (Section 3) — so a "provisional, still building sample" read is never
  visually indistinguishable from a "statistically solid" one.
- **Every review is also a recalibration checkpoint.** Session 2.3's model
  weights (currently a flat 50/50 blend) and Session 2.4's flag threshold
  (currently 0.03) get re-examined against the newly graded data at every
  review, not just once at some distant future date. This is what makes the
  system "get more accurate over time," per the user's explicit design
  goal for this session, rather than only ever grading itself.
- **This pulls part of Session 8.3's job forward.** Session 8.3 ("Ongoing
  Recalibration Cadence") was originally scoped to wait for Phase 8 (2+
  live tracks), since a *cross-track* cadence needs multiple tracks to be
  meaningful. A *single-track* weekly review has no such dependency — it
  can and should start as soon as real graded data exists. This is a real,
  named correction to the roadmap's sequencing, not a silent scope change;
  recorded as a Decision when this session closes, and noted on Session
  8.3's own card that its cross-track version builds on top of this
  single-track review, not from a blank start.
- **The review does not auto-apply anything.** It produces a
  recommendation (e.g. "high-edge flags are not outperforming low-edge
  flags — threshold may need raising" or "the model is running
  over-confident by N points — blend weights may need adjusting"). A person
  decides whether to act on it, consistent with this project's standing
  "flags and sizes, does not place bets" design principle (ROADMAP.md,
  Background & Approach) applied to model changes as well as bet
  placement.

**Deferred, not built this session:** grading a broader pool of
flagged-but-not-personally-bet legs against public final stat results
(auto-grading from nflverse, the same free source Session 2.3 already uses)
would reach a large sample much faster than real placed bets alone, since
Session 2.4 already produces thousands of flags per day. This tests the
*model's* accuracy rather than the user's real-money results — a related
but distinct question. Named here as a real, concrete candidate for a
future session, not built now.

## 7. Realized-outcome tracking — how it links to Session 2.4's CLV log

Every graded leg recorded by `outcome_tracker.py` (this session) links back
to exactly one row in `data/pickem/clv_log.csv` (Session 2.4) via that row's
`flag_id`. This keeps the two logs genuinely separate — CLV log is the
pre-outcome proxy, outcome log is the real, resolved result — while making
them joinable on a shared key. See `outcome_tracker.py`'s own docstring for
the full schema and the worked join example.

---
*This document is a draft output of Session 2.5, not yet a closed session.
It should not be treated as final until the session closes per ROADMAP.md's
standing convention (both CLV and outcome logs need at least one real
end-to-end trial before this session can close — see chat for the current
open items).*
