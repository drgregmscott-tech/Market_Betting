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

USAGE
-----
pip install pandas --break-system-packages
python sizing_engine.py --flag-ids "prizepicks|12345678" "prizepicks|87654321" --bankroll 500
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
# Paths -- matching Session 2.2/2.4/2.5's existing repo-relative pattern.
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
LOG_PATH = BASE_DIR / "logs" / "sizing.log"

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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--flag-ids",
        type=str,
        nargs="+",
        required=True,
        help=f"Exactly {SUPPORTED_LEG_COUNT} flag_id values from data/pickem/clv_log.csv "
        f"to combine into one {SUPPORTED_ENTRY_TYPE} (e.g. --flag-ids "
        f'"prizepicks|123" "prizepicks|456").',
    )
    parser.add_argument(
        "--bankroll",
        type=float,
        required=True,
        help="Total real bankroll available, in dollars.",
    )
    args = parser.parse_args()
    summary = run(args.flag_ids, args.bankroll)
    print(summary)
