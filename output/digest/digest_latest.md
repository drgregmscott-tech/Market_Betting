# Pipeline Digest -- 2026-10-11T20:11:58Z

## Run summary
- Ingestion: 16082 rows (PrizePicks OK, Underdog OK)
- Estimation: 16082 rows estimated (from 16082 ingested props)
- CLV logging: 86 newly flagged, 0 newly closed, 496 still open (100695 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|1b46f01b-7fda-4def-a3f5-87454bb59d9e | underdog | Jason Myers | FG Made | under | 0.4629061757595768 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|0d9601e6-1644-4608-bf51-06f2a5b98214 | underdog | Brice Turang | RBIs | over | 0.4447860962566845 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|97ecc7e0-8001-4a00-a537-1e86508a2ce7 | underdog | Jared Goff | Pass Yards | under | 0.4424089119535177 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|093667ee-9e39-43e1-8fce-68d03039aaef | underdog | Michael Penix | Pass Attempts | under | 0.4357142857142857 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|1e457aef-3642-47e4-bfcf-70a4f2b610d7 | underdog | Brock Purdy | Completions | under | 0.4357142857142857 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|57204767-ffb1-4a3d-8cdf-79b4c49ea29e | underdog | Matthew Stafford | Pass Yards | under | 0.4341741267068928 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|2bd0ed1c-f0c0-484d-a419-473307f8a034 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|63b484b3-7986-4201-9b17-b25c64c13571 | underdog | Josh Allen | Pass Attempts | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|765047d3-6006-47ea-9a2c-b5572dc4e6be | underdog | Michael Penix | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|4dd5f0c6-da42-406b-8607-ad18d5a179b5 | underdog | Jared Goff | Completions | under | 0.4 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|aa4801ae-3a04-46f7-a9f1-fd562064e6e6 | underdog | Josh Allen | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|b22ffd17-ba14-48b7-a938-568896cf1cbb | underdog | Brock Purdy | Rush Yards | under | 0.4 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|0fbfe1f0-c6f9-4702-aee6-b0276f4107d1 | underdog | Christian McCaffrey | Receptions | under | 0.3988102626733253 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|b8c471fa-f730-492c-aaff-de71f7ad6540 | underdog | Jason Myers | Kicking Points | under | 0.3937789558660911 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|129efc56-6f78-466c-9804-39217dffa69d | underdog | Puka Nacua | Receiving Yards | under | 0.3795480058010654 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|befc81f0-b21a-4405-9e36-1e02f3fb2f77 | underdog | Nick Folk | FG Made | under | 0.3745514871135351 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|871ea002-cb1d-4d37-9a67-b9ccd719e037 | underdog | Brock Purdy | Pass Attempts | under | 0.3723618090452261 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|fffbf28b-f8be-416d-af58-265c73ccbd0b | underdog | Jacoby Brissett | Pass Yards | under | 0.3642857142857143 | 2026-10-10T05:51:08Z | 2026-10-11T20:25:00Z |
| underdog|2eaf2435-4e22-4ba7-a5d2-6457f5b15eb3 | underdog | Trey McBride | Receiving Yards | under | 0.3598365116849146 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|e653d5c9-203f-4464-8d0f-58ba0e15da67 | underdog | Michael Penix | Pass Yards | under | 0.3595959595959597 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|5af199c9-a4ca-480e-9fec-ddee37ffee58 | underdog | Josh Allen | Pass Yards | under | 0.3591836734693877 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|a37c2c84-6bd0-4807-a3a7-6bbccf7d9d90 | underdog | Steven Kwan | Batter Walks | over | 0.3517938682322243 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15449673 | prizepicks | Jacoby Brissett | Pass Yards | under | 0.3509424650567749 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15533050 | prizepicks | Trey McBride | Rec Targets | under | 0.3509424650567749 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15494685 | prizepicks | Trey McBride | Recs | under | 0.3509424650567749 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15452205 | prizepicks | Christian McCaffrey | Recs | under | 0.3509424650567749 | 2026-10-11T20:18:47Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|f18c591d-b293-415a-9db5-12f21aaeb98b | underdog | Brice Turang | Batter Walks | over | 0.3503276539973787 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|1f14707b-275b-4f43-9374-74717b39b040 | underdog | Michael Penix | Pass TDs | under | 0.3467005076142132 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|a2fd2eb1-4913-46c7-b2ee-fbff43564395 | underdog | Jacoby Brissett | Completions | under | 0.3443720287564475 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|ab62192f-cec6-40f0-b0c1-3aac63435f7d | underdog | Andy Pages | RBIs | over | 0.3353389490573606 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|d91c6aa1-f274-4f9e-a95a-742cf2c29dc5 | underdog | Matthew Stafford | Completions | under | 0.3348008285125783 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|61513c25-9781-49b6-893f-3bf5a484c95f | underdog | Charles De Ketelaere | Shots Attempted | under | 0.3328299850613506 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|87a94a5a-88f1-46e4-9ca5-a0c1ff975267 | underdog | Jake Bauers | Batter Walks | over | 0.3270889487870619 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|2ae0f7e5-4ff3-44a9-9836-40696d8b1442 | underdog | Tyler Loop | FG Made | under | 0.3263281368597279 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|29cdf1f7-a211-4e3a-9cde-995abf60fff2 | underdog | Dawson Knox | Receiving Yards | under | 0.3256410256410256 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|15449672 | prizepicks | Jared Goff | Pass Yards | under | 0.3229208330880209 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15449909 | prizepicks | Trey McBride | Rec Yards | under | 0.3203423734117173 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|064dd30b-9aac-4164-8882-0ba99672690c | underdog | Jacoby Brissett | Pass TDs | under | 0.3116425980687034 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|94701aa5-8f21-4df5-852e-b94700a79716 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3095104204107922 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|5e4c0045-b85d-4f37-80bc-28b653c73f62 | underdog | Colby Parkinson | Receiving Yards | under | 0.304864547661155 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|f5d4b62c-6ada-41f3-8fd1-58eb65b443f8 | underdog | Eddy Pineiro | FG Made | under | 0.3013237790045318 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|c3c42681-2420-4c10-9c54-02119dc203bd | underdog | Tyler Allgeier | Receiving Yards | under | 0.298989898989899 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2eb7f05a-a05a-4b68-829b-fb75ae65fe94 | underdog | Mike Evans | Receiving Yards | under | 0.2969685991401806 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|5d0df89f-50bd-4cba-86c0-3b56f8d932ba | underdog | James Cook | Receiving Yards | under | 0.2856105912025095 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|15449900 | prizepicks | Christian McCaffrey | Rec Yards | under | 0.2786153182458308 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|d4060982-6b93-40e5-a4fe-ecb3dbc6ee6e | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.276281816724621 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15533063 | prizepicks | Troy Franklin | Rec Targets | under | 0.2762539045085913 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|fe280193-2f7d-47fc-aded-70fb9c741087 | underdog | Puka Nacua | Receptions | under | 0.2756118058538218 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|c4f8457d-53ec-4fc4-9c30-18114a8b3c71 | underdog | Sam Darnold | Pass Yards | under | 0.2729977800889878 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|6bf44240-0755-4388-880a-e47f0635d3c7 | underdog | Jacoby Brissett | Pass Attempts | under | 0.2709236835736173 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15449769 | prizepicks | Bo Nix | Rush Yards | under | 0.2679388206198347 | 2026-10-07T05:55:02Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|be7db7b4-f06e-4e3d-93fd-721bd0760e19 | underdog | Eddy Pineiro | Kicking Points | under | 0.2668372806611836 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|3a14827c-569f-4eb8-9345-895fe6e771f9 | underdog | Sam LaPorta | Receiving Yards | under | 0.2667595783945387 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|bdd85957-ef5a-4ba0-bc19-82eeb30f5e4e | underdog | Michael Wilson | Receiving Yards | under | 0.2663036175518312 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|0c67a299-6d50-4dfd-83d8-86ac1896c81b | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.265955000867306 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|95787424-9355-4ac6-a8f4-c182381725a2 | underdog | Brice Turang | Runs | over | 0.2641962143428416 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| prizepicks|15533351 | prizepicks | George Kittle | Rec Targets | under | 0.2626516200178651 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15489682 | prizepicks | Drake London | Rec Targets | under | 0.2622372257125874 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|aaf90278-20f0-46b9-9125-93dde4fac508 | underdog | Christian Yelich | Runs | over | 0.2567122593718339 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|a978bb2e-0d01-4165-af55-9cd269cfe52b | underdog | George Kittle | Receptions | under | 0.2528572985479788 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|427cad33-933f-4020-bf19-9b46db422f35 | underdog | Romello Height | Sacks | over | 0.2489526914183761 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|3094dc42-a0a4-4ac0-8f4a-6347d0461f2d | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2459715639810428 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| prizepicks|13975919 | prizepicks | Jayson Tatum | Pts+Asts | under | 0.2451279480496665 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975925 | prizepicks | Jayson Tatum | Pts+Rebs | under | 0.2442060163021608 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|42146f8c-0bc9-4c59-a2ef-76465251a014 | underdog | Garrett Mitchell | Runs | over | 0.2392967841921734 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|a9daa4e2-d391-4a56-8887-122069b1a6f8 | underdog | Felix Correia | Shots Attempted | under | 0.2388358806476083 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| prizepicks|15489684 | prizepicks | Jahan Dotson | Rec Targets | under | 0.2376385063381021 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|b5ceac39-f9dc-4159-9c6e-925813dba47e | underdog | Jake Bauers | Runs | over | 0.2362096138691884 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|626bcaa0-990f-459a-a407-9d234ed5dcbf | underdog | Kyle Tucker | Runs | over | 0.2345956145487672 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|79ac5ed9-8acd-47c3-abc9-f18a0272e653 | underdog | Jahmyr Gibbs | Receptions | under | 0.2341401940396219 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15489683 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.2335274669306117 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|4e4b2337-9bf3-4256-877e-50f933d65694 | underdog | Nick Folk | Kicking Points | under | 0.2320321233110344 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| prizepicks|15449911 | prizepicks | Michael Wilson | Rec Yards | under | 0.231695503206471 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|c92f9fe2-c6b1-42a6-b3fd-ce6f5508c02c | underdog | Jackson Chourio | Runs | over | 0.231060606060606 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|dc4b4422-e58a-499b-bb63-8deea069d91c | underdog | Sam Darnold | Completions | under | 0.2263108017814826 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15449901 | prizepicks | Mike Evans | Rec Yards | under | 0.2258028888845463 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|92464fde-118a-4129-a509-887930284223 | underdog | Kyren Williams | Rush Yards | under | 0.224502888663667 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|ce126fc7-7f6f-409b-9dc5-707826f71ef8 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2221856720995597 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| prizepicks|15533059 | prizepicks | Courtland Sutton | Rec Targets | under | 0.2212171503289755 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|e0b41f92-108b-4fbe-bd5a-9c70bdf2dbc9 | underdog | Aaron Donald | Sacks | under | 0.2211009174311926 | 2026-10-10T05:51:08Z | 2026-10-13T00:15:00Z |
| underdog|75d217fd-efc9-4ada-8851-73e19b817338 | underdog | Mike Evans | Receptions | under | 0.2168016992318034 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|e4cf2801-9fda-427b-9a6d-4c20e0a89562 | underdog | Jared Goff | Pass Attempts | under | 0.2167256153544267 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|0b8475a8-56e3-41a5-b351-1754db63f413 | underdog | Andy Pages | Runs | over | 0.2144535240040857 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|a7ec8655-e8a3-48dd-bd43-2cec1d5b6f64 | underdog | Jarran Reed | Sacks | over | 0.2135321139514836 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|e678fca0-b179-4564-8bc6-fb9df7821628 | underdog | Angel Martínez | RBIs | over | 0.210772501771793 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15644267 | prizepicks | Laura Samson | Total Games | over | 0.2081714079033 | 2026-10-11T20:18:47Z | 2026-10-12T05:30:00.000-04:00 |
| underdog|73bcc271-a76e-4002-84fd-adb01d8ce8ba | underdog | Jaxon Smith-Njigba | Receptions | under | 0.2078752692831559 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|6f8e2499-374e-4ba8-a526-e03ec03b1458 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2071827459411265 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|9a19b498-3df9-4bb3-96e1-b03e91ee4b1e | underdog | Teoscar Hernández | Runs | over | 0.2069889702092567 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|76c95021-1b26-4a70-a329-d38002cdd39b | underdog | Jahan Dotson | Receptions | under | 0.2029253788734003 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|d89f2e11-aba0-4fa7-953f-4bd607a20ad7 | underdog | Colby Parkinson | Receptions | under | 0.2028856735476636 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|7ff8ad42-badb-4aec-ac8e-08554c40623d | underdog | José Ramírez | Runs | over | 0.2027957652379485 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|15533053 | prizepicks | Zay Flowers | Rec Targets | under | 0.2016702118631688 | 2026-10-08T06:06:51Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|e941eee4-2a34-44e7-a72c-41d784a6a00a | underdog | Mark Andrews | Receiving Yards | under | 0.1996575311591329 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|7cb544f8-9d57-4984-9cea-a8f3aa1243a1 | underdog | Brayan Rocchio | RBIs | over | 0.1983322064457966 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b8ae61d8-a839-41b2-b71f-4b480b67ab87 | underdog | Taylor Walls | Runs | over | 0.1978573295009145 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|77dcff72-c3aa-4644-963f-7e91cbce939f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.197652652242817 | 2026-10-11T20:18:47Z | 2026-10-11T20:25:00Z |
| underdog|a071749d-f622-4a11-8e39-928b9b5a0126 | underdog | Derrick Barnes | Sacks | over | 0.196744771639426 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|3c232ca9-44d0-4eab-bb9b-d280dd0fda6f | underdog | Zay Flowers | Receptions | under | 0.1960405558292924 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| prizepicks|15449907 | prizepicks | Sam LaPorta | Rec Yards | under | 0.1952754562589411 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|b4389246-2c68-4e06-b877-19b0042440a8 | underdog | Jordan Whittington | Receiving Yards | under | 0.1951541850220265 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|fbca95b0-cd67-44ec-a7f4-24e973b530f5 | underdog | Jared Goff | Rush Yards | over | 0.1947516304227962 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|3165a526-cbe1-4f5b-b406-98c00b47aebc | underdog | Jameson Williams | Receiving Yards | under | 0.1946869283124519 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|732247f0-db3f-4cf3-a2da-052ec0eb1d3d | underdog | Shohei Ohtani | Runs | over | 0.1944300294066771 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|e83c6234-cc83-47d5-a7b8-dfbe3cd1e1e3 | underdog | Drake London | Receptions | under | 0.1933319434009791 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|97f2c7ae-5b0d-4d86-a1ab-ed8e3e064420 | underdog | Liam Hicks | RBIs | over | 0.1914378826782539 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3a6f406e-5e63-4d2e-a6a4-316043910332 | underdog | Jackson Chourio | Total Bases | over | 0.1912842485060322 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|da2d150e-22d0-47c6-9a0d-4b750291ae63 | underdog | Deone Walker | Sacks | over | 0.1905113805902615 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|1f034fea-65f0-4284-b71b-7dda16cb665d | underdog | Cooper Pratt | RBIs | over | 0.1896810549897226 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|1eab050c-610d-4b9f-94be-6ce6a6f57fbd | underdog | Jake Bauers | RBIs | over | 0.18812178173274 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|6ab1f534-39c0-4105-87db-421ec0f32659 | underdog | William Contreras | Runs | over | 0.1868576601522977 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|6a5b3fd9-1b1a-41ce-a0be-1cdfbf5f4961 | underdog | Garrett Mitchell | RBIs | over | 0.1865907653383934 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13975931 | prizepicks | Jayson Tatum | PRA | under | 0.1859948657142129 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|55e860af-c124-43b2-9676-a355ae92a46d | underdog | Kyle Tucker | RBIs | over | 0.1858042977382799 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|8fb9e07e-d089-4217-b9e2-3bff144d7eb5 | underdog | Sam LaPorta | Receptions | under | 0.1848821490777388 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|89db5515-d984-4e98-86ee-0ef155884e7d | underdog | Andy Pages | Total Bases | over | 0.1848739495798319 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|684212b7-4f49-4e54-bcfa-e35adefb36cf | underdog | William Contreras | Total Bases | over | 0.1843023046776688 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|21940918-0e1b-469c-a33d-ebe800fbfd3f | underdog | Christian McCaffrey | Rush Yards | under | 0.1840975522384134 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|c23a382f-af00-491d-a9ec-aa3258c7ad61 | underdog | Matthew Stafford | Pass Attempts | under | 0.1838682559925166 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|5a876cbb-5736-43a5-8e62-cc6bc9623c56 | underdog | Mark Andrews | Receptions | under | 0.1830028846839179 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|10fb776f-4f28-42ab-a6c4-432fc288c563 | underdog | Emanuel Wilson | Rush Yards | under | 0.1783597945324108 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|15451223 | prizepicks | Puka Nacua | Recs | under | 0.1774909016179514 | 2026-10-07T05:55:02Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|61315832-5e54-41b3-9c8b-23ef31024381 | underdog | Jordan Whittington | Receptions | over | 0.1770609074494917 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|57a58b2a-28f0-4759-8f4d-71ece5e13400 | underdog | Christian Yelich | RBIs | over | 0.175599128540305 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|f022c5b7-2fbc-4b91-b0a9-ab1a3c10186f | underdog | Mookie Betts | Runs | over | 0.1752836879432625 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|79bee78a-cb07-4948-810a-ff49cad25363 | underdog | Leonard Williams | Sacks | over | 0.1742919415388009 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|7a684e5b-b8aa-4cb6-b800-fa428c4e3f72 | underdog | George Holani | Rush Yards | under | 0.1734820045881857 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|8d963fd1-f678-4f6b-a084-3cecf8029e01 | underdog | Rashid Shaheed | Receiving Yards | under | 0.1731412065458198 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|15647015 | prizepicks | Susan Bandecchi | Total Games | over | 0.172667535186655 | 2026-10-11T20:18:47Z | 2026-10-12T09:30:00.000-04:00 |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|d8caf820-6627-4db4-9795-41101bfebd24 | underdog | Steven Kwan | Runs | over | 0.1706019649351353 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f2d5a157-6b17-48f8-940f-5996d62b0104 | underdog | Brayan Rocchio | Total Bases | over | 0.1704545454545454 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|257de987-8572-4ae2-a97b-f31577f78b93 | underdog | Andy Pages | Hits | over | 0.1700295405673744 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b31842c4-2a77-419f-b273-bceee9cff63e | underdog | Cameron Thomas | Sacks | over | 0.1692968689112151 | 2026-10-11T20:18:47Z | 2026-10-12T00:20:00Z |
| prizepicks|15533352 | prizepicks | Mike Evans | Rec Targets | under | 0.1687209545206485 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|201033ee-9253-467a-acc3-a68484156ae9 | underdog | Byron Murphy | Sacks | over | 0.1681797067434818 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|024d1cb4-e419-4d42-9d28-d1141624117a | underdog | Jahmyr Gibbs | Rush Yards | under | 0.1671926520706126 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|36afacc2-6921-4af0-a671-a64e783545d0 | underdog | Thorir Johann Helgason | Shots Attempted | under | 0.1671698741728939 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|92f22510-dc51-4fda-8b18-d32036175994 | underdog | Maria Sakkari | Double Faults | under | 0.164647319649402 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|761d6075-42b8-4f57-a24b-d2d063bc7c7a | underdog | Zay Flowers | Receiving Yards | under | 0.1642282559499017 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|f93169d4-e999-4dfa-b5b9-270247a194af | underdog | Matthew Stafford | Rush Yards | over | 0.163819340859309 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|f4dc9343-78b1-4b04-ae32-800cb3f165c5 | underdog | Tyler Bass | FG Made | under | 0.1627647580839394 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|d0ca5ba7-8499-4dd0-8ac8-b30b5732b4b9 | underdog | George Kittle | Receiving Yards | under | 0.1627368151166864 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|10bb1e15-c31d-4702-b0f8-efb2213f1cb2 | underdog | Travis Bazzana | RBIs | over | 0.1619855149266913 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3e82546c-560d-4165-8703-c3d04194801d | underdog | Khalil Shakir | Receiving Yards | under | 0.1612483808717202 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|8bde8952-262c-42f7-a5ab-e99e7cc290c7 | underdog | Emanuel Wilson | Receptions | under | 0.1600218879075018 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|1044053c-1bae-4abf-9352-24352b605d52 | underdog | Kyle Pitts | Receiving Yards | under | 0.159115126501148 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|65495953-2560-4fea-b2ca-f2b9b5c1007e | underdog | Clara Tauson | Double Faults | under | 0.158821217399791 | 2026-10-11T20:18:47Z | 2026-10-12T04:10:00Z |
| underdog|c39d19b8-d55c-4e1f-96bb-73af508fac3a | underdog | Jackson Chourio | RBIs | over | 0.158271853935566 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c6a6548d-0d18-40f7-8280-696efe97af8c | underdog | Richie Palacios | RBIs | over | 0.1581699346405227 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15599427 | prizepicks | Dawson Knox | Rec Targets | under | 0.1579834600344047 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|26385af5-fb82-4255-95ed-45999963f208 | underdog | Jon Rowe | Shots on Target | under | 0.157344942085266 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|b393ab9c-a9e9-447a-acae-23182ffaa172 | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.156922399556327 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15529495 | prizepicks | Jaxon Smith-Njigba | Recs | under | 0.156076292320025 | 2026-10-11T05:47:48Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|369afecf-4050-4528-8b4c-c116d3bfdf62 | underdog | Walter Nolen | Sacks | over | 0.1556628679468944 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|5ae4e1d2-506e-4c54-99fc-d80cb488368d | underdog | William Contreras | RBIs | over | 0.1556091030789825 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b1d48b58-67a5-44d9-94c9-dab60c05c9ce | underdog | AJ Barner | Receptions | under | 0.1544988677102636 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|0c34ed10-3383-48d9-bdfd-ce42dc1002f2 | underdog | Jonathan Aranda | RBIs | over | 0.1542598967297762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9ce7af5b-940d-457f-b26e-2002362fb020 | underdog | Justice Hill | Rush + Rec Yards | under | 0.1523107729380006 | 2026-10-10T05:51:08Z | 2026-10-12T00:20:00Z |
| underdog|33eb49a9-471d-423d-821d-1b1bd854ff15 | underdog | Freddie Freeman | RBIs | over | 0.1522643312924642 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15622908 | prizepicks | Ladd McConkey | Rec Targets | under | 0.1520127654694155 | 2026-10-11T05:47:48Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|92966efc-fdb9-4557-94fb-0f8b4590c20c | underdog | Derrick Henry | Rush Yards | under | 0.1517399760136696 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|0c91767e-bca8-45d8-a402-6e295fe5e408 | underdog | Travis Bazzana | Batter Walks | over | 0.150470520453236 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a98ec56f-30c1-47cc-9060-a7454a57443e | underdog | Junior Caminero | Total Bases | over | 0.15046792197542 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b468e304-bd8f-4ac2-b864-b58e2ea62a39 | underdog | Nikola Vlasic | Shots Attempted | under | 0.1494699778257078 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|15449905 | prizepicks | Amon-Ra St. Brown | Rec Yards | under | 0.149099489690797 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|49c172c3-2076-4e31-a0a1-8d9af3151f2e | underdog | Max Muncy | Total Bases | over | 0.1476708640659617 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c1c65ba2-c738-4f13-b4ca-9e1ba5fc4f8f | underdog | Teoscar Hernández | Hits | over | 0.1458015171583357 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|15449773 | prizepicks | Brock Purdy | Rush Yards | under | 0.14569357842741 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|28a6c346-65e6-454a-983a-f8b4a0a30ddb | underdog | Felix Auger-Aliassime | Aces | under | 0.1456145224554161 | 2026-10-11T20:18:47Z | 2026-10-12T04:00:00Z |
| underdog|9b611f51-bd5a-4ecd-bbfa-f2f13bfc765b | underdog | Khalil Shakir | Receptions | under | 0.1451710376003263 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|6de91ef0-d28b-4eb3-b362-934257475f02 | underdog | Rashid Shaheed | Receptions | under | 0.1451412870495274 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|29c881f7-8bca-4e58-9fb4-171396427021 | underdog | Nnamdi Madubuike | Sacks | under | 0.145136186770428 | 2026-10-10T05:51:08Z | 2026-10-12T00:20:00Z |
| underdog|72946955-4551-4e11-9ac7-045cf3a40fdf | underdog | Sam Darnold | Pass Attempts | under | 0.1438475849616487 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15449777 | prizepicks | Jeremiyah Love | Rush Yards | under | 0.1422832017672558 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15533215 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.1421721269280211 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|e4b2c31f-0dd9-4925-9430-2609f8120f12 | underdog | Nathaniel Lowe | RBIs | over | 0.1420708634330925 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ea65ec86-8f7b-441c-abcd-96c4d2875e7a | underdog | Yandy Díaz | Total Bases | over | 0.1417073170731705 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d9d295c7-29d5-42e6-9e36-ce234bd68880 | underdog | Cooper Kupp | Receiving Yards | under | 0.1409129241893112 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|dc36e57e-c99e-4f80-8989-e418fed3d013 | underdog | Kyle Pitts | Receptions | under | 0.1395988502616334 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| prizepicks|15480562 | prizepicks | Derrick Henry | Rush TDs | over | 0.1393538870791815 | 2026-10-11T20:18:47Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|55b09c9a-087e-4eab-b8a5-d94089b562fd | underdog | Teoscar Hernández | RBIs | over | 0.1388353155469837 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|a1d9d7c3-f635-4d7e-a68c-cac07a226bbf | underdog | Jo Adell | RBIs | over | 0.1381966221048577 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|54d0138c-923d-48a0-b27c-a148af1901e5 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1380953900749995 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|d6da0316-149a-485d-95a2-536d46cf977b | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1371894234082811 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|fc71cb20-e7fe-43ee-adcf-cd1f8720d31e | underdog | Mookie Betts | RBIs | over | 0.1366337168476205 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15605200 | prizepicks | Mark Andrews | Recs | under | 0.1361256072935218 | 2026-10-10T05:51:08Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|2f5811a7-79e9-49a1-81a0-32f77b4c9c58 | underdog | Tyler Bass | Kicking Points | under | 0.1358158405639887 | 2026-10-11T20:18:47Z | 2026-10-13T00:15:00Z |
| underdog|0addefb5-46dd-4c15-bee9-da21df8f0b84 | underdog | Cooper Kupp | Receptions | under | 0.1356011554882877 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|43a23ae9-1975-4a13-a3c3-cd928190b275 | underdog | Konata Mumpfield | Receiving Yards | over | 0.1355805680356587 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|78c4eb32-88f6-4489-9456-f5ef5baafb43 | underdog | Shohei Ohtani | RBIs | over | 0.1352506801399144 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|1f83e6d3-6a19-4120-998c-b3ca1718de9f | underdog | Shohei Ohtani | Total Bases | over | 0.1338535414165665 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449779 | prizepicks | Derrick Henry | Rush Yards | under | 0.1337962116634731 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|dbc513e4-003f-4486-8d5f-694c7cb2dc0a | underdog | Jon Rowe | Shots Attempted | under | 0.1333428069065197 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|e89616c7-8b1c-4013-b0fe-a3b920f12d9c | underdog | Garrett Mitchell | Batter Walks | over | 0.1327294808217791 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|1cd6cecc-5d3a-4edd-87a5-a9a82854bf87 | underdog | Junior Caminero | Runs | over | 0.1317122593718339 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|15605203 | prizepicks | Colby Parkinson | Recs | under | 0.131247358061172 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|97ba40d3-4a16-43a4-86a3-56b8321e0ce1 | underdog | Josh Allen | Rush Yards | under | 0.1305140998274795 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|15449902 | prizepicks | George Kittle | Rec Yards | under | 0.1301993571797353 | 2026-10-11T05:47:48Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|b8dcb39a-2ace-4daa-b851-0b89615596c6 | underdog | Liam Hicks | Total Bases | over | 0.1295527714208139 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f426a0da-e685-4536-ad48-93f182cbc7de | underdog | Josh Allen | Pass TDs | under | 0.1285629331990532 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| prizepicks|15494588 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.1276848732716379 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|a1c455e6-5404-463d-99e9-4535b988d0d8 | underdog | Jon Ander Olasagasti | Shots on Target | over | 0.1271010788156282 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|45d391ed-ffb8-4cbf-a155-c5ab78d5b573 | underdog | Dalibor Svrcina | Aces | over | 0.1270396690769569 | 2026-10-11T20:18:47Z | 2026-10-12T06:20:00Z |
| underdog|334aa8d6-75f8-4548-af20-c04ce18f95b0 | underdog | Harrison Mevis | FG Made | under | 0.1267568917612062 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|8fd4f5cc-d9f8-45d5-a597-9dd5909b1e2c | underdog | James Cook | Rush + Rec Yards | under | 0.1255606388412681 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|07fd516b-214c-4096-8f19-ba9a2505c5d6 | underdog | Emanuel Wilson | Rush + Rec Yards | under | 0.1254820974076079 | 2026-10-11T20:18:47Z | 2026-10-11T20:25:00Z |
| underdog|cf582d01-c13e-440a-ade2-f799db46bbd0 | underdog | Harrison Mevis | Kicking Points | under | 0.1254356679868777 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|04b2d9ea-bc53-4e87-a881-72b4f19e963f | underdog | Yandy Díaz | Runs | over | 0.1248479254939796 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|fcd73857-62c2-47c1-845c-aeb23636ac93 | underdog | Jameson Williams | Receptions | under | 0.1239347870102316 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15449913 | prizepicks | Mark Andrews | Rec Yards | under | 0.1238313359249307 | 2026-10-08T06:06:51Z | 2026-10-11T20:20:00.000-04:00 |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|2eb5b6b8-64a4-43d2-83cd-5b79c40609eb | underdog | Chase DeLauter | Total Bases | over | 0.123544051767048 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|387d8619-4484-46a0-8bbf-45010b00e34e | underdog | José Ramírez | RBIs | over | 0.1231774761186525 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|11a9885e-7415-427b-8c77-6bd6ae879ec4 | underdog | Daniil Medvedev | Aces | under | 0.122760307985375 | 2026-10-11T20:18:47Z | 2026-10-12T06:20:00Z |
| prizepicks|15599431 | prizepicks | Khalil Shakir | Rec Targets | under | 0.122300899095646 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15605198 | prizepicks | Mike Evans | Recs | under | 0.12222533688652 | 2026-10-10T05:51:08Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|c01e24f7-4ebe-4609-9fad-5ddd93a634e3 | underdog | Keon Coleman | Receptions | under | 0.1219943369127956 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|28df77fe-6c84-4cee-a1ee-18c7d3b0a090 | underdog | Shohei Ohtani | Hits | over | 0.1219051471829866 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15480028 | prizepicks | Cooper Kupp | Rec Targets | under | 0.1218370483861323 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|af50eeed-3e88-439a-b0a1-c9a64136e2f3 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1212980265375291 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|7a72e68d-e184-4336-9853-cbcd86d8d1aa | underdog | Drake London | Receiving Yards | under | 0.1208786058024502 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|6e5cef1c-3d52-4748-bbb4-14a7077ab89a | underdog | Jake Bates | FG Made | under | 0.1206348633535515 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|4cbfe398-89db-47fd-a922-bb6c6fe5bc2b | underdog | William Contreras | Hits + Runs + RBIs | over | 0.1205330311072093 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|937a5ea9-d159-4685-9eb7-ba36c6ac6e37 | underdog | Jeremiyah Love | Rush + Rec Yards | under | 0.1196443893368688 | 2026-10-11T20:18:47Z | 2026-10-11T20:25:00Z |
| underdog|d39abbd5-18c3-4e54-a4b9-aaf8d5a2184f | underdog | Freddie Freeman | Total Bases | over | 0.1192173839232662 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|0535d0fb-5048-4c93-a64b-96fd1ef5c355 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.116157619856066 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|21856232-7b31-4ae3-8518-9bb63987f66a | underdog | Brayan Rocchio | Runs | over | 0.1155172413793103 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|fca8350c-28e2-44bd-8ed6-3b238251543a | underdog | Christian Yelich | Batter Walks | over | 0.1148853763215743 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|a6f8eaf1-85f1-4fda-8d3c-2b888d7352f5 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.114575137794336 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|78fed814-b601-449c-b395-4b0300fecf23 | underdog | Jake Bauers | Total Bases | over | 0.1143320964749535 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4fa5ef51-cb9d-4386-8e3d-1747d9fc7fa7 | underdog | Angel Martínez | Runs | over | 0.1139984713974954 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f43b99b1-c0c6-4a4c-9e75-4c8afbf1a68c | underdog | Jonathan Aranda | Total Bases | over | 0.1139370078740158 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|abe573f9-1d74-4e1d-b04f-aa980d6ae1da | underdog | Jonny DeLuca | RBIs | over | 0.1139244103438475 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|24cd8df3-de9c-439f-a464-fde46d0c3c56 | underdog | Jared Goff | Pass TDs | under | 0.1129533261839722 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|444b09a8-8831-49b0-a1ef-2c9d83d20e84 | underdog | Cooper Pratt | Runs | over | 0.112777515351913 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|e0371795-229b-4ba8-a826-44b3549c775c | underdog | Will Smith | RBIs | over | 0.1126523389559607 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|bd89c92b-425b-48d5-9228-deb99dfcbb46 | underdog | Teoscar Hernández | Total Bases | over | 0.1120789109367789 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|97b81c66-8c31-43e3-8094-a40cb90242be | underdog | Christian Yelich | Total Bases | over | 0.1120789109367789 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c0bd9a94-cf50-4ce2-b5b3-f9a919d8ec88 | underdog | Yandy Díaz | RBIs | over | 0.111859761320162 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ca593b78-6206-47d9-88e7-ea597bfa44ef | underdog | José Ramírez | Batter Walks | over | 0.1111346765641569 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b5c478c0-f44a-452e-b52e-8ec57b00b1e0 | underdog | Brice Turang | Total Bases | over | 0.1105149752208576 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|f16a5dd7-0a11-4b3c-8573-75b726a574f6 | underdog | Freddie Freeman | Hits | over | 0.1101321850803321 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15576399 | prizepicks | Jared Goff | Pass TDs | under | 0.1084012634435631 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15606273 | prizepicks | Khalil Shakir | Fantasy Score | under | 0.1074900904271655 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|0091e8f0-20c6-49fc-9210-84b8edf70ad8 | underdog | Tyler Allgeier | Rush Yards | under | 0.1073381300159566 | 2026-10-11T20:18:47Z | 2026-10-11T20:25:00Z |
| prizepicks|15533061 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.1072789607453067 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| prizepicks|15605199 | prizepicks | Sam LaPorta | Recs | under | 0.1054567516001454 | 2026-10-10T05:51:08Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|56e7a848-9591-4052-8a7d-2a19200848b2 | underdog | Kyle Tucker | Hits | over | 0.1054360688190638 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|6ef5fd6e-2017-4be4-87d5-2cccaab82a24 | underdog | Brayan Rocchio | Hits | over | 0.105146286744669 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|4f7ccb76-a998-49cd-aade-4ad2e3c9bcfe | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.1045728146988547 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|ce5ae764-f911-47ba-8431-67d5b489200e | underdog | Brian Robinson | Rush Yards | under | 0.1037498664931149 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|f2abe0a4-bf61-4cce-8b6b-383e4bac62b0 | underdog | Tory Horton | Receiving Yards | over | 0.1032629529638766 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2c02128b-c63f-4c7a-93b2-921f656f115e | underdog | Jake Bates | Kicking Points | under | 0.1029821419012476 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|6e9f57c6-06e0-4922-bea7-fa854121d4d1 | underdog | Garrett Mitchell | Hits | over | 0.102916642043505 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b73b684e-50a1-481e-9206-a976600fa14d | underdog | Devontez Walker | Receptions | under | 0.1028513851406096 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|8c888a60-93ed-44d5-b569-d948d9892544 | underdog | William Contreras | Hits | over | 0.102207453183262 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|3a0a5fb4-8fec-4c1c-a4a3-990ec0962635 | underdog | Will Smith | Hits + Runs + RBIs | over | 0.1016822333860878 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4c6863d1-8a63-4019-9eb9-170704f07242 | underdog | Jo Adell | Total Bases | over | 0.1012237762237762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2e1069d1-ff71-466a-ac9a-8bb9bd9ba83d | underdog | Jackson Chourio | Hits | over | 0.1007073520271667 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4241a742-4708-4e8d-b8d9-a67643642c3e | underdog | Tyler Loop | Kicking Points | under | 0.1004524819334912 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|cb7633c9-ce7f-493c-90fe-299fbe2b2a52 | underdog | Travis Bazzana | Runs | over | 0.1004405286343612 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|603e79f6-045e-429d-bd7c-96054c888e7d | underdog | Bijan Robinson | Receptions | under | 0.1002136113334525 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|c16a1553-7ce9-41e3-94dd-35dcba1d50e9 | underdog | Dalton Kincaid | Receptions | under | 0.1001322302115007 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|a48b9cac-5835-4e17-bb94-488f64c2c4f2 | underdog | Yandy Díaz | Batter Walks | under | 0.0997986126650258 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d149922a-7aeb-4f9a-b519-a5c2490f0b89 | underdog | Patrick Bailey | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|c22ae601-6e01-4914-ac59-7455a5c99d05 | underdog | Garrett Mitchell | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|0d9ea553-5342-487d-9e05-dfebe5c8ab46 | underdog | Joey Ortiz | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|49403d31-be54-4fe0-9e8a-d308740d099f | underdog | Taylor Walls | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|23134ad5-b95d-47bc-9b05-45e53638a825 | underdog | Kyle Tucker | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|e388107d-71de-4d5c-9c18-12e453e8029a | underdog | James Cook | Receptions | under | 0.0989680426406112 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|066f0f9e-b6c9-47d2-b540-1f55c52394f5 | underdog | Joey Ortiz | RBIs | over | 0.0981818181818181 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|ce2bec88-2b1e-4517-939c-450ab2860797 | underdog | George Holani | Receptions | under | 0.0972730613848503 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15625124 | prizepicks | Felix Auger-Aliassime | Aces | under | 0.0965569875121911 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|020e3f8c-5c74-4741-abf7-323b92b10dd3 | underdog | Travis Bazzana | Hits | over | 0.0963112448193084 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|07405cba-3d11-4f03-aeeb-2884c179f9eb | underdog | Victor Mesa | Runs | over | 0.0962432915921288 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9b57a37f-f1cc-4ab5-a354-5c3317360da1 | underdog | Joey Ortiz | Hits | over | 0.095720022541028 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|625f44f8-5951-489a-85bb-13cfca832f4a | underdog | Brice Turang | Hits | over | 0.0953584302115455 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|85486ca9-90da-4c1a-be12-ffe17eb113db | underdog | Jo Adell | Hits + Runs + RBIs | over | 0.0949273782322186 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|814b06d9-b8e2-413b-8e3a-9735fe37a96c | underdog | Luis Lara | RBIs | over | 0.0946969696969696 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15639563 | prizepicks | Oronde Gadsden II | Rec Targets | under | 0.0942010817311632 | 2026-10-11T20:18:47Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|17572c88-b308-4c8b-8481-3af931e19c72 | underdog | Derrick Henry | Receiving Yards | over | 0.093917869973369 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|7b6a2d3e-11d3-4977-8e37-59858bf712d2 | underdog | Olamide Zaccheaus | Receptions | under | 0.0930780314349503 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|d2887c8e-fd22-43ae-a674-3fe85ac2a968 | underdog | Ryan Vilade | RBIs | over | 0.0915923945335709 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15629113 | prizepicks | Bianca Andreescu | Total Games | over | 0.0907422736850894 | 2026-10-11T20:18:47Z | 2026-10-13T04:00:00.000-04:00 |
| underdog|e9f69f58-1beb-4de9-8110-0a3d94dada53 | underdog | Victor Mesa | Total Bases | over | 0.0906717017515668 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ce4e9f34-09da-4672-b076-7b7130de1b2a | underdog | Deebo Samuel | Receptions | under | 0.0900977552209125 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|8f2816cf-0628-4963-8b2a-82ea1015aa29 | underdog | George Holani | Rush + Rec Yards | under | 0.0889255157795797 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|4896d960-2c35-4fda-8516-4f82c2063d39 | underdog | Max Muncy | Batter Walks | under | 0.0880119397743733 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|c289248d-cfaa-4879-89cf-3c0ba63b1a52 | underdog | Keinan Davis | Shots on Target | under | 0.0877224402576258 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|04a90fa0-b3af-4119-b9f1-d7460f453a2c | underdog | Rolando Mandragora | Shots Attempted | under | 0.0876597754181294 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|36a18375-6519-4861-9922-a146215318c5 | underdog | Richie Palacios | Batter Walks | over | 0.0875680580762249 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d0975eb0-1c8e-4abe-9bd0-4a67d0b8ba5d | underdog | Arthur Fils | Aces | under | 0.0868225479737846 | 2026-10-11T20:18:47Z | 2026-10-12T07:30:00Z |
| underdog|f845b7de-39c1-4709-a1e1-eb1c7704397a | underdog | Lazar Samardzic | Shots Attempted | under | 0.086336829755912 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| prizepicks|15599430 | prizepicks | Keon Coleman | Rec Targets | under | 0.0857557047580359 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|aadcd931-ec6e-43e9-b71b-ab0f190ab726 | underdog | Casper Ruud | Aces | under | 0.085324442102758 | 2026-10-11T20:18:47Z | 2026-10-12T04:00:00Z |
| underdog|fbae5726-4d6b-41ec-8862-a9660e524256 | underdog | Bijan Robinson | Rush Yards | under | 0.0847525563870223 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| prizepicks|15613937 | prizepicks | Katie Boulter | Total Games Won | over | 0.0846111425773317 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|a694e717-4402-4a5e-a72f-01b4638ef063 | underdog | Cooper Pratt | Hits | over | 0.0844009790834429 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4a47c7eb-a243-405f-a9ab-bcdf5f59a80a | underdog | Brayan Rocchio | Batter Walks | over | 0.0843799058084771 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|60f3cfcb-2cb5-40a3-a23c-05a35349c355 | underdog | AJ Barner | Receiving Yards | under | 0.0843014111798384 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|032f47c3-9f81-4409-bcb3-e481fb4f54ef | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.0838997555676377 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|670067ac-6857-476e-b7c5-4e8ba976c43d | underdog | Kyren Williams | Receptions | under | 0.0831238266239099 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|a20aa99d-df3c-4600-9a81-db6b4d4c1f11 | underdog | Deebo Samuel | Receiving Yards | under | 0.0827051358298942 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|15599423 | prizepicks | Tyler Allgeier | Rec Targets | under | 0.0823902362312282 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|7edf4227-babd-41fb-a4f6-2bc40bd841f0 | underdog | José Ramírez | Hits + Runs + RBIs | over | 0.082199819661831 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0eea8879-eab7-49dc-bebc-1d31e6758886 | underdog | Justice Hill | Rush Yards | under | 0.0819635347472056 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| prizepicks|15480030 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.0819174622423938 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15479810 | prizepicks | Drake London | Rec Yards | under | 0.081908695508628 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|cb65e2e2-83c4-4190-ade2-8ba55c28422a | underdog | Steven Kwan | Hits + Runs + RBIs | over | 0.0818522678804714 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|c1fbe418-a7dd-4fad-8905-aa1fb05b7eda | underdog | Will Smith | Total Bases | over | 0.0816220581449007 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15528722 | prizepicks | Cameron Dicker | Kicking Points | under | 0.0793017527260997 | 2026-10-09T20:57:57Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|296f5ffe-51f4-4765-b95f-3e18d5f4908f | underdog | Brian Robinson | Rush + Rec Yards | under | 0.0789728388728099 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|1ca1212a-2b6b-4a1e-9741-fa06c174f465 | underdog | Kyren Williams | Receiving Yards | over | 0.0780783225296581 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|47f952bd-5a7f-46c5-8a49-584daa01c62b | underdog | Stefanos Tsitsipas | Aces | under | 0.0780333980544074 | 2026-10-11T20:18:47Z | 2026-10-12T05:10:00Z |
| underdog|fca1ebba-1c1d-4e13-a135-0272391ad284 | underdog | Max Muncy | Hits + Runs + RBIs | over | 0.0775241925197955 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|6b765c38-fd1a-406a-8242-b70bc727a95b | underdog | Jasmine Paolini | Double Faults | under | 0.0773776365818569 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|4c9fc4a1-429d-4264-aec8-9b2684e69bc6 | underdog | Will Smith | Hits | over | 0.0771954309658208 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449775 | prizepicks | Jared Goff | Rush Yards | over | 0.0771661766978453 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|f34b8ea9-ff29-4042-8003-a35225c30654 | underdog | Max Muncy | RBIs | over | 0.0767567567567567 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|9ac3e1a2-6bb7-4966-b44e-62a1fd6fc8b6 | underdog | Mookie Betts | Hits + Runs + RBIs | over | 0.0766950942608024 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|67b2e3c8-cd7a-499f-86d9-4342556da29b | underdog | Mookie Betts | Total Bases | over | 0.076545916012921 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|e1cb8a5d-2b65-43f6-b325-a6727f6a7274 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.0761857882288901 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|8976841a-dcac-43f5-afc7-aff9aa7b05ca | underdog | Dalton Kincaid | Receiving Yards | under | 0.0758028403564352 | 2026-10-08T06:06:51Z | 2026-10-13T00:15:00Z |
| underdog|54c982e8-946c-470f-b968-54f7868e2184 | underdog | Giorgi Kochorashvili | Shots Attempted | under | 0.0754168684946894 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|29afb740-d596-462e-b47f-b72432e73649 | underdog | Jake Bauers | Hits | over | 0.0752782170654003 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449904 | prizepicks | Cooper Kupp | Rec Yards | under | 0.075270607297545 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|fafa1873-ee71-4b7a-bd33-ad2b3f8caad1 | underdog | Junior Caminero | RBIs | over | 0.0747467481867769 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|86e7ef31-a47e-4802-a478-10b67e4653eb | underdog | Max Muncy | Hits | over | 0.0746826887155556 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|f5a5c826-fcb2-4f72-b80b-6c57a50af3db | underdog | Sam Darnold | Pass TDs | under | 0.0743427570219392 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|3343bbe8-ffac-430d-aeaa-2c90744f6d0e | underdog | Freddie Freeman | Runs | over | 0.0743119266055046 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|347394ac-81b5-41a9-8fcb-201377429974 | underdog | Bradley Chubb | Sacks | over | 0.0735359375258569 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|0bf383f5-cd90-4375-a60e-b1ff311ede12 | underdog | Bijan Robinson | Receiving Yards | under | 0.0730816046593806 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|bb1faece-9afd-43bb-94ec-2c9ccc581d8b | underdog | Nathaniel Lowe | Batter Walks | over | 0.0729473684210526 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|eff29eb9-994c-46ec-a64d-ebc9f0025f60 | underdog | Junior Caminero | Hits | over | 0.0729261767542962 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|7b70747b-1bc7-479a-81e5-20d0c997f567 | underdog | Chase DeLauter | Runs | over | 0.0728110599078341 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|15639751 | prizepicks | Maria Sakkari | Double Faults | under | 0.0724425765843496 | 2026-10-11T20:18:47Z | 2026-10-12T01:20:00.000-04:00 |
| prizepicks|15619228 | prizepicks | Botic Van de Zandschulp | Total Games Won | over | 0.072356723476244 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|a912b059-e958-47ac-be91-0162a07e1484 | underdog | Andy Pages | Batter Walks | under | 0.0719731231425249 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|faee8069-99b5-4b6c-9e52-2fcd4cad3591 | underdog | Cooper Pratt | Batter Walks | over | 0.0719192559712534 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|328fd5df-b812-4adf-aabf-4121767a3610 | underdog | Matthew Stafford | Pass TDs | under | 0.0718820602819038 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|bf5b8b25-d9c6-4b86-9501-7f1430e1b063 | underdog | Travis Bazzana | Total Bases | over | 0.0718093228573808 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6bb6133b-cc35-4fc1-8762-49af70322fd4 | underdog | Jonathan Aranda | Hits | over | 0.0709511661299276 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|1981b6ed-0ee3-4837-8f27-71f80cee57fe | underdog | Jacoby Brissett | Rush Yards | under | 0.0698168702062143 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|1af97885-a088-40f7-b692-cece11bb1e27 | underdog | Jonny DeLuca | Total Bases | over | 0.0694444444444444 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15618537 | prizepicks | Zizou Bergs | Total Games Won | over | 0.0693889616944337 | 2026-10-11T20:18:47Z | 2026-10-12T06:00:00.000-04:00 |
| prizepicks|15639068 | prizepicks | Tarik Skubal | Batters Faced | under | 0.0691719225255271 | 2026-10-11T20:18:47Z | 2026-10-11T20:00:00.000-04:00 |
| underdog|4cba0a0e-510c-43b6-a377-afd73aa8e80a | underdog | Teoscar Hernández | Batter Walks | over | 0.0687847667950363 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|e0adfb00-4d15-4d74-8a9d-718e0aaafac3 | underdog | Tyler Higbee | Receiving Yards | under | 0.0687363615477286 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|0fd99d6d-9fd0-4696-aba9-2eba54bdb0db | underdog | Kendrick Bourne | Receiving Yards | under | 0.0686022399140668 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|e7e07049-21e8-4b18-ad3b-acc75ddc7862 | underdog | Blake Corum | Receptions | under | 0.0683732979337277 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|6bc2028c-074c-49d5-a899-58eb6add783e | underdog | Derrick Henry | Receptions | over | 0.0681999422383017 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|091284a0-c421-4eb2-971c-b847b809f686 | underdog | Devontez Walker | Receiving Yards | over | 0.0680054026858076 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|6e4e4760-d8c4-4052-84e1-2c4c36eeae36 | underdog | Liam Hicks | Hits | over | 0.067041942489502 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2cff0f32-2cb4-4106-8fed-a599462d2fb1 | underdog | Jo Adell | Hits | over | 0.0667688645081718 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b9852fd1-accf-47b3-a909-cc36f80d0eb4 | underdog | Jeremiyah Love | Rush Yards | under | 0.0667114093441835 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2c2f954b-0aea-4fd7-8b09-e9e332927a12 | underdog | Rashod Bateman | Receptions | under | 0.0664321324928192 | 2026-10-08T06:06:51Z | 2026-10-12T00:20:00Z |
| prizepicks|15533217 | prizepicks | Sam LaPorta | Rec Targets | under | 0.0662345067031578 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13976018 | prizepicks | Shai Gilgeous-Alexander | PRA | under | 0.0657969563767089 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|75596168-01a4-4f6f-81c9-992752bdc9c2 | underdog | Greg Rousseau | Sacks | over | 0.0657344319318249 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|cfed6d3d-871e-46d2-8839-be9b9f360f3c | underdog | Chad Ryland | Kicking Points | under | 0.0635639113992488 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15599460 | prizepicks | Emanuel Wilson | Rec Targets | under | 0.0630636453580861 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|e7d46ae1-92f4-4e4d-a1e3-be5fbcd1743c | underdog | Blake Corum | Rush + Rec Yards | under | 0.0629949724268884 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|99e00560-73c0-4e61-b371-fa655894e83f | underdog | Christian Yelich | Hits | over | 0.0627914611339157 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|e2f95fd1-7f77-41ee-a00f-ee231e084d36 | underdog | Jackson Chourio | Batter Walks | under | 0.0626486578321441 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|583b4eb9-8aae-48fd-b631-3141a5c4b97a | underdog | Jacob Misiorowski | Strikeouts | over | 0.0624775741265951 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|f8005c7b-8fd2-4fb4-b3e2-0c81fa133c49 | underdog | Ryan Vilade | Hits + Runs + RBIs | over | 0.062386362231787 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b469d046-409e-4aa2-9063-36688f962c6b | underdog | Donna Vekic | Double Faults | under | 0.0623577008705229 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|8da8b605-48b2-429a-bbce-4ea985b710b7 | underdog | Patrick Bailey | Batter Walks | over | 0.0621841661987646 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e92cb7d5-f7c8-4696-b089-2c994ccf70f5 | underdog | Jo Adell | Runs | over | 0.0619718309859155 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|23331c7d-6803-44fc-8408-70b0001a8635 | underdog | Angel Martínez | Hits | over | 0.0618390564962869 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|eb27401c-0756-4db9-a064-bcf769396118 | underdog | Brian Robinson | Receptions | over | 0.0612944395217355 | 2026-10-11T20:18:47Z | 2026-10-12T00:20:00Z |
| underdog|e958a43a-d936-4bdc-91eb-2f3bc11ebdd9 | underdog | Keon Coleman | Receiving Yards | under | 0.0612866533143504 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|7c7de086-eae2-4dc3-85f5-4888dd6208ab | underdog | Shohei Ohtani | Batter Walks | over | 0.0612623762376237 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|14bc07cf-0064-4171-838c-fa25c8567a15 | underdog | Chase DeLauter | Batter Walks | over | 0.0612067969020922 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|711ad2e3-3689-47a0-8ab5-f98595bc5429 | underdog | Chase DeLauter | RBIs | over | 0.0608891355284251 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|14336df8-3ab4-4dc1-87fb-e7a6bdd008c0 | underdog | Tyler Higbee | Receptions | under | 0.0606378768913719 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|cd9234b9-8070-488f-8546-e101fbfb4333 | underdog | Will Smith | Runs | over | 0.060377358490566 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|956016f6-b9b6-43ce-a8bc-b83ae1008494 | underdog | Luis Lara | Hits | over | 0.0603661401328439 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b62172d9-c61a-4b28-83ac-aa3c646560d2 | underdog | Jiri Lehecka | Aces | under | 0.0596886030882481 | 2026-10-11T20:18:47Z | 2026-10-12T05:10:00Z |
| underdog|0ef473ec-21b2-4a5e-b9fc-933621de9b1d | underdog | Andy Pages | Hits + Runs + RBIs | over | 0.05891969480564 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|29ff3760-5eff-4af5-944a-6c67a3e04c4b | underdog | Justice Hill | Receptions | under | 0.0586356807308978 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|ce8541ca-1777-414c-bd54-b1e6d73ac0c9 | underdog | Richie Palacios | Total Bases | over | 0.0586311872815423 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f14a1938-7b30-4a5e-8104-80da24175f0b | underdog | Ty Johnson | Receiving Yards | over | 0.0580552741488891 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|ae29e0a0-2c0b-410a-9698-c03bcbbb10de | underdog | Aidan Hutchinson | Sacks | under | 0.0579984274424641 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|a7447cc4-be62-401b-8dc6-12e779135453 | underdog | Dawson Knox | Receptions | under | 0.0577342318788118 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15599432 | prizepicks | Ty Johnson | Rec Targets | under | 0.056772117670328 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|96d44c63-4b21-4387-9460-7b2434936ac2 | underdog | Nathaniel Lowe | Total Bases | over | 0.0563003056903272 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15642500 | prizepicks | Kimberly Birrell | 1st Set Total Games Won | under | 0.0559697284835082 | 2026-10-11T20:18:47Z | 2026-10-12T22:00:00.000-04:00 |
| underdog|27aac917-d404-44a2-8a9e-8ea2f92f66b1 | underdog | Sam Darnold | Rush Yards | under | 0.0559092289903409 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|40958690-9df4-48e8-9fe2-35611d6fdcc8 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.055308759244754 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|ca1b3191-5477-4be6-bfd2-15097e1deb2d | underdog | Brock Purdy | Pass TDs | under | 0.0550959740544247 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|9e58334c-ef9e-4f8f-90bd-bdc34c6a3118 | underdog | Learner Tien | Aces | under | 0.0543865876742459 | 2026-10-11T20:18:47Z | 2026-10-12T04:00:00Z |
| underdog|ab84fc38-8730-45db-b82e-364f3b1aa4fc | underdog | Alim McNeill | Sacks | over | 0.0543797977811563 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15642489 | prizepicks | Zizou Bergs | 1st Set Total Games Won | over | 0.0541026738832632 | 2026-10-11T20:18:47Z | 2026-10-12T06:00:00.000-04:00 |
| underdog|5849120f-e652-488f-898a-b0d89c5c3464 | underdog | Freddie Freeman | Batter Walks | over | 0.0531567277395262 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|4aeb884e-3986-447e-9395-b55c383e23cd | underdog | Jonathan Aranda | Batter Walks | over | 0.0531567277395262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e1cfea09-037e-4b9f-a1b5-6d84e5fb944e | underdog | Tommy Paul | Aces | under | 0.05254203671261 | 2026-10-11T20:18:47Z | 2026-10-12T11:10:00Z |
| underdog|c175237f-5289-42c3-9e9d-60a357ad3d4f | underdog | Janice Tjen | Double Faults | over | 0.0524223044901993 | 2026-10-11T20:18:47Z | 2026-10-12T04:10:00Z |
| underdog|efdd9948-3b4a-477a-b59b-403a51a18b72 | underdog | Davante Adams | Receiving Yards | under | 0.0523788305225944 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|4f778fae-400b-4a23-81b0-06c0d3b8ec34 | underdog | Felix Correia | Shots on Target | under | 0.0522488691093763 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|b568f488-b37f-4d7b-b0f8-3e8c1bbca8cd | underdog | James Cook | Rush Yards | under | 0.052094586678718 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|b9a4c5de-d36b-424b-b103-060f62140753 | underdog | Blake Corum | Rush Yards | under | 0.0519852201387395 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15591673 | prizepicks | Kyren Williams | Rush TDs | under | 0.051964898491767 | 2026-10-09T06:09:55Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15564273 | prizepicks | Tyler Loop | Kicking Points | under | 0.0513949469902661 | 2026-10-11T05:47:48Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|3cf479f1-813b-4cff-b200-9f1bb47489e2 | underdog | Jeremiyah Love | Receiving Yards | under | 0.0512744398137398 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|bdd55feb-7967-47fe-b5b8-d7fbc2c79f9f | underdog | Angel Martínez | Total Bases | over | 0.0512241635583474 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ad15f125-9801-442c-8cfa-85327aed08f8 | underdog | Luis Lara | Total Bases | over | 0.0512241635583474 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15641961 | prizepicks | Janice Tjen | Total Games Won | under | 0.0508744023196168 | 2026-10-11T20:18:47Z | 2026-10-12T00:10:00.000-04:00 |
| underdog|bbd56793-88ff-4803-9675-19125cd2b287 | underdog | Joey Ortiz | Batter Walks | over | 0.0507256894049346 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|d454eccc-c68c-42bd-9543-0bb105a16865 | underdog | Davante Adams | Receptions | under | 0.0502337858941952 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|1b390482-7e2c-4b80-be39-258f4de29c17 | underdog | Kaelon Black | Rush Yards | under | 0.048637576309925 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2721c51f-a2c4-4863-b998-18ec650c98a3 | underdog | Jahan Dotson | Receiving Yards | under | 0.0484092199009141 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|fa7b6eda-05a1-46dc-80a7-04b2c5238dbf | underdog | Mookie Betts | Hits | over | 0.0481741767062777 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b1e0a846-63ea-4ad1-9ad7-096f48f376c7 | underdog | Chase DeLauter | Hits | over | 0.0481342569823664 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b8c7b8fb-790e-42b4-bd45-e84ca3d5af98 | underdog | Konata Mumpfield | Receptions | under | 0.0479771065940467 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|9bd809ff-4592-4ac2-b7a0-4478d0160eeb | underdog | Tory Horton | Receptions | over | 0.0478458045816117 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|1d16da96-9a43-47fe-baf2-2c8abe4366fd | underdog | Magdalena Frech | Double Faults | under | 0.047745029088223 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|5de42eb0-93d5-4db5-bcd1-7152e453765d | underdog | Mookie Betts | Batter Walks | under | 0.0476661951909476 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|73454e0c-49dc-41e4-9340-87f225f5d79f | underdog | José Ramírez | Hits | over | 0.0476522420101034 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d35b9dc4-6c41-4038-b44a-de5add2f440b | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.0471314024810165 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|5ed26ce5-cb2e-4ea9-b6d4-282bd12c3d65 | underdog | Jurgen Ekkelenkamp | Shots on Target | over | 0.0469164885339176 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|15599426 | prizepicks | Justice Hill | Rec Targets | under | 0.0469113281743684 | 2026-10-09T20:57:57Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|1c2662f5-ce99-4a16-a938-0685cbd1d6db | underdog | Kyle Tucker | Batter Walks | over | 0.0466697936210131 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|f2898a31-697f-48e4-810d-a097dfca055d | underdog | Taylor Walls | Batter Walks | under | 0.0461621486985761 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3a9a983a-4b09-4f55-bed9-7480d77410ea | underdog | Shohei Ohtani | Hits + Runs + RBIs | over | 0.0456065050162127 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|b73054a9-cf67-4ff2-9363-9d57a37918e6 | underdog | Thorir Johann Helgason | Shots on Target | over | 0.0450908781515718 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|b95fac47-98db-43ea-83b9-6ece7ce23238 | underdog | William Contreras | Batter Walks | over | 0.0449511016849298 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| prizepicks|15533046 | prizepicks | Jeremiyah Love | Rec Targets | under | 0.0435400686640043 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15599468 | prizepicks | Jordan Whittington | Rec Targets | under | 0.0433033789668447 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15613038 | prizepicks | Qinwen Zheng | Total Games | over | 0.0432704704006529 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|e95fefee-cd88-4bd5-baf7-28271a93235e | underdog | Victor Mesa | Hits | under | 0.0432698196376072 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|09074125-997d-41b7-ba3f-4a86c68b7856 | underdog | Austin Hooper | Receiving Yards | under | 0.0430403916046735 | 2026-10-11T20:18:47Z | 2026-10-12T00:20:00Z |
| underdog|162457f3-f404-42e3-908d-040da9e040e7 | underdog | Pablo Carreno Busta | Aces | under | 0.0429733153805502 | 2026-10-11T20:18:47Z | 2026-10-12T04:00:00Z |
| prizepicks|15616499 | prizepicks | Taylor Fritz | Total Games | over | 0.0429084695618681 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|dd35f75f-2676-4274-a2c9-3414d11fafce | underdog | Brayan Rocchio | Hits + Runs + RBIs | over | 0.0422326601217262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|15d644b5-f4e6-4759-aeb3-da2bb3d271c5 | underdog | George Holani | Receiving Yards | over | 0.0420246508054192 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|13976010 | prizepicks | Shai Gilgeous-Alexander | Pts+Asts | under | 0.0419653653034837 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|002dc6a7-15a2-4ef6-a09e-0658552cc5df | underdog | Emanuel Wilson | Receiving Yards | under | 0.0416189116317229 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|14482dd1-b7ee-4d32-87bb-3808e64e3f80 | underdog | Jo Adell | Batter Walks | over | 0.0414027149321265 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9df866af-d049-4b37-8f85-ff98164c8f61 | underdog | Drew Rasmussen | Strikeouts | under | 0.0412212547329545 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|2ef616d5-cfe3-4f4f-9210-fa1daea97e1e | underdog | Victor Mesa | RBIs | over | 0.0411510882670219 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6dfb9119-17c4-498d-8918-c08c536b7732 | underdog | Nathaniel Lowe | Hits | over | 0.0411136759865278 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|bcfdaef5-d634-4a42-9ddc-78df3c2a8391 | underdog | Cooper Pratt | Total Bases | over | 0.0410718792943881 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|d62b0fb3-49c0-460d-886b-9ba4a8383344 | underdog | Liam Hicks | Runs | over | 0.0407766990291261 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|15ea2bd2-f92c-4bbb-87a5-8835a0d6fc5b | underdog | Akor Adams | Shots Attempted | over | 0.0404757452208421 | 2026-10-09T06:09:55Z | 2026-10-12T16:30:00Z |
| underdog|5dc8f6db-1efa-467f-bf7b-5cae7ee7b20c | underdog | Byron Young | Sacks | under | 0.0404468577306219 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|8c33bf40-585b-403c-ab64-a7e928c0cea9 | underdog | John Yeboah | Shots Attempted | under | 0.0404014016880587 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| prizepicks|15533062 | prizepicks | RJ Harvey | Rec Targets | under | 0.0400924452244398 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|ec7fdc0c-7fe5-4b02-92c5-a7a81b83392a | underdog | Chad Ryland | FG Made | under | 0.0400270549141917 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|bacd7834-5ebd-49b5-9f30-246293086a12 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.0387451286206554 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15616492 | prizepicks | Learner Tien | Total Games | over | 0.0372537289376189 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|6f74877a-8932-4824-b496-80ed746ec3b7 | underdog | Chase DeLauter | Hits + Runs + RBIs | over | 0.0372398714202552 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|55e352ff-542d-48ae-82d1-51e2fbc7bb3e | underdog | Steven Kwan | RBIs | under | 0.0367231638418079 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|72fed86e-b34a-48ea-afc9-10ccacf47696 | underdog | Kendrick Bourne | Receptions | under | 0.0366745274473986 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|028fc641-c103-4113-be54-6486f0b58da3 | underdog | Junior Caminero | Batter Walks | over | 0.0365853658536585 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|fb0e5f42-0ca9-488a-acb0-bf69153f6d5e | underdog | Yandy Díaz | Hits | over | 0.0362411588662526 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|72033b2a-88ef-462c-915f-7f03873851a9 | underdog | Isaac TeSlaa | Receptions | under | 0.036224370427224 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|9006d476-771a-4df3-ac69-ae3700e11bf3 | underdog | José Ramírez | Total Bases | over | 0.0361422497100888 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|be49e7d8-11a5-44f5-9f10-4e5e6083f864 | underdog | Valentin Vacherot | Aces | under | 0.0357802214815206 | 2026-10-11T20:18:47Z | 2026-10-12T11:10:00Z |
| underdog|f5cb8405-576d-4eb2-99aa-534bad82e49d | underdog | Sara Bejlek | Double Faults | under | 0.0349956581607223 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|09e68f40-9982-4964-b331-cc34e2898a56 | underdog | Kaelon Black | Receptions | over | 0.0349648661590343 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15449771 | prizepicks | Omarion Hampton | Rush Yards | under | 0.034376948204944 | 2026-10-11T20:18:47Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|08b7f34d-743d-4468-a2ed-cb3842ebb039 | underdog | Taylor Fritz | Aces | over | 0.034228742384909 | 2026-10-11T20:18:47Z | 2026-10-12T05:10:00Z |
| underdog|16e22518-cd33-4795-a080-bea1605e1503 | underdog | Kyle Tucker | Hits + Runs + RBIs | over | 0.0341468329384453 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15630425 | prizepicks | Alina Charaeva | Total Games | over | 0.0340188199905898 | 2026-10-11T20:18:47Z | 2026-10-13T04:00:00.000-04:00 |
| prizepicks|15599461 | prizepicks | George Holani | Rec Targets | under | 0.033760828349025 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15638899 | prizepicks | Diana Shnaider | Total Games | over | 0.0330180720108165 | 2026-10-11T20:18:47Z | 2026-10-12T22:00:00.000-04:00 |
| underdog|5719d5a0-c81a-4047-af0b-1deda36ce93c | underdog | Taylor Walls | Hits | over | 0.0329688869050202 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15644266 | prizepicks | Laura Samson | 1st Set Total Games | over | 0.0320166574734205 | 2026-10-11T20:18:47Z | 2026-10-12T05:30:00.000-04:00 |
| prizepicks|15614077 | prizepicks | Cristina Bucsa | 1st Set Total Games Won | under | 0.0318910683523252 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|c53992df-422a-4cd6-866b-8530dc77029d | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.0314928070568637 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00Z |
| underdog|1d1906a4-7f37-41af-9e4f-76ba995dcc2c | underdog | Patrick Bailey | Hits | over | 0.0314555918613239 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2b1c6ee3-d12e-43cc-b8c2-418293364af4 | underdog | Ryan Vilade | Total Bases | over | 0.0309195950304287 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15646977 | prizepicks | Felix Auger-Aliassime | Break Points Won | under | 0.0308717793881996 | 2026-10-11T20:18:47Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|1d6754f5-5f74-4ed6-bbd6-bb9c2955cc8b | underdog | Liam Hicks | Batter Walks | over | 0.0307017543859648 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|15489681 | prizepicks | Bijan Robinson | Rec Targets | under | 0.0302836573340071 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|fd595d33-28a4-45b6-99a8-e3d2e5241180 | underdog | Steven Kwan | Total Bases | over | 0.0301365182854783 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|05d27070-b2b7-4dc4-b841-121845c4568f | underdog | Teoscar Hernández | Hits + Runs + RBIs | over | 0.0300105556293196 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
