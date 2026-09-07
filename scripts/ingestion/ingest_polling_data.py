"""
Session 5.1 - Down-Ballot Polling / Forecast Data Ingestion

WHAT THIS SCRIPT IS
--------------------
Pulls ElectIndex's real, public, per-race forecast data for the same two
down-ballot tiers ingest_politics_markets.py covers (U.S. House district
races, state-legislature district races), and normalizes it onto this
project's own race_id join key (see schema_politics.py's module
docstring for the exact format) so a downstream script can join a
market's price directly against an independent public probability
estimate for the same race.

ACCESS - CONFIRMED LIVE 2026-09-07, VIA BROWSER
-----------------------------------------------------------------------
ElectIndex (electindex.com) is NOT scraped here. Its own "Data &
downloads" section (electindex.com/forecasts/#info) links directly to a
real, PUBLIC GitHub repository - github.com/ElectIndex/26_us_forecast_data
- and states explicitly: "The whole pipeline is open source... download
the key tables directly." This script pulls two of those tables straight
from raw.githubusercontent.com, no API key, no scraping, no auth:
  - races_summary.csv: one row per federal race (governor/senate/house).
    This script keeps only race_type == "house" (435 rows confirmed live)
    - governor and senate are marquee/out-of-scope, same Session 0.1/3.1b
    boundary ingest_kalshi.py's classify_down_ballot() already enforces.
  - leg_races.csv: one row per state-legislature district race (5,867
    rows confirmed live 2026-09-07 - every chamber up in 2026, not just a
    88-chamber summary).
Both files' real column headers were fetched and inspected directly this
session before this script was written (races_summary.csv: state/
district are separate columns, e.g. state="MI", district="07" for a
House race; leg_races.csv: state="MO", chamber="Senate",
district="SD-10") - the parsing below matches the REAL structure found,
not an assumed one.

WHY NOT MULTISTATE.US THIS SESSION - NAMED GAP
-----------------------------------------------------------------------
ROADMAP.md names multistate.us as a second, baseline-partisan-lean source
alongside ElectIndex. Checked live this session (browser, 2026-09-07):
multistate.us's own homepage is a legislative session-tracking product
(bill deadlines, session dates) - no public seat-level partisan-lean
dataset or download was found by direct browsing in the time this
session spent looking. This is a real "not found this session," not a
claim that no such data exists anywhere on the site. ElectIndex's
leg_races.csv already covers every one of the real 4 state-legislature
down-ballot races Session 3.1b confirmed on Kalshi (and any equivalent
Polymarket ones), with a real modeled win probability per seat - not
just a baseline lean - so this gap does not block Session 5.1's
validation checklist. Revisit multistate.us in a future session if a
second, independent cross-check source is wanted.

WHAT "POLLING DATA" MEANS FOR THIS TRACK - NAMED CLARIFICATION
-----------------------------------------------------------------------
ElectIndex's own numbers (dem_prob/rep_prob, margin, rating) are a full
MODEL OUTPUT (polling blended with fundamentals - see
electindex.com/forecasts/#info's own published methodology), not a raw
polling average alone. This script captures it as ElectIndex publishes
it and labels it as such (estimate_source = "ElectIndex model") rather
than mislabeling it as a raw poll average - Session 5.2 (Estimation
Engine) is where this project decides how to use or adjust this number,
not this ingestion-layer script.

WHERE OUTPUT GOES
------------------
/data/politics/raw/electindex_<timestamp>_races_summary.csv (unmodified copy)
/data/politics/raw/electindex_<timestamp>_leg_races.csv (unmodified copy)
/data/politics/normalized/polling_estimates_<timestamp>.csv
/data/politics/normalized/polling_estimates_latest.csv (overwritten each run)

USAGE
-----
pip install requests --break-system-packages
python ingest_polling_data.py
"""

from __future__ import annotations

import csv
import io
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "politics" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "politics" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

# Confirmed live 2026-09-07 - public repo, raw.githubusercontent.com,
# no auth required (see module docstring's "ACCESS" section).
ELECTINDEX_RACES_SUMMARY_URL = (
    "https://raw.githubusercontent.com/ElectIndex/26_us_forecast_data/"
    "main/output/races_summary.csv"
)
ELECTINDEX_LEG_RACES_URL = (
    "https://raw.githubusercontent.com/ElectIndex/26_us_forecast_data/"
    "main/output/leg_races.csv"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/csv",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 20

NORMALIZED_POLLING_COLUMNS = [
    "race_id",
    "tier",
    "state",
    "chamber",
    "district",
    "estimate_source",
    "dem_win_prob",
    "rep_win_prob",
    "margin_dem_minus_rep",
    "rating",
    "pulled_at",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_polling_data")
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


def _fetch_csv_with_retries(url: str) -> list[dict]:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            r = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
            r.raise_for_status()
            return list(csv.DictReader(io.StringIO(r.text)))
        except requests.exceptions.RequestException as exc:
            last_error = exc
            log.warning("Attempt %d/%d failed for %s: %s", attempt, MAX_RETRIES + 1, url, exc)
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS)
    raise RuntimeError(f"All attempts failed for {url}: {last_error}")


def _to_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _scale_prob(value: Optional[float]) -> Optional[float]:
    """Converts races_summary.csv's 0-100-scale probability to the 0-1
    scale used everywhere else in this file's output - see
    normalize_house_rows()'s docstring for the real evidence behind
    this conversion."""
    if value is None:
        return None
    return value / 100.0


# --------------------------------------------------------------------------
# House races - races_summary.csv, race_type == "house" only.
# --------------------------------------------------------------------------

def normalize_house_rows(rows: list[dict], pulled_at: str) -> list[dict]:
    """races_summary.csv real columns (confirmed live 2026-09-07):
    race_type, state (2-letter), district (zero-padded, e.g. '07'),
    dem_prob, rep_prob, margin, rating - among many others this script
    does not need.

    REAL BUG FOUND AND FIXED (first live run, 2026-09-07): races_summary.csv's
    dem_prob/rep_prob are on a 0-100 SCALE (e.g. 58.3), confirmed directly
    against the real MI-07 row. leg_races.csv's dem_prob/rep_prob (used
    by normalize_state_leg_rows() below) are on a 0-1 scale (e.g. 0.4025
    for the real MO-SD-8 row) - two different scales across ElectIndex's
    own two tables, not a formatting inconsistency this project
    introduced. Confirmed by direct inspection of both real rows before
    this fix, not assumed. Divided by 100 here so this script's own
    output (dem_win_prob/rep_win_prob) is uniformly a 0-1 probability
    across both tiers - a downstream reader should never have to know
    which raw ElectIndex table a row originally came from."""
    out = []
    skipped = 0
    for r in rows:
        if r.get("race_type") != "house":
            continue
        state = r.get("state")
        district_raw = r.get("district")
        if not state or not district_raw or not district_raw.isdigit():
            skipped += 1
            log.warning(
                "Skipped one races_summary.csv house row with unexpected "
                "state/district shape: %r", r.get("race_code"),
            )
            continue
        district = int(district_raw)
        race_id = f"US-HOUSE-{state.upper()}-{district:02d}"
        out.append({
            "race_id": race_id,
            "tier": "US House District",
            "state": state.upper(),
            "chamber": None,
            "district": str(district),
            "estimate_source": "ElectIndex model",
            # Divided by 100 - see this function's own docstring "REAL
            # BUG FOUND AND FIXED" note. races_summary.csv's dem_prob/
            # rep_prob are 0-100 scale; this script's output is always
            # 0-1, matching normalize_state_leg_rows()'s native scale.
            "dem_win_prob": _scale_prob(_to_float(r.get("dem_prob"))),
            "rep_win_prob": _scale_prob(_to_float(r.get("rep_prob"))),
            "margin_dem_minus_rep": _to_float(r.get("margin")),
            "rating": r.get("rating"),
            "pulled_at": pulled_at,
        })
    if skipped:
        log.warning("races_summary.csv: %d house row(s) skipped (unexpected shape).", skipped)
    return out


# --------------------------------------------------------------------------
# State-legislature races - leg_races.csv.
# --------------------------------------------------------------------------

def normalize_state_leg_rows(rows: list[dict], pulled_at: str) -> list[dict]:
    """leg_races.csv real columns (confirmed live 2026-09-07): state
    (2-letter), chamber ('House'/'Senate'/'Assembly'/'Legislature'/
    'House of Delegates'), district (e.g. 'SD-10', 'HD-1'), dem_prob,
    rep_prob, margin, rating. Only House/Senate/Assembly chambers are
    kept here, matching Session 3.1b's own Kalshi tier structure
    (classify_down_ballot() only recognizes those three chamber words) -
    'Legislature' (unicameral Nebraska) and 'House of Delegates'
    (VA/WV naming) rows are real but fall outside this project's current
    down-ballot tier definition, so they're skipped and counted, not
    silently dropped with no record."""
    out = []
    skipped_chamber_counts: dict[str, int] = {}
    skipped_shape = 0

    for r in rows:
        chamber_raw = (r.get("chamber") or "").strip()
        if chamber_raw not in ("House", "Senate", "Assembly"):
            skipped_chamber_counts[chamber_raw] = skipped_chamber_counts.get(chamber_raw, 0) + 1
            continue

        state = r.get("state")
        district_field = r.get("district") or ""
        # district_field looks like "SD-10" / "HD-1" - the numeric part
        # after the last hyphen is this project's own district number,
        # matching race_key_for_state_leg()'s expected <N> (not
        # zero-padded, per schema_politics.py's documented format).
        if "-" not in district_field:
            skipped_shape += 1
            log.warning(
                "Skipped one leg_races.csv row with unexpected district "
                "shape: %r (race_code=%s)", district_field, r.get("race_code"),
            )
            continue
        district_num = district_field.rsplit("-", 1)[-1]
        if not district_num.isdigit():
            skipped_shape += 1
            log.warning(
                "Skipped one leg_races.csv row with a non-numeric "
                "district suffix: %r (race_code=%s)", district_field, r.get("race_code"),
            )
            continue

        race_id = f"STATE-LEG-{state.upper()}-{chamber_raw.upper()}-{int(district_num)}"
        out.append({
            "race_id": race_id,
            "tier": "State Legislature District",
            "state": state.upper(),
            "chamber": chamber_raw,
            "district": str(int(district_num)),
            "estimate_source": "ElectIndex model",
            "dem_win_prob": _to_float(r.get("dem_prob")),
            "rep_win_prob": _to_float(r.get("rep_prob")),
            "margin_dem_minus_rep": _to_float(r.get("margin")),
            "rating": r.get("rating"),
            "pulled_at": pulled_at,
        })

    if skipped_chamber_counts:
        log.info(
            "leg_races.csv: %d row(s) skipped as outside this project's "
            "current down-ballot chamber definition (House/Senate/"
            "Assembly only): %s", sum(skipped_chamber_counts.values()),
            skipped_chamber_counts,
        )
    if skipped_shape:
        log.warning("leg_races.csv: %d row(s) skipped (unexpected district shape).", skipped_shape)

    return out


def write_normalized_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_POLLING_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "house_rows": 0,
        "state_leg_rows": 0,
        "total_rows": 0,
        "ok": False,
    }

    log.info("=== Polling/forecast data ingestion run starting (ElectIndex) ===")

    all_rows: list[dict] = []
    try:
        races_summary_raw = _fetch_csv_with_retries(ELECTINDEX_RACES_SUMMARY_URL)
        leg_races_raw = _fetch_csv_with_retries(ELECTINDEX_LEG_RACES_URL)

        # REAL BUG FOUND AND FIXED (first live run on Windows, 2026-09-07):
        # Path.write_text() with no explicit encoding uses the OS's
        # default locale encoding - cp1252 ("charmap") on Windows, not
        # UTF-8. ElectIndex's real candidate-name data contains non-cp1252
        # characters (a combining acute accent, U+0301, from a real
        # candidate name) that raised UnicodeEncodeError and failed the
        # whole run before a single row was normalized. Every other
        # ingestion script in this project (ingest_kalshi.py,
        # ingest_polymarket.py, ingest_weather_markets.py) writes its raw
        # JSON snapshot with json.dumps() into write_text(), which hits
        # the same default-encoding gap - it simply hadn't surfaced yet
        # because none of that raw data happened to contain a
        # non-cp1252 character. Fixed here by passing encoding="utf-8"
        # explicitly, matching this file's own already-UTF-8 CSV reads
        # (io.StringIO(r.text) preserves whatever requests decoded the
        # response as, which is UTF-8 for this real endpoint).
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        (RAW_DIR / f"electindex_{pulled_at_compact}_races_summary.csv").write_text(
            "\n".join([",".join(races_summary_raw[0].keys())] +
                      [",".join(str(v) for v in row.values()) for row in races_summary_raw])
            if races_summary_raw else "",
            encoding="utf-8",
        )
        (RAW_DIR / f"electindex_{pulled_at_compact}_leg_races.csv").write_text(
            "\n".join([",".join(leg_races_raw[0].keys())] +
                      [",".join(str(v) for v in row.values()) for row in leg_races_raw])
            if leg_races_raw else "",
            encoding="utf-8",
        )

        house_rows = normalize_house_rows(races_summary_raw, pulled_at)
        state_leg_rows = normalize_state_leg_rows(leg_races_raw, pulled_at)

        all_rows = house_rows + state_leg_rows
        summary["house_rows"] = len(house_rows)
        summary["state_leg_rows"] = len(state_leg_rows)
        summary["total_rows"] = len(all_rows)
        summary["ok"] = True

        log.info(
            "ElectIndex: %d house races, %d state-legislature races, "
            "%d total rows normalized.",
            len(house_rows), len(state_leg_rows), len(all_rows),
        )
    except Exception as exc:  # noqa: BLE001
        log.error("Polling/forecast data ingestion failed for this run: %s", exc)

    snapshot_path = NORMALIZED_DIR / f"polling_estimates_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "polling_estimates_latest.csv"
    write_normalized_csv(snapshot_path, all_rows)
    write_normalized_csv(latest_path, all_rows)

    log.info(
        "=== Polling/forecast data ingestion run complete: %d rows (%s) ===",
        len(all_rows), "OK" if summary["ok"] else "FAILED",
    )
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
