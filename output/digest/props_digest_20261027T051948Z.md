# Props Pipeline Digest -- 2026-10-27T05:19:48Z

## Run summary
- DraftKings ingestion: 131 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 0 rows (OK)
- Estimation: 131 rows written (from 131 ingested rows) -- status breakdown: {'estimated': 87, 'unsupported_market_first_scorer': 28, 'no_player_match': 13, 'insufficient_history': 3}
- CLV logging: 1 newly flagged, 0 newly closed, 19 still open (1262 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|382678835|0QA382678835#2336411431_13L88808Q11890020597Q20 | draftkings | Anthony Tyus III | Anytime TD Scorer | over | 0.3198 | 0.0714 | 0.2484 | False | 2026-10-26T05:02:37Z |
| draftkings|382665132|0QA382665132#2336049742_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.5555 | 0.3279 | 0.2276 | False | 2026-10-26T15:30:26Z |
| draftkings|382641891|0QA382641891#2335870681_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.6068 | 0.3922 | 0.2146 | False | 2026-10-26T15:30:26Z |
| draftkings|382796087|0QA382796087#2336703200_13L88808Q1938922925Q20 | draftkings | Omar Cooper Jr. | Anytime TD Scorer | over | 0.5075 | 0.303 | 0.2045 | False | 2026-10-27T05:19:59Z |
| draftkings|382678835|0QA382678835#2336140028_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.3965 | 0.2 | 0.1965 | False | 2026-10-26T05:02:37Z |
| draftkings|382678835|0QA382678835#2336140032_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.3408 | 0.1905 | 0.1503 | False | 2026-10-26T05:02:37Z |
| draftkings|382709590|0QA382709590#2336304212_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.5813 | 0.4545 | 0.1268 | False | 2026-10-26T15:30:26Z |
| draftkings|382656185|0QA382656185#2336007908_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4206 | 0.2985 | 0.1221 | False | 2026-10-26T15:30:26Z |
| draftkings|382641891|0QA382641891#2335870682_13L88808Q1472584472Q20 | draftkings | Sam LaPorta | Anytime TD Scorer | over | 0.4025 | 0.3125 | 0.09 | False | 2026-10-26T15:30:26Z |
| draftkings|382656185|0QA382656185#2336007914_13L88808Q1-1895349765Q20 | draftkings | Quinshon Judkins | Anytime TD Scorer | over | 0.5034 | 0.4167 | 0.0867 | False | 2026-10-26T15:30:26Z |
| draftkings|382678835|0QA382678835#2336140012_13L88808Q1-135035926Q20 | draftkings | MarShawn Lloyd | Anytime TD Scorer | over | 0.3392 | 0.2597 | 0.0794 | False | 2026-10-26T05:02:37Z |
| draftkings|382734951|0QA382734951#2336425062_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.0917 | 0.0217 | 0.07 | False | 2026-10-26T05:02:37Z |
| draftkings|382678835|0QA382678835#2336140015_13L88808Q1-1213243313Q20 | draftkings | Jordan Love | Anytime TD Scorer | over | 0.1783 | 0.1111 | 0.0672 | False | 2026-10-26T05:02:37Z |
| draftkings|382678835|0QA382678835#2336140001_13L88808Q1-1411527739Q20 | draftkings | Christian Watson | Anytime TD Scorer | over | 0.4876 | 0.4255 | 0.062 | False | 2026-10-26T05:02:37Z |
| draftkings|382734951|0QA382734951#2336425047_13L88808Q1-1356601652Q20 | draftkings | Christian Watson | 2+ TDs | over | 0.145 | 0.0909 | 0.054 | False | 2026-10-26T05:02:37Z |
| draftkings|382734951|0QA382734951#2336425071_13L88808Q1-2074865306Q20 | draftkings | Anthony Tyus III | 2+ TDs | over | 0.0577 | 0.0055 | 0.0522 | False | 2026-10-26T05:02:37Z |
| draftkings|382734951|0QA382734951#2336425059_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.2147 | 0.1667 | 0.0481 | False | 2026-10-26T05:02:37Z |
| draftkings|382678835|0QA382678835#2336140031_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.1479 | 0.1 | 0.0479 | False | 2026-10-26T05:02:37Z |
| draftkings|382734951|0QA382734951#2336425063_13L88808Q1372601323Q20 | draftkings | Tommy Tremble | 2+ TDs | over | 0.0661 | 0.0196 | 0.0465 | False | 2026-10-26T05:02:37Z |
