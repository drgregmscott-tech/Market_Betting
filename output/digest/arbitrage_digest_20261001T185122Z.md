# Arbitrage Pipeline Digest -- 2026-10-01T18:51:22Z

## Run summary
- Kalshi ingestion: 2800 rows kept (589 target series, 94 down-ballot)
- Polymarket ingestion: 19193 rows
- Venue matching: 472 candidate pairs (472 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 472 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will Democratic win the House race for NM-2? | 0.927 | polymarket | Will the Democratic Party win the NM-02 House seat? | 0.05 | 0.0111 | True | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the VA-01 House seat? | 0.46 | kalshi | Will Republican win the House race for VA-1? | 0.5 | 0.0101 | True | both_venues_available |
