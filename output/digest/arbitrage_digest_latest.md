# Arbitrage Pipeline Digest -- 2026-11-26T22:18:22Z

## Run summary
- Kalshi ingestion: 3151 rows kept (762 target series, 95 down-ballot)
- Polymarket ingestion: 23347 rows
- Venue matching: 10 candidate pairs (0 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 10 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will Waymo launch in New York, NY by December 31 2026? | 0.05 | kalshi | Rain in New York City on Dec 31, 2026? | 0.72 | 0.2076 | True | both_venues_available |
