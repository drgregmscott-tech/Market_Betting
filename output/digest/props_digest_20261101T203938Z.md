# Props Pipeline Digest -- 2026-11-01T20:39:38Z

## Run summary
- DraftKings ingestion: 0 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 533 rows (OK)
- Estimation: 533 rows written (from 533 ingested rows) -- status breakdown: {'estimated': 222, 'unsupported_stat_type': 184, 'unsupported_market_first_scorer': 101, 'no_player_match': 20, 'insufficient_history': 6}
- CLV logging: 2 newly flagged, 0 newly closed, 4 still open (1344 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|15924 | betmgm | Charlie Kolar | recs | over | 1.0 | 0.4653 | 0.5347 | False | 2026-10-29T21:16:56Z |
| betmgm|anytd|19343 | betmgm | Caleb Douglas | anytd | over | 0.5374 | 0.2041 | 0.3333 | False | 2026-10-28T15:16:18Z |
| betmgm|anytd|11712 | betmgm | Deshaun Watson | anytd | over | 0.2184 | 0.0952 | 0.1232 | False | 2026-11-01T20:39:53Z |
| betmgm|anytd|19263 | betmgm | Germie Bernard | anytd | over | 0.1881 | 0.0667 | 0.1214 | False | 2026-11-01T20:39:53Z |
