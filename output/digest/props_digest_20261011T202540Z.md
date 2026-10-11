# Props Pipeline Digest -- 2026-10-11T20:25:40Z

## Run summary
- DraftKings ingestion: 254 rows across 6 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 407 rows (OK)
- Estimation: 661 rows written (from 661 ingested rows) -- status breakdown: {'estimated': 281, 'unsupported_market_first_scorer': 176, 'unsupported_stat_type': 134, 'no_player_match': 53, 'insufficient_history': 17}
- CLV logging: 22 newly flagged, 0 newly closed, 33 still open (951 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|16959 | betmgm | Elijah Higgins | recs | over | 1.0 | 0.4248 | 0.5752 | False | 2026-10-11T06:03:14Z |
| betmgm|recs|16849 | betmgm | Marvin Mims | recs | over | 0.9987 | 0.4518 | 0.5469 | False | 2026-10-10T06:05:24Z |
| betmgm|recs|16790 | betmgm | Puka Nacua | recs | over | 1.0 | 0.4554 | 0.5446 | False | 2026-10-07T15:40:15Z |
| betmgm|recs|17719 | betmgm | Troy Franklin | recs | over | 1.0 | 0.5347 | 0.4653 | False | 2026-10-10T06:05:24Z |
| betmgm|recs|17593 | betmgm | Emanuel Wilson | recs | over | 0.9987 | 0.5665 | 0.4322 | False | 2026-10-08T21:26:33Z |
| draftkings|376553393|0QA376553393#2311243931_13L88808Q12077388378Q20 | draftkings | Brian Robinson Jr. | Anytime TD Scorer | over | 0.7008 | 0.2857 | 0.415 | False | 2026-10-11T20:25:56Z |
| betmgm|recs|17081 | betmgm | Konata Mumpfield | recs | over | 1.0 | 0.6113 | 0.3887 | False | 2026-10-10T06:05:24Z |
| betmgm|recs|17728 | betmgm | Devontez Walker | recs | over | 1.0 | 0.6586 | 0.3414 | False | 2026-10-10T06:05:24Z |
| draftkings|376384640|0QA376384640#2310618219_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.502 | 0.1818 | 0.3202 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842105_13L88808Q1-2016866086Q20 | draftkings | Brian Robinson Jr. | 2+ TDs | over | 0.3397 | 0.0435 | 0.2963 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842121_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.4883 | 0.2083 | 0.28 | False | 2026-10-11T20:25:56Z |
| betmgm|anytd|17772 | betmgm | Tory Horton | anytd | over | 0.4182 | 0.1429 | 0.2754 | False | 2026-10-07T15:40:15Z |
| draftkings|376553393|0QA376553393#2311243955_13L88808Q12016884984Q20 | draftkings | Chris Moore | Anytime TD Scorer | over | 0.3198 | 0.0476 | 0.2722 | False | 2026-10-11T20:25:56Z |
| betmgm|anytd|16959 | betmgm | Elijah Higgins | anytd | over | 0.3198 | 0.1 | 0.2198 | False | 2026-10-07T15:40:15Z |
| draftkings|376231113|0QA376231113#2310053553_13L88808Q1916114112Q20 | draftkings | Elijah Higgins | Anytime TD Scorer | over | 0.3198 | 0.1176 | 0.2022 | False | 2026-10-11T20:25:56Z |
| draftkings|376553393|0QA376553393#2311243949_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.276 | 0.1053 | 0.1707 | False | 2026-10-11T20:25:56Z |
| draftkings|376553393|0QA376553393#2311243942_13L88808Q12018204784Q20 | draftkings | Zay Flowers | Anytime TD Scorer | over | 0.4919 | 0.3333 | 0.1586 | False | 2026-10-11T20:25:56Z |
| draftkings|376553393|0QA376553393#2311243937_13L88808Q1-189550648Q20 | draftkings | Austin Hooper | Anytime TD Scorer | over | 0.276 | 0.1176 | 0.1583 | False | 2026-10-11T20:25:56Z |
| draftkings|376107223|0QA376107223#2309581305_13L88808Q1-1508640754Q20 | draftkings | Konata Mumpfield | Anytime TD Scorer | over | 0.2296 | 0.1176 | 0.112 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842103_13L88808Q1-1354855512Q20 | draftkings | Bijan Robinson | 2+ TDs | over | 0.3881 | 0.2817 | 0.1064 | False | 2026-10-11T20:25:56Z |
| draftkings|376767865|0QA376767865#2312042386_13L88808Q176672589Q20 | draftkings | Amon-Ra St. Brown | 2+ TDs | over | 0.3042 | 0.2 | 0.1042 | False | 2026-10-11T20:25:56Z |
| betmgm|anytd|15850 | betmgm | Jahan Dotson | anytd | over | 0.2704 | 0.1667 | 0.1037 | False | 2026-10-07T15:40:15Z |
| draftkings|376553393|0QA376553393#2311243932_13L88808Q1-419764349Q20 | draftkings | Jahan Dotson | Anytime TD Scorer | over | 0.2704 | 0.1667 | 0.1037 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842122_13L88808Q1-1364480320Q20 | draftkings | Zay Flowers | 2+ TDs | over | 0.1479 | 0.0588 | 0.0891 | False | 2026-10-11T20:25:56Z |
| draftkings|376231113|0QA376231113#2310053189_13L88808Q11698530898Q20 | draftkings | Jacoby Brissett | Anytime TD Scorer | over | 0.2296 | 0.1429 | 0.0868 | False | 2026-10-11T20:25:56Z |
| draftkings|376767865|0QA376767865#2312042385_13L88808Q11455054237Q20 | draftkings | Jahmyr Gibbs | 2+ TDs | over | 0.5105 | 0.4444 | 0.066 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842134_13L88808Q1-621793542Q20 | draftkings | Chris Moore | 2+ TDs | over | 0.0577 | 0.005 | 0.0527 | False | 2026-10-11T20:25:56Z |
| draftkings|376384640|0QA376384640#2310618209_13L88808Q1-166127884Q20 | draftkings | Kyren Williams | 2+ TDs | over | 0.2842 | 0.2326 | 0.0517 | False | 2026-10-11T20:25:56Z |
| draftkings|376767865|0QA376767865#2312042339_13L88808Q1-1155015523Q20 | draftkings | Elijah Higgins | 2+ TDs | over | 0.0577 | 0.011 | 0.0467 | False | 2026-10-11T20:25:56Z |
| draftkings|376107223|0QA376107223#2309581312_13L88808Q11470829306Q20 | draftkings | Dawson Knox | Anytime TD Scorer | over | 0.2084 | 0.1739 | 0.0345 | False | 2026-10-11T20:25:56Z |
| draftkings|376714382|0QA376714382#2311842130_13L88808Q1-1618269213Q20 | draftkings | Matthew Hibner | 2+ TDs | over | 0.0422 | 0.0083 | 0.0339 | False | 2026-10-11T20:25:56Z |
| betmgm|anytd|16560 | betmgm | Rashid Shaheed | anytd | over | 0.2704 | 0.2381 | 0.0323 | False | 2026-10-08T06:21:26Z |
| draftkings|376714382|0QA376714382#2311842109_13L88808Q1-2106790228Q20 | draftkings | Austin Hooper | 2+ TDs | over | 0.0422 | 0.0099 | 0.0323 | False | 2026-10-11T20:25:56Z |
