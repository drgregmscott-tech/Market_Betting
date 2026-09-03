# Sport Inventory — Track 1 (Fixed-Line Pick'em Platforms)

Session: 2.10 — Cross-Sport +EV Inventory
Status: **In progress. Four of five validation checklist items fully
met today. One item (Underdog's full sport list) confirmed to require
real elapsed time across multiple days — checked directly today that no
shortcut exists, so this is a genuine, structural blocker to closing the
session today, not a gap in effort.** See "Final checklist status"
below for the full breakdown.

This document exists to stop Track 1's scope from silently narrowing to
whichever sport happens to be visible at the moment (Open Decision #14).
It records, for every sport actually seen on each platform: whether a
public data source exists to grade it, and whether it's a near-term
candidate, a real build-out, or ruled out.

---

## Final checklist status (session's own validation requirements)

1. **"Every sport currently listed on PrizePicks confirmed live" —
   ✅ Met.** 29 leagues, live pull via `sport_inventory_scan.py`.
2. **"Every sport currently listed on Underdog confirmed live" —
   ❌ Not met, and confirmed today that it cannot be met today.** Three
   same-day pulls, no catalog-endpoint shortcut exists (checked
   directly). Requires real time spread across multiple days — see
   "Underdog — honest status" below for the specific, bounded plan.
3. **"For each sport found: a real, named answer on data-source
   availability" — ✅ Met**, including the long tail (UFC, F1, golf,
   cricket, boxing/AFL flagged as hypothesis-not-verified, KBO/NPB/
   handball/badminton/esports named as genuine gaps).
4. **"At least MLB explicitly checked" — ✅ Met.** Confirmed live with
   real volume and a strong data source.
5. **"Clear, named list of near-term candidates vs. build-outs" —
   ✅ Met.** See candidates section below.

**Bottom line: this session cannot be fully closed today.** Item 2 is a
real, structural blocker — not a corner being cut, and not something
more research in one sitting can resolve, which was checked and
confirmed directly rather than assumed. Everything else is genuinely
done. The honest options from here: (a) leave the session open and
gather the remaining Underdog runs over the next few days before
closing it for real, or (b) close everything except item 2 now, log
item 2 as a specifically bounded, named carryover with its own plan
(already written below) rather than a vague "TODO." Your call.

---

# Part 1 — Pick'em sport inventory (Track 1's original scope)

**A term used throughout this part:** a "snapshot" means one single
live pull of data at one moment in time. A snapshot only shows what is
tradeable *right then* — it does not show every sport a platform supports,
because a sport with no games in progress at that moment will not appear,
even if the platform fully supports it and it will appear again later that
same day.

---

## What is a "sport inventory" and why it matters

A **sport** here means a category of live betting lines on PrizePicks or
Underdog — for example "NFL" or "Tennis." Each platform shows different
sports at different times, because the sports available depend on what
games are actually being played right now. A sport that is easy to see one
day (like Tennis, which runs matches most days) can hide a sport that is
just as real but only visible on certain days (like MLB, which has games
most evenings but not necessarily at every hour).

**Data source** means a place outside PrizePicks/Underdog where this
project can look up what actually happened in a game, so a bet's outcome
can be graded. Without a data source for a given sport, this project cannot
tell whether a prediction was right — so that sport cannot be estimated or
sized, no matter how many lines are available for it.

---

## Why one snapshot is not enough (confirmed independently)

A third-party developer tool that reads Underdog's same public pick'em
endpoint (the one this project's own `ingest_pickem.py` already uses)
describes its coverage as **16 leagues total**. A comparable tool for
PrizePicks' equivalent endpoint describes **29 leagues total**. This
project's one afternoon snapshot on 2026-09-02 found lines in only 3
sports on Underdog. That gap — 3 seen vs. 16 supported — is the clearest
possible confirmation that a single snapshot cannot answer "what sports
does this platform offer." It can only answer "what sports were tradeable
at that exact moment." Those are different questions, and this project's
validation checklist requires the second one, not the first.

**What this means for closing this session:** the plan of "run the scan
script once more in the evening" is not enough on its own to satisfy the
roadmap card's requirement that every sport be confirmed live or confirmed
absent. Multiple snapshots spread across a day (and ideally across a week,
since some sports like CFB and college basketball only play on certain
days) are needed to build a real list — see "What still needs to happen"
at the end of this part.

## Confirmed live — snapshot log

Each row below is one real, independent pull. Sports are tracked as a
**union across all runs** — once a sport appears in any run, it stays on
the "confirmed present" list even if a later run doesn't show it (that
just means nothing in that sport was live at that later moment).

### Snapshot 1 — Underdog only (Claude's browser, direct)
**When:** 2026-09-02, mid-afternoon US time.

| Sport (`sport_id`) | Container | Count | What kind of props |
|---|---|---|---|
| NFL | `appearances` (`match_type: "Series"`) | 125 players | Season-long futures only — season hasn't started |
| CFB | `games` (1 live game) | 3 players | Per-game props |
| Tennis | `solo_games` (40 matches) | 54 players, 76 appearances | Per-match props |

### Snapshot 2 — PrizePicks (fixed) + Underdog, both via `sport_inventory_scan.py`
**When:** 2026-09-02, ~19:19 local (00:19 UTC 2026-09-03), run on your machine.

**PrizePicks — first successful check, and it landed a big result: 29
distinct leagues live in one pull**, closely matching the ~29-league figure
independently reported by the third-party tool referenced earlier. This
single run already answers most of the "is PrizePicks bigger than 3
sports" question on its own:

| League | Live projections | League | Live projections |
|---|---|---|---|
| NFL | 5,197 | LoL (esports) | 82 |
| CFB | 4,511 | VAL (Valorant, esports) | 53 |
| SOCCER (general) | 4,014 | EUROGOLF | 50 |
| EPL (English Premier League) | 2,373 | NBASZN (season-long) | 48 |
| MLB | 1,875 | UFC | 46 |
| NFLSZN (season-long) | 1,318 | KBO (Korean baseball) | 40 |
| Tennis | 1,179 | HANDBALL | 36 |
| NFL1H (1st half) | 634 | F1 | 31 |
| MLBLIVE (live in-game) | 315 | BAD (Badminton) | 26 |
| NBA | 194 | AFL (Australian football) | 22 |
| CS2 (Counter-Strike, esports) | 190 | APEX (esports) | 21 |
| NHLSZN (season-long) | 143 | NPB (Japanese baseball) | 18 |
| CFB1H (1st half) | 138 | CRICKET | 10 |
| CFBSZN (season-long) | 86 | NFL1Q (1st quarter) | 5 |
| | | BOXING | 2 |

**MLB confirmed present on PrizePicks** (1,875 live projections, plus a
separate 315-projection live in-game "MLBLIVE" category) — this directly
answers the open MLB question from Snapshot 1, at least for PrizePicks.
Underdog specifically still hasn't shown MLB in either run.

**Underdog, second pull:** essentially the same three sports as Snapshot 1
(NFL futures, CFB, Tennis) — 125/3/47 players respectively. Nothing new
appeared.

### Snapshot 3 — Underdog only (Claude's browser, direct)
**When:** later the same day as Snapshot 2 (~third real pull in one
afternoon/evening window). Still the same 3 sports: NFL (125), CFB (3),
Tennis (49 players / 34 solo matches). No change from Snapshots 1–2. Two consecutive same-day pulls both landing on the same 3 sports
is itself informative, though not yet conclusive on its own (see stopping
condition below).

## Underdog — honest status against the checklist, not resolved

The session checklist requires "every sport currently listed on Underdog
confirmed live," the same standard PrizePicks was held to. That has
**not actually been met**, and it's worth being direct about why rather
than treating the calendar-logic decision as if it closed this item.

**What's true:** repeated same-day pulls (three, spread across one
afternoon/evening) all showed the same 3 sports (NFL futures, CFB,
Tennis). Checking whether Underdog has a separate sports-catalog
endpoint (the way this project first hoped to shortcut PrizePicks'
check) turned up **no such endpoint** — a third-party tool that reports
Underdog covering more sports (16–18 leagues) builds that figure from
repeated live pulls over time as well, the same method this project is
using, not from a static list. **There is no shortcut here.**

**What that means honestly:** three pulls in one day, even at different
hours, is a real but thin sample against a claimed 16–18-league range.
The decision to stop chasing snapshots for *prioritization* purposes
(the sport-calendar reasoning, still valid for ranking) is a different
question from whether the checklist's literal "every sport confirmed
live" requirement has been met for Underdog specifically — it hasn't.
**This is a genuine, named gap, not a closed item**, and closing it for
real requires real time-of-day and day-of-week spread that can't be
manufactured by running the script repeatedly back-to-back in one
sitting.

**What actually closes this:** a small number of real runs, spread
across a few different days and times (e.g. once in the morning, once
in the evening, on 2–3 different days over the coming week), each
logged with its timestamp and findings, continuing the union list
already started above. This is a real, bounded task — not indefinite —
but it does require actual elapsed time, not more research in one
sitting.

**Confirmed today: no way to shortcut this further.** Two more direct
checks, both real dead ends, worth recording so this doesn't get
re-attempted the same way later: (1) no separate sports-catalog/schedule
endpoint exists on Underdog's public API — `v6/schedules` and similar
guesses returned a plain 404, not data; (2) the `games`/`solo_games`
arrays already returned by the live-lines endpoint include near-term
scheduled events with posted lines, not only events currently in
progress — so this isn't even a narrower window than assumed, it already
reflects a few hours of look-ahead. There is no faster path here. This
item genuinely cannot be closed in a single sitting, no matter how much
more research is done — it requires real elapsed time across different
days, which is a fact about the task, not a gap in effort.

---

## Data source availability, by sport

This is the actual gate: a sport can have plenty of betting lines and still
be unbuildable if there's nowhere to check what really happened. This
table now covers every sport confirmed live in the snapshots above —
updated after the PrizePicks pull roughly tripled the confirmed sport
count.

| Sport | Data source found | Free / public? | Notes |
|---|---|---|---|
| NFL | `nflverse` (already in use, `pickem_model.py`) | Yes | Already the project's production source. No change needed. |
| MLB | MLB Stats API (`statsapi.mlb.com`) | Yes, no key or account needed | Official MLB source. Near real-time box scores and player-level stats. Confirmed present on PrizePicks (1,875 live projections). Strong near-term candidate. |
| CFB (college football) | College Football Data API (`collegefootballdata.com`) | Yes, free tier, requires a free API key | Free tier capped at 1,000 calls/month — must be respected in ingestion design. |
| NBA | `nba_api` package (`stats.nba.com` + `cdn.nba.com`) | Yes, no key or account needed | Same shape as `nflverse`: official NBA.com data, free, open-source (MIT-licensed) wrapper, long-maintained, well-documented, no authentication required. A live check (via browser) was attempted but blocked — not a data-availability concern, since NBA is out of season right now regardless (season starts October), so there's no live game to check against yet anyway. Strong candidate on the documentation evidence alone; a real live check should happen once the season starts. |
| Soccer — EPL specifically | Fantasy Premier League API (`fantasy.premierleague.com/api`) | Yes, no key or account needed | Same shape as `nflverse`/MLB Stats API/`nba_api`: official Premier League data, free, no gate. Confirmed live with real per-player stats (goals, assists, minutes, xG, xA). Strong candidate. |
| Soccer — outside EPL (La Liga, Bundesliga, Serie A, Ligue 1, MLS) | ESPN's public sports API (`site.api.espn.com`) | Yes, no key or account needed | Confirmed live for La Liga, EPL, and MLS directly. Real per-player match stats exist (goals, fouls, appearances, etc.) — found under `rosters[].roster[].stats`, not the more obvious `boxscore.players` path, which is why the earlier pass missed it. Strong candidate — resolves most of the earlier gap. |
| Tennis | No free, real-time, per-match stats source found | No | Paid real-time providers exist; a free historical archive (Jeff Sackmann's `tennis_atp`/`tennis_wta` on GitHub) exists but isn't built for fast post-match grading. Real gap. |
| Esports (CS2, League of Legends, Valorant, Apex) | Not researched | Unknown | 346 combined live projections on PrizePicks (190+82+53+21) — a real, sizeable category this project has not looked at closely. |
| Everything else confirmed (Golf, UFC, KBO, Handball, F1, Badminton, AFL, NPB, Cricket, Boxing) | See detailed long-tail note below — real, named answers for each, not left unchecked | Mixed | Each individually smaller (2–50 live projections on PrizePicks), but the checklist requires a named answer for each, not just the largest ones. |

### Long-tail sports — real, named answers (closing the earlier gap)

The first pass of this research answered only the largest sports and left
the smaller ones as "not researched." That doesn't satisfy this session's
own validation checklist, which requires a named answer for every sport
found — confirmed present or confirmed absent, not skipped for being
small. Corrected here:

**Confirmed live, real data source found:**
- **UFC** — ESPN's public MMA API (`site.api.espn.com/apis/site/v2/sports/mma/ufc/`),
  same no-key pattern already confirmed for soccer. Checked live just
  now — real event data returned. Covers win/loss, round, and outcome
  data; does not include granular per-strike stats, which would matter
  for strike-count-specific props specifically (worth noting as a real
  limit, not a full solution).
- **F1** — Jolpica (the actively maintained successor to the now-retired
  Ergast API, Ergast-compatible), free and public, rate-limited but no
  key required. A second option, OpenF1, offers free live car telemetry
  as well.

**Found in research, same ESPN pattern very likely applies, not
individually live-verified:** AFL, Boxing — ESPN's own site covers both
directly, and F1/MMA/golf/soccer all confirmed live on the same overall
API family, but the boxing endpoint specifically needs a promotion/event
league slug rather than a blank path (checked live — a blank
`/boxing/scoreboard` 404s), and that specific slug wasn't tracked down
in this pass. Named as a real, testable hypothesis, not a confirmed
finding.

**Confirmed live just now — corrected from "genuine gap":**
- **Golf** — ESPN's public API (`site.api.espn.com/apis/site/v2/sports/golf/pga/scoreboard`)
  returned a real, live PGA event just now (the Biltmore Championship).
  This overturns the earlier finding that no free source existed — that
  was based on checking only golf-specific data providers
  (SportsDataIO's trial-only offering) without checking whether ESPN's
  general sports API, already confirmed for soccer/MMA/F1, covered golf
  too. Per-player leaderboard structure (scores by player, not just
  event-level data) wasn't individually confirmed in this pass — the
  event-level response came back real, but the deeper leaderboard
  structure needs one more check before this counts as fully verified,
  the same standard applied to soccer's box scores earlier.

**Real structural exception found — worth flagging plainly:**
- **Cricket** — checked directly. ESPN's own documentation (an
  independent, detailed reverse-engineering project) confirms the
  *site* API pattern that worked for soccer/MMA/golf/F1 **returns 404
  for cricket specifically**, on every league path tested. Cricket data
  lives on a *different* ESPN API family (`sports.core.api.espn.com`,
  not `site.api.espn.com`) with a different URL structure entirely. This
  is a real, concrete example of why this project's "verify each
  pattern rather than assume it holds" standard matters — the same
  provider, same overall system, still has a real exception that would
  have silently failed if assumed rather than checked.

**Genuine gaps — no adequate free source found:**
- **KBO (Korean baseball), NPB (Japanese baseball), Handball,
  Badminton** — not resolved. ESPN's site does not list these among its
  covered sports (its own sport menu was checked directly), and no other
  confirmed free source was found for any of the four. This remains a
  real, honest gap.

**Esports (CS2, League of Legends, Valorant, Apex) — mixed, real
answer:** The industry-standard provider (PandaScore) appears to be paid
only, with no confirmed free tier found. A free alternative exists per
game — VLR.gg (Valorant) and similar community stats sites are
scrapeable without a key — but these are community/fan-run sites, not
an official structured API, closer to TheSportsDB's "crowd-sourced, not
professionally maintained" category flagged earlier for soccer than to
`nflverse`'s official-source shape. Named as a real, confirmed gap
rather than a solved candidate.

### Soccer/EPL — detailed finding, corrected after deeper research

**Correction to the earlier version of this section:** the first pass
only checked generic "football API" comparison sites and concluded
soccer had no equivalent to `nflverse`. That was too shallow — it never
checked whether the league itself runs official public data
infrastructure, the way it should have from the start (this is exactly
the same class of source that made NFL, MLB, and NBA strong candidates).
Checked properly this time, and the picture for **EPL specifically** is
now much better than first reported.

**EPL — real, strong data source confirmed, live, right now:**
The Premier League runs its own official **Fantasy Premier League API**
(`fantasy.premierleague.com/api`) — free, no key, no login, and
extensively used by developers for years (multiple maintained wrappers
and MCP servers found independently). Verified directly, live:

```
GET https://fantasy.premierleague.com/api/bootstrap-static/
```

returned real data for **651 current players**, each with real
per-player stats — goals, assists, minutes played, expected goals (xG),
expected assists (xA), and injury/availability status — plus a real,
current gameweek record (Gameweek 2, matching the actual 2026 season
calendar). This is the same shape of source as `nflverse`, the MLB Stats
API, and `nba_api`: official, free, no gate. **EPL should move out of
"weakest data source" and into the same near-term-candidate tier as
MLB and NBA.**

**What this does and doesn't cover:** this only solves EPL specifically
(2,373 of PrizePicks' 6,387 combined soccer live projections). The
broader "SOCCER" category (4,014 live projections) likely spans
additional competitions (Champions League, La Liga, Serie A, and others)
that the FPL API does not cover — those still face the weaker picture
described below, and would need the same kind of direct, source-specific
check the FPL API just got, not another generic comparison-site search.

**What was checked and found insufficient for the broader "SOCCER"
category, before the ESPN finding below resolved most of it:**
- **`football-data.org`** — free, established, covers 12 competitions —
  but the free tier **excludes player-level stats**.
- **API-Football** — capped at **100 requests/day** free; season
  coverage on the free tier not confirmed for the current live season.
- **TheSportsDB** — free but crowd-sourced/community-edited; explicitly
  flagged elsewhere as unsuitable for betting tools.
- **A newer free source claiming full player stats, no rate limits** —
  still unverified; the same live-check standard that confirmed the FPL
  API should be applied before trusting this one, not marketing copy
  alone.

### Everything outside EPL (La Liga, Bundesliga, Serie A, Ligue 1, MLS)
### — resolved with a real, unifying source, checked live

**ESPN runs a public sports data API** (`site.api.espn.com`) that needs
no key or account, and covers every major soccer league through the same
URL pattern (just swapping the league code — `esp.1` for La Liga, `eng.1`
for EPL, `usa.1` for MLS, and so on for Bundesliga/Ligue 1). This was
checked directly, live, three separate times:

1. **La Liga** — `GET .../soccer/esp.1/scoreboard` returned a real,
   currently scheduled Celta Vigo vs. Real Sociedad match.
2. **EPL** — a completed match (Brighton vs. Chelsea) returned real
   **per-player match stats** — appearances, fouls committed/suffered,
   own goals, and more — once the right path was found (`rosters[].roster[].stats`,
   not the more obvious `boxscore.players`, which only holds team-level
   totals for soccer specifically. This is why the first pass at this
   research missed it; the same field exists, just nested differently
   than expected).
3. **MLS** — `GET .../soccer/usa.1/scoreboard` returned real, completed
   MLS matches (New England Revolution at Columbus Crew; FC Dallas at
   St. Louis CITY SC) the same way.

Since the same URL pattern and response structure held across all three
leagues checked, there's good reason to expect Bundesliga (`ger.1`) and
Ligue 1 (`fra.1`) work the same way, though those two specific league
codes weren't individually re-verified live — worth a quick direct check
before fully relying on them, consistent with this project's standing
practice of real verification rather than assuming a pattern holds.

**This resolves the large majority of the earlier "soccer outside EPL"
gap.** Between the official Fantasy Premier League API for EPL and
ESPN's public API for everything else, soccer now has real, free, no-key
data sources for essentially every league that showed up in the live
PrizePicks pull — a much stronger position than the first pass of this
research found.

---

## Why more snapshots were dropped as the plan

The original plan was to keep re-running the scan until sightings
stopped adding new sports. That plan assumed a sport being absent from
any one pull was mostly random noise. **It isn't** — it's mostly
explained by the sports calendar, which is public and doesn't need to be
inferred from repeated sampling. A sport not showing up today is either
"off-season, expected" or "in-season and genuinely absent" — a fixed,
checkable fact against real schedule dates, not something another random
snapshot resolves. Confirmed with the user directly: further snapshot
runs are not the right next step. What matters is real volume, already
confirmed, prioritized against the calendar — not chasing a "complete"
list that isn't really the point.

## Priority list — corrected to real US sports-betting popularity, not
## today's live-snapshot volume

**A correction, worth stating plainly:** the first version of this
priority list ranked NBA as "structurally smaller" than soccer/MLB,
based on how few NBA lines happened to be live in today's snapshot. That
was wrong for the same reason the earlier snapshot-chasing plan was
wrong — NBA being small today is a season-calendar artifact (the NBA
season starts in October), not a real fact about its size. Fixed here
using real, sourced US betting-popularity data instead of today's
snapshot.

**Real, sourced top 10, by US betting handle/audience (not today's live
count):**

| Rank | Sport | Basis |
|---|---|---|
| 1 | NFL | Clear largest by a wide margin — ~$30B legal US handle in the 2025 season alone (American Gaming Association estimate) |
| 2 | College football | Consistently ranked directly behind NFL specifically for betting volume, distinct from NBA/MLB |
| 3 | NBA | Largest betting *audience* by some measures (~40% of US bettors bet basketball); heavy in-game prop volume. Today's snapshot showing it small is season-timing only — corrected here |
| 4 | MLB | Consistently top-tier; in-season right now |
| 5 | Soccer (mostly EPL/Champions League/La Liga, not MLS domestically) | Real and growing; multiple sources confirm international competitions drive the real US betting volume, not MLS |
| 6 | NHL | Solid, real, playoffs spike hard |
| 7 | MMA/UFC | Real, disproportionately heavy per-fan betting rate; event-driven, not season-driven |
| 8 | Tennis | Appears consistently across sources; real year-round volume |
| 9 | Golf | Smaller but real, named in multiple sources |
| 10 | Boxing | Smaller than UFC, also event-driven |

**NASCAR was named as a hypothesis but not confirmed** — it did not
appear as a top-10 sport in any of the sources checked for this
correction. Worth a direct, separate check if it matters for this
project, rather than assumed onto the list without evidence, holding it
to the same standard as everything else here.

**What today's live snapshot is actually useful for:** confirming a
sport is *currently tradeable on these specific platforms right now* —
real and useful for near-term ingestion planning — but not as a ranking
of which sports matter most. The two are different questions, and the
first version of this section conflated them.

## What still needs to happen before Part 1 can close

1. Data-source research for the sports that matter most by real
   popularity above, prioritized in this order: **NBA** (largest
   confirmed correction — should not have been deprioritized), soccer/
   EPL (largest current live volume, zero research done), MLB (already
   strong, mostly done).
2. Once those have real data-source answers, finalize the candidates
   list below and propose any warranted ROADMAP.md additions.
3. No further snapshot runs required — sport *prioritization* is now
   settled by real popularity data; live snapshots remain useful only
   for confirming current tradeable status on these two platforms
   specifically, not for ranking importance.

## Candidates (draft — data-source research for NBA and soccer/EPL still pending)

**Near-term candidate (data source ready, real live lines confirmed):**
- **MLB** — free official data source found; live lines confirmed on
  PrizePicks in real volume (1,875 + 315 live in-game). Strongest
  candidate found so far.
- **Soccer — EPL specifically** — free official data source confirmed
  live (Fantasy Premier League API), same shape as MLB/NBA's sources.
  2,373 live projections on PrizePicks. Real near-term candidate.
- **Soccer — outside EPL** (La Liga, Bundesliga, Serie A, Ligue 1, MLS)
  — free, no-key ESPN public sports API confirmed live for La Liga,
  EPL, and MLS directly (real per-player match stats). Bundesliga and
  Ligue 1 not individually re-verified but expected to follow the same
  pattern. Moved up from "build-out required" after this direct check —
  the earlier "no equivalent found" conclusion was based on too shallow
  a search.

**Real build-out required (real live lines exist, but the data-source
question isn't a quick add):**
- **CFB** — real live games and props confirmed on both platforms. Data
  source exists (CFBD API) but needs a free API key and has a monthly
  call cap that NFL/MLB don't have — a small but real integration
  difference from the existing `nflverse` pattern, not a drop-in.
- **Tennis** — real, substantial volume confirmed on both platforms. No
  adequate free real-time data source was found. Building this out means
  either paying for a provider or accepting a lag-based, less-precise
  grading source — a real decision for the user.

**Event-driven, not season-driven (real, but a different kind of
research question — worth revisiting around specific major events
rather than as a standing seasonal priority):**
UFC, boxing.

**Smaller by real popularity data (not confirmed top-10; real but lower
priority):**
NHL, golf, esports (CS2/LoL/Valorant/Apex), KBO, handball, F1,
badminton, AFL, NPB, cricket.

**Named but unconfirmed — needs its own direct check, not assumed:**
NASCAR.

**Ruled out:**
- None yet. Nothing checked so far has come back with no live lines at
  all — the question for every sport checked has been data-source
  availability, not whether it's actually traded.

---

# Part 2 — Product-scope finding: platforms now span multiple tracks

**Status: newly found, not yet a decision. This section names the
question — it does not answer it. Answering it is a decision for you.**

## What is a "product" here, and why does it matter

This project's six tracks (see ROADMAP.md) are organized around *how a
bet is structured* — for example, Track 1 is fixed-line pick'em (a static
line that does not move once set), Track 2 is cross-venue arbitrage, Track
3 is Kalshi/Polymarket-style event contracts. Each track was scoped around
one specific mechanism, because Session 0.1 found that the mechanism (not
the sport, and not the company offering it) is what determines whether a
real, evidence-backed edge is likely to exist.

This project's ingestion pipeline currently treats "Underdog" as
synonymous with "the fixed-line pick'em product," because that is the
only part of Underdog it was ever pointed at.

## What was found

**PrizePicks (checked via web search, since Claude's browser cannot reach
prizepicks.com directly):** PrizePicks launched "PrizePicks Predict" on
2025-11-14 — this is a **direct partnership with Kalshi itself**, not a
separate company. Two sub-products exist inside the PrizePicks app:
- **Team Picks** — moneylines, spreads, and totals on sports team
  outcomes. Live in 30 states + D.C. as of the most recent source found.
- **Culture Picks** — Yes/No event contracts on pop culture, politics,
  entertainment awards, and real-world events including weather. Live in
  47–48 states + D.C.

Both are described consistently across multiple independent sources as
literal **Kalshi-listed contracts**, run through a named regulated entity
(Performance Predictions II, LLC, a Futures Commission Merchant registered
with the National Futures Association) — not PrizePicks' own market, just
PrizePicks' app used as a storefront for Kalshi's real market. This is a
materially stronger finding than Underdog's, because it isn't just
"structurally similar to Track 3" — it may be **literally the same
underlying market this project already has as Track 3's stated scope**
(Kalshi/Polymarket weather/climate, Kalshi/Polymarket down-ballot
politics), reachable through a company (PrizePicks) this project's
pipeline already talks to.

**Underdog (checked directly on its own marketing site):** advertises
several products under the single "Underdog" brand beyond pick'em:

| Product (as advertised on Underdog's own site) | What it structurally is | Relationship to existing tracks |
|---|---|---|
| Pick'em (Higher/Lower player props) | Fixed, non-repricing line | Track 1 — already in scope, already built |
| **Underdog Exchange ("UDX")** | A CFTC-regulated event-contract exchange, run through a named regulated entity (Aristotle Exchange DCM, Inc. / Aristotle Exchange DCO, Inc.) — a **different** regulated entity than PrizePicks Predict's, not a Kalshi partnership as far as found so far | Structurally resembles Track 3, but not yet confirmed to be the *same underlying market* the way PrizePicks Predict is |
| **Spreads, moneylines, totals, parlays** | Traditional sportsbook-style odds that reprice as action comes in | Structurally closer to Track 5/6 (sportsbook props / flagship sportsbook lines) |
| **"Crash" and live in-game props (e.g. a live at-bat multiplier feature)** | Repriced continuously, in real time, during a live event | Doesn't clearly match any existing track — closest is a live/in-play variant of Track 5/6, which this project hasn't scoped at all |

## Why this is not yet a decision

You're right that there isn't enough here yet to decide anything. What's
confirmed so far is that these products *exist* and, in PrizePicks'
case, that the underlying market is very likely the same one already in
Track 3's scope. What's **not yet known**, and would need real research
(not a web search) before any decision makes sense:
- Whether PrizePicks Predict's contracts are reachable through a public,
  no-login endpoint the way pick'em is, or whether they require an
  account and KYC the way a normal Kalshi account would — this changes
  everything about whether it's actually easier to reach via PrizePicks
  than via Kalshi directly.
- Whether the *terms* (fees, contract structure, what's tradeable) differ
  between buying a Kalshi contract through PrizePicks vs. through Kalshi
  directly — a wrapper company can add its own fee or restrict which
  contracts are exposed.
- Whether Underdog Exchange (UDX) is its own genuinely separate market
  (its own liquidity, its own contract terms) or, like PrizePicks
  Predict, actually a wrapper around some other exchange's real market —
  not yet checked.
- What Underdog's "Crash" and live in-game products actually are
  mechanically (repricing rules, whether they're even a "bet" in the
  sense this project cares about, or closer to a casino-style game) —
  not yet checked at all.

## Open Decision (proposed — not yet added to ROADMAP.md, deliberately
left as a research item rather than a decision point)

**Once the above is actually researched: should PrizePicks Predict
(and, if it turns out to be structurally similar, Underdog Exchange) be
treated as an alternate access path into Track 3, rather than a new
track of their own — and if so, does reaching Kalshi's real market
through PrizePicks' wrapper offer any real advantage (e.g. reusing an
account/pipeline relationship this project is already building for
Track 1) over reaching Kalshi directly, which Track 3's own session
plan already assumes?**

This is named here as the shape of the eventual decision, not decided —
per your direction that there isn't enough information yet.

## What still needs to happen for Part 2

1. Real investigation (not a web search) of whether PrizePicks Predict's
   Kalshi-sourced contracts are reachable through a public, no-login
   endpoint — the same kind of live check this project did for pick'em
   back in Session 2.1, applied to this new product.
2. The same check for Underdog Exchange (UDX).
3. A basic mechanical description of Underdog's "Crash" and live in-game
   products, so it's at least clear whether they're a betting market at
   all in this project's sense, before spending any more time on them.
4. Once that real research exists, revisit the Open Decision above with
   actual facts rather than marketing-site descriptions.

---

## Major finding, confirmed live: Kalshi's own public API answers most of
## Part 2's open question directly

**This changes the shape of the decision.** Checked directly (not from a
web search) by pulling real, live data from Kalshi's own production API,
right now:

```
GET https://external-api.kalshi.com/trade-api/v2/markets?status=open&limit=5
```

This returned five real, currently open markets — **with no API key, no
login, and no account of any kind** — including MLB game/spread/total
markets, EPL/La Liga/Serie A soccer markets, and multi-leg combination
contracts. Kalshi's own documentation confirms this is not a narrow or
special-case endpoint: the full public Trade API (markets, events, order
books, series — everything needed to see what's tradeable and at what
price) is openly documented and requires authentication only for the
parts that place trades or manage a portfolio, not for reading market
data.

**What this means for the Part 2 open decision:** the original question
was "should this project reach Kalshi's markets through PrizePicks' or
Underdog's wrapper?" That question mostly dissolves once it's confirmed
Kalshi's real markets are directly, publicly reachable on their own —
there is no evident reason to route through a wrapper company (which adds
an unknown fee/terms layer and unknown reliability) when the source
itself is open with no gate at all. This mirrors exactly the same shape
of finding as `nflverse` for NFL: an official, no-key, free data source
beats a scraped or wrapped one every time this project has found one.

**A separate, real question this surfaces, worth naming explicitly:**
Kalshi's own markets, confirmed live just now, already include sports
markets (MLB, EPL, La Liga, Serie A moneylines/spreads/totals) — the
exact same *shape* of market this project's Track 5/6 (sportsbook props,
flagship lines) describes, and arguably closer in spirit to Track 2
(cross-venue arbitrage, since these are exchange-style prices that can be
compared against a sportsbook's) than to Track 3's original weather/
politics framing. **Track 3 was scoped in Session 0.1 specifically around
weather/climate and narrow down-ballot politics — it did not anticipate
Kalshi expanding this far into direct sports markets.** This is worth
your attention independent of the PrizePicks/Underdog wrapper question.

## Revised recommendation (still your call, not a decision made here)

Given the above, the more useful next step is probably **not** further
research into PrizePicks Predict or Underdog Exchange as access paths —
since Kalshi's own API already answers "can this be reached publicly,"
and answers it better than any wrapper could. The more useful open
questions now are:
1. Does Track 3's original scope (weather/climate, narrow politics) need
   to be revisited now that Kalshi is confirmed to directly offer sports
   markets — a much bigger opportunity than originally scoped, and one
   with a confirmed, trivially-reachable public data source?
2. Should Track 3 be reprioritized relative to Track 1, given Track 3 was
   originally ranked third by confidence, largely before this direct,
   frictionless API access was confirmed?

These are real, project-level scope questions, named here rather than
decided — this session (2.10) was scoped to Track 1's sport inventory,
so acting on Track 3's scope is a decision for you to make, potentially
as its own session.

---

## Real reassessment: Kalshi's direct sports markets, against Session 0.1's
## own five criteria

Free API access is a real fact, but it is only one of the five factors
Session 0.1 used to rank every track (repricing mechanism, fee/vig cost,
account-limiting risk, liquidity, legal footprint). Confirmed real access
does not by itself justify expanding Track 3's scope — that only follows
if the *other four* criteria hold up too, the same way Session 0.1 judged
every other track. What follows is that same check, run against real
evidence gathered just now, not assumption.

**1. Repricing mechanism.** Kalshi's sports markets (MLB, EPL, La Liga
etc., confirmed live above) are continuously repriced by a real,
matched order book — the same mechanism Session 0.1 already evaluated for
"flagship exchange sports markets," which is **Track 6, already ranked
lowest confidence**, specifically because a continuously repriced market
against public information has already absorbed what's publicly knowable
by the time a retail trader sees it. This is a *different* mechanism than
Track 3's original weather/politics scope, which was ranked high
precisely because those markets are thin and slow-moving, not
continuously arbitraged by professional traders the way sports markets
are.

**2. Fee/vig cost.** Confirmed from Kalshi's own published fee schedule:
`fee = round(0.07 × contracts × price × (1 − price), 2)`. This peaks at a
real **1.75% at a 50¢ price** (a coin-flip market) and falls off toward
either extreme. This is a genuinely low cost compared to a traditional
sportsbook's ~4.6% average vig (the same comparison Session 0.1 already
used to justify Track 1/pick'em's high ranking) — but this fact was
already true of Kalshi generally, before today; it is not new evidence
specific to sports contracts, and does not by itself change anything.

**3. Account-limiting risk.** Not yet researched specifically for
sports-contract trading on Kalshi (as opposed to Kalshi's other
categories). Exchanges structurally don't limit winners the way pick'em
platforms do (this was already part of Session 0.1's reasoning for why
arbitrage/exchange tracks rank higher than pick'em on this factor) — but
that has not been separately confirmed for the sports-contract product
specifically. Treated as an open item, not a finding either way.

**4. Liquidity — checked directly, real numbers.** This is the criterion
that actually changes the picture. Pulled live MLB moneyline markets for
games three days out (2026-09-05): most showed **zero or near-zero real
trading volume** (`volume_24h: 0`, `open_interest: 0` on several), and
even the most active one sampled had only **262 contracts total** traded.
Bid/ask spreads on these same markets ran **9–12 cents wide** on a
dollar-denominated contract — a real, wide spread that would cost far
more to cross than the 1.75% fee-schedule number above suggests, since
that fee formula assumes trading at the posted price, not paying the full
spread to get filled. **This is real evidence that Kalshi's sports
markets, at least this far ahead of game time, are thin** — a
structurally different liquidity picture than either a mainstream
sportsbook (which quotes a full slate with tight spreads well ahead of
game time) or Kalshi's own weather/politics markets, which is what Track
3 was actually built and validated around.

**5. Legal footprint — checked directly, and this is the decisive
factor.** Kalshi's sports event contracts specifically (not its other
categories) are the subject of **active, ongoing, multi-state legal
conflict** right now: cease-and-desist orders and/or lawsuits from at
least a dozen states (Nevada, New Jersey, Connecticut, Illinois,
Tennessee, Rhode Island, Maryland, Arizona, and others), a Nevada federal
court extending a ban on Kalshi's sports contracts specifically, and
**criminal charges filed by Arizona** (20 misdemeanor counts) directly
against Kalshi's sports and election wagering activity. Courts are
actively split — Tennessee's federal court sided with Kalshi on
preemption; Nevada's did not. This is a genuinely elevated, unresolved
legal-risk category **specific to the sports-contract product**, not
Kalshi's weather/climate contracts, which do not appear anywhere in this
litigation. This is exactly the kind of risk Session 0.1 named "legal
footprint" to capture, and exactly why Track 3 was originally scoped
narrowly (weather/climate, *narrow* down-ballot politics only) rather
than broadly across everything Kalshi lists.

## What the evidence actually supports

Applying Session 0.1's own method to real data gathered today, the
evidence does **not** support expanding Track 3 into Kalshi's direct
sports markets:
- The repricing mechanism matches Track 6 (already correctly ranked
  lowest-confidence) more than Track 3.
- The one genuinely new, favorable fact (free public API access) was
  already priced into Kalshi's existing ranking — it isn't new evidence
  about the *sports* product specifically.
- Real liquidity checked directly is thin, at least for games several
  days out.
- Real legal footprint checked directly is the most actively contested,
  least settled category found anywhere in this project's research so
  far — actively fought in court, with at least one state (Arizona)
  pursuing criminal charges.

**Recommendation, not a decision:** Track 3's original scope (weather/
climate, narrow down-ballot politics) should stay as originally ranked.
The free, no-login API access confirmed today is a genuine, useful fact
for **building** Track 3 when its own session comes up (it de-risks the
data-access question Session 0.1 flagged as unresolved) — but it is not,
on the evidence gathered, a reason to expand Track 3's scope into direct
sports contracts, or to move Track 3 ahead of Track 2 (arbitrage) in
priority. If anything, this reinforces Track 6's original "lowest
confidence" ranking, since it's now confirmed with real data (not just
reasoning) that Kalshi's own sports markets show the same thin-liquidity,
contested-legality profile that ranking already predicted.

This stays a recommendation for your review, not an applied decision —
consistent with how every other ranking call in this project has been
made.

---

## Handoff notes for `sport_inventory_scan.py`

The version already sent to you has the corrected PrizePicks endpoint
(`partner-api.prizepicks.com`, not `api.prizepicks.com` — the original
version's 403 error was Claude's own mistake, using an endpoint it never
verified against the real, working production script). No further script
changes are needed before your next run.
