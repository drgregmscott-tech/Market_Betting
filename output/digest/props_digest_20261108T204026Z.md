# Props Pipeline Digest -- 2026-11-08T20:40:26Z

## Run summary
- DraftKings ingestion: 85 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 711 rows (OK)
- Estimation: 796 rows written (from 796 ingested rows) -- status breakdown: {'estimated': 355, 'unsupported_stat_type': 222, 'unsupported_market_first_scorer': 167, 'no_player_match': 29, 'insufficient_history': 23}
- CLV logging: 10 newly flagged, 0 newly closed, 15 still open (1462 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|19445 | betmgm | Reggie Virgil | recs | over | 0.9912 | 0.4425 | 0.5487 | False | 2026-11-07T06:17:27Z |
| betmgm|recs|13582 | betmgm | Josh Jacobs | recs | over | 1.0 | 0.5071 | 0.4929 | False | 2026-11-04T19:58:29Z |
| betmgm|recs|18536 | betmgm | Ben Yurosek | recs | over | 1.0 | 0.5575 | 0.4425 | False | 2026-11-07T23:45:48Z |
| draftkings|385058260|0QA385058260#2346380044_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.4831 | 0.1667 | 0.3165 | False | 2026-11-08T20:40:41Z |
| draftkings|385058260|0QA385058260#2346380033_13L88808Q1201482072Q20 | draftkings | Hayden Rucci | Anytime TD Scorer | over | 0.276 | 0.0278 | 0.2482 | False | 2026-11-08T20:40:41Z |
| betmgm|anytd|13582 | betmgm | Josh Jacobs | anytd | over | 0.786 | 0.5556 | 0.2304 | False | 2026-11-03T12:08:57Z |
| betmgm|anytd|19240 | betmgm | Emmett Johnson | anytd | over | 0.2184 | 0.0769 | 0.1415 | False | 2026-11-08T20:40:41Z |
| draftkings|385058260|0QA385058260#2346380039_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.357 | 0.2273 | 0.1298 | False | 2026-11-08T20:40:41Z |
| draftkings|385715942|0QA385715942#2349512929_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.142 | 0.0179 | 0.1242 | False | 2026-11-08T20:40:41Z |
| draftkings|385058260|0QA385058260#2346380029_13L88808Q1-1158159522Q20 | draftkings | Kimani Vidal | Anytime TD Scorer | over | 0.2787 | 0.1739 | 0.1048 | False | 2026-11-08T20:40:41Z |
| betmgm|anytd|19231 | betmgm | Makai Lemon | anytd | over | 0.171 | 0.087 | 0.084 | False | 2026-11-08T20:40:41Z |
| draftkings|385058260|0QA385058260#2346380041_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.2184 | 0.1538 | 0.0646 | False | 2026-11-08T20:40:41Z |
| draftkings|385715942|0QA385715942#2349512928_13L88808Q1-1332651400Q20 | draftkings | Marvin Harrison Jr. | 2+ TDs | over | 0.0731 | 0.0278 | 0.0453 | False | 2026-11-08T20:40:41Z |
| betmgm|anytd|15459 | betmgm | Noah Gray | anytd | over | 0.2184 | 0.1739 | 0.0445 | False | 2026-11-05T00:59:13Z |
| draftkings|385715942|0QA385715942#2349513020_13L88808Q11652783646Q20 | draftkings | Hayden Rucci | 2+ TDs | over | 0.0422 | 0.004 | 0.0382 | False | 2026-11-08T20:40:41Z |
