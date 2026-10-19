# Props Pipeline Digest -- 2026-10-19T04:57:08Z

## Run summary
- DraftKings ingestion: 164 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 76 rows (OK)
- Estimation: 240 rows written (from 240 ingested rows) -- status breakdown: {'estimated': 120, 'unsupported_market_first_scorer': 69, 'unsupported_stat_type': 24, 'no_player_match': 22, 'insufficient_history': 5}
- CLV logging: 12 newly flagged, 0 newly closed, 25 still open (1119 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|16042 | betmgm | Chig Okonkwo | recs | over | 1.0 | 0.5835 | 0.4165 | False | 2026-10-17T18:37:50Z |
| draftkings|380414163|0QA380414163#2326615207_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.4908 | 0.2174 | 0.2735 | False | 2026-10-19T04:57:20Z |
| draftkings|378218690|0QA378218690#2317773852_13L88808Q1557870560Q20 | draftkings | Treylon Burks | Anytime TD Scorer | over | 0.3902 | 0.1429 | 0.2473 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773850_13L88808Q1111756323Q20 | draftkings | Jayden Daniels | Anytime TD Scorer | over | 0.5374 | 0.2985 | 0.2389 | False | 2026-10-18T22:31:17Z |
| draftkings|380414163|0QA380414163#2326615208_13L88808Q1-349638135Q20 | draftkings | Romeo Doubs | Anytime TD Scorer | over | 0.4647 | 0.2273 | 0.2375 | False | 2026-10-19T04:57:20Z |
| draftkings|380414163|0QA380414163#2326615197_13L88808Q11505799344Q20 | draftkings | Caleb Williams | Anytime TD Scorer | over | 0.442 | 0.2174 | 0.2246 | False | 2026-10-19T04:57:20Z |
| draftkings|380414163|0QA380414163#2326615199_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.253 | 0.0435 | 0.2095 | False | 2026-10-19T04:57:20Z |
| draftkings|378218690|0QA378218690#2317773854_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.4819 | 0.3125 | 0.1694 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773844_13L88808Q1436278619Q20 | draftkings | Brandin Cooks | Anytime TD Scorer | over | 0.4182 | 0.2817 | 0.1365 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977020_13L88808Q11175147349Q20 | draftkings | Jayden Daniels | 2+ TDs | over | 0.1808 | 0.0476 | 0.1331 | False | 2026-10-18T22:31:17Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|380457140|0QA380457140#2326805310_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.1472 | 0.0278 | 0.1194 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805312_13L88808Q1652552487Q20 | draftkings | Romeo Doubs | 2+ TDs | over | 0.1302 | 0.0278 | 0.1024 | False | 2026-10-19T04:57:20Z |
| draftkings|378535859|0QA378535859#2318977024_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1412 | 0.05 | 0.0912 | False | 2026-10-18T22:31:17Z |
| draftkings|380457140|0QA380457140#2326805300_13L88808Q1-77651570Q20 | draftkings | Caleb Williams | 2+ TDs | over | 0.1164 | 0.0278 | 0.0887 | False | 2026-10-19T04:57:20Z |
| draftkings|380414163|0QA380414163#2326615211_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.1881 | 0.1111 | 0.077 | False | 2026-10-19T04:57:20Z |
| draftkings|378535859|0QA378535859#2318977025_13L88808Q11674958948Q20 | draftkings | Treylon Burks | 2+ TDs | over | 0.0886 | 0.0132 | 0.0754 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2318847309_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.253 | 0.1818 | 0.0712 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773836_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.5439 | 0.4762 | 0.0677 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977007_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.1858 | 0.125 | 0.0608 | False | 2026-10-18T22:31:17Z |
| draftkings|380414163|0QA380414163#2326615206_13L88808Q1-1762786291Q20 | draftkings | Hunter Henry | Anytime TD Scorer | over | 0.3729 | 0.3125 | 0.0604 | False | 2026-10-19T04:57:20Z |
| draftkings|378535859|0QA378535859#2318977008_13L88808Q1-703528487Q20 | draftkings | Brandin Cooks | 2+ TDs | over | 0.1031 | 0.0435 | 0.0596 | False | 2026-10-18T22:31:17Z |
| draftkings|380457140|0QA380457140#2326805294_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.255 | 0.2222 | 0.0328 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805307_13L88808Q11740203848Q20 | draftkings | Hunter Henry | 2+ TDs | over | 0.0803 | 0.05 | 0.0303 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805304_13L88808Q1-704328598Q20 | draftkings | Jahdae Walker | 2+ TDs | over | 0.0351 | 0.005 | 0.0301 | False | 2026-10-19T04:57:20Z |
