# Arbitrage Pipeline Digest -- 2026-09-13T23:09:48Z

## Run summary
- Kalshi ingestion: 2654 rows kept (565 target series, 94 down-ballot)
- Polymarket ingestion: 20484 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Republican Party win the TX-15 House seat? | 0.36 | kalshi | Will Republican win the House race for TX-15? | 0.59 | 0.0208 | True | both_venues_available |
| cross_venue | kalshi | Will Democratic win the House race for AK-AL? | 0.046 | polymarket | Will the Democratic Party win the AK-AL House seat? | 0.93 | 0.0114 | True | both_venues_available |
