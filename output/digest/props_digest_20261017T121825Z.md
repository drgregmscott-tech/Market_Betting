# Props Pipeline Digest -- 2026-10-17T12:18:25Z

## Run summary
- DraftKings ingestion: 678 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 974 rows (OK)
- Estimation: 1652 rows written (from 1652 ingested rows) -- status breakdown: {'estimated': 728, 'unsupported_market_first_scorer': 425, 'unsupported_stat_type': 327, 'no_player_match': 127, 'insufficient_history': 43, 'no_line_value': 2}
- CLV logging: 0 newly flagged, 0 newly closed, 51 still open (1075 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|18550 | betmgm | Jalen Royals | recs | over | 0.9975 | 0.3887 | 0.6087 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|19262 | betmgm | Zachariah Branch | recs | over | 1.0 | 0.4335 | 0.5665 | False | 2026-10-15T19:58:24Z |
| betmgm|recs|16810 | betmgm | Keaton Mitchell | recs | over | 1.0 | 0.4518 | 0.5482 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|17821 | betmgm | Kimani Vidal | recs | over | 1.0 | 0.4554 | 0.5446 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|14657 | betmgm | Rico Dowdle | recs | over | 1.0 | 0.4797 | 0.5203 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|17185 | betmgm | Jalen Brooks | recs | over | 0.998 | 0.509 | 0.489 | False | 2026-10-14T23:21:18Z |
| betmgm|recs|19448 | betmgm | Nate Boerkircher | recs | over | 1.0 | 0.5941 | 0.4059 | False | 2026-10-13T19:24:28Z |
| draftkings|378331043|0QA378331043#2318198575_13L88808Q11627968604Q20 | draftkings | Darius Cooper | Anytime TD Scorer | over | 0.5873 | 0.2 | 0.3873 | False | 2026-10-16T04:45:58Z |
| betmgm|anytd|18251 | betmgm | Hayden Rucci | anytd | over | 0.4182 | 0.0345 | 0.3837 | False | 2026-10-15T23:09:30Z |
| draftkings|378209959|0QA378209959#2317732126_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.5995 | 0.2381 | 0.3614 | False | 2026-10-14T23:21:18Z |
| draftkings|378209599|0QA378209599#2321453607_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.3677 | 0.1176 | 0.25 | False | 2026-10-16T04:45:58Z |
| draftkings|378230346|0QA378230346#2317819254_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.3198 | 0.0769 | 0.2429 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|14563 | betmgm | Tyler Huntley | anytd | over | 0.4182 | 0.1905 | 0.2277 | False | 2026-10-16T19:38:27Z |
| draftkings|378211536|0QA378211536#2317738840_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.276 | 0.0625 | 0.2135 | False | 2026-10-14T23:21:18Z |
| draftkings|378211536|0QA378211536#2323467131_13L88808Q11550625606Q20 | draftkings | Tyler Huntley | Anytime TD Scorer | over | 0.4182 | 0.2083 | 0.2099 | False | 2026-10-16T19:38:27Z |
| draftkings|379187821|0QA379187821#2321427543_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.233 | 0.0278 | 0.2052 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016804_13L88808Q1-477962024Q20 | draftkings | Darius Cooper | 2+ TDs | over | 0.222 | 0.0217 | 0.2003 | False | 2026-10-16T04:45:58Z |
| draftkings|379077545|0QA379077545#2321016674_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.3534 | 0.1538 | 0.1996 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198581_13L88808Q1-537154100Q20 | draftkings | Jalen Coker | Anytime TD Scorer | over | 0.442 | 0.2439 | 0.1981 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198587_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.276 | 0.1 | 0.176 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|16751 | betmgm | DeMario Douglas | anytd | over | 0.4231 | 0.2632 | 0.1599 | False | 2026-10-14T20:17:30Z |
| draftkings|379077723|0QA379077723#2321017251_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.4355 | 0.2778 | 0.1577 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198585_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.3734 | 0.2222 | 0.1511 | False | 2026-10-14T23:21:18Z |
| draftkings|378211536|0QA378211536#2317738849_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2704 | 0.125 | 0.1454 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|378209599|0QA378209599#2317730702_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.4065 | 0.2985 | 0.108 | False | 2026-10-16T04:45:58Z |
| draftkings|379077723|0QA379077723#2321017243_13L88808Q1-862670716Q20 | draftkings | Harold Fannin Jr. | 2+ TDs | over | 0.1302 | 0.0435 | 0.0867 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016676_13L88808Q1131228805Q20 | draftkings | Jalen Coker | 2+ TDs | over | 0.1164 | 0.0323 | 0.0842 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427527_13L88808Q1-416383636Q20 | draftkings | Bucky Irving | 2+ TDs | over | 0.1523 | 0.0714 | 0.0809 | False | 2026-10-14T23:21:18Z |
| draftkings|378230346|0QA378230346#2317819255_13L88808Q1-216139177Q20 | draftkings | Kenyon Sadiq | Anytime TD Scorer | over | 0.2882 | 0.2083 | 0.0799 | False | 2026-10-16T19:38:27Z |
| draftkings|378209959|0QA378209959#2317732116_13L88808Q12127282699Q20 | draftkings | Ted Hurst | Anytime TD Scorer | over | 0.2296 | 0.1538 | 0.0758 | False | 2026-10-14T23:21:18Z |
| draftkings|379077723|0QA379077723#2323466956_13L88808Q1-1742943144Q20 | draftkings | Tyler Huntley | 2+ TDs | over | 0.1031 | 0.0278 | 0.0753 | False | 2026-10-16T19:38:27Z |
| draftkings|379077545|0QA379077545#2321016675_13L88808Q11934492119Q20 | draftkings | Tetairoa McMillan | 2+ TDs | over | 0.132 | 0.0588 | 0.0732 | False | 2026-10-14T23:21:18Z |
| draftkings|378811055|0QA378811055#2321453606_13L88808Q11581906537Q20 | draftkings | Devin Singletary | 2+ TDs | over | 0.0778 | 0.011 | 0.0669 | False | 2026-10-16T04:45:58Z |
| draftkings|378930895|0QA378930895#2320520988_13L88808Q180415155Q20 | draftkings | Garrett Wilson | 2+ TDs | over | 0.1336 | 0.0667 | 0.0669 | False | 2026-10-14T23:21:18Z |
| draftkings|378930895|0QA378930895#2320520979_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.1057 | 0.0435 | 0.0622 | False | 2026-10-14T23:21:18Z |
| draftkings|378230346|0QA378230346#2317819251_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.2015 | 0.1429 | 0.0586 | False | 2026-10-14T23:21:18Z |
| draftkings|379077723|0QA379077723#2321017242_13L88808Q1-540137833Q20 | draftkings | Denzel Boston | 2+ TDs | over | 0.1137 | 0.0556 | 0.0582 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016677_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.0805 | 0.0278 | 0.0527 | False | 2026-10-14T23:21:18Z |
| draftkings|378930895|0QA378930895#2320520996_13L88808Q1-1516021202Q20 | draftkings | Jeremy Ruckert | 2+ TDs | over | 0.0577 | 0.0071 | 0.0506 | False | 2026-10-14T23:21:18Z |
| draftkings|378811055|0QA378811055#2320016521_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.0969 | 0.0476 | 0.0492 | False | 2026-10-16T04:45:58Z |
| betmgm|anytd|19126 | betmgm | Kyle Williams | anytd | over | 0.2404 | 0.2 | 0.0404 | False | 2026-10-14T20:17:30Z |
| draftkings|379077723|0QA379077723#2321017247_13L88808Q1600398218Q20 | draftkings | Blake Whiteheart | 2+ TDs | over | 0.0422 | 0.0052 | 0.0369 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427528_13L88808Q11465714566Q20 | draftkings | Emeka Egbuka | 2+ TDs | over | 0.0712 | 0.0345 | 0.0367 | False | 2026-10-14T23:21:18Z |
| draftkings|378209599|0QA378209599#2317730689_13L88808Q1-1380864812Q20 | draftkings | Malik Nabers | Anytime TD Scorer | over | 0.3935 | 0.3571 | 0.0363 | False | 2026-10-16T04:45:58Z |
| draftkings|378211536|0QA378211536#2317738846_13L88808Q12018204784Q20 | draftkings | Zay Flowers | Anytime TD Scorer | over | 0.3631 | 0.3279 | 0.0352 | False | 2026-10-16T22:56:18Z |
| draftkings|379077545|0QA379077545#2321016681_13L88808Q1-1228251151Q20 | draftkings | John Metchie III | 2+ TDs | over | 0.0422 | 0.0083 | 0.0339 | False | 2026-10-14T23:21:18Z |
| draftkings|378209599|0QA378209599#2317730704_13L88808Q1-403572542Q20 | draftkings | Kendre Miller | Anytime TD Scorer | over | 0.3968 | 0.3636 | 0.0331 | False | 2026-10-16T04:45:58Z |
| draftkings|379077723|0QA379077723#2321017257_13L88808Q1-464941358Q20 | draftkings | Devontez Walker | 2+ TDs | over | 0.0404 | 0.0099 | 0.0305 | False | 2026-10-15T19:58:24Z |
| draftkings|378869520|0QA378869520#2320229132_13L88808Q11041398384Q20 | draftkings | Tyler Warren | 2+ TDs | over | 0.1137 | 0.0833 | 0.0304 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198584_13L88808Q11112660000Q20 | draftkings | Bryce Young | Anytime TD Scorer | over | 0.1732 | 0.1429 | 0.0304 | False | 2026-10-15T19:58:24Z |
