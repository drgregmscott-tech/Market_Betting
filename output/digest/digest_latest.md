# Pipeline Digest -- 2026-11-19T12:52:27Z

## Run summary
- Ingestion: 45328 rows (PrizePicks OK, Underdog OK)
- Estimation: 45328 rows estimated (from 45328 ingested props)
- CLV logging: 39 newly flagged, 0 newly closed, 76 still open (112302 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|00b55c3f-8b0c-4d3b-b154-5539e4b0cb6a | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17061845 | prizepicks | Caleb Williams | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061840 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.3252779099272486 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061852 | prizepicks | Bo Nix | Pass Yards | under | 0.3207875090752025 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061849 | prizepicks | Jared Goff | Pass Yards | under | 0.2998952886937002 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172881 | prizepicks | Simi Fehoko | Rec Targets | under | 0.27241322394721845 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173322 | prizepicks | Saquon Barkley | Rec Targets | under | 0.2614113836150421 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061853 | prizepicks | Kirk Cousins | Pass Yards | under | 0.26028541200637423 | 2026-11-17T13:14:06Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17061844 | prizepicks | Tyler Shough | Pass Yards | under | 0.249596263938357 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130513 | prizepicks | Anthony Gould | Rec Targets | under | 0.2024859989059048 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062823 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.20121645364759722 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130515 | prizepicks | Deion Burks | Rec Targets | under | 0.20109518155409178 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062826 | prizepicks | Colston Loveland | Rec Yards | under | 0.18934940884625828 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130516 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.1738729015911531 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17051036 | prizepicks | J.J. McCarthy | Pass Attempts | under | 0.17200392454345736 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17173278 | prizepicks | Bryce Young | Pass Attempts | under | 0.16981258723647652 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17145038 | prizepicks | J'Koby Williams | Rush Atts | under | 0.16445839277350327 | 2026-11-19T12:57:27Z | 2026-11-21T15:30:00.000-05:00 |
| prizepicks|17172878 | prizepicks | Devin Duvernay | Rec Targets | under | 0.16164416934279247 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173300 | prizepicks | Caleb Douglas | Rec Targets | under | 0.16088184950571505 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17108500 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.15592492640886924 | 2026-11-18T07:21:08Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172918 | prizepicks | Jonah Coleman | Rec Targets | under | 0.14978688180069022 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17173327 | prizepicks | George Kittle | Rec Targets | under | 0.1209148489978571 | 2026-11-19T12:57:27Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17173329 | prizepicks | Carnell Tate | Rec Targets | under | 0.11936405589873289 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173573 | prizepicks | Pierre-Hugues Herbert | Break Points Won | under | 0.11893560816962179 | 2026-11-19T12:57:27Z | 2026-11-19T13:10:00.000-05:00 |
| prizepicks|17130518 | prizepicks | Tyler Warren | Rec Targets | under | 0.11487669991604144 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17172934 | prizepicks | Rashee Rice | Rec Targets | under | 0.11021925715465086 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172901 | prizepicks | Rome Odunze | Rec Targets | under | 0.11012854291659335 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062819 | prizepicks | Saquon Barkley | Rec Yards | under | 0.09863869301169803 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172919 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.09754658311451958 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17182426 | prizepicks | Raleek Brown | Rush Atts | under | 0.09616113761388234 | 2026-11-19T12:57:27Z | 2026-11-21T15:30:00.000-05:00 |
| prizepicks|17172885 | prizepicks | Mark Andrews | Rec Targets | under | 0.09572067811479934 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17135345 | prizepicks | Thomas Castellanos | Pass Comp | under | 0.09536785048076302 | 2026-11-18T07:21:08Z | 2026-11-21T15:30:00.000-05:00 |
| prizepicks|17172915 | prizepicks | Courtland Sutton | Rec Targets | under | 0.09246124133941824 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17172910 | prizepicks | Brevyn Spann-Ford | Rec Targets | under | 0.09246107865183517 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172879 | prizepicks | Elijah Higgins | Rec Targets | under | 0.09033332967696128 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17108253 | prizepicks | Malik Washington | Recs | under | 0.08960270731713293 | 2026-11-18T07:21:08Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17133531 | prizepicks | Ben Shelton | Total Games | over | 0.08688440176281631 | 2026-11-18T07:21:08Z | 2026-11-19T08:00:00.000-05:00 |
| prizepicks|17172887 | prizepicks | Zay Flowers | Rec Targets | under | 0.08455536078122694 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172929 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.07673950782785632 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061961 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.07421460278652392 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17171192 | prizepicks | Trent Mosley | Recs | under | 0.07044771134950334 | 2026-11-19T12:57:27Z | 2026-11-21T18:15:00.000-05:00 |
| prizepicks|17062825 | prizepicks | Rome Odunze | Rec Yards | under | 0.06934931203037698 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172892 | prizepicks | Chuba Hubbard | Rec Targets | under | 0.06830618693227275 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062820 | prizepicks | Trey McBride | Rec Yards | under | 0.06498754344887514 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17108251 | prizepicks | Tyler Warren | Recs | under | 0.06469034806844876 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17108250 | prizepicks | Jonathan Taylor | Recs | under | 0.06375764686557794 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17172930 | prizepicks | Parker Washington | Rec Targets | under | 0.0633590315023902 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17173299 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.06292702037752551 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061832 | prizepicks | Jared Goff | Rush Yards | over | 0.060379424163094386 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17130510 | prizepicks | Kayshon Boutte | Rec Targets | under | 0.0599063789217118 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17172886 | prizepicks | Rashod Bateman | Rec Targets | under | 0.05903617850266274 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061958 | prizepicks | Javonte Williams | Rush Yards | under | 0.05867691672271225 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062828 | prizepicks | George Pickens | Rec Yards | under | 0.057941658909858806 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173320 | prizepicks | Dallas Goedert | Rec Targets | under | 0.05723699870527432 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172916 | prizepicks | Evan Engram | Rec Targets | under | 0.055149375824596114 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17130517 | prizepicks | Laquon Treadwell | Rec Targets | under | 0.051181524104547904 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17172882 | prizepicks | Trey McBride | Rec Targets | under | 0.05110290304981535 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17160348 | prizepicks | Caleb Komolafe | Rush Atts | under | 0.04848348416748782 | 2026-11-19T12:57:27Z | 2026-11-21T12:00:00.000-05:00 |
| prizepicks|17062838 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.04762708868780563 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
| prizepicks|17061833 | prizepicks | Bryce Young | Rush Yards | under | 0.047291172718622376 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172897 | prizepicks | Colston Loveland | Rec Targets | under | 0.04606205650067807 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17048468 | prizepicks | Jeremiah Smith | Recs | under | 0.0451889882160037 | 2026-11-17T13:14:06Z | 2026-11-21T12:00:00.000-05:00 |
| prizepicks|17173301 | prizepicks | Malik Washington | Rec Targets | under | 0.045000357409681446 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172900 | prizepicks | Luther Burden III | Rec Targets | under | 0.04402870912635659 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172911 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.04290639274739827 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173316 | prizepicks | Isaiah Likely | Rec Targets | under | 0.04213161314240221 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17130511 | prizepicks | Nico Collins | Rec Targets | under | 0.042106225908853046 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062822 | prizepicks | Chris Olave | Rec Yards | under | 0.04199283253040853 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062827 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0391841333439954 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172924 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.03913660075609349 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17172889 | prizepicks | DJ Moore | Rec Targets | under | 0.03600478749616709 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172922 | prizepicks | Jameson Williams | Rec Targets | under | 0.03533413292464671 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172914 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.03478762538563951 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061960 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.034137148515200666 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17124860 | prizepicks | Foster Moreau | Rec Yards | over | 0.03113122616529207 | 2026-11-18T07:21:08Z | 2026-11-19T20:15:00.000-05:00 |
| prizepicks|17062839 | prizepicks | Tee Higgins | Rec Yards | under | 0.03001893073314066 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
