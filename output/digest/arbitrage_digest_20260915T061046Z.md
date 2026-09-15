# Arbitrage Pipeline Digest -- 2026-09-15T06:10:46Z

## Run summary
- Kalshi ingestion: 2438 rows kept (565 target series, 94 down-ballot)
- Polymarket ingestion: 20545 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Democratic Party win the NY-17 House seat? | 0.57 | kalshi | Will Democratic win the House race for NY-17? | 0.39 | 0.0102 | False | both_venues_available |
