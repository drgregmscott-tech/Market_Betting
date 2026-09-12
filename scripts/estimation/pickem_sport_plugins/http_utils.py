"""
Hotfix (2026-09-12) -- shared retry/fault-isolation helper for plug-ins that
make many small per-item HTTP calls (MLB's per-team roster + per-player game
log, Session 2.13; EPL's per-player gameweek history and soccer's
per-match summary, Session 2.14).

WHY THIS EXISTS
----------------
The real GitHub Actions pipeline failed on 2026-09-12 with an unhandled
`requests.exceptions.ReadTimeout` from a single ESPN `summary?event=...`
call, inside `pickem_sport_plugins/soccer.py`'s per-match loop. That single
transient timeout, from ONE match out of hundreds, killed the entire
pipeline run -- ingestion's real 59,317 rows were pulled successfully, but
NO estimation output was written at all, for every sport (NFL/MLB/EPL/
soccer alike), because `fetch_stats()` raising an exception propagates
straight out of `process_props()` with no isolation.

This is a real, structural fragility: every plug-in that fetches per-item
(one HTTP call per game, per player, or per team) rather than one bulk file
(nflverse's single parquet) has hundreds of real chances for one transient
network hiccup to abort the whole run, not just lose one item's data.
MLB's plug-in (Session 2.13) had this same unprotected shape already in
production; this hotfix closes it project-wide rather than patching only
the ESPN call site that happened to fail this time.

WHAT THIS DOES
---------------
`get_json_with_retries()` retries a transient network failure (timeout,
connection error, or a 5xx server response) up to `max_attempts` times with
a short backoff, then raises. Call sites that fetch one ITEM out of many
(a single match, a single player) should catch that final raise, log a
warning naming the item, and skip it -- exactly the same "a real, stated
gap is fine; a silent crash is not" standard this project already applies
to unmapped stat types, just applied to network faults instead of data
gaps. A single missing match or player game log shows up as a slightly
smaller real sample for that one plug-in run, not a blank output file for
every sport.
"""

from __future__ import annotations

import logging
import time

import requests

log = logging.getLogger("pickem_model")


def get_json_with_retries(
    url: str,
    timeout: int = 20,
    max_attempts: int = 3,
    backoff_seconds: float = 2.0,
) -> dict:
    """GETs `url` and returns its parsed JSON body, retrying a failed
    attempt (read/connect timeout, connection error, or a non-2xx response)
    up to `max_attempts` times with a linearly increasing backoff. Raises
    the last real exception if every attempt fails -- the
    caller decides whether that means "abort this whole plug-in" (a
    one-off critical call, e.g. FPL's bootstrap-static) or "skip this one
    item and keep going" (a per-match/per-player call inside a loop)."""
    last_exc: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as exc:
            last_exc = exc
            if attempt < max_attempts:
                log.warning(
                    "HTTP GET failed (attempt %d/%d) for %s: %s -- retrying in %.1fs",
                    attempt, max_attempts, url, exc, backoff_seconds * attempt,
                )
                time.sleep(backoff_seconds * attempt)
    assert last_exc is not None
    raise last_exc
