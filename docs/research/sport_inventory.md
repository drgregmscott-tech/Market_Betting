# Sport Inventory — Track 1 (Fixed-Line Pick'em Platforms)

Session: 2.10 — Cross-Sport +EV Inventory
Status: **DRAFT — not final.** Underdog is confirmed directly. PrizePicks is
not yet checked (see "How to finish this document" below) because Claude's
browser tool cannot reach prizepicks.com. MLB needs a second check at a
different time of day before this document can be treated as complete.

This document exists to stop Track 1's scope from silently narrowing to
whichever sport happens to be visible at the moment (Open Decision #14).
It records, for every sport actually seen live on each platform: whether a
public data source exists to grade it, and whether it's a near-term
candidate, a real build-out, or ruled out.

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

## What still needs to happen before this session can close

1. Run `sport_inventory_scan.py` on your machine and send back the output —
   this is the only way to check PrizePicks at all, and gives a second,
   independent read on Underdog.
2. Re-run the scan again in the evening (US time) specifically to settle
   the MLB question and catch any sport that wasn't live during today's
   afternoon snapshot.
3. Once both of those are in hand, Claude will fill in the PrizePicks rows
   of the tables above, finalize the candidates list, and — only if new
   sessions are actually warranted (e.g. a real MLB build-out session) —
   propose specific additions to ROADMAP.md for your review.
4. Only after you and Claude agree this session's validation checklist is
   fully satisfied will ROADMAP.md and SESSION_LOG.md be updated to close
   Session 2.10.
