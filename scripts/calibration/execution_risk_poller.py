"""
Session 3.3 continuation -- Execution Risk Poller (Open Decision #23)

WHAT THIS SCRIPT IS
--------------------
Open Decision #23 (`EXECUTION_RISK_BUFFER = 0.85` in `sizing_engine.py`)
needed real minutes-scale evidence of how much a flagged arbitrage
position's fillable size decays between when it's flagged and when a
human could actually place both real orders. Two things this project
already tried both fell short:
  - Session 3.3's original check (67% swing in 13-30 real minutes) was
    real but a single before/after pair -- too thin to set a number from.
  - Revisiting it 2026-09-11 against `detector.py`'s own accumulated
    snapshot history found the pipeline's ~4-6 hour polling cadence is
    structurally too coarse to see minutes-scale decay at all -- real
    repeated observations either showed 0% change (gaps under 90 min,
    but only one market) or large swings (gaps of several hours, which
    is market movement, not execution risk).

This script is the fix named in both of those write-ups: a dedicated
poller that hits ONE real, currently-flagged pair's live order book
repeatedly at a short, fixed interval (minutes, not hours) for a bounded
real duration, and logs exactly the same fillable-size calculation
`detector.py` uses (via `liquidity_check.estimate_fillable_size()` --
reused directly, not reimplemented) so the numbers are comparable to
what a real trader would have seen at each moment.

WHAT IT DOES NOT DO
-------------------
It does not place any trade, and it does not change EXECUTION_RISK_BUFFER
itself -- per this project's "no silent adjustments" standard (same
posture as KELLY_FRACTION, MIN_SUFFICIENT_LIQUIDITY_DOLLARS, etc.), a
human reviews `--report`'s output and updates the constant in
`sizing_engine.py` directly, with the real evidence cited in the commit,
the same way every other constant in this project has been set.

USAGE
-----
pip install requests --break-system-packages

# Poll a specific real pair (get the tickers/condition-ids from a recent
# arbitrage_flags_*.csv row) every 2 minutes for 20 minutes:
python execution_risk_poller.py --poll \
    --market-a HOUSENJ9-26-D --side-a NO --platform-a kalshi \
    --market-b 0x025e8dbab75a4ab8d57838524c61660d8385ed80608a856d7f85fe5be2c3ce82 \
    --side-b YES --platform-b polymarket \
    --interval-seconds 120 --duration-minutes 20

# Or let it pick the single largest real fillable-size opportunity out of
# the latest detector.py run automatically:
python execution_risk_poller.py --poll --auto --interval-seconds 120 --duration-minutes 20

# Summarize every real poll session logged so far:
python execution_risk_poller.py --report
"""

from __future__ import annotations

import argparse
import csv
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "arbitrage"))
from liquidity_check import estimate_fillable_size  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
LATEST_FLAGS_PATH = BASE_DIR / "data" / "arbitrage" / "flags" / "arbitrage_flags_latest.csv"
POLLS_DIR = BASE_DIR / "data" / "arbitrage" / "execution_risk_polls"
LOG_PATH = BASE_DIR / "logs" / "execution_risk_poller.log"

KALSHI_MARKETS_ENDPOINT = "https://api.elections.kalshi.com/trade-api/v2/markets"
POLYMARKET_MARKETS_ENDPOINT = "https://gamma-api.polymarket.com/markets"

REQUEST_TIMEOUT_SECONDS = 15


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(LOG_PATH), logging.StreamHandler()],
    )
    return logging.getLogger("execution_risk_poller")


log = logging.getLogger("execution_risk_poller")


def _to_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_kalshi_market(ticker: str) -> Optional[dict]:
    """One real, single-market Kalshi pull -- same endpoint
    `ingest_kalshi.py` uses for bulk pulls, scoped to one ticker so a
    short poll interval stays cheap and fast."""
    try:
        response = requests.get(
            KALSHI_MARKETS_ENDPOINT,
            params={"tickers": ticker},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        markets = response.json().get("markets", [])
        return markets[0] if markets else None
    except (requests.RequestException, ValueError, IndexError) as exc:
        log.warning("Kalshi pull failed for %s: %s", ticker, exc)
        return None


def fetch_polymarket_market(condition_id: str) -> Optional[dict]:
    """One real, single-market Polymarket pull via the Gamma API's
    `condition_ids` filter -- confirmed live 2026-09-11 to return the
    same shape `ingest_polymarket.py` already normalizes from."""
    try:
        response = requests.get(
            POLYMARKET_MARKETS_ENDPOINT,
            params={"condition_ids": condition_id},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        markets = response.json()
        return markets[0] if markets else None
    except (requests.RequestException, ValueError, IndexError) as exc:
        log.warning("Polymarket pull failed for %s: %s", condition_id, exc)
        return None


def _kalshi_row_for_liquidity_check(market: dict) -> dict:
    """Maps Kalshi's raw market payload onto the same field names
    `liquidity_check.py` expects (`yes_ask_size`/`yes_bid_size`) -- same
    mapping `ingest_kalshi.py` already does at bulk-ingest time."""
    return {
        "yes_ask_size": _to_float(market.get("yes_ask_size_fp")),
        "yes_bid_size": _to_float(market.get("yes_bid_size_fp")),
    }


def _polymarket_row_for_liquidity_check(market: dict) -> dict:
    return {"liquidity": _to_float(market.get("liquidity"))}


def _price_for_side(market: dict, platform: str, side: str) -> Optional[float]:
    if platform == "kalshi":
        key = "yes_ask_dollars" if side == "YES" else "no_ask_dollars"
        return _to_float(market.get(key))
    if platform == "polymarket":
        # Gamma API's market summary exposes one outcome price array
        # (YES first, NO second) rather than separate named fields --
        # confirmed against the same real payload used in this file's
        # docstring example.
        prices = market.get("outcomePrices")
        if isinstance(prices, str):
            import json as _json

            try:
                prices = _json.loads(prices)
            except ValueError:
                prices = None
        if not prices:
            return None
        yes_price = _to_float(prices[0])
        if yes_price is None:
            return None
        return yes_price if side == "YES" else round(1.0 - yes_price, 4)
    return None


def poll_once(
    market_a: str, side_a: str, platform_a: str,
    market_b: str, side_b: str, platform_b: str,
) -> dict:
    """One real, timestamped read of both legs' live order books, run
    through the exact same `estimate_fillable_size()` detector.py uses --
    so this poll's numbers are directly comparable to a real flagged
    row's `fillable_size_dollars`."""
    fetchers = {"kalshi": fetch_kalshi_market, "polymarket": fetch_polymarket_market}
    row_mappers = {
        "kalshi": _kalshi_row_for_liquidity_check,
        "polymarket": _polymarket_row_for_liquidity_check,
    }

    raw_a = fetchers[platform_a](market_a)
    raw_b = fetchers[platform_b](market_b)

    row_a = row_mappers[platform_a](raw_a) if raw_a else None
    row_b = row_mappers[platform_b](raw_b) if raw_b else None

    price_a = _price_for_side(raw_a, platform_a, side_a) if raw_a else None
    price_b = _price_for_side(raw_b, platform_b, side_b) if raw_b else None

    fillable = estimate_fillable_size(
        row_a, side_a, platform_a, price_a,
        row_b, side_b, platform_b, price_b,
    )

    return {
        "polled_at": datetime.now(timezone.utc).isoformat(),
        "market_a": market_a,
        "price_a": price_a,
        "market_b": market_b,
        "price_b": price_b,
        "fillable_size_dollars": fillable["fillable_size_dollars"],
        "fillable_size_basis": fillable["basis"],
        "leg_a_fetch_ok": raw_a is not None,
        "leg_b_fetch_ok": raw_b is not None,
    }


def _auto_pick_pair() -> Optional[dict]:
    """Picks the real flagged row with the largest current
    `fillable_size_dollars` out of the latest detector.py run -- the
    opportunity most likely to still have meaningful size left to poll,
    rather than an already-thin one."""
    if not LATEST_FLAGS_PATH.exists():
        log.error("No latest flags file found at %s -- run detector.py first.", LATEST_FLAGS_PATH)
        return None
    with LATEST_FLAGS_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        log.error("Latest flags file is empty -- nothing real to poll.")
        return None
    best = max(rows, key=lambda r: _to_float(r.get("fillable_size_dollars")) or 0.0)
    return {
        "market_a": best["market_a"],
        "side_a": best["leg_a_side"],
        "platform_a": best["platform_a"],
        "market_b": best["market_b"],
        "side_b": best["leg_b_side"],
        "platform_b": best["platform_b"],
    }


def run_poll_session(
    market_a: str, side_a: str, platform_a: str,
    market_b: str, side_b: str, platform_b: str,
    interval_seconds: int, duration_minutes: int,
) -> Path:
    POLLS_DIR.mkdir(parents=True, exist_ok=True)
    session_started = datetime.now(timezone.utc)
    out_path = POLLS_DIR / f"poll_{session_started.strftime('%Y-%m-%dT%H-%M-%SZ')}.csv"

    total_polls = max(1, (duration_minutes * 60) // interval_seconds + 1)
    log.info(
        "Starting real execution-risk poll: %s/%s (%s) vs %s/%s (%s), "
        "every %ds for %d min (%d polls total) -> %s",
        platform_a, market_a, side_a, platform_b, market_b, side_b,
        interval_seconds, duration_minutes, total_polls, out_path,
    )

    fieldnames = [
        "polled_at", "market_a", "price_a", "market_b", "price_b",
        "fillable_size_dollars", "fillable_size_basis",
        "leg_a_fetch_ok", "leg_b_fetch_ok",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(total_polls):
            reading = poll_once(market_a, side_a, platform_a, market_b, side_b, platform_b)
            writer.writerow(reading)
            f.flush()
            log.info(
                "Poll %d/%d: fillable=$%.2f (basis=%s)",
                i + 1, total_polls,
                reading["fillable_size_dollars"] or 0.0,
                reading["fillable_size_basis"],
            )
            if i < total_polls - 1:
                time.sleep(interval_seconds)

    log.info("Real poll session complete -- %d readings written to %s", total_polls, out_path)
    return out_path


def report() -> None:
    """Summarizes every real poll session on disk: for each, the worst
    (most negative) real fillable-size change observed between any two
    consecutive readings, and the real gap in minutes that change
    happened over -- the exact evidence Open Decision #23 needs."""
    if not POLLS_DIR.exists():
        print("No poll sessions found yet -- run --poll first.")
        return

    session_files = sorted(POLLS_DIR.glob("poll_*.csv"))
    if not session_files:
        print("No poll sessions found yet -- run --poll first.")
        return

    print(f"{len(session_files)} real poll session(s) found.\n")
    worst_overall = None

    for path in session_files:
        with path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if len(rows) < 2:
            print(f"{path.name}: only {len(rows)} reading, no consecutive gap to measure.")
            continue

        print(f"{path.name} ({len(rows)} real readings, {rows[0]['market_a']} / {rows[0]['market_b']}):")
        worst_pct = None
        for i in range(len(rows) - 1):
            t0 = datetime.fromisoformat(rows[i]["polled_at"])
            t1 = datetime.fromisoformat(rows[i + 1]["polled_at"])
            gap_min = (t1 - t0).total_seconds() / 60
            f0 = _to_float(rows[i]["fillable_size_dollars"])
            f1 = _to_float(rows[i + 1]["fillable_size_dollars"])
            if f0 is None or f1 is None or f0 == 0:
                continue
            pct_change = (f1 - f0) / f0
            print(
                f"  {gap_min:6.1f} min: ${f0:.2f} -> ${f1:.2f} "
                f"({pct_change:+.1%})"
            )
            if worst_pct is None or pct_change < worst_pct:
                worst_pct = pct_change
        if worst_pct is not None:
            print(f"  Worst real observed decay this session: {worst_pct:+.1%}\n")
            if worst_overall is None or worst_pct < worst_overall:
                worst_overall = worst_pct
        else:
            print("  No valid consecutive-reading comparison in this session.\n")

    if worst_overall is not None:
        implied_buffer = round(1.0 + worst_overall, 4) if worst_overall < 0 else 1.0
        print(
            f"Worst real fillable-size decay observed across ALL sessions: "
            f"{worst_overall:+.1%}\n"
            f"(A buffer of {implied_buffer} would exactly cover this one worst "
            f"real observation -- current EXECUTION_RISK_BUFFER is 0.85. This "
            f"is a real data point to inform a human decision, not an "
            f"instruction to auto-apply; see sizing_engine.py's own docstring "
            f"on why this constant is a named judgment call, not a formula.)"
        )


if __name__ == "__main__":
    setup_logging()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--poll", action="store_true", help="Run a real poll session.")
    parser.add_argument("--report", action="store_true", help="Summarize all poll sessions on disk.")
    parser.add_argument("--auto", action="store_true", help="Auto-pick the largest real flagged pair from the latest detector.py run.")
    parser.add_argument("--market-a")
    parser.add_argument("--side-a", choices=["YES", "NO"])
    parser.add_argument("--platform-a", choices=["kalshi", "polymarket"])
    parser.add_argument("--market-b")
    parser.add_argument("--side-b", choices=["YES", "NO"])
    parser.add_argument("--platform-b", choices=["kalshi", "polymarket"])
    parser.add_argument("--interval-seconds", type=int, default=120)
    parser.add_argument("--duration-minutes", type=int, default=20)
    args = parser.parse_args()

    if args.report:
        report()
    elif args.poll:
        if args.auto:
            pair = _auto_pick_pair()
            if pair is None:
                sys.exit(1)
        else:
            required = [args.market_a, args.side_a, args.platform_a, args.market_b, args.side_b, args.platform_b]
            if any(v is None for v in required):
                parser.error("Either pass --auto, or all of --market-a/--side-a/--platform-a/--market-b/--side-b/--platform-b.")
            pair = {
                "market_a": args.market_a, "side_a": args.side_a, "platform_a": args.platform_a,
                "market_b": args.market_b, "side_b": args.side_b, "platform_b": args.platform_b,
            }
        run_poll_session(
            pair["market_a"], pair["side_a"], pair["platform_a"],
            pair["market_b"], pair["side_b"], pair["platform_b"],
            args.interval_seconds, args.duration_minutes,
        )
    else:
        parser.error("Pass --poll (with --auto or explicit market args) or --report.")
