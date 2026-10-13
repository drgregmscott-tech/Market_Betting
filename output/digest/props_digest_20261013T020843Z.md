# Props Pipeline Digest -- 2026-10-13T02:08:43Z

## Run summary
- DraftKings ingestion: 142 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 70 rows (OK)
- Estimation: 212 rows written (from 212 ingested rows) -- status breakdown: {'estimated': 121, 'unsupported_stat_type': 30, 'no_player_match': 29, 'unsupported_market_first_scorer': 25, 'insufficient_history': 7}
- CLV logging: 13 newly flagged, 0 newly closed, 30 still open (979 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|13587 | betmgm | Ty Johnson | recs | over | 1.0 | 0.396 | 0.604 | False | 2026-10-13T02:09:00Z |
| betmgm|recs|16790 | betmgm | Puka Nacua | recs | over | 1.0 | 0.4554 | 0.5446 | False | 2026-10-07T15:40:15Z |
| betmgm|recs|10854 | betmgm | Tyler Higbee | recs | over | 1.0 | 0.4929 | 0.5071 | False | 2026-10-13T02:09:00Z |
| betmgm|recs|17690 | betmgm | Blake Corum | recs | over | 1.0 | 0.5446 | 0.4554 | False | 2026-10-13T02:09:00Z |
| draftkings|378203985|0QA378203985#2317707850_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.5075 | 0.0588 | 0.4487 | False | 2026-10-12T06:13:10Z |
| betmgm|recs|17030 | betmgm | Davis Allen | recs | over | 1.0 | 0.5835 | 0.4165 | False | 2026-10-13T02:09:00Z |
| betmgm|recs|17081 | betmgm | Konata Mumpfield | recs | over | 1.0 | 0.6113 | 0.3887 | False | 2026-10-10T06:05:24Z |
| betmgm|recs|17688 | betmgm | Jordan Whittington | recs | over | 1.0 | 0.6334 | 0.3666 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707859_13L88808Q1-2108815135Q20 | draftkings | Tory Horton | Anytime TD Scorer | over | 0.4182 | 0.1176 | 0.3006 | False | 2026-10-12T06:13:10Z |
| draftkings|378238663|0QA378238663#2317852746_13L88808Q1491696445Q20 | draftkings | Jaxon Smith-Njigba | 2+ TDs | over | 0.3714 | 0.125 | 0.2464 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707851_13L88808Q11896367839Q20 | draftkings | Jaxon Smith-Njigba | Anytime TD Scorer | over | 0.7261 | 0.4878 | 0.2383 | False | 2026-10-12T06:13:10Z |
| draftkings|378200505|0QA378200505#2317691321_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.6084 | 0.3774 | 0.231 | False | 2026-10-13T02:09:00Z |
| draftkings|378209599|0QA378209599#2317730691_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.564 | 0.3448 | 0.2191 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691306_13L88808Q1-849064763Q20 | draftkings | Parker Washington | Anytime TD Scorer | over | 0.5893 | 0.4 | 0.1893 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691317_13L88808Q11380693923Q20 | draftkings | Josh Cameron | Anytime TD Scorer | over | 0.2882 | 0.125 | 0.1632 | False | 2026-10-13T02:09:00Z |
| draftkings|378238663|0QA378238663#2317852744_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1587 | 0.0055 | 0.1532 | False | 2026-10-12T06:13:10Z |
| draftkings|378200505|0QA378200505#2317691327_13L88808Q1242387080Q20 | draftkings | C.J. Stroud | Anytime TD Scorer | over | 0.2404 | 0.0909 | 0.1495 | False | 2026-10-13T02:09:00Z |
| draftkings|378200505|0QA378200505#2317691325_13L88808Q1-2078311456Q20 | draftkings | Jaylin Noel | Anytime TD Scorer | over | 0.2404 | 0.0952 | 0.1452 | False | 2026-10-13T02:09:00Z |
| draftkings|378203985|0QA378203985#2317707862_13L88808Q1-644359754Q20 | draftkings | Eric Saubert | Anytime TD Scorer | over | 0.1813 | 0.0476 | 0.1337 | False | 2026-10-12T06:13:10Z |
| draftkings|378230346|0QA378230346#2317819247_13L88808Q1322761913Q20 | draftkings | Garrett Wilson | Anytime TD Scorer | over | 0.4701 | 0.3509 | 0.1192 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691308_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.3462 | 0.2273 | 0.119 | False | 2026-10-13T02:09:00Z |
| draftkings|378200505|0QA378200505#2317691328_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.1813 | 0.0667 | 0.1146 | False | 2026-10-13T02:09:00Z |
| draftkings|378211536|0QA378211536#2317738831_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.4647 | 0.3571 | 0.1076 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2318845024_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.2704 | 0.1739 | 0.0965 | False | 2026-10-13T02:09:00Z |
| draftkings|378211536|0QA378211536#2317738832_13L88808Q1-1280421193Q20 | draftkings | Denzel Boston | Anytime TD Scorer | over | 0.4373 | 0.3448 | 0.0925 | False | 2026-10-12T18:04:39Z |
| draftkings|378238663|0QA378238663#2317852752_13L88808Q11556454751Q20 | draftkings | Tory Horton | 2+ TDs | over | 0.1031 | 0.0132 | 0.0899 | False | 2026-10-12T06:13:10Z |
| draftkings|378331043|0QA378331043#2318198580_13L88808Q1-719490824Q20 | draftkings | Tetairoa McMillan | Anytime TD Scorer | over | 0.4676 | 0.3922 | 0.0755 | False | 2026-10-12T18:04:39Z |
| draftkings|378193125|0QA378193125#2317660418_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.4373 | 0.3774 | 0.0599 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691307_13L88808Q1-992648746Q20 | draftkings | Jakobi Meyers | Anytime TD Scorer | over | 0.2882 | 0.2326 | 0.0557 | False | 2026-10-13T02:09:00Z |
| draftkings|378200505|0QA378200505#2317691310_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.2015 | 0.1538 | 0.0476 | False | 2026-10-13T02:09:00Z |
