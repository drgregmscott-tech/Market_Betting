# Props Pipeline Digest -- 2026-10-13T11:58:33Z

## Run summary
- DraftKings ingestion: 206 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 106 rows (OK)
- Estimation: 312 rows written (from 312 ingested rows) -- status breakdown: {'estimated': 189, 'unsupported_market_first_scorer': 49, 'no_player_match': 36, 'unsupported_stat_type': 29, 'insufficient_history': 9}
- CLV logging: 10 newly flagged, 0 newly closed, 33 still open (989 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|378203985|0QA378203985#2317707850_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.5075 | 0.0588 | 0.4487 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707859_13L88808Q1-2108815135Q20 | draftkings | Tory Horton | Anytime TD Scorer | over | 0.4182 | 0.1176 | 0.3006 | False | 2026-10-12T06:13:10Z |
| draftkings|378238663|0QA378238663#2317852746_13L88808Q1491696445Q20 | draftkings | Jaxon Smith-Njigba | 2+ TDs | over | 0.3714 | 0.125 | 0.2464 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707851_13L88808Q11896367839Q20 | draftkings | Jaxon Smith-Njigba | Anytime TD Scorer | over | 0.7261 | 0.4878 | 0.2383 | False | 2026-10-12T06:13:10Z |
| draftkings|378200505|0QA378200505#2317691321_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.6084 | 0.3774 | 0.231 | False | 2026-10-13T02:09:00Z |
| draftkings|378209599|0QA378209599#2317730691_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.564 | 0.3448 | 0.2191 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691306_13L88808Q1-849064763Q20 | draftkings | Parker Washington | Anytime TD Scorer | over | 0.5893 | 0.4 | 0.1893 | False | 2026-10-12T18:04:39Z |
| draftkings|378561764|0QA378561764#2319060864_13L88808Q1-721675132Q20 | draftkings | Nico Collins | 2+ TDs | over | 0.2413 | 0.0714 | 0.1698 | False | 2026-10-13T11:58:47Z |
| draftkings|378200505|0QA378200505#2317691317_13L88808Q11380693923Q20 | draftkings | Josh Cameron | Anytime TD Scorer | over | 0.2882 | 0.125 | 0.1632 | False | 2026-10-13T02:09:00Z |
| draftkings|378561764|0QA378561764#2319060849_13L88808Q1954782757Q20 | draftkings | Parker Washington | 2+ TDs | over | 0.2239 | 0.0625 | 0.1614 | False | 2026-10-13T11:58:47Z |
| draftkings|378238663|0QA378238663#2317852744_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1587 | 0.0055 | 0.1532 | False | 2026-10-12T06:13:10Z |
| draftkings|378200505|0QA378200505#2317691327_13L88808Q1242387080Q20 | draftkings | C.J. Stroud | Anytime TD Scorer | over | 0.2404 | 0.0909 | 0.1495 | False | 2026-10-13T02:09:00Z |
| draftkings|378200505|0QA378200505#2317691325_13L88808Q1-2078311456Q20 | draftkings | Jaylin Noel | Anytime TD Scorer | over | 0.2404 | 0.0952 | 0.1452 | False | 2026-10-13T02:09:00Z |
| draftkings|378203985|0QA378203985#2317707862_13L88808Q1-644359754Q20 | draftkings | Eric Saubert | Anytime TD Scorer | over | 0.1813 | 0.0476 | 0.1337 | False | 2026-10-12T06:13:10Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|378230346|0QA378230346#2317819247_13L88808Q1322761913Q20 | draftkings | Garrett Wilson | Anytime TD Scorer | over | 0.4701 | 0.3509 | 0.1192 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691308_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.3462 | 0.2273 | 0.119 | False | 2026-10-13T02:09:00Z |
| draftkings|378200505|0QA378200505#2317691328_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.1813 | 0.0667 | 0.1146 | False | 2026-10-13T02:09:00Z |
| draftkings|378209959|0QA378209959#2317732110_13L88808Q1666446492Q20 | draftkings | Bucky Irving | Anytime TD Scorer | over | 0.4984 | 0.3846 | 0.1138 | False | 2026-10-13T11:58:47Z |
| draftkings|378211536|0QA378211536#2317738831_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.4647 | 0.3571 | 0.1076 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2318845024_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.2704 | 0.1739 | 0.0965 | False | 2026-10-13T02:09:00Z |
| draftkings|378211536|0QA378211536#2317738832_13L88808Q1-1280421193Q20 | draftkings | Denzel Boston | Anytime TD Scorer | over | 0.4373 | 0.3448 | 0.0925 | False | 2026-10-12T18:04:39Z |
| draftkings|378238663|0QA378238663#2317852752_13L88808Q11556454751Q20 | draftkings | Tory Horton | 2+ TDs | over | 0.1031 | 0.0132 | 0.0899 | False | 2026-10-12T06:13:10Z |
| draftkings|378331043|0QA378331043#2318198580_13L88808Q1-719490824Q20 | draftkings | Tetairoa McMillan | Anytime TD Scorer | over | 0.4676 | 0.3922 | 0.0755 | False | 2026-10-12T18:04:39Z |
| draftkings|378193125|0QA378193125#2317660418_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.4373 | 0.3774 | 0.0599 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691307_13L88808Q1-992648746Q20 | draftkings | Jakobi Meyers | Anytime TD Scorer | over | 0.2882 | 0.2326 | 0.0557 | False | 2026-10-13T02:09:00Z |
| draftkings|378209959|0QA378209959#2317732111_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.3527 | 0.303 | 0.0497 | False | 2026-10-13T11:58:47Z |
| draftkings|378200505|0QA378200505#2317691310_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.2015 | 0.1538 | 0.0476 | False | 2026-10-13T02:09:00Z |
| draftkings|378561764|0QA378561764#2319060850_13L88808Q1-1327690156Q20 | draftkings | Chris Rodriguez Jr. | 2+ TDs | over | 0.0684 | 0.0278 | 0.0406 | False | 2026-10-13T11:58:47Z |
| betmgm|anytd|17593 | betmgm | Emanuel Wilson | anytd | over | 0.5157 | 0.4762 | 0.0395 | False | 2026-10-13T11:58:47Z |
| draftkings|378203985|0QA378203985#2317707852_13L88808Q11707072676Q20 | draftkings | Emanuel Wilson | Anytime TD Scorer | over | 0.5157 | 0.4762 | 0.0395 | False | 2026-10-13T11:58:47Z |
| draftkings|378561764|0QA378561764#2319060855_13L88808Q1-1585722573Q20 | draftkings | Josh Cameron | 2+ TDs | over | 0.0462 | 0.0123 | 0.0339 | False | 2026-10-13T11:58:47Z |
| draftkings|378238663|0QA378238663#2317852724_13L88808Q1-1357951342Q20 | draftkings | Emanuel Wilson | 2+ TDs | over | 0.1645 | 0.1333 | 0.0312 | False | 2026-10-13T11:58:47Z |
