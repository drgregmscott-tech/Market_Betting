# Session 4.1 — Weather Data Freshness Check

## What "freshness" means here

Before this project can trust a weather-market position, our own forecast
number for a city's temperature has to exist BEFORE Kalshi's market for
that same city and day closes. If our data showed up late, we would be
guessing blind or copying the market's own price back at itself. This
document records the real, live numbers checked on 2026-09-06 that answer
that question, plus the second freshness question that matters once a
market is over: does the actual observed temperature become available in
time to grade the position.

## Real close times observed (from the committed `kalshi_weather_latest.csv`,
run 2026-09-06T19:15:56Z, 576 real rows across 62 series)

Every market's `close_time` fell into one of these eight, real, live values:

| target_date | close_time (UTC) |
|---|---|
| 2026-09-06 | 2026-09-07T05:00:00Z – 08:00:00Z |
| 2026-09-07 | 2026-09-08T05:00:00Z – 08:00:00Z |

The four-hour spread within each date is real, not noise — it reflects
the different US time zones of the 24 mapped cities. A market closes a
few hours after its own city's calendar day ends locally, not at one
fixed UTC time for every city.

## Real forecast lead time (from a live NWS gridpoint pull, same day)

NWS's own gridded forecast for Philadelphia (station KPHL, office PHI,
grid 48,75), pulled live: `updateTime: 2026-09-06T08:09:46Z`, with daily
max-temperature values published out to `validTimes: .../P7DT23H` — just
under 8 real days ahead from that update.

Concretely: the forecast value for target_date 2026-09-07 was already
sitting in NWS's public API roughly **31–34 hours before** the earliest
Kalshi market for that date closes (2026-09-08T05:00Z), and this project
would in practice have several more forecast updates land in that window
too, since NWS revises its grid multiple times a day, not once.

**Conclusion: forecast data has a wide, comfortable lead over market
close — not a photo finish.** This is not a borderline pass.

## Real observation lead time (grading side)

Pulled live the same day: KPHL's observation feed had already logged
**192 real readings for the still-in-progress calendar day** by 19:09Z —
close to one reading every 3–4 minutes. A full day's actual high and low
is therefore known within minutes of that local day ending, many hours
before Kalshi's own close_time for that market (which comes 5–8 hours
after local midnight). Grading a resolved market does not have to wait on
this project's own pipeline cadence — the real data is already there well
in advance.

## What this does NOT check yet

This confirms data ARRIVES in time. It does not yet confirm the forecast
is ACCURATE, or measure how often NWS's grid actually gets revised in a
real day (assumed "multiple times daily" from general knowledge of NWS's
publishing practice, not measured directly this session — a fair thing
for a future session to verify with a real multi-pull-a-day comparison
once this pipeline is scheduled, Session 4.5).

## Validation checkbox this closes

Session 4.1 roadmap checkbox: **"Data freshness confirmed adequate for
the market's resolution timing (data arrives before markets need to be
evaluated)"** — met, on real evidence above, both for the forecast side
(new data) and the observation side (grading past markets).
