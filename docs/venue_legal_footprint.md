# Venue Legal Footprint Reference

**Session 3.2 — Arbitrage Detection Logic**

## What this document is

Before `detector.py` surfaces a flagged opportunity, it labels whether
both venues in that pair are legally available together. This document
is the human-readable evidence trail behind that label. The
machine-readable version of the same facts lives in
`/scripts/arbitrage/detector.py`, in the constants
`KALSHI_SPORTS_RESTRICTED_STATES`, `POLYMARKET_KNOWN_RESTRICTED_STATES`,
and the function `fully_available_states()`. **If this document and that
code ever disagree, this document is the source of truth — the code is
what's stale and needs updating.**

## Why this matters for a two-venue arbitrage specifically

A single-venue mispricing (Kalshi's own YES+NO, or Polymarket's own
YES+NO) only requires one venue to be available to the trader. A
cross-venue matched pair requires **both** venues to be legally available
to the same trader at the same time — if either venue is blocked in the
trader's state, the "arbitrage" can't actually be executed as a locked
position, even though the price gap itself is real.

## What was checked for this session, and how current it is

**Kalshi.** Kalshi is a CFTC-regulated designated contract market and is
nationally available by default. Its **sports contracts specifically**
are a real, moving exception: as of a July 2026 third-party legal
tracker (cross-checked against Kalshi's own framing that state rules are
contested and change on individual court rulings), Kalshi's sports
contracts were restricted, paused, or under active dispute in at least
**Arizona, Massachusetts, Maryland, Michigan, Montana, Nevada, and Ohio**,
with New York enforcement action also in progress. This restriction is
specific to Kalshi's Sports category. **None of this project's three
current Kalshi tracks — Climate and Weather, Commodities, or the narrow
down-ballot Elections tiers — are Sports contracts**, and no equivalent
state-by-state restriction has been confirmed for those three tracks as
of this session. That absence of evidence is treated here as "not yet
known to be restricted," not as "confirmed available in all 50 states" —
this project has not run a dedicated legal check for Climate/Commodities/
Elections the way sports betting trackers already have for Kalshi Sports.

**Polymarket.** Polymarket relaunched in the United States in 2026 as a
CFTC-regulated exchange (Polymarket US, operated by QCX LLC), following a
$2 billion investment from Intercontinental Exchange (ICE) and a
regulated relaunch. No state-by-state restriction list specific to
Polymarket US was found during this session's research, comparable in
detail to the Kalshi Sports list above. This is recorded here as an
**open gap**, not a clean bill of health — it means "not yet checked in
comparable depth," not "confirmed unrestricted everywhere."

**Minnesota — a real, separate flag.** A Minnesota law effective
**August 1, 2026** makes it a felony to create, operate, host, or
advertise a prediction-market **platform** in the state. It targets
platforms, not individual traders placing trades from Minnesota, and it
is under active federal litigation as of this session, so its practical
effect is unsettled. It is not modeled as a per-trade state restriction
in `detector.py`'s constants (it doesn't restrict the trader the way the
Kalshi Sports list does), but it is worth Greg's own awareness since it
could affect whether either venue keeps operating in Minnesota at all,
independent of any specific trade.

## What this means for `detector.py`'s current behavior

Given the above, `detector.py`'s `fully_available_states()` currently
returns `both_available_nationally = True` for every flagged pair, since
none of this project's three current Kalshi tracks intersect with the
one confirmed restriction (Kalshi Sports) and no comparable Polymarket
restriction list was found. **This is a real, named limitation, not a
verified guarantee** — every flagged row's `legal_footprint_note` field
says so explicitly, and repeats the same standing instruction below.

## Session 4.1 addendum — Track 3 (Weather/Climate, Kalshi)

Session 4.1 built real ingestion for Kalshi's temperature-threshold
markets, all of which live under Kalshi's "Climate and Weather" category
— confirmed live, 2026-09-06, none carry the "Sports" tag this document's
one confirmed Kalshi restriction applies to. Per this document's own
framing above, that means Track 3 inherits the same status already
recorded for Commodities and Elections: **not confirmed restricted, and
not confirmed clean either** — no dedicated state-by-state legal check
has been run for Climate/Weather specifically, the same honest gap this
document already names for the other two non-Sports tracks. Session 4.1
did not close this gap; it confirmed the gap's existing description
already covers a track it hadn't been written for by name yet, and adds
this one paragraph so a future reader doesn't have to re-derive that
Track 3 falls under the "not Sports" umbrella above by inference alone.

**Nothing in this session's real data ingestion (24 US city stations, all
domestic) intersects any of the restrictions named above** — no Track 3
weather market comes from a Sports-tagged series, and Minnesota's
platform-level law (not trader-level, see above) doesn't change whether
an individual trader can act on a flagged Track 3 opportunity. This
document's existing standing instruction (confirm live eligibility before
placing a real trade) applies to Track 3 exactly as written above; no new
instruction was needed.

## Session 6.1 addendum — Track 5 (Sportsbook Player Props, DraftKings/FanDuel)

Track 5 is a genuinely different legal question from every venue covered
above: DraftKings and FanDuel operate as licensed retail sportsbooks in
each state where they're legal, so **general sportsbook legality is not
the open question** — the ROADMAP.md card for this session is explicit
that prop-bet legality can be restricted **independently of, and more
narrowly than, a sportsbook's general legal status**, so that's the actual
thing to check.

**What's confirmed, at a category level, as of this session:**

- **College player props** are the most consistently restricted category
  found. Several states that otherwise permit DK/FD sportsbook wagering
  have banned or narrowly restricted **college-specific individual player
  props** (as opposed to team lines) at various points, driven by
  athlete-integrity/NCAA-pressure concerns rather than general gambling
  policy — Ohio, Louisiana, Vermont, Massachusetts, and Maryland have each
  had this restriction reported at some point. **This project's v1 scope
  is NFL only (see both ingestion scripts' module docstrings), so this
  specific restriction does not yet apply to any real flagged output** —
  recorded here so it is not silently missed if/when a future session
  expands stat-type or sport coverage to include college football.
- **Injury-specific or "will X leave the game" style props** have been
  singled out and restricted in at least one state (Ohio) independent of
  the college-props rule above, on player-welfare-optics grounds.
- No comprehensive, current, state-by-state matrix specifically for **NFL
  player performance props** (the `player_performance` category this
  session's `prop_category` field tags — passing yards, receptions, etc.)
  was found. This is recorded as an **open gap**, matching this
  document's own established pattern above for Polymarket and for
  Climate/Weather/Elections on Kalshi: absence of a confirmed restriction
  is treated as "not yet known to be restricted," not as "confirmed legal
  everywhere."

**What this means for `ingest_dk_props.py` / `ingest_fd_props.py`'s
current behavior:** both scripts tag every normalized row with a
`prop_category` field (`player_performance`, `player_touchdown`, or a
future value) specifically so a later session's flagging/sizing logic can
apply a category-level legal check the same way `detector.py` applies a
venue-level one — that hook exists in the schema now, but **no
state-by-state restriction list has been coded into either script yet**,
matching this document's own "the code is what's stale" framing above:
this addendum is the accurate, current statement; a future session should
build the actual per-state gating logic against it before this track is
trusted to flag a real bet in a restricted state/category combination.

**Standing instruction addition specific to this track:** the college-
props and injury-props restrictions above are known to be more volatile
and more athlete-advocacy-driven than the general sportsbook-legality
questions this document otherwise tracks — re-verify before any future
session expands Track 5 past NFL player-performance props.

## Standing instruction

**Always confirm current availability using each venue's own live
eligibility tool before placing a real trade.** State rules for
prediction markets are genuinely volatile — they change on individual
court rulings, sometimes within a single week — and neither this
document nor `detector.py`'s constants are a substitute for checking on
the day of the trade. This document should be revisited and re-verified:

- Before Track 6 (flagship sports/exchange markets, per `ROADMAP.md`) is
  built, since that is the track where Kalshi's confirmed Sports
  restriction would actually start applying to a flagged opportunity.
- Periodically regardless, since both venues' regulatory posture in 2026
  has already changed more than once (Polymarket's own US relaunch is
  itself a mid-2026 event).

## Sources checked this session

- Kalshi Sports state-restriction list: a July 2026 third-party
  prediction-market legal tracker, itself framed around checking
  Kalshi's own eligibility tool as the real authority.
- Polymarket US regulatory status: coverage of Polymarket's 2026 US
  relaunch under QCX LLC and its ICE investment.
- Minnesota felony-platform law: a July 2026 third-party tracker's
  callout of the law's August 1, 2026 effective date and its
  platform-level (not trader-level) scope.

None of these sources are legal advice, and none of them are a
substitute for each venue's own real-time eligibility check.
