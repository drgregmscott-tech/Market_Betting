# Props Pipeline Digest -- 2026-10-18T18:44:36Z

## Run summary
- DraftKings ingestion: 94 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 730 rows (OK)
- Estimation: 824 rows written (from 824 ingested rows) -- status breakdown: {'estimated': 329, 'unsupported_stat_type': 267, 'unsupported_market_first_scorer': 163, 'no_player_match': 47, 'insufficient_history': 17, 'no_line_value': 1}
- CLV logging: 9 newly flagged, 0 newly closed, 19 still open (1088 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|18550 | betmgm | Jalen Royals | recs | over | 0.9975 | 0.3887 | 0.6087 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|16810 | betmgm | Keaton Mitchell | recs | over | 1.0 | 0.4518 | 0.5482 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|17821 | betmgm | Kimani Vidal | recs | over | 1.0 | 0.4554 | 0.5446 | False | 2026-10-17T04:43:27Z |
| betmgm|recs|15976 | betmgm | Tyler Allgeier | recs | over | 1.0 | 0.4797 | 0.5203 | False | 2026-10-18T12:42:13Z |
| betmgm|recs|17185 | betmgm | Jalen Brooks | recs | over | 0.998 | 0.509 | 0.489 | False | 2026-10-14T23:21:18Z |
| betmgm|recs|16042 | betmgm | Chig Okonkwo | recs | over | 1.0 | 0.5835 | 0.4165 | False | 2026-10-17T18:37:50Z |
| betmgm|anytd|18251 | betmgm | Hayden Rucci | anytd | over | 0.4182 | 0.0345 | 0.3837 | False | 2026-10-15T23:09:30Z |
| betmgm|anytd|14563 | betmgm | Tyler Huntley | anytd | over | 0.4182 | 0.1905 | 0.2277 | False | 2026-10-16T19:38:27Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|378229561|0QA378229561#2317816408_13L88808Q1-1508640754Q20 | draftkings | Konata Mumpfield | Anytime TD Scorer | over | 0.2296 | 0.1 | 0.1296 | False | 2026-10-18T18:44:52Z |
| draftkings|378229561|0QA378229561#2317816421_13L88808Q1916114112Q20 | draftkings | Elijah Higgins | Anytime TD Scorer | over | 0.2296 | 0.1111 | 0.1185 | False | 2026-10-18T18:44:52Z |
| betmgm|anytd|10735 | betmgm | Hunter Henry | anytd | over | 0.2404 | 0.125 | 0.1154 | False | 2026-10-18T18:44:52Z |
| betmgm|anytd|17673 | betmgm | Drake Maye | anytd | over | 0.2404 | 0.1333 | 0.1071 | False | 2026-10-18T18:44:52Z |
| draftkings|378229561|0QA378229561#2317816420_13L88808Q11698530898Q20 | draftkings | Jacoby Brissett | Anytime TD Scorer | over | 0.1813 | 0.1111 | 0.0702 | False | 2026-10-18T18:44:52Z |
| betmgm|anytd|15372 | betmgm | Rhamondre Stevenson | anytd | over | 0.3935 | 0.3333 | 0.0601 | False | 2026-10-18T18:44:52Z |
| draftkings|378229561|0QA378229561#2317816416_13L88808Q11587306986Q20 | draftkings | Trey McBride | Anytime TD Scorer | over | 0.4373 | 0.3846 | 0.0527 | False | 2026-10-18T18:44:52Z |
| draftkings|378879408|0QA378879408#2320265526_13L88808Q1273996050Q20 | draftkings | Davante Adams | 2+ TDs | over | 0.2166 | 0.1739 | 0.0426 | False | 2026-10-18T18:44:52Z |
| betmgm|anytd|19126 | betmgm | Kyle Williams | anytd | over | 0.2404 | 0.2 | 0.0404 | False | 2026-10-14T20:17:30Z |
| draftkings|378879408|0QA378879408#2320265653_13L88808Q1-793431613Q20 | draftkings | Trey McBride | 2+ TDs | over | 0.1137 | 0.0769 | 0.0368 | False | 2026-10-18T18:44:52Z |
