# Pick'em Platform Endpoint Schemas — Session 2.1 Findings

**Status as of 2026-08-28:** Updated after the user ran all three prototype
scripts locally. Underdog and PrizePicks are now confirmed live with real
field names captured below. DK Pick6's guessed endpoint failed (404) as
expected — whether to keep researching it or drop it from scope is an open
decision, not yet resolved as of this update.

## Why this file exists

Session 2.1's job is to find out, for real, whether each of the three pick'em
platforms' data can actually be pulled by a script with no login and no API
key, and what shape that data comes back in. Session 2.3 (the estimation
model) depends on knowing the real field names — guessing them in advance
would risk building a model around fields that don't exist or are named
differently than assumed.

---

## Underdog Fantasy — CONFIRMED LIVE (2026-08-28)

**Endpoint:** `https://api.underdogfantasy.com/beta/v3/over_under_lines`
**Auth required:** None. Confirmed reachable directly, no login, no API key,
no special headers beyond a normal browser User-Agent.
**Confirmed by:** Live browser-based test during this session (not just
secondhand documentation).

**Response shape:** A single JSON object with these top-level lists,
cross-referenced by ID rather than nested inline (a "normalized" shape — you
must join across lists to build one full record):

| Top-level key | What it holds |
|---|---|
| `over_under_lines` | The actual prop lines — one entry per player/stat combination |
| `appearances` | Links a player to a specific game and team for that slate |
| `players` | Player name and metadata, looked up by `player_id` |
| `games` | Game/match schedule and matchup info, looked up by `match_id` |
| `providers` | Metadata about the data provider(s) backing the lines |
| `solo_games` | Present in the schema; empty (0 items) in the sample pulled |

**`over_under_lines` record fields** (confirmed from a live sample):
`id`, `contract_terms_url`, `contract_url`, `entry_stable_id`, `expires_at`,
`line_type`, `live_event`, `live_event_stat`, `non_discounted_stat_value`,
`options`, `over_under`, `over_under_id`, `provider_id`, `rank`, `sort_by`,
`stable_id`, `stat_value`, `status`, `updated_at`.

- `stat_value` is the actual line (e.g. `"8.5"`) — **returned as a string,
  not a number.** Session 2.2's normalization step needs to convert this.
- `over_under` is a nested object naming the stat itself (e.g. `"display_stat":
  "Regular Season Games Started"`), and contains an `appearance_stat` sub-object
  linking back to `appearance_id`.
- `options` is a list — typically the "Higher"/"Lower" choices — each with its
  own `american_price`, `decimal_price`, and `payout_multiplier`. This is
  where the actual payout structure lives, separate from the line itself.

**What this means for Session 2.2:** building one clean row of "Player X,
Stat Y, Line Z, Game W, Payout Multiplier" requires joining
`over_under_lines` → `appearances` (via `appearance_id` inside the nested
`over_under` object) → `players` (via `player_id`) → `games` (via
`match_id`). This is not a single flat table today.

**What breaks the pull:** Not yet determined — only a single successful pull
was performed this session. Recommend the first few days of Session 2.2's
production pipeline specifically watch for rate-limiting (HTTP 429) or
schema drift, since none was observed in this one-off test.

---

## PrizePicks — CONFIRMED LIVE (2026-08-28, by the user)

**Endpoint:** `https://partner-api.prizepicks.com/projections`
**Auth required:** None. Confirmed reachable directly, no login, no API key.
**Confirmed by:** Live run of `prototype_prizepicks.py` on the user's
machine. Response received in 2.01s.

**Response shape:** Confirmed as a JSON:API-style payload, as expected from
outside documentation, with real field names now captured directly:

| Top-level key | What it holds |
|---|---|
| `data` | 21,203 projections in the sample pull — type `"projection"` |
| `included` | 5,417 cross-referenced records of 7 different types (see below) |
| `links` | Not a list — pagination-related metadata |
| `meta` | Not a list — response-level metadata |

**`data` (projection) record fields** — under `attributes`:
`adjusted_odds`, `allowed_wager_types`, `board_time`, `custom_image`,
`description`, `discount_name`, `discount_percentage`, `end_time`,
`event_type`, `flash_sale_line_score`, `game_id`, `group_key`, `hr_20`,
`in_game`, `is_live`, `is_live_scored`, `is_promo`, `line_score`,
`odds_type`, `projection_type`, `rank`, `refundable`, `start_time`,
`stat_display_name`, `stat_type`, `status`, `trending_count`, `tv_channel`,
`updated_at`.

- **`line_score` is the actual prop line** (the equivalent of Underdog's
  `stat_value`). `stat_display_name`/`stat_type` name the stat.
- Under `relationships`: `duration`, `game`, `league`, `new_player`,
  `projection_type`, `score`, `stat_type` — each an ID pointing into
  `included`.

**`included` record types found, with real fields per type:**

| Type | Key fields |
|---|---|
| `duration` | `name` |
| `game` | `created_at`, `end_time`, `external_game_id`, `is_live`, `metadata`, `start_time`, `status`, `updated_at` |
| `league` | `active`, `full_logo`, `has_live_projections`, `name`, `rank`, and others (sport/league metadata) |
| `new_player` | `display_name`, `league`, `market`, `name`, `position`, `team`, `team_name` — **this is the player record**, named `new_player` rather than `player` |
| `projection_type` | `name` |
| `stat_type` | `name`, `rank`, `lfg_ignored_leagues` |
| `team` | `abbreviation`, `market`, `name`, and branding fields |

**What this means for Session 2.2:** same join pattern as Underdog — build
one clean row by following `data[].relationships.new_player` (note the field
name: `new_player`, not `player`) into `included`, matched by type and ID.
The player's real name is under `new_player.attributes.display_name` or
`.name`.

**What breaks the pull:** Not yet determined — only one successful pull
performed so far. No rate-limiting or blocking was observed on this first
run, despite the endpoint returning a large volume of data (21,203 records)
in about 2 seconds.

---

## DK Pick6 — GUESSED ENDPOINT FAILED (2026-08-28); SCOPE DECISION PENDING

**Endpoint used in the prototype script:**
`https://api.draftkings.com/pick6/v1/leagues` — this was always a guess, built
by analogy to DraftKings' other documented APIs, not a confirmed real URL.
**Result:** `404 Client Error: Not Found`. Failed as anticipated — this does
not mean Pick6 has no data endpoint, only that this specific guessed URL is
wrong.

**Status: open decision, not yet resolved.** The user has indicated openness
to dropping DK Pick6 from Track 1's scope entirely rather than continuing to
hunt for its real endpoint manually via browser Developer Tools, given no
credible public documentation exists and the manual reverse-engineering steps
in `prototype_dkpick6.py`'s docstring offer no guarantee of success (Pick6's
data may also require a logged-in session, which would break this project's
"no login required" design principle for pick'em ingestion). **This decision
had not been finalized as of this document's last update — check
ROADMAP.md's Phase 2 description and Open Decisions section for whether it
was formally dropped, and if so, when.**

---

## Summary table

| Platform | Endpoint confirmed live? | Auth needed? | Schema documented? |
|---|---|---|---|
| Underdog | **Yes** (this session) | No | Yes, from a real sample |
| PrizePicks | **Yes** (this session) | No | Yes, from a real sample |
| DK Pick6 | No — guessed endpoint 404'd | Unknown | No — real endpoint not found |

## What Session 2.1's validation checklist actually needs from here

The roadmap's four validation items for this session are:
1. All three endpoints return live data with no login/key — **2 of 3
   confirmed (Underdog, PrizePicks). DK Pick6's status depends on the pending
   scope decision — either keep researching it, or formally drop it from
   Track 1 and update this item to reflect a 2-platform scope.**
2. Schema documented per platform — **done for Underdog and PrizePicks, both
   from real captured output. DK Pick6 has no schema since no working
   endpoint was found.**
3. At least one full day's snapshot captured — **not yet; only one run each
   for Underdog and PrizePicks so far. This needs repeat runs spaced out over
   a real day.**
4. Explicit note on what breaks the pull — **not yet observed for either
   working platform; needs real repeated runs, ideally including a run during
   a period of likely high traffic (e.g. close to a major slate's lock
   time).**
