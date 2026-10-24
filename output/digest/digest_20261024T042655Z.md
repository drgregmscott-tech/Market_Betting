# Pipeline Digest -- 2026-10-24T04:26:55Z

## Run summary
- Ingestion: 45356 rows (PrizePicks OK, Underdog OK)
- Estimation: 45356 rows estimated (from 45356 ingested props)
- CLV logging: 418 newly flagged, 0 newly closed, 1082 still open (105167 total ever logged)

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
| underdog|d901ce25-9ca6-4d08-a605-d775897a85aa | underdog | Geno Smith | Pass Yards | under | 0.4090737399477504 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1eb3cc78-3cfa-4153-87dd-b9095b038836 | underdog | Deshaun Watson | Pass Attempts | under | 0.4087275591164793 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|1b5478e1-f142-43bc-bb58-44ee81db7923 | underdog | Brice Turang | RBIs | over | 0.40189393939393936 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|e1ed7c34-5984-4d1d-b0f0-10d131ce332c | underdog | Brock Purdy | Pass Attempts | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d424e459-1d04-4391-92fb-b90d20c159d8 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|68886647-dade-4f41-b1a5-aa635dcb7957 | underdog | Lamar Jackson | Pass Attempts | under | 0.4 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|fae16c8c-b4ea-431a-9eb2-c0ecdd1e0213 | underdog | Lamar Jackson | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cdb5e111-4cf9-4bfd-82c6-27b11ce762fc | underdog | Eddy Pineiro | FG Made | under | 0.3955537623462751 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e3084a60-03df-4043-9baa-8fdd03ce53ce | underdog | Malik Willis | Pass Yards | under | 0.3948522906927716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9693ec51-4551-43f9-853c-0fb05eafd96d | underdog | Daniel Jones | Pass Yards | under | 0.3939654564213076 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5f896a94-190d-4811-9b4b-b1f17ce66f93 | underdog | Jordan Love | Pass Yards | under | 0.3897173199669762 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|643cc8ea-4e4a-4d28-86a8-1e125427f8dd | underdog | Michael Penix | Pass Attempts | under | 0.3727880183899563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|df2d500b-274d-4174-b4d8-d32b5c551962 | underdog | Bo Nix | Pass Yards | under | 0.3619289340101522 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|38a39011-3779-4d19-a6e6-ca06836b54c2 | underdog | Brendan Baird | XP Made | under | 0.3592651266806685 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|0085fd80-5781-444c-9416-df3ebc46a0c0 | underdog | Ted Hurst | Receiving Yards | under | 0.35918367346938773 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|4ae8ad3b-3e4b-49b9-a170-e5307e2a5898 | underdog | Brock Purdy | Pass Yards | under | 0.3591836734693877 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|530a02a3-77b5-426f-8b14-0bcce21e13f4 | underdog | Tommy Carr | Pass Yards | under | 0.3589561692241783 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|aed9e657-4b01-41ed-a960-612d3d02a69a | underdog | Jacoby Brissett | Pass Yards | under | 0.3567731226756141 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|e9816757-ab71-40b2-92af-c6dad30b4143 | underdog | Jordan Dwyer | Receptions | under | 0.3511194572447186 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|a218a657-b6cc-4e53-bfe6-4b64bb11eaa5 | underdog | Tyler Allgeier | Receiving Yards | under | 0.35099657850370225 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| prizepicks|16039393 | prizepicks | Kyler Murray | Pass+Rush+Rec TDs | under | 0.3509424650567749 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|15944973 | prizepicks | Bo Nix | Pass Yards | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|67b9076a-4be2-44b7-a2ab-11721c8cbac7 | underdog | Saquon Barkley | Receiving Yards | under | 0.3504068968649158 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|d0517fae-e001-44f5-8e9a-0a74f44ad68b | underdog | Baker Mayfield | Pass Yards | under | 0.3467005076142132 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f2b579f8-0b0e-42c1-9f15-f905808f1547 | underdog | Brice Turang | Batter Walks | over | 0.345740498034076 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|86608b58-ef41-4874-b74b-6cb58e689196 | underdog | Bryce Young | Pass Attempts | under | 0.34321350423372066 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|37edd000-30ff-4318-96d8-a3ca5e430a8d | underdog | Patrick Mahomes | Pass Yards | under | 0.3421724696477669 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e2f6a64e-736b-406d-af04-9748d4794dd9 | underdog | Bo Nix | Pass Attempts | under | 0.34142338286125395 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|6671aa81-ba7b-4453-a8b6-fe3bfeee2cc8 | underdog | Eddy Pineiro | Kicking Points | under | 0.33856343461105154 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7a87240b-260e-417a-86ba-70208aa779d5 | underdog | Chris Godwin | Receiving Yards | under | 0.3343434343434344 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16128096 | prizepicks | Brandin Cooks | Rec Targets | under | 0.33414311839178035 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|847b0c28-14bd-4013-973e-05d76c8b982e | underdog | Matthew Stafford | Pass Yards | under | 0.33409895723922944 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|8dc47268-4a7d-404f-9e49-dcd9ba768270 | underdog | Kyler Murray | Pass Yards | under | 0.3335652027540378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4ab4a41a-52fd-4cc5-b31f-ec4b0c82bb82 | underdog | Trey McBride | Receptions | under | 0.3329820296458966 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|de1666e6-df3d-43ad-b5d6-c89105471ef8 | underdog | Cole Tabb | Receiving Yards | over | 0.3271958565311026 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|3246a459-7d1f-41ff-ba1b-b9c683e7b334 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3268677849268778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|24013bf3-a907-48ae-8533-86d3168e770c | underdog | Tyrone Tracy | Rush Yards | under | 0.3267094468242045 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|0837eb99-3beb-4beb-803a-b6d445424ac1 | underdog | Jordan Love | Pass TDs | under | 0.3243123493621316 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|f0fc31cd-bda5-492c-9fde-68412646daa5 | underdog | Kirk Cousins | Pass Yards | under | 0.3229461067989536 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|955df2b0-8f9a-4a16-8335-3391b127060c | underdog | Chase Brown | Rush + Rec Yards | under | 0.32063706977042394 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|21ae2dbb-b8cd-47b4-8d9e-617160fee214 | underdog | Jake Elliott | FG Made | under | 0.3198767487193468 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1776f06a-1d54-4810-893f-a6f0b18bce64 | underdog | Joe Burrow | Pass Yards | under | 0.317382759820503 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dbe5c55e-c922-47ce-80a9-02406cd98c80 | underdog | Jalen Royals | Receiving Yards | under | 0.31709006450626964 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|154124b9-f603-40a2-80d3-6e46172c515f | underdog | Cam Ward | Pass Attempts | under | 0.3135302584652062 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2ec6ad3-205c-4df4-915c-e02ff73d5ed6 | underdog | Trey McBride | Receiving Yards | under | 0.30725817844859604 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|6778a4ed-0a07-462f-ad67-3327e6b33ee7 | underdog | Tyler Shough | Pass Yards | under | 0.307201308387714 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|82aebfff-cfa1-4d98-b5bd-55154adc923e | underdog | J.K. Dobbins | Rush Yards | under | 0.30471317090038563 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|def3c45d-8dee-47c2-8568-4c3fd9106465 | underdog | Courtland Sutton | Receptions | under | 0.30202251379357925 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|e34970e2-eb5b-4c42-a983-df77a630b08c | underdog | Ja'Marr Chase | Receiving Yards | under | 0.3017403489827723 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e10287d-2f97-493e-ae55-2e6c78479625 | underdog | Tony Pollard | Rush Yards | under | 0.3014201136182672 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7a12d1ee-529c-49c9-966a-48bcaa8ce51c | underdog | Puka Nacua | Receiving Yards | under | 0.2961452597214975 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3c6300c9-4b09-4aec-8e6b-9a70d49c3f99 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.2943696215652248 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|c482250b-b72f-437f-a1be-d35070dc0701 | underdog | Daniel Jones | Pass Attempts | under | 0.29431420324174984 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16051310 | prizepicks | George Kittle | Rec Targets | under | 0.2942952711541847 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|e56d19e3-ff75-4054-8e81-a52ef8d30309 | underdog | Kyler Murray | Pass TDs | under | 0.2942390154326902 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|586acb89-828d-495a-b781-835f3b0cca6b | underdog | Courtland Sutton | Receiving Yards | under | 0.2913478359944116 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|1cb78bf3-5610-4b98-a9c4-2483ad1327b0 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.28954474820641707 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|04a4df3d-c7db-42ac-b930-94951fa9779e | underdog | Brock Bowers | Receiving Yards | under | 0.2882455496564065 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15945775 | prizepicks | Courtland Sutton | Rec Yards | under | 0.2858886737283282 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|739590e9-a831-4e2e-831f-8105a7b0bfa3 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.2856924823941684 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|07395bfc-011b-4422-b48a-9528906d7807 | underdog | Kedrick Reescano | Rush Yards | under | 0.28323084073343874 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|27afcb09-4472-4907-b73c-9de29d4e33b2 | underdog | George Kittle | Receptions | under | 0.2828324993741664 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1dc224d8-4045-43ec-97c9-959c5e18ba2f | underdog | Tucker Kraft | Receiving Yards | under | 0.2825174713014219 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|79b2b766-9806-4ad9-8c3b-a2f1e9541a4b | underdog | Aaron Rodgers | Pass Attempts | under | 0.2815799685858499 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
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
| underdog|1ad81329-a627-4424-ab4c-6c206dfbf3ad | underdog | DeVonta Smith | Receiving Yards | under | 0.27070561716917263 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|d60cfe44-e868-4c10-a96b-234bdd9c611b | underdog | Lamar Jackson | Pass TDs | under | 0.266696128639032 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ad87b775-bfc9-4f54-95ee-ff5ed677e61f | underdog | Ja'Marr Chase | Receptions | under | 0.2661038820739 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|89cf57cf-5c67-4f1a-8deb-192e8e8f0acf | underdog | Joe Burrow | Pass Attempts | under | 0.2649397836846312 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|15956871 | prizepicks | Daniel Jones | Pass Attempts | under | 0.2638857049460724 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|96c40cdc-691c-48db-89d3-4c55dbb29290 | underdog | Sam Darnold | Pass Yards | under | 0.2626055914367695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0e69f33d-bd78-42a8-bec9-9fba13cd8b7d | underdog | Sean Tucker | Receiving Yards | over | 0.26216865530539846 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|6d497603-aa41-45ea-b69e-ad7cb7b1173b | underdog | Nikoloz Basilashvili | Aces | under | 0.2618267443184972 | 2026-10-24T04:39:26Z | 2026-10-24T10:00:00Z |
| underdog|73395da4-8892-4961-b521-7e1248b8f7cf | underdog | Bo Nix | Rush Yards | under | 0.2605581005357792 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|37ebd74f-0972-43d0-94c1-041099293aaf | underdog | Will Hammond | Total TDs | under | 0.26040736947411103 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| prizepicks|16127533 | prizepicks | Fábio Silva | Shots | under | 0.2603038964111237 | 2026-10-24T04:39:26Z | 2026-10-24T12:30:00.000-04:00 |
| underdog|7f9ff427-eeca-41d9-b667-16c9f1fc8e5d | underdog | Tony Pollard | Rush + Rec Yards | under | 0.2596998817408331 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2ca7cc4-8309-462a-93ef-879c52f609b7 | underdog | Bryce Young | Rush Yards | under | 0.2592736328532177 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|53b8ca85-0058-4dab-98e2-975f4ff4fc68 | underdog | Jared Goff | Pass Attempts | under | 0.25914481558143354 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|c1c0ffd9-df31-4816-86e7-59f57eb89f4c | underdog | Sione Vaki | Receiving Yards | over | 0.2588272369464025 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|672c91b2-8aeb-400f-a8f4-81ff00601d2f | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2573371918577716 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|bb92d3d3-e3fa-40d3-8c32-40276e0a1d10 | underdog | Jordan Love | Pass Attempts | under | 0.25682947172423143 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|ca3632a2-8e4a-47c7-9eae-49763f89f19a | underdog | Jake Bauers | Batter Walks | over | 0.256043956043956 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|183dc84a-07dd-44fe-9baa-6b50e2dab0f0 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2554746786082785 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|09bee2cd-e008-407b-87a5-2ef9740a5f75 | underdog | Malik Willis | Pass TDs | under | 0.2548170435450879 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7594b837-9c0a-4a5e-a07c-cb03792bcec9 | underdog | Rico Dowdle | Rush Yards | under | 0.2523393133447593 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|047c7173-2580-4f0e-bee6-72ae14ca159a | underdog | Jauan Jennings | Receiving Yards | under | 0.25118382646039095 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|9827d4a6-1c80-4f8e-837a-59a7a4efad92 | underdog | Wil Lutz | FG Made | under | 0.2495510531033402 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a7d67cf1-2deb-4409-a28f-186fdbd101d0 | underdog | Malik Washington | Receiving Yards | under | 0.246141552704973 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|34430e10-7ba6-4e9b-86be-42e7f68c93de | underdog | Taylor Walls | Runs | over | 0.24603860558916735 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|41359dbd-8223-40ba-b01b-d548d0fd476b | underdog | George Kittle | Receiving Yards | under | 0.2453249563886891 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051276 | prizepicks | Brock Bowers | Rec Targets | under | 0.24528945408523 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|648dee62-ca9c-448b-bcfa-499810b73d24 | underdog | Xavier Hutchinson | Receptions | over | 0.2439123066762485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|151d3e83-45f8-463e-8fdc-cd3f943b9d80 | underdog | Matthew Golden | Receptions | under | 0.2412290414387117 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|4cfc595f-ace4-4eec-a562-9a61b88991da | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.240025789607406 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|cf9de8cc-9bb6-4aac-9635-ec94d6cbf61e | underdog | Woody Marks | Rush + Rec Yards | under | 0.23942161082921087 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|5c474bdc-04d7-47e0-867b-bcfee2a049ab | underdog | Baker Mayfield | Pass TDs | under | 0.2393581560012833 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|298e8d38-ac96-403f-9f7e-d6a0bf21ada9 | underdog | Nick Emmanwori | Sacks | over | 0.23869466592176167 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|1713fb00-7c86-4fb8-b9db-c0d3cd103304 | underdog | Cade Otton | Receptions | under | 0.2373958346481726 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ea96d4e7-d343-4032-ac48-3c5395f7363e | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.23477237529212425 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|fe787fef-c3ce-478e-9eaf-81cc4de74984 | underdog | Christian Yelich | Runs | over | 0.2345956145487672 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|86147115-576f-4689-8d0b-2666f24dde83 | underdog | J.J. McCarthy | Pass Attempts | under | 0.23225840306780554 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|586068fb-61a6-4896-adf5-555492e331a0 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.23041454820233864 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|193c6a4c-aa4a-46b0-a869-9e9de2826135 | underdog | Bo Nix | Pass TDs | under | 0.2300413174167165 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|7caf365c-b8e0-4138-9f38-48f4d8c2e085 | underdog | Jordan Watkins | Receptions | under | 0.22923645637992762 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|24df7a00-2988-4b67-b4ea-8506cca6af03 | underdog | Patrick Mahomes | Pass Attempts | under | 0.22838649764287888 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|58b3f25a-6eba-4472-9821-0fc96a39ffc8 | underdog | Geno Smith | Pass Attempts | under | 0.2275649013349008 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|17c2adf9-75e8-44b7-9e46-b0a6769151cf | underdog | Germie Bernard | Receiving Yards | under | 0.2275384159492459 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|e4c964b1-0b2b-4857-acae-59f009c1792e | underdog | J.J. McCarthy | Pass TDs | under | 0.2273642896866348 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|88ddddd3-918c-4785-9b4f-fdc9f6fb9182 | underdog | Xavier Worthy | Receiving Yards | under | 0.2257113356958771 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|f9352960-e46a-4bd0-887d-6b56e268fcec | underdog | Dak Prescott | Pass Attempts | under | 0.22420131322413994 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|d8ce48c2-d479-403b-9323-2a031b8681af | underdog | Malcolm Koonce | Sacks | over | 0.22140008020512947 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|bf1d95e3-f10c-4550-8a39-10f875aed153 | underdog | C.J. Stroud | Pass Attempts | under | 0.2210784579055988 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5b90486b-c32a-4e28-812e-3e86cebac5aa | underdog | KC Concepcion | Receiving Yards | under | 0.2207706046563152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0d5dbe4-9388-4622-8cc6-c162a5b0639f | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2206178911560523 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d9f8055e-799a-4e34-b09f-950d09443ddf | underdog | Kirk Cousins | Pass Attempts | under | 0.2206170397617192 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|67360a01-9b6c-445e-b346-4386fec6404b | underdog | Josh Downs | Receiving Yards | under | 0.22055561241605925 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|eb1b1fd9-3046-4288-a213-e4a77e45136e | underdog | Jacoby Brissett | Pass Attempts | under | 0.22019670734246832 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|dd981eb9-f019-43eb-8014-51c7e7f60995 | underdog | Marvin Harrison | Receiving Yards | under | 0.2201873079173418 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|4938e844-0f10-48db-8ce4-f416888b7caf | underdog | Ian Thomas | Receiving Yards | over | 0.2199241073605816 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|966b3c9f-fa61-487d-900b-b80f9390440f | underdog | Kayla Day | Double Faults | under | 0.21978830802907745 | 2026-10-24T04:39:26Z | 2026-10-24T06:40:00Z |
| underdog|56656c9d-ec82-4d22-befd-cf88edbd6a09 | underdog | C.J. Stroud | Pass TDs | under | 0.21922023288096 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c9dd882b-334e-4169-b37c-b296bb877d16 | underdog | Tyler Loop | FG Made | under | 0.2188399052787495 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a63cc8a0-36cc-4002-9d0a-9275fc20e5e3 | underdog | Devin Singletary | Rush Yards | under | 0.217094503944824 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7dbfe9c7-e77c-46aa-8f0d-da3c00ff3729 | underdog | Cam Ward | Pass TDs | under | 0.2169355074931716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16039395 | prizepicks | Bo Nix | Pass+Rush+Rec TDs | under | 0.2167665072623288 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|d3bd3ee5-389e-4547-ae5a-c9080b203aec | underdog | Jackson Chourio | Runs | over | 0.21590909090909083 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|0f9a3b7c-fd9b-4658-99e8-7ae8da660708 | underdog | Rico Scott | Receptions | under | 0.21547853242216997 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| prizepicks|16128087 | prizepicks | Xavier Worthy | Rec Targets | under | 0.214565411971544 | 2026-10-24T04:39:26Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|82fdc867-aad8-427f-9856-e3c82f62e9df | underdog | Saquon Barkley | Rush Yards | under | 0.21296609967876423 | 2026-10-24T04:39:26Z | 2026-10-27T00:15:00Z |
| underdog|b5b4cf2d-863c-4b07-8225-e61b4888d5da | underdog | Kenny Gainwell | Rush + Rec Yards | under | 0.2124926916515939 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051257 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.212391920232314 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|80998e29-827a-47a2-ac21-31900ecc9a6c | underdog | Wil Lutz | Kicking Points | under | 0.21088950433211662 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a9df4b24-c600-46b7-a5e9-ec9eb30eeff5 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.2103451992664808 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|78179df4-d48d-4dea-9683-aa1d37bce306 | underdog | Tait Reynolds | Pass TDs | under | 0.20877657627845503 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|b3d36ef2-c5d1-42ce-bdf6-3dcd1e9c4bd1 | underdog | Colby Parkinson | Receiving Yards | under | 0.2087631852016807 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|fb9265dc-daee-479a-b5e7-586745cc58cb | underdog | Brice Turang | Runs | over | 0.20866740676781348 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|5e78605e-bcba-4d2f-90f8-e6c3dfec5088 | underdog | Rico Scott | Receiving Yards | under | 0.2078501632803695 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|e4e5c670-0987-4d0a-8a4a-9428d204a893 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2077532646208933 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c1d936d4-68f3-4e44-837e-b333d2c4f1a2 | underdog | Jameson Williams | Receiving Yards | under | 0.2060331671729401 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5c338679-fd57-47ab-8bfc-0d1098e55176 | underdog | Garrett Mitchell | Runs | over | 0.20550924247915908 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|dcb7268c-2dff-4d12-96c7-22f9fcef69c7 | underdog | Francisco Cerundolo | Aces | under | 0.2043338888162981 | 2026-10-24T04:39:26Z | 2026-10-24T14:00:00Z |
| underdog|7de4c5a8-670a-47dc-9b4a-91427c914776 | underdog | Yandy Díaz | Runs | over | 0.2036922823897041 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|4ce494db-1a02-483c-9b1b-ee9ddf695bd0 | underdog | Woody Marks | Rush Yards | under | 0.2028480523660538 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|cccfadea-ede5-4a70-8bb4-241573025bb8 | underdog | Maddux Madsen | Pass Yards | under | 0.20108610937421978 | 2026-10-24T04:39:26Z | 2026-10-24T22:00:00Z |
| underdog|10021345-bbed-4a2f-a584-a3e81916b523 | underdog | Daniel Jones | Pass TDs | under | 0.200856388948677 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|434fe9a1-6f1c-4a5e-9933-75476c259a85 | underdog | Jonathan Aranda | RBIs | over | 0.1997668091721726 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|209a796c-6c53-4cb7-9286-8d0076babaf8 | underdog | Yandy Díaz | RBIs | over | 0.1987220135603141 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|f2c4be9d-9aee-4f55-8d4b-dbe30b779a70 | underdog | Javonte Williams | Rush Yards | under | 0.1985197402148549 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|f7ea1d63-47b7-4975-9db4-7db15515d650 | underdog | Christian McCaffrey | Rush Yards | under | 0.198275138398706 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051270 | prizepicks | Nico Collins | Rec Targets | under | 0.1977937055574494 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|07a4d392-bef4-4ae1-bad4-0c514f603d92 | underdog | Mark Andrews | Receiving Yards | under | 0.1973857281627509 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7478a968-ff4e-476b-9b0f-02fe597e1822 | underdog | Dallas Goedert | Receptions | under | 0.1970050433176551 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|bfc2e148-a21c-4383-a448-5598a14b86aa | underdog | Jonathan Taylor | Rush Yards | under | 0.1969151744354131 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dd2e01e1-9b2b-4090-aa87-6a74f55e0015 | underdog | Troy Franklin | Receptions | under | 0.19440896280038 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|592ee15a-985e-49a7-9223-eb16e977e1b7 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.19376542031955757 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8b92d278-dbd5-418b-b6f4-85464899feec | underdog | Tez Johnson | Receptions | under | 0.19344381194647653 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|f432a478-3b9f-431d-8339-bd9e2e2dceb7 | underdog | Richie Palacios | RBIs | over | 0.19268520416296603 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16093539 | prizepicks | Dylan Raiola | Pass Attempts | under | 0.192631721259933 | 2026-10-23T04:50:52Z | 2026-10-24T15:00:00.000-04:00 |
| underdog|7cff4e33-d73d-44f1-8d0d-5a5bf4c7277c | underdog | Matthew Golden | Receiving Yards | under | 0.1918683958802021 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|7872036b-85f2-4055-9bd7-2b99273655bf | underdog | Liam Hicks | RBIs | over | 0.19143788267825396 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|ec32d38f-4baa-4dd5-b4ce-84216707909c | underdog | Kyler Murray | Pass Attempts | under | 0.191433222145686 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|fa30225c-a2b8-4007-91b4-6e7775ca4b91 | underdog | Kendre Miller | Rush Yards | under | 0.1907546806271176 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1033879b-1237-423e-9da7-e15c7f9830d3 | underdog | Devon Dampier | Pass Yards | under | 0.1901558765692154 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|ee0fd630-668b-45c5-b6f7-9a2833d72609 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.1896770029694203 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a9599a2a-d2a5-4707-b22c-39668c345e29 | underdog | Zay Flowers | Receptions | under | 0.1892743875611844 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|c41836db-df10-4158-bf2a-d471ed143dcc | underdog | Chris Godwin | Receptions | under | 0.18927231998376215 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|83d77d5f-8f56-4d65-99e8-b21e59e22d59 | underdog | Jaylen Waddle | Receptions | under | 0.1879932654958955 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|d7de2d90-b7bd-4c83-9b27-12b0d1ba622d | underdog | Demario Davis | Sacks | over | 0.18797271543795124 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|86267553-d29e-4379-94fe-af64970990b8 | underdog | Elic Ayomanor | Receptions | under | 0.187836672850876 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|22798a80-b20a-40c8-844d-b6c37289bedb | underdog | Victor Mesa | Runs | over | 0.18755383290267014 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|c88c7dcc-4a68-42bb-820d-1bea91c00ef3 | underdog | Adonai Mitchell | Receiving Yards | under | 0.18622570632540836 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|e2f0945f-5958-4cd7-b310-8337022f84ec | underdog | Daniel Carlson | FG Made | under | 0.1857689129268523 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1c65cc1b-d472-4024-abf4-de2531acbd98 | underdog | Rueben Bain | Sacks | over | 0.1854966337408246 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|69170097-9590-4b1c-b393-fe6a547e6eb3 | underdog | Sam LaPorta | Receptions | under | 0.1854602802656819 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|16046139 | prizepicks | Daniel Jones | Pass TDs | under | 0.1853194844296951 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|73e3a771-b2a6-43cd-83d9-5d33eb4aa5d9 | underdog | Kyren Williams | Rush Yards | under | 0.184835086675048 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|80cda42e-dedd-480a-8e61-235d21eae853 | underdog | Kenny Gainwell | Receptions | under | 0.18440203930446974 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16051243 | prizepicks | Denzel Boston | Rec Targets | under | 0.1843661428516428 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|56ea29f1-8ea3-48d1-9471-8c912d8f747f | underdog | Drew Mestemaker | Pass Yards | under | 0.1842856682410804 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|73708500-1d15-4a82-9a36-bc941237ac8a | underdog | Jackson Chourio | Total Bases | over | 0.1840628984275393 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|eae5bd72-059d-4ede-8f80-befde1831596 | underdog | Alim McNeill | Sacks | over | 0.18296204825134377 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|9f05934f-b49e-4994-bd17-9ce1273d9dfe | underdog | Kayshon Boutte | Receiving Yards | over | 0.18201899838674063 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16128102 | prizepicks | Tez Johnson | Rec Targets | under | 0.1819663620320694 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|7da89ab3-c78a-4a6e-a6e2-21a7bb2647e1 | underdog | Bo MacCormack | Rush Yards | under | 0.18194523674499896 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|98e02204-e6fc-49e9-9efb-16eddaa9eb4d | underdog | Jake Elliott | Kicking Points | under | 0.1818784511935599 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|349ae640-0000-4a60-9e69-690f91a9e9ab | underdog | John Mateer | Pass Yards | under | 0.18179868100147756 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|593e72ac-0f96-4213-818e-ddbf2518f26a | underdog | John Mateer | Total TDs | under | 0.18173532099467016 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|ca74e334-4fb2-412b-bdb9-08168dd9098c | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.1815324987306645 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|95e13e96-3915-4814-acdb-210d240d4701 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1799180201769094 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ae863eaa-ab5e-4877-8585-dc5472a4473c | underdog | Emmett Johnson | Rush + Rec Yards | over | 0.17980433605544605 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16046140 | prizepicks | J.J. McCarthy | Pass TDs | under | 0.1795941015500882 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|15f3e859-2c6f-4254-abb6-7275ce408513 | underdog | Nico Collins | Receptions | under | 0.1794482585928581 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fd552aec-bc37-4eb5-8f1b-39fdc7baba5c | underdog | Arthur Fils | Aces | under | 0.1786592826676623 | 2026-10-24T04:39:26Z | 2026-10-24T16:30:00Z |
| prizepicks|16126867 | prizepicks | Carl Rushworth | Goalie Saves | under | 0.17792337173173578 | 2026-10-24T04:39:26Z | 2026-10-24T10:00:00.000-04:00 |
| prizepicks|16128099 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.17773769702399478 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|4cab8863-5993-4392-aac3-07a608ae52ef | underdog | Jalen Royals | Receptions | under | 0.17724030981279304 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|2f2a195e-2969-490a-a0cb-dc5921ec9427 | underdog | Ethan Moczulski | XP Made | over | 0.17591588281902049 | 2026-10-24T04:39:26Z | 2026-10-24T19:00:00Z |
| prizepicks|16051241 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.175795415306488 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|8dc8a64b-8a6d-4bbb-9c34-ed8b89025f6b | underdog | Brandon Aubrey | FG Made | under | 0.1756787358146653 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0bfe77e7-f046-485b-9c54-f72737f36efb | underdog | Garrett Wilson | Receptions | under | 0.1755107928461772 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|945d58cd-109f-4a19-8fb3-bbc4c38caa81 | underdog | Junior Caminero | Runs | over | 0.17528368794326254 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|58600dfe-36a7-46ed-bc53-8334433e51b6 | underdog | Sam LaPorta | Receiving Yards | under | 0.1746918808648834 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|88a723e6-d460-4e58-9ed0-8e2025c0f549 | underdog | Antonio Chadha | XP Made | over | 0.17407875872897388 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|a67515c6-0a36-4241-81e0-d3885298e1cc | underdog | Matthew Stafford | Rush Yards | over | 0.1739326192322227 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|11e17eff-c3c7-4b31-a4e1-eb3c30ed8c12 | underdog | KC Concepcion | Receptions | under | 0.173856293946127 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051252 | prizepicks | Courtland Sutton | Rec Targets | under | 0.1732814208652097 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|f6a20c0d-99dc-42b8-b9a2-1744200a3258 | underdog | Garrett Mitchell | RBIs | over | 0.17214605140301736 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|79299abb-7e2c-441a-8bf3-53cac444158a | underdog | Cooper Pratt | RBIs | over | 0.17214605140301736 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|0c6d1d46-22b0-4e2d-a42a-36569910f084 | underdog | Chris Barnes | Receiving Yards | over | 0.17208451809493552 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|3614abc9-c288-4ddb-a25e-d8e7de7b52ef | underdog | Darian Mensah | Rush Yards | over | 0.1718691063862979 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|92ff74d4-e9bb-4ce1-a7ee-cc356cd7daa8 | underdog | Osa Odighizuwa | Sacks | over | 0.17184980653399948 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|3a35b477-4c60-45fa-9600-f2cc31dc4557 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.17108720887133255 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|c3a86fd2-5057-449b-8f7e-612f9a1bba65 | underdog | Mason McKenzie | Total TDs | under | 0.1708308152413185 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| prizepicks|16051269 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.1706456696230398 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| prizepicks|16128098 | prizepicks | Cade Otton | Rec Targets | under | 0.17054963163974202 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|db8f2b09-cccf-4e7f-a3e0-6e29fc01c4da | underdog | Jalen Nailor | Receiving Yards | under | 0.17006200858051945 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|404ee6e2-c47e-4246-9c9a-08758d28c9ef | underdog | Arch Manning | Pass Yards | under | 0.1700288444215447 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|4d0bdde7-25de-4138-8269-c5164b728256 | underdog | Kamario Taylor | Pass TDs | over | 0.1699637516449155 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|49b762ed-4220-4576-ad51-f08750333ea7 | underdog | Austin Hooper | Receiving Yards | over | 0.16966890486115194 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|de3d8c98-966a-4753-8a4b-527a4158c0f5 | underdog | Isaiah Marshall | Total TDs | under | 0.1694242857956787 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|25c84983-7531-4d73-b90d-493d66582b20 | underdog | Pat Freiermuth | Receiving Yards | under | 0.1693161019733358 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|ee4edd7e-7b6f-41ad-933e-3a50e62080ea | underdog | Bijan Robinson | Receptions | under | 0.1692203598276945 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9356f071-22fc-4b06-8218-7d33d2f4fb9d | underdog | DK Metcalf | Receiving Yards | under | 0.1686306638130101 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|43275f7f-90ab-45a6-9c0b-6693c838cc11 | underdog | Noah Fifita | Pass Yards | under | 0.1685416348261316 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| prizepicks|15945781 | prizepicks | Jameson Williams | Rec Yards | under | 0.1684103099885777 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|2fd5f777-f98d-42fc-b079-413f01d2cea6 | underdog | Harold Fannin | Receiving Yards | under | 0.1684065370519358 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d9483f79-15e8-40bf-bc88-aa1b483059b4 | underdog | Jackson Chourio | RBIs | over | 0.16778803525791475 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|4379cc97-6c42-474d-9885-165493109730 | underdog | Denzel Boston | Receiving Yards | under | 0.167016966353541 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a6dc42f2-7deb-4899-978c-a82ddf28cc59 | underdog | Dani Dennis-Sutton | Sacks | over | 0.1668263272094302 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|b2a4ef33-4dd7-4a8d-bebf-9282e819c744 | underdog | Joe Burrow | Pass TDs | under | 0.1668059378425955 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1583ce20-2aed-4825-9210-33ee84203275 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1662215207642232 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c256d652-d92c-45e5-94af-5b89c102a308 | underdog | Christian Yelich | RBIs | over | 0.16568503193419315 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|02ce9912-bad9-43c4-85d0-1f38db50b2d1 | underdog | Dierre Hill | Rush Yards | under | 0.16513229022505882 | 2026-10-24T04:39:26Z | 2026-10-24T19:00:00Z |
| underdog|f65fcee2-679b-4d27-9424-1835a6bb5ec9 | underdog | Jahan Dotson | Receptions | under | 0.1642390573801065 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b7fc7bc1-d865-4e6d-908b-52a06ee4298b | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.1642276422764228 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|9fd9689b-0460-46da-8dd7-3031fc41a089 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.16347835416618184 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|9ddf5a37-e64d-4f4b-992a-33daca018e66 | underdog | Stefanos Tsitsipas | Aces | under | 0.1628123275983835 | 2026-10-24T04:39:26Z | 2026-10-24T10:00:00Z |
| underdog|4cfd5a4a-1f48-4365-b549-f1ac466a2341 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1626091840811822 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a4418c5e-2715-48f8-b2a9-e4d011256997 | underdog | William Contreras | Runs | over | 0.16223622910386398 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|c452f8b7-8eba-4428-9266-453524c4a278 | underdog | Kyle Ferrie | XP Made | over | 0.1614100094526827 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|5c3c4ca9-70d5-47fa-b40f-f008d064b59f | underdog | Jake Bauers | Runs | over | 0.1612937889533635 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|78c65036-bd71-42f0-8897-248434ccea92 | underdog | Quinshon Judkins | Rush Yards | under | 0.16094408862931908 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|88670807-df28-450c-89b9-2d671c6bfd03 | underdog | Ashton Jeanty | Receptions | under | 0.1596415908383356 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|6683a26b-8799-48bb-82ea-062d512e981c | underdog | Dakorien Moore | Receiving Yards | under | 0.1595997848412829 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|3ef8fdc9-08a4-41d9-8d28-99f6c7438824 | underdog | Andre Szmyt | FG Made | under | 0.159326507096576 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f67c5241-e43a-4a2e-be41-be204fb97d1b | underdog | Brandon Dorlus | Sacks | over | 0.15932503910312887 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|e89c37a5-6ffa-450c-a8c8-188777abb561 | underdog | Maddison Inglis | Double Faults | under | 0.1587743136799873 | 2026-10-24T04:39:26Z | 2026-10-24T06:30:00Z |
| underdog|189483bb-5f96-4e44-a814-7221fd0fde14 | underdog | Zachariah Branch | Receiving Yards | over | 0.15872114669711612 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|15959614 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.1587170648523245 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|3627b2cf-8e83-4470-8053-4744b48edbfd | underdog | Xavier Worthy | Receptions | under | 0.1583155139800515 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| prizepicks|16051232 | prizepicks | Drake London | Rec Targets | under | 0.1578375470720511 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|a72359e4-c625-4fd5-8791-4fd01e9b8c04 | underdog | Devaughn Vele | Receiving Yards | under | 0.1576991448693823 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|7f1b9de6-c09a-48a3-a6b1-890d0fcb4f96 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.15729493148797735 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|021764db-4551-4f29-9724-3d4e2d6cd55d | underdog | J.J. McCarthy | Rush Yards | under | 0.1572331357012335 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3182912b-bec7-451d-a4f6-a8aa028c7477 | underdog | Jameson Williams | Receptions | under | 0.1572143332788562 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5860840c-1704-43fe-bab1-1aacb0bf1fa9 | underdog | Romello Height | Sacks | over | 0.15633908831275967 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|d27438c2-0f93-4eb6-adb3-d42773a93ed8 | underdog | Taylor Walls | Total Bases | over | 0.15556996279174645 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|1281770c-e0ae-468e-a287-4aee48f2c034 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.1550542839780637 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|38c993aa-8bac-47c0-8941-740b3ef24351 | underdog | Dane Pizzaro | XP Made | over | 0.1545552838773531 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|8a310332-5951-4ac7-a77f-6c4a56dd8ed7 | underdog | AJ Barner | Receptions | under | 0.1541940474422654 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|7c562fd8-49b6-44ee-8676-bbf1b6cbac68 | underdog | Bryce Young | Pass TDs | under | 0.1535238626727116 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|37f21c56-5c3a-4702-9320-6b096b6218ef | underdog | Kyle Pitts | Receiving Yards | under | 0.1533697059674438 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051300 | prizepicks | Mason Taylor | Rec Targets | under | 0.1530383580179536 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|b5c654ad-bc35-47ca-b293-18de15295a6f | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.1528088230467457 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|c41b9c5a-8eb4-4e28-b530-7467445701da | underdog | Matthew Stafford | Pass TDs | under | 0.1524509996804636 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|9b5bac7f-853d-4f8d-b23e-638437b1afdb | underdog | Evan Engram | Receptions | under | 0.1522431104423216 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|d0e5175c-f995-4f19-992d-d6a7520bd2b7 | underdog | Jordan Addison | Receiving Yards | under | 0.1520912252614426 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cc956678-f2dc-416c-af59-3565941e17a8 | underdog | Marvin Harrison | Receptions | under | 0.1520330651894664 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3ac62e57-a7e6-4151-8ea8-16076ca580e3 | underdog | Dilin Jones | Rush Yards | under | 0.15173693176861336 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|f1759cba-b4e9-4603-aad8-c383295e0e2f | underdog | Malik Washington | Receptions | under | 0.1516278474524776 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051264 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1515049144076509 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|40c92b84-7aa2-4a31-ae7b-160596e0c514 | underdog | Isaiah Likely | Receiving Yards | under | 0.1509578137931236 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d43fe0e3-78bc-4ecb-b57f-9caa3fe6a1de | underdog | Ka'imi Fairbairn | FG Made | under | 0.15065512869964737 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|849d3a39-5737-43cd-8c6b-7289fdc268ea | underdog | Isaiah Mizell | Receptions | under | 0.15042794011869265 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|3fe03957-f78a-4577-b650-0f54860d6b2e | underdog | Chris Boswell | FG Made | under | 0.1495032069538866 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1fb7951e-4784-4d46-b66e-0e4b56243186 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.14908491831684723 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|eb118ae3-88ec-4af1-a4d5-238969093a3c | underdog | Greg Dulcich | Receptions | under | 0.148738688298966 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aa0b7a3e-d2b1-4670-bacd-e7f0265e9da6 | underdog | Kaelon Black | Rush Yards | under | 0.1484179947276228 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5244df7d-fcfd-411d-8267-7d650d4f5666 | underdog | Jake Bauers | RBIs | over | 0.14841428494246045 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|8e6bce48-c270-48c4-af74-f023a926fd3c | underdog | Trey Smack | Kicking Points | under | 0.1479856099025124 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ddc50985-e940-4ef7-b999-42c9ff78a029 | underdog | Jeremy Hecklinski | Pass Yards | under | 0.14795009038487694 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|cbdf6397-eda3-42b8-8e11-2e87240b78f5 | underdog | Lukas Van Ness | Sacks | over | 0.1479299343980902 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|894876c7-692d-4cf5-95c3-4b0632db54a3 | underdog | Mason Taylor | Receptions | under | 0.1475775689463663 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c14609ad-2239-49ea-85de-1e3db95fb733 | underdog | Tez Johnson | Receiving Yards | under | 0.14757641917703346 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|968ff81d-59d7-4800-83ce-cfa34ff971b7 | underdog | Dak Prescott | Pass TDs | under | 0.1473394026606165 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|3dcd92ab-0c27-4d63-9fb5-575d5f92cffd | underdog | Garrett Wilson | Receiving Yards | under | 0.1471362850852574 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|42debfb2-8c89-4d7f-8ddb-a5d7b2e44b3e | underdog | William Contreras | RBIs | over | 0.147020514490394 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|1ae5d24c-6f16-4cc5-8989-4a8e6240c971 | underdog | Tyler Shough | Pass Attempts | under | 0.1469924013389894 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|b0c4111a-6ff3-4cde-aff6-d4bb5a8e1e6c | underdog | Woody Marks | Receptions | under | 0.14697561493250333 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|c48a289c-ab9f-4495-895d-bcbc743bb51b | underdog | Ethan Moczulski | FG Made | over | 0.1469323117588332 | 2026-10-21T04:43:18Z | 2026-10-24T19:00:00Z |
| underdog|9e7823b5-6ba8-4931-8647-93f4834676fa | underdog | Tucker Kraft | Receptions | under | 0.14624892899467 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|359ed06b-9344-42b7-a543-df0895950a41 | underdog | Samaje Perine | Receptions | under | 0.1460568513705 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f70f42be-abab-443f-b135-0ed8073fcb63 | underdog | Aidan Chiles | Total TDs | under | 0.14566990256864543 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|9383f367-9dd3-49a0-8e9b-13c265badd06 | underdog | Jake Bauers | Total Bases | over | 0.1454545454545454 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|9fb64b31-fb4e-4775-8815-fd8a63623c12 | underdog | George Pickens | Receiving Yards | under | 0.1449746054605076 | 2026-10-21T23:24:30Z | 2026-10-27T00:15:00Z |
| underdog|6f6d00d7-38cc-4885-97b4-d1c12e4f2660 | underdog | Sam Williams | Sacks | over | 0.14422589886109222 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16051233 | prizepicks | Jahan Dotson | Rec Targets | under | 0.1439163357553819 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|39512b8d-dd2c-4104-92e8-1dcfc8ff0331 | underdog | Jalen Brooks | Receptions | under | 0.1437414270624527 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|8249186f-8862-4abc-9a48-7f8b007560fd | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1436257422239731 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e246b340-d805-4ba1-bd8b-4c6ecd0db227 | underdog | Dylan Edwards | Receiving Yards | over | 0.14346903173937264 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|3a21ad77-2638-4099-ae84-863dd656a054 | underdog | Chris Olave | Receptions | under | 0.1432171019256236 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a5c7fe6d-1a20-451b-a6f8-7879b27d6f11 | underdog | Derrick Henry | Rush Yards | under | 0.1431595063697152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bfcce5cc-c027-490d-8076-653dd3f79753 | underdog | Alex McPherson | XP Made | over | 0.1430779996374752 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|3d94aff5-fc92-4326-81da-a055e3c9a51e | underdog | David Hamilton | Total Bases | over | 0.1425947219339821 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|f06599db-6e94-41c7-b4e8-7df338f7a276 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.1424277006620714 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|6519da18-ac63-48a8-999f-abb2d8f78d4c | underdog | Arch Manning | Total TDs | under | 0.14238323705330513 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|ed3825a2-9c90-4618-bea7-7776443f101b | underdog | Bear Bachmeier | Pass TDs | over | 0.1419644793617892 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|75017fcb-3953-4cb7-b182-7145bd12f5ca | underdog | RJ Harvey | Rush Yards | under | 0.141851915435678 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|a44b2e7b-3b72-4501-9872-4e4fd70ab6bf | underdog | Christian Watson | Receiving Yards | under | 0.14179501125685845 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|7d5acb95-0afa-4e4f-9047-78103de8d00c | underdog | Kyren Williams | Rush + Rec Yards | under | 0.1415908950620287 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|511bd490-625c-46c8-bf34-df7019f5fa32 | underdog | Keion White | Sacks | over | 0.1415282710501512 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|e58c86c8-e648-43d4-b9d2-cabbfd06a61d | underdog | Drake London | Receptions | under | 0.1414594528835526 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|edd88ba0-b0bc-4c4b-bab1-6ced4e331af8 | underdog | CJ Donaldson | Receptions | under | 0.14138497062268784 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945777 | prizepicks | Michael Wilson | Rec Yards | under | 0.1412964357388831 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|bcedd6a5-9b12-434f-9ff9-088d92123f8f | underdog | Kirk Cousins | Rush Yards | under | 0.1412416511943182 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|33ee1c24-80b7-4a1d-ac59-1706d8770d44 | underdog | Caleb Hawkins | Rush Yards | under | 0.14098430850012955 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|ff359966-c8d3-48b1-9983-24650e564e95 | underdog | Emanuel Wilson | Rush Yards | under | 0.14078081962084332 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|cfc8d50f-dd4a-4ca7-bd79-8e305ce425d6 | underdog | Jaden Craig | Pass Yards | under | 0.1407745117400555 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|f99428c7-8e32-4a6a-915b-3a102c256e74 | underdog | David Olano | FG Made | over | 0.14026422999009447 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|7e32077b-6ff8-4003-b1be-f10985089148 | underdog | Caleb Douglas | Receptions | under | 0.1399122387421394 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|bde51c31-49f9-4ac5-ac7a-e2c75ddf5376 | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1395539397663328 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|48b922ca-bdb6-4e04-8520-17e4b9d55fee | underdog | Aidan Chiles | Pass Yards | under | 0.1394975675051353 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|9c22489a-921c-4a35-a1f6-ba9e6aee26d3 | underdog | Carnell Tate | Receiving Yards | under | 0.1394857182718097 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0143747-2eae-48ea-a3a6-8fab2c79ffeb | underdog | Michael Wilson | Receiving Yards | under | 0.1390199081777683 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|df77b125-2d5a-4fbe-a65c-83ddb7d6795f | underdog | Chris Jones | Sacks | under | 0.13828623575350096 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|44a4e634-3c12-458a-8a81-c8b06b39a7d7 | underdog | Will Hammond | Pass Yards | under | 0.1382318502544831 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|6e080788-8634-47c3-bd6e-7726cac733b2 | underdog | Rico Dowdle | Receptions | under | 0.1377303975112497 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a2bcf936-3120-46b9-a87d-b57713161c43 | underdog | Preston Rex | Rush Yards | under | 0.13633104542314856 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|13caf8a7-8887-4d40-b56b-1caca86e6d79 | underdog | Jauan Jennings | Receptions | under | 0.13615627510133188 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|990e3a36-0fa9-42d5-b447-447c46e0605b | underdog | Germie Bernard | Receptions | under | 0.1357845862590205 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|b20602df-b17c-4bb4-a6c4-1d4091790ae8 | underdog | Jonnu Smith | Receiving Yards | over | 0.1356458877681902 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|7391bff4-eda5-4a59-9d91-9864b0eb80fd | underdog | Jonny DeLuca | RBIs | over | 0.13551921460146987 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|a5dc555d-b835-41b2-b481-a747557a08b5 | underdog | Malik Nabers | Receiving Yards | under | 0.1355033403010405 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|575f222c-106d-4acd-bb96-fa38483730e4 | underdog | Jake Ferguson | Receptions | under | 0.1353654788338305 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|6aae9f5a-fcf3-47ab-a732-e20798619a6d | underdog | Nick Herbig | Sacks | over | 0.13536125851694314 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|b3dc7132-c2a2-4e3a-a11d-8be05eb6f82c | underdog | Junior Caminero | RBIs | over | 0.13525068013991448 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16051259 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.1350314279342374 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|e54f38c1-9c9a-4acf-9119-50e592375ad1 | underdog | Kenny Minchey | Pass Yards | under | 0.13411309437907204 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|84f62971-2d32-45a7-aa4d-7ab7e3f27a3d | underdog | Malachi Fields | Receiving Yards | under | 0.133936831108967 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|75d61aa1-7845-40a4-a1f7-85efdf585c7b | underdog | Princely Umanmielen | Sacks | over | 0.13388692782737888 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|7e24c2fc-b2a9-4cda-b16f-b9bc6153a23e | underdog | Greg Dulcich | Receiving Yards | under | 0.1336970921172516 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a10c41a7-9c38-40f4-a975-b99cfceab816 | underdog | George MacIntyre | Pass TDs | under | 0.13367404203418298 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|d4974c1b-7b7d-4201-bb0e-6cc04f67b9b5 | underdog | Kaleb Edwards | Receiving Yards | over | 0.1335945665689411 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|9ea38e9c-1d50-4e59-ac7a-7d8f082f7680 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.1327805088333317 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|1c29b99d-222a-4b53-8471-6ed50763c80d | underdog | Jaylen Waddle | Receiving Yards | under | 0.13267795028063345 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|19d3a6a2-1062-45c3-a09a-3a65050bd272 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.13205782499315033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b19f3052-9b2b-4892-9d9c-c814a1c421b8 | underdog | Jake Bates | FG Made | under | 0.1319024702666141 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a49fb210-9a51-4589-b092-bc9895a1ee4a | underdog | Gunnar Helm | Receiving Yards | under | 0.1316121759984837 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d74f82ee-d5f7-40d2-ac36-71cc37b42543 | underdog | Jordan Watkins | Receiving Yards | under | 0.13159640770920988 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ba49f517-710c-4051-95b6-4f8355eef1e7 | underdog | Bucky Irving | Receptions | under | 0.13158399196209436 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b1f9ad06-cd7d-4e5a-959b-569a72213b85 | underdog | Radarious Jackson | Receptions | over | 0.1315816830185312 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|91b4fa0f-a854-402a-8f83-b25bccd153a0 | underdog | Ian Thomas | Receptions | over | 0.1315316679906075 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|443ec428-a877-4631-bdf4-806c0b198809 | underdog | Konata Mumpfield | Receptions | under | 0.1309218799606248 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|362a367a-8287-4a9b-afac-79b549e4c9a2 | underdog | AJ Barner | Receiving Yards | under | 0.1306153642795884 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1b176313-e08a-4847-957b-32a569fdd619 | underdog | Danielle Hunter | Sacks | under | 0.1305467838319396 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|00b01f82-0268-4b96-b82c-afd43774bbb8 | underdog | Jackson Kleather | FG Made | over | 0.1303279119894879 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|82852cfd-efd1-4915-9961-43072a434d02 | underdog | Lamar Jackson | Rush Yards | under | 0.13026069436091892 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|d06eefe7-d221-4b8a-847e-dacdc1cae223 | underdog | Tyrone Tracy | Rush + Rec Yards | under | 0.1301385570274678 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b832c29c-26dd-4b07-a2d1-feaa7b7e7052 | underdog | Dallas Goedert | Receiving Yards | under | 0.1296687932557064 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|02d34a8f-3eed-4486-9769-1d3795f45afb | underdog | Nick Folk | FG Made | under | 0.1295761284029778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7da699a4-50a1-4dd2-b233-b79054316f54 | underdog | Wayne Knight | Receptions | over | 0.1290023444417333 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|e0969448-03e0-46e5-8539-6af71c7891ee | underdog | Gavin Freeman | Receptions | under | 0.1287710162149922 | 2026-10-23T04:50:52Z | 2026-10-24T17:00:00Z |
| underdog|34d055d7-33a5-4401-a090-0d03599b6aa7 | underdog | Caden Buhr | FG Made | over | 0.1283755219195639 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| prizepicks|16051245 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.1283711896398486 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|fe9a8643-cbb5-455e-917e-c33f3a025f7c | underdog | CeeDee Lamb | Receiving Yards | under | 0.1283347069925714 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|87fa81f1-4e8b-4f24-be98-1f49a7ee7f3a | underdog | Jayden Maiava | Pass Yards | under | 0.1279852222492714 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|0e68c868-6ccc-4fc9-8f71-5f130198661b | underdog | Bam Knight | Rush Yards | under | 0.12777840450237876 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|26d39b80-32f6-4d20-a89d-ce35e5c3bf55 | underdog | Jaylen Warren | Rush Yards | under | 0.1269833611823008 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ab744591-112e-49f8-88d0-de9771ab275d | underdog | Zay Flowers | Receiving Yards | under | 0.1266709228488783 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|6498dd8f-86d2-4c9f-a32f-689bc2c4bd76 | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.12641038555342476 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|b49a48bd-8058-449f-9388-8e31f44083ec | underdog | Kewan Lacy | Receiving Yards | over | 0.1261368582759802 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|39d3e316-5d17-465f-b268-469f78421358 | underdog | Tony Pollard | Receptions | under | 0.1260078504794592 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|40fdb3ab-4753-4d0e-b8f0-958e1cd508c9 | underdog | Nick Marsh | Receptions | under | 0.12593914764985736 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|0a9fbe3d-92db-484b-ba0f-ec618dfa3cd8 | underdog | Noah Gray | Receptions | under | 0.1256611502062177 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|7c54ff16-5ba7-493a-94fb-4e5c055ac228 | underdog | Isaiah Sategna | Receiving Yards | under | 0.12566072375453674 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|b3bf83ab-c79a-442e-a00a-95213b95e3de | underdog | Jake Ferguson | Receiving Yards | under | 0.1255662633886676 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|9d76b014-0fc4-4360-b3c4-6c3715996d7b | underdog | Carnell Tate | Receptions | under | 0.1254536750854675 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d9566fef-1840-4236-9053-b188e30aeb72 | underdog | Braylon Staley | Receiving Yards | under | 0.12444674535911959 | 2026-10-23T13:31:04Z | 2026-10-24T19:30:00Z |
| underdog|64ae0032-0dcd-42ee-951d-5b145e18e874 | underdog | Carson Schwesinger | Sacks | over | 0.12401156184683859 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|90c1dd53-3be2-43de-bf0b-baf6a360086b | underdog | Jerry Jeudy | Receptions | under | 0.1240065201300302 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|d9fe3afc-f162-42e1-b3d8-8569a9f122a1 | underdog | Alberto Mendoza | Pass Yards | under | 0.12372959342051237 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|eaddf12e-bf09-415a-9908-175b69e1378e | underdog | Joey Slye | FG Made | under | 0.1236431134007916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|74b3c34c-cbfd-479b-94fa-0c0b82800a8b | underdog | Dylan Raiola | Pass Yards | under | 0.1233911109612369 | 2026-10-24T04:39:26Z | 2026-10-24T19:00:00Z |
| underdog|61e7bf09-5421-4218-9b7d-53d1a654a3cc | underdog | George Pickens | Receptions | under | 0.1233908843202937 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|15945770 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1232415700497886 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|4e1224d2-e2fd-43b7-8c29-e9e7cf08c5f7 | underdog | Ashten Emory | Rush Yards | under | 0.12283039240148308 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|5e206181-9207-4bfc-88c8-f03aab0fb4c2 | underdog | Kenny Gainwell | Rush Yards | under | 0.12235820841958012 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|8248b0a4-7bbb-45f0-bb6b-f4afa7b390e3 | underdog | Tyrone Tracy | Receptions | under | 0.1223478921251329 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|15945069 | prizepicks | Derrick Henry | Rush Yards | under | 0.1220323805962527 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c3ffc3dc-69cd-49aa-a562-08776aa496c7 | underdog | Liam Hicks | Total Bases | over | 0.12173659673659665 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|2208d8d1-a462-4f13-a450-9e199aa06230 | underdog | Leonard Williams | Sacks | over | 0.1209722728248454 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|b4c1532b-82e4-44b9-b6eb-6fed241492bc | underdog | Derick Hall | Sacks | over | 0.12084592824767443 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|e362134a-febb-4a49-91db-9bbff996595b | underdog | MarShawn Lloyd | Receiving Yards | over | 0.12083104520736526 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|f7504d22-6145-4664-907b-263f5268a335 | underdog | Jordan Dwyer | Receiving Yards | under | 0.12076719522721713 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|3a053953-ec02-4875-bd19-fe66af684bf0 | underdog | Sam Darnold | Pass Attempts | under | 0.12062481839113282 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|47d2239b-9245-4a9f-a3af-efc901f6a31d | underdog | Pierre Strong Jr. | Receiving Yards | over | 0.1200814951903969 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051293 | prizepicks | Devaughn Vele | Rec Targets | under | 0.1192863816858713 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|9b47512a-afb1-4998-9a20-5d52f79cd0f4 | underdog | Junior Sherrill | Receptions | under | 0.11912444157661717 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|2b96e389-ec54-4965-a240-5d2e6eb051a0 | underdog | Jason Sanders | Kicking Points | under | 0.1187154660907585 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a04b010f-6f7a-4bca-bf84-a019fdc98cb2 | underdog | Jason Myers | FG Made | under | 0.1186141311795658 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e642bd88-7ada-49a6-bc3e-0426f77a3d02 | underdog | Jared Goff | Rush Yards | over | 0.1184823448445742 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|37c7f3a7-4eea-4ab7-bb95-51317d560802 | underdog | Christian McCaffrey | Receptions | under | 0.1181179607177566 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e96add8e-c781-442e-a464-2a7065a9227f | underdog | Justice Haynes | Rush Yards | under | 0.11799020614397115 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|18050014-bcc4-476c-89df-63b77bd75564 | underdog | Josh Sweat | Sacks | over | 0.11763891786002173 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|c55b0743-540a-494e-a977-109a525d9821 | underdog | Jordan Shipp | Receiving Yards | under | 0.11738020978616703 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|5a19d403-37ab-402e-958a-f872523cc695 | underdog | Laquon Treadwell | Receptions | under | 0.11729373694819256 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|55fcc996-4490-4c11-90b8-a80c3e2e57e3 | underdog | Patrick Mahomes | Rush Yards | under | 0.11724343659207292 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|bea4dc65-3219-4de0-9721-19a9becb8a7d | underdog | Keenan Allen | Receiving Yards | under | 0.1171946925687916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd0fc4c4-17dc-42fa-9656-b749a1f7d2ea | underdog | Blake Cashman | Sacks | over | 0.11713225592155074 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|66772312-3a35-456b-83a2-8f6715ca3611 | underdog | Will Anderson | Sacks | under | 0.117020833157628 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d6d91cbb-f5ff-4b1c-ae9c-9cb431a3bc9e | underdog | Junior Sherrill | Receiving Yards | under | 0.1165194099008191 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|8ac9a780-d1c0-4481-b02d-99d01d5ad8ef | underdog | Bucky Irving | Receiving Yards | under | 0.11641272640515987 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a8389eaa-f9e8-4862-9d49-e0eb14b5dbe3 | underdog | Geno Smith | Pass TDs | under | 0.1162581741290298 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16042874 | prizepicks | Cole Tabb | Rush Atts | under | 0.11608114452027218 | 2026-10-24T04:39:26Z | 2026-10-24T12:00:00.000-04:00 |
| underdog|1fb99745-67aa-4413-9e04-c89887b3cdf6 | underdog | Cooper Pratt | Hits + Runs + RBIs | over | 0.11595771002291405 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|5af52c05-0b3e-4d2c-a674-56afd14be234 | underdog | Brice Turang | Total Bases | over | 0.11564318034906274 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|9c0ab175-645e-4e81-8a2d-b2bffe22a35a | underdog | Braylon Staley | Receptions | under | 0.11553944780418735 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|d4109d54-463b-49c4-8d4a-55997cd5a25e | underdog | Jalen Nailor | Receptions | under | 0.11535940257387334 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|b4026f26-728a-4552-8fda-890d6d95855a | underdog | David Hamilton | Runs | over | 0.11520899192132067 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|43da2b56-6f19-429a-884b-a4c12ba9020c | underdog | Rashid Shaheed | Receiving Yards | under | 0.1151993821374695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|1b0fc4dd-38ef-4e17-85a8-e24686ccb9a1 | underdog | Drake London | Receiving Yards | under | 0.1146582581752583 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8ac96afb-46f0-4924-9765-9144862ff599 | underdog | Conor Talty | FG Made | over | 0.1146366001969039 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|43c485e5-9c93-4255-b8d5-e107d4a97583 | underdog | Malachi Toney | Receptions | under | 0.1145610050421888 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|2f1f417f-135b-4830-a474-fb5c75784b48 | underdog | KJ Duff | Receptions | under | 0.1145312653667987 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|ce1007f8-220c-4655-b458-f67911fa0823 | underdog | Bear Bachmeier | Total TDs | under | 0.1142811564602213 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|08f2910b-5bbc-47f8-bacc-3dff28ef8e33 | underdog | Daniil Medvedev | Aces | under | 0.11426240056968717 | 2026-10-24T04:39:26Z | 2026-10-24T13:00:00Z |
| underdog|e85445e5-423b-403d-b942-d8c2f9c8c893 | underdog | Baker Mayfield | Rush Yards | under | 0.1140527808285041 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f52f977d-a4a3-4e60-9c0b-7eec28e0f681 | underdog | Trent Walker | Receptions | under | 0.11398165369782698 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|6a027ba4-a559-4acd-aaab-ecdbbdaa4f47 | underdog | Griffin Wilde | Receptions | under | 0.1139519591506299 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|605c17ed-f34e-4fb2-8996-a030730c5a60 | underdog | Kevin Jennings | Total TDs | under | 0.11392754655474957 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|fa016a67-39b5-4de6-bed1-c7d5cc5acac1 | underdog | Jeremy Hecklinski | Pass TDs | under | 0.11354866650633832 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|8bc12081-ea2e-4ef8-9975-4cd0509a33b1 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.11320895442534473 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|b4fdcabe-4236-4ba3-b391-25a3dce3c454 | underdog | Cam Coleman | Receptions | under | 0.1130325570488033 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|d2269243-dd1c-4eca-a291-5a694b2fae84 | underdog | Tommy Carr | Rush Yards | over | 0.11293957548012523 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|157bb4f2-7d8e-46e6-bbc2-d96f6ce7d1ef | underdog | Eric Wilson | Sacks | over | 0.11293704759554901 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|85560838-e552-4d85-8d61-33d8f0a1f89e | underdog | Brock Purdy | Pass TDs | under | 0.112816096678015 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f6ee7d09-2550-4ac4-9cc8-9617b54f576d | underdog | Hogan Hansen | Receiving Yards | over | 0.11276187094050905 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|9f7f94fb-18db-4267-82c6-9b35a07b956f | underdog | Garrett Mitchell | Batter Walks | over | 0.11239573434695388 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|7dc6f951-9b3d-40a5-b445-de5ee0a7be8e | underdog | Christian Yelich | Batter Walks | over | 0.11239573434695388 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|dbe0fe3c-cf1b-4a10-a559-85faa5dfe813 | underdog | Ann Li | Double Faults | under | 0.11233600780675801 | 2026-10-24T04:39:26Z | 2026-10-24T04:30:00Z |
| underdog|32fc1802-fd8f-4a28-844d-71abcb793adf | underdog | Chase Brown | Rush Yards | under | 0.11231993620023117 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|c4a30c98-3ee5-437f-83ee-cef25c93d92c | underdog | Travis Kelce | Receptions | under | 0.1120341726504789 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| prizepicks|16051278 | prizepicks | Tre Tucker | Rec Targets | under | 0.1120161055590794 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|fcafb323-e005-4a22-964c-ea114b457bc0 | underdog | Deshaun Watson | Rush Yards | under | 0.1115471354898498 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051309 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.1111545654187005 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|d06fae69-fd00-458d-9aa6-209d3b9736f0 | underdog | Cam Skattebo | Receiving Yards | over | 0.1109557452316625 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|2f03ca60-0a15-44c5-92f4-51e5ced470e7 | underdog | Jalen Coker | Receiving Yards | under | 0.1109302760189151 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051234 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.1104253678764338 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|0051a452-fb9b-40ad-a637-151babcd7f3f | underdog | Nate McCashland | XP Made | under | 0.11039644702665496 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|a478ba13-6753-4bc9-921e-0d90fa1f54e0 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.11017739902575574 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|5c1d01bf-5469-4fb9-a3ad-d8a4de3206a2 | underdog | Spencer Shrader | FG Made | over | 0.110097123969825 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16127036 | prizepicks | Noah Atubolu | Goalie Saves | under | 0.10947409010495268 | 2026-10-24T04:39:26Z | 2026-10-24T12:30:00.000-04:00 |
| underdog|3a8bf996-c4f4-4eb5-9184-c95e30c03dc3 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.10861091931790107 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|8d8b31dd-ce32-4d87-b357-b939087eefe2 | underdog | Yandy Díaz | Total Bases | over | 0.10823792931806853 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|3b766a66-0018-4174-9c44-850d7caef285 | underdog | Matthew Stafford | Pass Attempts | under | 0.1082286184366853 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|482c6383-6992-4a0a-9f28-ef1f56597414 | underdog | Sam Leavitt | Pass Yards | under | 0.10818243537421335 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|9cc0c199-3698-4676-a6b5-d337c67ff542 | underdog | Blake Corum | Rush + Rec Yards | under | 0.10809334251465941 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|b01b4479-d0ff-4f0b-aa25-8572040fd5fb | underdog | Logan Hall | Sacks | over | 0.1080312577396586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|baf9d73f-2d37-4215-9e02-911fbea3f57a | underdog | LaNorris Sellers | Pass Yards | under | 0.1077114435091685 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|8e628752-d92e-437b-bdaf-439d79438856 | underdog | Samaje Perine | Rush Yards | under | 0.10769157598457713 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|c37e171f-5e70-4561-abd4-a2dca0b9ba20 | underdog | Mason Taylor | Receiving Yards | under | 0.1075683290440285 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051260 | prizepicks | Jameson Williams | Rec Targets | under | 0.1071890637021601 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|ae310fd2-3e4f-4081-9ec9-a79480ca7e73 | underdog | RJ Harvey | Rush + Rec Yards | under | 0.10677511795600558 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|427ce93d-828f-4e32-8a32-f3f2f5792078 | underdog | George MacIntyre | Pass Yards | under | 0.10614597241920243 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|1546548b-1134-41cc-9c61-82a9962eea67 | underdog | Sam Leavitt | Total TDs | under | 0.1060186137541691 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|2c93e22e-52d9-46ab-ba7b-0f7f3bd02f5c | underdog | Victor Mesa | RBIs | over | 0.10566928680429588 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|0660c889-a4a5-4941-beff-bf58b7b65837 | underdog | Deshaun Watson | Pass TDs | under | 0.1056653767810689 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|32c6a58f-4543-44ab-9513-73e8857d24bb | underdog | DK Metcalf | Receptions | under | 0.1054909425928073 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|4de78ef5-2ba0-41c0-a0a3-c4aa52f9c656 | underdog | J'Koby Williams | Rush Yards | under | 0.10542670636858342 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|5549b40f-c25b-4262-aa4b-46e8542b8221 | underdog | Brock Bowers | Receptions | under | 0.1052220927493255 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ea37df82-0d35-4f1b-acc4-e9a83779e8c9 | underdog | Conner Weigman | Pass TDs | over | 0.1050716675351449 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|b0bfe51b-13d6-4b91-acea-d98feb1896bd | underdog | Byron Young | Sacks | over | 0.10495469745057584 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|a4c421cb-08f2-4069-8b5c-bbd17b13dfe8 | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.1048589004293351 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|65ed8d6f-70cd-4f13-9b37-fff2700d0487 | underdog | Troy Franklin | Receiving Yards | under | 0.1046037934121351 | 2026-10-23T04:50:52Z | 2026-10-25T20:05:00Z |
| underdog|6c4f1fe9-524b-4bc2-b0e2-3fd92bd6f5b4 | underdog | Kenny Gainwell | Receiving Yards | under | 0.10426959129297086 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|0d312971-5e90-44b0-98ba-ce4e6f8abf3e | underdog | JC French | Pass TDs | over | 0.1041573990796 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|847d369b-bb80-447b-aeee-991efdf3af3d | underdog | Darian Mensah | Pass Yards | under | 0.10384928392549575 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|7bddc13b-1e8e-4ba5-8052-bb3dca935528 | underdog | Ashton Jeanty | Rush Yards | under | 0.1036891044730264 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|54680c7c-61e6-4921-be29-813cc4a2f7ce | underdog | Denzel Boston | Receptions | under | 0.1035724114812719 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051244 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.1034529192752869 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|e6179532-9e03-4921-b671-c168bf048757 | underdog | Adonai Mitchell | Receptions | under | 0.10320337539846192 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16127503 | prizepicks | Nadiem Amiri | Shots | under | 0.10319272770552435 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00.000-04:00 |
| underdog|26709e07-fec3-4650-91eb-030156843dbd | underdog | Junior Caminero | Hits | over | 0.10279207781041244 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|66a12d68-7694-45bf-bff5-0baebc9e9694 | underdog | Brandon Aubrey | Kicking Points | under | 0.1027789805682906 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|16025370 | prizepicks | Anthony Woods | Rush Atts | under | 0.10264130665463933 | 2026-10-24T04:39:26Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|1076b2e6-2055-4da5-9618-5952bef09f22 | underdog | Trinidad Chambliss | Pass TDs | over | 0.10246725800174455 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|fc902a02-0f0c-4227-abdc-bcd4c95ea4f6 | underdog | Carl Granderson | Sacks | over | 0.1022039628793836 | 2026-10-24T04:39:26Z | 2026-10-25T13:30:00Z |
| prizepicks|16128085 | prizepicks | Keenan Allen | Rec Targets | under | 0.10214355522625473 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|820386fd-f6a7-4a4f-b07b-4e867332ff05 | underdog | Tony Pollard | Receiving Yards | under | 0.1020926537605008 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16025299 | prizepicks | Wayne Knight | Rush Atts | under | 0.10184668395682339 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| prizepicks|16094300 | prizepicks | Kendrick Raphael | Rush Atts | under | 0.10157452904230857 | 2026-10-24T04:39:26Z | 2026-10-24T12:00:00.000-04:00 |
| underdog|78cf6f0e-5783-48ec-8b8d-1375889b9481 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.10146487350940303 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|883c9554-18e2-4c83-a8e4-86d5eff8ca2d | underdog | JC French | Rush Yards | over | 0.1013785104343703 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|ff61b03d-9f28-44a0-ab24-2363edfd3351 | underdog | Travis Kelce | Receiving Yards | under | 0.101127840693776 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| underdog|5bee9c19-46e7-45de-9505-7fffe7682621 | underdog | Colton Joseph | Pass TDs | over | 0.1009178937061043 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|bdd208dd-4e0d-4782-960c-7392e03373a9 | underdog | KJ Duff | Receiving Yards | under | 0.1006835033376762 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|4cb67320-4cea-4a1f-a732-f390fda796c2 | underdog | DeVonta Smith | Receptions | under | 0.10038240853526892 | 2026-10-23T04:50:52Z | 2026-10-27T00:15:00Z |
| underdog|a5031682-851a-4242-a86f-deeb9aa6ec6d | underdog | Josaiah Stewart | Sacks | over | 0.10024193483759136 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| prizepicks|16051305 | prizepicks | Germie Bernard | Rec Targets | under | 0.0999657351122397 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|01d3fe0d-6df4-4d43-91ed-c5a1aebc74a2 | underdog | Mark Andrews | Receptions | under | 0.0998519844527912 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|557db697-20ab-4b71-b516-64a4afeb68ce | underdog | Aidan Chiles | Pass TDs | under | 0.0996663803350599 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|23e720da-8343-4c9e-b954-bcd44ed56847 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.09962653784562692 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|01d7bd14-2cea-4655-87f7-1df94b0cfe7e | underdog | Nick Folk | Kicking Points | under | 0.09955642389684627 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a7d239a1-d17d-4c67-bbad-7f823dd294f6 | underdog | Sal Frelick | Total Bases | over | 0.09944751381215466 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|0904f38d-07a9-484d-bf1a-a810b718c0ef | underdog | Richie Palacios | Total Bases | over | 0.09944751381215466 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|ba0ba8fd-220f-46dd-9bd8-d826cf8c883b | underdog | Bam Knight | Rush + Rec Yards | under | 0.09938008332001058 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|c11d0c21-6120-4391-9ab3-73a426a17db1 | underdog | Davion Brown | Receiving Yards | over | 0.09911347794535608 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|602ad854-cba6-4aa9-938a-771d9ab27f0d | underdog | Tyler Higbee | Receiving Yards | under | 0.0990552102507815 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|0e6b9f02-0e24-4698-a06c-0fddfa7d7a4b | underdog | Christian Yelich | Total Bases | over | 0.0990259740259739 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|3d3c2c05-d629-473e-b0a9-64c5a643642e | underdog | Adin Huntington | Sacks | over | 0.09842241278974956 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|81ae88d0-af73-4cfc-80cd-8580d1ab72f3 | underdog | Tait Reynolds | Pass Yards | under | 0.09830056944410115 | 2026-10-23T13:31:04Z | 2026-10-24T23:00:00Z |
| prizepicks|15945774 | prizepicks | Jaylen Waddle | Rec Yards | under | 0.0982250040001608 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|7d98395f-f4ec-4d64-9c69-e4f7cc2131a7 | underdog | Jake Bates | Kicking Points | under | 0.0977903849845823 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|617cc43d-1693-42d3-baf7-6c7b2f500635 | underdog | Darnell Mooney | Receiving Yards | under | 0.09754939271681284 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|785d8153-ed65-433a-98ff-d1df6189376b | underdog | Kyler Murray | Rush Yards | under | 0.09745252830194728 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|aa464685-78e6-4276-b20e-05deb51392e2 | underdog | Dylan Lonergan | Pass Yards | under | 0.09731344523343077 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|724bb94f-576e-4f8b-93a8-be17d494866c | underdog | Dakorien Moore | Receptions | under | 0.0970600476350808 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| prizepicks|16051262 | prizepicks | Christian Watson | Rec Targets | under | 0.096747312779029 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| prizepicks|16010772 | prizepicks | Brock Bowers | Recs | under | 0.09671057143934203 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|45b83e3a-358b-4be0-8355-8c5baf5121e2 | underdog | Zach Sieler | Sacks | over | 0.09641209131875139 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|56e0f4b6-c8b5-4080-a302-a23c5afdfed8 | underdog | Christian Watson | Receptions | under | 0.0962434061653429 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|abbe1cc3-5354-4a9a-a9b9-18eb38d2da6d | underdog | Jonah Coleman | Receptions | over | 0.09620559167514198 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|7fcb6e7d-fbad-444a-ab90-a9fa1175351d | underdog | Jayden Maiava | Pass TDs | over | 0.0960556570545642 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|740f3e34-29ab-4fed-ae75-13f0bc56660e | underdog | Tyler Loop | Kicking Points | under | 0.0958446334098082 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d1654863-f01c-47db-9d4f-a80c3bb9857c | underdog | Marvin Mims Jr. | Receptions | under | 0.0957341704310761 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|ca7aafa2-8aa7-40d7-943b-d0b95afb247d | underdog | Bryce Lance | Receiving Yards | under | 0.09563747315955529 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|15945789 | prizepicks | Travis Kelce | Rec Yards | under | 0.0956329735871087 | 2026-10-21T04:43:18Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|622358a1-32b3-4b91-a383-96112df75b87 | underdog | Dylan Raiola | Pass TDs | under | 0.09537993661511324 | 2026-10-24T04:39:26Z | 2026-10-24T19:00:00Z |
| underdog|25ed5f3f-a2de-45eb-b5dc-ebf775b350ce | underdog | Andre Szmyt | Kicking Points | under | 0.0952743873816968 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6a798cc2-869f-4765-8413-cbdeb21f919f | underdog | Dylan Lonergan | Pass TDs | over | 0.0945615929103332 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|008172e8-e26a-4dd8-87f8-7aca2ed69421 | underdog | Keelon Russell | Pass Yards | under | 0.09455753371368913 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|7f3968ae-aba8-4755-95a9-c5ba93add8c1 | underdog | Dylan Edwards | Rush Yards | under | 0.09395845220020571 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|f824e6dd-281a-4b38-a0d7-75932b24fe55 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.09380971404807426 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|ee06f148-6f88-45e6-8880-02b1b55d5881 | underdog | Tyler Allgeier | Receptions | under | 0.09376242710196492 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|e101f669-6227-48bc-9a08-5a2c1cad57df | underdog | Isaiah Sategna | Receptions | under | 0.0935543794942828 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|b2a7fda4-f58c-4ca3-9951-f635bcaafabd | underdog | Byrum Brown | Pass TDs | over | 0.0933369173961139 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|535f1a5b-2ce2-481c-82bf-40f63ea8573b | underdog | David Bailey | Sacks | under | 0.09320237120215535 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|a8968aa0-639f-4060-a9da-d2f86ffc4e98 | underdog | Jackson Kleather | XP Made | under | 0.0924910603851204 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|61f4cf0f-c609-4ce9-99ff-1b7e55132d14 | underdog | Caleb Douglas | Receiving Yards | under | 0.0924857504634089 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ddd1d82b-b64d-4ead-8c47-1606dfc1f449 | underdog | Kenny Minchey | Pass TDs | under | 0.0924523671302844 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|aec94453-324b-4f3e-9b80-e8d5733e94ef | underdog | Michael Hawkins | Total TDs | over | 0.09225976669624447 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|280d7041-8b6c-4dd7-8d58-69f9ecb8dc19 | underdog | Felix Anudike-Uzomah | Sacks | over | 0.09223808023020835 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|911a1409-7dd1-4302-938f-a14d42eca102 | underdog | Reis Kessel | Receiving Yards | over | 0.09217039539678229 | 2026-10-24T04:39:26Z | 2026-10-25T02:00:00Z |
| underdog|5e49237b-efd4-43c0-b1c9-1e896f1e1de8 | underdog | Rashod Bateman | Receptions | under | 0.09202654093256402 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|d2968887-1877-4e52-8478-b20b88c59272 | underdog | Kayshon Boutte | Receptions | over | 0.0913518404432818 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|3f2f4cff-6fe0-43cb-8d2f-b4911865eb3e | underdog | Griffin Wilde | Receiving Yards | under | 0.0912305106518043 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|0fe90cac-61e9-4aa3-985b-7e83273c9af2 | underdog | Kendrick Raphael | Rush Yards | under | 0.091161347796472 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|c662b147-2a50-4c88-9c7b-ef28c09fba3d | underdog | Daniel Bellinger | Receiving Yards | under | 0.09110150359713487 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| prizepicks|16128101 | prizepicks | Ted Hurst III | Rec Targets | under | 0.09091390080650863 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|eecad4a0-88fe-4ebe-a8b2-0e0bfc8b0040 | underdog | Trinidad Chambliss | Pass Yards | under | 0.09087927496577841 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|3ecdcb49-c03e-4d63-a80e-749bfc200637 | underdog | Cam Cook | Receiving Yards | over | 0.09080804337147019 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|141f9ac0-a009-45ca-8701-040c3796a163 | underdog | Jordan Marshall | Rush Yards | under | 0.09066009388908292 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| prizepicks|16105111 | prizepicks | John Mateer | Pass Attempts | under | 0.09061174207972733 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|0e8858a7-5fb6-4ffd-a010-eddbbedf1bf6 | underdog | Alvin Kamara | Receptions | under | 0.0905814183401232 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|16046141 | prizepicks | Jared Goff | Pass TDs | under | 0.0902817486338214 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|764891d0-bf62-40ed-9e7a-027d82b9c59d | underdog | Diana Shnaider | Double Faults | over | 0.09021312334667442 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00Z |
| underdog|f10e571c-0024-481c-b4a0-9ab2de9ad060 | underdog | Darnell Washington | Receiving Yards | under | 0.090128614048436 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| prizepicks|16051316 | prizepicks | Carnell Tate | Rec Targets | under | 0.0899755364779774 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c66310f1-acdb-4b8e-b831-e1fd74214356 | underdog | Derek Meadows | Receiving Yards | over | 0.08988408824359218 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|245d329e-170d-471b-b37b-153a8bee8e51 | underdog | Jalen Coker | Receptions | under | 0.089640605964081 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|791fc351-e3f2-4e01-ac2e-95d1dc1a3341 | underdog | Daniel Jones | Rush Yards | under | 0.0893167984596011 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128090 | prizepicks | Jauan Jennings | Rec Targets | under | 0.08921349851248828 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|1fbeffd8-2b16-4502-9902-003accf8e7b6 | underdog | Sire Gaines | Rush Yards | under | 0.08901274296719075 | 2026-10-24T04:39:26Z | 2026-10-24T22:00:00Z |
| underdog|0d3d5682-5da9-440e-b1f4-787f722538c4 | underdog | Scott Starzyk | XP Made | over | 0.0889396502448031 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|ed418ef5-26ee-47e3-94ee-512386f680b3 | underdog | Junior Caminero | Total Bases | over | 0.08891435362023592 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|116be46b-f1d4-4310-8f46-e94563e753fb | underdog | Elijah Higgins | Receptions | under | 0.0886534112656307 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|5d1285be-3124-43f6-9931-914d5d6ecd90 | underdog | Dane Pizzaro | FG Made | under | 0.0885618352728215 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|cf64c5a7-a46c-4618-92ce-b662047529d7 | underdog | Devon Dampier | Rush Yards | under | 0.0883622175863563 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|b010c44c-10f7-453e-a045-7af6bf464967 | underdog | Tommy Tremble | Receptions | under | 0.0881185917029142 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|e6f3f01d-b7a6-44c0-8ec5-c7d8e88e40d1 | underdog | Holden Geriner | Pass Yards | under | 0.08800981633805016 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|2dbdfcd4-5c7d-4885-828f-cc3c48685cd3 | underdog | Isaiah Marshall | Pass Yards | under | 0.08787586430588823 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|9113a280-1a8d-4edc-b368-bac99ea17df4 | underdog | Michael Mayer | Receiving Yards | under | 0.0875972794063874 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|29f1e71c-cb3b-46dd-8df1-58b170be762c | underdog | Brice Turang | Hits | over | 0.08729806704789533 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|aa364d75-7110-45f8-88fd-66b6796445f3 | underdog | Cooper Pratt | Batter Walks | over | 0.08663967611336035 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|ee2b54a7-c70e-4525-aab3-157e73594ba0 | underdog | Jared Curtis | Pass Yards | under | 0.08643092013497977 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|8022d176-f92f-45ef-b9a8-b960f6f2cddd | underdog | Jacoby Brissett | Rush Yards | over | 0.086207431678947 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|d668b9cb-ed40-40cb-97a4-70f72c7280c3 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.08618995664773565 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|08b907c1-c47c-4a9f-8cf9-b043a2a100b3 | underdog | Cooper Kupp | Receiving Yards | under | 0.086095710674828 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|73b1aafd-baaa-4ff9-97b8-72eee79cadd9 | underdog | Tre Tucker | Receptions | under | 0.0860413061365301 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a8260b4c-a079-4809-a57f-8616228e7d15 | underdog | Bijan Robinson | Rush Yards | under | 0.08591905310287928 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16127002 | prizepicks | Alexander Schwolow | Goalie Fantasy Score | under | 0.08572186407884297 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00.000-04:00 |
| underdog|8edb7c30-2740-404d-ad73-c3d13d0c8b8f | underdog | Joe Jackson | Rush Yards | under | 0.08553009208987394 | 2026-10-24T04:39:26Z | 2026-10-24T19:45:00Z |
| underdog|4f72ec2a-f9f5-48ef-8988-fe968e84550c | underdog | Jordon Davison | Rush Yards | under | 0.08546579725724113 | 2026-10-24T04:39:26Z | 2026-10-24T19:00:00Z |
| underdog|2d66c2c2-8b03-45a0-a98b-5cfdc6585f75 | underdog | Darnell Washington | Receptions | under | 0.0851684391460022 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|a266e0dc-7d85-43e7-aeb0-f638f40a65fc | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.0851390837773276 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|8f3a2cfe-c9df-4006-a6a6-63a41183a051 | underdog | Tyler Allgeier | Rush Yards | under | 0.0846927854836112 | 2026-10-21T23:24:30Z | 2026-10-25T20:05:00Z |
| underdog|84d99d91-e7f4-4a28-9faf-3da2729847a0 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.0846102335479987 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|be4cbc1a-8a5d-4c12-8410-2bc6c9858974 | underdog | Sheldon Rankins | Sacks | under | 0.0843381307351941 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|18f6b0cb-e0d6-408b-b62d-da4f38218856 | underdog | Byron Murphy | Sacks | over | 0.0842998247988685 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| prizepicks|16126868 | prizepicks | Bernd Leno | Goalie Saves | under | 0.08419697162602124 | 2026-10-24T04:39:26Z | 2026-10-24T10:00:00.000-04:00 |
| underdog|f2cbfacd-a66e-475b-a780-f8b44c49ac47 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.08417121275104655 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|8504f84a-f3bc-4ed4-bcba-65a6766736b8 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.08403885437854836 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|c1ee2115-8353-4c59-9527-09c97124e1c0 | underdog | Cooper Pratt | Runs | over | 0.08362391033623906 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|fa0f28ce-b297-4b31-abea-d5617a1dd43f | underdog | Brock Wright | Receiving Yards | over | 0.08352861013723534 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|56f293ed-4635-4cc3-833c-4ed9a375750c | underdog | Tee Higgins | Receiving Yards | under | 0.0834112064258462 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2816aaad-c9d9-4cd5-ad6d-58de25217f97 | underdog | Michael Mayer | Receptions | under | 0.0834003397411226 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|50636f28-b556-4195-9780-5aff7702ef87 | underdog | Malik Willis | Rush Yards | under | 0.0832931322442289 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ccd3866e-e39d-4402-bb01-bbd92ca68ab9 | underdog | Spencer Shrader | Kicking Points | over | 0.08317987244058994 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ba6a7b98-429b-495e-8b9a-c3c97d70ff2e | underdog | Tyjae Spears | Rush + Rec Yards | over | 0.08298512096055805 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|38a333f7-f8a2-48ee-9d23-e5502a83021b | underdog | Richie Palacios | Batter Walks | over | 0.0828536184210526 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|4607fb29-45d1-43d5-be4c-c1e72fd87a37 | underdog | Junior Caminero | Batter Walks | over | 0.08280432119389691 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|7a40e228-09fa-4a93-b377-fd180106ab0e | underdog | Jonathan Aranda | Batter Walks | over | 0.08280432119389691 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|0c8acb0c-794e-4cd7-846e-be6600ed7ea8 | underdog | Josh Downs | Receptions | under | 0.0826092082715991 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|eccb476e-a91b-42b6-a4db-5ec7da7769cb | underdog | T.J. Moore | Receiving Yards | under | 0.0825764110815296 | 2026-10-21T23:24:30Z | 2026-10-24T23:00:00Z |
| underdog|1b806f20-be44-49e6-8f59-766270beb2b9 | underdog | Jason Myers | Kicking Points | under | 0.0825404894860757 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|ee420202-642a-4ac6-988b-e2cce1adb4b5 | underdog | Isaiah Likely | Receptions | under | 0.0825217515739429 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9b0e46ce-89e4-409d-be84-b67b36c68cc9 | underdog | George Holani | Rush Yards | under | 0.08245430904977002 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|cdbf5446-2666-4953-8fed-2a23abfb628d | underdog | Kenneth Walker III | Rush Yards | under | 0.0822691396401671 | 2026-10-21T23:24:30Z | 2026-10-26T00:20:00Z |
| underdog|3b0eb78b-d28f-46ab-8459-886657d5c203 | underdog | Isaac TeSlaa | Receptions | under | 0.0822432608821583 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3fdf958b-4aeb-446f-a872-8228a3fb7690 | underdog | Kendrick Bourne | Receiving Yards | under | 0.0821950618308543 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|5d84cbcd-6ff5-4c25-a255-d25907b4e2e5 | underdog | Jeffery Simmons | Sacks | under | 0.0821199883686009 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|d49be5da-f918-4376-a50c-307e74b8ac0d | underdog | Jonathan Aranda | Total Bases | over | 0.08185887420294757 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|6f5cec65-d493-4688-8a7f-0b44500d7e50 | underdog | Wayne Knight | Receiving Yards | over | 0.08181809612117052 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|98c8557b-1ef7-4740-bad9-9c76cec26da1 | underdog | Dohnte Meyers | Receiving Yards | over | 0.08147385061303802 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|80a3a39d-256d-4c93-be99-964f1c31f0e6 | underdog | Laiatu Latu | Sacks | under | 0.08144052723887041 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|ddab0bd3-7a9d-4f8f-b818-b843cc34659c | underdog | Aidan Laughery | Rush Yards | under | 0.08142683550601237 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|367dcf00-d37f-4616-942d-c295ece3fe5d | underdog | Taylor Walls | Hits | over | 0.0812120235236925 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16051290 | prizepicks | Jordan Addison | Rec Targets | under | 0.0810609688919091 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|cfa707d3-c8b9-477e-80c2-22c924cedaa6 | underdog | Daniel Carlson | Kicking Points | under | 0.0807323556687517 | 2026-10-22T04:39:42Z | 2026-10-25T13:30:00Z |
| underdog|41308d6a-1585-4bd8-88a3-c4fc5587e979 | underdog | Jason Sanders | FG Made | under | 0.0803782078621125 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e8e876b4-93d8-47de-aa26-04066201a1df | underdog | Katerina Siniakova | Double Faults | under | 0.08034899297969111 | 2026-10-24T04:39:26Z | 2026-10-24T06:00:00Z |
| underdog|e7b42cef-9825-40e6-860f-1e9a984e2a86 | underdog | CJ Donaldson | Rush + Rec Yards | over | 0.08021649795639368 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|1a8369b7-a587-4c4c-9f1c-af6bcfaf1f9c | underdog | Jackson Harris | Receptions | under | 0.08011995458845445 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|fa91546b-2faf-49cd-aa41-3929b7a7a669 | underdog | Chase McLaughlin | FG Made | under | 0.0799826010276563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128088 | prizepicks | Noah Gray | Rec Targets | under | 0.07986503444913706 | 2026-10-24T04:39:26Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|a864eb6c-fd01-498b-9630-51e183420e59 | underdog | Mikey Keene | Pass Yards | under | 0.07983876992350825 | 2026-10-24T04:39:26Z | 2026-10-24T19:45:00Z |
| underdog|0f1c9398-e57f-4a9f-bd43-882f1b5918e3 | underdog | Aidan Chiles | Rush Yards | under | 0.07971052999243466 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|5f3f904b-9605-420a-b9ad-e2b3ba77d57f | underdog | Colton Joseph | Total TDs | under | 0.07943142685462201 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|95ad8fe3-e38f-47b9-af72-6411261e19b6 | underdog | Quinshon Judkins | Receiving Yards | under | 0.07918115619319599 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|2327ca23-32ef-45ec-bc5b-ab13808e5f29 | underdog | Chandler Simpson | Runs | over | 0.0790784557907846 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|9fc78236-fb8a-4ffb-b787-54565b5b2745 | underdog | Andrew Marsh | Receptions | under | 0.07905396062975067 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|e091a42a-e0f8-44c0-8b29-4d4f96450333 | underdog | Jaylen Raynor | Pass Yards | under | 0.0788511546485264 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|d2e7f9b8-cd09-468a-a0fd-8c4b439ba633 | underdog | DeSean Bishop | Rush Yards | under | 0.07867452410259013 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|357d1c55-39ca-4e80-8e47-b9b3fb1d91e6 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0783802647011688 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d995a6ad-be9c-47ca-b76f-f39a56c78509 | underdog | Dylan Riley | Rush Yards | under | 0.07833360606522233 | 2026-10-24T04:39:26Z | 2026-10-24T22:00:00Z |
| underdog|fa1b7315-d8c5-468f-b057-1c96d70246da | underdog | Rodney Bullard | Receptions | over | 0.07805976093610967 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|24830e9f-bd50-407c-af23-065e3166b529 | underdog | TK Norman | Receptions | over | 0.0780188542071848 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|0d25c245-efca-4a13-baed-2eda4672ccf9 | underdog | Mike Gesicki | Receptions | under | 0.0779878372316424 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|cd41b2b9-c7a0-45df-bcc2-de420b13148a | underdog | Bucky Irving | Rush + Rec Yards | under | 0.07790152531371486 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ba66bea3-cfcc-40be-ad8c-fd53ecf64444 | underdog | Alvin Kamara | Rush Yards | under | 0.0777359816039499 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|58f02596-5585-4b0f-8b9b-da5378b9bde2 | underdog | Jonny DeLuca | Total Bases | over | 0.0774897213339425 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|6f06d48f-cce9-442a-8a93-5cd9c028fdb1 | underdog | Ollie Gordon | Receiving Yards | under | 0.07744253798791922 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|3984b74a-9d53-4369-9f72-6b21f9e2caa3 | underdog | Chandler Simpson | Hits + Runs + RBIs | over | 0.07725079118704203 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|99192d3b-e302-42f3-b7ab-2ff5db8b8a4e | underdog | Drake Lindsey | Pass Yards | under | 0.0772448058323824 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|ba245851-18e0-4e22-a6af-94dacecb7c22 | underdog | Nate McCashland | FG Made | over | 0.07717406962284173 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|9d0c75f1-aa2f-40d2-82f5-04107dec65e0 | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.07703946662894823 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|df9b05ca-60c3-446f-80a1-7ae08e7bf21d | underdog | Ed Small | Receptions | under | 0.07696174337933481 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|ff935cb5-cc24-41a6-9a69-b8839cf2a021 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.07694741593561627 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|9a23291c-d740-46d9-b862-79e3ebb3d2a5 | underdog | Derrick Henry | Receptions | over | 0.0769349421556845 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16090040 | prizepicks | Caleb Hawkins | Rush Atts | under | 0.07682306799504812 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00.000-04:00 |
| underdog|db83fe72-a11c-4c23-b946-1f780db7c1d9 | underdog | William Contreras | Batter Walks | over | 0.07675095099574858 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16051273 | prizepicks | Travis Kelce | Rec Targets | under | 0.0766485815662542 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|63e1975c-17e2-4f9c-bfaf-a709d8598e32 | underdog | Jaron-Keawe Sagapolutele | Pass TDs | over | 0.07631036348985182 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|23cc4a0a-23c5-4e37-98c2-b2ff5ed850aa | underdog | Trey Smack | FG Made | under | 0.0758399666432347 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5df27532-04eb-405c-b458-1cfd5b5b6c3a | underdog | Malik Nabers | Receptions | under | 0.0758087558960143 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|d266a85d-a66d-406b-bea5-4b7215c34d91 | underdog | Devaughn Vele | Receptions | under | 0.0757194055785056 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a09f7e47-aacb-4e78-a9f7-4728f5d1a430 | underdog | Wayshawn Parker | Rush Yards | under | 0.07570999371449916 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|ae60f3a8-a9ed-4acf-b13f-fdc17f7013f9 | underdog | Michael Penix | Pass TDs | under | 0.0756786003884431 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d49f6c62-edd5-4fe3-9832-a4d3f48f15ec | underdog | Brendan Baird | FG Made | under | 0.0756708302222249 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|1aa1c480-7758-462e-b1d2-d70194b54ba5 | underdog | Javarius Green | Receiving Yards | under | 0.07565987448132783 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|fb29e728-75f8-4029-8ea6-a2bb1473cd2b | underdog | Calais Campbell | Sacks | over | 0.07536283014091988 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8b8afb9a-0acf-4f99-8e56-c50b27995812 | underdog | DeForest Buckner | Sacks | over | 0.07524235100416299 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|a07fa21c-3979-456f-8f95-b6b62fe08663 | underdog | Kewan Lacy | Rush Yards | under | 0.07513621058774489 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|b7633e2a-8c11-4ada-8bd1-ddacccbf8dcb | underdog | Kenneth Walker III | Receptions | under | 0.0750174077225467 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|fa6b3d2e-4ca3-4536-8709-91606f82acdb | underdog | Jared Goff | Pass TDs | under | 0.0748246656634097 | 2026-10-22T04:39:42Z | 2026-10-25T20:25:00Z |
| underdog|b6f27736-e16b-471b-9d5a-c157d9c328fe | underdog | Wayne Knight | Rush Yards | under | 0.07480614054787882 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|5792edce-8992-4b47-97f2-2d4270689270 | underdog | Mason McKenzie | Pass Yards | under | 0.07473275268936663 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|dfbe2fbb-ed28-4fbb-8781-5bcac4758534 | underdog | Drew Sample | Receptions | under | 0.0745894946131864 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f840b552-3515-4584-9d35-d37fca257b1f | underdog | Chris Olave | Receiving Yards | under | 0.0744110380898498 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|d9a8338f-0c9f-47bf-95ed-3d25faaff51a | underdog | Jordan Whittington | Receptions | under | 0.07435492868539906 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|186e0ace-b3a3-4d78-83c7-1cf9b0fc8393 | underdog | Jahan Dotson | Receiving Yards | under | 0.0741904379865594 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051313 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.0741620403956118 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|a2dc5cfd-b6bc-4a55-9299-70d422b77b64 | underdog | Braden Pegan | Receiving Yards | under | 0.07412133280161459 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|0885b289-f09c-45ec-a38b-3b2dd7e57fb6 | underdog | Omar Cooper | Receiving Yards | under | 0.07399316521856691 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|6e3fda55-f2c5-4f09-a998-321e0db137a3 | underdog | Jonathan Aranda | Hits | over | 0.07396255458288514 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|08e81224-aba3-4108-a4c0-79506aeaf8be | underdog | Yannick Smith | Receiving Yards | under | 0.0738589437731918 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|0b37fb47-ebdc-4010-bcf5-622c00a374ac | underdog | Devon Dampier | Pass TDs | over | 0.0738331610963063 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|6aa8f84a-2ea9-4946-a243-4ba0a07c3993 | underdog | Ollie Gordon | Rush Yards | under | 0.0737138149062139 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e2e5065-8c00-4fbf-8932-920f5872117c | underdog | Isaac Wilson | Pass Yards | under | 0.07370820859155769 | 2026-10-23T13:31:04Z | 2026-10-24T23:00:00Z |
| underdog|9b71e840-f021-48d2-b4ac-fd72448fc9fe | underdog | Kevin Jennings | Pass Yards | under | 0.07359565684435676 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|455a71ba-1e78-4b27-8f94-d0afeba7b6fa | underdog | Kyren Williams | Receptions | under | 0.07341233571119932 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|27fb02f5-b3f7-4c9b-bf6f-2e51e4336088 | underdog | Austin Hooper | Receptions | over | 0.07334873265912745 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|1e6dcf52-47f9-487f-ae1e-f4976a392121 | underdog | Legend Glasker | Receptions | under | 0.0731708661649952 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|a7129366-fc43-494f-b6f1-380aae0353b9 | underdog | Jamarion Morrow | Rush Yards | over | 0.07310888064473242 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|6664dbee-84f6-4192-97a8-e1086c85f73b | underdog | Chase McLaughlin | Kicking Points | under | 0.0730635220054324 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|af786d49-ffc7-4b58-ad9d-a4a908de944c | underdog | Mario Craver | Receptions | over | 0.07278725325217272 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|ab4700cd-4ca2-4863-ac85-6301c804c057 | underdog | Mike Matthews | Receptions | under | 0.0726184227012455 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|25cd8759-8e2c-4914-8307-9dd5249af06b | underdog | Drew Wagner | Receiving Yards | under | 0.07256598868461706 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|4454d8f6-93b5-4c97-b913-449717cee8bc | underdog | Cam Skattebo | Receptions | under | 0.07246523258444959 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|e26442d1-e193-41a1-b88c-71f0f33d3168 | underdog | Evan McPherson | FG Made | under | 0.0722696105068416 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3a57a428-3d1c-4885-a1f8-5ee034f590aa | underdog | Javarius Green | Receptions | under | 0.072102008775498 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|f9b46522-0095-4985-96b6-1b7bd742682a | underdog | David Hamilton | Hits | over | 0.0720133292783155 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|868860bf-3b71-4eda-bd16-674bf3d41aef | underdog | Bear Bachmeier | Pass Yards | under | 0.07193390480468587 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| prizepicks|16047018 | prizepicks | Darnell Washington | Recs | under | 0.07187451637324271 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|670a33c3-effe-4429-ab06-316666438384 | underdog | Tallon Griekspoor | Aces | under | 0.07183294194825629 | 2026-10-24T04:39:26Z | 2026-10-24T14:00:00Z |
| underdog|65ee16bb-4962-497e-8c6a-1f6f205525ed | underdog | Kenny Darby | Receiving Yards | under | 0.07161832716991334 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| prizepicks|16127000 | prizepicks | Alexander Schwolow | Goalie Saves | under | 0.07153146945034716 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00.000-04:00 |
| underdog|a4ff4488-c410-4fb1-93bd-6846607552af | underdog | Jordan Love | Rush Yards | under | 0.071463102847337 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|7463844b-ea5b-4399-a5c1-816439dbc614 | underdog | Lloyd Avant | Rush Yards | under | 0.07143710623427568 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|feccbe68-8da4-4967-b819-a242590ff2bf | underdog | Liam Hicks | Runs | over | 0.07129629629629636 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|78ad2055-2f47-42e4-8a8b-1662a8a49ad7 | underdog | Ty Dieffenbach | Pass TDs | under | 0.0711863086593506 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| prizepicks|16051261 | prizepicks | Sam LaPorta | Rec Targets | under | 0.0711809713072434 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|99755d9f-1fcb-4c11-b802-6d9aa0b6d23c | underdog | Elija Lofton | Receptions | under | 0.0711106431709001 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|f35869de-fda0-4ff6-8837-90860751c2b9 | underdog | Will Reichard | FG Made | under | 0.071055087750351 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|052ab564-9a0a-4629-83a6-8bb879b4a0d6 | underdog | Kyle Pitts | Receptions | under | 0.0710490294424133 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|505cea21-7e6d-4f0c-a89b-2ea84e5055b9 | underdog | Josh Hoover | Pass TDs | over | 0.0710140089136008 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|24506b09-6b5e-40f9-a6d2-0ac4b6560420 | underdog | Taylor Walls | Batter Walks | over | 0.07088285229202046 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|6836add1-e50e-4ec1-86cc-eac77a9f1a17 | underdog | Kyren Williams | Receiving Yards | under | 0.07083989094132515 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|a7a9833f-1d23-42f2-911c-e6c6a9c0208e | underdog | Yulia Putintseva | Double Faults | over | 0.07076969148263285 | 2026-10-24T04:39:26Z | 2026-10-24T07:40:00Z |
| underdog|00946ae8-e51a-4625-8b97-ccea92a33ea1 | underdog | Chris Boswell | Kicking Points | under | 0.0706516180970466 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|2ded917a-7a76-4d1d-b255-35ed92207746 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0705952618185794 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6eb4ceca-ab6e-4b70-b779-c61fd77dcb3a | underdog | Emmett Johnson | Receiving Yards | over | 0.0704807198097645 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|b346f90c-1bcb-4cae-9a05-cf0428891334 | underdog | Keyone Jenkins | Pass Yards | under | 0.07027374103054362 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|3b0d8900-c970-4417-bc6a-2f5501367c92 | underdog | Malik Knight | Receptions | over | 0.07019802165511752 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|24312ff1-78a8-4546-a295-0dc2eb910b54 | underdog | Aaron Rodgers | Rush Yards | over | 0.0700844647787815 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|00aa1266-017b-4d1d-9745-2d4a2b1e4a7d | underdog | LaNorris Sellers | Pass TDs | over | 0.0699838081654409 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|b6b740f6-7ef3-4ea2-9a60-5b7d3258064d | underdog | Maxx Crosby | Sacks | over | 0.06992804715941348 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051306 | prizepicks | Jaylen Warren | Rec Targets | under | 0.0699206862123872 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|235e5aee-0050-4033-9a5d-05c1ca67b023 | underdog | Traylon Ray | Receptions | over | 0.06979772880995211 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| prizepicks|16128084 | prizepicks | Josh Downs | Rec Targets | under | 0.06975179944315124 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|da10b783-7335-4f3c-a096-e3c3df060a0c | underdog | Jayden Savoury | Receiving Yards | over | 0.06963560598257534 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| prizepicks|16051239 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.0694964909576487 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|9f8ce159-b80d-401d-bf13-9146b2ff57c0 | underdog | Quinshon Judkins | Receptions | under | 0.06949508244536684 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|13ba1be0-8bc1-4e43-ac89-5784da0c5cc8 | underdog | Noah Fifita | Rush Yards | over | 0.0694841615622458 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| prizepicks|15944963 | prizepicks | Jared Goff | Rush Yards | over | 0.0694248099013491 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|b977e7ae-9c34-47cb-be90-ee68ad34fdd9 | underdog | Cameron Heyward | Sacks | over | 0.06931539209198773 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| prizepicks|16051253 | prizepicks | Evan Engram | Rec Targets | under | 0.0692857795326448 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3bf0ae23-cfa7-4794-94a6-195093503861 | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.0691532959067324 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|232e7efd-c6d4-496f-94af-0fabfc853c94 | underdog | King Miller | Rush Yards | under | 0.0691076136614035 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|abe1f5d9-3690-4b8a-991e-436bd87b5318 | underdog | Evan Engram | Receiving Yards | under | 0.0687422940230393 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a402b43a-79ba-45b6-97ea-29901106333c | underdog | Jared Curtis | Pass TDs | over | 0.0687053103943738 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|335a1947-39f1-4a26-890f-827cfc2f3188 | underdog | Darian Mensah | Pass TDs | over | 0.0686136038680533 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|9ac882dd-d4dd-463d-acfb-721f768788e6 | underdog | Jaylen Raynor | Rush Yards | over | 0.06844628305270906 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|242e0dff-aa0e-41a2-96d2-5f5e9771ad20 | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.06844597515098405 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|6d20371c-7b8f-482f-a586-86f39d4ca35f | underdog | Gianni Spetic | XP Made | over | 0.06841584523129846 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|16f1cec5-3eb6-403b-b4be-ef4d06e7d3ad | underdog | TK Norman | Receiving Yards | over | 0.0681009371654977 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|7c47c6fe-f661-433c-b0b9-692864079609 | underdog | Richie Palacios | Hits | over | 0.06807826491487101 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|3eb3094e-9987-486a-9ed9-5bdc8cf799d9 | underdog | Zachariah Branch | Receptions | under | 0.06806583715894199 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|958d9f17-3be8-4fa0-82d3-ec2cd53ad8eb | underdog | Dylan Riley | Receiving Yards | over | 0.0680146425936009 | 2026-10-24T04:39:26Z | 2026-10-24T22:00:00Z |
| underdog|18cad147-501e-4ac2-8cbb-4bb608ee508a | underdog | William Contreras | Total Bases | over | 0.06795852669425984 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16127003 | prizepicks | Karl Hein | Goalie Fantasy Score | under | 0.06776160795903552 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00.000-04:00 |
| underdog|8c27351f-66ce-41b9-a394-381a9f0629d6 | underdog | Tylik Hill | Rush Yards | over | 0.06758943680677953 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|e3b4cb15-bd32-41fe-997b-31ef2b3d248e | underdog | Jonathan Taylor | Receptions | under | 0.0674513078149925 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea2dc53f-bd18-4fa7-875b-0d4d97360754 | underdog | Laquon Treadwell | Receiving Yards | under | 0.0671153960295503 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|6ea455bd-70ea-466d-acca-bfb1488fe8a5 | underdog | CJ Baxter | Rush Yards | under | 0.06696814176614518 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|bb4be0ab-ce90-442b-865c-47a4d263721c | underdog | Ayden Greene | Receiving Yards | over | 0.06690110040706054 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|3ba86dc2-f3d3-469a-be66-2b68cf969274 | underdog | Will Stone | FG Made | under | 0.0667977883764894 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|2dfd0e01-c783-4d1a-b3e0-5567d256fa60 | underdog | Gavin Freeman | Receiving Yards | under | 0.06674379288327614 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|fde52e23-fb79-47cb-92c3-84f812a63c58 | underdog | Logan Henderson | Strikeouts | over | 0.06671194249025736 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|5927237f-7942-4a3a-9097-d6f98547da17 | underdog | Noah Fifita | Pass TDs | under | 0.06667176335674008 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|91a94394-9962-45be-9dde-275e8ac9349f | underdog | Garrett Mitchell | Total Bases | over | 0.0664525899542866 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|f45b86d3-dbf7-4286-ab3e-dbf13b253ea0 | underdog | Lotzeir Brooks | Receiving Yards | under | 0.0664108283053951 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|70c8977a-374c-48e5-ba23-edc0fdcc3f39 | underdog | Bijan Robinson | Receiving Yards | under | 0.0663650266525974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|37667dc4-1793-418b-ac9d-f356f0b2c811 | underdog | Conner Weigman | Pass Yards | under | 0.06631198946823724 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|06a009bf-c546-4461-b1c4-1bde1ff75c14 | underdog | Blake Corum | Rush Yards | under | 0.0662621531811924 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a5bb8c4d-068d-4993-a457-9bf1d8b88fae | underdog | Scottre Humphrey | Rush Yards | under | 0.06602060692085798 | 2026-10-24T04:39:26Z | 2026-10-25T02:00:00Z |
| underdog|2a9dcee0-e5bf-40bf-a5cc-c145bc35b2b4 | underdog | Conor Talty | XP Made | under | 0.0658903549899069 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1f7419ba-44ed-4d10-8a7a-bc913e247a3b | underdog | Blake Corum | Receptions | over | 0.0657799728513109 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|352ced7e-8dac-418b-9c42-3093c7bff249 | underdog | Dalton Schultz | Receiving Yards | under | 0.0657798179755999 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|523e63f2-cd93-4051-9a92-051064daa5f9 | underdog | Nnamdi Madubuike | Sacks | under | 0.06576300797424106 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|bc5e98e3-a5ce-45a5-90f0-bbacbef40b3c | underdog | Tetairoa McMillan | Receptions | under | 0.0657606101669747 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dce9d985-12ad-457d-9c09-f482fdf45223 | underdog | Katie Boulter | Double Faults | under | 0.0657339010798681 | 2026-10-24T04:39:26Z | 2026-10-24T06:00:00Z |
| underdog|b82e159e-e027-45ea-ac51-7abc18e0919c | underdog | Ricky Johnson | Receptions | over | 0.06565632341199579 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|df559804-fa70-4170-9188-6091d2237843 | underdog | Cooper Barkate | Receptions | under | 0.06522046146098859 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|ece67c7e-490c-43d5-a1c5-276d6b344e83 | underdog | Rasean Jones | Receiving Yards | under | 0.06518403377583948 | 2026-10-24T04:39:26Z | 2026-10-24T22:00:00Z |
| underdog|db98665d-3d8e-4a28-a47b-c750a5028537 | underdog | Reece Vander Zee | Receptions | over | 0.06516393509099372 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|6331b0a6-8a34-42e8-8ca6-a2841c9baf66 | underdog | Liam Hicks | Hits | over | 0.06495244879794393 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|15945074 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.064833820071657 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|85bf20f3-7302-42b7-be69-5868b1aa3234 | underdog | Marcel Reed | Pass Yards | under | 0.06481870881744578 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|462e7a7f-6c55-4274-bf41-255ae3fc87dd | underdog | Chandler Simpson | RBIs | under | 0.06467661691542292 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|9df8e03e-f50e-4a07-ae41-0561472e4131 | underdog | Sean Tucker | Receptions | under | 0.06463248954578349 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8b94ec15-ffc9-46ff-857d-c62b003c5636 | underdog | Chandler Simpson | Total Bases | over | 0.06460839457513923 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|15944962 | prizepicks | Jordan Love | Rush Yards | under | 0.0645818534291142 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|2ecfb6b7-ca61-40d5-86df-244f82324a85 | underdog | Gianni Spetic | FG Made | over | 0.06447492432951912 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|dfe4d123-f091-4961-96b8-782a23a73d5a | underdog | William Contreras | Hits | over | 0.06444577168823462 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|69c654d5-7f0d-40ba-b4de-0146a790613e | underdog | Jordan Addison | Receptions | under | 0.0643744310105808 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|65d5841d-46ec-482d-ae00-03b1bb8559b2 | underdog | Calvin Ridley | Receptions | under | 0.06434385244888874 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|80949b99-08c9-47f9-8565-09b998f305cc | underdog | Aaron Jones | Receptions | under | 0.06431549031041361 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c749d904-8c14-4779-9228-9447ef105e11 | underdog | DJ Black | Receiving Yards | over | 0.06418475376728217 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| prizepicks|16127535 | prizepicks | Felix Nmecha | Shots | under | 0.06376684481379624 | 2026-10-24T04:39:26Z | 2026-10-24T12:30:00.000-04:00 |
| underdog|c28ead5c-8a19-420f-a474-89ef551e6c5b | underdog | Jonah Coleman | Rush Yards | under | 0.06364468438664261 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| prizepicks|16111971 | prizepicks | Darian Mensah | Pass Comp | under | 0.06361233653778786 | 2026-10-23T13:31:04Z | 2026-10-24T12:00:00.000-04:00 |
| underdog|1e5f94a5-c830-43f0-b9d7-0f240d56e448 | underdog | Trey Hendrickson | Sacks | over | 0.06350775359625249 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|60ae0df3-7461-471b-828f-ab419baae16f | underdog | Christian Yelich | Hits | over | 0.06347750701334554 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|b0238849-8d87-4a82-a650-a28c767755bd | underdog | Josh Hoover | Pass Yards | under | 0.06336259991071791 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|a3da5e5c-a888-405e-9dfa-c36687761062 | underdog | Drew Sample | Receiving Yards | over | 0.0629102314852918 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|f4f3d547-82ce-4e48-885a-a27db6f035ae | underdog | Dayana Yastremska | Double Faults | over | 0.06284075225492569 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00Z |
| underdog|d76069d3-8d26-4e71-a6a7-06b5b5f062d2 | underdog | Samaje Perine | Receiving Yards | over | 0.06271037602491508 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|3b625a33-dfe7-4c56-a081-2453c34284ce | underdog | Tate Sandell | XP Made | under | 0.062585771684329 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|cd894ebb-1464-4062-9e9d-d7034e80fd27 | underdog | Tommy Tremble | Receiving Yards | under | 0.0625505359363844 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|79e5199a-505e-4bcb-9f7b-4eb6dede73d8 | underdog | Mo Alie-Cox | Receiving Yards | over | 0.06231155663033794 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|d3e19a26-fc29-4173-97dd-daae9b0362b4 | underdog | Jake Bauers | Hits | over | 0.06219934850411013 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|04d5c5e5-e62e-43e4-b7ad-f05b27c1e49f | underdog | Aaron Rodgers | Pass TDs | under | 0.0620273967369939 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|bad7ccd3-6884-4391-aab3-98594caab197 | underdog | Chris Bell | Receiving Yards | under | 0.061951957479485 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|80589a9a-28cf-4b78-a688-2afde0a4a48f | underdog | Rodney Fields | Rush Yards | under | 0.06192091250277043 | 2026-10-24T04:39:26Z | 2026-10-24T19:45:00Z |
| prizepicks|16051228 | prizepicks | Kendrick Bourne | Rec Targets | under | 0.0616943000896329 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|365c7fa6-dcc5-4b1b-b9af-c0c3cdca5d6b | underdog | Puka Nacua | Receptions | under | 0.0616090079415561 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|9ff8ad4e-4c75-4cfd-badd-45cf27902270 | underdog | Chris Bell | Receptions | under | 0.0614599626838349 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|300681f0-5f41-440c-bc6a-141fa5fe86ef | underdog | Tyjae Spears | Receiving Yards | under | 0.061401526255426386 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|ad0ef3f7-fe1a-4267-99ab-4c3bf8bc4f9d | underdog | Cam Coleman | Receiving Yards | under | 0.0612304355005692 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|cdfeacfa-64e9-4079-a1ba-4d56131b2ab0 | underdog | Drew Rasmussen | Strikeouts | under | 0.061065414297040044 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|82932e52-6bd2-40d8-8f4e-8c0311ba997f | underdog | Sam Leavitt | Pass TDs | under | 0.0609996532059247 | 2026-10-22T04:39:42Z | 2026-10-24T16:00:00Z |
| underdog|4ce150dd-f14f-48e3-af25-4b882f188bc3 | underdog | Malik Knight | Receiving Yards | over | 0.06082737510352354 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|2b8f786a-ddf3-4c91-98e5-a939a1e123fe | underdog | Harold Fannin | Receptions | under | 0.0608103254568292 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|757d3abb-8848-4006-a50e-f2af3d90893f | underdog | Koby Young | Receiving Yards | over | 0.0607716190821504 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|9d50d307-5002-48ac-9bc0-5d542a19ea45 | underdog | Richie Palacios | Hits + Runs + RBIs | over | 0.06062352768016921 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|3c8721d1-a9d3-4553-a327-a86b397d702f | underdog | Jadeveon Clowney | Sacks | over | 0.0605759985732586 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|63ca294d-d976-4645-8c58-da78f48cb648 | underdog | Tommy Paul | Aces | under | 0.0604752206056981 | 2026-10-24T04:39:26Z | 2026-10-24T12:00:00Z |
| underdog|60491404-85e4-4da0-ba06-4d23eb4cbaf6 | underdog | Brock Purdy | Rush Yards | under | 0.0603702485832077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b6a1b9db-01d3-4138-9fab-4d50b72a4ef2 | underdog | Victor Mesa | Hits | over | 0.06016814981741647 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|15940804 | prizepicks | Devaughn Vele | Recs | under | 0.06015971284752153 | 2026-10-23T13:31:04Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|0d6f7a50-fa14-420e-bb35-6a8002c97c5a | underdog | Kendrick Bourne | Receptions | under | 0.0601364284559438 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|410fd1b1-2582-428f-bdae-1ad4c09f7927 | underdog | Hudson Clement | Receptions | under | 0.06012931151971457 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|f2c7e077-b430-4e2b-b8d2-b22a32ab1f15 | underdog | Kendre Miller | Receiving Yards | over | 0.0599966168566626 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|0b848e07-9ee9-4b51-bcf7-f9f29202ca1b | underdog | Will Reichard | Kicking Points | under | 0.05988293461374794 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|c2cfc127-7dcb-4e9c-b22d-bacb733553fe | underdog | Sione Vaki | Receptions | over | 0.0598689783880203 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|fec5e122-f59d-49aa-9430-e8b854af8e70 | underdog | Geno Smith | Rush Yards | under | 0.0596711983179013 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|95c1e474-6c5b-48b7-987a-a9b6b84d9ba3 | underdog | Aaron Jones | Receiving Yards | under | 0.05947359172960187 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| prizepicks|16123018 | prizepicks | Yulia Putintseva | Total Games | over | 0.059435233448213665 | 2026-10-24T04:39:26Z | 2026-10-24T03:40:00.000-04:00 |
| underdog|b4073c57-0eee-482e-9c8c-29a23326ac44 | underdog | Chuba Hubbard | Rush Yards | under | 0.0593658945119207 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|583e6b0d-22f5-481c-b34a-7f4a4b548be3 | underdog | Gavin Lahm | FG Made | under | 0.0593599272390517 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|5ce2fd6d-5432-48c0-8632-8621ec611c8c | underdog | KJ Edwards | Rush Yards | over | 0.05926510669749774 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|9a9ea7f4-3f25-475a-841c-9eaf75b89da4 | underdog | Yandy Díaz | Batter Walks | over | 0.059237824852587884 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|09b74476-b00c-4a2f-abc2-20d3e33100a6 | underdog | T.J. Hockenson | Receptions | under | 0.0587657925838965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3d70887e-e6dc-4f21-b877-ba6e2825f3f0 | underdog | Waden Charles | Receptions | under | 0.058761965328031796 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|71030697-8b7c-4727-9304-bd79a5ede904 | underdog | Zion Ragins | Receiving Yards | over | 0.05874322449346736 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|277a8aec-fac7-43c4-a344-09970c828c5d | underdog | Pierre Strong Jr. | Receptions | over | 0.05871475975977286 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|ad6ce3c3-20c9-4d64-9951-ea30302063b4 | underdog | Victor Mesa | Total Bases | over | 0.058631187281542374 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|3c27ced9-c782-4952-836e-43b81b480fcc | underdog | Tyler Higbee | Receptions | under | 0.0585445402433147 | 2026-10-21T23:24:30Z | 2026-10-25T20:25:00Z |
| underdog|f850eeaa-b79f-483b-90c4-6ffe630e9c5c | underdog | Dohnte Meyers | Receptions | under | 0.05807606094078033 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|3d0832bf-fd59-4d1f-838a-17608aa5af1e | underdog | Wyatt Young | Receiving Yards | under | 0.05791219576678508 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|ba195c04-721e-4a8f-a9d3-45d2c6c4a37a | underdog | Evan McPherson | Kicking Points | under | 0.05775934703395802 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|b359de29-0515-46be-8ab6-0d86fc6803fe | underdog | Ryan Fitzgerald | FG Made | under | 0.0575761782932597 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|49042e67-f88c-438c-9e92-03f6dbd2b21f | underdog | Caleb Komolafe | Rush Yards | under | 0.0573778751522929 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|5a2f85cf-5204-495e-a414-068f4e92cb53 | underdog | Mason McKenzie | Pass TDs | over | 0.05736766045657049 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|becc7bb1-72c0-4354-ae0e-6d0ff43df532 | underdog | Reed Harris | Receiving Yards | under | 0.05735319015511753 | 2026-10-24T04:39:26Z | 2026-10-24T19:45:00Z |
| underdog|6fa0097a-90c1-4755-b236-548718217bca | underdog | Chrishon McCray | Receptions | over | 0.0573275006552072 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|2b975295-68b0-404b-9811-4452287dd8d7 | underdog | Derrick Henry | Receiving Yards | over | 0.05729886958919905 | 2026-10-23T13:31:04Z | 2026-10-25T17:00:00Z |
| underdog|5b1209ba-20ce-4559-a6b5-422b5f506385 | underdog | Kenneth Walker III | Receiving Yards | under | 0.0570964245693671 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|487d9fcc-6679-4b44-a167-1b46a9226489 | underdog | Mike Washington | Rush Yards | under | 0.057058846958996434 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|788d321e-a413-42d1-9fe8-598725b5146c | underdog | Noah Fant | Receptions | under | 0.0569890350580739 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|9de90d0c-fc2e-4d4d-8991-42254596c301 | underdog | Darren Waller | Receiving Yards | under | 0.056903144274505 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|420a975f-c847-42e1-acb6-f2590c1aa0f5 | underdog | Alvin Kamara | Rush + Rec Yards | over | 0.0568139689190557 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|f7747872-2256-41eb-988e-da59a2931a51 | underdog | Chuba Hubbard | Receptions | under | 0.0567888839933112 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e89279f6-a314-4b89-8841-4fd7f9d7b15b | underdog | Cooper Pratt | Hits | over | 0.056745217326433894 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|f0b4fdf4-1a97-4e95-b89c-054143eb1fdf | underdog | Kimberly Birrell | Double Faults | over | 0.056646516410993164 | 2026-10-24T04:39:26Z | 2026-10-24T05:50:00Z |
| underdog|4d1b1d52-2eae-461c-9057-ce1d9bfc4ee0 | underdog | Patrick Overmyer | Receiving Yards | under | 0.056562823649637606 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|427f80d8-c20a-4953-9ba2-d4f260f1ca8e | underdog | Dierre Hill | Receptions | over | 0.056366340304735474 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| prizepicks|16127001 | prizepicks | Karl Hein | Goalie Saves | under | 0.0563156832801458 | 2026-10-24T04:39:26Z | 2026-10-24T09:30:00.000-04:00 |
| underdog|ea43b8f1-33b2-42c8-9d2e-1678399861e4 | underdog | Keelon Russell | Pass TDs | over | 0.056233643741644024 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|f15a3695-f852-4979-90f0-f2b517bf4da9 | underdog | Elijah Higgins | Receiving Yards | under | 0.0561049507995341 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|c56069f5-7322-40ba-a234-f5f699ae2646 | underdog | Chop Robinson | Sacks | over | 0.05601796101094486 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8933129e-bb98-41af-a84b-5e524615a1d6 | underdog | T.J. Hockenson | Receiving Yards | under | 0.0559605706113038 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3636946d-f9e6-4a3d-9368-cadef3a447d9 | underdog | Woody Marks | Receiving Yards | under | 0.055942806448925464 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|dcf89a53-7242-4b80-9067-f817f87fad1f | underdog | Noah Fant | Receiving Yards | under | 0.05569116003186114 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|6f6fed0c-f6ce-4a5e-914a-0aef85982115 | underdog | Horatio Fields | Receptions | over | 0.05567329872066995 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|d742fc76-3146-48bb-baf8-6aa7b3f709b1 | underdog | Willie Rodriguez | Receiving Yards | under | 0.055590809770993954 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|629e9af4-14d9-4e86-9db3-adeaf4f962e8 | underdog | Sanfrisco Magee | Receptions | under | 0.05545679230221434 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|8ac91a1d-e17e-4e89-917e-0741ed24326f | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.0552499210820918 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|9dec28bf-f1cc-4984-9300-00fc93a45701 | underdog | CJ Donaldson | Rush Yards | under | 0.05495515497621306 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|426409ee-3306-404e-a882-7ebe7e86f823 | underdog | JaQuail Smith | Rush Yards | under | 0.05449388264579191 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|2dd8d10d-2956-4b6a-9cb4-fda1851e8b02 | underdog | Radarious Jackson | Receiving Yards | over | 0.0544359927857397 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|096beaa3-503a-4e1c-9e67-fe625725b5c4 | underdog | Mateen Bhaghani | XP Made | over | 0.0543306333436769 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|4e5542db-139b-4799-9d3b-e8b9caa1b84d | underdog | Malachi Toney | Receiving Yards | under | 0.05414718965749732 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|d20ffbb4-ea0b-4628-822f-5927d2b25fd4 | underdog | Trae'shawn Brown | Rush Yards | under | 0.05395906160927333 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|1016ca21-bada-4f8c-89c3-8aa706b67cbf | underdog | Juwan Johnson | Receptions | under | 0.0539535225588111 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ce32c899-c546-40d5-b26e-9ced9c6ef8a3 | underdog | Cam Skattebo | Rush + Rec Yards | over | 0.0539214755329643 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|dd1375a5-b92b-4567-a66f-20f7f1e04f73 | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.05388790486413142 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|d6fef25a-1e32-4d8c-92b7-d29a4cb00582 | underdog | Dierre Hill | Receiving Yards | over | 0.053714462134274554 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|5ba71cee-ac69-464f-919d-e6292528dd49 | underdog | Javon Tracy | Receptions | under | 0.05358783947296375 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|ac3836b7-ed31-46ae-a383-3b2f7ddd8724 | underdog | RJ Harvey | Receiving Yards | under | 0.0533369848818797 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|47d8257d-2ea4-4623-916d-733646daaf24 | underdog | Scott Starzyk | FG Made | over | 0.0533337885644754 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|262dcb8e-4bc7-4305-a2b0-e717b681e5a6 | underdog | Ryan Flournoy | Receiving Yards | under | 0.0530145633905199 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|8afce3f7-def5-44ee-99dc-cae89d1f44eb | underdog | Byrum Brown | Pass Yards | under | 0.05293199362840961 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|cd14366b-8d4d-4e7e-853f-1ed27f89bade | underdog | JC French | Pass Yards | under | 0.05257251527898965 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|0cb669cf-b827-461d-9d39-42e64e403fdf | underdog | Tyrell Henry | Receptions | over | 0.0525262856234594 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| prizepicks|16051317 | prizepicks | Wan'Dale Robinson | Rec Targets | under | 0.0522923521605553 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c3e31ab1-4709-4b43-8b04-8f227c273411 | underdog | Harrison Butker | Kicking Points | under | 0.05183794000713 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0c7fe2c3-6b86-431f-9be5-2eb648c005b6 | underdog | Cody White | Receptions | over | 0.051779480133012146 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| prizepicks|16134830 | prizepicks | Fabian Marozsan | Total Games | over | 0.05155377504193581 | 2026-10-24T04:39:26Z | 2026-10-24T07:50:00.000-04:00 |
| underdog|07431a32-42ce-4d0b-abd0-cfb6db23b271 | underdog | Noah Jennings | Receiving Yards | under | 0.0515036832685247 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|662a988b-d8bd-4ab2-8a39-d3807e0ef5ef | underdog | Trent Mosley | Receiving Yards | under | 0.0513544523997693 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|79d34340-11b6-4b41-9894-413dae8c21c8 | underdog | Mason Mini | Receiving Yards | over | 0.05130437371051322 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|39cb0950-d224-4871-a255-7b93b815a0c9 | underdog | Emanuel Wilson | Rush + Rec Yards | under | 0.051275485959797584 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|583290fa-d7ba-4e4c-a7b6-5416c71ad379 | underdog | Jackson Chourio | Hits | over | 0.051024830073154726 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|81d3d9e3-d5c3-4a8c-a5b4-d60fe7edc089 | underdog | Kyler Kasper | Receiving Yards | under | 0.0509493282923424 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|783aa344-7332-43fa-ba78-b3cc2e729593 | underdog | Aidan Hutchinson | Sacks | over | 0.05077677472840869 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|744f7c64-587e-41f1-af9d-1bbabfac4473 | underdog | Chuba Hubbard | Receiving Yards | under | 0.0504931979002241 | 2026-10-22T04:39:42Z | 2026-10-25T17:00:00Z |
| underdog|25fa3790-d20b-4150-9c6a-160e2a5d2896 | underdog | Tyjae Spears | Rush Yards | under | 0.0503793612554041 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ec75ca22-cfa8-4fe1-af44-b136a12b3dcd | underdog | Shuai Zhang | Double Faults | over | 0.0502598728045226 | 2026-10-24T04:39:26Z | 2026-10-24T06:40:00Z |
| underdog|8478770a-27d8-46ec-99dd-bbd68a617b66 | underdog | Wayshawn Parker | Receiving Yards | over | 0.0501876493329525 | 2026-10-23T04:50:52Z | 2026-10-25T02:15:00Z |
| underdog|0a668414-4a0e-42fa-9f18-7f8c3ef5c6d8 | underdog | Isaiah McGuire | Sacks | over | 0.050164376121848764 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|8225d625-378d-487c-8596-68cf88140f58 | underdog | Ryan Flournoy | Receptions | under | 0.0501148528015784 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0c1a8b52-a086-444e-9bbf-7623ea229a24 | underdog | Rashid Shaheed | Receptions | under | 0.0500925370142416 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|4a5deac2-17dc-40d7-8e44-76ab0866612d | underdog | George Holani | Receptions | under | 0.05005544112939009 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| underdog|ef28db8f-70ad-410b-b7cc-a22e68e1490a | underdog | Pat Freiermuth | Receptions | under | 0.0499824428187301 | 2026-10-21T23:24:30Z | 2026-10-25T13:30:00Z |
| underdog|043f11be-fc7c-4b35-97e9-4d766bfbf47c | underdog | Brock Wright | Receptions | under | 0.04996663713700833 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|2637fc5f-5a0e-49ff-854c-2285f9f3a597 | underdog | Jonnu Smith | Receptions | over | 0.049960814737353365 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|2de5ac28-d00d-4457-93e8-d2427b57518f | underdog | Michael Hawkins | Pass TDs | under | 0.04983774362802329 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|03981001-9bfc-494f-b5de-c3f8be5c12e0 | underdog | Messiah Hampton | Receptions | over | 0.04967650862494999 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|ced80dce-59ad-4cbc-9c8d-69b3ca2801d1 | underdog | Kingsley Enagbare | Sacks | over | 0.04956081285635916 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|5f38dee7-872b-4757-a798-931f137332ed | underdog | Jordan Allen | Receiving Yards | under | 0.04955312435834858 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|507480b5-110f-4938-b6e8-497384f23c8b | underdog | Cade Keith | Receiving Yards | over | 0.04954998783166742 | 2026-10-24T04:39:26Z | 2026-10-25T02:00:00Z |
| prizepicks|16051304 | prizepicks | Darnell Washington | Rec Targets | under | 0.0493716300398139 | 2026-10-21T23:24:30Z | 2026-10-25T09:30:00.000-04:00 |
| underdog|aa76ff62-2cea-4932-a3b6-25933bffd7a3 | underdog | Jeremiah Koger | Receiving Yards | over | 0.0492893008519933 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|ede7b208-2151-441c-ba65-228a8c200c0d | underdog | Bam Knight | Receptions | under | 0.049108614094104164 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|f6c5d90c-aa20-4df0-8599-3fd8ba03d321 | underdog | J.K. Dobbins | Receiving Yards | over | 0.0489630391293001 | 2026-10-22T04:39:42Z | 2026-10-25T20:05:00Z |
| underdog|06c8c71a-f7db-4a2c-9d8a-ff6d764c68ef | underdog | Bucky Irving | Rush Yards | under | 0.0487607240531607 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16035052 | prizepicks | Jake Bates | Kicking Points | under | 0.0487274702622712 | 2026-10-23T13:31:04Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|38da6842-8e2b-4b9f-8e1a-2627589e622a | underdog | Harrison Butker | FG Made | under | 0.0486124772086066 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|f3ebf234-d8cb-4b70-ae85-4e26eeb452d9 | underdog | Dallas Turner | Sacks | over | 0.04831976333597565 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|1719fe92-ca52-4c4a-9698-8ea69a850602 | underdog | Trey'Dez Green | Receiving Yards | over | 0.04777622245188051 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| prizepicks|16051231 | prizepicks | Bijan Robinson | Rec Targets | under | 0.0477412880585349 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|7a805571-082c-4d49-86df-fa09a5485ead | underdog | Yandy Díaz | Hits | over | 0.047680597237872324 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|19497d03-c39f-46ac-80d2-e74b2c4a8634 | underdog | Wan'Dale Robinson | Receptions | under | 0.0476246066680077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c6eb4bd1-bbd4-4d84-a247-eef592bfa1f9 | underdog | J.K. Dobbins | Receptions | over | 0.0476044558282254 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|57243a15-62d8-4624-b55c-49b812912663 | underdog | Tyjae Spears | Receptions | over | 0.0474516029151996 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16051249 | prizepicks | Jake Ferguson | Rec Targets | under | 0.047278123853882 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|977b2034-4b67-463d-8a47-d48cfca4f3ea | underdog | John Metchie III | Receptions | under | 0.04724726183118366 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|a1ff5d6a-2777-412b-bebb-aeb1145b0fc4 | underdog | Kaelon Black | Receptions | over | 0.04704383794728084 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|b57929fa-a09d-4e6f-a44b-3038db73bdd9 | underdog | Samaje Perine | Rush + Rec Yards | over | 0.0470082519671165 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|ec454f0f-39d7-4085-8939-37caba2c5f53 | underdog | Omarion Miller | Receiving Yards | under | 0.04700525096816455 | 2026-10-23T04:50:52Z | 2026-10-24T19:45:00Z |
| underdog|b17ce54d-78a1-4fa1-ab15-3a025ee6ec33 | underdog | Mo Alie-Cox | Receptions | under | 0.04696581796029453 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|f56646dd-e9dc-47e0-b4cb-8184a207198c | underdog | Ty Dieffenbach | Pass Yards | under | 0.046696388412307 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|8530ffdb-b0b6-4aa9-84d7-111a9dee2681 | underdog | Maliek Collins | Sacks | over | 0.046256014221188635 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|d1dda524-e3d3-4fba-8cde-c8d9b3fb7823 | underdog | Amare Thomas | Receptions | over | 0.0462398251608691 | 2026-10-21T23:24:30Z | 2026-10-25T02:15:00Z |
| underdog|35962dae-0852-4830-ab91-68c9dcafb2d3 | underdog | Cam Skattebo | Rush Yards | under | 0.046116001037545 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|b6f0be07-3802-43c1-86c1-d6bb682a6d07 | underdog | Tyler Shough | Pass TDs | over | 0.0460949746765986 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|856219b6-2c95-43bd-8b72-75c50b9ac54b | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.0459857304500888 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16134135 | prizepicks | Titouan Droguet | Total Games | over | 0.04584506070236671 | 2026-10-24T04:39:26Z | 2026-10-24T06:40:00.000-04:00 |
| underdog|130a239c-1b64-4770-9290-c9748e447956 | underdog | Omar Cooper | Receptions | under | 0.04568377572350768 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|87557726-d244-4861-a281-61e88eb7a852 | underdog | Davis Allen | Receptions | over | 0.04540259617966852 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|6bcf6095-366d-4641-a1b4-d765144f12eb | underdog | Devon Dampier | Total TDs | under | 0.04505718999531316 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| prizepicks|16036976 | prizepicks | Conner Weigman | Rush Atts | under | 0.044846783355269815 | 2026-10-24T04:39:26Z | 2026-10-24T22:15:00.000-04:00 |
| underdog|2bdc8511-494e-48d0-8cdf-78689b0520d7 | underdog | Ryan Wingo | Receptions | under | 0.04472002541002029 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|ac1c6c6c-2327-4e95-af19-59c5bd28b38c | underdog | Juwan Johnson | Receiving Yards | under | 0.0446562817968326 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|249ee0b9-e0c3-41fc-8414-3c22214852df | underdog | Matt Gay | FG Made | under | 0.044627908003273875 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| underdog|e26cd63d-3055-4212-9f2e-cd41db34506e | underdog | Garrett Mitchell | Hits | over | 0.04456782829252026 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|74dea993-8edf-4ffa-9e0a-000ad1f37e22 | underdog | Jackson Chourio | Batter Walks | over | 0.044464609800362986 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| prizepicks|16051251 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.0440754381772996 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|2b8d2cf9-db2b-47d7-8f8b-ab4448b1edd6 | underdog | Lee Beebe | Rush Yards | over | 0.04402948271207929 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|e40c88ee-022c-460d-a447-35935e484914 | underdog | Joey Slye | Kicking Points | under | 0.0437911990002866 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|07356e41-4b2e-4e5c-85b2-37c5035acbdd | underdog | Brandon Phelps | Receiving Yards | under | 0.04347386683507748 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|951f0756-5616-48c0-bb15-989e6abd891d | underdog | Emanuel Wilson | Receptions | under | 0.043448009734545656 | 2026-10-24T04:39:26Z | 2026-10-26T00:20:00Z |
| prizepicks|16127115 | prizepicks | Taylor Fritz | Total Games | over | 0.04290846956186811 | 2026-10-24T04:39:26Z | 2026-10-24T08:00:00.000-04:00 |
| underdog|976edc90-d679-4566-8607-829d2e9644fc | underdog | Keenan Allen | Receptions | under | 0.042892061025248 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16128100 | prizepicks | Kenny Gainwell | Rec Targets | under | 0.04287892121183334 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|c635f281-ca04-4c4c-ae31-8bb556878ff3 | underdog | Daylyn Upshaw | Receptions | under | 0.0428467738274781 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|25ef4d6c-fafc-461a-91ad-cc9e6a9ca45e | underdog | Cooper Kupp | Receptions | under | 0.0428006415227674 | 2026-10-22T04:39:42Z | 2026-10-26T00:20:00Z |
| underdog|a81c8faf-5510-49b1-9965-e0551f32b97d | underdog | Cam Cook | Rush Yards | under | 0.042694566513198806 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|17f76a20-1ee1-47b8-9a3d-5f39912be6d5 | underdog | Bear Bachmeier | Rush Yards | under | 0.042588097960360005 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|b5e95228-34dc-4d82-a873-9396f8aec13e | underdog | Charlie Becker | Receptions | under | 0.04239973318552892 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|7aafb7c4-3a88-4ddf-ae42-e3e8e0789f45 | underdog | Isaiah Mizell | Receiving Yards | under | 0.04232720906811016 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|2244fdaf-5bad-4962-a931-aa2ee962c5c5 | underdog | John Mateer | Rush Yards | under | 0.04195846371523215 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|0fa9a4bf-e249-4a3d-8acf-9f1760034530 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.0418070609890378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051240 | prizepicks | Tommy Tremble | Rec Targets | under | 0.0417284345604694 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|5e2d7594-d323-4991-bc6e-fbe7d8abe96d | underdog | Kamari Moulton | Rush Yards | under | 0.04171229067531834 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|4d71b875-6dd2-4b78-a799-3a0909c0e2b6 | underdog | Trey Butkowski | FG Made | over | 0.0416026174253986 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|348122fb-28c4-4cb4-b1cf-6f19ea0055d5 | underdog | Kyle Juszczyk | Receptions | under | 0.0413755116703427 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|098c3980-acb0-4efc-904f-37a937d6a8af | underdog | Kendre Miller | Receptions | under | 0.04137499076753659 | 2026-10-24T04:39:26Z | 2026-10-25T13:30:00Z |
| prizepicks|16051263 | prizepicks | Matthew Golden | Rec Targets | under | 0.0413695180084056 | 2026-10-21T23:24:30Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|a6def6be-c653-4e03-a395-49db966867f2 | underdog | Bam Knight | Receiving Yards | under | 0.04126734093810713 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| prizepicks|16123698 | prizepicks | Dayana Yastremska | Total Games | over | 0.04117115357262113 | 2026-10-24T04:39:26Z | 2026-10-24T05:30:00.000-04:00 |
| underdog|8939856c-5a89-49bd-98f9-7321bfa71527 | underdog | John Mateer | Pass TDs | over | 0.040835130607410564 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|76df7d50-d1c8-4cef-a264-da1f137d2d44 | underdog | Mike Gesicki | Receiving Yards | over | 0.040754670182375 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16011586 | prizepicks | Drake Lindsey | Pass Comp | under | 0.04061445305421241 | 2026-10-24T04:39:26Z | 2026-10-24T15:30:00.000-04:00 |
| prizepicks|16128434 | prizepicks | Tommy Paul | Break Points Won | over | 0.040369610348702234 | 2026-10-24T04:39:26Z | 2026-10-24T08:00:00.000-04:00 |
| underdog|c620c5b0-762d-4cc3-9c1a-f3966aed4fd1 | underdog | Gunnar Helm | Receptions | under | 0.0400733577651734 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|907f820f-9660-4e13-8e24-10342107999c | underdog | Chase Hendricks | Receiving Yards | under | 0.03956865748562077 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|7a1d5366-61ce-4674-a634-a1e3b9ab6a7b | underdog | Bailen George | Receiving Yards | over | 0.03941616946063231 | 2026-10-24T04:39:26Z | 2026-10-25T02:00:00Z |
| underdog|ab737f2d-3b0a-4edf-b65e-7af8e6b44518 | underdog | Drew Mestemaker | Pass TDs | over | 0.03940465959910944 | 2026-10-23T04:50:52Z | 2026-10-24T23:00:00Z |
| underdog|f573a592-7913-42a5-bbb6-804638a67eb6 | underdog | Horatio Fields | Receiving Yards | over | 0.039350267125248695 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|776115e5-af34-402c-b054-a4d3027c8115 | underdog | Keshaun Singleton | Receiving Yards | under | 0.03931683876246994 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|382b3a7c-9a2a-4092-b9e8-a63bb7b4e264 | underdog | Byrum Brown | Rush Yards | under | 0.03930024073146854 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|1ad3d594-f785-442a-988e-37a405dc4bd9 | underdog | Pierre Strong Jr. | Rush Yards | over | 0.03903240736915592 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16051255 | prizepicks | Marvin Mims Jr. | Rec Targets | under | 0.0388842684737961 | 2026-10-21T23:24:30Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|3188fab2-f2b8-4313-895e-57c191d21509 | underdog | Kaelon Black | Receiving Yards | over | 0.0388077194402237 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16051242 | prizepicks | Tee Higgins | Rec Targets | under | 0.0387631549019464 | 2026-10-21T23:24:30Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|330820d7-8d2a-41ef-af1a-6866b6a9e287 | underdog | Elic Ayomanor | Receiving Yards | over | 0.038760146342862 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b795f4ba-5ba2-4cc6-ad95-76bdc67b4547 | underdog | David Hamilton | RBIs | under | 0.03872053872053871 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|21d767d6-f7db-4860-8a0f-089e5a27f285 | underdog | Kevin Jennings | Rush Yards | over | 0.03868602556384804 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|f15842e5-ff48-4497-a5f0-bdb75edb6fed | underdog | Trinidad Chambliss | Rush Yards | over | 0.038644386807208164 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|5e2fff7e-fa11-45b2-b350-f34bbbefb3c2 | underdog | Kolin Wilson | Rush Yards | over | 0.03860275423596038 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|c8c39f26-3329-4571-b0ba-cd4ee0093934 | underdog | Patrick Overmyer | Receptions | under | 0.0385503232486587 | 2026-10-21T23:24:30Z | 2026-10-25T02:15:00Z |
| underdog|7ae7d989-adee-4959-9057-42b96e9b4d2c | underdog | Makhi Hughes | Rush Yards | under | 0.038486788504749736 | 2026-10-23T04:50:52Z | 2026-10-25T02:15:00Z |
| underdog|8c7089b5-d35f-4dc3-8acc-bacdf10ca7f7 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.03848663685931952 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|e7f1b286-1bad-42fb-b0e7-0f0f4497b562 | underdog | Cooper Barkate | Receiving Yards | under | 0.03842533643681689 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|55dc01c8-c1bd-46c3-bc19-5a3c9fbd7aba | underdog | Carson Kent | Receiving Yards | over | 0.0383307343289383 | 2026-10-23T13:31:04Z | 2026-10-24T16:00:00Z |
| underdog|e3620db9-71a9-4ed1-8873-e30ae36cd8b5 | underdog | Jacoby Brissett | Pass TDs | under | 0.0382668553031229 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|16051246 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.03816939250727 | 2026-10-21T23:24:30Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f89ba872-d424-4e73-8bd7-6614b460990e | underdog | Noah Gray | Receiving Yards | under | 0.03811545624303703 | 2026-10-23T04:50:52Z | 2026-10-26T00:20:00Z |
| underdog|000a396f-0592-482b-9193-7c967d4da6e8 | underdog | Alberto Mendoza | Pass TDs | under | 0.03802515412022478 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|0beceeea-8dd0-4760-afe8-eeb63492b9e9 | underdog | Mateen Bhaghani | FG Made | over | 0.0377670802335744 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| underdog|05ea1410-88a6-44cd-a8ad-de5e26c8af7f | underdog | Gavin Lahm | XP Made | over | 0.0373018163286511 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|9c997051-d5f9-4e1b-999a-8f691a6f40fd | underdog | Kamario Taylor | Pass Yards | under | 0.03728703373907427 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|37b58552-22c6-476b-996f-76d857fff274 | underdog | Dalton Schultz | Receptions | over | 0.0372622958628433 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f8caab65-966d-4958-bc02-cd1cc7ac6f7f | underdog | Kenyon Sadiq | Receptions | over | 0.0371667149623974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f26e20ec-cce5-42d2-b0d0-65cdd3b8f5a7 | underdog | RJ Harvey | Receptions | under | 0.0371183056096371 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|16129119 | prizepicks | Emerson Jones | Total Games | over | 0.037075487141927654 | 2026-10-24T04:39:26Z | 2026-10-24T01:20:00.000-04:00 |
| underdog|e27761fb-c206-44d9-ab15-1df547597590 | underdog | Brayden Trimble | Receiving Yards | over | 0.03693525090665706 | 2026-10-23T04:50:52Z | 2026-10-24T19:00:00Z |
| underdog|b36c99d1-9b4e-4356-9b5f-76ea099ba1e2 | underdog | Joe Burrow | Rush Yards | over | 0.0369126735438984 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|16134820 | prizepicks | Hamad Medjedovic | Total Games | over | 0.03689338580657753 | 2026-10-24T04:39:26Z | 2026-10-24T07:20:00.000-04:00 |
| underdog|d30b9986-6ec1-499d-bad0-0f8909201cc8 | underdog | Tyler Shough | Rush Yards | under | 0.03669695108919868 | 2026-10-24T04:39:26Z | 2026-10-25T13:30:00Z |
| underdog|1b3c0d1d-6e11-43ae-8c46-b0bd4ad8c1e2 | underdog | TJ Thomas | Rush Yards | over | 0.0364190414929286 | 2026-10-21T23:24:30Z | 2026-10-24T19:30:00Z |
| prizepicks|16128079 | prizepicks | Samaje Perine | Rec Targets | under | 0.03636041796769329 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|393aadfa-7ea3-4799-ac7d-30aaa4574af6 | underdog | Oleksandra Oliynykova | Double Faults | under | 0.03632887501866777 | 2026-10-24T04:39:26Z | 2026-10-24T04:40:00Z |
| underdog|38f2a21d-8f0b-4316-b852-d137222284bb | underdog | Chase Brown | Receiving Yards | under | 0.0362468208379922 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|20a6828f-7b20-425b-8a99-b5533ff3dbdb | underdog | Alex Highsmith | Sacks | over | 0.036117046985766565 | 2026-10-23T04:50:52Z | 2026-10-25T13:30:00Z |
| underdog|7f9cf2d5-2fee-44a9-8064-f56c34f6daf9 | underdog | Trent Mosley | Receptions | under | 0.0360985891797962 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|1bd2931d-f443-44fe-a889-8a2694349d1b | underdog | Trinidad Chambliss | Total TDs | over | 0.036043712821523854 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|eb9400f4-cfe4-423f-875f-9a2a0433b614 | underdog | Erick All | Receptions | over | 0.03591696685781898 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| prizepicks|16127038 | prizepicks | Noah Atubolu | Goalie Fantasy Score | under | 0.03585676248241565 | 2026-10-24T04:39:26Z | 2026-10-24T12:30:00.000-04:00 |
| underdog|95151427-da0f-4d9b-9b64-708b8632ee19 | underdog | Colby Parkinson | Receptions | under | 0.035577182312387 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|2a220ee5-1d28-4719-b68e-b99237bd75f6 | underdog | Kyson Brown | Rush Yards | over | 0.03547441965739773 | 2026-10-24T04:39:26Z | 2026-10-24T19:45:00Z |
| prizepicks|16127035 | prizepicks | Gregor Kobel | Goalie Saves | under | 0.0354608867510271 | 2026-10-24T04:39:26Z | 2026-10-24T12:30:00.000-04:00 |
| underdog|aa104b28-f09d-4347-b2ca-6314a59c5fa1 | underdog | Kyle Ferrie | FG Made | over | 0.0354543097195177 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|f1a02319-532f-48ea-b85d-f1f8764f33d1 | underdog | Jaron Tibbs | Receiving Yards | under | 0.0352320649773695 | 2026-10-22T04:39:42Z | 2026-10-24T19:45:00Z |
| underdog|a0c58c32-0f6d-4bb3-885b-c72aa7289ee7 | underdog | Caleb Hawkins | Receiving Yards | over | 0.0350114322402898 | 2026-10-24T04:39:26Z | 2026-10-24T23:00:00Z |
| underdog|83375341-0bc4-4389-8595-dd4653ce1fea | underdog | Devin Singletary | Rush + Rec Yards | over | 0.03500589094834228 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|5aba7c83-7528-42ba-bcc1-e98faaf845fa | underdog | Darnell Mooney | Receptions | over | 0.0347146447100191 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| underdog|e88243b8-7b5f-4c7d-9c45-56f0a7149d7a | underdog | Jaylen Raynor | Pass TDs | over | 0.0347063301598346 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|d94a2574-5c13-4480-ba28-dfb7cc681c26 | underdog | Jeremy Scott | Receiving Yards | over | 0.034623492994426686 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|74feaf9b-e250-4842-b0e9-0eafab193972 | underdog | Kenny Johnson | Receiving Yards | under | 0.0345782823094164 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|0acf1d16-15c1-4ad2-b506-7a1bf70e7bbe | underdog | Walker Lyons | Receiving Yards | under | 0.0344986746849036 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|ba98eb9b-0a32-4e50-b155-ebeb5ea6bd74 | underdog | Taylor Fritz | Aces | over | 0.03422874238490903 | 2026-10-24T04:39:26Z | 2026-10-24T12:00:00Z |
| underdog|dc364f92-76cd-4db4-84af-95dd2c29f95f | underdog | Nyck Harbor | Receiving Yards | under | 0.0342231016278906 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|af070318-32e1-472d-8923-cf5ade068e1a | underdog | Walker Lyons | Receptions | under | 0.03421177976325318 | 2026-10-23T04:50:52Z | 2026-10-24T19:30:00Z |
| underdog|c3c79363-b269-4bd8-aa89-9204e093dba6 | underdog | Holden Geriner | Pass TDs | over | 0.03407513873321788 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|6b5a1de9-3eef-4741-9170-14f9deced32e | underdog | Matt Gay | Kicking Points | under | 0.0340167035528746 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|40d29ecb-61c3-40c7-90eb-f2834170e2b0 | underdog | Chandler Simpson | Hits | over | 0.03396442116364973 | 2026-10-24T04:39:26Z | 2026-10-25T00:00:00Z |
| underdog|cc0fb124-1eee-4a5d-8ec1-07ae0c63939c | underdog | Jonah Coleman | Rush + Rec Yards | over | 0.03377934918735054 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| underdog|a29c1696-1438-47a3-b01a-5912718e85a6 | underdog | Tyrone Tracy | Receiving Yards | under | 0.03364027564317851 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|aeeb1992-d659-4ee3-a723-c4ca21cb626a | underdog | Omari Hayes | Receiving Yards | under | 0.03342856941220629 | 2026-10-24T04:39:26Z | 2026-10-24T23:30:00Z |
| underdog|57e15af8-1326-4439-94c1-494b2c6c8db6 | underdog | Creed Whittemore | Receptions | over | 0.03335760136260307 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|73ccb174-e10e-4fab-b016-1288d6d50b2f | underdog | Chase Brown | Receptions | under | 0.0331873731070406 | 2026-10-21T23:24:30Z | 2026-10-25T17:00:00Z |
| prizepicks|15953468 | prizepicks | Braylon Staley | Recs | under | 0.03314857952762895 | 2026-10-23T04:50:52Z | 2026-10-24T15:30:00.000-04:00 |
| underdog|46b6ebd1-4af0-4990-84af-243e988664a0 | underdog | Chas Nimrod | Receiving Yards | under | 0.033045417710304115 | 2026-10-23T04:50:52Z | 2026-10-24T16:00:00Z |
| underdog|856ac129-0797-48f3-95ba-1448dd417fb1 | underdog | Nik McMillan | Receptions | under | 0.033003326382433085 | 2026-10-24T04:39:26Z | 2026-10-24T17:00:00Z |
| underdog|8a92afed-a878-4de7-bec7-1473621ff0a1 | underdog | Kirk Cousins | Pass TDs | under | 0.03291386837656618 | 2026-10-24T04:39:26Z | 2026-10-25T20:25:00Z |
| underdog|9ae00861-5dbe-4edb-ba32-2a64fe363093 | underdog | Emmett Johnson | Rush Yards | over | 0.0328425645250116 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|672fd8db-fc81-4c61-8366-cc5023140b71 | underdog | Erick All | Receiving Yards | over | 0.03264221436156661 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|425fbbd0-9045-445e-83f3-1092d3b649a5 | underdog | Deuce Alexander | Receiving Yards | under | 0.0324621299207996 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|f7464f83-92c4-424f-9a7e-b4a73ea0f4c3 | underdog | Zach Allen | Sacks | over | 0.03238628283552075 | 2026-10-24T04:39:26Z | 2026-10-25T20:05:00Z |
| prizepicks|16051314 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.032115498076035 | 2026-10-21T23:24:30Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|2756e528-6c45-41ec-9353-74f3729091c5 | underdog | Creed Whittemore | Receiving Yards | over | 0.03197247830376171 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|eea26e28-d674-4d7b-8f8e-fc71ea5a2dde | underdog | Trey Butkowski | XP Made | over | 0.0319308924100778 | 2026-10-21T23:24:30Z | 2026-10-24T16:00:00Z |
| underdog|7980f836-3a4d-4a57-a058-c185a707944e | underdog | Colton Joseph | Rush Yards | under | 0.031850316272014956 | 2026-10-23T04:50:52Z | 2026-10-24T23:30:00Z |
| underdog|e4480b0f-913c-4202-bf76-e2aff55f73c7 | underdog | Cam Ward | Rush Yards | under | 0.0318471189373211 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6b14deb0-fea6-4bf3-ad97-ef8e438bf376 | underdog | Ed Small | Receiving Yards | under | 0.031766980081673335 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|337d1046-001d-49de-8065-c0c8f2139d03 | underdog | Reece Vander Zee | Receiving Yards | over | 0.03168458627473303 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
| underdog|ddb3b6de-e82e-47a8-8018-e76d2c842a21 | underdog | Ryan Wingo | Receiving Yards | under | 0.0315164104140868 | 2026-10-21T23:24:30Z | 2026-10-24T23:30:00Z |
| underdog|437bcba0-d2dc-490b-b518-d597bc646e8d | underdog | MarShawn Lloyd | Receptions | under | 0.031455160163501805 | 2026-10-23T04:50:52Z | 2026-10-25T20:25:00Z |
| prizepicks|16128097 | prizepicks | Bucky Irving | Rec Targets | under | 0.031448787953933244 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|16e2ddea-e714-4ae0-967c-6128c1d08825 | underdog | Foster Moreau | Receiving Yards | over | 0.030947868389375688 | 2026-10-23T04:50:52Z | 2026-10-25T17:00:00Z |
| underdog|70688785-baad-476e-90a9-37341d94f0ae | underdog | Terrance Carter | Receiving Yards | under | 0.03090126700797602 | 2026-10-24T04:39:26Z | 2026-10-24T16:00:00Z |
| underdog|d9e4e22f-ac33-46ff-b4b5-2b6b3cc90b17 | underdog | John Franklin-Myers | Sacks | over | 0.03083049413015182 | 2026-10-24T04:39:26Z | 2026-10-25T17:00:00Z |
| underdog|3d7e70ce-060d-498c-9d7a-7bd4565fccc3 | underdog | Braden Pegan | Receptions | under | 0.03082119109782222 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| underdog|74d04f3c-1cc9-4276-895f-dca43dd39dbd | underdog | Conner Weigman | Total TDs | under | 0.030798283350140454 | 2026-10-24T04:39:26Z | 2026-10-25T02:15:00Z |
| prizepicks|16128081 | prizepicks | Jerry Jeudy | Rec Targets | under | 0.03047366483284586 | 2026-10-24T04:39:26Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|eb47b832-623a-4517-b8e3-f59db1fa3394 | underdog | Dominic Zvada | FG Made | over | 0.0304043417105965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|98567d65-69d2-46b3-804e-141171ccac4e | underdog | Kenny Darby | Receptions | under | 0.0301176139915753 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|d8958df4-dbda-4f8f-895c-fcc504fc3ac7 | underdog | Charlie Becker | Receiving Yards | under | 0.0300748709040623 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|0a63c1ce-cb96-4427-8b30-1e06c6b03272 | underdog | Anthony Evans III | Receiving Yards | under | 0.03002413817489069 | 2026-10-24T04:39:26Z | 2026-10-24T19:30:00Z |
