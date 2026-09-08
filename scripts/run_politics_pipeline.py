"""
Session 5.5 -- Automation Adaptation (Down-Ballot Politics Track Orchestrator)

WHAT THIS SCRIPT IS
--------------------
Runs Track 4 (down-ballot politics)'s four existing stages back-to-back, in
the correct order, in one process: race-market ingestion (Session 5.1) ->
polling/forecast data ingestion (Session 5.1) -> estimation (Session 5.2,
underconfidence-correction model) -> CLV logging (Session 5.3, shared
clv_logger.py). This is the single entry point GitHub Actions
(.github/workflows/politics_pipeline.yml, this same session) calls on a
schedule. It is this track's twin of scripts/run_pipeline.py (Session 2.7,
pick'em) and scripts/run_arbitrage_pipeline.py (Session 3.4, arbitrage) --
same importlib-by-path module loading, same "never let a stage's failure
silently flow into the next stage" stance, same digest-file pattern, rather
than inventing a third orchestration style for this fourth track.

This script does NOT call sizing_engine.py's `politics size` command
(Session 5.4). Same reasoning as the other two orchestrators: sizing needs
a human-supplied bankroll figure and a decision about which specific
flagged race/party is worth acting on -- there is nothing for an unattended
job to decide there. This project's standing "flags and sizes, never places
bets" rule (ROADMAP.md) means the automation's job ends at producing a
clear, reviewable list of open flags; a human still runs
`sizing_engine.py politics size` by hand against whichever flag_id they
choose.

WHY THIS STOPS EARLY IF EITHER INGESTION STAGE RETURNS 0 ROWS, OR IF
ESTIMATION PRODUCES 0 ROWS
------------------------------------------------------------------
clv_logger.py's run_politics() treats "this flag_id did not appear in the
latest estimates file" as "the market closed" and freezes closing values
for it -- correct when a race genuinely resolves or a venue genuinely pulls
a market, wrong if a transient network problem or upstream outage (Kalshi,
Polymarket, or the ElectIndex CSV endpoints) made ingestion or estimation
come back empty. A half-broken run must never look like a normal one and
silently mark every currently-open politics flag "closed" with meaningless
closing values. So: if race ingestion, polling ingestion, or estimation
returns 0 usable rows, this script stops immediately, BEFORE calling
clv_logger.py, and reports exactly why. Nothing gets written to
data/politics/clv_log.csv on a run where an upstream stage failed.

FILES TOUCHED
-------------
Reads/writes the same files the four underlying scripts already use
(data/politics/raw, data/politics/normalized, data/politics/estimates,
data/politics/clv_log.csv, data/politics/clv_snapshots/). Additionally
writes:
- output/digest/politics_digest_latest.md -- always overwritten, the
  current snapshot. Kept as a SEPARATE file from the pick'em and arbitrage
  digests so the three tracks' automated digests never overwrite each
  other.
- output/digest/politics_digest_<timestamp>.md -- one dated copy per run.
- logs/politics_pipeline.log -- orchestrator-level log, separate from each
  stage's own log file (ingestion.log, estimation.log, clv_logging.log),
  so a pipeline-level failure is findable without digging through three
  logs.

USAGE
-----
python scripts/run_politics_pipeline.py
Exit code 0 = pipeline completed; clv_log.csv was updated (even if 0 flags
              are currently open -- a real empty result is not a failure).
Exit code 1 = pipeline stopped early; clv_log.csv was NOT touched this run.
"""

from __future__ import annotations

import argparse
import importlib.util
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INGEST_RACES_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_politics_markets.py"
INGEST_POLLING_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_polling_data.py"
MODEL_SCRIPT = BASE_DIR / "scripts" / "estimation" / "politics_model.py"
CLV_SCRIPT = BASE_DIR / "scripts" / "calibration" / "clv_logger.py"
CLV_LOG_PATH = BASE_DIR / "data" / "politics" / "clv_log.csv"
DIGEST_DIR = BASE_DIR / "output" / "digest"
LOG_PATH = BASE_DIR / "logs" / "politics_pipeline.log"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("run_politics_pipeline")
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


def load_module(path: Path, name: str) -> ModuleType:
    """Loads one of the existing politics-track scripts as a Python module
    by file path, so this orchestrator can call its run() function
    directly and get real Python exceptions back -- no stdout-parsing, no
    subprocess exit-code guessing. Identical reasoning and mechanism to
    run_pipeline.py's and run_arbitrage_pipeline.py's own load_module(),
    duplicated here (not imported from there) so all three orchestrators
    stay fully independent -- a future change to one track's loading
    behavior should never silently affect another."""
    script_dir = str(path.parent)
    sys.path.insert(0, script_dir)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load {path} as a module.")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(script_dir)


class PipelineStageFailed(Exception):
    """Raised when a stage completes without a Python exception but its
    output is empty/unusable in a way that must not be allowed to flow
    into clv_logger.py. Kept distinct from a real exception so the digest
    can report a clear, specific reason instead of a traceback. Identical
    role to the other two orchestrators' own PipelineStageFailed."""


def run_races_ingestion() -> dict:
    log.info("--- Stage 1/4: race-market ingestion (Kalshi + Polymarket) ---")
    module = load_module(INGEST_RACES_SCRIPT, "ingest_politics_markets")
    summary = module.run()
    log.info("Race-market ingestion summary: %s", summary)

    if not summary.get("ok") or not summary.get("races_total"):
        raise PipelineStageFailed(
            "Race-market ingestion returned 0 usable race rows "
            f"(ok={summary.get('ok')}, races_total={summary.get('races_total')}). "
            "Stopping before polling ingestion/estimation/CLV logging so a "
            "transient Kalshi/Polymarket outage can never be mistaken for "
            "every down-ballot race closing."
        )
    return summary


def run_polling_ingestion() -> dict:
    log.info("--- Stage 2/4: polling/forecast data ingestion (ElectIndex) ---")
    module = load_module(INGEST_POLLING_SCRIPT, "ingest_polling_data")
    summary = module.run()
    log.info("Polling ingestion summary: %s", summary)

    if not summary.get("ok") or not summary.get("total_rows"):
        raise PipelineStageFailed(
            "Polling/forecast data ingestion returned 0 usable rows "
            f"(ok={summary.get('ok')}, total_rows={summary.get('total_rows')}). "
            "Stopping before estimation/CLV logging -- the estimation model "
            "needs a real ElectIndex baseline for every race, not an "
            "outage-driven empty file."
        )
    return summary


def run_estimation() -> tuple[dict, Path]:
    log.info("--- Stage 3/4: estimation (underconfidence-correction model) ---")
    module = load_module(MODEL_SCRIPT, "politics_model")
    summary = module.run()
    log.info("Estimation summary: %s", summary)

    out_path = Path(summary["snapshot_path"]) if "snapshot_path" in summary else None
    if out_path is None or not out_path.exists():
        raise PipelineStageFailed(
            f"Estimation did not produce a readable output file (summary={summary})."
        )
    if not summary.get("ok") or not summary.get("rows_written"):
        raise PipelineStageFailed(
            f"Estimation produced 0 output rows (summary={summary}). "
            "Stopping before CLV logging."
        )
    return summary, out_path


def run_clv_logging(estimates_path: Path) -> dict:
    log.info("--- Stage 4/4: CLV logging ---")
    clv_module = load_module(CLV_SCRIPT, "clv_logger")
    summary = clv_module.run_politics(estimates_path)
    log.info("CLV logging summary: %s", summary)
    return summary


def build_digest(
    run_started_at: str,
    races_summary: dict,
    polling_summary: dict,
    estimation_summary: dict,
    clv_summary: dict,
) -> Path:
    """Writes a plain-language summary of this run plus a table of every
    currently OPEN politics flag, read straight from the just-updated
    clv_log.csv. This is the file a person actually looks at to decide
    which race/party flags, if any, are worth manually running through
    `sizing_engine.py politics size` -- the automation's output ends here;
    sizing stays a human decision, per this project's standing rule."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")

    lines: list[str] = []
    lines.append(f"# Politics Pipeline Digest -- {run_started_at}")
    lines.append("")
    lines.append("## Run summary")
    lines.append(
        f"- Race-market ingestion: {races_summary.get('races_total', 0)} races "
        f"({races_summary.get('races_both_venues', 0)} on both venues, "
        f"{races_summary.get('kalshi_series_matched', 0)} Kalshi series matched)"
    )
    lines.append(
        f"- Polling ingestion: {polling_summary.get('total_rows', 0)} rows "
        f"({polling_summary.get('house_rows', 0)} House, "
        f"{polling_summary.get('state_leg_rows', 0)} state legislature)"
    )
    lines.append(
        f"- Estimation: {estimation_summary.get('rows_written', 0)} (race, party) "
        f"rows written (from {estimation_summary.get('races_read', 0)} races read)"
    )
    lines.append(
        f"- CLV logging: {clv_summary.get('newly_flagged', 0)} newly flagged, "
        f"{clv_summary.get('newly_closed', 0)} newly closed, "
        f"{clv_summary.get('still_open', 0)} still open "
        f"({clv_summary.get('total_logged', 0)} total ever logged)"
    )
    lines.append("")

    lines.append("## Currently open flags")
    lines.append(
        "Sizing is a manual step (`sizing_engine.py politics size`, Session "
        "5.4) -- this table is what to scan to pick a race/party worth "
        "sizing. `hours_to_resolution` matters here more than for the other "
        "two tracks: politics positions can sit open for weeks or months "
        "(Session 5.4's lockup dampener)."
    )
    lines.append("")

    if CLV_LOG_PATH.exists():
        clv_df = pd.read_csv(CLV_LOG_PATH)
        open_df = clv_df.loc[clv_df["status"] == "open"].copy()
        if len(open_df) == 0:
            lines.append("_No open flags right now._")
        else:
            cols = [
                "flag_id", "race_id", "candidate_name", "flagged_side",
                "first_flagged_model_prob", "first_flagged_market_price",
                "first_flagged_edge", "hours_to_resolution", "first_flagged_at",
            ]
            cols = [c for c in cols if c in open_df.columns]
            open_df = open_df[cols].sort_values("first_flagged_edge", ascending=False)
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "---|" * len(cols))
            for _, row in open_df.iterrows():
                lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    else:
        lines.append("_clv_log.csv does not exist yet._")

    digest_text = "\n".join(lines) + "\n"

    latest_path = DIGEST_DIR / "politics_digest_latest.md"
    dated_path = DIGEST_DIR / f"politics_digest_{timestamp_compact}.md"
    latest_path.write_text(digest_text, encoding="utf-8")
    dated_path.write_text(digest_text, encoding="utf-8")
    log.info("Wrote digest to %s and %s", latest_path, dated_path)
    return latest_path


def build_failure_digest(run_started_at: str, reason: str) -> Path:
    """A stopped run still gets a digest -- so a failure is visible by
    opening a file, not just by reading Actions logs. Same reasoning as
    the other two orchestrators' build_failure_digest()."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")
    text = (
        f"# Politics Pipeline Digest -- {run_started_at}\n\n"
        f"## RUN FAILED\n\n"
        f"{reason}\n\n"
        f"data/politics/clv_log.csv was NOT modified this run.\n"
    )
    latest_path = DIGEST_DIR / "politics_digest_latest.md"
    dated_path = DIGEST_DIR / f"politics_digest_{timestamp_compact}_FAILED.md"
    latest_path.write_text(text, encoding="utf-8")
    dated_path.write_text(text, encoding="utf-8")
    return latest_path


def main() -> int:
    run_started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log.info("=== Politics pipeline run starting at %s ===", run_started_at)

    try:
        races_summary = run_races_ingestion()
        polling_summary = run_polling_ingestion()
        estimation_summary, estimates_path = run_estimation()
        clv_summary = run_clv_logging(estimates_path)
    except PipelineStageFailed as exc:
        log.error("Pipeline stopped: %s", exc)
        build_failure_digest(run_started_at, str(exc))
        return 1
    except Exception as exc:  # noqa: BLE001 -- deliberately broad: any
        # unexpected exception from any stage must still stop the run and
        # be logged, not crash the orchestrator with a bare traceback that
        # skips the failure digest.
        log.exception("Pipeline stopped on an unexpected error: %s", exc)
        build_failure_digest(run_started_at, f"Unexpected error: {exc}")
        return 1

    build_digest(run_started_at, races_summary, polling_summary, estimation_summary, clv_summary)
    log.info("=== Politics pipeline run complete ===")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()  # no arguments today; kept for symmetry with the
    # other two orchestrators, so a future flag has a place to go without
    # changing the calling convention in the workflow file.
    sys.exit(main())
