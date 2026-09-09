"""
Session 6.2 -- Estimation Engine Adaptation (Sportsbook Player Props: DK/FD)

WHAT THIS SCRIPT IS
--------------------
Adapts Session 2.3's pick'em model (pickem_model.py) to the sportsbook player
prop shape (Session 6.1's data). Per the roadmap card, this reuses the
existing nflverse pull, name-matching, and stat-resolution logic from
pickem_model.py directly (imported, not copied) -- only the parts that
differ because the market shape differs get new code here.

WHY THIS IS NOT A DIRECT COPY OF pickem_model.py -- TWO REAL SHAPE
DIFFERENCES FOUND IN SESSION 6.1'S REAL DATA
---------------------------------------------------------------------------
Session 6.1's real ingested data (data/sportsbook_props/normalized/
{dk,fd}_latest.csv) turned out to contain two market shapes neither of
which matches PrizePicks/Underdog's "one line, two-sided, single game"
shape pickem_model.py was built for:

1. FanDuel's real v1 data is SEASON-LONG FUTURES, not single-game props
   (confirmed directly in Session 6.1's continuation entry, SESSION_LOG.md:
   the "nfl" custom page returns markets like "Aaron Rodgers Regular Season
   Passing Yards 2026-27" with a season-total line, e.g. 3050.5 -- not a
   per-game number). pickem_model.py's mean/sigma are PER-GAME. Applying a
   per-game mean directly against a season-total line would silently
   compare the wrong units. This script instead projects a FULL-SEASON
   TOTAL (see project_season_total() below) and only then compares it to
   the line.
2. DraftKings' real v1 data (Session 6.1: subcategory 12438) is TD-SCORER
   PROPS -- "First TD Scorer", "Anytime TD Scorer", "2+ TDs" -- which are
   NOT two-sided Over/Under markets at all. There is no numeric line and no
   "under" price; each row is one priced selection ("this player scores"),
   priced against the whole field of players in the game. This needs a
   genuinely different probability model (a Poisson TD-count model, see
   "TD-SCORER PROPS" below), not a normal-CDF-over-a-line comparison.

Both are handled explicitly below, each producing a real model_status value
so a row this v1 can't handle yet is visible, never silently dropped -- the
same standard pickem_model.py already holds itself to.

SEASON-TOTAL PROJECTION (FanDuel player_performance rows)
-----------------------------------------------------------------------
full_season_projection = stat_accrued_so_far + games_remaining * recent_form

  - stat_accrued_so_far: the real sum of the player's own REG-season games
    played so far this season (from nflverse), for the resolved stat.
  - games_remaining = ASSUMED_SEASON_LENGTH_GAMES - games_played. v1 assumes
    every player finishes a standard 17-game season -- a stated,
    unadjusted simplification (no bye-week-already-passed correction, no
    injury/rest-of-season-out adjustment). A player already out for the
    season would get an inflated projection under this assumption; this is
    a named v1 gap, not a hidden one.
  - the "recent_form" rate used for the remaining games is the SAME
    recency-weighted per-game rate pickem_model.py already computes
    (imported directly, not recomputed) -- so this script adds a
    season-total wrapper around an unchanged per-game estimate rather than
    inventing a second per-game model.
  - sigma for the total: per-game sample sigma scaled by
    sqrt(games_remaining) (standard i.i.d.-games variance scaling), since
    only the REMAINING games are still uncertain -- the accrued portion is
    already a known, fixed number, not a random variable.
  - a player with 0 games remaining (season already over) has sigma=0 and
    is reported as model_status="season_complete_no_remaining_games", not
    forced through the normal-CDF path.

TD-SCORER PROPS (DraftKings player_touchdown rows)
-----------------------------------------------------------------------
"Anytime TD Scorer" and "2+ TDs" are modeled as a Poisson count of the
player's total touchdowns (passing + rushing + receiving) per game, using
the SAME recency-weighted blend of season_avg/recent_form pickem_model.py
already computes for the composite ["passing_tds","rushing_tds",
"receiving_tds"] stat (imported, not recomputed):
  lambda = model_mean_tds_per_game (floored at a small positive epsilon,
           since a Poisson rate of exactly 0 makes every probability
           degenerate)
  P(Anytime TD, i.e. >=1 TD)  = 1 - exp(-lambda)
  P(2+ TDs)                   = 1 - exp(-lambda) - lambda*exp(-lambda)
"First TD Scorer" is NOT modeled in v1 -- stated gap, not silently
approximated. Correctly modeling "first" requires knowing the relative TD
rates of every player in the game (a full-field race, not a per-player
independent probability), which is real additional modeling this session
does not attempt. Every "First TD Scorer" row gets
model_status="unsupported_market_first_scorer".

IMPLIED PROBABILITY -- WHY THE TWO MARKET SHAPES ARE HANDLED DIFFERENTLY
(this directly answers the roadmap card's own validation checkbox: "model
correctly separates true edge from vig cost")
-----------------------------------------------------------------------
- Two-sided rows (FanDuel player_performance, real over AND under American
  odds present): the true no-vig probability is computed by normalizing
  both sides' raw implied probabilities (from
  schema_props.american_odds_to_implied_probability) so they sum to
  exactly 1.0 -- the same de-vig math already proven correct in Session
  6.1's own test (test_vig_extraction_matches_known_example). This is a
  clean, textbook two-outcome de-vig.
- One-sided rows (DraftKings TD-scorer props): there is no "under" price to
  de-vig against -- the market's real vig here is spread across every
  player in the field (all those individual prices sum to well over 100%
  together), not between two sides of one line. **FIXED in Session 6.4**:
  `ingest_dk_props.py` already carries the real DK `marketId` per selection
  as `source_market_id`, so every player priced in the SAME real market
  (e.g. one game's "Anytime TD Scorer" market) can be grouped together
  (`schema_props.same_market_group_key`) and their raw implied
  probabilities normalized against each other so they sum to exactly 1.0
  (`schema_props.normalize_field_vig`, `build_field_vig_index` below) --
  the honest N-way generalization of the two-sided de-vig used for
  FanDuel's rows. `implied_prob_includes_field_vig` is now False for every
  row this session can actually group (group_size >= 2 real selections);
  a row this run's real data could only capture alone (group_size == 1, or
  missing odds) still reports the raw, vig-included price with the flag
  left True -- an honest per-row boundary, not a blanket claim the fix
  covers every possible row.

WHAT THIS MODEL DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Only NFL rows are modeled (same v1 boundary as pickem_model.py).
- Only stat types already known to pickem_model.py's NFL_STAT_TYPE_MAP /
  COMPOSITE_STAT_TYPES / COMPUTED_STAT_TYPES are modeled for the
  season-total path; an unrecognized stat_type is a visible
  "unsupported_stat_type" row.
- "First TD Scorer" markets are not modeled at all (see above).
- The season-total projection assumes every player plays a full 17-game
  season with no rest-of-season-out adjustment (see above).
- The one-sided TD-scorer implied probability is field-normalized as of
  Session 6.4 ONLY for rows this run could actually group (group_size >= 2
  real selections in the same real market); a row captured alone still
  reports the raw, vig-included price with `implied_prob_includes_field_vig
  =True` (see above).
- No opponent/matchup, injury/role, home/away, or pace/usage adjustment --
  same stated gap as pickem_model.py.

USAGE
-----
pip install pandas numpy pyarrow --break-system-packages
python sportsbook_props_model.py --season 2025
"""

from __future__ import annotations

import argparse
import logging
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ingestion"))

from pickem_model import (  # noqa: E402  (path insert must happen first)
    NFL_SPORT_LABELS,
    build_name_lookup,
    build_stat_series,
    fetch_nfl_weekly_stats,
    normalize_name,
    recent_form,
    resolve_stat_spec,
    resolved_stat_key_for,
    sample_sigma,
    season_average,
)
from schema_props import (  # noqa: E402
    american_odds_to_implied_probability,
    normalize_field_vig,
    same_market_group_key,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "sportsbook_props" / "normalized"
DK_LATEST = NORMALIZED_DIR / "dk_latest.csv"
FD_LATEST = NORMALIZED_DIR / "fd_latest.csv"
OUTPUT_DIR = BASE_DIR / "output" / "estimation"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

# ---------------------------------------------------------------------------
# Model constants -- named explicitly, per this project's "no unnamed
# black-box factors" standard. Values reused from pickem_model.py are
# imported, not redefined, so the two models can never silently drift.
# ---------------------------------------------------------------------------
ASSUMED_SEASON_LENGTH_GAMES = 17  # stated v1 simplification -- see docstring
TD_COMPOSITE_COLUMNS = ["passing_tds", "rushing_tds", "receiving_tds"]
POISSON_LAMBDA_FLOOR = 1e-6  # avoids a degenerate P(0 TDs)=1.0 for a
# player with a real observed rate of exactly zero so far

DK_TD_MARKET_STAT_TYPES = {
    "anytime td scorer": "anytime",
    "2+ tds": "two_plus",
    "first td scorer": "unsupported_first_scorer",
}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("sportsbook_props_model")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


# ---------------------------------------------------------------------------
# Season-total projection (FanDuel player_performance rows)
# ---------------------------------------------------------------------------
def project_season_total(series: pd.Series) -> tuple[Optional[float], Optional[float], int, int]:
    """Returns (full_season_mean, full_season_sigma, games_played,
    games_remaining) for the player's resolved stat, per the docstring's
    "SEASON-TOTAL PROJECTION" section. series is the player's real
    per-game values so far this season, oldest to newest (same series
    build_stat_series() already produces for pickem_model.py)."""
    games_played = len(series)
    games_remaining = max(ASSUMED_SEASON_LENGTH_GAMES - games_played, 0)

    if games_played < 2:
        return None, None, games_played, games_remaining

    accrued = float(series.sum())
    per_game_rate = recent_form(series)  # same recency-weighted rate pickem_model.py uses
    if per_game_rate is None:
        return None, None, games_played, games_remaining

    full_season_mean = accrued + games_remaining * per_game_rate

    if games_remaining == 0:
        return full_season_mean, 0.0, games_played, games_remaining

    per_game_mean_for_sigma = accrued / games_played if games_played else per_game_rate
    per_game_sigma = sample_sigma(series, per_game_mean_for_sigma)
    if per_game_sigma != per_game_sigma:  # NaN
        return full_season_mean, None, games_played, games_remaining

    full_season_sigma = per_game_sigma * math.sqrt(games_remaining)
    return full_season_mean, full_season_sigma, games_played, games_remaining


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def prob_over(line: float, mean: float, sigma: float) -> Optional[float]:
    if sigma is None or sigma != sigma or sigma <= 0:  # NaN-safe check
        return None
    z = (line - mean) / sigma
    return 1.0 - normal_cdf(z)


# ---------------------------------------------------------------------------
# TD-scorer Poisson model (DraftKings player_touchdown rows)
# ---------------------------------------------------------------------------
def poisson_prob_at_least(lam: float, k: int) -> float:
    """P(X >= k) for a Poisson(lam) count. Only k=1 (Anytime) and k=2
    (2+ TDs) are needed here."""
    lam = max(lam, POISSON_LAMBDA_FLOOR)
    p0 = math.exp(-lam)
    if k <= 0:
        return 1.0
    if k == 1:
        return 1.0 - p0
    if k == 2:
        p1 = lam * p0
        return 1.0 - p0 - p1
    raise ValueError(f"poisson_prob_at_least only supports k in {{1, 2}}, got {k}")


def build_field_vig_index(props_df: pd.DataFrame) -> dict[int, tuple[float, int]]:
    """Session 6.4 — the DK field-vig fix. Groups every row by its real
    same-market key (`same_market_group_key`, keyed on the existing
    platform/source_event_id/source_market_id columns — no schema change
    needed, since `ingest_dk_props.py` already carries the real DK
    `marketId` per selection) and field-normalizes each group's raw
    American-odds implied probabilities with `normalize_field_vig` so
    they sum to exactly 1.0, the honest N-way generalization of the
    two-sided de-vig already proven for FanDuel's rows.

    Returns a dict mapping each row's real DataFrame index to
    (field_normalized_prob, group_size) — group_size is returned
    alongside the probability so callers can tell a REAL group
    normalization (group_size >= 2, multiple real selections priced
    against each other) apart from a group of one (this run's data only
    captured a single selection for that real market — nothing to
    normalize against, so the raw price cannot honestly be called
    field-normalized). Rows with missing/invalid odds are skipped
    entirely (excluded from both the group's total and the returned
    dict) rather than treated as a real $0-vig contribution."""
    groups: dict[str, list[tuple[int, float]]] = {}
    for idx, row in props_df.iterrows():
        platform = row.get("platform")
        event_id = row.get("source_event_id")
        market_id = row.get("source_market_id")
        if pd.isna(platform) or pd.isna(event_id) or pd.isna(market_id) or not platform or not event_id or not market_id:
            continue
        raw = american_odds_to_implied_probability(row.get("over_american_odds"))
        if raw is None:
            continue
        key = same_market_group_key(str(platform), str(event_id), str(market_id))
        groups.setdefault(key, []).append((idx, raw))

    result: dict[int, tuple[float, int]] = {}
    for members in groups.values():
        indices = [m[0] for m in members]
        raw_probs = [m[1] for m in members]
        normalized = normalize_field_vig(raw_probs)
        group_size = len(members)
        for idx, norm_prob in zip(indices, normalized):
            result[idx] = (norm_prob, group_size)
    return result


def two_sided_devig(over_odds: Optional[int], under_odds: Optional[int]) -> tuple[Optional[float], Optional[float]]:
    """Normalizes both sides' raw American-odds implied probabilities so
    they sum to exactly 1.0 (removes the vig). Returns (implied_prob_over,
    implied_prob_under), both None if either side's odds are missing."""
    raw_over = american_odds_to_implied_probability(over_odds)
    raw_under = american_odds_to_implied_probability(under_odds)
    if raw_over is None or raw_under is None:
        return None, None
    total = raw_over + raw_under
    if total <= 0:
        return None, None
    return raw_over / total, raw_under / total


# ---------------------------------------------------------------------------
# Main per-row processing
# ---------------------------------------------------------------------------
def _blank_model_fields() -> dict:
    return {
        "season_avg": None,
        "recent_form": None,
        "games_played": None,
        "games_remaining": None,
        "model_mean": None,
        "model_sigma": None,
        "prob_over": None,
        "prob_under": None,
        "implied_prob_over": None,
        "implied_prob_under": None,
        "implied_prob_includes_field_vig": None,
        "edge_over": None,
        "edge_under": None,
    }


def process_props(props_df: pd.DataFrame, weekly_df: pd.DataFrame) -> pd.DataFrame:
    name_lookup = build_name_lookup(weekly_df)
    field_vig_index = build_field_vig_index(props_df)

    out_rows = []
    for row_idx, prop in props_df.iterrows():
        row = prop.to_dict()
        sport = str(row.get("sport") or "").strip().lower()
        prop_category = str(row.get("prop_category") or "").strip().lower()
        raw_stat_type = row.get("stat_type")
        stat_key_lower = str(raw_stat_type or "").strip().lower()

        if sport not in NFL_SPORT_LABELS:
            row["model_status"] = "unsupported_sport"
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        norm_name = normalize_name(row.get("player_name"))
        player_id = name_lookup.get(norm_name)
        if player_id is None:
            row["model_status"] = "no_player_match"
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        # -----------------------------------------------------------
        # TD-scorer props (one-sided, no numeric line)
        # -----------------------------------------------------------
        if prop_category == "player_touchdown" or stat_key_lower in DK_TD_MARKET_STAT_TYPES:
            market_kind = DK_TD_MARKET_STAT_TYPES.get(stat_key_lower)
            row["resolved_stat_key"] = "+".join(TD_COMPOSITE_COLUMNS)

            if market_kind == "unsupported_first_scorer" or market_kind is None:
                row["model_status"] = (
                    "unsupported_market_first_scorer" if market_kind else "unsupported_stat_type"
                )
                row.update(_blank_model_fields())
                out_rows.append(row)
                continue

            series = build_stat_series(weekly_df, player_id, "columns", TD_COMPOSITE_COLUMNS)
            if len(series) < 2:
                row["model_status"] = "insufficient_history"
                row.update(_blank_model_fields())
                row["games_played"] = len(series)
                out_rows.append(row)
                continue

            s_avg = season_average(series)
            r_form = recent_form(series)
            model_mean = 0.5 * s_avg + 0.5 * r_form  # same 50/50 blend as pickem_model.py

            model_prob = (
                poisson_prob_at_least(model_mean, 1)
                if market_kind == "anytime"
                else poisson_prob_at_least(model_mean, 2)
            )

            # Session 6.4 -- real DK field-vig fix. field_vig_index holds
            # every row's own same-market group's field-normalized
            # probability (group_size >= 2 selections priced against each
            # other) precomputed by build_field_vig_index() above. A row
            # this run's data could only capture alone (group_size == 1,
            # or the row's own odds were missing so it never entered any
            # group) falls back to the raw, still-vig-included price --
            # honestly still flagged True, never silently assumed fixed.
            field_entry = field_vig_index.get(row_idx)
            raw_implied = american_odds_to_implied_probability(row.get("over_american_odds"))
            if field_entry is not None and field_entry[1] >= 2:
                implied_prob = field_entry[0]
                includes_field_vig = False
            else:
                implied_prob = raw_implied
                includes_field_vig = True

            row["model_status"] = "estimated"
            row["season_avg"] = s_avg
            row["recent_form"] = r_form
            row["games_played"] = len(series)
            row["games_remaining"] = None
            row["model_mean"] = model_mean
            row["model_sigma"] = None
            row["prob_over"] = model_prob
            row["prob_under"] = None
            row["implied_prob_over"] = implied_prob
            row["implied_prob_under"] = None
            row["implied_prob_includes_field_vig"] = includes_field_vig
            row["edge_over"] = (
                (model_prob - implied_prob) if (model_prob is not None and implied_prob is not None) else None
            )
            row["edge_under"] = None
            out_rows.append(row)
            continue

        # -----------------------------------------------------------
        # Season-total player_performance props (two-sided, numeric line)
        # -----------------------------------------------------------
        kind, value, reason = resolve_stat_spec(raw_stat_type)
        if kind is None:
            row["model_status"] = reason
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        row["resolved_stat_key"] = resolved_stat_key_for(kind, value)

        series = build_stat_series(weekly_df, player_id, kind, value)
        full_mean, full_sigma, games_played, games_remaining = project_season_total(series)

        if full_mean is None:
            row["model_status"] = "insufficient_history"
            row.update(_blank_model_fields())
            row["games_played"] = games_played
            row["games_remaining"] = games_remaining
            out_rows.append(row)
            continue

        if games_remaining == 0:
            row["model_status"] = "season_complete_no_remaining_games"
            row.update(_blank_model_fields())
            row["games_played"] = games_played
            row["games_remaining"] = 0
            row["model_mean"] = full_mean
            out_rows.append(row)
            continue

        line = row.get("line")
        p_over = prob_over(line, full_mean, full_sigma) if line is not None else None
        implied_over, implied_under = two_sided_devig(
            row.get("over_american_odds"), row.get("under_american_odds")
        )

        row["model_status"] = "estimated" if p_over is not None else "no_line_value"
        row["season_avg"] = season_average(series)
        row["recent_form"] = recent_form(series)
        row["games_played"] = games_played
        row["games_remaining"] = games_remaining
        row["model_mean"] = full_mean
        row["model_sigma"] = full_sigma
        row["prob_over"] = p_over
        row["prob_under"] = (1.0 - p_over) if p_over is not None else None
        row["implied_prob_over"] = implied_over
        row["implied_prob_under"] = implied_under
        row["implied_prob_includes_field_vig"] = False
        row["edge_over"] = (p_over - implied_over) if (p_over is not None and implied_over is not None) else None
        row["edge_under"] = (
            (row["prob_under"] - implied_under)
            if (row["prob_under"] is not None and implied_under is not None)
            else None
        )
        out_rows.append(row)

    return pd.DataFrame(out_rows)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def load_props() -> pd.DataFrame:
    frames = []
    for path in (DK_LATEST, FD_LATEST):
        if path.exists():
            frames.append(pd.read_csv(path))
        else:
            log.warning("%s not found -- skipping that platform for this run.", path)
    if not frames:
        raise FileNotFoundError(
            f"Neither {DK_LATEST} nor {FD_LATEST} found. Run "
            f"scripts/ingestion/ingest_dk_props.py and/or ingest_fd_props.py first "
            f"(Session 6.1)."
        )
    return pd.concat(frames, ignore_index=True)


def run(season: int) -> dict:
    log.info("=== Sportsbook props estimation run starting (season=%d) ===", season)

    props_df = load_props()
    log.info("Loaded %d ingested sportsbook prop rows", len(props_df))

    weekly_df = fetch_nfl_weekly_stats(season)
    log.info("Loaded %d nflverse weekly-stat rows for season %d", len(weekly_df), season)

    result_df = process_props(props_df, weekly_df)

    status_counts = result_df["model_status"].value_counts(dropna=False).to_dict()
    log.info("Model status breakdown: %s", status_counts)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"sportsbook_props_estimates_{timestamp}.csv"
    result_df.to_csv(out_path, index=False)
    log.info("Wrote %d rows to %s", len(result_df), out_path)

    latest_path = OUTPUT_DIR / "sportsbook_props_latest.csv"
    result_df.to_csv(latest_path, index=False)
    log.info("Wrote %d rows to %s", len(result_df), latest_path)

    return {
        "rows_in": len(props_df),
        "rows_out": len(result_df),
        "status_counts": status_counts,
        "output_path": str(out_path),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--season",
        type=int,
        required=True,
        help="NFL season year to pull nflverse weekly stats for (e.g. 2025).",
    )
    args = parser.parse_args()
    summary = run(args.season)
    print(summary)
