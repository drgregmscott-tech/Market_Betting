# Arbitrage Pipeline Digest -- 2026-11-11T20:12:24Z

## Run summary
- Kalshi ingestion: 3431 rows kept (717 target series, 95 down-ballot)
- Polymarket ingestion: 22198 rows
- Venue matching: 24 candidate pairs (14 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 24 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will Waymo launch in New York, NY by December 31 2026? | 0.05 | kalshi | Rain in New York City on Dec 31, 2026? | 0.72 | 0.2076 | False | both_venues_available |
