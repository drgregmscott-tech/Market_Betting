# Pipeline Digest -- 2026-10-23T13:20:54Z

## Run summary
- Ingestion: 52464 rows (PrizePicks OK, Underdog OK)
- Estimation: 52464 rows estimated (from 52464 ingested props)
- CLV logging: 50 newly flagged, 0 newly closed, 929 still open (104749 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|f8a727e6-f7b0-4157-b00b-0e79f18b706f | underdog | Bryce Young | Pass Yards | under | 0.4692307692307692 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd46726c-1a01-433c-aa7f-adfd3cba34d5 | underdog | Deshaun Watson | Pass Yards | under | 0.4656565656565657 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|0e14180e-fbdb-4a03-bd4e-6fde932b009e | underdog | Cam Ward | Pass Yards | under | 0.4641025641025641 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7a5a87ce-ed58-4331-8eca-c965c013a075 | underdog | Aaron Rodgers | Pass Yards | under | 0.4482233502538072 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|b56c7b79-4bf1-4e9c-8811-7ae67ead8511 | underdog | Chris Godwin | Receiving Yards | under | 0.4408163265306123 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|5669e007-1810-4de9-9feb-ea3d1b56340e | underdog | Jared Goff | Pass Yards | under | 0.4357142857142857 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|520cbedc-2c18-47e2-8d28-495bc32d4e01 | underdog | Brandin Cooks | Receiving Yards | under | 0.42763819095477384 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7c13508f-ad8a-440d-ae01-29774bf4e852 | underdog | Brice Turang | RBIs | over | 0.4266335227272727 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|026dcf42-9a7e-472d-9b73-8d8bcd162c79 | underdog | Baker Mayfield | Pass Attempts | under | 0.4226130653266332 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d290053f-bb7e-4fc5-a2d6-2cd2d02e6ee2 | underdog | Chase Brown | Rush + Rec Yards | under | 0.4190595736163557 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|065460d7-1c5c-43d4-8968-bba3d831f322 | underdog | C.J. Stroud | Pass Yards | under | 0.4144451746277202 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d901ce25-9ca6-4d08-a605-d775897a85aa | underdog | Geno Smith | Pass Yards | under | 0.4090737399477504 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1eb3cc78-3cfa-4153-87dd-b9095b038836 | underdog | Deshaun Watson | Pass Attempts | under | 0.4087275591164793 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e1ed7c34-5984-4d1d-b0f0-10d131ce332c | underdog | Brock Purdy | Pass Attempts | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d424e459-1d04-4391-92fb-b90d20c159d8 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cdb5e111-4cf9-4bfd-82c6-27b11ce762fc | underdog | Eddy Pineiro | FG Made | under | 0.3955537623462751 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e3084a60-03df-4043-9baa-8fdd03ce53ce | underdog | Malik Willis | Pass Yards | under | 0.3948522906927716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9693ec51-4551-43f9-853c-0fb05eafd96d | underdog | Daniel Jones | Pass Yards | under | 0.3939654564213076 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5f896a94-190d-4811-9b4b-b1f17ce66f93 | underdog | Jordan Love | Pass Yards | under | 0.3897173199669762 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|643cc8ea-4e4a-4d28-86a8-1e125427f8dd | underdog | Michael Penix | Pass Attempts | under | 0.3727880183899563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|df2d500b-274d-4174-b4d8-d32b5c551962 | underdog | Bo Nix | Pass Yards | under | 0.3619289340101522 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|38a39011-3779-4d19-a6e6-ca06836b54c2 | underdog | Brendan Baird | XP Made | under | 0.3592651266806685 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|0085fd80-5781-444c-9416-df3ebc46a0c0 | underdog | Ted Hurst | Receiving Yards | under | 0.35918367346938773 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|4ae8ad3b-3e4b-49b9-a170-e5307e2a5898 | underdog | Brock Purdy | Pass Yards | under | 0.3591836734693877 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aed9e657-4b01-41ed-a960-612d3d02a69a | underdog | Jacoby Brissett | Pass Yards | under | 0.3567731226756141 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a218a657-b6cc-4e53-bfe6-4b64bb11eaa5 | underdog | Tyler Allgeier | Receiving Yards | under | 0.35099657850370225 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| prizepicks|16039393 | prizepicks | Kyler Murray | Pass+Rush+Rec TDs | under | 0.3509424650567749 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|15944973 | prizepicks | Bo Nix | Pass Yards | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|67b9076a-4be2-44b7-a2ab-11721c8cbac7 | underdog | Saquon Barkley | Receiving Yards | under | 0.3504068968649158 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|d0517fae-e001-44f5-8e9a-0a74f44ad68b | underdog | Baker Mayfield | Pass Yards | under | 0.3467005076142132 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|86608b58-ef41-4874-b74b-6cb58e689196 | underdog | Bryce Young | Pass Attempts | under | 0.34321350423372066 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|37edd000-30ff-4318-96d8-a3ca5e430a8d | underdog | Patrick Mahomes | Pass Yards | under | 0.3421724696477669 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|6671aa81-ba7b-4453-a8b6-fe3bfeee2cc8 | underdog | Eddy Pineiro | Kicking Points | under | 0.33856343461105154 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|847b0c28-14bd-4013-973e-05d76c8b982e | underdog | Matthew Stafford | Pass Yards | under | 0.33409895723922944 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|8dc47268-4a7d-404f-9e49-dcd9ba768270 | underdog | Kyler Murray | Pass Yards | under | 0.3335652027540378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4ab4a41a-52fd-4cc5-b31f-ec4b0c82bb82 | underdog | Trey McBride | Receptions | under | 0.3329820296458966 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|79b37311-f15b-4882-b6a3-944e0502707c | underdog | Bo Nix | Pass Attempts | under | 0.3304520785470337 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|7c372f92-fddc-4538-b64d-da23f20da55a | underdog | Tommy Carr | Pass Yards | under | 0.32940560368065763 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|de1666e6-df3d-43ad-b5d6-c89105471ef8 | underdog | Cole Tabb | Receiving Yards | over | 0.3271958565311026 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|3246a459-7d1f-41ff-ba1b-b9c683e7b334 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3268677849268778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|24013bf3-a907-48ae-8533-86d3168e770c | underdog | Tyrone Tracy | Rush Yards | under | 0.3267094468242045 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|0837eb99-3beb-4beb-803a-b6d445424ac1 | underdog | Jordan Love | Pass TDs | under | 0.3243123493621316 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|f0fc31cd-bda5-492c-9fde-68412646daa5 | underdog | Kirk Cousins | Pass Yards | under | 0.3229461067989536 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|21ae2dbb-b8cd-47b4-8d9e-617160fee214 | underdog | Jake Elliott | FG Made | under | 0.3198767487193468 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1776f06a-1d54-4810-893f-a6f0b18bce64 | underdog | Joe Burrow | Pass Yards | under | 0.317382759820503 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dbe5c55e-c922-47ce-80a9-02406cd98c80 | underdog | Jalen Royals | Receiving Yards | under | 0.31709006450626964 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|154124b9-f603-40a2-80d3-6e46172c515f | underdog | Cam Ward | Pass Attempts | under | 0.3135302584652062 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|469a1bdc-08fa-448d-abcb-21164ec4757c | underdog | Daniel Jones | Pass Attempts | under | 0.3129432398892975 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2ec6ad3-205c-4df4-915c-e02ff73d5ed6 | underdog | Trey McBride | Receiving Yards | under | 0.30725817844859604 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|6778a4ed-0a07-462f-ad67-3327e6b33ee7 | underdog | Tyler Shough | Pass Yards | under | 0.307201308387714 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|82aebfff-cfa1-4d98-b5bd-55154adc923e | underdog | J.K. Dobbins | Rush Yards | under | 0.30471317090038563 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|def3c45d-8dee-47c2-8568-4c3fd9106465 | underdog | Courtland Sutton | Receptions | under | 0.30202251379357925 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|e34970e2-eb5b-4c42-a983-df77a630b08c | underdog | Ja'Marr Chase | Receiving Yards | under | 0.3017403489827723 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e10287d-2f97-493e-ae55-2e6c78479625 | underdog | Tony Pollard | Rush Yards | under | 0.3014201136182672 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7a12d1ee-529c-49c9-966a-48bcaa8ce51c | underdog | Puka Nacua | Receiving Yards | under | 0.2961452597214975 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3c6300c9-4b09-4aec-8e6b-9a70d49c3f99 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.2943696215652248 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| prizepicks|16051310 | prizepicks | George Kittle | Rec Targets | under | 0.2942952711541847 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|e56d19e3-ff75-4054-8e81-a52ef8d30309 | underdog | Kyler Murray | Pass TDs | under | 0.2942390154326902 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|586acb89-828d-495a-b781-835f3b0cca6b | underdog | Courtland Sutton | Receiving Yards | under | 0.2913478359944116 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|1cb78bf3-5610-4b98-a9c4-2483ad1327b0 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.28954474820641707 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b8668647-fb9f-4bcf-b66b-1fd4c8ff8998 | underdog | Taylor Walls | Runs | over | 0.2885461614047079 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|04a4df3d-c7db-42ac-b930-94951fa9779e | underdog | Brock Bowers | Receiving Yards | under | 0.2882455496564065 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15945775 | prizepicks | Courtland Sutton | Rec Yards | under | 0.2858886737283282 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|739590e9-a831-4e2e-831f-8105a7b0bfa3 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.2856924823941684 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|27afcb09-4472-4907-b73c-9de29d4e33b2 | underdog | George Kittle | Receptions | under | 0.2828324993741664 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1dc224d8-4045-43ec-97c9-959c5e18ba2f | underdog | Tucker Kraft | Receiving Yards | under | 0.2825174713014219 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|79b2b766-9806-4ad9-8c3b-a2f1e9541a4b | underdog | Aaron Rodgers | Pass Attempts | under | 0.2815799685858499 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|00581e62-c08c-43d3-88ff-652d3356abce | underdog | Brice Turang | Batter Walks | over | 0.28142857142857136 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|20101bac-ad93-4e34-a0df-6c368515e5c9 | underdog | Ted Hurst | Receptions | under | 0.281326472163252 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ed554cdd-6711-4d20-ab5c-3f9edfe1ddf7 | underdog | Jahmyr Gibbs | Receptions | under | 0.2812284582963593 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|17ee8953-2dc9-435f-abb2-1065e9ccb4c1 | underdog | Dak Prescott | Pass Yards | under | 0.2811881188118813 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|ac9fca16-ff29-46ad-a999-aad384676c5f | underdog | Brandin Cooks | Receptions | under | 0.2793271159273394 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e05823a2-4f3a-4f97-8e09-a2063261bd71 | underdog | J.J. McCarthy | Pass Yards | under | 0.2792251388086186 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051230 | prizepicks | Trey McBride | Rec Targets | under | 0.2781956898542684 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|16051256 | prizepicks | Troy Franklin | Rec Targets | under | 0.2765686467453297 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|2ef34ff6-b6af-4c78-88e6-b43e09e6eba7 | underdog | Jaylen Wright | Rush Yards | under | 0.2759048149626352 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|00c9927f-5ade-43b4-b9b7-fefb63611a2d | underdog | Malik Willis | Pass Attempts | under | 0.2754400964710172 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a2e72db1-e0c9-49ec-aeee-0a2f7b145f93 | underdog | Cade Otton | Receiving Yards | under | 0.2738237354408446 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e975f741-7c02-4bd6-ad98-eede89cbef4a | underdog | Nico Collins | Receiving Yards | under | 0.2731951910841539 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2dbfa5ca-83df-4571-bbcf-8a84842d2649 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.27223836748338215 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|1ad81329-a627-4424-ab4c-6c206dfbf3ad | underdog | DeVonta Smith | Receiving Yards | under | 0.27070561716917263 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|9324ecc4-fa13-4053-a657-df19163a720b | underdog | Jared Goff | Pass Attempts | under | 0.2687730655877962 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ad87b775-bfc9-4f54-95ee-ff5ed677e61f | underdog | Ja'Marr Chase | Receptions | under | 0.2661038820739 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b55f9b1b-ed72-41fa-a296-39210a20b4bf | underdog | Jordan Love | Pass Attempts | under | 0.2646802457389526 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15956871 | prizepicks | Daniel Jones | Pass Attempts | under | 0.2638857049460724 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|96c40cdc-691c-48db-89d3-4c55dbb29290 | underdog | Sam Darnold | Pass Yards | under | 0.2626055914367695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|73395da4-8892-4961-b521-7e1248b8f7cf | underdog | Bo Nix | Rush Yards | under | 0.2605581005357792 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|daabe970-a6f3-4747-9887-9ec6c2b4a1d8 | underdog | Woody Marks | Rush + Rec Yards | under | 0.26013723356413776 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7f9ff427-eeca-41d9-b667-16c9f1fc8e5d | underdog | Tony Pollard | Rush + Rec Yards | under | 0.2596998817408331 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2ca7cc4-8309-462a-93ef-879c52f609b7 | underdog | Bryce Young | Rush Yards | under | 0.2592736328532177 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c1c0ffd9-df31-4816-86e7-59f57eb89f4c | underdog | Sione Vaki | Receiving Yards | over | 0.2588272369464025 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|672c91b2-8aeb-400f-a8f4-81ff00601d2f | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2573371918577716 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|09bee2cd-e008-407b-87a5-2ef9740a5f75 | underdog | Malik Willis | Pass TDs | under | 0.2548170435450879 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|198558ac-0686-475a-8b78-cb8654c58971 | underdog | Joe Burrow | Pass Attempts | under | 0.2525151606208103 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|4d49df5b-b50b-4f4f-b3cc-23c54ad94116 | underdog | Liam Hicks | RBIs | over | 0.2523518732464103 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7594b837-9c0a-4a5e-a07c-cb03792bcec9 | underdog | Rico Dowdle | Rush Yards | under | 0.2523393133447593 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|9827d4a6-1c80-4f8e-837a-59a7a4efad92 | underdog | Wil Lutz | FG Made | under | 0.2495510531033402 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|16087735 | prizepicks | Sofiane Diop | Shots | under | 0.24740222366914588 | 2026-10-23T04:50:52Z | 2026-10-23T14:45:00.000-04:00 |
| underdog|a7d67cf1-2deb-4409-a28f-186fdbd101d0 | underdog | Malik Washington | Receiving Yards | under | 0.246141552704973 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|41359dbd-8223-40ba-b01b-d548d0fd476b | underdog | George Kittle | Receiving Yards | under | 0.2453249563886891 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051276 | prizepicks | Brock Bowers | Rec Targets | under | 0.24528945408523 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|648dee62-ca9c-448b-bcfa-499810b73d24 | underdog | Xavier Hutchinson | Receptions | over | 0.2439123066762485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|151d3e83-45f8-463e-8fdc-cd3f943b9d80 | underdog | Matthew Golden | Receptions | under | 0.2412290414387117 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|6030f46c-6c57-4c46-931c-9a150e5901e0 | underdog | Jonathan Aranda | RBIs | over | 0.2407494747673969 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4cfc595f-ace4-4eec-a562-9a61b88991da | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.240025789607406 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|5c474bdc-04d7-47e0-867b-bcfee2a049ab | underdog | Baker Mayfield | Pass TDs | under | 0.2393581560012833 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b12fe859-db0b-49c6-bb78-c544b80293d7 | underdog | Patrick Mahomes | Pass Attempts | under | 0.2376070105771173 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|1713fb00-7c86-4fb8-b9db-c0d3cd103304 | underdog | Cade Otton | Receptions | under | 0.2373958346481726 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ea96d4e7-d343-4032-ac48-3c5395f7363e | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.23477237529212425 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|0a21b579-be4c-4502-b653-2800bbfc14bd | underdog | Jacoby Brissett | Pass Attempts | under | 0.2341561518035735 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|63a589be-c960-48d9-a32f-d3109bb47742 | underdog | Kirk Cousins | Pass Attempts | under | 0.2338585829420534 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|86147115-576f-4689-8d0b-2666f24dde83 | underdog | J.J. McCarthy | Pass Attempts | under | 0.23225840306780554 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|193c6a4c-aa4a-46b0-a869-9e9de2826135 | underdog | Bo Nix | Pass TDs | under | 0.2300413174167165 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|fe2f93c1-c969-4428-9c67-a4752f851695 | underdog | Jake Bauers | Batter Walks | over | 0.22980420594633788 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|7caf365c-b8e0-4138-9f38-48f4d8c2e085 | underdog | Jordan Watkins | Receptions | under | 0.22923645637992762 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|58b3f25a-6eba-4472-9821-0fc96a39ffc8 | underdog | Geno Smith | Pass Attempts | under | 0.2275649013349008 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|4425a4ae-92fa-449a-8a8a-b7432c7029f7 | underdog | Yandy Díaz | Runs | over | 0.2275535585332581 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|17c2adf9-75e8-44b7-9e46-b0a6769151cf | underdog | Germie Bernard | Receiving Yards | under | 0.2275384159492459 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|e4c964b1-0b2b-4857-acae-59f009c1792e | underdog | J.J. McCarthy | Pass TDs | under | 0.2273642896866348 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|88ddddd3-918c-4785-9b4f-fdc9f6fb9182 | underdog | Xavier Worthy | Receiving Yards | under | 0.2257113356958771 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|4b4cd0e1-111a-4801-8cdd-f6ce7820bfd3 | underdog | Kedrick Reescano | Rush Yards | under | 0.22531986986921448 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|f9352960-e46a-4bd0-887d-6b56e268fcec | underdog | Dak Prescott | Pass Attempts | under | 0.22420131322413994 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|32c667b7-abd0-4436-bf1e-dab251e7a113 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2235175135999006 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|d8ce48c2-d479-403b-9323-2a031b8681af | underdog | Malcolm Koonce | Sacks | over | 0.22140008020512947 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|bf1d95e3-f10c-4550-8a39-10f875aed153 | underdog | C.J. Stroud | Pass Attempts | under | 0.2210784579055988 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5b90486b-c32a-4e28-812e-3e86cebac5aa | underdog | KC Concepcion | Receiving Yards | under | 0.2207706046563152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0d5dbe4-9388-4622-8cc6-c162a5b0639f | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2206178911560523 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|dd981eb9-f019-43eb-8014-51c7e7f60995 | underdog | Marvin Harrison | Receiving Yards | under | 0.2201873079173418 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|56656c9d-ec82-4d22-befd-cf88edbd6a09 | underdog | C.J. Stroud | Pass TDs | under | 0.21922023288096 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c9dd882b-334e-4169-b37c-b296bb877d16 | underdog | Tyler Loop | FG Made | under | 0.2188399052787495 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a63cc8a0-36cc-4002-9d0a-9275fc20e5e3 | underdog | Devin Singletary | Rush Yards | under | 0.217094503944824 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7dbfe9c7-e77c-46aa-8f0d-da3c00ff3729 | underdog | Cam Ward | Pass TDs | under | 0.2169355074931716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16039395 | prizepicks | Bo Nix | Pass+Rush+Rec TDs | under | 0.2167665072623288 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|99247015-1071-472a-a332-8dde64f53ebf | underdog | Kenny Gainwell | Receiving Yards | under | 0.21558858776841594 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|d4b47417-e8a1-4b5e-89ac-a276f3f40d42 | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.2132167545309671 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|b5b4cf2d-863c-4b07-8225-e61b4888d5da | underdog | Kenny Gainwell | Rush + Rec Yards | under | 0.2124926916515939 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|3f783fb7-df8b-4a45-8475-a55bae43b063 | underdog | Davion Gause | Rush Yards | under | 0.21242244660490384 | 2026-10-23T13:31:04Z | 2026-10-24T02:30:00Z |
| prizepicks|16051257 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.212391920232314 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|80998e29-827a-47a2-ac21-31900ecc9a6c | underdog | Wil Lutz | Kicking Points | under | 0.21088950433211662 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|3d7bdfbe-fd96-4e73-b04d-e4b53c629b08 | underdog | Yandy Díaz | RBIs | over | 0.210772501771793 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a9df4b24-c600-46b7-a5e9-ec9eb30eeff5 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.2103451992664808 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|78179df4-d48d-4dea-9683-aa1d37bce306 | underdog | Tait Reynolds | Pass TDs | under | 0.20877657627845503 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|b3d36ef2-c5d1-42ce-bdf6-3dcd1e9c4bd1 | underdog | Colby Parkinson | Receiving Yards | under | 0.2087631852016807 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|70651333-501c-4679-a021-bd49e0d4b78f | underdog | Kyren Williams | Rush Yards | under | 0.2086633991668998 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5e78605e-bcba-4d2f-90f8-e6c3dfec5088 | underdog | Rico Scott | Receiving Yards | under | 0.2078501632803695 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|e4e5c670-0987-4d0a-8a4a-9428d204a893 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2077532646208933 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c1d936d4-68f3-4e44-837e-b333d2c4f1a2 | underdog | Jameson Williams | Receiving Yards | under | 0.2060331671729401 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16043109 | prizepicks | Jacob Misiorowski | Pitches Thrown | under | 0.2038387781039828 | 2026-10-21T23:24:30Z | 2026-10-23T20:00:00.000-04:00 |
| underdog|4ce494db-1a02-483c-9b1b-ee9ddf695bd0 | underdog | Woody Marks | Rush Yards | under | 0.2028480523660538 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|f2f01af3-8358-4d74-8b46-805e5e5b4468 | underdog | Junior Caminero | Runs | over | 0.2027957652379485 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|8c0c1e3a-1993-48d5-8800-fb0c7901e647 | underdog | Victor Mesa | Runs | over | 0.20253699788583512 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|10021345-bbed-4a2f-a584-a3e81916b523 | underdog | Daniel Jones | Pass TDs | under | 0.200856388948677 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945793 | prizepicks | DeVonta Smith | Rec Yards | under | 0.1997754527670513 | 2026-10-21T04:43:18Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f2c4be9d-9aee-4f55-8d4b-dbe30b779a70 | underdog | Javonte Williams | Rush Yards | under | 0.1985197402148549 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|f7ea1d63-47b7-4975-9db4-7db15515d650 | underdog | Christian McCaffrey | Rush Yards | under | 0.198275138398706 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051270 | prizepicks | Nico Collins | Rec Targets | under | 0.1977937055574494 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|07a4d392-bef4-4ae1-bad4-0c514f603d92 | underdog | Mark Andrews | Receiving Yards | under | 0.1973857281627509 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7478a968-ff4e-476b-9b0f-02fe597e1822 | underdog | Dallas Goedert | Receptions | under | 0.1970050433176551 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|bfc2e148-a21c-4383-a448-5598a14b86aa | underdog | Jonathan Taylor | Rush Yards | under | 0.1969151744354131 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|507911ea-631b-42b4-8236-7f091e1d45c3 | underdog | Christian Yelich | Runs | over | 0.19620601804034987 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|e2b1a7d8-10f5-474f-9df7-e86663e06492 | underdog | John Mateer | Pass Yards | under | 0.1956346122009749 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|dd2e01e1-9b2b-4090-aa87-6a74f55e0015 | underdog | Troy Franklin | Receptions | under | 0.19440896280038 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|8b92d278-dbd5-418b-b6f4-85464899feec | underdog | Tez Johnson | Receptions | under | 0.19344381194647653 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16093539 | prizepicks | Dylan Raiola | Pass Attempts | under | 0.192631721259933 | 2026-10-23T04:50:52Z | 2026-10-24T15:00:00.000-04:00 |
| underdog|7cff4e33-d73d-44f1-8d0d-5a5bf4c7277c | underdog | Matthew Golden | Receiving Yards | under | 0.1918683958802021 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ec32d38f-4baa-4dd5-b4ce-84216707909c | underdog | Kyler Murray | Pass Attempts | under | 0.191433222145686 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|fa30225c-a2b8-4007-91b4-6e7775ca4b91 | underdog | Kendre Miller | Rush Yards | under | 0.1907546806271176 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ee0fd630-668b-45c5-b6f7-9a2833d72609 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.1896770029694203 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a9599a2a-d2a5-4707-b22c-39668c345e29 | underdog | Zay Flowers | Receptions | under | 0.1892743875611844 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c41836db-df10-4158-bf2a-d471ed143dcc | underdog | Chris Godwin | Receptions | under | 0.18927231998376215 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|83d77d5f-8f56-4d65-99e8-b21e59e22d59 | underdog | Jaylen Waddle | Receptions | under | 0.1879932654958955 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|86267553-d29e-4379-94fe-af64970990b8 | underdog | Elic Ayomanor | Receptions | under | 0.187836672850876 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aa76f845-051c-4f41-86fb-b35d6b2b6dd3 | underdog | Jonny DeLuca | RBIs | over | 0.1858042977382799 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e2f0945f-5958-4cd7-b310-8337022f84ec | underdog | Daniel Carlson | FG Made | under | 0.1857689129268523 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|69170097-9590-4b1c-b393-fe6a547e6eb3 | underdog | Sam LaPorta | Receptions | under | 0.1854602802656819 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16046139 | prizepicks | Daniel Jones | Pass TDs | under | 0.1853194844296951 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|80cda42e-dedd-480a-8e61-235d21eae853 | underdog | Kenny Gainwell | Receptions | under | 0.18440203930446974 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051243 | prizepicks | Denzel Boston | Rec Targets | under | 0.1843661428516428 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|ccc2aee5-dbaf-4449-a788-85d8e2cafe2f | underdog | Jackson Chourio | Runs | over | 0.1833756345177665 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|01b304ef-c918-44f1-8674-16230b54ff51 | underdog | Jackson Chourio | Total Bases | over | 0.1832038589898196 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9f05934f-b49e-4994-bd17-9ce1273d9dfe | underdog | Kayshon Boutte | Receiving Yards | over | 0.18201899838674063 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|98e02204-e6fc-49e9-9efb-16eddaa9eb4d | underdog | Jake Elliott | Kicking Points | under | 0.1818784511935599 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|16b7eb23-d92b-411f-b77d-6625a3a327ed | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.18177543346127867 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|ca74e334-4fb2-412b-bdb9-08168dd9098c | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.1815324987306645 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3819447b-036b-46d1-9648-c722854bc2ed | underdog | Josh Downs | Receiving Yards | under | 0.1811543635690468 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0c431785-fb37-41ca-85af-21df097d4c2a | underdog | Tyler Warren | Receiving Yards | under | 0.1810919665120708 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0fbe9c08-877b-4266-baae-db3d1c07e3eb | underdog | Garrett Mitchell | Runs | over | 0.18047084002140173 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|787e8e67-8fee-4197-9ec8-56cd2ca575d9 | underdog | Devon Dampier | Pass Yards | under | 0.1803463623954326 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|95e13e96-3915-4814-acdb-210d240d4701 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1799180201769094 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ae863eaa-ab5e-4877-8585-dc5472a4473c | underdog | Emmett Johnson | Rush + Rec Yards | over | 0.17980433605544605 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16046140 | prizepicks | J.J. McCarthy | Pass TDs | under | 0.1795941015500882 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|15f3e859-2c6f-4254-abb6-7275ce408513 | underdog | Nico Collins | Receptions | under | 0.1794482585928581 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c944e0a7-baf5-4df3-bada-6c428cd23be5 | underdog | Josh Downs | Receptions | under | 0.17854377502334728 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|4cab8863-5993-4392-aac3-07a608ae52ef | underdog | Jalen Royals | Receptions | under | 0.17724030981279304 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16051241 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.175795415306488 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|8dc8a64b-8a6d-4bbb-9c34-ed8b89025f6b | underdog | Brandon Aubrey | FG Made | under | 0.1756787358146653 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0bfe77e7-f046-485b-9c54-f72737f36efb | underdog | Garrett Wilson | Receptions | under | 0.1755107928461772 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|58600dfe-36a7-46ed-bc53-8334433e51b6 | underdog | Sam LaPorta | Receiving Yards | under | 0.1746918808648834 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a67515c6-0a36-4241-81e0-d3885298e1cc | underdog | Matthew Stafford | Rush Yards | over | 0.1739326192322227 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|11e17eff-c3c7-4b31-a4e1-eb3c30ed8c12 | underdog | KC Concepcion | Receptions | under | 0.173856293946127 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea4459fa-5f07-4a26-b2c8-da05776fd757 | underdog | Taylor Walls | Total Bases | over | 0.1738064881711291 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16051252 | prizepicks | Courtland Sutton | Rec Targets | under | 0.1732814208652097 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3614abc9-c288-4ddb-a25e-d8e7de7b52ef | underdog | Darian Mensah | Rush Yards | over | 0.1718691063862979 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|0bfd5d30-8477-4ee0-9287-84f672399f87 | underdog | Dierre Hill | Rush Yards | under | 0.17103802051097539 | 2026-10-23T13:31:04Z | 2026-10-24T19:00:00Z |
| prizepicks|16051269 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.1706456696230398 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|d0b24edb-4dc8-4f46-ae4f-c250461a8311 | underdog | Jake Bauers | Total Bases | over | 0.1704545454545454 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|2eef6a10-bacb-4d87-80f2-e93f2ddb4319 | underdog | Jonny DeLuca | Total Bases | over | 0.1704545454545454 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|db8f2b09-cccf-4e7f-a3e0-6e29fc01c4da | underdog | Jalen Nailor | Receiving Yards | under | 0.17006200858051945 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|404ee6e2-c47e-4246-9c9a-08758d28c9ef | underdog | Arch Manning | Pass Yards | under | 0.1700288444215447 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|49b762ed-4220-4576-ad51-f08750333ea7 | underdog | Austin Hooper | Receiving Yards | over | 0.16966890486115194 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|25c84983-7531-4d73-b90d-493d66582b20 | underdog | Pat Freiermuth | Receiving Yards | under | 0.1693161019733358 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|ee4edd7e-7b6f-41ad-933e-3a50e62080ea | underdog | Bijan Robinson | Receptions | under | 0.1692203598276945 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9356f071-22fc-4b06-8218-7d33d2f4fb9d | underdog | DK Metcalf | Receiving Yards | under | 0.1686306638130101 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|15945781 | prizepicks | Jameson Williams | Rec Yards | under | 0.1684103099885777 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|2fd5f777-f98d-42fc-b079-413f01d2cea6 | underdog | Harold Fannin | Receiving Yards | under | 0.1684065370519358 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fc3864d2-892c-463e-b7d7-1b45f64c3248 | underdog | Jake Bauers | RBIs | over | 0.1677880352579147 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4379cc97-6c42-474d-9885-165493109730 | underdog | Denzel Boston | Receiving Yards | under | 0.167016966353541 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a6dc42f2-7deb-4899-978c-a82ddf28cc59 | underdog | Dani Dennis-Sutton | Sacks | over | 0.1668263272094302 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|b2a4ef33-4dd7-4a8d-bebf-9282e819c744 | underdog | Joe Burrow | Pass TDs | under | 0.1668059378425955 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1583ce20-2aed-4825-9210-33ee84203275 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1662215207642232 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9ba79002-9245-4ab0-a6c7-eeca915701b2 | underdog | Brice Turang | Runs | over | 0.16545706254981718 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|f65fcee2-679b-4d27-9424-1835a6bb5ec9 | underdog | Jahan Dotson | Receptions | under | 0.1642390573801065 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b7fc7bc1-d865-4e6d-908b-52a06ee4298b | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.1642276422764228 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d2a44b0c-8645-4577-b115-54031e32c920 | underdog | Dilin Jones | Rush Yards | under | 0.1642089840751517 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|dcf5511e-2b26-4d33-8ab0-ed6de7733f1f | underdog | Junior Caminero | RBIs | over | 0.1639716761783977 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9fd9689b-0460-46da-8dd7-3031fc41a089 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.16347835416618184 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|b21ede0e-c8d0-4b03-a66c-e119384843bc | underdog | William Contreras | RBIs | over | 0.1626771402791783 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|6d646301-5e70-443e-9fc2-6a051e4e53d9 | underdog | Noah Fifita | Pass Yards | under | 0.16265104033119515 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|4cfd5a4a-1f48-4365-b549-f1ac466a2341 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1626091840811822 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c452f8b7-8eba-4428-9266-453524c4a278 | underdog | Kyle Ferrie | XP Made | over | 0.1614100094526827 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|0ab2e936-3528-4098-ad40-27b9c6983f4b | underdog | Antonio Chadha | XP Made | over | 0.1610898946506532 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|78c65036-bd71-42f0-8897-248434ccea92 | underdog | Quinshon Judkins | Rush Yards | under | 0.16094408862931908 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c9bd1c5a-6975-4a80-ba7e-77a595cc8b70 | underdog | Garrett Mitchell | RBIs | over | 0.1600925713995065 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|88670807-df28-450c-89b9-2d671c6bfd03 | underdog | Ashton Jeanty | Receptions | under | 0.1596415908383356 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|6683a26b-8799-48bb-82ea-062d512e981c | underdog | Dakorien Moore | Receiving Yards | under | 0.1595997848412829 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|3ef8fdc9-08a4-41d9-8d28-99f6c7438824 | underdog | Andre Szmyt | FG Made | under | 0.159326507096576 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4171bbe8-181b-4d86-b23e-9939d0e3cf04 | underdog | Jake Bauers | Runs | over | 0.15926845951686658 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|2d54750b-a6de-495e-a900-cf03ec7b64b5 | underdog | Christian Yelich | RBIs | over | 0.1591350081699345 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|189483bb-5f96-4e44-a814-7221fd0fde14 | underdog | Zachariah Branch | Receiving Yards | over | 0.15872114669711612 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|15959614 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.1587170648523245 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|ffb2588e-8134-4172-9896-65d9f49fb994 | underdog | Drew Mestemaker | Pass Yards | under | 0.1587029716552819 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|3627b2cf-8e83-4470-8053-4744b48edbfd | underdog | Xavier Worthy | Receptions | under | 0.1583155139800515 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|40c97ee5-565d-4fa0-a0f3-0964eabdf2fe | underdog | Jackson Chourio | RBIs | over | 0.158271853935566 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16051232 | prizepicks | Drake London | Rec Targets | under | 0.1578375470720511 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|a72359e4-c625-4fd5-8791-4fd01e9b8c04 | underdog | Devaughn Vele | Receiving Yards | under | 0.1576991448693823 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6325dc45-98a8-42e5-8ff7-c2fe7210d03d | underdog | Saquon Barkley | Rush Yards | under | 0.15753254304903574 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|4297c15a-19d8-4aad-a7d1-e28979baca47 | underdog | Preston Rex | Rush Yards | under | 0.157395970027809 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|7f1b9de6-c09a-48a3-a6b1-890d0fcb4f96 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.15729493148797735 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|021764db-4551-4f29-9724-3d4e2d6cd55d | underdog | J.J. McCarthy | Rush Yards | under | 0.1572331357012335 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3182912b-bec7-451d-a4f6-a8aa028c7477 | underdog | Jameson Williams | Receptions | under | 0.1572143332788562 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|1281770c-e0ae-468e-a287-4aee48f2c034 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.1550542839780637 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|38c993aa-8bac-47c0-8941-740b3ef24351 | underdog | Dane Pizzaro | XP Made | over | 0.1545552838773531 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|8a310332-5951-4ac7-a77f-6c4a56dd8ed7 | underdog | AJ Barner | Receptions | under | 0.1541940474422654 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|7c562fd8-49b6-44ee-8676-bbf1b6cbac68 | underdog | Bryce Young | Pass TDs | under | 0.1535238626727116 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|37f21c56-5c3a-4702-9320-6b096b6218ef | underdog | Kyle Pitts | Receiving Yards | under | 0.1533697059674438 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051300 | prizepicks | Mason Taylor | Rec Targets | under | 0.1530383580179536 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c41b9c5a-8eb4-4e28-b530-7467445701da | underdog | Matthew Stafford | Pass TDs | under | 0.1524509996804636 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|9b5bac7f-853d-4f8d-b23e-638437b1afdb | underdog | Evan Engram | Receptions | under | 0.1522431104423216 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|d0e5175c-f995-4f19-992d-d6a7520bd2b7 | underdog | Jordan Addison | Receiving Yards | under | 0.1520912252614426 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cc956678-f2dc-416c-af59-3565941e17a8 | underdog | Marvin Harrison | Receptions | under | 0.1520330651894664 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f1759cba-b4e9-4603-aad8-c383295e0e2f | underdog | Malik Washington | Receptions | under | 0.1516278474524776 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051264 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1515049144076509 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|40c92b84-7aa2-4a31-ae7b-160596e0c514 | underdog | Isaiah Likely | Receiving Yards | under | 0.1509578137931236 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fe464e1e-f6c0-4abe-b76a-3316fe11545b | underdog | Liam Hicks | Hits | over | 0.1508110346565297 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d43fe0e3-78bc-4ecb-b57f-9caa3fe6a1de | underdog | Ka'imi Fairbairn | FG Made | under | 0.15065512869964737 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|90d57fe3-bd43-4f9e-9ef6-84cef03e6f50 | underdog | Woody Marks | Receiving Yards | under | 0.15053344370246202 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|83cc1041-7a0f-47b2-84ac-351e9d8533f3 | underdog | Taylor Walls | Hits | over | 0.1504427927544617 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f649e406-fd37-43ad-8bae-7bb995d397fd | underdog | Beau Pribula | Pass TDs | over | 0.1499521545038517 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|3fe03957-f78a-4577-b650-0f54860d6b2e | underdog | Chris Boswell | FG Made | under | 0.1495032069538866 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1fb7951e-4784-4d46-b66e-0e4b56243186 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.14908491831684723 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|eb118ae3-88ec-4af1-a4d5-238969093a3c | underdog | Greg Dulcich | Receptions | under | 0.148738688298966 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|52e828a6-c228-46b9-ba0c-81b778711038 | underdog | Jeremy Hecklinski | Pass Yards | under | 0.1484425373240185 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|aa0b7a3e-d2b1-4670-bacd-e7f0265e9da6 | underdog | Kaelon Black | Rush Yards | under | 0.1484179947276228 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8e6bce48-c270-48c4-af74-f023a926fd3c | underdog | Trey Smack | Kicking Points | under | 0.1479856099025124 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|cbdf6397-eda3-42b8-8e11-2e87240b78f5 | underdog | Lukas Van Ness | Sacks | over | 0.1479299343980902 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|894876c7-692d-4cf5-95c3-4b0632db54a3 | underdog | Mason Taylor | Receptions | under | 0.1475775689463663 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c14609ad-2239-49ea-85de-1e3db95fb733 | underdog | Tez Johnson | Receiving Yards | under | 0.14757641917703346 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|968ff81d-59d7-4800-83ce-cfa34ff971b7 | underdog | Dak Prescott | Pass TDs | under | 0.1473394026606165 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|3dcd92ab-0c27-4d63-9fb5-575d5f92cffd | underdog | Garrett Wilson | Receiving Yards | under | 0.1471362850852574 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|1ae5d24c-6f16-4cc5-8989-4a8e6240c971 | underdog | Tyler Shough | Pass Attempts | under | 0.1469924013389894 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|c48a289c-ab9f-4495-895d-bcbc743bb51b | underdog | Ethan Moczulski | FG Made | over | 0.1469323117588332 | 2026-10-21T04:43:18Z | 2026-10-24T19:00:00Z |
| underdog|9e7823b5-6ba8-4931-8647-93f4834676fa | underdog | Tucker Kraft | Receptions | under | 0.14624892899467 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|b952decd-601e-4f92-8345-d2f8930b6eb8 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.146220517841205 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|359ed06b-9344-42b7-a543-df0895950a41 | underdog | Samaje Perine | Receptions | under | 0.1460568513705 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|9fb64b31-fb4e-4775-8815-fd8a63623c12 | underdog | George Pickens | Receiving Yards | under | 0.1449746054605076 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|64da0b97-2529-4288-9c25-313568910759 | underdog | David Olano | FG Made | over | 0.1442033197591167 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| prizepicks|16051233 | prizepicks | Jahan Dotson | Rec Targets | under | 0.1439163357553819 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|39512b8d-dd2c-4104-92e8-1dcfc8ff0331 | underdog | Jalen Brooks | Receptions | under | 0.1437414270624527 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|22b39507-a838-43d3-aca0-16eb972ac142 | underdog | Kenny Minchey | Pass Yards | under | 0.1437248785638849 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|8249186f-8862-4abc-9a48-7f8b007560fd | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1436257422239731 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3a21ad77-2638-4099-ae84-863dd656a054 | underdog | Chris Olave | Receptions | under | 0.1432171019256236 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a5c7fe6d-1a20-451b-a6f8-7879b27d6f11 | underdog | Derrick Henry | Rush Yards | under | 0.1431595063697152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bfcce5cc-c027-490d-8076-653dd3f79753 | underdog | Alex McPherson | XP Made | over | 0.1430779996374752 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|bd5833ce-b0e6-4960-9506-705850df7ad8 | underdog | Richie Palacios | Total Bases | over | 0.1425947219339821 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f06599db-6e94-41c7-b4e8-7df338f7a276 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.1424277006620714 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|ed3825a2-9c90-4618-bea7-7776443f101b | underdog | Bear Bachmeier | Pass TDs | over | 0.1419644793617892 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|75017fcb-3953-4cb7-b182-7145bd12f5ca | underdog | RJ Harvey | Rush Yards | under | 0.141851915435678 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|11effad5-80fc-47d9-b6c9-d853122dcbdc | underdog | Yandy Díaz | Total Bases | over | 0.1417073170731705 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e58c86c8-e648-43d4-b9d2-cabbfd06a61d | underdog | Drake London | Receptions | under | 0.1414594528835526 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|edd88ba0-b0bc-4c4b-bab1-6ced4e331af8 | underdog | CJ Donaldson | Receptions | under | 0.14138497062268784 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945777 | prizepicks | Michael Wilson | Rec Yards | under | 0.1412964357388831 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|bcedd6a5-9b12-434f-9ff9-088d92123f8f | underdog | Kirk Cousins | Rush Yards | under | 0.1412416511943182 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|cfc8d50f-dd4a-4ca7-bd79-8e305ce425d6 | underdog | Jaden Craig | Pass Yards | under | 0.1407745117400555 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|8375befd-3629-4e68-bc30-385d084febe3 | underdog | Cooper Pratt | RBIs | over | 0.1399226357209549 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7e32077b-6ff8-4003-b1be-f10985089148 | underdog | Caleb Douglas | Receptions | under | 0.1399122387421394 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|48b922ca-bdb6-4e04-8520-17e4b9d55fee | underdog | Aidan Chiles | Pass Yards | under | 0.1394975675051353 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|9c22489a-921c-4a35-a1f6-ba9e6aee26d3 | underdog | Carnell Tate | Receiving Yards | under | 0.1394857182718097 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0143747-2eae-48ea-a3a6-8fab2c79ffeb | underdog | Michael Wilson | Receiving Yards | under | 0.1390199081777683 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|df77b125-2d5a-4fbe-a65c-83ddb7d6795f | underdog | Chris Jones | Sacks | under | 0.13828623575350096 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|44a4e634-3c12-458a-8a81-c8b06b39a7d7 | underdog | Will Hammond | Pass Yards | under | 0.1382318502544831 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|6e080788-8634-47c3-bd6e-7726cac733b2 | underdog | Rico Dowdle | Receptions | under | 0.1377303975112497 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ee5b9227-9f37-4dbe-a6e8-55c41f22dd4f | underdog | Jekail Middlebrook | Rush Yards | under | 0.1366528604973662 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|2040be03-458f-48ee-8f52-176b05544b82 | underdog | Ja'Kobi Lane | Receptions | under | 0.13634986916589997 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|990e3a36-0fa9-42d5-b447-447c46e0605b | underdog | Germie Bernard | Receptions | under | 0.1357845862590205 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|b20602df-b17c-4bb4-a6c4-1d4091790ae8 | underdog | Jonnu Smith | Receiving Yards | over | 0.1356458877681902 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|a5dc555d-b835-41b2-b481-a747557a08b5 | underdog | Malik Nabers | Receiving Yards | under | 0.1355033403010405 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|575f222c-106d-4acd-bb96-fa38483730e4 | underdog | Jake Ferguson | Receptions | under | 0.1353654788338305 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|6aae9f5a-fcf3-47ab-a732-e20798619a6d | underdog | Nick Herbig | Sacks | over | 0.13536125851694314 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|16051259 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.1350314279342374 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|42ef4801-1d28-442e-b42d-981aec45d842 | underdog | Caleb Hawkins | Rush Yards | under | 0.1344977882639632 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|84f62971-2d32-45a7-aa4d-7ab7e3f27a3d | underdog | Malachi Fields | Receiving Yards | under | 0.133936831108967 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|75d61aa1-7845-40a4-a1f7-85efdf585c7b | underdog | Princely Umanmielen | Sacks | over | 0.13388692782737888 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7e24c2fc-b2a9-4cda-b16f-b9bc6153a23e | underdog | Greg Dulcich | Receiving Yards | under | 0.1336970921172516 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a10c41a7-9c38-40f4-a975-b99cfceab816 | underdog | George MacIntyre | Pass TDs | under | 0.13367404203418298 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|94b93669-f3bf-42eb-8662-bd1c412798a9 | underdog | Tyler Warren | Receptions | under | 0.1328695780272055 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1c29b99d-222a-4b53-8471-6ed50763c80d | underdog | Jaylen Waddle | Receiving Yards | under | 0.13267795028063345 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|19d3a6a2-1062-45c3-a09a-3a65050bd272 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.13205782499315033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|008abfdb-bdff-4539-816c-b7f703ee2a9e | underdog | Liam Hicks | Total Bases | over | 0.1319930069930068 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b19f3052-9b2b-4892-9d9c-c814a1c421b8 | underdog | Jake Bates | FG Made | under | 0.1319024702666141 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a49fb210-9a51-4589-b092-bc9895a1ee4a | underdog | Gunnar Helm | Receiving Yards | under | 0.1316121759984837 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d74f82ee-d5f7-40d2-ac36-71cc37b42543 | underdog | Jordan Watkins | Receiving Yards | under | 0.13159640770920988 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ba49f517-710c-4051-95b6-4f8355eef1e7 | underdog | Bucky Irving | Receptions | under | 0.13158399196209436 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b1f9ad06-cd7d-4e5a-959b-569a72213b85 | underdog | Radarious Jackson | Receptions | over | 0.1315816830185312 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|565b428f-a6cf-4af8-85e6-cb5ef00a4a9a | underdog | Chase Brown | Rush Yards | under | 0.1310820845889924 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|443ec428-a877-4631-bdf4-806c0b198809 | underdog | Konata Mumpfield | Receptions | under | 0.1309218799606248 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|362a367a-8287-4a9b-afac-79b549e4c9a2 | underdog | AJ Barner | Receiving Yards | under | 0.1306153642795884 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1b176313-e08a-4847-957b-32a569fdd619 | underdog | Danielle Hunter | Sacks | under | 0.1305467838319396 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|00b01f82-0268-4b96-b82c-afd43774bbb8 | underdog | Jackson Kleather | FG Made | over | 0.1303279119894879 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|d06eefe7-d221-4b8a-847e-dacdc1cae223 | underdog | Tyrone Tracy | Rush + Rec Yards | under | 0.1301385570274678 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b832c29c-26dd-4b07-a2d1-feaa7b7e7052 | underdog | Dallas Goedert | Receiving Yards | under | 0.1296687932557064 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|02d34a8f-3eed-4486-9769-1d3795f45afb | underdog | Nick Folk | FG Made | under | 0.1295761284029778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6e2b8ba4-322a-4d4a-baf7-1f473b0b3969 | underdog | Jonathan Aranda | Hits | over | 0.1291573597776903 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7da699a4-50a1-4dd2-b233-b79054316f54 | underdog | Wayne Knight | Receptions | over | 0.1290023444417333 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|e0969448-03e0-46e5-8539-6af71c7891ee | underdog | Gavin Freeman | Receptions | under | 0.1287710162149922 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|34d055d7-33a5-4401-a090-0d03599b6aa7 | underdog | Caden Buhr | FG Made | over | 0.1283755219195639 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| prizepicks|16051245 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.1283711896398486 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|fe9a8643-cbb5-455e-917e-c33f3a025f7c | underdog | CeeDee Lamb | Receiving Yards | under | 0.1283347069925714 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|87fa81f1-4e8b-4f24-be98-1f49a7ee7f3a | underdog | Jayden Maiava | Pass Yards | under | 0.1279852222492714 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|d3c78fb1-24fb-4022-825b-11cb5e84b5fc | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.1277825349237309 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cb509be0-2b5d-4563-b28b-e94cb396030c | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.127491030204322 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|5e6dcb8e-3159-4761-a5ab-5310ee38bef6 | underdog | Justice Haynes | Rush Yards | under | 0.12703047032515302 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|26d39b80-32f6-4d20-a89d-ce35e5c3bf55 | underdog | Jaylen Warren | Rush Yards | under | 0.1269833611823008 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ab744591-112e-49f8-88d0-de9771ab275d | underdog | Zay Flowers | Receiving Yards | under | 0.1266709228488783 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|45502e2d-d93b-4cf0-9d40-efb7918831c4 | underdog | Dylan Raiola | Pass Yards | under | 0.1262659882499534 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|b49a48bd-8058-449f-9388-8e31f44083ec | underdog | Kewan Lacy | Receiving Yards | over | 0.1261368582759802 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|39d3e316-5d17-465f-b268-469f78421358 | underdog | Tony Pollard | Receptions | under | 0.1260078504794592 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0a9fbe3d-92db-484b-ba0f-ec618dfa3cd8 | underdog | Noah Gray | Receptions | under | 0.1256611502062177 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|b3bf83ab-c79a-442e-a00a-95213b95e3de | underdog | Jake Ferguson | Receiving Yards | under | 0.1255662633886676 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|9d76b014-0fc4-4360-b3c4-6c3715996d7b | underdog | Carnell Tate | Receptions | under | 0.1254536750854675 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aca97cea-9fb5-4506-b53b-cfd3352d8353 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.12451584239681568 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|d9566fef-1840-4236-9053-b188e30aeb72 | underdog | Braylon Staley | Receiving Yards | under | 0.12444674535911959 | 2026-10-23T13:31:04Z | 2026-10-24T19:30:00Z |
| underdog|90c1dd53-3be2-43de-bf0b-baf6a360086b | underdog | Jerry Jeudy | Receptions | under | 0.1240065201300302 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|eaddf12e-bf09-415a-9908-175b69e1378e | underdog | Joey Slye | FG Made | under | 0.1236431134007916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|61e7bf09-5421-4218-9b7d-53d1a654a3cc | underdog | George Pickens | Receptions | under | 0.1233908843202937 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|15945770 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1232415700497886 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|90006bf7-f321-4955-95cd-018f58fe2476 | underdog | Victor Mesa | RBIs | over | 0.1231774761186525 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|bd7409fb-5432-4e66-a7f5-17c61264dc73 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.1231584316522158 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|015228e2-4b01-423b-bc13-815d3bcc4b3a | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.12280849617456358 | 2026-10-23T13:31:04Z | 2026-10-26T00:20:00Z |
| underdog|5e206181-9207-4bfc-88c8-f03aab0fb4c2 | underdog | Kenny Gainwell | Rush Yards | under | 0.12235820841958012 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|8248b0a4-7bbb-45f0-bb6b-f4afa7b390e3 | underdog | Tyrone Tracy | Receptions | under | 0.1223478921251329 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|cdb7d26e-5b5d-44ee-b1d9-ffc08b833663 | underdog | David Hamilton | Total Bases | over | 0.1220605791387878 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945069 | prizepicks | Derrick Henry | Rush Yards | under | 0.1220323805962527 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|d6e012d6-0c25-4cdb-b92f-7acf86dff941 | underdog | LaNorris Sellers | Pass Yards | under | 0.12190293460682822 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|9023ba89-bfaa-477b-b72c-7408017ef70b | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1213989620392013 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e362134a-febb-4a49-91db-9bbff996595b | underdog | MarShawn Lloyd | Receiving Yards | over | 0.12083104520736526 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|47d2239b-9245-4a9f-a3af-efc901f6a31d | underdog | Pierre Strong Jr. | Receiving Yards | over | 0.1200814951903969 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|ed87d34a-c2b8-43de-912f-855a52740239 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.11998772384821477 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|f6e160d7-5be2-4d1e-97e5-92acd1f28d87 | underdog | William Contreras | Runs | over | 0.11992662233432694 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| prizepicks|16051293 | prizepicks | Devaughn Vele | Rec Targets | under | 0.1192863816858713 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|71d25405-940f-4f8b-abee-212c655d2faf | underdog | Dylan Edwards | Receiving Yards | over | 0.11924723227336254 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|9b47512a-afb1-4998-9a20-5d52f79cd0f4 | underdog | Junior Sherrill | Receptions | under | 0.11912444157661717 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|6f6b68bb-0f13-4a6e-960e-9aaa06bf2c88 | underdog | Richie Palacios | Hits | over | 0.1190986730781363 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|8511dcf4-aaac-4a37-8f6b-424f6fd42e73 | underdog | Sam Leavitt | Pass Yards | under | 0.11878734877496 | 2026-10-22T04:39:42Z | 2026-10-24T16:00:00Z |
| underdog|2b96e389-ec54-4965-a240-5d2e6eb051a0 | underdog | Jason Sanders | Kicking Points | under | 0.1187154660907585 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a04b010f-6f7a-4bca-bf84-a019fdc98cb2 | underdog | Jason Myers | FG Made | under | 0.1186141311795658 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e642bd88-7ada-49a6-bc3e-0426f77a3d02 | underdog | Jared Goff | Rush Yards | over | 0.1184823448445742 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|37c7f3a7-4eea-4ab7-bb95-51317d560802 | underdog | Christian McCaffrey | Receptions | under | 0.1181179607177566 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051302 | prizepicks | DeVonta Smith | Rec Targets | under | 0.1173764515336942 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|5a19d403-37ab-402e-958a-f872523cc695 | underdog | Laquon Treadwell | Receptions | under | 0.11729373694819256 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|bea4dc65-3219-4de0-9721-19a9becb8a7d | underdog | Keenan Allen | Receiving Yards | under | 0.1171946925687916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd0fc4c4-17dc-42fa-9656-b749a1f7d2ea | underdog | Blake Cashman | Sacks | over | 0.11713225592155074 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|66772312-3a35-456b-83a2-8f6715ca3611 | underdog | Will Anderson | Sacks | under | 0.117020833157628 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|fd03aa78-2c5a-4805-a861-921613637aef | underdog | Isaiah Sategna | Receiving Yards | under | 0.11678886617245543 | 2026-10-23T13:31:04Z | 2026-10-24T19:30:00Z |
| underdog|d6d91cbb-f5ff-4b1c-ae9c-9cb431a3bc9e | underdog | Junior Sherrill | Receiving Yards | under | 0.1165194099008191 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|8ac9a780-d1c0-4481-b02d-99d01d5ad8ef | underdog | Bucky Irving | Receiving Yards | under | 0.11641272640515987 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a8389eaa-f9e8-4862-9d49-e0eb14b5dbe3 | underdog | Geno Smith | Pass TDs | under | 0.1162581741290298 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9c0ab175-645e-4e81-8a2d-b2bffe22a35a | underdog | Braylon Staley | Receptions | under | 0.11553944780418735 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|d4109d54-463b-49c4-8d4a-55997cd5a25e | underdog | Jalen Nailor | Receptions | under | 0.11535940257387334 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|43da2b56-6f19-429a-884b-a4c12ba9020c | underdog | Rashid Shaheed | Receiving Yards | under | 0.1151993821374695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1b0fc4dd-38ef-4e17-85a8-e24686ccb9a1 | underdog | Drake London | Receiving Yards | under | 0.1146582581752583 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8ac96afb-46f0-4924-9765-9144862ff599 | underdog | Conor Talty | FG Made | over | 0.1146366001969039 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|2f1f417f-135b-4830-a474-fb5c75784b48 | underdog | KJ Duff | Receptions | under | 0.1145312653667987 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|f9118e9b-4b7a-443f-bdb8-c5519b8b3ba0 | underdog | CJ Bailey | Pass Yards | under | 0.11451761946720151 | 2026-10-23T04:50:52Z | 2026-10-24T02:30:00Z |
| underdog|7e65673c-68cc-43d7-8230-c848586a250c | underdog | Jonathan Aranda | Total Bases | over | 0.1141668788727612 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e85445e5-423b-403d-b942-d8c2f9c8c893 | underdog | Baker Mayfield | Rush Yards | under | 0.1140527808285041 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|6a027ba4-a559-4acd-aaab-ecdbbdaa4f47 | underdog | Griffin Wilde | Receptions | under | 0.1139519591506299 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|fa016a67-39b5-4de6-bed1-c7d5cc5acac1 | underdog | Jeremy Hecklinski | Pass TDs | under | 0.11354866650633832 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|82ab5aa5-420e-4364-bd82-207d555c2689 | underdog | Sam Darnold | Pass Attempts | under | 0.1133043312291657 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|b4fdcabe-4236-4ba3-b391-25a3dce3c454 | underdog | Cam Coleman | Receptions | under | 0.1130325570488033 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|d2269243-dd1c-4eca-a291-5a694b2fae84 | underdog | Tommy Carr | Rush Yards | over | 0.11293957548012523 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|157bb4f2-7d8e-46e6-bbc2-d96f6ce7d1ef | underdog | Eric Wilson | Sacks | over | 0.11293704759554901 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|f6e4d0b0-e037-405e-b285-07e6fe26eedb | underdog | Cooper Pratt | Hits + Runs + RBIs | over | 0.1129325344089059 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|85560838-e552-4d85-8d61-33d8f0a1f89e | underdog | Brock Purdy | Pass TDs | under | 0.112816096678015 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c4a30c98-3ee5-437f-83ee-cef25c93d92c | underdog | Travis Kelce | Receptions | under | 0.1120341726504789 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| prizepicks|16051278 | prizepicks | Tre Tucker | Rec Targets | under | 0.1120161055590794 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|6de3d3ef-7eba-4e16-9998-bb5cfa3f3ec9 | underdog | J'Koby Williams | Rush Yards | under | 0.11181066919349392 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|fcafb323-e005-4a22-964c-ea114b457bc0 | underdog | Deshaun Watson | Rush Yards | under | 0.1115471354898498 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051309 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.1111545654187005 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|cc4bf360-0930-4b3a-baa3-7fc97323ef5e | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.11106185769546062 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|d06fae69-fd00-458d-9aa6-209d3b9736f0 | underdog | Cam Skattebo | Receiving Yards | over | 0.1109557452316625 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|2f03ca60-0a15-44c5-92f4-51e5ced470e7 | underdog | Jalen Coker | Receiving Yards | under | 0.1109302760189151 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|709c73c7-0fe0-4b09-a6ec-8f6ddd312747 | underdog | Junior Caminero | Hits | over | 0.1108421213934509 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|959728b4-52ed-4783-ad59-ef31f5becd2e | underdog | Christian Watson | Receiving Yards | under | 0.1105929494288048 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16051234 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.1104253678764338 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|5c1d01bf-5469-4fb9-a3ad-d8a4de3206a2 | underdog | Spencer Shrader | FG Made | over | 0.110097123969825 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|35f9a380-30b1-45fb-8e8a-61aa1d40b25a | underdog | Liam Hicks | Runs | over | 0.10995670995670997 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|13305a5c-f079-40ce-8413-3bc5b8b0dd5d | underdog | Rodney Fields | Rush Yards | under | 0.10941526633943055 | 2026-10-23T04:50:52Z | 2026-10-24T19:45:00Z |
| underdog|cba6f501-aa84-445a-8f9c-d04ca3c7fb33 | underdog | Jordan Dwyer | Receiving Yards | under | 0.10876287533414564 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|3b766a66-0018-4174-9c44-850d7caef285 | underdog | Matthew Stafford | Pass Attempts | under | 0.1082286184366853 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|0466576a-af31-4e3c-a0a7-17f51d4042f9 | underdog | Alberto Mendoza | Pass Yards | under | 0.10811122211051938 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|b01b4479-d0ff-4f0b-aa25-8572040fd5fb | underdog | Logan Hall | Sacks | over | 0.1080312577396586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|597aae0e-eb41-4ea7-83b4-6a1df4cade0f | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.10763526224208053 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|c37e171f-5e70-4561-abd4-a2dca0b9ba20 | underdog | Mason Taylor | Receiving Yards | under | 0.1075683290440285 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051260 | prizepicks | Jameson Williams | Rec Targets | under | 0.1071890637021601 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16087733 | prizepicks | Gauthier Hein | Shots | under | 0.10685777837272048 | 2026-10-23T04:50:52Z | 2026-10-23T14:45:00.000-04:00 |
| underdog|fd02b717-c3a5-4e7d-91cb-9989e22c31cd | underdog | Patrick Mahomes | Rush Yards | under | 0.105668666481013 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0660c889-a4a5-4941-beff-bf58b7b65837 | underdog | Deshaun Watson | Pass TDs | under | 0.1056653767810689 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|32c6a58f-4543-44ab-9513-73e8857d24bb | underdog | DK Metcalf | Receptions | under | 0.1054909425928073 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5549b40f-c25b-4262-aa4b-46e8542b8221 | underdog | Brock Bowers | Receptions | under | 0.1052220927493255 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|f8e1e49f-cc5f-43e5-910e-84dc1bb53c3a | underdog | Jaziun Patterson | Rush Yards | under | 0.1052016470706469 | 2026-10-22T04:39:42Z | 2026-10-24T19:30:00Z |
| underdog|ea37df82-0d35-4f1b-acc4-e9a83779e8c9 | underdog | Conner Weigman | Pass TDs | over | 0.1050716675351449 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|65ed8d6f-70cd-4f13-9b37-fff2700d0487 | underdog | Troy Franklin | Receiving Yards | under | 0.1046037934121351 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| prizepicks|16051301 | prizepicks | Dallas Goedert | Rec Targets | under | 0.104508400091262 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|0d312971-5e90-44b0-98ba-ce4e6f8abf3e | underdog | JC French | Pass TDs | over | 0.1041573990796 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|7bddc13b-1e8e-4ba5-8052-bb3dca935528 | underdog | Ashton Jeanty | Rush Yards | under | 0.1036891044730264 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|57571695-f9a3-476b-80b4-a9524aaec87b | underdog | George MacIntyre | Pass Yards | under | 0.103588549629116 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|54680c7c-61e6-4921-be29-813cc4a2f7ce | underdog | Denzel Boston | Receptions | under | 0.1035724114812719 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051244 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.1034529192752869 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|bb10c724-592c-4e93-89f8-55f339b3ee9d | underdog | Brice Turang | Total Bases | over | 0.1032412965186075 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|548416c7-0afb-4659-9d00-251696eab277 | underdog | Jared Curtis | Pass Yards | under | 0.1032303512801479 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|66a12d68-7694-45bf-bff5-0baebc9e9694 | underdog | Brandon Aubrey | Kicking Points | under | 0.1027789805682906 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1aa26c70-6b43-441b-8b06-9f607ccf83f7 | underdog | Aidan Chiles | Rush Yards | under | 0.10270237748131861 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|99f7d836-efd8-4905-b9e8-aa0fa8d4379b | underdog | CJ Bailey | Pass TDs | under | 0.1023031786424184 | 2026-10-21T23:24:30Z | 2026-10-24T02:30:00Z |
| underdog|820386fd-f6a7-4a4f-b07b-4e867332ff05 | underdog | Tony Pollard | Receiving Yards | under | 0.1020926537605008 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16025299 | prizepicks | Wayne Knight | Rush Atts | under | 0.10184668395682339 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|f1ec3633-09db-4631-8122-d6237233bafd | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.10173252534256966 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|a918ff3a-256c-4ff1-99f8-a76599f5eb5a | underdog | Trinidad Chambliss | Pass TDs | over | 0.1015714872609133 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|883c9554-18e2-4c83-a8e4-86d5eff8ca2d | underdog | JC French | Rush Yards | over | 0.1013785104343703 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|cb6b3385-177c-4f4c-a76f-851fc6f581d6 | underdog | Christian Yelich | Total Bases | over | 0.1012237762237762 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|ff61b03d-9f28-44a0-ab24-2363edfd3351 | underdog | Travis Kelce | Receiving Yards | under | 0.101127840693776 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| underdog|3b079c5e-ac07-42c8-af8a-98041f6f8dfa | underdog | Victor Mesa | Hits | over | 0.1009844763480287 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|5bee9c19-46e7-45de-9505-7fffe7682621 | underdog | Colton Joseph | Pass TDs | over | 0.1009178937061043 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|0a8e9968-79e9-4e19-9777-a06b21b6c1c3 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.1007112845271449 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|bdd208dd-4e0d-4782-960c-7392e03373a9 | underdog | KJ Duff | Receiving Yards | under | 0.1006835033376762 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|4cb67320-4cea-4a1f-a732-f390fda796c2 | underdog | DeVonta Smith | Receptions | under | 0.10038240853526892 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|475dffcf-6add-49a7-acb4-e5fff9ff48a5 | underdog | Keelon Russell | Pass Yards | under | 0.10038147091438865 | 2026-10-23T13:31:04Z | 2026-10-24T19:30:00Z |
| prizepicks|16051305 | prizepicks | Germie Bernard | Rec Targets | under | 0.0999657351122397 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|01d3fe0d-6df4-4d43-91ed-c5a1aebc74a2 | underdog | Mark Andrews | Receptions | under | 0.0998519844527912 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|d534137b-8378-4ede-9c7f-1768901647d8 | underdog | Avery Johnson | Pass Yards | under | 0.09978109233236221 | 2026-10-23T04:50:52Z | 2026-10-24T19:45:00Z |
| underdog|557db697-20ab-4b71-b516-64a4afeb68ce | underdog | Aidan Chiles | Pass TDs | under | 0.0996663803350599 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|01d7bd14-2cea-4655-87f7-1df94b0cfe7e | underdog | Nick Folk | Kicking Points | under | 0.09955642389684627 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|d19378d4-7b16-452b-906d-5f161be21dda | underdog | Victor Mesa | Total Bases | over | 0.0994475138121546 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9a70aa52-1fd9-4201-bc6d-d00ebd15f2d7 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.0993449768275279 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|27667dcb-daf2-4997-9395-bcd047c330ad | underdog | Bam Knight | Rush Yards | under | 0.09929573906889211 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|602ad854-cba6-4aa9-938a-771d9ab27f0d | underdog | Tyler Higbee | Receiving Yards | under | 0.0990552102507815 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|81ae88d0-af73-4cfc-80cd-8580d1ab72f3 | underdog | Tait Reynolds | Pass Yards | under | 0.09830056944410115 | 2026-10-23T13:31:04Z | 2026-10-24T23:00:00Z |
| prizepicks|15945774 | prizepicks | Jaylen Waddle | Rec Yards | under | 0.0982250040001608 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|f306a99b-5a55-45d9-aab8-d30c63bd7613 | underdog | Dylan Raiola | Pass TDs | under | 0.09799020020333293 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|ab1c3f52-8d19-4a07-8886-0d55bab8d009 | underdog | William Contreras | Total Bases | over | 0.0978456373156402 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7d98395f-f4ec-4d64-9c69-e4f7cc2131a7 | underdog | Jake Bates | Kicking Points | under | 0.0977903849845823 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d969d472-0006-49a6-96a1-39c0ce1cf08e | underdog | Dylan Lonergan | Pass Yards | under | 0.0976455339561735 | 2026-10-22T04:39:42Z | 2026-10-24T16:00:00Z |
| underdog|617cc43d-1693-42d3-baf7-6c7b2f500635 | underdog | Darnell Mooney | Receiving Yards | under | 0.09754939271681284 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|785d8153-ed65-433a-98ff-d1df6189376b | underdog | Kyler Murray | Rush Yards | under | 0.09745252830194728 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|724bb94f-576e-4f8b-93a8-be17d494866c | underdog | Dakorien Moore | Receptions | under | 0.0970600476350808 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| prizepicks|16051262 | prizepicks | Christian Watson | Rec Targets | under | 0.096747312779029 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16010772 | prizepicks | Brock Bowers | Recs | under | 0.09671057143934203 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|884c4ba2-bfd4-41b9-bd3f-b6fe530a612a | underdog | Yannick Smith | Receiving Yards | under | 0.09655701454779198 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|43184486-3e8e-4267-8bf4-7ffe1ae25813 | underdog | Chandler Simpson | Runs | over | 0.09637531822039036 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|0d97a0f7-4b3c-4896-afc7-5e08cbd83e12 | underdog | David Hamilton | Runs | over | 0.09637531822039036 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|56e0f4b6-c8b5-4080-a302-a23c5afdfed8 | underdog | Christian Watson | Receptions | under | 0.0962434061653429 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|7fcb6e7d-fbad-444a-ab90-a9fa1175351d | underdog | Jayden Maiava | Pass TDs | over | 0.0960556570545642 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|740f3e34-29ab-4fed-ae75-13f0bc56660e | underdog | Tyler Loop | Kicking Points | under | 0.0958446334098082 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d1654863-f01c-47db-9d4f-a80c3bb9857c | underdog | Marvin Mims Jr. | Receptions | under | 0.0957341704310761 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|7ed37d87-d675-4f6c-a0ff-8bad34041ac7 | underdog | Jake Bauers | Hits | over | 0.0957158320205936 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|ca7aafa2-8aa7-40d7-943b-d0b95afb247d | underdog | Bryce Lance | Receiving Yards | under | 0.09563747315955529 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945789 | prizepicks | Travis Kelce | Rec Yards | under | 0.0956329735871087 | 2026-10-21T04:43:18Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|25ed5f3f-a2de-45eb-b5dc-ebf775b350ce | underdog | Andre Szmyt | Kicking Points | under | 0.0952743873816968 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0f7916e4-5189-45ec-81bd-8741389faad3 | underdog | Chandler Simpson | Hits + Runs + RBIs | over | 0.0946840065898005 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cdb7df08-b122-4746-b6a4-f1a28a8a2189 | underdog | Isaiah Marshall | Pass Yards | under | 0.09456768606542931 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|6a798cc2-869f-4765-8413-cbdeb21f919f | underdog | Dylan Lonergan | Pass TDs | over | 0.0945615929103332 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|70d3eee2-da03-4988-a667-14a183033678 | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.094209080703896 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fe80682c-0e04-450e-9223-a949ee5399b5 | underdog | Junior Caminero | Total Bases | over | 0.093964858670741 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|5f059838-bf65-4a1c-b367-0439087f5356 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.0935892146626595 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e101f669-6227-48bc-9a08-5a2c1cad57df | underdog | Isaiah Sategna | Receptions | under | 0.0935543794942828 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|0123e5c7-742c-4880-bf17-c3c0b8599a9a | underdog | Walker Eget | Pass TDs | over | 0.0934927299248743 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|b2a7fda4-f58c-4ca3-9951-f635bcaafabd | underdog | Byrum Brown | Pass TDs | over | 0.0933369173961139 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|a8968aa0-639f-4060-a9da-d2f86ffc4e98 | underdog | Jackson Kleather | XP Made | under | 0.0924910603851204 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|61f4cf0f-c609-4ce9-99ff-1b7e55132d14 | underdog | Caleb Douglas | Receiving Yards | under | 0.0924857504634089 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ddd1d82b-b64d-4ead-8c47-1606dfc1f449 | underdog | Kenny Minchey | Pass TDs | under | 0.0924523671302844 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|280d7041-8b6c-4dd7-8d58-69f9ecb8dc19 | underdog | Felix Anudike-Uzomah | Sacks | over | 0.09223808023020835 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|5e49237b-efd4-43c0-b1c9-1e896f1e1de8 | underdog | Rashod Bateman | Receptions | under | 0.09202654093256402 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|87bada19-4885-4bf7-b204-c0ce4a6b5d96 | underdog | Junior Caminero | Batter Walks | over | 0.09162821357943313 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|d2968887-1877-4e52-8478-b20b88c59272 | underdog | Kayshon Boutte | Receptions | over | 0.0913518404432818 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3f2f4cff-6fe0-43cb-8d2f-b4911865eb3e | underdog | Griffin Wilde | Receiving Yards | under | 0.0912305106518043 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|c662b147-2a50-4c88-9c7b-ef28c09fba3d | underdog | Daniel Bellinger | Receiving Yards | under | 0.09110150359713487 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|3ecdcb49-c03e-4d63-a80e-749bfc200637 | underdog | Cam Cook | Receiving Yards | over | 0.09080804337147019 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| prizepicks|16105111 | prizepicks | John Mateer | Pass Attempts | under | 0.09061174207972733 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|0e8858a7-5fb6-4ffd-a010-eddbbedf1bf6 | underdog | Alvin Kamara | Receptions | under | 0.0905814183401232 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|16046141 | prizepicks | Jared Goff | Pass TDs | under | 0.0902817486338214 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|9f6dbce0-450c-4427-a7ec-510843b8a5a6 | underdog | Brice Turang | Hits | over | 0.0902807986020555 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f10e571c-0024-481c-b4a0-9ab2de9ad060 | underdog | Darnell Washington | Receiving Yards | under | 0.090128614048436 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| prizepicks|16051316 | prizepicks | Carnell Tate | Rec Targets | under | 0.0899755364779774 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|245d329e-170d-471b-b37b-153a8bee8e51 | underdog | Jalen Coker | Receptions | under | 0.089640605964081 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16087496 | prizepicks | Egil Selvik | Goalie Fantasy Score | under | 0.08949309820512041 | 2026-10-23T04:50:52Z | 2026-10-23T14:45:00.000-04:00 |
| underdog|791fc351-e3f2-4e01-ac2e-95d1dc1a3341 | underdog | Daniel Jones | Rush Yards | under | 0.0893167984596011 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0d3d5682-5da9-440e-b1f4-787f722538c4 | underdog | Scott Starzyk | XP Made | over | 0.0889396502448031 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|116be46b-f1d4-4310-8f46-e94563e753fb | underdog | Elijah Higgins | Receptions | under | 0.0886534112656307 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|5d1285be-3124-43f6-9931-914d5d6ecd90 | underdog | Dane Pizzaro | FG Made | under | 0.0885618352728215 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|cf64c5a7-a46c-4618-92ce-b662047529d7 | underdog | Devon Dampier | Rush Yards | under | 0.0883622175863563 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|d2ab21f7-0981-4373-b2f1-b655b1b5e06b | underdog | Richie Palacios | Hits + Runs + RBIs | over | 0.088261718634943 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b010c44c-10f7-453e-a045-7af6bf464967 | underdog | Tommy Tremble | Receptions | under | 0.0881185917029142 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|9113a280-1a8d-4edc-b368-bac99ea17df4 | underdog | Michael Mayer | Receiving Yards | under | 0.0875972794063874 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|c4fc0e83-fc68-45f7-b838-9b795f4a517e | underdog | Richie Palacios | Batter Walks | over | 0.08756805807622503 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|76b095a2-bf24-4b3d-879a-bc4dbdfe4bc6 | underdog | Darian Mensah | Pass Yards | under | 0.0862435305790116 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|8022d176-f92f-45ef-b9a8-b960f6f2cddd | underdog | Jacoby Brissett | Rush Yards | over | 0.086207431678947 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|08b907c1-c47c-4a9f-8cf9-b043a2a100b3 | underdog | Cooper Kupp | Receiving Yards | under | 0.086095710674828 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|73b1aafd-baaa-4ff9-97b8-72eee79cadd9 | underdog | Tre Tucker | Receptions | under | 0.0860413061365301 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a8260b4c-a079-4809-a57f-8616228e7d15 | underdog | Bijan Robinson | Rush Yards | under | 0.08591905310287928 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|58fbf850-966d-44ca-b1d0-e9818a1a2490 | underdog | Bear Bachmeier | Pass Yards | under | 0.0858770865616204 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|2d66c2c2-8b03-45a0-a98b-5cfdc6585f75 | underdog | Darnell Washington | Receptions | under | 0.0851684391460022 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|84d99d91-e7f4-4a28-9faf-3da2729847a0 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.0846102335479987 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|be4cbc1a-8a5d-4c12-8410-2bc6c9858974 | underdog | Sheldon Rankins | Sacks | under | 0.0843381307351941 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|573631cf-53e6-4bd4-bc65-8708981cff8f | underdog | Blake Corum | Rush + Rec Yards | under | 0.0837213148980291 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|fa0f28ce-b297-4b31-abea-d5617a1dd43f | underdog | Brock Wright | Receiving Yards | over | 0.08352861013723534 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|56f293ed-4635-4cc3-833c-4ed9a375750c | underdog | Tee Higgins | Receiving Yards | under | 0.0834112064258462 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2816aaad-c9d9-4cd5-ad6d-58de25217f97 | underdog | Michael Mayer | Receptions | under | 0.0834003397411226 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|50636f28-b556-4195-9780-5aff7702ef87 | underdog | Malik Willis | Rush Yards | under | 0.0832931322442289 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ccd3866e-e39d-4402-bb01-bbd92ca68ab9 | underdog | Spencer Shrader | Kicking Points | over | 0.08317987244058994 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|90a7f7cb-14ab-4b95-9ff3-43ba9205e63e | underdog | Holden Geriner | Pass Yards | under | 0.08315275215319684 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|ba6a7b98-429b-495e-8b9a-c3c97d70ff2e | underdog | Tyjae Spears | Rush + Rec Yards | over | 0.08298512096055805 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|eccb476e-a91b-42b6-a4db-5ec7da7769cb | underdog | T.J. Moore | Receiving Yards | under | 0.0825764110815296 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|1b806f20-be44-49e6-8f59-766270beb2b9 | underdog | Jason Myers | Kicking Points | under | 0.0825404894860757 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|ee420202-642a-4ac6-988b-e2cce1adb4b5 | underdog | Isaiah Likely | Receptions | under | 0.0825217515739429 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cdbf5446-2666-4953-8fed-2a23abfb628d | underdog | Kenneth Walker III | Rush Yards | under | 0.0822691396401671 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|3b0eb78b-d28f-46ab-8459-886657d5c203 | underdog | Isaac TeSlaa | Receptions | under | 0.0822432608821583 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3fdf958b-4aeb-446f-a872-8228a3fb7690 | underdog | Kendrick Bourne | Receiving Yards | under | 0.0821950618308543 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|98c8557b-1ef7-4740-bad9-9c76cec26da1 | underdog | Dohnte Meyers | Receiving Yards | over | 0.08147385061303802 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ddab0bd3-7a9d-4f8f-b818-b843cc34659c | underdog | Aidan Laughery | Rush Yards | under | 0.08142683550601237 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|cbbed3b9-1596-44f6-937c-6747d065344b | underdog | Bam Knight | Rush + Rec Yards | under | 0.08141747575278768 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|9e6f6020-6713-4bcd-9cf4-bfca8ffb5165 | underdog | Christian Yelich | Batter Walks | over | 0.0813381069590513 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| prizepicks|16051290 | prizepicks | Jordan Addison | Rec Targets | under | 0.0810609688919091 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|cfa707d3-c8b9-477e-80c2-22c924cedaa6 | underdog | Daniel Carlson | Kicking Points | under | 0.0807323556687517 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|73fdb8c0-cd85-4ead-8b5d-106ec0f6c09a | underdog | Woody Marks | Receptions | under | 0.08057939082420718 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|39f1f9a0-e7a0-4cb4-87ee-7308d19c7841 | underdog | Kendrick Raphael | Rush Yards | under | 0.0803878760950758 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|41308d6a-1585-4bd8-88a3-c4fc5587e979 | underdog | Jason Sanders | FG Made | under | 0.0803782078621125 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e7b42cef-9825-40e6-860f-1e9a984e2a86 | underdog | CJ Donaldson | Rush + Rec Yards | over | 0.08021649795639368 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|fa91546b-2faf-49cd-aa41-3929b7a7a669 | underdog | Chase McLaughlin | FG Made | under | 0.0799826010276563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5a015a20-1646-49b0-905f-1e21fef83b11 | underdog | Jayden Savoury | Receiving Yards | over | 0.0798869647179381 | 2026-10-22T04:39:42Z | 2026-10-24T19:30:00Z |
| underdog|95ad8fe3-e38f-47b9-af72-6411261e19b6 | underdog | Quinshon Judkins | Receiving Yards | under | 0.07918115619319599 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e091a42a-e0f8-44c0-8b29-4d4f96450333 | underdog | Jaylen Raynor | Pass Yards | under | 0.0788511546485264 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051285 | prizepicks | Caleb Douglas | Rec Targets | under | 0.0785950926735681 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|357d1c55-39ca-4e80-8e47-b9b3fb1d91e6 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0783802647011688 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051235 | prizepicks | Chuba Hubbard | Rec Targets | under | 0.0781746328140772 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|fa1b7315-d8c5-468f-b057-1c96d70246da | underdog | Rodney Bullard | Receptions | over | 0.07805976093610967 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|0d25c245-efca-4a13-baed-2eda4672ccf9 | underdog | Mike Gesicki | Receptions | under | 0.0779878372316424 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|cd41b2b9-c7a0-45df-bcc2-de420b13148a | underdog | Bucky Irving | Rush + Rec Yards | under | 0.07790152531371486 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ed020878-152d-4eb0-8ab1-fcce6f111e2b | underdog | Lloyd Avant | Rush Yards | under | 0.07759199481976553 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|6f06d48f-cce9-442a-8a93-5cd9c028fdb1 | underdog | Ollie Gordon | Receiving Yards | under | 0.07744253798791922 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|0b11598f-d6c1-4460-8dd2-be4346f61ed8 | underdog | Dylan Edwards | Rush Yards | under | 0.07729934663216664 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|99192d3b-e302-42f3-b7ab-2ff5db8b8a4e | underdog | Drake Lindsey | Pass Yards | under | 0.0772448058323824 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|ba245851-18e0-4e22-a6af-94dacecb7c22 | underdog | Nate McCashland | FG Made | over | 0.07717406962284173 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|9a23291c-d740-46d9-b862-79e3ebb3d2a5 | underdog | Derrick Henry | Receptions | over | 0.0769349421556845 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|70b33786-1ff1-4ddc-8055-ed50d818650e | underdog | Sal Frelick | Hits + Runs + RBIs | over | 0.07689360619974517 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|26cd3467-0e84-45ff-96dc-d727a8953a71 | underdog | Cooper Pratt | Total Bases | over | 0.0768344484855214 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16090040 | prizepicks | Caleb Hawkins | Rush Atts | under | 0.07682306799504812 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00.000-04:00 |
| underdog|4ae9c51c-8cf7-4564-b275-80212e884b36 | underdog | Garrett Mitchell | Batter Walks | over | 0.07675095099574858 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| prizepicks|16051273 | prizepicks | Travis Kelce | Rec Targets | under | 0.0766485815662542 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|88e69978-4804-40b0-acdb-45afd1ba4233 | underdog | Jaylen Raynor | Rush Yards | over | 0.07663471577183145 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|63e1975c-17e2-4f9c-bfaf-a709d8598e32 | underdog | Jaron-Keawe Sagapolutele | Pass TDs | over | 0.07631036348985182 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|cb547cf1-514a-4f86-a033-a83a85347487 | underdog | Beau Pribula | Pass Yards | under | 0.0761872661390257 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|800b748f-4cf3-4101-a0bf-a1e92185df52 | underdog | Walker Eget | Pass Yards | under | 0.07616135268485114 | 2026-10-23T13:31:04Z | 2026-10-23T23:00:00Z |
| underdog|23cc4a0a-23c5-4e37-98c2-b2ff5ed850aa | underdog | Trey Smack | FG Made | under | 0.0758399666432347 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5df27532-04eb-405c-b458-1cfd5b5b6c3a | underdog | Malik Nabers | Receptions | under | 0.0758087558960143 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|44f20002-9789-4c75-9583-99868acf6a17 | underdog | Javarius Green | Receiving Yards | under | 0.07575188720103154 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|d266a85d-a66d-406b-bea5-4b7215c34d91 | underdog | Devaughn Vele | Receptions | under | 0.0757194055785056 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ae60f3a8-a9ed-4acf-b13f-fdc17f7013f9 | underdog | Michael Penix | Pass TDs | under | 0.0756786003884431 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d49f6c62-edd5-4fe3-9832-a4d3f48f15ec | underdog | Brendan Baird | FG Made | under | 0.0756708302222249 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| prizepicks|16051237 | prizepicks | Jalen Coker | Rec Targets | under | 0.0752314568085358 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|b7633e2a-8c11-4ada-8bd1-ddacccbf8dcb | underdog | Kenneth Walker III | Receptions | under | 0.0750174077225467 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|f25ffd07-3f96-4391-a7b4-6f6d04a0fc54 | underdog | Yandy Díaz | Hits | over | 0.0749959435830694 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fa6b3d2e-4ca3-4536-8709-91606f82acdb | underdog | Jared Goff | Pass TDs | under | 0.0748246656634097 | 2026-10-22T04:39:42Z | 2026-10-25T20:25:00Z |
| underdog|c3d10d56-b8f3-4d0a-bd84-e55ece65a8f1 | underdog | Joe Jackson | Rush Yards | under | 0.07480092017414575 | 2026-10-23T13:31:04Z | 2026-10-24T19:45:00Z |
| underdog|dfbe2fbb-ed28-4fbb-8781-5bcac4758534 | underdog | Drew Sample | Receptions | under | 0.0745894946131864 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f840b552-3515-4584-9d35-d37fca257b1f | underdog | Chris Olave | Receiving Yards | under | 0.0744110380898498 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|d9a8338f-0c9f-47bf-95ed-3d25faaff51a | underdog | Jordan Whittington | Receptions | under | 0.07435492868539906 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|186e0ace-b3a3-4d78-83c7-1cf9b0fc8393 | underdog | Jahan Dotson | Receiving Yards | under | 0.0741904379865594 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051313 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.0741620403956118 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|0b37fb47-ebdc-4010-bcf5-622c00a374ac | underdog | Devon Dampier | Pass TDs | over | 0.0738331610963063 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|0aebbe26-4a4c-460b-b0b7-07b5fd2bc1ce | underdog | Jonathan Aranda | Batter Walks | over | 0.07373532068654026 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|6aa8f84a-2ea9-4946-a243-4ba0a07c3993 | underdog | Ollie Gordon | Rush Yards | under | 0.0737138149062139 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e2e5065-8c00-4fbf-8932-920f5872117c | underdog | Isaac Wilson | Pass Yards | under | 0.07370820859155769 | 2026-10-23T13:31:04Z | 2026-10-24T23:00:00Z |
| underdog|455a71ba-1e78-4b27-8f94-d0afeba7b6fa | underdog | Kyren Williams | Receptions | under | 0.07341233571119932 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|27fb02f5-b3f7-4c9b-bf6f-2e51e4336088 | underdog | Austin Hooper | Receptions | over | 0.07334873265912745 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|1e6dcf52-47f9-487f-ae1e-f4976a392121 | underdog | Legend Glasker | Receptions | under | 0.0731708661649952 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|6664dbee-84f6-4192-97a8-e1086c85f73b | underdog | Chase McLaughlin | Kicking Points | under | 0.0730635220054324 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ab4700cd-4ca2-4863-ac85-6301c804c057 | underdog | Mike Matthews | Receptions | under | 0.0726184227012455 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|25cd8759-8e2c-4914-8307-9dd5249af06b | underdog | Drew Wagner | Receiving Yards | under | 0.07256598868461706 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|1ccf19eb-95c4-4223-b46a-50da910203fa | underdog | Davis Warren | Pass Yards | under | 0.07250515863819518 | 2026-10-23T13:31:04Z | 2026-10-24T02:30:00Z |
| underdog|4454d8f6-93b5-4c97-b913-449717cee8bc | underdog | Cam Skattebo | Receptions | under | 0.07246523258444959 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e26442d1-e193-41a1-b88c-71f0f33d3168 | underdog | Evan McPherson | FG Made | under | 0.0722696105068416 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|19f22021-b6a3-47ea-9ac3-f58c262c7593 | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.07217465091352959 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|3a57a428-3d1c-4885-a1f8-5ee034f590aa | underdog | Javarius Green | Receptions | under | 0.072102008775498 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|dec83796-a559-4c28-b27a-563b6106bd80 | underdog | David Hamilton | Hits | over | 0.0720133292783155 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16047018 | prizepicks | Darnell Washington | Recs | under | 0.07187451637324271 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|83952101-4b7a-488e-92a8-f2da161b929f | underdog | Garrett Mitchell | Total Bases | over | 0.0718093228573808 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a4ff4488-c410-4fb1-93bd-6846607552af | underdog | Jordan Love | Rush Yards | under | 0.071463102847337 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|01c34076-3545-4337-860f-0fbcb59b943c | underdog | Malachi Toney | Receptions | under | 0.07140797471389948 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|f8efa2fa-32af-4349-8958-6f4b28ce4826 | underdog | Victor Snow | Receiving Yards | under | 0.0713608377167683 | 2026-10-21T23:24:30Z | 2026-10-24T02:30:00Z |
| underdog|78ad2055-2f47-42e4-8a8b-1662a8a49ad7 | underdog | Ty Dieffenbach | Pass TDs | under | 0.0711863086593506 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| prizepicks|16051261 | prizepicks | Sam LaPorta | Rec Targets | under | 0.0711809713072434 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|99755d9f-1fcb-4c11-b802-6d9aa0b6d23c | underdog | Elija Lofton | Receptions | under | 0.0711106431709001 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|052ab564-9a0a-4629-83a6-8bb879b4a0d6 | underdog | Kyle Pitts | Receptions | under | 0.0710490294424133 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|505cea21-7e6d-4f0c-a89b-2ea84e5055b9 | underdog | Josh Hoover | Pass TDs | over | 0.0710140089136008 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| prizepicks|16089117 | prizepicks | Taylor Fritz | Total Games | over | 0.07095837171967034 | 2026-10-23T04:50:52Z | 2026-10-23T09:10:00.000-04:00 |
| underdog|6836add1-e50e-4ec1-86cc-eac77a9f1a17 | underdog | Kyren Williams | Receiving Yards | under | 0.07083989094132515 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|3ba9f0f6-fbd1-4fe2-8699-b93baa48518b | underdog | Nick Martinez | Strikeouts | over | 0.07077283524877742 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|00946ae8-e51a-4625-8b97-ccea92a33ea1 | underdog | Chris Boswell | Kicking Points | under | 0.0706516180970466 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|2ded917a-7a76-4d1d-b255-35ed92207746 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0705952618185794 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6eb4ceca-ab6e-4b70-b779-c61fd77dcb3a | underdog | Emmett Johnson | Receiving Yards | over | 0.0704807198097645 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|408571bc-53da-472d-bbb4-e599e75b62f5 | underdog | Trinidad Chambliss | Pass Yards | under | 0.0703578542110781 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|3b0d8900-c970-4417-bc6a-2f5501367c92 | underdog | Malik Knight | Receptions | over | 0.07019802165511752 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|24312ff1-78a8-4546-a295-0dc2eb910b54 | underdog | Aaron Rodgers | Rush Yards | over | 0.0700844647787815 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|00aa1266-017b-4d1d-9745-2d4a2b1e4a7d | underdog | LaNorris Sellers | Pass TDs | over | 0.0699838081654409 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|b6b740f6-7ef3-4ea2-9a60-5b7d3258064d | underdog | Maxx Crosby | Sacks | over | 0.06992804715941348 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051306 | prizepicks | Jaylen Warren | Rec Targets | under | 0.0699206862123872 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|7b1fc2af-71c5-48df-88b9-857ea04dbd55 | underdog | Wayne Knight | Receiving Yards | over | 0.06955506893018204 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| prizepicks|16051239 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.0694964909576487 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|9f8ce159-b80d-401d-bf13-9146b2ff57c0 | underdog | Quinshon Judkins | Receptions | under | 0.06949508244536684 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|15944963 | prizepicks | Jared Goff | Rush Yards | over | 0.0694248099013491 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|b977e7ae-9c34-47cb-be90-ee68ad34fdd9 | underdog | Cameron Heyward | Sacks | over | 0.06931539209198773 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|16051253 | prizepicks | Evan Engram | Rec Targets | under | 0.0692857795326448 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3bf0ae23-cfa7-4794-94a6-195093503861 | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.0691532959067324 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|ec550da2-dccb-4258-8ffb-682546bd8a58 | underdog | Wayne Knight | Rush Yards | under | 0.06905382801501858 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|efdd7f35-7c44-4ace-98c2-a182d44e5953 | underdog | Kevin Jennings | Pass Yards | under | 0.06903682342103612 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|abe1f5d9-3690-4b8a-991e-436bd87b5318 | underdog | Evan Engram | Receiving Yards | under | 0.0687422940230393 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a402b43a-79ba-45b6-97ea-29901106333c | underdog | Jared Curtis | Pass TDs | over | 0.0687053103943738 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|335a1947-39f1-4a26-890f-827cfc2f3188 | underdog | Darian Mensah | Pass TDs | over | 0.0686136038680533 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|0e53a9d0-d0b0-4cb8-97d3-bf576202f434 | underdog | Jonathan Aranda | Runs | over | 0.06855657026889905 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|eb11db4a-744a-4042-b577-ce976667973d | underdog | Christian Yelich | Hits | over | 0.0685536491453252 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|81b3e5a2-a320-46b5-819c-31907d2b0d4a | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.068445975150984 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|6d20371c-7b8f-482f-a586-86f39d4ca35f | underdog | Gianni Spetic | XP Made | over | 0.06841584523129846 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|9367740f-79eb-4f66-857a-a6e484e66a92 | underdog | Malik Knight | Receiving Yards | over | 0.0682003490907852 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|3eb3094e-9987-486a-9ed9-5bdc8cf799d9 | underdog | Zachariah Branch | Receptions | under | 0.06806583715894199 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|5ad27210-0e96-415e-92ed-873fdfd0d6d0 | underdog | Wyatt Young | Receiving Yards | under | 0.0675393856611779 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|e3b4cb15-bd32-41fe-997b-31ef2b3d248e | underdog | Jonathan Taylor | Receptions | under | 0.0674513078149925 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea2dc53f-bd18-4fa7-875b-0d4d97360754 | underdog | Laquon Treadwell | Receiving Yards | under | 0.0671153960295503 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ea6ed2c7-17c9-4c9d-8c49-45aad8a8143e | underdog | Micah Ford | Rush Yards | under | 0.06698195362320136 | 2026-10-23T04:50:52Z | 2026-10-24T02:30:00Z |
| underdog|6ea455bd-70ea-466d-acca-bfb1488fe8a5 | underdog | CJ Baxter | Rush Yards | under | 0.06696814176614518 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|bb4be0ab-ce90-442b-865c-47a4d263721c | underdog | Ayden Greene | Receiving Yards | over | 0.06690110040706054 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|3e1887c5-46be-4b0c-a61e-08d031ee08c7 | underdog | Josh Hoover | Pass Yards | under | 0.06687467641827971 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|3ba86dc2-f3d3-469a-be66-2b68cf969274 | underdog | Will Stone | FG Made | under | 0.0667977883764894 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|f45b86d3-dbf7-4286-ab3e-dbf13b253ea0 | underdog | Lotzeir Brooks | Receiving Yards | under | 0.0664108283053951 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|70c8977a-374c-48e5-ba23-edc0fdcc3f39 | underdog | Bijan Robinson | Receiving Yards | under | 0.0663650266525974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|06a009bf-c546-4461-b1c4-1bde1ff75c14 | underdog | Blake Corum | Rush Yards | under | 0.0662621531811924 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|2a9dcee0-e5bf-40bf-a5cc-c145bc35b2b4 | underdog | Conor Talty | XP Made | under | 0.0658903549899069 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1f7419ba-44ed-4d10-8a7a-bc913e247a3b | underdog | Blake Corum | Receptions | over | 0.0657799728513109 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|352ced7e-8dac-418b-9c42-3093c7bff249 | underdog | Dalton Schultz | Receiving Yards | under | 0.0657798179755999 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2047a103-6641-4551-a223-10b0b1ce23c3 | underdog | Davis Warren | Pass TDs | over | 0.0657634292166943 | 2026-10-21T23:24:30Z | 2026-10-24T02:30:00Z |
| underdog|bc5e98e3-a5ce-45a5-90f0-bbacbef40b3c | underdog | Tetairoa McMillan | Receptions | under | 0.0657606101669747 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0131b66-956e-40d4-b77b-fa40d10bbfc1 | underdog | Mazeo Bennett | Receiving Yards | under | 0.0655546726670815 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|df559804-fa70-4170-9188-6091d2237843 | underdog | Cooper Barkate | Receptions | under | 0.06522046146098859 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|45fa3593-0103-4921-9164-e34b2d1a2c37 | underdog | Nico Brown | Receiving Yards | under | 0.06486438037818043 | 2026-10-23T13:31:04Z | 2026-10-24T02:30:00Z |
| prizepicks|15945074 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.064833820071657 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|15944962 | prizepicks | Jordan Love | Rush Yards | under | 0.0645818534291142 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|3d22988e-6ca4-4104-b88b-0a0063bb07ec | underdog | Tyler Allgeier | Rush Yards | under | 0.0644856369050936 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|2ecfb6b7-ca61-40d5-86df-244f82324a85 | underdog | Gianni Spetic | FG Made | over | 0.06447492432951912 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|69c654d5-7f0d-40ba-b4de-0146a790613e | underdog | Jordan Addison | Receptions | under | 0.0643744310105808 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|80949b99-08c9-47f9-8565-09b998f305cc | underdog | Aaron Jones | Receptions | under | 0.06431549031041361 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|2eb5e568-cc96-4531-ab10-ffab55af03fd | underdog | Sal Frelick | Batter Walks | over | 0.06364124597207299 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|cfbdd3d7-05e4-4a61-b2f7-be3f0ae409aa | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.0636127420865686 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16111971 | prizepicks | Darian Mensah | Pass Comp | under | 0.06361233653778786 | 2026-10-23T13:31:04Z | 2026-10-24T12:00:00.000-04:00 |
| underdog|a3da5e5c-a888-405e-9dfa-c36687761062 | underdog | Drew Sample | Receiving Yards | over | 0.0629102314852918 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d76069d3-8d26-4e71-a6a7-06b5b5f062d2 | underdog | Samaje Perine | Receiving Yards | over | 0.06271037602491508 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|3b625a33-dfe7-4c56-a081-2453c34284ce | underdog | Tate Sandell | XP Made | under | 0.062585771684329 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|cd894ebb-1464-4062-9e9d-d7034e80fd27 | underdog | Tommy Tremble | Receiving Yards | under | 0.0625505359363844 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|524d894d-b73c-4c7b-b623-faa86d67fbfb | underdog | Cooper Pratt | Runs | over | 0.062376553042370164 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|04d5c5e5-e62e-43e4-b7ad-f05b27c1e49f | underdog | Aaron Rodgers | Pass TDs | under | 0.0620273967369939 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|bad7ccd3-6884-4391-aab3-98594caab197 | underdog | Chris Bell | Receiving Yards | under | 0.061951957479485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051228 | prizepicks | Kendrick Bourne | Rec Targets | under | 0.0616943000896329 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|365c7fa6-dcc5-4b1b-b9af-c0c3cdca5d6b | underdog | Puka Nacua | Receptions | under | 0.0616090079415561 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|9ff8ad4e-4c75-4cfd-badd-45cf27902270 | underdog | Chris Bell | Receptions | under | 0.0614599626838349 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|aac8f74c-2119-4b2e-a91e-5efe2a4b948d | underdog | Samaje Perine | Rush Yards | under | 0.0614244302386539 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|300681f0-5f41-440c-bc6a-141fa5fe86ef | underdog | Tyjae Spears | Receiving Yards | under | 0.061401526255426386 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ad0ef3f7-fe1a-4267-99ab-4c3bf8bc4f9d | underdog | Cam Coleman | Receiving Yards | under | 0.0612304355005692 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|5954f148-25b6-4392-adb1-cc64c04c60fc | underdog | Wayshawn Parker | Rush Yards | under | 0.0611840684856361 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|82932e52-6bd2-40d8-8f4e-8c0311ba997f | underdog | Sam Leavitt | Pass TDs | under | 0.0609996532059247 | 2026-10-22T04:39:42Z | 2026-10-24T16:00:00Z |
| underdog|24666207-a1dd-46e8-aab0-107b45a16292 | underdog | Jackson Chourio | Hits | over | 0.0609658343933108 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|2b8f786a-ddf3-4c91-98e5-a939a1e123fe | underdog | Harold Fannin | Receptions | under | 0.0608103254568292 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|757d3abb-8848-4006-a50e-f2af3d90893f | underdog | Koby Young | Receiving Yards | over | 0.0607716190821504 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|3c8721d1-a9d3-4553-a327-a86b397d702f | underdog | Jadeveon Clowney | Sacks | over | 0.0605759985732586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|60491404-85e4-4da0-ba06-4d23eb4cbaf6 | underdog | Brock Purdy | Rush Yards | under | 0.0603702485832077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15940804 | prizepicks | Devaughn Vele | Recs | under | 0.06015971284752153 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|0d6f7a50-fa14-420e-bb35-6a8002c97c5a | underdog | Kendrick Bourne | Receptions | under | 0.0601364284559438 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|410fd1b1-2582-428f-bdae-1ad4c09f7927 | underdog | Hudson Clement | Receptions | under | 0.06012931151971457 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|f0574182-5160-4aae-ac42-7326e5cd1a8a | underdog | Isaiah Marshall | Pass TDs | over | 0.0600539828055765 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|f2c7e077-b430-4e2b-b8d2-b22a32ab1f15 | underdog | Kendre Miller | Receiving Yards | over | 0.0599966168566626 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|0b848e07-9ee9-4b51-bcf7-f9f29202ca1b | underdog | Will Reichard | Kicking Points | under | 0.05988293461374794 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051226 | prizepicks | Elijah Higgins | Rec Targets | under | 0.0598253921377927 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|49daeb9b-6b9c-4ebd-b104-a6d5432851ed | underdog | Garrett Mitchell | Hits | over | 0.0597962546884593 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fec5e122-f59d-49aa-9430-e8b854af8e70 | underdog | Geno Smith | Rush Yards | under | 0.0596711983179013 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|95c1e474-6c5b-48b7-987a-a9b6b84d9ba3 | underdog | Aaron Jones | Receiving Yards | under | 0.05947359172960187 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b4073c57-0eee-482e-9c8c-29a23326ac44 | underdog | Chuba Hubbard | Rush Yards | under | 0.0593658945119207 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|583e6b0d-22f5-481c-b34a-7f4a4b548be3 | underdog | Gavin Lahm | FG Made | under | 0.0593599272390517 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|b8437d2f-d150-418a-a56d-62792bbe967f | underdog | John Mateer | Rush Yards | under | 0.05931326096304501 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|e1b02812-0720-4112-a468-608f821b451a | underdog | DeSean Bishop | Rush Yards | under | 0.05891477188332783 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|09b74476-b00c-4a2f-abc2-20d3e33100a6 | underdog | T.J. Hockenson | Receptions | under | 0.0587657925838965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|277a8aec-fac7-43c4-a344-09970c828c5d | underdog | Pierre Strong Jr. | Receptions | over | 0.05871475975977286 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|3c27ced9-c782-4952-836e-43b81b480fcc | underdog | Tyler Higbee | Receptions | under | 0.0585445402433147 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|5585fcc2-4a13-429f-8e52-c78d296cf0bc | underdog | Conner Weigman | Pass Yards | under | 0.058345996023547 | 2026-10-21T23:24:30Z | 2026-10-25T02:15:00Z |
| underdog|4b7329da-dbec-4af2-96c4-93d046abc581 | underdog | Tyler Allgeier | Receptions | under | 0.0583402865378401 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|ef6347b0-0ad7-4789-b83d-bdc81dde88e0 | underdog | Trae'shawn Brown | Rush Yards | under | 0.05832735160000313 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|599691a9-9057-4af8-91d1-d013efdd5223 | underdog | Preston Douglas | Receiving Yards | under | 0.05817065488057893 | 2026-10-23T04:50:52Z | 2026-10-24T02:30:00Z |
| underdog|f850eeaa-b79f-483b-90c4-6ffe630e9c5c | underdog | Dohnte Meyers | Receptions | under | 0.05807606094078033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b359de29-0515-46be-8ab6-0d86fc6803fe | underdog | Ryan Fitzgerald | FG Made | under | 0.0575761782932597 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|11977e8c-1468-4369-bd39-5d487c3972a7 | underdog | Braden Pegan | Receiving Yards | under | 0.0575034827429468 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|49042e67-f88c-438c-9e92-03f6dbd2b21f | underdog | Caleb Komolafe | Rush Yards | under | 0.0573778751522929 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|5a2f85cf-5204-495e-a414-068f4e92cb53 | underdog | Mason McKenzie | Pass TDs | over | 0.05736766045657049 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|6fa0097a-90c1-4755-b236-548718217bca | underdog | Chrishon McCray | Receptions | over | 0.0573275006552072 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|2b975295-68b0-404b-9811-4452287dd8d7 | underdog | Derrick Henry | Receiving Yards | over | 0.05729886958919905 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|5b1209ba-20ce-4559-a6b5-422b5f506385 | underdog | Kenneth Walker III | Receiving Yards | under | 0.0570964245693671 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|788d321e-a413-42d1-9fe8-598725b5146c | underdog | Noah Fant | Receptions | under | 0.0569890350580739 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|c0a5ad75-7b4e-4830-91bb-5bf2bc4bc492 | underdog | Mike Washington | Rush Yards | under | 0.0569427656299265 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|9de90d0c-fc2e-4d4d-8991-42254596c301 | underdog | Darren Waller | Receiving Yards | under | 0.056903144274505 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|420a975f-c847-42e1-acb6-f2590c1aa0f5 | underdog | Alvin Kamara | Rush + Rec Yards | over | 0.0568139689190557 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|f7747872-2256-41eb-988e-da59a2931a51 | underdog | Chuba Hubbard | Receptions | under | 0.0567888839933112 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|39c5f5d9-269b-4f71-bbab-95e121e8a0b9 | underdog | Nick Marsh | Receptions | under | 0.0567063898269377 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|83cf691e-8593-4f7e-adc0-e1abc3446ddd | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.05666341739362113 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|427f80d8-c20a-4953-9ba2-d4f260f1ca8e | underdog | Dierre Hill | Receptions | over | 0.056366340304735474 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|ea43b8f1-33b2-42c8-9d2e-1678399861e4 | underdog | Keelon Russell | Pass TDs | over | 0.056233643741644024 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|f15a3695-f852-4979-90f0-f2b517bf4da9 | underdog | Elijah Higgins | Receiving Yards | under | 0.0561049507995341 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|8933129e-bb98-41af-a84b-5e524615a1d6 | underdog | T.J. Hockenson | Receiving Yards | under | 0.0559605706113038 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e003fcb8-09f4-4fe7-be62-c00c1751d87d | underdog | Holden Geriner | Pass TDs | over | 0.055893830641398856 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|c4ea5c9d-4af5-4fb1-a0d3-ce920d2e12bd | underdog | Semaj Morgan | Receptions | under | 0.055890311835268 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|14780cc0-80ce-4e69-a65e-9bac9020139b | underdog | Will Bettridge | XP Made | over | 0.0558018821462565 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|dcf89a53-7242-4b80-9067-f817f87fad1f | underdog | Noah Fant | Receiving Yards | under | 0.05569116003186114 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|a0300642-02c7-49c3-909f-7ff1b09d1382 | underdog | Kamari Moulton | Rush Yards | under | 0.0555951821254596 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c68d1bb1-5199-47e8-8dac-8d8a3f546afc | underdog | Calvin Ridley | Receptions | under | 0.0551783452688616 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5370b3c0-bab6-413f-bab1-db354b16d2d0 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.0551642788819503 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|9dec28bf-f1cc-4984-9300-00fc93a45701 | underdog | CJ Donaldson | Rush Yards | under | 0.05495515497621306 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|32058cd1-abc4-4cbc-8c34-1534704cfc05 | underdog | Mason McKenzie | Pass Yards | under | 0.054546322648263645 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|d3d14224-d4f3-44e4-b59f-eea3b318c350 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.0545437934043115 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2dd8d10d-2956-4b6a-9cb4-fda1851e8b02 | underdog | Radarious Jackson | Receiving Yards | over | 0.0544359927857397 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|096beaa3-503a-4e1c-9e67-fe625725b5c4 | underdog | Mateen Bhaghani | XP Made | over | 0.0543306333436769 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|4955647d-aa21-4715-a60b-c7e2090532fb | underdog | Gage Hurych | XP Made | under | 0.05431532170391373 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|4e5542db-139b-4799-9d3b-e8b9caa1b84d | underdog | Malachi Toney | Receiving Yards | under | 0.05414718965749732 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|1016ca21-bada-4f8c-89c3-8aa706b67cbf | underdog | Juwan Johnson | Receptions | under | 0.0539535225588111 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ce32c899-c546-40d5-b26e-9ced9c6ef8a3 | underdog | Cam Skattebo | Rush + Rec Yards | over | 0.0539214755329643 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|6b9c5594-b8af-4155-99e7-1bdcacdccd19 | underdog | Cooper Pratt | Hits | over | 0.0538445646795883 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d6fef25a-1e32-4d8c-92b7-d29a4cb00582 | underdog | Dierre Hill | Receiving Yards | over | 0.053714462134274554 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|ac3836b7-ed31-46ae-a383-3b2f7ddd8724 | underdog | RJ Harvey | Receiving Yards | under | 0.0533369848818797 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|47d8257d-2ea4-4623-916d-733646daaf24 | underdog | Scott Starzyk | FG Made | over | 0.0533337885644754 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|ac3b79eb-a5c7-46d4-b81d-4144d003c99e | underdog | King Miller | Rush Yards | under | 0.0531509199491621 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|262dcb8e-4bc7-4305-a2b0-e717b681e5a6 | underdog | Ryan Flournoy | Receiving Yards | under | 0.0530145633905199 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|2e311167-8780-48c6-922e-8921f4e43833 | underdog | Chandler Simpson | RBIs | under | 0.052757793764988 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|0cb669cf-b827-461d-9d39-42e64e403fdf | underdog | Tyrell Henry | Receptions | over | 0.0525262856234594 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051317 | prizepicks | Wan'Dale Robinson | Rec Targets | under | 0.0522923521605553 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c3e31ab1-4709-4b43-8b04-8f227c273411 | underdog | Harrison Butker | Kicking Points | under | 0.05183794000713 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|ccfdea0a-25ae-43bc-a5ed-0abbd620d81a | underdog | Chandler Simpson | Hits | over | 0.0518297023595296 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f49b82cf-9c43-4794-8eab-7c12b861a016 | underdog | Will Bettridge | FG Made | over | 0.0516947110884357 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|7ccf04a8-6cf7-461f-b40b-5bae170f518c | underdog | Yandy Díaz | Batter Walks | over | 0.05163644405130474 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|07431a32-42ce-4d0b-abd0-cfb6db23b271 | underdog | Noah Jennings | Receiving Yards | under | 0.0515036832685247 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|8a7998ca-5322-4a0f-bd43-794b3defda38 | underdog | Will Reichard | FG Made | under | 0.051354859593969904 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|662a988b-d8bd-4ab2-8a39-d3807e0ef5ef | underdog | Trent Mosley | Receiving Yards | under | 0.0513544523997693 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051288 | prizepicks | Malik Washington | Rec Targets | under | 0.050971826753459 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|81d3d9e3-d5c3-4a8c-a5b4-d60fe7edc089 | underdog | Kyler Kasper | Receiving Yards | under | 0.0509493282923424 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|744f7c64-587e-41f1-af9d-1bbabfac4473 | underdog | Chuba Hubbard | Receiving Yards | under | 0.0504931979002241 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|25fa3790-d20b-4150-9c6a-160e2a5d2896 | underdog | Tyjae Spears | Rush Yards | under | 0.0503793612554041 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8478770a-27d8-46ec-99dd-bbd68a617b66 | underdog | Wayshawn Parker | Receiving Yards | over | 0.0501876493329525 | 2026-10-23T04:50:52Z | 2026-10-25T02:15:00Z |
| underdog|8225d625-378d-487c-8596-68cf88140f58 | underdog | Ryan Flournoy | Receptions | under | 0.0501148528015784 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0c1a8b52-a086-444e-9bbf-7623ea229a24 | underdog | Rashid Shaheed | Receptions | under | 0.0500925370142416 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|ef28db8f-70ad-410b-b7cc-a22e68e1490a | underdog | Pat Freiermuth | Receptions | under | 0.0499824428187301 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|043f11be-fc7c-4b35-97e9-4d766bfbf47c | underdog | Brock Wright | Receptions | under | 0.04996663713700833 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|2637fc5f-5a0e-49ff-854c-2285f9f3a597 | underdog | Jonnu Smith | Receptions | over | 0.049960814737353365 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|d330b5bb-8718-48e3-bba0-0d522539a540 | underdog | David Hamilton | Batter Walks | over | 0.04982517482517479 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|9749696e-8717-4ed8-9d9e-e6a396043031 | underdog | RJ Harvey | Rush + Rec Yards | under | 0.0497149333024727 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|03981001-9bfc-494f-b5de-c3f8be5c12e0 | underdog | Messiah Hampton | Receptions | over | 0.04967650862494999 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|ac01d325-bcba-4e2f-a91e-28061f0885fd | underdog | Kewan Lacy | Rush Yards | under | 0.0494802756609389 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051304 | prizepicks | Darnell Washington | Rec Targets | under | 0.0493716300398139 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|aa76ff62-2cea-4932-a3b6-25933bffd7a3 | underdog | Jeremiah Koger | Receiving Yards | over | 0.0492893008519933 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|f6c5d90c-aa20-4df0-8599-3fd8ba03d321 | underdog | J.K. Dobbins | Receiving Yards | over | 0.0489630391293001 | 2026-10-22T04:39:42Z | 2026-10-25T20:05:00Z |
| underdog|06c8c71a-f7db-4a2c-9d8a-ff6d764c68ef | underdog | Bucky Irving | Rush Yards | under | 0.0487607240531607 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16035052 | prizepicks | Jake Bates | Kicking Points | under | 0.0487274702622712 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|38da6842-8e2b-4b9f-8e1a-2627589e622a | underdog | Harrison Butker | FG Made | under | 0.0486124772086066 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|b6571da0-cfdd-4408-a40f-9ae3ad574756 | underdog | Charlie Becker | Receptions | under | 0.0485302858619418 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|7f4bce83-fa6d-4487-9f6a-5c219c05606b | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.048402522074492 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|27fc268e-10b4-49d2-aaf1-0ff311eada68 | underdog | William Contreras | Hits | over | 0.048354401129859 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f50bcadf-833b-4788-8fee-74ee7c305872 | underdog | Gavin Freeman | Receiving Yards | under | 0.04826130347272506 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|94b7a884-9297-416e-b4a3-fbe5bc9c0057 | underdog | Cam Cook | Rush Yards | under | 0.048200907783784164 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| prizepicks|16051231 | prizepicks | Bijan Robinson | Rec Targets | under | 0.0477412880585349 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|19497d03-c39f-46ac-80d2-e74b2c4a8634 | underdog | Wan'Dale Robinson | Receptions | under | 0.0476246066680077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c6eb4bd1-bbd4-4d84-a247-eef592bfa1f9 | underdog | J.K. Dobbins | Receptions | over | 0.0476044558282254 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|57243a15-62d8-4624-b55c-49b812912663 | underdog | Tyjae Spears | Receptions | over | 0.0474516029151996 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051249 | prizepicks | Jake Ferguson | Rec Targets | under | 0.047278123853882 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|977b2034-4b67-463d-8a47-d48cfca4f3ea | underdog | John Metchie III | Receptions | under | 0.04724726183118366 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|07a5aab6-6348-499c-9435-5fc9726caa32 | underdog | Chandler Simpson | Total Bases | over | 0.0471927901595421 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fed27918-101a-4ae5-bbde-503c287dad55 | underdog | Marcel Reed | Pass Yards | under | 0.0471762985324026 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|a1ff5d6a-2777-412b-bebb-aeb1145b0fc4 | underdog | Kaelon Black | Receptions | over | 0.04704383794728084 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b57929fa-a09d-4e6f-a44b-3038db73bdd9 | underdog | Samaje Perine | Rush + Rec Yards | over | 0.0470082519671165 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ec454f0f-39d7-4085-8939-37caba2c5f53 | underdog | Omarion Miller | Receiving Yards | under | 0.04700525096816455 | 2026-10-23T04:50:52Z | 2026-10-24T19:45:00Z |
| underdog|f56646dd-e9dc-47e0-b4cb-8184a207198c | underdog | Ty Dieffenbach | Pass Yards | under | 0.046696388412307 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|d1dda524-e3d3-4fba-8cde-c8d9b3fb7823 | underdog | Amare Thomas | Receptions | over | 0.0462398251608691 | 2026-10-21T23:24:30Z | 2026-10-25T02:15:00Z |
| underdog|35962dae-0852-4830-ab91-68c9dcafb2d3 | underdog | Cam Skattebo | Rush Yards | under | 0.046116001037545 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b6f0be07-3802-43c1-86c1-d6bb682a6d07 | underdog | Tyler Shough | Pass TDs | over | 0.0460949746765986 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|905ba66e-7d5c-4806-8f15-25124b39931e | underdog | William Contreras | Batter Walks | under | 0.04581280788177333 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|130a239c-1b64-4770-9290-c9748e447956 | underdog | Omar Cooper | Receptions | under | 0.04568377572350768 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|87557726-d244-4861-a281-61e88eb7a852 | underdog | Davis Allen | Receptions | over | 0.04540259617966852 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|2bdc8511-494e-48d0-8cdf-78689b0520d7 | underdog | Ryan Wingo | Receptions | under | 0.04472002541002029 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|ac1c6c6c-2327-4e95-af19-59c5bd28b38c | underdog | Juwan Johnson | Receiving Yards | under | 0.0446562817968326 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|249ee0b9-e0c3-41fc-8414-3c22214852df | underdog | Matt Gay | FG Made | under | 0.044627908003273875 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051247 | prizepicks | George Pickens | Rec Targets | under | 0.0443567244490695 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|42b4ce0c-6967-4f41-8971-3ab713e4b156 | underdog | Gideon Davidson | Rush Yards | under | 0.0443032159264056 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| prizepicks|16051251 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.0440754381772996 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|26e188e4-5702-4798-95e5-7343fe610a16 | underdog | Arch Manning | Pass TDs | under | 0.0438757827757912 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|e40c88ee-022c-460d-a447-35935e484914 | underdog | Joey Slye | Kicking Points | under | 0.0437911990002866 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|07356e41-4b2e-4e5c-85b2-37c5035acbdd | underdog | Brandon Phelps | Receiving Yards | under | 0.04347386683507748 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|976edc90-d679-4566-8607-829d2e9644fc | underdog | Keenan Allen | Receptions | under | 0.042892061025248 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c635f281-ca04-4c4c-ae31-8bb556878ff3 | underdog | Daylyn Upshaw | Receptions | under | 0.0428467738274781 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|25ef4d6c-fafc-461a-91ad-cc9e6a9ca45e | underdog | Cooper Kupp | Receptions | under | 0.0428006415227674 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| prizepicks|16051240 | prizepicks | Tommy Tremble | Rec Targets | under | 0.0417284345604694 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|4d71b875-6dd2-4b78-a799-3a0909c0e2b6 | underdog | Trey Butkowski | FG Made | over | 0.0416026174253986 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|492260ec-80dc-429f-a65b-5653d01c5dae | underdog | Jackson Chourio | Batter Walks | over | 0.04139372035238309 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|e4173729-8e10-47ec-961b-d80fc7735590 | underdog | Taylor Walls | Batter Walks | over | 0.04139372035238309 | 2026-10-23T04:50:52Z | 2026-10-24T00:00:00Z |
| underdog|348122fb-28c4-4cb4-b1cf-6f19ea0055d5 | underdog | Kyle Juszczyk | Receptions | under | 0.0413755116703427 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051263 | prizepicks | Matthew Golden | Rec Targets | under | 0.0413695180084056 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|9d9af6cc-66dc-4a00-94c9-d99fb3ceb996 | underdog | JC French | Pass Yards | under | 0.0411605391515214 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|8939856c-5a89-49bd-98f9-7321bfa71527 | underdog | John Mateer | Pass TDs | over | 0.040835130607410564 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|c641d8fc-faa8-49cf-8db0-7d035a6b672b | underdog | Byrum Brown | Pass Yards | under | 0.04079121617128334 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|76df7d50-d1c8-4cef-a264-da1f137d2d44 | underdog | Mike Gesicki | Receiving Yards | over | 0.040754670182375 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9883b094-eb96-49bb-b19e-acb1de659a8f | underdog | Sedrick Alexander | Rush Yards | under | 0.0404961008798157 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|377ea8d9-04b2-4679-9e3d-17a676242ae1 | underdog | Davion Brown | Receiving Yards | over | 0.0403180544038364 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|c620c5b0-762d-4cc3-9c1a-f3966aed4fd1 | underdog | Gunnar Helm | Receptions | under | 0.0400733577651734 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051303 | prizepicks | DK Metcalf | Rec Targets | under | 0.0397695291855245 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|f5a591b9-9906-4f91-b4df-254ce3c7681c | underdog | Noah Fifita | Pass TDs | under | 0.03965781467306506 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|7facc89d-e2cf-4c35-a7e7-1e852463830d | underdog | Lee Beebe | Rush Yards | over | 0.03951924199306678 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|ab737f2d-3b0a-4edf-b65e-7af8e6b44518 | underdog | Drew Mestemaker | Pass TDs | over | 0.03940465959910944 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|382b3a7c-9a2a-4092-b9e8-a63bb7b4e264 | underdog | Byrum Brown | Rush Yards | under | 0.03930024073146854 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|5b2552e2-f8f3-4183-b25f-e7a984c1f805 | underdog | DJ Black | Receiving Yards | over | 0.03912143510538624 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|1ad3d594-f785-442a-988e-37a405dc4bd9 | underdog | Pierre Strong Jr. | Rush Yards | over | 0.03903240736915592 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051255 | prizepicks | Marvin Mims Jr. | Rec Targets | under | 0.0388842684737961 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3188fab2-f2b8-4313-895e-57c191d21509 | underdog | Kaelon Black | Receiving Yards | over | 0.0388077194402237 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051242 | prizepicks | Tee Higgins | Rec Targets | under | 0.0387631549019464 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|330820d7-8d2a-41ef-af1a-6866b6a9e287 | underdog | Elic Ayomanor | Receiving Yards | over | 0.038760146342862 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c8c39f26-3329-4571-b0ba-cd4ee0093934 | underdog | Patrick Overmyer | Receptions | under | 0.0385503232486587 | 2026-10-21T23:24:30Z | 2026-10-25T02:15:00Z |
| underdog|7ae7d989-adee-4959-9057-42b96e9b4d2c | underdog | Makhi Hughes | Rush Yards | under | 0.038486788504749736 | 2026-10-23T04:50:52Z | 2026-10-25T02:15:00Z |
| underdog|55dc01c8-c1bd-46c3-bc19-5a3c9fbd7aba | underdog | Carson Kent | Receiving Yards | over | 0.0383307343289383 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|e3620db9-71a9-4ed1-8873-e30ae36cd8b5 | underdog | Jacoby Brissett | Pass TDs | under | 0.0382668553031229 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|16051246 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.03816939250727 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f89ba872-d424-4e73-8bd7-6614b460990e | underdog | Noah Gray | Receiving Yards | under | 0.03811545624303703 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|000a396f-0592-482b-9193-7c967d4da6e8 | underdog | Alberto Mendoza | Pass TDs | under | 0.03802515412022478 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|0beceeea-8dd0-4760-afe8-eeb63492b9e9 | underdog | Mateen Bhaghani | FG Made | over | 0.0377670802335744 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|3753c21e-bad3-43a8-8e6f-e7002d0790cb | underdog | Reece Vander Zee | Receptions | over | 0.0374300137689319 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|05ea1410-88a6-44cd-a8ad-de5e26c8af7f | underdog | Gavin Lahm | XP Made | over | 0.0373018163286511 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|37b58552-22c6-476b-996f-76d857fff274 | underdog | Dalton Schultz | Receptions | over | 0.0372622958628433 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f8caab65-966d-4958-bc02-cd1cc7ac6f7f | underdog | Kenyon Sadiq | Receptions | over | 0.0371667149623974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f26e20ec-cce5-42d2-b0d0-65cdd3b8f5a7 | underdog | RJ Harvey | Receptions | under | 0.0371183056096371 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a1439ecb-61a0-4132-b340-9b65f6413638 | underdog | JaQuail Smith | Rush Yards | under | 0.0370252421973547 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|e27761fb-c206-44d9-ab15-1df547597590 | underdog | Brayden Trimble | Receiving Yards | over | 0.03693525090665706 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|b36c99d1-9b4e-4356-9b5f-76ea099ba1e2 | underdog | Joe Burrow | Rush Yards | over | 0.0369126735438984 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|1b3c0d1d-6e11-43ae-8c46-b0bd4ad8c1e2 | underdog | TJ Thomas | Rush Yards | over | 0.0364190414929286 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|4deafeb0-8398-4a54-bece-82ab8693e503 | underdog | Willie Rodriguez | Receiving Yards | under | 0.0362943645092556 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|199b9729-2a09-46ba-9d22-0447014a9127 | underdog | Sal Frelick | Hits | over | 0.0362883664873167 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|38f2a21d-8f0b-4316-b852-d137222284bb | underdog | Chase Brown | Receiving Yards | under | 0.0362468208379922 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|20a6828f-7b20-425b-8a99-b5533ff3dbdb | underdog | Alex Highsmith | Sacks | over | 0.036117046985766565 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|7f9cf2d5-2fee-44a9-8064-f56c34f6daf9 | underdog | Trent Mosley | Receptions | under | 0.0360985891797962 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|cf250d16-74e7-4690-b197-f25c4276855d | underdog | Evan McPherson | Kicking Points | under | 0.0360049530640667 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|db6fa1d1-b2bc-49a7-afb1-86e53613d012 | underdog | Sam Leavitt | Rush Yards | over | 0.0358407986377768 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|95151427-da0f-4d9b-9b64-708b8632ee19 | underdog | Colby Parkinson | Receptions | under | 0.035577182312387 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|72c9953f-c670-4bc2-9799-3c8f16d50d10 | underdog | JJ Buchanan | Receptions | over | 0.0354632731283425 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|aa104b28-f09d-4347-b2ca-6314a59c5fa1 | underdog | Kyle Ferrie | FG Made | over | 0.0354543097195177 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c07c53d6-5e28-4e56-84c4-7f5377197c29 | underdog | Sal Frelick | Total Bases | over | 0.0353449497095905 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f1a02319-532f-48ea-b85d-f1f8764f33d1 | underdog | Jaron Tibbs | Receiving Yards | under | 0.0352320649773695 | 2026-10-22T04:39:42Z | 2026-10-24T19:45:00Z |
| underdog|6de3ecf1-c2e1-4ffd-af16-c9510234efe0 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.0351824731940149 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4ea266e4-5fc1-44e7-af58-73c75a517562 | underdog | Cooper Pratt | Batter Walks | over | 0.03508771929824561 | 2026-10-23T13:31:04Z | 2026-10-24T00:00:00Z |
| underdog|83375341-0bc4-4389-8595-dd4653ce1fea | underdog | Devin Singletary | Rush + Rec Yards | over | 0.03500589094834228 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|5aba7c83-7528-42ba-bcc1-e98faaf845fa | underdog | Darnell Mooney | Receptions | over | 0.0347146447100191 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|e88243b8-7b5f-4c7d-9c45-56f0a7149d7a | underdog | Jaylen Raynor | Pass TDs | over | 0.0347063301598346 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|4b0693d6-e2e3-4e81-8c87-7af72c6bfba0 | underdog | David Hamilton | Hits + Runs + RBIs | over | 0.0346043286046869 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|74feaf9b-e250-4842-b0e9-0eafab193972 | underdog | Kenny Johnson | Receiving Yards | under | 0.0345782823094164 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|5e8a1a4d-6855-408d-92fe-bde76464fbca | underdog | Noah Bennee | Receiving Yards | over | 0.0345719590912054 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|1a5520d8-dc0e-4149-b0f8-bd112b30d722 | underdog | Avery Johnson | Pass TDs | over | 0.0345275702524721 | 2026-10-21T23:24:30Z | 2026-10-24T19:45:00Z |
| underdog|0acf1d16-15c1-4ad2-b506-7a1bf70e7bbe | underdog | Walker Lyons | Receiving Yards | under | 0.0344986746849036 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|484399f4-298f-4063-9c16-33871082f309 | underdog | Patrick Overmyer | Receiving Yards | under | 0.0344533909502258 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|52326920-4044-4862-87d2-a4905df331c4 | underdog | Nate McCashland | XP Made | over | 0.03445160238831568 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|dc364f92-76cd-4db4-84af-95dd2c29f95f | underdog | Nyck Harbor | Receiving Yards | under | 0.0342231016278906 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|af070318-32e1-472d-8923-cf5ade068e1a | underdog | Walker Lyons | Receptions | under | 0.03421177976325318 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|6b5a1de9-3eef-4741-9170-14f9deced32e | underdog | Matt Gay | Kicking Points | under | 0.0340167035528746 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c4570c51-d4b2-49a4-be2a-a8dd9be0c3f3 | underdog | David Hamilton | RBIs | under | 0.0340022296544035 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|16085772 | prizepicks | Lorenzo Musetti | 1st Set Total Games | over | 0.033652707315786956 | 2026-10-23T04:50:52Z | 2026-10-23T14:10:00.000-04:00 |
| underdog|a29c1696-1438-47a3-b01a-5912718e85a6 | underdog | Tyrone Tracy | Receiving Yards | under | 0.03364027564317851 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|73ccb174-e10e-4fab-b016-1288d6d50b2f | underdog | Chase Brown | Receptions | under | 0.0331873731070406 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|15953468 | prizepicks | Braylon Staley | Recs | under | 0.03314857952762895 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|46b6ebd1-4af0-4990-84af-243e988664a0 | underdog | Chas Nimrod | Receiving Yards | under | 0.033045417710304115 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|9ae00861-5dbe-4edb-ba32-2a64fe363093 | underdog | Emmett Johnson | Rush Yards | over | 0.0328425645250116 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|672fd8db-fc81-4c61-8366-cc5023140b71 | underdog | Erick All | Receiving Yards | over | 0.03264221436156661 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|425fbbd0-9045-445e-83f3-1092d3b649a5 | underdog | Deuce Alexander | Receiving Yards | under | 0.0324621299207996 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051314 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.032115498076035 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|9f7d9367-cb26-4244-b0e5-04282d9a5386 | underdog | Caleb Hawkins | Receiving Yards | over | 0.03195836746924963 | 2026-10-23T13:31:04Z | 2026-10-24T23:00:00Z |
| underdog|eea26e28-d674-4d7b-8f8e-fc71ea5a2dde | underdog | Trey Butkowski | XP Made | over | 0.0319308924100778 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|7980f836-3a4d-4a57-a058-c185a707944e | underdog | Colton Joseph | Rush Yards | under | 0.031850316272014956 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|e4480b0f-913c-4202-bf76-e2aff55f73c7 | underdog | Cam Ward | Rush Yards | under | 0.0318471189373211 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0f41da18-0d9d-441e-acd6-39469e55d1f7 | underdog | Reece Vander Zee | Receiving Yards | over | 0.0316182443989341 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1f939575-5ddc-4b82-9561-76c4952c4966 | underdog | Jacob Misiorowski | Strikeouts | over | 0.0316158443643395 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|ddb3b6de-e82e-47a8-8018-e76d2c842a21 | underdog | Ryan Wingo | Receiving Yards | under | 0.0315164104140868 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|437bcba0-d2dc-490b-b518-d597bc646e8d | underdog | MarShawn Lloyd | Receptions | under | 0.031455160163501805 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|16e2ddea-e714-4ae0-967c-6128c1d08825 | underdog | Foster Moreau | Receiving Yards | over | 0.030947868389375688 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|cac9d7ae-0b31-4f2c-b7f0-5bfaf2215a61 | underdog | Bear Bachmeier | Rush Yards | under | 0.030904426266193052 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|eb47b832-623a-4517-b8e3-f59db1fa3394 | underdog | Dominic Zvada | FG Made | over | 0.0304043417105965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|98567d65-69d2-46b3-804e-141171ccac4e | underdog | Kenny Darby | Receptions | under | 0.0301176139915753 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|d8958df4-dbda-4f8f-895c-fcc504fc3ac7 | underdog | Charlie Becker | Receiving Yards | under | 0.0300748709040623 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
