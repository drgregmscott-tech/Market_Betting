# Arbitrage Pipeline Digest -- 2026-10-02T18:23:12Z

## Run summary
- Kalshi ingestion: 3008 rows kept (594 target series, 94 down-ballot)
- Polymarket ingestion: 19184 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.012 | kalshi | Snow in New York City in Dec 2026? | 0.9 | 0.0774 | True | both_venues_available |
