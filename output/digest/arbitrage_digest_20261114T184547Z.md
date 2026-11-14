# Arbitrage Pipeline Digest -- 2026-11-14T18:45:47Z

## Run summary
- Kalshi ingestion: 2942 rows kept (746 target series, 95 down-ballot)
- Polymarket ingestion: 22053 rows
- Venue matching: 22 candidate pairs (12 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 22 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will Waymo launch in New York, NY by December 31 2026? | 0.043 | kalshi | Rain in New York City on Dec 31, 2026? | 0.72 | 0.2149 | True | both_venues_available |
