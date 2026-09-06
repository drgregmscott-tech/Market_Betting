# Session 4.1 — NWS-vs-Settlement-Source Numeric Gap: Resolved

## The question this answers

Earlier in Session 4.1, comparing our NWS-based pipeline's daily high/low
against Kalshi's own settlement record for the same city and day showed
small differences (0.2°F to 0.9°F on the high, exact match on the low,
for Philadelphia, September 5, 2026). A second concern came up alongside
it: two pulls of our own pipeline's number for the same historical day
gave two different answers (84.2°F and 84.9°F). Both are now resolved.

## Finding 1: the pipeline "instability" was a bug in a quick manual
check, not in the real pipeline

The 84.9°F number came from an ad hoc verification script written to
double-check the pipeline's output, not from `ingest_nws_weather_data.py`
itself. That quick script converted each reading's UTC timestamp to
Philadelphia local time by formatting it as a locale string and parsing
that string back into a date — a known-fragile technique. Redone with a
direct, explicit UTC-offset conversion, it reproduced the production
pipeline's real number (84.2°F) exactly.

**Conclusion: `ingest_nws_weather_data.py`'s `zoneinfo`-based local-day
conversion (the actual production code) was correct the entire time.** No
code change was needed here — the bug was in a one-off manual check, now
discarded.

## Finding 2: the small gap against Kalshi's settlement record is a real,
bounded rounding effect, not an unexplained data discrepancy

Inspecting the real 5-minute-resolution readings around September 5's
peak showed the true high (84.2°F) was a brief, roughly 10-minute spike,
with readings of 82.4°F immediately before and after it. Kalshi's own
settlement feed (`weather.com/kalshi`'s API) stores exactly one value per
clock hour, and that hour's hour bucket reported 84°F — consistent with
"take the highest reading in the hour, then round to the nearest whole
degree," not an exact decimal reading the way this project's own NWS
pipeline keeps.

This means the two numbers are not drawn from different underlying
physical readings — they are the same real station's data, reported at
different precision. Kalshi's rounding-to-nearest-whole-degree,
once-per-hour convention puts a real, calculable ceiling on how far its
number can drift from an exact, all-readings maximum: **at most about
1°F**, the size of a single rounding step, not an open-ended or growing
gap.

## What this means going forward

Session 4.2 (Estimation Engine) should treat this project's own
forecast/observation numbers as accurate to roughly **±1°F** relative to
Kalshi's actual settlement value, by design — not as exact to a tenth of
a degree. Concretely: a contract whose threshold sits more than about 1°F
away from this project's estimated value can be sized with confidence
that the rounding effect described here won't flip the outcome. A
contract whose threshold sits within about 1°F of the estimate is now a
named, understood edge case, not a silent risk — Session 4.2's sizing
logic should treat these as lower-confidence, the same way this project
already discounts thin-liquidity or execution-risk positions elsewhere.

## Validation status

Both real, named gaps opened during Session 4.1's real-data checks are
now closed:
- Pipeline output stability: confirmed correct, root-caused to a
  verification-script bug, not a production bug.
- NWS-vs-settlement numeric gap: mechanically explained and bounded at
  ≈1°F, carried forward as a documented modeling input for Session 4.2
  rather than an open question.
