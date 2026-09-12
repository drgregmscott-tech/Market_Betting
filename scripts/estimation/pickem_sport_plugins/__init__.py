"""
Session 2.12 -- per-sport plug-in shape for pickem_model.py's estimation
engine.

WHY THIS EXISTS
---------------
Session 2.10's `/docs/research/sport_inventory.md` confirmed the real cost
of pickem_model.py being NFL-only: of ~59,000 real ingested pick'em props
(2026-09-11 scan), only ~2.5% (NFL) were actually scored -- everything else
got a real, visible model_status="unsupported_sport" row and nothing more.
That was a stated v1 scope decision (Session 2.3), not an oversight, but it
means every future sport (MLB, soccer, NBA, CFB, tennis -- Sessions 2.13
through 2.17) needs a real place to plug in without re-copying
pickem_model.py's scoring math per sport.

A SportPlugin bundles everything that actually differs by sport:
  - which of the platforms' own `sport` strings mean "this sport"
  - how to fetch one season's per-player game log for that sport
  - how to resolve a platform's raw stat_type string down to that sport's
    stats-source columns/formulas

The season-avg / recency-weighted "recent form" / sample-sigma / normal-CDF
probability math in pickem_model.py is already sport-agnostic -- it operates
on a plain per-game numeric series regardless of which sport produced it --
and is NOT part of a plug-in. Adding a new sport means adding a new plug-in
file and registering it in PLUGINS below; pickem_model.py's core
process_props() loop does not change.

FETCH_STATS CONTRACT
---------------------
A plug-in's `fetch_stats(season)` must return a DataFrame with at least
these columns, regardless of sport:
  - player_id            (str -- stable identifier from that sport's source)
  - player_display_name  (str -- full name, used for cross-platform matching)
  - sort_key             (sortable, e.g. week number or a date ordinal --
                           chronological order within one player's rows)
plus whatever raw per-game stat columns that sport's stat_type_map /
composite_stat_types / computed_stat_types reference.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

import pandas as pd


@dataclass
class SportPlugin:
    name: str
    sport_labels: frozenset[str]
    fetch_stats: Callable[[int], pd.DataFrame]
    stat_type_map: dict[str, str] = field(default_factory=dict)
    composite_stat_types: dict[str, list[str]] = field(default_factory=dict)
    computed_stat_types: dict[str, Callable[[pd.DataFrame], pd.Series]] = field(default_factory=dict)
    computed_required_columns: dict[str, list[str]] = field(default_factory=dict)


def _load_plugins() -> list[SportPlugin]:
    from .nfl import NFL_PLUGIN
    from .mlb import MLB_PLUGIN
    from .epl import EPL_PLUGIN
    from .soccer import SOCCER_PLUGIN
    from .nba import NBA_PLUGIN

    return [NFL_PLUGIN, MLB_PLUGIN, EPL_PLUGIN, SOCCER_PLUGIN, NBA_PLUGIN]


PLUGINS: list[SportPlugin] = _load_plugins()


def plugin_for_sport(sport_label: str) -> Optional[SportPlugin]:
    """sport_label must already be lowercased/trimmed by the caller (matches
    pickem_model.py's existing normalization before this is called)."""
    for plugin in PLUGINS:
        if sport_label in plugin.sport_labels:
            return plugin
    return None
