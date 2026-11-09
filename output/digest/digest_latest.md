# Pipeline Digest -- 2026-11-09T06:04:05Z

## Run summary
- Ingestion: 8059 rows (PrizePicks OK, Underdog OK)
- Estimation: 8059 rows estimated (from 8059 ingested props)
- CLV logging: 23 newly flagged, 0 newly closed, 63 still open (109709 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|6f655839-d390-4b43-8c4f-9e9362052e1a | underdog | Carson Wentz | Pass Yards | under | 0.4 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|47ec053c-388c-4d74-a581-14d22b98c92a | underdog | Carson Wentz | Pass Attempts | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|df8df649-116d-4f79-aac3-9d4b0ddca963 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|c6a46c9c-97e3-41c1-8234-05ef6bd988f7 | underdog | Skyler Bell | Receiving Yards | under | 0.4 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|b28f9a1a-548f-4fb3-8232-ba2907c0d3d4 | underdog | Stefon Diggs | Receiving Yards | under | 0.4 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|9a903d32-e69b-4fa6-8d5f-3e98df85a0cb | underdog | Jayden Daniels | Pass Yards | under | 0.3567068402069584 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|9e14cfdb-3be3-4ec4-a9b0-18a08e517978 | underdog | Skyler Bell | Receptions | under | 0.32591289918005106 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|4fd3a242-cf5f-4eb3-a5db-95f253c0db3a | underdog | Josh Allen | Pass Attempts | under | 0.3201476032121736 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|d1da01d2-8a92-4c9c-86d5-ac8fbf2d66ab | underdog | Antonio Williams | Receiving Yards | under | 0.280908372433627 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|235bc5a6-5ffa-4292-9d05-83cd6c95c397 | underdog | Blake Cashman | Sacks | over | 0.2742574835777045 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|e6e1c7d2-f81f-4ae4-9a22-1cf7bf22151d | underdog | Antonio Williams | Receptions | under | 0.24608099046216125 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|29215f61-fe62-4284-8fc0-a042e9d4c3a1 | underdog | Jayden Daniels | Pass Attempts | under | 0.23347155275467768 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|a8b660fa-3a02-4ffb-8861-1006d51fe9ff | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.19375530348183467 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|6d173119-25d4-4548-83ad-03156b0cf2dd | underdog | Ben Yurosek | Receptions | over | 0.19167896654283034 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|df028c43-0eee-4273-830e-703d5cb09224 | underdog | Rachaad White | Rush Yards | under | 0.19157154630314255 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|abe2db3e-7934-4822-98c4-aea8bdf90d1d | underdog | Eric Wilson | Sacks | over | 0.19031011217644545 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|1e181e12-56a4-4cc4-bde1-a00efbe88740 | underdog | Stefon Diggs | Receptions | under | 0.17719685057933365 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|8d152fc4-c66d-4c70-a95d-b1d825710984 | underdog | Ben Yurosek | Receiving Yards | over | 0.16984442336545214 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|b9338725-50fc-40f4-8453-1eca37fc7ec6 | underdog | Austin Ekeler | Receptions | under | 0.1614508530669193 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|904783cb-04c2-43be-b609-6f5753669449 | underdog | Chig Okonkwo | Receiving Yards | under | 0.1558096055192143 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|dc298725-6b1d-47d4-8dac-3617ff5e42ae | underdog | Jordan Mason | Rush Yards | under | 0.15576327193870432 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|1c160925-5147-43f9-8d8c-223db258773d | underdog | Austin Ekeler | Rush Yards | under | 0.15174900832478166 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|cb8a7959-37d5-4d0e-b9e9-d1149ed712c1 | underdog | Jordan Mason | Rush + Rec Yards | under | 0.1517324211162261 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|36662c72-eeb6-4098-8bda-06fdddb4bea7 | underdog | Jayden Daniels | Pass TDs | under | 0.1470544440824959 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|f5310450-53ab-4b3c-a68a-83436be791d9 | underdog | Rachaad White | Rush + Rec Yards | under | 0.14044566961801475 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|d750f1b4-ebcd-49c0-9b03-97137f1f422f | underdog | Carson Wentz | Rush Yards | under | 0.1396304799819178 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e9e775c1-e65e-481a-8e80-4451df551d94 | underdog | James Cook | Receptions | under | 0.13675024566789118 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|552d6ed3-57fe-4ea3-8bd6-3bcec6e29b71 | underdog | Jordan Addison | Receiving Yards | under | 0.10614115606118668 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|580739db-4e70-415f-9eac-ccb5b17417aa | underdog | Dallas Turner | Sacks | over | 0.10380860711294093 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|0956c551-7636-4e3a-9169-b3769b75c668 | underdog | James Cook | Rush + Rec Yards | under | 0.10280034547108508 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|8ca38ea4-fb7d-450d-93e0-ad698309f00c | underdog | Dawson Knox | Receiving Yards | under | 0.10256010348325972 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|fd5615f6-e4a3-4ac6-9018-5e642c247a0e | underdog | Ed Oliver | Sacks | over | 0.09940819915056864 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|57f73ccb-63b1-451c-bbeb-fbaac3456b03 | underdog | Aaron Jones | Receptions | under | 0.09908473856146005 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|3f23715e-eab4-429e-96e2-2eee189080a2 | underdog | James Cook | Rush Yards | under | 0.09623021274134713 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|fca3da4f-9476-4b17-ad79-8f80aef153b9 | underdog | Elina Svitolina | Double Faults | under | 0.08423149243173988 | 2026-11-05T12:22:13Z | 2026-11-09T21:10:00Z |
| underdog|30991dac-153e-4344-b3ff-ad0dab588a17 | underdog | Khalil Shakir | Receptions | under | 0.08115998065425789 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|4172a2e0-cc73-4a02-8e18-e7b1e77ef4fa | underdog | Chig Okonkwo | Receptions | under | 0.07662959369636402 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| prizepicks|16719174 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.07349799752159802 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|1bc31085-4e77-40d3-8b0f-fb3e585817e6 | underdog | Andrew Van Ginkel | Sacks | under | 0.07086304367418039 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| prizepicks|16644357 | prizepicks | Khalil Shakir | Recs | under | 0.06997285596944036 | 2026-11-09T06:06:04Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16719175 | prizepicks | Jordan Addison | Rec Targets | under | 0.06403524396214921 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| prizepicks|16778054 | prizepicks | Tomas Martin Etcheverry | Total Games | over | 0.06076899465086305 | 2026-11-08T06:01:51Z | 2026-11-09T06:00:00.000-05:00 |
| underdog|8c922767-d6ce-492b-afcc-e30ea1cab602 | underdog | Khalil Shakir | Receiving Yards | under | 0.06036533598113303 | 2026-11-09T06:06:04Z | 2026-11-10T01:15:00Z |
| underdog|8a748e05-956a-4a40-a6dc-c7788188b33f | underdog | Carson Wentz | Pass TDs | under | 0.058336194057320934 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| prizepicks|16718497 | prizepicks | DJ Moore | Rec Targets | under | 0.051713641503083774 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|076c3eea-9331-4033-a108-3edf0279b36a | underdog | Ty Johnson | Receiving Yards | over | 0.048848215340260515 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| prizepicks|16718501 | prizepicks | James Cook III | Rec Targets | under | 0.04803584807788108 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|0ca8ef3d-f95e-42ea-87de-5024356affdc | underdog | Jayden Daniels | Rush Yards | under | 0.04718928584575788 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|e08d4f66-a7e7-4286-8e10-12e06db8fcac | underdog | James Cook | Receiving Yards | over | 0.04487381857719097 | 2026-11-08T15:09:02Z | 2026-11-10T01:15:00Z |
| underdog|f30dd4e7-dacd-455c-8ed4-95be1fa5e74c | underdog | Karolina Muchova | Double Faults | under | 0.044153512874079426 | 2026-11-05T12:22:13Z | 2026-11-09T20:00:00Z |
| underdog|085c90df-5803-45fc-ac14-b28618abec44 | underdog | Aaron Jones | Receiving Yards | over | 0.04183150381663703 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| prizepicks|16764324 | prizepicks | Ty Johnson | Rec Targets | under | 0.03893224664571926 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16763490 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.037410921153935406 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16718503 | prizepicks | Keon Coleman | Rec Targets | under | 0.037191314735347314 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|0bfdaf51-6b45-47cf-841f-e2ef80666205 | underdog | Jalen Redmond | Sacks | under | 0.036716350712867496 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
