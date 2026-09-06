"""
Session 4.1 - Kalshi Weather Series -> Official Station Reference Map

WHAT THIS FILE IS
------------------
A hand-built lookup from a Kalshi weather series ticker to the specific,
official government weather station this project uses for BOTH sides of
the comparison: NWS's public forecast (Session 4.2) and NWS's public
observed data (this session), which is the same real-world source
Kalshi's own settlement page (weather.com/kalshi) draws from - confirmed
live, 2026-09-06: that page states its own data is "METAR airport
observations relayed via The Weather Company," for a fixed, named list of
37 stations, each with its own official station code.

This map was built by cross-referencing two real, live sources - not
assumed:
1. Kalshi's own GET /series?category=Climate%20and%20Weather (104 series
   whose ticker starts with KXHIGH or KXLOW, confirmed live).
2. weather.com/kalshi's own "Domestic" station list (37 named
   city/station pairs, confirmed live the same day).

ONLY series with a confirmed, unambiguous match to a station on
weather.com/kalshi's list are included below. Series naming an
international city (Toronto, Paris, Tokyo, Shanghai, Mumbai, Brussels,
Seoul, Amsterdam, Sydney, Sao Paulo, Berlin, Istanbul, Dubai, Hong Kong,
Beijing, Geneva, Mexico City, London, Frankfurt - 20 series found live)
are DELIBERATELY EXCLUDED from Session 4.1's scope: NWS is a United
States government agency and does not publish forecast or observation
data for stations outside the US. This is a real, structural scope
narrowing within Track 3, the same kind of thing Session 3.1 already did
for city/county political races - logged here as such, not silently
dropped. Revisit only if a comparable free, official, non-US government
weather data source is identified for a future session.

NAMED, UNRESOLVED GAPS (do not silently guess past these)
-----------------------------------------------------------------------
Both of this project's original station-identity gaps (Houston, Chicago)
were resolved this session (2026-09-06) against two independent real
sources - a Houston Chronicle article naming "William P. Hobby Airport"
in a real, executed Kalshi weather block trade, and a third-party Kalshi
weather-data vendor's own published station mapping, which separately
confirmed both Houston=Hobby and Chicago=Midway (explicitly flagging
Midway-vs-O'Hare as a known mistake to avoid - this project's own
original KXHIGHCHI mapping was exactly that mistake, caught and fixed
before it reached real sizing). Both are now treated as confirmed, not
placeholders - see SERIES_TICKER_TO_STATION below.

No other station-identity gaps are currently open. A few station codes on
weather.com/kalshi's own list still don't match the airport code this
project would otherwise expect from general knowledge (e.g. West Palm
Beach shown as KDJT, not the more common KPBI) - these are taken as given
from Kalshi's own live reference page rather than overridden, flagged
here so a future session doesn't assume it's this file's typo, but they
are not treated as open decisions the way Houston/Chicago were, since
weather.com/kalshi is itself the authoritative source, not a guess.

Cities appearing on weather.com/kalshi's list but not yet matched to a
live KXHIGH/KXLOW series in this project's Session 3.1 pull (College
Station, Columbus, Gainesville, Jacksonville, Lexington, Louisville,
Milwaukee, Providence, San Jose, St. Petersburg, Tampa, West Palm Beach)
are included below anyway, keyed by city name, in case a future series
discovery run finds a matching ticker - harmless to have an unused
reference row, costly to have to rebuild this map from scratch later.
"""

from typing import Optional

# series_ticker (without KXHIGH/KXLOW/KXHIGHT/KXLOWT prefix ambiguity -
# keyed on the FULL series ticker as returned live by Kalshi) -> station_id
SERIES_TICKER_TO_STATION: dict[str, str] = {
    # -- confirmed, unambiguous matches --
    "KXHIGHAUS": "KAUS", "KXLOWAUS": "KAUS",
    "KXHIGHMIA": "KMIA", "KXLOWMIA": "KMIA",
    "KXHIGHTMIN": "KMSP", "KXLOWTMIN": "KMSP",
    "KXHIGHTPHX": "KPHX", "KXLOWTPHX": "KPHX",
    "KXHIGHTTTN": "KTTN", "KXLOWTTTN": "KTTN",
    "KXHIGHTATL": "KATL", "KXLOWTATL": "KATL",
    "KXHIGHTLV": "KLAS", "KXLOWTLV": "KLAS",
    "KXHIGHNY": "KNYC", "KXHIGHNYD": "KNYC",
    "KXLOWNY": "KNYC", "KXLOWNYC": "KNYC",
    "KXHIGHTDAL": "KDFW", "KXLOWTDAL": "KDFW",
    "KXHIGHTSATX": "KSAT", "KXLOWTSATX": "KSAT",
    "KXHIGHTBOS": "KBOS", "KXLOWTBOS": "KBOS",
    "KXHIGHTSAN": "KSAN", "KXHIGHTKSAN": "KSAN",
    "KXLOWTSAN": "KSAN", "KXLOWTKSAN": "KSAN",
    "KXHIGHTSEA": "KSEA", "KXLOWTSEA": "KSEA",
    "KXHIGHLAX": "KLAX", "KXLOWLAX": "KLAX",
    "KXHIGHDEN": "KDEN", "KXLOWDEN": "KDEN",
    "KXHIGHPHIL": "KPHL", "KXLOWPHIL": "KPHL", "KXLOWTPHIL": "KPHL",
    "KXHIGHTDC": "KDCA", "KXLOWTDC": "KDCA",
    "KXHIGHTNOLA": "KMSY", "KXLOWTNOLA": "KMSY",
    "KXHIGHTSFO": "KSFO", "KXLOWTSFO": "KSFO",
    "KXHIGHTOKC": "KOKC", "KXLOWTOKC": "KOKC",
    "KXHIGHTEWR": "KEWR", "KXLOWTEWR": "KEWR",
    "KXHIGHTOMDB_US_PLACEHOLDER": None,  # not real - guard, see below
    # Louisville: Kalshi's own title text for this ticker reads
    # "HIGHEST Temperature SATX" / "Lowest Temperature SDX" - a real,
    # confirmed Kalshi title/ticker mismatch (ticker code is SDF,
    # Louisville's real airport code, but the human title text
    # incorrectly says "SATX"). Mapped by TICKER (authoritative),
    # not by the mislabeled title text.
    "KXHIGHTSDF": "KSDF", "KXLOWTSDF": "KSDF",

    # -- named, unresolved gaps (see module docstring - do not treat as
    # confirmed) --
    "KXHIGHHOU": "KHOU", "KXLOWHOU": "KHOU",  # Hobby vs Bush - see notes
    "KXHIGHOU": "KHOU", "KXHIGHTHOU": "KHOU", "KXLOWTHOU": "KHOU",
    # ^ SESSION 4.1 CORRECTION (2026-09-06, found from the real first live
    # run, not assumed in advance): Kalshi runs at least three distinct
    # ticker spellings for Houston high temp (KXHIGHHOU, KXHIGHOU,
    # KXHIGHTHOU) and two for low (KXLOWHOU, KXLOWTHOU) - confirmed live,
    # all real series, not a typo on this project's side. All point to
    # the same real city/question and are mapped to the same placeholder
    # station (KHOU) pending the Hobby-vs-Bush confirmation noted above.
    "KXHIGHCHI": "KMDW", "KXLOWCHI": "KMDW", "KXLOWTCHI": "KMDW",
    # ^ SESSION 4.1 CORRECTION (2026-09-06): originally placeholder-mapped
    # to KORD (O'Hare) as a named, unconfirmed guess. Confirmed via a
    # third-party Kalshi weather-data vendor's own published mapping
    # (which explicitly calls out "Chicago = Midway" as a known
    # gotcha - the same kind of mistake this project was trying not to
    # make) that Kalshi's Chicago temperature series settle against
    # Midway, not O'Hare. Corrected here; no longer a placeholder.

    # -- SESSION 4.1 CORRECTION: real ticker variants missed on the first
    # pass, found from the actual first live run's "unmapped" warnings
    # (2026-09-06) rather than assumed complete in advance. Confirmed
    # each of these names the same real city already mapped above under
    # a different ticker spelling. --
    "KXLOWTLAX": "KLAX",   # LA low - KXLOWLAX already mapped, this is a
                           # second real ticker for the same city
    "KXLOWTMIA": "KMIA",   # Miami low - only the high was mapped before
    "KXLOWTNYC": "KNYC",   # NYC low - a second real ticker spelling
    "KXHIGHTEMPDEN": "KDEN",  # Denver high - a third real ticker spelling
    "KXLOWTDEN": "KDEN",      # Denver low - was missing entirely
    "KXLOWTAUS": "KAUS",      # Austin low - was missing entirely
}

# SESSION 4.1 CORRECTION: found live, not a station-mapping gap at all -
# KXHIGHUS ("High temp in United States") asks about the whole country,
# not one city. No single station can answer it, so it does not belong
# in SERIES_TICKER_TO_STATION at any station code - it belongs in its own
# excluded category, same treatment as an international series.
NATIONAL_AGGREGATE_SERIES_OUT_OF_SCOPE = ["KXHIGHUS"]

# Reference-only: cities confirmed live on weather.com/kalshi's own
# station list but not yet matched to a live series ticker in this
# project's data. Not wired into SERIES_TICKER_TO_STATION because there
# is no ticker to key on yet - kept here so a future series-discovery run
# doesn't have to re-research these station codes from scratch.
UNMATCHED_REFERENCE_STATIONS: dict[str, str] = {
    "College Station": "KCLL",
    "Columbus": "KCMH",
    "Gainesville": "KGNV",
    "Jacksonville": "KJAX",
    "Lexington": "KLEX",
    "Milwaukee": "KMKE",
    "Providence": "KPVD",
    "San Jose": "KSJC",
    "St. Petersburg": "KSPG",
    "Tampa": "KTPA",
    "West Palm Beach": "KDJT",  # as given by Kalshi's own page - see notes
    "Chicago (Midway)": "KMDW",  # the OTHER Chicago station - see notes
    "Houston (Bush Intercontinental)": "KIAH",  # the OTHER Houston station
}

del SERIES_TICKER_TO_STATION["KXHIGHTOMDB_US_PLACEHOLDER"]

# International series confirmed live (category "Climate and Weather",
# ticker matches KXHIGH*/KXLOW*) whose city has no NWS station because it
# is outside the United States. Listed explicitly, not just implied by
# absence, so a future session can see at a glance this was checked and
# excluded on purpose.
INTERNATIONAL_SERIES_OUT_OF_SCOPE = [
    "KXHIGHTCYYZ", "KXLOWTCYYZ",  # Toronto
    "KXLOWTLFPG", "KXHIGHTLFPG",  # Paris
    "KXLOWTWSSS", "KXHIGHTWSSS",  # Singapore
    "KXHIGHTRJTT", "KXLOWTRJTT",  # Tokyo
    "KXLOWTZSPD", "KXHIGHTZSPD",  # Shanghai
    "KXHIGHTVABB", "KXLOWTVABB",  # Mumbai
    "KXLOWTEBBR", "KXHIGHTEBBR",  # Brussels
    "KXLOWTRKSI", "KXHIGHTRKSI",  # Seoul
    "KXHIGHTEHAM", "KXLOWTEHAM",  # Amsterdam
    "KXHIGHTYSSY", "KXLOWTYSSY",  # Sydney
    "KXHIGHTSBGR", "KXLOWTSBGR",  # Sao Paulo
    "KXHIGHTEDDB", "KXLOWTEDDB",  # Berlin
    "KXHIGHTLTFM", "KXLOWTLTFM",  # Istanbul
    "KXHIGHTOMDB", "KXLOWTOMDB",  # Dubai
    "KXHIGHTVHHH", "KXLOWTVHHH",  # Hong Kong
    "KXHIGHTZBAA", "KXLOWTZBAA",  # Beijing
    "KXHIGHTLSGG", "KXLOWTLSGG", "KXLOWTLSSG",  # Geneva
    "KXHIGHTMMMX", "KXLOWTMMMX",  # Mexico City
    "KXHIGHTEGLL", "KXLOWTEGLL",  # London
    "KXHIGHTEDDF", "KXLOWTEDDF",  # Frankfurt
]


def station_for_series(series_ticker: str) -> Optional[str]:
    """Returns the mapped station_id for a series ticker, or None if the
    series is out of scope (international) or genuinely unmapped. Callers
    must treat None as 'skip this row, do not guess' - see
    ingest_weather_markets.py."""
    return SERIES_TICKER_TO_STATION.get(series_ticker)
