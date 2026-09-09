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

---

# Addendum — Track 4 (Down-Ballot Politics) Sizing

**Session:** 5.4 — Sizing Adaptation
**Prerequisite:** Session 5.3 (`clv_logger.py --track politics`) — this
addendum sizes flags directly out of `data/politics/clv_log.csv`.

## 8. Why politics needs a third sizing shape

Sections 1–7 above size a **multi-leg pick'em parlay** (Session 2.6) and
the arbitrage addendum sizes a **locked, guaranteed-profit pair** (Session
3.3). A flagged politics position is neither: it is a single, genuinely
probabilistic contract (buy YES on one candidate at one venue) — closer to
arbitrage's single-leg mechanics than to a parlay, but a real bet with a
win/loss outcome like pick'em, so Kelly applies directly, unlike
arbitrage.

`size_politics_position()` uses the standard binary-contract Kelly
formula, expressed directly in terms of the contract's own price:

```
b = (1 - price) / price
f* = (p × (b + 1) − 1) / b
```

where `price` is the flagged side's market price (0–1) and `p` is the
model's own probability for that side (`first_flagged_model_prob`, logged
by Session 5.3). The same `KELLY_FRACTION = 0.25` used everywhere else in
this project is applied on top — no new fraction was invented for this
track.

## 9. Capital-lockup dampener — why this track needs one and pick'em/arbitrage don't

A down-ballot political contract can sit open for **weeks or months**
(Session 5.1's real ingested race data runs to the 2026 general election —
still roughly two months out as of this session), unlike a pick'em entry
(resolves same day) or a typical arbitrage position. A dollar tied up for
months carries more opportunity cost, and more can go wrong before
resolution, than a dollar tied up for hours — nothing upstream of this
session accounted for that.

`POLITICS_LOCKUP_DAMPENER_TABLE`, keyed on Session 5.3's own
`hours_to_resolution` field, applies a stated, conservative step function:

| Time to resolution | Dampener |
|---|---|
| < 30 days | 1.00 (no extra dampening) |
| 30–90 days | 0.85 |
| 90–180 days | 0.70 |
| 180+ days | 0.55 |

**This is a named judgment call, not a sourced or derived number** — same
posture as `SAME_GAME_CAUTION_MULTIPLIER` (Section 4.5 above) and
`EXECUTION_RISK_BUFFER` (arbitrage addendum). No source gives a precise
dollar figure for how much a specific number of months of lockup should
discount a position; a conservative, monotonically-decreasing step
function is used instead of inventing one. Re-deriving it against real
graded political positions is Session 8.3's job, and per Session 5.2's own
stated constraint, cannot happen until real down-ballot contracts start
resolving after the 2026 general election.

## 10. A second cap — portfolio-level exposure, not just single-position

Because positions resolve slowly, a real user placing several flagged
politics bets over a few weeks will likely have **many open at the same
time** — unlike pick'em (one entry settles before the next is placed) or
arbitrage (Session 3.3's own per-venue ledger already guards this). A
single-position cap alone cannot see that ten simultaneously-open
long-dated positions collectively lock up far more of a bankroll than any
one position looks risky on its own.

`data/politics/open_positions.csv` is a new ledger (same append/settle
pattern as Session 3.3's arbitrage ledger) that `size_politics_position()`
checks on every run:

- `POLITICS_MAX_SINGLE_POSITION_PCT = 5%` — same per-position ceiling
  posture as every other track, checked against the venue's own bankroll.
- `POLITICS_MAX_TOTAL_EXPOSURE_PCT = 25%` — **new**, checked against the
  user's total combined bankroll and the sum of every currently-open
  politics position across every venue, regardless of which venue each one
  sits at (see the code's `committed_capital_politics(venue=None)`). Both
  caps are stated placeholders, not derived numbers.

## 11. Worked example (synthetic — no real politics CLV log exists in this
sandbox; see `test_sizing_engine.py` for the full, automated versions of
these)

| Scenario | hours_to_resolution | Dampener | Suggested stake ($1,000 venue bankroll) |
|---|---|---|---|
| p=0.57, price=0.50, 10 days out | 240 | 1.00 | $35.00 |
| Same edge, 200 days out | 4,800 | 0.55 | $19.25 |
| p=0.40, price=0.50 (below breakeven) | any | n/a | **$0 — `no_bet_negative_edge`** |
| p=0.97, price=0.30 (extreme edge) | 120 | 1.00 | **$50.00 — capped** (5% single-position ceiling) |
| Portfolio already at $245 of $250 total-exposure room | 120 | 1.00 | **$5.00 — capped** (portfolio exposure ceiling, not the single-position one) |

Longer lockup → smaller stake for the identical edge; a combined
probability at or below breakeven never produces a positive stake; either
cap can bind, and the output's `binding_constraint` field always says
which one, never leaving it ambiguous.

## 12. What this addendum does NOT do yet (stated gap, not silent)

- Does not model real opportunity-cost dollar figures (e.g. an actual
  annualized-return comparison) — the dampener table is a conservative
  step function, not a derived rate.
- Does not release capital gradually as a position's resolution date gets
  closer over time — each open position's committed capital is treated as
  fully locked at its originally recorded amount until settled (same
  simplification the arbitrage ledger already makes).
- Does not re-derive the dampener table or either cap percentage from real
  graded results — Session 8.3's job, blocked on real resolved down-ballot
  contracts existing (post-2026-general-election, per Session 5.2).

---

# ADDENDUM — SESSION 6.4: SPORTSBOOK PLAYER PROPS (DK/FD) SIZING

## 13. Why this track's own dampener, not a reused one

Session 6.3's `clv_logger.py --track props` flags a single flagged side
with a single flag-time model probability and market-implied price — the
exact same shape politics' single-contract Kelly math (Section 8 above)
already handles, so `raw_kelly_fraction_binary_contract` is reused
directly, unchanged. What this session actually adds is a dampener no
other track has needed: sportsbooks limiting or banning consistently-
winning bettors is the single most widely documented account-restriction
pattern in the entire sports-betting industry — more so than either
pick'em platform (Section 3's `PLATFORM_RISK_MULTIPLIER`, sourced to
ToS-power-plus-scattered-first-hand-reports research) or an exchange
(which structurally cannot limit a winner the way a bookmaker can). No
project research doc quantifies DK/FD's real limiting rate specifically
(`docs/research/sport_inventory.md` names this as a real, open gap), so
`PROPS_PLATFORM_RISK_MULTIPLIER = {"draftkings": 0.50, "fanduel": 0.50}`
is a named, stated judgment call — set more conservative than pick'em's
0.70 specifically because this venue type's limiting reputation is the
best-corroborated of the three, not because a specific DK/FD figure was
found. Both platforms get the same figure because nothing in this
project's research distinguishes them.

## 14. A second, distinct dampener: field-vig-unresolved caution

Session 6.4 also fixed DK's TD-scorer field-vig problem in
`sportsbook_props_model.py` (grouping same-market selections by their
real `source_market_id` and normalizing the whole group's implied
probabilities to sum to 1.0) — but the fix only reaches a row whose real
same-market group had 2+ real selections captured this run. A row
captured alone still reports the raw, vig-included price with
`implied_prob_includes_field_vig=True`. Sizing that row as if its edge
were already trustworthy would risk staking real money against a number
that may still include real field vig, so `size_props_position()` applies
a second, independent dampener — `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER =
0.60` — only when that flag is `True`. Both dampeners are always reported
separately in the output (never blended into one unlabeled number), so
it's always visible which one, or both, reduced a given suggested stake.

## 15. Why no portfolio-level exposure ledger, unlike politics

Politics needed a second, portfolio-level cap (Section 9 above) because
down-ballot positions can stay open for weeks or months, so many can
realistically be open at once. A sportsbook player prop resolves same-day
or same-week (the underlying game), the same fast-resolving shape as
pick'em — so v1 judges a single-position cap
(`PROPS_MAX_SINGLE_POSITION_PCT = 0.05`) sufficient, without building a
second ledger this track's own resolution speed doesn't need.

## 16. What this addendum does NOT do yet (stated gap, not silent)

- Does not distinguish DraftKings' real limiting practice from FanDuel's
  — both get the same `PROPS_PLATFORM_RISK_MULTIPLIER`, since no source in
  this project's research separates them.
- Does not track a portfolio-level open-positions ledger (see Section 15).
- Does not re-derive `PROPS_PLATFORM_RISK_MULTIPLIER` or
  `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` from real graded results —
  Session 8.3's job, once real graded props positions exist.
