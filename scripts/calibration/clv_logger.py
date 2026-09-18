"""
Session 2.4 (pick'em) / Session 4.3 (weather) / Session 5.3 (politics) /
Session 6.3 (sportsbook props) / Session 2.19 (pick'em CLV-at-close fix)
-- CLV-Equivalent Calibration Logging, Generalized Across Tracks

SESSION 2.19 FIX -- THE TAUTOLOGICAL PICK'EM CLV-AT-CLOSE METRIC
-----------------------------------------------------------------------
Checked live, 2026-09-14: every one of PrizePicks' closed flags in
data/pickem/clv_log.csv showed clv_edge_at_close byte-identical to
first_flagged_edge, because closing_implied_prob for PrizePicks is
always PRIZEPICKS_ASSUMED_IMPLIED_PROB -- a flat, unverified constant
(0.5) that pickem_model.py assigns to every PrizePicks row regardless of
the real line, not something derived from a real, moving market price.
A flag can only be created above the flag-edge threshold in the first
place, so every closed PrizePicks flag was mathematically guaranteed to
show a "positive" CLV at close. That is a tautology, not evidence the
model is any good. PrizePicks does not publish a per-side price that
could move, so there is no fix that makes this number real -- Session
2.19's decision is to report it as not-available (None) for PrizePicks
going forward, leaning on Session 2.18's real-outcome grading as this
platform's real validation signal instead. See process_run_pickem()
below for the exact fix and the second, independent bug found alongside
it (line_moved was comparing the wrong field for Underdog).

SESSION 6.3 ADDITION -- SPORTSBOOK PLAYER PROPS (DK/FD)
-----------------------------------------------------------------------
Adds a --track props path, reusing the generic (weather/politics) engine
rather than pick'em's own dedicated functions, but with pick'em's
cross-ROW consensus search (not politics' same-row lookup), since DK and
FD props for the same real player/stat/game live in different rows of
Session 6.2's combined `sportsbook_props_latest.csv`, exactly like
pick'em's cross-platform case. Match key is (normalized player_name,
resolved_stat_key, game_id) -- the same three-part key pick'em already
uses, imported by pattern, not by code (props' key uses game_id directly
from the ingested row, pick'em's uses the same field name).

WHAT COUNTS AS THE "SHARP-BOOK BENCHMARK" HERE (this track's ROADMAP.md
validation item asks for this explicitly): Session 6.1/6.2 only ingest
DraftKings and FanDuel -- neither is a sharp book (e.g. Pinnacle), and no
sharp-book feed exists anywhere in this project yet. So "real sharp-book
benchmark... where available" is met the same honest way pick'em's own
Session 2.4 handled the same gap: the OTHER book's own no-vig price on the
same real prop, when both books carry it, is logged as consensus_price
(consensus_label names which book: "draftkings" or "fanduel") -- the
closest real two-source benchmark this project's actual ingested data can
produce today. This is explicitly NOT a Pinnacle-style sharp line; that
remains a stated, named gap, not something this script pretends to solve.
A row whose OWN estimate is already the de-vigged two-sided probability
(FanDuel player_performance rows) additionally carries a real analogue to
CLV's classic "closing line" signal via the shared own-price-movement-to-
close mechanism every track's generic engine already provides -- a prop
that drops out of a later ingestion run has closed/settled/come off the
board, and its last-seen price is frozen as closing_market_price, same as
weather and politics.

WHY THE ONE-SIDED DK TD-SCORER ROWS ARE INCLUDED, NOT EXCLUDED
-----------------------------------------------------------------------
Session 6.2 already flags DK's one-sided rows with
implied_prob_includes_field_vig=True rather than silently treating the raw
price as vig-free. That flag is carried straight through into this
track's log as an extra column (see PROPS_EXTRA_COLUMNS) so a later
session reviewing CLV results can filter it out or weight it differently,
rather than this script either dropping those rows (losing real flagged
opportunities) or quietly mixing a vig-inflated edge in with a clean
de-vigged one.

USAGE (props)
-------------
python clv_logger.py --track props

===========================================================================
ORIGINAL (Session 2.4 / 4.3 / 5.3) MODULE DOCSTRING CONTINUES BELOW
===========================================================================

WHAT CHANGED THIS SESSION (5.3) AND WHY
-----------------------------------------------------------------------
This script started (Session 2.4) as a pick'em-only tool. ROADMAP.md's
Session 4.3 card ("CLV Logging Hook-In" for the weather track) was
opened in parallel with Session 4.2 but never actually built -- the
version of this file on GitHub going into Session 5.3 was still exactly
the Session 2.4 pick'em-only version, with no track parameter at all.
That gap was found and flagged at the start of this session, and the
user chose to close both Session 4.3 and Session 5.3 together rather
than build a second politics-only patch on top of a file that still
didn't generalize.

This version adds a --track {pickem, weather, politics} argument. The
pick'em code path (functions with a _pickem suffix, plus
CLV_LOG_COLUMNS_PICKEM) is UNCHANGED from the Session 2.4 version --
same file (data/pickem/clv_log.csv), same columns, same logic, same
snapshot behavior. This is a deliberate, non-negotiable choice: Track
1's GitHub Actions automation (Session 2.7) and Cloudflare Pages
frontend (Session 2.8) already read that file's existing schema in
production. Nothing about this session's work touches that path.

Weather and politics get their own new code paths and their own log
files (data/weather/clv_log.csv, data/politics/clv_log.csv), sharing a
common CORE column set (flag_id, track, flagged_side, first/last-seen
values, status, closing values -- see CLV_CORE_COLUMNS) plus a
track-specific set of identity/context columns appended after it (see
WEATHER_EXTRA_COLUMNS / POLITICS_EXTRA_COLUMNS). This is what "shared
CLV structure" means in this script: one shared lifecycle engine
(generic_process_run, below) and one shared set of core columns that
every track's log carries -- not one single physical file mixing three
structurally different market types together, and not three fully
independent copies of the open/refresh/close bookkeeping logic either.

WHY WEATHER AND POLITICS DON'T REUSE PICK'EM'S OWN FUNCTIONS DIRECTLY
-----------------------------------------------------------------------
Pick'em's consensus benchmark requires a real search across OTHER rows
in the same file (the same prop, on the other platform, may be a
different row). Politics does not need that search -- Session 5.2's
politics_estimates_latest.csv is already wide-format, with both venues'
prices for the same race/party sitting in the SAME row -- so its
consensus benchmark is a same-row lookup, not a cross-row search.
Weather has no second venue at all (Kalshi only), so it has no
consensus benchmark. Forcing all three into pick'em's exact
cross-row-search shape would have meant writing fake search logic for
tracks that don't need it. Instead, each track gets its own
`build_<track>_candidates()` / `build_<track>_present_and_prices()` pair
that turns that track's real file into a common, generic shape
(flag_id, side, model_prob, market_price, edge, consensus fields, extra
identity fields) -- and one shared engine (generic_process_run) does
the actual open/refresh/close bookkeeping identically for both.

WEATHER: WHAT COUNTS AS A "FLAG," AND WHAT THE BENCHMARK MEANS
-----------------------------------------------------------------------
Every weather contract is a single yes/no question (Session 4.2's
strike_type/floor_strike/cap_strike). The market's own implied "yes"
probability is the bid/ask midpoint. A flag fires on whichever side
(yes or no) the model's probability clears WEATHER_FLAG_EDGE_THRESHOLD
away from that implied probability -- mirroring pick'em's over/under
mutual-exclusivity (a contract can only be flagged on one side, never
both, since a yes-side edge and a no-side edge are mirror images of the
same gap). There is no cross-venue consensus (Kalshi is the only venue
Session 4.1 ingests), so consensus_available is always False here --
this is a real, stated limitation of the weather track today, not a
bug in this script. The benchmark that DOES apply is the same
own-line-movement-to-close signal pick'em uses: this track's daily
calibration pipeline (Session 4.2) re-pulls Kalshi's weather markets on
a schedule, so a contract that stops appearing in a fresh pull has
settled or been delisted, and its last-seen price is frozen as its
closing value. Per this session's ROADMAP validation item, this
benchmark is meaningful here specifically because weather contracts
resolve in days, not months -- unlike politics below, most weather
flags should reach a real "closed" state within a single validation
window.

POLITICS: WHAT COUNTS AS A "FLAG," AND WHY THIS BENCHMARK IS DIFFERENT
-----------------------------------------------------------------------
Each (race, party, venue) cell is its own independent buy-side
question -- unlike pick'em/weather's single mirrored contract, a race's
Dem and Rep cells are two separate markets that need not sum to 1, so
each is evaluated for its own edge independently, using the edge
Session 5.2's politics_model.py already computed
(`{venue}_edge_vs_raw_{party}`). flag_id is `venue|race_id|party` --
stable for the life of the race, not tied to a specific market ticker,
since Session 5.2's own output does not carry per-venue ticker IDs
forward (see Open Decision logged at the end of this docstring).
Consensus here is the OTHER venue's own raw price on the SAME race and
party, read directly from the same row -- the closest real two-venue
read this project has, same idea as pick'em's cross-platform check, but
a same-row lookup instead of a cross-row search.

ROADMAP.md's own validation item for this session asks explicitly
whether the logged benchmark is "meaningful pre-resolution, not just a
placeholder" for this specific track, because down-ballot races resolve
on a single date (2026-11-03) two months out, not hours or days away.
Two real, distinct answers apply here, not one:
1. The CONSENSUS benchmark (other venue's price on the same race) is
real and meaningful from day one -- it does not depend on time to
resolution at all, and both stated re-verification and Session 5.2's
own methodology treat it as informative immediately.
2. The CLOSING benchmark (own-line movement to close, via
disappearance from the latest file) will mostly sit "open" for
weeks, since these races will not disappear from the feed until
Election Day or a race being called early. That is expected, not a
bug -- it is the same real, stated shape Session 5.4 (Sizing
Adaptation) is built to handle (capital tied up for weeks/months,
not hours/days), not something this session should try to solve.

A REAL, NAMED GOTCHA THIS SCRIPT DOES NOT SILENTLY WORK AROUND:
PRICE SCALE
-----------------------------------------------------------------------
Kalshi's raw API typically returns bid/ask prices as whole cents (0 to
100), not as a 0-to-1 probability. Neither weather_model.py nor
politics_model.py documents scaling its own bid/ask inputs before
using them as a probability. This script defends against that
ambiguity with `_normalize_price()`: any value greater than 1 is
treated as a 0-100 scale and divided by 100; anything already in [0, 1]
is passed through unchanged. This is a real, stated assumption, not a
verified fact -- flagged here as Open Decision #42 (see SESSION_LOG.md)
for confirmation against real live data, the same way every other
placeholder constant in this project is confirmed against real data
before being trusted.

USAGE
-----
pip install pandas numpy --break-system-packages
python clv_logger.py --track pickem --estimates path/to/pickem_estimates_TIMESTAMP.csv
python clv_logger.py --track weather
python clv_logger.py --track politics
If --estimates is omitted, the most recently written *_latest.csv (or,
for pick'em, the most recent timestamped file) for that track is used
automatically.
"""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

ESTIMATION_DIR = BASE_DIR / "output" / "estimation"
CLV_LOG_PATH_PICKEM = BASE_DIR / "data" / "pickem" / "clv_log.csv"
CLV_SNAPSHOT_DIR_PICKEM = BASE_DIR / "data" / "pickem" / "clv_snapshots"

WEATHER_ESTIMATES_LATEST = BASE_DIR / "data" / "weather" / "estimates" / "weather_estimates_latest.csv"
CLV_LOG_PATH_WEATHER = BASE_DIR / "data" / "weather" / "clv_log.csv"
CLV_SNAPSHOT_DIR_WEATHER = BASE_DIR / "data" / "weather" / "clv_snapshots"

POLITICS_ESTIMATES_LATEST = BASE_DIR / "data" / "politics" / "estimates" / "politics_estimates_latest.csv"
CLV_LOG_PATH_POLITICS = BASE_DIR / "data" / "politics" / "clv_log.csv"
CLV_SNAPSHOT_DIR_POLITICS = BASE_DIR / "data" / "politics" / "clv_snapshots"

PROPS_ESTIMATES_LATEST = BASE_DIR / "output" / "estimation" / "sportsbook_props_latest.csv"
CLV_LOG_PATH_PROPS = BASE_DIR / "data" / "sportsbook_props" / "clv_log.csv"
CLV_SNAPSHOT_DIR_PROPS = BASE_DIR / "data" / "sportsbook_props" / "clv_snapshots"

LOG_PATH = BASE_DIR / "logs" / "clv_logging.log"

# ---------------------------------------------------------------------------
# Constants -- named explicitly, per this project's "no unnamed black-box
# factors" documentation standard. See module docstring for full reasoning.
# ---------------------------------------------------------------------------
FLAG_EDGE_THRESHOLD_PICKEM = 0.03   # unchanged from Session 2.4 -- stated, unvalidated placeholder
WEATHER_FLAG_EDGE_THRESHOLD = 0.03  # same placeholder logic, applied to this track -- unvalidated
POLITICS_FLAG_EDGE_THRESHOLD = 0.03  # same placeholder logic, applied to this track -- unvalidated
PROPS_FLAG_EDGE_THRESHOLD = 0.03    # same placeholder logic, applied to this track -- unvalidated

# ---------------------------------------------------------------------------
# Shared (core) CLV log columns -- every track's log carries these.
# ---------------------------------------------------------------------------
CLV_CORE_COLUMNS = [
    "flag_id",
    "track",
    "flagged_side",
    "first_flagged_at",
    "first_flagged_model_prob",
    "first_flagged_market_price",
    "first_flagged_edge",
    "consensus_available",
    "consensus_label",
    "consensus_price",
    "consensus_edge",
    "last_seen_at",
    "last_seen_market_price",
    "status",
    "closing_market_price",
    "closing_pulled_at",
    "price_moved",
    "clv_edge_at_close",
]

# Pick'em keeps its exact, unchanged Session 2.4 schema (own file, own
# columns) -- listed here only so load/save helpers can validate against it.
# FIX (2026-09-11): "team" (the player's own team name) replaced with
# "game_matchup" (the game's "Away @ Home" string) -- see schema.py's own
# docstring for why; ingest_pickem.py's normalized rows no longer carry a
# "team" field at all.
CLV_LOG_COLUMNS_PICKEM = [
    "flag_id", "platform", "source_line_id", "player_name", "game_matchup", "sport",
    "stat_type", "resolved_stat_key",
    # SESSION 2.32 -- real-time MLB starter/lineup confirmation signal
    # (see pickem_model.py's compute_mlb_starter_status() and ROADMAP.md
    # Session 2.32). Carried straight through from the estimates file, same
    # as resolved_stat_key -- this file does not compute it. Always None
    # for every non-MLB or non-Underdog row (additive only, no other
    # column's meaning changed).
    "mlb_starter_status", "nfl_injury_status", "odds_type", "allowed_wager_types", "game_id", "game_start_time",
    "flagged_side", "first_flagged_at", "first_flagged_line",
    "first_flagged_model_prob", "first_flagged_implied_prob", "first_flagged_edge",
    "consensus_available", "consensus_platform", "consensus_source_line_id",
    "consensus_line", "consensus_implied_prob_same_side", "consensus_edge",
    "last_seen_at", "last_seen_line", "last_seen_implied_prob", "status",
    "closing_line", "closing_implied_prob", "closing_pulled_at", "line_moved",
    "clv_edge_at_close",
]

WEATHER_EXTRA_COLUMNS = [
    "series_ticker", "city_label", "station_id", "target_date", "strike_type",
    "floor_strike", "cap_strike", "forecast_kind", "forecast_value_f",
    "lead_days", "model_sigma_f", "sigma_source",
]
CLV_LOG_COLUMNS_WEATHER = CLV_CORE_COLUMNS + WEATHER_EXTRA_COLUMNS

POLITICS_EXTRA_COLUMNS = [
    "venue", "race_id", "party", "tier", "state", "chamber", "district",
    "candidate_name", "hours_to_resolution", "electindex_prob",
    "edge_vs_electindex",
]
CLV_LOG_COLUMNS_POLITICS = CLV_CORE_COLUMNS + POLITICS_EXTRA_COLUMNS

PROPS_EXTRA_COLUMNS = [
    "platform", "source_event_id", "source_market_id", "source_selection_id",
    "player_name", "team", "sport", "stat_type", "prop_category",
    "resolved_stat_key", "line", "game_id", "game_start_time",
    "implied_prob_includes_field_vig",
    # Real American odds as the book itself quotes them, carried straight
    # through from the estimates file (over_american_odds/under_american_odds
    # already exist there -- see sportsbook_props_model.py's output columns)
    # -- added 2026-09-10 so the frontend can show the real quoted odds
    # instead of only an implied-probability price.
    "over_american_odds", "under_american_odds",
]
CLV_LOG_COLUMNS_PROPS = CLV_CORE_COLUMNS + PROPS_EXTRA_COLUMNS


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("clv_logger")
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


def _normalize_price(value) -> Optional[float]:
    """Defends against the real, unconfirmed price-scale ambiguity
    described in the module docstring: treats any value > 1 as a 0-100
    scale (Kalshi's typical raw cents format) and divides by 100;
    passes values already in [0, 1] through unchanged. Returns None for
    missing/unparseable values -- never guesses a number."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    if f > 1.0:
        return f / 100.0
    return f


def _mid(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is not None and b is not None:
        return (a + b) / 2.0
    return a if a is not None else b


# ===========================================================================
# PICK'EM TRACK -- Session 2.4 code, UNCHANGED. Own file, own schema.
# ===========================================================================

def find_latest_estimates_file_pickem() -> Path:
    files = sorted(ESTIMATION_DIR.glob("pickem_estimates_*.csv"))
    if not files:
        raise FileNotFoundError(
            f"No pickem_estimates_*.csv files found in {ESTIMATION_DIR}. "
            f"Run scripts/estimation/pickem_model.py first (Session 2.3)."
        )
    return files[-1]


def load_clv_log_pickem() -> pd.DataFrame:
    """Every column is forced to object dtype -- same fix as
    load_clv_log_generic() below (Session 4.3): a column still entirely
    blank after its first run (e.g. consensus_platform, before any
    cross-platform match exists) gets inferred by pandas as float64, and
    a later run writing a real string into that column then raises a
    hard TypeError. Confirmed live against data/pickem/clv_log.csv
    (Open Decision #43): consensus_platform, consensus_source_line_id,
    consensus_line, consensus_implied_prob_same_side, and consensus_edge
    were all still float64 after 6,850 real rows."""
    if CLV_LOG_PATH_PICKEM.exists():
        df = pd.read_csv(CLV_LOG_PATH_PICKEM)
        for col in CLV_LOG_COLUMNS_PICKEM:
            if col not in df.columns:
                df[col] = None
        return df[CLV_LOG_COLUMNS_PICKEM].astype(object).where(
            pd.notna(df[CLV_LOG_COLUMNS_PICKEM]), None
        )
    return pd.DataFrame(columns=CLV_LOG_COLUMNS_PICKEM, dtype=object)


def determine_flagged_side_pickem(row: pd.Series) -> Optional[str]:
    if row.get("model_status") != "estimated":
        return None
    edge_over = row.get("edge_over")
    edge_under = row.get("edge_under")
    if pd.notna(edge_over) and edge_over >= FLAG_EDGE_THRESHOLD_PICKEM:
        return "over"
    if pd.notna(edge_under) and edge_under >= FLAG_EDGE_THRESHOLD_PICKEM:
        return "under"
    return None


def consensus_match_key_pickem(row: pd.Series) -> Optional[str]:
    name = row.get("player_name")
    stat_key = row.get("resolved_stat_key")
    game_id = row.get("game_id")
    if not name or not isinstance(name, str):
        return None
    if not stat_key or not isinstance(stat_key, str):
        return None
    if not game_id or (isinstance(game_id, float) and pd.isna(game_id)):
        return None
    norm_name = " ".join(name.strip().lower().split())
    return f"{norm_name}|{stat_key}|{game_id}"


def implied_prob_same_side_pickem(row: pd.Series, side: str) -> Optional[float]:
    if side == "over":
        return row.get("implied_prob_over")
    return row.get("implied_prob_under")


def build_consensus_index_pickem(estimates_df: pd.DataFrame) -> dict[tuple[str, str], list[int]]:
    index: dict[tuple[str, str], list[int]] = {}
    for idx, row in estimates_df.iterrows():
        key = consensus_match_key_pickem(row)
        if key is None:
            continue
        platform = row.get("platform")
        if not platform:
            continue
        index.setdefault((platform, key), []).append(idx)
    return index


def find_consensus_row_pickem(
    estimates_df: pd.DataFrame,
    index: dict[tuple[str, str], list[int]],
    own_platform: str,
    match_key: str,
) -> Optional[pd.Series]:
    other_platform = "underdog" if own_platform == "prizepicks" else "prizepicks"
    candidates = index.get((other_platform, match_key))
    if not candidates:
        return None
    if len(candidates) > 1:
        log.warning(
            "Multiple consensus candidates found for platform=%s key=%s "
            "(%d matches) -- using the first.",
            other_platform, match_key, len(candidates),
        )
    return estimates_df.loc[candidates[0]]


def _is_scorable_pickem_row(row: pd.Series) -> bool:
    """FIX (2026-09-11): mirrors pickem_model.py's own
    is_scorable_prizepicks_odds_type() -- a PrizePicks Demon/Goblin
    alt-line has no real implied probability in this project's data (see
    that function's docstring) and pickem_model.py marked it
    model_status="unsupported_odds_type" rather than "estimated". Without
    this check, a Demon/Goblin row that was flagged and logged BEFORE that
    fix would still show up in `present_flag_ids` below (it's still a real,
    live PrizePicks line) and keep getting refreshed as "open" forever,
    even though it can never be newly flagged again -- exactly the stuck,
    stale-looking flags found live in data/pickem/clv_log.csv (e.g.
    Edgerrin Cooper/Karl Brooks Sacks at a Demon 1.5 line, Jordan Mason
    Receiving Yards at a Demon 19.5 line). Treating a non-scorable row as
    "not present" lets the existing close-on-disappearance logic below
    retire these the same way it would if PrizePicks had stopped returning
    the line altogether.

    SESSION 2.21 FIX (2026-09-14): mirrors pickem_model.py's own
    PRIZEPICKS_SCORABLE_ODDS_TYPES, updated the same session to include
    "demon" and "goblin" now that a real, sourced implied probability
    exists for both (see that module's SESSION 2.21 FIX docstring)."""
    if row.get("platform") != "prizepicks":
        return True
    odds_type = row.get("odds_type")
    if not isinstance(odds_type, str) or not odds_type.strip():
        return True
    return odds_type.strip().lower() in {"standard", "demon", "goblin"}


def _side_is_buyable_pickem(row: pd.Series, side: str) -> bool:
    """SESSION 2.36 FIX (2026-09-16, real finding): mirrors pickem_model.py's
    own prizepicks_side_is_buyable(). Found live: 4 real, currently-open
    Christian Pulisic Shots flags (Demon 7.5/3.5, Goblin 2.5/1.5) were all
    showing flagged_side="under", even though PrizePicks' own real
    allowed_wager_types="over" on every one of those rows -- the Under
    side of a PrizePicks Demon/Goblin line usually does not exist to buy
    at all. These 4 flags were created 2026-09-15, one day BEFORE the
    Session 2.33 fix (which stops a NEW flag from picking a disallowed
    side) landed -- that fix has no retroactive effect on a flag already
    open, since process_run_pickem only ever refreshes an existing flag's
    last_seen_*/mlb_starter_status fields, never its flagged_side. Without
    this, a flag mis-flagged before the fix keeps showing "open" and the
    wrong side forever, since its own source_line_id genuinely is still
    live on PrizePicks -- it would never hit the close-on-disappearance
    path below on that basis alone."""
    if row.get("platform") != "prizepicks":
        return True
    raw = row.get("allowed_wager_types")
    if not isinstance(raw, str) or not raw.strip():
        return True
    restriction = raw.strip().lower()
    if restriction == "over":
        return side == "over"
    if restriction == "under":
        return side == "under"
    return True  # "under_or_over" or any other stated value -- both sides buyable


def process_run_pickem(estimates_df: pd.DataFrame, existing_log: pd.DataFrame, run_pulled_at: str) -> pd.DataFrame:
    log_df = existing_log.copy()
    log_df = log_df.set_index("flag_id", drop=False) if not log_df.empty else log_df

    consensus_index = build_consensus_index_pickem(estimates_df)

    estimates_df = estimates_df.copy()
    estimates_df["_flag_id"] = estimates_df["platform"].astype(str) + "|" + estimates_df["source_line_id"].astype(str)
    scorable_mask = estimates_df.apply(_is_scorable_pickem_row, axis=1)

    # SESSION 2.36 -- an existing flag's own recorded flagged_side can be
    # ruled out by allowed_wager_types even though its source_line_id is
    # still live (see _side_is_buyable_pickem() above). Folding this into
    # present_flag_ids means such a flag is simply not "present" this run
    # -- the same trick _is_scorable_pickem_row already uses -- so the
    # existing close-on-disappearance pass below retires it with no
    # separate closing code path needed. A flag_id with no existing
    # record yet (first time seen) always passes here; its side gets
    # decided fresh by determine_flagged_side_pickem()/prizepicks_side_is_
    # buyable() further down (pickem_model.py), not by this check.
    def _existing_side_still_buyable(row: pd.Series) -> bool:
        flag_id = row["_flag_id"]
        if log_df.empty or flag_id not in log_df.index:
            return True
        existing_side = log_df.loc[flag_id, "flagged_side"]
        if not isinstance(existing_side, str) or not existing_side.strip():
            return True
        return _side_is_buyable_pickem(row, existing_side)

    buyable_mask = estimates_df.apply(_existing_side_still_buyable, axis=1)
    present_flag_ids = set(estimates_df.loc[scorable_mask & buyable_mask, "_flag_id"])

    new_rows = []
    existing_flag_ids = set(log_df["flag_id"]) if not log_df.empty else set()

    for _, row in estimates_df.iterrows():
        side = determine_flagged_side_pickem(row)
        flag_id = row["_flag_id"]
        scorable = _is_scorable_pickem_row(row)

        if flag_id in existing_flag_ids:
            if scorable and flag_id in present_flag_ids:
                log_df.loc[flag_id, "last_seen_at"] = run_pulled_at
                log_df.loc[flag_id, "last_seen_line"] = row.get("line")
                side_for_update = log_df.loc[flag_id, "flagged_side"]
                log_df.loc[flag_id, "last_seen_implied_prob"] = implied_prob_same_side_pickem(row, side_for_update)
                log_df.loc[flag_id, "status"] = "open"
                # SESSION 2.32 -- refresh on every run, not just at first
                # flag: a real lineup can go from "not_yet_confirmed" to
                # "confirmed"/"different_than_expected" as MLB posts it
                # closer to first pitch, and an open flag should show the
                # latest real state, not a stale first-seen snapshot.
                log_df.loc[flag_id, "mlb_starter_status"] = row.get("mlb_starter_status")
                log_df.loc[flag_id, "nfl_injury_status"] = row.get("nfl_injury_status")  # Session 2.45
            # else: leave it alone -- it's not in present_flag_ids (either
            # unsupported_odds_type, or SESSION 2.36's own recorded side
            # is no longer buyable), so the close-on-disappearance pass
            # below will retire it correctly.
            continue

        if side is None or not scorable:
            continue

        match_key = consensus_match_key_pickem(row)
        consensus_row = None
        if match_key is not None:
            consensus_row = find_consensus_row_pickem(estimates_df, consensus_index, row.get("platform"), match_key)

        consensus_available = consensus_row is not None
        consensus_platform = consensus_row.get("platform") if consensus_available else None
        consensus_source_line_id = consensus_row.get("source_line_id") if consensus_available else None
        consensus_line = consensus_row.get("line") if consensus_available else None
        consensus_implied = implied_prob_same_side_pickem(consensus_row, side) if consensus_available else None
        model_prob = row.get("prob_over") if side == "over" else row.get("prob_under")
        consensus_edge = (
            (model_prob - consensus_implied)
            if (consensus_available and model_prob is not None and consensus_implied is not None)
            else None
        )

        own_implied = implied_prob_same_side_pickem(row, side)
        own_edge = row.get("edge_over") if side == "over" else row.get("edge_under")

        new_rows.append({
            "flag_id": flag_id,
            "platform": row.get("platform"),
            "source_line_id": row.get("source_line_id"),
            "player_name": row.get("player_name"),
            "game_matchup": row.get("game_matchup"),
            "sport": row.get("sport"),
            "stat_type": row.get("stat_type"),
            "resolved_stat_key": row.get("resolved_stat_key"),
            "mlb_starter_status": row.get("mlb_starter_status"),  # Session 2.32
            "nfl_injury_status": row.get("nfl_injury_status"),  # Session 2.45
            "odds_type": row.get("odds_type"),
            "allowed_wager_types": row.get("allowed_wager_types"),
            "game_id": row.get("game_id"),
            "game_start_time": row.get("game_start_time"),
            "flagged_side": side,
            "first_flagged_at": run_pulled_at,
            "first_flagged_line": row.get("line"),
            "first_flagged_model_prob": model_prob,
            "first_flagged_implied_prob": own_implied,
            "first_flagged_edge": own_edge,
            "consensus_available": consensus_available,
            "consensus_platform": consensus_platform,
            "consensus_source_line_id": consensus_source_line_id,
            "consensus_line": consensus_line,
            "consensus_implied_prob_same_side": consensus_implied,
            "consensus_edge": consensus_edge,
            "last_seen_at": run_pulled_at,
            "last_seen_line": row.get("line"),
            "last_seen_implied_prob": own_implied,
            "status": "open",
            "closing_line": None,
            "closing_implied_prob": None,
            "closing_pulled_at": None,
            "line_moved": None,
            "clv_edge_at_close": None,
        })

    if new_rows:
        new_df = pd.DataFrame(new_rows).set_index("flag_id", drop=False)
        log_df = pd.concat([log_df, new_df]) if not log_df.empty else new_df

    if not log_df.empty:
        open_mask = log_df["status"] == "open"
        dropped_mask = open_mask & (~log_df["flag_id"].isin(present_flag_ids))
        for flag_id in log_df.loc[dropped_mask, "flag_id"]:
            closing_line = log_df.loc[flag_id, "last_seen_line"]
            closing_implied = log_df.loc[flag_id, "last_seen_implied_prob"]
            first_implied = log_df.loc[flag_id, "first_flagged_implied_prob"]
            first_model_prob = log_df.loc[flag_id, "first_flagged_model_prob"]
            platform = log_df.loc[flag_id, "platform"]
            log_df.loc[flag_id, "status"] = "closed"
            log_df.loc[flag_id, "closing_line"] = closing_line
            log_df.loc[flag_id, "closing_implied_prob"] = closing_implied
            log_df.loc[flag_id, "closing_pulled_at"] = log_df.loc[flag_id, "last_seen_at"]

            # SESSION 2.19 FIX -- see module docstring section "SESSION 2.19"
            # below for the full finding. Two independent bugs lived here:
            #
            # 1. PrizePicks' closing_implied_prob is always
            #    PRIZEPICKS_ASSUMED_IMPLIED_PROB (a flat, constant 0.5 --
            #    pickem_model.py never derives it from a real market price).
            #    That is the SAME constant used to compute first_flagged_edge
            #    in the first place, so clv_edge_at_close for PrizePicks was
            #    mathematically guaranteed to equal first_flagged_edge on
            #    every closed row -- a tautology, not a real validation
            #    signal. There is no fix that makes this number real (
            #    PrizePicks does not publish a per-side price that could
            #    move), so it is reported as not-available (None) instead.
            #    Session 2.18's real-outcome grading is the real validation
            #    signal for this platform going forward.
            # 2. `line_moved` compared closing_line vs first_flagged_line --
            #    the point stat threshold (e.g. "74.5 yards"), which platforms
            #    essentially never revise once posted. The real price signal
            #    that clv_edge_at_close is actually computed from is the
            #    IMPLIED PROBABILITY (Underdog: derived from its real,
            #    independently-moving per-side payout multipliers), not the
            #    line. Comparing the wrong field made Underdog's real price
            #    movement look almost nonexistent (0 of 9,885 closed flags
            #    showed line_moved=True, confirmed live 2026-09-14) even
            #    though 1,379 of those same 9,885 rows have a
            #    closing_implied_prob that genuinely differs from
            #    first_flagged_implied_prob. Fixed to compare implied
            #    probability, the field the CLV math actually uses.
            if platform == "prizepicks":
                log_df.loc[flag_id, "line_moved"] = None
                log_df.loc[flag_id, "clv_edge_at_close"] = None
            else:
                log_df.loc[flag_id, "line_moved"] = (
                    bool(pd.notna(closing_implied) and pd.notna(first_implied) and closing_implied != first_implied)
                )
                log_df.loc[flag_id, "clv_edge_at_close"] = (
                    (first_model_prob - closing_implied)
                    if (pd.notna(first_model_prob) and pd.notna(closing_implied))
                    else None
                )

    return log_df.reset_index(drop=True)[CLV_LOG_COLUMNS_PICKEM]


def run_pickem(estimates_path: Optional[Path]) -> dict:
    path = estimates_path or find_latest_estimates_file_pickem()
    estimates_df = pd.read_csv(path)
    log.info("[pickem] Loaded %d estimate rows from %s", len(estimates_df), path)

    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing_log = load_clv_log_pickem()
    log.info("[pickem] Existing CLV log has %d rows before this run", len(existing_log))

    updated_log = process_run_pickem(estimates_df, existing_log, run_pulled_at)

    newly_opened = int((updated_log["first_flagged_at"] == run_pulled_at).sum())
    newly_closed = int(
        ((updated_log["status"] == "closed") & (updated_log["closing_pulled_at"] == run_pulled_at)).sum()
    )
    still_open = int((updated_log["status"] == "open").sum())

    CLV_LOG_PATH_PICKEM.parent.mkdir(parents=True, exist_ok=True)
    updated_log.to_csv(CLV_LOG_PATH_PICKEM, index=False)
    log.info("[pickem] Wrote %d total rows to %s", len(updated_log), CLV_LOG_PATH_PICKEM)

    CLV_SNAPSHOT_DIR_PICKEM.mkdir(parents=True, exist_ok=True)
    snapshot_path = CLV_SNAPSHOT_DIR_PICKEM / f"clv_log_{run_pulled_at.replace(':', '').replace('-', '')}.csv"
    updated_log.to_csv(snapshot_path, index=False)

    return {
        "track": "pickem", "estimates_file": str(path), "rows_in_estimates": len(estimates_df),
        "newly_flagged": newly_opened, "newly_closed": newly_closed, "still_open": still_open,
        "total_logged": len(updated_log), "log_path": str(CLV_LOG_PATH_PICKEM),
    }


# ===========================================================================
# SHARED (GENERIC) ENGINE -- used by weather and politics.
# ===========================================================================

def load_clv_log_generic(path: Path, columns: list[str]) -> pd.DataFrame:
    """Loads an existing track log, or an empty one with the right
    columns if none exists yet. Every column is forced to object dtype
    -- a REAL bug found and fixed during this session's own smoke
    testing: a column that is still entirely blank after its first run
    (e.g. closing_pulled_at, before anything has closed) gets inferred
    by pandas as float64, and a later run's attempt to write a real
    string timestamp into that column then raises a hard TypeError.
    Forcing object dtype on load avoids that entirely, for every
    column, not just the ones this session happened to trip over."""
    if path.exists():
        df = pd.read_csv(path)
        for col in columns:
            if col not in df.columns:
                df[col] = None
        return df[columns].astype(object).where(pd.notna(df[columns]), None)
    return pd.DataFrame(columns=columns, dtype=object)


def generic_process_run(
    track: str,
    candidates: list[dict],
    present_ids: set[str],
    price_for_side_fn,
    existing_log: pd.DataFrame,
    run_pulled_at: str,
    columns: list[str],
    extra_columns: list[str],
    odds_for_side_fn=None,
) -> pd.DataFrame:
    """Generic open/refresh/close lifecycle, shared by weather and
    politics. `candidates` is the list of newly-flagged rows this run
    (already filtered to those clearing that track's edge threshold, one
    dict per flag, using the canonical core keys plus that track's own
    extra_columns keys). `present_ids` is every flag_id seen in this
    run's raw file, flagged or not -- used to detect a flag that has
    dropped out of the feed entirely (settled/delisted/race called), the
    same 'disappearance = closed' signal pick'em's own engine uses.
    `price_for_side_fn(flag_id, flagged_side) -> Optional[float]` gives
    this run's own current market price for an ALREADY-OPEN flag, on the
    side it was originally flagged on -- used to refresh
    last_seen_market_price even when a flag isn't newly created this
    run. It is a function, not a flat dict, because a raw row's own
    'yes' price (weather) needs converting to a 'no' price when that is
    the side the flag was originally logged on -- see the per-track
    build_*_present_and_prices() helpers below. `odds_for_side_fn(flag_id,
    side) -> (over_odds, under_odds)`, props-only (None for every other
    track): refreshes the log's own over_american_odds/under_american_odds
    display columns on each run so the frontend's Odds column always shows
    the platform's current line, not the price at first-flag time --
    first_flagged_market_price/first_flagged_edge already preserve that
    original snapshot for real CLV grading, so this does not touch CLV
    math, only display."""
    log_df = existing_log.copy()
    log_df = log_df.set_index("flag_id", drop=False) if not log_df.empty else log_df
    existing_flag_ids_before_this_run = set(log_df["flag_id"]) if not log_df.empty else set()

    new_rows = []
    for cand in candidates:
        flag_id = cand["flag_id"]
        if flag_id in existing_flag_ids_before_this_run:
            continue  # already logged from a prior run -- refreshed below, not re-created
        row = {col: None for col in columns}
        row.update({
            "flag_id": flag_id,
            "track": track,
            "flagged_side": cand.get("flagged_side"),
            "first_flagged_at": run_pulled_at,
            "first_flagged_model_prob": cand.get("model_prob"),
            "first_flagged_market_price": cand.get("market_price"),
            "first_flagged_edge": cand.get("edge"),
            "consensus_available": cand.get("consensus_available", False),
            "consensus_label": cand.get("consensus_label"),
            "consensus_price": cand.get("consensus_price"),
            "consensus_edge": cand.get("consensus_edge"),
            "last_seen_at": run_pulled_at,
            "last_seen_market_price": cand.get("market_price"),
            "status": "open",
            "closing_market_price": None,
            "closing_pulled_at": None,
            "price_moved": None,
            "clv_edge_at_close": None,
        })
        for col in extra_columns:
            if col in cand:
                row[col] = cand[col]
        new_rows.append(row)

    if new_rows:
        new_df = pd.DataFrame(new_rows).set_index("flag_id", drop=False)
        log_df = pd.concat([log_df, new_df]) if not log_df.empty else new_df

    if not log_df.empty:
        # Refresh: any OPEN flag that existed BEFORE this run (not one
        # just created above) and is still present in this run's raw
        # file gets its last_seen values updated, matching pick'em's own
        # "already logged -- refresh only" branch. Newly-created rows
        # above already carry this run's correct values and are left
        # alone here.
        open_mask = log_df["status"] == "open"
        refresh_mask = open_mask & log_df["flag_id"].isin(existing_flag_ids_before_this_run)
        for flag_id in log_df.loc[refresh_mask, "flag_id"]:
            if flag_id in present_ids:
                log_df.loc[flag_id, "last_seen_at"] = run_pulled_at
                side = log_df.loc[flag_id, "flagged_side"]
                price = price_for_side_fn(flag_id, side)
                if price is not None:
                    log_df.loc[flag_id, "last_seen_market_price"] = price
                if odds_for_side_fn is not None:
                    over_odds, under_odds = odds_for_side_fn(flag_id, side)
                    if over_odds is not None:
                        log_df.loc[flag_id, "over_american_odds"] = over_odds
                    if under_odds is not None:
                        log_df.loc[flag_id, "under_american_odds"] = under_odds

        # Close: any OPEN flag no longer present in this run's raw file
        # at all -- settled, delisted, or (politics) the race dropped
        # from the feed.
        dropped_mask = open_mask & (~log_df["flag_id"].isin(present_ids))
        for flag_id in log_df.loc[dropped_mask, "flag_id"]:
            closing_price = log_df.loc[flag_id, "last_seen_market_price"]
            first_price = log_df.loc[flag_id, "first_flagged_market_price"]
            first_model_prob = log_df.loc[flag_id, "first_flagged_model_prob"]
            log_df.loc[flag_id, "status"] = "closed"
            log_df.loc[flag_id, "closing_market_price"] = closing_price
            log_df.loc[flag_id, "closing_pulled_at"] = log_df.loc[flag_id, "last_seen_at"]
            log_df.loc[flag_id, "price_moved"] = (
                bool(pd.notna(closing_price) and pd.notna(first_price) and closing_price != first_price)
            )
            log_df.loc[flag_id, "clv_edge_at_close"] = (
                (first_model_prob - closing_price)
                if (pd.notna(first_model_prob) and pd.notna(closing_price))
                else None
            )

    return log_df.reset_index(drop=True)[columns]


# ===========================================================================
# WEATHER TRACK (Session 4.3)
# ===========================================================================

def build_weather_candidates(df: pd.DataFrame) -> list[dict]:
    candidates = []
    for _, row in df.iterrows():
        if row.get("model_status") != "estimated":
            continue
        model_prob_yes = row.get("model_prob_yes")
        implied_yes = _normalize_price(_mid(row.get("yes_bid"), row.get("yes_ask")))
        if pd.isna(model_prob_yes) or implied_yes is None:
            continue
        model_prob_yes = float(model_prob_yes)
        edge_yes = model_prob_yes - implied_yes
        if edge_yes >= WEATHER_FLAG_EDGE_THRESHOLD:
            side, model_prob, market_price, edge = "yes", model_prob_yes, implied_yes, edge_yes
        elif -edge_yes >= WEATHER_FLAG_EDGE_THRESHOLD:
            side, model_prob, market_price, edge = "no", 1.0 - model_prob_yes, 1.0 - implied_yes, -edge_yes
        else:
            continue

        candidates.append({
            "flag_id": row.get("market_ticker"),
            "flagged_side": side,
            "model_prob": round(model_prob, 4),
            "market_price": round(market_price, 4),
            "edge": round(edge, 4),
            "consensus_available": False,  # real, stated limitation -- Kalshi is the only venue ingested
            "consensus_label": None,
            "consensus_price": None,
            "consensus_edge": None,
            "series_ticker": row.get("series_ticker"),
            "city_label": row.get("city_label"),
            "station_id": row.get("station_id"),
            "target_date": row.get("target_date"),
            "strike_type": row.get("strike_type"),
            "floor_strike": row.get("floor_strike"),
            "cap_strike": row.get("cap_strike"),
            "forecast_kind": row.get("forecast_kind"),
            "forecast_value_f": row.get("forecast_value_f"),
            "lead_days": row.get("lead_days"),
            "model_sigma_f": row.get("model_sigma_f"),
            "sigma_source": row.get("sigma_source"),
        })
    return candidates


def build_weather_present_and_prices(df: pd.DataFrame) -> tuple[set[str], dict]:
    """Returns (present_ids, yes_price_by_ticker). yes_price_by_ticker
    holds the raw 'yes' side implied price -- callers wanting the 'no'
    side price must convert it (1 - yes_price), since a flag logged on
    the 'no' side needs its own-side price refreshed, not the 'yes'
    side's. See price_for_side_weather() below."""
    present_ids = set()
    yes_prices: dict[str, Optional[float]] = {}
    for _, row in df.iterrows():
        ticker = row.get("market_ticker")
        if not ticker or (isinstance(ticker, float) and pd.isna(ticker)):
            continue
        present_ids.add(ticker)
        yes_prices[ticker] = _normalize_price(_mid(row.get("yes_bid"), row.get("yes_ask")))
    return present_ids, yes_prices


def price_for_side_weather(yes_prices: dict) -> "callable":
    def _fn(flag_id: str, side: str) -> Optional[float]:
        yes_price = yes_prices.get(flag_id)
        if yes_price is None:
            return None
        return yes_price if side == "yes" else (1.0 - yes_price)
    return _fn


def find_latest_estimates_file_weather() -> Path:
    if WEATHER_ESTIMATES_LATEST.exists():
        return WEATHER_ESTIMATES_LATEST
    raise FileNotFoundError(
        f"{WEATHER_ESTIMATES_LATEST} does not exist -- run "
        f"scripts/estimation/weather_model.py first (Session 4.2)."
    )


def run_weather(estimates_path: Optional[Path]) -> dict:
    path = estimates_path or find_latest_estimates_file_weather()
    estimates_df = pd.read_csv(path)
    log.info("[weather] Loaded %d estimate rows from %s", len(estimates_df), path)

    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing_log = load_clv_log_generic(CLV_LOG_PATH_WEATHER, CLV_LOG_COLUMNS_WEATHER)
    log.info("[weather] Existing CLV log has %d rows before this run", len(existing_log))

    candidates = build_weather_candidates(estimates_df)
    present_ids, yes_prices = build_weather_present_and_prices(estimates_df)

    updated_log = generic_process_run(
        "weather", candidates, present_ids, price_for_side_weather(yes_prices), existing_log, run_pulled_at,
        CLV_LOG_COLUMNS_WEATHER, WEATHER_EXTRA_COLUMNS,
    )

    newly_opened = int((updated_log["first_flagged_at"] == run_pulled_at).sum())
    newly_closed = int(
        ((updated_log["status"] == "closed") & (updated_log["closing_pulled_at"] == run_pulled_at)).sum()
    )
    still_open = int((updated_log["status"] == "open").sum())

    CLV_LOG_PATH_WEATHER.parent.mkdir(parents=True, exist_ok=True)
    updated_log.to_csv(CLV_LOG_PATH_WEATHER, index=False)
    log.info("[weather] Wrote %d total rows to %s", len(updated_log), CLV_LOG_PATH_WEATHER)

    CLV_SNAPSHOT_DIR_WEATHER.mkdir(parents=True, exist_ok=True)
    snapshot_path = CLV_SNAPSHOT_DIR_WEATHER / f"clv_log_{run_pulled_at.replace(':', '').replace('-', '')}.csv"
    updated_log.to_csv(snapshot_path, index=False)

    return {
        "track": "weather", "estimates_file": str(path), "rows_in_estimates": len(estimates_df),
        "newly_flagged": newly_opened, "newly_closed": newly_closed, "still_open": still_open,
        "total_logged": len(updated_log), "log_path": str(CLV_LOG_PATH_WEATHER),
    }


# ===========================================================================
# POLITICS TRACK (Session 5.3)
# ===========================================================================

def build_politics_candidates(df: pd.DataFrame) -> list[dict]:
    candidates = []
    for _, row in df.iterrows():
        race_id = row.get("race_id")
        party = row.get("party")
        if not race_id or not party:
            continue
        for venue, other_venue in (("kalshi", "polymarket"), ("polymarket", "kalshi")):
            status_col = f"{venue}_model_status_{str(party).lower()}"
            if row.get(status_col) != "estimated":
                continue
            model_prob = row.get(f"{venue}_corrected_prob_{str(party).lower()}")
            market_price = row.get(f"{venue}_raw_price_{str(party).lower()}")
            edge = row.get(f"{venue}_edge_vs_raw_{str(party).lower()}")
            if pd.isna(model_prob) or pd.isna(market_price) or pd.isna(edge):
                continue
            if edge < POLITICS_FLAG_EDGE_THRESHOLD:
                continue  # only a real, positive mispricing counts as a flag -- no short/fade flags yet

            other_status_col = f"{other_venue}_model_status_{str(party).lower()}"
            consensus_available = row.get(other_status_col) == "estimated"
            consensus_price = row.get(f"{other_venue}_raw_price_{str(party).lower()}") if consensus_available else None
            consensus_edge = (
                round(float(model_prob) - float(consensus_price), 4)
                if consensus_available and pd.notna(consensus_price) else None
            )

            candidates.append({
                "flag_id": f"{venue}|{race_id}|{party}",
                "flagged_side": str(party).lower(),
                "model_prob": round(float(model_prob), 4),
                "market_price": round(float(market_price), 4),
                "edge": round(float(edge), 4),
                "consensus_available": bool(consensus_available),
                "consensus_label": other_venue if consensus_available else None,
                "consensus_price": round(float(consensus_price), 4) if consensus_available and pd.notna(consensus_price) else None,
                "consensus_edge": consensus_edge,
                "venue": venue,
                "race_id": race_id,
                "party": party,
                "tier": row.get("tier"),
                "state": row.get("state"),
                "chamber": row.get("chamber"),
                "district": row.get("district"),
                "candidate_name": row.get("candidate_name"),
                "hours_to_resolution": row.get("hours_to_resolution"),
                "electindex_prob": row.get("electindex_prob"),
                "edge_vs_electindex": row.get(f"{venue}_edge_vs_electindex_{str(party).lower()}"),
            })
    return candidates


def build_politics_present_and_prices(df: pd.DataFrame) -> tuple[set[str], dict[str, Optional[float]]]:
    """Returns (present_ids, price_by_flag_id). Unlike weather, a
    politics flag_id already encodes its own side (the party), so the
    price lookup needs no side conversion -- price_for_side_politics()
    below just ignores the side argument and reads this dict directly."""
    present_ids = set()
    prices: dict[str, Optional[float]] = {}
    for _, row in df.iterrows():
        race_id = row.get("race_id")
        party = row.get("party")
        if not race_id or not party:
            continue
        for venue in ("kalshi", "polymarket"):
            price = row.get(f"{venue}_raw_price_{str(party).lower()}")
            if pd.isna(price):
                continue
            flag_id = f"{venue}|{race_id}|{party}"
            present_ids.add(flag_id)
            prices[flag_id] = float(price)
    return present_ids, prices


def price_for_side_politics(prices: dict) -> "callable":
    def _fn(flag_id: str, side: str) -> Optional[float]:  # side unused -- see docstring above
        return prices.get(flag_id)
    return _fn


def find_latest_estimates_file_politics() -> Path:
    if POLITICS_ESTIMATES_LATEST.exists():
        return POLITICS_ESTIMATES_LATEST
    raise FileNotFoundError(
        f"{POLITICS_ESTIMATES_LATEST} does not exist -- run "
        f"scripts/estimation/politics_model.py first (Session 5.2)."
    )


def run_politics(estimates_path: Optional[Path]) -> dict:
    path = estimates_path or find_latest_estimates_file_politics()
    estimates_df = pd.read_csv(path)
    log.info("[politics] Loaded %d estimate rows from %s", len(estimates_df), path)

    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing_log = load_clv_log_generic(CLV_LOG_PATH_POLITICS, CLV_LOG_COLUMNS_POLITICS)
    log.info("[politics] Existing CLV log has %d rows before this run", len(existing_log))

    candidates = build_politics_candidates(estimates_df)
    present_ids, prices = build_politics_present_and_prices(estimates_df)

    updated_log = generic_process_run(
        "politics", candidates, present_ids, price_for_side_politics(prices), existing_log, run_pulled_at,
        CLV_LOG_COLUMNS_POLITICS, POLITICS_EXTRA_COLUMNS,
    )

    newly_opened = int((updated_log["first_flagged_at"] == run_pulled_at).sum())
    newly_closed = int(
        ((updated_log["status"] == "closed") & (updated_log["closing_pulled_at"] == run_pulled_at)).sum()
    )
    still_open = int((updated_log["status"] == "open").sum())

    CLV_LOG_PATH_POLITICS.parent.mkdir(parents=True, exist_ok=True)
    updated_log.to_csv(CLV_LOG_PATH_POLITICS, index=False)
    log.info("[politics] Wrote %d total rows to %s", len(updated_log), CLV_LOG_PATH_POLITICS)

    CLV_SNAPSHOT_DIR_POLITICS.mkdir(parents=True, exist_ok=True)
    snapshot_path = CLV_SNAPSHOT_DIR_POLITICS / f"clv_log_{run_pulled_at.replace(':', '').replace('-', '')}.csv"
    updated_log.to_csv(snapshot_path, index=False)

    return {
        "track": "politics", "estimates_file": str(path), "rows_in_estimates": len(estimates_df),
        "newly_flagged": newly_opened, "newly_closed": newly_closed, "still_open": still_open,
        "total_logged": len(updated_log), "log_path": str(CLV_LOG_PATH_POLITICS),
    }


# ===========================================================================
# SPORTSBOOK PROPS TRACK (Session 6.3)
# ===========================================================================

# Session 6.9 (BetMGM CLV hook-in) -- real finding: sportsbook_props_
# model.py gives EVERY TD-scorer-shaped market (Anytime, 2+, First, Last)
# the SAME resolved_stat_key ("rushing_tds+receiving_tds" -- it's the same
# underlying stat, only the probability QUESTION differs). Matching on
# resolved_stat_key alone silently merged three real, different DraftKings
# markets for the same player into one match-key bucket, so a real
# consensus lookup could pick "First TD Scorer" (unsupported, blank
# implied_prob) as a "match" for a BetMGM "Anytime TD Scorer" flag --
# caught by inspecting this session's own first real post-fix run's output
# (consensus_available=True but consensus_price/consensus_edge blank),
# not assumed correct because the flag count looked right. Only TD-shaped
# markets need this extra bucket -- every other real stat already gets a
# distinct resolved_stat_key per real stat (e.g. "passing_yards" vs
# "rushing_yards"), so this map is deliberately narrow, not a general
# stat_type normalizer.
_TD_MARKET_KIND_SYNONYMS = {
    "anytime td scorer": "anytime", "anytd": "anytime",
    "2+ tds": "two_plus", "twotd": "two_plus",
    "first td scorer": "first", "firsttd": "first",
    "last td scorer": "last", "lasttd": "last",
    "3+ tds": "three_plus", "threetd": "three_plus",
}


def _props_market_kind(row) -> Optional[str]:
    resolved_stat_key = row.get("resolved_stat_key")
    if resolved_stat_key != "rushing_tds+receiving_tds":
        return None  # not a TD-composite market -- resolved_stat_key alone already distinguishes it
    raw = str(row.get("stat_type") or "").strip().lower()
    return _TD_MARKET_KIND_SYNONYMS.get(raw, raw)


def _props_match_key(row) -> Optional[str]:
    """Session 6.9 (BetMGM CLV hook-in) -- real finding: this key used to
    include `game_id`, which is each PLATFORM'S OWN internal event id (DK's
    own numbering, Rotowire's own numbering, etc.) -- confirmed directly
    against real data that the SAME real player/game/stat gets two totally
    different game_id values across platforms (e.g. Jahmyr Gibbs' real
    Anytime-TD-Scorer market this week: DraftKings' own id "34118210" vs.
    Rotowire/BetMGM's own id "2978635"). Including it meant cross-platform
    consensus could structurally never match on real data -- confirmed 0
    of 154 real pre-existing DraftKings flags had a consensus match before
    this fix, not a coincidence. Only the earlier synthetic test fixtures
    (which hand the same fake game_id to both platforms) ever exercised
    the matching path. Dropped `game_id` from the key: (player_name,
    resolved_stat_key) alone is a safe real-world match for this track
    because an NFL player has at most one real upcoming game open across
    every ingested platform at any one time -- there is no real ambiguity
    this would introduce for this sport."""
    name = row.get("player_name")
    stat_key = row.get("resolved_stat_key")
    if not name or not isinstance(name, str):
        return None
    if not stat_key or not isinstance(stat_key, str):
        return None
    norm_name = " ".join(name.strip().lower().split())
    market_kind = _props_market_kind(row)
    if market_kind:
        return f"{norm_name}|{stat_key}|{market_kind}"
    return f"{norm_name}|{stat_key}"


def _props_implied_for_side(row, side: str) -> Optional[float]:
    return row.get("implied_prob_over") if side == "over" else row.get("implied_prob_under")


def build_props_consensus_index(df: pd.DataFrame) -> dict[tuple[str, str], list[int]]:
    index: dict[tuple[str, str], list[int]] = {}
    for idx, row in df.iterrows():
        key = _props_match_key(row)
        if key is None:
            continue
        platform = row.get("platform")
        if not platform:
            continue
        index.setdefault((platform, key), []).append(idx)
    return index


def find_props_consensus_row(df: pd.DataFrame, index: dict, own_platform: str, match_key: str) -> Optional[pd.Series]:
    """Session 6.1 originally hardcoded this to a single "the other one of
    two platforms" lookup (draftkings<->fanduel), which is exactly wrong
    now that a third platform (Session 6.9's betmgm, via Rotowire) exists
    in the same pipeline -- that version would never find fanduel<->betmgm
    or draftkings<->betmgm consensus. Generalized here to check EVERY
    other real platform present in the index, not one hardcoded guess."""
    other_platform_keys = {
        platform for (platform, key) in index.keys()
        if key == match_key and platform != own_platform
    }
    candidates: list[int] = []
    for other_platform in sorted(other_platform_keys):
        candidates.extend(index.get((other_platform, match_key), []))
    if not candidates:
        return None
    if len(candidates) > 1:
        log.warning(
            "[props] Multiple consensus candidates for own_platform=%s key=%s (%d matches "
            "across other platform(s)) -- using the first.",
            own_platform, match_key, len(candidates),
        )
    return df.loc[candidates[0]]


def props_flag_id(platform, source_market_id, selection_id) -> Optional[str]:
    """Single source of truth for a props flag's identity, shared by
    build_props_candidates() and build_props_present_and_prices() so the
    two can never drift apart. Must include source_market_id, not just
    source_selection_id: confirmed real 2026-09-10 that BetMGM (via
    Rotowire) reuses the same plain numeric selection_id across DIFFERENT
    real markets for the same player (e.g. Jahmyr Gibbs' real id 16808 is
    both his Anytime TD Scorer market AND his separate rushing+receiving
    yards market) -- platform+selection_id alone silently collapsed two
    real props onto one CLV-log row, each overwriting the other's price/
    status on every refresh. DraftKings/FanDuel's own selection_id is
    already a compound string encoding market identity, so this is not a
    behavior change for them beyond widening (harmlessly) their own
    already-unique flag_id."""
    if not platform or source_market_id is None or selection_id is None:
        return None
    if isinstance(source_market_id, float) and source_market_id != source_market_id:  # NaN
        return None
    return f"{platform}|{source_market_id}|{selection_id}"


def build_props_candidates(df: pd.DataFrame) -> list[dict]:
    """Mirrors pick'em's determine_flagged_side/consensus-search pattern
    (cross-row, not same-row -- see module docstring), but emits the
    generic engine's core+extra dict shape so props can share
    generic_process_run() with weather/politics rather than duplicating
    the open/refresh/close lifecycle a third time."""
    index = build_props_consensus_index(df)
    candidates = []
    for _, row in df.iterrows():
        if row.get("model_status") != "estimated":
            continue
        edge_over = row.get("edge_over")
        edge_under = row.get("edge_under")
        if pd.notna(edge_over) and edge_over >= PROPS_FLAG_EDGE_THRESHOLD:
            side, model_prob, market_price, edge = (
                "over", row.get("prob_over"), row.get("implied_prob_over"), edge_over,
            )
        elif pd.notna(edge_under) and edge_under >= PROPS_FLAG_EDGE_THRESHOLD:
            side, model_prob, market_price, edge = (
                "under", row.get("prob_under"), row.get("implied_prob_under"), edge_under,
            )
        else:
            continue

        platform = row.get("platform")
        selection_id = row.get("source_selection_id")
        flag_id = props_flag_id(platform, row.get("source_market_id"), selection_id)
        if flag_id is None:
            continue

        match_key = _props_match_key(row)
        consensus_row = find_props_consensus_row(df, index, platform, match_key) if match_key else None
        consensus_available = consensus_row is not None
        consensus_price = _props_implied_for_side(consensus_row, side) if consensus_available else None
        consensus_edge = (
            round(float(model_prob) - float(consensus_price), 4)
            if (consensus_available and model_prob is not None and pd.notna(consensus_price))
            else None
        )

        candidates.append({
            "flag_id": flag_id,
            "flagged_side": side,
            "model_prob": round(float(model_prob), 4) if model_prob is not None else None,
            "market_price": round(float(market_price), 4) if market_price is not None else None,
            "edge": round(float(edge), 4),
            "consensus_available": bool(consensus_available),
            "consensus_label": consensus_row.get("platform") if consensus_available else None,
            "consensus_price": round(float(consensus_price), 4) if consensus_available and pd.notna(consensus_price) else None,
            "consensus_edge": consensus_edge,
            "platform": platform,
            "source_event_id": row.get("source_event_id"),
            "source_market_id": row.get("source_market_id"),
            "source_selection_id": selection_id,
            "player_name": row.get("player_name"),
            "team": row.get("team"),
            "sport": row.get("sport"),
            "stat_type": row.get("stat_type"),
            "prop_category": row.get("prop_category"),
            "resolved_stat_key": row.get("resolved_stat_key"),
            "line": row.get("line"),
            "game_id": row.get("game_id"),
            "game_start_time": row.get("game_start_time"),
            "implied_prob_includes_field_vig": row.get("implied_prob_includes_field_vig"),
            "over_american_odds": row.get("over_american_odds"),
            "under_american_odds": row.get("under_american_odds"),
        })
    return candidates


def build_props_present_and_prices(df: pd.DataFrame) -> tuple[set[str], dict[str, dict]]:
    """Returns (present_ids, row_by_flag_id) -- row_by_flag_id holds each
    live flag_id's own current over/under implied prices, so
    price_for_side_props() can refresh an already-open flag on whichever
    side it was originally flagged on, same pattern as weather's yes/no
    conversion."""
    present_ids = set()
    rows_by_id: dict[str, dict] = {}
    for _, row in df.iterrows():
        platform = row.get("platform")
        selection_id = row.get("source_selection_id")
        flag_id = props_flag_id(platform, row.get("source_market_id"), selection_id)
        if flag_id is None:
            continue
        present_ids.add(flag_id)
        rows_by_id[flag_id] = {
            "implied_prob_over": row.get("implied_prob_over"),
            "implied_prob_under": row.get("implied_prob_under"),
            "over_american_odds": row.get("over_american_odds"),
            "under_american_odds": row.get("under_american_odds"),
        }
    return present_ids, rows_by_id


def price_for_side_props(rows_by_id: dict) -> "callable":
    def _fn(flag_id: str, side: str) -> Optional[float]:
        row = rows_by_id.get(flag_id)
        if row is None:
            return None
        value = row.get("implied_prob_over") if side == "over" else row.get("implied_prob_under")
        return float(value) if value is not None and value == value else None  # NaN-safe
    return _fn


def odds_for_side_props(rows_by_id: dict) -> "callable":
    """Same shape as price_for_side_props, but returns this run's raw
    American odds for a flag's own side instead of an implied
    probability -- used to refresh over_american_odds/under_american_odds
    on an already-open flag so the frontend's Odds column reflects the
    platform's current line, not the price at first-flag time (which
    first_flagged_market_price/first_flagged_odds already preserve on
    their own, by design, for CLV purposes)."""
    def _fn(flag_id: str, side: str) -> tuple[Optional[float], Optional[float]]:
        row = rows_by_id.get(flag_id)
        if row is None:
            return None, None
        over = row.get("over_american_odds")
        under = row.get("under_american_odds")
        over = float(over) if over is not None and over == over else None
        under = float(under) if under is not None and under == under else None
        return over, under
    return _fn


def find_latest_estimates_file_props() -> Path:
    if PROPS_ESTIMATES_LATEST.exists():
        return PROPS_ESTIMATES_LATEST
    raise FileNotFoundError(
        f"{PROPS_ESTIMATES_LATEST} does not exist -- run "
        f"scripts/estimation/sportsbook_props_model.py first (Session 6.2)."
    )


def run_props(estimates_path: Optional[Path]) -> dict:
    path = estimates_path or find_latest_estimates_file_props()
    estimates_df = pd.read_csv(path)
    log.info("[props] Loaded %d estimate rows from %s", len(estimates_df), path)

    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing_log = load_clv_log_generic(CLV_LOG_PATH_PROPS, CLV_LOG_COLUMNS_PROPS)
    log.info("[props] Existing CLV log has %d rows before this run", len(existing_log))

    candidates = build_props_candidates(estimates_df)
    present_ids, rows_by_id = build_props_present_and_prices(estimates_df)

    updated_log = generic_process_run(
        "props", candidates, present_ids, price_for_side_props(rows_by_id), existing_log, run_pulled_at,
        CLV_LOG_COLUMNS_PROPS, PROPS_EXTRA_COLUMNS,
        odds_for_side_fn=odds_for_side_props(rows_by_id),
    )

    newly_opened = int((updated_log["first_flagged_at"] == run_pulled_at).sum())
    newly_closed = int(
        ((updated_log["status"] == "closed") & (updated_log["closing_pulled_at"] == run_pulled_at)).sum()
    )
    still_open = int((updated_log["status"] == "open").sum())

    CLV_LOG_PATH_PROPS.parent.mkdir(parents=True, exist_ok=True)
    updated_log.to_csv(CLV_LOG_PATH_PROPS, index=False)
    log.info("[props] Wrote %d total rows to %s", len(updated_log), CLV_LOG_PATH_PROPS)

    CLV_SNAPSHOT_DIR_PROPS.mkdir(parents=True, exist_ok=True)
    snapshot_path = CLV_SNAPSHOT_DIR_PROPS / f"clv_log_{run_pulled_at.replace(':', '').replace('-', '')}.csv"
    updated_log.to_csv(snapshot_path, index=False)

    return {
        "track": "props", "estimates_file": str(path), "rows_in_estimates": len(estimates_df),
        "newly_flagged": newly_opened, "newly_closed": newly_closed, "still_open": still_open,
        "total_logged": len(updated_log), "log_path": str(CLV_LOG_PATH_PROPS),
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--track", type=str, default="pickem", choices=["pickem", "weather", "politics", "props"],
        help="Which track's CLV log to update. Defaults to pickem (Session 2.4 behavior, unchanged).",
    )
    parser.add_argument(
        "--estimates", type=str, default=None,
        help="Path to a specific estimates CSV file. Defaults to that track's own latest file.",
    )
    args = parser.parse_args()
    estimates_arg = Path(args.estimates) if args.estimates else None

    log.info("=== CLV logging run starting (track=%s) ===", args.track)
    if args.track == "pickem":
        result = run_pickem(estimates_arg)
    elif args.track == "weather":
        result = run_weather(estimates_arg)
    elif args.track == "politics":
        result = run_politics(estimates_arg)
    else:
        result = run_props(estimates_arg)
    log.info("Run summary: %s", result)
    print(result)
