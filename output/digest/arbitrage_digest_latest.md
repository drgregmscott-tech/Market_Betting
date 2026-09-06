# Arbitrage Pipeline Digest -- 2026-09-06T10:09:26Z

## Run summary
- Kalshi ingestion: 1539 rows kept (541 target series, 93 down-ballot)
- Polymarket ingestion: 20703 rows
- Venue matching: 497 candidate pairs (497 elections-wide)
- Detection: 10 flags (0 single-venue, 10 cross-venue) from 497 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will a Republican win the House race for WA-08? | 0.055 | polymarket | Will the Republican Party win the IN-08 House seat? | 0.033 | 0.9007 | True | both_venues_available |
| cross_venue | kalshi | Will Democratic win the House race for UT-03? | 0.099 | polymarket | Will the Democratic Party win the OR-03 House seat? | 0.046 | 0.8432 | True | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the OR-03 House seat? | 0.047 | kalshi | Will Republican win the House race for UT-03? | 0.099 | 0.8422 | True | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for MO-05? | 0.23 | polymarket | Will the Republican Party win the IN-05 House seat? | 0.17 | 0.5744 | True | both_venues_available |
| cross_venue | polymarket | Will the Democratic Party win the IN-05 House seat? | 0.17 | kalshi | Will Democratic win the House race for MO-05? | 0.23 | 0.5744 | False | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the OR-05 House seat? | 0.076 | kalshi | Will Republican win the House race for MO-05? | 0.79 | 0.1112 | False | both_venues_available |
| cross_venue | kalshi | Will Democratic win the House race for MO-05? | 0.8 | polymarket | Will the Democratic Party win the OR-05 House seat? | 0.0899999999999999 | 0.0867 | False | both_venues_available |
| cross_venue | polymarket | Will the Democratic Party win the IN-09 House seat? | 0.06 | kalshi | Will Democratic win the House race for TX-09? | 0.85 | 0.0777 | False | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for TX-09? | 0.86 | polymarket | Will the Republican Party win the IN-09 House seat? | 0.06 | 0.0677 | True | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the MI-07 House seat? | 0.4 | kalshi | Will Republican win the House race for MI-7? | 0.56 | 0.0104 | True | both_venues_available |
