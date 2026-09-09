# Sportsbook Player Props Estimation Model Spec (Session 6.2)

This is the same-detail-level spec document required by this project's "no
unnamed black-box factors" standard, matching `pickem_estimation_model_spec.md`'s
role for Track 1. Full reasoning lives in `scripts/estimation/
sportsbook_props_model.py`'s own module docstring -- this file is the short,
standalone reference version.

## Why this isn't a straight reuse of the pick'em model

Session 6.1's real ingested data (DK/FD) turned out to contain two market
shapes, neither of which matches PrizePicks/Underdog's "one line, two-sided,
single game" shape:

1. **FanDuel v1 real data is season-long futures**, not single-game props
   (e.g. "Aaron Rodgers Regular Season Passing Yards 2026-27", line =
   season total, not a per-game number).
2. **DraftKings v1 real data is TD-scorer props** (Anytime TD Scorer, 2+
   TDs, First TD Scorer) -- one priced selection per player, no numeric
   line, no "under" side.

Both are real, discovered shapes (not assumed in advance) -- see
`scripts/estimation/sportsbook_props_model.py`'s module docstring for the
full derivation.

## Model 1 -- Season-total projection (FanDuel `player_performance` rows)

```
full_season_projection = stat_accrued_so_far + games_remaining * recent_form
```

- `stat_accrued_so_far`: real sum of the player's REG-season games played
  so far this season (nflverse).
- `games_remaining = 17 - games_played` (stated v1 assumption: every player
  finishes a standard 17-game season -- no rest-of-season-out adjustment).
- `recent_form`: the same recency-weighted per-game rate
  `pickem_model.py` already computes (imported, not recomputed).
- `full_season_sigma = per_game_sigma * sqrt(games_remaining)` (only the
  remaining games are uncertain; the accrued portion is already known).
- `prob_over(line, full_season_projection, full_season_sigma)` via the same
  normal-CDF approach as the pick'em model.
- Implied probability: real two-sided de-vig (`over`/`under` American odds
  normalized to sum to 1.0) -- a clean, textbook de-vig, proven correct
  against the -115/-105 example in both Session 6.1's and this session's
  own tests.

## Model 2 -- TD-scorer Poisson model (DraftKings `player_touchdown` rows)

```
lambda = 0.5 * season_avg(total_TDs_per_game) + 0.5 * recent_form(total_TDs_per_game)
P(Anytime TD, "1+")  = 1 - exp(-lambda)
P(2+ TDs)            = 1 - exp(-lambda) - lambda*exp(-lambda)
```

`total_TDs_per_game` = passing_tds + rushing_tds + receiving_tds (nflverse
columns, same composite pattern as `pickem_model.py`'s "player tds" entry).

`"First TD Scorer"` is **not modeled in v1** -- correctly pricing "first"
requires the relative TD rates of every player in the game (a full-field
race), not an independent per-player probability. Every such row gets
`model_status="unsupported_market_first_scorer"`, a stated gap.

Implied probability for this market: the **raw** single-side American-odds
implied probability, explicitly flagged
`implied_prob_includes_field_vig=True`. There is no "under" side to de-vig
against -- the real vig here is spread across every player priced in the
same market, which this session's per-row data does not preserve as a
group. This is an honestly-stated v1 limitation, not a hidden one -- see
"WHY THE TWO MARKET SHAPES ARE HANDLED DIFFERENTLY" in the script's
docstring.

## Real validation run (2026-09-09, against live ingested data)

**First run (stale FanDuel snapshot, before the user re-ran ingestion):**
947 real rows; `estimated`: 326 (all DraftKings, 0 FanDuel); `no_player_match`:
458 (275 FanDuel + 183 DraftKings); `unsupported_market_first_scorer`: 163.
FanDuel's 0% match rate was diagnosed as stale on-disk data (see below), not
a bug -- the file on disk predated the real per-market player-name parsing
fix recorded in Session 6.1's continuation entry.

**Second run (after the user re-ran `python scripts/ingestion/
ingest_fd_props.py` locally, producing a fresh `fd_latest.csv` with 141 real
player-prop rows):** 813 real rows; `estimated`: 374 (326 DraftKings + 48
FanDuel); `no_player_match`: 191 (8 FanDuel -- real rookies not yet in
nflverse's weekly-stats data, e.g. Fernando Mendoza, Jeremiyah Love -- plus
183 DraftKings); `unsupported_market_first_scorer`: 163;
`unsupported_stat_type`: 44 (all FanDuel, real stat_type strings "Passing
TDs"/"Rushing TDs"); `season_complete_no_remaining_games`: 41.

**Real gap found and fixed from this second run's real output:** the 44
`unsupported_stat_type` rows were FanDuel's real wording "Passing TDs" /
"Rushing TDs" (lowercased: `"passing tds"` / `"rushing tds"`), which did
not match any key in `pickem_model.py`'s `NFL_STAT_TYPE_MAP` -- that map
already had `"pass tds"` and `"passing touchdowns"` (PrizePicks/Underdog
wordings) but not FanDuel's own phrasing. Added the two missing key
variants directly to `NFL_STAT_TYPE_MAP` (additive only -- no existing key
changed), matching the exact pattern Session 2.3's Decision #4 already
established for real-data-driven stat-type coverage gaps.

**Third run (after the stat-type fix, same `fd_latest.csv`/`dk_latest.csv`
inputs):** 813 real rows; `estimated`: 396 (326 DraftKings + 70 FanDuel);
`no_player_match`: 191 (unchanged); `unsupported_market_first_scorer`: 163
(unchanged); `season_complete_no_remaining_games`: 63.
`unsupported_stat_type`: 0. The 44 previously-unsupported rows split
cleanly into +22 `estimated` and +22 `season_complete_no_remaining_games`
(players already at 17 games played) -- fully accounted for, confirming
the fix did not silently misroute any row.

- DraftKings' real Poisson output is sane and monotonic in the expected
  direction on spot-check: e.g. Rhamondre Stevenson (14 games, model_mean
  ~1.20 TDs/game) produced `prob_over` (P(2+ TDs)) = 0.336 against a raw
  implied probability of 0.125 (edge +0.211); low-usage players (e.g.
  Rashid Shaheed, model_mean ~0.056) produced `prob_over` = 0.0015, far
  below their raw implied price -- correctly negative edge.
- FanDuel's real Passing Yards de-vig produced a flat 0.5/0.5 implied
  probability across every real row checked -- confirmed as a REAL
  finding, not a bug: FanDuel prices every real Passing Yards season
  future at symmetric -114/-114 odds (spot-checked directly against
  `fd_latest.csv`), which de-vigs to exactly 0.5/0.5 by construction.
  FanDuel's real Passing TDs market prices asymmetrically (e.g. -114/-114
  is NOT universal there), confirmed by real varying `implied_prob_over`
  values (0.4718-0.5379) once the stat-type fix above let those rows
  through.
- FanDuel's real season-total projections behave sensibly on spot-check:
  e.g. Aaron Rodgers (16 games played, 1 remaining, real accrued total
  already near the season line) produced `prob_over` near 1.0 against a
  3050.5-yard line; Jayden Daniels (7 games played, 10 remaining, a real
  lower recent-form rate) produced `prob_over` = 0.001 against a
  3200.5-yard line -- correctly reflecting that most of his season total
  is still unaccrued and projected low.

## What this model does NOT do yet (stated gap, not silent)

- Only NFL rows are modeled.
- Only stat types already in `pickem_model.py`'s `NFL_STAT_TYPE_MAP` /
  `COMPOSITE_STAT_TYPES` / `COMPUTED_STAT_TYPES` are modeled for the
  season-total path.
- "First TD Scorer" markets are entirely unmodeled.
- Season-total projection assumes a flat 17-game season for every player,
  with no rest-of-season-out adjustment.
- The one-sided TD-scorer implied probability still includes field vig,
  not yet de-vigged against the rest of the market's real prices.
- No opponent/matchup, injury/role, home/away, or pace/usage adjustment.
