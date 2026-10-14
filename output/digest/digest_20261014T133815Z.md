# Pipeline Digest -- 2026-10-14T13:38:15Z

## Run summary
- Ingestion: 31821 rows (PrizePicks OK, Underdog OK)
- Estimation: 31821 rows estimated (from 31821 ingested props)
- CLV logging: 752 newly flagged, 0 newly closed, 773 still open (101576 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|fc780c36-4c37-400f-b73e-b7d5f22eb97f | underdog | Jalen Hurts | Pass Yards | under | 0.4846153846153845 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|51b2d1db-1a40-4dc0-8329-590c7fbfd37c | underdog | Bhayshul Tuten | Rush Yards | under | 0.4583756345177665 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|37204193-6127-433e-a27a-2840304a56d6 | underdog | Rico Dowdle | Receptions | under | 0.4510204081632654 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|bd1d8bc9-8db9-42b4-a944-b34294025b5c | underdog | Dak Prescott | Pass Yards | under | 0.4357142857142857 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|7f4f5321-a5a7-436e-85be-21b87e127214 | underdog | Cam Ward | Completions | under | 0.4357142857142857 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|ccdd0e22-5f7f-4aa0-8e90-6d129e6873f8 | underdog | C.J. Stroud | Pass Yards | under | 0.4275095132104642 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|75b4ec86-f762-4d23-8d87-37a23c0e31e0 | underdog | Brice Turang | RBIs | over | 0.4177471930459978 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|2061beb4-a062-45fc-ab07-afb168f64713 | underdog | Drake Maye | Pass Yards | under | 0.4111261484410682 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2201f28c-07c1-40fa-8da4-37b32701ec75 | underdog | C.J. Stroud | Completions | under | 0.4010256812509019 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|62243537-95c2-47b7-b97c-b916cc4f932e | underdog | Trevor Lawrence | Completions | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|8fe4cf12-83be-4f79-b10a-301df00fa387 | underdog | Jordan Love | Completions | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|772f574c-f68d-4b62-b864-7e9f124c7dd8 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|ccdcdb79-cb81-4b8a-9e5a-061fc12ce25a | underdog | Cam Ward | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|672efe4e-700a-44b2-b073-d529efaec934 | underdog | Daniel Jones | Completions | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|558e93a8-af20-4e7f-a3bf-b4d53c831a53 | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|913179c5-5f4c-42d7-a6fa-c4e086b9af85 | underdog | Bo Nix | Completions | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|8f20911c-0977-442e-8ea1-d56313c700db | underdog | Brock Bowers | Receiving Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|d999d013-7f1c-44f0-a3ef-388240580758 | underdog | Jacoby Brissett | Pass Yards | under | 0.3990868523006889 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|53dd1a76-7510-4a33-ab9a-4cfdde0704d6 | underdog | Bo Nix | Rush Yards | under | 0.3975363175477312 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|36bd8f02-5712-4172-bedf-d5f1e38f2fd3 | underdog | Bo Nix | Pass Yards | under | 0.3952610880631269 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|2e43bfba-d649-4a25-891d-f0afe52ac7e8 | underdog | Jalen Hurts | Completions | under | 0.3941834030149655 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0fc5a90d-d46a-43a1-acb5-a428e76c89e8 | underdog | Drake Maye | Completions | under | 0.3907749648626163 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c5400d76-0c42-422b-a2ba-cc588efd8226 | underdog | Matthew Stafford | Pass Yards | under | 0.3893178531832612 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|439f721c-d9a1-4af5-aa10-1c2c1fc921e2 | underdog | Patrick Mahomes | Pass Yards | under | 0.3888093202184146 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|bca19c70-8173-4dbf-9c97-310b536c68af | underdog | Deshaun Watson | Completions | under | 0.3834285107704754 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|643b7f07-041c-4012-8d02-060a5bce3b43 | underdog | Deshaun Watson | Pass Attempts | under | 0.3801969861056373 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|21a3bf23-bece-4735-9f8d-0c89f53e33ae | underdog | Nico Collins | Receptions | under | 0.3784872632706449 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|ddcb16ad-7cc1-4994-8d1d-2317c966e808 | underdog | Rico Dowdle | Rush Yards | under | 0.3773869346733668 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|ad060ed6-2e7a-4455-8555-3e27047e4f12 | underdog | Jordan Love | Pass Yards | under | 0.3745565574821633 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|b7582a7b-1d30-47a1-984a-56546465c98b | underdog | Deshaun Watson | Pass Yards | under | 0.3666666666666667 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7dab4049-49b8-4aae-865f-72eecbda1495 | underdog | Bo Nix | Pass Attempts | under | 0.3652502058081595 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|54c0ddbe-6f6b-4eab-8b34-18fdbeb12d53 | underdog | Josh Allen | Pass Yards | under | 0.3642857142857143 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|30825256-dd0f-4b08-b83b-407bdfd1f608 | underdog | Dak Prescott | Pass Attempts | under | 0.3611567123463544 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|9bd4243b-d66a-44f0-bee0-cb305545e0c7 | underdog | Dak Prescott | Completions | under | 0.3591836734693877 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|7e37f673-c4c4-4da2-9214-dce687340fbf | underdog | MarShawn Lloyd | Rush + Rec Yards | under | 0.3584775430066913 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|ea4185cf-2d5a-45f1-86ba-146999352de8 | underdog | Bryce Young | Completions | under | 0.3568527918781726 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|670ffe88-f898-45b6-a02c-54325118bf6d | underdog | Caleb Williams | Completions | under | 0.3564102564102563 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9649df7d-26e2-4396-b781-b09a819883e3 | underdog | Daniel Jones | Pass Yards | under | 0.3517766497461929 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15683925 | prizepicks | Brock Purdy | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683924 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683909 | prizepicks | Cam Ward | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15683919 | prizepicks | Justin Herbert | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15723424 | prizepicks | Nico Collins | Rec Targets | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15683903 | prizepicks | Bryce Young | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15735889 | prizepicks | Jordan Marshall | Rush Atts | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-17T15:30:00.000-04:00 |
| underdog|c61f6639-a8c2-4e20-8354-9f795b44678d | underdog | Puka Nacua | Receiving Yards | under | 0.3495795126746557 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|765536f2-5839-4303-8f76-5a2a4524feb6 | underdog | Jameis Winston | Pass Yards | under | 0.348546777600185 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|db1d13ee-0b8a-41bc-8a70-aba8c034ee79 | underdog | Trey McBride | Receptions | under | 0.342145746487567 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15723443 | prizepicks | George Kittle | Rec Targets | under | 0.341921366253107 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683906 | prizepicks | Geno Smith | Pass Yards | under | 0.338311604119263 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15683899 | prizepicks | C.J. Stroud | Pass Yards | under | 0.3382107114340275 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|c67b981b-b23d-47db-adf6-b8f5f6a4e62b | underdog | Bryce Young | Pass Attempts | under | 0.3353909493099263 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|ecf9c6f4-e5fa-4ed0-bea3-5b8982916aee | underdog | Trevor Lawrence | Pass Attempts | under | 0.3294277790484354 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|12806d11-1e9e-4a32-8fc2-04028e5904ab | underdog | Daniel Jones | Pass TDs | under | 0.3266041330003657 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|af90f7f8-717d-4f94-9b0d-333362186e51 | underdog | Cam Ward | Pass Attempts | under | 0.3261081579549447 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e6e83f06-ae4f-41e5-a5cc-c9f665ee7579 | underdog | Daniel Jones | Pass Attempts | under | 0.3244294467701507 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dbef21f7-8539-4676-bdff-2a4ddf1252f1 | underdog | Steven Kwan | Batter Walks | over | 0.3238095238095237 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|f05c24fc-78c0-493b-8ce6-9feb3858682e | underdog | Jake Elliott | FG Made | under | 0.3225381400412137 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|aee40d9f-461c-4f06-8b9b-fe203e02c6d5 | underdog | Jalen Hurts | Pass Attempts | under | 0.3206722392424812 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|58b5d29c-2d56-4c1a-966b-292e02495e88 | underdog | Pat Freiermuth | Receiving Yards | under | 0.3141555179995734 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3164163f-7617-40cb-aa56-0856f1e0584b | underdog | MarShawn Lloyd | Rush Yards | under | 0.311954300748184 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|2744aeb4-0653-48c6-b4a7-e651a98c0ccc | underdog | Javonte Williams | Rush + Rec Yards | under | 0.3103105265361454 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|72028630-5ab0-4b39-865b-851e65097487 | underdog | Drake Maye | Pass Attempts | under | 0.308375205762582 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|db134f85-1a29-40ce-b046-e6d955c3ef5c | underdog | Tyler Allgeier | Receiving Yards | under | 0.3060913705583756 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15683920 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.3055814338761505 | 2026-10-14T13:48:29Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15682636 | prizepicks | Nico Collins | Recs | under | 0.3053857655203934 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|744acf38-d3c3-4f1f-9cd8-7e2b50b26645 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.2999518308336556 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|897a3c30-9a33-448e-ba83-2f00b649c62e | underdog | Colby Parkinson | Receiving Yards | under | 0.2992094934886594 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|2a9c2df2-8e18-49a9-b7c2-2aad9db24e0c | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.2972482863172812 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c8ac6bfb-e09b-4cb1-803c-6a56f5d52516 | underdog | Bryce Young | Pass Yards | under | 0.2919597989949749 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|964dcae5-96e9-44b6-a27e-ee7fbadaf6a4 | underdog | Nico Collins | Receiving Yards | under | 0.2884463944318267 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|55d0d31c-3f7a-4482-8405-f9a5abe59b9a | underdog | Jake Ferguson | Receptions | under | 0.2876336994087167 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|55b47abf-32ed-45e5-a2ec-361f022d0ef9 | underdog | Jonathan Taylor | Rush Yards | under | 0.2867669174203633 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c3b1e631-4f04-4743-a9b2-290dba6a2a67 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.2823119981048771 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|957b9f0c-82e8-4b2e-91e9-c2d76ca35389 | underdog | Jacoby Brissett | Completions | under | 0.2816213188948928 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|5cbedd25-a7a8-4005-addb-961571b64f36 | underdog | Tyler Shough | Completions | under | 0.2808957153525451 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|03b6c7bf-e8dc-4440-9a9c-4781de9cc969 | underdog | Trey McBride | Receiving Yards | under | 0.2801520136261292 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|d3c3a6e9-5929-4a3e-9088-35799b74f01c | underdog | Matthew Golden | Receptions | under | 0.2775508426244876 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|c4962bd0-9cad-4db6-b290-37c617e9b340 | underdog | Sam Darnold | Pass Yards | under | 0.2741939397553101 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|e588c048-2140-4bc6-8395-1fe1c4865ed9 | underdog | Patrick Mahomes | Completions | under | 0.2708723424371061 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|2b57daf7-22b6-4816-991e-47e724821f20 | underdog | Cade Otton | Receiving Yards | under | 0.2707419203198506 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a22e1a0c-8a95-411f-b104-565d5b814e6b | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.2693715380754727 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|15744347 | prizepicks | William Yarbrough | Goalie Saves | under | 0.2653322542431131 | 2026-10-14T13:48:29Z | 2026-10-14T19:30:00.000-04:00 |
| underdog|22fb7c91-776f-4678-8ea0-4782ab3c13f1 | underdog | Kayshon Boutte | Receiving Yards | under | 0.2632087138051393 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|8f0a4c6f-0b3f-4710-93f3-96bbe1c5ca98 | underdog | Courtland Sutton | Receptions | under | 0.2629885512783336 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|c8baa336-1aa0-4ab5-b3d2-3c83d7535d90 | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.2622004393874644 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|62b0a1fd-5554-468e-b71a-6536af05538b | underdog | Andy Borregales | Kicking Points | under | 0.2613710015278975 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15723421 | prizepicks | Troy Franklin | Rec Targets | under | 0.2604130964540189 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| underdog|a7876469-c0e7-4334-98d0-a505f8b8dc80 | underdog | Chris Godwin | Receiving Yards | under | 0.2567496945982092 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|81a2fcab-0a7b-4595-94f8-1b271019cd44 | underdog | Tucker Kraft | Receiving Yards | under | 0.2536667531167488 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|64fa3fb0-371a-4399-a470-4806cd9fa069 | underdog | Jameis Winston | Completions | under | 0.2532280767597126 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15683997 | prizepicks | Jonathan Taylor | Rush Yards | under | 0.2517606567079542 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|c5acba82-935e-474c-987f-00b0cf877447 | underdog | Cam Ward | Pass TDs | under | 0.2512320552021212 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b5fa4b0e-a5ba-42e4-8cb6-a0d202119dba | underdog | Cam Skattebo | Rush Yards | under | 0.2487082794547079 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a92ad24e-ec99-46d0-8f50-4af1e8f1635a | underdog | Matthew Stafford | Completions | under | 0.2473784624359858 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|7c99b3f0-2889-4f46-9fdc-a4851043a1f1 | underdog | Jacoby Brissett | Pass Attempts | under | 0.2460501997507972 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|e7ccfe46-abb5-46b8-84d3-faff98c13061 | underdog | John Mateer | Pass Yards | under | 0.2457678039126989 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|05485cd8-dc2c-4521-81bf-a481cdc1ecd2 | underdog | Courtland Sutton | Receiving Yards | under | 0.2454785145903021 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|af45a3d6-0d67-4920-883d-b2b6365a851d | underdog | C.J. Stroud | Pass Attempts | under | 0.2437286377589941 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|e3a2e6f2-4cbb-4af3-bea5-e56fe1603c50 | underdog | Tyler Shough | Pass Yards | under | 0.2427210130268616 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d09b90b6-3ab5-4090-b15c-f1ccc808787a | underdog | Cade Otton | Receptions | under | 0.2423514232380079 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|65ef2c13-cfea-42a7-bdbf-93a8550656e2 | underdog | Drew Stevens | FG Made | under | 0.2421453388790657 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|996a220b-78df-492f-b574-56b82f208efa | underdog | Bryce Young | Rush Yards | under | 0.2405083178181394 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|aef8c163-690d-4dae-8fc0-485f829790bc | underdog | Tyler Warren | Receiving Yards | under | 0.2404375756721354 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|4780f111-f055-461e-a54b-1e65e3512120 | underdog | Taylor Walls | Runs | over | 0.2392967841921734 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15683901 | prizepicks | Tyler Shough | Pass Yards | under | 0.2390376714724932 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15687743 | prizepicks | Mike Evans | Rec Yards | under | 0.2385575580504614 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|84078f63-d932-45e1-8085-b2f10127c8da | underdog | Caleb Williams | Pass TDs | under | 0.2380544783775852 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7047f00e-c97b-41a5-9426-fc42ecf0639d | underdog | Javonte Williams | Rush Yards | under | 0.2372141038649273 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|977dec9d-6402-426e-8f51-6d4bb5c3e733 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.2365589508306458 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|558d40fd-e8d3-4c4b-970e-26160aa67a11 | underdog | Andy Borregales | FG Made | under | 0.2361857173045409 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|02f8d30a-3faf-4019-9e4b-3f18499f139b | underdog | Andy Pages | RBIs | over | 0.2329749103942652 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|587af320-781b-4741-92e5-04e6948efe32 | underdog | James Cook | Receiving Yards | under | 0.2318445501439744 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|a8e80302-8d45-4e80-9ad2-09fefb833a87 | underdog | Kayshon Boutte | Receptions | under | 0.2317193988254039 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|3868e530-a5de-43c7-8b1d-edeec1e76d31 | underdog | Brice Turang | Runs | over | 0.2292889367988179 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|9cfb0112-0ade-4d22-803f-de0262b0faba | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2284157658901 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|6bc10753-8297-457d-9518-25d4ee1eba65 | underdog | Devaughn Vele | Receiving Yards | under | 0.2240964216381492 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1d4a82ed-e7b1-4924-8f6e-eab2a4ba54a8 | underdog | Jordan Love | Pass Attempts | under | 0.222580596214166 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|2452706d-bd2d-4083-aa3d-1ce7c6afd13a | underdog | Joey Slye | FG Made | under | 0.2223264379230971 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15723442 | prizepicks | Mike Evans | Rec Targets | under | 0.2220100080898542 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|86eef5f7-1c9f-400e-9e64-e332b3f79b80 | underdog | Brock Bowers | Receptions | under | 0.2210269090232406 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|3ce9570e-6224-4323-b856-ce4395e0d562 | underdog | Christian Watson | Receptions | under | 0.2209177914243855 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|155eea42-f1c0-48f5-9525-e018a546a660 | underdog | J.K. Dobbins | Rush Yards | under | 0.219301241831077 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|15687737 | prizepicks | Tucker Kraft | Rec Yards | under | 0.2190911706849104 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|9e52bb65-8439-4676-9593-c897df710a9d | underdog | Woody Marks | Rush + Rec Yards | under | 0.2177120715184628 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|b0164882-418d-4442-86e1-85dfa04318c5 | underdog | Brice Turang | Batter Walks | over | 0.2173469387755102 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|88911d68-704d-41c3-afdb-ab87b0d9d340 | underdog | Kyren Williams | Rush Yards | under | 0.2169659386271212 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|1f3d7ff2-39cd-4c06-a894-fb8e4ead7d9f | underdog | Patrick Mahomes | Pass Attempts | under | 0.2162126154027662 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|89f4e5fd-aa0f-4725-bb01-b4467e84a52f | underdog | Jake Ferguson | Receiving Yards | under | 0.2160391354209354 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|5e43ac6c-63e7-410f-9265-d601fa11e0ad | underdog | Harrison Butker | FG Made | under | 0.214587288997989 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|e5b7e240-510f-457e-8edf-9a771c4fe543 | underdog | Jonathan Aranda | RBIs | over | 0.2136452787895768 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|5a91a24e-49e5-4209-83f9-3b7c8d51ce0d | underdog | Drew Stevens | Kicking Points | under | 0.2124726155728683 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|7d8943fe-5951-424f-8995-603567e55bd8 | underdog | Rashid Shaheed | Receiving Yards | under | 0.212319413790601 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|c4b860b8-b613-4c35-93e2-56c781831e79 | underdog | Woody Marks | Rush Yards | under | 0.2117935457831465 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|351db95d-f239-4fa0-8c57-a06f0d7572e3 | underdog | Jakobi Meyers | Receiving Yards | under | 0.2116111373551161 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|de8111af-ab9b-47ca-ad72-c608c7427ea0 | underdog | Wil Lutz | FG Made | under | 0.2095113360718971 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|8054aefb-c0bd-4a10-a5ef-e7c0e4e7ab00 | underdog | Tyler Shough | Pass Attempts | under | 0.208079456536072 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|94a6ea69-df25-4406-9f94-a0ed8e9ceff8 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.2071901102718252 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|8fac6f32-0743-4149-9a77-c77f4f385ef0 | underdog | Garrett Mitchell | Runs | over | 0.2069889702092567 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|65d7986b-e2e8-445c-b028-434042f6381a | underdog | Liam Hicks | RBIs | over | 0.206850933144342 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|22e7f08c-673a-40d5-9db8-3afc5bac20a2 | underdog | Daniel Carlson | FG Made | under | 0.2050604333166797 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dc679d8f-b4f8-4421-8da4-89177cc127d2 | underdog | Darnell Washington | Receptions | under | 0.2045237698362181 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|69bfc8c2-fae1-4e15-95fa-cf1f9f22fb01 | underdog | Juwan Johnson | Receiving Yards | under | 0.2034750253722937 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|bbd58c2e-96a7-4138-a392-dba610056bd4 | underdog | Keenan Allen | Receiving Yards | under | 0.2018763061455277 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|caf87b5b-3cb6-4166-a934-44799c45d9b4 | underdog | Kenny Gainwell | Rush + Rec Yards | under | 0.2009188670650303 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|09435cfa-954d-4d25-8356-54fa86974f59 | underdog | Kyle Pitts | Receiving Yards | under | 0.200879687248247 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d79a2dc9-8fd9-482b-a1cd-829342024ae7 | underdog | Michael Wilson | Receiving Yards | under | 0.1995963998953762 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|12232759-b565-42b1-b1d6-9582b3b2ef29 | underdog | Rickie Collins | Rush Yards | under | 0.1995200276051804 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|f1ef8ef5-e398-454d-8097-cc5ecb56e4ca | underdog | Gunnar Helm | Receiving Yards | under | 0.1988442240792169 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c626e584-99ea-47a0-ae53-bafaf2f6f5cb | underdog | Wil Lutz | Kicking Points | under | 0.19883205462497 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|3b8a9290-d4c6-46d0-8f50-97a3f6b11b6b | underdog | Yandy Díaz | Runs | over | 0.1987171580115946 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|46ba4bba-d7fe-426e-9018-fdfe8531b8f4 | underdog | Dilin Jones | Rush Yards | under | 0.1974183012515771 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|8a02783a-1dff-4c0b-9a55-3edb3ef8b8e3 | underdog | Tony Pollard | Rush Yards | under | 0.1965890475866585 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|735e06d2-b1b9-4e60-b29b-299434f44981 | underdog | Jackson Chourio | Runs | over | 0.1964285714285714 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|ed222574-5695-447d-b3eb-1881e6688bcd | underdog | Colby Parkinson | Receptions | under | 0.1957637012704456 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|42891c21-671a-4321-ac17-50ada03e2836 | underdog | Bo Nix | Pass TDs | under | 0.1944401539646314 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|e46f2c75-efcb-49d2-8ae7-d5b69c2fcd24 | underdog | Marvin Harrison | Receiving Yards | under | 0.1941604442781539 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|6d2481a4-2c5c-4778-81c1-f5acc7af0bd3 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.1939201311318077 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| prizepicks|15723434 | prizepicks | Drake London | Rec Targets | under | 0.1937930998385586 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|9405dfd5-60b0-43c0-8202-eba95b163556 | underdog | Jake Bauers | RBIs | over | 0.1936036830247819 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|a695b86c-d124-43a7-a8e7-aa24fcb588fe | underdog | Jackson Chourio | Total Bases | over | 0.193356143253779 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|35d861c6-9932-4a6d-a8aa-b5342670c1bc | underdog | Hunter Henry | Receiving Yards | under | 0.1925969360185846 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|f1db0b0d-d3fe-41f1-b6a8-e17ac63a567d | underdog | Derick Hall | Sacks | over | 0.1921574868764754 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|a016d077-c21e-4d53-855d-f9edfcf77c78 | underdog | Brayan Rocchio | RBIs | over | 0.1904400257755683 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|7256e676-627a-40ac-a9e4-3a7b4113b44a | underdog | Derrick Henry | Rush Yards | under | 0.1903353082826653 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dd38c784-2201-44d7-8db0-602989b6df33 | underdog | Patrick Mahomes | Pass TDs | under | 0.1902228449795199 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|fb98833b-bf32-43a9-bb5c-4e3c72cb508a | underdog | Byron Murphy | Sacks | over | 0.1898461744293597 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|e49f5936-c6d1-4afb-ac6d-1c0234134b44 | underdog | Yandy Díaz | RBIs | over | 0.1892362839788907 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|07b66d9d-a869-4f25-8d86-2a85cdcb7a20 | underdog | Jordan Marshall | Rush Yards | under | 0.1891973770499735 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|44c0e623-9a0c-4178-80c6-9cb29d6c4efc | underdog | Richie Palacios | RBIs | over | 0.1881469076361267 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|b68506ca-3a8d-46f0-affd-77f2faa26576 | underdog | Avery Johnson | Pass Yards | under | 0.1878565173243475 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|e893bd4b-7a6f-4040-9ff1-0a52171ad604 | underdog | Jake Bauers | Runs | over | 0.1877346683354194 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|958b580a-5ab5-4044-934b-0ac081fdc6a0 | underdog | Sam Darnold | Completions | under | 0.1868429662256046 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|9bab758e-34cc-4fb3-8c31-200293b9885b | underdog | Jahan Dotson | Receptions | under | 0.1860641735232708 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|50422981-5c77-4f11-ae41-67cd350683a6 | underdog | Cooper Barkate | Receptions | under | 0.1859728406878125 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|5349d44c-86c6-4858-8d42-fd22cb4b4144 | underdog | Trey Smack | Kicking Points | under | 0.1857794312901399 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|b23d17c9-7c52-404e-aa5e-028d92effe52 | underdog | Kyle Tucker | Runs | over | 0.1840460641808863 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|65f38e1a-ada4-4ac5-8639-203a3a9ea58e | underdog | Troy Franklin | Receptions | under | 0.1815161076631426 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|15687720 | prizepicks | Harold Fannin Jr. | Rec Yards | under | 0.180946868081903 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|6876b9e9-32d4-419f-a431-b48fcbe763ae | underdog | Jake Elliott | Kicking Points | under | 0.1805952065005913 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15723416 | prizepicks | Courtland Sutton | Rec Targets | under | 0.1792819374942463 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|90b5fe03-1736-4d24-8645-967f7f0979c7 | underdog | Trinidad Chambliss | Pass Yards | under | 0.1782944841996697 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|b3eec42f-7778-4279-9037-8b1faaa16fe6 | underdog | Chris Boswell | FG Made | under | 0.1781179386493 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|f5d389a9-6382-4527-999b-2455ec093edd | underdog | Trey Smack | FG Made | under | 0.1778895553592853 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|d8de004a-6275-4664-8ef9-c8ba52498bbc | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.1776296612544015 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|556cfe0e-8dbc-44f9-b74c-a5180c4a28a1 | underdog | Dak Prescott | Pass TDs | under | 0.1773583982428295 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|6772e16a-1bdf-453a-a28b-0c748bbea7e0 | underdog | Tyler Loop | FG Made | under | 0.1770424297998158 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|731d37c6-ade6-44ea-bb7f-091a1903844b | underdog | Victor Mesa | Runs | over | 0.1767441860465116 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|e946b002-73d9-4915-80ee-974ac181f60b | underdog | Tyler Bass | Kicking Points | under | 0.1766617003170982 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|56ef781e-69f5-4c15-ba2f-c0373967b1a9 | underdog | Cairo Santos | FG Made | under | 0.1764682504265735 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2b638c80-9720-4cdd-aebf-7b5548d8cb19 | underdog | George Pickens | Receiving Yards | under | 0.1763502988084485 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|44297deb-d9d9-4e65-8f5c-0a24cc2920eb | underdog | Josh Downs | Receiving Yards | under | 0.1752931823371081 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3005c7a2-7bf6-413d-a5d9-e48e2366cec1 | underdog | Dani Dennis-Sutton | Sacks | over | 0.1748527974565202 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|f8335bdf-c993-479c-8c04-efbecb774228 | underdog | William Contreras | RBIs | over | 0.1745695227260975 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|4c68e229-9921-4182-ba6d-c40aec14cd71 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.1740586189714768 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15755605 | prizepicks | Tamara Zidansek | Break Points Won | under | 0.1739023924809642 | 2026-10-14T13:48:29Z | 2026-10-15T04:00:00.000-04:00 |
| underdog|55341b8c-cf22-4325-b79f-152bbe3814fe | underdog | Hunter Henry | Receptions | under | 0.1739016258424721 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|393bbdfb-4861-4029-a382-9bbdbe7ca088 | underdog | James Cook | Rush + Rec Yards | under | 0.1732532918133281 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|d31ec3c1-1454-4f6e-a1cf-b5909d8958f4 | underdog | Jake Bauers | Batter Walks | over | 0.1714285714285713 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|e5c633f6-2c24-4231-ad22-6d39df9ac0c4 | underdog | Josh Downs | Receptions | under | 0.1713631742035923 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3d6b3630-c595-4547-bb7c-f221365eb3ad | underdog | Brock Glenn | Pass Yards | under | 0.171158638005568 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|0e30ea08-702e-45d5-8d5e-4c032c135d03 | underdog | Jake Bauers | Total Bases | over | 0.1704545454545454 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b672c11a-0696-4bc3-9be0-b37c7908bb1c | underdog | Brayan Rocchio | Total Bases | over | 0.1704545454545454 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15684002 | prizepicks | Javonte Williams | Rush Yards | under | 0.1702978224716673 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|11a4e7fa-7b14-445d-832a-1ae8e64b713c | underdog | James Cook | Rush Yards | under | 0.1689159382095952 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|ca3ac3a3-ff99-4085-a837-d3b1f7afb399 | underdog | Arch Manning | Pass Yards | under | 0.1685351776459563 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|38d8e1c2-90aa-4c16-b808-7b2906d9cfe7 | underdog | Garrett Mitchell | RBIs | over | 0.1674929091133308 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|70f924d8-5beb-498c-bed1-313b001e69b2 | underdog | Matthew Stafford | Rush Yards | over | 0.167094951302097 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|4efa3762-a676-4d5b-a1d1-3a3748385fcf | underdog | Joey Slye | Kicking Points | under | 0.1655511449168644 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|761b5e37-e881-4e5b-b90e-2320cadf53a0 | underdog | Jackson Chourio | RBIs | over | 0.1652549060872309 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|1dd43681-eaf9-4b33-936c-c6c41f735c4e | underdog | Evan Engram | Receptions | under | 0.1644800840376477 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|8559d807-e609-46ff-9be0-ff32cfd8143e | underdog | Cooper Pratt | RBIs | over | 0.1638494478251069 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15687714 | prizepicks | Devaughn Vele | Rec Yards | under | 0.1635409176999198 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|69715286-9666-42f8-9954-c03bca37ac63 | underdog | Junior Caminero | Runs | over | 0.1632987633201469 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|89d3eb30-9a85-4e3e-9c4f-159e9a43dcad | underdog | Max Muncy | Singles | over | 0.1627802691739626 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|0d3c4ee1-ca6a-40eb-84b9-c8e3b65db064 | underdog | Josh Allen | Pass TDs | under | 0.1627144064890061 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|b1011fa5-ab4c-4310-9b46-4ae8ffcb2813 | underdog | Pat Freiermuth | Receptions | under | 0.1624330256402943 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|83b4abde-6928-4a4a-a2df-b5fd87cd74bd | underdog | Christian Watson | Receiving Yards | under | 0.1621802881678482 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|bf8ccbb4-d1af-4277-ab08-437558f49937 | underdog | William Contreras | Runs | over | 0.1604428288169199 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|6a24444b-d4f1-450e-95d0-4dc9ed5c5024 | underdog | Leonard Williams | Sacks | over | 0.1572757506198505 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|15684004 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.1568613213703028 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|c982d1b6-c6bb-4ecb-9d07-f1cac39fdefe | underdog | Cairo Santos | Kicking Points | under | 0.1567601511555229 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|8e6b4547-0422-442f-abb9-55686caf27af | underdog | Harrison Butker | Kicking Points | under | 0.1551636721561381 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|f659de6c-1bd6-423f-935d-55d8524379fe | underdog | Tucker Kraft | Receptions | under | 0.1549622277027542 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|4284d8db-84c7-4141-9f1f-f30d2adcfdce | underdog | Sam Darnold | Pass Attempts | under | 0.1549136920761094 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|58327e81-8020-44ad-af44-03b1fbd8bb71 | underdog | Conner Weigman | Pass Yards | under | 0.1538721988856832 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|48904c0d-1c73-428c-aa26-7ad5cd913032 | underdog | Malik Nabers | Receiving Yards | under | 0.1533379309309255 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7ca2d8ca-b26c-4dc3-bb49-db1ddb56b143 | underdog | Emeka Egbuka | Receiving Yards | under | 0.1530574072708483 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2aad0d22-9c66-4ed6-80d7-a56b81749ba7 | underdog | Taylor Walls | Total Bases | over | 0.1527470061979415 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|ff39f108-c483-44f8-9400-804891c0967f | underdog | Travis Bazzana | RBIs | over | 0.1522643312924642 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|5693a7a9-10ae-4fbc-9aa9-ca340cfc5634 | underdog | Parker Washington | Receiving Yards | under | 0.1516952925945273 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|a082f757-9917-4475-b528-a6c4093c2f34 | underdog | Jonny DeLuca | RBIs | over | 0.1512605042016806 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|fe7699d1-ef91-4af1-b659-848a9fc6f064 | underdog | Jonathan Taylor | Receptions | under | 0.1510995727170617 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15693996 | prizepicks | Jordan Love | Pass Attempts | under | 0.1509099959443077 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|b9124811-9067-49e8-a49f-16ad145f87a5 | underdog | Elic Ayomanor | Receptions | under | 0.1496107501484767 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b685af26-4e67-42f7-8e85-3c64bfff033d | underdog | Jacory Croskey-Merritt | Rush + Rec Yards | under | 0.1495013359615125 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| prizepicks|15723441 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.147919974847375 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|01efb930-7229-4c70-8539-9616f238bc3e | underdog | Daniel Carlson | Kicking Points | under | 0.1476873009888748 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7dba62e5-13b5-40af-83ba-fb61eceab125 | underdog | Chris Godwin | Receptions | under | 0.1476587162709488 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9dcf07e6-d358-4479-aa3a-72b18cb3d208 | underdog | Emeka Egbuka | Receptions | under | 0.147192188115118 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|be3387a7-1752-465d-a92a-5c7b352d46bb | underdog | José Ramírez | Runs | over | 0.1470183818208135 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|c8daf8e0-a220-4bf3-8012-86ff17ec6759 | underdog | Drake London | Receiving Yards | under | 0.1469107209479405 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|89750f74-0504-4bab-9c47-931043edb6ea | underdog | Jordan Love | Rush Yards | under | 0.1465833076874886 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|f6e3d970-b1bc-4a40-8375-c832832a7e6d | underdog | Matthew Golden | Receiving Yards | under | 0.1463499623163882 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|854d1314-7df8-46b5-b6e5-98995ded8435 | underdog | Kyle Pitts | Receptions | under | 0.1462561148496879 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0d657f9f-5cc9-410d-a731-b8f008a04f9a | underdog | Jameis Winston | Pass Attempts | under | 0.1458576148114706 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|da3204f8-50c1-4d25-a7b1-04cabc62f5f9 | underdog | Drake Maye | Pass TDs | under | 0.1445611797481127 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b690ec45-4eb6-4556-a968-04a52d77cb79 | underdog | Jekail Middlebrook | Rush Yards | under | 0.1442512573198966 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|fc83c18b-331a-4c3a-800e-84a83437f162 | underdog | Darren Waller | Receiving Yards | under | 0.1442073115479826 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1edbd709-9e5b-4071-9070-ea2ad5a88144 | underdog | Matthew Stafford | Pass TDs | under | 0.1434007846415811 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|4cd411d0-1d04-4f88-ac50-44f6e4b2371a | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1432605559807707 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|aae23a7b-4d1f-4a0e-a93c-01448b17e9f4 | underdog | Tyler Warren | Receptions | under | 0.1431750538962589 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|4626afd9-b955-49c7-9d7d-784b4abe46a2 | underdog | Cam Little | Kicking Points | under | 0.1428729801196245 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|36f1f660-ed1d-4f1f-b5e8-ea3850ac8a9a | underdog | Malik Nabers | Receptions | under | 0.1426361824714577 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|5ba40722-cb7d-4263-aef5-bb3be75aa8f5 | underdog | Rico Scott | Receiving Yards | under | 0.1413507354201854 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|05ddfd89-449c-44e5-b00c-ff2696a9cf91 | underdog | Brayan Rocchio | Hits | over | 0.1408628071100003 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|e51c7ebf-108e-4509-9e3a-2a684b2bb5f8 | underdog | Mark Andrews | Receiving Yards | under | 0.1406615144072164 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13976081 | prizepicks | Jalen Brunson | Rebounds | over | 0.1400370452709755 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|15723437 | prizepicks | Jake Ferguson | Rec Targets | under | 0.1397834877057258 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|f1764ba0-d7da-47cc-956b-c982d0ec9d66 | underdog | Junior Caminero | RBIs | over | 0.1396495071193866 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|518fd580-fed4-4ea1-86ae-ef539fafae2b | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1395519778414601 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|017e6b0f-06ca-4394-a658-6a69c27baa4f | underdog | Wan'Dale Robinson | Receptions | under | 0.1382017927383453 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|96b8518f-79aa-42c6-aa2c-0f5d6de375ae | underdog | Jo Adell | RBIs | over | 0.1381966221048577 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|08c3d255-a1cf-4a00-9f13-32a35855a1db | underdog | J'Koby Williams | Rush Yards | under | 0.1381093344868171 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e368a210-c3d2-42ae-ad9e-d24d3f8e1835 | underdog | Cam Little | FG Made | under | 0.1379148774693905 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|93af2306-0e1f-48d1-a8b8-f6ef900f4337 | underdog | Drew Mestemaker | Pass Yards | under | 0.1375025085733709 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|53eda10b-bf8c-4c6f-85bc-22a77273c413 | underdog | Brock Purdy | Pass TDs | under | 0.1373225827661014 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|05e73abe-e018-4b06-b159-fd10192323b8 | underdog | Anthony Colandrea | Pass TDs | over | 0.1372035430637996 | 2026-10-14T13:48:29Z | 2026-10-18T03:00:00Z |
| underdog|336272c0-48a1-46c6-b423-233bd0d5dc71 | underdog | Isaiah Likely | Receiving Yards | under | 0.1369634294565795 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|52b183a0-070a-4f73-9931-9fc5664f982b | underdog | Troy Franklin | Receiving Yards | under | 0.1363517857132303 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|2e8b6c23-5daa-4495-8d66-abb23106897c | underdog | C.J. Stroud | Pass TDs | under | 0.1362461611569514 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|c907f46a-2e4e-4dcc-a2b7-541fd6d3d654 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1360626149331018 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|04a42d00-fef3-4785-8749-86d545d780e9 | underdog | MarShawn Lloyd | Receptions | under | 0.1354703699526813 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|0e1dd9cb-4ac6-440c-ab72-589ce1b98411 | underdog | Jayden Daniels | Pass TDs | under | 0.1352637925651718 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|256f9f21-5a05-48e7-97c3-c2fb50ee0eb4 | underdog | CeeDee Lamb | Receiving Yards | under | 0.1351589551748778 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|a66691ae-d152-4253-a077-0c537bcd1542 | underdog | Ryan Fitzgerald | FG Made | under | 0.1350263003861453 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15723411 | prizepicks | Cooper Kupp | Rec Targets | under | 0.1348282274980462 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| underdog|60bfc91e-ff35-409c-ac5c-7efbd9a59044 | underdog | Ryan Barker | FG Made | over | 0.134220881286297 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| prizepicks|15703059 | prizepicks | Arch Manning | Pass Comp | under | 0.1338761387974633 | 2026-10-14T13:48:29Z | 2026-10-17T12:00:00.000-04:00 |
| underdog|7b8c3375-0547-4f2b-b908-a1715fc69a8c | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.1335112990991613 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|ebc26d94-ef8a-4c8e-a07b-95f25400def1 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.1326552834888987 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|edbcc8b0-a15c-455e-9269-b75ae7cf7782 | underdog | Darnell Mooney | Receptions | under | 0.1326182860090983 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e04dda28-f32e-4177-9579-3f9beb321c3d | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.1325910275573866 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|e28679b2-79b4-439a-98e4-5784e0c4a6d5 | underdog | Brandon Aubrey | FG Made | under | 0.1322309173028082 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|7e6a6450-96af-4589-82c2-1dcc59e05d07 | underdog | Emanuel Wilson | Rush + Rec Yards | under | 0.1320152048981795 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|e03e5d9c-a2d2-4c2d-85b0-9a58b94efee3 | underdog | Nick Folk | FG Made | under | 0.1315878843452703 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|cacb937b-5573-451d-b0be-69a2b0b60065 | underdog | Carnell Tate | Receiving Yards | under | 0.1315205412070208 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|98e704c2-ee80-41dd-8696-b926d68199f1 | underdog | Brenton Strange | Receptions | under | 0.1314302019946471 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|06608b98-dae4-4264-9356-49baaa077485 | underdog | Javonte Williams | Receptions | under | 0.131226019827754 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|46c04706-7bfe-411e-acfb-c9914c149cd6 | underdog | Steven Kwan | Runs | over | 0.1311049630173337 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|a4cc36ea-f984-44d6-a14b-c271f39f1bce | underdog | Arthur Gea | Aces | under | 0.1310766336700012 | 2026-10-14T13:48:29Z | 2026-10-15T06:30:00Z |
| underdog|7961b7b0-565d-4d11-ac81-be5fb5be791d | underdog | Kyren Williams | Rush + Rec Yards | under | 0.1306509353670555 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|9349be15-d3c1-4c05-94f7-47a08e4812df | underdog | Isaiah Likely | Receptions | under | 0.1304791959976202 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|15727075 | prizepicks | Nick Folk | FG Made | under | 0.1279848948565908 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15687715 | prizepicks | Juwan Johnson | Rec Yards | under | 0.1278523832775254 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|c3d8d8a1-a24f-402f-bc51-2d80ecc42496 | underdog | Malachi Fields | Receiving Yards | under | 0.1276186276712521 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0aa1856d-3806-4756-b7da-37d6c853b968 | underdog | Shohei Ohtani | RBIs | over | 0.1275987671616699 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|6e75dfba-c511-4e11-8e92-7187de64254f | underdog | Matthew Stafford | Pass Attempts | under | 0.1275798957866172 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|516e9821-b698-4d06-be1f-12c949cbaaba | underdog | Jalen Coker | Receptions | under | 0.127008450964096 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|24b2b78b-bdda-43c4-a6ec-7026899fdb48 | underdog | Nathaniel Lowe | RBIs | over | 0.1267477455117067 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|6c3d3386-5e6d-45ca-bb2d-6b8f9ddb5fe6 | underdog | Darren Waller | Receptions | under | 0.1266185476584086 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|743a8dc2-c923-4c72-9624-65c97b7b56cc | underdog | Brice Turang | Total Bases | over | 0.1264983150620654 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|57409e37-3284-4b6b-a4e6-42c0655c9b27 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1263581750485907 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0bbaebf2-0667-4425-ab37-79d6c27b735d | underdog | Jackson Chourio | Batter Walks | under | 0.1259047531234153 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b4ab111e-ca5e-482e-9ffa-366e17ad7309 | underdog | Chase DeLauter | Total Bases | over | 0.1256159465147949 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|92676318-045f-46e6-90d3-276b410888d6 | underdog | Cooper Pratt | Hits | over | 0.1252516550610468 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|9b07b432-f878-4867-9bfc-acbd60899adb | underdog | Connor Hawkins | XP Made | over | 0.1249892046322839 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|9844b7d9-0b18-4fa0-9398-8074611e1263 | underdog | Shohei Ohtani | Runs | over | 0.1243862520458266 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|19a216e3-7d1e-4d58-904f-1f98b691eeb6 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.1236909515697444 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|16c5ab5d-5fa6-4e0e-881a-06e762364838 | underdog | Julian Sayin | Pass Yards | under | 0.1234500436230191 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|44981899-a000-4af5-b03b-0c7ee9b779ea | underdog | Freddie Freeman | RBIs | over | 0.1231774761186525 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|92b9ee43-245a-4247-afc6-821ff5ac9b01 | underdog | Will Hammond | Pass Yards | under | 0.1230623843251792 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|c7c87939-8b99-4597-9128-d4d6e943fa11 | underdog | Jaylen Waddle | Receptions | under | 0.1228131021422119 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|c309c81f-3a64-49bd-9339-bc721c151b5e | underdog | Anthony Colandrea | Pass Yards | under | 0.1226203306197764 | 2026-10-14T13:48:29Z | 2026-10-18T03:00:00Z |
| underdog|12a4bd26-aea2-4bc5-8bf6-80a2da1391f6 | underdog | Parker Washington | Receptions | under | 0.1226055683366299 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|13f99988-b1cb-4291-a2ee-2c9e4834b2b6 | underdog | Andy Pages | Runs | over | 0.1219985170820737 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15687728 | prizepicks | DK Metcalf | Rec Yards | under | 0.1219425927990364 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|c6771fa7-8a0a-4674-b34a-597d2d5084af | underdog | Chuba Hubbard | Receptions | under | 0.1217008955571709 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|5c9e671c-d68f-47a2-a0db-bd7a2e6279c9 | underdog | Aaron Philo | Pass TDs | over | 0.1215764351993459 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|8bafe031-5466-490b-a3f9-c399570fc58c | underdog | Nick Folk | Kicking Points | under | 0.1209137845939196 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9c3ad746-1376-4173-a364-a01ac7ca9168 | underdog | Lukas Van Ness | Sacks | over | 0.1206696724802429 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|8eefb5ac-bfba-45c2-a04b-9e7fe7769aa1 | underdog | Jeremiyah Love | Rush Yards | under | 0.1204846031042061 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15683890 | prizepicks | Daniel Jones | Rush Yards | under | 0.1202366346625336 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|19d1a9b3-054d-4501-9393-6e4242e60fec | underdog | Jaylen Waddle | Receiving Yards | under | 0.1202317599706011 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|d9c8f99e-6ef8-4f96-86b9-27e52b36715f | underdog | Brad Jackson | Pass Yards | under | 0.1199901901251098 | 2026-10-14T13:48:29Z | 2026-10-16T00:00:00Z |
| underdog|35913607-5ae6-4763-ac56-90f2fce9b135 | underdog | Emanuel Wilson | Rush Yards | under | 0.1198462083358172 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|88fdb9fe-fb46-452b-8413-4837508895dc | underdog | Chris Olave | Receiving Yards | under | 0.1190278151800631 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e22c3eeb-8758-4db7-be02-2f6132883440 | underdog | Jalen Coker | Receiving Yards | under | 0.1189723975464867 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|26dc5c4c-5341-40c5-9861-731625b3ba9e | underdog | Emmett Mosley | Receiving Yards | under | 0.1188221033285921 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|15723423 | prizepicks | Kayshon Boutte | Rec Targets | under | 0.1187858723281723 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|a847ed62-068f-4393-9e56-3425ff9e71b3 | underdog | Taylor Walls | Hits | over | 0.1169100211195373 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723418 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.1168702935957014 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| prizepicks|13976095 | prizepicks | Cade Cunningham | 3PTM | over | 0.1168098507846668 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|f0ac91c9-b841-4439-baa2-adba50f76e7b | underdog | Austin Simmons | Pass Yards | under | 0.1165471146163044 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|f875b22b-4692-42a8-96fa-933154dcc649 | underdog | José Ramírez | RBIs | over | 0.1164356547216586 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|e7951ede-9a81-46ae-b047-1245e22c9633 | underdog | Tyler Bass | FG Made | under | 0.1158854415361276 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|1c840971-411e-4022-acc7-8302fec7df9a | underdog | Blake Craig | FG Made | over | 0.1156848880986118 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|05fea6a6-d269-45d8-823b-99b2e8091434 | underdog | Darian Mensah | Pass Yards | under | 0.1156485223467613 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|97d6db96-7dc9-4de2-8e9e-a855982afbde | underdog | George Holani | Receiving Yards | over | 0.114991831994325 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|3ff18823-b458-472d-9c52-d9994d91813f | underdog | Jason Myers | FG Made | under | 0.1147348113477929 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|7a82cbea-172d-46d6-863e-15a71d88ac13 | underdog | William Contreras | Total Bases | over | 0.1139370078740158 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15723440 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1138970259974462 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|f5a06d10-7bdf-4fbb-bab7-942c3fe0f7df | underdog | Jonathan Aranda | Hits | over | 0.1138414824874567 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|8d7366b0-e582-4a95-90ba-03e0e5874f07 | underdog | Jeremiyah Love | Rush + Rec Yards | under | 0.113447328808652 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|dcb9dec9-59b5-4081-a1ef-95c8b48e91b0 | underdog | Yandy Díaz | Total Bases | over | 0.113339970134395 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|923a9016-3dff-40b2-b5ba-f1989e9adbc1 | underdog | Woody Marks | Receiving Yards | under | 0.1131482734714991 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|68c9a9db-76e2-44f7-b6ef-0f19d7958d55 | underdog | Blake Craig | XP Made | over | 0.1123320613372827 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|0603b0f2-530e-44bc-b5b7-d5c5c3be71dc | underdog | Lotzeir Brooks | Receiving Yards | under | 0.112308795104296 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|adf7e332-c9b1-4355-b2fb-bcc11d483b8a | underdog | Blake Snell | Strikeouts | under | 0.1120458855333597 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|268e3409-919a-4f99-a317-228f55145227 | underdog | Kenny Gainwell | Receiving Yards | under | 0.1119350062186287 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|6b52acc4-b1c9-4763-8379-eb2293fc7f6a | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.1119022634943183 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|1e04d0ba-7760-4f83-b492-09044e097d68 | underdog | Teoscar Hernández | Runs | over | 0.1118462328181143 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|9a80bc3d-09a3-4074-a6c0-45a45290843f | underdog | Puka Nacua | Receptions | under | 0.1117839507567785 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|72130ece-6c2e-4d50-bd93-93f6972a84b9 | underdog | Travis Bazzana | Hits + Runs + RBIs | over | 0.1114610568013791 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|cd6afd8a-1623-4416-9dcf-c4cd4a0abddd | underdog | Mookie Betts | Runs | over | 0.1113040961065279 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15699170 | prizepicks | Drake London | Recs | under | 0.1112022024757409 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|013e401c-2129-4b56-9e6b-b4d6ccc9f2d4 | underdog | Tetairoa McMillan | Receptions | under | 0.1105577370929219 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|613a1ccc-6141-4afa-a997-39dc66fb4586 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.1093807515343165 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|589292fd-e313-4970-be91-21aa1035d9d5 | underdog | Chuba Hubbard | Rush Yards | under | 0.1093312003771705 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|793d65b1-5851-4057-b5ca-162393c8bf21 | underdog | Gianni Spetic | FG Made | over | 0.1091090991032103 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|8e117324-92f0-44bb-a37c-a889ced24a03 | underdog | Mason McKenzie | Pass Yards | under | 0.1089047483111833 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|82010a34-6636-4a18-b29f-0aa88061cc0c | underdog | Marvin Harrison | Receptions | under | 0.1081481642574225 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|626cc581-a1d0-48f9-8da4-843c00b1e028 | underdog | Daniel Jones | Rush Yards | under | 0.1075336467742743 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1f97771f-bdcb-49e4-b1dc-1d50acc9eac4 | underdog | RJ Harvey | Rush Yards | under | 0.1069206313775376 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|94c06aab-1ecb-4659-b369-c5943e9c1e66 | underdog | Patrick Mahomes | Rush Yards | under | 0.1067296472878259 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|a3376319-a8cd-4eed-80f4-697af7d389b7 | underdog | Keenan Allen | Receptions | under | 0.1065901050774998 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|45dd96f6-d811-4c37-ab48-3ee467ff9ea0 | underdog | Rickie Collins | Pass Yards | under | 0.1052964816947082 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|6873b000-4880-4088-9a30-9227274230d3 | underdog | Re'Shaun Sanford | Rush Yards | under | 0.1052054430183153 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|8085b2d7-88db-45e1-bc45-d1d921f6ce43 | underdog | Brian Bonner | Rush Yards | under | 0.1051578722515238 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|7f8534fd-b792-43d8-8d0c-f22b6da185b7 | underdog | Josh Hoover | Pass Yards | under | 0.1049042669094626 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|b873802c-8213-4900-a4c4-db6f3e84a9da | underdog | Kyle Tucker | RBIs | over | 0.1043438024177222 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15683993 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.1041918917578245 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|372d8659-1743-470e-9a40-eb47685d98c8 | underdog | Jonny DeLuca | Total Bases | over | 0.1041280148423005 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|c6f56c35-de96-47f7-85ac-77095ff29557 | underdog | Richie Palacios | Hits | over | 0.1037766872719045 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|e6a80532-7552-46c1-9332-1cb029eb9161 | underdog | Drake London | Receptions | under | 0.103534681513115 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d5fcefcb-dea3-4f94-8bbf-631892597b8b | underdog | Michael Mayer | Receiving Yards | under | 0.1033070471995536 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|71fb1754-1ac0-4faa-8e52-d151f58906d0 | underdog | Gunner Stockton | Pass Yards | under | 0.1032806192142695 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|a4006249-2f9e-41c3-a323-db40372e8b81 | underdog | Shohei Ohtani | Total Bases | over | 0.1032412965186075 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|ca05ca8f-a2c4-494a-a913-d03fcc72752d | underdog | Jmariyae Robinson | Receiving Yards | under | 0.1031870924544966 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|f0408397-d9b4-4af1-8568-80f94223407c | underdog | Mookie Betts | Total Bases | over | 0.1031358885017419 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|ee5a2df0-4ad7-4193-8347-a04f6791f3d5 | underdog | Najee Harris | Receiving Yards | over | 0.1030373186154452 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0af93701-e9c4-411e-be3a-7e99700c097e | underdog | Ryan Fitzgerald | Kicking Points | under | 0.1026614021541227 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|20739d0e-7a3a-46c7-b910-c091e3307377 | underdog | Andrew Vaughn | Hits + Runs + RBIs | over | 0.1026273838663677 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15683896 | prizepicks | Jordan Love | Rush Yards | under | 0.1023572340303807 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|e050b752-9200-4f21-8276-e64203482e59 | underdog | Garrett Mitchell | Batter Walks | under | 0.1021978021978021 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15657531 | prizepicks | Sam Darnold | Pass Attempts | under | 0.1019925659465945 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| underdog|a3bd92bc-1efb-4be9-b775-65f500b7e98d | underdog | Jacory Croskey-Merritt | Receptions | under | 0.1019884569795354 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|a8ca70d0-bf2b-4e4f-8643-6324e6176762 | underdog | Rashid Shaheed | Receptions | under | 0.10182799504344 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|994ee10b-d790-445b-a81a-660ec7aafe38 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.1015962975439155 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|09dec485-a3d7-4f98-9dcc-0efa97ad445f | underdog | Jason Sanders | FG Made | under | 0.1015815221805782 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|8f88a427-e4f3-4800-8f0b-e3f1f13de438 | underdog | Bhayshul Tuten | Receptions | under | 0.1014884388520287 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|1d6aab74-ed30-4651-8fa7-a7e7ed1dd44a | underdog | Ajay Allen | Rush Yards | under | 0.1013729393918837 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|97e8ba44-bff6-4238-8b55-1d605752d517 | underdog | Brice Turang | Hits | over | 0.1011969893492797 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b76b8a9d-b2c1-4e55-a9a9-6468c8b97ae7 | underdog | Victor Mesa | Hits + Runs + RBIs | over | 0.1011744198407369 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0cde4461-ba10-48f2-89ad-ce1b2a2c98cd | underdog | Brayan Rocchio | Runs | over | 0.1004405286343612 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|7cff2371-018e-44fa-b9ea-29b07c3022ba | underdog | Connor Hawkins | FG Made | under | 0.1002703109704536 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|1f0abd98-6a07-4ae2-9af1-33c1fb0e01fe | underdog | Andrew Vaughn | Batter Walks | under | 0.0997986126650258 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|0975c92b-8a41-4605-aaae-d8a153ccabbe | underdog | Liam Hicks | Hits | over | 0.0997801331853979 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|a87e20e4-59f0-4aeb-9ec5-0a256f561a04 | underdog | Garrett Mitchell | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|45704e51-b7a0-44bf-a2c1-03e6a9ba0b76 | underdog | Patrick Bailey | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0770ad9e-355f-49a3-a5be-4d4d294718a0 | underdog | Max Muncy | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|171add43-c76a-4b05-a07a-90eadeeffdcb | underdog | Joey Ortiz | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b542f6d5-9297-426d-b79d-5a1f02c62dd3 | underdog | Luis Lara | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|a4de9b58-1756-408d-9bdb-e8709ad34a8f | underdog | Richie Palacios | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|39e56dea-c76c-4752-8d7e-9e538867985c | underdog | Cooper Pratt | Total Bases | over | 0.0994475138121546 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|a9f5dce0-f16b-413a-87ff-cb2fbbc6a8ac | underdog | Jonathan Aranda | Total Bases | over | 0.0981392557022809 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|bb174e98-5d37-4b4d-bbdf-2d18ed0e014b | underdog | Luis Lara | Batter Walks | under | 0.098022624031353 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15723431 | prizepicks | Parker Washington | Rec Targets | under | 0.0979824115619523 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|44f1d509-98b4-478f-a03f-2dc9e8386e0d | underdog | Junior Caminero | Hits | over | 0.0977059303086785 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|b6950ec7-7122-4177-99fb-f479a06180bb | underdog | Emmett Johnson | Rush Yards | under | 0.0975247443669429 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|1bb486d9-7443-4465-8d08-2506b3b1ce9a | underdog | Cam Coleman | Receiving Yards | under | 0.0966763357195231 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|c59674c5-54e6-4da9-ba4f-b65f38bc849d | underdog | Brandon Aubrey | Kicking Points | under | 0.0965614256298216 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15723438 | prizepicks | Christian Watson | Rec Targets | under | 0.0964687264954906 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|53f17686-bcc3-4f42-a3a4-7704ec674818 | underdog | Cameron Dicker | Kicking Points | under | 0.0961563743035448 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15751147 | prizepicks | Will Hammond | Pass Comp | under | 0.0961304323550477 | 2026-10-14T13:48:29Z | 2026-10-17T15:30:00.000-04:00 |
| underdog|b951aecc-b294-419d-8d1e-59dbebd324f4 | underdog | Sam Leavitt | Pass Yards | under | 0.09608716482195 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|03dbc1f4-cba4-49da-acc8-c6651af56a55 | underdog | Joey Ortiz | Hits | over | 0.0957399905558153 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|580170c6-3734-48d3-a957-9fed50768331 | underdog | Jake Bauers | Hits | over | 0.0957045002708393 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|66e96097-8aa3-41ab-8847-c2d6427208c0 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.0956936640558731 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|cc2af0eb-88ca-433d-825d-5aac29872468 | underdog | Isaiah Sategna | Receiving Yards | under | 0.0954410352057788 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|7e007ebc-8dfe-4606-8cf1-8d1cfd59c9c2 | underdog | Darnell Mooney | Receiving Yards | under | 0.0953848471327593 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|5c6d55d2-6a08-489d-8d06-1748f38d4e0a | underdog | William Contreras | Batter Walks | under | 0.0948979591836733 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|3cf2022a-833c-4943-a736-c78a14245536 | underdog | Teoscar Hernández | Total Bases | over | 0.0948460987831066 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|68e1c86d-4c69-4a96-b44c-1a0473632de9 | underdog | Isaiah Marshall | Pass Yards | under | 0.0948302851253267 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|d84c05e4-84e8-4e3e-9a24-6f90360c72ad | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.0945839353532648 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|09d727cd-6f88-46ae-80e9-1a945eec238b | underdog | Jonathan Taylor | Receiving Yards | under | 0.0943886262641457 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a7a05969-8c2d-4707-b1bb-f0215d453204 | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.0942058564342689 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15687723 | prizepicks | Drake London | Rec Yards | under | 0.0940748748925212 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|7385ba7e-513b-4458-934f-7df7e3d0ffe0 | underdog | Max Muncy | Batter Strikeouts | over | 0.0939744091918004 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|61713538-4726-486f-b764-7ad37f1327bb | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.0932571819253615 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|7771c2ce-75ac-4252-899b-134ad3ceafb0 | underdog | Jeremiyah Love | Receptions | under | 0.0932033136466121 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|b17576c4-e1c2-404f-94f5-1a8d21e70689 | underdog | Victor Mesa | RBIs | over | 0.0930115635997988 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|90d3d553-8a6f-416a-a938-69a505587133 | underdog | Carnell Tate | Receptions | under | 0.0925648120770283 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dd813034-0a62-4f6b-a06d-01d76820fb07 | underdog | Nathaniel Lowe | Hits + Runs + RBIs | over | 0.0924569958907763 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0b0fcbd2-c756-44fa-b59f-547f57d7b1ba | underdog | Deshaun Watson | Pass TDs | under | 0.09205750895952 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|bdb42823-0e98-4d24-b91f-2d2ec93c8d04 | underdog | Dalton Schultz | Receiving Yards | under | 0.0919137773943742 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|1bc76d99-4e01-4cbd-ae9f-3c88279a8341 | underdog | Cam Ward | Rush Yards | under | 0.0917728657142905 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|89bb9b87-2373-4d4b-afbd-36b0d13bf5fb | underdog | Chase DeLauter | RBIs | over | 0.0915923945335709 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|d81e2d1b-8b89-47e7-819c-7a43f87d9c63 | underdog | Tony Pollard | Receptions | under | 0.0915594796591671 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|707ac118-1447-4dd1-b33a-b12b584b1c85 | underdog | Jeremiyah Love | Receiving Yards | under | 0.0913362946056339 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|b04836a3-d0d0-489e-b574-e9fb3efdbe1c | underdog | Kendrick Bourne | Receiving Yards | under | 0.0910802931161529 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|5afe9842-0dce-4dd8-af0f-fe8cb03b92f5 | underdog | Ashton Jeanty | Rush Yards | under | 0.0907831438926858 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|8fe32d62-3c59-4421-ad26-9bf7533924c2 | underdog | Chris Boswell | Kicking Points | under | 0.0900969810523529 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|60f4821d-c16b-46ce-81d1-437dcc8497bd | underdog | Patrick Overmyer | Receiving Yards | under | 0.0895960586869808 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|e4ea7ddf-3222-4f4f-855a-edfd81fd678f | underdog | Javonte Williams | Receiving Yards | under | 0.0890453697711329 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|82bf6f8e-6dfb-4379-8df2-457f64fa58db | underdog | Cam Skattebo | Receptions | under | 0.0890453013136044 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|283e7fbc-01aa-4eae-9e0d-27d72324e645 | underdog | Jaylen Warren | Receptions | under | 0.0888336011639515 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a0d430bd-5d99-4a9a-bcf1-8bbddbc7a15a | underdog | Liam Hicks | Total Bases | over | 0.088821892393321 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|b2b3e245-2c62-48c8-9533-81532527cedd | underdog | AJ Barner | Receptions | under | 0.0887928110147371 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|e7159183-fe24-4d7f-a0b8-c2cfe010a77f | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.0886428805911269 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|22cb5a12-2f04-47b2-b810-3b88a277129c | underdog | Teoscar Hernández | RBIs | over | 0.0884866767219708 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|3890fc60-a33f-488c-b2f1-45256a0db5f4 | underdog | Deuce Bailey | Pass TDs | over | 0.0883464270526802 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|1e05fc5a-cac8-4c37-be92-551a8881aaf1 | underdog | Cooper Kupp | Receiving Yards | under | 0.087922426035973 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|3d68ccfc-edd5-432d-bb18-bfa02b91df95 | underdog | Josh Hoover | Pass TDs | over | 0.0876987421624225 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|3052d8c9-858f-482b-bda3-d3e5de9f3cbc | underdog | Travis Bazzana | Batter Walks | over | 0.087370531239559 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|651cba81-2983-4324-a08d-4c26f0b3cfa5 | underdog | Brock Glenn | Pass TDs | under | 0.0872644025047191 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|8c76e7b9-2277-4230-a565-fab0a90ad846 | underdog | Alejandro Davidovich Fokina | Aces | over | 0.0871703141354152 | 2026-10-14T13:48:29Z | 2026-10-15T06:30:00Z |
| underdog|764fb93b-4e8d-4808-a93f-5c76551a6af2 | underdog | Deuce Alexander | Receiving Yards | under | 0.0870722101076381 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| prizepicks|15724311 | prizepicks | Luther Burden III | Recs | under | 0.0867852920160726 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|d0889bdd-5310-45da-a35f-77f5f73e4f25 | underdog | Deshaun Watson | Rush Yards | under | 0.0866433236945503 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|aefeec99-45f6-44dc-9be1-3cd6bb92828b | underdog | Landyn Locke | Pass Yards | under | 0.0859961512358817 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|92595d84-68cb-4177-9a6b-9ea184ab4be4 | underdog | Will Smith | Total Bases | over | 0.0858391608391608 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|a084944c-2a0e-4d21-8950-f0bd6264b945 | underdog | Will Smith | RBIs | over | 0.0855940549735875 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|14d9ef39-325d-4cee-8dc2-f0199f87a64f | underdog | Mookie Betts | RBIs | over | 0.0855940549735875 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15723425 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.0855089911871084 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|780227d1-544a-4839-9a18-747f71c8eb95 | underdog | Byrum Brown | Pass Yards | under | 0.085087412945824 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|1453e2a3-ccd7-4487-a786-01331c415ed9 | underdog | Bijan Robinson | Rush Yards | under | 0.0847719303932046 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1d5b0a10-2875-43fd-a065-6eb6ab216dd0 | underdog | Kenny Gainwell | Receptions | under | 0.084484967608178 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c8f9081f-cd63-448c-ac1b-f11acf60195b | underdog | Jo Adell | Hits + Runs + RBIs | over | 0.084125590122587 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|b6488efc-5a71-4607-bde9-03dc4c1e68ef | underdog | Robert Gasser | Strikeouts | over | 0.0839505181698491 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15723439 | prizepicks | Matthew Golden | Rec Targets | under | 0.0838509495053801 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|cb276c1d-3b1b-4917-8013-a46238c70ea7 | underdog | Walker Eget | Pass Yards | under | 0.0837827301871376 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|4a25317c-96bc-41ec-bcb4-c96381d32823 | underdog | Andre Szmyt | FG Made | under | 0.0835776067842513 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a0e1f9aa-6484-4678-a350-69e1857b4e6a | underdog | Cooper Kupp | Receptions | under | 0.0834964645793346 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|7e4f2057-2747-4195-89f6-01a2f42dcf4e | underdog | Tyler Allgeier | Rush Yards | under | 0.0832128538830825 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|a2601d4f-a2f1-418c-aab9-0e04d9baabc6 | underdog | Caleb Hawkins | Rush Yards | under | 0.0830982282033241 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|fe3ae261-189b-4da6-adad-f3b48b2e7f29 | underdog | Terrance Carter | Receptions | under | 0.0827538456702415 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| prizepicks|15723415 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.0825025120852771 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| underdog|4465cd71-02f7-4576-90ab-881f658ee6fc | underdog | Luis Lara | RBIs | over | 0.0823529411764705 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|07c1106f-d7b1-409a-8443-a586f438bce0 | underdog | Bijan Robinson | Receiving Yards | under | 0.0821952672016379 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e5d26d68-33a6-4a69-b84a-ff3b69f56947 | underdog | Cooper Pratt | Runs | over | 0.0821917808219178 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|18924a9e-1ff3-469a-892c-098b7bc35a14 | underdog | Andy Pages | Hits + Runs + RBIs | over | 0.0821087900666331 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|0c458582-fcbc-431b-a883-d561d75af6c5 | underdog | Chase McLaughlin | FG Made | under | 0.0820147125331578 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dc78457c-4518-49fa-8c54-f5a9c27bf1f7 | underdog | Liam Hicks | Runs | over | 0.0818181818181819 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|8296e5aa-a4a8-4def-a3a2-8f5855b79f3d | underdog | Alex de Minaur | Aces | under | 0.081658419588682 | 2026-10-14T13:48:29Z | 2026-10-15T10:00:00Z |
| prizepicks|15657706 | prizepicks | Troy Franklin | Recs | under | 0.0814381645566522 | 2026-10-14T13:48:29Z | 2026-10-15T20:15:00.000-04:00 |
| underdog|8bba299f-dc2e-4897-97e1-da8de1700bae | underdog | Brock Glenn | Rush Yards | under | 0.081148938365543 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|55e1e0f0-9290-4c2e-aaf5-8c646a3be01b | underdog | Luis Lara | Hits | over | 0.081000050388639 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|19e1ef15-1f14-4076-986d-b09f0961b3d6 | underdog | Jacory Croskey-Merritt | Rush Yards | under | 0.0808758164599126 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|8905928f-0507-4a0f-9fd3-ad4149ee1b2e | underdog | Ja'Kobi Jackson | Rush Yards | over | 0.0807827172717451 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|f36ac3e3-af65-4960-87e0-b9e4996d5f65 | underdog | Jo Adell | Total Bases | over | 0.0807109557109557 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|2e8cf69b-6539-42ca-a708-16ac6aa37b81 | underdog | Jason Myers | Kicking Points | under | 0.0805408451440432 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|b1967469-2237-401a-ac7e-150836d7039e | underdog | Keelon Russell | Pass Yards | under | 0.0804918979958354 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|ea0634f4-b17f-415b-a84c-e7c513b748d5 | underdog | Chase DeLauter | Hits + Runs + RBIs | over | 0.0803887115851425 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|50b90400-9e6d-4b56-898d-0646639a028b | underdog | Tyjae Spears | Receiving Yards | under | 0.0803376295021978 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|46b610c7-23c6-41d6-8fe3-aabf2107882c | underdog | Bo Jackson | Rush Yards | under | 0.0801372522852813 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|921adb57-1d16-4544-b93b-2a3aafa46572 | underdog | Chandler Simpson | Hits + Runs + RBIs | over | 0.0800450340545976 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723427 | prizepicks | Brenton Strange | Rec Targets | under | 0.0797448193319028 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|35ed8bca-9331-4bd1-b66a-0669b5c33bb5 | underdog | Kyle Tucker | Hits + Runs + RBIs | over | 0.0794800510764113 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|4c5fc106-d748-457e-a0d4-ba887902154d | underdog | Aidan Chiles | Pass Yards | under | 0.0792715794409906 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|15744799 | prizepicks | Anthony Colandrea | Pass Comp | under | 0.0789971146989575 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00.000-04:00 |
| underdog|30218482-4c31-4c16-9395-1f78c114a846 | underdog | Junior Caminero | Total Bases | over | 0.0788133435192259 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|54950af3-8ce5-4dca-8d74-8089dde6a843 | underdog | Charlie Becker | Receiving Yards | under | 0.0786170531121083 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|49429ad5-57c5-4b84-8a7a-91fcf10a52f2 | underdog | Braylon Staley | Receiving Yards | under | 0.0784786580532947 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|7749d140-243f-4a63-b3bb-087f2c645d71 | underdog | Fame Ijeboi | Rush Yards | under | 0.0778620324347132 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|31f1191e-5d1a-48c7-a6e8-64883039208d | underdog | Jalen Hurts | Rush Yards | under | 0.0778486119954576 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dd7e6279-f267-4c18-a48d-b8df2c51f608 | underdog | Josh Allen | Rush Yards | under | 0.0777475753956967 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|c74b3197-a406-4454-99fe-6da596466cac | underdog | Brian Thomas | Receiving Yards | under | 0.0776225769357386 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|de898704-9629-4765-a4d9-6f2fe591aafb | underdog | Dominic Zvada | Kicking Points | under | 0.0771719757591167 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7a58628e-cb6b-473c-8e90-15189762c9b1 | underdog | Daniel Kinney | FG Made | under | 0.0769721323912844 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|b76b1aee-046b-4c56-8b1c-bb23727f50e1 | underdog | Jeremiah Smith | Receiving Yards | under | 0.0767756789783409 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|281b3eb3-0e59-411b-95c6-71d8aea2a476 | underdog | Freddie Freeman | Batter Walks | over | 0.0767509509957485 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|d41f1596-96b2-4ebb-bea6-3f0c64dd4af0 | underdog | Chandler Simpson | RBIs | under | 0.0765765765765765 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|c4d67e0a-889e-41bf-a108-45bc1f992924 | underdog | Gage Hurych | XP Made | under | 0.0762090911046318 | 2026-10-14T13:48:29Z | 2026-10-18T03:00:00Z |
| underdog|24a5aaf5-54a8-4ea7-b748-fe5e56f2e132 | underdog | Travis Bazzana | Runs | over | 0.0759259259259259 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|1d171ffb-43ac-4c17-a9d6-ae1446b71a33 | underdog | Cooper Barkate | Receiving Yards | under | 0.0758977593553755 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| prizepicks|15687736 | prizepicks | Matthew Golden | Rec Yards | under | 0.0757899658036277 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|f7cb8084-ab60-401d-8150-4bd58e4351bc | underdog | Woody Marks | Receptions | under | 0.0756857147176727 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|94a128cd-fa19-466f-bd9f-4aee6d5469e9 | underdog | Garrett Mitchell | Hits | over | 0.0752949523467787 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|79fafca0-392d-4fa7-a05a-e4e132b4938e | underdog | Kenny Gainwell | Rush Yards | under | 0.0752791090544141 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|5f3b9ee5-614e-458a-89e3-3bf130ef8a1e | underdog | Freddie Freeman | Total Bases | over | 0.0748739495798319 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|7898ef01-f5e8-4506-9ab6-1c73a6b94973 | underdog | Ka'imi Fairbairn | FG Made | under | 0.074756436597449 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|2a885006-1e49-43df-b843-5e8e83a46eb5 | underdog | Quinn Henicle | Pass TDs | under | 0.0747430151626611 | 2026-10-14T13:48:29Z | 2026-10-15T23:30:00Z |
| underdog|6fb1b098-5104-48b4-919b-562e0c194fa2 | underdog | Max Muncy | Hits | over | 0.0747173261895777 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b99a8d42-6da3-4779-86c4-d343aaf05adf | underdog | Bucky Irving | Rush + Rec Yards | under | 0.0745857339979372 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|89963e5e-2c19-488b-bace-d7a22faaaad9 | underdog | Billy Edwards Jr. | Pass TDs | over | 0.0744162856537563 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e8269487-686b-410c-b311-21ee42e6994b | underdog | Shohei Ohtani | Hits | over | 0.0742114713698814 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|088c10be-1d02-47b5-98ba-7c03289a6462 | underdog | Alessio Milivojevic | Pass TDs | under | 0.0741913663567804 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|15723429 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.0736296881640543 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|f5976780-3c0b-409f-aee0-1af0221260d7 | underdog | Tyler Higbee | Receptions | under | 0.0735716424142496 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15683884 | prizepicks | Jalen Hurts | Rush Yards | under | 0.0733473851895312 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|45c566bc-182a-4034-a9af-9740dd98680c | underdog | Emanuel Wilson | Receptions | under | 0.0732510967806403 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|b1835bad-503d-4619-b764-812a48b47b69 | underdog | DJ Miller | Receiving Yards | over | 0.073156973958673 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|5c858d75-4b5b-4616-9eb5-cac6c5ebf37c | underdog | Zach Allen | Sacks | over | 0.0729192946027978 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|bc066a1c-6c83-44dd-89ed-e78f53e7980e | underdog | Jahan Dotson | Receiving Yards | under | 0.0723198425457335 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9b2519e8-ccd3-479d-b773-d6f943302711 | underdog | Nathaniel Lowe | Batter Walks | over | 0.0719192559712534 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|f33d7be9-671b-41c0-a592-a25bb6a3abd8 | underdog | Drew Mestemaker | Pass TDs | under | 0.0717605051473828 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|3c9903c8-6fa4-4688-8982-4770c38a8b51 | underdog | Donyell Malen | Shots Attempted | under | 0.071689075953392 | 2026-10-14T13:48:29Z | 2026-10-14T19:00:00Z |
| underdog|ae749070-492e-4741-a6f3-8d500caf406d | underdog | Chandler Simpson | Runs | over | 0.0715722005781073 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|38d77afc-2fed-4601-b8a7-ac8fdc7986d5 | underdog | Andy Pages | Hits | over | 0.0710619176351821 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|a9e67d89-a2a1-491e-949c-84de6089e167 | underdog | Tyjae Spears | Rush + Rec Yards | under | 0.0708529654735127 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|69375ac0-7bc3-4a71-9226-18839bb54abb | underdog | Ryan Browne | Pass Yards | under | 0.070707289506944 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|72087370-822d-44cc-af10-eef1d0b13caa | underdog | Kyren Williams | Receptions | over | 0.0706598600779713 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|101a35c0-8b26-444e-b88e-d87724b37182 | underdog | Jonathan Stafford | Receiving Yards | under | 0.0705959686722552 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15694850 | prizepicks | Jeremiah Smith | Recs | under | 0.0704524795822084 | 2026-10-14T13:48:29Z | 2026-10-17T12:00:00.000-04:00 |
| underdog|2f269a1c-d194-4856-9883-2e5b050d979d | underdog | Aaron Philo | Pass Yards | under | 0.0703977638560622 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|ed29c37c-cb4c-4728-ae93-103da38fb79c | underdog | Zay Flowers | Receiving Yards | under | 0.0693306605284327 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1422b39c-2ad4-4b05-a5fe-c421326e429b | underdog | Dezmen Roebuck | Receiving Yards | under | 0.0692233307050055 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|a07ef610-5e97-4cb1-83b1-fcf2c7e96c39 | underdog | Andy Pages | Total Bases | over | 0.0691104027818023 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|fb840643-e805-4370-9e1c-4c0c42bb744c | underdog | Rashod Bateman | Receiving Yards | under | 0.0690370329438483 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|6893c9c9-87b3-492c-b2c8-cd6780258ed0 | underdog | Bucky Irving | Receptions | over | 0.068856214671551 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|29b94d00-4661-4724-8b52-3df36ca103a6 | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.0684438942264875 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|41a6d7f8-51d6-48ff-8792-da174ded81ce | underdog | Brayan Rocchio | Batter Walks | over | 0.0682449319633434 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723426 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.0682003833538789 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|d2d14f02-e826-4c77-b502-08be54a8cf1e | underdog | Jaylen Warren | Rush Yards | under | 0.0679341120144584 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|ab67acbc-86f1-492e-b6aa-791544443eb8 | underdog | Jayce Brown | Receiving Yards | over | 0.0673066678463174 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|36f4d7f9-6a4d-40ef-9974-811523e2ed46 | underdog | Gunnar Helm | Receptions | under | 0.0671645487138128 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|760351f6-37f2-430b-9730-53ab174f821b | underdog | Alessio Milivojevic | Pass Yards | under | 0.0670591162531071 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|637c5bb7-1a13-4b06-abdd-2dd038c6fd67 | underdog | Savion Hiter | Rush Yards | under | 0.0669247036749257 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|20294e71-6364-45fb-b2e6-7822b3e18860 | underdog | Lloyd Avant | Rush Yards | under | 0.0669061817221016 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|b48fd1b6-3be6-4f2a-bcbf-195e0d9da7b5 | underdog | Paulo Dybala | Shots on Target | under | 0.0667375632044572 | 2026-10-14T13:48:29Z | 2026-10-14T19:00:00Z |
| underdog|d81040e4-cd08-4261-b61b-a067f2996083 | underdog | Jacobo Echeverria Lozano | XP Made | over | 0.066708698528601 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|8f388aa4-4b22-43b4-881b-ec1a98a18e6c | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.0666184003861891 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|43963736-4413-48cb-9fc3-ebef1b798524 | underdog | Dominic Zvada | FG Made | under | 0.066601134278204 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|af0850f2-52aa-4ce8-afb0-078ae125d32c | underdog | William Contreras | Hits | over | 0.0665082402849597 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|d35cd29a-ef46-43a0-ae53-fb6932c28d6b | underdog | John Mateer | Rush Yards | under | 0.0665053649145875 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|c5cddea4-79dc-4e95-be93-230b39c7b228 | underdog | Drake Maye | Rush Yards | under | 0.0664808117781989 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d1aac18d-ebc0-4706-9b60-6f37a92a9c15 | underdog | Lawson Luckie | Receiving Yards | over | 0.0660645411281918 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|2f17fd0d-ad74-43be-aea5-e6900384daf7 | underdog | Tony Pollard | Receiving Yards | under | 0.0660331448301843 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|fe69d5c5-7d36-4646-aba0-f6eb18a8f03f | underdog | Matthias Dunn | XP Made | over | 0.066008632677848 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|0a8fcd1a-9517-43f5-ac76-b336d90b56fb | underdog | Tyler Allgeier | Receptions | under | 0.0659957392088463 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|897036e6-fa64-4395-92b3-98c83466ecd7 | underdog | Beau Pribula | Pass Yards | under | 0.0659780698480565 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|2d2ddf19-4587-4f98-8d37-bd4dacec0a1f | underdog | Travis Bazzana | Hits | over | 0.0655763841424205 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|1b452820-1da8-4232-a402-e376f672ee62 | underdog | Antonio Chadha | XP Made | over | 0.0654532094300855 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|b18b0e56-51f1-4b18-9e07-245cd7e1cdf0 | underdog | Chris Reed | Receiving Yards | under | 0.0653165517865118 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|d74833d9-508a-42d3-9a60-bdc1e59d591f | underdog | Blake Corum | Receptions | under | 0.0650781095642691 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|ae001305-785a-4bad-9962-692d0af34a11 | underdog | Petey Halpin | Total Bases | over | 0.0650406504065038 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|d56582b6-247f-46b6-a1be-65e8abc938f6 | underdog | Joey Ortiz | RBIs | over | 0.0650199203187251 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15687732 | prizepicks | Travis Kelce | Rec Yards | under | 0.0649741061208702 | 2026-10-14T13:48:29Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|aed86e8e-a00a-4c08-a853-b4c1a8f01cc1 | underdog | Kevin Jennings | Pass Yards | under | 0.0647011406177436 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|15683885 | prizepicks | Deshaun Watson | Rush Yards | under | 0.0644770036981225 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|3737448f-da43-44d5-b691-2d6fc42c5568 | underdog | Grady O'Neill | Receiving Yards | under | 0.0643486114513386 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|2b3125b3-390c-4d34-bf54-f49fef21f3f4 | underdog | Steven Kwan | Hits + Runs + RBIs | over | 0.06429475925883 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|2afafaab-b5cf-4131-b20f-90312ffc6faf | underdog | Andrew Vaughn | RBIs | over | 0.064 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b848e002-c499-41be-a1c6-1fbe5f4248ad | underdog | Stone Harrington | FG Made | over | 0.0639136425266995 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e1818f2b-c03c-4fbe-aa2e-f749439133aa | underdog | Blake Corum | Receiving Yards | under | 0.0637542324125917 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|9fa54f3f-df55-47ee-8fc3-7b6962fd15c3 | underdog | Jameis Winston | Rush Yards | over | 0.0629221551802247 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d5e6de3a-f38e-4e3d-869e-ba968eabf4a0 | underdog | Jason Sanders | Kicking Points | under | 0.062918205138056 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a5a67d4e-b990-42ae-81d4-68baab022f8f | underdog | Chandler Simpson | Total Bases | over | 0.0628730163095793 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15687738 | prizepicks | Christian Watson | Rec Yards | under | 0.0621131131326925 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|85ed2ce2-6233-484b-a0b8-7857fabb69bc | underdog | Chandler Simpson | Hits | over | 0.0619797029950358 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|696de9a0-1686-4146-a1ba-7346ef15538a | underdog | Brenton Strange | Receiving Yards | under | 0.0614460641643638 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|79163c1a-7134-4c51-8b72-f4397768542f | underdog | Petey Halpin | RBIs | under | 0.0612745098039215 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|bb697291-4c67-4400-a16e-f4877438ce42 | underdog | Junior Caminero | Batter Walks | over | 0.0612067969020922 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0928f0a2-fa17-4cd5-ac58-67c99af9146d | underdog | José Ramírez | Batter Walks | over | 0.0612067969020922 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|4e2926b8-d144-4ca1-aeab-c11482e91980 | underdog | Kyson Brown | Rush Yards | over | 0.061150798899788 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|df7d066b-53fe-4403-9e3f-539beab7a3bd | underdog | Richie Palacios | Hits + Runs + RBIs | over | 0.0606206270289991 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723436 | prizepicks | George Pickens | Rec Targets | under | 0.0604557293312356 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|c8a42a90-b00e-421f-876a-73995f3283d6 | underdog | Sanfrisco Magee | Receiving Yards | over | 0.0603985425852549 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|7352e62f-2035-4698-89fc-743411c6dd2b | underdog | Byrum Brown | Pass TDs | over | 0.0596722749094441 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|43c68892-0ace-4957-b66c-8fb6ce6bd593 | underdog | Matt Gay | Kicking Points | under | 0.0596411145252263 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|fd7bebc7-feb1-4027-b459-1af6bda9a90f | underdog | Austin Simmons | Pass TDs | over | 0.0589047225785225 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|47115be8-1993-4f93-849e-53017cdfed37 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0587595094818914 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|83fc2d31-9405-4622-9ca7-58c6a551db8b | underdog | Chase Sowell | Receptions | under | 0.0587206997826217 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|3ac93a02-8063-4493-88fb-0e5a9dc33a25 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.0585498679054923 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|f9dacc8b-aace-4e31-8d08-505c9ae8fa61 | underdog | Evan Engram | Receiving Yards | under | 0.0584708199647786 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|7583cc4d-2377-4b1a-9b3c-8f8ca14bffa8 | underdog | Chad Ryland | Kicking Points | under | 0.0584223215423245 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|1d08d753-8352-47b7-8645-d7de0f30a663 | underdog | Will Smith | Hits + Runs + RBIs | over | 0.0579275060492415 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|b6ea11fa-2723-4b7f-a67b-9ee68588aebb | underdog | Gianni Spetic | XP Made | under | 0.0578414646262421 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|49ea4064-f5ff-4773-8eaf-57b52a17a9a3 | underdog | Sam Darnold | Rush Yards | under | 0.0575362558043196 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|9e2c0086-a86e-4d42-968d-7e464f67dc5f | underdog | Jacob Bonilla | FG Made | under | 0.0572437880486553 | 2026-10-14T13:48:29Z | 2026-10-16T00:00:00Z |
| prizepicks|15744364 | prizepicks | Antoine Griezmann | Shots | under | 0.0572123865306346 | 2026-10-14T13:48:29Z | 2026-10-14T19:30:00.000-04:00 |
| underdog|a96e4427-502c-4752-b801-24f2d13547eb | underdog | AJ Barner | Receiving Yards | under | 0.0570413234305303 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|48abaeb9-2330-410d-9ce2-653715251795 | underdog | Deuce Bailey | Pass Yards | under | 0.0570351476171805 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|8622b6b0-dee7-413e-b16a-7645ee2002fa | underdog | Nik Bonitto | Sacks | over | 0.0566568392258264 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|6106096f-26a9-4a32-8ff7-f6c51ef600fd | underdog | Darian Mensah | Pass TDs | under | 0.0566345954538549 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|4ac31a2c-868b-42cd-8487-369a6f2b9168 | underdog | José Ramírez | Hits + Runs + RBIs | over | 0.0565403811879586 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|c4ba5fa1-8f23-4f83-8869-ea1fb92324c4 | underdog | Teoscar Hernández | Batter Walks | under | 0.0565255992897306 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|80421dff-0bb8-4df7-b3d3-fc032ad1fa46 | underdog | Legend Glasker | Receiving Yards | over | 0.0564616955802352 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|192b9c26-829e-4c80-aed8-9de7c5c88347 | underdog | Cutter Boley | Pass TDs | under | 0.0563708956952825 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e51110ff-a3ef-4f2b-bdf5-3f6ea1572d3e | underdog | Trinidad Chambliss | Pass TDs | under | 0.056262173133603 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|a0955c7e-27cf-4e88-b75a-044bf49420dc | underdog | Kyler Kasper | Receptions | under | 0.056242320985134 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|33611c35-750d-4b37-8611-d7419c681f6b | underdog | Davante Adams | Receptions | under | 0.0562005213775146 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|45840fcc-73e3-4a0e-b5d6-289d7e8131ad | underdog | Jaylen Warren | Receiving Yards | over | 0.0555091329077407 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0d81f706-76b1-439b-b237-a7a5e17117af | underdog | Andy Pages | Batter Walks | under | 0.055045871559633 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|9ac8f859-8926-4339-ae10-65d64188a497 | underdog | Kyle Tucker | Batter Walks | over | 0.0548199767711962 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|6ae31d71-13f7-4826-90df-724ae4922593 | underdog | Andrew Vaughn | Hits | over | 0.0547387424022743 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|805b68b1-87f0-4816-a5f1-f51e10d54dbe | underdog | Brayan Rocchio | Hits + Runs + RBIs | over | 0.0546396856523868 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|52cf6a92-8ab9-43c3-b7dc-1e7ab2afeff7 | underdog | Malachi Toney | Receiving Yards | under | 0.0541834505606884 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|990de442-0765-493a-9810-0b565a5db2ca | underdog | Tutu Atwell | Receiving Yards | over | 0.0540903705016898 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|5c32d1cb-8408-4afe-9bb0-e78c207dbed8 | underdog | Tyler Loop | Kicking Points | under | 0.0539584489818791 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|f2046168-9ee8-4e0f-9c4e-9313dd5fcc26 | underdog | Tyler Higbee | Receiving Yards | under | 0.0538566414719516 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|18b7fc64-fae6-4017-8b12-791bf03ef25b | underdog | Yousef Obeid | XP Made | under | 0.0526060666262268 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|c0864956-9ea8-4c34-8246-ff3778a4f6e3 | underdog | RJ Harvey | Rush + Rec Yards | under | 0.0524309831798919 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|af084f2f-bd74-4432-be6c-3d1df297b686 | underdog | Justice Hill | Rush + Rec Yards | under | 0.0523358947727566 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|416b82ff-795f-4d97-8df8-a9664f32525c | underdog | Tyler Shough | Pass TDs | under | 0.0513199434637003 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|36e83b0b-9301-4ead-b81a-ae977dee5ec3 | underdog | Tate Sandell | XP Made | under | 0.0512464871444993 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|3de9b46e-726d-4b41-91d3-9c0adc425468 | underdog | Jackson Chourio | Hits | over | 0.0510151802502132 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|20c0b688-60b9-45c7-ac86-5699e4442e49 | underdog | Najee Harris | Rush + Rec Yards | under | 0.0510017174191684 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a6bd5368-6cfb-4ea0-bbe1-0b489cd0e6dd | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0506786239076874 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1eb44f41-674e-413a-aebd-5a7fbdd980a6 | underdog | Victor Mesa | Hits | over | 0.0504600586476422 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|a934b1e5-68d3-425b-8980-eaf46741f589 | underdog | Jo Adell | Batter Walks | under | 0.0504587155963303 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|36cd5c29-f4fc-4f02-88de-5f03cf37bb01 | underdog | Bucky Irving | Rush Yards | under | 0.0504325997434061 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|4ccbd4db-d288-48b7-b08f-adc5183a3c6c | underdog | Cameron Dicker | FG Made | under | 0.0502901662275662 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|25906cb0-050b-4f5f-a444-14a6436832bd | underdog | Durell Robinson | Rush Yards | under | 0.0501345345843409 | 2026-10-14T13:48:29Z | 2026-10-16T00:00:00Z |
| underdog|7750b77b-fbce-43a1-adc9-beba866b0cdc | underdog | Chase Sowell | Receiving Yards | under | 0.0500155790206331 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|b7593fc7-ea47-4cfa-a3e1-44b58b1a53c8 | underdog | Patrick Bailey | Batter Walks | over | 0.0498251748251747 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|7dcc233f-d5d8-481b-8c15-d8d61edb7ff1 | underdog | Michael Mayer | Receptions | under | 0.0496693096459766 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15683999 | prizepicks | Jeremiyah Love | Rush Yards | under | 0.0494370853019927 | 2026-10-14T13:48:29Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|9a961900-217f-4ed5-b1ad-c866566bc9b9 | underdog | Andre Szmyt | Kicking Points | under | 0.0494295994317495 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|cf79653a-45c4-40f4-83cb-53f9342985f2 | underdog | Walker Eget | Pass TDs | over | 0.0493296574352674 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|5a141853-27e8-4424-9562-2e0253dfe130 | underdog | Conner Weigman | Pass TDs | under | 0.049184338786069 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|d4ddbc0e-9ead-4e0e-9c51-835ee04afad1 | underdog | Najee Harris | Rush Yards | under | 0.0491801716630684 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3eb81c75-b997-495c-aac7-ec7d2f040d27 | underdog | Victor Mesa | Total Bases | over | 0.048942463307104 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|4362a3d8-ecc4-4c7e-a626-3609d02d9698 | underdog | Andrew Marsh | Receiving Yards | under | 0.0486700710097008 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|33dc314c-06a2-4c79-8c89-2fd9a3bc19cf | underdog | Gunner Stockton | Pass TDs | under | 0.0484288861752177 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|eb808d02-92f8-42b6-8401-87af56758f91 | underdog | Davis Allen | Receiving Yards | over | 0.0482671786839454 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|c7083eb8-e0be-43a3-bf9b-884e4d68feca | underdog | Shohei Ohtani | Hits + Runs + RBIs | over | 0.0481607773331995 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|cb6c0e2e-8512-43e9-b7b9-7259afcb74db | underdog | Marvin Mims Jr. | Receptions | under | 0.047592879984083 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|8de12e0a-781e-4a9b-b6a8-83e96bd43f8d | underdog | Yandy Díaz | Batter Walks | under | 0.0475813177648041 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0e1e0693-08a1-45b6-9cbc-c12f1d39f25d | underdog | Cooper Pratt | Batter Walks | under | 0.0475813177648041 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|63d5cda0-6f90-4118-a10e-9dc653b0fa9f | underdog | Tyler Robles | FG Made | under | 0.0475102077117031 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| underdog|cae0440e-b712-43fb-b56e-d8882e7acbc0 | underdog | George Holani | Receptions | under | 0.0474827880586826 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|2f5e3fb3-36f7-4c6f-90e0-ef4717c8a1c3 | underdog | Ryan Wingo | Receiving Yards | under | 0.0472637241811433 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|30f47b7e-1e56-42e2-8775-004df55bb259 | underdog | Rico Dowdle | Receiving Yards | under | 0.0465739350570626 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|07f528aa-1f51-405f-a849-30268e82d0b5 | underdog | Kenneth Walker III | Rush Yards | under | 0.0461590986520688 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|f159812d-547e-401e-a4f4-df4fc9426766 | underdog | George Pickens | Receptions | under | 0.0460692547186782 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|d6975ed3-6220-43a0-ab9b-662420bc2bbb | underdog | Jayvan Boggs | Receiving Yards | over | 0.0459795544258399 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|883c889f-ccca-46dd-951f-c6f778e8c075 | underdog | John Mateer | Pass TDs | over | 0.0458819723720702 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|497e5430-360e-43d4-808d-da9ae6f838e9 | underdog | DeSean Bishop | Rush Yards | under | 0.0454730258435064 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e518467d-e615-4492-90bd-fce375197152 | underdog | Keshaun Singleton | Receiving Yards | under | 0.0454678798877553 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|b1fefa2d-20dd-4201-bb47-5e284257bc92 | underdog | Walker Lyons | Receiving Yards | over | 0.0452414748710237 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|eec2233a-2d98-4e07-a8b9-ca9bee88819c | underdog | Griffin Jax | Strikeouts | under | 0.0449748759293023 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|841df5c3-928f-4d11-aab6-defeaa176c4a | underdog | Bijan Robinson | Receptions | under | 0.0446517709336508 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|5ff1eaeb-bfd7-4997-870b-77690ed70880 | underdog | Jacory Croskey-Merritt | Receiving Yards | over | 0.0444024412346101 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|3067e39a-c165-4495-90f3-ae3a89f02784 | underdog | Jude Bellingham | Shots Attempted | under | 0.0440101089851405 | 2026-10-14T13:48:29Z | 2026-10-14T19:00:00Z |
| underdog|ac0574e7-bbef-4121-8369-57db099bbe3c | underdog | Beau Sparks | Receiving Yards | under | 0.0436721636024071 | 2026-10-14T13:48:29Z | 2026-10-16T00:00:00Z |
| underdog|78874487-c5c9-48b2-a485-663d3026afa6 | underdog | Shohei Ohtani | Batter Walks | over | 0.043560606060606 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|48050135-8671-4987-82ba-b50ab9d2e54f | underdog | Davante Adams | Receiving Yards | under | 0.043510578091841 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|4c2e64dc-1b0e-4764-a4ba-a85643cea6c7 | underdog | Brett Eskildsen | Receiving Yards | under | 0.043473585526443 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|77907612-5380-41a7-9993-cc69068b7945 | underdog | Freddie Freeman | Hits | over | 0.0434506692744413 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|c1ce351c-8f12-4dd0-a555-8c628095ee91 | underdog | Yandy Díaz | Hits | over | 0.0428648126844984 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|b372044e-ddbd-4dea-bd06-022138675b13 | underdog | Paulo Dybala | Shots Attempted | over | 0.0428006795917338 | 2026-10-14T13:48:29Z | 2026-10-14T19:00:00Z |
| underdog|090e4658-63a6-44b4-8998-b6c496e32616 | underdog | Rocco Becht | Pass Yards | under | 0.0427345138693942 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|91ef73ee-52c7-413c-81fb-4499934487a6 | underdog | Darnell Washington | Receiving Yards | under | 0.0421896820002846 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|1ea9f7b8-c951-4d39-907a-245df881d644 | underdog | Jo Adell | Hits | over | 0.042093036685826 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723430 | prizepicks | Josh Cameron | Rec Targets | under | 0.0420460524337077 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|7c24c420-fa0a-4cbe-be72-b445b226b469 | underdog | Landyn Locke | Pass TDs | under | 0.0419102833514907 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|1507c3d0-3df7-4629-a157-1f39742fb89a | underdog | Max Muncy | Batter Walks | under | 0.0416372618207481 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15723432 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.0415547959081805 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|6dfa4a70-dd48-456f-a4ed-f732f6dfaf0f | underdog | Mike Matthews | Receiving Yards | under | 0.041528714018298 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|ec6025b0-afb3-4ae4-9c6c-818a7a10ba97 | underdog | Kyle Tucker | Total Bases | over | 0.0410718792943881 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|29bf6dd9-6cda-41d8-89b8-47a04d8abe03 | underdog | Braylon Staley | Receptions | under | 0.0407780823622626 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|e84ddbf6-4ffb-4cdd-9d68-f591a135ab9d | underdog | Kenny Minchey | Pass TDs | under | 0.0406731513706911 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|ecde2b10-b812-44cd-aa4a-9a63fa241e08 | underdog | Ousmane Kromah | Rush Yards | over | 0.0405451069221252 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| prizepicks|15687735 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0402737822356972 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|9166d8d0-d863-4a2b-a164-282fe63aa175 | underdog | George Holani | Rush + Rec Yards | under | 0.0401697128985846 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|cef85e8d-ef3f-45ab-b64d-01fa87c45c96 | underdog | Trey Butkowski | XP Made | under | 0.0400894528511476 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|3d0a736e-03d9-4418-8ead-177da944ffc2 | underdog | Eli Raridon | Receiving Yards | over | 0.0400417126497323 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|f8c97e4a-6d9a-4a49-9686-8c79e65da1b0 | underdog | Kenneth Walker III | Receptions | under | 0.0397300431017207 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|32a6ecce-524c-4f99-b0c8-e2c21cfa9063 | underdog | Theo Johnson | Receiving Yards | over | 0.0392797891077163 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|410a9c80-22cd-49cd-bb98-cfe35da8c17c | underdog | Lofton Howard | Receiving Yards | over | 0.0391803715472633 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|f122ff64-38ed-4ca8-80d7-c971e9dfd232 | underdog | Julian Sayin | Pass TDs | under | 0.0391752977543867 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|57338cc9-9f17-4205-a875-814d1331bdd3 | underdog | Chad Ryland | FG Made | over | 0.0391548933724004 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|9cee33e1-fa7d-447e-84cd-39a56c64d679 | underdog | Arch Manning | Pass TDs | under | 0.0384736317353318 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|9a8a666f-a772-4783-a639-838fb37554ba | underdog | Antonio Chadha | FG Made | over | 0.0383206493881594 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| prizepicks|15723768 | prizepicks | Patrick Schulte | Goalie Fantasy Score | under | 0.0379222512043401 | 2026-10-14T13:48:29Z | 2026-10-14T19:30:00.000-04:00 |
| underdog|cf314717-673f-4301-99d9-b003b608416d | underdog | Will Hammond | Rush Yards | over | 0.0378121518665017 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|95bdbcb5-344d-402d-bb27-1965139f923d | underdog | Richie Palacios | Batter Walks | over | 0.0376430205949656 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|3a8eff7e-27a7-4704-b7d4-8bd48d95192d | underdog | Jalen Hurts | Pass TDs | over | 0.0375422365530552 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|463eae3f-8e36-4860-8447-224046aff655 | underdog | Steven Kwan | RBIs | under | 0.0374149659863946 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|69fb3ddc-97ba-42e9-840f-00a8cdbba003 | underdog | Stone Harrington | XP Made | under | 0.0374054928804139 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|cdaa24af-1b83-4df9-80f2-1ecfa8b48bb5 | underdog | Davis Allen | Receptions | over | 0.0372542802336087 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|6c5b7b75-0cdb-4b36-a122-c3c2a4256e57 | underdog | Mookie Betts | Hits | under | 0.037246542303756 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|01503e06-b6ba-454c-86cb-0bfea8d7eff0 | underdog | Brian Thomas | Receptions | under | 0.036910613248958 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|7de2a5b6-998a-42e4-b235-a21bf8e06b84 | underdog | Freddie Freeman | Hits + Runs + RBIs | over | 0.0367858120565844 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| prizepicks|15702752 | prizepicks | Byrum Brown | Pass Yards | under | 0.0360298780025989 | 2026-10-14T13:48:29Z | 2026-10-17T15:30:00.000-04:00 |
| underdog|64f7cd21-0938-495e-bd2b-f5444cf9dde1 | underdog | Nathaniel Lowe | Total Bases | over | 0.0359957371624084 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|0f90f52a-afc9-45bb-b8f8-cd3115279f0f | underdog | Trevor Lawrence | Pass TDs | over | 0.035966064711529 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|c12b0b39-6eb1-4357-b953-9ff51cd946b9 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.0357727206142327 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|e2a489e5-e062-4098-a2bb-1e35efc1a643 | underdog | Terrance Carter | Receiving Yards | under | 0.0351835829264646 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|16959164-964b-4e6f-8fe1-55fafb859aa8 | underdog | Nick Marsh | Receiving Yards | under | 0.0351425526773283 | 2026-10-14T13:48:29Z | 2026-10-17T16:00:00Z |
| underdog|0fbe3942-d68d-41e8-b863-89b7c470aa5a | underdog | Steven Kwan | Total Bases | over | 0.0349865651589789 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|5d645dae-73d4-472c-9bd9-d3a0d39de4ac | underdog | Javon Rogers | Receptions | under | 0.0349542394492083 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|2c05402c-d5f9-4027-bbba-456d8f7112ee | underdog | Willie Rodriguez | Receiving Yards | over | 0.0349067434178327 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|1ed94d99-014c-499c-8b97-1e8eff6b3bb4 | underdog | Jonathan Aranda | Batter Walks | over | 0.0347919655667144 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|890ac03e-bd83-41b3-88b4-068e5577a6d9 | underdog | RJ Harvey | Receptions | under | 0.0345271068898794 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| prizepicks|13975911 | prizepicks | Jayson Tatum | Assists | over | 0.0344807325358837 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|1ecd56dd-d414-4af6-af1b-7caa3969b0fa | underdog | Kendrick Bourne | Receptions | under | 0.0335777878673256 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|7fb546f8-9997-4701-bbbf-2281d6bbeed8 | underdog | Taylor Walls | Batter Walks | under | 0.0335044254940791 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15723435 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.0333312105037999 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|628bb7fe-da72-46bd-92d5-7f9cedd1b742 | underdog | Tory Horton | Receptions | under | 0.0332431140805705 | 2026-10-14T13:48:29Z | 2026-10-16T00:15:00Z |
| underdog|d5af2314-a9f1-4691-a77a-cc80c0e7ef71 | underdog | Travis Bazzana | Total Bases | over | 0.0331209831999097 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| prizepicks|15687734 | prizepicks | Javonte Williams | Rec Yards | under | 0.0330651897214345 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|bce9a091-d1be-4486-b7a9-a5aae10cd905 | underdog | Ramone Green | Rush Yards | under | 0.0330444084830745 | 2026-10-14T13:48:29Z | 2026-10-14T23:30:00Z |
| underdog|9cb9cca3-4d41-48a8-8507-db94a4a62ab5 | underdog | Rocco Becht | Pass TDs | under | 0.0325926107787958 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|61c56d34-e189-4fa9-a6ce-7555f0b759dc | underdog | Daylyn Upshaw | Receiving Yards | under | 0.0325878712699763 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| prizepicks|15687724 | prizepicks | Carnell Tate | Rec Yards | under | 0.032181768563304 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|9e462494-c7c6-47ba-a07c-06231c11e16b | underdog | Ryan Browne | Pass TDs | under | 0.0320375516904352 | 2026-10-14T13:48:29Z | 2026-10-17T00:00:00Z |
| prizepicks|15725743 | prizepicks | Alex de Minaur | Break Points Won | over | 0.0319369103257183 | 2026-10-14T13:48:29Z | 2026-10-15T06:00:00.000-04:00 |
| prizepicks|15684003 | prizepicks | Jacory Croskey-Merritt | Rush Yards | under | 0.0318182815166875 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|d4bdd1cc-8b12-4191-9f3b-304cf7c5a2e9 | underdog | Jonathan Aranda | Runs | over | 0.0314066154360173 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|3e1a85eb-9771-4c17-9929-d3a9b1ca9927 | underdog | Alexander Zverev | Aces | under | 0.0313648591358949 | 2026-10-14T13:48:29Z | 2026-10-15T10:00:00Z |
| underdog|e4d6dfd2-e561-44ea-b1c7-3b6f06b5b1dd | underdog | James Cook | Receptions | under | 0.0313267407554888 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|1b0871df-9ee3-4b10-b7c7-8bd37fd1d99c | underdog | Tate Sandell | FG Made | over | 0.0312723582363936 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|14726947-2bc8-412b-9e24-e62add1e24a0 | underdog | Duce Robinson | Receiving Yards | under | 0.0312150878131656 | 2026-10-14T13:48:29Z | 2026-10-17T23:00:00Z |
| underdog|71c918ec-c286-414c-b418-b26df9327d43 | underdog | Bear Bachmeier | Pass Yards | under | 0.031126705036781 | 2026-10-14T13:48:29Z | 2026-10-17T23:30:00Z |
| underdog|8662a61b-52b6-48d9-b983-f630d2d532f3 | underdog | Matt Gay | FG Made | under | 0.0310485582065587 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|89402be3-8729-4dd8-8132-b1561dd26f93 | underdog | Chase DeLauter | Hits | over | 0.0307835132404009 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
| underdog|1f72cf94-0128-4bd1-91f5-1c7b3e53c78f | underdog | JJ Buchanan | Receiving Yards | under | 0.0306630464023602 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|7d570564-b625-4d42-9c3c-b4b815f2e27f | underdog | Kenny Johnson | Receiving Yards | under | 0.0305388066756949 | 2026-10-14T13:48:29Z | 2026-10-17T19:30:00Z |
| underdog|7abd062d-029f-45dd-982b-23c0a1dda6bd | underdog | Calvin Ridley | Receiving Yards | under | 0.0304122734825799 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|281452f3-8b42-4c1b-918a-ef0da74b3e22 | underdog | Joey Ortiz | Batter Walks | over | 0.0303970223325061 | 2026-10-14T13:48:29Z | 2026-10-15T00:00:00Z |
| underdog|26b6d028-3d76-4969-b84b-9dedb8029c38 | underdog | Michael Wilson | Receptions | under | 0.0300666672483528 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|7ee48a58-1ad5-4077-b722-72c3aba5322b | underdog | José Ramírez | Total Bases | over | 0.0300420972062763 | 2026-10-14T13:48:29Z | 2026-10-15T22:00:00Z |
