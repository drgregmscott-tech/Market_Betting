# Props Pipeline Digest -- 2026-10-15T13:34:58Z

## Run summary
- DraftKings ingestion: 635 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 827 rows (OK)
- Estimation: 1462 rows written (from 1462 ingested rows) -- status breakdown: {'estimated': 704, 'unsupported_market_first_scorer': 379, 'unsupported_stat_type': 231, 'no_player_match': 112, 'insufficient_history': 35, 'no_line_value': 1}
- CLV logging: 2 newly flagged, 0 newly closed, 40 still open (1051 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|19319 | betmgm | Bryce Lance | recs | over | 0.9946 | 0.4425 | 0.5521 | False | 2026-10-15T13:35:16Z |
| betmgm|recs|17185 | betmgm | Jalen Brooks | recs | over | 0.998 | 0.509 | 0.489 | False | 2026-10-14T23:21:18Z |
| betmgm|recs|17772 | betmgm | Tory Horton | recs | over | 1.0 | 0.5446 | 0.4554 | False | 2026-10-15T13:35:16Z |
| betmgm|recs|19448 | betmgm | Nate Boerkircher | recs | over | 1.0 | 0.5941 | 0.4059 | False | 2026-10-13T19:24:28Z |
| draftkings|378209959|0QA378209959#2317732126_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.5995 | 0.2381 | 0.3614 | False | 2026-10-14T23:21:18Z |
| draftkings|378230346|0QA378230346#2317819254_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.3198 | 0.0769 | 0.2429 | False | 2026-10-14T23:21:18Z |
| draftkings|378209959|0QA378209959#2317732133_13L88808Q1292660006Q20 | draftkings | Ben Skowronek | Anytime TD Scorer | over | 0.276 | 0.05 | 0.226 | False | 2026-10-14T23:21:18Z |
| draftkings|378209959|0QA378209959#2317732115_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.3677 | 0.1538 | 0.2138 | False | 2026-10-14T23:21:18Z |
| draftkings|378211536|0QA378211536#2317738840_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.276 | 0.0625 | 0.2135 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427543_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.233 | 0.0278 | 0.2052 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016674_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.3534 | 0.1538 | 0.1996 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198581_13L88808Q1-537154100Q20 | draftkings | Jalen Coker | Anytime TD Scorer | over | 0.442 | 0.2439 | 0.1981 | False | 2026-10-14T23:21:18Z |
| draftkings|378211536|0QA378211536#2317738851_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.276 | 0.0833 | 0.1926 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198587_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.276 | 0.1 | 0.176 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198568_13L88808Q1-1879851941Q20 | draftkings | Dallas Goedert | Anytime TD Scorer | over | 0.442 | 0.2667 | 0.1753 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|16751 | betmgm | DeMario Douglas | anytd | over | 0.4231 | 0.2632 | 0.1599 | False | 2026-10-14T20:17:30Z |
| draftkings|379077723|0QA379077723#2321017251_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.4355 | 0.2778 | 0.1577 | False | 2026-10-14T23:21:18Z |
| draftkings|378331043|0QA378331043#2318198585_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.3734 | 0.2222 | 0.1511 | False | 2026-10-14T23:21:18Z |
| draftkings|378211536|0QA378211536#2317738849_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2704 | 0.125 | 0.1454 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|379077723|0QA379077723#2321017243_13L88808Q1-862670716Q20 | draftkings | Harold Fannin Jr. | 2+ TDs | over | 0.1302 | 0.0435 | 0.0867 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016676_13L88808Q1131228805Q20 | draftkings | Jalen Coker | 2+ TDs | over | 0.1164 | 0.0323 | 0.0842 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427527_13L88808Q1-416383636Q20 | draftkings | Bucky Irving | 2+ TDs | over | 0.1523 | 0.0714 | 0.0809 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016798_13L88808Q1-1781882123Q20 | draftkings | Dallas Goedert | 2+ TDs | over | 0.1164 | 0.0385 | 0.078 | False | 2026-10-14T23:21:18Z |
| draftkings|378209959|0QA378209959#2317732116_13L88808Q12127282699Q20 | draftkings | Ted Hurst | Anytime TD Scorer | over | 0.2296 | 0.1538 | 0.0758 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016675_13L88808Q11934492119Q20 | draftkings | Tetairoa McMillan | 2+ TDs | over | 0.132 | 0.0588 | 0.0732 | False | 2026-10-14T23:21:18Z |
| draftkings|378930895|0QA378930895#2320520988_13L88808Q180415155Q20 | draftkings | Garrett Wilson | 2+ TDs | over | 0.1336 | 0.0667 | 0.0669 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427533_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.0778 | 0.0141 | 0.0638 | False | 2026-10-14T23:21:18Z |
| draftkings|378930895|0QA378930895#2320520979_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.1057 | 0.0435 | 0.0622 | False | 2026-10-14T23:21:18Z |
| draftkings|378230346|0QA378230346#2317819251_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.2015 | 0.1429 | 0.0586 | False | 2026-10-14T23:21:18Z |
| draftkings|379077723|0QA379077723#2321017242_13L88808Q1-540137833Q20 | draftkings | Denzel Boston | 2+ TDs | over | 0.1137 | 0.0556 | 0.0582 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016677_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.0805 | 0.0278 | 0.0527 | False | 2026-10-14T23:21:18Z |
| draftkings|378930895|0QA378930895#2320520996_13L88808Q1-1516021202Q20 | draftkings | Jeremy Ruckert | 2+ TDs | over | 0.0577 | 0.0071 | 0.0506 | False | 2026-10-14T23:21:18Z |
| betmgm|anytd|19126 | betmgm | Kyle Williams | anytd | over | 0.2404 | 0.2 | 0.0404 | False | 2026-10-14T20:17:30Z |
| betmgm|anytd|17593 | betmgm | Emanuel Wilson | anytd | over | 0.5157 | 0.4762 | 0.0395 | False | 2026-10-13T11:58:47Z |
| draftkings|379077723|0QA379077723#2321017247_13L88808Q1600398218Q20 | draftkings | Blake Whiteheart | 2+ TDs | over | 0.0422 | 0.0052 | 0.0369 | False | 2026-10-14T23:21:18Z |
| draftkings|379187821|0QA379187821#2321427528_13L88808Q11465714566Q20 | draftkings | Emeka Egbuka | 2+ TDs | over | 0.0712 | 0.0345 | 0.0367 | False | 2026-10-14T23:21:18Z |
| draftkings|379077723|0QA379077723#2321017258_13L88808Q1-1618269213Q20 | draftkings | Matthew Hibner | 2+ TDs | over | 0.0422 | 0.0076 | 0.0345 | False | 2026-10-14T23:21:18Z |
| draftkings|379077545|0QA379077545#2321016681_13L88808Q1-1228251151Q20 | draftkings | John Metchie III | 2+ TDs | over | 0.0422 | 0.0083 | 0.0339 | False | 2026-10-14T23:21:18Z |
| draftkings|378869520|0QA378869520#2320229132_13L88808Q11041398384Q20 | draftkings | Tyler Warren | 2+ TDs | over | 0.1137 | 0.0833 | 0.0304 | False | 2026-10-14T23:21:18Z |
