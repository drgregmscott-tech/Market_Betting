# Pipeline Digest -- 2026-10-12T05:46:30Z

## Run summary
- Ingestion: 11332 rows (PrizePicks OK, Underdog OK)
- Estimation: 11332 rows estimated (from 11332 ingested props)
- CLV logging: 129 newly flagged, 0 newly closed, 308 still open (100824 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|57204767-ffb1-4a3d-8cdf-79b4c49ea29e | underdog | Matthew Stafford | Pass Yards | under | 0.4341741267068928 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|681f75c9-fa4d-4135-af2a-2d88b46207a4 | underdog | Brice Turang | RBIs | over | 0.4275910859568447 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|aa4801ae-3a04-46f7-a9f1-fd562064e6e6 | underdog | Josh Allen | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|63b484b3-7986-4201-9b17-b25c64c13571 | underdog | Josh Allen | Pass Attempts | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|129efc56-6f78-466c-9804-39217dffa69d | underdog | Puka Nacua | Receiving Yards | under | 0.3795480058010654 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|5af199c9-a4ca-480e-9fec-ddee37ffee58 | underdog | Josh Allen | Pass Yards | under | 0.3591836734693877 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|e2207feb-b15f-4ddc-b467-ae4c8d4845bd | underdog | Steven Kwan | Batter Walks | over | 0.3549148099606815 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|d91c6aa1-f274-4f9e-a95a-742cf2c29dc5 | underdog | Matthew Stafford | Completions | under | 0.3348008285125783 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|61513c25-9781-49b6-893f-3bf5a484c95f | underdog | Charles De Ketelaere | Shots Attempted | under | 0.3328299850613506 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|29cdf1f7-a211-4e3a-9cde-995abf60fff2 | underdog | Dawson Knox | Receiving Yards | under | 0.3256410256410256 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|a2f9edff-a721-4577-8938-327d5f7a9f13 | underdog | Brice Turang | Batter Walks | over | 0.3221462747778537 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d4de8820-0d74-43b4-94f6-3c01cf8b078c | underdog | Andy Pages | RBIs | over | 0.3141762452107279 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|5e4c0045-b85d-4f37-80bc-28b653c73f62 | underdog | Colby Parkinson | Receiving Yards | under | 0.304864547661155 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|5d0df89f-50bd-4cba-86c0-3b56f8d932ba | underdog | James Cook | Receiving Yards | under | 0.2856105912025095 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|fe280193-2f7d-47fc-aded-70fb9c741087 | underdog | Puka Nacua | Receptions | under | 0.2756118058538218 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| prizepicks|15651417 | prizepicks | Yasmine Kabbaj | Total Games Won | over | 0.2649406522283639 | 2026-10-12T05:56:17Z | 2026-10-12T08:30:00.000-04:00 |
| underdog|32885dff-5f89-4135-8375-22a3f5f90357 | underdog | Jake Bauers | Batter Walks | over | 0.2632653061224489 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|ba2c57a6-c39a-42e7-8f1a-d2c6191191a8 | underdog | Brice Turang | Runs | over | 0.2595879194119661 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13975919 | prizepicks | Jayson Tatum | Pts+Asts | under | 0.2451279480496665 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975925 | prizepicks | Jayson Tatum | Pts+Rebs | under | 0.2442060163021608 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|a9daa4e2-d391-4a56-8887-122069b1a6f8 | underdog | Felix Correia | Shots Attempted | under | 0.2388358806476083 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|6f0c1e39-29d3-46c0-8430-289f2c2fa827 | underdog | Garrett Mitchell | Runs | over | 0.2355134684264755 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|e5da3412-af8f-4be6-9188-9187bd59a232 | underdog | Jackson Chourio | Runs | over | 0.2280150753768843 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|92464fde-118a-4129-a509-887930284223 | underdog | Kyren Williams | Rush Yards | under | 0.224502888663667 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|e0b41f92-108b-4fbe-bd5a-9c70bdf2dbc9 | underdog | Aaron Donald | Sacks | under | 0.2211009174311926 | 2026-10-10T05:51:08Z | 2026-10-13T00:15:00Z |
| underdog|b6952c2a-aa2a-4576-a8d6-7a3dcaf6d32d | underdog | Kyle Tucker | Runs | over | 0.2190514604551108 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|5e0cba79-d415-4c4c-9be1-b423aa351e04 | underdog | Christian Yelich | Runs | over | 0.2143121239622198 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|251444df-2d2c-419b-8e22-fbf98452bbca | underdog | Jake Bauers | Runs | over | 0.2126646403242149 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|bb4b8567-4220-4a0f-bf04-beed49652447 | underdog | Taylor Walls | Runs | over | 0.2113478061924856 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|e678fca0-b179-4564-8bc6-fb9df7821628 | underdog | Angel Martínez | RBIs | over | 0.210772501771793 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a568dfce-6c1f-4a82-a181-06c27422720e | underdog | Tommy Edman | Runs | over | 0.2101175374100346 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15644267 | prizepicks | Laura Samson | Total Games | over | 0.2081714079033 | 2026-10-11T20:18:47Z | 2026-10-12T05:30:00.000-04:00 |
| underdog|45d4b495-2bc0-4b3a-8516-3ee33aecf6de | underdog | William Contreras | Runs | over | 0.2069889702092567 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d89f2e11-aba0-4fa7-953f-4bd607a20ad7 | underdog | Colby Parkinson | Receptions | under | 0.2028856735476636 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|732227df-c10d-4c19-90ab-4ef27e694aa7 | underdog | Andy Pages | Runs | over | 0.1993861839367457 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|7cb544f8-9d57-4984-9cea-a8f3aa1243a1 | underdog | Brayan Rocchio | RBIs | over | 0.1983322064457966 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|80eb3fa4-07d7-48b0-9f9a-ac288fa7f4c7 | underdog | José Ramírez | Runs | over | 0.1979648473635524 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|b4389246-2c68-4e06-b877-19b0042440a8 | underdog | Jordan Whittington | Receiving Yards | under | 0.1951541850220265 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|97f2c7ae-5b0d-4d86-a1ab-ed8e3e064420 | underdog | Liam Hicks | RBIs | over | 0.1914378826782539 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|da2d150e-22d0-47c6-9a0d-4b750291ae63 | underdog | Deone Walker | Sacks | over | 0.1905113805902615 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15653271 | prizepicks | Jazmin Ortenzi | 1st Set Total Games Won | over | 0.1896103988268541 | 2026-10-12T05:56:17Z | 2026-10-12T09:10:00.000-04:00 |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9bb88636-50b8-486e-907d-8952e4620448 | underdog | William Contreras | RBIs | over | 0.18812178173274 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|e62852f3-55e9-40f9-98c9-c676a687112e | underdog | Jackson Chourio | Total Bases | over | 0.1861822076897056 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13975931 | prizepicks | Jayson Tatum | PRA | under | 0.1859948657142129 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|6142f7c6-020f-48ef-aa6d-5b9db262beea | underdog | Garrett Mitchell | RBIs | over | 0.1842142654163114 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|c23a382f-af00-491d-a9ec-aa3258c7ad61 | underdog | Matthew Stafford | Pass Attempts | under | 0.1838682559925166 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|7966751d-975d-4de5-82cb-b1daea263327 | underdog | Cooper Pratt | RBIs | over | 0.1797742127153891 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|ba4e968c-1cd6-4013-a222-57809f4f8e65 | underdog | Jackson Chourio | RBIs | over | 0.1781703083520522 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|6e8cb313-6410-438c-8e70-8e828904a8dc | underdog | Jake Bauers | RBIs | over | 0.1781703083520522 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15451223 | prizepicks | Puka Nacua | Recs | under | 0.1774909016179514 | 2026-10-07T05:55:02Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|61315832-5e54-41b3-9c8b-23ef31024381 | underdog | Jordan Whittington | Receptions | over | 0.1770609074494917 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|15647015 | prizepicks | Susan Bandecchi | Total Games | over | 0.172667535186655 | 2026-10-11T20:18:47Z | 2026-10-12T09:30:00.000-04:00 |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|6753f894-3cb6-43a6-9381-d4af425e4b9d | underdog | Jake Bauers | Total Bases | over | 0.1704545454545454 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f2d5a157-6b17-48f8-940f-5996d62b0104 | underdog | Brayan Rocchio | Total Bases | over | 0.1704545454545454 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|cae9d7ab-acdf-468b-b4ae-04877217cdc9 | underdog | Steven Kwan | Runs | over | 0.1688665866695755 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|7062900f-1f64-4edd-a211-4475d2439187 | underdog | Christian Yelich | RBIs | over | 0.1683866529067766 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|36afacc2-6921-4af0-a671-a64e783545d0 | underdog | Thorir Johann Helgason | Shots Attempted | under | 0.1671698741728939 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|e227a520-7d58-4602-91e4-351b2f58359f | underdog | Tommy Edman | RBIs | over | 0.164770742902759 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|92f22510-dc51-4fda-8b18-d32036175994 | underdog | Maria Sakkari | Double Faults | under | 0.164647319649402 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|f93169d4-e999-4dfa-b5b9-270247a194af | underdog | Matthew Stafford | Rush Yards | over | 0.163819340859309 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|f4dc9343-78b1-4b04-ae32-800cb3f165c5 | underdog | Tyler Bass | FG Made | under | 0.1627647580839394 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|d7cd9c50-2f79-4ba3-88e2-e27014504fb5 | underdog | Teoscar Hernández | Runs | over | 0.1622362291038639 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|10bb1e15-c31d-4702-b0f8-efb2213f1cb2 | underdog | Travis Bazzana | RBIs | over | 0.1619855149266913 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3e82546c-560d-4165-8703-c3d04194801d | underdog | Khalil Shakir | Receiving Yards | under | 0.1612483808717202 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|c6a6548d-0d18-40f7-8280-696efe97af8c | underdog | Richie Palacios | RBIs | over | 0.1581699346405227 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15599427 | prizepicks | Dawson Knox | Rec Targets | under | 0.1579834600344047 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|26385af5-fb82-4255-95ed-45999963f208 | underdog | Jon Rowe | Shots on Target | under | 0.157344942085266 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|e4bf566a-0258-4c27-a357-98ae0fdea15b | underdog | Mookie Betts | Runs | over | 0.1562432839028584 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|bf244187-83c4-4f70-a237-deac3554d030 | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.1548572777955499 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|0c34ed10-3383-48d9-bdfd-ce42dc1002f2 | underdog | Jonathan Aranda | RBIs | over | 0.1542598967297762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0c91767e-bca8-45d8-a402-6e295fe5e408 | underdog | Travis Bazzana | Batter Walks | over | 0.150470520453236 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a98ec56f-30c1-47cc-9060-a7454a57443e | underdog | Junior Caminero | Total Bases | over | 0.15046792197542 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b468e304-bd8f-4ac2-b864-b58e2ea62a39 | underdog | Nikola Vlasic | Shots Attempted | under | 0.1494699778257078 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9b611f51-bd5a-4ecd-bbfa-f2f13bfc765b | underdog | Khalil Shakir | Receptions | under | 0.1451710376003263 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|e4b2c31f-0dd9-4925-9430-2609f8120f12 | underdog | Nathaniel Lowe | RBIs | over | 0.1420708634330925 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ea65ec86-8f7b-441c-abcd-96c4d2875e7a | underdog | Yandy Díaz | Total Bases | over | 0.1417073170731705 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|7b021b00-586b-4e6d-8c6c-cf45aaca565f | underdog | Kyle Tucker | RBIs | over | 0.1399226357209549 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f7d05b09-cb35-4338-999d-6b80c41e0f20 | underdog | Junior Caminero | Runs | over | 0.1389638909889478 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|a1d9d7c3-f635-4d7e-a68c-cac07a226bbf | underdog | Jo Adell | RBIs | over | 0.1381966221048577 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e2e99232-56d7-436b-ab75-36683e883868 | underdog | Shohei Ohtani | Runs | over | 0.1368143001881605 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f1f8b8ac-c252-4cee-933f-3cfc3ff82aba | underdog | Andy Pages | Total Bases | over | 0.1366505993260247 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|2f5811a7-79e9-49a1-81a0-32f77b4c9c58 | underdog | Tyler Bass | Kicking Points | under | 0.1358158405639887 | 2026-10-11T20:18:47Z | 2026-10-13T00:15:00Z |
| underdog|43a23ae9-1975-4a13-a3c3-cd928190b275 | underdog | Konata Mumpfield | Receiving Yards | over | 0.1355805680356587 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|b912ec7b-2de2-463e-877b-e595fd7094e4 | underdog | Mookie Betts | RBIs | over | 0.1355192146014698 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|dbc513e4-003f-4486-8d5f-694c7cb2dc0a | underdog | Jon Rowe | Shots Attempted | under | 0.1333428069065197 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| prizepicks|15605203 | prizepicks | Colby Parkinson | Recs | under | 0.131247358061172 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|97ba40d3-4a16-43a4-86a3-56b8321e0ce1 | underdog | Josh Allen | Rush Yards | under | 0.1305140998274795 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|b8dcb39a-2ace-4daa-b851-0b89615596c6 | underdog | Liam Hicks | Total Bases | over | 0.1295527714208139 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f426a0da-e685-4536-ad48-93f182cbc7de | underdog | Josh Allen | Pass TDs | under | 0.1285629331990532 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|a1c455e6-5404-463d-99e9-4535b988d0d8 | underdog | Jon Ander Olasagasti | Shots on Target | over | 0.1271010788156282 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|d6619e79-77f1-4e75-8bf2-9c5efaff42bd | underdog | William Contreras | Hits + Runs + RBIs | over | 0.1269762264174635 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|334aa8d6-75f8-4548-af20-c04ce18f95b0 | underdog | Harrison Mevis | FG Made | under | 0.1267568917612062 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|cf582d01-c13e-440a-ade2-f799db46bbd0 | underdog | Harrison Mevis | Kicking Points | under | 0.1254356679868777 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|2eb5b6b8-64a4-43d2-83cd-5b79c40609eb | underdog | Chase DeLauter | Total Bases | over | 0.123544051767048 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|387d8619-4484-46a0-8bbf-45010b00e34e | underdog | José Ramírez | RBIs | over | 0.1231774761186525 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|542507ad-a6bf-41f9-b946-594ecfd6119c | underdog | Will Smith | RBIs | over | 0.1231774761186525 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15599431 | prizepicks | Khalil Shakir | Rec Targets | under | 0.122300899095646 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|068053b2-3914-4433-a173-e9933bc2b739 | underdog | James Cook | Rush + Rec Yards | under | 0.1220958942003876 | 2026-10-08T06:06:51Z | 2026-10-13T00:15:00Z |
| underdog|c01e24f7-4ebe-4609-9fad-5ddd93a634e3 | underdog | Keon Coleman | Receptions | under | 0.1219943369127956 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|87dbd1ea-79e8-4d12-9b4f-de84d044e28a | underdog | Kyren Williams | Rush + Rec Yards | under | 0.121640090863162 | 2026-10-12T05:56:17Z | 2026-10-13T00:15:00Z |
| underdog|ef7e37dc-ae43-40bb-8177-0e1649d397d7 | underdog | José Ramírez | Batter Walks | over | 0.1215879605604566 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|c292f410-6a70-4364-bc4c-579ed29a01e3 | underdog | Freddie Freeman | RBIs | over | 0.1207459995492449 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|1ec6b717-525a-43d0-971e-68aa16ee9029 | underdog | Mookie Betts | Total Bases | over | 0.1205398043828151 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|4c14aa5a-d226-453b-919a-f5a6fda0d66c | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.1204375230897167 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|292a0a47-f488-4918-b554-8e99eef28e0f | underdog | Teoscar Hernández | RBIs | over | 0.1201223751912111 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|150ee01f-99a9-459d-8f9e-fd28dcdb815d | underdog | Shohei Ohtani | RBIs | over | 0.1198031562871203 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|e185b47d-6075-4e87-9eca-6c9878e85433 | underdog | Andy Pages | Hits | over | 0.1167450576223843 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|ced63fde-c41b-4250-8368-fee8741642ac | underdog | Teoscar Hernández | Hits + Runs + RBIs | over | 0.1165936181493897 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|0535d0fb-5048-4c93-a64b-96fd1ef5c355 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.116157619856066 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|21856232-7b31-4ae3-8518-9bb63987f66a | underdog | Brayan Rocchio | Runs | over | 0.1155172413793103 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|6824e594-00ca-4040-b294-69aba1a0dd93 | underdog | Shohei Ohtani | Total Bases | over | 0.1154636622508354 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|4fa5ef51-cb9d-4386-8e3d-1747d9fc7fa7 | underdog | Angel Martínez | Runs | over | 0.1139984713974954 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f43b99b1-c0c6-4a4c-9e75-4c8afbf1a68c | underdog | Jonathan Aranda | Total Bases | over | 0.1139370078740158 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|abe573f9-1d74-4e1d-b04f-aa980d6ae1da | underdog | Jonny DeLuca | RBIs | over | 0.1139244103438475 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a8af04de-0c61-4c6c-a83a-e29721dd7810 | underdog | Tommy Edman | Hits | over | 0.1124634759742845 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|c0bd9a94-cf50-4ce2-b5b3-f9a919d8ec88 | underdog | Yandy Díaz | RBIs | over | 0.111859761320162 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a1fab498-597e-457d-b659-99f39a6e5e66 | underdog | Yandy Díaz | Runs | over | 0.1093899248307651 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|f937065e-19d6-4fe3-8aca-c54e686313c0 | underdog | Brice Turang | Hits | over | 0.1084504100400205 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|fefc2ead-21b3-4a59-9d04-68dc672dfe1b | underdog | Brice Turang | Total Bases | over | 0.108343337334934 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15606273 | prizepicks | Khalil Shakir | Fantasy Score | under | 0.1074900904271655 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|8cadeb44-cf58-4d91-b6a6-6b2acbf4ddec | underdog | Thiago Fernandez | Shots Attempted | under | 0.1074410409229201 | 2026-10-12T05:56:17Z | 2026-10-12T19:00:00Z |
| underdog|4126c657-112a-4f49-9e07-61d3adcdc383 | underdog | Teoscar Hernández | Total Bases | over | 0.1070027688047992 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|18b8cfd8-ce06-494e-b78d-b9227f7a8114 | underdog | Joey Ortiz | RBIs | over | 0.1052112676056337 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|6ef5fd6e-2017-4be4-87d5-2cccaab82a24 | underdog | Brayan Rocchio | Hits | over | 0.105146286744669 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ca34a7cb-9c63-421e-84fc-f0db502e071c | underdog | Shohei Ohtani | Hits | over | 0.1037908886749543 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|2f69a72b-df5e-49b9-9e6d-f9d053b09222 | underdog | Jake Bauers | Hits | over | 0.1037783346607937 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|a5818eff-7f0e-4f10-bf0f-e6300c6f2340 | underdog | Garrett Mitchell | Hits | over | 0.1029310848498122 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|53fd4abb-ae4f-47ff-b7c1-3c881c826e19 | underdog | Freddie Freeman | Hits + Runs + RBIs | over | 0.1024414220981996 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|aefb68f4-d1e5-49d4-8ba7-3be6a77576d4 | underdog | Shohei Ohtani | Hits + Runs + RBIs | over | 0.1014593953722549 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|4c6863d1-8a63-4019-9eb9-170704f07242 | underdog | Jo Adell | Total Bases | over | 0.1012237762237762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|cb7633c9-ce7f-493c-90fe-299fbe2b2a52 | underdog | Travis Bazzana | Runs | over | 0.1004405286343612 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|cf1fda23-5be0-447a-906f-35529dac84c9 | underdog | Freddie Freeman | Total Bases | over | 0.1002585649644474 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|c16a1553-7ce9-41e3-94dd-35dcba1d50e9 | underdog | Dalton Kincaid | Receptions | under | 0.1001322302115007 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|916aa94d-098b-4ae0-a88a-5647ad1d2d61 | underdog | Garrett Mitchell | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|20846463-535a-44db-a7bc-e280b11f258e | underdog | Joey Ortiz | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d0187b1c-1e27-4949-a016-8721838838ce | underdog | Sal Frelick | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f822b77d-65a6-46f0-96eb-c48af6c14047 | underdog | Tommy Edman | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|759ca990-be87-4727-9e5b-6615fd95611c | underdog | Kyle Tucker | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d149922a-7aeb-4f9a-b519-a5c2490f0b89 | underdog | Patrick Bailey | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|39de42da-3baf-4f84-8c94-abb430fded5b | underdog | Max Muncy | Total Bases | over | 0.0994475138121546 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|49403d31-be54-4fe0-9e8a-d308740d099f | underdog | Taylor Walls | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e388107d-71de-4d5c-9c18-12e453e8029a | underdog | James Cook | Receptions | under | 0.0989680426406112 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|3075a7fe-50a7-4514-b1bf-88840b618ca5 | underdog | Yandy Díaz | Batter Walks | under | 0.098022624031353 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|1c507199-ad31-4a9f-b2d0-a1d951a7cea4 | underdog | Cooper Pratt | Runs | over | 0.0977008026069639 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|020e3f8c-5c74-4741-abf7-323b92b10dd3 | underdog | Travis Bazzana | Hits | over | 0.0963112448193084 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|07405cba-3d11-4f03-aeeb-2884c179f9eb | underdog | Victor Mesa | Runs | over | 0.0962432915921288 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|41dc68e8-a99f-47cf-b8b8-54cd633a76ee | underdog | Joey Ortiz | Hits | over | 0.0957374996444639 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|85486ca9-90da-4c1a-be12-ffe17eb113db | underdog | Jo Adell | Hits + Runs + RBIs | over | 0.0949273782322186 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|87ef302d-42f1-40b0-9d37-4672d952a849 | underdog | Alexander Bublik | Aces | under | 0.0935767355563673 | 2026-10-12T05:56:17Z | 2026-10-13T04:00:00Z |
| underdog|b23b81ea-0add-41a6-a95f-ed9936b9996b | underdog | Christian Yelich | Total Bases | over | 0.0931349578256793 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|57e0188c-e77f-4d8c-b702-a44b0a76ac2c | underdog | William Contreras | Total Bases | over | 0.0930372148859544 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d2887c8e-fd22-43ae-a674-3fe85ac2a968 | underdog | Ryan Vilade | RBIs | over | 0.0915923945335709 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9c9f4eaa-8513-45a0-8295-71a2bc91aedc | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.0910560871701171 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15629113 | prizepicks | Bianca Andreescu | Total Games | over | 0.0907422736850894 | 2026-10-11T20:18:47Z | 2026-10-13T04:00:00.000-04:00 |
| underdog|e9f69f58-1beb-4de9-8110-0a3d94dada53 | underdog | Victor Mesa | Total Bases | over | 0.0906717017515668 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|929c28db-7527-447c-8c84-3d41d964b2b8 | underdog | Alexander Zverev | Aces | under | 0.0893003049615314 | 2026-10-12T05:56:17Z | 2026-10-13T04:00:00Z |
| underdog|a860a1b6-0715-45b8-8145-c83eba86cd4a | underdog | Will Smith | Hits + Runs + RBIs | over | 0.0885377837508405 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|c289248d-cfaa-4879-89cf-3c0ba63b1a52 | underdog | Keinan Davis | Shots on Target | under | 0.0877224402576258 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|15658485 | prizepicks | Alexander Bublik | Aces | under | 0.0876664087349696 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00.000-04:00 |
| underdog|04a90fa0-b3af-4119-b9f1-d7460f453a2c | underdog | Rolando Mandragora | Shots Attempted | under | 0.0876597754181294 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|030e07f5-0c1d-43e5-ae3e-8582e298e9fe | underdog | Garrett Mitchell | Batter Walks | over | 0.087370531239559 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f845b7de-39c1-4709-a1e1-eb1c7704397a | underdog | Lazar Samardzic | Shots Attempted | under | 0.086336829755912 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| prizepicks|15599430 | prizepicks | Keon Coleman | Rec Targets | under | 0.0857557047580359 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|ea8cc63e-3fd4-46c0-9148-ec8a1f36d953 | underdog | Chase DeLauter | Batter Walks | over | 0.0856969429422801 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|53836660-bf98-4489-8964-83449efaaf97 | underdog | Yandy Díaz | Hits | over | 0.0854504404924995 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|252aacd5-f393-4a50-b619-1ce9fbc16ce7 | underdog | Richie Palacios | Batter Walks | over | 0.0847613219094246 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| prizepicks|15613937 | prizepicks | Katie Boulter | Total Games Won | over | 0.0846111425773317 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|ee4c9dd3-1799-4903-9b3a-0385e226d021 | underdog | Kyle Tucker | Batter Walks | over | 0.0842572062084258 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15658486 | prizepicks | Alexander Zverev | Aces | under | 0.0833899781401337 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00.000-04:00 |
| underdog|670067ac-6857-476e-b7c5-4e8ba976c43d | underdog | Kyren Williams | Receptions | under | 0.0831238266239099 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|7edf4227-babd-41fb-a4f6-2bc40bd841f0 | underdog | José Ramírez | Hits + Runs + RBIs | over | 0.082199819661831 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|1c73fa45-62d5-4e6c-99d4-2fb4ef24b963 | underdog | Freddie Freeman | Hits | over | 0.0818931273384159 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|cb65e2e2-83c4-4190-ade2-8ba55c28422a | underdog | Steven Kwan | Hits + Runs + RBIs | over | 0.0818522678804714 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3837276a-14f9-432a-8c21-3f37cae690e0 | underdog | Jo Adell | Runs | over | 0.080365296803653 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|4ed9ec5a-9310-4e90-b5c0-dc2a75583081 | underdog | Freddie Freeman | Batter Walks | over | 0.0798583792289536 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|c35f24d0-3456-4f0a-9e67-62ee993e823c | underdog | Foster Griffin | Strikeouts | over | 0.0792385546820282 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|9dee00db-4e18-491a-9f8a-e167881c6c3a | underdog | Tommy Edman | Batter Walks | over | 0.0788395453343906 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|a1071041-1c45-4c7c-8f51-ff223763354c | underdog | Will Smith | Total Bases | over | 0.0786178107606678 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|1ca1212a-2b6b-4a1e-9741-fa06c174f465 | underdog | Kyren Williams | Receiving Yards | over | 0.0780783225296581 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|6b765c38-fd1a-406a-8242-b70bc727a95b | underdog | Jasmine Paolini | Double Faults | under | 0.0773776365818569 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|269c59bc-eda5-455a-b2e3-04fa11e0186d | underdog | Teoscar Hernández | Hits | over | 0.0772911704908337 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|e1cb8a5d-2b65-43f6-b325-a6727f6a7274 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.0761857882288901 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a7fd2b9a-1f05-4cb9-8e44-a4b46486e86b | underdog | Cooper Pratt | Batter Walks | over | 0.0759829415435822 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|8976841a-dcac-43f5-afc7-aff9aa7b05ca | underdog | Dalton Kincaid | Receiving Yards | under | 0.0758028403564352 | 2026-10-08T06:06:51Z | 2026-10-13T00:15:00Z |
| underdog|54c982e8-946c-470f-b968-54f7868e2184 | underdog | Giorgi Kochorashvili | Shots Attempted | under | 0.0754168684946894 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|cc12fa74-c395-469b-8538-c79eb6cf6d55 | underdog | Max Muncy | Batter Walks | under | 0.075177181616592 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|c815d805-fe28-43c5-86b6-0a0f32639ff5 | underdog | Taylor Walls | Batter Walks | over | 0.0749791144527986 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|fafa1873-ee71-4b7a-bd33-ad2b3f8caad1 | underdog | Junior Caminero | RBIs | over | 0.0747467481867769 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|347394ac-81b5-41a9-8fcb-201377429974 | underdog | Bradley Chubb | Sacks | over | 0.0735359375258569 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|8d325026-0a5a-4c85-83cb-c1dca060f0a0 | underdog | Alex de Minaur | Aces | under | 0.0733442048153371 | 2026-10-12T05:56:17Z | 2026-10-13T04:00:00Z |
| underdog|bb1faece-9afd-43bb-94ec-2c9ccc581d8b | underdog | Nathaniel Lowe | Batter Walks | over | 0.0729473684210526 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|eff29eb9-994c-46ec-a64d-ebc9f0025f60 | underdog | Junior Caminero | Hits | over | 0.0729261767542962 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|7b70747b-1bc7-479a-81e5-20d0c997f567 | underdog | Chase DeLauter | Runs | over | 0.0728110599078341 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|f6632558-5732-4290-a167-72d86391d9e9 | underdog | William Contreras | Batter Walks | over | 0.072206466250709 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|663e0017-2f2b-4ffa-a87f-8e633f3d0e51 | underdog | Brayan Rocchio | Batter Walks | over | 0.0721494817239497 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|328fd5df-b812-4adf-aabf-4121767a3610 | underdog | Matthew Stafford | Pass TDs | under | 0.0718820602819038 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|bf5b8b25-d9c6-4b86-9501-7f1430e1b063 | underdog | Travis Bazzana | Total Bases | over | 0.0718093228573808 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0973913c-a8c4-49df-8b3a-eb191dfc204f | underdog | Shohei Ohtani | Batter Walks | over | 0.0716463414634145 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|3d5f0856-c965-4972-b688-c89e0c0e5a42 | underdog | William Contreras | Hits | over | 0.0716084008453451 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|6bb6133b-cc35-4fc1-8762-49af70322fd4 | underdog | Jonathan Aranda | Hits | over | 0.0709511661299276 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|7ec3af10-9a7a-4850-9052-fee5ef243c57 | underdog | Sal Frelick | Batter Walks | over | 0.0698380566801619 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|9bc15cb6-0d58-46e9-94cb-a709b00816e3 | underdog | Liam Hicks | Runs | over | 0.0697674418604651 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|1af97885-a088-40f7-b692-cece11bb1e27 | underdog | Jonny DeLuca | Total Bases | over | 0.0694444444444444 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e0adfb00-4d15-4d74-8a9d-718e0aaafac3 | underdog | Tyler Higbee | Receiving Yards | under | 0.0687363615477286 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|e7e07049-21e8-4b18-ad3b-acc75ddc7862 | underdog | Blake Corum | Receptions | under | 0.0683732979337277 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|f3de133e-8ea6-4df9-94ce-35eeb97a9de5 | underdog | Blake Corum | Rush + Rec Yards | under | 0.0678111698991777 | 2026-10-12T05:56:17Z | 2026-10-13T00:15:00Z |
| underdog|6e4e4760-d8c4-4052-84e1-2c4c36eeae36 | underdog | Liam Hicks | Hits | over | 0.067041942489502 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2cff0f32-2cb4-4106-8fed-a599462d2fb1 | underdog | Jo Adell | Hits | over | 0.0667688645081718 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|13976018 | prizepicks | Shai Gilgeous-Alexander | PRA | under | 0.0657969563767089 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|75596168-01a4-4f6f-81c9-992752bdc9c2 | underdog | Greg Rousseau | Sacks | over | 0.0657344319318249 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|1c7a9e11-996e-4900-acac-dee717505b78 | underdog | Kyle Tucker | Hits | over | 0.0646341505172481 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|0e1c58dd-54a8-40ec-8736-70c0adf39fce | underdog | Mookie Betts | Hits + Runs + RBIs | over | 0.0635245475120903 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|e0817bac-f447-4259-931e-83576508e9fa | underdog | Teoscar Hernández | Batter Walks | over | 0.0625539257981017 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|f8005c7b-8fd2-4fb4-b3e2-0c81fa133c49 | underdog | Ryan Vilade | Hits + Runs + RBIs | over | 0.062386362231787 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b469d046-409e-4aa2-9063-36688f962c6b | underdog | Donna Vekic | Double Faults | under | 0.0623577008705229 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|23331c7d-6803-44fc-8408-70b0001a8635 | underdog | Angel Martínez | Hits | over | 0.0618390564962869 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e958a43a-d936-4bdc-91eb-2f3bc11ebdd9 | underdog | Keon Coleman | Receiving Yards | under | 0.0612866533143504 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|711ad2e3-3689-47a0-8ab5-f98595bc5429 | underdog | Chase DeLauter | RBIs | over | 0.0608891355284251 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|14336df8-3ab4-4dc1-87fb-e7a6bdd008c0 | underdog | Tyler Higbee | Receptions | under | 0.0606378768913719 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|54322013-2be0-4d02-aeb5-0e40d1564158 | underdog | Jackson Chourio | Hits | over | 0.0592188814276049 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|ce8541ca-1777-414c-bd54-b1e6d73ac0c9 | underdog | Richie Palacios | Total Bases | over | 0.0586311872815423 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f14a1938-7b30-4a5e-8104-80da24175f0b | underdog | Ty Johnson | Receiving Yards | over | 0.0580552741488891 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|a7447cc4-be62-401b-8dc6-12e779135453 | underdog | Dawson Knox | Receptions | under | 0.0577342318788118 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15658488 | prizepicks | Alex de Minaur | Aces | under | 0.0576200032054453 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00.000-04:00 |
| prizepicks|15599432 | prizepicks | Ty Johnson | Rec Targets | under | 0.056772117670328 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|96d44c63-4b21-4387-9460-7b2434936ac2 | underdog | Nathaniel Lowe | Total Bases | over | 0.0563003056903272 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|c946be8f-d0f2-4c8b-87bb-31e6f72c8494 | underdog | Cooper Pratt | Hits | over | 0.0560166009370182 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15642500 | prizepicks | Kimberly Birrell | 1st Set Total Games Won | under | 0.0559697284835082 | 2026-10-11T20:18:47Z | 2026-10-12T22:00:00.000-04:00 |
| prizepicks|15651630 | prizepicks | Despina Papamichail | Total Games Won | over | 0.0559560594699254 | 2026-10-12T05:56:17Z | 2026-10-13T04:00:00.000-04:00 |
| underdog|40958690-9df4-48e8-9fe2-35611d6fdcc8 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.055308759244754 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| prizepicks|15642489 | prizepicks | Zizou Bergs | 1st Set Total Games Won | over | 0.0541026738832632 | 2026-10-11T20:18:47Z | 2026-10-12T06:00:00.000-04:00 |
| underdog|efdd9948-3b4a-477a-b59b-403a51a18b72 | underdog | Davante Adams | Receiving Yards | under | 0.0523788305225944 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|36883448-351a-452e-a672-9a43e449fda3 | underdog | Victor Mesa | Hits + Runs + RBIs | over | 0.0522716735646892 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|4f778fae-400b-4a23-81b0-06c0d3b8ec34 | underdog | Felix Correia | Shots on Target | under | 0.0522488691093763 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|b568f488-b37f-4d7b-b0f8-3e8c1bbca8cd | underdog | James Cook | Rush Yards | under | 0.052094586678718 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|b9a4c5de-d36b-424b-b103-060f62140753 | underdog | Blake Corum | Rush Yards | under | 0.0519852201387395 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15591673 | prizepicks | Kyren Williams | Rush TDs | under | 0.051964898491767 | 2026-10-09T06:09:55Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|bdd55feb-7967-47fe-b5b8-d7fbc2c79f9f | underdog | Angel Martínez | Total Bases | over | 0.0512241635583474 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|65885021-1ad6-4f19-aec8-c212fa6d0b41 | underdog | Jackson Chourio | Batter Walks | over | 0.0504663557628247 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|d454eccc-c68c-42bd-9543-0bb105a16865 | underdog | Davante Adams | Receptions | under | 0.0502337858941952 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|b1e0a846-63ea-4ad1-9ad7-096f48f376c7 | underdog | Chase DeLauter | Hits | over | 0.0481342569823664 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b8c7b8fb-790e-42b4-bd45-e84ca3d5af98 | underdog | Konata Mumpfield | Receptions | under | 0.0479771065940467 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|1d16da96-9a43-47fe-baf2-2c8abe4366fd | underdog | Magdalena Frech | Double Faults | under | 0.047745029088223 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|73454e0c-49dc-41e4-9340-87f225f5d79f | underdog | José Ramírez | Hits | over | 0.0476522420101034 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|5ed26ce5-cb2e-4ea9-b6d4-282bd12c3d65 | underdog | Jurgen Ekkelenkamp | Shots on Target | over | 0.0469164885339176 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|d9a449eb-2eef-4db4-99c3-4438da1d2214 | underdog | Will Smith | Batter Walks | over | 0.0466697936210131 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|6553d66c-3dbf-4848-894a-7dfe528bb421 | underdog | Jonathan Aranda | Batter Walks | over | 0.0466697936210131 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|fdda0b75-cd85-4aaa-a4f7-bfb1182afcb1 | underdog | Patrick Bailey | Batter Walks | over | 0.0452182952182951 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|b73054a9-cf67-4ff2-9363-9d57a37918e6 | underdog | Thorir Johann Helgason | Shots on Target | over | 0.0450908781515718 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|2fe7300c-7fa9-487e-a110-ce28118915ee | underdog | Thiago Fernandez | Shots on Target | under | 0.044814987487319 | 2026-10-12T05:56:17Z | 2026-10-12T19:00:00Z |
| prizepicks|15599468 | prizepicks | Jordan Whittington | Rec Targets | under | 0.0433033789668447 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15613038 | prizepicks | Qinwen Zheng | Total Games | over | 0.0432704704006529 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|e95fefee-cd88-4bd5-baf7-28271a93235e | underdog | Victor Mesa | Hits | under | 0.0432698196376072 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|da03cf52-f37c-47dc-8d25-fa7894f9a07a | underdog | Christian Yelich | Batter Walks | over | 0.04321572341937 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|e5fe04d9-3749-40f9-a135-2fb287e6d314 | underdog | Christian Yelich | Hits | over | 0.0422976271042165 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|a5e15d2f-160f-4fd1-a546-1965575330a2 | underdog | Arthur Gea | Aces | over | 0.0422555893990856 | 2026-10-12T05:56:17Z | 2026-10-13T04:00:00Z |
| underdog|dd35f75f-2676-4274-a2c9-3414d11fafce | underdog | Brayan Rocchio | Hits + Runs + RBIs | over | 0.0422326601217262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3342b33f-60eb-4e9d-b2e2-fa56c00c5bfe | underdog | Tommy Edman | Hits + Runs + RBIs | over | 0.0421113273027777 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|13976010 | prizepicks | Shai Gilgeous-Alexander | Pts+Asts | under | 0.0419653653034837 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|41898ef9-e535-43b5-871d-19833739b7b9 | underdog | Will Smith | Hits | over | 0.0416928449584654 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|9df866af-d049-4b37-8f85-ff98164c8f61 | underdog | Drew Rasmussen | Strikeouts | under | 0.0412212547329545 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|2ef616d5-cfe3-4f4f-9210-fa1daea97e1e | underdog | Victor Mesa | RBIs | over | 0.0411510882670219 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6dfb9119-17c4-498d-8918-c08c536b7732 | underdog | Nathaniel Lowe | Hits | over | 0.0411136759865278 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3c000e19-abab-4c2e-8505-1818122bc2eb | underdog | Yoshinobu Yamamoto | Strikeouts | under | 0.0406096804865188 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|15ea2bd2-f92c-4bbb-87a5-8835a0d6fc5b | underdog | Akor Adams | Shots Attempted | over | 0.0404757452208421 | 2026-10-09T06:09:55Z | 2026-10-12T16:30:00Z |
| underdog|5dc8f6db-1efa-467f-bf7b-5cae7ee7b20c | underdog | Byron Young | Sacks | under | 0.0404468577306219 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|8c33bf40-585b-403c-ab64-a7e928c0cea9 | underdog | John Yeboah | Shots Attempted | under | 0.0404014016880587 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|38c9727c-c270-4ad0-b1b0-5a6d4f32db0a | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.0392653945940132 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|828c7dc7-628f-4c97-bea0-cc5659dc1177 | underdog | José Ramírez | Total Bases | under | 0.0390117401660253 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| underdog|c4e10e26-8a23-46f4-bb3e-ce2705278638 | underdog | Max Muncy | Hits | over | 0.0389987196291198 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|bacd7834-5ebd-49b5-9f30-246293086a12 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.0387451286206554 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a064ed1c-48b7-401f-ab1b-7f509ff49b2d | underdog | Travis Bazzana | Hits + Runs + RBIs | over | 0.0384760299179031 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|7cfba528-1e3d-46ff-881e-3b14a2841989 | underdog | Joey Ortiz | Batter Walks | over | 0.0374811463046756 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|6f74877a-8932-4824-b496-80ed746ec3b7 | underdog | Chase DeLauter | Hits + Runs + RBIs | over | 0.0372398714202552 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|55e352ff-542d-48ae-82d1-51e2fbc7bb3e | underdog | Steven Kwan | RBIs | under | 0.0367231638418079 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f5cb8405-576d-4eb2-99aa-534bad82e49d | underdog | Sara Bejlek | Double Faults | under | 0.0349956581607223 | 2026-10-11T20:18:47Z | 2026-10-12T05:20:00Z |
| underdog|2acbd0cb-0017-4698-92af-92d0e60e8d42 | underdog | Junior Caminero | Batter Walks | over | 0.0347919655667144 | 2026-10-12T05:56:17Z | 2026-10-13T00:00:00Z |
| prizepicks|15630425 | prizepicks | Alina Charaeva | Total Games | over | 0.0340188199905898 | 2026-10-11T20:18:47Z | 2026-10-13T04:00:00.000-04:00 |
| underdog|aaa50644-932e-4a93-8719-f01841542d68 | underdog | Andy Pages | Batter Walks | under | 0.0335044254940791 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|1f8e3582-6acf-4060-b207-83ed0c8b6f9b | underdog | Cooper Pratt | Total Bases | over | 0.0331209831999097 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| prizepicks|15638899 | prizepicks | Diana Shnaider | Total Games | over | 0.0330180720108165 | 2026-10-11T20:18:47Z | 2026-10-12T22:00:00.000-04:00 |
| underdog|5719d5a0-c81a-4047-af0b-1deda36ce93c | underdog | Taylor Walls | Hits | over | 0.0329688869050202 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15644266 | prizepicks | Laura Samson | 1st Set Total Games | over | 0.0320166574734205 | 2026-10-11T20:18:47Z | 2026-10-12T05:30:00.000-04:00 |
| prizepicks|15614077 | prizepicks | Cristina Bucsa | 1st Set Total Games Won | under | 0.0318910683523252 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|949ac8d1-5fc5-4a45-9247-752fb61e9465 | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.0314928070568637 | 2026-10-12T05:56:17Z | 2026-10-12T21:00:00Z |
| underdog|1d1906a4-7f37-41af-9e4f-76ba995dcc2c | underdog | Patrick Bailey | Hits | over | 0.0314555918613239 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2b1c6ee3-d12e-43cc-b8c2-418293364af4 | underdog | Ryan Vilade | Total Bases | over | 0.0309195950304287 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|1d6754f5-5f74-4ed6-bbd6-bb9c2955cc8b | underdog | Liam Hicks | Batter Walks | over | 0.0307017543859648 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
| underdog|fd595d33-28a4-45b6-99a8-e3d2e5241180 | underdog | Steven Kwan | Total Bases | over | 0.0301365182854783 | 2026-10-11T20:18:47Z | 2026-10-13T00:00:00Z |
