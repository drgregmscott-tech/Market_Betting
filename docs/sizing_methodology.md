# Bankroll & Sizing Methodology — Track 1 (Fixed-Line Pick'em Platforms)

**Session:** 2.6 — Bankroll & Sizing Logic
**Prerequisite:** Session 2.5 (`sample_size_methodology.md`) — this document
uses that session's sourced 2-pick Power Play payout number directly.

## What this document answers

Session 2.3's model produces a probability. Session 2.4's logger flags an
opportunity when that probability clears an edge threshold. Neither one
says how much money to actually risk. This document explains, step by
step, how `sizing_engine.py` turns two flagged legs into one suggested
dollar stake — and states plainly which numbers in that chain are sourced
facts and which are this project's own judgment calls.

## 1. Scope — why only the 2-pick PrizePicks Power Play

A pick'em "entry" is not one leg — it's a group of legs (2 to 6, depending
on the platform and entry type) that all have to hit together for a
Power Play, or that pay out on a sliding scale for a Flex Play. Sizing real
money against an entry requires knowing that entry's real payout
multiplier. Session 2.5 sourced exactly one such number directly from
PrizePicks' own published payout page: a 2-pick Power Play pays **3x** the
stake if both legs hit. No other entry size, and no Underdog entry type,
has a confirmed real multiplier anywhere in this project's research yet.

Rather than assume a multiplier for an unresearched entry type — which
would mean sizing real money off an invented number — `sizing_engine.py`
v1 only accepts exactly two open PrizePicks legs, sized as a 2-pick Power
Play. Every other combination (wrong leg count, any Underdog leg, a mix of
platforms) is rejected outright, with the specific reason stated in the
output. This mirrors Session 2.3's own NFL-only scoping decision: a named,
stated boundary, not a silent one.

**What this means in practice:** if you have three or more real open flags
you'd like to combine, or want to size an Underdog entry, this version of
the tool will not do it — not because the underlying math couldn't be
extended, but because the real payout number it would need doesn't exist
yet in this project's research. Extending coverage to more entry types is
a named candidate for a future session, not a gap this session tried to
paper over.

## 2. The sizing formula — Kelly criterion

For an all-or-nothing bet with win probability `p` and net odds `b` (the
profit on a $1 stake if the bet wins), the Kelly criterion gives the
bankroll fraction that maximizes long-run growth:

```
f* = (p × (b + 1) − 1) / b
```

For a 2-pick Power Play, `b = 2` (a $1 stake returns $3 total — $2 of
profit — on a win). `p` is the entry's **combined** win probability: the
two legs' individual model probabilities multiplied together, since both
legs must hit. This treats the two legs as independent events. That's a
real simplification — two legs from the *same* real game (e.g. a
quarterback's passing yards and his own team's leading receiver's
receiving yards) are not fully independent in reality — and is stated here
as a known limitation, not fixed in v1.

**Worked example:** two legs, each with a model probability of 0.70.
Combined `p = 0.70 × 0.70 = 0.49`. With `b = 2`:

```
f* = (0.49 × 3 − 1) / 2 = (1.47 − 1) / 2 = 0.235
```

Full Kelly here says stake 23.5% of bankroll on this one entry — a real
number, but far too aggressive to actually bet, given how much uncertainty
sits behind that 0.70 probability estimate. That's what the next two steps
are for.

## 3. Why full Kelly is never staked directly — quarter-Kelly

`sizing_engine.py` applies `KELLY_FRACTION = 0.25` to the raw Kelly number
above. This is standard, widely-used practice specifically when the win
probability itself carries real estimation uncertainty — full Kelly
assumes the probability input is exactly correct, which this project's own
model does not claim to be (Session 2.3's model has no opponent, injury,
pace, or matchup adjustment yet; Session 2.4's edge threshold is itself an
explicitly unvalidated placeholder). Quarter-Kelly trades some long-run
growth for a much smaller chance of a large drawdown from an overconfident
probability estimate.

**This is a placeholder, not a derived number** — in the same sense
Session 2.4's `FLAG_EDGE_THRESHOLD = 0.03` and Session 2.5's `p1 = 0.60`
target win rate were both stated placeholders rather than proven figures.
Re-tuning `KELLY_FRACTION` against real graded outcomes is Session 8.3's
job (Ongoing Recalibration Cadence), once enough real results exist to
check it against.

Continuing the worked example: `0.235 × 0.25 = 0.0588` — about 5.9% of
bankroll, before the next two adjustments.

## 4. Platform risk adjustment — why PrizePicks gets an extra dampener

The Session 1.1 continuation research
(`docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md`)
found real, first-hand evidence (BBB, Trustpilot) of PrizePicks accounts
being closed or having withdrawals withheld in a pattern users describe as
win-triggered — while noting the specific "55% win rate over 200 entries"
threshold claim could not be independently corroborated and is **not**
used as a hard number anywhere in this project.

Kelly's formula has no concept of "the platform might not let you collect
your winnings." A real edge that can't actually be realized isn't worth
what the raw math says it's worth. `sizing_engine.py` applies
`PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70` on top of quarter-Kelly to
account for this — a further, stated judgment call, not sourced to a
specific number (no source gives one). Continuing the example:
`0.0588 × 0.70 = 0.0412` — about 4.1% of a hypothetical bankroll.

An Underdog multiplier (`0.85`, reflecting the research's finding that
Underdog is reputationally more winner-tolerant, though not independently
verified) is present in the code for future use but is not currently
reachable — v1's entry-type gate (Section 1) rejects any Underdog leg
before this adjustment would ever apply.

## 4.5. Same-game caution — flagging a modeling gap, not fixing it

The Kelly formula above assumes the two legs are independent. When both
legs come from the **same real game**, that assumption weakens — a
blowout, an overtime, or an injury can move several players' stats
together at once. This project has no real data on how strongly, or in
which direction, same-game pairs actually move together for different
stat combinations, and manufacturing a "corrected" probability without
that data would mean sizing real money off a guess.

**Decision (discussed directly with the user during this session):**
rather than leave this silently unaddressed, `sizing_engine.py` treats it
as something to flag as riskier, not something to precisely model.
Whenever both requested legs share the same real `game_id`,
`SAME_GAME_CAUTION_MULTIPLIER = 0.85` is applied on top of every other
adjustment, and the output reports `same_game_pair: True` so it's always
visible when it happens — never a silent adjustment. This mirrors the
Kelly fraction and PrizePicks dampener: a stated, direction-agnostic
placeholder, not a derived number, and a real candidate for replacement
once actual same-game correlation data exists to check it against.

**Worked example, using two real flags pulled from the live `clv_log.csv`
during this session's validation** (Drake Maye Pass+Rush Yards under 374.5,
model probability 0.9765; Sam Darnold Pass Yards under 358.5, model
probability 0.9825 — both tied to the same real game_id):

| | Without same-game flag | With same-game flag |
|---|---|---|
| Dampened Kelly fraction | 0.1643 | 0.1397 |
| Uncapped stake ($500 bankroll) | $82.17 | $69.84 |
| Suggested stake | $25.00 (capped) | $25.00 (capped) — cap still binds either way in this high-edge example |

For a smaller-edge real pair (same session, Drake Maye's two different
Pass+Rush Yards lines, both tied to the same game): the uncapped stake
moved from $15.15 to $12.88 once the same-game flag applied — a real,
visible reduction in a case where the cap did not otherwise bind.

## 5. The bankroll cap — a hard ceiling, not just a description

Regardless of what the dampened Kelly fraction computes to,
`sizing_engine.py` never suggests a stake above
`MAX_SINGLE_POSITION_PCT = 5%` of the bankroll figure supplied on that
run. This is enforced directly in code (`size_entry()`, the `capped`
check), not left as a documentation-only rule — a status of
`sized_capped_at_max_position` is returned whenever this ceiling is what
actually limited the suggested stake, so it's visible in the output when
it happens, not silently applied.

## 6. Manual sanity checks (see `test_sizing_engine.py` for the full,
   automated versions of these)

| Combined probability (p) | Raw Kelly (f*) | After quarter-Kelly + 0.70 dampener | Suggested stake ($1,000 bankroll) |
|---|---|---|---|
| 0.60 × 0.60 = 0.36 (below breakeven) | −0.02 (negative) | n/a | **$0 — `no_bet_negative_edge`** |
| 0.68 × 0.66 = 0.449 | 0.173 | 0.030 | **$30.30** |
| 0.70 × 0.70 = 0.49 | 0.235 | 0.041 | **$41.13** |
| 0.75 × 0.75 = 0.5625 | 0.344 | 0.060 | **$50.00 — capped** (5% ceiling) |

Bigger edge → bigger suggested stake, up to the hard cap; a combined
probability at or below the 57.7% breakeven never produces a positive
stake. Both properties are also proven directly in
`test_sizing_engine.py` (tests 1–3), run against synthetic data since this
sandbox cannot reach the real `clv_log.csv`.

## 7. What this does NOT do yet (stated gap, not silent)

- No entry type other than the 2-pick PrizePicks Power Play is sized
  (Section 1).
- Same-game legs are **flagged and given a caution dampener** (Section
  4.5), not precisely modeled — the true strength and direction of
  same-game correlation, per stat pair, remains unknown and unmodeled.
- No running bankroll tracking across multiple suggested entries over
  time — each run is a single, independent suggestion against whatever
  bankroll figure is supplied that run.
- `KELLY_FRACTION`, `PLATFORM_RISK_MULTIPLIER`, and
  `SAME_GAME_CAUTION_MULTIPLIER` are all stated placeholders, not derived
  from real graded results — re-deriving them is Session 8.3's job, once
  enough real outcome data exists (Session 2.5's `outcome_tracker.py` /
  `weekly_review.py`) to check same-game vs. cross-game entries against
  their real win rates specifically.
