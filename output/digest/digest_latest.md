# Pipeline Digest -- 2026-10-11T05:36:30Z

## Run summary
- Ingestion: 37397 rows (PrizePicks OK, Underdog OK)
- Estimation: 37397 rows estimated (from 37397 ingested props)
- CLV logging: 256 newly flagged, 0 newly closed, 1127 still open (100609 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|66d055bd-a74a-4cd8-bfde-f680b481da0c | underdog | Chig Okonkwo | Receptions | under | 0.4909090909090909 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|9962cadb-eae1-49ec-b7e0-4cd9c8188c9e | underdog | Kevin Coleman | Receiving Yards | under | 0.4786802030456853 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|1b46f01b-7fda-4def-a3f5-87454bb59d9e | underdog | Jason Myers | FG Made | under | 0.4629061757595768 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|14c518a5-830f-497e-a48a-dc7e1644ea6d | underdog | Trevor Lawrence | Pass Yards | under | 0.4561224489795918 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|0d9601e6-1644-4608-bf51-06f2a5b98214 | underdog | Brice Turang | RBIs | over | 0.4447860962566845 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|97ecc7e0-8001-4a00-a537-1e86508a2ce7 | underdog | Jared Goff | Pass Yards | under | 0.4424089119535177 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|d6e84092-11ab-4ea2-812d-e1e6a9555d0c | underdog | Trevor Lawrence | Completions | under | 0.4408163265306123 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|354947f9-082d-4d72-a3a2-8ef8abd57f38 | underdog | Aaron Rodgers | Pass Yards | under | 0.4404040404040404 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|1459ae2d-1d7c-4846-ac12-dde89713b927 | underdog | Aaron Rodgers | Completions | under | 0.4357142857142857 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|093667ee-9e39-43e1-8fce-68d03039aaef | underdog | Michael Penix | Pass Attempts | under | 0.4357142857142857 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|1e457aef-3642-47e4-bfcf-70a4f2b610d7 | underdog | Brock Purdy | Completions | under | 0.4357142857142857 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|57204767-ffb1-4a3d-8cdf-79b4c49ea29e | underdog | Matthew Stafford | Pass Yards | under | 0.4341741267068928 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|7657b6f3-eace-44f3-84cb-c0e338e5ac2b | underdog | Chig Okonkwo | Receiving Yards | under | 0.4276381909547738 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|72806696-493f-4dcb-98fd-4d0a0e3d13b4 | underdog | Jameis Winston | Completions | under | 0.4276381909547738 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|3ca6c353-3187-43ab-8369-5b9b4221c250 | underdog | J.K. Dobbins | Rush Yards | under | 0.4121951219512195 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|982f1ebe-df86-4536-a3ae-38d22b4f218f | underdog | Brock Bowers | Receiving Yards | under | 0.4115489262354732 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|aab4f50a-d6b3-49ab-a3c7-22f4b485d6b2 | underdog | Daniel Jones | Completions | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|2bd0ed1c-f0c0-484d-a419-473307f8a034 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|74963368-2c3e-41cb-a7c4-367ca3ff4b37 | underdog | Deshaun Watson | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|c6205726-5a42-4700-9caa-4a2753eea2e8 | underdog | Drake Maye | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|1e4bf0bf-34af-4b90-9e5d-eac8eebfd51e | underdog | Deshaun Watson | Pass Attempts | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|36b49990-f877-49de-abf8-2c0285ed40d2 | underdog | Drake Maye | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|c89bae0c-c281-4f25-beec-ca031480bf48 | underdog | Deshaun Watson | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|81b209ad-99d4-4dda-b8a4-88b034069992 | underdog | Nico Collins | Receptions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|4dd5f0c6-da42-406b-8607-ad18d5a179b5 | underdog | Jared Goff | Completions | under | 0.4 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|bfed269f-b74a-4594-b799-5f2f3fa699ad | underdog | Jayden Daniels | Completions | under | 0.4 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|7b8274c8-f3e6-4448-bbf1-f57a7eb2c9e0 | underdog | Aaron Rodgers | Pass Attempts | under | 0.4 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|811b5d19-4fab-4da7-afef-4576cde820e4 | underdog | Jacory Croskey-Merritt | Rush + Rec Yards | under | 0.4 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|891c78b5-30be-4139-aab0-7f26bddeaea7 | underdog | Chase Brown | Rush + Rec Yards | under | 0.4 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|8e423da7-f095-4692-aff5-784832b7f839 | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|b22ffd17-ba14-48b7-a938-568896cf1cbb | underdog | Brock Purdy | Rush Yards | under | 0.4 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|ce544108-4672-4cb1-b863-56fdeb957fce | underdog | Cam Ward | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|765047d3-6006-47ea-9a2c-b5572dc4e6be | underdog | Michael Penix | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|aa4801ae-3a04-46f7-a9f1-fd562064e6e6 | underdog | Josh Allen | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|63b484b3-7986-4201-9b17-b25c64c13571 | underdog | Josh Allen | Pass Attempts | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|7fbc50e2-3ee4-414a-9142-3032c4686484 | underdog | Will Shipley | Rush + Rec Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|61980b61-14ee-4445-90e5-67b838e9491e | underdog | Tyler Shough | Completions | under | 0.4 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|0e0b4e01-5671-4f4a-81ea-9c9449dc5774 | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|4c858346-3630-43ff-90c7-cc61389bcdf3 | underdog | Braelon Allen | Receiving Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|78acab0b-0150-4103-ac39-30d8cb9f164f | underdog | Jameis Winston | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|6370e178-d935-4d02-a3b1-db1b5b18d54c | underdog | Justin Herbert | Completions | under | 0.4 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|01169487-2067-4c9c-8382-f09a0610cfe6 | underdog | Jayden Daniels | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|f13c3168-2ee9-4b08-b6cd-eeaefdb5f0d7 | underdog | Bo Nix | Pass Yards | under | 0.4 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|ea5e46b5-a349-4c51-a52f-972d0bdf3223 | underdog | Bo Nix | Completions | under | 0.4 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|d41f0cf3-e63a-4ecd-9b93-99de0b5f9495 | underdog | Jonathan Taylor | Rush Yards | under | 0.4 | 2026-10-05T05:31:46Z | 2026-10-11T17:00:00Z |
| underdog|ef85da58-ec95-46e4-94db-770a62fce90f | underdog | Jameis Winston | Pass Attempts | under | 0.4 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|0fbfe1f0-c6f9-4702-aee6-b0276f4107d1 | underdog | Christian McCaffrey | Receptions | under | 0.3988102626733253 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|9e739adf-45fc-46be-96ce-5d0b10f137cb | underdog | Woody Marks | Rush + Rec Yards | under | 0.3968694107302759 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|0edd7261-c069-4bd9-bdab-9cf4d9dfa357 | underdog | Jaylen Wright | Rush Yards | under | 0.3941515298402422 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|b8c471fa-f730-492c-aaff-de71f7ad6540 | underdog | Jason Myers | Kicking Points | under | 0.3937789558660911 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|1de2a922-5489-4eb3-9be5-76a184e8a221 | underdog | Kirk Cousins | Pass Yards | under | 0.3928887526107247 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|af8eda16-8a19-4b4a-8e68-99a74f97ca13 | underdog | Daniel Jones | Pass Attempts | under | 0.3901960784313726 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|fd75d910-d6c3-4948-b77d-60ff2a2cb9fd | underdog | Geno Smith | Pass Yards | under | 0.384052347154186 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|1cff7e88-0c83-4353-8686-1f2823de25ac | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.3829669446339478 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|e75712ca-d691-41d6-9c34-08a77c337ec0 | underdog | Jalen Hurts | Pass Attempts | under | 0.3828969564884831 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|77559fb6-664e-4365-94cc-b1f4ab559a9f | underdog | C.J. Stroud | Completions | under | 0.3811649383428178 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|75ffaa8f-a70d-4e0d-9a55-19504267e393 | underdog | Jalen Hurts | Completions | under | 0.3806126747967909 | 2026-10-08T06:06:51Z | 2026-10-11T13:30:00Z |
| underdog|129efc56-6f78-466c-9804-39217dffa69d | underdog | Puka Nacua | Receiving Yards | under | 0.3795480058010654 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|09772d8b-730f-4697-96b6-0defe654d14f | underdog | Kirk Cousins | Completions | under | 0.3773869346733668 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|18afe87a-d024-4e7d-b42b-fa6a5d9a5dbc | underdog | Drew Stevens | FG Made | under | 0.3769907560114856 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|befc81f0-b21a-4405-9e36-1e02f3fb2f77 | underdog | Nick Folk | FG Made | under | 0.3745514871135351 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|ed60716c-ada0-445c-97b1-6df0dea0a03e | underdog | Justin Jefferson | Receiving Yards | under | 0.3742231457581579 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|7267df05-15fd-4ce0-b601-edd2bb5a183d | underdog | Justin Herbert | Pass Attempts | under | 0.3723618090452261 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|871ea002-cb1d-4d37-9a67-b9ccd719e037 | underdog | Brock Purdy | Pass Attempts | under | 0.3723618090452261 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|e81a3eae-d106-4a85-b37e-a39ef18b066b | underdog | Bo Nix | Rush Yards | under | 0.3707111012606017 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|8ed6a26c-c080-45cf-b0ef-5e4159d38a36 | underdog | Andy Borregales | Kicking Points | under | 0.3680515865443136 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|2236079c-c073-47f6-86ca-5a7396a36a99 | underdog | Bo Nix | Pass Attempts | under | 0.3668505795814127 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|70711919-a87f-4a24-a741-217c48efb11f | underdog | Juwan Johnson | Receiving Yards | under | 0.3654552868264906 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e722cedf-b6ad-44b5-8a63-faada1e2ce91 | underdog | Trevor Lawrence | Pass Attempts | under | 0.3642857142857143 | 2026-10-08T06:06:51Z | 2026-10-11T13:30:00Z |
| underdog|fffbf28b-f8be-416d-af58-265c73ccbd0b | underdog | Jacoby Brissett | Pass Yards | under | 0.3642857142857143 | 2026-10-10T05:51:08Z | 2026-10-11T20:25:00Z |
| underdog|2eaf2435-4e22-4ba7-a5d2-6457f5b15eb3 | underdog | Trey McBride | Receiving Yards | under | 0.3598365116849146 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|e653d5c9-203f-4464-8d0f-58ba0e15da67 | underdog | Michael Penix | Pass Yards | under | 0.3595959595959597 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|5af199c9-a4ca-480e-9fec-ddee37ffee58 | underdog | Josh Allen | Pass Yards | under | 0.3591836734693877 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|78d1479f-c423-4f3b-85fd-1b6194096252 | underdog | Malik Washington | Receptions | under | 0.3582056634442441 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|39265d24-cd13-473b-a4a6-eed91b5e1bb4 | underdog | Tyler Warren | Receiving Yards | under | 0.3581197447396478 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|1f7cba0c-eaba-4b99-8c40-4026f86b98b6 | underdog | Braelon Allen | Rush Yards | under | 0.3545363228270375 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|dc78415d-6eab-46cc-9769-890623ddfda5 | underdog | Malik Willis | Completions | under | 0.3540816326530612 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|4891f2d2-5f08-4d3b-b4c0-86feff92b89a | underdog | Jordan Love | Completions | under | 0.3540816326530612 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|7236a285-d3af-4be9-9b99-5cd71b5df37a | underdog | Tyler Shough | Pass Yards | under | 0.3533090780788326 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|5f8d0733-bc5b-44fc-84f3-ff2405474cbc | underdog | Brice Turang | Batter Walks | over | 0.3532467532467532 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|a37c2c84-6bd0-4807-a3a7-6bbccf7d9d90 | underdog | Steven Kwan | Batter Walks | over | 0.3517938682322243 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|75174370-c9a6-46d6-be9e-bebc772e32d3 | underdog | Bhayshul Tuten | Rush Yards | under | 0.3517766497461929 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| prizepicks|15622903 | prizepicks | Chig Okonkwo | Recs | under | 0.3509424650567749 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15494685 | prizepicks | Trey McBride | Recs | under | 0.3509424650567749 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15449663 | prizepicks | Jameis Winston | Pass Yards | under | 0.3509424650567749 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15449669 | prizepicks | Justin Herbert | Pass Yards | under | 0.3509424650567749 | 2026-10-07T05:55:02Z | 2026-10-11T16:05:00.000-04:00 |
| prizepicks|15449667 | prizepicks | Daniel Jones | Pass Yards | under | 0.3509424650567749 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15449673 | prizepicks | Jacoby Brissett | Pass Yards | under | 0.3509424650567749 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15435321 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.3509424650567749 | 2026-10-05T05:31:46Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15533050 | prizepicks | Trey McBride | Rec Targets | under | 0.3509424650567749 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15533347 | prizepicks | Pat Freiermuth | Rec Targets | under | 0.3509424650567749 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15604861 | prizepicks | Dontayvion Wicks | Rec Targets | under | 0.3509424650567749 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| prizepicks|15533221 | prizepicks | Nico Collins | Rec Targets | under | 0.3509424650567749 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15622905 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.3509424650567749 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15576376 | prizepicks | Tyson Bagent | Pass+Rush+Rec TDs | under | 0.3509424650567749 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15533331 | prizepicks | Brock Bowers | Rec Targets | under | 0.3509424650567749 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|b1eb26f6-d949-4e06-a647-5bb961166b7b | underdog | Braelon Allen | Rush + Rec Yards | under | 0.3502304315790387 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|794cd9f8-740d-4b99-ae34-09f1333f419e | underdog | Elye Wahi | Shots Attempted | under | 0.3474495889796638 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|8e85ed6b-9d7c-470e-b5d7-23ab7e045154 | underdog | Malik Washington | Receiving Yards | under | 0.3467005076142132 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|1f14707b-275b-4f43-9374-74717b39b040 | underdog | Michael Penix | Pass TDs | under | 0.3467005076142132 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|f8e036c4-b34d-4cd8-ac8b-9931139a0af5 | underdog | Nico Collins | Receiving Yards | under | 0.3446688170419643 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|a2fd2eb1-4913-46c7-b2ee-fbff43564395 | underdog | Jacoby Brissett | Completions | under | 0.3443720287564475 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|003e5e7b-bc55-475b-8325-d7212da89c02 | underdog | Tyson Bagent | Pass TDs | under | 0.3438775510204083 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|f5ccd5e8-d720-4ed5-b69c-b02f9d0d982f | underdog | Malik Willis | Pass Yards | under | 0.3438775510204083 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|204fd473-93dd-4a88-9fab-efe827b1bfdf | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.3419712220286377 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|9ce47f78-dded-4053-9149-85d4529492b6 | underdog | Tyson Bagent | Rush Yards | under | 0.341025641025641 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|be2ba4ef-06ce-4691-a433-25d0728ce043 | underdog | Drake Maye | Pass Attempts | under | 0.340132019522017 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|ab62192f-cec6-40f0-b0c1-3aac63435f7d | underdog | Andy Pages | RBIs | over | 0.3353389490573606 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|d91c6aa1-f274-4f9e-a95a-742cf2c29dc5 | underdog | Matthew Stafford | Completions | under | 0.3348008285125783 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|4d01d7b4-3aac-4a2e-94d9-50396b6c6223 | underdog | Luther Burden | Receiving Yards | under | 0.3344123464627682 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15599458 | prizepicks | Will Shipley | Rec Targets | under | 0.3343839542105346 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|a0f6fa92-1f73-45c8-8876-d7614459cf88 | underdog | Riley Patterson | Kicking Points | under | 0.3341957702340512 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449657 | prizepicks | Malik Willis | Pass Yards | under | 0.3333701694639619 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|031c7243-279e-45cc-ae69-6ffa71635551 | underdog | Cam Ward | Pass Attempts | under | 0.3331905431004385 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|61513c25-9781-49b6-893f-3bf5a484c95f | underdog | Charles De Ketelaere | Shots Attempted | under | 0.3328299850613506 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|4880455a-4647-452f-830b-51975778b833 | underdog | Makai Lemon | Receptions | under | 0.331891245319532 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|842d48e4-d9bb-4477-9ee5-98bfe85808b6 | underdog | Daniel Jones | Pass Yards | under | 0.3314720812182742 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|1102dd43-5768-477d-8143-dc351d834b6a | underdog | Jalen Hurts | Pass Yards | under | 0.3314720812182742 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| prizepicks|15449888 | prizepicks | Brock Bowers | Rec Yards | under | 0.329740166255388 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|e9d48e21-937e-4fe2-8a44-0e3d9cc9a8c7 | underdog | Jake Bauers | Batter Walks | over | 0.3270889487870619 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|2ae0f7e5-4ff3-44a9-9836-40696d8b1442 | underdog | Tyler Loop | FG Made | under | 0.3263281368597279 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|7a04d189-80e3-41cb-8e01-a282c01fdeaa | underdog | Cam Ward | Pass Yards | under | 0.3256410256410256 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|29cdf1f7-a211-4e3a-9cde-995abf60fff2 | underdog | Dawson Knox | Receiving Yards | under | 0.3256410256410256 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|15449672 | prizepicks | Jared Goff | Pass Yards | under | 0.3229208330880209 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|e258eac8-2b91-4d22-a73b-794a4e32ea59 | underdog | Drew Stevens | Kicking Points | under | 0.3223748040781854 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15449909 | prizepicks | Trey McBride | Rec Yards | under | 0.3203423734117173 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|f091cac5-4f05-42ef-b175-754f1791849f | underdog | C.J. Stroud | Pass Yards | under | 0.3156355597388093 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15533336 | prizepicks | Chris Olave | Rec Targets | under | 0.315630273383343 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|6080670d-2cfb-45a1-b9b4-0e0657e30305 | underdog | Will Shipley | Rush Yards | under | 0.3139883359065296 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|f2c13f8a-1cd3-496f-b6d9-39e02549bcca | underdog | Makai Lemon | Receiving Yards | under | 0.3139334853531217 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| prizepicks|15449660 | prizepicks | Kirk Cousins | Pass Yards | under | 0.311907947731458 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|064dd30b-9aac-4164-8882-0ba99672690c | underdog | Jacoby Brissett | Pass TDs | under | 0.3116425980687034 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|f06eb33b-4e63-4301-ba01-0edfbbb33d7f | underdog | Kyler Murray | Rush Yards | under | 0.3112400700494911 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15449644 | prizepicks | Joe Burrow | Pass Yards | under | 0.3100566818814402 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|238671cb-13f7-4d35-98b1-6044ba37f694 | underdog | Will Shipley | Receiving Yards | under | 0.309578456534118 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|94701aa5-8f21-4df5-852e-b94700a79716 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3095104204107922 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|27512774-bdf7-4095-996f-f2b9009da9a7 | underdog | Jakobi Meyers | Receiving Yards | under | 0.3093413624919094 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|e181aeee-c199-4ae6-8faa-e2ccf0001c5f | underdog | Kyler Murray | Pass Yards | under | 0.3092425742167098 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|00e397be-100c-4ad3-9477-c4e557282dca | underdog | Wil Lutz | FG Made | under | 0.3063647382931589 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| prizepicks|15449759 | prizepicks | Kyler Murray | Rush Yards | under | 0.3053674690789453 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|5e4c0045-b85d-4f37-80bc-28b653c73f62 | underdog | Colby Parkinson | Receiving Yards | under | 0.304864547661155 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|336ad40b-658d-46d8-87e2-ee2dc19f8307 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.302396094451143 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|432d7b45-6da8-4be5-b8cb-ca30565306b2 | underdog | Alvin Kamara | Rush Yards | under | 0.3018676329916925 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|188676ed-1afa-4b51-8567-4a0e106d2aa1 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.3017177210381112 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|f5d4b62c-6ada-41f3-8fd1-58eb65b443f8 | underdog | Eddy Pineiro | FG Made | under | 0.3013237790045318 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|c3c42681-2420-4c10-9c54-02119dc203bd | underdog | Tyler Allgeier | Receiving Yards | under | 0.298989898989899 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|b7d88720-2c24-4e23-9738-2ba37cad8acb | underdog | Joe Burrow | Completions | under | 0.2974381289807906 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|2eb7f05a-a05a-4b68-829b-fb75ae65fe94 | underdog | Mike Evans | Receiving Yards | under | 0.2969685991401806 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|4d21592e-ebe9-42e3-bf4f-ea7e4681ada3 | underdog | Joe Burrow | Pass Yards | under | 0.2954947355468827 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|9392237f-b999-4108-9652-ccb36edcfba0 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.2943238109415608 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|add1772f-2070-44fa-9398-fc5892fd9648 | underdog | DK Metcalf | Receptions | under | 0.2940024688560316 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|d1974575-0dea-4581-87a8-962ab2e41268 | underdog | Andy Borregales | FG Made | under | 0.2938341625287526 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e6618d76-6c28-4025-bf7d-31c890770dad | underdog | Mohamed Amoura | Shots Attempted | under | 0.2896577404114593 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|2ceab9dd-4b53-4375-a734-54e232e25a20 | underdog | Tre' Harris | Receiving Yards | under | 0.2887093904528367 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|f3abb736-060e-4f59-8986-e2f851377702 | underdog | Tyson Bagent | Pass Yards | under | 0.2875354691531914 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|5d0df89f-50bd-4cba-86c0-3b56f8d932ba | underdog | James Cook | Receiving Yards | under | 0.2856105912025095 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|278f5aaa-4381-4ee9-afd3-cb0e5297bdcd | underdog | Chris Olave | Receptions | under | 0.2855437567850502 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|9f0c097a-dc3f-432f-821d-7820b2e0564e | underdog | Will Shipley | Receptions | under | 0.2852267491638394 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|a3725ffb-cd23-464e-b333-fc5040ed36e7 | underdog | Malik Willis | Pass TDs | under | 0.2839614209819722 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|b4a05962-a3f6-490a-b2f4-e298c4d7a8cc | underdog | Kevin Coleman | Receptions | under | 0.2837935091637323 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|f7d2ae6d-ba84-46af-b9a1-3a6a0d8e756a | underdog | Kyler Murray | Pass TDs | under | 0.2818710576119041 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|11d68ac2-38ef-4f46-8d81-fd4caa362d90 | underdog | Malik Willis | Pass Attempts | under | 0.2807499905371733 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15529445 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.2806532166570322 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|ffb77627-b9ce-492a-9753-ceddd590adf2 | underdog | Jacory Croskey-Merritt | Rush Yards | under | 0.2806035319642522 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|61e038ea-2f52-46b2-85d1-f0998612312a | underdog | Jordan Love | Pass Yards | under | 0.2792351742198379 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449900 | prizepicks | Christian McCaffrey | Rec Yards | under | 0.2786153182458308 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|30d4b757-382c-4956-85d2-a0d3ab1d7b46 | underdog | Oronde Gadsden | Receiving Yards | under | 0.2777182211804526 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| underdog|d4060982-6b93-40e5-a4fe-ecb3dbc6ee6e | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.276281816724621 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15533063 | prizepicks | Troy Franklin | Rec Targets | under | 0.2762539045085913 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|ffb4019d-afe3-44e5-ae7b-493887d9041b | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.2762520937401261 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|df7727b2-36a9-42fa-bde7-8f29d569fd26 | underdog | Jayden Daniels | Pass Attempts | under | 0.2760309605481029 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|fe280193-2f7d-47fc-aded-70fb9c741087 | underdog | Puka Nacua | Receptions | under | 0.2756118058538218 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|c4f8457d-53ec-4fc4-9c30-18114a8b3c71 | underdog | Sam Darnold | Pass Yards | under | 0.2729977800889878 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|6bf44240-0755-4388-880a-e47f0635d3c7 | underdog | Jacoby Brissett | Pass Attempts | under | 0.2709236835736173 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|65d745e8-ea3e-4d0c-8cea-87b17b526aa9 | underdog | Courtland Sutton | Receiving Yards | under | 0.2699625509266661 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| prizepicks|15449769 | prizepicks | Bo Nix | Rush Yards | under | 0.2679388206198347 | 2026-10-07T05:55:02Z | 2026-10-11T16:05:00.000-04:00 |
| prizepicks|15533340 | prizepicks | Darnell Mooney | Rec Targets | under | 0.2678215238053804 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|be7db7b4-f06e-4e3d-93fd-721bd0760e19 | underdog | Eddy Pineiro | Kicking Points | under | 0.2668372806611836 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|3a14827c-569f-4eb8-9345-895fe6e771f9 | underdog | Sam LaPorta | Receiving Yards | under | 0.2667595783945387 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|bdd85957-ef5a-4ba0-bc19-82eeb30f5e4e | underdog | Michael Wilson | Receiving Yards | under | 0.2663036175518312 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|0c67a299-6d50-4dfd-83d8-86ac1896c81b | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.265955000867306 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|b0b72aa6-a578-41e9-98a6-744aadecf895 | underdog | Terry McLaurin | Receiving Yards | under | 0.2644273715815673 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15533351 | prizepicks | George Kittle | Rec Targets | under | 0.2626516200178651 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|92b2bfcb-8de9-4dcc-a359-e7268296118d | underdog | Bo Nix | Pass TDs | under | 0.2623089174790989 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| prizepicks|15489682 | prizepicks | Drake London | Rec Targets | under | 0.2622372257125874 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|b4fa7aba-1a6a-42ab-830f-d85d3e5b824b | underdog | Geno Smith | Completions | under | 0.2600700297199395 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15599454 | prizepicks | Braelon Allen | Rec Targets | under | 0.258499423330523 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|a0f23d7d-4682-4216-b484-e6d547f8ff36 | underdog | Courtland Sutton | Receptions | under | 0.2580032145651396 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|80985dc1-5d20-445a-b1d5-1090618bd695 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.2576868449076697 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449658 | prizepicks | Jordan Love | Pass Yards | under | 0.2571437253567415 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15525492 | prizepicks | DK Metcalf | Recs | under | 0.2569690113466795 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15449893 | prizepicks | Nico Collins | Rec Yards | under | 0.2568311333120517 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|59f4bae8-4e72-4443-a7af-41db83a86b65 | underdog | Chris Boswell | FG Made | under | 0.2567139537079915 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|05fd5d0b-9797-4d5f-b1ef-e1adcec11515 | underdog | Garrett Wilson | Receiving Yards | under | 0.2559479027601589 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15599467 | prizepicks | Colby Parkinson | Rec Targets | under | 0.2554866320959934 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|b178a530-22ae-4ba9-b596-f67abbbbf437 | underdog | Dontayvion Wicks | Receptions | under | 0.2551253817329821 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|6bb2be9a-d7ad-41f5-a2db-4d395bdbef56 | underdog | Christian Yelich | Runs | over | 0.2539773816369562 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|eca48ddf-eed0-42da-985d-93ad1d876242 | underdog | Tucker Kraft | Receiving Yards | under | 0.2538886076157679 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|a978bb2e-0d01-4165-af55-9cd269cfe52b | underdog | George Kittle | Receptions | under | 0.2528572985479788 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|e68e4ffe-2461-4d8d-80fa-4b67c9545985 | underdog | Elic Ayomanor | Receptions | under | 0.2527787855509557 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|6898c9de-9997-4138-924d-4c24eaf45bd2 | underdog | MarShawn Lloyd | Rush + Rec Yards | under | 0.2525376782754274 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|cb403c05-8ae0-4333-9be0-8a5d48fd5f87 | underdog | Ka'imi Fairbairn | FG Made | under | 0.2520415654693235 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15533051 | prizepicks | Mark Andrews | Rec Targets | under | 0.2511520614464914 | 2026-10-08T06:06:51Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|6243a247-3dfc-4e99-83ea-95ed915f7573 | underdog | Brice Turang | Runs | over | 0.2503282613732908 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|427cad33-933f-4020-bf19-9b46db422f35 | underdog | Romello Height | Sacks | over | 0.2489526914183761 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|51ab9308-89cc-4510-ab10-f35b71218f70 | underdog | Efton Chism | Receptions | under | 0.2481703419541677 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|3094dc42-a0a4-4ac0-8f4a-6347d0461f2d | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2459715639810428 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|e9154b68-c9cf-49d9-be8d-79614a25c20d | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.2458336009028559 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|13975919 | prizepicks | Jayson Tatum | Pts+Asts | under | 0.2451279480496665 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975925 | prizepicks | Jayson Tatum | Pts+Rebs | under | 0.2442060163021608 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|dfffc85b-b3b3-4334-9dcd-3b095c54151d | underdog | Antonio Williams | Receptions | under | 0.2441319198227238 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|40f916d5-e93b-4ca5-a639-a249ca825da9 | underdog | Quinshon Judkins | Rush Yards | under | 0.2439344298080761 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|ecd912bb-b955-4914-b366-259f6a9827ac | underdog | Riley Patterson | FG Made | under | 0.2429305009555447 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|05ee000c-4a6a-430a-b254-248a00b207a2 | underdog | Kyler Murray | Completions | under | 0.2416780091424136 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|12329758-8ce2-4782-9610-5ac8e8c3f621 | underdog | Alvin Kamara | Rush + Rec Yards | under | 0.2414761218488055 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|f9c622a6-624b-4373-a286-ffe2289a2105 | underdog | Daniel Jones | Pass TDs | under | 0.2409516659547806 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|f72fbefd-19f9-4e65-97b1-423a73b74d50 | underdog | Kyle Tucker | Runs | over | 0.2406489847469155 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|615030c6-c5dc-49bc-b2db-aef26aeca116 | underdog | Garrett Mitchell | Runs | over | 0.2405362395717798 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|b0ac5a2d-b9fb-4b18-ae57-e8f4f5e4b8a6 | underdog | Justin Jefferson | Receptions | under | 0.2398841798759714 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|93287b7c-8820-416c-a77d-fdcb70ffe403 | underdog | Tyler Shough | Pass Attempts | under | 0.2392669925726875 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|676c41cc-f796-4680-a33d-629cdd3d190f | underdog | Jake Bauers | Runs | over | 0.2391827705120699 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|a9daa4e2-d391-4a56-8887-122069b1a6f8 | underdog | Felix Correia | Shots Attempted | under | 0.2388358806476083 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|2681c8e2-4ec6-46a5-9628-192b77c64bbf | underdog | Joe Burrow | Pass Attempts | under | 0.2385284941063676 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|b444a78c-4fc8-4056-8344-cb4260481ac6 | underdog | RJ Harvey | Rush Yards | under | 0.2384554427410479 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| prizepicks|15576380 | prizepicks | C.J. Stroud | Pass+Rush+Rec TDs | under | 0.2378671185795918 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15489684 | prizepicks | Jahan Dotson | Rec Targets | under | 0.2376385063381021 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|6751adf2-fa18-4fbb-b556-3ac920d65434 | underdog | Wil Lutz | Kicking Points | under | 0.2372819413422627 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|3050dde8-37d1-4db1-8408-081df08df056 | underdog | TreVeyon Henderson | Receiving Yards | under | 0.2364485981308411 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|7b95f33b-47e2-4619-8793-ac5c52ebfb1b | underdog | Mattia Zaccagni | Shots Attempted | under | 0.2345663749316897 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|79ac5ed9-8acd-47c3-abc9-f18a0272e653 | underdog | Jahmyr Gibbs | Receptions | under | 0.2341401940396219 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|3ec292ee-323d-47eb-84fc-12faec7e235c | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.2338645885222401 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| prizepicks|15489683 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.2335274669306117 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|4e4b2337-9bf3-4256-877e-50f933d65694 | underdog | Nick Folk | Kicking Points | under | 0.2320321233110344 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|a682acd7-5322-49c7-99a7-2782436d8ab5 | underdog | Sterling Shepard | Receiving Yards | under | 0.2317757009345794 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15449911 | prizepicks | Michael Wilson | Rec Yards | under | 0.231695503206471 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15604862 | prizepicks | Dallas Goedert | Rec Targets | under | 0.2301377876771176 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|84bdb261-e306-43f0-bd9f-8c8350bca79f | underdog | Tyson Bagent | Completions | under | 0.2300379181682935 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|f9725ec9-a047-4256-9d92-57304856be26 | underdog | DeMario Douglas | Receiving Yards | under | 0.2299592466123223 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|c68b03b1-7937-4f85-8fc6-ceb7ae5aa7fb | underdog | TreVeyon Henderson | Receptions | under | 0.2289397261388017 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|aad56839-2e13-4206-945b-c57f810f01d2 | underdog | Josh Downs | Receiving Yards | under | 0.2280417669903913 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|fb5b5edf-9d25-4666-a562-fbae48bfe8aa | underdog | Woody Marks | Rush Yards | under | 0.2276408542490519 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|d284599a-7624-47ac-bc46-4073d88327d4 | underdog | Parker Washington | Receiving Yards | under | 0.2270874262256726 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|dc4b4422-e58a-499b-bb63-8deea069d91c | underdog | Sam Darnold | Completions | under | 0.2263108017814826 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|6d8b3c17-fc1a-427f-8889-37eea2c07fda | underdog | Daniel Jones | Rush Yards | under | 0.2260348380485218 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449901 | prizepicks | Mike Evans | Rec Yards | under | 0.2258028888845463 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|9e77d7e4-b1ea-4ac5-be36-534f42c193a6 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.2250794034871224 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|c8615955-8661-4024-92ae-b2f2688c461c | underdog | Brock Bowers | Receptions | under | 0.2248127207057465 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|ff67590c-1684-477f-ac6c-eb3da3332670 | underdog | Joey Slye | FG Made | under | 0.2245414925899477 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|92464fde-118a-4129-a509-887930284223 | underdog | Kyren Williams | Rush Yards | under | 0.224502888663667 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|69a0a95e-0fa1-4218-b49d-f069dbf0a678 | underdog | Khalil Mack | Sacks | over | 0.2231195901680223 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|0a190d3a-aef9-41da-aa00-7514742a1f03 | underdog | Gauthier Hein | Shots Attempted | under | 0.222889800147483 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|ce126fc7-7f6f-409b-9dc5-707826f71ef8 | underdog | Amon-Ra St. Brown | Receptions | under | 0.2221856720995597 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|93260779-b409-4b7a-890b-439d6244e590 | underdog | Jordan Love | Rush Yards | under | 0.2214636115631517 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|5ce44cf4-1b0e-4f05-a4f6-645093249b8e | underdog | Pat Freiermuth | Receiving Yards | under | 0.2212885220471538 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533059 | prizepicks | Courtland Sutton | Rec Targets | under | 0.2212171503289755 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|e0b41f92-108b-4fbe-bd5a-9c70bdf2dbc9 | underdog | Aaron Donald | Sacks | under | 0.2211009174311926 | 2026-10-10T05:51:08Z | 2026-10-13T00:15:00Z |
| underdog|6c66a73a-f78b-4085-ae5b-9b34586c8089 | underdog | Jackson Chourio | Runs | over | 0.2209595959595959 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|0f4d6995-3db6-45c7-9dc4-d375a8c24270 | underdog | Kayshon Boutte | Receiving Yards | under | 0.2208823535192222 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|7905bd66-0389-4e47-b016-02dceeb6c1f6 | underdog | Kirk Cousins | Pass Attempts | under | 0.2204761395272305 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|03cb6e4d-f656-4dc6-b066-bdb455be99f9 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.2200685344507653 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449903 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.217540442988474 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|6e4d3f6e-9102-44fb-b416-f9442f7a14ee | underdog | Samaje Perine | Rush Yards | under | 0.2173368952100646 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|3af1ecf1-65e7-4495-82a4-94d77e731f6f | underdog | Logan Hall | Sacks | over | 0.2170418339268822 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|75d217fd-efc9-4ada-8851-73e19b817338 | underdog | Mike Evans | Receptions | under | 0.2168016992318034 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|e4cf2801-9fda-427b-9a6d-4c20e0a89562 | underdog | Jared Goff | Pass Attempts | under | 0.2167256153544267 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|6c0a597d-7e0f-40f0-a7a6-c215486300e1 | underdog | Shohei Ohtani | Runs | over | 0.215944065301753 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|13a79ef2-f641-487f-80af-82857c2c3779 | underdog | Hunter Henry | Receptions | under | 0.2154838628723674 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|903dade0-d796-4cad-80bf-f0c1e15f849a | underdog | Matteo Cancellieri | Shots Attempted | under | 0.215199401955599 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|0b8475a8-56e3-41a5-b351-1754db63f413 | underdog | Andy Pages | Runs | over | 0.2144535240040857 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|7ae96072-ec98-494b-a3d0-85510557e5f9 | underdog | Troy Franklin | Receptions | under | 0.2139868666183766 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|61fcb1cd-f8fd-4564-a7fe-4ea0da59964e | underdog | Chase Brown | Rush Yards | under | 0.2138735062415819 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|43f7e00d-843d-47c9-bb27-e67f897a5ec0 | underdog | Roman Wilson | Receiving Yards | under | 0.2137921389192351 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|a7ec8655-e8a3-48dd-bd43-2cec1d5b6f64 | underdog | Jarran Reed | Sacks | over | 0.2135321139514836 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|f0dd3d5e-0c0b-42b9-817f-1726278b8b7c | underdog | Derick Hall | Sacks | over | 0.2131525902021196 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|e0227de8-3ccb-4f77-bf7b-c07fc0371264 | underdog | Josh Downs | Receptions | under | 0.2126733478580765 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|1e5bed87-199d-469b-9853-71be6d5e0d99 | underdog | Eliezer Mayenda | Shots Attempted | under | 0.2125184278623569 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|e678fca0-b179-4564-8bc6-fb9df7821628 | underdog | Angel Martínez | RBIs | over | 0.210772501771793 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f1085fb8-6b3a-4dea-b20f-cc2845b53b7d | underdog | KC Concepcion | Receiving Yards | under | 0.2106469089091266 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|ed10bdc1-8730-4084-85fd-daa45bedd0b1 | underdog | Amine Harit | Shots Attempted | under | 0.2082134268048945 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|73bcc271-a76e-4002-84fd-adb01d8ce8ba | underdog | Jaxon Smith-Njigba | Receptions | under | 0.2078752692831559 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|6f8e2499-374e-4ba8-a526-e03ec03b1458 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.2071827459411265 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|9a19b498-3df9-4bb3-96e1-b03e91ee4b1e | underdog | Teoscar Hernández | Runs | over | 0.2069889702092567 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|f9aeab48-b4f6-440a-9742-6e6940183e7b | underdog | Kendre Miller | Rush Yards | under | 0.2068438807179956 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|086199dd-2b08-49b6-b363-9adf5b5b06c4 | underdog | Tucker Kraft | Receptions | under | 0.206807826430273 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|c9f18882-b77c-420e-be7b-9039a2e38375 | underdog | Harold Fannin | Receiving Yards | under | 0.206185509200954 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|f7146c71-fc50-4faa-998f-d103cdc0f6e5 | underdog | Joey Slye | Kicking Points | under | 0.2060097627977997 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|452891e0-0a4a-4a3b-a860-b89bc84e7726 | underdog | Kaleb Johnson | Rush Yards | under | 0.2051064057951495 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|848df3dd-fc1a-40af-9e24-796b9aea5cdd | underdog | Christian Pulisic | Shots Attempted | under | 0.2049433443770592 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|13ec7c46-f1a4-49bf-86fc-e098b3258936 | underdog | Darius Cooper | Receiving Yards | under | 0.2045308377145825 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|5ed10e6c-c27c-45f6-b06e-b488448c09c7 | underdog | Joe Burrow | Pass TDs | under | 0.203878918842333 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|76c95021-1b26-4a70-a329-d38002cdd39b | underdog | Jahan Dotson | Receptions | under | 0.2029253788734003 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|d89f2e11-aba0-4fa7-953f-4bd607a20ad7 | underdog | Colby Parkinson | Receptions | under | 0.2028856735476636 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|82f16a56-bc2e-4ebb-a9d0-9270056bc3bb | underdog | Malachi Fields | Receiving Yards | under | 0.2022872334031797 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533053 | prizepicks | Zay Flowers | Rec Targets | under | 0.2016702118631688 | 2026-10-08T06:06:51Z | 2026-10-11T20:20:00.000-04:00 |
| prizepicks|15604857 | prizepicks | Justin Jefferson | Rec Targets | under | 0.200537455335387 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|afdd0ec1-28aa-4816-bdde-c4edf9692569 | underdog | Colston Loveland | Receiving Yards | under | 0.2003043116291809 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e941eee4-2a34-44e7-a72c-41d784a6a00a | underdog | Mark Andrews | Receiving Yards | under | 0.1996575311591329 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|b7b76dbf-f441-4f41-ae8b-ed38049f1cb3 | underdog | Taylor Walls | Runs | over | 0.1993861839367457 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0d78b55b-a49b-46e2-a8e5-e8a6f9a42b59 | underdog | Tyson Bagent | Pass Attempts | under | 0.1986176568491733 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|7cb544f8-9d57-4984-9cea-a8f3aa1243a1 | underdog | Brayan Rocchio | RBIs | over | 0.1983322064457966 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|810982be-0d9d-4221-8a0e-df4a784c1f7c | underdog | Neal Maupay | Shots Attempted | under | 0.1972555214481075 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|0fe76733-cbc2-4994-a35e-67fe8272b312 | underdog | Jake Elliott | FG Made | under | 0.1972276876626942 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|a7f9f221-bd1f-4977-ba27-7fea0a1b2d79 | underdog | Javon Kinlaw | Sacks | over | 0.1970277849471546 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|31f02654-8077-4c49-ade7-fdf9ce4b5985 | underdog | Tyjae Spears | Receptions | under | 0.1968777871133948 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|a071749d-f622-4a11-8e39-928b9b5a0126 | underdog | Derrick Barnes | Sacks | over | 0.196744771639426 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|db56d9d5-7b87-477d-810b-094261ac6811 | underdog | Malik Nabers | Receptions | under | 0.196349056327543 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|3c232ca9-44d0-4eab-bb9b-d280dd0fda6f | underdog | Zay Flowers | Receptions | under | 0.1960405558292924 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|16b5bb89-7e83-4f78-83d9-bdaca93c3351 | underdog | Luther Burden | Receptions | under | 0.1959993754954977 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15480097 | prizepicks | Denzel Boston | Rec Targets | under | 0.1958779220733016 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|a1b5ed7a-c2c1-418c-b9e4-d572bf661572 | underdog | Garrett Wilson | Receptions | under | 0.1954449874391693 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15449907 | prizepicks | Sam LaPorta | Rec Yards | under | 0.1952754562589411 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|b4389246-2c68-4e06-b877-19b0042440a8 | underdog | Jordan Whittington | Receiving Yards | under | 0.1951541850220265 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|e5112511-7764-4b1e-bcef-fe696ba63110 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1949623638884035 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|89a083da-ed30-4631-8ab0-c4847ea86edd | underdog | TreVeyon Henderson | Rush + Rec Yards | under | 0.194757964036893 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|fbca95b0-cd67-44ec-a7f4-24e973b530f5 | underdog | Jared Goff | Rush Yards | over | 0.1947516304227962 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|3165a526-cbe1-4f5b-b406-98c00b47aebc | underdog | Jameson Williams | Receiving Yards | under | 0.1946869283124519 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|19340189-9083-42c4-b13a-60318460e0b8 | underdog | Ruke Orhorhoro | Sacks | over | 0.1940537303129973 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|e83c6234-cc83-47d5-a7b8-dfbe3cd1e1e3 | underdog | Drake London | Receptions | under | 0.1933319434009791 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|eeaaebdf-788e-4f68-b550-549154979372 | underdog | Roman Wilson | Receptions | under | 0.1933296068198631 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|120e250e-fa18-407e-841c-10eeb4c14422 | underdog | Ollie Gordon | Receiving Yards | under | 0.1932905251806308 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|8d348db2-67f6-48c4-9314-90fe8ad307f9 | underdog | Aaron Jones | Rush Yards | under | 0.1924344483838027 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|33c9882b-561a-46a1-9c5f-8abdd06d24c0 | underdog | Tony Pollard | Rush Yards | under | 0.1923515318345046 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|97f2c7ae-5b0d-4d86-a1ab-ed8e3e064420 | underdog | Liam Hicks | RBIs | over | 0.1914378826782539 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6a430778-a8b2-49b4-9a2b-01bb586957eb | underdog | Dayo Odeyingbo | Sacks | over | 0.1913339263267269 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|3a6f406e-5e63-4d2e-a6a4-316043910332 | underdog | Jackson Chourio | Total Bases | over | 0.1912842485060322 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|da2d150e-22d0-47c6-9a0d-4b750291ae63 | underdog | Deone Walker | Sacks | over | 0.1905113805902615 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|6303d9e8-cdb4-41d9-9cd7-218c8924d569 | underdog | William Contreras | Runs | over | 0.1900617186263649 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|1f034fea-65f0-4284-b71b-7dda16cb665d | underdog | Cooper Pratt | RBIs | over | 0.1896810549897226 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c994a85e-bd27-4feb-be6d-8b97fc0a7773 | underdog | David Montgomery | Rush Yards | under | 0.1892744255759634 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|fb584a96-cc72-4479-88a9-e416df146cd7 | underdog | Cam Skattebo | Rush Yards | under | 0.1890943980221455 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|57e57aa0-bf90-4c39-9e4b-302a6ea11a7b | underdog | MarShawn Lloyd | Rush Yards | under | 0.1886765227420784 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|295a7594-5977-4038-a420-68b1d18b30f8 | underdog | Chris Rodriguez | Rush Yards | under | 0.1882057330074009 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|1eab050c-610d-4b9f-94be-6ce6a6f57fbd | underdog | Jake Bauers | RBIs | over | 0.18812178173274 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|73474dc6-e67a-49e7-a217-10d6f09b3197 | underdog | Terry McLaurin | Receptions | under | 0.1879783734336115 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|cf14e5ac-da65-408b-855d-1fa117ee8f78 | underdog | Daniel Carlson | FG Made | under | 0.1879773898467173 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|14f12403-320f-4df3-9eec-99e890ef977e | underdog | Rhamondre Stevenson | Rush Yards | under | 0.187745137554351 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|d33717e3-9348-4118-ac49-ca02c8cedf36 | underdog | Romeo Doubs | Receiving Yards | under | 0.1876916221631408 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533224 | prizepicks | Tyler Warren | Rec Targets | under | 0.1874950747427977 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|149c5143-d633-43fb-ba9e-900c93ceb4a9 | underdog | Mike Gesicki | Receptions | under | 0.1874943643270745 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|53015217-dee8-4b34-815d-4f62847b153e | underdog | Abde Ezzalzouli | Shots Attempted | under | 0.1866614708754486 | 2026-10-09T20:57:57Z | 2026-10-11T16:30:00Z |
| underdog|6a5b3fd9-1b1a-41ce-a0be-1cdfbf5f4961 | underdog | Garrett Mitchell | RBIs | over | 0.1865907653383934 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15533222 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.1862855432853848 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|13975931 | prizepicks | Jayson Tatum | PRA | under | 0.1859948657142129 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|e948bb0a-4e71-49a6-a9e7-dbe364c5dcef | underdog | Mookie Betts | Runs | over | 0.1858994514900606 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|55e860af-c124-43b2-9676-a355ae92a46d | underdog | Kyle Tucker | RBIs | over | 0.1858042977382799 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c3db35d8-bedd-43d0-b439-aad7f0c22d68 | underdog | Aaron Jones | Rush + Rec Yards | under | 0.185780213482512 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|98b31f0e-1994-478c-ac71-bacbd8cdc24c | underdog | Cairo Santos | FG Made | under | 0.1854155272526558 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|8b1dd8af-816b-4bc2-b87e-8aa9aa98ef29 | underdog | Tyler Bass | Kicking Points | under | 0.1850716748351706 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|8fb9e07e-d089-4217-b9e2-3bff144d7eb5 | underdog | Sam LaPorta | Receptions | under | 0.1848821490777388 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|89db5515-d984-4e98-86ee-0ef155884e7d | underdog | Andy Pages | Total Bases | over | 0.1848739495798319 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|addf9453-7553-41b4-97ba-935e29e8c6a7 | underdog | Jonathan Taylor | Receptions | under | 0.1847985717038194 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|684212b7-4f49-4e54-bcfa-e35adefb36cf | underdog | William Contreras | Total Bases | over | 0.1843023046776688 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|21940918-0e1b-469c-a33d-ebe800fbfd3f | underdog | Christian McCaffrey | Rush Yards | under | 0.1840975522384134 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|c23a382f-af00-491d-a9ec-aa3258c7ad61 | underdog | Matthew Stafford | Pass Attempts | under | 0.1838682559925166 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|da6d6ded-d79b-4eca-8d51-fdfd97b85a2c | underdog | Jordan Love | Pass Attempts | under | 0.1833587676111072 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|9d4746d0-fd82-4632-ae17-84dedf0873de | underdog | Kwity Paye | Sacks | over | 0.1832662478679131 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|5a876cbb-5736-43a5-8e62-cc6bc9623c56 | underdog | Mark Andrews | Receptions | under | 0.1830028846839179 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|220d5940-700b-4ec8-98f0-4d23d6a9fd25 | underdog | Troy Franklin | Receiving Yards | under | 0.1816994313970772 | 2026-10-09T20:57:57Z | 2026-10-11T20:05:00Z |
| underdog|2d5c08c7-a6ab-44ee-ac88-45c9e7eaf24e | underdog | Tijjani Noslin | Shots Attempted | under | 0.1812409273618878 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|663834d8-3fff-419d-9aa3-2d9735a0df9d | underdog | D'Andre Swift | Rush Yards | under | 0.1805566061981877 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|921e858c-6667-4959-8b4f-5db02cf33568 | underdog | David Montgomery | Rush + Rec Yards | under | 0.1803615019179272 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e876c17e-37a7-46a3-82eb-de3591c0f69f | underdog | Hunter Henry | Receiving Yards | under | 0.1802598277911742 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|c51dd7a8-11e4-4245-9abd-782927b4c773 | underdog | Geno Smith | Pass Attempts | under | 0.1796565809973912 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|f6e4fc53-1e49-48f5-a5ff-a9db114bdf29 | underdog | Kaleb Johnson | Rush + Rec Yards | under | 0.1794547508498991 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|10fb776f-4f28-42ab-a6c4-432fc288c563 | underdog | Emanuel Wilson | Rush Yards | under | 0.1783597945324108 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|15604863 | prizepicks | Makai Lemon | Rec Targets | under | 0.1779667051263448 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|14b15dc5-39ac-4df6-8f17-271507a3ef2b | underdog | Antonio Williams | Receiving Yards | under | 0.1778854800450195 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15451223 | prizepicks | Puka Nacua | Recs | under | 0.1774909016179514 | 2026-10-07T05:55:02Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|61315832-5e54-41b3-9c8b-23ef31024381 | underdog | Jordan Whittington | Receptions | over | 0.1770609074494917 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|47f753a5-caf7-4faf-9301-1e37510c8435 | underdog | Greg Dulcich | Receiving Yards | under | 0.1761887933014442 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|57a58b2a-28f0-4759-8f4d-71ece5e13400 | underdog | Christian Yelich | RBIs | over | 0.175599128540305 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|7a967103-0027-4812-af79-d243604b630f | underdog | Eric Wilson | Sacks | over | 0.1754500485761057 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|7c470d7b-1609-4fb9-8307-5c41f4842f30 | underdog | Evan McPherson | FG Made | under | 0.1750933456284263 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|db7b705d-d53d-4606-a395-f057c350a4bc | underdog | Colston Loveland | Receptions | under | 0.1743819993651213 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|79bee78a-cb07-4948-810a-ff49cad25363 | underdog | Leonard Williams | Sacks | over | 0.1742919415388009 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|79167483-55c9-4279-bf38-d643d6375459 | underdog | Danielle Hunter | Sacks | under | 0.1740987931711355 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|8d3a38f5-8b3c-4126-a6b4-396cf0388083 | underdog | Treylon Burks | Receptions | under | 0.1739978857594647 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|7a684e5b-b8aa-4cb6-b800-fa428c4e3f72 | underdog | George Holani | Rush Yards | under | 0.1734820045881857 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|8d963fd1-f678-4f6b-a084-3cecf8029e01 | underdog | Rashid Shaheed | Receiving Yards | under | 0.1731412065458198 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|b4f847a3-febb-4da2-a1f2-ebfe7f2227c6 | underdog | Chris Boswell | Kicking Points | under | 0.1730487402374262 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|29ad90aa-64e2-46c8-80b7-9e7a385cf895 | underdog | Tuli Tuipulotu | Sacks | over | 0.1728320543642288 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|38046d4c-7a22-46fb-be89-57f58e265808 | underdog | Romeo Doubs | Receptions | under | 0.172620238361046 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|d765724f-2afd-4288-8601-3a736889bff6 | underdog | Malik Nabers | Receiving Yards | under | 0.1719078815391725 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|a633c4c2-10b4-4e15-b3e4-c44bedcc14ef | underdog | Cameron Jordan | Sacks | under | 0.1708333333333334 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|f2d5a157-6b17-48f8-940f-5996d62b0104 | underdog | Brayan Rocchio | Total Bases | over | 0.1704545454545454 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|257de987-8572-4ae2-a97b-f31577f78b93 | underdog | Andy Pages | Hits | over | 0.1700295405673744 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|65ffc768-52b9-4eee-8722-d9fdb42815f9 | underdog | Jonathan Asp Jensen | Shots on Target | over | 0.1693749694108624 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|7d4a43f7-20d2-4872-b9f9-0d4cc918122c | underdog | Parker Washington | Receptions | under | 0.1691430040079576 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|c3f80a5c-c8e7-41d5-b5b0-564baf71a963 | underdog | Kyler Murray | Pass Attempts | under | 0.1690926809003619 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|887a921a-4f05-4225-aab2-9aea5a584832 | underdog | Diego Moreira | Shots Attempted | under | 0.1689767091019137 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|0d4c3b95-3026-4fea-8e22-2992ce100637 | underdog | Steven Kwan | Runs | over | 0.1688665866695755 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15533352 | prizepicks | Mike Evans | Rec Targets | under | 0.1687209545206485 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|30498c39-0c98-4828-8e1d-a0982a5e99dc | underdog | José Ramírez | Runs | over | 0.1683238889482876 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|7dcde031-f74d-4263-b01c-00161007c286 | underdog | Keaton Mitchell | Rush + Rec Yards | under | 0.1683208447882928 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|201033ee-9253-467a-acc3-a68484156ae9 | underdog | Byron Murphy | Sacks | over | 0.1681797067434818 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15449884 | prizepicks | Colston Loveland | Rec Yards | under | 0.1681452487329925 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|b407d06c-4ab5-4cdd-9576-b8637293af16 | underdog | Ja'Marr Chase | Receptions | under | 0.1674320814310429 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|024d1cb4-e419-4d42-9d28-d1141624117a | underdog | Jahmyr Gibbs | Rush Yards | under | 0.1671926520706126 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|36afacc2-6921-4af0-a671-a64e783545d0 | underdog | Thorir Johann Helgason | Shots Attempted | under | 0.1671698741728939 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|8ea10c88-278d-4cf6-a8af-cb391d508d64 | underdog | Lukas Van Ness | Sacks | over | 0.1669551481785428 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|9a6fab41-6c49-4a21-a975-51e072cd4f27 | underdog | C.J. Stroud | Pass Attempts | under | 0.166283868389501 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15533058 | prizepicks | Rome Odunze | Rec Targets | under | 0.1655527286799025 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|bafd018e-4229-436d-ac67-5c1afb3a9602 | underdog | Arnaud Nordin | Shots Attempted | under | 0.1646073107144637 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|761d6075-42b8-4f57-a24b-d2d063bc7c7a | underdog | Zay Flowers | Receiving Yards | under | 0.1642282559499017 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|f93169d4-e999-4dfa-b5b9-270247a194af | underdog | Matthew Stafford | Rush Yards | over | 0.163819340859309 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|243a77e9-c788-439d-99c8-bf6ce5bb6da1 | underdog | Matthew Golden | Receptions | under | 0.1637468725261556 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|b3cc5f8b-478a-40fe-a237-326bf8dd3722 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.1633832283104532 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|f4dc9343-78b1-4b04-ae32-800cb3f165c5 | underdog | Tyler Bass | FG Made | under | 0.1627647580839394 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|bbf24dda-ebd2-48d1-822a-39ee79a81c12 | underdog | DK Metcalf | Receiving Yards | under | 0.162747663729015 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|d0ca5ba7-8499-4dd0-8ac8-b30b5732b4b9 | underdog | George Kittle | Receiving Yards | under | 0.1627368151166864 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|b4616eba-cd80-4c16-9f2d-ab1837a6e874 | underdog | Sam Williams | Sacks | over | 0.1621586190631266 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|10bb1e15-c31d-4702-b0f8-efb2213f1cb2 | underdog | Travis Bazzana | RBIs | over | 0.1619855149266913 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|21fad3c5-3580-46bd-aeb1-17a4953b6374 | underdog | TreVeyon Henderson | Rush Yards | under | 0.1616405366588312 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|3e82546c-560d-4165-8703-c3d04194801d | underdog | Khalil Shakir | Receiving Yards | under | 0.1612483808717202 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|15533349 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.1611281403071227 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|1649702d-ccfa-4a43-b8de-647642bd85ac | underdog | Isaiah Likely | Receiving Yards | under | 0.1600286536906883 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|8bde8952-262c-42f7-a5ab-e99e7cc290c7 | underdog | Emanuel Wilson | Receptions | under | 0.1600218879075018 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|75fe08ea-ce90-47b7-8f76-10ae6bc26f26 | underdog | Jayden Daniels | Pass TDs | under | 0.1595250373946191 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|bdc2790b-2d53-42e7-b924-7fa97896ecc3 | underdog | Dallas Goedert | Receptions | under | 0.1595198014574333 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|ee8312df-81db-4f05-a2dd-5a475fc0dfd7 | underdog | Randal Kolo Muani | Shots on Target | under | 0.1593650346064019 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|38d6704b-cfd6-4a15-8ff6-b43f627c642c | underdog | Dallas Goedert | Receiving Yards | under | 0.1591697771451469 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| underdog|1044053c-1bae-4abf-9352-24352b605d52 | underdog | Kyle Pitts | Receiving Yards | under | 0.159115126501148 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|e398e419-2c82-44f6-8539-b9fbae39bd42 | underdog | Blake Cashman | Sacks | over | 0.1588302647836433 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|dbb9ad72-4436-4bbd-8c2f-8993ecbd1401 | underdog | Dontayvion Wicks | Receiving Yards | under | 0.1583969661280596 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|9702cce6-4f3e-4242-a3e4-5c328f541b16 | underdog | Adin Huntington | Sacks | over | 0.1583850341574662 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|c39d19b8-d55c-4e1f-96bb-73af508fac3a | underdog | Jackson Chourio | RBIs | over | 0.158271853935566 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|9c976c1a-cd73-4fd6-854d-a5e4b087f302 | underdog | Tyler Warren | Receptions | under | 0.1582522576838575 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|c6a6548d-0d18-40f7-8280-696efe97af8c | underdog | Richie Palacios | RBIs | over | 0.1581699346405227 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15599427 | prizepicks | Dawson Knox | Rec Targets | under | 0.1579834600344047 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15572164 | prizepicks | Tucker Kraft | Recs | under | 0.1579254264991273 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15469070 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.1576609951421698 | 2026-10-07T05:55:02Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|26385af5-fb82-4255-95ed-45999963f208 | underdog | Jon Rowe | Shots on Target | under | 0.157344942085266 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|900f095f-3f13-49b4-8a59-55a96eae4a88 | underdog | Kingsley Enagbare | Sacks | over | 0.1572265858720211 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|d30c392e-51c9-4423-ba01-a8dff9b7e383 | underdog | Cody White | Receiving Yards | under | 0.1570946100182647 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|b393ab9c-a9e9-447a-acae-23182ffaa172 | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.156922399556327 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|519c1338-1698-4fd9-8c72-514033828780 | underdog | Yuito Suzuki | Shots Attempted | under | 0.1568457272488139 | 2026-10-11T05:47:48Z | 2026-10-11T15:30:00Z |
| underdog|6596c3f2-5bcf-48e2-b2a0-54aef4a4076d | underdog | Efton Chism | Receiving Yards | under | 0.1566075147752799 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15529495 | prizepicks | Jaxon Smith-Njigba | Recs | under | 0.156076292320025 | 2026-10-11T05:47:48Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|a19d70f2-57dd-4e41-b3b4-c6622befbf32 | underdog | Aaron Jones | Receptions | under | 0.155897954728026 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|369afecf-4050-4528-8b4c-c116d3bfdf62 | underdog | Walter Nolen | Sacks | over | 0.1556628679468944 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|5ae4e1d2-506e-4c54-99fc-d80cb488368d | underdog | William Contreras | RBIs | over | 0.1556091030789825 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|6c171b37-53ea-4dfe-b440-fcdcbfe243f2 | underdog | Darius Cooper | Receptions | under | 0.1553009183745237 | 2026-10-09T20:57:57Z | 2026-10-11T13:30:00Z |
| prizepicks|15542189 | prizepicks | Mile Svilar | Goalie Saves | under | 0.1545075912022189 | 2026-10-08T06:06:51Z | 2026-10-11T06:30:00.000-04:00 |
| underdog|b1d48b58-67a5-44d9-94c9-dab60c05c9ce | underdog | AJ Barner | Receptions | under | 0.1544988677102636 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|0c34ed10-3383-48d9-bdfd-ce42dc1002f2 | underdog | Jonathan Aranda | RBIs | over | 0.1542598967297762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9ce7af5b-940d-457f-b26e-2002362fb020 | underdog | Justice Hill | Rush + Rec Yards | under | 0.1523107729380006 | 2026-10-10T05:51:08Z | 2026-10-12T00:20:00Z |
| underdog|33eb49a9-471d-423d-821d-1b1bd854ff15 | underdog | Freddie Freeman | RBIs | over | 0.1522643312924642 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|dad586c0-c8c1-495e-ae96-c56a608b75fa | underdog | Oronde Gadsden | Receptions | under | 0.1521874468562993 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| prizepicks|15622908 | prizepicks | Ladd McConkey | Rec Targets | under | 0.1520127654694155 | 2026-10-11T05:47:48Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|66d5e05c-ac01-45ce-82d6-e289c99ad121 | underdog | Cameron Archer | Shots Attempted | under | 0.1518774530144352 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|dd239596-ad57-4723-896b-604bcf012525 | underdog | Jonnu Smith | Receiving Yards | over | 0.1518347589137881 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|92966efc-fdb9-4557-94fb-0f8b4590c20c | underdog | Derrick Henry | Rush Yards | under | 0.1517399760136696 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|4eb1ecbc-cdb3-40de-b503-c2179e763e1b | underdog | Jordan Addison | Receiving Yards | under | 0.1508556820299178 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| prizepicks|15487552 | prizepicks | Jordan Love | Pass Attempts | under | 0.1505646075824736 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|0c91767e-bca8-45d8-a402-6e295fe5e408 | underdog | Travis Bazzana | Batter Walks | over | 0.150470520453236 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|a98ec56f-30c1-47cc-9060-a7454a57443e | underdog | Junior Caminero | Total Bases | over | 0.15046792197542 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15542188 | prizepicks | Jean Butez | Goalie Saves | under | 0.1504498680991512 | 2026-10-08T06:06:51Z | 2026-10-11T06:30:00.000-04:00 |
| underdog|b468e304-bd8f-4ac2-b864-b58e2ea62a39 | underdog | Nikola Vlasic | Shots Attempted | under | 0.1494699778257078 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|15449905 | prizepicks | Amon-Ra St. Brown | Rec Yards | under | 0.149099489690797 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|49c172c3-2076-4e31-a0a1-8d9af3151f2e | underdog | Max Muncy | Total Bases | over | 0.1476708640659617 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|45774592-96ea-442f-89d6-4842ce811dc9 | underdog | Cam Ward | Pass TDs | under | 0.1472825180442586 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|40452423-519e-45a9-b75b-bc7e74647b5e | underdog | Drake Maye | Pass TDs | under | 0.147059550443754 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|bfd16ddb-07de-4142-b9f1-05af06ff583b | underdog | RJ Harvey | Rush + Rec Yards | under | 0.1468742732386874 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| underdog|118dcc33-d15f-4b8d-b407-91d38142be4b | underdog | Daniel Carlson | Kicking Points | under | 0.1464780277428076 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|3d960d16-7ba3-4cf5-afcb-b82c9b9c9284 | underdog | Esteban Lepaul | Shots Attempted | under | 0.1463883654579097 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|f494c472-a062-4720-988b-afd76ea3bc6d | underdog | Cam Skattebo | Receptions | under | 0.1463603216511522 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|c1c65ba2-c738-4f13-b4ca-9e1ba5fc4f8f | underdog | Teoscar Hernández | Hits | over | 0.1458015171583357 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|15449773 | prizepicks | Brock Purdy | Rush Yards | under | 0.14569357842741 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|d6e72a44-9538-48ea-ac6f-1e42b9041de5 | underdog | Felix Auger-Aliassime | Aces | under | 0.1456145224554161 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|22392ac7-b6bd-4436-89d8-f7fdda0dd523 | underdog | Rome Odunze | Receptions | under | 0.145384470266199 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|9b611f51-bd5a-4ecd-bbfa-f2f13bfc765b | underdog | Khalil Shakir | Receptions | under | 0.1451710376003263 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|6de91ef0-d28b-4eb3-b362-934257475f02 | underdog | Rashid Shaheed | Receptions | under | 0.1451412870495274 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|29c881f7-8bca-4e58-9fb4-171396427021 | underdog | Nnamdi Madubuike | Sacks | under | 0.145136186770428 | 2026-10-10T05:51:08Z | 2026-10-12T00:20:00Z |
| underdog|18902c7e-3936-467e-a6f3-861d640c9bd4 | underdog | Mohamed Amoura | Shots on Target | under | 0.1446959313276956 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|6d5a8852-bb0c-4e61-bb32-8420c89212aa | underdog | Jakobi Meyers | Receptions | under | 0.1444347231613432 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|553254db-2776-409e-b076-046a2c542dc5 | underdog | Devaughn Vele | Receiving Yards | under | 0.1444266033339374 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|d669707b-61d9-4b26-80a4-e861b5ddc356 | underdog | Brian Thomas | Receiving Yards | under | 0.1443875800625451 | 2026-10-08T06:06:51Z | 2026-10-11T13:30:00Z |
| underdog|1c34c0eb-63a6-48d3-a4e2-4fb0a30ca17e | underdog | Roberto Piccoli | Shots on Target | under | 0.1442916251697374 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|31a03166-3f76-4ae6-9abe-409d9ef243d0 | underdog | Cam Little | FG Made | under | 0.1442121421798081 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|56fa8687-196b-4c40-b356-dd54985a55d3 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.1441384995953865 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|72946955-4551-4e11-9ac7-045cf3a40fdf | underdog | Sam Darnold | Pass Attempts | under | 0.1438475849616487 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|24260bd5-87c0-46b8-923a-d435f5ce967b | underdog | Myles Murphy | Sacks | over | 0.1435832918511665 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|7d761891-9c3c-4710-b52c-dee33c17d73a | underdog | Jeremiyah Love | Rush + Rec Yards | under | 0.1432537653626603 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| prizepicks|15449777 | prizepicks | Jeremiyah Love | Rush Yards | under | 0.1422832017672558 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15533215 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.1421721269280211 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|e4b2c31f-0dd9-4925-9430-2609f8120f12 | underdog | Nathaniel Lowe | RBIs | over | 0.1420708634330925 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|42b5ae82-0c54-4e31-82d8-321576d4f729 | underdog | Jaylen Warren | Receptions | under | 0.1418073771333056 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|b68c8b49-392f-43ab-9f07-845fca3cf923 | underdog | Sterling Shepard | Receptions | under | 0.1418065028454121 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|ea65ec86-8f7b-441c-abcd-96c4d2875e7a | underdog | Yandy Díaz | Total Bases | over | 0.1417073170731705 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d9d295c7-29d5-42e6-9e36-ce234bd68880 | underdog | Cooper Kupp | Receiving Yards | under | 0.1409129241893112 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|dd75a4f0-e019-4940-8bee-29e910915ac8 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1407492024446349 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|b3e974cc-7bad-4c8d-bd3a-4e69583465e0 | underdog | Ollie Gordon | Receptions | under | 0.1405305766441357 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533338 | prizepicks | Juwan Johnson | Rec Targets | under | 0.140066644958984 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|dc36e57e-c99e-4f80-8989-e418fed3d013 | underdog | Kyle Pitts | Receptions | under | 0.1395988502616334 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|3427cfc2-400e-4ab3-b822-f5309b46fc3e | underdog | Jacory Croskey-Merritt | Receptions | under | 0.1395620251411317 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15449767 | prizepicks | Daniel Jones | Rush Yards | under | 0.1393913251517721 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|3e4c8b7e-112e-49de-8429-6ba722d284fe | underdog | Jason Sanders | FG Made | under | 0.1393458974198749 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|5dd8b31c-2018-482d-91c2-eee7169dfe6c | underdog | Malik Willis | Rush Yards | under | 0.1391639516758371 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|55b09c9a-087e-4eab-b8a5-d94089b562fd | underdog | Teoscar Hernández | RBIs | over | 0.1388353155469837 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15533220 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1388040432760633 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|e1f11d54-d68b-4059-82b3-d00643b97813 | underdog | Rachaad White | Rush Yards | under | 0.1385735263545163 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|a1d9d7c3-f635-4d7e-a68c-cac07a226bbf | underdog | Jo Adell | RBIs | over | 0.1381966221048577 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|54d0138c-923d-48a0-b27c-a148af1901e5 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.1380953900749995 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|f9adeead-269e-4779-bdfa-4513c0d7a0f1 | underdog | Arik Armstead | Sacks | over | 0.1375746129344438 | 2026-10-11T05:47:48Z | 2026-10-11T13:30:00Z |
| underdog|09fee6d3-b8f2-47c5-86eb-8e5cbaf08db0 | underdog | Cairo Santos | Kicking Points | under | 0.1374245668310596 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|e8c57134-84d4-449d-a4d9-f54117dc686b | underdog | Evan Engram | Receiving Yards | under | 0.1369976122409074 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| prizepicks|15557962 | prizepicks | Dontayvion Wicks | Recs | under | 0.1368370775589878 | 2026-10-11T05:47:48Z | 2026-10-11T09:30:00.000-04:00 |
| prizepicks|15487604 | prizepicks | Cairo Santos | Kicking Points | under | 0.1366754180481727 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|fc71cb20-e7fe-43ee-adcf-cd1f8720d31e | underdog | Mookie Betts | RBIs | over | 0.1366337168476205 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15605200 | prizepicks | Mark Andrews | Recs | under | 0.1361256072935218 | 2026-10-10T05:51:08Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|5ea8f546-a6d4-465b-9b90-236169b77e7a | underdog | Andre Szmyt | FG Made | under | 0.1357302867117852 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|0addefb5-46dd-4c15-bee9-da21df8f0b84 | underdog | Cooper Kupp | Receptions | under | 0.1356011554882877 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|43a23ae9-1975-4a13-a3c3-cd928190b275 | underdog | Konata Mumpfield | Receiving Yards | over | 0.1355805680356587 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|78c4eb32-88f6-4489-9456-f5ef5baafb43 | underdog | Shohei Ohtani | RBIs | over | 0.1352506801399144 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15533345 | prizepicks | DK Metcalf | Rec Targets | under | 0.1349627874253393 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|289234d9-2e97-4c1b-9154-7abbdcc0652d | underdog | Marvin Mims Jr. | Receptions | under | 0.1346068288876304 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|de950b28-dca7-4a8f-92e1-86c731bb7711 | underdog | Ryunosuke Sato | Shots Attempted | under | 0.1342790122946053 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|1f83e6d3-6a19-4120-998c-b3ca1718de9f | underdog | Shohei Ohtani | Total Bases | over | 0.1338535414165665 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449779 | prizepicks | Derrick Henry | Rush Yards | under | 0.1337962116634731 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|dcb9f875-4c50-4055-b46b-e16020cf2d7e | underdog | J.K. Dobbins | Receptions | under | 0.1336864857180996 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|b9c6b14b-07d8-43a7-a8a5-c7da4d538896 | underdog | Bo Melton | Receiving Yards | under | 0.1335968890947302 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|dbc513e4-003f-4486-8d5f-694c7cb2dc0a | underdog | Jon Rowe | Shots Attempted | under | 0.1333428069065197 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|e1f639e0-947c-4740-a182-725bbc89e523 | underdog | Greg Dulcich | Receptions | under | 0.133306406630307 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|59d44fcf-30cf-4ff8-b002-ff2ec9479624 | underdog | Cam Little | Kicking Points | under | 0.1330125622390986 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|6d2e27ad-1f86-4a90-9a86-8794361bfa68 | underdog | C.J. Stroud | Pass TDs | under | 0.1330035539002533 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|c09df52b-01fa-4f94-9eb3-c4223c74f745 | underdog | Chris Bell | Receiving Yards | under | 0.1327962301900571 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|8810c53a-0aaf-429f-bc7e-83d4b0c761f9 | underdog | Germie Bernard | Receiving Yards | under | 0.1326548409517892 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|071ef0a9-f0d9-4814-92ab-a2cb744371bc | underdog | Raheim Sanders | Receptions | under | 0.1325240013679948 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e90e3fb2-7727-4218-87d5-edcc78743f05 | underdog | Chris Olave | Receiving Yards | under | 0.1323192556349706 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15599456 | prizepicks | Kenyon Sadiq | Rec Targets | under | 0.1321668662467615 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|ff2c5601-bd2f-4fb6-80e2-acb129c136f8 | underdog | Deshaun Watson | Pass TDs | under | 0.1312661382896718 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15605203 | prizepicks | Colby Parkinson | Recs | under | 0.131247358061172 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|87e06a6b-d10a-4b25-8c65-9d5ef5c235f6 | underdog | Keenan Allen | Receiving Yards | under | 0.1309842929602362 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15525501 | prizepicks | Josh Downs | Recs | under | 0.130950022097498 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|30a5bb2a-b533-48db-bafe-7b1a7eabfb12 | underdog | Kenan Karaman | Shots Attempted | under | 0.130805662879993 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| underdog|9c10439e-b139-452e-a50d-95ad6ea3b093 | underdog | Trey Smack | Kicking Points | under | 0.1305833255223802 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|97ba40d3-4a16-43a4-86a3-56b8321e0ce1 | underdog | Josh Allen | Rush Yards | under | 0.1305140998274795 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| prizepicks|15605190 | prizepicks | Justin Jefferson | Recs | under | 0.1302318472434762 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15449902 | prizepicks | George Kittle | Rec Yards | under | 0.1301993571797353 | 2026-10-11T05:47:48Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|5aa3cd14-8a09-43b5-b4d1-8afdd59188c4 | underdog | Jalen Hurts | Rush Yards | under | 0.1294518975548588 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|4f3c2c58-5850-4daa-b007-52b33289f704 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1287914869647599 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|f426a0da-e685-4536-ad48-93f182cbc7de | underdog | Josh Allen | Pass TDs | under | 0.1285629331990532 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| prizepicks|15542803 | prizepicks | Elia Caprile | Goalie Saves | under | 0.1279169815399686 | 2026-10-08T06:06:51Z | 2026-10-11T14:45:00.000-04:00 |
| prizepicks|15494588 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.1276848732716379 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|74a22269-a367-4783-ada4-cd05e74c9c6c | underdog | Garrett Mitchell | Batter Walks | over | 0.1274390243902439 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|4f95f1be-db30-42a2-8ee3-ff3b68b0df71 | underdog | Cody White | Receptions | under | 0.1272089090314258 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|a1c455e6-5404-463d-99e9-4535b988d0d8 | underdog | Jon Ander Olasagasti | Shots on Target | over | 0.1271010788156282 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|60e95349-564d-4aeb-b400-5b1238745cac | underdog | Dalibor Svrcina | Aces | over | 0.1270396690769569 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|334aa8d6-75f8-4548-af20-c04ce18f95b0 | underdog | Harrison Mevis | FG Made | under | 0.1267568917612062 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|86eb2052-71bd-4a94-8ffe-d4e08e5e2be2 | underdog | Jay Robinson | Shots on Target | over | 0.1263611682778579 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|13fcd8a1-dcb8-4764-ae38-fc3ae0d8ddd7 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.1263354720085338 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|7d568917-ac73-4b38-bee5-881c2affc534 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.1260287598410046 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|dd31cc96-b109-46e1-9482-aa25549d982b | underdog | Aaron Jones | Receiving Yards | under | 0.1257008609308435 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|8fd4f5cc-d9f8-45d5-a597-9dd5909b1e2c | underdog | James Cook | Rush + Rec Yards | under | 0.1255606388412681 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|3c834586-5751-4ad9-a80f-80b81ba00685 | underdog | Hugo Gonzalez | Shots Attempted | under | 0.1254689550743722 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|cf582d01-c13e-440a-ade2-f799db46bbd0 | underdog | Harrison Mevis | Kicking Points | under | 0.1254356679868777 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|2e56c036-81e4-4bfc-8207-d2472b66db5a | underdog | Mikel Oyarzabal | Shots Attempted | under | 0.1252484499204212 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|dc33ee41-5b73-450f-9579-942a7fb90cc6 | underdog | Chris Bell | Receptions | under | 0.1248610668114653 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|fcd73857-62c2-47c1-845c-aeb23636ac93 | underdog | Jameson Williams | Receptions | under | 0.1239347870102316 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|08d90960-04e8-4127-a3a6-f5b777643640 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1238546016596884 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| prizepicks|15449913 | prizepicks | Mark Andrews | Rec Yards | under | 0.1238313359249307 | 2026-10-08T06:06:51Z | 2026-10-11T20:20:00.000-04:00 |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|2eb5b6b8-64a4-43d2-83cd-5b79c40609eb | underdog | Chase DeLauter | Total Bases | over | 0.123544051767048 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|4a51f4a0-4e09-4e80-b5c6-bdec32063937 | underdog | Wan'Dale Robinson | Receptions | under | 0.1232699072517647 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|387d8619-4484-46a0-8bbf-45010b00e34e | underdog | José Ramírez | RBIs | over | 0.1231774761186525 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|561005f1-0832-4c2e-b79e-2e99eb00a1b8 | underdog | Emanuel Wilson | Rush + Rec Yards | under | 0.1230257221171684 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|a6a7894d-bcd4-4fbb-b247-c4f6a880a471 | underdog | Roberto Piccoli | Shots Attempted | under | 0.1229530908530861 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|b414ca29-1cd7-4ae5-8d1e-46b44db942a9 | underdog | Aaron Rodgers | Pass TDs | under | 0.1223049911798246 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15599431 | prizepicks | Khalil Shakir | Rec Targets | under | 0.122300899095646 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15605198 | prizepicks | Mike Evans | Recs | under | 0.12222533688652 | 2026-10-10T05:51:08Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|c01e24f7-4ebe-4609-9fad-5ddd93a634e3 | underdog | Keon Coleman | Receptions | under | 0.1219943369127956 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15599449 | prizepicks | Malik Washington | Rec Targets | under | 0.1219103405315166 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|28df77fe-6c84-4cee-a1ee-18c7d3b0a090 | underdog | Shohei Ohtani | Hits | over | 0.1219051471829866 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|9697c57c-fd71-4705-8337-cc88f51ebcdc | underdog | Rodrigo Mora | Shots Attempted | under | 0.1218442727562265 | 2026-10-09T20:57:57Z | 2026-10-11T10:30:00Z |
| prizepicks|15480028 | prizepicks | Cooper Kupp | Rec Targets | under | 0.1218370483861323 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15533333 | prizepicks | Tre Tucker | Rec Targets | under | 0.1217967134567569 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|ad527c65-e894-4792-9939-33f2e5447d85 | underdog | Jaylen Warren | Rush Yards | under | 0.1210157429563112 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15480098 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.1208795095025114 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|7a72e68d-e184-4336-9853-cbcd86d8d1aa | underdog | Drake London | Receiving Yards | under | 0.1208786058024502 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|6e5cef1c-3d52-4748-bbb4-14a7077ab89a | underdog | Jake Bates | FG Made | under | 0.1206348633535515 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|4cbfe398-89db-47fd-a922-bb6c6fe5bc2b | underdog | William Contreras | Hits + Runs + RBIs | over | 0.1205330311072093 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|ca1ca15d-5035-4949-8c44-ae05c6b1801a | underdog | Jermaine Johnson | Sacks | over | 0.1200680172183055 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|46744b45-9b88-44ee-8b93-8625f2bcb5dd | underdog | Trey Smack | FG Made | under | 0.1200175731478777 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15449885 | prizepicks | Matthew Golden | Rec Yards | under | 0.1196070275313497 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15605195 | prizepicks | Tyjae Spears | Recs | under | 0.1194166763165164 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|d39abbd5-18c3-4e54-a4b9-aaf8d5a2184f | underdog | Freddie Freeman | Total Bases | over | 0.1192173839232662 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|95d96654-2ef3-428e-97ce-540633d27a64 | underdog | Elijah Ponder | Sacks | over | 0.1185893411576372 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15449891 | prizepicks | Isaiah Likely | Rec Yards | under | 0.1181390038168248 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|2d075bc2-6d96-47f6-9df2-6e38e3326f93 | underdog | Ollie Gordon | Rush Yards | under | 0.1180008071369889 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|a9d6e187-d2eb-4231-96f1-5c497555381c | underdog | Lucas Da Cunha | Shots Attempted | over | 0.1179801917395407 | 2026-10-09T06:09:55Z | 2026-10-11T10:30:00Z |
| underdog|0ad2d55e-7eac-413b-9d22-5b24c6e2e505 | underdog | DeForest Buckner | Sacks | over | 0.1173785258181736 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|0535d0fb-5048-4c93-a64b-96fd1ef5c355 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.116157619856066 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|faf508eb-b383-4d71-8610-4f9ad4eb2e82 | underdog | Pat Freiermuth | Receptions | under | 0.1158911584941863 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|8b717fc9-4388-4f84-bad0-9cb6f4327d0e | underdog | David Montgomery | Receiving Yards | under | 0.1151674716964025 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15614079 | prizepicks | Katie Boulter | 1st Set Total Games Won | over | 0.1150363918622577 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|6800bc1f-b947-41a7-b1a1-8d85e8e2ed73 | underdog | Denzel Boston | Receiving Yards | under | 0.1149072496798576 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|73221e27-8e3e-4183-acea-22d5334d59ad | underdog | Christian Pulisic | Shots on Target | under | 0.1146715938144284 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|a6f8eaf1-85f1-4fda-8d3c-2b888d7352f5 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.114575137794336 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|f6248a9b-7a6e-4113-9aab-4941aaba8afb | underdog | RJ Harvey | Receptions | under | 0.1145560550822413 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|78fed814-b601-449c-b395-4b0300fecf23 | underdog | Jake Bauers | Total Bases | over | 0.1143320964749535 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|758568c7-c919-42c9-8cbe-8940d6735c66 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.114211803544009 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|0ab95d0d-f2f3-4328-910e-5266361c388a | underdog | John Franklin-Myers | Sacks | over | 0.1142083385956842 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|aef219ec-beec-40aa-9580-c33e005e5e0f | underdog | Matthew Golden | Receiving Yards | under | 0.1139781917753548 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|f43b99b1-c0c6-4a4c-9e75-4c8afbf1a68c | underdog | Jonathan Aranda | Total Bases | over | 0.1139370078740158 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|abe573f9-1d74-4e1d-b04f-aa980d6ae1da | underdog | Jonny DeLuca | RBIs | over | 0.1139244103438475 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e51e69b1-5a6d-43c8-bc97-2f0a8001d399 | underdog | Kendre Miller | Receptions | under | 0.1138562351080293 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|20858ba0-bb8e-4aea-9cad-0c8ebb1a66e8 | underdog | Bhayshul Tuten | Receptions | under | 0.1136842890276715 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|289ee770-77f0-4870-90bf-8e9374483441 | underdog | Gunnar Helm | Receiving Yards | under | 0.1133307900155715 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|24cd8df3-de9c-439f-a464-fde46d0c3c56 | underdog | Jared Goff | Pass TDs | under | 0.1129533261839722 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15449908 | prizepicks | Jahmyr Gibbs | Rec Yards | under | 0.112865296774001 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|62723aca-ce3b-4df0-9c30-ef1cd7749860 | underdog | Job Ochieng | Shots on Target | under | 0.1127017763679212 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|e0371795-229b-4ba8-a826-44b3549c775c | underdog | Will Smith | RBIs | over | 0.1126523389559607 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c2a6b932-c246-4bfa-992d-15cc8f641825 | underdog | Michael Mayer | Receiving Yards | under | 0.1124092973263886 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|465edc4e-da49-443e-b06a-58a2b82715fa | underdog | Joel Monteiro | Shots Attempted | under | 0.1122178447323365 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|bd89c92b-425b-48d5-9228-deb99dfcbb46 | underdog | Teoscar Hernández | Total Bases | over | 0.1120789109367789 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|97b81c66-8c31-43e3-8094-a40cb90242be | underdog | Christian Yelich | Total Bases | over | 0.1120789109367789 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|c0bd9a94-cf50-4ce2-b5b3-f9a919d8ec88 | underdog | Yandy Díaz | RBIs | over | 0.111859761320162 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|c1a4bc19-4a33-4905-a508-3edc8ca6dd69 | underdog | Rhamondre Stevenson | Receptions | under | 0.111845646463508 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|ff1b71e8-14a7-49c3-9475-05528fcdd5aa | underdog | Dre'Mont Jones | Sacks | over | 0.1117229865667461 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|ca593b78-6206-47d9-88e7-ea597bfa44ef | underdog | José Ramírez | Batter Walks | over | 0.1111346765641569 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15622906 | prizepicks | Terry McLaurin | Rec Targets | under | 0.110992135394928 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|6ca1d79c-5d56-4d25-bb3c-3b1ea60138bc | underdog | Darnell Mooney | Receptions | under | 0.1106931724826717 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|d3c29019-a31b-4965-b714-fcddad402ac4 | underdog | Jaylen Waddle | Receptions | under | 0.1106734036857285 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|b5c478c0-f44a-452e-b52e-8ec57b00b1e0 | underdog | Brice Turang | Total Bases | over | 0.1105149752208576 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|f6e9d50a-abfe-437e-9605-adcf61849a5c | underdog | Deshaun Watson | Rush Yards | under | 0.1103708651501996 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|f16a5dd7-0a11-4b3c-8573-75b726a574f6 | underdog | Freddie Freeman | Hits | over | 0.1101321850803321 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|fdd70aa8-d95e-45fe-913f-a70054e3de07 | underdog | Keaton Mitchell | Rush Yards | under | 0.1100167877785137 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|af35b71f-542d-4132-91c1-b0345c698752 | underdog | Jacob Martin | Sacks | over | 0.1099009963929575 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| prizepicks|15533223 | prizepicks | Josh Downs | Rec Targets | under | 0.1095182341995211 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|09f306da-6fb7-4875-a6f0-0eb62ab34cf9 | underdog | Odafe Oweh | Sacks | over | 0.1094230755007361 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|8e0220ac-f788-4865-8f31-f754b779e487 | underdog | Denzel Boston | Receptions | under | 0.1094145693487267 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|08c7cc9d-8a0c-4fcd-8051-b503401d0ab1 | underdog | Carl Granderson | Sacks | over | 0.1092861146863093 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|e3874035-563b-489c-9353-575c63ae7399 | underdog | KC Concepcion | Receptions | under | 0.108986568809092 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|5b2855a8-a267-4c45-a9fb-940f689fed9b | underdog | Nikola Stulic | Shots Attempted | under | 0.1088406815145727 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| prizepicks|15576399 | prizepicks | Jared Goff | Pass TDs | under | 0.1084012634435631 | 2026-10-09T06:09:55Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|5f055e40-4f2c-4bbd-9770-6b31b95b85f8 | underdog | Nolan Smith | Sacks | over | 0.1079415155551957 | 2026-10-11T05:47:48Z | 2026-10-11T13:30:00Z |
| prizepicks|15606273 | prizepicks | Khalil Shakir | Fantasy Score | under | 0.1074900904271655 | 2026-10-10T05:51:08Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|0aa56a42-1590-4b7e-a7ae-2c4a96293708 | underdog | Brayan Rocchio | Runs | over | 0.1074235807860262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15533061 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.1072789607453067 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|bf25c1c1-6597-4067-9c1d-3638032853f9 | underdog | Matt Gay | FG Made | under | 0.10681189266177 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15598638 | prizepicks | Matthew Stafford | Fantasy Score | under | 0.1059909354453244 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15605199 | prizepicks | Sam LaPorta | Recs | under | 0.1054567516001454 | 2026-10-10T05:51:08Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|56e7a848-9591-4052-8a7d-2a19200848b2 | underdog | Kyle Tucker | Hits | over | 0.1054360688190638 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|7c4a2ec4-e671-4be1-8b9b-4dcece285ff8 | underdog | Gessime Yassine | Shots on Target | over | 0.1053772533391154 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|6ef5fd6e-2017-4be4-87d5-2cccaab82a24 | underdog | Brayan Rocchio | Hits | over | 0.105146286744669 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6d951bee-ca80-4576-8208-681924fd93ae | underdog | Ben Skowronek | Receiving Yards | over | 0.1049903304490513 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|ea078d75-4106-447d-913c-5973f642bd93 | underdog | Rome Odunze | Receiving Yards | under | 0.1047095644361859 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|3d5cf33b-5db6-4e01-891a-0752515149cb | underdog | Cooper Pratt | Runs | over | 0.1046838547586289 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4f7ccb76-a998-49cd-aade-4ad2e3c9bcfe | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.1045728146988547 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15533057 | prizepicks | Luther Burden III | Rec Targets | under | 0.1044032753944964 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|7adef54f-511d-49ab-a583-48c15b84f557 | underdog | Adil Aouchiche | Shots on Target | over | 0.1043269577787521 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| underdog|32d31070-c398-4840-bfa6-77a2aefc84fa | underdog | Travon Walker | Sacks | over | 0.1042047057646978 | 2026-10-11T05:47:48Z | 2026-10-11T13:30:00Z |
| underdog|6e84efd1-d3c3-42db-ac40-68e36bf10249 | underdog | Amine Gouiri | Shots Attempted | under | 0.104152285155024 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|ce5ae764-f911-47ba-8431-67d5b489200e | underdog | Brian Robinson | Rush Yards | under | 0.1037498664931149 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|f2abe0a4-bf61-4cce-8b6b-383e4bac62b0 | underdog | Tory Horton | Receiving Yards | over | 0.1032629529638766 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|dde13221-2016-44fc-9a67-89c4c96ace8b | underdog | Douglas Luiz | Shots on Target | over | 0.1031128519230439 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|2c02128b-c63f-4c7a-93b2-921f656f115e | underdog | Jake Bates | Kicking Points | under | 0.1029821419012476 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|6e9f57c6-06e0-4922-bea7-fa854121d4d1 | underdog | Garrett Mitchell | Hits | over | 0.102916642043505 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|fcea3f53-7169-4621-89e4-46becb668f66 | underdog | Christian Yelich | Batter Walks | over | 0.1028795530246051 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|b73b684e-50a1-481e-9206-a976600fa14d | underdog | Devontez Walker | Receptions | under | 0.1028513851406096 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|b1ec12ff-7d53-4e31-bd7d-c71a820cbc31 | underdog | Jacory Croskey-Merritt | Receiving Yards | over | 0.1025347661906796 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e03fca21-03e1-49b1-95d5-866b1580abad | underdog | Jaylen Waddle | Receiving Yards | under | 0.1025169630404604 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|bcc1629c-1414-46da-b831-bc4ebf7dde12 | underdog | Jowon Briggs | Sacks | over | 0.1023725022157499 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15599441 | prizepicks | Kayshon Boutte | Rec Targets | under | 0.1022705198609968 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|8c888a60-93ed-44d5-b569-d948d9892544 | underdog | William Contreras | Hits | over | 0.102207453183262 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|4cde131d-0ed8-42db-8735-94174b8d667f | underdog | Tre' Harris | Receptions | under | 0.1021258695107437 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| underdog|3a0a5fb4-8fec-4c1c-a4a3-990ec0962635 | underdog | Will Smith | Hits + Runs + RBIs | over | 0.1016822333860878 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|e6dd44bb-c562-401c-aa59-e4bb51c4db13 | underdog | Geno Smith | Rush Yards | under | 0.101616388480121 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|4c6863d1-8a63-4019-9eb9-170704f07242 | underdog | Jo Adell | Total Bases | over | 0.1012237762237762 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ad171ced-0801-44a7-b745-24f8d2812c12 | underdog | Junior Caminero | Runs | over | 0.1011000144738747 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|def7beb5-8738-4640-84dc-c0528f5b699a | underdog | Diego Moreira | Shots on Target | under | 0.1009374689134036 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|2e1069d1-ff71-466a-ac9a-8bb9bd9ba83d | underdog | Jackson Chourio | Hits | over | 0.1007073520271667 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4241a742-4708-4e8d-b8d9-a67643642c3e | underdog | Tyler Loop | Kicking Points | under | 0.1004524819334912 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|603e79f6-045e-429d-bd7c-96054c888e7d | underdog | Bijan Robinson | Receptions | under | 0.1002136113334525 | 2026-10-07T05:55:02Z | 2026-10-12T00:20:00Z |
| underdog|c16a1553-7ce9-41e3-94dd-35dcba1d50e9 | underdog | Dalton Kincaid | Receptions | under | 0.1001322302115007 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15622904 | prizepicks | Terry McLaurin | Recs | under | 0.1000636808088266 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|a48b9cac-5835-4e17-bb94-488f64c2c4f2 | underdog | Yandy Díaz | Batter Walks | under | 0.0997986126650258 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|8b500992-025e-412f-8c3f-a4758f37a2cd | underdog | RJ Harvey | Receiving Yards | under | 0.0997242863509314 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| prizepicks|15533334 | prizepicks | Romeo Doubs | Rec Targets | under | 0.0995415876657849 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|c22ae601-6e01-4914-ac59-7455a5c99d05 | underdog | Garrett Mitchell | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|23134ad5-b95d-47bc-9b05-45e53638a825 | underdog | Kyle Tucker | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|49403d31-be54-4fe0-9e8a-d308740d099f | underdog | Taylor Walls | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0d9ea553-5342-487d-9e05-dfebe5c8ab46 | underdog | Joey Ortiz | Total Bases | over | 0.0994475138121546 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|d149922a-7aeb-4f9a-b519-a5c2490f0b89 | underdog | Patrick Bailey | Total Bases | over | 0.0994475138121546 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15542574 | prizepicks | Arijanet Muric | Goalie Saves | under | 0.0993513856075698 | 2026-10-08T06:06:51Z | 2026-10-11T12:00:00.000-04:00 |
| underdog|ec4d13b7-9813-421f-9b59-309bf282e304 | underdog | Angel Martínez | Runs | over | 0.099014659937515 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e388107d-71de-4d5c-9c18-12e453e8029a | underdog | James Cook | Receptions | under | 0.0989680426406112 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|08897ad0-a69d-4127-84f5-c12b64984212 | underdog | Najee Harris | Rush + Rec Yards | under | 0.0988376852948689 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|8a309dcf-a85e-41ea-8de6-4629ff76be0f | underdog | Tijjani Noslin | Shots on Target | under | 0.0988181596512371 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|7f9ae422-c3a8-4fb9-bb34-8f0118fb0869 | underdog | Mike Gesicki | Receiving Yards | under | 0.09881565636636 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|1c78bf81-9285-46f5-bebe-eeb69631a4b8 | underdog | Brenton Strange | Receptions | under | 0.0988096883441336 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|ce0299f1-317b-4d65-8a9a-c24eb465ecb1 | underdog | Amine Harit | Shots on Target | under | 0.0982575075529187 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|066f0f9e-b6c9-47d2-b540-1f55c52394f5 | underdog | Joey Ortiz | RBIs | over | 0.0981818181818181 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|ce2bec88-2b1e-4517-939c-450ab2860797 | underdog | George Holani | Receptions | under | 0.0972730613848503 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|7e077e54-d21e-4bb4-a692-74ff7da1dde7 | underdog | Andrew Van Ginkel | Sacks | over | 0.097175684944906 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|4d318284-ffac-4f92-99ab-5ec7a8ab3950 | underdog | Arnaut Danjuma | Shots Attempted | under | 0.097148611959777 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|cabf69d4-23b6-4e59-9c84-f1f400fc0216 | underdog | Matt Gay | Kicking Points | under | 0.0968799853435736 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15449886 | prizepicks | Christian Watson | Rec Yards | under | 0.0967429912749512 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15625124 | prizepicks | Felix Auger-Aliassime | Aces | under | 0.0965569875121911 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|020e3f8c-5c74-4741-abf7-323b92b10dd3 | underdog | Travis Bazzana | Hits | over | 0.0963112448193084 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|07405cba-3d11-4f03-aeeb-2884c179f9eb | underdog | Victor Mesa | Runs | over | 0.0962432915921288 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b0f42392-0953-41ef-b1cc-7eef2984ac77 | underdog | Jason Sanders | Kicking Points | under | 0.0961338799210567 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|9b57a37f-f1cc-4ab5-a354-5c3317360da1 | underdog | Joey Ortiz | Hits | over | 0.095720022541028 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|411f90d3-97a1-4da2-9da0-8ba6b0829737 | underdog | Theo Johnson | Receiving Yards | under | 0.0956572820272645 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|3beb9741-18c3-459a-b1b7-0b3dcbcd30db | underdog | Zach Sieler | Sacks | over | 0.0955337158204928 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|625f44f8-5951-489a-85bb-13cfca832f4a | underdog | Brice Turang | Hits | over | 0.0953584302115455 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|acc952e5-7186-4231-90b8-ecf1d9533cc9 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.0952464995163607 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|149f488d-ceef-4a0b-8b82-aba5c470e127 | underdog | Samuel Chukwueze | Shots Attempted | under | 0.0951244227186777 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|f0c777ae-422c-428b-ad7b-fd5c395e3071 | underdog | Carnell Tate | Receptions | under | 0.0950939470990873 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|85486ca9-90da-4c1a-be12-ffe17eb113db | underdog | Jo Adell | Hits + Runs + RBIs | over | 0.0949273782322186 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|8f27c991-9406-4e0d-b316-76be90b575cc | underdog | Trevor Lawrence | Rush Yards | under | 0.0948536734372971 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|cd29425c-6a1c-4424-b310-9b0bdf717c81 | underdog | Gauthier Hein | Shots on Target | under | 0.0948197060267735 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00Z |
| underdog|814b06d9-b8e2-413b-8e3a-9735fe37a96c | underdog | Luis Lara | RBIs | over | 0.0946969696969696 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|a7bc58fe-e3c4-4871-b766-36d946c6a01f | underdog | Mikel Oyarzabal | Shots on Target | under | 0.0944230304164159 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|9184703a-2117-4987-8453-9753dbe0869c | underdog | David Bailey | Sacks | over | 0.0943576831156814 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|c985be79-5602-435b-9f4a-ec0b877b854e | underdog | Drew Sample | Receptions | under | 0.0941816682256289 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|4cec8ecb-7ad4-4940-b3fc-965e84897afa | underdog | Drew Sample | Receiving Yards | over | 0.0941525171526582 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|93e20e67-25d3-4e0c-ad40-887c16e3a738 | underdog | Justin Herbert | Rush Yards | under | 0.0941216129566173 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|17572c88-b308-4c8b-8481-3af931e19c72 | underdog | Derrick Henry | Receiving Yards | over | 0.093917869973369 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|492d1286-c136-42f8-89cf-24690d67dd15 | underdog | Lucas Cepeda | Shots Attempted | under | 0.0934642840507938 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|11136590-0d1f-4acc-9ea5-cd6775bc7114 | underdog | Darnell Washington | Receptions | under | 0.0932131482165088 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|b487247b-6ec1-4531-ab9a-f8d7f73a8001 | underdog | Samaje Perine | Receiving Yards | over | 0.0931591293281145 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|0a98a584-e688-48bc-b132-9ecfd9a727f1 | underdog | Kayshon Boutte | Receptions | under | 0.0931115163345064 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|7b6a2d3e-11d3-4977-8e37-59858bf712d2 | underdog | Olamide Zaccheaus | Receptions | under | 0.0930780314349503 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|0241a595-f3b2-45da-8145-2d2ce07fc1a3 | underdog | Tee Higgins | Receptions | under | 0.0929694953548248 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15533218 | prizepicks | Christian Watson | Rec Targets | under | 0.0928717406603493 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|611fc835-df50-4f9e-b50b-73d68f691dc4 | underdog | Cameron Dicker | Kicking Points | under | 0.0925923918660095 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|b9ac92c0-bbc8-4c5e-9179-c1bfe8d6c86e | underdog | Kenyon Sadiq | Receptions | under | 0.0923062390004479 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|6fc172f4-5c53-47d5-aaa0-0557a3b2401c | underdog | Rachaad White | Receptions | under | 0.0922505995531172 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|0b9cc5d0-8455-4163-99be-bf8e3deffd08 | underdog | Patrick Cutrone | Shots Attempted | under | 0.0920317577329846 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|2a618a4e-4536-4379-8084-62511997dfd8 | underdog | DeMario Douglas | Receptions | under | 0.0917616202676058 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e348ae16-805c-4257-8c3f-bcdae472b176 | underdog | Kendre Miller | Receiving Yards | under | 0.0917235257260813 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|f6b48357-fcc3-4166-a635-c2c60a265fc3 | underdog | Weston McKennie | Shots Attempted | under | 0.0916462679278388 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|d2887c8e-fd22-43ae-a674-3fe85ac2a968 | underdog | Ryan Vilade | RBIs | over | 0.0915923945335709 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9f5b253e-0e5e-4963-9dc3-94f40089b3c7 | underdog | Christian Watson | Receptions | under | 0.0915460671690993 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15533054 | prizepicks | Colston Loveland | Rec Targets | under | 0.0909847081155098 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|fef2c26a-58e0-40d4-9475-b3fb706d9cf9 | underdog | Tony Pollard | Receptions | under | 0.0907149093128795 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|e9f69f58-1beb-4de9-8110-0a3d94dada53 | underdog | Victor Mesa | Total Bases | over | 0.0906717017515668 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9df7bc1f-f451-4027-91cd-916d4fb686eb | underdog | Keaton Mitchell | Receiving Yards | under | 0.0902219610265201 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| underdog|96af368d-b750-47ab-ae81-ed9a7790f27c | underdog | Danny Namaso | Shots Attempted | under | 0.0901882454758903 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|834874ea-0c75-4fb4-8a40-c0ddc342ee17 | underdog | D'Andre Swift | Receptions | under | 0.0901552158033653 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|ce4e9f34-09da-4672-b076-7b7130de1b2a | underdog | Deebo Samuel | Receptions | under | 0.0900977552209125 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|04dd6307-7f03-4b6a-9f72-4de43d33a7d6 | underdog | Ryunosuke Sato | Shots on Target | under | 0.0897311743589852 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|123a774d-3b72-4068-a499-6bf28d0b1e03 | underdog | Tre Tucker | Receptions | under | 0.0897017801151375 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|0cb3e70d-4db1-4e8f-93f9-9310dfea2701 | underdog | Daniil Medvedev | Aces | under | 0.0895580010049378 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|66aa5abd-6385-4823-ac86-d0b240a94f8e | underdog | Travis Bazzana | Runs | over | 0.0891891891891892 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15605188 | prizepicks | Romeo Doubs | Recs | under | 0.0890068433576546 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|8f2816cf-0628-4963-8b2a-82ea1015aa29 | underdog | George Holani | Rush + Rec Yards | under | 0.0889255157795797 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|4896d960-2c35-4fda-8516-4f82c2063d39 | underdog | Max Muncy | Batter Walks | under | 0.0880119397743733 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|ff871fdc-1684-40cc-a922-1e31f1b92584 | underdog | Cameron Dicker | FG Made | under | 0.0877580880115889 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|c289248d-cfaa-4879-89cf-3c0ba63b1a52 | underdog | Keinan Davis | Shots on Target | under | 0.0877224402576258 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|04a90fa0-b3af-4119-b9f1-d7460f453a2c | underdog | Rolando Mandragora | Shots Attempted | under | 0.0876597754181294 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| underdog|36a18375-6519-4861-9922-a146215318c5 | underdog | Richie Palacios | Batter Walks | over | 0.0875680580762249 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|e20cb9a5-38dd-4f2f-a8d4-3468a3c668b6 | underdog | Will Reichard | Kicking Points | under | 0.0875310244055148 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|6b560716-5977-41a9-b3c5-771e315b55a6 | underdog | Jake Elliott | Kicking Points | under | 0.0874310087586351 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|0fcbffa6-988c-451f-87ef-206e9fddf12b | underdog | Kyle Williams | Receptions | under | 0.0873903765218927 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|16daaff9-309e-4ff5-a04f-c01f82a2cea9 | underdog | Will Anderson | Sacks | under | 0.0872948575523089 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15599444 | prizepicks | Keenan Allen | Rec Targets | under | 0.0872007470725335 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|13572e05-92c0-4f3d-9bf7-026da5d1e1a1 | underdog | Yandy Díaz | Runs | over | 0.0867768595041319 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2b5a13a8-1aec-4d70-a260-82c8519882c5 | underdog | Andre Szmyt | Kicking Points | under | 0.0867275022653247 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|59998a7b-e183-4acb-b68f-30e16fac4a0d | underdog | Liam Hicks | Total Bases | over | 0.0866982002768804 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b27cf9e9-1095-4ead-be50-5344cada59d1 | underdog | Martin Baturina | Shots Attempted | under | 0.0864785013196712 | 2026-10-08T06:06:51Z | 2026-10-11T10:30:00Z |
| underdog|f845b7de-39c1-4709-a1e1-eb1c7704397a | underdog | Lazar Samardzic | Shots Attempted | under | 0.086336829755912 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|11a3134c-898a-463a-b722-c0c1a7094dee | underdog | Jadeveon Clowney | Sacks | over | 0.0862785339663382 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15599464 | prizepicks | Gunnar Helm | Rec Targets | under | 0.0858892977824899 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15599430 | prizepicks | Keon Coleman | Rec Targets | under | 0.0857557047580359 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|fbae5726-4d6b-41ec-8862-a9660e524256 | underdog | Bijan Robinson | Rush Yards | under | 0.0847525563870223 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|b6ee13d0-3c33-4d7a-b267-51b6513a099f | underdog | Liam Hicks | Runs | over | 0.0846846846846847 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|3ce54e52-f620-44f5-814d-2db358803882 | underdog | Nik Bonitto | Sacks | under | 0.0846658635801514 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|035d461a-c8c6-4029-90bd-447c5b7a77af | underdog | Jeffery Simmons | Sacks | under | 0.0846498605362922 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15613937 | prizepicks | Katie Boulter | Total Games Won | over | 0.0846111425773317 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|a694e717-4402-4a5e-a72f-01b4638ef063 | underdog | Cooper Pratt | Hits | over | 0.0844009790834429 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4a47c7eb-a243-405f-a9ab-bcdf5f59a80a | underdog | Brayan Rocchio | Batter Walks | over | 0.0843799058084771 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|60f3cfcb-2cb5-40a3-a23c-05a35349c355 | underdog | AJ Barner | Receiving Yards | under | 0.0843014111798384 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|587799b7-44a0-42c7-b782-8576761b2bea | underdog | Brian Thomas | Receptions | under | 0.0841261574860754 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| prizepicks|15599679 | prizepicks | Cam Little | Kicking Points | under | 0.0840163614560148 | 2026-10-11T05:47:48Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|032f47c3-9f81-4409-bcb3-e481fb4f54ef | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.0838997555676377 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|e428f04b-4f1e-4a4a-aaf5-ec88a348c4b8 | underdog | D'Andre Swift | Receiving Yards | under | 0.0838840701297883 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|fe81700b-0fa6-418b-b787-612d64d6e60f | underdog | Alvin Kamara | Receptions | under | 0.0837786368430993 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15599463 | prizepicks | Elic Ayomanor | Rec Targets | under | 0.0833410965632875 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|670067ac-6857-476e-b7c5-4e8ba976c43d | underdog | Kyren Williams | Receptions | under | 0.0831238266239099 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|a34b9ab1-b6af-410b-923c-23ee91624402 | underdog | Arnaud Nordin | Shots on Target | under | 0.0830299929007986 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|a20aa99d-df3c-4600-9a81-db6b4d4c1f11 | underdog | Deebo Samuel | Receiving Yards | under | 0.0827051358298942 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|15599423 | prizepicks | Tyler Allgeier | Rec Targets | under | 0.0823902362312282 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|7edf4227-babd-41fb-a4f6-2bc40bd841f0 | underdog | José Ramírez | Hits + Runs + RBIs | over | 0.082199819661831 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|0eea8879-eab7-49dc-bebc-1d31e6758886 | underdog | Justice Hill | Rush Yards | under | 0.0819635347472056 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| prizepicks|15480030 | prizepicks | Rashid Shaheed | Rec Targets | under | 0.0819174622423938 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15479810 | prizepicks | Drake London | Rec Yards | under | 0.081908695508628 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|cb65e2e2-83c4-4190-ade2-8ba55c28422a | underdog | Steven Kwan | Hits + Runs + RBIs | over | 0.0818522678804714 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d3d7013f-4105-43fa-91ac-580273b5ed8a | underdog | Igor Matanovic | Shots Attempted | under | 0.0818302661100245 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| underdog|c1fbe418-a7dd-4fad-8905-aa1fb05b7eda | underdog | Will Smith | Total Bases | over | 0.0816220581449007 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|4775da9d-a2f2-42b8-a0a3-f83bbace2465 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.0813483118205232 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|04b8fb1a-a39d-417a-8b56-199f0dad0b86 | underdog | Chop Robinson | Sacks | over | 0.0807347591090111 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|5a10c880-37c2-425c-a43e-d6a57e1c159f | underdog | Kerim Alajbegovic | Shots on Target | under | 0.080453897567941 | 2026-10-09T06:09:55Z | 2026-10-11T18:45:00Z |
| prizepicks|15604858 | prizepicks | Jordan Addison | Rec Targets | under | 0.0802825589805311 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|8a1d6843-57ec-460c-b781-35df07ffedfe | underdog | Randal Kolo Muani | Shots Attempted | under | 0.0801527590477695 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|87b4d80e-192a-4e00-b7e2-600320df6b6f | underdog | Edin Dzeko | Shots Attempted | under | 0.0801484727578276 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| prizepicks|15605185 | prizepicks | Colston Loveland | Recs | under | 0.0798793547309021 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|f3bcfdf5-8141-489d-83d7-25ee48fc79a2 | underdog | Tyler Allgeier | Rush Yards | under | 0.0797024117759623 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|36a219cb-f327-4ae1-b78e-4940a21bc39c | underdog | Jalen Hurts | Pass TDs | under | 0.079475355979367 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| prizepicks|15528722 | prizepicks | Cameron Dicker | Kicking Points | under | 0.0793017527260997 | 2026-10-09T20:57:57Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|296f5ffe-51f4-4765-b95f-3e18d5f4908f | underdog | Brian Robinson | Rush + Rec Yards | under | 0.0789728388728099 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|7c6ee5e5-4683-4379-99d6-a7b6a20227d6 | underdog | Freddie Freeman | Runs | over | 0.0788990825688074 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|327cb0c3-03ef-4f5d-9d3c-26372bdaa6f3 | underdog | Cameron Thomas | Sacks | over | 0.0787924237272426 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| underdog|55374dc1-4890-441c-af69-86fc0623a0da | underdog | Domenico Berardi | Shots Attempted | under | 0.0784874968780099 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|00cb13cb-2253-4a16-89e2-d7e49f5267c8 | underdog | Najee Harris | Rush Yards | under | 0.078229324628907 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|1ca1212a-2b6b-4a1e-9741-fa06c174f465 | underdog | Kyren Williams | Receiving Yards | over | 0.0780783225296581 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|9673aa41-6745-4a6f-a004-fe74877ef0fd | underdog | Stefanos Tsitsipas | Aces | under | 0.0780333980544074 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|8cde9532-b05a-40a6-823c-4542c9180df5 | underdog | Jaylin Noel | Receiving Yards | over | 0.0780104072600637 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|fca1ebba-1c1d-4e13-a135-0272391ad284 | underdog | Max Muncy | Hits + Runs + RBIs | over | 0.0775241925197955 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|3b9879c6-977c-4f40-8691-a71e366d2954 | underdog | Juwan Johnson | Receptions | under | 0.0773670488934006 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|4c9fc4a1-429d-4264-aec8-9b2684e69bc6 | underdog | Will Smith | Hits | over | 0.0771954309658208 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449775 | prizepicks | Jared Goff | Rush Yards | over | 0.0771661766978453 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|4aa6d95a-4a8c-40a4-bfd9-82f3f5ac1762 | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.0771190385503421 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|74ee00b4-bb2d-488e-971a-54d34685bb99 | underdog | Will Kacmarek | Receptions | under | 0.0770051896934109 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|f34b8ea9-ff29-4042-8003-a35225c30654 | underdog | Max Muncy | RBIs | over | 0.0767567567567567 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|9ac3e1a2-6bb7-4966-b44e-62a1fd6fc8b6 | underdog | Mookie Betts | Hits + Runs + RBIs | over | 0.0766950942608024 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|67b2e3c8-cd7a-499f-86d9-4342556da29b | underdog | Mookie Betts | Total Bases | over | 0.076545916012921 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|9bdb39b6-d2ba-41d8-8092-ad1db4f7f624 | underdog | Casper Ruud | Aces | under | 0.0761973383597885 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|e1cb8a5d-2b65-43f6-b325-a6727f6a7274 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.0761857882288901 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|94b18365-a58f-4e36-b67b-04191cae3cd7 | underdog | Dalton Kincaid | Receiving Yards | under | 0.0755953191263589 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|54c982e8-946c-470f-b968-54f7868e2184 | underdog | Giorgi Kochorashvili | Shots Attempted | under | 0.0754168684946894 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|346daaa8-cd2a-43de-a47a-ecd51691ba06 | underdog | Josh Hines-Allen | Sacks | under | 0.0752876069014633 | 2026-10-11T05:47:48Z | 2026-10-11T13:30:00Z |
| underdog|29afb740-d596-462e-b47f-b72432e73649 | underdog | Jake Bauers | Hits | over | 0.0752782170654003 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449904 | prizepicks | Cooper Kupp | Rec Yards | under | 0.075270607297545 | 2026-10-07T05:55:02Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|5d2c7501-1861-4e5f-8dc8-6176bb036c0a | underdog | Rachaad White | Receiving Yards | over | 0.0750915736550397 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|691454c0-f345-4914-a569-a73f2b2f42f6 | underdog | Teoscar Hernández | Batter Walks | over | 0.0749791144527986 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|fafa1873-ee71-4b7a-bd33-ad2b3f8caad1 | underdog | Junior Caminero | RBIs | over | 0.0747467481867769 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|86e7ef31-a47e-4802-a478-10b67e4653eb | underdog | Max Muncy | Hits | over | 0.0746826887155556 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15599445 | prizepicks | Josh Cameron | Rec Targets | under | 0.0744811943184808 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|f5a5c826-fcb2-4f72-b80b-6c57a50af3db | underdog | Sam Darnold | Pass TDs | under | 0.0743427570219392 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|df315952-3cec-40db-85e3-d8efd16fbb1c | underdog | Jalen Carter | Sacks | over | 0.0743359303022232 | 2026-10-11T05:47:48Z | 2026-10-11T13:30:00Z |
| underdog|eb290db0-8490-4e77-a304-0fa0d5ce6e08 | underdog | Luka Sucic | Shots Attempted | under | 0.0742529277282342 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|347394ac-81b5-41a9-8fcb-201377429974 | underdog | Bradley Chubb | Sacks | over | 0.0735359375258569 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|0bf383f5-cd90-4375-a60e-b1ff311ede12 | underdog | Bijan Robinson | Receiving Yards | under | 0.0730816046593806 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|bb1faece-9afd-43bb-94ec-2c9ccc581d8b | underdog | Nathaniel Lowe | Batter Walks | over | 0.0729473684210526 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|eff29eb9-994c-46ec-a64d-ebc9f0025f60 | underdog | Junior Caminero | Hits | over | 0.0729261767542962 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d01bef26-4146-4bdc-8b70-590d42445352 | underdog | Treylon Burks | Receiving Yards | under | 0.0728803131621171 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|57e70e89-9d25-4bb6-8532-35e874e2f843 | underdog | Davide Frattesi | Shots Attempted | under | 0.0728509241028978 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|936bc52e-8dc0-4ac7-a262-c453d822f0b5 | underdog | Devaughn Vele | Receptions | under | 0.072592562968332 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|e58b289f-6dd7-4030-ac69-7f5bb2698a88 | underdog | Ante Budimir | Shots on Target | under | 0.0725307618922417 | 2026-10-09T20:57:57Z | 2026-10-11T16:30:00Z |
| prizepicks|15619228 | prizepicks | Botic Van de Zandschulp | Total Games Won | over | 0.072356723476244 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|faee8069-99b5-4b6c-9e52-2fcd4cad3591 | underdog | Cooper Pratt | Batter Walks | over | 0.0719192559712534 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|328fd5df-b812-4adf-aabf-4121767a3610 | underdog | Matthew Stafford | Pass TDs | under | 0.0718820602819038 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|bf5b8b25-d9c6-4b86-9501-7f1430e1b063 | underdog | Travis Bazzana | Total Bases | over | 0.0718093228573808 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|976c6551-201a-43cd-b71d-0521c3f1c4b9 | underdog | Jayden Daniels | Rush Yards | under | 0.071557214280032 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|4267bcfd-4f6b-41cc-83d9-af4ead9f7fa0 | underdog | Will Smith | Runs | over | 0.0712962962962963 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|b2127480-abcb-4644-8a4e-1885ce75907d | underdog | Omarion Hampton | Rush Yards | under | 0.0711138234984402 | 2026-10-09T20:57:57Z | 2026-10-11T20:05:00Z |
| underdog|39f14180-091b-4507-bed7-f12a3b5ac3e7 | underdog | Javier Guerra | Shots Attempted | under | 0.0710948487191501 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|80975a12-2586-4ebb-b1d1-1efa7055ebc3 | underdog | Chase Brown | Receptions | under | 0.071032842359059 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|6bb6133b-cc35-4fc1-8762-49af70322fd4 | underdog | Jonathan Aranda | Hits | over | 0.0709511661299276 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f4521365-69ef-4f42-a0f2-6ae23602b913 | underdog | Amine Gouiri | Shots on Target | over | 0.0704203332253872 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|219a547c-11aa-422a-871f-73f24d889c5b | underdog | Omarion Hampton | Rush + Rec Yards | under | 0.0702467762201549 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|f197317f-01af-447b-8dcc-2f1a93c3a8c8 | underdog | Samaje Perine | Rush + Rec Yards | under | 0.0700944447959356 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|cb3854d9-f2b7-48e5-8db1-61e6a43f89f4 | underdog | Shohei Ohtani | Batter Walks | over | 0.0698529411764705 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|1981b6ed-0ee3-4837-8f27-71f80cee57fe | underdog | Jacoby Brissett | Rush Yards | under | 0.0698168702062143 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|86c42add-4fd0-4b11-aa16-dd6c4af284d9 | underdog | Remy Labeau Lascary | Shots on Target | over | 0.0697856987924657 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|da79a87a-a666-44b3-a057-092f894001e6 | underdog | Tee Higgins | Receiving Yards | under | 0.0695544352651112 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|07a4d75e-f6aa-4ed2-b8d2-cd4167d4e5a6 | underdog | Danny Namaso | Shots on Target | over | 0.0694504694256902 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|1af97885-a088-40f7-b692-cece11bb1e27 | underdog | Jonny DeLuca | Total Bases | over | 0.0694444444444444 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|683a6a04-4a73-4016-89e3-a21e4c7721f7 | underdog | Davide Frattesi | Shots on Target | under | 0.0693825699941811 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|53107198-6437-46f7-bd29-8b6f4dcef955 | underdog | Braelon Allen | Receptions | under | 0.0690704408831274 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|cb59b73f-90f4-47c2-a627-46801bc83957 | underdog | Alvin Kamara | Receiving Yards | under | 0.0687623538825822 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|e0adfb00-4d15-4d74-8a9d-718e0aaafac3 | underdog | Tyler Higbee | Receiving Yards | under | 0.0687363615477286 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|0fd99d6d-9fd0-4696-aba9-2eba54bdb0db | underdog | Kendrick Bourne | Receiving Yards | under | 0.0686022399140668 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15476309 | prizepicks | Harold Fannin Jr. | Recs | under | 0.0685096067801623 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|e7e07049-21e8-4b18-ad3b-acc75ddc7862 | underdog | Blake Corum | Receptions | under | 0.0683732979337277 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|6bc2028c-074c-49d5-a899-58eb6add783e | underdog | Derrick Henry | Receptions | over | 0.0681999422383017 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|091284a0-c421-4eb2-971c-b847b809f686 | underdog | Devontez Walker | Receiving Yards | over | 0.0680054026858076 | 2026-10-11T05:47:48Z | 2026-10-12T00:20:00Z |
| prizepicks|15542802 | prizepicks | Guglielmo Vicario | Goalie Saves | under | 0.0676796645319098 | 2026-10-08T06:06:51Z | 2026-10-11T14:45:00.000-04:00 |
| underdog|e69e4dd4-31d3-48f1-9009-2fe8f6164e8a | underdog | Freddie Freeman | Batter Walks | over | 0.0675553034600113 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|36477a7e-c59c-441e-adc8-922bd67114fa | underdog | Harold Fannin | Receptions | under | 0.0674382846152032 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|21530813-9913-46de-9214-d4db429882dc | underdog | Cameron Archer | Shots on Target | over | 0.0672664924063877 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|9c02be2c-d2ce-4854-bc2b-4e781f08251b | underdog | Kristian Thorstvedt | Shots on Target | over | 0.0671603324509587 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|6e4e4760-d8c4-4052-84e1-2c4c36eeae36 | underdog | Liam Hicks | Hits | over | 0.067041942489502 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2cff0f32-2cb4-4106-8fed-a599462d2fb1 | underdog | Jo Adell | Hits | over | 0.0667688645081718 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15533342 | prizepicks | Malachi Fields | Rec Targets | under | 0.0667258742805178 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|b9852fd1-accf-47b3-a909-cc36f80d0eb4 | underdog | Jeremiyah Love | Rush Yards | under | 0.0667114093441835 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2c2f954b-0aea-4fd7-8b09-e9e332927a12 | underdog | Rashod Bateman | Receptions | under | 0.0664321324928192 | 2026-10-08T06:06:51Z | 2026-10-12T00:20:00Z |
| prizepicks|15533217 | prizepicks | Sam LaPorta | Rec Targets | under | 0.0662345067031578 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15605191 | prizepicks | Devaughn Vele | Recs | under | 0.0660626855966661 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15599447 | prizepicks | Chris Bell | Rec Targets | under | 0.0659462803090177 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|13976018 | prizepicks | Shai Gilgeous-Alexander | PRA | under | 0.0657969563767089 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|f5cb1600-8b25-4275-8dc6-f218b284ebc3 | underdog | Isaiah Williams | Receptions | under | 0.0657947448732658 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|75596168-01a4-4f6f-81c9-992752bdc9c2 | underdog | Greg Rousseau | Sacks | over | 0.0657344319318249 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|920f44e5-682b-43c7-b114-ef9d0f38b689 | underdog | Aaron Rodgers | Rush Yards | over | 0.0656860931851113 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|5030f5dd-f92c-4926-883c-58f2468a91bf | underdog | Jaylin Noel | Receptions | under | 0.0654934658102431 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|31eb9469-5787-47b8-bc09-600dd6083db4 | underdog | Kirk Cousins | Rush Yards | over | 0.0654801965150794 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15599453 | prizepicks | Eli Raridon | Rec Targets | under | 0.0650920557758655 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|9e6b6ed4-71c2-4672-b9f8-8b8c509246ef | underdog | Christian Watson | Receiving Yards | under | 0.0650046863243084 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15613908 | prizepicks | Shuai Zhang | Total Games Won | over | 0.0648720586997275 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| prizepicks|15599455 | prizepicks | Isaiah Williams | Rec Targets | under | 0.0648033070038873 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|490e0bc2-4747-4ec7-bb36-6ec37fab3248 | underdog | Noah Fant | Receptions | under | 0.0643230378809457 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|aca59ac6-bcb4-4876-ad2b-6fd19a652c81 | underdog | Calvin Ridley | Receptions | under | 0.0642175340145783 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|802fa6b0-d8b0-4a30-bbed-ddfc0d3ba6bb | underdog | Jordan Addison | Receptions | under | 0.0641653475698695 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|cfed6d3d-871e-46d2-8839-be9b9f360f3c | underdog | Chad Ryland | Kicking Points | under | 0.0635639113992488 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|e9150ea6-d7df-4164-bebd-6a60e766ea6e | underdog | Mattia Zaccagni | Shots on Target | over | 0.0634525825382998 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|63873f2c-e652-49b2-97ff-936791738882 | underdog | Will Kacmarek | Receiving Yards | under | 0.0632998161800548 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|5fa16cb9-3036-4344-a474-98ff5766708a | underdog | Carlos Soler | Shots on Target | over | 0.0632507150994984 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15599460 | prizepicks | Emanuel Wilson | Rec Targets | under | 0.0630636453580861 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|e7d46ae1-92f4-4e4d-a1e3-be5fbcd1743c | underdog | Blake Corum | Rush + Rec Yards | under | 0.0629949724268884 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|99e00560-73c0-4e61-b371-fa655894e83f | underdog | Christian Yelich | Hits | over | 0.0627914611339157 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15449757 | prizepicks | Drake Maye | Rush Yards | under | 0.0626996072293499 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|55b8f5e8-df95-476c-8e49-a68d71901f39 | underdog | Tre Tucker | Receiving Yards | under | 0.062677885181109 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|e2f95fd1-7f77-41ee-a00f-ee231e084d36 | underdog | Jackson Chourio | Batter Walks | under | 0.0626486578321441 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|583b4eb9-8aae-48fd-b631-3141a5c4b97a | underdog | Jacob Misiorowski | Strikeouts | over | 0.0624775741265951 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|760cd9bf-bc88-4c0b-9eed-5bfa05fefc69 | underdog | Douglas Luiz | Shots Attempted | over | 0.0623954562981268 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|f8005c7b-8fd2-4fb4-b3e2-0c81fa133c49 | underdog | Ryan Vilade | Hits + Runs + RBIs | over | 0.062386362231787 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|8da8b605-48b2-429a-bbce-4ea985b710b7 | underdog | Patrick Bailey | Batter Walks | over | 0.0621841661987646 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15596256 | prizepicks | Quentin Halys | Total Games Won | over | 0.06218029333802 | 2026-10-09T20:57:57Z | 2026-10-11T00:00:00.000-04:00 |
| underdog|23331c7d-6803-44fc-8408-70b0001a8635 | underdog | Angel Martínez | Hits | over | 0.0618390564962869 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|40e3fc3a-cbd2-435c-bedd-6b8e6bbe5b07 | underdog | Evan McPherson | Kicking Points | under | 0.0615565501863706 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533219 | prizepicks | Matthew Golden | Rec Targets | under | 0.0614323068960948 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|e958a43a-d936-4bdc-91eb-2f3bc11ebdd9 | underdog | Keon Coleman | Receiving Yards | under | 0.0612866533143504 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|15542226 | prizepicks | Noel Törnqvist | Goalie Saves | under | 0.0612272727059003 | 2026-10-08T06:06:51Z | 2026-10-11T09:00:00.000-04:00 |
| underdog|14bc07cf-0064-4171-838c-fa25c8567a15 | underdog | Chase DeLauter | Batter Walks | over | 0.0612067969020922 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|67c768c9-a93f-49e5-9815-142a1d2ab023 | underdog | Mahdi Camara | Shots on Target | over | 0.0611273162311297 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|711ad2e3-3689-47a0-8ab5-f98595bc5429 | underdog | Chase DeLauter | RBIs | over | 0.0608891355284251 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|14336df8-3ab4-4dc1-87fb-e7a6bdd008c0 | underdog | Tyler Higbee | Receptions | under | 0.0606378768913719 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|956016f6-b9b6-43ce-a8bc-b83ae1008494 | underdog | Luis Lara | Hits | over | 0.0603661401328439 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| prizepicks|15533332 | prizepicks | Michael Mayer | Rec Targets | under | 0.0593911844258144 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|9b7139f6-f9b7-445c-b68e-03b80020f5df | underdog | Rachaad White | Rush + Rec Yards | under | 0.0589613252319829 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|5f8e4c60-5f58-426c-8626-930e2776ff5a | underdog | J.K. Dobbins | Receiving Yards | under | 0.0589363835237102 | 2026-10-09T06:09:55Z | 2026-10-11T20:05:00Z |
| underdog|0ef473ec-21b2-4a5e-b9fc-933621de9b1d | underdog | Andy Pages | Hits + Runs + RBIs | over | 0.05891969480564 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|a66a81d4-aab6-4641-9905-efa172f5f5da | underdog | Paulo Dybala | Shots Attempted | over | 0.058860190882896 | 2026-10-09T06:09:55Z | 2026-10-11T10:30:00Z |
| underdog|0b253cee-0647-4587-a5a3-22eeb7295453 | underdog | Raheim Sanders | Receiving Yards | over | 0.0588329704327007 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15599448 | prizepicks | Greg Dulcich | Rec Targets | under | 0.058799538855619 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|23d9e3ff-d761-464d-a25a-2ccbba398822 | underdog | Jo Adell | Runs | over | 0.0587677725118483 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15605194 | prizepicks | Wan'Dale Robinson | Recs | under | 0.0587626911101839 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|29ff3760-5eff-4af5-944a-6c67a3e04c4b | underdog | Justice Hill | Receptions | under | 0.0586356807308978 | 2026-10-09T06:09:55Z | 2026-10-12T00:20:00Z |
| underdog|ce8541ca-1777-414c-bd54-b1e6d73ac0c9 | underdog | Richie Palacios | Total Bases | over | 0.0586311872815423 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2eeacaf7-7641-46c9-aa29-c839ed4c77d3 | underdog | Javier Guerra | Shots on Target | under | 0.0583285156829901 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|f14a1938-7b30-4a5e-8104-80da24175f0b | underdog | Ty Johnson | Receiving Yards | over | 0.0580552741488891 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|ae29e0a0-2c0b-410a-9698-c03bcbbb10de | underdog | Aidan Hutchinson | Sacks | under | 0.0579984274424641 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| prizepicks|15599466 | prizepicks | Tyjae Spears | Rec Targets | under | 0.057968811283434 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|a7447cc4-be62-401b-8dc6-12e779135453 | underdog | Dawson Knox | Receptions | under | 0.0577342318788118 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|dca040c2-f523-4703-bcd4-e46a8619d786 | underdog | Tyler Shough | Pass TDs | over | 0.057703993440012 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|74ba7bd0-a169-4967-9e7a-ac9c4d357b8a | underdog | Lucas Cepeda | Shots on Target | over | 0.0572693847219132 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|9391e72e-f268-4e67-884f-8e7d3fb2ee16 | underdog | Jaylen Warren | Receiving Yards | under | 0.0571692451117062 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|339f7022-7f92-4b6e-9c90-3d298e94e29a | underdog | Will Reichard | FG Made | under | 0.0570799645458505 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|25ea7975-98fc-49ee-8d21-5c1875039f78 | underdog | Michael Mayer | Receptions | under | 0.0568497942248852 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15599432 | prizepicks | Ty Johnson | Rec Targets | under | 0.056772117670328 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15604860 | prizepicks | Darius Cooper | Rec Targets | under | 0.0565847706248153 | 2026-10-09T20:57:57Z | 2026-10-11T09:30:00.000-04:00 |
| underdog|96d44c63-4b21-4387-9460-7b2434936ac2 | underdog | Nathaniel Lowe | Total Bases | over | 0.0563003056903272 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|8d128ea3-05ca-4da8-8b9a-3bf075f8379b | underdog | Drake Maye | Rush Yards | under | 0.0560287034484765 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|27aac917-d404-44a2-8a9e-8ea2f92f66b1 | underdog | Sam Darnold | Rush Yards | under | 0.0559092289903409 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|f2752fd8-64b5-4c3e-ac41-1066456ea64d | underdog | Arnaut Danjuma | Shots on Target | under | 0.055549653532421 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|ca1b3191-5477-4be6-bfd2-15097e1deb2d | underdog | Brock Purdy | Pass TDs | under | 0.0550959740544247 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| underdog|78910761-07f4-4184-abb7-761c3fef0716 | underdog | Andy Pages | Batter Walks | under | 0.055045871559633 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| prizepicks|15533341 | prizepicks | Isaiah Likely | Rec Targets | under | 0.0549729434433424 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|55d8046d-e577-40bc-84df-6561d8ac1c91 | underdog | Jonathan Asp Jensen | Shots Attempted | over | 0.0548270495336102 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|c588e5e9-48c8-42ad-aa3f-0caf45a98653 | underdog | Kyle Tucker | Batter Walks | over | 0.0548199767711962 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| prizepicks|15533346 | prizepicks | Darnell Washington | Rec Targets | under | 0.0544438164117958 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|ab84fc38-8730-45db-b82e-364f3b1aa4fc | underdog | Alim McNeill | Sacks | over | 0.0543797977811563 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| underdog|94c3c97e-1a2a-4941-9434-f8a72f976d6a | underdog | Igor Matanovic | Shots on Target | over | 0.0543311308116279 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| prizepicks|15599452 | prizepicks | Efton Chism III | Rec Targets | under | 0.0540590803260235 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|4e48126e-3fb0-4b40-84a1-01af6f518e71 | underdog | Laiatu Latu | Sacks | over | 0.0536388986443384 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| prizepicks|15605193 | prizepicks | Kayshon Boutte | Recs | under | 0.0531901365539206 | 2026-10-10T05:51:08Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|4aeb884e-3986-447e-9395-b55c383e23cd | underdog | Jonathan Aranda | Batter Walks | over | 0.0531567277395262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|f8279730-4480-4adb-bf25-5c4aea98ac07 | underdog | Gustavo Varela | Shots on Target | over | 0.0530714044689619 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|f95ed05f-2644-476e-99f8-a874e2b8bb0e | underdog | Hugo Gonzalez | Shots on Target | under | 0.052864689502121 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|d4410e2b-6e79-4437-b775-168db354b284 | underdog | Nikola Stulic | Shots on Target | under | 0.0527242033973307 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| prizepicks|15599446 | prizepicks | Cody White | Rec Targets | under | 0.0526315618879372 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|efdd9948-3b4a-477a-b59b-403a51a18b72 | underdog | Davante Adams | Receiving Yards | under | 0.0523788305225944 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| underdog|cd9718a2-718e-413d-98d0-b8d70956fa89 | underdog | Brenton Strange | Receiving Yards | under | 0.0522924315822024 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|22362ed1-93fe-4ac8-af1a-1c17668c2f68 | underdog | Spencer Shrader | FG Made | under | 0.0522809563627131 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|9a70589a-7459-4958-863b-c5aa3512565f | underdog | Thomas Lemar | Shots on Target | over | 0.05226380277827 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|4f778fae-400b-4a23-81b0-06c0d3b8ec34 | underdog | Felix Correia | Shots on Target | under | 0.0522488691093763 | 2026-10-11T05:47:48Z | 2026-10-12T19:00:00Z |
| underdog|b568f488-b37f-4d7b-b0f8-3e8c1bbca8cd | underdog | James Cook | Rush Yards | under | 0.052094586678718 | 2026-10-09T06:09:55Z | 2026-10-13T00:15:00Z |
| underdog|b9a4c5de-d36b-424b-b103-060f62140753 | underdog | Blake Corum | Rush Yards | under | 0.0519852201387395 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| prizepicks|15591673 | prizepicks | Kyren Williams | Rush TDs | under | 0.051964898491767 | 2026-10-09T06:09:55Z | 2026-10-12T20:15:00.000-04:00 |
| underdog|cdddeabc-ade1-491b-9bce-2ba77abc3c15 | underdog | Daniel Maldini | Shots Attempted | under | 0.0519191458071393 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|b1b4717d-6e77-478f-b83a-cf3a1e08d593 | underdog | Isaiah Williams | Receiving Yards | under | 0.0517889382811641 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|e8e6e218-22fb-4f7f-be3e-08abd3f1fd6c | underdog | Steven Kwan | Total Bases | over | 0.0516426642664265 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ec111872-8b96-4ae1-8173-f699c7170135 | underdog | Tanner Hudson | Receptions | over | 0.0515063896464016 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|2fdb2ee5-b414-48a5-9823-8810e97fe297 | underdog | Cam Ward | Rush Yards | under | 0.0514867769064468 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|da0669ca-c84b-43b0-aef1-e85140ebeb88 | underdog | Tyjae Spears | Rush + Rec Yards | under | 0.0514276407346809 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15564273 | prizepicks | Tyler Loop | Kicking Points | under | 0.0513949469902661 | 2026-10-11T05:47:48Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|3cf479f1-813b-4cff-b200-9f1bb47489e2 | underdog | Jeremiyah Love | Receiving Yards | under | 0.0512744398137398 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|ad15f125-9801-442c-8cfa-85327aed08f8 | underdog | Luis Lara | Total Bases | over | 0.0512241635583474 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|bdd55feb-7967-47fe-b5b8-d7fbc2c79f9f | underdog | Angel Martínez | Total Bases | over | 0.0512241635583474 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b7ec11ec-2331-482b-b6d4-5dd590e42c37 | underdog | Kaleb Johnson | Receptions | under | 0.0507343822731093 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|bbd56793-88ff-4803-9675-19125cd2b287 | underdog | Joey Ortiz | Batter Walks | over | 0.0507256894049346 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|d271cb9f-1717-4bd9-830c-a1c1fae478a4 | underdog | Paulo Dybala | Shots on Target | under | 0.0504224582068929 | 2026-10-09T06:09:55Z | 2026-10-11T10:30:00Z |
| underdog|e510fca3-6e87-4eef-a45b-d2d4af90834b | underdog | Calvin Ridley | Receiving Yards | over | 0.050361017348545 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|d454eccc-c68c-42bd-9543-0bb105a16865 | underdog | Davante Adams | Receptions | under | 0.0502337858941952 | 2026-10-07T05:55:02Z | 2026-10-13T00:15:00Z |
| underdog|7bf49ff6-556b-4b3d-9648-9d4b64bfe8e3 | underdog | Cam Skattebo | Receiving Yards | under | 0.0501051233398871 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|6c22ee74-1d24-42b8-b331-5a6642775629 | underdog | Tyjae Spears | Rush Yards | under | 0.0498070336129585 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15542573 | prizepicks | Mike Maignan | Goalie Saves | under | 0.0496167951819059 | 2026-10-08T06:06:51Z | 2026-10-11T12:00:00.000-04:00 |
| underdog|3ed62f8f-9496-4978-afd3-274defea5969 | underdog | Elic Ayomanor | Receiving Yards | under | 0.0495270291286717 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15449761 | prizepicks | Geno Smith | Rush Yards | under | 0.0490331034091593 | 2026-10-07T05:55:02Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|96037d9b-c6ef-4f0a-8d32-16be44c2e81b | underdog | Chase Brown | Receiving Yards | under | 0.0488388323967373 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|0746a0f1-46ca-459e-b2fb-e63154b8828c | underdog | Gustavo Varela | Shots Attempted | under | 0.0488141295875885 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|d2ee254a-15d4-4c79-9687-98e53c3e1cbc | underdog | Jerry Jeudy | Receptions | under | 0.0486938419502581 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|9c8d410c-53c7-4f90-814a-8de9d083cec0 | underdog | Donyell Malen | Shots on Target | over | 0.0486817835841816 | 2026-10-08T06:06:51Z | 2026-10-11T10:30:00Z |
| underdog|c5d6e03c-b52a-4209-b275-c153ae1c7a1a | underdog | Weston McKennie | Shots on Target | over | 0.0486584898910605 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|27518563-6e41-4721-bea0-9905ca082925 | underdog | K'Lavon Chaisson | Sacks | over | 0.0486554893080395 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|1b390482-7e2c-4b80-be39-258f4de29c17 | underdog | Kaelon Black | Rush Yards | under | 0.048637576309925 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|2721c51f-a2c4-4863-b998-18ec650c98a3 | underdog | Jahan Dotson | Receiving Yards | under | 0.0484092199009141 | 2026-10-09T20:57:57Z | 2026-10-12T00:20:00Z |
| underdog|fa7b6eda-05a1-46dc-80a7-04b2c5238dbf | underdog | Mookie Betts | Hits | over | 0.0481741767062777 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|b1e0a846-63ea-4ad1-9ad7-096f48f376c7 | underdog | Chase DeLauter | Hits | over | 0.0481342569823664 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|b8c7b8fb-790e-42b4-bd45-e84ca3d5af98 | underdog | Konata Mumpfield | Receptions | under | 0.0479771065940467 | 2026-10-09T20:57:57Z | 2026-10-13T00:15:00Z |
| prizepicks|15599195 | prizepicks | Hubert Hurkacz | Total Games | over | 0.0478962119662994 | 2026-10-09T20:57:57Z | 2026-10-11T00:00:00.000-04:00 |
| underdog|9bd809ff-4592-4ac2-b7a0-4478d0160eeb | underdog | Tory Horton | Receptions | over | 0.0478458045816117 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| underdog|123b8b15-67f2-4a53-8bde-624ee98bc83d | underdog | Remy Labeau Lascary | Shots Attempted | under | 0.0478378570801684 | 2026-10-11T05:47:48Z | 2026-10-11T15:15:00Z |
| underdog|73454e0c-49dc-41e4-9340-87f225f5d79f | underdog | José Ramírez | Hits | over | 0.0476522420101034 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|d2a4f439-f44e-4c12-a266-00a05ff35a24 | underdog | Jonathan Taylor | Receiving Yards | under | 0.0472892565622767 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|d35b9dc4-6c41-4038-b44a-de5add2f440b | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.0471314024810165 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|5ed26ce5-cb2e-4ea9-b6d4-282bd12c3d65 | underdog | Jurgen Ekkelenkamp | Shots on Target | over | 0.0469164885339176 | 2026-10-08T06:06:51Z | 2026-10-12T18:45:00Z |
| prizepicks|15599426 | prizepicks | Justice Hill | Rec Targets | under | 0.0469113281743684 | 2026-10-09T20:57:57Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|4bb6dcfb-1307-4cd4-898e-9d4555c490c6 | underdog | Dohnte Meyers | Receiving Yards | under | 0.0464664054718026 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|f2898a31-697f-48e4-810d-a097dfca055d | underdog | Taylor Walls | Batter Walks | under | 0.0461621486985761 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ebcb99f6-f9a0-4293-a193-aeec33d55ca1 | underdog | Evan Engram | Receptions | under | 0.0458061389540194 | 2026-10-08T06:06:51Z | 2026-10-11T20:05:00Z |
| underdog|3a9a983a-4b09-4f55-bed9-7480d77410ea | underdog | Shohei Ohtani | Hits + Runs + RBIs | over | 0.0456065050162127 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|b73054a9-cf67-4ff2-9363-9d57a37918e6 | underdog | Thorir Johann Helgason | Shots on Target | over | 0.0450908781515718 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|25798088-9899-40d1-b07b-be022423acbe | underdog | Kyle Williams | Receiving Yards | under | 0.0445337165996326 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|15527698 | prizepicks | Aaron Jones Sr. | Recs | under | 0.0437890505035218 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| prizepicks|15533046 | prizepicks | Jeremiyah Love | Rec Targets | under | 0.0435400686640043 | 2026-10-08T06:06:51Z | 2026-10-11T16:25:00.000-04:00 |
| prizepicks|15599468 | prizepicks | Jordan Whittington | Rec Targets | under | 0.0433033789668447 | 2026-10-09T20:57:57Z | 2026-10-12T20:15:00.000-04:00 |
| prizepicks|15613038 | prizepicks | Qinwen Zheng | Total Games | over | 0.0432704704006529 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|e95fefee-cd88-4bd5-baf7-28271a93235e | underdog | Victor Mesa | Hits | under | 0.0432698196376072 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|42b5713a-8289-406f-a90f-8b5ee9ce35ef | underdog | Pablo Carreno Busta | Aces | under | 0.0429733153805502 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| prizepicks|15616499 | prizepicks | Taylor Fritz | Total Games | over | 0.0429084695618681 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|c1a3ff1c-bca2-4682-a20b-ea92fb6d8754 | underdog | Isaiah Likely | Receptions | under | 0.0428762717304954 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| underdog|042e94c2-6f30-4c72-8252-eb0edacf94a1 | underdog | Laquon Treadwell | Receptions | over | 0.042745843565835 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|8724c680-935e-45ad-93b2-8ee0d84443de | underdog | Omarion Hampton | Receiving Yards | over | 0.0427408179802855 | 2026-10-10T05:51:08Z | 2026-10-11T20:05:00Z |
| underdog|7429ccdc-74e4-42c2-ae9c-6eabd60be76f | underdog | Quinshon Judkins | Receiving Yards | under | 0.0426526193503552 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|82c4356b-26cc-4da4-9ef3-39e363ce5689 | underdog | Job Ochieng | Shots Attempted | under | 0.0423167322414048 | 2026-10-09T20:57:57Z | 2026-10-11T14:15:00Z |
| underdog|dd35f75f-2676-4274-a2c9-3414d11fafce | underdog | Brayan Rocchio | Hits + Runs + RBIs | over | 0.0422326601217262 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|15d644b5-f4e6-4759-aeb3-da2bb3d271c5 | underdog | George Holani | Receiving Yards | over | 0.0420246508054192 | 2026-10-09T06:09:55Z | 2026-10-11T20:25:00Z |
| prizepicks|13976010 | prizepicks | Shai Gilgeous-Alexander | Pts+Asts | under | 0.0419653653034837 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|002dc6a7-15a2-4ef6-a09e-0658552cc5df | underdog | Emanuel Wilson | Receiving Yards | under | 0.0416189116317229 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|0d841021-e895-4cc8-bb26-e9719e35b4d8 | underdog | Montez Sweat | Sacks | over | 0.0415766543379325 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|14482dd1-b7ee-4d32-87bb-3808e64e3f80 | underdog | Jo Adell | Batter Walks | over | 0.0414027149321265 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|2ef616d5-cfe3-4f4f-9210-fa1daea97e1e | underdog | Victor Mesa | RBIs | over | 0.0411510882670219 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|6dfb9119-17c4-498d-8918-c08c536b7732 | underdog | Nathaniel Lowe | Hits | over | 0.0411136759865278 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|bcfdaef5-d634-4a42-9ddc-78df3c2a8391 | underdog | Cooper Pratt | Total Bases | over | 0.0410718792943881 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|7ae498d0-8b1e-4634-8b3f-2b0943b5c769 | underdog | Kirk Cousins | Pass TDs | under | 0.0409917405772947 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| prizepicks|15614068 | prizepicks | Shuai Zhang | 1st Set Total Games Won | over | 0.0408223148540826 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|2dff6365-68af-4681-bb9d-61cf88f2d95e | underdog | Josh Cameron | Receptions | under | 0.0408078079260765 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|fdecd6a3-2340-4b56-87b4-99f2a8e18fa9 | underdog | Darnell Mooney | Receiving Yards | under | 0.0406565513254704 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|15ea2bd2-f92c-4bbb-87a5-8835a0d6fc5b | underdog | Akor Adams | Shots Attempted | over | 0.0404757452208421 | 2026-10-09T06:09:55Z | 2026-10-12T16:30:00Z |
| underdog|5dc8f6db-1efa-467f-bf7b-5cae7ee7b20c | underdog | Byron Young | Sacks | under | 0.0404468577306219 | 2026-10-11T05:47:48Z | 2026-10-13T00:15:00Z |
| underdog|8c33bf40-585b-403c-ab64-a7e928c0cea9 | underdog | John Yeboah | Shots Attempted | under | 0.0404014016880587 | 2026-10-08T06:06:51Z | 2026-10-12T16:30:00Z |
| underdog|eb471f33-3f61-4af8-9274-1989732b49bf | underdog | Carnell Tate | Receiving Yards | under | 0.0403896557308171 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|e1c95da6-624b-4fde-ae1e-b52fe66a8448 | underdog | Paul Mendy | Shots on Target | over | 0.0403023070491791 | 2026-10-08T06:06:51Z | 2026-10-11T18:45:00Z |
| underdog|89b4278b-c402-4008-97e8-179c610ceb0c | underdog | Kalif Raymond | Receptions | over | 0.0402780104316515 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|842e9c40-1f35-420b-89fd-c3d06c3939ed | underdog | Qinwen Zheng | Double Faults | under | 0.040202305020031 | 2026-10-11T05:47:48Z | 2026-10-11T11:30:00Z |
| prizepicks|15533062 | prizepicks | RJ Harvey | Rec Targets | under | 0.0400924452244398 | 2026-10-08T06:06:51Z | 2026-10-11T16:05:00.000-04:00 |
| underdog|887b4717-b08b-4f9a-a5e3-7f9676439392 | underdog | Maliek Collins | Sacks | over | 0.0400573845760939 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|ec7fdc0c-7fe5-4b02-92c5-a7a81b83392a | underdog | Chad Ryland | FG Made | under | 0.0400270549141917 | 2026-10-08T06:06:51Z | 2026-10-11T20:25:00Z |
| underdog|4fb3d495-5606-4294-a69a-bebeb381cf24 | underdog | Jameis Winston | Pass TDs | over | 0.0396005605407765 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|9ad95f66-2a9d-45ad-979a-c88163a0f7e2 | underdog | Adrien Thomasson | Shots on Target | under | 0.0395052837272464 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|73e04d3f-70ce-4826-8618-a56f01930f79 | underdog | Dominic Zvada | Kicking Points | under | 0.039434785227103 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|bc25bd19-d606-4cae-9968-4074498362e5 | underdog | Tony Pollard | Receiving Yards | under | 0.0393181158070664 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|258d09ff-56f8-40b1-bfab-9b523772a3d9 | underdog | Darnell Washington | Receiving Yards | under | 0.0391773518620307 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|dff0a61d-5ad2-4af5-a4db-accff5bb84b7 | underdog | Raheim Sanders | Rush Yards | under | 0.0391142628876352 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15533354 | prizepicks | Wan'Dale Robinson | Rec Targets | under | 0.0388828862379944 | 2026-10-08T06:06:51Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|29e93751-e4c0-40d5-ae0e-d0f469c72ec8 | underdog | Zach Allen | Sacks | under | 0.0388134263854621 | 2026-10-11T05:47:48Z | 2026-10-11T20:05:00Z |
| underdog|bacd7834-5ebd-49b5-9f30-246293086a12 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.0387451286206554 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15576379 | prizepicks | Tyler Shough | Pass+Rush+Rec TDs | under | 0.0385217818019923 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|a2d80723-3430-46b0-bb16-d7503dd6d1e8 | underdog | William Contreras | Batter Walks | over | 0.0383613544873312 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|06412611-d60e-4a5d-843b-527f4ee7515b | underdog | Tyler Shough | Rush Yards | over | 0.0376597216753686 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|7ee5da09-3fc1-4c89-b656-e8dff52b3ff8 | underdog | Mookie Betts | Batter Walks | under | 0.0372822299651568 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
| underdog|9cb24e16-f970-4a09-a363-eaa63185df21 | underdog | Theo Johnson | Receptions | under | 0.0372620564940527 | 2026-10-08T06:06:51Z | 2026-10-11T17:00:00Z |
| prizepicks|15616492 | prizepicks | Learner Tien | Total Games | over | 0.0372537289376189 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00.000-04:00 |
| underdog|6f74877a-8932-4824-b496-80ed746ec3b7 | underdog | Chase DeLauter | Hits + Runs + RBIs | over | 0.0372398714202552 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|440d1cf8-c58b-4f5c-92ed-ced70636bee3 | underdog | Dallas Turner | Sacks | over | 0.0372363283773524 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|6dd93257-e00a-4c0b-80a7-8931933974e1 | underdog | Esteban Lepaul | Shots on Target | under | 0.0371164474739956 | 2026-10-09T20:57:57Z | 2026-10-11T15:15:00Z |
| underdog|81ed470f-fcf2-4536-892b-ffe55020be3b | underdog | Dohnte Meyers | Receptions | over | 0.0370812580390212 | 2026-10-11T05:47:48Z | 2026-10-11T17:00:00Z |
| underdog|1d827d4f-315a-45d6-acfe-a04aec6d110e | underdog | Dominic Zvada | FG Made | under | 0.0367663461645783 | 2026-10-10T05:51:08Z | 2026-10-11T17:00:00Z |
| underdog|55e352ff-542d-48ae-82d1-51e2fbc7bb3e | underdog | Steven Kwan | RBIs | under | 0.0367231638418079 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|72fed86e-b34a-48ea-afc9-10ccacf47696 | underdog | Kendrick Bourne | Receptions | under | 0.0366745274473986 | 2026-10-11T05:47:48Z | 2026-10-11T20:25:00Z |
| underdog|aee9c338-257b-44b5-a679-1bca0d16f1a0 | underdog | MarShawn Lloyd | Receiving Yards | under | 0.0365702274482132 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|ab52a7e3-e6fe-4d67-9990-96602e86792e | underdog | Jerry Jeudy | Receiving Yards | under | 0.0363772864059361 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|fb0e5f42-0ca9-488a-acb0-bf69153f6d5e | underdog | Yandy Díaz | Hits | over | 0.0362411588662526 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|72033b2a-88ef-462c-915f-7f03873851a9 | underdog | Isaac TeSlaa | Receptions | under | 0.036224370427224 | 2026-10-07T05:55:02Z | 2026-10-11T20:25:00Z |
| prizepicks|15549205 | prizepicks | Greg Dulcich | Recs | under | 0.0360255214332747 | 2026-10-11T05:47:48Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|9eed7fcb-d587-40b3-bc0b-a31e1e70503e | underdog | Isaiah McGuire | Sacks | over | 0.0359999060753661 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|fd04298b-8310-43f6-ab3b-06939b468b8a | underdog | Samuel Chukwueze | Shots on Target | over | 0.0359591791501983 | 2026-10-09T06:09:55Z | 2026-10-11T16:00:00Z |
| underdog|6a7e2f73-c7ca-48b8-acba-3bafa0da6852 | underdog | Quinshon Judkins | Receptions | under | 0.0354417619464345 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|944b7b01-6321-4ec3-a692-78ac85c0b9a5 | underdog | Sergio Canales | Shots Attempted | under | 0.0352617642447898 | 2026-10-09T20:57:57Z | 2026-10-11T19:00:00Z |
| underdog|f1fd1b12-f8f1-40d8-bc20-db7742812988 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.0350550281161768 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|09e68f40-9982-4964-b331-cc34e2898a56 | underdog | Kaelon Black | Receptions | over | 0.0349648661590343 | 2026-10-09T20:57:57Z | 2026-10-11T20:25:00Z |
| prizepicks|15599462 | prizepicks | Calvin Ridley | Rec Targets | under | 0.0342664749737003 | 2026-10-09T20:57:57Z | 2026-10-11T13:00:00.000-04:00 |
| underdog|f1328e37-9faf-48d7-afcc-58bff61e6e96 | underdog | Taylor Fritz | Aces | over | 0.034228742384909 | 2026-10-11T05:47:48Z | 2026-10-12T04:00:00Z |
| underdog|16e22518-cd33-4795-a080-bea1605e1503 | underdog | Kyle Tucker | Hits + Runs + RBIs | over | 0.0341468329384453 | 2026-10-09T06:09:55Z | 2026-10-12T00:00:00Z |
| underdog|57e79cc8-2fd4-42b8-92bc-99fc9dcfa5cd | underdog | Trevor Lawrence | Pass TDs | under | 0.0337898395327892 | 2026-10-07T05:55:02Z | 2026-10-11T13:30:00Z |
| underdog|933a1291-8abf-4b7e-99c1-03acb022f99c | underdog | Mirra Andreeva | Double Faults | under | 0.0337823059398411 | 2026-10-11T05:47:48Z | 2026-10-11T11:30:00Z |
| prizepicks|15599461 | prizepicks | George Holani | Rec Targets | under | 0.033760828349025 | 2026-10-09T20:57:57Z | 2026-10-11T16:25:00.000-04:00 |
| underdog|4e5adf87-7d75-4c7c-a413-26c738cc9a7f | underdog | Antoine Mille | Shots on Target | over | 0.0337579508060221 | 2026-10-09T20:57:57Z | 2026-10-11T18:45:00Z |
| underdog|e708d9c9-dad3-44c4-9796-e82b07b0ff77 | underdog | Gunnar Helm | Receptions | under | 0.033285204693046 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|5719d5a0-c81a-4047-af0b-1deda36ce93c | underdog | Taylor Walls | Hits | over | 0.0329688869050202 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| prizepicks|15596796 | prizepicks | Frances Tiafoe | Total Games | over | 0.0321409161180068 | 2026-10-10T05:51:08Z | 2026-10-11T00:00:00.000-04:00 |
| underdog|801d470c-041c-4ab7-8003-49b874f2f8bb | underdog | Woody Marks | Receiving Yards | over | 0.0321052002212405 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|63b89295-21af-40c4-9cdc-2d721968b667 | underdog | T.J. Hockenson | Receiving Yards | under | 0.0320888722363011 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|98225952-0651-4160-8f69-35b17458d1dd | underdog | Jameis Winston | Rush Yards | over | 0.0320770258328804 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| prizepicks|15614077 | prizepicks | Cristina Bucsa | 1st Set Total Games Won | under | 0.0318910683523252 | 2026-10-11T05:47:48Z | 2026-10-11T22:00:00.000-04:00 |
| underdog|3f626b40-469c-4c10-96fe-a11e5d20e83f | underdog | Josh Cameron | Receiving Yards | over | 0.0318873761451889 | 2026-10-09T06:09:55Z | 2026-10-11T13:30:00Z |
| underdog|1d1906a4-7f37-41af-9e4f-76ba995dcc2c | underdog | Patrick Bailey | Hits | over | 0.0314555918613239 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|9ab2a08f-a322-431b-af84-1c2618c0f4cf | underdog | Gonzalo Villar | Shots Attempted | under | 0.0313902230526317 | 2026-10-09T20:57:57Z | 2026-10-11T12:00:00Z |
| underdog|ec759ae0-8770-4773-8e18-28e14baec56b | underdog | Skyy Moore | Receiving Yards | under | 0.0313217710681557 | 2026-10-09T06:09:55Z | 2026-10-11T17:00:00Z |
| underdog|6004390b-5d94-40ee-89d2-165e0a21d2c0 | underdog | Patrick Cutrone | Shots on Target | under | 0.0310082227410748 | 2026-10-09T06:09:55Z | 2026-10-11T13:00:00Z |
| underdog|7916f912-a87f-4eef-85cd-9d678572a904 | underdog | Sheldon Rankins | Sacks | over | 0.0309962278514902 | 2026-10-09T20:57:57Z | 2026-10-11T17:00:00Z |
| underdog|2b1c6ee3-d12e-43cc-b8c2-418293364af4 | underdog | Ryan Vilade | Total Bases | over | 0.0309195950304287 | 2026-10-11T05:47:48Z | 2026-10-13T00:00:00Z |
| underdog|ee801977-1388-439c-9529-aee399b68f0e | underdog | Geno Smith | Pass TDs | under | 0.0308012453608023 | 2026-10-07T05:55:02Z | 2026-10-11T17:00:00Z |
| underdog|891224d1-5f67-4a67-8e24-f3381f693472 | underdog | Yuito Suzuki | Shots on Target | under | 0.0307635936897582 | 2026-10-09T06:09:55Z | 2026-10-11T15:30:00Z |
| prizepicks|15489681 | prizepicks | Bijan Robinson | Rec Targets | under | 0.0302836573340071 | 2026-10-07T05:55:02Z | 2026-10-11T20:20:00.000-04:00 |
| underdog|05d27070-b2b7-4dc4-b841-121845c4568f | underdog | Teoscar Hernández | Hits + Runs + RBIs | over | 0.0300105556293196 | 2026-10-11T05:47:48Z | 2026-10-12T00:00:00Z |
