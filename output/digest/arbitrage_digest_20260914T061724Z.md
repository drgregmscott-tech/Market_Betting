# Arbitrage Pipeline Digest -- 2026-09-14T06:17:24Z

## Run summary
- Kalshi ingestion: 2412 rows kept (565 target series, 94 down-ballot)
- Polymarket ingestion: 20544 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will Democratic win the House race for AK-AL? | 0.045 | polymarket | Will the Democratic Party win the AK-AL House seat? | 0.93 | 0.0124 | True | both_venues_available |
