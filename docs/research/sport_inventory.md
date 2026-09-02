# Sport Inventory — Track 1 (Fixed-Line Pick'em Platforms)

Session: 2.10 — Cross-Sport +EV Inventory
Status: **DRAFT — not final, and Part 2 is intentionally left as an open
research item, not a decision, per direction that there isn't enough
information yet to decide anything.** Underdog's pick'em product is partly
checked. PrizePicks pick'em is not yet checked. Both companies' non-pick'em
products are named but not yet investigated in enough depth to act on.

This document exists to stop Track 1's scope from silently narrowing to
whichever sport happens to be visible at the moment (Open Decision #14).
It records, for every sport actually seen on each platform: whether a
public data source exists to grade it, and whether it's a near-term
candidate, a real build-out, or ruled out.

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

## Confirmed live right now — Underdog

Checked directly by Claude, via Underdog's live public endpoint
(`api.underdogfantasy.com/beta/v3/over_under_lines`), on 2026-09-02
(mid-afternoon, US time). This is a snapshot at one moment — the mix will
change hour to hour.

| Sport (Underdog `sport_id`) | Container | Count seen | What kind of props |
|---|---|---|---|
| NFL | `appearances` tagged `match_type: "Series"` | 125 players | Season-long futures (e.g. "Higher 8.5 Regular Season Games Started") — **not weekly game props**, since the regular season has not started yet (starts 2026-09-07) |
| CFB (college football) | `games` (1 live game) + some `appearances` | 3 players | Per-game props, real live game found |
| Tennis | `solo_games` (40 live matches) | 54 players, 76 appearances | Per-match props (e.g. Aces, Double Faults, Games Won) |
| MLB | — | **0 found** | Not present in this particular snapshot — see note below |

**MLB note:** MLB is mid-season right now, so its complete absence from
this one snapshot is more likely a timing artifact (this snapshot happened
to catch a moment with no MLB lines posted yet) than genuine unavailability.
The roadmap card for this session explicitly requires MLB to be checked —
this snapshot does not satisfy that requirement on its own. **Action
needed:** re-run the scan below in the evening (US time), when MLB games
are more likely to be in progress, before treating "MLB not on Underdog" as
a real finding.

---

## PrizePicks — not yet checked

Claude's browser tool is blocked by its own safety category filter from
reaching `prizepicks.com`, the same restriction recorded back in Session
2.1. This has not changed. PrizePicks cannot be inventoried from Claude's
side at all.

**Action needed:** run the attached `sport_inventory_scan.py` on your own
machine (same pattern as Session 2.1's prototype scripts). It prints a
league-by-league breakdown of every live PrizePicks projection at the
moment you run it, plus a second, independent read of Underdog for
comparison. Paste the output back and Claude will fold it into this
document and finish the "candidates" table below.

---

## Data source availability, by sport

This is the actual gate: a sport can have plenty of betting lines and still
be unbuildable if there's nowhere to check what really happened.

| Sport | Data source found | Free / public? | Notes |
|---|---|---|---|
| NFL | `nflverse` (already in use, `pickem_model.py`) | Yes | Already the project's production source. No change needed. |
| MLB | MLB Stats API (`statsapi.mlb.com`) | Yes, no key or account needed | Official MLB source. Near real-time box scores and player-level stats. Strong candidate — same "official, free, no-key" shape as `nflverse`. |
| CFB (college football) | College Football Data API (`collegefootballdata.com`) | Yes, free tier, but requires a free API key | Free tier is capped at 1,000 calls/month — workable for this project's likely call volume, but the cap must be respected in any ingestion design, unlike `nflverse`/MLB which have no such limit. |
| Tennis | No free, real-time, per-match stats source found | No | Paid real-time providers exist (Sportradar and similar) but all require a paid plan. A free historical dataset (Jeff Sackmann's public `tennis_atp`/`tennis_wta` match archives on GitHub) exists but updates with a lag and is not built for grading a specific prop shortly after a match ends. This is a real gap, not a "not researched yet" gap. |

---

## Candidates (draft — will be finalized once PrizePicks is checked)

**Near-term candidate (data source ready, real live lines confirmed):**
- **MLB** — free official data source found; presence on the platforms
  still needs the evening re-check noted above before this is confirmed
  rather than assumed.

**Real build-out required (real live lines exist, but the data-source
question isn't a quick add):**
- **CFB** — real live game and props confirmed on Underdog. Data source
  exists (CFBD API) but needs a free API key and has a monthly call cap
  that NFL/MLB don't have — a small but real integration difference from
  the existing `nflverse` pattern, not a drop-in.
- **Tennis** — real, substantial volume confirmed on Underdog (54 players,
  76 appearances at this snapshot alone). No adequate free real-time data
  source was found. Building this out would mean either paying for a
  provider or accepting a lag-based, less-precise grading source — a real
  decision for the user, not a default "yes, build it."

**Ruled out:**
- None yet. Nothing checked so far has come back with no live lines at
  all — the question for every sport checked has been data-source
  availability, not whether it's actually traded.

**Not yet checked:** everything on PrizePicks, and any sport that might
exist on either platform outside the categories already seen (e.g. NBA,
NHL, soccer, esports, golf) — none of those appeared in this snapshot, but
"didn't appear in one snapshot" is not the same as "confirmed absent." A
second, later-in-day check (the same run needed for the MLB question) will
also help settle this.

---

## What still needs to happen before Part 1 can close

1. Run `sport_inventory_scan.py` on your machine (fixed endpoint, see
   handoff notes) and send back the output — this is the only way to
   check PrizePicks at all, and gives a second, independent read on
   Underdog.
2. Run the scan several more times, spread across at least one full day
   (morning/afternoon/evening) and ideally a few different days, since a
   single evening re-check only adds one more moment in time, not real
   day-of-week or time-of-day coverage. Each run should be logged with
   its own timestamp so the sport list can be built up as a **union**
   across runs, not treated as a single truth.
3. Once enough runs are in hand to have seen the platforms' real range
   (a working stopping condition — matching this project's own standing
   practice, e.g. Session 2.1's evidence-based stopping rule, rather than
   a fixed number picked in advance — might be: no new sport appears
   across 3 consecutive runs spread across different times of day), Claude
   will fill in the PrizePicks rows, finalize the candidates list, and
   propose any warranted ROADMAP.md additions.
4. Only after you and Claude agree Part 1's validation checklist is fully
   satisfied will ROADMAP.md and SESSION_LOG.md be updated for that part
   of Session 2.10.

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

## Handoff notes for `sport_inventory_scan.py`

The version already sent to you has the corrected PrizePicks endpoint
(`partner-api.prizepicks.com`, not `api.prizepicks.com` — the original
version's 403 error was Claude's own mistake, using an endpoint it never
verified against the real, working production script). No further script
changes are needed before your next run.
