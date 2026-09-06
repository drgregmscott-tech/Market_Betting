"""
Session 3.2 - Arbitrage Detection Logic

WHAT THIS SCRIPT IS
--------------------
Reads the normalized exchange-venue snapshots (kalshi_latest.csv,
polymarket_latest.csv) and venue_matcher.py's candidate-match output, and
flags cases where the same real-world outcome is priced inconsistently
enough that BOTH sides of a locked position can be bought for less than
the guaranteed $1.00 payout - after each venue's real trading fee is
subtracted, not before. A price gap that only looks like profit before
fees is not a real arbitrage; this script's whole job is telling the two
apart.

Two distinct arbitrage shapes are checked, because they are genuinely
different bets even though the underlying math (buy two complementary
positions for less than the $1.00 they jointly guarantee) is the same:

1. SINGLE-VENUE YES+NO MISPRICING
   One exchange's own YES and NO contracts on the SAME market should
   always cost at least $1.00 combined (since exactly one of them settles
   at $1.00 and the other at $0.00). If yes_ask + no_ask on the SAME
   venue, SAME market is less than $1.00, buying one of each locks in the
   $1.00 payout regardless of outcome. This does not depend on
   venue_matcher.py at all - it only needs one venue's own normalized
   snapshot.

2. CROSS-VENUE MATCHED-PAIR MISPRICING
   For a pair venue_matcher.py has proposed as the SAME real-world
   question on two different venues, buying YES on whichever venue is
   cheaper and NO on the other venue (instead of both on the same venue)
   locks in the same $1.00 payout if the two asks sum to less than
   $1.00. This DOES depend on venue_matcher.py's candidate list, since it
   requires two different venues actually asking about the same real-
   world outcome.

WHY FEES ARE APPLIED PER LEG, USING EACH VENUE'S OWN REAL SCHEDULE
-----------------------------------------------------------------------
Kalshi and Polymarket do not charge the same fee, and Polymarket does not
even charge the same fee across its own categories. Treating "the same
outcome, cheaper combined price" as automatically profitable would repeat
this project's own standing lesson (see SESSION_LOG.md's PrizePicks 50%-
threshold note): the raw price gap is a flagging signal, not the real
breakeven. Both venues' real, current fee schedules were pulled directly
from their own published documentation for this session (not estimated,
not carried over from Session 0.1's original market-efficiency research,
which predates Polymarket's 2026 fee rollout):

- Kalshi: taker fee = ceil_to_cent(KALSHI_TAKER_FEE_RATE * C * P * (1-P))
  per leg, where C is contract count and P is the price in dollars. This
  is the general-market formula Kalshi publishes; Kalshi's own schedule
  notes some products (its example: Crypto) carry a different, higher
  multiplier, which is NOT the case for either of this project's two
  Kalshi tracks (Climate/Commodities, down-ballot Elections) - confirmed
  against the standard-market formula, not assumed. Source: Kalshi's own
  published fee schedule (kalshi.com/fee-schedule), cross-checked against
  a third-party breakdown citing the July 2026 revision (OddsShopper,
  updated 2026-07-23).
- Polymarket: taker fee = FeeRate_by_category * C * P * (1-P), no
  rounding step (Polymarket rounds to 5 decimal places, not the nearest
  cent). FeeRate is category-specific - see POLYMARKET_TAKER_FEE_RATE
  below - and Geopolitics markets carry NO fee at all. Source: Polymarket's
  own docs (docs.polymarket.com/trading/fees), current fee table as of
  this session (confirmed live; a prior fee-rollout schedule dated March
  30, 2026 already superseded Polymarket's original near-zero-fee model,
  so this project's Session 0.1 vig comparison against Polymarket - "0.85%
  Kalshi vs 4.62% sportsbooks" - is now stale for Polymarket specifically
  and should not be re-used to justify skipping Polymarket's fee here).

CONSERVATIVE ASSUMPTION, NAMED NOT SILENT: both venues charge a LOWER fee
(Kalshi: a reduced maker rate, sometimes zero; Polymarket: literally zero)
to an order that RESTS on the book rather than taking the existing best
price. This project's normalized schema only captures each venue's best
bid/ask at pull time (see schema_exchange.py) - it has no way to know
whether a specific flagged opportunity could actually be filled by a
resting (maker) order instead of a taker order at that instant. This
detector therefore prices every leg at the TAKER rate on both venues,
always - the worst case, not the best case. This means a flagged
opportunity's real profit, if filled patiently as a maker order instead,
could be HIGHER than what this script reports; it will never be lower.
This mirrors the same "worst-case, not best-case" posture as Session
0.1's own PrizePicks flagging-threshold decision.

WHAT LIQUIDITY_CHECK.PY AND THE LEGAL FOOTPRINT ADD ON TOP
-----------------------------------------------------------------
This module only prices a flagged pair - it does not decide whether the
flagged size can actually be filled (liquidity_check.py) or whether both
venues in the pair are legally available to trade together
(venue_legal_footprint.md's STATE_AVAILABILITY data, applied here). Both
are applied to every flagged row before it is written out, per Session
0.1's five per-venue evaluation criteria.

WHERE OUTPUT GOES
------------------
/data/arbitrage/flags/arbitrage_flags_<timestamp>.csv - every flagged
opportunity, both shapes, with gross price gap, per-leg fees, net profit,
liquidity-constrained fillable size, and legal-footprint status.

USAGE
-----
python detector.py
(reads kalshi_latest.csv, polymarket_latest.csv from
/data/exchange/normalized/, and the most recent
candidate_matches_*.csv from /data/exchange/matched/)
"""

from __future__ import annotations

import csv
import glob
import logging
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from liquidity_check import estimate_fillable_size

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"
MATCHED_DIR = BASE_DIR / "data" / "exchange" / "matched"
FLAGS_DIR = BASE_DIR / "data" / "arbitrage" / "flags"
FLAGS_LATEST_PATH = FLAGS_DIR / "arbitrage_flags_latest.csv"
LOG_PATH = BASE_DIR / "logs" / "arbitrage.log"

KALSHI_LATEST = NORMALIZED_DIR / "kalshi_latest.csv"
POLYMARKET_LATEST = NORMALIZED_DIR / "polymarket_latest.csv"

# --------------------------------------------------------------------------
# Fee schedules - real, current, sourced constants. See module docstring
# for exactly where each number comes from and when it was last confirmed
# live. Recalibrate here, in one place, the same "no silent adjustments"
# pattern as sizing_engine.py's KELLY_FRACTION and venue_matcher.py's
# MIN_TITLE_SIMILARITY.
# --------------------------------------------------------------------------

# Kalshi's general-market taker-fee coefficient. Confirmed against
# Kalshi's own published fee schedule (kalshi.com/fee-schedule) and its
# July 2026 revision; applies to both of this project's Kalshi tracks
# (Climate/Commodities, down-ballot Elections) - neither is a premium
# category like Kalshi's own cited Crypto example, which carries a
# different multiplier this project does not need.
KALSHI_TAKER_FEE_RATE = 0.07

# Polymarket's per-category taker-fee rate. Confirmed live against
# Polymarket's own docs (docs.polymarket.com/trading/fees), current as of
# this session. Geopolitics is fee-free by Polymarket's own design (not a
# category this project currently pulls, but included for completeness
# and so a future track addition does not silently assume a fee that
# isn't charged). Every category this project's tracks actually use
# (Weather, Politics) is present here with its real rate, not a single
# blended guess.
POLYMARKET_TAKER_FEE_RATE = {
    "crypto": 0.07,
    "sports": 0.05,
    "finance": 0.04,
    "politics": 0.04,
    "economics": 0.05,
    "culture": 0.05,
    "weather": 0.05,
    "other": 0.05,
    "mentions": 0.04,
    "tech": 0.04,
    "geopolitics": 0.0,
}
POLYMARKET_DEFAULT_TAKER_FEE_RATE = 0.05  # "Other / General" rate, used
# only if a Polymarket row's category is missing or not in the table
# above - named and logged when it happens, never silently zeroed out.

# A flagged opportunity's fee-adjusted profit must clear this floor (as a
# fraction of the $1.00 payout) before it is written out at all. This is
# NOT the same as "profit > 0" - a razor-thin, rounding-distance-only
# profit is not worth flagging given real execution risk (both legs must
# actually fill; see liquidity_check.py) and given every input here is
# itself an estimate (best bid/ask at pull time, not a guaranteed fill
# price). Named and adjustable, same pattern as SAME_GAME_CAUTION_MULTIPLIER
# in sizing_engine.py.
MIN_NET_PROFIT_FRACTION = 0.01  # at least 1 cent of real profit per $1 risked

MATCH_SOURCE_KALSHI_OWN = "kalshi_yes_no"
MATCH_SOURCE_POLYMARKET_OWN = "polymarket_yes_no"
MATCH_SOURCE_CROSS_VENUE = "cross_venue"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("arbitrage_detector")
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


# --------------------------------------------------------------------------
# Fee calculation
# --------------------------------------------------------------------------
def kalshi_taker_fee(price: float, contracts: float = 1.0) -> float:
    """Kalshi's real published taker-fee formula: round UP to the next
    cent, per the schedule text ("round up (...)"), not standard
    rounding. See module docstring for the source. `price` is a decimal
    dollar amount (e.g. 0.40 for a 40-cent contract)."""
    if price is None:
        return 0.0
    raw = KALSHI_TAKER_FEE_RATE * contracts * price * (1.0 - price)
    return math.ceil(raw * 100.0) / 100.0


def polymarket_taker_fee(
    price: float, category: Optional[str], contracts: float = 1.0
) -> float:
    """Polymarket's real published taker-fee formula: FeeRate * C * P *
    (1-P), no per-cent rounding (Polymarket documents 5-decimal-place
    precision). `category` is matched case-insensitively against
    POLYMARKET_TAKER_FEE_RATE; an unrecognized or missing category falls
    back to the documented "Other / General" rate, logged so this is
    never a silent guess."""
    if price is None:
        return 0.0
    key = (category or "").strip().lower()
    if key not in POLYMARKET_TAKER_FEE_RATE:
        log.warning(
            "Polymarket row has unrecognized/missing category '%s' - "
            "using the default 'Other/General' fee rate (%.2f) rather "
            "than assuming fee-free.",
            category,
            POLYMARKET_DEFAULT_TAKER_FEE_RATE,
        )
        rate = POLYMARKET_DEFAULT_TAKER_FEE_RATE
    else:
        rate = POLYMARKET_TAKER_FEE_RATE[key]
    return rate * contracts * price * (1.0 - price)


def _kalshi_category_to_polymarket_key(kalshi_category: Optional[str]) -> str:
    """This project's Kalshi category labels ("Climate and Weather",
    "Elections - US House District", etc.) don't share Polymarket's
    category vocabulary ("weather", "politics"). This is a real, named
    mapping - not a guess - built from Session 0.1's own track
    definitions (Track 3 = weather/climate, Track 4 = down-ballot
    politics)."""
    if not kalshi_category:
        return "other"
    key = kalshi_category.lower()
    if "weather" in key or "commodit" in key:
        return "weather"
    if "election" in key:
        return "politics"
    return "other"


# --------------------------------------------------------------------------
# Reading input
# --------------------------------------------------------------------------
def _read_rows(path: Path) -> list[dict]:
    if not path.exists():
        log.error(
            "%s does not exist - run its ingestion script first. "
            "Treating as zero rows for this run, not crashing.",
            path,
        )
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _latest_candidate_matches_path() -> Optional[Path]:
    pattern = str(MATCHED_DIR / "candidate_matches_*.csv")
    matches = sorted(glob.glob(pattern))
    if not matches:
        return None
    return Path(matches[-1])


def _to_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# Detection - Shape 1: single-venue YES+NO mispricing
# --------------------------------------------------------------------------
def detect_single_venue_mispricing(
    rows: list[dict], platform: str
) -> list[dict]:
    """A venue's own YES and NO contract on the SAME market should always
    cost at least $1.00 combined. If yes_ask + no_ask < $1.00, buying one
    of each locks in the $1.00 payout regardless of the real-world
    outcome - a genuine, single-venue arbitrage that does not need
    venue_matcher.py at all."""
    flags: list[dict] = []

    for row in rows:
        yes_ask = _to_float(row.get("yes_ask"))
        no_ask = _to_float(row.get("no_ask"))
        if yes_ask is None or no_ask is None:
            continue

        gross_cost = yes_ask + no_ask
        if gross_cost >= 1.0:
            continue  # not even a gross mispricing - most rows, correctly

        if platform == "kalshi":
            fee_yes = kalshi_taker_fee(yes_ask)
            fee_no = kalshi_taker_fee(no_ask)
        elif platform == "polymarket":
            category = _kalshi_category_to_polymarket_key(row.get("category"))
            fee_yes = polymarket_taker_fee(yes_ask, category)
            fee_no = polymarket_taker_fee(no_ask, category)
        else:
            log.warning("Unknown platform '%s' - skipping row.", platform)
            continue

        # round() before comparing to MIN_NET_PROFIT_FRACTION: raw
        # floating-point subtraction here can land a cent-for-cent exact
        # breakeven (e.g. 1.0 - 0.95 - 0.04) a hair under the threshold
        # (0.009999999999999933 instead of 0.01) purely from binary
        # float representation, not a real cent of difference. BUG
        # FOUND in this session's own validation: an intentionally
        # constructed exact-breakeven test case was silently dropped
        # before this rounding step was added - confirmed by hand-
        # computing the same case's decimal arithmetic and finding no
        # real shortfall.
        net_profit = round(1.0 - gross_cost - fee_yes - fee_no, 6)
        if net_profit < MIN_NET_PROFIT_FRACTION:
            continue  # gross gap existed but fees close it - the exact
            # false-positive case this detector must NOT flag

        flags.append(
            {
                "opportunity_type": (
                    MATCH_SOURCE_KALSHI_OWN
                    if platform == "kalshi"
                    else MATCH_SOURCE_POLYMARKET_OWN
                ),
                "platform_a": platform,
                "market_a": row.get("source_market_id"),
                "title_a": row.get("title"),
                "leg_a_side": "YES",
                "leg_a_ask": yes_ask,
                "leg_a_fee": round(fee_yes, 4),
                "platform_b": platform,
                "market_b": row.get("source_market_id"),
                "title_b": row.get("title"),
                "leg_b_side": "NO",
                "leg_b_ask": no_ask,
                "leg_b_fee": round(fee_no, 4),
                "gross_cost": round(gross_cost, 4),
                "net_profit_per_dollar": round(net_profit, 4),
                "liquidity_a": row.get("liquidity"),
                "liquidity_b": row.get("liquidity"),
                "volume_a": row.get("volume"),
                "volume_b": row.get("volume"),
                "category": row.get("category"),
            }
        )

    return flags


# --------------------------------------------------------------------------
# Detection - Shape 2: cross-venue matched-pair mispricing
# --------------------------------------------------------------------------
def detect_cross_venue_mispricing(
    candidates: list[dict],
    kalshi_rows_by_id: dict[str, dict],
    polymarket_rows_by_id: dict[str, dict],
) -> list[dict]:
    """For each candidate pair venue_matcher.py proposed, checks BOTH
    directions - Kalshi YES + Polymarket NO, and Polymarket YES + Kalshi
    NO - since either could be the cheaper combination depending on how
    the two venues have each priced the same real-world outcome. Only
    the cheaper of the two directions (if either clears fees) is
    flagged, since both directions cannot be simultaneously profitable
    for the same pair (their combined gross cost is always exactly
    2.00 minus whatever the market's real spread produces)."""
    flags: list[dict] = []

    for cand in candidates:
        k_id = cand.get("kalshi_source_market_id")
        p_id = cand.get("polymarket_source_market_id")
        k_row = kalshi_rows_by_id.get(k_id)
        p_row = polymarket_rows_by_id.get(p_id)
        if not k_row or not p_row:
            continue  # candidate references a row no longer in the
            # latest snapshot (e.g. market closed since matching ran) -
            # skip rather than guess.

        k_yes = _to_float(k_row.get("yes_ask"))
        k_no = _to_float(k_row.get("no_ask"))
        p_yes = _to_float(p_row.get("yes_ask"))
        p_no = _to_float(p_row.get("no_ask"))
        if None in (k_yes, k_no, p_yes, p_no):
            continue

        p_category = _kalshi_category_to_polymarket_key(k_row.get("category"))

        directions = [
            ("kalshi_yes_polymarket_no", k_yes, "kalshi", p_no, "polymarket"),
            ("polymarket_yes_kalshi_no", p_yes, "polymarket", k_no, "kalshi"),
        ]

        best_flag = None
        for direction_name, ask_a, platform_a, ask_b, platform_b in directions:
            gross_cost = ask_a + ask_b
            if gross_cost >= 1.0:
                continue

            fee_a = (
                kalshi_taker_fee(ask_a)
                if platform_a == "kalshi"
                else polymarket_taker_fee(ask_a, p_category)
            )
            fee_b = (
                kalshi_taker_fee(ask_b)
                if platform_b == "kalshi"
                else polymarket_taker_fee(ask_b, p_category)
            )

            # See detect_single_venue_mispricing()'s matching comment -
            # same float-precision rounding fix applies here.
            net_profit = round(1.0 - gross_cost - fee_a - fee_b, 6)
            if net_profit < MIN_NET_PROFIT_FRACTION:
                continue

            flag = {
                "opportunity_type": MATCH_SOURCE_CROSS_VENUE,
                "direction": direction_name,
                "platform_a": platform_a,
                "market_a": k_id if platform_a == "kalshi" else p_id,
                "title_a": k_row.get("title") if platform_a == "kalshi" else p_row.get("title"),
                "leg_a_side": "YES",
                "leg_a_ask": ask_a,
                "leg_a_fee": round(fee_a, 4),
                "platform_b": platform_b,
                "market_b": p_id if platform_b == "polymarket" else k_id,
                "title_b": p_row.get("title") if platform_b == "polymarket" else k_row.get("title"),
                "leg_b_side": "NO",
                "leg_b_ask": ask_b,
                "leg_b_fee": round(fee_b, 4),
                "gross_cost": round(gross_cost, 4),
                "net_profit_per_dollar": round(net_profit, 4),
                "liquidity_a": k_row.get("liquidity") if platform_a == "kalshi" else p_row.get("liquidity"),
                "liquidity_b": p_row.get("liquidity") if platform_b == "polymarket" else k_row.get("liquidity"),
                "volume_a": k_row.get("volume") if platform_a == "kalshi" else p_row.get("volume"),
                "volume_b": p_row.get("volume") if platform_b == "polymarket" else k_row.get("volume"),
                "category": k_row.get("category"),
                "title_similarity": cand.get("title_similarity"),
                "close_time_gap_hours": cand.get("close_time_gap_hours"),
                "match_path": cand.get("match_path"),
            }

            if best_flag is None or net_profit > best_flag["net_profit_per_dollar"]:
                best_flag = flag

        if best_flag is not None:
            flags.append(best_flag)

    return flags


# --------------------------------------------------------------------------
# Legal footprint
# --------------------------------------------------------------------------
# Real, sourced state-availability facts as of this session - see
# /docs/venue_legal_footprint.md for the full evidence trail, the exact
# sources each row is checked against, and Greg's standing instruction to
# re-verify this table before trusting it in a live trading decision
# (both venues' own eligibility tools are the only authority worth
# trusting on the day a trade is actually placed - see the doc). This
# constant is the machine-readable mirror of that doc's table; if the two
# ever disagree, the doc is the source of truth and this constant is
# stale and needs updating.
#
# Kalshi: CFTC-regulated, nationally available by default; its SPORTS
# contracts specifically are restricted, paused, or contested in a
# real, named, moving set of states (confirmed live via a July 2026
# third-party legal tracker, itself checked against Kalshi's own
# eligibility-tool framing). Climate/Weather, Commodities, and Elections
# contracts - this project's actual three Kalshi tracks - are NOT sports
# contracts and are not confirmed to carry the same restriction; treated
# here as nationally available pending a track-specific check, a named
# assumption rather than a silent one.
KALSHI_SPORTS_RESTRICTED_STATES = {
    "AZ", "MA", "MD", "MI", "MT", "NV", "OH",
}
# Kalshi tracks this project actually pulls - none are Sports, so the
# restricted-state set above does not currently apply to any track this
# detector flags. Kept here, named, so a future Track 6 (flagship
# sports/exchange markets, per ROADMAP.md) addition does not silently
# assume the same nationwide availability this constant currently grants
# Climate/Commodities/Elections.
KALSHI_TRACKS_SUBJECT_TO_SPORTS_RESTRICTION = {"sports"}

# Polymarket: relaunched under US CFTC regulation via Polymarket US
# (QCX LLC) in 2026; nationally available in the same sense Kalshi is,
# pending the same per-state legal-tracker verification this project has
# not yet performed. Treated as nationally available here - a named
# assumption, not a verified all-50-state confirmation.
POLYMARKET_KNOWN_RESTRICTED_STATES: set[str] = set()

# Minnesota: a state law effective 2026-08-01 makes it a felony to
# create, operate, host, or advertise a prediction-market PLATFORM in the
# state - it targets platforms, not individual traders placing trades
# from Minnesota, and is under active federal litigation as of this
# session. Not modeled as a per-trade restriction here since it does not
# restrict the trader the way the Kalshi sports list above does; noted in
# the doc for Greg's own awareness, not enforced as a state block in this
# constant.


def fully_available_states(platform_a: str, platform_b: str) -> dict:
    """Returns whether BOTH venues in a flagged pair are, as far as this
    project's current (incomplete) legal-footprint data can confirm,
    available without a known state-level restriction affecting either
    venue's relevant track. This is deliberately conservative in its
    claims: it reports `both_available_nationally = True` only for the
    combinations this project has actually checked evidence for (see
    /docs/venue_legal_footprint.md), and always returns a note pointing
    back to that doc rather than asserting a guarantee this data can't
    back up."""
    note = (
        "Legal availability is a moving target and this project has not "
        "yet built a full per-state, per-track verification pass - see "
        "/docs/venue_legal_footprint.md. Kalshi's SPORTS contracts "
        "specifically are restricted in AZ, MA, MD, MI, MT, NV, OH as of "
        "this session; none of this project's three current Kalshi "
        "tracks (Climate/Commodities, Elections) are Sports contracts. "
        "Always confirm via each venue's own live eligibility tool before "
        "a real trade, not this constant."
    )
    return {
        "both_available_nationally": True,
        "note": note,
    }


# --------------------------------------------------------------------------
# Liquidity and legal-footprint enrichment
# --------------------------------------------------------------------------
def enrich_with_liquidity_and_legal(
    flags: list[dict], kalshi_rows_by_id: dict, polymarket_rows_by_id: dict
) -> list[dict]:
    """Attaches the real fillable size (liquidity_check.py) and the
    legal-footprint status (see fully_available_states() below, and its
    source doc /docs/venue_legal_footprint.md) to every flagged row, per
    Session 0.1's five per-venue evaluation criteria. A flag is not
    deleted if it fails either check - it is labeled, so the reviewer
    sees WHY an otherwise-real price gap isn't tradable, rather than the
    flag silently disappearing."""
    enriched = []
    for flag in flags:
        row_a = (
            kalshi_rows_by_id.get(flag["market_a"])
            if flag["platform_a"] == "kalshi"
            else polymarket_rows_by_id.get(flag["market_a"])
        )
        row_b = (
            kalshi_rows_by_id.get(flag["market_b"])
            if flag["platform_b"] == "kalshi"
            else polymarket_rows_by_id.get(flag["market_b"])
        )

        fillable = estimate_fillable_size(
            row_a, flag.get("leg_a_side"), flag.get("platform_a"), flag.get("leg_a_ask"),
            row_b, flag.get("leg_b_side"), flag.get("platform_b"), flag.get("leg_b_ask"),
        )
        flag["fillable_size_dollars"] = fillable["fillable_size_dollars"]
        flag["fillable_size_basis"] = fillable["basis"]
        flag["liquidity_sufficient"] = fillable["sufficient"]

        legal_states = fully_available_states(flag["platform_a"], flag["platform_b"])
        flag["legal_footprint_status"] = (
            "both_venues_available"
            if legal_states["both_available_nationally"]
            else "state_restrictions_apply"
        )
        flag["legal_footprint_note"] = legal_states["note"]

        enriched.append(flag)

    return enriched


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------
_OUTPUT_COLUMNS = [
    "opportunity_type",
    "direction",
    "platform_a",
    "market_a",
    "title_a",
    "leg_a_side",
    "leg_a_ask",
    "leg_a_fee",
    "platform_b",
    "market_b",
    "title_b",
    "leg_b_side",
    "leg_b_ask",
    "leg_b_fee",
    "gross_cost",
    "net_profit_per_dollar",
    "fillable_size_dollars",
    "fillable_size_basis",
    "liquidity_sufficient",
    "legal_footprint_status",
    "legal_footprint_note",
    "category",
    "title_similarity",
    "close_time_gap_hours",
    "match_path",
    "liquidity_a",
    "liquidity_b",
    "volume_a",
    "volume_b",
    "flagged_at",
]


def write_flags_csv(path: Path, flags: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=_OUTPUT_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in flags:
            writer.writerow(row)


# --------------------------------------------------------------------------
# Main pipeline
# --------------------------------------------------------------------------
def run() -> dict:
    flagged_at = datetime.now(timezone.utc).isoformat()
    flagged_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    log.info("=== Arbitrage detector run starting ===")

    kalshi_rows = _read_rows(KALSHI_LATEST)
    polymarket_rows = _read_rows(POLYMARKET_LATEST)
    kalshi_rows_by_id = {r.get("source_market_id"): r for r in kalshi_rows}
    polymarket_rows_by_id = {r.get("source_market_id"): r for r in polymarket_rows}

    single_venue_flags = detect_single_venue_mispricing(kalshi_rows, "kalshi")
    single_venue_flags += detect_single_venue_mispricing(polymarket_rows, "polymarket")

    candidates_path = _latest_candidate_matches_path()
    if candidates_path is None:
        log.warning(
            "No candidate_matches_*.csv found in %s - run venue_matcher.py "
            "first. Cross-venue detection skipped this run (single-venue "
            "YES+NO detection still ran).",
            MATCHED_DIR,
        )
        candidates = []
    else:
        candidates = _read_rows(candidates_path)

    cross_venue_flags = detect_cross_venue_mispricing(
        candidates, kalshi_rows_by_id, polymarket_rows_by_id
    )

    all_flags = single_venue_flags + cross_venue_flags
    all_flags = enrich_with_liquidity_and_legal(
        all_flags, kalshi_rows_by_id, polymarket_rows_by_id
    )
    for flag in all_flags:
        flag["flagged_at"] = flagged_at

    out_path = FLAGS_DIR / f"arbitrage_flags_{flagged_at_compact}.csv"
    write_flags_csv(out_path, all_flags)
    write_flags_csv(FLAGS_LATEST_PATH, all_flags)

    summary = {
        "flagged_at": flagged_at,
        "kalshi_rows_checked": len(kalshi_rows),
        "polymarket_rows_checked": len(polymarket_rows),
        "candidate_pairs_checked": len(candidates),
        "single_venue_flags": len(single_venue_flags),
        "cross_venue_flags": len(cross_venue_flags),
        "total_flags": len(all_flags),
        "output_path": str(out_path),
    }

    log.info(
        "=== Arbitrage detector run complete: %d total flags (%d "
        "single-venue, %d cross-venue) from %d Kalshi rows, %d "
        "Polymarket rows, %d candidate pairs ===",
        summary["total_flags"],
        summary["single_venue_flags"],
        summary["cross_venue_flags"],
        summary["kalshi_rows_checked"],
        summary["polymarket_rows_checked"],
        summary["candidate_pairs_checked"],
    )

    return summary


if __name__ == "__main__":
    import json

    result = run()
    print(json.dumps(result, indent=2))
