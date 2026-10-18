# Props Pipeline Digest -- 2026-10-18T22:31:04Z

## Run summary
- DraftKings ingestion: 173 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 228 rows (OK)
- Estimation: 401 rows written (from 401 ingested rows) -- status breakdown: {'estimated': 180, 'unsupported_market_first_scorer': 88, 'unsupported_stat_type': 81, 'no_player_match': 40, 'insufficient_history': 12}
- CLV logging: 19 newly flagged, 0 newly closed, 22 still open (1107 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|16042 | betmgm | Chig Okonkwo | recs | over | 1.0 | 0.5835 | 0.4165 | False | 2026-10-17T18:37:50Z |
| betmgm|anytd|18251 | betmgm | Hayden Rucci | anytd | over | 0.4182 | 0.0345 | 0.3837 | False | 2026-10-15T23:09:30Z |
| draftkings|378218690|0QA378218690#2317773852_13L88808Q1557870560Q20 | draftkings | Treylon Burks | Anytime TD Scorer | over | 0.3902 | 0.1429 | 0.2473 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773850_13L88808Q1111756323Q20 | draftkings | Jayden Daniels | Anytime TD Scorer | over | 0.5374 | 0.2985 | 0.2389 | False | 2026-10-18T22:31:17Z |
| draftkings|378204047|0QA378204047#2317708168_13L88808Q1-1411527739Q20 | draftkings | Christian Watson | Anytime TD Scorer | over | 0.6958 | 0.4651 | 0.2307 | False | 2026-10-18T22:31:17Z |
| draftkings|378561952|0QA378561952#2319061383_13L88808Q1-1356601652Q20 | draftkings | Christian Watson | 2+ TDs | over | 0.3338 | 0.125 | 0.2088 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773854_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.4819 | 0.3125 | 0.1694 | False | 2026-10-18T22:31:17Z |
| draftkings|378204047|0QA378204047#2317708183_13L88808Q1-144445670Q20 | draftkings | Jake Ferguson | Anytime TD Scorer | over | 0.4055 | 0.2597 | 0.1457 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773844_13L88808Q1436278619Q20 | draftkings | Brandin Cooks | Anytime TD Scorer | over | 0.4182 | 0.2817 | 0.1365 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977020_13L88808Q11175147349Q20 | draftkings | Jayden Daniels | 2+ TDs | over | 0.1808 | 0.0476 | 0.1331 | False | 2026-10-18T22:31:17Z |
| betmgm|anytd|9260 | betmgm | Brandin Cooks | anytd | over | 0.4182 | 0.2857 | 0.1325 | False | 2026-10-13T11:58:47Z |
| draftkings|378561952|0QA378561952#2319061393_13L88808Q12056061885Q20 | draftkings | Javonte Williams | 2+ TDs | over | 0.4185 | 0.2941 | 0.1244 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977024_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1412 | 0.05 | 0.0912 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977025_13L88808Q11674958948Q20 | draftkings | Treylon Burks | 2+ TDs | over | 0.0886 | 0.0132 | 0.0754 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2318847309_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.253 | 0.1818 | 0.0712 | False | 2026-10-18T22:31:17Z |
| draftkings|378204047|0QA378204047#2317708186_13L88808Q1744413187Q20 | draftkings | KaVontae Turpin | Anytime TD Scorer | over | 0.1813 | 0.1111 | 0.0702 | False | 2026-10-18T22:31:17Z |
| draftkings|378218690|0QA378218690#2317773836_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.5439 | 0.4762 | 0.0677 | False | 2026-10-18T22:31:17Z |
| draftkings|378561952|0QA378561952#2319061396_13L88808Q1-691724415Q20 | draftkings | Jake Ferguson | 2+ TDs | over | 0.0963 | 0.0345 | 0.0618 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977007_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.1858 | 0.125 | 0.0608 | False | 2026-10-18T22:31:17Z |
| draftkings|378535859|0QA378535859#2318977008_13L88808Q1-703528487Q20 | draftkings | Brandin Cooks | 2+ TDs | over | 0.1031 | 0.0435 | 0.0596 | False | 2026-10-18T22:31:17Z |
| draftkings|378561952|0QA378561952#2319061394_13L88808Q1-1472312629Q20 | draftkings | CeeDee Lamb | 2+ TDs | over | 0.1506 | 0.1053 | 0.0453 | False | 2026-10-18T22:31:17Z |
| draftkings|378204047|0QA378204047#2317708181_13L88808Q1759561049Q20 | draftkings | CeeDee Lamb | Anytime TD Scorer | over | 0.4959 | 0.4545 | 0.0414 | False | 2026-10-18T22:31:17Z |
