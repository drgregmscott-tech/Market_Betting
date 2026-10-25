# Pipeline Digest -- 2026-10-25T04:30:24Z

## Run summary
- Ingestion: 30218 rows (PrizePicks OK, Underdog OK)
- Estimation: 30218 rows estimated (from 30218 ingested props)
- CLV logging: 198 newly flagged, 0 newly closed, 771 still open (105365 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|f8a727e6-f7b0-4157-b00b-0e79f18b706f | underdog | Bryce Young | Pass Yards | under | 0.4692307692307692 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd46726c-1a01-433c-aa7f-adfd3cba34d5 | underdog | Deshaun Watson | Pass Yards | under | 0.4656565656565657 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|0e14180e-fbdb-4a03-bd4e-6fde932b009e | underdog | Cam Ward | Pass Yards | under | 0.4641025641025641 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7a5a87ce-ed58-4331-8eca-c965c013a075 | underdog | Aaron Rodgers | Pass Yards | under | 0.4482233502538072 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5669e007-1810-4de9-9feb-ea3d1b56340e | underdog | Jared Goff | Pass Yards | under | 0.4357142857142857 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|520cbedc-2c18-47e2-8d28-495bc32d4e01 | underdog | Brandin Cooks | Receiving Yards | under | 0.42763819095477384 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|026dcf42-9a7e-472d-9b73-8d8bcd162c79 | underdog | Baker Mayfield | Pass Attempts | under | 0.4226130653266332 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|065460d7-1c5c-43d4-8968-bba3d831f322 | underdog | C.J. Stroud | Pass Yards | under | 0.4144451746277202 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|94cf4703-b8cb-447e-a113-b01c2f6e1b18 | underdog | Brice Turang | RBIs | over | 0.41361796098638204 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|d901ce25-9ca6-4d08-a605-d775897a85aa | underdog | Geno Smith | Pass Yards | under | 0.4090737399477504 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1eb3cc78-3cfa-4153-87dd-b9095b038836 | underdog | Deshaun Watson | Pass Attempts | under | 0.4087275591164793 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e1ed7c34-5984-4d1d-b0f0-10d131ce332c | underdog | Brock Purdy | Pass Attempts | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a9cf004e-d670-4772-b852-e468757750fc | underdog | Tyler Huntley | Pass Yards | under | 0.4 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|d424e459-1d04-4391-92fb-b90d20c159d8 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cdb5e111-4cf9-4bfd-82c6-27b11ce762fc | underdog | Eddy Pineiro | FG Made | under | 0.3955537623462751 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e3084a60-03df-4043-9baa-8fdd03ce53ce | underdog | Malik Willis | Pass Yards | under | 0.3948522906927716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9693ec51-4551-43f9-853c-0fb05eafd96d | underdog | Daniel Jones | Pass Yards | under | 0.3939654564213076 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5f896a94-190d-4811-9b4b-b1f17ce66f93 | underdog | Jordan Love | Pass Yards | under | 0.3897173199669762 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|643cc8ea-4e4a-4d28-86a8-1e125427f8dd | underdog | Michael Penix | Pass Attempts | under | 0.3727880183899563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8d45849d-0d0c-4b42-a982-ded829882fd0 | underdog | Puka Nacua | Receiving Yards | under | 0.36765433111576884 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|df2d500b-274d-4174-b4d8-d32b5c551962 | underdog | Bo Nix | Pass Yards | under | 0.3619289340101522 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|0085fd80-5781-444c-9416-df3ebc46a0c0 | underdog | Ted Hurst | Receiving Yards | under | 0.35918367346938773 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|4ae8ad3b-3e4b-49b9-a170-e5307e2a5898 | underdog | Brock Purdy | Pass Yards | under | 0.3591836734693877 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aed9e657-4b01-41ed-a960-612d3d02a69a | underdog | Jacoby Brissett | Pass Yards | under | 0.3567731226756141 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a218a657-b6cc-4e53-bfe6-4b64bb11eaa5 | underdog | Tyler Allgeier | Receiving Yards | under | 0.35099657850370225 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| prizepicks|16166603 | prizepicks | Orlando Gill | Goalie Saves | under | 0.35094246505677495 | 2026-10-25T04:41:09Z | 2026-10-25T10:00:00.000-04:00 |
| prizepicks|15944973 | prizepicks | Bo Nix | Pass Yards | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|16039393 | prizepicks | Kyler Murray | Pass+Rush+Rec TDs | under | 0.3509424650567749 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|58412a5e-b36b-488a-949e-91b9df9eb0ea | underdog | Tyler Huntley | Rush Yards | under | 0.3508897080125236 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|67b9076a-4be2-44b7-a2ab-11721c8cbac7 | underdog | Saquon Barkley | Receiving Yards | under | 0.3504068968649158 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|d0517fae-e001-44f5-8e9a-0a74f44ad68b | underdog | Baker Mayfield | Pass Yards | under | 0.3467005076142132 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|86608b58-ef41-4874-b74b-6cb58e689196 | underdog | Bryce Young | Pass Attempts | under | 0.34321350423372066 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e48a70f4-8dc6-4a1a-8915-dffe5495c10b | underdog | Makai Lemon | Receiving Yards | under | 0.34278335770874946 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|37edd000-30ff-4318-96d8-a3ca5e430a8d | underdog | Patrick Mahomes | Pass Yards | under | 0.3421724696477669 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|6671aa81-ba7b-4453-a8b6-fe3bfeee2cc8 | underdog | Eddy Pineiro | Kicking Points | under | 0.33856343461105154 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7a87240b-260e-417a-86ba-70208aa779d5 | underdog | Chris Godwin | Receiving Yards | under | 0.3343434343434344 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16128096 | prizepicks | Brandin Cooks | Rec Targets | under | 0.33414311839178035 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|847b0c28-14bd-4013-973e-05d76c8b982e | underdog | Matthew Stafford | Pass Yards | under | 0.33409895723922944 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|8dc47268-4a7d-404f-9e49-dcd9ba768270 | underdog | Kyler Murray | Pass Yards | under | 0.3335652027540378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4ab4a41a-52fd-4cc5-b31f-ec4b0c82bb82 | underdog | Trey McBride | Receptions | under | 0.3329820296458966 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|79b37311-f15b-4882-b6a3-944e0502707c | underdog | Bo Nix | Pass Attempts | under | 0.3304520785470337 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|3246a459-7d1f-41ff-ba1b-b9c683e7b334 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3268677849268778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|24013bf3-a907-48ae-8533-86d3168e770c | underdog | Tyrone Tracy | Rush Yards | under | 0.3267094468242045 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|0837eb99-3beb-4beb-803a-b6d445424ac1 | underdog | Jordan Love | Pass TDs | under | 0.3243123493621316 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|f0fc31cd-bda5-492c-9fde-68412646daa5 | underdog | Kirk Cousins | Pass Yards | under | 0.3229461067989536 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|863dd3e6-d99d-4172-83c0-14146a4c198a | underdog | Brice Turang | Batter Walks | over | 0.3221462747778537 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|955df2b0-8f9a-4a16-8335-3391b127060c | underdog | Chase Brown | Rush + Rec Yards | under | 0.32063706977042394 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|21ae2dbb-b8cd-47b4-8d9e-617160fee214 | underdog | Jake Elliott | FG Made | under | 0.3198767487193468 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1776f06a-1d54-4810-893f-a6f0b18bce64 | underdog | Joe Burrow | Pass Yards | under | 0.317382759820503 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dbe5c55e-c922-47ce-80a9-02406cd98c80 | underdog | Jalen Royals | Receiving Yards | under | 0.31709006450626964 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|b2ec6ad3-205c-4df4-915c-e02ff73d5ed6 | underdog | Trey McBride | Receiving Yards | under | 0.30725817844859604 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|6778a4ed-0a07-462f-ad67-3327e6b33ee7 | underdog | Tyler Shough | Pass Yards | under | 0.307201308387714 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|82aebfff-cfa1-4d98-b5bd-55154adc923e | underdog | J.K. Dobbins | Rush Yards | under | 0.30471317090038563 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|def3c45d-8dee-47c2-8568-4c3fd9106465 | underdog | Courtland Sutton | Receptions | under | 0.30202251379357925 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|e34970e2-eb5b-4c42-a983-df77a630b08c | underdog | Ja'Marr Chase | Receiving Yards | under | 0.3017403489827723 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e10287d-2f97-493e-ae55-2e6c78479625 | underdog | Tony Pollard | Rush Yards | under | 0.3014201136182672 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b500d66b-e713-4724-a8e6-c64f4c3858a1 | underdog | Aaron Rodgers | Pass Attempts | under | 0.2989717924321307 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|3c6300c9-4b09-4aec-8e6b-9a70d49c3f99 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.2943696215652248 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|c482250b-b72f-437f-a1be-d35070dc0701 | underdog | Daniel Jones | Pass Attempts | under | 0.29431420324174984 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16051310 | prizepicks | George Kittle | Rec Targets | under | 0.2942952711541847 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|e56d19e3-ff75-4054-8e81-a52ef8d30309 | underdog | Kyler Murray | Pass TDs | under | 0.2942390154326902 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|586acb89-828d-495a-b781-835f3b0cca6b | underdog | Courtland Sutton | Receiving Yards | under | 0.2913478359944116 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|1cb78bf3-5610-4b98-a9c4-2483ad1327b0 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.28954474820641707 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|04a4df3d-c7db-42ac-b930-94951fa9779e | underdog | Brock Bowers | Receiving Yards | under | 0.2882455496564065 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15945775 | prizepicks | Courtland Sutton | Rec Yards | under | 0.2858886737283282 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|739590e9-a831-4e2e-831f-8105a7b0bfa3 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.2856924823941684 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|27afcb09-4472-4907-b73c-9de29d4e33b2 | underdog | George Kittle | Receptions | under | 0.2828324993741664 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1dc224d8-4045-43ec-97c9-959c5e18ba2f | underdog | Tucker Kraft | Receiving Yards | under | 0.2825174713014219 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|bfc42786-335b-419e-8324-7610eae813b6 | underdog | Makai Lemon | Receptions | under | 0.282040857766078 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|20101bac-ad93-4e34-a0df-6c368515e5c9 | underdog | Ted Hurst | Receptions | under | 0.281326472163252 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ed554cdd-6711-4d20-ab5c-3f9edfe1ddf7 | underdog | Jahmyr Gibbs | Receptions | under | 0.2812284582963593 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|17ee8953-2dc9-435f-abb2-1065e9ccb4c1 | underdog | Dak Prescott | Pass Yards | under | 0.2811881188118813 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|ac9fca16-ff29-46ad-a999-aad384676c5f | underdog | Brandin Cooks | Receptions | under | 0.2793271159273394 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e05823a2-4f3a-4f97-8e09-a2063261bd71 | underdog | J.J. McCarthy | Pass Yards | under | 0.2792251388086186 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051230 | prizepicks | Trey McBride | Rec Targets | under | 0.2781956898542684 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|16051256 | prizepicks | Troy Franklin | Rec Targets | under | 0.2765686467453297 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|2ef34ff6-b6af-4c78-88e6-b43e09e6eba7 | underdog | Jaylen Wright | Rush Yards | under | 0.2759048149626352 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|00c9927f-5ade-43b4-b9b7-fefb63611a2d | underdog | Malik Willis | Pass Attempts | under | 0.2754400964710172 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9ddcab10-fb85-439b-ac4a-8b192bac7679 | underdog | Cam Ward | Pass Attempts | under | 0.27510005541406 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|a2e72db1-e0c9-49ec-aeee-0a2f7b145f93 | underdog | Cade Otton | Receiving Yards | under | 0.2738237354408446 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e975f741-7c02-4bd6-ad98-eede89cbef4a | underdog | Nico Collins | Receiving Yards | under | 0.2731951910841539 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2dbfa5ca-83df-4571-bbcf-8a84842d2649 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.27223836748338215 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|9324ecc4-fa13-4053-a657-df19163a720b | underdog | Jared Goff | Pass Attempts | under | 0.2687730655877962 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ad87b775-bfc9-4f54-95ee-ff5ed677e61f | underdog | Ja'Marr Chase | Receptions | under | 0.2661038820739 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15956871 | prizepicks | Daniel Jones | Pass Attempts | under | 0.2638857049460724 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|96c40cdc-691c-48db-89d3-4c55dbb29290 | underdog | Sam Darnold | Pass Yards | under | 0.2626055914367695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0e69f33d-bd78-42a8-bec9-9fba13cd8b7d | underdog | Sean Tucker | Receiving Yards | over | 0.26216865530539846 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|73395da4-8892-4961-b521-7e1248b8f7cf | underdog | Bo Nix | Rush Yards | under | 0.2605581005357792 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|7f9ff427-eeca-41d9-b667-16c9f1fc8e5d | underdog | Tony Pollard | Rush + Rec Yards | under | 0.2596998817408331 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2ca7cc4-8309-462a-93ef-879c52f609b7 | underdog | Bryce Young | Rush Yards | under | 0.2592736328532177 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c1c0ffd9-df31-4816-86e7-59f57eb89f4c | underdog | Sione Vaki | Receiving Yards | over | 0.2588272369464025 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|672c91b2-8aeb-400f-a8f4-81ff00601d2f | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2573371918577716 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|bb92d3d3-e3fa-40d3-8c32-40276e0a1d10 | underdog | Jordan Love | Pass Attempts | under | 0.25682947172423143 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|e1b7cf41-ad39-43bd-9dcd-840aab138a0e | underdog | Jake Bauers | Batter Walks | over | 0.256043956043956 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|183dc84a-07dd-44fe-9baa-6b50e2dab0f0 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2554746786082785 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|09bee2cd-e008-407b-87a5-2ef9740a5f75 | underdog | Malik Willis | Pass TDs | under | 0.2548170435450879 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7594b837-9c0a-4a5e-a07c-cb03792bcec9 | underdog | Rico Dowdle | Rush Yards | under | 0.2523393133447593 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|047c7173-2580-4f0e-bee6-72ae14ca159a | underdog | Jauan Jennings | Receiving Yards | under | 0.25118382646039095 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|5af0ef77-d433-4c51-983a-71cce8152bf7 | underdog | Brice Turang | Runs | over | 0.2503282613732908 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9827d4a6-1c80-4f8e-837a-59a7a4efad92 | underdog | Wil Lutz | FG Made | under | 0.2495510531033402 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a7d67cf1-2deb-4409-a28f-186fdbd101d0 | underdog | Malik Washington | Receiving Yards | under | 0.246141552704973 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|41359dbd-8223-40ba-b01b-d548d0fd476b | underdog | George Kittle | Receiving Yards | under | 0.2453249563886891 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051276 | prizepicks | Brock Bowers | Rec Targets | under | 0.24528945408523 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|648dee62-ca9c-448b-bcfa-499810b73d24 | underdog | Xavier Hutchinson | Receptions | over | 0.2439123066762485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|151d3e83-45f8-463e-8fdc-cd3f943b9d80 | underdog | Matthew Golden | Receptions | under | 0.2412290414387117 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ecc7acd2-6c39-44d8-a974-81e00e0baa3a | underdog | Keion White | Sacks | over | 0.24049556544177875 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|4cfc595f-ace4-4eec-a562-9a61b88991da | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.240025789607406 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|4372c2a4-e3a0-4193-97f2-9579fd48f8c2 | underdog | Joe Burrow | Pass Attempts | under | 0.2397570360617678 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cf9de8cc-9bb6-4aac-9635-ec94d6cbf61e | underdog | Woody Marks | Rush + Rec Yards | under | 0.23942161082921087 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|5c474bdc-04d7-47e0-867b-bcfee2a049ab | underdog | Baker Mayfield | Pass TDs | under | 0.2393581560012833 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|298e8d38-ac96-403f-9f7e-d6a0bf21ada9 | underdog | Nick Emmanwori | Sacks | over | 0.23869466592176167 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|1713fb00-7c86-4fb8-b9db-c0d3cd103304 | underdog | Cade Otton | Receptions | under | 0.2373958346481726 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ea96d4e7-d343-4032-ac48-3c5395f7363e | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.23477237529212425 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|86147115-576f-4689-8d0b-2666f24dde83 | underdog | J.J. McCarthy | Pass Attempts | under | 0.23225840306780554 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|193c6a4c-aa4a-46b0-a869-9e9de2826135 | underdog | Bo Nix | Pass TDs | under | 0.2300413174167165 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|c8b9c55e-5d0a-43b5-b56b-8109af36dd93 | underdog | Alim McNeill | Sacks | over | 0.22966902910771664 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|7caf365c-b8e0-4138-9f38-48f4d8c2e085 | underdog | Jordan Watkins | Receptions | under | 0.22923645637992762 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|24df7a00-2988-4b67-b4ea-8506cca6af03 | underdog | Patrick Mahomes | Pass Attempts | under | 0.22838649764287888 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|17c2adf9-75e8-44b7-9e46-b0a6769151cf | underdog | Germie Bernard | Receiving Yards | under | 0.2275384159492459 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|e4c964b1-0b2b-4857-acae-59f009c1792e | underdog | J.J. McCarthy | Pass TDs | under | 0.2273642896866348 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|88ddddd3-918c-4785-9b4f-fdc9f6fb9182 | underdog | Xavier Worthy | Receiving Yards | under | 0.2257113356958771 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|7b942506-88d8-4b68-9738-5f5bcc969d45 | underdog | Christian Yelich | Runs | over | 0.22539996701303 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9e7d3aa0-a238-4f90-a8fb-36975cd5c3d1 | underdog | Javonte Williams | Rush Yards | under | 0.22420942315544656 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|f9352960-e46a-4bd0-887d-6b56e268fcec | underdog | Dak Prescott | Pass Attempts | under | 0.22420131322413994 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|fffb1fba-28a8-466b-81b1-c04af461a000 | underdog | Darius Cooper | Receptions | under | 0.22382965160242474 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|bf1d95e3-f10c-4550-8a39-10f875aed153 | underdog | C.J. Stroud | Pass Attempts | under | 0.2210784579055988 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5b90486b-c32a-4e28-812e-3e86cebac5aa | underdog | KC Concepcion | Receiving Yards | under | 0.2207706046563152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0d5dbe4-9388-4622-8cc6-c162a5b0639f | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2206178911560523 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d9f8055e-799a-4e34-b09f-950d09443ddf | underdog | Kirk Cousins | Pass Attempts | under | 0.2206170397617192 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|67360a01-9b6c-445e-b346-4386fec6404b | underdog | Josh Downs | Receiving Yards | under | 0.22055561241605925 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|eb1b1fd9-3046-4288-a213-e4a77e45136e | underdog | Jacoby Brissett | Pass Attempts | under | 0.22019670734246832 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|dd981eb9-f019-43eb-8014-51c7e7f60995 | underdog | Marvin Harrison | Receiving Yards | under | 0.2201873079173418 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|4938e844-0f10-48db-8ce4-f416888b7caf | underdog | Ian Thomas | Receiving Yards | over | 0.2199241073605816 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|56656c9d-ec82-4d22-befd-cf88edbd6a09 | underdog | C.J. Stroud | Pass TDs | under | 0.21922023288096 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c9dd882b-334e-4169-b37c-b296bb877d16 | underdog | Tyler Loop | FG Made | under | 0.2188399052787495 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bd162112-7e8b-4a7f-a074-95237599ba0d | underdog | Darius Cooper | Receiving Yards | under | 0.217515251017403 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|a63cc8a0-36cc-4002-9d0a-9275fc20e5e3 | underdog | Devin Singletary | Rush Yards | under | 0.217094503944824 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7dbfe9c7-e77c-46aa-8f0d-da3c00ff3729 | underdog | Cam Ward | Pass TDs | under | 0.2169355074931716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16039395 | prizepicks | Bo Nix | Pass+Rush+Rec TDs | under | 0.2167665072623288 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|16128087 | prizepicks | Xavier Worthy | Rec Targets | under | 0.214565411971544 | 2026-10-24T04:39:26Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|594d1e60-46f2-4609-bf47-dd61ec27b4f3 | underdog | Geno Smith | Pass Attempts | under | 0.21377937983293482 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|82fdc867-aad8-427f-9856-e3c82f62e9df | underdog | Saquon Barkley | Rush Yards | under | 0.21296609967876423 | 2026-10-24T04:39:26Z | 2026-10-27T00:15:00Z |
| underdog|b5b4cf2d-863c-4b07-8225-e61b4888d5da | underdog | Kenny Gainwell | Rush + Rec Yards | under | 0.2124926916515939 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051257 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.212391920232314 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|80998e29-827a-47a2-ac21-31900ecc9a6c | underdog | Wil Lutz | Kicking Points | under | 0.21088950433211662 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a9df4b24-c600-46b7-a5e9-ec9eb30eeff5 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.2103451992664808 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|a7f2054d-2853-4233-ab2a-9dca7fe8752a | underdog | Garrett Mitchell | Runs | over | 0.20990806945863127 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|b3d36ef2-c5d1-42ce-bdf6-3dcd1e9c4bd1 | underdog | Colby Parkinson | Receiving Yards | under | 0.2087631852016807 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|e4e5c670-0987-4d0a-8a4a-9428d204a893 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2077532646208933 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|6f9d3984-97b3-4d02-8bf0-fab8d7724424 | underdog | Junior Caminero | Total Bases | over | 0.20748771481717976 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|fefdbc7d-cd0a-40d6-863c-1d11a1b58678 | underdog | Jackson Chourio | Runs | over | 0.20663265306122452 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|087d9f60-bdb4-49f5-9784-3ea05603e98e | underdog | Tyler Huntley | Pass Attempts | under | 0.20628205537717625 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|c1d936d4-68f3-4e44-837e-b333d2c4f1a2 | underdog | Jameson Williams | Receiving Yards | under | 0.2060331671729401 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|0dd5a0a8-c37e-4043-a619-b4ab13fcc914 | underdog | Dallas Goedert | Receiving Yards | under | 0.20444155632497307 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|4ce494db-1a02-483c-9b1b-ee9ddf695bd0 | underdog | Woody Marks | Rush Yards | under | 0.2028480523660538 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|10021345-bbed-4a2f-a584-a3e81916b523 | underdog | Daniel Jones | Pass TDs | under | 0.200856388948677 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d1201b90-f3fd-4725-bf4d-a85136a27bf6 | underdog | Jonathan Aranda | RBIs | over | 0.1997668091721726 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|558b8078-9f60-48e8-9dcd-53fa4b90f102 | underdog | Liam Hicks | RBIs | over | 0.1987220135603141 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051270 | prizepicks | Nico Collins | Rec Targets | under | 0.1977937055574494 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|bfc2e148-a21c-4383-a448-5598a14b86aa | underdog | Jonathan Taylor | Rush Yards | under | 0.1969151744354131 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dd2e01e1-9b2b-4090-aa87-6a74f55e0015 | underdog | Troy Franklin | Receptions | under | 0.19440896280038 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|592ee15a-985e-49a7-9223-eb16e977e1b7 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.19376542031955757 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|a906dd3f-c93a-42f2-bd24-eabd6f738d33 | underdog | Derrick Henry | Rush Yards | under | 0.19357559378280897 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|8b92d278-dbd5-418b-b6f4-85464899feec | underdog | Tez Johnson | Receptions | under | 0.19344381194647653 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7cff4e33-d73d-44f1-8d0d-5a5bf4c7277c | underdog | Matthew Golden | Receiving Yards | under | 0.1918683958802021 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ec32d38f-4baa-4dd5-b4ce-84216707909c | underdog | Kyler Murray | Pass Attempts | under | 0.191433222145686 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|fa30225c-a2b8-4007-91b4-6e7775ca4b91 | underdog | Kendre Miller | Rush Yards | under | 0.1907546806271176 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|dc025e40-887a-46b4-a762-450410cad6f3 | underdog | Christian McCaffrey | Rush Yards | under | 0.18980099144679619 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|ee0fd630-668b-45c5-b6f7-9a2833d72609 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.1896770029694203 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a9599a2a-d2a5-4707-b22c-39668c345e29 | underdog | Zay Flowers | Receptions | under | 0.1892743875611844 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c41836db-df10-4158-bf2a-d471ed143dcc | underdog | Chris Godwin | Receptions | under | 0.18927231998376215 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|83d77d5f-8f56-4d65-99e8-b21e59e22d59 | underdog | Jaylen Waddle | Receptions | under | 0.1879932654958955 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|d7de2d90-b7bd-4c83-9b27-12b0d1ba622d | underdog | Demario Davis | Sacks | over | 0.18797271543795124 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|86267553-d29e-4379-94fe-af64970990b8 | underdog | Elic Ayomanor | Receptions | under | 0.187836672850876 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c88c7dcc-4a68-42bb-820d-1bea91c00ef3 | underdog | Adonai Mitchell | Receiving Yards | under | 0.18622570632540836 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|e2f0945f-5958-4cd7-b310-8337022f84ec | underdog | Daniel Carlson | FG Made | under | 0.1857689129268523 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1c65cc1b-d472-4024-abf4-de2531acbd98 | underdog | Rueben Bain | Sacks | over | 0.1854966337408246 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|69170097-9590-4b1c-b393-fe6a547e6eb3 | underdog | Sam LaPorta | Receptions | under | 0.1854602802656819 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16046139 | prizepicks | Daniel Jones | Pass TDs | under | 0.1853194844296951 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|73e3a771-b2a6-43cd-83d9-5d33eb4aa5d9 | underdog | Kyren Williams | Rush Yards | under | 0.184835086675048 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| prizepicks|16163745 | prizepicks | Zay Flowers | Rec Targets | under | 0.18475278552532493 | 2026-10-25T04:41:09Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|80cda42e-dedd-480a-8e61-235d21eae853 | underdog | Kenny Gainwell | Receptions | under | 0.18440203930446974 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051243 | prizepicks | Denzel Boston | Rec Targets | under | 0.1843661428516428 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|9f05934f-b49e-4994-bd17-9ce1273d9dfe | underdog | Kayshon Boutte | Receiving Yards | over | 0.18201899838674063 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16128102 | prizepicks | Tez Johnson | Rec Targets | under | 0.1819663620320694 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|98e02204-e6fc-49e9-9efb-16eddaa9eb4d | underdog | Jake Elliott | Kicking Points | under | 0.1818784511935599 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|95e13e96-3915-4814-acdb-210d240d4701 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1799180201769094 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ae863eaa-ab5e-4877-8585-dc5472a4473c | underdog | Emmett Johnson | Rush + Rec Yards | over | 0.17980433605544605 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16046140 | prizepicks | J.J. McCarthy | Pass TDs | under | 0.1795941015500882 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|15f3e859-2c6f-4254-abb6-7275ce408513 | underdog | Nico Collins | Receptions | under | 0.1794482585928581 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aa3b84e7-6860-4dc9-aae4-f9e6e23f9731 | underdog | Yandy Díaz | RBIs | over | 0.17817030835205228 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|622aa0a6-52b2-4cfe-a957-7d5769e1b45c | underdog | Jackson Chourio | Total Bases | over | 0.1781277168578399 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16128099 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.17773769702399478 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|4cab8863-5993-4392-aac3-07a608ae52ef | underdog | Jalen Royals | Receptions | under | 0.17724030981279304 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|e61caff8-e55e-44e3-98c4-37563c93f6d5 | underdog | Mark Andrews | Receiving Yards | under | 0.17607211955407587 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| prizepicks|16051241 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.175795415306488 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|8dc8a64b-8a6d-4bbb-9c34-ed8b89025f6b | underdog | Brandon Aubrey | FG Made | under | 0.1756787358146653 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0bfe77e7-f046-485b-9c54-f72737f36efb | underdog | Garrett Wilson | Receptions | under | 0.1755107928461772 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|58600dfe-36a7-46ed-bc53-8334433e51b6 | underdog | Sam LaPorta | Receiving Yards | under | 0.1746918808648834 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a67515c6-0a36-4241-81e0-d3885298e1cc | underdog | Matthew Stafford | Rush Yards | over | 0.1739326192322227 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|90dbb2ba-2f98-4754-84c1-13c9dc6d763f | underdog | Nick Herbig | Sacks | over | 0.173893178426052 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|11e17eff-c3c7-4b31-a4e1-eb3c30ed8c12 | underdog | KC Concepcion | Receptions | under | 0.173856293946127 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051252 | prizepicks | Courtland Sutton | Rec Targets | under | 0.1732814208652097 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|fa22171a-c9bd-41f1-b4fe-854e831bfa35 | underdog | Cooper Pratt | RBIs | over | 0.1730190203422193 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051269 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.1706456696230398 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16128098 | prizepicks | Cade Otton | Rec Targets | under | 0.17054963163974202 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|48d1c90d-f762-462a-82ca-21faf8a02983 | underdog | Jake Bauers | Total Bases | over | 0.17045454545454541 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|db8f2b09-cccf-4e7f-a3e0-6e29fc01c4da | underdog | Jalen Nailor | Receiving Yards | under | 0.17006200858051945 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|49b762ed-4220-4576-ad51-f08750333ea7 | underdog | Austin Hooper | Receiving Yards | over | 0.16966890486115194 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|25c84983-7531-4d73-b90d-493d66582b20 | underdog | Pat Freiermuth | Receiving Yards | under | 0.1693161019733358 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|ee4edd7e-7b6f-41ad-933e-3a50e62080ea | underdog | Bijan Robinson | Receptions | under | 0.1692203598276945 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9356f071-22fc-4b06-8218-7d33d2f4fb9d | underdog | DK Metcalf | Receiving Yards | under | 0.1686306638130101 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|15945781 | prizepicks | Jameson Williams | Rec Yards | under | 0.1684103099885777 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|2fd5f777-f98d-42fc-b079-413f01d2cea6 | underdog | Harold Fannin | Receiving Yards | under | 0.1684065370519358 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4379cc97-6c42-474d-9885-165493109730 | underdog | Denzel Boston | Receiving Yards | under | 0.167016966353541 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a6dc42f2-7deb-4899-978c-a82ddf28cc59 | underdog | Dani Dennis-Sutton | Sacks | over | 0.1668263272094302 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|b2a4ef33-4dd7-4a8d-bebf-9282e819c744 | underdog | Joe Burrow | Pass TDs | under | 0.1668059378425955 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1583ce20-2aed-4825-9210-33ee84203275 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1662215207642232 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bfa74549-a618-4eec-abc1-c188e291e76a | underdog | Yandy Díaz | Runs | over | 0.16545706254981718 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|ef5ac341-4675-41bb-9d48-8088ce627fec | underdog | Jackson Chourio | RBIs | over | 0.16525490608723098 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|b7fc7bc1-d865-4e6d-908b-52a06ee4298b | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.1642276422764228 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c298782a-318d-45aa-85b5-e37cd79f6406 | underdog | Jake Bauers | RBIs | over | 0.16397167617839775 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|4cfd5a4a-1f48-4365-b549-f1ac466a2341 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1626091840811822 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|55a3fca0-4109-4be7-8d0a-087adc34879a | underdog | Cam Skattebo | Receiving Yards | over | 0.16247511944904636 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|be86ddd0-b36e-4ed3-a403-f663d445f402 | underdog | Cameron Heyward | Sacks | over | 0.16167992449726948 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|d207e73d-f7fe-47c6-bdfc-094ce28bfa54 | underdog | Jake Bauers | Runs | over | 0.1612937889533635 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|0c456eba-5929-4f50-8fef-847cb3ef9cee | underdog | Ryan Vilade | RBIs | over | 0.16104271165830672 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|78c65036-bd71-42f0-8897-248434ccea92 | underdog | Quinshon Judkins | Rush Yards | under | 0.16094408862931908 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|88670807-df28-450c-89b9-2d671c6bfd03 | underdog | Ashton Jeanty | Receptions | under | 0.1596415908383356 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3ef8fdc9-08a4-41d9-8d28-99f6c7438824 | underdog | Andre Szmyt | FG Made | under | 0.159326507096576 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f67c5241-e43a-4a2e-be41-be204fb97d1b | underdog | Brandon Dorlus | Sacks | over | 0.15932503910312887 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8840c5dd-55c0-437a-8ec8-fde961e75822 | underdog | Garrett Mitchell | RBIs | over | 0.1591350081699346 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|15959614 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.1587170648523245 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|3627b2cf-8e83-4470-8053-4744b48edbfd | underdog | Xavier Worthy | Receptions | under | 0.1583155139800515 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16051232 | prizepicks | Drake London | Rec Targets | under | 0.1578375470720511 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|a72359e4-c625-4fd5-8791-4fd01e9b8c04 | underdog | Devaughn Vele | Receiving Yards | under | 0.1576991448693823 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|16159362 | prizepicks | Jalen Royals | Rec Targets | under | 0.15767740728466995 | 2026-10-25T04:41:09Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|7f1b9de6-c09a-48a3-a6b1-890d0fcb4f96 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.15729493148797735 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|021764db-4551-4f29-9724-3d4e2d6cd55d | underdog | J.J. McCarthy | Rush Yards | under | 0.1572331357012335 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3182912b-bec7-451d-a4f6-a8aa028c7477 | underdog | Jameson Williams | Receptions | under | 0.1572143332788562 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|04f83a63-96f0-4d32-af9f-f13b23123e60 | underdog | William Contreras | RBIs | over | 0.15694636954899244 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|5860840c-1704-43fe-bab1-1aacb0bf1fa9 | underdog | Romello Height | Sacks | over | 0.15633908831275967 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|7547ee98-5f6f-40d9-93d2-72793c85c4ac | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.1560786062167198 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16167915 | prizepicks | Darius Cooper | Rec Targets | under | 0.1557301912721043 | 2026-10-25T04:41:09Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f134dfbd-611f-47bc-8055-17d94f881094 | underdog | William Contreras | Runs | over | 0.15554086803260625 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|8a310332-5951-4ac7-a77f-6c4a56dd8ed7 | underdog | AJ Barner | Receptions | under | 0.1541940474422654 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|7c562fd8-49b6-44ee-8676-bbf1b6cbac68 | underdog | Bryce Young | Pass TDs | under | 0.1535238626727116 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|37f21c56-5c3a-4702-9320-6b096b6218ef | underdog | Kyle Pitts | Receiving Yards | under | 0.1533697059674438 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c41b9c5a-8eb4-4e28-b530-7467445701da | underdog | Matthew Stafford | Pass TDs | under | 0.1524509996804636 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|edd7e5ed-8207-44e5-a8bf-d2d85af48848 | underdog | Christian Yelich | RBIs | over | 0.15226433129246425 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9b5bac7f-853d-4f8d-b23e-638437b1afdb | underdog | Evan Engram | Receptions | under | 0.1522431104423216 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|d0e5175c-f995-4f19-992d-d6a7520bd2b7 | underdog | Jordan Addison | Receiving Yards | under | 0.1520912252614426 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cc956678-f2dc-416c-af59-3565941e17a8 | underdog | Marvin Harrison | Receptions | under | 0.1520330651894664 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f1759cba-b4e9-4603-aad8-c383295e0e2f | underdog | Malik Washington | Receptions | under | 0.1516278474524776 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051264 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1515049144076509 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16167916 | prizepicks | Makai Lemon | Rec Targets | under | 0.15132967939544328 | 2026-10-25T04:41:09Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|b48dee9d-b16b-44f1-b35b-25977a0a5a6e | underdog | Mason Taylor | Receiving Yards | under | 0.1512744658440447 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|40c92b84-7aa2-4a31-ae7b-160596e0c514 | underdog | Isaiah Likely | Receiving Yards | under | 0.1509578137931236 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d43fe0e3-78bc-4ecb-b57f-9caa3fe6a1de | underdog | Ka'imi Fairbairn | FG Made | under | 0.15065512869964737 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|90d57fe3-bd43-4f9e-9ef6-84cef03e6f50 | underdog | Woody Marks | Receiving Yards | under | 0.15053344370246202 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|673c269d-6b8a-43f5-aacc-e89db2daa931 | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1497580213989858 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|3fe03957-f78a-4577-b650-0f54860d6b2e | underdog | Chris Boswell | FG Made | under | 0.1495032069538866 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|8078eb4f-a1a8-4ed9-9052-abf9aeff0b47 | underdog | Maliek Collins | Sacks | over | 0.1491187094341877 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|1fb7951e-4784-4d46-b66e-0e4b56243186 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.14908491831684723 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|eb118ae3-88ec-4af1-a4d5-238969093a3c | underdog | Greg Dulcich | Receptions | under | 0.148738688298966 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aa0b7a3e-d2b1-4670-bacd-e7f0265e9da6 | underdog | Kaelon Black | Rush Yards | under | 0.1484179947276228 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|64323c38-703e-4295-ab01-28c0d3237f3d | underdog | Tyler Goodson | Receiving Yards | over | 0.14839819250235148 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|8e6bce48-c270-48c4-af74-f023a926fd3c | underdog | Trey Smack | Kicking Points | under | 0.1479856099025124 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|cbdf6397-eda3-42b8-8e11-2e87240b78f5 | underdog | Lukas Van Ness | Sacks | over | 0.1479299343980902 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|894876c7-692d-4cf5-95c3-4b0632db54a3 | underdog | Mason Taylor | Receptions | under | 0.1475775689463663 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c14609ad-2239-49ea-85de-1e3db95fb733 | underdog | Tez Johnson | Receiving Yards | under | 0.14757641917703346 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|968ff81d-59d7-4800-83ce-cfa34ff971b7 | underdog | Dak Prescott | Pass TDs | under | 0.1473394026606165 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|3dcd92ab-0c27-4d63-9fb5-575d5f92cffd | underdog | Garrett Wilson | Receiving Yards | under | 0.1471362850852574 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|1ae5d24c-6f16-4cc5-8989-4a8e6240c971 | underdog | Tyler Shough | Pass Attempts | under | 0.1469924013389894 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|9e7823b5-6ba8-4931-8647-93f4834676fa | underdog | Tucker Kraft | Receptions | under | 0.14624892899467 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|359ed06b-9344-42b7-a543-df0895950a41 | underdog | Samaje Perine | Receptions | under | 0.1460568513705 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|9fb64b31-fb4e-4775-8815-fd8a63623c12 | underdog | George Pickens | Receiving Yards | under | 0.1449746054605076 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|8ed91643-9bf1-48d6-8c60-bf30efa41d98 | underdog | David Hamilton | Total Bases | over | 0.1449020592667002 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|31dad224-5bc7-4e6f-b703-f0f2543dbbd8 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1446776712141652 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|6f6d00d7-38cc-4885-97b4-d1c12e4f2660 | underdog | Sam Williams | Sacks | over | 0.14422589886109222 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|e16c9202-3bcd-44e4-a10c-85115a9f9fb2 | underdog | Junior Caminero | Runs | over | 0.1440400331209275 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051233 | prizepicks | Jahan Dotson | Rec Targets | under | 0.1439163357553819 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|39512b8d-dd2c-4104-92e8-1dcfc8ff0331 | underdog | Jalen Brooks | Receptions | under | 0.1437414270624527 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|8249186f-8862-4abc-9a48-7f8b007560fd | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1436257422239731 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3a21ad77-2638-4099-ae84-863dd656a054 | underdog | Chris Olave | Receptions | under | 0.1432171019256236 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|4323651e-7d75-43e1-8bec-e7432a7af8de | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.1426846691132519 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|f06599db-6e94-41c7-b4e8-7df338f7a276 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.1424277006620714 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|75017fcb-3953-4cb7-b182-7145bd12f5ca | underdog | RJ Harvey | Rush Yards | under | 0.141851915435678 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a44b2e7b-3b72-4501-9872-4e4fd70ab6bf | underdog | Christian Watson | Receiving Yards | under | 0.14179501125685845 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|7d5acb95-0afa-4e4f-9047-78103de8d00c | underdog | Kyren Williams | Rush + Rec Yards | under | 0.1415908950620287 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|e58c86c8-e648-43d4-b9d2-cabbfd06a61d | underdog | Drake London | Receptions | under | 0.1414594528835526 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|edd88ba0-b0bc-4c4b-bab1-6ced4e331af8 | underdog | CJ Donaldson | Receptions | under | 0.14138497062268784 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945777 | prizepicks | Michael Wilson | Rec Yards | under | 0.1412964357388831 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|bcedd6a5-9b12-434f-9ff9-088d92123f8f | underdog | Kirk Cousins | Rush Yards | under | 0.1412416511943182 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|ff359966-c8d3-48b1-9983-24650e564e95 | underdog | Emanuel Wilson | Rush Yards | under | 0.14078081962084332 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|2b6a92ef-28be-4a03-a48f-77aa4938b614 | underdog | Isaiah McGuire | Sacks | over | 0.14052525640947455 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|6332c6d7-e124-410d-b3bd-707008fea706 | underdog | John Franklin-Myers | Sacks | over | 0.14026187076576863 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|7e32077b-6ff8-4003-b1be-f10985089148 | underdog | Caleb Douglas | Receptions | under | 0.1399122387421394 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|9c22489a-921c-4a35-a1f6-ba9e6aee26d3 | underdog | Carnell Tate | Receiving Yards | under | 0.1394857182718097 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0143747-2eae-48ea-a3a6-8fab2c79ffeb | underdog | Michael Wilson | Receiving Yards | under | 0.1390199081777683 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|6e080788-8634-47c3-bd6e-7726cac733b2 | underdog | Rico Dowdle | Receptions | under | 0.1377303975112497 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|d2684865-ed7b-4f14-af16-4087fb0cc715 | underdog | Alex Highsmith | Sacks | over | 0.13763923271087464 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|e2f21f48-43d5-46ad-b8d9-015b430b3708 | underdog | Jahan Dotson | Receptions | under | 0.1371634498538823 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|13caf8a7-8887-4d40-b56b-1caca86e6d79 | underdog | Jauan Jennings | Receptions | under | 0.13615627510133188 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|990e3a36-0fa9-42d5-b447-447c46e0605b | underdog | Germie Bernard | Receptions | under | 0.1357845862590205 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|b20602df-b17c-4bb4-a6c4-1d4091790ae8 | underdog | Jonnu Smith | Receiving Yards | over | 0.1356458877681902 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|a5dc555d-b835-41b2-b481-a747557a08b5 | underdog | Malik Nabers | Receiving Yards | under | 0.1355033403010405 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|575f222c-106d-4acd-bb96-fa38483730e4 | underdog | Jake Ferguson | Receptions | under | 0.1353654788338305 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|16051259 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.1350314279342374 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|734104cf-6077-46fa-89c8-d3578234b36c | underdog | Liam Hicks | Total Bases | over | 0.13474025974025972 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|4c5d5935-5ba3-43f0-966d-8118af67de15 | underdog | Velus Jones Jr. | Receiving Yards | over | 0.13397640039475395 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| underdog|84f62971-2d32-45a7-aa4d-7ab7e3f27a3d | underdog | Malachi Fields | Receiving Yards | under | 0.133936831108967 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c1ee834c-b0aa-4b99-87ba-83f7e96405da | underdog | Dallas Goedert | Receptions | under | 0.13392764460250173 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|75d61aa1-7845-40a4-a1f7-85efdf585c7b | underdog | Princely Umanmielen | Sacks | over | 0.13388692782737888 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7e24c2fc-b2a9-4cda-b16f-b9bc6153a23e | underdog | Greg Dulcich | Receiving Yards | under | 0.1336970921172516 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1c29b99d-222a-4b53-8471-6ed50763c80d | underdog | Jaylen Waddle | Receiving Yards | under | 0.13267795028063345 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|19d3a6a2-1062-45c3-a09a-3a65050bd272 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.13205782499315033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b19f3052-9b2b-4892-9d9c-c814a1c421b8 | underdog | Jake Bates | FG Made | under | 0.1319024702666141 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a49fb210-9a51-4589-b092-bc9895a1ee4a | underdog | Gunnar Helm | Receiving Yards | under | 0.1316121759984837 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d74f82ee-d5f7-40d2-ac36-71cc37b42543 | underdog | Jordan Watkins | Receiving Yards | under | 0.13159640770920988 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ba49f517-710c-4051-95b6-4f8355eef1e7 | underdog | Bucky Irving | Receptions | under | 0.13158399196209436 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|91b4fa0f-a854-402a-8f83-b25bccd153a0 | underdog | Ian Thomas | Receptions | over | 0.1315316679906075 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|443ec428-a877-4631-bdf4-806c0b198809 | underdog | Konata Mumpfield | Receptions | under | 0.1309218799606248 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|362a367a-8287-4a9b-afac-79b549e4c9a2 | underdog | AJ Barner | Receiving Yards | under | 0.1306153642795884 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|4c26d47b-7c8a-4f5c-acd7-dee2e1d7d022 | underdog | Seth McGowan | Receiving Yards | over | 0.13025991601772757 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|d06eefe7-d221-4b8a-847e-dacdc1cae223 | underdog | Tyrone Tracy | Rush + Rec Yards | under | 0.1301385570274678 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|02d34a8f-3eed-4486-9769-1d3795f45afb | underdog | Nick Folk | FG Made | under | 0.1295761284029778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16163743 | prizepicks | Ja'Kobi Lane | Rec Targets | under | 0.12868556161710598 | 2026-10-25T04:41:09Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|7187463b-9887-4a6c-b1db-b77139cd617c | underdog | David Hamilton | Runs | over | 0.12866523265028867 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|0ff74f3e-98f9-4c92-aa08-69ba30d94992 | underdog | Emanuel Wilson | Rush + Rec Yards | under | 0.12861192416867306 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| underdog|59164236-bc6b-417a-89c8-954969435463 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.12843738082128386 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051245 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.1283711896398486 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|fe9a8643-cbb5-455e-917e-c33f3a025f7c | underdog | CeeDee Lamb | Receiving Yards | under | 0.1283347069925714 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0e68c868-6ccc-4fc9-8f71-5f130198661b | underdog | Bam Knight | Rush Yards | under | 0.12777840450237876 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|3f39df10-9e4e-4276-8374-2a207f29486a | underdog | AJ Dillon | Receiving Yards | over | 0.1275276484826307 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|c09b46dc-e720-4c91-8e9e-3a57450fabe0 | underdog | Jonny DeLuca | RBIs | over | 0.1267477455117068 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|39d3e316-5d17-465f-b268-469f78421358 | underdog | Tony Pollard | Receptions | under | 0.1260078504794592 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0a9fbe3d-92db-484b-ba0f-ec618dfa3cd8 | underdog | Noah Gray | Receptions | under | 0.1256611502062177 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|b3bf83ab-c79a-442e-a00a-95213b95e3de | underdog | Jake Ferguson | Receiving Yards | under | 0.1255662633886676 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|9d76b014-0fc4-4360-b3c4-6c3715996d7b | underdog | Carnell Tate | Receptions | under | 0.1254536750854675 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16154947 | prizepicks | Karen Khachanov | Total Games Won | over | 0.1250905288721501 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| underdog|ec0e0e84-de77-43fa-a77c-e85718c6f1e3 | underdog | Ashton Dulin | Receiving Yards | over | 0.124751622660007 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|64ae0032-0dcd-42ee-951d-5b145e18e874 | underdog | Carson Schwesinger | Sacks | over | 0.12401156184683859 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|90c1dd53-3be2-43de-bf0b-baf6a360086b | underdog | Jerry Jeudy | Receptions | under | 0.1240065201300302 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|b1649b67-9605-4a0c-97f9-386bf9540cab | underdog | Tyler Goodson | Rush Yards | under | 0.12379553104779495 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|eaddf12e-bf09-415a-9908-175b69e1378e | underdog | Joey Slye | FG Made | under | 0.1236431134007916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|61e7bf09-5421-4218-9b7d-53d1a654a3cc | underdog | George Pickens | Receptions | under | 0.1233908843202937 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|15945770 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1232415700497886 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|bd7409fb-5432-4e66-a7f5-17c61264dc73 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.1231584316522158 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|015228e2-4b01-423b-bc13-815d3bcc4b3a | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.12280849617456358 | 2026-10-23T13:31:04Z | 2026-10-26T00:20:00Z |
| underdog|5f0a713d-10ba-4d56-b2ce-de883b78fc28 | underdog | Josaiah Stewart | Sacks | over | 0.12275171418382164 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|b7d388c9-2969-4da4-84b2-a88fc3353074 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1227092709671912 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|5e206181-9207-4bfc-88c8-f03aab0fb4c2 | underdog | Kenny Gainwell | Rush Yards | under | 0.12235820841958012 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|8248b0a4-7bbb-45f0-bb6b-f4afa7b390e3 | underdog | Tyrone Tracy | Receptions | under | 0.1223478921251329 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|15945069 | prizepicks | Derrick Henry | Rush Yards | under | 0.1220323805962527 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16163741 | prizepicks | Mark Andrews | Rec Targets | under | 0.12144733262783558 | 2026-10-25T04:41:09Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|2208d8d1-a462-4f13-a450-9e199aa06230 | underdog | Leonard Williams | Sacks | over | 0.1209722728248454 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|b4c1532b-82e4-44b9-b6eb-6fed241492bc | underdog | Derick Hall | Sacks | over | 0.12084592824767443 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|e362134a-febb-4a49-91db-9bbff996595b | underdog | MarShawn Lloyd | Receiving Yards | over | 0.12083104520736526 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|3a053953-ec02-4875-bd19-fe66af684bf0 | underdog | Sam Darnold | Pass Attempts | under | 0.12062481839113282 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|47d2239b-9245-4a9f-a3af-efc901f6a31d | underdog | Pierre Strong Jr. | Receiving Yards | over | 0.1200814951903969 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051293 | prizepicks | Devaughn Vele | Rec Targets | under | 0.1192863816858713 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|aec096af-773f-41dd-a4d1-3c329f6e780c | underdog | Zay Flowers | Receiving Yards | under | 0.11888737869410793 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|2b96e389-ec54-4965-a240-5d2e6eb051a0 | underdog | Jason Sanders | Kicking Points | under | 0.1187154660907585 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a04b010f-6f7a-4bca-bf84-a019fdc98cb2 | underdog | Jason Myers | FG Made | under | 0.1186141311795658 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e642bd88-7ada-49a6-bc3e-0426f77a3d02 | underdog | Jared Goff | Rush Yards | over | 0.1184823448445742 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|37c7f3a7-4eea-4ab7-bb95-51317d560802 | underdog | Christian McCaffrey | Receptions | under | 0.1181179607177566 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5a19d403-37ab-402e-958a-f872523cc695 | underdog | Laquon Treadwell | Receptions | under | 0.11729373694819256 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|55fcc996-4490-4c11-90b8-a80c3e2e57e3 | underdog | Patrick Mahomes | Rush Yards | under | 0.11724343659207292 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|bea4dc65-3219-4de0-9721-19a9becb8a7d | underdog | Keenan Allen | Receiving Yards | under | 0.1171946925687916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd0fc4c4-17dc-42fa-9656-b749a1f7d2ea | underdog | Blake Cashman | Sacks | over | 0.11713225592155074 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e2d137a6-5210-4080-803f-61cd321db90a | underdog | Will Kacmarek | Receptions | under | 0.11705680106340244 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|8ac9a780-d1c0-4481-b02d-99d01d5ad8ef | underdog | Bucky Irving | Receiving Yards | under | 0.11641272640515987 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a8389eaa-f9e8-4862-9d49-e0eb14b5dbe3 | underdog | Geno Smith | Pass TDs | under | 0.1162581741290298 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9c77f910-9d88-4206-8b14-80983b0866d8 | underdog | Brice Turang | Total Bases | over | 0.11564318034906274 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|d4109d54-463b-49c4-8d4a-55997cd5a25e | underdog | Jalen Nailor | Receptions | under | 0.11535940257387334 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|43da2b56-6f19-429a-884b-a4c12ba9020c | underdog | Rashid Shaheed | Receiving Yards | under | 0.1151993821374695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1b0fc4dd-38ef-4e17-85a8-e24686ccb9a1 | underdog | Drake London | Receiving Yards | under | 0.1146582581752583 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8694b376-84f2-40a7-9264-ce681e1ddf51 | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.11413440917302492 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|e85445e5-423b-403d-b942-d8c2f9c8c893 | underdog | Baker Mayfield | Rush Yards | under | 0.1140527808285041 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|157bb4f2-7d8e-46e6-bbc2-d96f6ce7d1ef | underdog | Eric Wilson | Sacks | over | 0.11293704759554901 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|85560838-e552-4d85-8d61-33d8f0a1f89e | underdog | Brock Purdy | Pass TDs | under | 0.112816096678015 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dfaea733-2786-4ed5-bdbc-bd92599f6e17 | underdog | Garrett Mitchell | Batter Walks | over | 0.11239573434695388 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|32fc1802-fd8f-4a28-844d-71abcb793adf | underdog | Chase Brown | Rush Yards | under | 0.11231993620023117 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|c4a30c98-3ee5-437f-83ee-cef25c93d92c | underdog | Travis Kelce | Receptions | under | 0.1120341726504789 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| prizepicks|16051278 | prizepicks | Tre Tucker | Rec Targets | under | 0.1120161055590794 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|da6ccd8c-ebd7-47e9-903b-e2b20457ecab | underdog | Andrew Van Ginkel | Sacks | over | 0.11189161774770573 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|fcafb323-e005-4a22-964c-ea114b457bc0 | underdog | Deshaun Watson | Rush Yards | under | 0.1115471354898498 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6127ec28-8bbd-4e0c-b986-02da6b62dec5 | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.11146340703384167 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051309 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.1111545654187005 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|2f03ca60-0a15-44c5-92f4-51e5ced470e7 | underdog | Jalen Coker | Receiving Yards | under | 0.1109302760189151 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051234 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.1104253678764338 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|483ad90e-ed7f-4702-9bf7-ff64d4a23b3e | underdog | Junior Caminero | RBIs | over | 0.11021227768215713 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|5c1d01bf-5469-4fb9-a3ad-d8a4de3206a2 | underdog | Spencer Shrader | FG Made | over | 0.110097123969825 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fd3cde28-3e40-4a1b-aaa9-9f040568556b | underdog | Lil'Jordan Humphrey | Receiving Yards | over | 0.10997888520020416 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|e5b38cbc-f572-4889-9078-613a27696cb0 | underdog | Justice Hill | Receptions | under | 0.1094985811840331 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|947184a5-40f7-4682-b518-d330e95113f6 | underdog | Tyler Loop | Kicking Points | under | 0.10889652574261188 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|3b766a66-0018-4174-9c44-850d7caef285 | underdog | Matthew Stafford | Pass Attempts | under | 0.1082286184366853 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|9cc0c199-3698-4676-a6b5-d337c67ff542 | underdog | Blake Corum | Rush + Rec Yards | under | 0.10809334251465941 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|b01b4479-d0ff-4f0b-aa25-8572040fd5fb | underdog | Logan Hall | Sacks | over | 0.1080312577396586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d3170ace-e4d5-416b-9843-d7b02790428e | underdog | Cooper Pratt | Hits + Runs + RBIs | over | 0.10788202935840085 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|6d3ee215-a9cc-4cf2-9db6-b62f4efe0cd6 | underdog | Ollie Gordon | Rush Yards | under | 0.10743299560358321 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| prizepicks|16051260 | prizepicks | Jameson Williams | Rec Targets | under | 0.1071890637021601 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|be534b7f-cb7f-4f58-972f-5da5fb118673 | underdog | Ashton Jeanty | Rush Yards | under | 0.10705959434188328 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|34f23a90-4bc8-4ade-bdbc-2bcba0fdb26b | underdog | Carl Granderson | Sacks | over | 0.10691804578810366 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|1c4aa9f8-007b-477d-b964-a15c81e0b4e4 | underdog | Brice Turang | Hits | over | 0.10625688600671412 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|0660c889-a4a5-4941-beff-bf58b7b65837 | underdog | Deshaun Watson | Pass TDs | under | 0.1056653767810689 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|32c6a58f-4543-44ab-9513-73e8857d24bb | underdog | DK Metcalf | Receptions | under | 0.1054909425928073 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5549b40f-c25b-4262-aa4b-46e8542b8221 | underdog | Brock Bowers | Receptions | under | 0.1052220927493255 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|65ed8d6f-70cd-4f13-9b37-fff2700d0487 | underdog | Troy Franklin | Receiving Yards | under | 0.1046037934121351 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|6c4f1fe9-524b-4bc2-b0e2-3fd92bd6f5b4 | underdog | Kenny Gainwell | Receiving Yards | under | 0.10426959129297086 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|54680c7c-61e6-4921-be29-813cc4a2f7ce | underdog | Denzel Boston | Receptions | under | 0.1035724114812719 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051244 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.1034529192752869 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|66a12d68-7694-45bf-bff5-0baebc9e9694 | underdog | Brandon Aubrey | Kicking Points | under | 0.1027789805682906 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|820386fd-f6a7-4a4f-b07b-4e867332ff05 | underdog | Tony Pollard | Receiving Yards | under | 0.1020926537605008 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ff61b03d-9f28-44a0-ab24-2363edfd3351 | underdog | Travis Kelce | Receiving Yards | under | 0.101127840693776 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| underdog|2ba18293-80df-437f-949d-1d069957f111 | underdog | Osa Odighizuwa | Sacks | over | 0.10038213277819841 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|66176240-9346-4efb-a506-abe54845d954 | underdog | Daniel Carlson | Kicking Points | under | 0.1001222893209393 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|16051305 | prizepicks | Germie Bernard | Rec Targets | under | 0.0999657351122397 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|01d3fe0d-6df4-4d43-91ed-c5a1aebc74a2 | underdog | Mark Andrews | Receptions | under | 0.0998519844527912 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|d7c45a71-ae34-474c-b8ae-3a9eac5ba5b2 | underdog | Jacob Martin | Sacks | over | 0.09979540886226029 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|23e720da-8343-4c9e-b954-bcd44ed56847 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.09962653784562692 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|01d7bd14-2cea-4655-87f7-1df94b0cfe7e | underdog | Nick Folk | Kicking Points | under | 0.09955642389684627 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c6c5af67-125a-4344-aaab-494edf32c260 | underdog | Sal Frelick | Total Bases | over | 0.09944751381215466 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|6ec5db6a-0ed2-4ecb-8ccc-8f00c140a71d | underdog | Ryan Vilade | Total Bases | over | 0.09944751381215466 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|602ad854-cba6-4aa9-938a-771d9ab27f0d | underdog | Tyler Higbee | Receiving Yards | under | 0.0990552102507815 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3d3c2c05-d629-473e-b0a9-64c5a643642e | underdog | Adin Huntington | Sacks | over | 0.09842241278974956 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|15945774 | prizepicks | Jaylen Waddle | Rec Yards | under | 0.0982250040001608 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|6ad228c0-c3dc-4c91-bb18-20c03f4e606d | underdog | Zach Sieler | Sacks | over | 0.09814553227481387 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|7d98395f-f4ec-4d64-9c69-e4f7cc2131a7 | underdog | Jake Bates | Kicking Points | under | 0.0977903849845823 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|990b66f3-6684-40c9-8049-1221b32612bf | underdog | Brycen Tremayne | Receiving Yards | over | 0.09769308207393057 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|785d8153-ed65-433a-98ff-d1df6189376b | underdog | Kyler Murray | Rush Yards | under | 0.09745252830194728 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051262 | prizepicks | Christian Watson | Rec Targets | under | 0.096747312779029 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16010772 | prizepicks | Brock Bowers | Recs | under | 0.09671057143934203 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|56e0f4b6-c8b5-4080-a302-a23c5afdfed8 | underdog | Christian Watson | Receptions | under | 0.0962434061653429 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|abbe1cc3-5354-4a9a-a9b9-18eb38d2da6d | underdog | Jonah Coleman | Receptions | over | 0.09620559167514198 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|d1654863-f01c-47db-9d4f-a80c3bb9857c | underdog | Marvin Mims Jr. | Receptions | under | 0.0957341704310761 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|ca7aafa2-8aa7-40d7-943b-d0b95afb247d | underdog | Bryce Lance | Receiving Yards | under | 0.09563747315955529 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945789 | prizepicks | Travis Kelce | Rec Yards | under | 0.0956329735871087 | 2026-10-21T04:43:18Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|25ed5f3f-a2de-45eb-b5dc-ebf775b350ce | underdog | Andre Szmyt | Kicking Points | under | 0.0952743873816968 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|894a8dba-d383-40ae-9802-7bb88ff84f45 | underdog | Velus Jones Jr. | Receptions | over | 0.09519448802480579 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| prizepicks|16154936 | prizepicks | Martin Landaluce | Total Games Won | over | 0.09489887458140489 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| underdog|ee06f148-6f88-45e6-8880-02b1b55d5881 | underdog | Tyler Allgeier | Receptions | under | 0.09376242710196492 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|61f4cf0f-c609-4ce9-99ff-1b7e55132d14 | underdog | Caleb Douglas | Receiving Yards | under | 0.0924857504634089 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|280d7041-8b6c-4dd7-8d58-69f9ecb8dc19 | underdog | Felix Anudike-Uzomah | Sacks | over | 0.09223808023020835 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|5274339d-ba71-48fb-85dc-530831db1a8c | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.0920483199829712 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|5e49237b-efd4-43c0-b1c9-1e896f1e1de8 | underdog | Rashod Bateman | Receptions | under | 0.09202654093256402 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|d2968887-1877-4e52-8478-b20b88c59272 | underdog | Kayshon Boutte | Receptions | over | 0.0913518404432818 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c662b147-2a50-4c88-9c7b-ef28c09fba3d | underdog | Daniel Bellinger | Receiving Yards | under | 0.09110150359713487 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| prizepicks|16128101 | prizepicks | Ted Hurst III | Rec Targets | under | 0.09091390080650863 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|0e8858a7-5fb6-4ffd-a010-eddbbedf1bf6 | underdog | Alvin Kamara | Receptions | under | 0.0905814183401232 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|16046141 | prizepicks | Jared Goff | Pass TDs | under | 0.0902817486338214 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|f10e571c-0024-481c-b4a0-9ab2de9ad060 | underdog | Darnell Washington | Receiving Yards | under | 0.090128614048436 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|8d358243-b3a0-4a89-82cc-1a91a9425047 | underdog | AJ Dillon | Rush Yards | under | 0.0899813876772596 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| prizepicks|16051316 | prizepicks | Carnell Tate | Rec Targets | under | 0.0899755364779774 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|245d329e-170d-471b-b37b-153a8bee8e51 | underdog | Jalen Coker | Receptions | under | 0.089640605964081 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b47ee798-25c0-4807-9c5b-f09c8a5f7d8b | underdog | Chandler Simpson | RBIs | under | 0.08933333333333338 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|791fc351-e3f2-4e01-ac2e-95d1dc1a3341 | underdog | Daniel Jones | Rush Yards | under | 0.0893167984596011 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128090 | prizepicks | Jauan Jennings | Rec Targets | under | 0.08921349851248828 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|725eef3f-a47e-463b-a1b6-515523a58827 | underdog | Tyler Huntley | Pass TDs | under | 0.08883680157859586 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|0fcd329c-289f-4be1-8838-071c4e5bc7f5 | underdog | Christian Yelich | Total Bases | over | 0.08882189239332106 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|116be46b-f1d4-4310-8f46-e94563e753fb | underdog | Elijah Higgins | Receptions | under | 0.0886534112656307 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|9ce71a06-1e9a-4326-a70f-555ae960a371 | underdog | Seth McGowan | Rush + Rec Yards | over | 0.0884133246088093 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|b010c44c-10f7-453e-a045-7af6bf464967 | underdog | Tommy Tremble | Receptions | under | 0.0881185917029142 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f4f2e5e9-f798-4f07-a3cd-11e10ef566d1 | underdog | Liam Hicks | Runs | over | 0.08778280542986427 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9113a280-1a8d-4edc-b368-bac99ea17df4 | underdog | Michael Mayer | Receiving Yards | under | 0.0875972794063874 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|b861b575-d1a2-4d0e-9c47-53963708bcd8 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.08636973596976355 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|8022d176-f92f-45ef-b9a8-b960f6f2cddd | underdog | Jacoby Brissett | Rush Yards | over | 0.086207431678947 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|08b907c1-c47c-4a9f-8cf9-b043a2a100b3 | underdog | Cooper Kupp | Receiving Yards | under | 0.086095710674828 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|73b1aafd-baaa-4ff9-97b8-72eee79cadd9 | underdog | Tre Tucker | Receptions | under | 0.0860413061365301 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a8260b4c-a079-4809-a57f-8616228e7d15 | underdog | Bijan Robinson | Rush Yards | under | 0.08591905310287928 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16159145 | prizepicks | Patrick Beach | Goalie Saves | under | 0.08576837518635905 | 2026-10-25T04:41:09Z | 2026-10-25T12:15:00.000-04:00 |
| underdog|68e7b91f-5dde-4f84-a011-bf9c9fa25743 | underdog | Christian Yelich | Batter Walks | over | 0.08569694294228014 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|2d66c2c2-8b03-45a0-a98b-5cfdc6585f75 | underdog | Darnell Washington | Receptions | under | 0.0851684391460022 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|8f3a2cfe-c9df-4006-a6a6-63a41183a051 | underdog | Tyler Allgeier | Rush Yards | under | 0.0846927854836112 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|84d99d91-e7f4-4a28-9faf-3da2729847a0 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.0846102335479987 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|be4cbc1a-8a5d-4c12-8410-2bc6c9858974 | underdog | Sheldon Rankins | Sacks | under | 0.0843381307351941 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|e81bae4e-2725-4195-a6de-1e42407def0f | underdog | AJ Dillon | Receptions | over | 0.0843143156021593 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|18f6b0cb-e0d6-408b-b62d-da4f38218856 | underdog | Byron Murphy | Sacks | over | 0.0842998247988685 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|eebf79c3-7abe-4974-bd5f-23a4867f9e1d | underdog | Bam Knight | Rush + Rec Yards | under | 0.08429768516956038 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|2ed3f6df-ed1b-4990-afb2-3d9e3e1d3077 | underdog | Robert Gasser | Strikeouts | over | 0.08417933441264536 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|16e56b6b-98b0-4ed4-ac88-6e2b0f470ac1 | underdog | Josh Sweat | Sacks | over | 0.08389794004233009 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|bee9315c-e8b7-44c4-909e-7de29b262880 | underdog | William Contreras | Total Bases | over | 0.08386384856973095 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|fa0f28ce-b297-4b31-abea-d5617a1dd43f | underdog | Brock Wright | Receiving Yards | over | 0.08352861013723534 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|ce529d10-3fd4-44c9-b8a1-473def604cb6 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.08352042529822867 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|56f293ed-4635-4cc3-833c-4ed9a375750c | underdog | Tee Higgins | Receiving Yards | under | 0.0834112064258462 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2816aaad-c9d9-4cd5-ad6d-58de25217f97 | underdog | Michael Mayer | Receptions | under | 0.0834003397411226 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|50636f28-b556-4195-9780-5aff7702ef87 | underdog | Malik Willis | Rush Yards | under | 0.0832931322442289 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ccd3866e-e39d-4402-bb01-bbd92ca68ab9 | underdog | Spencer Shrader | Kicking Points | over | 0.08317987244058994 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a85ce77c-0267-4036-8076-22976be21df5 | underdog | Ben Williamson | Hits + Runs + RBIs | over | 0.08317573126892003 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|ba6a7b98-429b-495e-8b9a-c3c97d70ff2e | underdog | Tyjae Spears | Rush + Rec Yards | over | 0.08298512096055805 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c108025d-89e7-4b07-b8f8-5e94bb6f0a5a | underdog | Yandy Díaz | Total Bases | over | 0.0827277252364359 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|0c8acb0c-794e-4cd7-846e-be6600ed7ea8 | underdog | Josh Downs | Receptions | under | 0.0826092082715991 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1b806f20-be44-49e6-8f59-766270beb2b9 | underdog | Jason Myers | Kicking Points | under | 0.0825404894860757 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|ee420202-642a-4ac6-988b-e2cce1adb4b5 | underdog | Isaiah Likely | Receptions | under | 0.0825217515739429 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9b0e46ce-89e4-409d-be84-b67b36c68cc9 | underdog | George Holani | Rush Yards | under | 0.08245430904977002 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|cdbf5446-2666-4953-8fed-2a23abfb628d | underdog | Kenneth Walker III | Rush Yards | under | 0.0822691396401671 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|3b0eb78b-d28f-46ab-8459-886657d5c203 | underdog | Isaac TeSlaa | Receptions | under | 0.0822432608821583 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3fdf958b-4aeb-446f-a872-8228a3fb7690 | underdog | Kendrick Bourne | Receiving Yards | under | 0.0821950618308543 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|8036ad49-3893-40cb-867e-481f601868f7 | underdog | Seth McGowan | Receptions | over | 0.0817194127236972 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|98c8557b-1ef7-4740-bad9-9c76cec26da1 | underdog | Dohnte Meyers | Receiving Yards | over | 0.08147385061303802 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051290 | prizepicks | Jordan Addison | Rec Targets | under | 0.0810609688919091 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|73fdb8c0-cd85-4ead-8b5d-106ec0f6c09a | underdog | Woody Marks | Receptions | under | 0.08057939082420718 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|41308d6a-1585-4bd8-88a3-c4fc5587e979 | underdog | Jason Sanders | FG Made | under | 0.0803782078621125 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e7b42cef-9825-40e6-860f-1e9a984e2a86 | underdog | CJ Donaldson | Rush + Rec Yards | over | 0.08021649795639368 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|bebc2d1d-594c-4873-8647-ae50d361a9e3 | underdog | Liam Hicks | Hits | over | 0.08010396394945907 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|fa91546b-2faf-49cd-aa41-3929b7a7a669 | underdog | Chase McLaughlin | FG Made | under | 0.0799826010276563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128088 | prizepicks | Noah Gray | Rec Targets | under | 0.07986503444913706 | 2026-10-24T04:39:26Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|941b980e-1d81-4ddf-933b-e929a72f893d | underdog | Cooper Pratt | Runs | over | 0.0790784557907846 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|357d1c55-39ca-4e80-8e47-b9b3fb1d91e6 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0783802647011688 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0d25c245-efca-4a13-baed-2eda4672ccf9 | underdog | Mike Gesicki | Receptions | under | 0.0779878372316424 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|cd41b2b9-c7a0-45df-bcc2-de420b13148a | underdog | Bucky Irving | Rush + Rec Yards | under | 0.07790152531371486 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|68435d74-738b-48b2-acb0-659ca57c408d | underdog | Jermaine Johnson | Sacks | under | 0.0775536282277145 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|6f06d48f-cce9-442a-8a93-5cd9c028fdb1 | underdog | Ollie Gordon | Receiving Yards | under | 0.07744253798791922 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|72ffaa76-3ae9-430b-a82c-c5f4fc755ff8 | underdog | Sal Frelick | Batter Walks | over | 0.07697886448404478 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|ff935cb5-cc24-41a6-9a69-b8839cf2a021 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.07694741593561627 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|9a23291c-d740-46d9-b862-79e3ebb3d2a5 | underdog | Derrick Henry | Receptions | over | 0.0769349421556845 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ae9c030c-04dc-4a2e-a6f5-f5732aca2fac | underdog | Cyrus Allen | Receptions | under | 0.07681941958933014 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| prizepicks|16159478 | prizepicks | Jacen Russell-Rowe | Shots | under | 0.07665167648093296 | 2026-10-25T04:41:09Z | 2026-10-25T12:15:00.000-04:00 |
| prizepicks|16051273 | prizepicks | Travis Kelce | Rec Targets | under | 0.0766485815662542 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|6276fdfc-7b83-41ef-8472-22d3a361af67 | underdog | Jonny DeLuca | Total Bases | over | 0.07654591601292104 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|8b0d49ec-a1da-450a-ba93-5bdfbe49135c | underdog | David Hamilton | Batter Walks | over | 0.07591798445456982 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|23cc4a0a-23c5-4e37-98c2-b2ff5ed850aa | underdog | Trey Smack | FG Made | under | 0.0758399666432347 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5df27532-04eb-405c-b458-1cfd5b5b6c3a | underdog | Malik Nabers | Receptions | under | 0.0758087558960143 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d266a85d-a66d-406b-bea5-4b7215c34d91 | underdog | Devaughn Vele | Receptions | under | 0.0757194055785056 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ae60f3a8-a9ed-4acf-b13f-fdc17f7013f9 | underdog | Michael Penix | Pass TDs | under | 0.0756786003884431 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fb29e728-75f8-4029-8ea6-a2bb1473cd2b | underdog | Calais Campbell | Sacks | over | 0.07536283014091988 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8b8afb9a-0acf-4f99-8e56-c50b27995812 | underdog | DeForest Buckner | Sacks | over | 0.07524235100416299 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|b7633e2a-8c11-4ada-8bd1-ddacccbf8dcb | underdog | Kenneth Walker III | Receptions | under | 0.0750174077225467 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|fa6b3d2e-4ca3-4536-8709-91606f82acdb | underdog | Jared Goff | Pass TDs | under | 0.0748246656634097 | 2026-10-22T04:39:42Z | 2026-10-25T20:25:00Z |
| underdog|dfbe2fbb-ed28-4fbb-8781-5bcac4758534 | underdog | Drew Sample | Receptions | under | 0.0745894946131864 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f840b552-3515-4584-9d35-d37fca257b1f | underdog | Chris Olave | Receiving Yards | under | 0.0744110380898498 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|d9a8338f-0c9f-47bf-95ed-3d25faaff51a | underdog | Jordan Whittington | Receptions | under | 0.07435492868539906 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|186e0ace-b3a3-4d78-83c7-1cf9b0fc8393 | underdog | Jahan Dotson | Receiving Yards | under | 0.0741904379865594 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051313 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.0741620403956118 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|0885b289-f09c-45ec-a38b-3b2dd7e57fb6 | underdog | Omar Cooper | Receiving Yards | under | 0.07399316521856691 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|eb10225b-212e-4412-a43b-2257beed9aea | underdog | Nik Bonitto | Sacks | under | 0.07360688298223128 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|455a71ba-1e78-4b27-8f94-d0afeba7b6fa | underdog | Kyren Williams | Receptions | under | 0.07341233571119932 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|27fb02f5-b3f7-4c9b-bf6f-2e51e4336088 | underdog | Austin Hooper | Receptions | over | 0.07334873265912745 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|6664dbee-84f6-4192-97a8-e1086c85f73b | underdog | Chase McLaughlin | Kicking Points | under | 0.0730635220054324 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e26442d1-e193-41a1-b88c-71f0f33d3168 | underdog | Evan McPherson | FG Made | under | 0.0722696105068416 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5e85e82e-19fc-4f4e-9390-bfd8933da1bd | underdog | David Hamilton | Hits | over | 0.0720133292783155 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16047018 | prizepicks | Darnell Washington | Recs | under | 0.07187451637324271 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|a4ff4488-c410-4fb1-93bd-6846607552af | underdog | Jordan Love | Rush Yards | under | 0.071463102847337 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16051261 | prizepicks | Sam LaPorta | Rec Targets | under | 0.0711809713072434 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|a99ebc26-992c-4fe3-8fb1-6e20c3d8df6a | underdog | Chandler Simpson | Total Bases | over | 0.07113477881891483 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|f35869de-fda0-4ff6-8837-90860751c2b9 | underdog | Will Reichard | FG Made | under | 0.071055087750351 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|052ab564-9a0a-4629-83a6-8bb879b4a0d6 | underdog | Kyle Pitts | Receptions | under | 0.0710490294424133 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6836add1-e50e-4ec1-86cc-eac77a9f1a17 | underdog | Kyren Williams | Receiving Yards | under | 0.07083989094132515 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|00946ae8-e51a-4625-8b97-ccea92a33ea1 | underdog | Chris Boswell | Kicking Points | under | 0.0706516180970466 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6eb4ceca-ab6e-4b70-b779-c61fd77dcb3a | underdog | Emmett Johnson | Receiving Yards | over | 0.0704807198097645 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|24312ff1-78a8-4546-a295-0dc2eb910b54 | underdog | Aaron Rodgers | Rush Yards | over | 0.0700844647787815 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|b6b740f6-7ef3-4ea2-9a60-5b7d3258064d | underdog | Maxx Crosby | Sacks | over | 0.06992804715941348 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051306 | prizepicks | Jaylen Warren | Rec Targets | under | 0.0699206862123872 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| prizepicks|16128084 | prizepicks | Josh Downs | Rec Targets | under | 0.06975179944315124 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16051239 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.0694964909576487 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|9f8ce159-b80d-401d-bf13-9146b2ff57c0 | underdog | Quinshon Judkins | Receptions | under | 0.06949508244536684 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|15944963 | prizepicks | Jared Goff | Rush Yards | over | 0.0694248099013491 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16051253 | prizepicks | Evan Engram | Rec Targets | under | 0.0692857795326448 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|f3153d34-fc09-4c41-9bb2-d0ab46ae7892 | underdog | Brycen Tremayne | Receptions | under | 0.06886445546872477 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|abe1f5d9-3690-4b8a-991e-436bd87b5318 | underdog | Evan Engram | Receiving Yards | under | 0.0687422940230393 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|5651ffc5-716f-41ff-a0cf-691e34951f60 | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.06844597515098405 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|e3b4cb15-bd32-41fe-997b-31ef2b3d248e | underdog | Jonathan Taylor | Receptions | under | 0.0674513078149925 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea2dc53f-bd18-4fa7-875b-0d4d97360754 | underdog | Laquon Treadwell | Receiving Yards | under | 0.0671153960295503 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|edd4b43a-975f-4d48-8157-b4bb1ed6ab74 | underdog | Jonathan Aranda | Total Bases | over | 0.0667834973185254 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|70c8977a-374c-48e5-ba23-edc0fdcc3f39 | underdog | Bijan Robinson | Receiving Yards | under | 0.0663650266525974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|06a009bf-c546-4461-b1c4-1bde1ff75c14 | underdog | Blake Corum | Rush Yards | under | 0.0662621531811924 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|1f7419ba-44ed-4d10-8a7a-bc913e247a3b | underdog | Blake Corum | Receptions | over | 0.0657799728513109 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|352ced7e-8dac-418b-9c42-3093c7bff249 | underdog | Dalton Schultz | Receiving Yards | under | 0.0657798179755999 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|523e63f2-cd93-4051-9a92-051064daa5f9 | underdog | Nnamdi Madubuike | Sacks | under | 0.06576300797424106 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|bc5e98e3-a5ce-45a5-90f0-bbacbef40b3c | underdog | Tetairoa McMillan | Receptions | under | 0.0657606101669747 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16152548 | prizepicks | Lilli Tagger | 1st Set Total Games | over | 0.06532227291338599 | 2026-10-25T04:41:09Z | 2026-10-25T23:00:00.000-04:00 |
| prizepicks|16159477 | prizepicks | Casper Tengstedt | Shots | under | 0.06523711929995113 | 2026-10-25T04:41:09Z | 2026-10-25T12:15:00.000-04:00 |
| prizepicks|16166391 | prizepicks | Konstantinos Tzolakis | Goalie Saves | under | 0.06495512016613536 | 2026-10-25T04:41:09Z | 2026-10-25T10:00:00.000-04:00 |
| prizepicks|15945074 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.064833820071657 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|5f2f84f7-bf47-49ac-af38-66f092aa9127 | underdog | Ben Williamson | RBIs | under | 0.06467661691542292 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9df8e03e-f50e-4a07-ae41-0561472e4131 | underdog | Sean Tucker | Receptions | under | 0.06463248954578349 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|15944962 | prizepicks | Jordan Love | Rush Yards | under | 0.0645818534291142 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|69c654d5-7f0d-40ba-b4de-0146a790613e | underdog | Jordan Addison | Receptions | under | 0.0643744310105808 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|65d5841d-46ec-482d-ae00-03b1bb8559b2 | underdog | Calvin Ridley | Receptions | under | 0.06434385244888874 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|80949b99-08c9-47f9-8565-09b998f305cc | underdog | Aaron Jones | Receptions | under | 0.06431549031041361 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|6d1324e3-6f8b-4d06-b6da-b13366604175 | underdog | Mike Washington | Rush + Rec Yards | under | 0.06413848205594719 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|3b5737ba-1952-412e-ac03-a7508837341e | underdog | Jonathan Aranda | Hits | over | 0.06386154448187509 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|c28ead5c-8a19-420f-a474-89ef551e6c5b | underdog | Jonah Coleman | Rush Yards | under | 0.06364468438664261 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|a101b93b-1254-4c52-bbd2-9070ecc0ff48 | underdog | Adam Trautman | Receptions | over | 0.06308471474675131 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|a3da5e5c-a888-405e-9dfa-c36687761062 | underdog | Drew Sample | Receiving Yards | over | 0.0629102314852918 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d76069d3-8d26-4e71-a6a7-06b5b5f062d2 | underdog | Samaje Perine | Receiving Yards | over | 0.06271037602491508 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|cd894ebb-1464-4062-9e9d-d7034e80fd27 | underdog | Tommy Tremble | Receiving Yards | under | 0.0625505359363844 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|79e5199a-505e-4bcb-9f7b-4eb6dede73d8 | underdog | Mo Alie-Cox | Receiving Yards | over | 0.06231155663033794 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|6ba3b054-427d-480d-89f1-a45f0e478d96 | underdog | Jake Bauers | Hits | over | 0.06219934850411013 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|04d5c5e5-e62e-43e4-b7ad-f05b27c1e49f | underdog | Aaron Rodgers | Pass TDs | under | 0.0620273967369939 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|bad7ccd3-6884-4391-aab3-98594caab197 | underdog | Chris Bell | Receiving Yards | under | 0.061951957479485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051228 | prizepicks | Kendrick Bourne | Rec Targets | under | 0.0616943000896329 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|365c7fa6-dcc5-4b1b-b9af-c0c3cdca5d6b | underdog | Puka Nacua | Receptions | under | 0.0616090079415561 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|9ff8ad4e-4c75-4cfd-badd-45cf27902270 | underdog | Chris Bell | Receptions | under | 0.0614599626838349 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|300681f0-5f41-440c-bc6a-141fa5fe86ef | underdog | Tyjae Spears | Receiving Yards | under | 0.061401526255426386 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16155080 | prizepicks | Ben Shelton | Total Games | over | 0.061040211655997934 | 2026-10-25T04:41:09Z | 2026-10-25T05:00:00.000-04:00 |
| underdog|2b8f786a-ddf3-4c91-98e5-a939a1e123fe | underdog | Harold Fannin | Receptions | under | 0.0608103254568292 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3c8721d1-a9d3-4553-a327-a86b397d702f | underdog | Jadeveon Clowney | Sacks | over | 0.0605759985732586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|60491404-85e4-4da0-ba06-4d23eb4cbaf6 | underdog | Brock Purdy | Rush Yards | under | 0.0603702485832077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16166389 | prizepicks | Senne Lammens | Goalie Saves | under | 0.06030159832897797 | 2026-10-25T04:41:09Z | 2026-10-25T10:00:00.000-04:00 |
| prizepicks|15940804 | prizepicks | Devaughn Vele | Recs | under | 0.06015971284752153 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|0d6f7a50-fa14-420e-bb35-6a8002c97c5a | underdog | Kendrick Bourne | Receptions | under | 0.0601364284559438 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|f2c7e077-b430-4e2b-b8d2-b22a32ab1f15 | underdog | Kendre Miller | Receiving Yards | over | 0.0599966168566626 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|0b848e07-9ee9-4b51-bcf7-f9f29202ca1b | underdog | Will Reichard | Kicking Points | under | 0.05988293461374794 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c2cfc127-7dcb-4e9c-b22d-bacb733553fe | underdog | Sione Vaki | Receptions | over | 0.0598689783880203 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|fec5e122-f59d-49aa-9430-e8b854af8e70 | underdog | Geno Smith | Rush Yards | under | 0.0596711983179013 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|95c1e474-6c5b-48b7-987a-a9b6b84d9ba3 | underdog | Aaron Jones | Receiving Yards | under | 0.05947359172960187 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b4073c57-0eee-482e-9c8c-29a23326ac44 | underdog | Chuba Hubbard | Rush Yards | under | 0.0593658945119207 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e95ff3e8-4fba-45fe-a9cd-c5e3f5139f69 | underdog | Jaylen Warren | Rush Yards | under | 0.058867250754107925 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|dfb0734a-980d-4afc-a3aa-74509c4487f7 | underdog | Michael Wilson | Receptions | under | 0.05878305109835957 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|09b74476-b00c-4a2f-abc2-20d3e33100a6 | underdog | T.J. Hockenson | Receptions | under | 0.0587657925838965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|277a8aec-fac7-43c4-a344-09970c828c5d | underdog | Pierre Strong Jr. | Receptions | over | 0.05871475975977286 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|b1ce77d3-02c2-4848-944d-6bf6461362a7 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.05855176569296172 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|3c27ced9-c782-4952-836e-43b81b480fcc | underdog | Tyler Higbee | Receptions | under | 0.0585445402433147 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|f850eeaa-b79f-483b-90c4-6ffe630e9c5c | underdog | Dohnte Meyers | Receptions | under | 0.05807606094078033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|f182c79e-7cc9-4951-a25b-7b81f7f77224 | underdog | Chandler Simpson | Runs | over | 0.057637632463168775 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|b359de29-0515-46be-8ab6-0d86fc6803fe | underdog | Ryan Fitzgerald | FG Made | under | 0.0575761782932597 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ff89c271-25fb-4c54-8a1f-fdf8628af230 | underdog | Darnell Mooney | Receiving Yards | over | 0.0574533030448441 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|5b1209ba-20ce-4559-a6b5-422b5f506385 | underdog | Kenneth Walker III | Receiving Yards | under | 0.0570964245693671 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|3d248cc4-0508-481d-9a59-1f20f1e8e6e0 | underdog | Seth McGowan | Rush Yards | under | 0.05707618827281735 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|487d9fcc-6679-4b44-a167-1b46a9226489 | underdog | Mike Washington | Rush Yards | under | 0.057058846958996434 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|788d321e-a413-42d1-9fe8-598725b5146c | underdog | Noah Fant | Receptions | under | 0.0569890350580739 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|9de90d0c-fc2e-4d4d-8991-42254596c301 | underdog | Darren Waller | Receiving Yards | under | 0.056903144274505 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|420a975f-c847-42e1-acb6-f2590c1aa0f5 | underdog | Alvin Kamara | Rush + Rec Yards | over | 0.0568139689190557 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|f7747872-2256-41eb-988e-da59a2931a51 | underdog | Chuba Hubbard | Receptions | under | 0.0567888839933112 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6276286c-e5bf-4672-8e51-640ff2a07dc4 | underdog | Kevin Coleman | Receiving Yards | over | 0.05657005791714098 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|b3371c8f-6832-4056-84be-a457bd651bf4 | underdog | Freddy Peralta | Strikeouts | under | 0.05639936349981178 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|f15a3695-f852-4979-90f0-f2b517bf4da9 | underdog | Elijah Higgins | Receiving Yards | under | 0.0561049507995341 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|c56069f5-7322-40ba-a234-f5f699ae2646 | underdog | Chop Robinson | Sacks | over | 0.05601796101094486 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8933129e-bb98-41af-a84b-5e524615a1d6 | underdog | T.J. Hockenson | Receiving Yards | under | 0.0559605706113038 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|12b11f2f-ae2a-4022-b854-56eaf1b3f69c | underdog | Garrett Mitchell | Total Bases | over | 0.05585777022241101 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|5a51841a-2746-4196-91a2-dfa1b46f7483 | underdog | Adonai Mitchell | Receptions | over | 0.055696016546392 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|dcf89a53-7242-4b80-9067-f817f87fad1f | underdog | Noah Fant | Receiving Yards | under | 0.05569116003186114 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|3047e4cb-3e23-406e-b1f8-e373e2da84b4 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.055311426932114216 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|3945e7d1-93a5-4245-a581-d71dc28ff4f7 | underdog | Brevyn Spann-Ford | Receptions | under | 0.055133256726465296 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| underdog|ec03b994-7606-4fdd-8758-0d399d9fcbd0 | underdog | Jackson Chourio | Batter Walks | under | 0.05504587155963303 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9dec28bf-f1cc-4984-9300-00fc93a45701 | underdog | CJ Donaldson | Rush Yards | under | 0.05495515497621306 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|20f33eab-6a5f-405f-aef4-4e70082d55c6 | underdog | Dallas Turner | Sacks | over | 0.05403315962290178 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|1016ca21-bada-4f8c-89c3-8aa706b67cbf | underdog | Juwan Johnson | Receptions | under | 0.0539535225588111 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ce32c899-c546-40d5-b26e-9ced9c6ef8a3 | underdog | Cam Skattebo | Rush + Rec Yards | over | 0.0539214755329643 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|de81035a-8fe0-4d20-943a-ec1f3756f92c | underdog | Samaje Perine | Rush Yards | under | 0.05374503171523115 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|cd5d7e06-30da-4741-96ce-ad2f7b10df87 | underdog | Yandy Díaz | Batter Walks | under | 0.05357965732478742 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|ac3836b7-ed31-46ae-a383-3b2f7ddd8724 | underdog | RJ Harvey | Receiving Yards | under | 0.0533369848818797 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|262dcb8e-4bc7-4305-a2b0-e717b681e5a6 | underdog | Ryan Flournoy | Receiving Yards | under | 0.0530145633905199 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|16154910 | prizepicks | Learner Tien | Total Games | over | 0.05295065723555026 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| prizepicks|16051317 | prizepicks | Wan'Dale Robinson | Rec Targets | under | 0.0522923521605553 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16151763 | prizepicks | Himeno Sakatsume | Total Games Won | over | 0.051990749745927656 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|be3b2598-50de-45f0-a5e0-023637d39ee2 | underdog | David Hamilton | RBIs | under | 0.05197132616487454 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|9a3669b9-daf9-4d97-9a11-9b63d7b6c1c5 | underdog | Garrett Mitchell | Hits | over | 0.051923054647021405 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|c3e31ab1-4709-4b43-8b04-8f227c273411 | underdog | Harrison Butker | Kicking Points | under | 0.05183794000713 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0c7fe2c3-6b86-431f-9be5-2eb648c005b6 | underdog | Cody White | Receptions | over | 0.051779480133012146 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|c01f7d6b-9ff9-4aaf-8d56-d4522c63a040 | underdog | Cam Skattebo | Receptions | over | 0.0512513434405716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|744f7c64-587e-41f1-af9d-1bbabfac4473 | underdog | Chuba Hubbard | Receiving Yards | under | 0.0504931979002241 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| prizepicks|15980928 | prizepicks | Javonte Williams | Rush TDs | over | 0.05045837473167836 | 2026-10-25T04:41:09Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|25fa3790-d20b-4150-9c6a-160e2a5d2896 | underdog | Tyjae Spears | Rush Yards | under | 0.0503793612554041 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8225d625-378d-487c-8596-68cf88140f58 | underdog | Ryan Flournoy | Receptions | under | 0.0501148528015784 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0c1a8b52-a086-444e-9bbf-7623ea229a24 | underdog | Rashid Shaheed | Receptions | under | 0.0500925370142416 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|4a5deac2-17dc-40d7-8e44-76ab0866612d | underdog | George Holani | Receptions | under | 0.05005544112939009 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|ef28db8f-70ad-410b-b7cc-a22e68e1490a | underdog | Pat Freiermuth | Receptions | under | 0.0499824428187301 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|043f11be-fc7c-4b35-97e9-4d766bfbf47c | underdog | Brock Wright | Receptions | under | 0.04996663713700833 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|2637fc5f-5a0e-49ff-854c-2285f9f3a597 | underdog | Jonnu Smith | Receptions | over | 0.049960814737353365 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|9749696e-8717-4ed8-9d9e-e6a396043031 | underdog | RJ Harvey | Rush + Rec Yards | under | 0.0497149333024727 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|ced80dce-59ad-4cbc-9c8d-69b3ca2801d1 | underdog | Kingsley Enagbare | Sacks | over | 0.04956081285635916 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16051304 | prizepicks | Darnell Washington | Rec Targets | under | 0.0493716300398139 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|ede7b208-2151-441c-ba65-228a8c200c0d | underdog | Bam Knight | Receptions | under | 0.049108614094104164 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|443e9afe-dfee-477e-9747-8ffb5469c774 | underdog | Justice Hill | Rush + Rec Yards | under | 0.04901574459855218 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|f6c5d90c-aa20-4df0-8599-3fd8ba03d321 | underdog | J.K. Dobbins | Receiving Yards | over | 0.0489630391293001 | 2026-10-22T04:39:42Z | 2026-10-25T20:05:00Z |
| underdog|f6ceccea-ad08-4498-a7b6-c41146122c3c | underdog | Justice Hill | Rush Yards | under | 0.04895985807778913 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|03579dce-9db2-4320-9c09-20d800724e28 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.04887599900158035 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|06c8c71a-f7db-4a2c-9d8a-ff6d764c68ef | underdog | Bucky Irving | Rush Yards | under | 0.0487607240531607 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16035052 | prizepicks | Jake Bates | Kicking Points | under | 0.0487274702622712 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|38da6842-8e2b-4b9f-8e1a-2627589e622a | underdog | Harrison Butker | FG Made | under | 0.0486124772086066 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1ca4e6b0-0258-4dc4-be31-aabffca2de5c | underdog | Justice Hill | Receiving Yards | under | 0.04854682015486733 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|944a601c-2208-4a78-8911-90f0a1088da5 | underdog | Velus Jones Jr. | Rush Yards | under | 0.04809891097003571 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| prizepicks|16051231 | prizepicks | Bijan Robinson | Rec Targets | under | 0.0477412880585349 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|128f8674-af8f-46aa-a044-e134d733e4a0 | underdog | Jackson Chourio | Hits | over | 0.04771409740347976 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|19497d03-c39f-46ac-80d2-e74b2c4a8634 | underdog | Wan'Dale Robinson | Receptions | under | 0.0476246066680077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c6eb4bd1-bbd4-4d84-a247-eef592bfa1f9 | underdog | J.K. Dobbins | Receptions | over | 0.0476044558282254 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|57243a15-62d8-4624-b55c-49b812912663 | underdog | Tyjae Spears | Receptions | over | 0.0474516029151996 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051249 | prizepicks | Jake Ferguson | Rec Targets | under | 0.047278123853882 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|977b2034-4b67-463d-8a47-d48cfca4f3ea | underdog | John Metchie III | Receptions | under | 0.04724726183118366 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|d158cff3-7017-4bf0-9c63-9a006c591ce3 | underdog | Tre Tucker | Receiving Yards | under | 0.04716970455897673 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|a1ff5d6a-2777-412b-bebb-aeb1145b0fc4 | underdog | Kaelon Black | Receptions | over | 0.04704383794728084 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b57929fa-a09d-4e6f-a44b-3038db73bdd9 | underdog | Samaje Perine | Rush + Rec Yards | over | 0.0470082519671165 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b17ce54d-78a1-4fa1-ab15-3a025ee6ec33 | underdog | Mo Alie-Cox | Receptions | under | 0.04696581796029453 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|234ff42d-a4a9-45d5-b7b6-65c9076b7b2c | underdog | Cooper Pratt | Hits | over | 0.04659293306247447 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|35962dae-0852-4830-ab91-68c9dcafb2d3 | underdog | Cam Skattebo | Rush Yards | under | 0.046116001037545 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b6f0be07-3802-43c1-86c1-d6bb682a6d07 | underdog | Tyler Shough | Pass TDs | over | 0.0460949746765986 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|130a239c-1b64-4770-9290-c9748e447956 | underdog | Omar Cooper | Receptions | under | 0.04568377572350768 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|87557726-d244-4861-a281-61e88eb7a852 | underdog | Davis Allen | Receptions | over | 0.04540259617966852 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|6f301dcc-5c86-42bb-8513-865d701917a4 | underdog | Will Kacmarek | Receiving Yards | over | 0.04486438127943204 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|5689b0d3-95b4-48cf-8b7a-64637e335481 | underdog | Derrick Henry | Receiving Yards | over | 0.0446794913234094 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ac1c6c6c-2327-4e95-af19-59c5bd28b38c | underdog | Juwan Johnson | Receiving Yards | under | 0.0446562817968326 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|249ee0b9-e0c3-41fc-8414-3c22214852df | underdog | Matt Gay | FG Made | under | 0.044627908003273875 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|9efbbe74-2567-4004-95f8-f90d660bc440 | underdog | Chad Ryland | FG Made | under | 0.04460205320461674 | 2026-10-25T04:41:09Z | 2026-10-25T20:05:00Z |
| underdog|fed7d146-f17a-402e-86a7-975c0933e22d | underdog | Junior Caminero | Hits | over | 0.044319754871084416 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16051251 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.0440754381772996 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|55693097-fe57-4624-8555-093260858595 | underdog | Mike Washington | Receiving Yards | over | 0.04393676507784294 | 2026-10-25T04:41:09Z | 2026-10-25T20:25:00Z |
| underdog|e40c88ee-022c-460d-a447-35935e484914 | underdog | Joey Slye | Kicking Points | under | 0.0437911990002866 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|951f0756-5616-48c0-bb15-989e6abd891d | underdog | Emanuel Wilson | Receptions | under | 0.043448009734545656 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|8c94a8b7-8234-4b38-b03e-cc405bcf44dc | underdog | William Contreras | Hits | over | 0.043354401129859 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|29ac09e2-63d1-426c-ba2d-439c32da20ba | underdog | Ryan Vilade | Hits | over | 0.04298800052923557 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| prizepicks|16156694 | prizepicks | Taylor Fritz | Total Games | over | 0.04290846956186811 | 2026-10-25T04:41:09Z | 2026-10-26T07:00:00.000-04:00 |
| underdog|976edc90-d679-4566-8607-829d2e9644fc | underdog | Keenan Allen | Receptions | under | 0.042892061025248 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128100 | prizepicks | Kenny Gainwell | Rec Targets | under | 0.04287892121183334 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|25ef4d6c-fafc-461a-91ad-cc9e6a9ca45e | underdog | Cooper Kupp | Receptions | under | 0.0428006415227674 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| prizepicks|16163740 | prizepicks | Justice Hill | Rec Targets | under | 0.04265890298558239 | 2026-10-25T04:41:09Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16154916 | prizepicks | Luca Van Assche | Total Games Won | over | 0.04224858068907933 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| underdog|0fa9a4bf-e249-4a3d-8acf-9f1760034530 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.0418070609890378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051240 | prizepicks | Tommy Tremble | Rec Targets | under | 0.0417284345604694 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|348122fb-28c4-4cb4-b1cf-6f19ea0055d5 | underdog | Kyle Juszczyk | Receptions | under | 0.0413755116703427 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|098c3980-acb0-4efc-904f-37a937d6a8af | underdog | Kendre Miller | Receptions | under | 0.04137499076753659 | 2026-10-24T04:39:26Z | 2026-10-25T13:30:00Z |
| prizepicks|16051263 | prizepicks | Matthew Golden | Rec Targets | under | 0.0413695180084056 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|a6def6be-c653-4e03-a395-49db966867f2 | underdog | Bam Knight | Receiving Yards | under | 0.04126734093810713 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|692ba1d6-2be8-483b-ae39-5bda64236faf | underdog | Christian Yelich | Hits | over | 0.041070697804505896 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|0b5ab754-49ef-43e7-8477-a62ff19e59b3 | underdog | Kevin Coleman | Receptions | under | 0.0410197431717918 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|76df7d50-d1c8-4cef-a264-da1f137d2d44 | underdog | Mike Gesicki | Receiving Yards | over | 0.040754670182375 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16151744 | prizepicks | Moyuka Uchijima | Total Games Won | over | 0.040446924065292156 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|c620c5b0-762d-4cc3-9c1a-f3966aed4fd1 | underdog | Gunnar Helm | Receptions | under | 0.0400733577651734 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3baf102e-18a4-4fa0-930f-45569bbf62d1 | underdog | Danielle Hunter | Sacks | under | 0.03949611270366671 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|72fba08d-633c-40eb-89ae-8a0908addd6d | underdog | Brevyn Spann-Ford | Receiving Yards | under | 0.039376877029623336 | 2026-10-25T04:41:09Z | 2026-10-27T00:15:00Z |
| prizepicks|16151756 | prizepicks | Diane Parry | 1st Set Total Games | under | 0.03928919509868389 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|1ad3d594-f785-442a-988e-37a405dc4bd9 | underdog | Pierre Strong Jr. | Rush Yards | over | 0.03903240736915592 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051255 | prizepicks | Marvin Mims Jr. | Rec Targets | under | 0.0388842684737961 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3188fab2-f2b8-4313-895e-57c191d21509 | underdog | Kaelon Black | Receiving Yards | over | 0.0388077194402237 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051242 | prizepicks | Tee Higgins | Rec Targets | under | 0.0387631549019464 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|330820d7-8d2a-41ef-af1a-6866b6a9e287 | underdog | Elic Ayomanor | Receiving Yards | over | 0.038760146342862 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e3620db9-71a9-4ed1-8873-e30ae36cd8b5 | underdog | Jacoby Brissett | Pass TDs | under | 0.0382668553031229 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|16051246 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.03816939250727 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f89ba872-d424-4e73-8bd7-6614b460990e | underdog | Noah Gray | Receiving Yards | under | 0.03811545624303703 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16151769 | prizepicks | Leylah Fernandez | Total Games | over | 0.037775107846283684 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|f3e0c24d-dacd-42f1-be81-2a591332ddc8 | underdog | Cooper Pratt | Batter Walks | under | 0.03751638269986901 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|37b58552-22c6-476b-996f-76d857fff274 | underdog | Dalton Schultz | Receptions | over | 0.0372622958628433 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f8caab65-966d-4958-bc02-cd1cc7ac6f7f | underdog | Kenyon Sadiq | Receptions | over | 0.0371667149623974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f26e20ec-cce5-42d2-b0d0-65cdd3b8f5a7 | underdog | RJ Harvey | Receptions | under | 0.0371183056096371 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|fac29e41-f948-4669-9e0b-1d83285c693c | underdog | T.J. Watt | Sacks | over | 0.036968923678276866 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|b36c99d1-9b4e-4356-9b5f-76ea099ba1e2 | underdog | Joe Burrow | Rush Yards | over | 0.0369126735438984 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d30b9986-6ec1-499d-bad0-0f8909201cc8 | underdog | Tyler Shough | Rush Yards | under | 0.03669695108919868 | 2026-10-24T04:39:26Z | 2026-10-25T13:30:00Z |
| prizepicks|16128079 | prizepicks | Samaje Perine | Rec Targets | under | 0.03636041796769329 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|38f2a21d-8f0b-4316-b852-d137222284bb | underdog | Chase Brown | Receiving Yards | under | 0.0362468208379922 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|489a8a45-65e5-4e7a-9430-927c5962e4b2 | underdog | Rico Dowdle | Receiving Yards | over | 0.036132166882107075 | 2026-10-25T04:41:09Z | 2026-10-25T13:30:00Z |
| underdog|30a953ab-88f0-45b0-adfb-97ce665a9ac6 | underdog | Zachariah Branch | Receiving Yards | under | 0.0361238064043945 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|cf250d16-74e7-4690-b197-f25c4276855d | underdog | Evan McPherson | Kicking Points | under | 0.0360049530640667 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|eb9400f4-cfe4-423f-875f-9a2a0433b614 | underdog | Erick All | Receptions | over | 0.03591696685781898 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|95151427-da0f-4d9b-9b64-708b8632ee19 | underdog | Colby Parkinson | Receptions | under | 0.035577182312387 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|83375341-0bc4-4389-8595-dd4653ce1fea | underdog | Devin Singletary | Rush + Rec Yards | over | 0.03500589094834228 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ab83b69d-5a82-44be-aa82-18afedf56ef1 | underdog | William Contreras | Batter Walks | over | 0.03479196556671449 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|e84d43d4-e77a-46b0-8a42-34611e9f7119 | underdog | Junior Caminero | Batter Walks | over | 0.03479196556671449 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|5aba7c83-7528-42ba-bcc1-e98faaf845fa | underdog | Darnell Mooney | Receptions | over | 0.0347146447100191 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b2494e96-bb5e-4c81-b6d3-1919cabc6813 | underdog | David Bailey | Sacks | under | 0.03407335691512081 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|6b5a1de9-3eef-4741-9170-14f9deced32e | underdog | Matt Gay | Kicking Points | under | 0.0340167035528746 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|cc0fb124-1eee-4a5d-8ec1-07ae0c63939c | underdog | Jonah Coleman | Rush + Rec Yards | over | 0.03377934918735054 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|a29c1696-1438-47a3-b01a-5912718e85a6 | underdog | Tyrone Tracy | Receiving Yards | under | 0.03364027564317851 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|73ccb174-e10e-4fab-b016-1288d6d50b2f | underdog | Chase Brown | Receptions | under | 0.0331873731070406 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|012ba749-986d-4620-bb54-b8d085f7c130 | underdog | Cooper Pratt | Total Bases | over | 0.03312098319990975 | 2026-10-25T04:41:09Z | 2026-10-27T00:00:00Z |
| underdog|8a92afed-a878-4de7-bec7-1473621ff0a1 | underdog | Kirk Cousins | Pass TDs | under | 0.03291386837656618 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|9ae00861-5dbe-4edb-ba32-2a64fe363093 | underdog | Emmett Johnson | Rush Yards | over | 0.0328425645250116 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| prizepicks|16160170 | prizepicks | Titouan Droguet | Total Games | over | 0.03280035872921794 | 2026-10-25T04:41:09Z | 2026-10-25T08:00:00.000-04:00 |
| underdog|a8715203-bfdd-4d40-83b9-f77ce1740b4f | underdog | Will Anderson | Sacks | under | 0.03268582975049328 | 2026-10-25T04:41:09Z | 2026-10-25T17:00:00Z |
| underdog|672fd8db-fc81-4c61-8366-cc5023140b71 | underdog | Erick All | Receiving Yards | over | 0.03264221436156661 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|f7464f83-92c4-424f-9a7e-b4a73ea0f4c3 | underdog | Zach Allen | Sacks | over | 0.03238628283552075 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|c3204946-1e17-48fa-87ef-8cfe038f2b6b | underdog | Chris Jones | Sacks | over | 0.03225957989751327 | 2026-10-25T04:41:09Z | 2026-10-26T00:20:00Z |
| prizepicks|16051314 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.032115498076035 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|e4480b0f-913c-4202-bf76-e2aff55f73c7 | underdog | Cam Ward | Rush Yards | under | 0.0318471189373211 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|437bcba0-d2dc-490b-b518-d597bc646e8d | underdog | MarShawn Lloyd | Receptions | under | 0.031455160163501805 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16128097 | prizepicks | Bucky Irving | Rec Targets | under | 0.031448787953933244 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16166605 | prizepicks | Yvon Mvogo | Goalie Saves | under | 0.031047934909710473 | 2026-10-25T04:41:09Z | 2026-10-25T12:15:00.000-04:00 |
| underdog|16e2ddea-e714-4ae0-967c-6128c1d08825 | underdog | Foster Moreau | Receiving Yards | over | 0.030947868389375688 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16128081 | prizepicks | Jerry Jeudy | Rec Targets | under | 0.03047366483284586 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|eb47b832-623a-4517-b8e3-f59db1fa3394 | underdog | Dominic Zvada | FG Made | over | 0.0304043417105965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
