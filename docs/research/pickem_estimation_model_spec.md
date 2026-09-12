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

## Session 2.12 addendum — multi-sport plug-in architecture

Everything above this line describes the NFL-specific logic as it stood at
Session 2.3 — still accurate for NFL, but as of Session 2.12 it lives in
`scripts/estimation/pickem_sport_plugins/nfl.py`, not directly in
`pickem_model.py`. `pickem_model.py` now holds only the sport-agnostic
scoring math (season-avg/recent-form blend, sample sigma, normal-CDF
probability) plus a generic `process_props()` loop that dispatches to
whichever `SportPlugin` matches a prop's `sport` field (see
`pickem_sport_plugins/__init__.py` for the plug-in contract). This was a
pure refactor — NFL scoring output is proven byte-for-byte unchanged via
`scripts/estimation/test_pickem_model.py`'s regression fixture, not just
re-described here. Every input/gap named above (NFL-only stat coverage,
the two named PrizePicks formulas, the player-name-matching approach) is
still exactly correct; only its file location changed. Future sports
(Sessions 2.13+, starting with MLB) get their own plug-in file under
`pickem_sport_plugins/`, each with its own spec-doc section following this
same "no unnamed black-box factors" standard, rather than being folded into
this NFL-specific document.

## Session 2.13 — MLB stat-type coverage, checked against real data

Session 2.12 shipped `pickem_sport_plugins/mlb.py` as a proof case with real
fetch code but a small, explicitly UNVERIFIED stat map. This session did the
real verification `mlb.py`'s own docstring said Session 2.13 owed: a live
production ingestion pull (`scripts/ingestion/ingest_pickem.py`,
2026-09-11) returned 57,628 real rows, 11,142 of them real MLB props (plus a
separate 1,428-row `MLBLIVE` category — see below). Every real MLB
`stat_type` string was counted before any mapping decision was made, then
each one was checked directly against a real, live MLB Stats API response
(Aaron Judge's — person id 592450 — real hitting game log; Gerrit Cole's —
person id 543037 — real pitching game log) before being added.

| Real `stat_type` string (platform) | Count | Outcome |
|---|---|---|
| `Hits+Runs+RBIs` (PP) / `Hits + Runs + RBIs` (UD) | 1,436 / 253 | Mapped — composite, sum of `hits`+`runs`+`rbi` |
| `TB` (PP) / `Total Bases` (UD) | 1,329 / 252 | Mapped — `totalBases` |
| `Hitter FS` (PP) | 739 | **Mapped** — real PrizePicks formula (see below) |
| `Hits` | 719 / 250 | Mapped — `hits` |
| `Hitter Ks` (PP) / `Batter Strikeouts` (UD) | 617 / 71 | Mapped — `strikeOuts` (hitting group) |
| `RBIs` | 541 / 253 | Mapped — `rbi` |
| `Runs` | 524 / 251 | Mapped — `runs` |
| `Singles` (PP) | 366 | **Mapped** — computed, `hits − doubles − triples − homeRuns` (no direct column) |
| `Home Runs` | 273 / 251 | Mapped — `homeRuns` |
| `Doubles` | 270 / 71 | Mapped — `doubles` |
| `Walks` (PP) / `Batter Walks` (UD) | 268 / 227 | Mapped — `baseOnBalls` (hitting group) |
| `SB` (PP) / `Stolen Bases` (UD) | 219 / 119 | Mapped — `stolenBases` |
| `Ks` (PP) / `Strikeouts` (UD) | 200 / 28 | Mapped — `p_strikeOuts` (pitching group — confirmed pitcher-side by matching real row counts against other same-batch pitcher stats) |
| `Hits Allowed` | 155 / 28 | Mapped — `p_hits` |
| `Earned Runs Allowed` | 143 / 28 | Mapped — `p_earnedRuns` |
| `Strikes Counted` (PP) | 112 | **Left unsupported** — a batter's own ball/strike split does not exist in MLB Stats API's hitting game log (only a total `numberOfPitches` does) |
| `Pitches Seen` (PP) | 111 | Mapped — hitting group's `numberOfPitches`, aliased to `numberOfPitchesSeen` to avoid colliding with the pitching side's own pitch-count columns |
| `Balls Counted` (PP) | 111 | **Left unsupported** — same reason as `Strikes Counted` |
| `Plate Appearances` (PP) | 108 | Mapped — `plateAppearances` |
| `Walks Allowed` | 97 / 28 | Mapped — `p_baseOnBalls` |
| `PO` (PP) / `Pitching Outs` (UD) | 83 / 28 | Mapped — `p_outs` |
| `Pitcher FS` (PP) | 66 | **Mapped** — real PrizePicks formula (see below) |
| `Pitches Thrown` (PP) | 54 | Mapped — `p_numberOfPitches` |
| `Triples` | 27 / — | Mapped — `triples` |
| `Strikes Thrown` (PP) | 18 | Mapped — `p_strikes` |
| `Balls Thrown` (PP) | 18 | **Mapped** — computed, `p_numberOfPitches − p_strikes` (no direct column) |
| `Batters Faced` | 18 / 25 | Mapped — `p_battersFaced` |
| `Fantasy Points` (UD) | 170 | **Left unsupported** — no official Underdog MLB scoring formula could be sourced (underdogfantasy.com/underdogsports.com's rules pages 301-redirect to a JS app that returns 403 to an unauthenticated fetch); guessing a formula here would present an assumption as a real number |
| `1st Inn(ing). ___` (both platforms, 9 real variants) | 25 each ×5 (UD) + 7 each ×2 (PP) | **Left unsupported** — per-inning splits do not exist in MLB Stats API's season game log (per-GAME totals only); a real architecture mismatch, not a missing mapping |

10 of the 11 distinct real gaps found are stated, permanent architecture
limits (no matching MLB Stats API column/split exists at all), not
mapping oversights. `Fantasy Points` is the one gap that could close later
if Underdog's real formula becomes sourceable.

**Player-match rate**, checked directly against this same real pull: 29
`no_player_match` out of 2,931 real MLB rows that reached name matching
(rows with a resolvable stat type and a scorable odds type) — **99.0%**.

**MLBLIVE — a separate, deliberately unregistered sport label.** Real
ingested data carries `MLB` (11,142 rows, pre-game props — what this
plug-in supports) and `MLBLIVE` (1,428 rows) as two different `sport`
strings. Checked directly: 100% of real MLBLIVE stat_type strings are
inning-specific (`1st Inn. Pitches Seen`, `1-3 Inn. HRR`, `3rd Inn. Balls
Counted`, etc.) — the same per-game-number mismatch as the `1st Inn.`
rows above, for the whole category. `pickem_sport_plugins/mlb.py`'s
`MLB_SPORT_LABELS` deliberately excludes `"mlblive"`, so these rows keep
reporting `model_status="unsupported_sport"` — an honest, correct result,
not a bug to fix later.

### Computed stat types: Hitter FS and Pitcher FS

Both are real PrizePicks scoring formulas, confirmed live (2026-09-11) via
`prizepicks.com/playbook-article/how-to-play-prizepicks-mlb-fantasy-scoring-system`,
not guessed:

- **Hitter FS**: Single = 3, Double = 5, Triple = 8, Home Run = 10,
  Run = 2, RBI = 2, Walk = 2, Hit By Pitch = 2, Stolen Base = 5.
- **Pitcher FS**: Win = 6, Quality Start = 4, Earned Run = −3,
  Strikeout = 3, Out = 1. "Win" reads MLB Stats API's own real per-game
  `wins` field directly (not derived). "Quality Start" (MLB's real rule:
  ≥6 innings pitched AND ≤3 earned runs) is derived from `p_outs >= 18`
  (6 full innings, using the real outs count rather than parsing MLB's
  "X.Y" innings-pitched STRING, where `.1`/`.2` mean partial-inning outs,
  not decimal tenths) and `p_earnedRuns <= 3`.

**Verification performed before handoff**, same standard as NFL's Kicking
Points/Fantasy Score: both formulas were independently hand-computed
outside the model's own code, against a real player's full real season
game log, and cross-checked against the model's real output.
- Hitter FS: Aaron Judge's real 2026 hitting log (61 games) hand-summed to
  a season Hitter FS total of 581; `_compute_hitter_fs()` on the same real
  data produced 581 — identical. Run independently through
  `pickem_model.py`'s own `resolve_stat_spec()`/`build_stat_series()` path
  (not just the standalone function) — same result, 581, confirming the
  formula is correctly wired into the real pipeline, not just correct in
  isolation.
- Pitcher FS: Gerrit Cole's real 2026 pitching log (19 games — 8 wins, 333
  outs, 42 earned runs, 113 strikeouts, 11 real quality starts) hand-summed
  to a season Pitcher FS total of 638; `_compute_pitcher_fs()` on the same
  real data produced 638 — identical.

### Real, live end-to-end proof

A full production run (`python pickem_model.py --season 2026`) against the
real 57,628-row ingested snapshot produced 2,880 real `estimated` MLB+NFL
rows (MLB dominant — 2026 NFL season data is still sparse this early).
Independently re-pulled Framber Valdez's real 2026 pitching game log
(person id 664285) outside the model's own code: 28 games, mean
`numberOfPitches` = 89.321429 — matched the model's own `season_avg` for
his real "Pitches Thrown" prop (line 94.5, `model_mean` 92.18) to the same
six decimal places, proving the real MLB Stats API data is flowing
correctly through `fetch_mlb_season_stats()` into the model's scoring math,
not just producing a plausible-looking number.

Real MLB `model_status` breakdown from that same run (11,142 total real
MLB rows): `unsupported_odds_type` 7,824 (Demon/Goblin lines — a pre-
existing, sport-agnostic gap, not this session's scope), `estimated`
2,880, `unsupported_stat_type` 387 (all of them real, stated gaps from the
table above — nothing unexpected/unmapped), `no_player_match` 29,
`no_line_value` 22.

### Real bug found and fixed: two-way players (`build_stat_series()`)

While independently verifying a two-way player's (real example: Shohei
Ohtani, MLB Stats API person id 660271) real data against the model,
found that `build_stat_series()` in `pickem_model.py` filtered a player's
rows by `player_id` only, then summed the requested stat across every one
of those rows — for a normal player, every row is the same game-log type,
so this was correct; for a two-way player, whose row set (per
`fetch_mlb_season_stats()`) includes BOTH his real hitting rows and real
pitching rows under one `player_id`, a hitting-stat query silently
included his unrelated pitching rows too. `.sum(axis=1)` treats the
missing (`NaN`) hitting columns on his pitching rows as 0 rather than
excluding those rows, so the SUM came out numerically right but the game
COUNT did not — confirmed live: his real Home Runs season_average came
out `30/144 = 0.208` (144 = his real 130 hitting games + his real 14
unrelated pitching games) instead of the real `30/130 = 0.231`.
`recent_form`'s "last 5 by `sort_key`" was worse: since his hitting and
pitching logs each restart `sort_key` at 1, his real last-5-batting-games
window could be contaminated with rows from his pitching log entirely.

**Fix:** `build_stat_series()` now drops rows where the requested stat's
own columns are entirely absent (`games.dropna(subset=stat_cols,
how="all")`) before summing/computing — so a hitting-stat query only ever
sees a player's hitting rows, and a pitching-stat query only ever sees
their pitching rows, regardless of what else shares their `player_id`.
This is a fix in the shared, sport-agnostic file, not MLB-specific — it
protects any current or future plug-in that might fetch more than one
game-log type per player.

**Verified after the fix**, against Ohtani's real 2026 data (Los Angeles
Dodgers, MLB Stats API team id 119): Home Runs now resolves to exactly his
130 real hitting games, season_average `0.230769...`, matching an
independent hand-filter of his real hitting-only rows to the same value;
Ks (a pitching stat) resolves to exactly his 14 real pitching games,
correctly excluded from his hitting query and vice versa.

The regression suite (`test_pickem_model.py`) gained a dedicated test,
`test_mlb_two_way_player_stats_do_not_cross_contaminate`, built from a
synthetic two-way-player fixture reproducing this exact row shape, so this
cannot silently regress. The existing NFL golden-snapshot regression test
was re-run after the fix and is still byte-for-byte identical — the fix
is a no-op for every single-game-log-type scenario, which is every sport
this project supports except this one real MLB edge case.

No real ingested prop for a two-way player existed in this session's own
live pull (checked directly — zero rows for "Ohtani" or any name variant
in the real 2026-09-11 ingested data), so this could not be proven via a
real end-to-end props → estimate run today. It was instead proven against
his real MLB Stats API season data directly, independently of the ingested
props pipeline, plus the new synthetic regression test. This should be
re-confirmed via a real ingested prop the next time a two-way player has
one live on either platform.

---

## Session 2.14 — Soccer stat-type coverage (EPL via the FPL plug-in,
## everything else via the ESPN plug-in)

**Real ingested sport labels (2026-09-11 live production pull, 56,841 total
rows):** unlike every prior sport, soccer arrives under THREE distinct real
sport strings, not one — `SOCCER` (10,113 rows, PrizePicks), `EPL` (3,512
rows, PrizePicks — PrizePicks itself already splits EPL out as its own
category), and `FIFA` (2,581 rows, Underdog). `FIFA` was checked directly
and is real-life soccer, not the video game — real player names in that
category include Ousmane Dembele, Erling Haaland, Lamine Yamal, Kylian
Mbappe, Jude Bellingham, and other real, current top-flight players.
`pickem_sport_plugins/epl.py`'s `EPL_SPORT_LABELS` covers `EPL` only;
`pickem_sport_plugins/soccer.py`'s `SOCCER_SPORT_LABELS` covers `SOCCER` and
`FIFA` (both route to the ESPN-based plug-in, since Underdog's `FIFA` label
does not distinguish EPL players from any other league's — see that file's
own docstring). Note also: `SOCCER`-labeled real `game_matchup` values span
a much wider real set of leagues than the roadmap card's five (La Liga,
Serie A, Bundesliga, Ligue 1, MLS) — real matchups included Argentine,
Brazilian, Liga MX, NWSL, and Saudi-league team names. Only the five
ESPN-confirmed leagues are wired into `fetch_soccer_espn_season_stats()`;
props for a player from an unmapped league correctly fall through to
`no_player_match` (an honest result — this plug-in genuinely has no data
for them — not a bug).

### EPL — real stat-type strings, mapped against real FPL fields

Real per-gameweek FPL fields (`element-summary/{id}/`'s `history`,
confirmed live 2026-09-11): `minutes, goals_scored, assists, clean_sheets,
goals_conceded, own_goals, penalties_saved, penalties_missed, yellow_cards,
red_cards, saves, bonus, bps, tackles, clearances_blocks_interceptions,
recoveries, starts, expected_goals, expected_assists`.

| Real stat_type string | Real count | Outcome |
|---|---|---|
| Shots | 937 | **Unsupported** — no shot-count field in FPL's real per-gameweek data |
| SOT | 639 | Unsupported — same reason |
| Goal + Assist | 414 | **Mapped** (composite) → `goals_scored + assists` |
| Goals | 382 | **Mapped** → `goals_scored` |
| Assists | 349 | **Mapped** → `assists` |
| Fouls | 319 | Unsupported — no foul-count field in FPL's real data |
| Tackles | 318 | **Mapped** → `tackles` (a real FPL field) |
| Goalie Saves | 105 | **Mapped** → `saves` |
| Passes Attempted | 16 | Unsupported — no field |
| Fantasy Score | 14 | Unsupported — PrizePicks' real outfield formula (see below) needs 6 real components FPL's data doesn't carry |
| Goalie Fantasy Score | 8 | Unsupported — see below |
| Clearances | 3 | Unsupported — FPL's real `clearances_blocks_interceptions` is a DIFFERENT combined stat (clearances+blocks+interceptions), not pure clearances; mapping it to a stat literally named "Clearances" would misrepresent it |
| Attempted Dribbles | 3 | Unsupported — no field |
| Crosses | 2 | Unsupported — no field |
| Goals Allowed | 2 | **Mapped** → `goals_conceded` |
| GA F30 Mins | 1 | Unsupported — needs a within-game time split FPL's per-gameweek totals don't carry |

Real, checked result: 1,570 of 3,512 real EPL rows (44.7%) map to a real
FPL column; the remaining 1,942 (55.3%) are real, stated gaps — a real
MAJORITY left unsupported, disclosed plainly rather than papered over,
because FPL's real per-gameweek data structurally does not carry shot
counts, foul counts, or most of PrizePicks' own outfield Fantasy Score
inputs. See `pickem_sport_plugins/epl.py`'s own docstring for the full
reasoning.

### SOCCER / FIFA (non-EPL) — real stat-type strings, mapped against real
### ESPN fields

Real per-player match fields (`summary?event={id}`'s
`rosters[].roster[].stats`, confirmed live across La Liga/Serie A/
Bundesliga/Ligue 1/MLS, 2026-09-11): `appearances, foulsCommitted,
foulsSuffered, goalAssists, goalsConceded, offsides, ownGoals, redCards,
saves, shotsFaced, shotsOnTarget, subIns, totalGoals, totalShots,
yellowCards` — identical field set across all five leagues checked.

| Real stat_type string (platform) | Real count | Outcome |
|---|---|---|
| Shots (PP) | 2,605 | **Mapped** → `totalShots` |
| SOT (PP) | 1,950 | **Mapped** → `shotsOnTarget` |
| Goals (PP) | 1,304 | **Mapped** → `totalGoals` |
| Goal + Assist (PP) | 1,138 | **Mapped** (composite) → `totalGoals + goalAssists` |
| Tackles (PP) | 1,109 | **Unsupported** — no tackles field anywhere in ESPN's real per-player soccer stats, checked directly across all 5 leagues |
| Assists (PP) | 993 | **Mapped** → `goalAssists` |
| Fouls (PP) | 677 | **Mapped** → `foulsCommitted` |
| Goalie Saves (PP) | 174 | **Mapped** → `saves` |
| Passes Attempted (PP) | 68 | Unsupported — no field |
| Fantasy Score (PP) | 40 | Unsupported — needs 6 of 11 real formula components (Passes Attempted, Shots Assisted, Clearances, Tackles Attempted, Attempted Dribbles, Crosses) that ESPN's real data doesn't carry |
| Goalie Fantasy Score (PP) | 17 | **Mapped** (computed) — every component (`starter`, `saves`, `goalsConceded`) IS a real ESPN field |
| Clearances (PP) | 13 | Unsupported — no field |
| Attempted Dribbles (PP) | 12 | Unsupported — no field |
| Shots Assisted (PP) | 9 | Unsupported — no field |
| Crosses (PP) | 4 | Unsupported — no field |
| Goals + Assists (UD) | 573 | **Mapped** (composite) → `totalGoals + goalAssists` |
| Goals (UD) | 430 | **Mapped** → `totalGoals` |
| Assists (UD) | 392 | **Mapped** → `goalAssists` |
| Shots on Target (UD) | 374 | **Mapped** → `shotsOnTarget` |
| Cards (UD) | 282 | **Mapped** (composite) → `yellowCards + redCards` |
| Shots Attempted (UD) | 251 | **Mapped** → `totalShots` |
| 1H Goals (UD) | 131 | Unsupported — needs a first-half-only split; same "no per-game-scoped number" mismatch as MLB's per-inning gap (Session 2.13) |
| Fouls Committed (UD) | 52 | **Mapped** → `foulsCommitted` |
| Saves (UD) | 51 | **Mapped** → `saves` |
| Fouls Drawn (UD) | 45 | **Mapped** → `foulsSuffered` |

Real, checked result: 8,858 of 10,113 real SOCCER rows (87.6%) and 2,450 of
2,581 real FIFA rows (94.9%) map to a real ESPN field or derivation.

### PrizePicks' official Soccer Fantasy Score formulas (sourced, confirmed
### live 2026-09-11, via prizepicks.com/playbook-article/how-to-play-
### prizepicks-soccer-fantasy-scoring-system-for-world-cup)

**Outfield Fantasy Score:** Goal Scored=10, Assist=5, Shot=1, Shot on
Target=1, Passes Attempted=0.05, Shots Assisted=0.5, Clearances=1, Tackles
Attempted=1, Attempted Dribbles=1, Crosses=0.5, Yellow Card=-1, Red
Card=-2, Fouls=-0.5. **Not coded** — 6 of these 11 real components
(Passes Attempted, Shots Assisted, Clearances, Tackles Attempted, Attempted
Dribbles, Crosses) have no equivalent in either real data source available
to this project (FPL or ESPN). Computing a partial version from only the 5
available components would silently misrepresent the real formula — this
project's "no unnamed black-box factors" rule (Session 2.3 onward) means
this stays a named, stated gap instead.

**Goalie Fantasy Score:** Starting Score=5 (if started), Saves=2 each,
Goals Conceded=-2 each, Clean Sheet=+5 (started AND 0 conceded). **Coded**
in `pickem_sport_plugins/soccer.py` — every component maps to a real ESPN
field this plug-in already fetches (`starter`, `saves`, `goalsConceded`);
Clean Sheet is derived (started AND `goalsConceded == 0`), the same way
MLB's Quality Start (Session 2.13) was derived from real columns rather than
guessed. Not coded for the FPL/EPL plug-in — FPL's real data doesn't expose
a per-gameweek `starter` flag or goals-conceded-while-on-pitch distinction
in the same directly usable shape, and EPL's own real Goalie Fantasy Score
volume (8 rows) is small; left as a stated gap there (see `epl.py`).

### Real, live, independently re-verified end-to-end proofs

1. **EPL (FPL path):** Alisson Becker's real "Goalie Saves" prop scored
`model_status="estimated"`, `season_avg=3.0` (3 real gameweeks played:
saves of 3, 1, 5). Independently re-pulled his real FPL id and per-gameweek
`saves` history directly (separate script, no import from `epl.py` or
`pickem_model.py`) — `[3, 1, 5]`, mean `3.0`, matching exactly.
2. **Non-EPL (ESPN path):** Lamine Yamal's (La Liga, Barcelona) real "Goals"
prop scored `model_status="estimated"`, `season_avg=1.0` (4 real La Liga
matches). Independently re-pulled his real match-by-match `totalGoals` from
ESPN's public API directly (separate script, no import from `soccer.py`) —
goals of `[0, 0, 2, 2]` across his 4 real completed matches, mean `1.0`,
matching exactly.
3. **Real, live props from 4 distinct non-EPL leagues scored end-to-end**
in the same production run (`output/estimation/latest.csv`, 2026-09-11):
La Liga (e.g. Vinícius Júnior, Kylian Mbappé, Jude Bellingham — Shots/SOT),
Serie A (Lorenzo Palmisani — Goalie Saves), Bundesliga (Finn Dahmen, Mark
Flekken — Goalie Saves and Goalie Fantasy Score), and MLS (Kristijan
Kahlina, James Pantemis — Goalie Saves) — exceeding the roadmap card's
"at least 3 distinct non-EPL leagues" bar.
4. **Bundesliga and Ligue 1 individually confirmed live against ESPN's
API** (this session, 2026-09-11) — real completed matches found for both
(`ger.1`: 18 completed events in the season so far; `fra.1`: 27), not
assumed from the La Liga/Serie A/MLS pattern holding.

### Real `model_status` breakdown after this session (same 2026-09-11
### production run as the independent proofs above)

Most SOCCER/EPL rows are gated by the pre-existing, sport-agnostic
Demon/Goblin `unsupported_odds_type` check (Session 2.13's own priority
note — most real PrizePicks volume across every sport is Demon/Goblin, not
just MLB) before ever reaching stat resolution — this is why the real
`estimated` counts below are smaller than the raw stat-type-coverage
percentages above would suggest, and is not a defect introduced by this
session. Underdog rows (FIFA) are not subject to that gate.

- `SOCCER` (10,113 rows): `unsupported_odds_type` 9,874, `unsupported_stat_type`
146, `no_player_match` 56, **`estimated` 32**, `no_line_value` 3,
`insufficient_history` 2.
- `EPL` (3,512 rows): `unsupported_odds_type` 3,400, `unsupported_stat_type`
90, **`estimated` 12**, `no_player_match` 10.
- `FIFA` (2,581 rows, not gated by the Demon/Goblin check): `no_player_match`
1,276 (real players from leagues outside this plug-in's five, or unmatched
naming — see the "real, checked" note above), `no_line_value` 562,
**`estimated` 548**, `unsupported_stat_type` 131, `insufficient_history` 64.

### Real cost note (same "no bulk alternative" precedent as MLB, Session
### 2.13, applied here at a larger scale)

Neither the FPL API nor ESPN's public API has a bulk "every player's season
stat line" endpoint. A full production run of the two new plug-ins makes
roughly 650+ real HTTP calls to the FPL API (one per current player, for
each player's own per-gameweek history) and roughly 470+ real calls to
ESPN's API (one scoreboard call per league per calendar month of the season
so far, plus one summary call per completed match — 474 completed matches
found across the five confirmed leagues as of 2026-09-11, MLS alone
accounting for 358 of them). Total real run time for this session's full
production pipeline (all four registered plug-ins, not just soccer):
approximately 6.5 minutes. This is an accepted, real cost of these data
sources, same standing as MLB's own per-team-roster HTTP-call cost — there
is no bulk alternative to fall back to.
