# Arbitrage Pipeline Digest -- 2026-09-09T19:45:43Z

## Run summary
- Kalshi ingestion: 2545 rows kept (561 target series, 94 down-ballot)
- Polymarket ingestion: 20646 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 4 flags (0 single-venue, 4 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Republican Party win the TX-32 House seat? | 0.81 | kalshi | Will Republican win the House race for TX-32? | 0.16 | 0.0138 | False | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the IA-01 House seat? | 0.28 | kalshi | Will Republican win the House race for IA-1? | 0.68 | 0.0119 | True | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the NY-17 House seat? | 0.33 | kalshi | Will Republican win the House race for NY-17? | 0.63 | 0.0112 | True | both_venues_available |
| cross_venue | kalshi | Will Democratic win the House race for NY-17? | 0.62 | polymarket | Will the Democratic Party win the NY-17 House seat? | 0.3399999999999999 | 0.011 | False | both_venues_available |
