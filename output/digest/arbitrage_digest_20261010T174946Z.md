# Arbitrage Pipeline Digest -- 2026-10-10T17:49:46Z

## Run summary
- Kalshi ingestion: 2419 rows kept (615 target series, 94 down-ballot)
- Polymarket ingestion: 18900 rows
- Venue matching: 480 candidate pairs (472 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 480 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.92 | 0.0648 | False | both_venues_available |
| cross_venue | kalshi | Will a Category 4 hurricane make landfall in Tampa before 2027? | 0.03 | polymarket | Will any Category 4 hurricane make landfall in the US in before 2027? | 0.94 | 0.0172 | True | both_venues_available |
