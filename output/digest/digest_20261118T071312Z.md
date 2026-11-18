# Pipeline Digest -- 2026-11-18T07:13:12Z

## Run summary
- Ingestion: 30522 rows (PrizePicks OK, Underdog OK)
- Estimation: 30522 rows estimated (from 30522 ingested props)
- CLV logging: 19 newly flagged, 0 newly closed, 45 still open (112263 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| prizepicks|17061845 | prizepicks | Caleb Williams | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17132864 | prizepicks | Otávio | Goalie Fantasy Score | under | 0.35094246505677495 | 2026-11-18T07:21:08Z | 2026-11-18T18:30:00.000-05:00 |
| prizepicks|17061840 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.3252779099272486 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061852 | prizepicks | Bo Nix | Pass Yards | under | 0.3207875090752025 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061849 | prizepicks | Jared Goff | Pass Yards | under | 0.2998952886937002 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061853 | prizepicks | Kirk Cousins | Pass Yards | under | 0.26028541200637423 | 2026-11-17T13:14:06Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17061844 | prizepicks | Tyler Shough | Pass Yards | under | 0.249596263938357 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130513 | prizepicks | Anthony Gould | Rec Targets | under | 0.2024859989059048 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062823 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.20121645364759722 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130515 | prizepicks | Deion Burks | Rec Targets | under | 0.20109518155409178 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062826 | prizepicks | Colston Loveland | Rec Yards | under | 0.18934940884625828 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130516 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.1738729015911531 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17108500 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.15592492640886924 | 2026-11-18T07:21:08Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|7366db87-6436-4261-a7ab-08d5c3ea89ae | underdog | Chuba Hubbard | Rush Yards | under | 0.13714694341105027 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17130518 | prizepicks | Tyler Warren | Rec Targets | under | 0.11487669991604144 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062819 | prizepicks | Saquon Barkley | Rec Yards | under | 0.09863869301169803 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17135345 | prizepicks | Thomas Castellanos | Pass Comp | under | 0.09536785048076302 | 2026-11-18T07:21:08Z | 2026-11-21T15:30:00.000-05:00 |
| prizepicks|17108253 | prizepicks | Malik Washington | Recs | under | 0.08960270731713293 | 2026-11-18T07:21:08Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17133531 | prizepicks | Ben Shelton | Total Games | over | 0.08688440176281631 | 2026-11-18T07:21:08Z | 2026-11-19T08:00:00.000-05:00 |
| prizepicks|17069903 | prizepicks | Cibastian Broughton | Pass Comp | under | 0.07703897220700162 | 2026-11-17T13:14:06Z | 2026-11-18T19:00:00.000-05:00 |
| prizepicks|17061961 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.07421460278652392 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|d8b8533e-23fb-49eb-9469-929457ca0f41 | underdog | Tony Pollard | Rush Yards | under | 0.07124799057234155 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17062825 | prizepicks | Rome Odunze | Rec Yards | under | 0.06934931203037698 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062820 | prizepicks | Trey McBride | Rec Yards | under | 0.06498754344887514 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17108251 | prizepicks | Tyler Warren | Recs | under | 0.06469034806844876 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17108250 | prizepicks | Jonathan Taylor | Recs | under | 0.06375764686557794 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062817 | prizepicks | Pat Freiermuth | Rec Yards | under | 0.061571812750696786 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061832 | prizepicks | Jared Goff | Rush Yards | over | 0.060379424163094386 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130510 | prizepicks | Kayshon Boutte | Rec Targets | under | 0.0599063789217118 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17061958 | prizepicks | Javonte Williams | Rush Yards | under | 0.05867691672271225 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062828 | prizepicks | George Pickens | Rec Yards | under | 0.057941658909858806 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17127984 | prizepicks | Dino Prizmic | Total Games | over | 0.057852190533829395 | 2026-11-18T07:21:08Z | 2026-11-18T08:50:00.000-05:00 |
| prizepicks|17130517 | prizepicks | Laquon Treadwell | Rec Targets | under | 0.051181524104547904 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17061040 | prizepicks | Sofia Costoulas | Total Games Won | over | 0.050836700848094774 | 2026-11-18T07:21:08Z | 2026-11-18T09:30:00.000-05:00 |
| prizepicks|17062838 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.04762708868780563 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
| prizepicks|17061833 | prizepicks | Bryce Young | Rush Yards | under | 0.047291172718622376 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17127779 | prizepicks | Nicolai Budkov Kjaer | Break Points Won | under | 0.046932714913350715 | 2026-11-18T07:21:08Z | 2026-11-18T07:40:00.000-05:00 |
| prizepicks|17048468 | prizepicks | Jeremiah Smith | Recs | under | 0.0451889882160037 | 2026-11-17T13:14:06Z | 2026-11-21T12:00:00.000-05:00 |
| prizepicks|17130511 | prizepicks | Nico Collins | Rec Targets | under | 0.042106225908853046 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062822 | prizepicks | Chris Olave | Rec Yards | under | 0.04199283253040853 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062827 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0391841333439954 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061960 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.034137148515200666 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17127760 | prizepicks | Nishesh Basavareddy | Total Games | over | 0.0338495236823797 | 2026-11-18T07:21:08Z | 2026-11-18T06:30:00.000-05:00 |
| prizepicks|17124860 | prizepicks | Foster Moreau | Rec Yards | over | 0.03113122616529207 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062839 | prizepicks | Tee Higgins | Rec Yards | under | 0.03001893073314066 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
