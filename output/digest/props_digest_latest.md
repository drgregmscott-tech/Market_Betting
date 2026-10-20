# Props Pipeline Digest -- 2026-10-20T05:03:14Z

## Run summary
- DraftKings ingestion: 187 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 0 rows (OK)
- Estimation: 187 rows written (from 187 ingested rows) -- status breakdown: {'estimated': 117, 'unsupported_market_first_scorer': 48, 'no_player_match': 17, 'insufficient_history': 5}
- CLV logging: 12 newly flagged, 0 newly closed, 28 still open (1137 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|380413767|0QA380413767#2326613364_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.4173 | 0.1333 | 0.2839 | False | 2026-10-20T05:03:27Z |
| draftkings|380414163|0QA380414163#2326615207_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.4908 | 0.2174 | 0.2735 | False | 2026-10-19T04:57:20Z |
| draftkings|380414163|0QA380414163#2326615197_13L88808Q11505799344Q20 | draftkings | Caleb Williams | Anytime TD Scorer | over | 0.442 | 0.2174 | 0.2246 | False | 2026-10-19T04:57:20Z |
| draftkings|380413767|0QA380413767#2326613373_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4951 | 0.274 | 0.2211 | False | 2026-10-20T05:03:27Z |
| draftkings|380407190|0QA380407190#2326583675_13L88808Q1354446541Q20 | draftkings | Ollie Gordon II | Anytime TD Scorer | over | 0.555 | 0.3448 | 0.2102 | False | 2026-10-19T15:46:16Z |
| draftkings|380414163|0QA380414163#2326615199_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.253 | 0.0435 | 0.2095 | False | 2026-10-19T04:57:20Z |
| draftkings|380429075|0QA380429075#2326686729_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.569 | 0.3636 | 0.2054 | False | 2026-10-19T15:46:16Z |
| draftkings|380413767|0QA380413767#2326613357_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.4908 | 0.2941 | 0.1967 | False | 2026-10-19T15:46:16Z |
| draftkings|380412485|0QA380412485#2326607832_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.4231 | 0.2597 | 0.1633 | False | 2026-10-19T15:46:16Z |
| draftkings|380413767|0QA380413767#2326613365_13L88808Q144959304Q20 | draftkings | Tyler Shough | Anytime TD Scorer | over | 0.3173 | 0.1905 | 0.1268 | False | 2026-10-20T05:03:27Z |
| draftkings|380457140|0QA380457140#2326805310_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.1472 | 0.0278 | 0.1194 | False | 2026-10-19T04:57:20Z |
| draftkings|380413767|0QA380413767#2326613374_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.357 | 0.2439 | 0.1131 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888777_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.1472 | 0.0345 | 0.1127 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888819_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.15 | 0.0385 | 0.1116 | False | 2026-10-20T05:03:27Z |
| draftkings|380413767|0QA380413767#2326613363_13L88808Q11438391772Q20 | draftkings | Bryce Lance | Anytime TD Scorer | over | 0.2277 | 0.125 | 0.1027 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888781_13L88808Q1669299964Q20 | draftkings | Noah Fant | 2+ TDs | over | 0.1026 | 0.0123 | 0.0902 | False | 2026-10-20T05:03:27Z |
| draftkings|380457140|0QA380457140#2326805300_13L88808Q1-77651570Q20 | draftkings | Caleb Williams | 2+ TDs | over | 0.1164 | 0.0278 | 0.0887 | False | 2026-10-19T04:57:20Z |
| draftkings|380414163|0QA380414163#2326615211_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.1881 | 0.1111 | 0.077 | False | 2026-10-19T04:57:20Z |
| draftkings|380412485|0QA380412485#2326607841_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.4457 | 0.3774 | 0.0683 | False | 2026-10-19T15:46:16Z |
| draftkings|380428471|0QA380428471#2326683927_13L88808Q11365449708Q20 | draftkings | Ja'Marr Chase | Anytime TD Scorer | over | 0.5484 | 0.4878 | 0.0606 | False | 2026-10-19T15:46:16Z |
| draftkings|380414163|0QA380414163#2326615206_13L88808Q1-1762786291Q20 | draftkings | Hunter Henry | Anytime TD Scorer | over | 0.3729 | 0.3125 | 0.0604 | False | 2026-10-19T04:57:20Z |
| draftkings|380421646|0QA380421646#2326654425_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.375 | 0.3279 | 0.0471 | False | 2026-10-20T05:03:27Z |
| draftkings|380413767|0QA380413767#2326613361_13L88808Q1873985604Q20 | draftkings | Juwan Johnson | Anytime TD Scorer | over | 0.3093 | 0.2667 | 0.0426 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888820_13L88808Q1854391200Q20 | draftkings | Darnell Washington | 2+ TDs | over | 0.0731 | 0.0323 | 0.0408 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888779_13L88808Q1-1801413616Q20 | draftkings | Tyler Shough | 2+ TDs | over | 0.0567 | 0.0217 | 0.035 | False | 2026-10-20T05:03:27Z |
| draftkings|380457140|0QA380457140#2326805294_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.255 | 0.2222 | 0.0328 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805307_13L88808Q11740203848Q20 | draftkings | Hunter Henry | 2+ TDs | over | 0.0803 | 0.05 | 0.0303 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805304_13L88808Q1-704328598Q20 | draftkings | Jahdae Walker | 2+ TDs | over | 0.0351 | 0.005 | 0.0301 | False | 2026-10-19T04:57:20Z |
