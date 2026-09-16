# Arbitrage Pipeline Digest -- 2026-09-16T06:01:58Z

## Run summary
- Kalshi ingestion: 2420 rows kept (566 target series, 94 down-ballot)
- Polymarket ingestion: 20516 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 3 flags (0 single-venue, 3 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will a Republican win the House race for NH-1? | 0.073 | polymarket | Will the Republican Party win the NH-01 House seat? | 0.89 | 0.0231 | True | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for TX-09? | 0.87 | polymarket | Will the Republican Party win the TX-09 House seat? | 0.0999999999999999 | 0.0164 | True | both_venues_available |
| cross_venue | polymarket | Will the Democratic Party win the TX-09 House seat? | 0.1 | kalshi | Will Democratic win the House race for TX-09? | 0.87 | 0.0164 | False | both_venues_available |
