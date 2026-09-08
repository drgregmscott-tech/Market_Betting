"""
Session 5.2 - Down-Ballot Politics Estimation Engine (Underconfidence-
Correction Model)

WHAT THIS SCRIPT ANSWERS
--------------------------
For every real, live Kalshi/Polymarket down-ballot candidate market
Session 5.1c ingests (one row per race, per party, per venue, matched to
a specific named candidate - see schema_politics.py's module docstring),
this script computes this project's own corrected probability estimate
of that candidate winning, so it can be compared against the venue's own
raw price to find a real, sourced mispricing.

WHY A CORRECTION MODEL, NOT A FROM-SCRATCH FORECAST
--------------------------------------------------------------------------
Weather (Session 4.2) and pick'em (Session 2.3) both built an independent
forecast from scratch, because no independent forecast existed to lean
on. Down-ballot politics is different: ElectIndex already publishes a
real, independent, per-race probability model this project reuses as-is
(see ingest_polling_data.py) - building a second from-scratch election
forecasting model on top of it would duplicate real expert work this
project has no comparative advantage at.

What ElectIndex's own number does NOT do is answer "is Kalshi's or
Polymarket's live price wrong, and by how much, in a way this project
can act on." That is a market-calibration question, not an election-
forecasting question, and it has its own real, published, statistically-
validated answer: political prediction-market prices are measurably
compressed toward 50 cents (Le, 2026, "Decomposing Crowd Wisdom", arXiv
2602.19520v2 - see docs/research/politics_estimation_model_spec.md for
the full re-verification this session ran before trusting this paper).
This script's job is narrow and specific: apply that published,
domain-specific correction directly to the venue's own raw price, so the
gap between the corrected price and the raw price is this project's own
sourced estimate of the mispricing - with ElectIndex's independent
number used as a real, logged sanity check on the result, not as the
estimate itself.

THE CORRECTION FORMULA
--------------------------------------------------------------------------
Le (2026) models calibration as a logistic recalibration: a raw market
price p is mapped to a corrected probability p* via
    p* = sigmoid(a + b * logit(p))
where b is a "calibration slope" (b > 1 means the raw price is too
compressed toward 50%, matching "underconfidence") and a is an intercept
capturing directional bias. For political markets specifically, the
paper's own Table 10 (first-stage intercept summary) reports a Politics
mean intercept of -0.006 - close enough to zero that this model treats
a = 0 for every political race, a real, named simplification, not an
omission (see spec doc for the exact evidence this rests on).

The slope b is domain- and horizon-specific (Table 4 in the paper).
This model uses the Politics row of that table, bucketed by real time-
to-resolution, exactly as published - see POLITICS_SLOPE_BY_HORIZON
below for the sourced numbers.

RE-VERIFICATION FINDING APPLIED, THIS SESSION - DAMPENING FACTOR
--------------------------------------------------------------------------
ROADMAP.md required this finding be re-checked against current sources
before being built into the model, given a noted contested magnitude in
the original Session 0.1 research. Checked live this session: the paper
has since been revised (v2, including a formal peer-review response) to
add a Bayesian measurement-error model that treats each first-stage
slope as uncertain rather than exact. That model's own posterior mean
for the Politics domain intercept effect shrinks to roughly 68.6% of the
raw descriptive estimate (0.107 posterior mean vs 0.156 raw - the
paper's own Section 8.2 comparison), once real estimation noise is
accounted for. The finding survives (its 95% credible interval is
entirely above zero, and it replicates independently on Polymarket), but
its magnitude is smaller than a naive reading of the raw table would
suggest.

This model applies that same shrinkage ratio directly to the horizon
slopes below, as a named, sourced dampening factor
(POSTERIOR_SHRINKAGE_FACTOR), rather than using Table 4's raw numbers at
full strength. This is the cautious choice, consistent with this
project's own weather-model precedent (Session 4.2 chose the upper,
more-cautious end of its own literature range for the same reason):
applying the full, undamped correction risks manufacturing a
false-positive edge from a magnitude the paper's own more careful check
already found to be overstated.

WHY THIS MODEL USES A FIXED, NAMED ELECTION DATE FOR TIME-TO-RESOLUTION
--------------------------------------------------------------------------
This project's own tools-and-api-patterns notes already record a real,
confirmed gotcha: Kalshi's `close_time` field for political contracts
reflects the swearing-in date (~2027), not the election date, and must
not be used for time-proximity logic. This model does not use either
venue's own close_time for the horizon bucket lookup - it uses a single,
named constant, GENERAL_ELECTION_DATE (2026-11-03, the real, fixed date
of the 2026 U.S. general election), applied identically to every race
and every venue, so horizon is computed the same way regardless of which
venue's own close_time field happens to be trustworthy this cycle.

WHAT EVERY OUTPUT ROW CONTAINS
--------------------------------------------------------------------------
One row per (race_id, party) - matching ElectIndex's own two-number-per-
race structure (see ingest_polling_data.py). Each row carries both
venues' own raw price, corrected estimate, and an explicit
`kalshi_model_status` / `polymarket_model_status` explaining why a venue
could not be estimated when that's the case - nothing silently skipped,
same standard every other estimation script in this project already
sets:

`estimated` - `no_market_price` (no open market matched this candidate
at this venue) - `no_electindex_prob` (ElectIndex published no
probability for this party in this race - a real, observed case, e.g. an
uncontested race)

WHERE OUTPUT GOES
------------------
/data/politics/estimates/politics_estimates_<timestamp>.csv
/data/politics/estimates/politics_estimates_latest.csv (overwritten each run)

USAGE
-----
python politics_model.py
(reads /data/politics/normalized/politics_races_latest.csv and
polling_estimates_latest.csv - run Session 5.1c's ingestion scripts
first)
"""

from __future__ import annotations

import csv
import json
import logging
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parents[2]
RACES_LATEST = BASE_DIR / "data" / "politics" / "normalized" / "politics_races_latest.csv"
POLLING_LATEST = BASE_DIR / "data" / "politics" / "normalized" / "polling_estimates_latest.csv"
ESTIMATES_DIR = BASE_DIR / "data" / "politics" / "estimates"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

# --------------------------------------------------------------------------
# Sourced constants - see module docstring for the full evidence trail.
# --------------------------------------------------------------------------

# Real, fixed date of the 2026 U.S. general election. See module
# docstring's "WHY THIS MODEL USES A FIXED, NAMED ELECTION DATE" section
# for why this is used instead of either venue's own close_time field.
GENERAL_ELECTION_DATE = datetime(2026, 11, 3, tzinfo=timezone.utc)

# Le (2026), "Decomposing Crowd Wisdom: Domain-Specific Calibration
# Dynamics in Prediction Markets," arXiv:2602.19520v2, Table 4 (Politics
# row). Real, published, cell-level calibration slopes by
# time-to-resolution bucket. b > 1.0 means the raw price is compressed
# toward 50 cents (underconfident) at that horizon; the one bucket below
# 1.0 (1-3h) is real and reported as such, not omitted for not fitting
# the "underconfidence" story - Section 6.2 of the paper attributes it to
# a real composition effect (a specific political subcategory dominating
# that narrow bucket), not a genuine reversal.
POLITICS_SLOPE_BY_HORIZON: list[tuple[float, float, float]] = [
    # (min_hours, max_hours, raw_slope_b)
    (0.0, 1.0, 1.34),
    (1.0, 3.0, 0.93),
    (3.0, 6.0, 1.32),
    (6.0, 12.0, 1.55),
    (12.0, 24.0, 1.48),
    (24.0, 48.0, 1.52),
    (48.0, 24.0 * 7, 1.83),
    (24.0 * 7, 24.0 * 30, 1.83),
    (24.0 * 30, math.inf, 1.73),
]

# Le (2026) Table 10: Politics domain mean first-stage intercept is
# -0.006 - close enough to zero (see paper's own A.1: "Politics has a
# mean intercept close to zero, so its slope-based underconfidence
# interpretation is less affected by directional yes/no bias") that this
# model treats it as exactly zero. Named and sourced, not an omission.
POLITICS_INTERCEPT = 0.0

# Le (2026) Section 8.2: the Bayesian measurement-error model's posterior
# mean Politics domain-intercept effect (+0.107) versus the raw
# descriptive estimate (+0.156) - 0.107 / 0.156 = 0.686. Applied as a
# dampening factor on each horizon slope's deviation from 1.0, per this
# module's own "RE-VERIFICATION FINDING APPLIED" docstring section. This
# is this project's own modeling choice (a conservative one), not a
# number the paper itself states as a slope multiplier.
POSTERIOR_SHRINKAGE_FACTOR = 0.107 / 0.156


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("politics_model")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fh = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    ch = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    fmt.converter = time.gmtime
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


log = setup_logging()


def _to_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def slope_for_horizon(hours_to_resolution: float) -> float:
    """Returns the dampened Politics calibration slope for a given real
    time-to-resolution, per POLITICS_SLOPE_BY_HORIZON and
    POSTERIOR_SHRINKAGE_FACTOR above. Horizons beyond the table's last
    bucket (1mo+) use that bucket's own slope (math.inf upper bound), so
    every real horizon resolves to a value - never unsupported, unlike
    the weather model's MAX_LITERATURE_LEAD_DAY cutoff, because Le
    (2026)'s own 1mo+ bucket already has no upper bound."""
    raw_slope = POLITICS_SLOPE_BY_HORIZON[-1][2]
    for lo, hi, b in POLITICS_SLOPE_BY_HORIZON:
        if lo <= hours_to_resolution < hi:
            raw_slope = b
            break
    return 1.0 + (raw_slope - 1.0) * POSTERIOR_SHRINKAGE_FACTOR


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return math.log(p / (1 - p))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def recalibrate(raw_price: float, hours_to_resolution: float) -> tuple[float, float]:
    """Returns (corrected_probability, slope_used)."""
    b = slope_for_horizon(hours_to_resolution)
    corrected = sigmoid(POLITICS_INTERCEPT + b * logit(raw_price))
    return corrected, b


def _mid_price(bid: Optional[float], ask: Optional[float]) -> Optional[float]:
    """Uses the bid/ask midpoint as the raw price being corrected -
    consistent with treating the market price as the crowd's aggregate
    belief rather than either side's own quote. Falls back to whichever
    single side is available (a real, observed case on thin down-ballot
    markets - see Session 5.1's own liquidity findings) rather than
    leaving the row unestimated when only one side has a resting quote."""
    if bid is not None and ask is not None:
        return (bid + ask) / 2.0
    return bid if bid is not None else ask


def hours_until_election(pulled_at: str) -> float:
    try:
        now = datetime.fromisoformat(pulled_at.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        now = datetime.now(timezone.utc)
    delta = GENERAL_ELECTION_DATE - now
    return max(delta.total_seconds() / 3600.0, 0.0)


# --------------------------------------------------------------------------
# Per-venue, per-party estimation
# --------------------------------------------------------------------------

def estimate_side(row: dict, venue: str, party: str, hours_to_resolution: float) -> dict:
    """venue is 'kalshi' or 'polymarket'; party is 'dem' or 'rep'."""
    prefix = f"{venue}_{party}"
    ticker_or_id = row.get(f"{prefix}_ticker") or row.get(f"{prefix}_market_id")

    if not ticker_or_id:
        return {f"{venue}_model_status_{party}": "no_market_price"}

    bid = _to_float(row.get(f"{prefix}_yes_bid"))
    ask = _to_float(row.get(f"{prefix}_yes_ask"))
    raw_price = _mid_price(bid, ask)

    if raw_price is None:
        return {f"{venue}_model_status_{party}": "no_market_price"}

    corrected, slope_used = recalibrate(raw_price, hours_to_resolution)

    return {
        f"{venue}_raw_price_{party}": round(raw_price, 4),
        f"{venue}_corrected_prob_{party}": round(corrected, 4),
        f"{venue}_slope_used_{party}": round(slope_used, 4),
        f"{venue}_edge_vs_raw_{party}": round(corrected - raw_price, 4),
        f"{venue}_model_status_{party}": "estimated",
    }


def build_estimate_rows(races: list[dict], polling_by_race: dict[str, dict]) -> list[dict]:
    out: list[dict] = []
    status_counts: dict[str, int] = {}

    for race in races:
        race_id = race.get("race_id")
        polling = polling_by_race.get(race_id, {})
        pulled_at = race.get("pulled_at") or datetime.now(timezone.utc).isoformat()
        hours_to_resolution = hours_until_election(pulled_at)

        for party in ("dem", "rep"):
            electindex_prob = _to_float(polling.get(f"{party}_win_prob"))
            candidate_name = (
                race.get(f"kalshi_{party}_candidate_name")
                or race.get(f"polymarket_{party}_candidate_name")
                or polling.get(f"{'dem' if party == 'dem' else 'rep'}_name")
                or ""
            )

            out_row = {
                "race_id": race_id,
                "tier": race.get("tier"),
                "state": race.get("state"),
                "chamber": race.get("chamber"),
                "district": race.get("district"),
                "party": party.upper(),
                "candidate_name": candidate_name,
                "electindex_prob": electindex_prob,
                "hours_to_resolution": round(hours_to_resolution, 1),
                "electindex_model_status": "estimated" if electindex_prob is not None else "no_electindex_prob",
            }

            for venue in ("kalshi", "polymarket"):
                venue_result = estimate_side(race, venue, party, hours_to_resolution)
                out_row.update(venue_result)
                # Also compute a divergence-from-ElectIndex sanity check,
                # once both numbers exist - see module docstring's
                # "ElectIndex's independent number used as a real, logged
                # sanity check" note. This does NOT feed back into the
                # corrected estimate itself.
                corrected_key = f"{venue}_corrected_prob_{party}"
                if out_row.get(corrected_key) is not None and electindex_prob is not None:
                    out_row[f"{venue}_edge_vs_electindex_{party}"] = round(
                        out_row[corrected_key] - electindex_prob, 4
                    )

            for key in (f"kalshi_model_status_{party}", f"polymarket_model_status_{party}"):
                status = out_row.get(key, "no_market_price")
                status_counts[status] = status_counts.get(status, 0) + 1

            out.append(out_row)

    log.info("Estimation status counts across all (venue, party) cells: %s", status_counts)
    return out


def load_races() -> list[dict]:
    if not RACES_LATEST.exists():
        raise FileNotFoundError(
            f"{RACES_LATEST} does not exist - run ingest_politics_markets.py "
            "(Session 5.1c) first."
        )
    with RACES_LATEST.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_polling() -> dict[str, dict]:
    if not POLLING_LATEST.exists():
        log.warning(
            "%s does not exist - run ingest_polling_data.py first. "
            "Proceeding with no ElectIndex sanity check for any race "
            "this run.",
            POLLING_LATEST,
        )
        return {}
    with POLLING_LATEST.open(newline="", encoding="utf-8") as f:
        return {row["race_id"]: row for row in csv.DictReader(f) if row.get("race_id")}


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


ESTIMATE_COLUMNS = [
    "race_id", "tier", "state", "chamber", "district", "party", "candidate_name",
    "electindex_prob", "electindex_model_status", "hours_to_resolution",
    "kalshi_raw_price_dem", "kalshi_raw_price_rep",
    "kalshi_corrected_prob_dem", "kalshi_corrected_prob_rep",
    "kalshi_slope_used_dem", "kalshi_slope_used_rep",
    "kalshi_edge_vs_raw_dem", "kalshi_edge_vs_raw_rep",
    "kalshi_edge_vs_electindex_dem", "kalshi_edge_vs_electindex_rep",
    "kalshi_model_status_dem", "kalshi_model_status_rep",
    "polymarket_raw_price_dem", "polymarket_raw_price_rep",
    "polymarket_corrected_prob_dem", "polymarket_corrected_prob_rep",
    "polymarket_slope_used_dem", "polymarket_slope_used_rep",
    "polymarket_edge_vs_raw_dem", "polymarket_edge_vs_raw_rep",
    "polymarket_edge_vs_electindex_dem", "polymarket_edge_vs_electindex_rep",
    "polymarket_model_status_dem", "polymarket_model_status_rep",
]


def run() -> dict:
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    summary = {"races_read": 0, "rows_written": 0, "ok": False}

    log.info("=== Politics estimation run starting (Session 5.2, underconfidence-correction model) ===")

    try:
        races = load_races()
        polling_by_race = load_polling()
        summary["races_read"] = len(races)

        rows = build_estimate_rows(races, polling_by_race)
        summary["rows_written"] = len(rows)
        summary["ok"] = True
    except Exception as exc:  # noqa: BLE001
        log.error("Politics estimation failed for this run: %s", exc)
        rows = []

    snapshot_path = ESTIMATES_DIR / f"politics_estimates_{pulled_at_compact}.csv"
    latest_path = ESTIMATES_DIR / "politics_estimates_latest.csv"
    write_csv(snapshot_path, rows, ESTIMATE_COLUMNS)
    write_csv(latest_path, rows, ESTIMATE_COLUMNS)

    log.info(
        "=== Politics estimation run complete: %d race rows read, %d "
        "(race, party) rows written (%s) ===",
        summary["races_read"], summary["rows_written"],
        "OK" if summary["ok"] else "FAILED",
    )
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
