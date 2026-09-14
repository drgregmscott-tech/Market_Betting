# Arbitrage Pipeline Digest -- 2026-09-14T23:52:37Z

## Run summary
- Kalshi ingestion: 2671 rows kept (565 target series, 94 down-ballot)
- Polymarket ingestion: 20595 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will Democratic win the House race for AK-AL? | 0.046 | polymarket | Will the Democratic Party win the AK-AL House seat? | 0.93 | 0.0114 | True | both_venues_available |
| cross_venue | polymarket | Will the Democratic Party win the NY-17 House seat? | 0.57 | kalshi | Will Democratic win the House race for NY-17? | 0.39 | 0.0102 | False | both_venues_available |
