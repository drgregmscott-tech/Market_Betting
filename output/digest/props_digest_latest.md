# Props Pipeline Digest -- 2026-10-25T19:10:09Z

## Run summary
- DraftKings ingestion: 85 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 613 rows (OK)
- Estimation: 698 rows written (from 698 ingested rows) -- status breakdown: {'estimated': 319, 'unsupported_stat_type': 187, 'unsupported_market_first_scorer': 131, 'no_player_match': 34, 'insufficient_history': 25, 'no_line_value': 2}
- CLV logging: 7 newly flagged, 0 newly closed, 14 still open (1236 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|14418 | betmgm | J.K. Dobbins | recs | over | 1.0 | 0.3666 | 0.6334 | False | 2026-10-23T20:01:31Z |
| betmgm|recs|14541 | betmgm | Adam Trautman | recs | over | 0.9947 | 0.491 | 0.5038 | False | 2026-10-25T19:10:21Z |
| draftkings|380432183|0QA380432183#2326700023_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.5075 | 0.0909 | 0.4166 | False | 2026-10-25T19:10:21Z |
| betmgm|recs|19631 | betmgm | Cyrus Allen | recs | over | 0.9993 | 0.625 | 0.3743 | False | 2026-10-25T04:59:12Z |
| draftkings|380432183|0QA380432183#2331429775_13L88808Q1-2126192684Q20 | draftkings | Jonah Coleman | Anytime TD Scorer | over | 0.4182 | 0.2174 | 0.2008 | False | 2026-10-25T19:10:21Z |
| betmgm|anytd|19241 | betmgm | Jonah Coleman | anytd | over | 0.4182 | 0.2174 | 0.2008 | False | 2026-10-24T12:49:27Z |
| betmgm|anytd|19426 | betmgm | Josh Cuevas | anytd | over | 0.2704 | 0.0909 | 0.1795 | False | 2026-10-22T05:06:55Z |
| betmgm|anytd|10729 | betmgm | Jared Goff | anytd | over | 0.2404 | 0.0645 | 0.1759 | False | 2026-10-20T13:42:44Z |
| draftkings|380432190|0QA380432190#2326700052_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1587 | 0.0083 | 0.1504 | False | 2026-10-25T19:10:21Z |
| betmgm|anytd|14371 | betmgm | Jordan Love | anytd | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-20T13:42:44Z |
| betmgm|anytd|19268 | betmgm | Carnell Tate | anytd | over | 0.2277 | 0.1481 | 0.0795 | False | 2026-10-25T19:10:21Z |
| draftkings|380432190|0QA380432190#2331429698_13L88808Q1872485381Q20 | draftkings | Jonah Coleman | 2+ TDs | over | 0.1031 | 0.0278 | 0.0753 | False | 2026-10-25T19:10:21Z |
| draftkings|380432183|0QA380432183#2326700005_13L88808Q1916114112Q20 | draftkings | Elijah Higgins | Anytime TD Scorer | over | 0.1813 | 0.1176 | 0.0636 | False | 2026-10-25T19:10:21Z |
| betmgm|anytd|15875 | betmgm | Dameon Pierce | anytd | over | 0.4182 | 0.3636 | 0.0546 | False | 2026-10-22T13:57:22Z |
