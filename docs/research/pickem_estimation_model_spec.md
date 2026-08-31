# Pick'em Estimation Model — v1 Specification (Session 2.3)

## What this document is

This document names every input the v1 estimation model
(`scripts/estimation/pickem_model.py`) uses, exactly how each one is
calculated, and exactly what is deliberately left out of v1 and why — at the
same level of detail as the DFS_Optimizer repo's own projection
documentation, per this project's standing "no unnamed black-box factors"
rule.

## What the model does, in one paragraph

For every prop ingested by Session 2.2's pipeline (`data/pickem/normalized/
latest.csv`), the model tries to build a probability that the real stat
lands over the platform's line. It can only do this for props where (1) the
sport is NFL, (2) the stat type is one this model recognizes, and (3) the
named player can be matched to a real player in nflverse's public weekly
stats data. Every prop that fails one of those three checks still gets a
row in the output — with a `model_status` explaining which check it failed
— rather than being silently dropped.

## Inputs used (v1)

| Input | Definition | Source |
|---|---|---|
| `season_avg` | Mean of the target stat across the player's REG-season games so far this season | nflverse weekly stats |
| `recent_form` | Recency-weighted average of the player's last 5 REG-season games (weights 0.35/0.25/0.20/0.12/0.08, most recent first; renormalized if fewer than 5 games exist) | nflverse weekly stats |
| `model_mean` | 50% `season_avg` + 50% `recent_form` | Derived |
| `model_sigma` | Sample standard deviation of the player's own game log for the target stat this season | nflverse weekly stats |
| `line` | The platform's fixed prop line | Session 2.2's ingested data |
| `implied_prob_over` (Underdog) | No-vig-style normalization of the platform's own `over_payout_multiplier` / `under_payout_multiplier` — see "Implied probability" below | Session 2.2's ingested data |
| `implied_prob_over` (PrizePicks) | Flat 50% — a **stated, unverified assumption**, not a researched figure — see "Implied probability" below | Assumption |

## Why season_avg + recent_form, blended 50/50

This mirrors the DFS_Optimizer repo's own first-pass projection pattern
(`projections_baseline.py`, its Session 2.1): a season baseline plus a
recency-weighted recent-form signal, blended together. The 50/50 blend
weight is a deliberate, simple starting point — not a tuned or researched
number. Re-weighting this blend against real graded results is explicitly
deferred to Session 8.3 (Ongoing Recalibration Cadence), once Sessions
2.4/2.5 have produced real CLV and outcome data to tune against. Shipping a
falsely-precise blend weight now, before any real evidence exists to derive
one from, would violate this project's standing rule against dishonest
precision (see SESSION_LOG.md, Session 2.2, Decision #1, which established
this same principle for a different question).

## How the probability is computed

Given `model_mean` and `model_sigma` for a player/stat, and the platform's
`line`, the model assumes the stat is approximately normally distributed
around `model_mean` with standard deviation `model_sigma`, and computes:

```
prob_over = 1 - NormalCDF((line - model_mean) / model_sigma)
prob_under = 1 - prob_over
```

This is a standard, named simplification (a normal approximation), not a
sport-specific or stat-specific fitted distribution. Whether a normal
approximation is a good fit for every stat type here (e.g. receptions,
which is a low-count discrete stat, behaves less like a bell curve than
passing yards) is an open question — flagged in "What v1 does not do,"
below, rather than assumed away.

## Implied probability — how it is computed, and what it assumes

**Underdog:** Session 2.2's schema captures `over_payout_multiplier` and
`under_payout_multiplier` per prop. Treating each multiplier as a fair-odds
number (payout × true win probability = 1 at breakeven), the model computes
a no-vig-style normalized implied probability:

```
implied_prob_over = (1 / over_multiplier) / (1/over_multiplier + 1/under_multiplier)
```

This normalizes the two raw implied probabilities so they sum to 1,
consistent with how a sharp-book no-vig line is derived in traditional
sports betting — the raw `1/multiplier` on each side alone would not sum to
1 and would understate the platform's real edge.

**PrizePicks:** Session 2.2's schema does not capture a per-side multiplier
for PrizePicks (standard PrizePicks lines pay a fixed multiplier on the
whole entry, not per individual pick — see `schema.py`). In the absence of
a real per-side number, v1 assumes a flat 50% implied probability on both
sides. **This is a stated, unverified assumption**, not a confirmed
industry figure — it should not be treated as fact anywhere downstream
until it is checked against a real benchmark. This project has an explicit
standing rule against exactly this kind of unverified claim being quietly
absorbed as settled (see ROADMAP.md Open Decision #4, on the PrizePicks
win-rate demotion claim) — the same discipline applies here. Session 2.4's
CLV logging is the first place a real benchmark will exist to check this
assumption against.

## What v1 does NOT do (stated gap)

- **Sport coverage:** only NFL props are modeled. PrizePicks/Underdog carry
  props across many sports (Session 2.2's real ingested data included
  tennis and esports rows). A non-NFL row is marked
  `model_status="unsupported_sport"`. Against a real live pull of 20,861
  ingested props, 17,740 (85%) were non-NFL — this is expected and not a
  bug.
- **Stat-type coverage:** the stat types listed in
  `NFL_STAT_TYPE_MAP`/`COMPOSITE_STAT_TYPES` in `pickem_model.py` are
  modeled; everything else is marked `model_status="unsupported_stat_type"`.
  This list was built and expanded directly from a real ingested-data run
  (Session 2.3), not guessed in advance — see "Stat-type coverage, checked
  against real data" below for the full record of what was added and what
  was deliberately left out.
- **No opponent/matchup adjustment.** The model does not yet account for
  the opponent's defensive strength against the relevant stat.
- **No injury/role status.** A player listed as questionable, or who lost
  snaps to another player, is not yet reflected — `season_avg`/
  `recent_form` will include games where their role was different from
  their current one.
- **No home/away split.**
- **No pace/usage adjustment** (e.g. a team's expected play volume this
  week).
- **No weather input** for outdoor games.
- **Normal-distribution assumption not validated per stat type** — see
  "How the probability is computed," above.

Each of these is a real, named candidate for a v2 iteration once real CLV
data (Session 2.4) shows where v1's blind spots actually cost accuracy —
building them in now, before that evidence exists, would be guessing in
advance, which the roadmap card for this session explicitly avoids.

## Model status values (every output row gets exactly one)

| `model_status` | Meaning |
|---|---|
| `estimated` | A real probability was produced |
| `unsupported_sport` | Prop is not NFL |
| `unsupported_stat_type` | Prop is NFL but the stat type isn't mapped yet |
| `no_player_match` | Player name couldn't be matched to nflverse data |
| `insufficient_history` | Player matched, but has fewer than 2 qualifying games so far this season |
| `no_line_value` | Everything else resolved, but the ingested row had no usable `line` value |

## Stat-type coverage, checked against real data

Session 2.3's first real run, against 20,861 live ingested props
(`--season 2025`), returned this `model_status` breakdown before any
stat-type expansion:

```
unsupported_sport      17,740
unsupported_stat_type   1,650
estimated                1,420
no_player_match             50
no_line_value                 1
```

The player-match rate among NFL props with a mapped stat type was
1,420 / (1,420 + 50) = **96.6%** — checked directly against real data, not
assumed.

The 1,650 `unsupported_stat_type` rows were then inspected directly (their
real `stat_type` strings, with counts). Each one was checked against
nflverse's real column list before any mapping decision was made:

| Real `stat_type` string | Count | Outcome |
|---|---|---|
| `Player TDs` | 426 | Mapped — sum of `passing_tds`+`rushing_tds`+`receiving_tds` |
| `Recs` | 420 | Mapped — `receptions` (spelling variant of an already-mapped stat) |
| `Longest Rec` | 244 | **Left unsupported** — nflverse has no per-game "longest reception" column |
| `Longest Completion` | 136 | **Left unsupported** — same reason |
| `Pass+Rush Yds` | 92 | Mapped — sum of `passing_yards`+`rushing_yards` |
| `Kicking Points` | 85 | **Mapped** — real, tiered scoring formula (see "Computed stat types," below), not a column sum |
| `FG Made` | 77 | Mapped — `fg_made` |
| `Fantasy Score` | 53 | **Mapped** — real scoring formula (see "Computed stat types," below), not a column sum |
| `Longest Rush` | 36 | **Left unsupported** — no matching nflverse column |
| `INT` | 26 | Mapped — `passing_interceptions` |
| `Rec TDs` | 17 | Mapped — `receiving_tds` |
| `Rush+Rec Yds` | 14 | Mapped — spelling variant of an already-mapped composite |
| `Sacks` | 13 | Mapped — `def_sacks` (a defensive player's own recorded sacks) |
| `Rec Targets` | 8 | Mapped — `targets` |
| `Pass+Rush+Rec TDs` | 3 | Mapped — same composite as `Player TDs` |

10 of 15 real unmapped stat types (1,096 of the 1,650 rows) were mapped
from this evidence, then 2 more (`Kicking Points`, `Fantasy Score` — 138
more rows) were added in a follow-up pass once their real scoring formulas
were confirmed (see "Computed stat types," below). The remaining 3 (416
rows — the three "Longest ___" stat types) stay unsupported for a real,
named reason: the underlying per-game data does not exist in nflverse at
all. This is recorded in `pickem_model.py` directly, so a future session
doesn't have to re-run this same investigation.

A live run after adding the first 10 mappings, against a small hand-built
set of real players covering every newly-added stat type, confirmed each
one produces a plausible `estimated` result (e.g. Myles Garrett's modeled
sacks/game of ~1.03 reflects his real 2025 season; Harrison Butker's
modeled FG-made/game of ~2.38 is consistent with a real kicker's workload).
None were left to guesswork.

## Computed stat types: Kicking Points and Fantasy Score

Unlike every other mapped stat type (a straight nflverse column, or a sum
of a few columns), `Kicking Points` and `Fantasy Score` are real, weighted
scoring **formulas** — PrizePicks converts several raw stats into a single
number using its own point values per stat. Guessing at that formula would
mean presenting an assumption as a real number, so both were confirmed
directly against PrizePicks' own official sources before being coded:

- **Kicking Points** — confirmed via PrizePicks Support's own reply on X
  (`https://x.com/PrizeSupport/status/1963792635933434257`) and PrizePicks'
  own scoring page
  (`https://www.prizepicks.com/playbook-article/how-to-play-prizepicks-nfl-fantasy-scoring-system`,
  published September 17, 2025): field goals are tiered by distance, not a
  flat 3 points — 0–39 yards = 3 pts, 40–49 yards = 4 pts, 50+ yards =
  5 pts; a made PAT = 1 pt; a missed FG or missed PAT = **−1** pt each.
  PrizePicks' own page states explicitly that Kicking Points is **not**
  the same stat as Fantasy Score.
- **Fantasy Score** — confirmed via the same official PrizePicks scoring
  page: full-PPR-style scoring (0.04 pts/passing yard, 4 pts/passing TD,
  −1/interception, 0.1 pts/rushing yard, 6/rushing TD, 1 pt/reception,
  0.1 pts/receiving yard, 6/receiving TD, −1/fumble lost, 2/2-point
  conversion, plus 6 pts each for Offensive Fumble Recovery TDs and
  Kick/Punt/FG Return TDs).

Every nflverse column each formula needs was checked to exist before being
used (`fg_made_0_19` through `fg_made_60_`, `fg_missed`, `pat_made`,
`pat_missed` for Kicking Points; the full offensive stat line plus
per-category lost-fumble and 2-point-conversion columns for Fantasy Score).

**One real, stated gap:** the implemented Fantasy Score formula omits the
two 6-point return-TD/fumble-recovery-TD components. This is not a
shortcut — nflverse's closest-named column for return touchdowns,
`pt_return_tds`, was checked directly against real 2025 data and found to
fire on **punters**, not the players who actually returned a kick (e.g.
real punters Bryce Baringer, AJ Cole, and Thomas Morstead all show a
nonzero `pt_return_tds` value with zero recorded returns) — it does not
measure what its name suggests, and using it would produce a wrong number
with false confidence. Rather than guess at an alternative, this component
is left out and documented here. Both omitted events are rare (well under
1% of player-games across a full season), so the practical accuracy impact
is small, but it is a real, named limitation, not a hidden one.

**Verification performed before handoff:** both formulas were independently
recomputed by hand, directly from raw nflverse data, outside the model's
own code, and cross-checked against the model's real output for real
players (Harrison Butker for Kicking Points, Patrick Mahomes for Fantasy
Score). The model's `model_mean` for Butker (9.72) was confirmed to equal
exactly the documented 50/50 blend of his hand-computed season average
(8.29) and hand-computed recency-weighted recent form (11.15) — proving
the formula is correctly wired into the rest of the pipeline, not just
producing a plausible-looking number that happens not to crash.

## Deferred: folding in real 2026 season data

As of this session (2026-08-31), nflverse's `stats_player_week_2026.parquet`
release does not exist yet — checked directly, returns 404. This is
expected: nflverse only publishes a season's file once real games from
that season have been played, and the 2026 NFL season's first games are
2026-09-07. Until then, this model is deliberately run with
`--season 2025`, so `season_avg`/`recent_form` reflect real, complete
2025 performance rather than nothing at all.

**Agreed, deferred to a future session:** once 2026 games start being
played, this model should begin folding in real 2026 data — either by
switching to `--season 2026` once enough 2026 games exist to be
meaningful, or by blending 2025 and early-2026 data during the transition
period when 2026 has only a few games logged (a blended approach avoids
the model swinging on a tiny early-2026 sample). Which approach, and
exactly when to switch, is intentionally left open rather than decided in
advance — no evidence yet exists to make that call correctly. Flagging
this here so it isn't lost, per this project's standing convention that a
deferred item is stated explicitly, not silently dropped.

## Known operational risk: early-season data sparsity

Nflverse's weekly-stats release for the current season only contains games
that have already been played. Early in a season, most players will not yet
have `MIN_GAMES_FOR_ESTIMATE` (2) games logged, and will fall into
`insufficient_history`. This is expected behavior, not a bug — it should be
visible in the `model_status` breakdown printed at the end of each run, not
hidden.

## Player-name matching

PrizePicks/Underdog player names and nflverse player names are matched via
a normalized form (lowercased, punctuation stripped, common suffixes
Jr/Sr/II/III/IV/V removed). This is an exact match on the normalized string,
not a fuzzy/similarity match — a real mismatch (e.g. a nickname the
platform uses that nflverse doesn't) will show up as `no_player_match`
rather than being silently and possibly incorrectly matched to the wrong
player. The real match rate should be checked against actual ingested data
as part of closing this session (see handoff notes / remaining validation
items).

**Real bug found and fixed before handoff:** nflverse's weekly-stats
release has two different name columns — `player_name` (an abbreviated
form, e.g. `"P.Mahomes"`) and `player_display_name` (the full form, e.g.
`"Patrick Mahomes"`). This was checked directly against a live pull of the
2025 release before this script was handed off, not assumed. The model
matches on `player_display_name`, since that is the form PrizePicks and
Underdog both actually use in Session 2.2's ingested data. Matching on
`player_name` instead would have silently produced a `no_player_match`
result for nearly every real row — the kind of gap that would look like a
working pipeline (no crash, no error) while quietly modeling almost
nothing. Recorded here as a real, concrete example of why every field this
model reads is checked against a live pull first, not assumed from a
sibling project's code.
