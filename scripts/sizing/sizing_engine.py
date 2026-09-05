"""
Session 2.6 -- Bankroll & Sizing Logic

WHAT THIS SCRIPT IS
--------------------
Turns two open, flagged legs from Session 2.4's data/pickem/clv_log.csv into
a concrete suggested stake for a real PrizePicks 2-pick Power Play entry --
the one entry type this project has a real, sourced payout number for
(Session 2.5, sample_size_methodology.md Section 2: 3x payout, 57.7% real
per-leg breakeven win rate). This is the first place in the project where
a probability estimate turns into an actual dollar suggestion, so every
number this script produces is either sourced (the 3x payout) or an
explicitly named, documented judgment call (the Kelly fraction, the
platform dampener, the bankroll cap) -- never a guessed one.

This script does NOT place any bet. Per ROADMAP.md's standing "flags and
sizes, does not place bets" principle, it prints a suggested stake; a human
decides whether to place it and reports the real outcome back through
Session 2.5's outcome_tracker.py.

WHY ONLY THE 2-PICK POWER PLAY, IN V1
----------------------------------------
PrizePicks and Underdog both require 2+ legs to be combined into one
all-or-nothing (or Flex) entry before a real payout multiplier applies.
Session 2.5 only sourced one real, confirmed payout number: PrizePicks'
standard 2-pick Power Play, 3x payout. No other entry size (3-pick, 4-pick,
Flex) or Underdog's own payout table has been researched yet -- guessing at
one here would mean sizing real money against an invented number, which
this project does not do (see e.g. Session 2.3's refusal to guess at
PrizePicks' Fantasy Score formula before confirming it against PrizePicks'
own source). So v1 supports exactly one entry shape: two open legs on
PrizePicks, sized as a 2-pick Power Play. Every other combination is
rejected with an explicit, named status -- never silently sized using a
number that was never confirmed.

THE SIZING METHOD -- FRACTIONAL KELLY, NAMED AND JUSTIFIED
---------------------------------------------------------------
Standard Kelly criterion for an all-or-nothing bet with combined win
probability p and net odds b (profit per $1 staked if the whole entry
hits):

    f* = (p * (b + 1) - 1) / b

For a 2-pick Power Play, b = 2 (a $1 stake returns $3 total on a win --
$2 of that is profit). p is the entry's combined win probability: this
script multiplies the two legs' own model_prob values together
(first_flagged_model_prob for each leg, from Session 2.3's model),
treating the two legs as independent events -- a stated simplification
(two different players/stats are a reasonable independence assumption;
see sizing_methodology.md for the case where this could fail, e.g. two
legs from the same game).

Full Kelly is never staked directly. This script applies
KELLY_FRACTION = 0.25 (quarter-Kelly) -- a standard, named, conservative
practice used specifically when the win-probability input carries real
estimation uncertainty (this project's own model has no opponent/injury/
pace adjustments yet -- a stated v1 gap since Session 2.3 -- and
Session 2.4's own FLAG_EDGE_THRESHOLD is itself an unvalidated
placeholder). Quarter-Kelly is not a derived number any more than
FLAG_EDGE_THRESHOLD or Session 2.5's p1=0.60 were -- it is a reasoned
starting point, explicitly flagged here as a candidate for Session 8.3's
recalibration work once real graded outcomes exist to check it against.

PLATFORM-SPECIFIC RISK ADJUSTMENT
-------------------------------------
Per the Session 1.1 continuation research (account-limiting policy,
archived at docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md):
PrizePicks has the most documented first-hand pattern of win-adjacent
account closures and withheld withdrawals; the specific "55% win rate over
200+ entries" threshold could not be corroborated and is NOT used here as
a hard number. What IS used: a named, conservative dampener applied on top
of quarter-Kelly for PrizePicks specifically, reflecting that a suspended
or limited account can turn a real, currently-winning edge into money that
is never actually collected -- a risk the raw Kelly formula does not know
about, since Kelly assumes every future bet is genuinely available to be
placed. PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70 is this project's own
stated judgment call, not sourced to a specific number, since no source
gives one -- flagged explicitly, same as every other placeholder in this
project.

Underdog is NOT sized in v1 (see "WHY ONLY THE 2-PICK POWER PLAY" above --
no real Underdog payout multiplier has been sourced yet), so
PLATFORM_RISK_MULTIPLIER carries an "underdog" entry for the code's own
future use, but the entry-type gate below prevents it from ever being
reached until Underdog's real payout table is researched (a stated, open
gap -- see sizing_methodology.md).

SAME-GAME CAUTION DAMPENER -- FLAGGING, NOT MODELING, A REAL CORRELATION GAP
------------------------------------------------------------------------------
Kelly's formula (and the combined-probability multiplication above it)
assumes the two legs are independent events. When both legs come from the
SAME real game (same game_id), that assumption is weaker: a blowout, an
overtime, or a key injury can move several players' stats in the same
direction at once. This project does not have real correlation data to
model that properly yet, and manufacturing a number to "correct" for it
would mean sizing real money off a guess -- exactly what this project does
not do (see Session 2.3's refusal to guess at an unconfirmed scoring
formula, or the PrizePicks dampener discussion above).

Rather than silently ignore this or invent a precise correction, this
script applies one more small, explicitly named dampener,
SAME_GAME_CAUTION_MULTIPLIER = 0.85, whenever both requested legs share a
game_id -- and reports it plainly in the output (same_game_pair: True,
same_game_caution_applied: True) so it is visible whenever it happens,
never a hidden adjustment. This is a deliberate, direction-agnostic choice:
same-game correlation could in reality make the true combined probability
higher OR lower than the independence assumption suggests (it depends on
whether the two legs tend to move together or compete against each other),
and this project does not yet have the real data to know which, for which
stat pairs. Applying a mild, flagged caution factor nudges toward the
safer of the two possible errors (understaking a same-game pair) rather
than pretending independence is a safe default. This is a "flag it as
riskier, don't pretend to model it precisely" choice, not a corrected
number -- revisiting it with real same-game correlation data belongs to a
future session, once enough graded same-game entries exist to check
against (see Session 8.3).

BANKROLL CAP -- ENFORCED IN CODE, NOT JUST DESCRIBED
----------------------------------------------------------
MAX_SINGLE_POSITION_PCT = 0.05 -- no single suggested stake will ever
exceed 5% of the bankroll figure the user provides, regardless of what the
(already-dampened) Kelly fraction computes to. This is a hard ceiling,
applied after every other adjustment, so a large modeled edge cannot
produce an unreasonably large single-entry suggestion. Named and adjustable
here, not left as a documentation-only rule.

WHAT THIS SCRIPT DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------
- Does not size any entry type other than a 2-pick Power Play on
  PrizePicks (see above).
- Does not account for correlation between two legs from the SAME real
  game (e.g. a QB's passing yards and his team's leading WR's receiving
  yards in the same game are not fully independent events) -- the combined
  probability is a straight product, a stated simplification.
- Does not track a running bankroll balance across multiple suggested
  entries placed over time -- each run is a single, independent
  suggestion against the bankroll figure supplied on that run. A real
  running-bankroll tracker (sized off the outcome_tracker.py log) is a
  named candidate for a future session, not built here.
- Does not re-derive KELLY_FRACTION or PLATFORM_RISK_MULTIPLIER from real
  graded results -- that is Session 8.3's job, same as
  FLAG_EDGE_THRESHOLD and Session 2.5's p1=0.60.

USAGE (pick'em sizing)
-----------------------
pip install pandas --break-system-packages
python sizing_engine.py pickem --flag-ids "prizepicks|12345678" "prizepicks|87654321" --bankroll 500

===============================================================================
SESSION 3.3 ADDENDUM -- ARBITRAGE SIZING (extends, does not replace, the above)
===============================================================================

WHAT WAS ADDED AND WHY IT IS NOT JUST "KELLY AGAIN"
-----------------------------------------------------
Everything above sizes a PROBABILISTIC bet: one entry either wins or loses,
and Kelly answers "how much of my bankroll should I risk on a estimated
edge." Session 3.2's arbitrage detector (`detector.py`) finds a genuinely
different shape of opportunity: two legs that, once both are actually
filled, are a LOCKED position with a guaranteed profit
(`net_profit_per_dollar`) regardless of which real-world outcome occurs --
there is no win/loss probability to plug into Kelly at all. Applying Kelly
here would be a category error, not a stricter or looser version of the
same math.

Arbitrage's real risk is not "did I pick the right side" -- it is:
1. CAPITAL LOCKUP ACROSS TWO VENUES AT ONCE. A pick'em entry stakes money
   at ONE platform. An arbitrage position requires buying one leg at
   Kalshi and the other leg at Polymarket SIMULTANEOUSLY -- the same
   dollar amount must be sitting, available, at BOTH venues at the same
   time, not split from one shared pool. `sizing_engine.py`'s pick'em
   code has always assumed a single bankroll figure because it only ever
   sizes a single-venue bet; that assumption is wrong for arbitrage and
   is not reused here.
2. EXECUTION ("LEGGING") RISK. `detector.py` prices a flagged opportunity
   at the ask price it read at pull time. Placing two real trades on two
   real venues is not instantaneous -- the price or available size on
   either leg can move in the seconds it takes to place both orders. A
   Kelly-style probability-of-winning adjustment does not describe this
   risk; a haircut on the sized position does.

WHY BANKROLL IS TWO NUMBERS, NOT ONE, FOR ARBITRAGE
------------------------------------------------------
`size_arbitrage_position()` below takes `kalshi_bankroll` and
`polymarket_bankroll` as two separate arguments -- real dollars actually
sitting, right now, in each venue's own account -- rather than one
combined bankroll figure. This mirrors the real mechanics: a $200
arbitrage position requires $200 already deposited at Kalshi AND $200
already deposited at Polymarket, a total of $400 tied up, not $200 drawn
from a shared $400 pool. Treating this as one pool would let the sizing
math suggest a position that cannot actually be placed because one
venue's account is thinner than the other's.

WHY AN OPEN-POSITIONS LEDGER WAS ADDED
------------------------------------------
A pick'em entry resolves in hours (the game ends). A real arbitrage
position may sit open for days or longer, since both legs settle only
when their real-world event resolves -- and this project has not
researched real settlement-time data for either venue, so no specific
number of days is assumed here (that would be exactly the kind of
guessed number this project's own standing rule forbids). What CAN be
tracked honestly, without guessing at settlement timing, is which
positions are currently open and how much capital each one has already
committed at each venue. `data/arbitrage/open_positions.csv` is a new,
small ledger (same pattern as Session 2.5's outcome_tracker.py): every
time a real arbitrage trade is placed, `record_open_arbitrage_position()`
appends a row; once it settles, `settle_arbitrage_position()` marks it
closed and frees that capital back up. `size_arbitrage_position()` always
subtracts currently-open commitments from the bankroll figures supplied,
so it never suggests a new position against capital that is already
tied up in an earlier, still-open one.

EXECUTION_RISK_BUFFER -- NAMED, NOT DERIVED, SAME POSTURE AS KELLY_FRACTION
------------------------------------------------------------------------------
EXECUTION_RISK_BUFFER = 0.85 is a flat haircut applied to the
liquidity/capital-bound raw position size, exactly the same "named
judgment call, not a sourced number" posture as KELLY_FRACTION and
SAME_GAME_CAUTION_MULTIPLIER above. It exists because `detector.py`'s
`fillable_size_dollars` describes size available at the INSTANT the
snapshot was pulled -- by the time a human actually places both real
orders, some of that size may already be gone or the price may have
ticked. Flagged explicitly as a candidate for Session 8.3 recalibration
once real placed-and-filled arbitrage trades exist to check it against.

MAX_ARBITRAGE_POSITION_PCT -- SAME HARD-CAP PATTERN, APPLIED TO COMBINED CAPITAL
-----------------------------------------------------------------------------------
MAX_ARBITRAGE_POSITION_PCT = 0.05 caps a single arbitrage position at 5%
of the user's TOTAL combined bankroll (Kalshi + Polymarket balances
added together), the same hard-ceiling posture as pick'em's
MAX_SINGLE_POSITION_PCT, so one large flagged price gap cannot suggest an
outsized single commitment even before the per-venue capital check is
applied.

WHAT THIS ADDITION DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Does not model real settlement time / capital-lockup DURATION -- see
  "open-positions ledger" above. It tracks that capital IS locked, not
  for how long.
- Does not re-derive EXECUTION_RISK_BUFFER from real fill data -- a
  starting value, same as KELLY_FRACTION was in Session 2.6.
- Does not net opposing open positions against each other (e.g. an open
  Kalshi commitment from one arbitrage trade is not offset against a
  fresh flag that would sell back into the same market) -- each open
  position's committed capital is treated as fully locked until settled.

USAGE (arbitrage sizing)
--------------------------
python sizing_engine.py arbitrage size --market-a KXHOUSEMO5-26-R --market-b 0x1234abcd --kalshi-bankroll 1000 --polymarket-bankroll 1000
python sizing_engine.py arbitrage record-open --market-a KXHOUSEMO5-26-R --market-b 0x1234abcd --kalshi-bankroll 1000 --polymarket-bankroll 1000
python sizing_engine.py arbitrage settle --position-id <id> --note "both legs settled, profit collected"
"""

from __future__ import annotations

import argparse
import csv
import glob
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Paths -- matching Session 2.2/2.4/2.5's existing repo-relative pattern.
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
LOG_PATH = BASE_DIR / "logs" / "sizing.log"

# Session 3.3 additions -- arbitrage sizing reads Session 3.2's flag output
# and maintains its own small open-positions ledger (see docstring
# addendum above for why this ledger exists).
ARBITRAGE_FLAGS_DIR = BASE_DIR / "data" / "arbitrage" / "flags"
ARBITRAGE_OPEN_POSITIONS_PATH = BASE_DIR / "data" / "arbitrage" / "open_positions.csv"

# ---------------------------------------------------------------------------
# Constants -- named explicitly, per this project's "no unnamed black-box
# factors" documentation standard. See module docstring for full reasoning
# on each one.
# ---------------------------------------------------------------------------
SUPPORTED_ENTRY_TYPE = "2-pick Power Play"
SUPPORTED_LEG_COUNT = 2
ENTRY_PAYOUT_MULTIPLIER = 3.0  # PrizePicks' own published 2-pick Power Play payout (sample_size_methodology.md Section 2)
ENTRY_NET_ODDS_B = ENTRY_PAYOUT_MULTIPLIER - 1.0  # b in the Kelly formula (profit per $1 staked on a win)
BREAKEVEN_WIN_RATE = 0.5774  # sample_size_methodology.md Section 2 -- sqrt(1/3)

KELLY_FRACTION = 0.25  # quarter-Kelly -- stated placeholder, see docstring

PLATFORM_RISK_MULTIPLIER = {
    "prizepicks": 0.70,  # stated judgment call, see docstring -- account-closure risk dampener
    "underdog": 0.85,    # NOT currently reachable -- see SUPPORTED_PLATFORMS gate below
}
SUPPORTED_PLATFORMS = {"prizepicks"}  # v1 gate -- Underdog has no sourced payout multiplier yet

MAX_SINGLE_POSITION_PCT = 0.05  # hard bankroll cap, enforced below -- see docstring
MIN_BANKROLL = 1.0  # guards against a zero/negative bankroll producing a nonsense stake

SAME_GAME_CAUTION_MULTIPLIER = 0.85  # stated, direction-agnostic placeholder -- see docstring

# ---------------------------------------------------------------------------
# Session 3.3 additions -- arbitrage-specific constants. Same "named, not
# guessed" standard as the pick'em constants above -- see docstring
# addendum for the reasoning behind each one.
# ---------------------------------------------------------------------------
ARBITRAGE_SUPPORTED_PLATFORMS = {"kalshi", "polymarket"}
EXECUTION_RISK_BUFFER = 0.85  # stated placeholder -- legging-risk haircut, see docstring
MAX_ARBITRAGE_POSITION_PCT = 0.05  # hard cap vs. TOTAL combined bankroll -- see docstring
MIN_ARBITRAGE_BANKROLL = 1.0  # guards against a zero/negative bankroll figure

ARBITRAGE_LEDGER_FIELDS = [
    "position_id",
    "opened_at",
    "platform_a",
    "market_a",
    "leg_a_side",
    "leg_a_ask",
    "capital_committed_a",
    "platform_b",
    "market_b",
    "leg_b_side",
    "leg_b_ask",
    "capital_committed_b",
    "net_profit_per_dollar",
    "expected_profit_dollars",
    "status",
    "settled_at",
    "settlement_note",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("sizing_engine")
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
# CLV log lookup
# ---------------------------------------------------------------------------
def load_clv_log() -> pd.DataFrame:
    if not CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{CLV_LOG_PATH} not found. Run clv_logger.py first (Session 2.4) "
            f"so there are flagged opportunities to size."
        )
    return pd.read_csv(CLV_LOG_PATH)


def fetch_legs(flag_ids: list[str]) -> tuple[list[dict], list[str]]:
    """Looks up each flag_id in the live CLV log. Returns (legs_found,
    problems) -- problems is a list of human-readable reasons any
    requested flag_id could not be used, so a rejected sizing request
    always says exactly why, not just that it failed."""
    clv_df = load_clv_log()
    legs: list[dict] = []
    problems: list[str] = []

    for flag_id in flag_ids:
        matches = clv_df.loc[clv_df["flag_id"] == flag_id]
        if len(matches) == 0:
            problems.append(f"flag_id '{flag_id}' not found in {CLV_LOG_PATH}")
            continue
        row = matches.iloc[0].to_dict()

        if row.get("status") != "open":
            problems.append(
                f"flag_id '{flag_id}' has status='{row.get('status')}', not 'open' "
                f"-- this leg is no longer available to bet (game likely locked)."
            )
            continue

        model_prob = row.get("first_flagged_model_prob")
        if model_prob is None or pd.isna(model_prob):
            problems.append(f"flag_id '{flag_id}' has no first_flagged_model_prob logged.")
            continue

        if row.get("game_id") is None or pd.isna(row.get("game_id")):
            problems.append(
                f"flag_id '{flag_id}' has no game_id logged -- required to check for a "
                f"same-game pair (see SAME_GAME_CAUTION_MULTIPLIER in the docstring)."
            )
            continue

        legs.append(row)

    return legs, problems


# ---------------------------------------------------------------------------
# Sizing math
# ---------------------------------------------------------------------------
def combined_entry_probability(legs: list[dict]) -> float:
    """Product of each leg's own flagged-side model probability. Treats
    legs as independent -- a stated simplification, see docstring."""
    p = 1.0
    for leg in legs:
        p *= float(leg["first_flagged_model_prob"])
    return p


def raw_kelly_fraction(p: float, b: float) -> float:
    """f* = (p*(b+1) - 1) / b. Can be negative (no real edge) -- callers
    must floor at 0, never bet a negative fraction."""
    return (p * (b + 1.0) - 1.0) / b


def size_entry(legs: list[dict], bankroll: float) -> dict:
    """Runs the full sizing pipeline for one 2-pick Power Play entry and
    returns a fully-explained result dict -- every intermediate number is
    included, not just the final stake, so a manual sanity check never
    requires re-deriving the math by hand."""
    platforms = {leg.get("platform") for leg in legs}

    if len(legs) != SUPPORTED_LEG_COUNT:
        return _rejected(
            f"sizing_engine v1 only supports exactly {SUPPORTED_LEG_COUNT} legs "
            f"({SUPPORTED_ENTRY_TYPE}) -- received {len(legs)}."
        )

    if platforms != SUPPORTED_PLATFORMS:
        return _rejected(
            f"sizing_engine v1 only supports platform(s) {sorted(SUPPORTED_PLATFORMS)} "
            f"-- received leg(s) from {sorted(platforms)}. No sourced payout "
            f"multiplier exists yet for the platform(s) requested (see docstring)."
        )

    if bankroll < MIN_BANKROLL:
        return _rejected(f"--bankroll must be at least {MIN_BANKROLL}, got {bankroll}.")

    p_combined = combined_entry_probability(legs)
    f_raw = raw_kelly_fraction(p_combined, ENTRY_NET_ODDS_B)
    f_quarter = max(f_raw, 0.0) * KELLY_FRACTION

    platform = legs[0]["platform"]
    dampener = PLATFORM_RISK_MULTIPLIER[platform]

    game_ids = {leg.get("game_id") for leg in legs}
    same_game_pair = len(game_ids) == 1
    same_game_multiplier = SAME_GAME_CAUTION_MULTIPLIER if same_game_pair else 1.0

    f_dampened = f_quarter * dampener * same_game_multiplier

    uncapped_stake = bankroll * f_dampened
    cap_amount = bankroll * MAX_SINGLE_POSITION_PCT
    capped = uncapped_stake > cap_amount
    final_stake = min(uncapped_stake, cap_amount)

    if f_raw <= 0:
        status = "no_bet_negative_edge"
        final_stake = 0.0
    elif capped:
        status = "sized_capped_at_max_position"
    else:
        status = "sized"

    return {
        "status": status,
        "entry_type": SUPPORTED_ENTRY_TYPE,
        "platform": platform,
        "leg_flag_ids": [leg["flag_id"] for leg in legs],
        "leg_model_probs": [float(leg["first_flagged_model_prob"]) for leg in legs],
        "combined_entry_probability": round(p_combined, 4),
        "breakeven_win_rate_reference": BREAKEVEN_WIN_RATE,
        "entry_net_odds_b": ENTRY_NET_ODDS_B,
        "raw_kelly_fraction": round(f_raw, 4),
        "quarter_kelly_fraction": round(f_quarter, 4),
        "platform_risk_multiplier_applied": dampener,
        "same_game_pair": same_game_pair,
        "same_game_caution_multiplier_applied": same_game_multiplier,
        "dampened_kelly_fraction": round(f_dampened, 4),
        "bankroll": bankroll,
        "uncapped_suggested_stake": round(uncapped_stake, 2),
        "max_single_position_cap": round(cap_amount, 2),
        "suggested_stake": round(final_stake, 2),
        "suggested_stake_pct_of_bankroll": round(100 * final_stake / bankroll, 2) if bankroll else None,
    }


def _rejected(reason: str) -> dict:
    return {"status": "rejected", "reason": reason}


# ===========================================================================
# SESSION 3.3 -- ARBITRAGE SIZING
# See the "SESSION 3.3 ADDENDUM" section of the module docstring above for
# why this is a genuinely different sizing problem from the pick'em code
# above it, not a variant of the same Kelly math.
# ===========================================================================

# ---------------------------------------------------------------------------
# Reading Session 3.2's flag output
# ---------------------------------------------------------------------------
def _latest_arbitrage_flags_path() -> Optional[Path]:
    pattern = str(ARBITRAGE_FLAGS_DIR / "arbitrage_flags_*.csv")
    matches = sorted(glob.glob(pattern))
    if not matches:
        return None
    return Path(matches[-1])


def load_latest_arbitrage_flags() -> list[dict]:
    """Reads the most recent arbitrage_flags_<timestamp>.csv written by
    detector.py. Raises FileNotFoundError with a clear, actionable message
    if detector.py has never been run -- same "fail loud, not silent"
    posture as load_clv_log() above."""
    path = _latest_arbitrage_flags_path()
    if path is None:
        raise FileNotFoundError(
            f"No arbitrage_flags_*.csv found in {ARBITRAGE_FLAGS_DIR}. "
            f"Run detector.py first (Session 3.2) so there are flagged "
            f"opportunities to size."
        )
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fetch_arbitrage_flag(market_a: str, market_b: str) -> tuple[Optional[dict], list[str]]:
    """Looks up a specific flagged pair by its two market ids in the
    latest arbitrage_flags_*.csv. market_a/market_b are matched in either
    position, since which venue detector.py labeled 'a' vs. 'b' for a
    given direction is not something the caller should have to know in
    advance. Returns (flag_row_or_None, problems)."""
    try:
        flags = load_latest_arbitrage_flags()
    except FileNotFoundError as exc:
        return None, [str(exc)]

    for row in flags:
        ids = {row.get("market_a"), row.get("market_b")}
        if ids == {market_a, market_b}:
            return row, []

    return None, [
        f"No open flag matching market_a='{market_a}' and market_b='{market_b}' "
        f"found in the latest arbitrage_flags_*.csv. The opportunity may have "
        f"closed, or detector.py needs to be re-run against current data."
    ]


# ---------------------------------------------------------------------------
# Open-positions ledger -- tracks capital already committed at each venue
# ---------------------------------------------------------------------------
def load_open_arbitrage_positions() -> list[dict]:
    """Reads the open-positions ledger. Returns an empty list, not an
    error, if the ledger doesn't exist yet -- a brand-new project has no
    open positions, which is a valid real state, not a missing-file
    problem."""
    if not ARBITRAGE_OPEN_POSITIONS_PATH.exists():
        return []
    with ARBITRAGE_OPEN_POSITIONS_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def committed_capital_by_venue(open_positions: list[dict]) -> dict[str, float]:
    """Sums capital currently tied up at each venue across every
    still-open position. A single arbitrage position commits capital at
    BOTH its platform_a and platform_b -- see docstring on why this is
    two separate commitments, not one shared amount."""
    committed: dict[str, float] = {"kalshi": 0.0, "polymarket": 0.0}
    for pos in open_positions:
        if pos.get("status") != "open":
            continue
        plat_a = pos.get("platform_a")
        plat_b = pos.get("platform_b")
        if plat_a in committed:
            committed[plat_a] += float(pos.get("capital_committed_a") or 0.0)
        if plat_b in committed:
            committed[plat_b] += float(pos.get("capital_committed_b") or 0.0)
    return committed


def _append_ledger_row(row: dict) -> None:
    ARBITRAGE_OPEN_POSITIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = ARBITRAGE_OPEN_POSITIONS_PATH.exists()
    with ARBITRAGE_OPEN_POSITIONS_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ARBITRAGE_LEDGER_FIELDS, extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def record_open_arbitrage_position(sized_result: dict) -> dict:
    """Appends a real, placed arbitrage position to the open-positions
    ledger, using the output of size_arbitrage_position() below. Call
    this only after the human has actually placed both real legs -- this
    project sizes and flags, it does not place bets (see ROADMAP.md's
    standing principle), so this function records a decision the human
    already made, it does not make one."""
    if sized_result.get("status") not in ("sized", "sized_capped"):
        return _rejected(
            f"Refusing to record an open position from a sizing result "
            f"with status='{sized_result.get('status')}' -- only a "
            f"successfully sized result should be recorded as a real, "
            f"placed trade."
        )

    position_id = datetime.now(timezone.utc).strftime("arb_%Y%m%dT%H%M%SZ")
    row = {
        "position_id": position_id,
        "opened_at": datetime.now(timezone.utc).isoformat(),
        "platform_a": sized_result["platform_a"],
        "market_a": sized_result["market_a"],
        "leg_a_side": sized_result.get("leg_a_side"),
        "leg_a_ask": sized_result.get("leg_a_ask"),
        "capital_committed_a": sized_result["capital_required_at_platform_a"],
        "platform_b": sized_result["platform_b"],
        "market_b": sized_result["market_b"],
        "leg_b_side": sized_result.get("leg_b_side"),
        "leg_b_ask": sized_result.get("leg_b_ask"),
        "capital_committed_b": sized_result["capital_required_at_platform_b"],
        "net_profit_per_dollar": sized_result["net_profit_per_dollar"],
        "expected_profit_dollars": sized_result["expected_profit_dollars_if_both_legs_fill"],
        "status": "open",
        "settled_at": "",
        "settlement_note": "",
    }
    _append_ledger_row(row)
    log.info("Recorded open arbitrage position %s: %s", position_id, row)
    return {"status": "recorded", "position_id": position_id, "ledger_row": row}


def settle_arbitrage_position(position_id: str, note: str = "") -> dict:
    """Marks a ledger row as settled, freeing its committed capital back
    up for future sizing. Rewrites the whole ledger file (small file,
    same acceptable pattern as other CSV logs in this project) rather
    than appending, since this is an update to an existing row, not a
    new one."""
    positions = load_open_arbitrage_positions()
    found = False
    for pos in positions:
        if pos.get("position_id") == position_id and pos.get("status") == "open":
            pos["status"] = "settled"
            pos["settled_at"] = datetime.now(timezone.utc).isoformat()
            pos["settlement_note"] = note
            found = True
            break

    if not found:
        return _rejected(
            f"No OPEN position with position_id='{position_id}' found in "
            f"{ARBITRAGE_OPEN_POSITIONS_PATH} -- check the id, or it may "
            f"already be settled."
        )

    with ARBITRAGE_OPEN_POSITIONS_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ARBITRAGE_LEDGER_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for pos in positions:
            writer.writerow(pos)

    log.info("Settled arbitrage position %s (note=%r)", position_id, note)
    return {"status": "settled", "position_id": position_id}


# ---------------------------------------------------------------------------
# Arbitrage sizing math
# ---------------------------------------------------------------------------
def size_arbitrage_position(
    flag_row: dict, kalshi_bankroll: float, polymarket_bankroll: float
) -> dict:
    """Runs the full arbitrage sizing pipeline for one flagged pair from
    detector.py and returns a fully-explained result dict, same
    "every intermediate number included" standard as size_entry() above.

    kalshi_bankroll / polymarket_bankroll are real dollars currently
    sitting in each venue's own account -- see docstring for why these
    are two separate numbers, not one combined bankroll.

    UNIT FIX (found via real-data validation, not a design choice made
    up front): detector.py's `fillable_size_dollars` field name is
    misleading. liquidity_check.py's own docstring says plainly that it
    is a CONTRACT COUNT ("a contract count IS a dollar notional amount"
    -- referring to the $1 PAYOUT each contract settles for, not its
    purchase cost). Buying N contracts at an ask price of $0.20 costs
    N * $0.20 in real dollars, not N dollars. Confirmed directly against
    real live Kalshi order-book data this session, e.g. MO-05
    Republican: yes_ask=$0.20, yes_ask_size=15.28 contracts -- the real
    cost to buy all 15.28 is $3.06, not $15.28. The first version of
    this function treated the contract count as if it were already a
    dollar amount, which would have UNDER-committed the sizing math's
    own bankroll caps relative to what a position of that many contracts
    actually costs to buy at low-priced legs, and OVER-stated real
    capital tied up at each venue. This version sizes in CONTRACTS
    throughout and converts to real per-leg dollar cost using each leg's
    own ask price only at the end, where a dollar figure is actually
    needed."""
    platform_a = flag_row.get("platform_a")
    platform_b = flag_row.get("platform_b")

    if platform_a not in ARBITRAGE_SUPPORTED_PLATFORMS or platform_b not in ARBITRAGE_SUPPORTED_PLATFORMS:
        return _rejected(
            f"Unrecognized platform(s) in flag row: platform_a='{platform_a}', "
            f"platform_b='{platform_b}'. Supported: {sorted(ARBITRAGE_SUPPORTED_PLATFORMS)}."
        )

    if platform_a == platform_b:
        return _rejected(
            f"size_arbitrage_position() expects two DIFFERENT venues for capital-"
            f"lockup purposes; got platform_a == platform_b == '{platform_a}' "
            f"(a single-venue YES+NO flag -- both legs are filled at the same "
            f"venue, so this is not a two-venue capital-lockup case; size it as "
            f"a single-venue bankroll check instead, not via this function)."
        )

    if kalshi_bankroll < MIN_ARBITRAGE_BANKROLL or polymarket_bankroll < MIN_ARBITRAGE_BANKROLL:
        return _rejected(
            f"Both --kalshi-bankroll and --polymarket-bankroll must be at least "
            f"{MIN_ARBITRAGE_BANKROLL}, got kalshi={kalshi_bankroll}, "
            f"polymarket={polymarket_bankroll}."
        )

    try:
        ask_a = float(flag_row.get("leg_a_ask"))
        ask_b = float(flag_row.get("leg_b_ask"))
    except (TypeError, ValueError):
        return _rejected(
            f"Flag row is missing a usable leg_a_ask/leg_b_ask -- cannot convert "
            f"contract count to a real dollar cost without both ask prices."
        )
    if ask_a <= 0 or ask_b <= 0:
        return _rejected(f"Flag row has a non-positive ask price (ask_a={ask_a}, ask_b={ask_b}).")

    fillable_contracts = float(flag_row.get("fillable_size_dollars") or 0.0)  # see docstring: really a contract count
    net_profit_per_dollar = float(flag_row.get("net_profit_per_dollar") or 0.0)  # profit per contract

    bankroll_by_venue = {"kalshi": kalshi_bankroll, "polymarket": polymarket_bankroll}
    committed = committed_capital_by_venue(load_open_arbitrage_positions())

    available_a = bankroll_by_venue[platform_a] - committed.get(platform_a, 0.0)
    available_b = bankroll_by_venue[platform_b] - committed.get(platform_b, 0.0)

    total_bankroll = kalshi_bankroll + polymarket_bankroll
    max_capital_by_pct = total_bankroll * MAX_ARBITRAGE_POSITION_PCT
    gross_cost_per_contract = ask_a + ask_b  # real total $ cost to buy one contract on each leg

    # Every candidate below is expressed in CONTRACTS, so they compare on
    # the same footing as fillable_contracts -- real dollar limits are
    # divided by the relevant real price first.
    contract_candidates = {
        "fillable_contracts": fillable_contracts,
        f"available_capital_{platform_a}": available_a / ask_a,
        f"available_capital_{platform_b}": available_b / ask_b,
        "max_position_pct_cap": max_capital_by_pct / gross_cost_per_contract,
    }
    binding_constraint = min(contract_candidates, key=contract_candidates.get)
    raw_contracts = max(contract_candidates[binding_constraint], 0.0)

    if raw_contracts <= 0:
        return _rejected(
            f"Sized position is 0 contracts -- binding constraint was "
            f"'{binding_constraint}' ({contract_candidates[binding_constraint]:.4f}). "
            f"Committed capital so far: {committed}."
        )

    buffered_contracts = round(raw_contracts * EXECUTION_RISK_BUFFER, 4)
    was_capped = binding_constraint != "fillable_contracts"

    capital_a = round(buffered_contracts * ask_a, 2)
    capital_b = round(buffered_contracts * ask_b, 2)
    expected_profit_dollars = round(buffered_contracts * net_profit_per_dollar, 2)

    return {
        "status": "sized_capped" if was_capped else "sized",
        "opportunity_type": flag_row.get("opportunity_type"),
        "platform_a": platform_a,
        "market_a": flag_row.get("market_a"),
        "leg_a_side": flag_row.get("leg_a_side"),
        "leg_a_ask": ask_a,
        "platform_b": platform_b,
        "market_b": flag_row.get("market_b"),
        "leg_b_side": flag_row.get("leg_b_side"),
        "leg_b_ask": ask_b,
        "net_profit_per_dollar": net_profit_per_dollar,
        "fillable_contracts": fillable_contracts,
        "kalshi_bankroll": kalshi_bankroll,
        "polymarket_bankroll": polymarket_bankroll,
        "committed_capital_kalshi": round(committed.get("kalshi", 0.0), 2),
        "committed_capital_polymarket": round(committed.get("polymarket", 0.0), 2),
        "available_capital_platform_a": round(available_a, 2),
        "available_capital_platform_b": round(available_b, 2),
        "max_position_pct_cap_dollars": round(max_capital_by_pct, 2),
        "binding_constraint": binding_constraint,
        "raw_contracts_before_execution_buffer": round(raw_contracts, 4),
        "execution_risk_buffer_applied": EXECUTION_RISK_BUFFER,
        "suggested_contracts": buffered_contracts,
        "capital_required_at_platform_a": capital_a,
        "capital_required_at_platform_b": capital_b,
        "capital_required_total_across_both_venues": round(capital_a + capital_b, 2),
        "expected_profit_dollars_if_both_legs_fill": expected_profit_dollars,
        "liquidity_sufficient": flag_row.get("liquidity_sufficient"),
        "legal_footprint_status": flag_row.get("legal_footprint_status"),
    }


def run_arbitrage_sizing(
    market_a: str, market_b: str, kalshi_bankroll: float, polymarket_bankroll: float
) -> dict:
    log.info(
        "=== Arbitrage sizing run starting: market_a=%s, market_b=%s, "
        "kalshi_bankroll=%s, polymarket_bankroll=%s ===",
        market_a, market_b, kalshi_bankroll, polymarket_bankroll,
    )
    flag_row, problems = fetch_arbitrage_flag(market_a, market_b)
    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Arbitrage sizing request rejected: %s", result["reason"])
        return result

    result = size_arbitrage_position(flag_row, kalshi_bankroll, polymarket_bankroll)
    log.info("Arbitrage sizing result: %s", result)
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def run(flag_ids: list[str], bankroll: float) -> dict:
    log.info("=== Sizing run starting: flag_ids=%s, bankroll=%s ===", flag_ids, bankroll)
    legs, problems = fetch_legs(flag_ids)

    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Sizing request rejected: %s", result["reason"])
        return result

    result = size_entry(legs, bankroll)
    log.info("Sizing result: %s", result)
    return result


if __name__ == "__main__":
    import json

    parser = argparse.ArgumentParser(
        description="Session 2.6 pick'em sizing and Session 3.3 arbitrage sizing."
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    # -- pickem (Session 2.6, unchanged behavior, now under a subcommand) --
    pickem_parser = subparsers.add_parser(
        "pickem", help=f"Size a {SUPPORTED_ENTRY_TYPE} entry from data/pickem/clv_log.csv."
    )
    pickem_parser.add_argument(
        "--flag-ids",
        type=str,
        nargs="+",
        required=True,
        help=f"Exactly {SUPPORTED_LEG_COUNT} flag_id values from data/pickem/clv_log.csv "
        f"to combine into one {SUPPORTED_ENTRY_TYPE} (e.g. --flag-ids "
        f'"prizepicks|123" "prizepicks|456").',
    )
    pickem_parser.add_argument(
        "--bankroll", type=float, required=True, help="Total real bankroll available, in dollars."
    )

    # -- arbitrage (Session 3.3, new) --
    arb_parser = subparsers.add_parser(
        "arbitrage", help="Size, record, or settle an arbitrage position from detector.py's flags."
    )
    arb_subparsers = arb_parser.add_subparsers(dest="action", required=True)

    arb_size = arb_subparsers.add_parser(
        "size", help="Compute a suggested position size for one flagged pair."
    )
    arb_size.add_argument("--market-a", type=str, required=True, help="market_a or market_b id from the flag.")
    arb_size.add_argument("--market-b", type=str, required=True, help="The other market id from the flag.")
    arb_size.add_argument(
        "--kalshi-bankroll", type=float, required=True, help="Real dollars currently in the Kalshi account."
    )
    arb_size.add_argument(
        "--polymarket-bankroll", type=float, required=True, help="Real dollars currently in the Polymarket account."
    )

    arb_record = arb_subparsers.add_parser(
        "record-open",
        help="Size a flagged pair AND record it as a real, placed open position in the ledger.",
    )
    arb_record.add_argument("--market-a", type=str, required=True)
    arb_record.add_argument("--market-b", type=str, required=True)
    arb_record.add_argument("--kalshi-bankroll", type=float, required=True)
    arb_record.add_argument("--polymarket-bankroll", type=float, required=True)

    arb_settle = arb_subparsers.add_parser(
        "settle", help="Mark an open position as settled, freeing its committed capital."
    )
    arb_settle.add_argument("--position-id", type=str, required=True)
    arb_settle.add_argument("--note", type=str, default="", help="Optional free-text settlement note.")

    args = parser.parse_args()

    if args.mode == "pickem":
        summary = run(args.flag_ids, args.bankroll)
        print(summary)

    elif args.mode == "arbitrage":
        if args.action in ("size", "record-open"):
            result = run_arbitrage_sizing(
                args.market_a, args.market_b, args.kalshi_bankroll, args.polymarket_bankroll
            )
            if args.action == "record-open" and result.get("status") in ("sized", "sized_capped"):
                record_result = record_open_arbitrage_position(result)
                result["ledger_record"] = record_result
            print(json.dumps(result, indent=2, default=str))

        elif args.action == "settle":
            result = settle_arbitrage_position(args.position_id, args.note)
            print(json.dumps(result, indent=2, default=str))
