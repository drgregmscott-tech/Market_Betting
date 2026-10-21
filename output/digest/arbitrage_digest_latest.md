# Arbitrage Pipeline Digest -- 2026-10-21T18:00:58Z

## Run summary
- Kalshi ingestion: 3262 rows kept (654 target series, 94 down-ballot)
- Polymarket ingestion: 19171 rows
- Venue matching: 480 candidate pairs (472 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 480 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.003 | kalshi | Snow in New York City in Dec 2026? | 0.8 | 0.1769 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.003 | kalshi | Snow in New York City in Dec 2026? | 0.89 | 0.0969 | False | both_venues_available |
