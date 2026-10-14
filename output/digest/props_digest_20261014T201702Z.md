# Props Pipeline Digest -- 2026-10-14T20:17:02Z

## Run summary
- DraftKings ingestion: 0 rows across 0 events (FAILED -- see logs/ingestion.log)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 661 rows (OK)
- Estimation: 661 rows written (from 661 ingested rows) -- status breakdown: {'estimated': 325, 'unsupported_market_first_scorer': 202, 'unsupported_stat_type': 105, 'no_player_match': 15, 'insufficient_history': 14}
- CLV logging: 2 newly flagged, 0 newly closed, 5 still open (1015 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|19448 | betmgm | Nate Boerkircher | recs | over | 1.0 | 0.5941 | 0.4059 | False | 2026-10-13T19:24:28Z |
| betmgm|anytd|16751 | betmgm | DeMario Douglas | anytd | over | 0.4231 | 0.2632 | 0.1599 | False | 2026-10-14T20:17:30Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| betmgm|anytd|19126 | betmgm | Kyle Williams | anytd | over | 0.2404 | 0.2 | 0.0404 | False | 2026-10-14T20:17:30Z |
| betmgm|anytd|17593 | betmgm | Emanuel Wilson | anytd | over | 0.5157 | 0.4762 | 0.0395 | False | 2026-10-13T11:58:47Z |
