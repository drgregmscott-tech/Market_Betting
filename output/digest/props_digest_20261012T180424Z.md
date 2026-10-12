# Props Pipeline Digest -- 2026-10-12T18:04:24Z

## Run summary
- DraftKings ingestion: 202 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 80 rows (OK)
- Estimation: 282 rows written (from 282 ingested rows) -- status breakdown: {'estimated': 139, 'unsupported_market_first_scorer': 70, 'no_player_match': 37, 'unsupported_stat_type': 26, 'insufficient_history': 10}
- CLV logging: 7 newly flagged, 0 newly closed, 21 still open (966 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|16790 | betmgm | Puka Nacua | recs | over | 1.0 | 0.4554 | 0.5446 | False | 2026-10-07T15:40:15Z |
| draftkings|378203985|0QA378203985#2317707850_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.5075 | 0.0588 | 0.4487 | False | 2026-10-12T06:13:10Z |
| betmgm|recs|17081 | betmgm | Konata Mumpfield | recs | over | 1.0 | 0.6113 | 0.3887 | False | 2026-10-10T06:05:24Z |
| betmgm|recs|17688 | betmgm | Jordan Whittington | recs | over | 1.0 | 0.6334 | 0.3666 | False | 2026-10-12T06:13:10Z |
| draftkings|376384640|0QA376384640#2310618219_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.502 | 0.1818 | 0.3202 | False | 2026-10-11T20:25:56Z |
| draftkings|378203985|0QA378203985#2317707859_13L88808Q1-2108815135Q20 | draftkings | Tory Horton | Anytime TD Scorer | over | 0.4182 | 0.1176 | 0.3006 | False | 2026-10-12T06:13:10Z |
| draftkings|378238663|0QA378238663#2317852746_13L88808Q1491696445Q20 | draftkings | Jaxon Smith-Njigba | 2+ TDs | over | 0.3714 | 0.125 | 0.2464 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707851_13L88808Q11896367839Q20 | draftkings | Jaxon Smith-Njigba | Anytime TD Scorer | over | 0.7261 | 0.4878 | 0.2383 | False | 2026-10-12T06:13:10Z |
| draftkings|378209599|0QA378209599#2317730691_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.564 | 0.3448 | 0.2191 | False | 2026-10-12T18:04:39Z |
| draftkings|378200505|0QA378200505#2317691306_13L88808Q1-849064763Q20 | draftkings | Parker Washington | Anytime TD Scorer | over | 0.5893 | 0.4 | 0.1893 | False | 2026-10-12T18:04:39Z |
| draftkings|378238663|0QA378238663#2317852744_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1587 | 0.0055 | 0.1532 | False | 2026-10-12T06:13:10Z |
| draftkings|378203985|0QA378203985#2317707862_13L88808Q1-644359754Q20 | draftkings | Eric Saubert | Anytime TD Scorer | over | 0.1813 | 0.0476 | 0.1337 | False | 2026-10-12T06:13:10Z |
| draftkings|378230346|0QA378230346#2317819247_13L88808Q1322761913Q20 | draftkings | Garrett Wilson | Anytime TD Scorer | over | 0.4701 | 0.3509 | 0.1192 | False | 2026-10-12T18:04:39Z |
| draftkings|376107223|0QA376107223#2309581305_13L88808Q1-1508640754Q20 | draftkings | Konata Mumpfield | Anytime TD Scorer | over | 0.2296 | 0.1176 | 0.112 | False | 2026-10-11T20:25:56Z |
| draftkings|378211536|0QA378211536#2317738831_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.4647 | 0.3571 | 0.1076 | False | 2026-10-12T18:04:39Z |
| draftkings|378211536|0QA378211536#2317738832_13L88808Q1-1280421193Q20 | draftkings | Denzel Boston | Anytime TD Scorer | over | 0.4373 | 0.3448 | 0.0925 | False | 2026-10-12T18:04:39Z |
| draftkings|378238663|0QA378238663#2317852752_13L88808Q11556454751Q20 | draftkings | Tory Horton | 2+ TDs | over | 0.1031 | 0.0132 | 0.0899 | False | 2026-10-12T06:13:10Z |
| draftkings|378331043|0QA378331043#2318198580_13L88808Q1-719490824Q20 | draftkings | Tetairoa McMillan | Anytime TD Scorer | over | 0.4676 | 0.3922 | 0.0755 | False | 2026-10-12T18:04:39Z |
| draftkings|378193125|0QA378193125#2317660418_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.4373 | 0.3774 | 0.0599 | False | 2026-10-12T18:04:39Z |
| draftkings|376384640|0QA376384640#2310618209_13L88808Q1-166127884Q20 | draftkings | Kyren Williams | 2+ TDs | over | 0.2842 | 0.2326 | 0.0517 | False | 2026-10-11T20:25:56Z |
| draftkings|376107223|0QA376107223#2309581312_13L88808Q11470829306Q20 | draftkings | Dawson Knox | Anytime TD Scorer | over | 0.2084 | 0.1739 | 0.0345 | False | 2026-10-11T20:25:56Z |
