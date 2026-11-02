# Props Pipeline Digest -- 2026-11-02T18:34:57Z

## Run summary
- DraftKings ingestion: 204 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 83 rows (OK)
- Estimation: 287 rows written (from 287 ingested rows) -- status breakdown: {'estimated': 153, 'unsupported_market_first_scorer': 66, 'no_player_match': 35, 'unsupported_stat_type': 28, 'insufficient_history': 5}
- CLV logging: 9 newly flagged, 0 newly closed, 34 still open (1378 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|19357 | betmgm | Sam Roush | recs | over | 0.9996 | 0.3887 | 0.6108 | False | 2026-11-02T06:30:02Z |
| draftkings|385025617|0QA385025617#2346198696_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2817 | 0.3504 | False | 2026-11-02T18:35:10Z |
| draftkings|382704598|0QA382704598#2336274497_13L88808Q11707072676Q20 | draftkings | Emanuel Wilson | Anytime TD Scorer | over | 0.4937 | 0.2128 | 0.281 | False | 2026-11-02T06:30:02Z |
| draftkings|385025617|0QA385025617#2346198681_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.4701 | 0.2326 | 0.2375 | False | 2026-11-02T18:35:10Z |
| draftkings|385070262|0QA385070262#2346502179_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.6255 | 0.4082 | 0.2173 | False | 2026-11-02T18:35:10Z |
| draftkings|385020238|0QA385020238#2346168574_13L88808Q11230695518Q20 | draftkings | Bhayshul Tuten | Anytime TD Scorer | over | 0.6565 | 0.4444 | 0.2121 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168583_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.3729 | 0.1667 | 0.2062 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301467_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.5492 | 0.3448 | 0.2043 | False | 2026-11-02T18:35:10Z |
| draftkings|385105249|0QA385105249#2346697217_13L88808Q1163343434Q20 | draftkings | Bhayshul Tuten | 2+ TDs | over | 0.2894 | 0.1053 | 0.1842 | False | 2026-11-02T06:30:02Z |
| draftkings|382704598|0QA382704598#2336274516_13L88808Q11505799344Q20 | draftkings | Caleb Williams | Anytime TD Scorer | over | 0.3164 | 0.1667 | 0.1498 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168569_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.0556 | 0.1459 | False | 2026-11-02T06:30:02Z |
| draftkings|382704598|0QA382704598#2336274518_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.1732 | 0.0385 | 0.1348 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168578_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.3147 | 0.1818 | 0.1329 | False | 2026-11-02T06:30:02Z |
| draftkings|383246973|0QA383246973#2338622604_13L88808Q1-1357951342Q20 | draftkings | Emanuel Wilson | 2+ TDs | over | 0.1491 | 0.0278 | 0.1214 | False | 2026-11-02T06:30:02Z |
| draftkings|383246973|0QA383246973#2338622506_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.2734 | 0.1538 | 0.1196 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168579_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.3869 | 0.274 | 0.113 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168570_13L88808Q11714132096Q20 | draftkings | Josh Cuevas | Anytime TD Scorer | over | 0.1675 | 0.0556 | 0.112 | False | 2026-11-02T06:30:02Z |
| draftkings|385070262|0QA385070262#2346502164_13L88808Q11579636272Q20 | draftkings | Malik Willis | Anytime TD Scorer | over | 0.3555 | 0.2597 | 0.0958 | False | 2026-11-02T18:35:10Z |
| draftkings|385020238|0QA385020238#2346168568_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.1479 | 0.0625 | 0.0854 | False | 2026-11-02T06:30:02Z |
| draftkings|383246973|0QA383246973#2338622500_13L88808Q1491696445Q20 | draftkings | Jaxon Smith-Njigba | 2+ TDs | over | 0.2372 | 0.1538 | 0.0834 | False | 2026-11-02T06:30:02Z |
| draftkings|385025617|0QA385025617#2346198695_13L88808Q1106346443Q20 | draftkings | Tee Higgins | Anytime TD Scorer | over | 0.551 | 0.4762 | 0.0748 | False | 2026-11-02T18:35:10Z |
| draftkings|385020238|0QA385020238#2346168562_13L88808Q12018204784Q20 | draftkings | Zay Flowers | Anytime TD Scorer | over | 0.3156 | 0.25 | 0.0656 | False | 2026-11-02T06:30:02Z |
| draftkings|385105249|0QA385105249#2346697225_13L88808Q1-1058483772Q20 | draftkings | Nate Boerkircher | 2+ TDs | over | 0.0803 | 0.0196 | 0.0607 | False | 2026-11-02T06:30:02Z |
| draftkings|385105249|0QA385105249#2346697203_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.2047 | 0.1538 | 0.0509 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301464_13L88808Q1968442089Q20 | draftkings | Rachaad White | Anytime TD Scorer | over | 0.4566 | 0.4082 | 0.0485 | False | 2026-11-02T18:35:10Z |
| draftkings|385070262|0QA385070262#2346502163_13L88808Q1354446541Q20 | draftkings | Ollie Gordon II | Anytime TD Scorer | over | 0.4823 | 0.4348 | 0.0475 | False | 2026-11-02T18:35:10Z |
| draftkings|385105249|0QA385105249#2346697220_13L88808Q1-1327690156Q20 | draftkings | Chris Rodriguez Jr. | 2+ TDs | over | 0.087 | 0.0435 | 0.0435 | False | 2026-11-02T06:30:02Z |
| draftkings|382704598|0QA382704598#2336274514_13L88808Q1-2109230062Q20 | draftkings | Colston Loveland | Anytime TD Scorer | over | 0.3578 | 0.3175 | 0.0403 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301465_13L88808Q1111756323Q20 | draftkings | Jayden Daniels | Anytime TD Scorer | over | 0.3297 | 0.2899 | 0.0398 | False | 2026-11-02T18:35:10Z |
| draftkings|383246973|0QA383246973#2338622612_13L88808Q1-77651570Q20 | draftkings | Caleb Williams | 2+ TDs | over | 0.0564 | 0.0179 | 0.0385 | False | 2026-11-02T06:30:02Z |
| draftkings|385105249|0QA385105249#2346697224_13L88808Q11304672355Q20 | draftkings | Brian Thomas Jr. | 2+ TDs | over | 0.0557 | 0.0179 | 0.0379 | False | 2026-11-02T06:30:02Z |
| draftkings|382704598|0QA382704598#2336274498_13L88808Q12121391530Q20 | draftkings | George Holani | Anytime TD Scorer | over | 0.1783 | 0.1429 | 0.0355 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168580_13L88808Q1-458881524Q20 | draftkings | Travis Hunter | Anytime TD Scorer | over | 0.1783 | 0.1429 | 0.0355 | False | 2026-11-02T06:30:02Z |
| draftkings|382704598|0QA382704598#2336274506_13L88808Q1-644359754Q20 | draftkings | Eric Saubert | Anytime TD Scorer | over | 0.1054 | 0.0714 | 0.034 | False | 2026-11-02T06:30:02Z |
