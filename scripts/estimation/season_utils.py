"""
Session 2.17 follow-up (2026-09-12) -- shared "what season should we
default to" helper. Replaces three separate hardcoded `--season 2025`
literals (`run_full_pipeline.bat`, `.github/workflows/pickem_pipeline.yml`,
`.github/workflows/props_pipeline.yml`) that had already gone stale --
found 5 real days into the 2026 season (first 2026 NFL/CFB games:
2026-09-07) with nobody having updated any of the three, per ROADMAP.md's
Open Decision #9.

WHY A SIMPLE DATE ROLLOVER, AND WHY THAT IS NOT THE WHOLE STORY
--------------------------------------------------------------
NFL/CFB seasons are named by the year they START in (the "2025 season"
runs Sept 2025 - Jan 2026); nflverse and CFBD both publish their season
files under that starting year. This function reproduces that same
convention: from August onward, the current calendar year IS that year's
real season; from January through July, the real current season is still
last year's (the one that just finished, or is still being graded).
August, not September, is used as the rollover month deliberately --
preseason data starts appearing before Week 1, and a year with no real
file yet simply comes back as an honest empty result from that plug-in's
own fetch (the same "no data yet" shape every plug-in already returns),
not a wrong guess.

This resolves the literal-staleness bug -- a value that never updates on
its own -- but deliberately does NOT resolve Open Decision #9's separate,
harder question: once real 2026 games exist but only a handful have been
played, should the model switch cleanly to season=2026 or blend 2025/2026
data during the transition? That decision needs real evidence about how
thin an early-season sample is too thin, which does not exist yet. This
function only answers "which season number is real right now" -- not
"is there enough real data in it to trust yet". That second question
stays with each model's own per-player sample-size handling (and, for
Track 5's DK/FD props, the separate Session 6.6 stale-season-stats guard
in `sportsbook_props_model.py`).

Tennis (Session 2.17) is unaffected by the rollover choice either way --
Sackmann's archive is filed by plain calendar year, and the rollover
month only matters once a year during Jan-Jul, when it's the only plug-in
of the two that actually wants the new year already.
"""

from __future__ import annotations

from datetime import date

# See module docstring for why August, specifically, is the rollover
# point rather than September (Week 1) or January (calendar new year).
SEASON_ROLLOVER_MONTH = 8


def current_pickem_season(today: date | None = None) -> int:
    """The real current NFL/CFB-style season year, computed from today's
    date rather than hardcoded. `today` is only ever overridden in tests."""
    today = today or date.today()
    return today.year if today.month >= SEASON_ROLLOVER_MONTH else today.year - 1
