# Props Pipeline Digest -- 2026-11-15T21:09:05Z

## Run summary
- DraftKings ingestion: 82 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 542 rows (OK)
- Estimation: 624 rows written (from 624 ingested rows) -- status breakdown: {'estimated': 282, 'unsupported_stat_type': 172, 'unsupported_market_first_scorer': 126, 'no_player_match': 36, 'insufficient_history': 8}
- CLV logging: 6 newly flagged, 0 newly closed, 15 still open (1590 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|14636 | betmgm | Devin Duvernay | recs | over | 1.0 | 0.4335 | 0.5665 | False | 2026-11-15T06:52:17Z |
| betmgm|anytd|16034 | betmgm | Teagan Quitoriano | anytd | over | 0.6002 | 0.0476 | 0.5525 | False | 2026-11-12T07:29:25Z |
| betmgm|recs|15229 | betmgm | Tutu Atwell | recs | over | 1.0 | 0.4797 | 0.5203 | False | 2026-11-13T22:04:26Z |
| betmgm|recs|15559 | betmgm | Simi Fehoko | recs | over | 0.9529 | 0.4425 | 0.5104 | False | 2026-11-13T22:04:26Z |
| betmgm|recs|16897 | betmgm | Zach Charbonnet | recs | over | 1.0 | 0.5575 | 0.4425 | False | 2026-11-14T06:47:45Z |
| betmgm|anytd|19258 | betmgm | Jack Endries | anytd | over | 0.3677 | 0.0714 | 0.2962 | False | 2026-11-10T21:54:10Z |
| betmgm|anytd|14608 | betmgm | Charlie Woerner | anytd | over | 0.2277 | 0.087 | 0.1407 | False | 2026-11-12T07:29:25Z |
| draftkings|387687955|0QA387687955#2358299677_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.253 | 0.1333 | 0.1196 | False | 2026-11-15T21:09:21Z |
| draftkings|387687955|0QA387687955#2358299679_13L88808Q1-1863661381Q20 | draftkings | Deebo Samuel | Anytime TD Scorer | over | 0.4316 | 0.3448 | 0.0868 | False | 2026-11-15T21:09:21Z |
| draftkings|388118989|0QA388118989#2360320733_13L88808Q1-1442390665Q20 | draftkings | Christian McCaffrey | 2+ TDs | over | 0.4082 | 0.3279 | 0.0803 | False | 2026-11-15T21:09:21Z |
| betmgm|anytd|18647 | betmgm | Jordan Watkins | anytd | over | 0.2704 | 0.2041 | 0.0663 | False | 2026-11-13T22:04:26Z |
| draftkings|387687955|0QA387687955#2358299676_13L88808Q11030682857Q20 | draftkings | Jordan Watkins | Anytime TD Scorer | over | 0.2704 | 0.2083 | 0.062 | False | 2026-11-15T21:09:21Z |
| draftkings|388118989|0QA388118989#2360320735_13L88808Q1-1288734733Q20 | draftkings | Deebo Samuel | 2+ TDs | over | 0.1105 | 0.0625 | 0.048 | False | 2026-11-15T21:09:21Z |
| betmgm|anytd|13854 | betmgm | Ashton Dulin | anytd | over | 0.2404 | 0.2041 | 0.0363 | False | 2026-11-12T07:29:25Z |
| draftkings|387687955|0QA387687955#2358299664_13L88808Q1795642865Q20 | draftkings | Dak Prescott | Anytime TD Scorer | over | 0.1652 | 0.1333 | 0.0319 | False | 2026-11-15T21:09:21Z |
