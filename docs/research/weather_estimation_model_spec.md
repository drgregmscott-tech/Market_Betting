# Weather Threshold Estimation Model — Spec (Session 4.2)

Documented at the same specificity level as `pickem_estimation_model_spec.md`
(Session 2.3): every input, every formula, every named constant and its
evidence basis, and every stated gap.

## What this model answers

For every real, live Kalshi weather-threshold contract Session 4.1 ingests
(e.g. *"Will Philadelphia's high temperature be over 85°F on September 7,
2026?"*), this model computes this project's own real probability estimate
that the contract resolves YES, so it can be compared against Kalshi's own
live `yes_bid`/`yes_ask`.

## Inputs

| Input | Source | Real field(s) used |
|---|---|---|
| Contract threshold | `kalshi_weather_latest.csv` (Session 4.1) | `strike_type`, `floor_strike`, `cap_strike` |
| Point forecast | `nws_forecast_latest.csv` (Session 4.1) | `forecast_value_f`, joined on `(station_id, target_date, forecast_kind)` |
| Real measured forecast error (once it exists) | `forecast_error_by_leadtime.csv` (new, this session) | `mae_f`, `sample_count`, per `lead_days` |

## Why a single point forecast needed a manufactured uncertainty band

Confirmed live, this session: NWS's public gridded forecast returns **one
number** per station per day — no ensemble, no published confidence
interval. A probability model needs a real, documented spread to turn that
one number into a probability. See `weather_model.py`'s own module
docstring for the full investigation; summarized here:

## The blended uncertainty source (the model's core design decision)

**Starting point — literature-sourced, not this project's own data.**
Penn State's public course material (`courses.ems.psu.edu/meteo3/node/2285`,
accessed 2026-09-07), summarizing published U.S. temperature-forecast
verification research, states three real anchor points for daily high/low
MAE:

| Lead time | Cited MAE range | Anchor used (upper end, cautious) |
|---|---|---|
| ~1–2 days out | "3°F or less" | **2.5°F** (day 1) |
| ~3–4 days out | "3 to 4°F" | **4.0°F** (day 4) |
| ~7 days out | "5 to 6°F" | **5.5°F** (day 7) |

Days 2, 3, 5, and 6 are **linearly interpolated** between these three real,
cited anchors — this project's own modeling choice, clearly separated from
the literature's own numbers. Choosing the upper end of each cited range
(rather than the midpoint or lower end) is a deliberate, cautious choice:
underestimating uncertainty is the riskier error for a system whose whole
purpose is finding thin, real pricing gaps — an artificially narrow
confidence band would manufacture false-positive edges. Beyond day 7
(`MAX_LITERATURE_LEAD_DAY`), there is no real citation to extrapolate from,
so those contracts are marked `unsupported_lead_day` rather than guessed.

**Real data, collected automatically, replacing the placeholder bucket by
bucket.** A new scheduled GitHub Action
(`weather_calibration_pipeline.yml`) runs `ingest_nws_weather_data.py` once
daily and — unlike the arbitrage pipeline — **commits every day's raw and
normalized snapshot**, deliberately building a real historical record. A
new script, `weather_forecast_error.py`, recomputes this project's own real
mean absolute error per lead day from all accumulated snapshots on every
run. `weather_model.py` checks, **per lead-day bucket**, whether the real
file has reached `MIN_REAL_SAMPLES_PER_LEAD_DAY` (20, a named, round,
conservative starting threshold — not claimed as statistically optimal) real
samples for that specific lead day; if so, it uses the real measured MAE for
that bucket, otherwise it falls back to the literature anchor for that
bucket only. This means the model gets more accurate automatically, one
lead-day bucket at a time, with no future session needing to remember to
manually cut over.

**MAE → sigma conversion.** For a normal distribution,
`E[|X - mean|] = sigma * sqrt(2/π)`, so `sigma = MAE / sqrt(2/π)` — the
standard relationship, not an arbitrary multiplier.

**Settlement-gap term.** Session 4.1's Open Decision #31 found a real,
root-caused ~1°F gap between this project's own NWS-based reading and
Kalshi's actual settlement value (a rounding effect, not open-ended). This
is combined with the forecast-error sigma **in quadrature**
(`sqrt(forecast_sigma² + 1.0²)`) as an independent second error source, per
that decision's stated action for Session 4.2.

## Probability formula

The true temperature is modeled as normally distributed around the NWS
forecast value (mean) with the lead-day-specific sigma above. Kalshi's own
real structured threshold fields determine the formula:

- `strike_type == "greater"`: `P(YES) = 1 − Φ(floor_strike; mean, σ)`
- `strike_type == "less"`: `P(YES) = Φ(cap_strike; mean, σ)`
- `strike_type == "between"`: `P(YES) = Φ(cap_strike; mean, σ) − Φ(floor_strike; mean, σ)`

Implemented via Python's built-in `math.erf` (no third-party stats
dependency needed for a single normal distribution).

## What every output row contains

Every real Kalshi weather contract gets a row in the output, with either a
real probability estimate or an explicit `model_status` explaining why it
couldn't be estimated — nothing silently dropped (same standard
`pickem_model.py` set in Session 2.3):

`estimated` · `no_forecast_kind` · `no_forecast_data` · `target_date_passed`
· `unsupported_lead_day` · `missing_strike_fields`

Every estimated row also records `sigma_source` (`literature_placeholder` or
`real_measured`) so the uncertainty source behind any given estimate is
auditable, not hidden.

## Stated gaps (v1, this session)

1. **No real measured error data exists yet at hand-off.** The literature
   placeholder is what every estimate will use until the new daily pipeline
   accumulates `MIN_REAL_SAMPLES_PER_LEAD_DAY` real samples per bucket —
   expect this to take several real weeks for the shortest lead days.
2. **No regional variation.** Real published research (a 2024 Washington
   Post analysis of a full year of NWS's own shared verification data)
   found forecast accuracy genuinely varies by region — the Great Plains
   degrades faster than the Southwest or Florida. This model applies one
   national curve to every station. Left out deliberately rather than
   guessing regional multipliers with no real per-station backing yet;
   worth revisiting once this project's own real per-station data
   (collected by the same new pipeline) is large enough to check.
3. **`MAX_LITERATURE_LEAD_DAY` (7) is not yet confirmed against NWS's real
   forecast horizon.** Session 4.1 did not check the real maximum number of
   days `forecastGridData` returns. If Kalshi lists a contract further out
   than NWS's real forecast horizon, or further out than 7 days, that
   contract is marked `unsupported_lead_day` — a safe default, but the real
   NWS horizon should be confirmed with live data, not assumed, in a future
   session.
4. **No sizing, flagging, or CLV logging.** Same ingestion/estimation
   boundary `schema_weather.py` and `pickem_model.py` already established —
   Session 4.3 wires this into that downstream pipeline.
