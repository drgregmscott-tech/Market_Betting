# Pipeline Digest -- 2026-10-21T04:32:59Z

## Run summary
- Ingestion: 43285 rows (PrizePicks OK, Underdog OK)
- Estimation: 43285 rows estimated (from 43285 ingested props)
- CLV logging: 588 newly flagged, 0 newly closed, 612 still open (103979 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|f8a727e6-f7b0-4157-b00b-0e79f18b706f | underdog | Bryce Young | Pass Yards | under | 0.4692307692307692 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7a5a87ce-ed58-4331-8eca-c965c013a075 | underdog | Aaron Rodgers | Pass Yards | under | 0.4482233502538072 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5669e007-1810-4de9-9feb-ea3d1b56340e | underdog | Jared Goff | Pass Yards | under | 0.4357142857142857 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|7c13508f-ad8a-440d-ae01-29774bf4e852 | underdog | Brice Turang | RBIs | over | 0.4266335227272727 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d901ce25-9ca6-4d08-a605-d775897a85aa | underdog | Geno Smith | Pass Yards | under | 0.4090737399477504 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fae16c8c-b4ea-431a-9eb2-c0ecdd1e0213 | underdog | Lamar Jackson | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e1ed7c34-5984-4d1d-b0f0-10d131ce332c | underdog | Brock Purdy | Pass Attempts | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d424e459-1d04-4391-92fb-b90d20c159d8 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9ac2fb87-7b6f-4695-9458-ccea6878beba | underdog | Drake Maye | Pass Yards | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|00b0662f-876d-4f27-b8de-738d4ca273ff | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|7a520285-f44f-4692-8b2c-e0a7ebd6e60c | underdog | A.J. Brown | Receptions | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|8ddd3d29-fe64-4279-87e3-2a09c8b64156 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|744ff821-5f30-4dad-ac3a-d24911e71405 | underdog | A.J. Brown | Receiving Yards | under | 0.4 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|cdb5e111-4cf9-4bfd-82c6-27b11ce762fc | underdog | Eddy Pineiro | FG Made | under | 0.3955537623462751 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e3084a60-03df-4043-9baa-8fdd03ce53ce | underdog | Malik Willis | Pass Yards | under | 0.3948522906927716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9693ec51-4551-43f9-853c-0fb05eafd96d | underdog | Daniel Jones | Pass Yards | under | 0.3939654564213076 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e876f263-f270-46fd-8799-71558b131266 | underdog | Deshaun Watson | Pass Attempts | under | 0.3923580334909812 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e1ed00b0-0bb2-4493-8295-f6dc71c144a4 | underdog | Lamar Jackson | Pass Attempts | under | 0.3922309590886397 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5f896a94-190d-4811-9b4b-b1f17ce66f93 | underdog | Jordan Love | Pass Yards | under | 0.3897173199669762 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|643cc8ea-4e4a-4d28-86a8-1e125427f8dd | underdog | Michael Penix | Pass Attempts | under | 0.3727880183899563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|07ddf6c9-4178-4e02-aaaf-2d85f534773f | underdog | Chase Brown | Rush + Rec Yards | under | 0.3666666666666667 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cd9b95c8-1eee-41de-874d-220e9f32f39b | underdog | Eddy Pineiro | Kicking Points | under | 0.364741071554112 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a0214899-42a8-40aa-b5af-7ec7e13774fa | underdog | Jacoby Brissett | Pass Yards | under | 0.3642857142857143 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|c88864cd-10ff-4b61-a84b-29dc767a03b9 | underdog | Drake Maye | Pass Attempts | under | 0.3635582410030858 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|96c94a21-3cb9-4c2f-9451-66f87ea9e93b | underdog | Bryce Young | Pass Attempts | under | 0.3624299417853736 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|df2d500b-274d-4174-b4d8-d32b5c551962 | underdog | Bo Nix | Pass Yards | under | 0.3619289340101522 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|38a39011-3779-4d19-a6e6-ca06836b54c2 | underdog | Brendan Baird | XP Made | under | 0.3592651266806685 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|4ae8ad3b-3e4b-49b9-a170-e5307e2a5898 | underdog | Brock Purdy | Pass Yards | under | 0.3591836734693877 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15944973 | prizepicks | Bo Nix | Pass Yards | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|15902072 | prizepicks | A.J. Brown | Recs | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-22T20:15:00.000-04:00 |
| prizepicks|15944979 | prizepicks | Dak Prescott | Pass Yards | under | 0.3509424650567749 | 2026-10-21T04:43:18Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f6ae9fbb-9d9b-4197-aac0-f2b5bef7b975 | underdog | Courtland Sutton | Receptions | under | 0.3467583550754631 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|733826c6-7b9e-47f5-9671-e7055d65c4bf | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.3457724965619085 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|0416d4a2-26e9-45a7-9f37-2777bbd905f4 | underdog | Bo Nix | Rush Yards | under | 0.3455497545580275 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|37edd000-30ff-4318-96d8-a3ca5e430a8d | underdog | Patrick Mahomes | Pass Yards | under | 0.3421724696477669 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|817e96c4-5511-4ea1-83e0-001050f7e874 | underdog | Deshaun Watson | Pass Yards | under | 0.3416243654822335 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a05edf68-a4dc-462e-8dad-49f5add046b9 | underdog | C.J. Stroud | Pass Yards | under | 0.3365482233502538 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|275ada1e-5712-4c62-8eaf-c3fd618f6b39 | underdog | Cam Ward | Pass Yards | under | 0.3358974358974359 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8dc47268-4a7d-404f-9e49-dcd9ba768270 | underdog | Kyler Murray | Pass Yards | under | 0.3335652027540378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4ab4a41a-52fd-4cc5-b31f-ec4b0c82bb82 | underdog | Trey McBride | Receptions | under | 0.3329820296458966 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|4aef0982-b0f9-4fb9-9068-d7c06de3a9b5 | underdog | Matthew Stafford | Pass Yards | under | 0.3323559588937339 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|79b37311-f15b-4882-b6a3-944e0502707c | underdog | Bo Nix | Pass Attempts | under | 0.3304520785470337 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|4f09f801-7168-49ce-a662-d98c3a4e69f4 | underdog | Trey McBride | Receiving Yards | under | 0.3290583502977099 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|3246a459-7d1f-41ff-ba1b-b9c683e7b334 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3268677849268778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0837eb99-3beb-4beb-803a-b6d445424ac1 | underdog | Jordan Love | Pass TDs | under | 0.3243123493621316 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|f0fc31cd-bda5-492c-9fde-68412646daa5 | underdog | Kirk Cousins | Pass Yards | under | 0.3229461067989536 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|21ae2dbb-b8cd-47b4-8d9e-617160fee214 | underdog | Jake Elliott | FG Made | under | 0.3198767487193468 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1776f06a-1d54-4810-893f-a6f0b18bce64 | underdog | Joe Burrow | Pass Yards | under | 0.317382759820503 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|154124b9-f603-40a2-80d3-6e46172c515f | underdog | Cam Ward | Pass Attempts | under | 0.3135302584652062 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|469a1bdc-08fa-448d-abcb-21164ec4757c | underdog | Daniel Jones | Pass Attempts | under | 0.3129432398892975 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6778a4ed-0a07-462f-ad67-3327e6b33ee7 | underdog | Tyler Shough | Pass Yards | under | 0.307201308387714 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|e34970e2-eb5b-4c42-a983-df77a630b08c | underdog | Ja'Marr Chase | Receiving Yards | under | 0.3017403489827723 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0e10287d-2f97-493e-ae55-2e6c78479625 | underdog | Tony Pollard | Rush Yards | under | 0.3014201136182672 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|96b734ec-c92b-4a1a-ad83-2d303febc0a5 | underdog | Brice Turang | Batter Walks | over | 0.2970443349753694 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7a12d1ee-529c-49c9-966a-48bcaa8ce51c | underdog | Puka Nacua | Receiving Yards | under | 0.2961452597214975 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|e56d19e3-ff75-4054-8e81-a52ef8d30309 | underdog | Kyler Murray | Pass TDs | under | 0.2942390154326902 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|586acb89-828d-495a-b781-835f3b0cca6b | underdog | Courtland Sutton | Receiving Yards | under | 0.2913478359944116 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|b014eef2-594f-4c80-9d5b-a085e4a2ebe8 | underdog | Taylor Walls | Runs | over | 0.2903540385838457 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|04a4df3d-c7db-42ac-b930-94951fa9779e | underdog | Brock Bowers | Receiving Yards | under | 0.2882455496564065 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|dd2e2081-f616-4204-bcca-e9dc82322443 | underdog | Aaron Rodgers | Pass Attempts | under | 0.2859768457225595 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|15945775 | prizepicks | Courtland Sutton | Rec Yards | under | 0.2858886737283282 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|82c1dc43-56ca-49df-997e-77509563f6d5 | underdog | Tyler Allgeier | Receiving Yards | under | 0.285 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|c11d6abb-9301-4b7f-a75b-0121f5e5949d | underdog | J.K. Dobbins | Rush Yards | under | 0.2835422534352462 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|27afcb09-4472-4907-b73c-9de29d4e33b2 | underdog | George Kittle | Receptions | under | 0.2828324993741664 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1dc224d8-4045-43ec-97c9-959c5e18ba2f | underdog | Tucker Kraft | Receiving Yards | under | 0.2825174713014219 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ed554cdd-6711-4d20-ab5c-3f9edfe1ddf7 | underdog | Jahmyr Gibbs | Receptions | under | 0.2812284582963593 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|17ee8953-2dc9-435f-abb2-1065e9ccb4c1 | underdog | Dak Prescott | Pass Yards | under | 0.2811881188118813 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|15945785 | prizepicks | Puka Nacua | Rec Yards | under | 0.2807439602633035 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|fa47da34-dc24-4af1-87ed-54c3fd5991ac | underdog | Javonte Williams | Rush + Rec Yards | under | 0.2778238745949251 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|00c9927f-5ade-43b4-b9b7-fefb63611a2d | underdog | Malik Willis | Pass Attempts | under | 0.2754400964710172 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945073 | prizepicks | J.K. Dobbins | Rush Yards | under | 0.2753101688140499 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|e975f741-7c02-4bd6-ad98-eede89cbef4a | underdog | Nico Collins | Receiving Yards | under | 0.2731951910841539 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e296ce35-a81f-49e2-af2f-4786a54b96b7 | underdog | Caleb Williams | Pass TDs | under | 0.2699980933802138 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|9324ecc4-fa13-4053-a657-df19163a720b | underdog | Jared Goff | Pass Attempts | under | 0.2687730655877962 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d60cfe44-e868-4c10-a96b-234bdd9c611b | underdog | Lamar Jackson | Pass TDs | under | 0.266696128639032 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ad87b775-bfc9-4f54-95ee-ff5ed677e61f | underdog | Ja'Marr Chase | Receptions | under | 0.2661038820739 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b55f9b1b-ed72-41fa-a296-39210a20b4bf | underdog | Jordan Love | Pass Attempts | under | 0.2646802457389526 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15956871 | prizepicks | Daniel Jones | Pass Attempts | under | 0.2638857049460724 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|96c40cdc-691c-48db-89d3-4c55dbb29290 | underdog | Sam Darnold | Pass Yards | under | 0.2626055914367695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| prizepicks|15945766 | prizepicks | Nico Collins | Rec Yards | under | 0.259763061869277 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|7f9ff427-eeca-41d9-b667-16c9f1fc8e5d | underdog | Tony Pollard | Rush + Rec Yards | under | 0.2596998817408331 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c36d1310-dae3-43f8-bcf2-44cbaae783a7 | underdog | Jake Bauers | Batter Walks | over | 0.2551849166062363 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|09bee2cd-e008-407b-87a5-2ef9740a5f75 | underdog | Malik Willis | Pass TDs | under | 0.2548170435450879 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4d49df5b-b50b-4f4f-b3cc-23c54ad94116 | underdog | Liam Hicks | RBIs | over | 0.2523518732464103 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7594b837-9c0a-4a5e-a07c-cb03792bcec9 | underdog | Rico Dowdle | Rush Yards | under | 0.2523393133447593 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|9827d4a6-1c80-4f8e-837a-59a7a4efad92 | underdog | Wil Lutz | FG Made | under | 0.2495510531033402 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|44021269-f0d9-4911-b749-f056a90069ff | underdog | Yandy Díaz | Runs | over | 0.247154217994698 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a7d67cf1-2deb-4409-a28f-186fdbd101d0 | underdog | Malik Washington | Receiving Yards | under | 0.246141552704973 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6184f886-9dae-4e0e-9275-ead56fdda1d4 | underdog | Wil Lutz | Kicking Points | under | 0.246033094417752 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|41359dbd-8223-40ba-b01b-d548d0fd476b | underdog | George Kittle | Receiving Yards | under | 0.2453249563886891 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|29b2a43f-7f8a-4846-9b2d-a61aec1b5747 | underdog | Andy Borregales | Kicking Points | under | 0.2444283245360812 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|6fc9410b-a66d-49d4-9a6e-3e3ec1d8e84a | underdog | Christian Yelich | Runs | over | 0.2421018697614444 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|151d3e83-45f8-463e-8fdc-cd3f943b9d80 | underdog | Matthew Golden | Receptions | under | 0.2412290414387117 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|6030f46c-6c57-4c46-931c-9a150e5901e0 | underdog | Jonathan Aranda | RBIs | over | 0.2407494747673969 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4cfc595f-ace4-4eec-a562-9a61b88991da | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.240025789607406 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|4372c2a4-e3a0-4193-97f2-9579fd48f8c2 | underdog | Joe Burrow | Pass Attempts | under | 0.2397570360617678 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0a21b579-be4c-4502-b653-2800bbfc14bd | underdog | Jacoby Brissett | Pass Attempts | under | 0.2341561518035735 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|63a589be-c960-48d9-a32f-d3109bb47742 | underdog | Kirk Cousins | Pass Attempts | under | 0.2338585829420534 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|fe831560-509f-4242-9401-4ecd4e49d5cb | underdog | Dak Prescott | Pass Attempts | under | 0.2320315894402933 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|751c6c65-bb0e-4b5a-bdd1-24aa64b44573 | underdog | Colston Loveland | Receiving Yards | under | 0.2310302617610162 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|193c6a4c-aa4a-46b0-a869-9e9de2826135 | underdog | Bo Nix | Pass TDs | under | 0.2300413174167165 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|4d576151-8dfd-4253-b495-f9e32f0fbfcb | underdog | Luther Burden | Receiving Yards | under | 0.2288068722746987 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|17c2adf9-75e8-44b7-9e46-b0a6769151cf | underdog | Germie Bernard | Receiving Yards | under | 0.2275384159492459 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|32c667b7-abd0-4436-bf1e-dab251e7a113 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2235175135999006 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ae0a75f0-8fde-4629-9e70-516e0115471c | underdog | Cairo Santos | FG Made | under | 0.2234479238389184 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|bf1d95e3-f10c-4550-8a39-10f875aed153 | underdog | C.J. Stroud | Pass Attempts | under | 0.2210784579055988 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|01578e35-0cb4-4a02-903e-322c92960ad3 | underdog | John Mateer | Pass Yards | under | 0.2208981207704506 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|5b90486b-c32a-4e28-812e-3e86cebac5aa | underdog | KC Concepcion | Receiving Yards | under | 0.2207706046563152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0d5dbe4-9388-4622-8cc6-c162a5b0639f | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2206178911560523 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|56656c9d-ec82-4d22-befd-cf88edbd6a09 | underdog | C.J. Stroud | Pass TDs | under | 0.21922023288096 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c9dd882b-334e-4169-b37c-b296bb877d16 | underdog | Tyler Loop | FG Made | under | 0.2188399052787495 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7f4e3123-436c-4f72-a4d7-85bd83ab7675 | underdog | Garrett Wilson | Receiving Yards | under | 0.2184905047655458 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|154fee81-5f85-4520-97bb-4c3c6043a2d8 | underdog | Geno Smith | Pass Attempts | under | 0.2178984742245129 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7dbfe9c7-e77c-46aa-8f0d-da3c00ff3729 | underdog | Cam Ward | Pass TDs | under | 0.2169355074931716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|71405e6e-4a14-4865-bab6-ba62e5a3ef7d | underdog | Junior Caminero | Runs | over | 0.2143121239622198 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|185549b0-d516-4b7f-aa37-c49d79be59e5 | underdog | Brice Turang | Runs | over | 0.2142278398962888 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9fa385ef-3694-42cb-a76e-d2a7fe5d8c37 | underdog | Jackson Chourio | Runs | over | 0.2138324873096446 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|0e1febf1-4c5b-4073-ae4c-98463ef7dc88 | underdog | Victor Mesa | Runs | over | 0.2133822929416565 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|3d7bdfbe-fd96-4e73-b04d-e4b53c629b08 | underdog | Yandy Díaz | RBIs | over | 0.210772501771793 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cca13465-8252-4583-b62f-7d1a577c6168 | underdog | Garrett Mitchell | Runs | over | 0.2099080694586312 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b3d36ef2-c5d1-42ce-bdf6-3dcd1e9c4bd1 | underdog | Colby Parkinson | Receiving Yards | under | 0.2087631852016807 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|70651333-501c-4679-a021-bd49e0d4b78f | underdog | Kyren Williams | Rush Yards | under | 0.2086633991668998 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5e78605e-bcba-4d2f-90f8-e6c3dfec5088 | underdog | Rico Scott | Receiving Yards | under | 0.2078501632803695 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|e4e5c670-0987-4d0a-8a4a-9428d204a893 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2077532646208933 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c1d936d4-68f3-4e44-837e-b333d2c4f1a2 | underdog | Jameson Williams | Receiving Yards | under | 0.2060331671729401 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|b370506b-e908-4214-93a8-152af846ee21 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.2052940952466103 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|18a8053e-96a8-43b5-909e-4c6210c3a9b2 | underdog | Andy Borregales | FG Made | under | 0.2038454190489985 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|dee64e29-a37f-4460-926f-e59809784b84 | underdog | Jared Goff | Pass TDs | under | 0.203422304954593 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|34385afe-49f2-48b5-8b4a-6630c3ae7446 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.2023355512513842 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|10021345-bbed-4a2f-a584-a3e81916b523 | underdog | Daniel Jones | Pass TDs | under | 0.200856388948677 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945793 | prizepicks | DeVonta Smith | Rec Yards | under | 0.1997754527670513 | 2026-10-21T04:43:18Z | 2026-10-26T20:15:00.000-04:00 |
| underdog|f2c4be9d-9aee-4f55-8d4b-dbe30b779a70 | underdog | Javonte Williams | Rush Yards | under | 0.1985197402148549 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|f7ea1d63-47b7-4975-9db4-7db15515d650 | underdog | Christian McCaffrey | Rush Yards | under | 0.198275138398706 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7478a968-ff4e-476b-9b0f-02fe597e1822 | underdog | Dallas Goedert | Receptions | under | 0.1970050433176551 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|bfc2e148-a21c-4383-a448-5598a14b86aa | underdog | Jonathan Taylor | Rush Yards | under | 0.1969151744354131 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7cff4e33-d73d-44f1-8d0d-5a5bf4c7277c | underdog | Matthew Golden | Receiving Yards | under | 0.1918683958802021 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|fa30225c-a2b8-4007-91b4-6e7775ca4b91 | underdog | Kendre Miller | Rush Yards | under | 0.1907546806271176 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ee0fd630-668b-45c5-b6f7-9a2833d72609 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.1896770029694203 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|86267553-d29e-4379-94fe-af64970990b8 | underdog | Elic Ayomanor | Receptions | under | 0.187836672850876 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|aa76f845-051c-4f41-86fb-b35d6b2b6dd3 | underdog | Jonny DeLuca | RBIs | over | 0.1858042977382799 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e2f0945f-5958-4cd7-b310-8337022f84ec | underdog | Daniel Carlson | FG Made | under | 0.1857689129268523 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|69170097-9590-4b1c-b393-fe6a547e6eb3 | underdog | Sam LaPorta | Receptions | under | 0.1854602802656819 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|01b304ef-c918-44f1-8674-16230b54ff51 | underdog | Jackson Chourio | Total Bases | over | 0.1832038589898196 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d5f7613a-54af-4d37-b05a-48a2b92f3df7 | underdog | Jake Bauers | Runs | over | 0.1821742352069441 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|98e02204-e6fc-49e9-9efb-16eddaa9eb4d | underdog | Jake Elliott | Kicking Points | under | 0.1818784511935599 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|495b1b8b-5942-48f5-b5f3-530e2443c7b4 | underdog | Malik Washington | Receptions | under | 0.1818756780390703 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3819447b-036b-46d1-9648-c722854bc2ed | underdog | Josh Downs | Receiving Yards | under | 0.1811543635690468 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0c431785-fb37-41ca-85af-21df097d4c2a | underdog | Tyler Warren | Receiving Yards | under | 0.1810919665120708 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b269873c-1dbc-4a2d-8234-526d80b95ae4 | underdog | Christian Barmore | Sacks | over | 0.1806750889882438 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|787e8e67-8fee-4197-9ec8-56cd2ca575d9 | underdog | Devon Dampier | Pass Yards | under | 0.1803463623954326 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|95e13e96-3915-4814-acdb-210d240d4701 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1799180201769094 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|15f3e859-2c6f-4254-abb6-7275ce408513 | underdog | Nico Collins | Receptions | under | 0.1794482585928581 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8dc8a64b-8a6d-4bbb-9c34-ed8b89025f6b | underdog | Brandon Aubrey | FG Made | under | 0.1756787358146653 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0bfe77e7-f046-485b-9c54-f72737f36efb | underdog | Garrett Wilson | Receptions | under | 0.1755107928461772 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|58600dfe-36a7-46ed-bc53-8334433e51b6 | underdog | Sam LaPorta | Receiving Yards | under | 0.1746918808648834 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a67515c6-0a36-4241-81e0-d3885298e1cc | underdog | Matthew Stafford | Rush Yards | over | 0.1739326192322227 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|11e17eff-c3c7-4b31-a4e1-eb3c30ed8c12 | underdog | KC Concepcion | Receptions | under | 0.173856293946127 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea4459fa-5f07-4a26-b2c8-da05776fd757 | underdog | Taylor Walls | Total Bases | over | 0.1738064881711291 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|906ea4dc-8125-423e-9356-fa13d3abcf3a | underdog | George Pickens | Receiving Yards | under | 0.1722765015592237 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|3614abc9-c288-4ddb-a25e-d8e7de7b52ef | underdog | Darian Mensah | Rush Yards | over | 0.1718691063862979 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|72bbe3a3-c9ed-4f5e-9efe-d6367c597685 | underdog | Rome Odunze | Receiving Yards | under | 0.1718158725979823 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|00ea7550-cb36-4538-806a-5d5487b0589f | underdog | Michael Wilson | Receiving Yards | under | 0.1705184591676428 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|2eef6a10-bacb-4d87-80f2-e93f2ddb4319 | underdog | Jonny DeLuca | Total Bases | over | 0.1704545454545454 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d0b24edb-4dc8-4f46-ae4f-c250461a8311 | underdog | Jake Bauers | Total Bases | over | 0.1704545454545454 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|24286879-1900-4fed-a44b-eecb46a2e0f1 | underdog | Camden Coleman | Pass Yards | under | 0.1703602943724456 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|ee4edd7e-7b6f-41ad-933e-3a50e62080ea | underdog | Bijan Robinson | Receptions | under | 0.1692203598276945 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fd02656c-1b55-442c-917e-205a8522dac1 | underdog | William Contreras | Runs | over | 0.1688665866695755 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9356f071-22fc-4b06-8218-7d33d2f4fb9d | underdog | DK Metcalf | Receiving Yards | under | 0.1686306638130101 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| prizepicks|15945781 | prizepicks | Jameson Williams | Rec Yards | under | 0.1684103099885777 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|2fd5f777-f98d-42fc-b079-413f01d2cea6 | underdog | Harold Fannin | Receiving Yards | under | 0.1684065370519358 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fc3864d2-892c-463e-b7d7-1b45f64c3248 | underdog | Jake Bauers | RBIs | over | 0.1677880352579147 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a4cd3dc7-85d8-4813-9663-5f976d994f69 | underdog | Junior Sherrill | Receptions | under | 0.1673593393538859 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|4379cc97-6c42-474d-9885-165493109730 | underdog | Denzel Boston | Receiving Yards | under | 0.167016966353541 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b2a4ef33-4dd7-4a8d-bebf-9282e819c744 | underdog | Joe Burrow | Pass TDs | under | 0.1668059378425955 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1583ce20-2aed-4825-9210-33ee84203275 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1662215207642232 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f65fcee2-679b-4d27-9424-1835a6bb5ec9 | underdog | Jahan Dotson | Receptions | under | 0.1642390573801065 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dcf5511e-2b26-4d33-8ab0-ed6de7733f1f | underdog | Junior Caminero | RBIs | over | 0.1639716761783977 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b21ede0e-c8d0-4b03-a66c-e119384843bc | underdog | William Contreras | RBIs | over | 0.1626771402791783 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4cfd5a4a-1f48-4365-b549-f1ac466a2341 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1626091840811822 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c452f8b7-8eba-4428-9266-453524c4a278 | underdog | Kyle Ferrie | XP Made | over | 0.1614100094526827 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c9bd1c5a-6975-4a80-ba7e-77a595cc8b70 | underdog | Garrett Mitchell | RBIs | over | 0.1600925713995065 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|88670807-df28-450c-89b9-2d671c6bfd03 | underdog | Ashton Jeanty | Receptions | under | 0.1596415908383356 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3ef8fdc9-08a4-41d9-8d28-99f6c7438824 | underdog | Andre Szmyt | FG Made | under | 0.159326507096576 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2d54750b-a6de-495e-a900-cf03ec7b64b5 | underdog | Christian Yelich | RBIs | over | 0.1591350081699345 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|40c97ee5-565d-4fa0-a0f3-0964eabdf2fe | underdog | Jackson Chourio | RBIs | over | 0.158271853935566 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a72359e4-c625-4fd5-8791-4fd01e9b8c04 | underdog | Devaughn Vele | Receiving Yards | under | 0.1576991448693823 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|4297c15a-19d8-4aad-a7d1-e28979baca47 | underdog | Preston Rex | Rush Yards | under | 0.157395970027809 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|3182912b-bec7-451d-a4f6-a8aa028c7477 | underdog | Jameson Williams | Receptions | under | 0.1572143332788562 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|abd4a840-141d-4e5c-b5f6-6338e95117ed | underdog | Jahmyr Gibbs | Rush Yards | under | 0.1567067787160168 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|7547ee98-5f6f-40d9-93d2-72793c85c4ac | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.1560786062167198 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea0839a7-b407-4729-b1f4-054f8e57be8b | underdog | Milton Williams | Sacks | over | 0.1548528827285218 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|8a310332-5951-4ac7-a77f-6c4a56dd8ed7 | underdog | AJ Barner | Receptions | under | 0.1541940474422654 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e3db4a56-7b2f-44c8-b3e2-ddd80a82dbab | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.1541234677071855 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|7c562fd8-49b6-44ee-8676-bbf1b6cbac68 | underdog | Bryce Young | Pass TDs | under | 0.1535238626727116 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|37f21c56-5c3a-4702-9320-6b096b6218ef | underdog | Kyle Pitts | Receiving Yards | under | 0.1533697059674438 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c41b9c5a-8eb4-4e28-b530-7467445701da | underdog | Matthew Stafford | Pass TDs | under | 0.1524509996804636 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|9b5bac7f-853d-4f8d-b23e-638437b1afdb | underdog | Evan Engram | Receptions | under | 0.1522431104423216 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|d0e5175c-f995-4f19-992d-d6a7520bd2b7 | underdog | Jordan Addison | Receiving Yards | under | 0.1520912252614426 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|40c92b84-7aa2-4a31-ae7b-160596e0c514 | underdog | Isaiah Likely | Receiving Yards | under | 0.1509578137931236 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fe464e1e-f6c0-4abe-b76a-3316fe11545b | underdog | Liam Hicks | Hits | over | 0.1508110346565297 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|83cc1041-7a0f-47b2-84ac-351e9d8533f3 | underdog | Taylor Walls | Hits | over | 0.1504427927544617 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f649e406-fd37-43ad-8bae-7bb995d397fd | underdog | Beau Pribula | Pass TDs | over | 0.1499521545038517 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|3fe03957-f78a-4577-b650-0f54860d6b2e | underdog | Chris Boswell | FG Made | under | 0.1495032069538866 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|eb118ae3-88ec-4af1-a4d5-238969093a3c | underdog | Greg Dulcich | Receptions | under | 0.148738688298966 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b63c3a37-09bc-42ec-acde-2b15af175d27 | underdog | Tyler Shough | Pass Attempts | under | 0.1486185642801181 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|52e828a6-c228-46b9-ba0c-81b778711038 | underdog | Jeremy Hecklinski | Pass Yards | under | 0.1484425373240185 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|aa0b7a3e-d2b1-4670-bacd-e7f0265e9da6 | underdog | Kaelon Black | Rush Yards | under | 0.1484179947276228 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8e6bce48-c270-48c4-af74-f023a926fd3c | underdog | Trey Smack | Kicking Points | under | 0.1479856099025124 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|dfcf3d2f-2bf0-48ae-bcbb-1e6ad4b39a9e | underdog | Matthew Stafford | Pass Attempts | under | 0.1478843620945529 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|894876c7-692d-4cf5-95c3-4b0632db54a3 | underdog | Mason Taylor | Receptions | under | 0.1475775689463663 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|968ff81d-59d7-4800-83ce-cfa34ff971b7 | underdog | Dak Prescott | Pass TDs | under | 0.1473394026606165 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|c48a289c-ab9f-4495-895d-bcbc743bb51b | underdog | Ethan Moczulski | FG Made | over | 0.1469323117588332 | 2026-10-21T04:43:18Z | 2026-10-24T19:00:00Z |
| underdog|9e7823b5-6ba8-4931-8647-93f4834676fa | underdog | Tucker Kraft | Receptions | under | 0.14624892899467 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|b952decd-601e-4f92-8345-d2f8930b6eb8 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.146220517841205 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d1d03112-0155-4136-93e2-5ad6c20dc792 | underdog | Braylon Staley | Receptions | under | 0.1456644416724575 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|765a2af0-4350-434c-a349-c576efd78c11 | underdog | TreVeyon Henderson | Receiving Yards | over | 0.1447113440135895 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|22b39507-a838-43d3-aca0-16eb972ac142 | underdog | Kenny Minchey | Pass Yards | under | 0.1437248785638849 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|8249186f-8862-4abc-9a48-7f8b007560fd | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1436257422239731 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3a21ad77-2638-4099-ae84-863dd656a054 | underdog | Chris Olave | Receptions | under | 0.1432171019256236 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a5c7fe6d-1a20-451b-a6f8-7879b27d6f11 | underdog | Derrick Henry | Rush Yards | under | 0.1431595063697152 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|6b69bdc8-296e-48f7-acc2-b95f5ac68d4f | underdog | Braylon Staley | Receiving Yards | under | 0.1430721831158183 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|ceb80c8d-d67c-45db-8b9b-efd6615cda7f | underdog | Tony Pollard | Receiving Yards | under | 0.1429028060309192 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4323651e-7d75-43e1-8bec-e7432a7af8de | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.1426846691132519 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|bd5833ce-b0e6-4960-9506-705850df7ad8 | underdog | Richie Palacios | Total Bases | over | 0.1425947219339821 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f06599db-6e94-41c7-b4e8-7df338f7a276 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.1424277006620714 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|cc694e60-9523-4ed2-a9c6-3646385f9315 | underdog | Ka'imi Fairbairn | FG Made | under | 0.1420318353198051 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ed3825a2-9c90-4618-bea7-7776443f101b | underdog | Bear Bachmeier | Pass TDs | over | 0.1419644793617892 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|11effad5-80fc-47d9-b6c9-d853122dcbdc | underdog | Yandy Díaz | Total Bases | over | 0.1417073170731705 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e58c86c8-e648-43d4-b9d2-cabbfd06a61d | underdog | Drake London | Receptions | under | 0.1414594528835526 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945777 | prizepicks | Michael Wilson | Rec Yards | under | 0.1412964357388831 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| prizepicks|15958668 | prizepicks | James Jones | Rush Atts | under | 0.1411288044374005 | 2026-10-21T04:43:18Z | 2026-10-21T20:00:00.000-04:00 |
| underdog|7be2c377-0bca-4111-a99a-0bef1da61de7 | underdog | David Olano | FG Made | over | 0.1405031761018376 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|8375befd-3629-4e68-bc30-385d084febe3 | underdog | Cooper Pratt | RBIs | over | 0.1399226357209549 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e7d5dbde-88a3-4383-9e54-826f1c7a0b5d | underdog | Jaylen Waddle | Receiving Yards | under | 0.1396373111187602 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|9c22489a-921c-4a35-a1f6-ba9e6aee26d3 | underdog | Carnell Tate | Receiving Yards | under | 0.1394857182718097 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|71cf2bdd-726a-490e-88b2-62ba6b5ccedd | underdog | Ethan Moczulski | XP Made | over | 0.138966102454317 | 2026-10-21T04:43:18Z | 2026-10-24T19:00:00Z |
| underdog|0938d052-b379-4057-b914-c43b6591ad06 | underdog | D'Andre Swift | Rush Yards | under | 0.1379712055333796 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|6e080788-8634-47c3-bd6e-7726cac733b2 | underdog | Rico Dowdle | Receptions | under | 0.1377303975112497 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ee5b9227-9f37-4dbe-a6e8-55c41f22dd4f | underdog | Jekail Middlebrook | Rush Yards | under | 0.1366528604973662 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|a36d3b0c-087b-4e18-84f8-70f064fd3aad | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.136283636992093 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|990e3a36-0fa9-42d5-b447-447c46e0605b | underdog | Germie Bernard | Receptions | under | 0.1357845862590205 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|a5dc555d-b835-41b2-b481-a747557a08b5 | underdog | Malik Nabers | Receiving Yards | under | 0.1355033403010405 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|575f222c-106d-4acd-bb96-fa38483730e4 | underdog | Jake Ferguson | Receptions | under | 0.1353654788338305 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|96598eb7-171b-44ef-8842-bbd789d6d72d | underdog | Cairo Santos | Kicking Points | under | 0.1348240121618629 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|7e24c2fc-b2a9-4cda-b16f-b9bc6153a23e | underdog | Greg Dulcich | Receiving Yards | under | 0.1336970921172516 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|606b0925-6155-487f-8a03-5228a08ddf06 | underdog | Colston Loveland | Receptions | under | 0.1336120349687193 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|94b93669-f3bf-42eb-8662-bd1c412798a9 | underdog | Tyler Warren | Receptions | under | 0.1328695780272055 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|008abfdb-bdff-4539-816c-b7f703ee2a9e | underdog | Liam Hicks | Total Bases | over | 0.1319930069930068 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b19f3052-9b2b-4892-9d9c-c814a1c421b8 | underdog | Jake Bates | FG Made | under | 0.1319024702666141 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|a49fb210-9a51-4589-b092-bc9895a1ee4a | underdog | Gunnar Helm | Receiving Yards | under | 0.1316121759984837 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b1f9ad06-cd7d-4e5a-959b-569a72213b85 | underdog | Radarious Jackson | Receptions | over | 0.1315816830185312 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|0fb50bc9-621b-4b85-99e0-28b0e5f153b2 | underdog | Rhamondre Stevenson | Receptions | under | 0.1315147469871405 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|565b428f-a6cf-4af8-85e6-cb5ef00a4a9a | underdog | Chase Brown | Rush Yards | under | 0.1310820845889924 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e77f583e-4054-4247-97c8-f76829754390 | underdog | Junior Sherrill | Receiving Yards | under | 0.1307650000363489 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|362a367a-8287-4a9b-afac-79b549e4c9a2 | underdog | AJ Barner | Receiving Yards | under | 0.1306153642795884 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e6bda541-d996-46c4-8c72-5d84e4a9455e | underdog | Liam Hicks | Runs | over | 0.1302904564315352 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d3e7a81d-6114-4db4-bc38-f399c76501e2 | underdog | David Hamilton | Runs | over | 0.1297705620384463 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b832c29c-26dd-4b07-a2d1-feaa7b7e7052 | underdog | Dallas Goedert | Receiving Yards | under | 0.1296687932557064 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|daf87a2e-804d-4d72-a2fe-77e260478754 | underdog | LaNorris Sellers | Pass Yards | under | 0.1296056863781028 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|02d34a8f-3eed-4486-9769-1d3795f45afb | underdog | Nick Folk | FG Made | under | 0.1295761284029778 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|08540b4a-fb83-438a-8e8c-41a3a05428fd | underdog | Dre'Mont Jones | Sacks | over | 0.1292194655448312 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|6e2b8ba4-322a-4d4a-baf7-1f473b0b3969 | underdog | Jonathan Aranda | Hits | over | 0.1291573597776903 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945756 | prizepicks | Harold Fannin Jr. | Rec Yards | under | 0.1286742733624186 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|34d055d7-33a5-4401-a090-0d03599b6aa7 | underdog | Caden Buhr | FG Made | over | 0.1283755219195639 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|fe9a8643-cbb5-455e-917e-c33f3a025f7c | underdog | CeeDee Lamb | Receiving Yards | under | 0.1283347069925714 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|d3c78fb1-24fb-4022-825b-11cb5e84b5fc | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.1277825349237309 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cb509be0-2b5d-4563-b28b-e94cb396030c | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.127491030204322 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|26d39b80-32f6-4d20-a89d-ce35e5c3bf55 | underdog | Jaylen Warren | Rush Yards | under | 0.1269833611823008 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6fff192d-2b5c-4bd7-8459-57e261dcc582 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.1266593999996237 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|39d3e316-5d17-465f-b268-469f78421358 | underdog | Tony Pollard | Receptions | under | 0.1260078504794592 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b3bf83ab-c79a-442e-a00a-95213b95e3de | underdog | Jake Ferguson | Receiving Yards | under | 0.1255662633886676 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|9300f70d-cf3a-44bf-a344-1ffccf82b88e | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1255312394568363 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9d76b014-0fc4-4360-b3c4-6c3715996d7b | underdog | Carnell Tate | Receptions | under | 0.1254536750854675 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|eaddf12e-bf09-415a-9908-175b69e1378e | underdog | Joey Slye | FG Made | under | 0.1236431134007916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|30d9b768-f076-4bf2-bc53-fae6cbfb5392 | underdog | Cooper Barkate | Receptions | under | 0.1236103888243352 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|e8852d35-ce00-44ba-b78c-d37302c09646 | underdog | CJ Bailey | Pass Yards | under | 0.1235122775008285 | 2026-10-21T04:43:18Z | 2026-10-24T02:30:00Z |
| underdog|61e7bf09-5421-4218-9b7d-53d1a654a3cc | underdog | George Pickens | Receptions | under | 0.1233908843202937 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| prizepicks|15945770 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1232415700497886 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|60cace4c-dfd0-4667-a103-b08cb4f6d79d | underdog | Walker Lyons | Receptions | under | 0.1232359978751732 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|90006bf7-f321-4955-95cd-018f58fe2476 | underdog | Victor Mesa | RBIs | over | 0.1231774761186525 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|bd7409fb-5432-4e66-a7f5-17c61264dc73 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.1231584316522158 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d78bf3d4-d352-475d-85ce-1396bbf0d873 | underdog | Gunnar Helm | Receptions | under | 0.1228111531139143 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|cdb7d26e-5b5d-44ee-b1d9-ffc08b833663 | underdog | David Hamilton | Total Bases | over | 0.1220605791387878 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945069 | prizepicks | Derrick Henry | Rush Yards | under | 0.1220323805962527 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|9023ba89-bfaa-477b-b72c-7408017ef70b | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1213989620392013 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|6f6b68bb-0f13-4a6e-960e-9aaa06bf2c88 | underdog | Richie Palacios | Hits | over | 0.1190986730781363 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|2b96e389-ec54-4965-a240-5d2e6eb051a0 | underdog | Jason Sanders | Kicking Points | under | 0.1187154660907585 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a04b010f-6f7a-4bca-bf84-a019fdc98cb2 | underdog | Jason Myers | FG Made | under | 0.1186141311795658 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e642bd88-7ada-49a6-bc3e-0426f77a3d02 | underdog | Jared Goff | Rush Yards | over | 0.1184823448445742 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|37c7f3a7-4eea-4ab7-bb95-51317d560802 | underdog | Christian McCaffrey | Receptions | under | 0.1181179607177566 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bea4dc65-3219-4de0-9721-19a9becb8a7d | underdog | Keenan Allen | Receiving Yards | under | 0.1171946925687916 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945783 | prizepicks | Jahmyr Gibbs | Rec Yards | under | 0.1168491101977031 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|a8389eaa-f9e8-4862-9d49-e0eb14b5dbe3 | underdog | Geno Smith | Pass TDs | under | 0.1162581741290298 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|43da2b56-6f19-429a-884b-a4c12ba9020c | underdog | Rashid Shaheed | Receiving Yards | under | 0.1151993821374695 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|04f5fcbc-4780-4d20-9c3d-345e6cd2ea8a | underdog | D'Andre Swift | Receptions | under | 0.1151747294320429 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|1b0fc4dd-38ef-4e17-85a8-e24686ccb9a1 | underdog | Drake London | Receiving Yards | under | 0.1146582581752583 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8ac96afb-46f0-4924-9765-9144862ff599 | underdog | Conor Talty | FG Made | over | 0.1146366001969039 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|231c4c82-8c83-44fa-95a3-a3748a7aee08 | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.1146179526454099 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|7e65673c-68cc-43d7-8230-c848586a250c | underdog | Jonathan Aranda | Total Bases | over | 0.1141668788727612 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|8aa1c383-f2a2-4617-a19c-f44214cfd4f6 | underdog | RJ Harvey | Rush Yards | under | 0.1137840709178916 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|82ab5aa5-420e-4364-bd82-207d555c2689 | underdog | Sam Darnold | Pass Attempts | under | 0.1133043312291657 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|f6e4d0b0-e037-405e-b285-07e6fe26eedb | underdog | Cooper Pratt | Hits + Runs + RBIs | over | 0.1129325344089059 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e89b86e3-ff12-4d6f-a2fe-818c587a8383 | underdog | Keelon Russell | Pass Yards | under | 0.1129234550913104 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|85560838-e552-4d85-8d61-33d8f0a1f89e | underdog | Brock Purdy | Pass TDs | under | 0.112816096678015 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c4a30c98-3ee5-437f-83ee-cef25c93d92c | underdog | Travis Kelce | Receptions | under | 0.1120341726504789 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|fcafb323-e005-4a22-964c-ea114b457bc0 | underdog | Deshaun Watson | Rush Yards | under | 0.1115471354898498 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|58f1b1ab-2870-4a4f-9629-39eb56a86d3d | underdog | Jaylen Waddle | Receptions | under | 0.1114967573933463 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|14fcaffb-85d1-4d1f-a938-d1a84828eab3 | underdog | Hunter Henry | Receiving Yards | under | 0.1113066130488846 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|709c73c7-0fe0-4b09-a6ec-8f6ddd312747 | underdog | Junior Caminero | Hits | over | 0.1108421213934509 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e72f5d6a-1c89-4517-b3e5-1df48dfff888 | underdog | Nick Folk | Kicking Points | under | 0.110772652961521 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|959728b4-52ed-4783-ad59-ef31f5becd2e | underdog | Christian Watson | Receiving Yards | under | 0.1105929494288048 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5c1d01bf-5469-4fb9-a3ad-d8a4de3206a2 | underdog | Spencer Shrader | FG Made | over | 0.110097123969825 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|147eafa0-8ae0-4d0a-be58-413d0472c6e9 | underdog | Elijah Ponder | Sacks | over | 0.1087067325384188 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|309f3f09-f15f-4c7d-9a77-6213274e2724 | underdog | Bijan Robinson | Rush Yards | under | 0.1086167266871781 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c37e171f-5e70-4561-abd4-a2dca0b9ba20 | underdog | Mason Taylor | Receiving Yards | under | 0.1075683290440285 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|349793f7-6a35-43bd-be86-669e5bf6f8cc | underdog | Kyren Williams | Rush + Rec Yards | under | 0.1071814066988122 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d3850c26-85bc-4082-a18f-1f8853b6f594 | underdog | Drake Maye | Rush Yards | under | 0.1068196271586217 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|33b6fb1b-243f-4946-8212-e797f561fe8b | underdog | Luther Burden | Receptions | under | 0.1067635448973685 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|459305bc-a8d2-47be-9d85-7abf617e183e | underdog | Bucky Irving | Rush Yards | under | 0.1066361803088958 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fd02b717-c3a5-4e7d-91cb-9989e22c31cd | underdog | Patrick Mahomes | Rush Yards | under | 0.105668666481013 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|0660c889-a4a5-4941-beff-bf58b7b65837 | underdog | Deshaun Watson | Pass TDs | under | 0.1056653767810689 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|32c6a58f-4543-44ab-9513-73e8857d24bb | underdog | DK Metcalf | Receptions | under | 0.1054909425928073 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5549b40f-c25b-4262-aa4b-46e8542b8221 | underdog | Brock Bowers | Receptions | under | 0.1052220927493255 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ea37df82-0d35-4f1b-acc4-e9a83779e8c9 | underdog | Conner Weigman | Pass TDs | over | 0.1050716675351449 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|461909ac-72fc-4954-8f53-031088f82680 | underdog | Antonio Chadha | XP Made | over | 0.1049028544387513 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|af3f221e-c2f7-47bf-a87d-9558e5637a3d | underdog | Tyler Higbee | Receptions | under | 0.1040476758946392 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|ac8c9a6d-a5e6-46dc-bede-bfdb665288d9 | underdog | Walker Eget | Pass Yards | under | 0.10402312530551 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|7bddc13b-1e8e-4ba5-8052-bb3dca935528 | underdog | Ashton Jeanty | Rush Yards | under | 0.1036891044730264 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|54680c7c-61e6-4921-be29-813cc4a2f7ce | underdog | Denzel Boston | Receptions | under | 0.1035724114812719 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bb10c724-592c-4e93-89f8-55f339b3ee9d | underdog | Brice Turang | Total Bases | over | 0.1032412965186075 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|548416c7-0afb-4659-9d00-251696eab277 | underdog | Jared Curtis | Pass Yards | under | 0.1032303512801479 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|66a12d68-7694-45bf-bff5-0baebc9e9694 | underdog | Brandon Aubrey | Kicking Points | under | 0.1027789805682906 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|1f61ca69-a504-485e-89f7-66bd2aced799 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.1027014115660162 | 2026-10-19T04:39:53Z | 2026-10-24T23:00:00Z |
| underdog|29e7d993-7d0f-49e4-ab63-a4a598637f90 | underdog | Tyjae Spears | Receptions | under | 0.1018966640435529 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e78a3150-01af-4911-935d-3f7efa466938 | underdog | Garrett Mitchell | Batter Walks | over | 0.1015540686380315 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cb6b3385-177c-4f4c-a76f-851fc6f581d6 | underdog | Christian Yelich | Total Bases | over | 0.1012237762237762 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|3b079c5e-ac07-42c8-af8a-98041f6f8dfa | underdog | Victor Mesa | Hits | over | 0.1009844763480287 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|415cd07a-ad7b-410d-9946-3eb07aeec2ab | underdog | C.J. Stroud | Rush Yards | over | 0.1008527574840064 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0a8e9968-79e9-4e19-9777-a06b21b6c1c3 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.1007112845271449 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|66176240-9346-4efb-a506-abe54845d954 | underdog | Daniel Carlson | Kicking Points | under | 0.1001222893209393 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|25473403-4276-4b6e-b54d-9bd4c192aa32 | underdog | TreVeyon Henderson | Receptions | under | 0.0999337311915784 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|a5ad1a59-ac57-4111-8f14-57870ee7dd07 | underdog | Hunter Henry | Receptions | under | 0.0994567664427219 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|d19378d4-7b16-452b-906d-5f161be21dda | underdog | Victor Mesa | Total Bases | over | 0.0994475138121546 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9a70aa52-1fd9-4201-bc6d-d00ebd15f2d7 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.0993449768275279 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|602ad854-cba6-4aa9-938a-771d9ab27f0d | underdog | Tyler Higbee | Receiving Yards | under | 0.0990552102507815 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15945774 | prizepicks | Jaylen Waddle | Rec Yards | under | 0.0982250040001608 | 2026-10-21T04:43:18Z | 2026-10-25T16:05:00.000-04:00 |
| underdog|4cdfe789-3c0f-465a-a210-8ca44253d398 | underdog | Malik Willis | Rush Yards | under | 0.0979466614355935 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ab1c3f52-8d19-4a07-8886-0d55bab8d009 | underdog | William Contreras | Total Bases | over | 0.0978456373156402 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|7d98395f-f4ec-4d64-9c69-e4f7cc2131a7 | underdog | Jake Bates | Kicking Points | under | 0.0977903849845823 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|5601128f-d4fb-4340-811b-2d1b48f13fe6 | underdog | Chandler Simpson | Runs | over | 0.0977008026069639 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|3a7f9d86-1eff-4f73-890e-01385c3bde3e | underdog | Junior Caminero | Batter Walks | over | 0.0975062889642349 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|4a3d8c3a-2255-48b6-add7-8a9ccaf422eb | underdog | Kirk Cousins | Rush Yards | over | 0.0973825339695121 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|56e0f4b6-c8b5-4080-a302-a23c5afdfed8 | underdog | Christian Watson | Receptions | under | 0.0962434061653429 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|740f3e34-29ab-4fed-ae75-13f0bc56660e | underdog | Tyler Loop | Kicking Points | under | 0.0958446334098082 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|7ed37d87-d675-4f6c-a0ff-8bad34041ac7 | underdog | Jake Bauers | Hits | over | 0.0957158320205936 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945789 | prizepicks | Travis Kelce | Rec Yards | under | 0.0956329735871087 | 2026-10-21T04:43:18Z | 2026-10-25T20:20:00.000-04:00 |
| underdog|22d58a57-d0ab-488c-9ae4-4babf7b7e71b | underdog | Austin Booker | Sacks | over | 0.0956255806439988 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|25ed5f3f-a2de-45eb-b5dc-ebf775b350ce | underdog | Andre Szmyt | Kicking Points | under | 0.0952743873816968 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0f7916e4-5189-45ec-81bd-8741389faad3 | underdog | Chandler Simpson | Hits + Runs + RBIs | over | 0.0946840065898005 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|70d3eee2-da03-4988-a667-14a183033678 | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.094209080703896 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fe80682c-0e04-450e-9223-a949ee5399b5 | underdog | Junior Caminero | Total Bases | over | 0.093964858670741 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|5f059838-bf65-4a1c-b367-0439087f5356 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.0935892146626595 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0123e5c7-742c-4880-bf17-c3c0b8599a9a | underdog | Walker Eget | Pass TDs | over | 0.0934927299248743 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|ddd1d82b-b64d-4ead-8c47-1606dfc1f449 | underdog | Kenny Minchey | Pass TDs | under | 0.0924523671302844 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|3bb69601-ceeb-41ea-b2af-537f3b45bd82 | underdog | Bear Bachmeier | Pass Yards | under | 0.0909562619608485 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|0e8858a7-5fb6-4ffd-a010-eddbbedf1bf6 | underdog | Alvin Kamara | Receptions | under | 0.0905814183401232 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|bb005938-7afb-4d7f-b449-0c0d67912e1e | underdog | Camden Coleman | Pass TDs | under | 0.0904844050792004 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|9f6dbce0-450c-4427-a7ec-510843b8a5a6 | underdog | Brice Turang | Hits | over | 0.0902807986020555 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|59d370fc-dd05-4027-964e-1195ca7272cb | underdog | Christian Yelich | Batter Walks | over | 0.0902218298201081 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|245d329e-170d-471b-b37b-153a8bee8e51 | underdog | Jalen Coker | Receptions | under | 0.089640605964081 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|791fc351-e3f2-4e01-ac2e-95d1dc1a3341 | underdog | Daniel Jones | Rush Yards | under | 0.0893167984596011 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d7f36314-a7c9-49c1-85e1-221eadd0369e | underdog | Malachi Singleton | Pass Yards | under | 0.0891787116833733 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|116be46b-f1d4-4310-8f46-e94563e753fb | underdog | Elijah Higgins | Receptions | under | 0.0886534112656307 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a2a0a9f9-a948-49bc-85ef-b581c8f3ffd1 | underdog | Richie Palacios | Batter Walks | over | 0.088489353153877 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|cf64c5a7-a46c-4618-92ce-b662047529d7 | underdog | Devon Dampier | Rush Yards | under | 0.0883622175863563 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|d2ab21f7-0981-4373-b2f1-b655b1b5e06b | underdog | Richie Palacios | Hits + Runs + RBIs | over | 0.088261718634943 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|72bba676-733c-4f38-935f-db988c749e29 | underdog | Kevin Jennings | Pass Yards | under | 0.0870823812645363 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|a0139a5a-9f00-4fe0-b66b-c90af34d0aea | underdog | Drew Sample | Receptions | over | 0.0870549798013065 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|76b095a2-bf24-4b3d-879a-bc4dbdfe4bc6 | underdog | Darian Mensah | Pass Yards | under | 0.0862435305790116 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|8022d176-f92f-45ef-b9a8-b960f6f2cddd | underdog | Jacoby Brissett | Rush Yards | over | 0.086207431678947 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|08b907c1-c47c-4a9f-8cf9-b043a2a100b3 | underdog | Cooper Kupp | Receiving Yards | under | 0.086095710674828 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|73b1aafd-baaa-4ff9-97b8-72eee79cadd9 | underdog | Tre Tucker | Receptions | under | 0.0860413061365301 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|fa61d393-e095-4590-b9c1-df688b7a18f9 | underdog | DeMario Douglas | Receiving Yards | under | 0.0846938897785486 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|56f293ed-4635-4cc3-833c-4ed9a375750c | underdog | Tee Higgins | Receiving Yards | under | 0.0834112064258462 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2816aaad-c9d9-4cd5-ad6d-58de25217f97 | underdog | Michael Mayer | Receptions | under | 0.0834003397411226 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|98d69b6f-f49b-4173-9565-e62e24af724e | underdog | Puka Nacua | Receptions | under | 0.0832851629286903 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|0c8acb0c-794e-4cd7-846e-be6600ed7ea8 | underdog | Josh Downs | Receptions | under | 0.0826092082715991 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ee420202-642a-4ac6-988b-e2cce1adb4b5 | underdog | Isaiah Likely | Receptions | under | 0.0825217515739429 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3b0eb78b-d28f-46ab-8459-886657d5c203 | underdog | Isaac TeSlaa | Receptions | under | 0.0822432608821583 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|3fdf958b-4aeb-446f-a872-8228a3fb7690 | underdog | Kendrick Bourne | Receiving Yards | under | 0.0821950618308543 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|2ac82195-7d56-4592-b4af-ca9b8586632a | underdog | Sal Frelick | Batter Walks | over | 0.0818885448916408 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|da649ac8-7eb7-442e-b69f-82cd70319f62 | underdog | Davis Warren | Pass Yards | under | 0.0812852514778754 | 2026-10-21T04:43:18Z | 2026-10-24T02:30:00Z |
| underdog|41308d6a-1585-4bd8-88a3-c4fc5587e979 | underdog | Jason Sanders | FG Made | under | 0.0803782078621125 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|fa91546b-2faf-49cd-aa41-3929b7a7a669 | underdog | Chase McLaughlin | FG Made | under | 0.0799826010276563 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0562b5f4-e52b-4875-a7c4-8c6ca0f6cffb | underdog | Emory Williams | Pass TDs | under | 0.0798418420376368 | 2026-10-21T04:43:18Z | 2026-10-22T23:30:00Z |
| underdog|ccbb2f68-eb79-4ad2-a495-e847e535bfba | underdog | Cooper Pratt | Runs | over | 0.0790784557907846 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|357d1c55-39ca-4e80-8e47-b9b3fb1d91e6 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0783802647011688 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ba66bea3-cfcc-40be-ad8c-fd53ecf64444 | underdog | Alvin Kamara | Rush Yards | under | 0.0777359816039499 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|99192d3b-e302-42f3-b7ab-2ff5db8b8a4e | underdog | Drake Lindsey | Pass Yards | under | 0.0772448058323824 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|26cd3467-0e84-45ff-96dc-d727a8953a71 | underdog | Cooper Pratt | Total Bases | over | 0.0768344484855214 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945778 | prizepicks | Christian Watson | Rec Yards | under | 0.0762747321156909 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|cb547cf1-514a-4f86-a033-a83a85347487 | underdog | Beau Pribula | Pass Yards | under | 0.0761872661390257 | 2026-10-21T04:43:18Z | 2026-10-23T23:00:00Z |
| underdog|edbee897-53dc-4356-8007-901016e55183 | underdog | Landyn Locke | Pass TDs | over | 0.0760860556431563 | 2026-10-21T04:43:18Z | 2026-10-22T00:00:00Z |
| underdog|23cc4a0a-23c5-4e37-98c2-b2ff5ed850aa | underdog | Trey Smack | FG Made | under | 0.0758399666432347 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|d266a85d-a66d-406b-bea5-4b7215c34d91 | underdog | Devaughn Vele | Receptions | under | 0.0757194055785056 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|ae60f3a8-a9ed-4acf-b13f-fdc17f7013f9 | underdog | Michael Penix | Pass TDs | under | 0.0756786003884431 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d49f6c62-edd5-4fe3-9832-a4d3f48f15ec | underdog | Brendan Baird | FG Made | under | 0.0756708302222249 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|598f8fc0-56bb-4f16-9b73-580be2ff67a0 | underdog | James Jones | Rush Yards | under | 0.0752137762098756 | 2026-10-21T04:43:18Z | 2026-10-22T00:00:00Z |
| underdog|cf07cbb5-28a5-4bb4-a9df-af4204445dc6 | underdog | Brian Robinson | Rush Yards | under | 0.0751544900174681 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|b7633e2a-8c11-4ada-8bd1-ddacccbf8dcb | underdog | Kenneth Walker III | Receptions | under | 0.0750174077225467 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|f25ffd07-3f96-4391-a7b4-6f6d04a0fc54 | underdog | Yandy Díaz | Hits | over | 0.0749959435830694 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f840b552-3515-4584-9d35-d37fca257b1f | underdog | Chris Olave | Receiving Yards | under | 0.0744110380898498 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|338ba131-3607-4a20-a144-4b4ba4900451 | underdog | Spencer Shrader | Kicking Points | over | 0.0742499051746541 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|186e0ace-b3a3-4d78-83c7-1cf9b0fc8393 | underdog | Jahan Dotson | Receiving Yards | under | 0.0741904379865594 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ea8dbe3c-3671-4662-87d9-4f2b32109df5 | underdog | TJ Engleman | Rush Yards | under | 0.0740512035783648 | 2026-10-21T04:43:18Z | 2026-10-22T23:30:00Z |
| underdog|0b37fb47-ebdc-4010-bcf5-622c00a374ac | underdog | Devon Dampier | Pass TDs | over | 0.0738331610963063 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|6aa8f84a-2ea9-4946-a243-4ba0a07c3993 | underdog | Ollie Gordon | Rush Yards | under | 0.0737138149062139 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|1e6dcf52-47f9-487f-ae1e-f4976a392121 | underdog | Legend Glasker | Receptions | under | 0.0731708661649952 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|6664dbee-84f6-4192-97a8-e1086c85f73b | underdog | Chase McLaughlin | Kicking Points | under | 0.0730635220054324 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ac0259ac-ca8b-499f-9bdf-b30e8ec016d2 | underdog | Kenneth Walker III | Rush Yards | under | 0.0725086052507029 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|17d6ef90-6748-4e56-99a2-a8358b2bcd95 | underdog | Chris Reed | Receiving Yards | under | 0.0723854353720192 | 2026-10-21T04:43:18Z | 2026-10-22T00:00:00Z |
| underdog|e26442d1-e193-41a1-b88c-71f0f33d3168 | underdog | Evan McPherson | FG Made | under | 0.0722696105068416 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|dec83796-a559-4c28-b27a-563b6106bd80 | underdog | David Hamilton | Hits | over | 0.0720133292783155 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|83952101-4b7a-488e-92a8-f2da161b929f | underdog | Garrett Mitchell | Total Bases | over | 0.0718093228573808 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|a4ff4488-c410-4fb1-93bd-6846607552af | underdog | Jordan Love | Rush Yards | under | 0.071463102847337 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15968468 | prizepicks | Facundo Diaz Acosta | 1st Set Total Games Won | under | 0.0713781317836775 | 2026-10-21T04:43:18Z | 2026-10-21T03:40:00.000-04:00 |
| underdog|99755d9f-1fcb-4c11-b802-6d9aa0b6d23c | underdog | Elija Lofton | Receptions | under | 0.0711106431709001 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|f35869de-fda0-4ff6-8837-90860751c2b9 | underdog | Will Reichard | FG Made | under | 0.071055087750351 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|052ab564-9a0a-4629-83a6-8bb879b4a0d6 | underdog | Kyle Pitts | Receptions | under | 0.0710490294424133 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|505cea21-7e6d-4f0c-a89b-2ea84e5055b9 | underdog | Josh Hoover | Pass TDs | over | 0.0710140089136008 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| prizepicks|15998568 | prizepicks | Taylor Fritz | Total Games | over | 0.0709583717196703 | 2026-10-21T04:43:18Z | 2026-10-22T06:00:00.000-04:00 |
| underdog|90443b6a-f88c-4b34-8f04-c63b212353f6 | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.0709298110898831 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|be1b741e-f4f0-4b77-b55d-588c406db2ae | underdog | Trae'shawn Brown | Rush Yards | under | 0.0708507874912628 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|00946ae8-e51a-4625-8b97-ccea92a33ea1 | underdog | Chris Boswell | Kicking Points | under | 0.0706516180970466 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|2ded917a-7a76-4d1d-b255-35ed92207746 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0705952618185794 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6eb4ceca-ab6e-4b70-b779-c61fd77dcb3a | underdog | Emmett Johnson | Receiving Yards | over | 0.0704807198097645 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|569ac77b-d993-4d8d-968a-1792c6b74392 | underdog | Cole Kmet | Receptions | over | 0.0703821345408157 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|24312ff1-78a8-4546-a295-0dc2eb910b54 | underdog | Aaron Rodgers | Rush Yards | over | 0.0700844647787815 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|7f10cedd-5cac-41a5-9819-e2515fb44f10 | underdog | Jonathan Aranda | Runs | over | 0.0700713338804368 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|00aa1266-017b-4d1d-9745-2d4a2b1e4a7d | underdog | LaNorris Sellers | Pass TDs | over | 0.0699838081654409 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|b8067499-71ed-48f3-a177-7d32cc527feb | underdog | Josh Hoover | Pass Yards | under | 0.069659832017654 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| prizepicks|15944963 | prizepicks | Jared Goff | Rush Yards | over | 0.0694248099013491 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|abe1f5d9-3690-4b8a-991e-436bd87b5318 | underdog | Evan Engram | Receiving Yards | under | 0.0687422940230393 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|a402b43a-79ba-45b6-97ea-29901106333c | underdog | Jared Curtis | Pass TDs | over | 0.0687053103943738 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|335a1947-39f1-4a26-890f-827cfc2f3188 | underdog | Darian Mensah | Pass TDs | over | 0.0686136038680533 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|eb11db4a-744a-4042-b577-ce976667973d | underdog | Christian Yelich | Hits | over | 0.0685536491453252 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15945072 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.0684517780880537 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|81b3e5a2-a320-46b5-819c-31907d2b0d4a | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.068445975150984 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|35a91dd6-b745-412d-922f-b6ae84d66283 | underdog | Kendre Miller | Receptions | over | 0.0682171400399986 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|5abacd1f-1860-4452-9bfc-c03d8dd8db6c | underdog | Emory Williams | Pass Yards | under | 0.0678988638565122 | 2026-10-21T04:43:18Z | 2026-10-22T23:30:00Z |
| underdog|abea532d-9839-4598-a505-eac4a75b759d | underdog | William Contreras | Batter Walks | over | 0.0675553034600113 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|d6673b3b-452d-4fc7-9e32-d0656157ff5a | underdog | Jonathan Aranda | Batter Walks | over | 0.0675553034600113 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|e3b4cb15-bd32-41fe-997b-31ef2b3d248e | underdog | Jonathan Taylor | Receptions | under | 0.0674513078149925 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3ba86dc2-f3d3-469a-be66-2b68cf969274 | underdog | Will Stone | FG Made | under | 0.0667977883764894 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|480c7b98-495e-4dd2-9950-cf558262314b | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.0665767306145787 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f45b86d3-dbf7-4286-ab3e-dbf13b253ea0 | underdog | Lotzeir Brooks | Receiving Yards | under | 0.0664108283053951 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|70c8977a-374c-48e5-ba23-edc0fdcc3f39 | underdog | Bijan Robinson | Receiving Yards | under | 0.0663650266525974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|06a009bf-c546-4461-b1c4-1bde1ff75c14 | underdog | Blake Corum | Rush Yards | under | 0.0662621531811924 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|2a9dcee0-e5bf-40bf-a5cc-c145bc35b2b4 | underdog | Conor Talty | XP Made | under | 0.0658903549899069 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1f7419ba-44ed-4d10-8a7a-bc913e247a3b | underdog | Blake Corum | Receptions | over | 0.0657799728513109 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|352ced7e-8dac-418b-9c42-3093c7bff249 | underdog | Dalton Schultz | Receiving Yards | under | 0.0657798179755999 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|bc5e98e3-a5ce-45a5-90f0-bbacbef40b3c | underdog | Tetairoa McMillan | Receptions | under | 0.0657606101669747 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d0131b66-956e-40d4-b77b-fa40d10bbfc1 | underdog | Mazeo Bennett | Receiving Yards | under | 0.0655546726670815 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|bebb9fcd-25b5-4cc2-9117-5d996c6b688c | underdog | Deshawn Purdie | Pass Yards | under | 0.0653797844737866 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| prizepicks|15945074 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.064833820071657 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|cb49c65a-d9c3-4097-a44f-5fdeb899d702 | underdog | Rome Odunze | Receptions | under | 0.0646316627856106 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|15944962 | prizepicks | Jordan Love | Rush Yards | under | 0.0645818534291142 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|3d22988e-6ca4-4104-b88b-0a0063bb07ec | underdog | Tyler Allgeier | Rush Yards | under | 0.0644856369050936 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|69c654d5-7f0d-40ba-b4de-0146a790613e | underdog | Jordan Addison | Receptions | under | 0.0643744310105808 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8c66b214-2beb-4cf9-be7d-cf621cb15bd7 | underdog | DJ Black | Receiving Yards | over | 0.0640859389916257 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|57f77837-6417-4a77-8305-2febe49769f2 | underdog | Bryce Young | Rush Yards | under | 0.0639499257290726 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|e28bc6e9-744d-4db8-a47a-b57fdee92fd1 | underdog | Landyn Locke | Pass Yards | under | 0.063659655930349 | 2026-10-21T04:43:18Z | 2026-10-22T00:00:00Z |
| underdog|cfbdd3d7-05e4-4a61-b2f7-be3f0ae409aa | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.0636127420865686 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|3b625a33-dfe7-4c56-a081-2453c34284ce | underdog | Tate Sandell | XP Made | under | 0.062585771684329 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|cd894ebb-1464-4062-9e9d-d7034e80fd27 | underdog | Tommy Tremble | Receiving Yards | under | 0.0625505359363844 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15944954 | prizepicks | Deshaun Watson | Rush Yards | under | 0.0624538418965843 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|5954f148-25b6-4392-adb1-cc64c04c60fc | underdog | Wayshawn Parker | Rush Yards | under | 0.0611840684856361 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|24666207-a1dd-46e8-aab0-107b45a16292 | underdog | Jackson Chourio | Hits | over | 0.0609658343933108 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|2b8f786a-ddf3-4c91-98e5-a939a1e123fe | underdog | Harold Fannin | Receptions | under | 0.0608103254568292 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|757d3abb-8848-4006-a50e-f2af3d90893f | underdog | Koby Young | Receiving Yards | over | 0.0607716190821504 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|9e502825-ef60-4a8d-80cf-bf13182154cb | underdog | D'Andre Swift | Receiving Yards | under | 0.0604497389486565 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|60491404-85e4-4da0-ba06-4d23eb4cbaf6 | underdog | Brock Purdy | Rush Yards | under | 0.0603702485832077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0d6f7a50-fa14-420e-bb35-6a8002c97c5a | underdog | Kendrick Bourne | Receptions | under | 0.0601364284559438 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|f2c7e077-b430-4e2b-b8d2-b22a32ab1f15 | underdog | Kendre Miller | Receiving Yards | over | 0.0599966168566626 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|49daeb9b-6b9c-4ebd-b104-a6d5432851ed | underdog | Garrett Mitchell | Hits | over | 0.0597962546884593 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b4073c57-0eee-482e-9c8c-29a23326ac44 | underdog | Chuba Hubbard | Rush Yards | under | 0.0593658945119207 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|035d62f9-a0a9-461c-8d81-4aa2d44b514b | underdog | Jeremy Hecklinski | Pass TDs | over | 0.059027794071683 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| prizepicks|15985676 | prizepicks | Moyuka Uchijima | 1st Set Total Games Won | under | 0.0588195313635939 | 2026-10-21T04:43:18Z | 2026-10-21T22:30:00.000-04:00 |
| underdog|09b74476-b00c-4a2f-abc2-20d3e33100a6 | underdog | T.J. Hockenson | Receptions | under | 0.0587657925838965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d6621be4-5bff-46ff-962e-0460297191db | underdog | Willie Rodriguez | Receptions | under | 0.0587377030395643 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|164633fa-5589-47e1-99e9-15fad6a9eaed | underdog | Kyler Murray | Rush Yards | under | 0.0586655465615735 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15945764 | prizepicks | Malik Nabers | Rec Yards | under | 0.0586404682364277 | 2026-10-21T04:43:18Z | 2026-10-25T13:00:00.000-04:00 |
| underdog|6858e0d3-30f0-48cb-ae37-6c56fa80e833 | underdog | Conner Weigman | Pass Yards | under | 0.058345996023547 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|4b7329da-dbec-4af2-96c4-93d046abc581 | underdog | Tyler Allgeier | Receptions | under | 0.0583402865378401 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|0ae804a5-84f2-4446-95c6-dfaad3ffdf55 | underdog | Cooper Pratt | Batter Walks | over | 0.0581140350877192 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|b359de29-0515-46be-8ab6-0d86fc6803fe | underdog | Ryan Fitzgerald | FG Made | under | 0.0575761782932597 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|11977e8c-1468-4369-bd39-5d487c3972a7 | underdog | Braden Pegan | Receiving Yards | under | 0.0575034827429468 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|6d772296-bc21-40ac-a05c-9aec92e6d3a5 | underdog | Will Reichard | Kicking Points | under | 0.0572808672239796 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|5b1209ba-20ce-4559-a6b5-422b5f506385 | underdog | Kenneth Walker III | Receiving Yards | under | 0.0570964245693671 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|788d321e-a413-42d1-9fe8-598725b5146c | underdog | Noah Fant | Receptions | under | 0.0569890350580739 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|f828bfce-adf2-4113-bdf6-73ec22b9bdfa | underdog | Taylor Walls | Batter Walks | over | 0.0569808412243998 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|420a975f-c847-42e1-acb6-f2590c1aa0f5 | underdog | Alvin Kamara | Rush + Rec Yards | over | 0.0568139689190557 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|45a12c13-3b83-4d96-ae36-157c9325e673 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.0567981928866471 | 2026-10-21T04:43:18Z | 2026-10-24T23:00:00Z |
| underdog|f7747872-2256-41eb-988e-da59a2931a51 | underdog | Chuba Hubbard | Receptions | under | 0.0567888839933112 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|15983310 | prizepicks | Mary Stoiana | Total Games | over | 0.0562484605851002 | 2026-10-21T04:43:18Z | 2026-10-21T22:30:00.000-04:00 |
| underdog|f15a3695-f852-4979-90f0-f2b517bf4da9 | underdog | Elijah Higgins | Receiving Yards | under | 0.0561049507995341 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|8933129e-bb98-41af-a84b-5e524615a1d6 | underdog | T.J. Hockenson | Receiving Yards | under | 0.0559605706113038 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|14780cc0-80ce-4e69-a65e-9bac9020139b | underdog | Will Bettridge | XP Made | over | 0.0558018821462565 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|a0300642-02c7-49c3-909f-7ff1b09d1382 | underdog | Kamari Moulton | Rush Yards | under | 0.0555951821254596 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c71abd5e-4df0-410b-b5cc-237b4e6b89ef | underdog | CJ Bailey | Pass TDs | under | 0.055387363820171 | 2026-10-21T04:43:18Z | 2026-10-24T02:30:00Z |
| underdog|8ac91a1d-e17e-4e89-917e-0741ed24326f | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.0552499210820918 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|7e550ddd-6c5f-4197-ba91-929eeaf952a5 | underdog | Drake Maye | Pass TDs | under | 0.0551889519417927 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|c68d1bb1-5199-47e8-8dac-8d8a3f546afc | underdog | Calvin Ridley | Receptions | under | 0.0551783452688616 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|d3d14224-d4f3-44e4-b59f-eea3b318c350 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.0545437934043115 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|2dd8d10d-2956-4b6a-9cb4-fda1851e8b02 | underdog | Radarious Jackson | Receiving Yards | over | 0.0544359927857397 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1016ca21-bada-4f8c-89c3-8aa706b67cbf | underdog | Juwan Johnson | Receptions | under | 0.0539535225588111 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|6b9c5594-b8af-4155-99e7-1bdcacdccd19 | underdog | Cooper Pratt | Hits | over | 0.0538445646795883 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|ac3836b7-ed31-46ae-a383-3b2f7ddd8724 | underdog | RJ Harvey | Receiving Yards | under | 0.0533369848818797 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|6cbf19ff-b866-45ad-b0c9-f847270d1f00 | underdog | Jaylin Carter | Rush Yards | under | 0.0531318485618999 | 2026-10-21T04:43:18Z | 2026-10-22T23:30:00Z |
| underdog|262dcb8e-4bc7-4305-a2b0-e717b681e5a6 | underdog | Ryan Flournoy | Receiving Yards | under | 0.0530145633905199 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|2e311167-8780-48c6-922e-8921f4e43833 | underdog | Chandler Simpson | RBIs | under | 0.052757793764988 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|dfba68ee-d29a-4eec-987a-b2c4b83be096 | underdog | Malachi Toney | Receiving Yards | under | 0.0518552229293483 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|c3e31ab1-4709-4b43-8b04-8f227c273411 | underdog | Harrison Butker | Kicking Points | under | 0.05183794000713 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|ccfdea0a-25ae-43bc-a5ed-0abbd620d81a | underdog | Chandler Simpson | Hits | over | 0.0518297023595296 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|f49b82cf-9c43-4794-8eab-7c12b861a016 | underdog | Will Bettridge | FG Made | over | 0.0516947110884357 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|07431a32-42ce-4d0b-abd0-cfb6db23b271 | underdog | Noah Jennings | Receiving Yards | under | 0.0515036832685247 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c01f7d6b-9ff9-4aaf-8d56-d4522c63a040 | underdog | Cam Skattebo | Receptions | over | 0.0512513434405716 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|81d3d9e3-d5c3-4a8c-a5b4-d60fe7edc089 | underdog | Kyler Kasper | Receiving Yards | under | 0.0509493282923424 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|bd024d3e-d866-4c4d-b1c1-64bd1707ce94 | underdog | Calvin Ridley | Receiving Yards | under | 0.0507494952659456 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16007852 | prizepicks | Ekaterina Alexandrova | 1st Set Total Games Won | under | 0.0507141060960208 | 2026-10-21T04:43:18Z | 2026-10-21T07:00:00.000-04:00 |
| underdog|25fa3790-d20b-4150-9c6a-160e2a5d2896 | underdog | Tyjae Spears | Rush Yards | under | 0.0503793612554041 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|8225d625-378d-487c-8596-68cf88140f58 | underdog | Ryan Flournoy | Receptions | under | 0.0501148528015784 | 2026-10-21T04:43:18Z | 2026-10-27T00:15:00Z |
| underdog|0c1a8b52-a086-444e-9bbf-7623ea229a24 | underdog | Rashid Shaheed | Receptions | under | 0.0500925370142416 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|9749696e-8717-4ed8-9d9e-e6a396043031 | underdog | RJ Harvey | Rush + Rec Yards | under | 0.0497149333024727 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| prizepicks|15945076 | prizepicks | Ashton Jeanty | Rush Yards | under | 0.0495987762443249 | 2026-10-21T04:43:18Z | 2026-10-25T16:25:00.000-04:00 |
| underdog|788dd9c7-6866-4b20-98c7-2c5d4e417cd0 | underdog | Rico Dowdle | Receiving Yards | under | 0.0493372067079616 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|1ceaf7f9-ef04-4cb3-8126-bf2e192e0c6b | underdog | Liam Hicks | Batter Walks | over | 0.0492863514719 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|38da6842-8e2b-4b9f-8e1a-2627589e622a | underdog | Harrison Butker | FG Made | under | 0.0486124772086066 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|7f4bce83-fa6d-4487-9f6a-5c219c05606b | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.048402522074492 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|27fc268e-10b4-49d2-aaf1-0ff311eada68 | underdog | William Contreras | Hits | over | 0.048354401129859 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|9f6e1ab5-783f-4278-8f0f-6de356b2430b | underdog | Yandy Díaz | Batter Walks | over | 0.0480963045912653 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|8013e31d-bd8b-4999-bc9b-560a68cefba4 | underdog | DJ Vonnahme | Receptions | under | 0.0479906983735245 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|19497d03-c39f-46ac-80d2-e74b2c4a8634 | underdog | Wan'Dale Robinson | Receptions | under | 0.0476246066680077 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c6eb4bd1-bbd4-4d84-a247-eef592bfa1f9 | underdog | J.K. Dobbins | Receptions | over | 0.0476044558282254 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|07a5aab6-6348-499c-9435-5fc9726caa32 | underdog | Chandler Simpson | Total Bases | over | 0.0471927901595421 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|fed27918-101a-4ae5-bbde-503c287dad55 | underdog | Marcel Reed | Pass Yards | under | 0.0471762985324026 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1ed271cb-bba9-4c2c-9364-f85aff6afeee | underdog | Michael Mayer | Receiving Yards | over | 0.0471328995672784 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| prizepicks|15885649 | prizepicks | Tomas Machac | Total Games | over | 0.0468800419372322 | 2026-10-21T04:43:18Z | 2026-10-21T03:40:00.000-04:00 |
| prizepicks|15980960 | prizepicks | Polina Kudermetova | Total Games Won | over | 0.04626309288049 | 2026-10-21T04:43:18Z | 2026-10-22T01:00:00.000-04:00 |
| underdog|b6f0be07-3802-43c1-86c1-d6bb682a6d07 | underdog | Tyler Shough | Pass TDs | over | 0.0460949746765986 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|9cfb8155-8c81-4433-b71a-9a7bcbe13ab2 | underdog | DeSean Bishop | Rush Yards | under | 0.0455126201840139 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| prizepicks|15987376 | prizepicks | Stefanos Tsitsipas | Total Games | over | 0.0452460013121037 | 2026-10-21T04:43:18Z | 2026-10-21T10:30:00.000-04:00 |
| underdog|5689b0d3-95b4-48cf-8b7a-64637e335481 | underdog | Derrick Henry | Receiving Yards | over | 0.0446794913234094 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|ac1c6c6c-2327-4e95-af19-59c5bd28b38c | underdog | Juwan Johnson | Receiving Yards | under | 0.0446562817968326 | 2026-10-21T04:43:18Z | 2026-10-25T13:30:00Z |
| underdog|55268f15-89b8-440f-9709-13195e8ca085 | underdog | Makhi Hughes | Rush Yards | under | 0.0444703429217645 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|e40c88ee-022c-460d-a447-35935e484914 | underdog | Joey Slye | Kicking Points | under | 0.0437911990002866 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|a93da550-3e70-4372-9914-466cf4f6a966 | underdog | Efton Chism | Receiving Yards | under | 0.0430119877844051 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|976edc90-d679-4566-8607-829d2e9644fc | underdog | Keenan Allen | Receptions | under | 0.042892061025248 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|c635f281-ca04-4c4c-ae31-8bb556878ff3 | underdog | Daylyn Upshaw | Receptions | under | 0.0428467738274781 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|3feb5e4d-c956-478b-b7e2-561f9e433c5c | underdog | Mike Matthews | Receptions | under | 0.0424999793848326 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|12bfff80-1934-4f3a-a28d-5b8cdafeac85 | underdog | Marcus Stokes | Pass Yards | under | 0.0424536333070093 | 2026-10-21T04:43:18Z | 2026-10-22T23:30:00Z |
| underdog|d1a9db61-ffce-482e-bc6b-98706add7fe6 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.0423914620274074 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3fbd3419-83f4-4912-89f1-cd3c466b1cff | underdog | Cole Kmet | Receiving Yards | under | 0.0420084288264219 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| prizepicks|15946181 | prizepicks | Moise Kouame | Total Games Won | over | 0.0419742020694768 | 2026-10-21T04:43:18Z | 2026-10-21T13:00:00.000-04:00 |
| underdog|0fa9a4bf-e249-4a3d-8acf-9f1760034530 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.0418070609890378 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4d71b875-6dd2-4b78-a799-3a0909c0e2b6 | underdog | Trey Butkowski | FG Made | over | 0.0416026174253986 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|96f84345-5f36-4f5a-9056-13914b64c59c | underdog | Ricky Johnson | Receiving Yards | over | 0.0414466829015862 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|76df7d50-d1c8-4cef-a264-da1f137d2d44 | underdog | Mike Gesicki | Receiving Yards | over | 0.040754670182375 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9883b094-eb96-49bb-b19e-acb1de659a8f | underdog | Sedrick Alexander | Rush Yards | under | 0.0404961008798157 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|95e7d081-aa15-4135-9ca6-6659bebf45c9 | underdog | Drew Rasmussen | Strikeouts | over | 0.0403526728606122 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|3188fab2-f2b8-4313-895e-57c191d21509 | underdog | Kaelon Black | Receiving Yards | over | 0.0388077194402237 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|330820d7-8d2a-41ef-af1a-6866b6a9e287 | underdog | Elic Ayomanor | Receiving Yards | over | 0.038760146342862 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| prizepicks|16010451 | prizepicks | Benjamin Bonzi | Total Games Won | over | 0.0386538961436011 | 2026-10-21T04:43:18Z | 2026-10-21T14:10:00.000-04:00 |
| underdog|9cc03fdf-3868-45f9-9a81-a782eba2ab48 | underdog | Eli Raridon | Receptions | over | 0.0383137825842563 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|e3620db9-71a9-4ed1-8873-e30ae36cd8b5 | underdog | Jacoby Brissett | Pass TDs | under | 0.0382668553031229 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|046ad160-8a73-4019-9661-3da94708c8f4 | underdog | Deshawn Purdie | Pass TDs | over | 0.0378066594112244 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|24fc4929-32c0-43d3-8142-b83dd6d88dfc | underdog | Cam Skattebo | Rush Yards | under | 0.0374576623319525 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|3753c21e-bad3-43a8-8e6f-e7002d0790cb | underdog | Reece Vander Zee | Receptions | over | 0.0374300137689319 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|37b58552-22c6-476b-996f-76d857fff274 | underdog | Dalton Schultz | Receptions | over | 0.0372622958628433 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f8caab65-966d-4958-bc02-cd1cc7ac6f7f | underdog | Kenyon Sadiq | Receptions | over | 0.0371667149623974 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|f26e20ec-cce5-42d2-b0d0-65cdd3b8f5a7 | underdog | RJ Harvey | Receptions | under | 0.0371183056096371 | 2026-10-21T04:43:18Z | 2026-10-25T20:05:00Z |
| underdog|cf4c446d-dcc1-494e-817d-2787a74da32a | underdog | Evan McPherson | Kicking Points | under | 0.036901211017894 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|4deafeb0-8398-4a54-bece-82ab8693e503 | underdog | Willie Rodriguez | Receiving Yards | under | 0.0362943645092556 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|199b9729-2a09-46ba-9d22-0447014a9127 | underdog | Sal Frelick | Hits | over | 0.0362883664873167 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|38f2a21d-8f0b-4316-b852-d137222284bb | underdog | Chase Brown | Receiving Yards | under | 0.0362468208379922 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|95151427-da0f-4d9b-9b64-708b8632ee19 | underdog | Colby Parkinson | Receptions | under | 0.035577182312387 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|aa104b28-f09d-4347-b2ca-6314a59c5fa1 | underdog | Kyle Ferrie | FG Made | over | 0.0354543097195177 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|c07c53d6-5e28-4e56-84c4-7f5377197c29 | underdog | Sal Frelick | Total Bases | over | 0.0353449497095905 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|6de3ecf1-c2e1-4ffd-af16-c9510234efe0 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.0351824731940149 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|8db350de-6410-46bf-9c27-7d0328352246 | underdog | Jackson Chourio | Batter Walks | over | 0.0350877192982455 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|c66e8fe0-4e1e-4c20-a04e-49dc04b3a837 | underdog | Jamari Person | Receiving Yards | over | 0.0349027322063265 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|4b0693d6-e2e3-4e81-8c87-7af72c6bfba0 | underdog | David Hamilton | Hits + Runs + RBIs | over | 0.0346043286046869 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|5e8a1a4d-6855-408d-92fe-bde76464fbca | underdog | Noah Bennee | Receiving Yards | over | 0.0345719590912054 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|0acf1d16-15c1-4ad2-b506-7a1bf70e7bbe | underdog | Walker Lyons | Receiving Yards | under | 0.0344986746849036 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|484399f4-298f-4063-9c16-33871082f309 | underdog | Patrick Overmyer | Receiving Yards | under | 0.0344533909502258 | 2026-10-21T04:43:18Z | 2026-10-25T02:15:00Z |
| underdog|dc364f92-76cd-4db4-84af-95dd2c29f95f | underdog | Nyck Harbor | Receiving Yards | under | 0.0342231016278906 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|d92d231d-58a6-4ef9-b39e-4a82d9662500 | underdog | Eli Raridon | Receiving Yards | over | 0.034179084008324 | 2026-10-21T04:43:18Z | 2026-10-23T00:15:00Z |
| underdog|6b5a1de9-3eef-4741-9170-14f9deced32e | underdog | Matt Gay | Kicking Points | under | 0.0340167035528746 | 2026-10-21T04:43:18Z | 2026-10-25T20:25:00Z |
| underdog|c4570c51-d4b2-49a4-be2a-a8dd9be0c3f3 | underdog | David Hamilton | RBIs | under | 0.0340022296544035 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| prizepicks|15944449 | prizepicks | Lorenzo Musetti | 1st Set Total Games | over | 0.0336527073157869 | 2026-10-21T04:43:18Z | 2026-10-21T13:00:00.000-04:00 |
| underdog|e1237ca6-c1de-42af-af96-2f51a245e8ca | underdog | Isaiah Horton | Receptions | under | 0.0335034079007621 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|9dbc436f-aa52-4668-9616-c736415d380c | underdog | Tyjae Spears | Receiving Yards | under | 0.0334345042428332 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|9ae00861-5dbe-4edb-ba32-2a64fe363093 | underdog | Emmett Johnson | Rush Yards | over | 0.0328425645250116 | 2026-10-21T04:43:18Z | 2026-10-26T00:20:00Z |
| underdog|e4480b0f-913c-4202-bf76-e2aff55f73c7 | underdog | Cam Ward | Rush Yards | under | 0.0318471189373211 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|0f41da18-0d9d-441e-acd6-39469e55d1f7 | underdog | Reece Vander Zee | Receiving Yards | over | 0.0316182443989341 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|1f939575-5ddc-4b82-9561-76c4952c4966 | underdog | Jacob Misiorowski | Strikeouts | over | 0.0316158443643395 | 2026-10-21T04:43:18Z | 2026-10-24T00:00:00Z |
| underdog|6dceb37a-1f3c-4781-b4dd-d17735519b96 | underdog | Makai Jackson | Receiving Yards | under | 0.0310717080847511 | 2026-10-21T04:43:18Z | 2026-10-22T23:00:00Z |
| underdog|ae6a1b6b-65d7-4ec6-844c-c6cc1c49c137 | underdog | Keelon Russell | Pass TDs | over | 0.0309791832376557 | 2026-10-21T04:43:18Z | 2026-10-24T19:30:00Z |
| underdog|0266c68f-fb4e-4581-bffe-8d4ac46bb909 | underdog | Malik Knight | Receiving Yards | over | 0.0305004001869657 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
| underdog|eb47b832-623a-4517-b8e3-f59db1fa3394 | underdog | Dominic Zvada | FG Made | over | 0.0304043417105965 | 2026-10-21T04:43:18Z | 2026-10-25T17:00:00Z |
| underdog|98567d65-69d2-46b3-804e-141171ccac4e | underdog | Kenny Darby | Receptions | under | 0.0301176139915753 | 2026-10-21T04:43:18Z | 2026-10-24T23:30:00Z |
| underdog|d8958df4-dbda-4f8f-895c-fcc504fc3ac7 | underdog | Charlie Becker | Receiving Yards | under | 0.0300748709040623 | 2026-10-21T04:43:18Z | 2026-10-24T16:00:00Z |
