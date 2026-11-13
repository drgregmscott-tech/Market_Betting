# Pipeline Digest -- 2026-11-13T12:06:47Z

## Run summary
- Ingestion: 39868 rows (PrizePicks OK, Underdog OK)
- Estimation: 39868 rows estimated (from 39868 ingested props)
- CLV logging: 152 newly flagged, 0 newly closed, 851 still open (111427 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|31a33637-10de-42b7-9cb8-d9a87d355fdd | underdog | Riley Patterson | FG Made | under | 0.40062585991961885 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|f2eeb02f-698a-47c9-abbe-a195f7c7dc3d | underdog | King Miller | Receiving Yards | over | 0.4 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|bdfd294a-de03-4dd4-8b3f-0eb9a1928a22 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-13T12:14:20Z | 2026-11-15T21:25:00Z |
| underdog|c6c07a22-7858-46d3-aaa3-096f53414f8f | underdog | Riley Patterson | Kicking Points | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|a14ab79d-2c35-4572-b5e5-65f7e4f3d25f | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|abbeb5c4-21e6-4875-8173-8f2e9eb69d19 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|42070c06-f98b-402f-b072-cf90401e5dfa | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|e6543c89-d139-402a-be7b-4d5cb96ea168 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|02236b14-ee6c-4f53-aa2b-4cc4244da560 | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|bd4195f9-d156-43b9-b229-f6dc8a9320ea | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|146a5d3b-156f-4cb2-9957-793d78599811 | underdog | Aaron Rodgers | Pass Yards | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|053c3e50-6f32-466c-a249-84cee7048674 | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|651718aa-f819-4e2f-ad0b-6295b7832c86 | underdog | Drake Maye | Pass Yards | under | 0.38488538296258934 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|bf3b1159-fa11-42f9-ae28-7421be127235 | underdog | Eddy Pineiro | FG Made | under | 0.3826019825177006 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|08345c52-8552-4b04-813c-2f46ea4286f3 | underdog | Simi Fehoko | Receptions | under | 0.3799490814604448 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|32e57fb5-3a64-4c53-97aa-17eb15555590 | underdog | Cam Ward | Pass Yards | under | 0.3740656357441683 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|097da4d7-3f16-4c66-8f2f-b61faddf0e8b | underdog | Geno Smith | Pass Yards | under | 0.3642316931423827 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|f23e8b67-27a1-486b-84c4-7189cabc9f1b | underdog | Anthony Gould | Receptions | under | 0.3555233950704253 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|9b68965c-3c26-46a8-baae-a65e2eecf9ad | underdog | Brandon McManus | FG Made | under | 0.35442585143255134 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16834516 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16834515 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16864061 | prizepicks | Jack Endries | Rec Yards | over | 0.35094246505677495 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|1a25507b-8125-4524-83eb-bd6dc420d8a6 | underdog | Jared Goff | Pass Yards | under | 0.3501184306337788 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|b9435fd5-7f24-4097-8678-b955d06381e2 | underdog | Brandon McManus | Kicking Points | under | 0.34329896907216495 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|7ba17254-22b1-4b2c-9b2c-4eacf8338ebe | underdog | Michael Penix | Pass Attempts | under | 0.3427792036855505 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|5f6ecb8a-85b5-407a-ae58-df231bcd0038 | underdog | Bryce Young | Pass Yards | under | 0.33872136607667247 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|c2a5c1ca-7520-4e9d-89e0-2f5050979d68 | underdog | Kirk Cousins | Pass Yards | under | 0.32486137327291564 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|5a8bc524-564a-4dab-a5db-95d4d162a85c | underdog | Patrick Mahomes | Pass Yards | under | 0.32398040614566614 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|b339b747-c34b-4dee-a200-552943b8e199 | underdog | Anthony Gould | Receiving Yards | under | 0.3232196114915491 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16942049 | prizepicks | Demarcus Robinson | Rec Targets | under | 0.32153436796155255 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f9978ce2-db4f-472d-ae6b-7ae2ed4383c0 | underdog | Brock Purdy | Pass Attempts | under | 0.3095759047079447 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|1274d86c-7008-4ee9-8d78-0673167319cd | underdog | Simi Fehoko | Receiving Yards | under | 0.3080823241841719 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|00efed34-b5f2-4951-abad-8c8793e5c954 | underdog | Joe Burrow | Pass Yards | under | 0.3079937259333765 | 2026-11-12T07:07:56Z | 2026-11-16T01:20:00Z |
| underdog|4737cea0-616e-4604-a6e5-fd14ac48e709 | underdog | Tutu Atwell | Receptions | under | 0.30768720817936746 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a4aff594-458d-4ab2-8741-d573c94fd29c | underdog | Tyler Shough | Pass Yards | under | 0.30396344221607396 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|be878b70-3c21-471e-ae3b-905d8c13efb6 | underdog | Daniel Jones | Pass Yards | under | 0.29807473152035446 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|04d9b629-2110-40ef-b134-82649932148a | underdog | Jacoby Brissett | Pass Yards | under | 0.2979783699769716 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|de2cfefc-7fd1-4cea-827b-ac8782ff783e | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.29523037210716163 | 2026-11-13T01:09:17Z | 2026-11-15T21:25:00Z |
| underdog|017de95e-24a8-4a55-9185-759ab5e39785 | underdog | Drake Maye | Pass Attempts | under | 0.2870204978984535 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|ce6d242c-c0af-4493-9e32-e27a0163e420 | underdog | Deshaun Watson | Pass Yards | under | 0.28602615128970466 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|b5fb6661-40fc-4196-9686-d21c10809596 | underdog | Bryce Young | Pass Attempts | under | 0.2854974352714704 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2b554710-678c-443f-bb14-2208a77f507c | underdog | Justin Herbert | Pass Attempts | under | 0.2847606859755615 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| prizepicks|16941222 | prizepicks | Deion Burks | Rec Targets | under | 0.27909833862126254 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16834509 | prizepicks | Geno Smith | Pass Yards | under | 0.2763361682548745 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|cae65947-99bd-4320-b592-67e741e8e3f3 | underdog | Cam Ward | Pass Attempts | under | 0.27575003596339265 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|c8b72634-2199-44b4-918c-14b8b75a5665 | underdog | Josh Allen | Pass Attempts | under | 0.27359287330136317 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4426e732-6666-4dad-8847-df60408b6e0e | underdog | Eddy Pineiro | Kicking Points | under | 0.27246339729437163 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|cc32a0a8-f5c4-4665-b91c-5b1deb8556ae | underdog | Colby Parkinson | Receiving Yards | under | 0.2664498982632588 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| prizepicks|16864050 | prizepicks | Brock Wright | Rec Yards | over | 0.26570772133930776 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|bcdde121-b386-493e-864c-4bcc61392f15 | underdog | Tutu Atwell | Receiving Yards | under | 0.2642699536334714 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a7f2cda3-7806-4825-94cb-3314772c5a43 | underdog | Mike Washington | Receiving Yards | over | 0.26259620989363885 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|10263892-5ee5-4f59-8522-e20b1759b282 | underdog | Reggie Virgil | Receiving Yards | under | 0.26075603566011674 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|dd740bd3-6b74-45da-9756-483cfbb09d28 | underdog | Deshaun Watson | Pass Attempts | under | 0.25863657281386854 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16941221 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.25598115127940624 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16864049 | prizepicks | Tyler Conklin | Rec Yards | over | 0.2534382625358713 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|7e50f8a8-2469-4c42-8b1b-a4594a66ff81 | underdog | C.J. Stroud | Pass Yards | under | 0.2501195185787335 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|fe8292b1-ce05-486d-b732-66142a05472c | underdog | Andy Borregales | FG Made | under | 0.2485620967855957 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|76ebd5e4-98e6-4e69-b5c3-e679ebe74a07 | underdog | Chase Brown | Rush + Rec Yards | under | 0.24835130844327968 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|7279c326-d7e6-469c-9dd8-f0ec2a171e89 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.24593076762155852 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|83373ed9-f9ce-45e1-9625-900830675049 | underdog | Luca Lombardo | XP Made | over | 0.24473454966597602 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|b8c865b1-d106-47b2-9488-278cbed8b179 | underdog | Zach Charbonnet | Receiving Yards | under | 0.2431888534802754 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|6fd045da-e0dd-4ab0-8819-c11153822667 | underdog | Aaron Rodgers | Pass Attempts | under | 0.2422362767070224 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|26d4ddfa-d9fc-4f08-86e6-a916620f7be4 | underdog | Jordan Love | Pass Yards | under | 0.2343087179750497 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|14b46430-d112-4bb9-8474-9f3e043c7262 | underdog | Kyle Pitts | Receiving Yards | under | 0.23074083814986768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|97aac05f-2532-4c35-b6f1-c126fa85fa69 | underdog | Devin Duvernay | Receiving Yards | under | 0.2269256510729184 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|ed57ccdb-f29c-4416-ae5f-4aded39dc014 | underdog | Andy Borregales | Kicking Points | under | 0.22609089805035 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|71a44785-bf6a-4472-b7f6-b8472341adf9 | underdog | Alonza Barnett | Pass Yards | under | 0.22542330344856398 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|cb59d30a-2afc-4baa-8c0a-72f3ccb727e9 | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.22183471664785864 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|c056f71a-3a42-40b4-96f9-d2609cc9beed | underdog | Joe Burrow | Pass Attempts | under | 0.22141583740196058 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|169cb841-cffa-4109-8027-3415c4f4b563 | underdog | George Kittle | Receptions | under | 0.2194077839592593 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|29dffe93-265b-49a7-92f6-f591352f2f4e | underdog | Drew Mestemaker | Pass Yards | under | 0.2146249828603649 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| prizepicks|16834513 | prizepicks | Tyler Shough | Pass Yards | under | 0.21404760098629738 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|900a6acc-8f2e-4a73-8d6c-9a35b225cafb | underdog | Jared Goff | Pass Attempts | under | 0.2123603264736973 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|18a61f36-9cc0-49bf-813a-2cbed646880a | underdog | Demarcus Robinson | Receptions | under | 0.2098129701184389 | 2026-11-13T01:09:17Z | 2026-11-15T21:25:00Z |
| underdog|43eab978-b035-4b9e-91fe-97a8d57d94cb | underdog | Cooper Barkate | Receptions | under | 0.20979341100184778 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|e361b0b3-846c-4d00-ab28-2acf28eed70b | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.2087967118476648 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|e94c9cd9-eb43-4a62-912e-a83f4184c727 | underdog | Trey McBride | Receptions | under | 0.20737779171812365 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|34ffe77e-d083-49fe-a233-c2a7085b1a55 | underdog | Jordan Addison | Receptions | under | 0.20675489884434617 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ae9ffd9a-ad31-460f-b0d9-472730e245c3 | underdog | Demarcus Robinson | Receiving Yards | under | 0.20520961983923902 | 2026-11-13T01:09:17Z | 2026-11-15T21:25:00Z |
| underdog|e867dd92-2ce3-4e0e-8aa7-56b0042a3ae7 | underdog | Germie Bernard | Receiving Yards | under | 0.20503393613278686 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|081218b4-9196-449c-9fdf-62d2d39e0e03 | underdog | Zane Gonzalez | Kicking Points | under | 0.2048077405855635 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8cde15a-8b1a-4730-848f-163f3f890c7d | underdog | George Kittle | Receiving Yards | under | 0.20443082432893867 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|051a8c4f-8105-4095-aab4-7a5b0cba7371 | underdog | C.J. Stroud | Pass Attempts | under | 0.20323087968521425 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|65aed765-d701-4c7c-b180-c92353b6287f | underdog | Jadarian Price | Rush Yards | under | 0.2026452278850812 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|f90743a5-9d2a-47d3-a4e4-089c9764ad13 | underdog | Dak Prescott | Pass Attempts | under | 0.2011150399848315 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|306e7fdc-ff79-4617-b76c-a9f6f3f59c86 | underdog | Daniel Jones | Pass TDs | under | 0.20080324674994554 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6170a823-3e05-4ebd-97d3-044e73ce874f | underdog | Christian McCaffrey | Rush Yards | under | 0.20034018401002118 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|b786ee26-692a-4f4d-87d1-a8c475952d8a | underdog | Deion Burks | Receptions | under | 0.1984991277921363 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|8a1b591a-8990-49d6-b67d-de2ef4f6aacb | underdog | Rashee Rice | Receiving Yards | under | 0.1982963392264364 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|97f17a14-3d73-4de2-b8ed-5fe1812529d7 | underdog | Devonte Wyatt | Sacks | over | 0.1980309357726293 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|5066d8e1-f617-4f8b-ae0e-3354ea829f4a | underdog | Woody Marks | Rush + Rec Yards | under | 0.19725546483040635 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|87bfd021-0498-4180-b485-15610037e2e5 | underdog | Kaelon Black | Receiving Yards | over | 0.1963921949855576 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|83b44129-9596-4ab7-910d-0d5b5037b4ab | underdog | Geno Smith | Pass Attempts | under | 0.19625166531744365 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|45eaa191-9cdc-463c-8d91-beefc80f7256 | underdog | Trevor Lawrence | Pass Attempts | under | 0.19395844303678533 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|0ca5f198-cc15-4b12-b643-c3388a576202 | underdog | Tank Dell | Receptions | under | 0.19110284381179832 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8bfeabc8-5299-494a-bfeb-85b8e61de674 | underdog | Daylyn Upshaw | Receptions | under | 0.1909920607875113 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| prizepicks|16864052 | prizepicks | Jackson Hawes | Rec Yards | over | 0.18803943875076268 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|e53d005a-db4d-40e9-b843-107136039d88 | underdog | Bo Jackson | Rush Yards | under | 0.18598061441788571 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| prizepicks|16941214 | prizepicks | Savion Williams | Rec Targets | under | 0.185837094416891 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|3d1b3b14-b375-41f9-a9dd-f8e6b2e61696 | underdog | Anthony Colandrea | Pass Yards | under | 0.18438146826760027 | 2026-11-13T12:14:20Z | 2026-11-14T17:30:00Z |
| underdog|1e0b9273-b720-4a4b-9515-b69d611e23d5 | underdog | Zach Charbonnet | Rush + Rec Yards | under | 0.18394252594257776 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|0c90304b-97a9-4467-9736-313bc4155ac0 | underdog | Khalil Herbert | Rush Yards | under | 0.18354154495685115 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|145d0e7c-ebc2-4247-b8cd-ed5b0d92a96b | underdog | Ja'Marr Chase | Receiving Yards | under | 0.1833658811737735 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|afcf847e-b68c-4aba-bb13-ca2805a3d64d | underdog | Jackson Kleather | FG Made | over | 0.18300916559450464 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|336befd7-fc3b-4fc6-be96-8f9f930dd43f | underdog | Jared Goff | Pass TDs | under | 0.1828305718973564 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|2b2e87a1-8e51-41ec-9150-0c85b01fabcd | underdog | Tyler Warren | Receiving Yards | under | 0.1823268415850886 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|eb1c3c80-366a-4251-99fb-356251e8356f | underdog | Evan McPherson | FG Made | under | 0.18227554836779813 | 2026-11-11T16:13:16Z | 2026-11-16T01:20:00Z |
| underdog|4bd25d23-908c-451e-9da7-e2c0ccf89bef | underdog | Jordan Shipp | Receptions | under | 0.18194525950331109 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|08002729-32e7-4c29-b25d-22644abe6bad | underdog | Jack Bech | Receiving Yards | over | 0.18168505454405048 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| prizepicks|16834801 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1816833032066426 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|f1ae34e8-674a-4744-a233-47c5f2216dd4 | underdog | Cam Ward | Pass TDs | under | 0.18083709268551018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16864055 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.17800572418642757 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|2204a7a9-9d27-447e-bdbd-9156e58564a4 | underdog | Zach Charbonnet | Rush Yards | under | 0.17732013196837215 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|607f5ae6-2116-4003-99af-5442503e0ae4 | underdog | Brock Purdy | Pass TDs | under | 0.17680376455348845 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|129b5b3b-cca7-4376-9115-9a21b2e1a8f2 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.17549254438509287 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|513300f9-e455-4d65-bc1c-d2a6b4d794fc | underdog | Jordan Mason | Rush + Rec Yards | under | 0.17499086646220285 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|ab208bdb-ddee-40f9-a2ed-f481ef72f216 | underdog | Drake London | Receptions | under | 0.17466437471048346 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e6ed003a-0261-43f3-8539-8b3a5843dcf4 | underdog | Michael Hawkins | Rush Yards | under | 0.17369289774038532 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|bed83661-cc7d-4b22-9b07-e0978ada4d5d | underdog | Jameson Williams | Receiving Yards | under | 0.1733097016002607 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|9a273eba-2d5d-404c-b81f-93d6389c3340 | underdog | Ben Black | Receiving Yards | under | 0.17156866779821567 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|cb516925-3b8d-476b-a0a1-f86967eb258b | underdog | Deion Burks | Receiving Yards | under | 0.17072964581538708 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|b59c83a6-7075-4cc3-84dd-27157fa643ac | underdog | Jahan Dotson | Receptions | under | 0.17063963423916995 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|16f7ac78-0db9-439a-b28c-c528416128ed | underdog | Breece Hall | Rush + Rec Yards | under | 0.17060228312474868 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|be0035fc-f65b-4a47-a351-fdae458aeb02 | underdog | Seth McGowan | Rush + Rec Yards | under | 0.17011641982527048 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| prizepicks|16864057 | prizepicks | Oscar Delp | Rec Yards | over | 0.16971647479255814 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4e9d2b81-8437-409b-8ff4-2380820c1bc4 | underdog | Gianni Spetic | XP Made | over | 0.1690686381121324 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|ee9a0405-33bb-456d-a2ef-754c6c2c03a7 | underdog | Tyler Shough | Pass Attempts | under | 0.1678377974371722 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8905aa05-23fc-48e9-a07c-e1e7471f42ac | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.16733291732669142 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| prizepicks|16942016 | prizepicks | Tutu Atwell | Rec Targets | under | 0.16716285331431757 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|696c6b73-3e04-426b-a463-26276c4aee5c | underdog | Ryan Fitzgerald | FG Made | under | 0.16692795074675848 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c97d330b-3d6f-4b03-83d5-f93c56394bed | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.16641302347698494 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16913746 | prizepicks | Vanja Milinkovic-Savic | Goalie Saves | under | 0.16609088018417573 | 2026-11-12T07:07:56Z | 2026-11-13T14:45:00.000-05:00 |
| underdog|ab3ca458-4792-4be4-86cf-cfcefafc1532 | underdog | Walker Eget | Pass Yards | under | 0.1656176011824837 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|b81b56da-fe21-4e55-9f3d-fb0b1d061257 | underdog | Daniel Jones | Pass Attempts | under | 0.16440373749700898 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|659b286c-687a-43f0-b782-5a1234a05458 | underdog | Quinshon Judkins | Receptions | over | 0.16431586645270752 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16941224 | prizepicks | Tyler Warren | Rec Targets | under | 0.16357413164889356 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5d9334d9-a335-471c-92f4-54bd683075ca | underdog | Hank Brown | Pass Yards | under | 0.16133319573176919 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|9a9b4886-cd1f-4523-9dc3-cd8753a51f8b | underdog | Kirk Cousins | Pass Attempts | under | 0.16130209940228557 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|43d067f1-bb0f-4c09-acf1-fa7919bc9723 | underdog | Jared Goff | Rush Yards | over | 0.16011142578061638 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|a2bd1b57-9bee-4a1a-a27a-1cbfdd5681b8 | underdog | Elic Ayomanor | Receptions | under | 0.15978654253309588 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0d051be2-f5ae-4b14-b42e-964de378c630 | underdog | Katin Houser | Pass TDs | over | 0.15938089279781648 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|28e41540-e6d5-4ec1-b474-b3fb179168ec | underdog | Justin Herbert | Pass TDs | under | 0.1593713737739526 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|c4908744-700e-43fa-a098-7874f3c71c27 | underdog | Evan Stewart | Receiving Yards | over | 0.15933869172649118 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|3e4ae174-e4d9-4c59-b781-2aa8bc07c297 | underdog | Wayne Knight | Receiving Yards | over | 0.15917827448977762 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|f96a368b-744f-47f4-bd47-9731731f5d1b | underdog | Caden Buhr | FG Made | over | 0.15900548451896535 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| prizepicks|16834646 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.15848722202295062 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f3733138-10af-46da-8e69-cf5ca4b940fc | underdog | Reggie Virgil | Receptions | under | 0.15825220568688703 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d4535591-3a5f-4c28-b756-d85acd4fdf77 | underdog | Jordan Mason | Rush Yards | under | 0.15679467436665007 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16864059 | prizepicks | Ian Thomas | Rec Yards | over | 0.15662706211871924 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|25185fe8-2e75-4f8e-a1b5-f6c471df1357 | underdog | Arch Manning | Pass TDs | over | 0.15631529903366037 | 2026-11-12T07:07:56Z | 2026-11-15T00:30:00Z |
| underdog|51482ef6-863b-47ca-8fe5-ddce1363c28f | underdog | Theo Melin Ohrstrom | Receiving Yards | over | 0.15614556650528089 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|34592e3c-3b83-4af7-bd2b-617a52ca4334 | underdog | Trey McBride | Receiving Yards | under | 0.15553372270182042 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|eb8162e7-e14c-4796-b160-d74fedaa7315 | underdog | Jordan Love | Pass Attempts | under | 0.1550294298047722 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|b470bd4b-1813-44ad-9c4c-e7d50bdbeae5 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15499103436448625 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| prizepicks|16941231 | prizepicks | Rashee Rice | Rec Targets | under | 0.1549150253690711 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4ff762f9-ce25-4a46-92ee-4f38ba5be3b1 | underdog | Nolan James | Rush Yards | under | 0.1540052267861841 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|97a67afc-3f9f-4982-8bae-be868c2c4737 | underdog | Devon Dampier | Pass Yards | under | 0.15303323942761993 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|585b41b2-1294-443c-8440-2524471c4ddf | underdog | Laquon Treadwell | Receptions | under | 0.15250354276005051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0b6b9464-f3ca-4d21-bb53-19e9a2f9619a | underdog | Karl Brooks | Sacks | over | 0.15173315822223826 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|abcda181-8a45-42d8-bd51-8479c62c0cba | underdog | Holden Geriner | Pass TDs | under | 0.15167357913948876 | 2026-11-12T07:07:56Z | 2026-11-14T00:00:00Z |
| prizepicks|16849017 | prizepicks | Ty Dieffenbach | Rush Atts | under | 0.15134416123436234 | 2026-11-11T06:09:33Z | 2026-11-13T21:00:00.000-05:00 |
| underdog|c5c4fe7e-563e-4a77-ae50-060011c7dec8 | underdog | Xavier Hutchinson | Receptions | under | 0.1509666630300549 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16933287 | prizepicks | Elizabeth Mandlik | Break Points Won | under | 0.15093061145365672 | 2026-11-13T01:09:17Z | 2026-11-13T10:00:00.000-05:00 |
| underdog|af522396-84d1-406b-b37c-206c42ee1d80 | underdog | Jake Fette | Pass Yards | under | 0.15017672058611453 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| prizepicks|16942048 | prizepicks | George Kittle | Rec Targets | under | 0.14983085550655606 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|2e165ef5-272e-47fb-8214-52bc9d58510a | underdog | Amon-Ra St. Brown | Receptions | under | 0.14980442293467233 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|c6f5d95f-2b53-4656-bed1-792f520c72ba | underdog | Garrett Wilson | Receiving Yards | under | 0.14922011393352663 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16941176 | prizepicks | Reggie Virgil | Rec Targets | under | 0.14907298120417656 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|e3317ebd-1d1a-4ac2-8dc1-999860638691 | underdog | Jameson Williams | Receptions | under | 0.1486746602368635 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|1a20f785-f85c-4e70-a420-adf5f0ed3164 | underdog | Ollie Gordon | Receptions | under | 0.148665850420447 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5211515d-7ad3-4eb4-b67f-a89b5e6b4abd | underdog | Laquon Treadwell | Receiving Yards | under | 0.1485527232635908 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|7d76e9dd-5308-4c1a-ba1c-ba61b79e4408 | underdog | Jayden Maiava | Pass TDs | over | 0.14850033842731425 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|3dd60339-cf17-45f0-b767-75c894f95225 | underdog | Cooper Barkate | Receiving Yards | under | 0.14832914398251418 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|21840c90-ffe6-4de8-a572-babff46fbc10 | underdog | Nico Collins | Receiving Yards | under | 0.14826178517808342 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|5436fb8f-64d7-4f34-b094-0a3b99848f90 | underdog | Thomas Castellanos | Pass TDs | under | 0.1480820063637336 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|58103c82-771e-4fbe-bcb3-fbd7b42b077f | underdog | Matthew Stafford | Pass Yards | under | 0.1479404364360365 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|61750b40-600e-4985-ba4f-4746992f5a79 | underdog | Pat Freiermuth | Receiving Yards | under | 0.14668230275794958 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|bd5586fa-284e-4331-87b5-39a9a336cb92 | underdog | Isaiah Marshall | Pass TDs | under | 0.1455916479416146 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|7281e3b0-a702-402a-8b62-fc9add59bf36 | underdog | Chuba Hubbard | Rush Yards | under | 0.14389175335524607 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cf6cb602-6d19-4560-92cf-eba77e59abce | underdog | Byrum Brown | Pass Yards | under | 0.14379008226835766 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|4d0e9f33-30c1-4cbd-811b-3f0d61054bcb | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.14378965381475595 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| prizepicks|16942028 | prizepicks | Hunter Henry | Rec Targets | under | 0.1433641205147107 | 2026-11-13T12:14:20Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|21ace0c9-85f0-43f3-9392-a8bbadc5666b | underdog | Trey Butkowski | XP Made | over | 0.14320322887137465 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|f2e836b0-0889-4532-817f-f54d419292c9 | underdog | Connor Hawkins | FG Made | over | 0.14287325912611332 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|4c42a4f7-59bd-4cc5-96de-2caa245cf96e | underdog | Ja'Marr Chase | Receptions | under | 0.14198666098231127 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8d8893ec-f444-46e0-bc6b-b229539f440a | underdog | Kyren Williams | Rush Yards | under | 0.14173771981934158 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a8df2bfd-753f-497d-81c7-7d8c49469970 | underdog | Foster Moreau | Receptions | over | 0.14124636142536817 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|c14dec7d-e82b-46f4-a1fb-3c0d04a7e2d0 | underdog | Tyler Robles | FG Made | over | 0.14073377627119343 | 2026-11-13T01:09:17Z | 2026-11-14T21:15:00Z |
| underdog|3a49fa1c-36bc-416d-92d4-c3b2c6e26dbc | underdog | Jordan Shipp | Receiving Yards | under | 0.14060337375049958 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|9225cf3c-9296-4248-97ac-5b3485eb6a24 | underdog | George MacIntyre | Pass TDs | under | 0.14047384523423212 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| underdog|fbacb3aa-1a1f-4fcc-aea9-63cdc8591a0f | underdog | Dierre Hill | Rush Yards | under | 0.13996174257805338 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|fe324cdb-30f6-4ec0-b83b-b7cfbc3bb25f | underdog | Zay Flowers | Receptions | under | 0.13889916886043374 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|58ce845a-51d9-463a-aa26-838b3a4ff3b9 | underdog | Khalil Herbert | Receiving Yards | over | 0.1386036873391392 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|aa70ba25-a303-4c52-9769-639de476cfcf | underdog | Javonte Williams | Receptions | under | 0.13847697518960522 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|d916e27f-ed11-420a-9678-c3711e981147 | underdog | Christian Watson | Receptions | under | 0.13831813948612726 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|23ae2186-6a88-42f5-bc18-a2ecf2955bea | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.13801470883584288 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16834820 | prizepicks | Christian McCaffrey | Rec Yards | under | 0.1379306598172515 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16941177 | prizepicks | Trey McBride | Rec Targets | under | 0.13778578805206876 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|ea76791d-135e-4d10-bb38-5059c94eda28 | underdog | Ollie Gordon | Rush Yards | under | 0.13620307901154893 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|562eb515-a846-4afd-aef0-5624e8ade1e0 | underdog | John Mateer | Pass Yards | under | 0.1360173762068857 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|97a856d7-a3cf-475d-8612-0b72b87c6603 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.13600948649593914 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|fe724bab-b489-4c4c-8b33-22905a3abcf6 | underdog | Caden Buhr | XP Made | under | 0.1356076785255077 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| prizepicks|16941182 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.13558369281022298 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|d16f08ba-8dcb-45d6-82db-c36a28ca4b50 | underdog | Tucker Kraft | Receiving Yards | under | 0.13538807270342912 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e121edb0-7612-4a41-a5f0-4d185a267e18 | underdog | Isaiah Marshall | Pass Yards | under | 0.13514145247717368 | 2026-11-13T12:14:20Z | 2026-11-14T22:30:00Z |
| underdog|f360ab27-deb2-4f72-b437-6349dc28e573 | underdog | Parker Washington | Receptions | under | 0.13510031202715655 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|170532ef-6942-4db9-8607-c52a3838bfe9 | underdog | James Cook | Rush + Rec Yards | under | 0.13472649314653207 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|357567dd-807d-4205-8940-b5dbeb224c9d | underdog | Christian McCaffrey | Receiving Yards | under | 0.1337306969230765 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| prizepicks|16864054 | prizepicks | Jonnu Smith | Rec Yards | over | 0.13268296711964045 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|f0100902-2759-4817-a164-2c7d3cb0236d | underdog | Quinshon Judkins | Receiving Yards | over | 0.13251091684739158 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8033e91a-8918-4480-835b-e3a813bc5008 | underdog | Blake Corum | Rush + Rec Yards | under | 0.13222893877316322 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|8475bce1-90cf-43c8-9bdc-19e950db157a | underdog | AJ Barner | Receptions | under | 0.1321036071433428 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|ad49c1a3-20cd-48ee-8447-3f9c6b778470 | underdog | Zach Charbonnet | Receptions | under | 0.13186048887942314 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|606f16ce-fb51-4f44-af6e-d6bbcf312123 | underdog | Parker Washington | Receiving Yards | under | 0.13139403359963797 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|c5d93fba-443f-4254-bbb2-c9a81bae6bd5 | underdog | Derrick Henry | Rush Yards | under | 0.1311683774303094 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|7a1ed30d-da55-441c-b6f0-c5cf7618c573 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.13110361173012197 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|668418d8-7c0f-4d71-8dfe-70e116c329d5 | underdog | Caleb Komolafe | Receiving Yards | over | 0.13076499471061398 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16941180 | prizepicks | Drake London | Rec Targets | under | 0.13054552219056026 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16834805 | prizepicks | Tucker Kraft | Rec Yards | under | 0.13048896157966627 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5265ce9f-d1a4-4ac8-8168-2476d15b68b4 | underdog | Rashee Rice | Receptions | under | 0.13038787864818369 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|cc9534dd-af53-46ff-8c5c-3d5f8947c322 | underdog | Thomas Castellanos | Pass Yards | under | 0.13025265461754632 | 2026-11-13T12:14:20Z | 2026-11-15T02:30:00Z |
| underdog|6e81085a-3d8a-42e7-819c-98a47c132d00 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.12980647573211435 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|693fb5e3-148f-43fc-b054-d44605b4d1fb | underdog | Kimani Vidal | Receptions | under | 0.12943283574984177 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|a51976ae-665d-4e1e-9e7f-fe7fb5e0ba10 | underdog | Deebo Samuel | Receiving Yards | under | 0.12866658249865393 | 2026-11-13T12:14:20Z | 2026-11-15T21:25:00Z |
| underdog|96e276e1-1776-4362-ad24-31d755491dfe | underdog | Nyziah Hunter | Receiving Yards | under | 0.12807471318269004 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|da61ada7-6550-4585-84d2-1388eed99d50 | underdog | James Cook | Rush Yards | under | 0.12765289952620407 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|c7678b73-9c60-4770-9676-d99c5e6b71c7 | underdog | Khalil Shakir | Receptions | under | 0.12759270653403465 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6316e5dc-af73-4c98-8b96-f7165729f535 | underdog | Jaylen Warren | Receptions | under | 0.1263299336202357 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|7d4a66d7-5e66-4433-b339-05c2970ccb9f | underdog | Josh Allen | Pass TDs | under | 0.12444210905973119 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9b61aff8-a93b-4671-b173-f7ca4286eead | underdog | Jakobi Meyers | Receiving Yards | under | 0.12435976055640752 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|64fe717c-14a9-4a4d-b286-fb2c31130ca5 | underdog | Jason Myers | FG Made | under | 0.12423824312528586 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|7e047dba-151c-4432-9416-d4e3155ae527 | underdog | Jordan Mason | Receptions | under | 0.12364698409171138 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|94c55bd4-7e31-4d47-b147-9078d5c53331 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.12317941215822503 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|eace84de-3208-48c2-a13a-790770049e30 | underdog | Colby Parkinson | Receptions | under | 0.12317933713140317 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|7da7556c-a1f4-42ec-ad80-c12d0d953524 | underdog | John Metchie III | Receptions | under | 0.12299883356747898 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16887420 | prizepicks | Dilin Jones | Rush Atts | under | 0.12214678937678047 | 2026-11-12T07:07:56Z | 2026-11-14T19:30:00.000-05:00 |
| underdog|8b13e336-25a6-43c9-a99c-1123e53e88c6 | underdog | Jordan Addison | Receiving Yards | under | 0.12210936192935584 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|7a9e2c86-7dba-4c5b-bb6a-3ef5749dc1c0 | underdog | Zane Gonzalez | FG Made | under | 0.1218622688697637 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cf37c889-4eca-4cd0-acdb-5ef3caf76c5b | underdog | Ka'imi Fairbairn | FG Made | under | 0.12158788342133897 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b74d6dd8-986c-4d47-a602-c9563892a472 | underdog | Seth McGowan | Receptions | under | 0.12157868635609315 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|c2dbcea4-f1d3-48e4-8a3d-1ca56f89605e | underdog | Luke Fahey | Pass TDs | under | 0.12082321745904379 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|f50cd189-6177-4b69-b305-61d234a7a82e | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.12075474357899663 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|59450b43-2430-40b2-87aa-bdea2257af7d | underdog | Blake Corum | Rush Yards | under | 0.12071235785906831 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|a5e30ad8-1103-42c0-a807-c001b30ff2c9 | underdog | Cam Little | FG Made | under | 0.12040122477593274 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|23d7ce9e-ca96-462a-9341-596b14afa179 | underdog | AJ Surace | Pass Yards | under | 0.12035603183798049 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|45f18132-2bc5-4802-9392-b9791841f245 | underdog | DK Metcalf | Receiving Yards | under | 0.1202334887553217 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|61af56d0-7bbf-44b8-95db-df3abfd900b4 | underdog | Michael Salgado-Medina | FG Made | over | 0.11962802201761302 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|dd1d9caa-101d-491b-badf-bb1b87735495 | underdog | Jonathan Taylor | Receptions | under | 0.1194495485112097 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|04f3c9ed-cd8b-4094-ae64-c8df94076667 | underdog | Elina Svitolina | Double Faults | under | 0.11932112983967558 | 2026-11-13T01:09:17Z | 2026-11-13T21:10:00Z |
| underdog|b9a30083-4e27-4adb-bed7-b117feee5e5b | underdog | Davis Allen | Receiving Yards | under | 0.11926942043123134 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|48551e6e-707c-45df-bd3c-bd742dd16fc2 | underdog | Evan Stewart | Receptions | over | 0.1188898847151112 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| prizepicks|16941218 | prizepicks | Nico Collins | Rec Targets | under | 0.11882558222332162 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7d1eec2d-0448-4b94-b456-6922f66904df | underdog | Konata Mumpfield | Receiving Yards | under | 0.1188198417781472 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|941cffba-4b42-4435-8769-a31cbd72dc50 | underdog | Tee Higgins | Receptions | under | 0.11877140010710996 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|cc3c5506-155c-4fef-9a4a-d7e5ed500010 | underdog | Bhayshul Tuten | Rush Yards | under | 0.11861726759120372 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|77d45d7c-6c80-4ce0-845e-806b3103525f | underdog | Jasen Lopez | Receiving Yards | under | 0.11852010308283689 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| underdog|45e66548-e5c7-4a7e-956f-625a5da4c258 | underdog | Demon June | Rush Yards | under | 0.11838823555999534 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|bf204c41-dc6c-45e7-ac59-b29e8b440e59 | underdog | Adonai Mitchell | Receptions | under | 0.11812295339085888 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|c8dd15d3-4419-45ae-a884-55bd1290a78f | underdog | Garrett Wilson | Receptions | under | 0.11792466411828051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16942023 | prizepicks | Greg Dulcich | Rec Targets | under | 0.11772120696406463 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c7c1feb1-0d59-4f4b-a9e9-7f9535f0df33 | underdog | Drew Mestemaker | Pass TDs | under | 0.11768525797870777 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|87995482-f84f-41d8-8800-702c9335230d | underdog | Noah Fant | Receiving Yards | over | 0.11765498132506613 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|185591e2-8a87-4901-a817-5630cf1e58ae | underdog | Jackson Harris | Receptions | under | 0.11759493096585649 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|782044c7-2f53-457b-ac41-94e27e9261d8 | underdog | Dilin Jones | Rush Yards | under | 0.11750758277247497 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|471b086b-8e30-4b89-8030-a31f346304fa | underdog | Bryce Young | Rush Yards | under | 0.11671082433541491 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16934020 | prizepicks | Aiden Flora | Rush Atts | under | 0.11622830763827319 | 2026-11-13T12:14:20Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|3614f11e-aa5b-4d51-9032-b3f195f419d5 | underdog | Jacobo Echeverria Lozano | XP Made | over | 0.1161780296945728 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|49e3a291-f12d-46b8-94cb-887193ba15f5 | underdog | Aryna Sabalenka | Double Faults | under | 0.11605055261485508 | 2026-11-13T01:09:17Z | 2026-11-13T21:10:00Z |
| underdog|2420a1ae-3693-4c18-900e-a72641811872 | underdog | David Olano | FG Made | over | 0.11523648181086699 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| prizepicks|16913759 | prizepicks | Jan Oblak | Goalie Saves | under | 0.11465066373203547 | 2026-11-12T07:07:56Z | 2026-11-13T14:45:00.000-05:00 |
| underdog|e004a1f2-b6a2-4812-95f8-7de64c96598a | underdog | Derrick Henry | Rush + Rec Yards | under | 0.11454429482230055 | 2026-11-11T16:13:16Z | 2026-11-17T01:15:00Z |
| underdog|4980e13b-b332-4cb3-b311-c8aada8c0159 | underdog | Kyle Pitts | Receptions | under | 0.11437219464215653 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5c625434-b11a-46c4-a6af-d0fc53c2f2a9 | underdog | Dak Prescott | Pass TDs | under | 0.11340998483490083 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|20ebc7f0-08e7-425c-99e6-1af2fd35d3fb | underdog | Dierre Hill | Receptions | over | 0.11330426194714777 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|7a6dd424-2fdc-466c-b847-16a47251614c | underdog | Connor Calvert | FG Made | over | 0.11328783871436227 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|7857c427-00ea-44f3-9c45-48f9e7f2c9b5 | underdog | Trevor Lawrence | Pass TDs | under | 0.11317375136374375 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|865ea4d0-9767-4b60-8c93-3d426d51d7a8 | underdog | Breece Hall | Rush Yards | under | 0.11314740643781795 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9426e0ec-8206-417f-b10b-e3539e8bfc77 | underdog | Trey Butkowski | FG Made | under | 0.11305000927901931 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|2f0eb7c1-de78-4fe0-962d-72826e5d0d6f | underdog | Malik Washington | Receiving Yards | under | 0.11299206031990372 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|cde7c70e-d481-4784-9d2e-2a93b9e2daa7 | underdog | Sam LaPorta | Receiving Yards | under | 0.11256764743862924 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|d30c2651-ff31-4115-a5e9-3e40d4bc947f | underdog | Ryan Hopkins | Pass Yards | under | 0.1125057528061264 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|9861fb0a-1a44-4119-9006-6e9c7ea976cd | underdog | Cole Tabb | Receiving Yards | over | 0.11223545456037964 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|c521d73c-2a75-4a75-9c17-33b2205da002 | underdog | Rico Dowdle | Rush Yards | under | 0.11217901116890283 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|992fa67a-feec-4626-95dc-f2c04f2580cf | underdog | Matthew Stafford | Rush Yards | over | 0.11213733898109268 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|461f158a-b95d-4759-b48d-ca72ea246c1d | underdog | Jadarian Price | Receptions | under | 0.1116533229738974 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|5db956f1-b511-4050-a6b4-671177d5b7ee | underdog | Max Gilbert | FG Made | over | 0.11156379694782498 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| prizepicks|16941190 | prizepicks | Zay Flowers | Rec Targets | under | 0.1114495281356832 | 2026-11-13T12:14:20Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|3b01acf2-eefa-4496-a642-bf1c849db45d | underdog | Chris Bell | Receptions | under | 0.11116746721824522 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|611d5095-8649-470d-aad5-f9b1d3f8f85c | underdog | David Olano | XP Made | over | 0.11008098092875374 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| prizepicks|16870373 | prizepicks | Brock Bowers | Rec Targets | under | 0.10995797661937423 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|038e387a-d50b-4f48-affd-5ef89b035e44 | underdog | Jonathan Taylor | Rush Yards | under | 0.1097004716717318 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|6822a773-5f4b-457d-a3c1-4ba92bff9865 | underdog | Junior Sherrill | Receptions | under | 0.10806956997685557 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|59cf7dc6-d278-4398-adeb-4bfc5f294cc7 | underdog | Holden Geriner | Pass Yards | under | 0.10797330072021805 | 2026-11-13T01:09:17Z | 2026-11-14T00:00:00Z |
| underdog|2d9a6fb5-8c84-46f0-bcba-b14291360099 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1075619962096197 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|fd21faaf-bffa-4216-93db-e8f524c4e0f0 | underdog | Gianni Spetic | FG Made | over | 0.10755910381656675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| prizepicks|16897138 | prizepicks | Thomas Castellanos | Rush Atts | under | 0.10724354939051584 | 2026-11-12T07:07:56Z | 2026-11-14T21:30:00.000-05:00 |
| prizepicks|16942015 | prizepicks | Colby Parkinson | Rec Targets | under | 0.1069695868003464 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|4bd23df4-deb5-49bc-8c4b-86a313802ac5 | underdog | Mason Taylor | Receptions | under | 0.10673294964450386 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|ea72a765-c2a4-45fa-8d1c-4ed978abad0e | underdog | Chase Brown | Rush Yards | under | 0.10663476696726415 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|02dfa4d1-6864-4a3b-a333-800bb999bca2 | underdog | Kirk Cousins | Pass TDs | over | 0.10613134956836634 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|325a8205-94f4-4430-8e00-d9d2ddc2a9ec | underdog | Mike Gesicki | Receptions | under | 0.10565045023732611 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|ee19d5c8-bb25-43c9-8e93-ac1b2e8e0ad7 | underdog | Tyler Higbee | Receptions | under | 0.10523114864570438 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|5295bac1-30de-41a5-a366-720942bb1b37 | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.10500925442321007 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|5644a858-15de-44fe-a1f7-0fd329feac31 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.10415675245658362 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|0ff862cd-b707-4128-b7b5-1837380bc39e | underdog | Davis Allen | Receptions | under | 0.10399951412686148 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|9b902c48-bdaf-41d6-a2bc-2a1798df028c | underdog | Matt Gay | Kicking Points | over | 0.10370064668973422 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|b6d53a6f-91ff-4d84-891c-ba5ec224a70d | underdog | Trey'Dez Green | Receiving Yards | under | 0.10332531587973903 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|f399a008-c858-4758-94a2-ef7afed2d790 | underdog | Mazeo Bennett | Receiving Yards | under | 0.1031381432688534 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|077e30e4-9320-449b-a228-b1b97a8abd83 | underdog | Trey Smack | FG Made | under | 0.10289090955929303 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|846092aa-807d-43c4-80cd-af7dc9c3234b | underdog | Breece Hall | Receptions | under | 0.10276383668301403 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|b58d4951-3cf7-4235-9f2b-f9836e774dae | underdog | Drake London | Receiving Yards | under | 0.1020493545084814 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2d00be5f-dba3-4c34-a708-079e49994847 | underdog | Calvin Ridley | Receptions | under | 0.10167650278337226 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|51820dd7-063c-4751-be38-84c9a6983fed | underdog | Christian McCaffrey | Receptions | under | 0.1016183424097532 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| prizepicks|16942021 | prizepicks | Caleb Douglas | Rec Targets | under | 0.1016082162097357 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|ebba22ce-6173-4b6e-b454-1df66a084a08 | underdog | Tyler Higbee | Receiving Yards | under | 0.10146410288215946 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|dd69b512-b698-428c-bd34-5a8e020ae6e3 | underdog | Tyler Bass | FG Made | under | 0.10117399188091525 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6e7a5219-ee88-466f-80b7-208dc41a4a98 | underdog | DeSean Bishop | Rush Yards | under | 0.09973628451165995 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|ffdf6928-c765-4901-bcf9-925978a42dfd | underdog | Jacoby Brissett | Pass Attempts | under | 0.09857496516557318 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|8150638b-9a7e-427a-aba6-76704ed97855 | underdog | Ethan Moczulski | FG Made | over | 0.09839210553400768 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|6f6e76ef-69e3-4315-83cb-ea6ec48daea1 | underdog | Chad Ryland | FG Made | over | 0.09807717467815241 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|5f95b22a-44d2-4c89-b35c-17c275ad8b09 | underdog | Gunner Stockton | Pass Yards | under | 0.09783371432939425 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|89777911-6168-4f57-8662-8d3f09ac1716 | underdog | Chris Boswell | FG Made | under | 0.09775400624264463 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|369bb4d5-4bfc-4124-8e50-51030898365a | underdog | Tony Pollard | Receptions | under | 0.09758293132802409 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|954ad452-8bec-4840-bae5-048bcd6542d9 | underdog | Mitchell Evans | Receiving Yards | over | 0.09733725531537551 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9014f61e-7a7c-4198-9cdb-151bfe9070cc | underdog | Mason McKenzie | Pass TDs | over | 0.09712306017585648 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|16dc39f4-bd6e-4e92-89f9-ae72c02b8c0a | underdog | Jonathan Dimas | FG Made | under | 0.09709066624784901 | 2026-11-11T16:13:16Z | 2026-11-14T03:15:00Z |
| underdog|7d1b7f21-aa87-4f17-bf44-77c18f015227 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.09657686894256146 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|4449e604-1137-41ce-845a-cf2d65eee460 | underdog | Darian Mensah | Pass TDs | over | 0.09646249729861844 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|506821c8-a453-4a20-a85b-f97bfaa4e1fe | underdog | Zay Flowers | Receiving Yards | under | 0.09632328774235666 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|92efc1e0-6e09-45b5-9380-ed2ef9424766 | underdog | Noah Fifita | Pass Yards | under | 0.0962718991546474 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|0e196ee8-4db3-4fce-a18c-a14e74e12905 | underdog | Marcel Reed | Pass TDs | under | 0.09624315580046416 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|c3d405f2-f65d-4f28-9dab-86ac43a8d975 | underdog | Kenneth Walker III | Receptions | under | 0.0960980842757887 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|8ef9ae68-5181-46e4-b083-fe1c2dc728cc | underdog | Cardae Mack | Rush Yards | under | 0.09591445564927736 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|5d124f4c-22e7-4e63-aabe-d97f5d3a856e | underdog | Jakobi Meyers | Receptions | under | 0.09590453564859014 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|42c42d28-9906-4573-bc38-358501324684 | underdog | Trinidad Chambliss | Pass Yards | under | 0.09587484579963956 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|414eda07-0d36-4a31-bc1a-e617e8d005d8 | underdog | Mazeo Bennett | Receptions | under | 0.09562543815033575 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|382be9ea-4cd8-4981-9243-ba13a3e9bca4 | underdog | Evan McPherson | Kicking Points | under | 0.09540198598918959 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|45ea8cf2-2e66-4230-a4fe-1bc4be7cfbd4 | underdog | Jaylen Raynor | Pass Yards | under | 0.09539041220737754 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|a0d2c31e-f6cb-4bee-81be-02dcf80d0449 | underdog | Carnell Tate | Receiving Yards | under | 0.09537210117181494 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|6ea29960-71f2-4c50-b308-5014bf65c42d | underdog | Jahmyr Gibbs | Rush Yards | under | 0.09464878956736067 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|0789564f-aac7-4796-ad55-71434916df49 | underdog | T.J. Hockenson | Receiving Yards | under | 0.09463140071749987 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d2cdc210-fcc2-4276-9810-a70ee7020fdd | underdog | Bear Bachmeier | Pass Yards | under | 0.09458764346729465 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|1d37f459-f6d1-4307-99ec-bf177e3a6437 | underdog | Jason Sanders | FG Made | over | 0.09433045418762181 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fa4c7f93-3a59-4d24-a659-ab3a46d49e2b | underdog | Greg Dulcich | Receiving Yards | under | 0.09403894171268923 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|2ab602db-837a-4c6d-baf3-4ae491410bb2 | underdog | Josh Cuevas | Receiving Yards | over | 0.09390233366912559 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|f25cc4b1-d05b-4650-aa6c-9a9a1304580d | underdog | Rashid Shaheed | Receptions | under | 0.09383692899756757 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|60aaccb5-940f-4bc2-a9c2-5cd432a930b3 | underdog | Kenny Minchey | Pass Yards | under | 0.09378357249772407 | 2026-11-13T01:09:17Z | 2026-11-14T23:15:00Z |
| underdog|5c500fd7-4b60-43bf-9f00-634ec5ecfade | underdog | Josh Cuevas | Receptions | under | 0.09376007412754472 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|192016d6-c59a-4f73-bd58-5a17cebf9824 | underdog | Keelon Russell | Pass Yards | under | 0.09373932422374998 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|1887c7e3-ddd8-484c-a447-87758d64c76e | underdog | Thomas Castellanos | Rush Yards | under | 0.09371264365278897 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|3d42fad4-14d1-4b6c-a87e-74f9a36ad66e | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.09346265131080267 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|abf6366a-98c0-4dca-a13b-5a0221de2afa | underdog | Trinidad Chambliss | Pass TDs | over | 0.09346167782668713 | 2026-11-11T22:47:13Z | 2026-11-14T21:15:00Z |
| underdog|f51c8941-84b9-4662-a1b2-dbb0c6b4e70d | underdog | CeeDee Lamb | Receiving Yards | under | 0.09269504099383397 | 2026-11-13T12:14:20Z | 2026-11-15T21:25:00Z |
| underdog|ae5450f4-879d-43e7-9896-44a93fb15d07 | underdog | Alessio Milivojevic | Pass TDs | under | 0.092497836794454 | 2026-11-13T01:09:17Z | 2026-11-14T21:15:00Z |
| underdog|f8f6356d-592e-4e3a-8d8b-6bfaa2874eef | underdog | Luke Fahey | Pass Yards | under | 0.09241833281916434 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| prizepicks|16864060 | prizepicks | Luke Farrell | Rec Yards | over | 0.0923962774082826 | 2026-11-11T06:09:33Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|147243e6-fcee-4814-8b0f-73b49c924682 | underdog | Chris Olave | Receiving Yards | under | 0.09207479159828746 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|873ed1e2-f539-4bd9-9f44-3c49ea44fe7d | underdog | Alessio Milivojevic | Pass Yards | under | 0.09170993588038479 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|f4b1d058-417d-45ae-a386-97ecc96781e2 | underdog | Trey'Dez Green | Receptions | under | 0.09095912725310384 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|7aa6308c-d5e6-4a77-a069-483e31e47c22 | underdog | Willie Rodriguez | Receptions | under | 0.09080568724128812 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|cde77409-6c4b-4d8e-9073-074e686e1b6d | underdog | Cam Little | Kicking Points | under | 0.09049138686982805 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|81e4effc-b4be-4a9c-8d85-1a319d170d18 | underdog | Carson Hilbert | FG Made | under | 0.09042966404950137 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| prizepicks|16834826 | prizepicks | DK Metcalf | Rec Yards | under | 0.09020306892719043 | 2026-11-10T12:33:48Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16941175 | prizepicks | Elijah Higgins | Rec Targets | under | 0.09009803240688008 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16942047 | prizepicks | Deebo Samuel Sr. | Rec Targets | under | 0.08983159220469517 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f62cef0d-51f0-4d95-8e29-efa118a3c0be | underdog | Jaron-Keawe Sagapolutele | Pass TDs | over | 0.0892547976787258 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|f16d8234-6143-4268-97ff-fc3289037ce3 | underdog | J'Koby Williams | Rush Yards | under | 0.08921620416726928 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| prizepicks|16894974 | prizepicks | Ashton Daniels | Rush Atts | under | 0.08812597680513468 | 2026-11-12T07:07:56Z | 2026-11-13T19:00:00.000-05:00 |
| prizepicks|16897183 | prizepicks | Caleb Hawkins | Rush Atts | under | 0.08801035811918012 | 2026-11-13T12:14:20Z | 2026-11-14T21:30:00.000-05:00 |
| underdog|f9fc5b80-57fb-4d48-b0d6-01920f66516f | underdog | Rece Verhoff | FG Made | under | 0.08797576918997374 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|9ea2bc5d-65cf-4749-b4f2-ef74fea29512 | underdog | Arch Manning | Pass Yards | under | 0.0878083317921382 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|7b9cbde9-983a-4d99-84fd-1e3dd0ea2c7f | underdog | Tre Tucker | Receiving Yards | over | 0.0875329970402473 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|0c761c58-be15-416b-b703-6a586bf39be5 | underdog | Kenny Johnson | Receptions | under | 0.08742722952237947 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16942042 | prizepicks | Germie Bernard | Rec Targets | under | 0.08682541820520961 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863709 | prizepicks | Germie Bernard | Rec Targets | under | 0.0868140274679029 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|568c3de8-7943-4733-a62e-0ad545ed654c | underdog | Emmett Johnson | Receptions | under | 0.0867952807296627 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16834650 | prizepicks | Derrick Henry | Rush Yards | under | 0.08663217446763538 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|0bfc6753-5f10-4e6f-9e3c-1785134a300d | underdog | Hank Brown | Pass TDs | under | 0.08611303327074238 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|828da51d-e687-4454-826f-bb1788d4eaeb | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.08597941891790728 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|ae43e221-f14b-42bc-9be5-744ae382cc89 | underdog | KJ Jackson | Pass Yards | under | 0.08594895049633855 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|7271a380-a961-4101-afbb-6871fdf84491 | underdog | Hunter Henry | Receiving Yards | under | 0.08579727034280116 | 2026-11-13T01:09:17Z | 2026-11-15T14:30:00Z |
| underdog|a0f28536-1ea4-460f-8056-53d93cf15ad8 | underdog | Dani Dennis-Sutton | Sacks | over | 0.08579135002694815 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|61e1b16e-fc64-4a20-aaf7-c86a2ed3ba0c | underdog | Travis Kelce | Receiving Yards | under | 0.08538377569690225 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|b31f3fa0-6f4a-45f4-949e-38b59a516e08 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.08529394052891348 | 2026-11-12T07:07:56Z | 2026-11-15T21:25:00Z |
| underdog|0791176b-ca45-4db5-adce-5e0033f90282 | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.08517285225941984 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|0149f1ed-8d01-4fb3-8c29-ee43cba33fce | underdog | Kaleb Johnson | Rush Yards | under | 0.08513771358831856 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16941181 | prizepicks | Jahan Dotson | Rec Targets | under | 0.08499685770574694 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|fe742815-78d4-49a8-89d4-b09df9d494f8 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.08495752665294976 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|2e347a2b-8cd6-4dee-b05e-a080b7eb5f86 | underdog | Elija Lofton | Receiving Yards | under | 0.08489231076511361 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|2241dc3b-3cce-4713-948a-899c19938a90 | underdog | Bhayshul Tuten | Receptions | under | 0.08488347843269772 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ab688298-7ac6-4998-bad8-ed8a0d01a1f4 | underdog | Konata Mumpfield | Receptions | under | 0.0847625992849359 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|16a163f8-37a8-4814-9673-e9079fc7d360 | underdog | Khalil Shakir | Receiving Yards | under | 0.08458463166509522 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|a9e7114f-4108-43da-97c7-bbe34afcbd6a | underdog | George MacIntyre | Pass Yards | under | 0.08432128549331452 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|095d7662-7876-4544-a661-85a9352bc8b9 | underdog | Darnell Washington | Receptions | under | 0.08429478520005662 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b59cb19d-8acc-407f-8dca-326a375b33eb | underdog | Tory Horton | Receiving Yards | over | 0.08418990069868826 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|6a800e8e-f81b-4bdb-9cee-fc7e90da63ae | underdog | Chuba Hubbard | Receptions | under | 0.08408782592218833 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|37738fae-4753-4e52-b227-99303a546958 | underdog | Caleb Hawkins | Rush Yards | under | 0.0840529047691323 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|2d6f2c26-3679-4462-b5f9-154fdf837d9a | underdog | Malik Washington | Receptions | under | 0.08380896020559803 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e4971822-0afb-4f50-93e5-4d1c7bd2e60c | underdog | Brian Thomas | Receptions | under | 0.08369582901305839 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|5978a0c4-b089-4243-93ce-fed7ae99460e | underdog | Kenny Johnson | Receiving Yards | under | 0.08365563340133153 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|7f654e7f-ce6f-4514-b607-3b45826bc886 | underdog | Carnell Tate | Receptions | under | 0.08352541400712155 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|30b534aa-3c8d-4e2a-8532-7046212f8423 | underdog | Keon Coleman | Receptions | over | 0.08351427326810018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fa89e139-2ff7-4471-9a99-3cff435d0b81 | underdog | Michael Mayer | Receiving Yards | over | 0.083113027814818 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|6d5c6e7a-9c71-4fd6-a60a-58523488f46f | underdog | Davis Warren | Pass Yards | under | 0.08292817370928895 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|0a225afc-fca1-4959-82b0-c5702e9643ba | underdog | KC Concepcion | Receiving Yards | under | 0.08273359636168665 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|11c5edd2-7864-4477-af58-f500b2c8be84 | underdog | Jeremiah Smith | Receptions | under | 0.08241258763340897 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16942017 | prizepicks | Konata Mumpfield | Rec Targets | under | 0.08195824652932926 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|68c8554e-294b-4278-b7e6-a04547b16b80 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.08188544698110789 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1c822beb-341f-4ef6-91e5-340df5d45d2e | underdog | Quinshon Judkins | Rush Yards | under | 0.08150218705697565 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|b4b14665-4501-496c-8be0-d530e6e1fbe5 | underdog | CeeDee Lamb | Receptions | under | 0.08142420706840037 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|3a2140cc-34ac-432c-a338-20fc5d386a93 | underdog | Anthony Colandrea | Pass TDs | under | 0.0812395078517486 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| prizepicks|16942053 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.08114388361716462 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|879eaed1-2f48-4ebf-82ba-fffcc451343a | underdog | Pat Freiermuth | Receptions | under | 0.08099921416069444 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0948aa96-7ab1-4a01-8009-90f637fe281c | underdog | Walker Eget | Pass TDs | under | 0.08075629229645986 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|2c6a1766-9888-43db-8463-79a5e3158ac9 | underdog | Foster Moreau | Receiving Yards | over | 0.08074063361249817 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16834642 | prizepicks | Jonathan Taylor | Rush Yards | under | 0.08067797097966689 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c4e5cef0-a68c-4f30-8bf1-e0db1f36c83b | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08046760762807637 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|23238e4a-a453-48b3-888b-37d8d5c24a0e | underdog | Caleb Douglas | Receiving Yards | under | 0.08033066710225367 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|664d4cb2-7e0b-47ca-9e51-872e5972e87b | underdog | Makhi Hughes | Rush Yards | under | 0.0802482036438541 | 2026-11-13T01:09:17Z | 2026-11-14T03:15:00Z |
| underdog|67d69720-f75a-4a58-8666-e3e822ae68f8 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.08006957549511673 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|5e94977c-0093-48e8-becf-5e8910977a9b | underdog | Drake Maye | Rush Yards | under | 0.08004423976338015 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|6751175c-ff62-4777-924f-e7d17832e931 | underdog | Aiden Flora | Receiving Yards | over | 0.07986935749827329 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|950859b7-8ce4-4a6c-be8f-ece3e3fcdac6 | underdog | Seth McGowan | Rush Yards | under | 0.07978214294232122 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|0b2e9d13-d865-4ce4-8130-1811f8c75f1f | underdog | Jahmyr Gibbs | Receptions | under | 0.07974674760702072 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|28b73f9a-7464-4028-9994-b3e9777c631e | underdog | Juwan Johnson | Receptions | under | 0.07927138801736044 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2063a4a7-dfda-48db-b7cf-8db794e23b5a | underdog | Jaleel Skinner | Receptions | over | 0.07909948837131958 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|aec9f942-d44c-43ee-8847-b10728935f0d | underdog | Omarion Hampton | Receptions | over | 0.0790537300117724 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|fcf60ef4-6d8a-4e5f-a5dc-ab09c139b1d7 | underdog | Olamide Zaccheaus | Receptions | under | 0.07875857917335316 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|8450e859-24f2-4721-9b6d-6aceb59b963a | underdog | Aaron Rodgers | Pass TDs | under | 0.07874658502524756 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|3637def0-7f94-4c1d-b113-e64172610ae4 | underdog | CJ Bailey | Pass Yards | under | 0.07868912571857178 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|e783dc26-5825-408b-ba88-074ae8338f79 | underdog | Tyler Allgeier | Receptions | under | 0.07858479788991879 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16942030 | prizepicks | Chris Olave | Rec Targets | under | 0.07835608420773721 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7802a2ce-f30a-457a-9eee-18da61262d1f | underdog | Fluff Bothwell | Rush Yards | under | 0.07802002745995362 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|238f90cc-3081-4edd-a3bb-d45650cbeb1c | underdog | Jamal Rule | Rush Yards | under | 0.07795938913876044 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|0c094349-7670-4e83-b31d-4b938a956227 | underdog | Towns McGough | XP Made | over | 0.07790025829990821 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|29f1ac2f-dcda-413a-af6c-9b468030f898 | underdog | Jared Curtis | Pass Yards | under | 0.07780032366697098 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| underdog|cdc2071a-3842-44a4-9f0d-c3706f5c9309 | underdog | Bijan Robinson | Rush Yards | under | 0.07770038799830425 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16906374 | prizepicks | Ryan Hopkins | Pass Comp | under | 0.07753883763235836 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|62b67815-d048-466d-95d3-0363eaf266c5 | underdog | Nico Brown | Receiving Yards | under | 0.07745968323050245 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|bfc0ed1c-ae95-4fdb-935b-67f2feedf364 | underdog | Sedrick Alexander | Receiving Yards | over | 0.07739760435885867 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| underdog|b6f11e09-9689-4381-b880-65db73f14005 | underdog | Omarion Hampton | Receiving Yards | over | 0.07729965562532948 | 2026-11-13T12:14:20Z | 2026-11-17T01:15:00Z |
| underdog|e7f1bbea-2d7b-4c56-8e47-9e0b571c984f | underdog | Will Bettridge | FG Made | over | 0.07725741826529164 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|943b6125-955d-4c4e-a9cb-d4c65e6b426a | underdog | Aaron Rodgers | Rush Yards | over | 0.07712631679230819 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b25fcb52-8786-406a-858d-52e7672af5fc | underdog | Antonio Chadha | FG Made | over | 0.07704066761603501 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|18e1b2b8-d6db-474b-bbfb-ab7200988bd2 | underdog | LaNorris Sellers | Pass Yards | under | 0.07690782897298154 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|b60a1138-01f1-4292-b874-5acaf191af21 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.0767893063215298 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|058b0488-9d5f-43ce-ae6a-dde3d1e4de82 | underdog | Nate Frazier | Rush Yards | under | 0.07674922775801507 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|2f3c01e8-56f2-4972-80d6-96a7c641e276 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.07651862763115314 | 2026-11-11T16:13:16Z | 2026-11-15T14:30:00Z |
| underdog|693f5fff-95ff-4e29-b913-be01aef304c7 | underdog | Savion Williams | Receiving Yards | under | 0.0763692412291278 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9afc918c-33f0-4d49-94c8-ae1c1087877a | underdog | London Humphreys | Receiving Yards | over | 0.07632980997810002 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|93f57aed-6f22-4917-bbcd-a64859bd454f | underdog | KC Concepcion | Receptions | under | 0.07613263220312116 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|921893b1-e130-4cc1-9e68-fae07083d8d6 | underdog | Tee Higgins | Receiving Yards | under | 0.07552956056808402 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|81ff0621-4501-4f89-a90c-53b654828353 | underdog | Tucker Kraft | Receptions | under | 0.07531614878084558 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|8754f62d-b007-4c8d-9bfd-32eda659a14a | underdog | Trae'shawn Brown | Rush Yards | under | 0.07531611655518433 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| underdog|5e509b77-232b-42d0-9461-5701bd8ae7a0 | underdog | Samaje Perine | Receiving Yards | over | 0.07517445268493195 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|4dfa0157-e1a7-41c5-98a2-53df06995587 | underdog | Brendan Baird | FG Made | under | 0.07501720483065888 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|0c1b8205-16c9-4bba-b677-32477bbf7cc6 | underdog | Aaron Jones | Receptions | under | 0.07498021252064768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|1453952e-59e2-4974-8658-e2590a469b1a | underdog | Terrance Carter | Receiving Yards | under | 0.0749423255246151 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|7a3c0c30-9e3a-4121-8183-82b5691e17c4 | underdog | Josh Downs | Receiving Yards | over | 0.07467962997722255 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16941206 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.07461924310815837 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|904b626c-0df7-4bcd-8080-cd2438332c7d | underdog | Deshaun Watson | Rush Yards | under | 0.0743514519962496 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16941211 | prizepicks | Christian Watson | Rec Targets | under | 0.07423664668190944 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|1d790904-3e3a-490f-9135-fab5363ea396 | underdog | Chas Nimrod | Receiving Yards | under | 0.07407940070248409 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|7eda251b-5bb5-4672-b317-2b57fa7740b9 | underdog | Jadon Porter | Receiving Yards | over | 0.07400421754769337 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| prizepicks|16941196 | prizepicks | Khalil Shakir | Rec Targets | under | 0.0734283027956808 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|80d5b669-4608-4a70-af3d-0ca04f2a9ce7 | underdog | Braylon Staley | Receptions | under | 0.07334461051353225 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|68ba7c9c-dafb-4579-93dc-ee5dd8c6e55e | underdog | Jamal Polite | Receptions | under | 0.07329683820316635 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|1401b805-b55d-4f62-9585-45359cf41b66 | underdog | Patrick Mahomes | Pass TDs | under | 0.07319579691346556 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|7fddc7b2-9d72-4ff1-b1b0-9b0333b60dbd | underdog | Gunnar Helm | Receptions | under | 0.07318955792213211 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|15895332-a1f7-4ca9-9f82-51abcab141d4 | underdog | Seth McGowan | Receiving Yards | under | 0.07317673931460811 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|06ae6764-4717-4fd0-90d4-cba7d420c077 | underdog | Sam Leavitt | Pass TDs | over | 0.07311759928344974 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|228e3396-f2f2-4d99-afc3-05ad8927a249 | underdog | Keelon Russell | Pass TDs | under | 0.07311368179295119 | 2026-11-12T07:07:56Z | 2026-11-14T17:45:00Z |
| underdog|5aa07c5c-3160-4bf9-bae2-17272d017de0 | underdog | Tetairoa McMillan | Receptions | under | 0.07291530262227885 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|4d9ccd47-5062-4cf9-93f8-ea2dd19fa6d2 | underdog | Kayshon Boutte | Receiving Yards | over | 0.07290969522574386 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f65d31f8-6cb0-46ef-973a-612d369e3cc2 | underdog | Lukas Van Ness | Sacks | over | 0.0725672770341067 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|afe168bf-abfa-4e5a-9c00-b1163353af0c | underdog | JC French | Pass TDs | over | 0.07241472236418672 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|a0cd60d1-929a-4503-848a-8b24dad869a7 | underdog | Dylan Raiola | Pass Yards | under | 0.07204706439513853 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|707d8339-a7f0-468c-a5f3-2b025bfa73d7 | underdog | Mateen Bhaghani | XP Made | over | 0.07183282096813365 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|858c7d02-f1ef-43e2-ac44-a0e9447d8e99 | underdog | Tommy Tremble | Receptions | under | 0.07126105154425799 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d4d98b9c-0bbb-480c-841a-373f26ae1956 | underdog | Jalen Coker | Receiving Yards | under | 0.07123604540034678 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|c25edc7c-0902-46d8-922f-add8b4542118 | underdog | Ethan Grunkemeyer | Pass TDs | under | 0.07113280126479149 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|ce0fce9b-aa9c-4627-95f3-7606f345a845 | underdog | Braelon Allen | Receiving Yards | over | 0.07107039823732642 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| prizepicks|16941213 | prizepicks | Tucker Kraft | Rec Targets | under | 0.07104685444251368 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7a75e646-5664-41bf-83d2-fea36aea9458 | underdog | AJ Barner | Receiving Yards | under | 0.07075613788298196 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|23aff467-3c88-4829-ad32-2dc97e30d278 | underdog | Germie Bernard | Receptions | under | 0.07070199720871251 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| prizepicks|16863705 | prizepicks | Jameson Williams | Rec Targets | under | 0.07067193012939765 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|96b084f0-e61e-4d6f-bbda-ee645d2f7d65 | underdog | Jason Myers | Kicking Points | under | 0.07035458570297104 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|32afa744-a7db-46b1-8166-59407c4e4dd5 | underdog | Nico Collins | Receptions | under | 0.06991731066614237 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8dc776e9-341d-424e-97a4-cb1076f15650 | underdog | Darren Waller | Receptions | under | 0.06987874258747295 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3a0a1923-9d00-45fe-b0ce-7f76d9913a34 | underdog | Darian Mensah | Rush Yards | over | 0.06986848826057779 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|10729dc7-2bc5-45f6-b6a1-f2e8ec1605d7 | underdog | Conner Weigman | Pass Yards | under | 0.06985803494675158 | 2026-11-11T22:47:13Z | 2026-11-14T03:15:00Z |
| prizepicks|16942027 | prizepicks | Jordan Addison | Rec Targets | under | 0.06983799794181811 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|ac4d8a30-9225-43c8-88e7-08dcda48c633 | underdog | Nick Marsh | Receptions | under | 0.06969050600733206 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| prizepicks|16941225 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.06952431849126628 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|9fb692ca-1ded-474d-ace1-e954d47e3038 | underdog | Isaac TeSlaa | Receptions | under | 0.06945554268955467 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|edd8f0e4-7008-474c-8413-041ca06749b0 | underdog | Drew Sample | Receptions | over | 0.0693941433699456 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b0a672c0-cb8f-42ef-a549-777c38acf50e | underdog | Dylan Edwards | Rush Yards | under | 0.06929821317703688 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| prizepicks|16942026 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.06927754626167526 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|44222ca6-7319-4558-9011-4baebd4dae89 | underdog | Chris Olave | Receptions | under | 0.06860046597796887 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ab5a705a-6a78-49b7-bcfd-7321ae88e69f | underdog | Kaelon Black | Receptions | under | 0.0685332352021717 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|8aa2ecd1-22be-421d-828e-4d205fe6b04f | underdog | Micahi Danzy | Receiving Yards | under | 0.06844881191786067 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| underdog|2f9b9eb9-ccb3-4449-9821-4dee9cb0e528 | underdog | Nate Boerkircher | Receiving Yards | over | 0.06839844091264013 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16863716 | prizepicks | Tee Higgins | Rec Targets | under | 0.06814305302582702 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|cc687153-6c15-4213-8e26-4c90c7def680 | underdog | Jonathan Taylor | Receiving Yards | under | 0.06802934736360589 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|0a2dcbf7-b7e8-4d71-8034-a024ef71e687 | underdog | Tate Sandell | XP Made | under | 0.06802582102225152 | 2026-11-11T06:09:33Z | 2026-11-14T21:15:00Z |
| underdog|b7573824-7d88-45cc-8bc1-9e98836c986d | underdog | Bijan Robinson | Receiving Yards | under | 0.06782521035230094 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|45ec7f88-0699-40a2-87dd-29c280d1e781 | underdog | Kenneth Walker III | Rush Yards | under | 0.0676084025258199 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|66e7d6f6-050e-472a-bf34-2e00c796f56d | underdog | Aiden Flora | Rush Yards | under | 0.06744265191423993 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|67bb66e0-36f8-4bfb-b364-8db821ce624f | underdog | Daylyn Upshaw | Receiving Yards | under | 0.0674153490159497 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|7627dd31-dcb0-4356-b6c1-21656c34392a | underdog | Ashton Daniels | Pass TDs | over | 0.06711574287975197 | 2026-11-12T07:07:56Z | 2026-11-14T00:00:00Z |
| underdog|34a7f042-c797-4140-87c0-9d13fe4ac49a | underdog | Eric Singleton | Receptions | over | 0.06683429911141725 | 2026-11-13T01:09:17Z | 2026-11-14T23:15:00Z |
| underdog|500509cc-70ed-419e-b01b-6be54d934764 | underdog | Amari Thomas | Rush Yards | under | 0.06674668340859635 | 2026-11-11T16:13:16Z | 2026-11-14T00:00:00Z |
| underdog|28a6f2e6-c201-4e00-9b8a-71e36e17333b | underdog | Devon Dampier | Pass TDs | over | 0.06672449840713934 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|75d6f3fa-7734-49c4-9e25-90076e135660 | underdog | Darian Mensah | Pass Yards | under | 0.06666845712800784 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|11524372-bbae-47eb-abc7-77f03ee31c7a | underdog | Dawson Knox | Receptions | under | 0.06664316355524857 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e3895608-8c85-4816-aad0-fe8098f92933 | underdog | Dawson Knox | Receiving Yards | under | 0.06643222901337464 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|5e7c97c3-ca82-4a5d-a44a-72514ce16b3c | underdog | Isaac Wilson | Pass Yards | under | 0.06630442318418894 | 2026-11-13T01:09:17Z | 2026-11-14T03:15:00Z |
| underdog|88469ae0-7923-439e-8ecd-83506eac545d | underdog | Charlie Becker | Receptions | under | 0.06609322679226748 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|97733708-ed62-42d6-891a-4827e8fe144e | underdog | Noah Gray | Receiving Yards | over | 0.06572912691694155 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f5596fdf-42d3-4466-abd8-87dc98e9fbc2 | underdog | Dylan Sampson | Rush Yards | under | 0.06544891409344189 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|7d812101-a26c-4f16-8061-0ac18951a7e6 | underdog | Kenny Darby | Receptions | under | 0.06543754998000173 | 2026-11-13T12:14:20Z | 2026-11-14T23:15:00Z |
| prizepicks|16834811 | prizepicks | Jalen Coker | Rec Yards | under | 0.0652772475778256 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|74c0873e-371f-437e-9de3-77eacadb9d01 | underdog | Tony Livingston | Receiving Yards | over | 0.06517859139566806 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|d4150a17-b459-4876-b557-7ba5873c9026 | underdog | Barryn Sorrell | Sacks | over | 0.06498589556022877 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|8a5a2942-cbf3-4389-befa-f6325f90a1a2 | underdog | Tyler Warren | Receptions | under | 0.06494609926234585 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|27ba9d6a-0872-4d4b-80e2-4bcf6e38f2fa | underdog | Beau Pribula | Pass Yards | under | 0.06463501056828735 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|e2e1f58e-7c18-479a-b4ce-0f2e20dd3d06 | underdog | Keshaun Singleton | Receiving Yards | under | 0.0646132151416744 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|b6c8147c-61d0-4fb3-86b0-a7a192137d3f | underdog | Marcel Reed | Pass Yards | under | 0.06440771322136041 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|9a532a02-b59d-4cec-ba94-d1a9bda101ab | underdog | Lincoln Kienholz | Pass Yards | under | 0.0643521527053672 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|aa25f9a8-4bd8-47a2-a186-2b8195262abf | underdog | Tristen Brown | Receiving Yards | over | 0.0643019368295239 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| prizepicks|16942039 | prizepicks | Breece Hall | Rec Targets | under | 0.06414825334372365 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|067410a9-e4e9-468e-ac1c-c09828fb5b19 | underdog | Matthew Golden | Receiving Yards | under | 0.06410870794329593 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3b3d0c4f-70c5-41e6-8a4b-b405eb8d0143 | underdog | Alonza Barnett | Rush Yards | under | 0.06407750546115587 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| prizepicks|16941201 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.064016928569531 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4371c896-a43e-4bf0-8a98-208692654d46 | underdog | Jeremiah Cobb | Rush Yards | under | 0.06390755034298268 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|2ef3cdfc-603a-4a90-8dd1-c78a10783d71 | underdog | Greg Dulcich | Receptions | under | 0.06371545917699406 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16942035 | prizepicks | Garrett Wilson | Rec Targets | under | 0.06335703964183648 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c489387a-fbec-48c8-ba91-c6a7f48a4d0a | underdog | Tyler Shough | Pass TDs | under | 0.06300540300276691 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7f0d6a2b-7b34-4d47-984e-08b8cfd1a9f2 | underdog | Tory Horton | Receptions | under | 0.06292579500923501 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|10a3c810-4d63-4b32-8043-7bd1c8a89bb3 | underdog | Kevin Jennings | Pass Yards | under | 0.06270576499724212 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|09467e0e-3d0e-486b-89a5-e6f753153d08 | underdog | Nicco Marchiol | Pass Yards | under | 0.06254896998290815 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16942052 | prizepicks | Zach Charbonnet | Rec Targets | under | 0.06241369652539952 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|707423ed-e4de-44d4-8f0a-f41859c3dcbb | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.06222463039349091 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16870372 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.06214267328538181 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|ad790425-afe4-45bf-a342-c54d290c7cad | underdog | Ty Dieffenbach | Pass Yards | under | 0.062121002170596906 | 2026-11-13T01:09:17Z | 2026-11-14T02:00:00Z |
| underdog|4cecc174-35d7-4651-9676-27d5756251d2 | underdog | Javonte Williams | Rush Yards | under | 0.06196379751073866 | 2026-11-12T07:07:56Z | 2026-11-15T21:25:00Z |
| underdog|74035606-4682-41d0-8085-255b16e43f27 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.06181328099453465 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16942020 | prizepicks | Tyler Higbee | Rec Targets | under | 0.06174816194012789 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|76a68710-9ef5-42b0-86d7-66fcc5b58d9c | underdog | Tre Tucker | Receptions | over | 0.06172070169914223 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|7f662455-94a7-4b44-98d9-3a1141a6e561 | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.06160934850898092 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| prizepicks|16941188 | prizepicks | Ja'Kobi Lane | Rec Targets | under | 0.06156634147713902 | 2026-11-13T12:14:20Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|9c30f32f-0641-45c9-98cd-31914710134a | underdog | Conner Weigman | Pass TDs | under | 0.06146923964179296 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|25507ed7-e0b7-476c-822f-cfdb87ed4361 | underdog | Denzel Boston | Receiving Yards | under | 0.06096609640716899 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|6e0dcb16-0162-4770-816d-09f39e78c848 | underdog | Bo Jackson | Receiving Yards | over | 0.060886535252514085 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16941212 | prizepicks | Matthew Golden | Rec Targets | under | 0.06085890822970175 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|dacd015b-859e-4b90-abc2-437f8cc02b93 | underdog | Cameron Dicker | FG Made | under | 0.060825633187946426 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|eb4e770e-7d6c-4302-9ca3-5b8ab646e8e3 | underdog | Tate Sandell | FG Made | over | 0.06064011194939378 | 2026-11-11T06:09:33Z | 2026-11-14T21:15:00Z |
| underdog|2ca12ee0-e6d2-41c8-b151-acf00be8c9a3 | underdog | Noah Bennee | Receiving Yards | over | 0.0605452926650496 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|b3423be4-c1c8-4eca-b84d-eda9c307336d | underdog | Kenny Darby | Receiving Yards | under | 0.06042170971127514 | 2026-11-13T12:14:20Z | 2026-11-14T23:15:00Z |
| underdog|15dacbb1-1137-4ecd-813a-83e3d65404ec | underdog | Chase Brown | Receiving Yards | under | 0.06031556029363805 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|d2aca639-0fcc-421f-bff6-1dc28f8b4fa4 | underdog | Dalton Kincaid | Receptions | under | 0.060234650924518074 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|37316135-e25d-4cd5-9c1a-c8f0b3d12a7a | underdog | Wayne Knight | Rush Yards | under | 0.05996784711098602 | 2026-11-13T12:14:20Z | 2026-11-14T02:00:00Z |
| underdog|11b4b2af-a1af-4863-a1d3-2077193d67fe | underdog | Drake Maye | Pass TDs | under | 0.05982086422742261 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|8ae06971-abf9-4235-88c3-08c0d0340567 | underdog | Tony Pollard | Receiving Yards | under | 0.059755840017869266 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|78748d91-4060-44ca-959a-a5962e13a530 | underdog | Brandon Aubrey | Kicking Points | under | 0.059463924496844345 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| prizepicks|16940098 | prizepicks | Stole Dimitrievski | Goalie Saves | under | 0.05929017831064565 | 2026-11-13T12:14:20Z | 2026-11-13T14:45:00.000-05:00 |
| underdog|bf6d8568-1c2e-4352-aa80-f22b9a01d700 | underdog | Elijah Higgins | Receptions | under | 0.05927277420068855 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|24457ce7-a29e-4e65-aaab-d2f2d38d5a63 | underdog | Mark Andrews | Receptions | over | 0.05909484948085142 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|09922b6e-e917-4c32-8e83-1664e7f4b1e8 | underdog | Carson Hansen | Rush Yards | under | 0.05888276472852805 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|72cc3a7c-7e0b-41c4-92b2-892a717cec25 | underdog | Antonio Chadha | XP Made | over | 0.0587925060107784 | 2026-11-13T12:14:20Z | 2026-11-14T00:00:00Z |
| underdog|4d0fcffd-ad43-47a6-82aa-6629600c756c | underdog | Drew Lock | Pass TDs | under | 0.058702533200966744 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|e6163bbc-03be-4b36-a81a-7b48da689608 | underdog | JC French | Rush Yards | over | 0.05867492863064305 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|f5777302-cf71-4ed0-a67e-fe6c6156946c | underdog | C.J. Stroud | Pass TDs | over | 0.058654369818583796 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|290e195d-8e34-4596-b14f-bf19adc896d6 | underdog | Kyle Juszczyk | Receptions | over | 0.05854227335361084 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|e85a0b19-b548-4442-98b0-3ecfd04f953c | underdog | Chris Boswell | Kicking Points | under | 0.05833293094762393 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0b91d70f-0d9f-42b6-a4c3-7dcfdcbc4892 | underdog | Mike Matthews | Receptions | under | 0.058284766086376116 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|888fa28c-e758-43a2-8045-d5e4ca7f7e60 | underdog | Junior Sherrill | Receiving Yards | under | 0.05824464639264759 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| prizepicks|16941232 | prizepicks | Travis Kelce | Rec Targets | under | 0.05818111390825431 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|96e2d673-829f-4b11-8bcf-36b6baf3b013 | underdog | Walker Lyons | Receiving Yards | under | 0.05808358415812187 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|d6f5cd67-0f2d-42ea-b7a3-d1c84a3dd9bf | underdog | Gavin Grover | Receiving Yards | over | 0.058013040558561046 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|3781f038-1e2d-4add-834e-b1c8ce30f9eb | underdog | Bryce Young | Pass TDs | under | 0.05761978630482656 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e61ebfb0-1043-4481-9421-83b62bbf6009 | underdog | Chad Ryland | Kicking Points | over | 0.05754776899208275 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|cfe9dc12-c7f7-46a2-a5b3-7062507b4b7a | underdog | Spencer Porath | XP Made | under | 0.05746279372126262 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|5e97417a-5e1a-46ec-a628-38d2ce6156ba | underdog | Spencer Shrader | FG Made | under | 0.05723488095356977 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d574c7ec-e37c-4a11-9707-70d6710cd050 | underdog | Jake Bates | Kicking Points | under | 0.057056345727721 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|6f045679-096a-4592-9eb6-f1c464dac753 | underdog | Noah Fant | Receptions | under | 0.057003581476649634 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|36b5231b-d5e6-4040-94cc-b2d96541bed8 | underdog | Dierre Hill | Receiving Yards | over | 0.056780139921930095 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|ad5e8781-bd90-4378-89a8-d05b327c7f69 | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.056683977237381056 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|c585e3a7-97f0-4d10-b50b-2bc1276b0661 | underdog | Lee Beebe | Rush Yards | under | 0.05666225880908082 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|1fcaea85-7de8-4228-8b8c-94bc768e0933 | underdog | Waymond Jordan | Rush Yards | over | 0.056657622533493046 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|5c0ed3ab-e47b-4f5c-9575-21e7f9446dfc | underdog | Bam Knight | Receiving Yards | over | 0.056580944292172086 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|450e6500-80eb-4a39-b11d-91501af45e2b | underdog | Gunner Stockton | Pass TDs | under | 0.05640008620207193 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|6baaf9ac-5c5a-4c60-a6f1-7c72d78c06a5 | underdog | Katin Houser | Pass Yards | under | 0.05637977765636992 | 2026-11-11T22:47:13Z | 2026-11-14T02:00:00Z |
| underdog|9db900b6-98c4-44c5-9401-d670160cd60b | underdog | Matthew Golden | Receptions | under | 0.05633066769825512 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ccd6f642-f3f5-4fc3-8498-72ce41161385 | underdog | Conner Weigman | Rush Yards | under | 0.05627406593607254 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|0400f1e3-d2ae-4ff4-8ac8-6cc9df35a44e | underdog | Caleb Hawkins | Receptions | under | 0.05602218902003142 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16834814 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.05595171947998501 | 2026-11-10T12:33:48Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|7fc13d80-5c19-4981-95c0-1c5a9a22a74b | underdog | Walker Lyons | Receptions | under | 0.055913215695103435 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|f080a415-e7c5-4b6a-bf89-f005fdf79946 | underdog | Matt Gay | FG Made | over | 0.05586119946761431 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|214cbd24-84bb-458e-b1f4-1bd3a2149b36 | underdog | Brenton Strange | Receiving Yards | under | 0.05577611188639431 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f0b24d0a-f51d-4ec6-8f8f-ac17d8e0d0eb | underdog | Jalen Nailor | Receptions | over | 0.05545990463319178 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|f2067b31-0d16-4656-91cd-454d91ca62bd | underdog | Brandon Aubrey | FG Made | under | 0.05538164462438755 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|f9982662-f335-40b3-9dff-dcf0a72383a9 | underdog | Deebo Samuel | Receptions | under | 0.05533870914257788 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| prizepicks|16905893 | prizepicks | Malik Washington | Rush Atts | under | 0.05523106423632507 | 2026-11-13T01:09:17Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|08944bde-db15-46d3-8aee-65d143957886 | underdog | Trey Smack | Kicking Points | under | 0.05510427899823733 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|f77cdfc4-0b84-4c82-9242-02cb0fd152f6 | underdog | Demond Williams | Pass TDs | over | 0.05502559503905735 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|f8b50df0-df15-4845-9173-0adba2cfe7e2 | underdog | Samaje Perine | Receptions | under | 0.05489044582304281 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|2fb6b68c-630e-4d2a-a229-4d0133bb4f00 | underdog | Creed Whittemore | Receiving Yards | over | 0.05483588486226332 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|3dd950b0-0c21-4346-85ae-f62f9682e66b | underdog | Damon Ferguson | Rush Yards | under | 0.05482425247734968 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| underdog|13fbd334-9803-480e-8228-8383196b05d7 | underdog | Charlie Becker | Receiving Yards | under | 0.054340862550077196 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|5a28b010-365f-4fb1-9087-b88df07ee519 | underdog | Sedrick Alexander | Receptions | under | 0.054244200164998424 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|f819253c-7926-489c-ab0f-6adad1524b1a | underdog | Jacory Barney | Receptions | over | 0.05408789706973449 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| prizepicks|16864051 | prizepicks | Charlie Woerner | Rec Yards | over | 0.05401463087599445 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|09e85dc1-6ddb-434e-a936-6fd8aed43b03 | underdog | Andre Szmyt | FG Made | under | 0.05378693771750487 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bf0328b9-baf9-4e7f-86c3-4243ed90ce42 | underdog | Dylan Raiola | Pass TDs | over | 0.053647536822512054 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|c9e94429-e49a-4d7a-87b6-ed6884b65e96 | underdog | Christian Watson | Receiving Yards | under | 0.053404311395892634 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|752fb99e-c305-4d7e-b195-0395288a569d | underdog | Kaelon Black | Rush Yards | under | 0.05338295577490937 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|522b5aab-5b20-463d-9161-d48a3646bcb4 | underdog | Raleek Brown | Rush Yards | under | 0.05337188176570529 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|5f5a3116-6c86-495f-b0cc-76ebd5261b14 | underdog | Justin Bowick | Receiving Yards | under | 0.053320411307768434 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|8eb77084-e310-4720-b87f-8f97bc2c8b8f | underdog | Jaden Craig | Pass Yards | under | 0.0532779357184594 | 2026-11-13T01:09:17Z | 2026-11-14T19:00:00Z |
| prizepicks|16864058 | prizepicks | Eric Saubert | Rec Yards | over | 0.05300845751715566 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16834798 | prizepicks | Drake London | Rec Yards | under | 0.05299181956525634 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16874417 | prizepicks | John Mateer | Rush Atts | under | 0.052868503995310734 | 2026-11-13T12:14:20Z | 2026-11-14T16:15:00.000-05:00 |
| underdog|115d1147-17ab-4f53-af6d-903795d66814 | underdog | Wayshawn Parker | Receiving Yards | over | 0.052795762377819244 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16942046 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.052792794428390244 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|2ce30bec-63fb-4dfe-8e38-4cd955159f2a | underdog | Kyren Williams | Receptions | under | 0.05275196940203419 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|90077d5d-1a1d-45eb-b5b7-2d1770fc7b48 | underdog | Braylon Staley | Receiving Yards | under | 0.05274413200052008 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|83bde468-8247-4b83-9b7b-8e66878a0b19 | underdog | Griffin Wilde | Receiving Yards | over | 0.05250436186658791 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|cfa3359c-93fb-4dec-8875-330c5bb338fe | underdog | Ty Dieffenbach | Pass TDs | over | 0.0524472047601649 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|4cec3df3-17bb-4b74-9a57-c52695175cfc | underdog | Brian Thomas | Receiving Yards | over | 0.05238716839913293 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|edfe393d-b4f8-44bf-aa7b-fa433fdd0917 | underdog | Byrum Brown | Rush Yards | under | 0.05238318347911897 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|ab0a73bf-b563-4104-bac9-ce4b1db81a5a | underdog | Jabree Coleman | Rush Yards | under | 0.052355878432298386 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|d0b995e5-4279-4478-bb85-2f6f33206ed2 | underdog | Benjamin Brahmer | Receptions | under | 0.052319357229314245 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|1a046fef-2ddc-4a9e-8ed1-2e90509c2587 | underdog | Tyler Bass | Kicking Points | under | 0.05211400342992334 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|b9b24f29-9b19-472a-92e3-17ff3637168b | underdog | Sam Leavitt | Pass Yards | under | 0.05206185419169984 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|f48fdb97-2987-4a39-9762-8108b030233c | underdog | Jerry Jeudy | Receptions | over | 0.0520295111392754 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16941230 | prizepicks | Parker Washington | Rec Targets | under | 0.052005431792165546 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|a4cdc3ef-e490-44f7-9d22-9688f41616da | underdog | Jackson Kleather | XP Made | over | 0.051919363673327945 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|c9f605a5-326f-46ac-9cc2-82f5e0345179 | underdog | Malik Knight | Receiving Yards | over | 0.051802082035021235 | 2026-11-13T01:09:17Z | 2026-11-14T00:00:00Z |
| underdog|a7a97f4c-9167-4ac1-bef4-b737a40b1ec3 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.05172891772094268 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|feaedf13-f1cb-4e76-92bf-d9d0f7f8348f | underdog | Darnell Washington | Receiving Yards | under | 0.051680680891570296 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|bc62aeed-6c5e-47c6-a33c-aa9b907f08c8 | underdog | Javon Tracy | Receptions | under | 0.05167370253794945 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|c81f7f2e-696e-4498-b8ca-7a5799d1ee5a | underdog | Matthew Stafford | Pass TDs | under | 0.05151171430881951 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|1cad5c50-a14c-4264-b134-2fea30d0ce4b | underdog | Michael Hawkins | Pass TDs | under | 0.05140454628829705 | 2026-11-11T22:47:13Z | 2026-11-14T22:30:00Z |
| underdog|2617048a-16d2-4090-93bd-da80e31dbd5d | underdog | Will Reichard | FG Made | under | 0.05137550778273203 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|7cb811fe-c69d-4856-ac57-f73eaad0a230 | underdog | Emmett Johnson | Receiving Yards | over | 0.051125680051020694 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|788eeafc-d70a-4674-9706-fb65ca231536 | underdog | Rocco Becht | Pass Yards | under | 0.0510690370048652 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|098448c6-792b-4aaf-8f02-ba09091cf1ab | underdog | Jacoby Brissett | Rush Yards | over | 0.05093240883796324 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|41d0472a-ee6d-4c60-89cd-d9f433caba37 | underdog | Matthew Stafford | Pass Attempts | under | 0.05081255657798445 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| prizepicks|16931252 | prizepicks | Laura Samson | Total Games | over | 0.05072214408901943 | 2026-11-13T01:09:17Z | 2026-11-13T10:00:00.000-05:00 |
| underdog|3ca28cbe-3045-437d-b482-074b9e547595 | underdog | Justice Hill | Receptions | under | 0.050695143750179694 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|95bb1f37-aede-4d17-9905-18286a2f0b06 | underdog | Justin Bowick | Receptions | under | 0.05059544511891889 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|cd33d2fb-e1dd-42a2-9cd9-ba5d87ad4c6b | underdog | Ryan Wingo | Receptions | under | 0.0505654551818322 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|11bfdf20-29ab-4c85-835f-e9d4d9ae6b72 | underdog | Cayden Lee | Receiving Yards | over | 0.050444543170382605 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| prizepicks|16941210 | prizepicks | Javonte Williams | Rec Targets | under | 0.050359638435533705 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|d16ad2c6-ad17-4db5-81a9-5669a9184744 | underdog | Marvin Harrison | Receiving Yards | under | 0.05018515195819906 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|4532362a-de26-4d7c-8925-848d6105a4b4 | underdog | Ollie Gordon | Receiving Yards | under | 0.05016806446484068 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1c5fd9b2-1999-4144-9085-bcd7a7150d91 | underdog | Rece Verhoff | XP Made | over | 0.05016435267545344 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|6f3992ec-ac05-417d-a59f-5320790a1d41 | underdog | Peyton Woodring | XP Made | over | 0.050105935886552544 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|42c2cfee-02ed-4f7f-a137-6dbae4ccca98 | underdog | Chris Marshall | Receiving Yards | under | 0.049777652835880315 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| prizepicks|16942043 | prizepicks | Jaylen Warren | Rec Targets | under | 0.04961774127753471 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863710 | prizepicks | Jaylen Warren | Rec Targets | under | 0.04958776690173983 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|b38d0fe8-eeff-48b0-b233-c1b9ed0a7e6b | underdog | Ja'Cory Thomas | Receptions | over | 0.04930579434434934 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|0e47b5e3-2f9a-43f5-b530-f47623ccfa9d | underdog | Drew Sample | Receiving Yards | over | 0.049239250011618774 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|951caecc-29fa-49d5-805b-bf8f0f9cc838 | underdog | Nicco Marchiol | Pass TDs | over | 0.04913819551733667 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16921156 | prizepicks | Brandon Tullis | Rush Atts | under | 0.049030937000035024 | 2026-11-13T01:09:17Z | 2026-11-14T16:15:00.000-05:00 |
| prizepicks|16898722 | prizepicks | CJ Baxter Jr. | Rush Atts | under | 0.04899163749296942 | 2026-11-12T07:07:56Z | 2026-11-14T18:15:00.000-05:00 |
| underdog|9023da88-45ca-48fc-8bec-4e8f73ece9ba | underdog | Xavier Hutchinson | Receiving Yards | under | 0.04896690384698854 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16834806 | prizepicks | Caleb Douglas | Rec Yards | under | 0.048911928496814694 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|005fa26e-3f90-4f37-b964-8614d3ab6b93 | underdog | Tony Pollard | Rush Yards | under | 0.04887990433142231 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|a866c628-b0be-4b1d-97ea-bb7cbe41078a | underdog | Elija Lofton | Receptions | under | 0.048515481309444164 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|9cd6e319-56d8-4146-8720-122e222c0af3 | underdog | Kimani Vidal | Receiving Yards | under | 0.04845077626655159 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|320e4928-163a-4eb4-baca-1fffe8cf4cf0 | underdog | Jamal Roberts | Rush Yards | over | 0.04837798218349576 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|95231ceb-e90a-420c-98e0-a38f678fbb41 | underdog | Joe Burrow | Pass TDs | over | 0.04830047288438544 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|6acbfb7a-1667-4143-82f8-d566e5c26ae3 | underdog | Brock Bowers | Receptions | under | 0.04826815873810608 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|9989e1b9-b4e8-419b-a6df-1817c05c39eb | underdog | Mark Andrews | Receiving Yards | under | 0.04815263125185609 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|62eb81c8-587e-4412-aa01-e88467fb3ba9 | underdog | Aidan Mizell | Receptions | over | 0.04807968139293489 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|7c39f112-919c-49a0-afa7-1531cb9e8151 | underdog | Dylan Sampson | Receptions | under | 0.04803084524216095 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8ae7a0e-0afb-41bd-98a8-4bfa74cfc4b7 | underdog | Kirk Cousins | Rush Yards | over | 0.04794648374314203 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|0e9a4487-87c8-4333-aeb3-599e0ba3e2d4 | underdog | Dylan Sampson | Receiving Yards | under | 0.047889791154614225 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|1def9b6e-8fea-42a1-9f7a-1846031c16cd | underdog | Tank Dell | Receiving Yards | under | 0.047762943478220854 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16941223 | prizepicks | Laquon Treadwell | Rec Targets | under | 0.04764715308963674 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5ddca326-fb5c-4be7-9264-555c0deffac8 | underdog | Wyatt Young | Receiving Yards | under | 0.047495342258227824 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|cbb27715-4c5c-4930-9405-886767da9aa0 | underdog | Spencer Porath | FG Made | under | 0.04726926706009371 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|0ea9a1f4-b2c7-49f5-ae0a-5fb13ab0b949 | underdog | Jake Bates | FG Made | under | 0.04711758110912212 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|7e0fb8d1-b423-43bb-a329-6ced7a02fad1 | underdog | Jonaz Walton | Rush Yards | under | 0.04709424505482318 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|fd31bc9e-cff4-44fb-ae49-6c536d56bce8 | underdog | Caleb Douglas | Receptions | under | 0.046873180612608145 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f388882e-bf96-4bf0-ab4f-c20217916353 | underdog | Harold Fannin | Receptions | under | 0.046638245325585026 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d4acec1c-8f8f-4897-8e60-b7c7b956d82d | underdog | James Cook | Receptions | under | 0.0465337444974383 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e18e2b81-f40d-4c81-9fee-a10203692c8b | underdog | Brett Eskildsen | Receiving Yards | over | 0.04644721882940239 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|64bae3d3-f674-4a45-807a-d51d2feb6d54 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.046435927839737046 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| prizepicks|16899263 | prizepicks | Chuba Hubbard | Rush TDs | under | 0.04625994985710902 | 2026-11-11T22:47:13Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6c90d765-2043-4abc-be89-2441e45fdbc2 | underdog | Josh Downs | Receptions | over | 0.04620180299105142 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|49dbe735-a6e1-435e-b05b-067376ee32f9 | underdog | Joey Slye | FG Made | under | 0.04617041472475325 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f5af09ce-6733-4b1b-9e56-a6de2b4cbcf4 | underdog | Rocco Becht | Pass TDs | over | 0.04606321132899205 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|0d7845b0-7f5f-4d31-91af-99fe5edf24ed | underdog | James Cook | Receiving Yards | over | 0.04596118738224697 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|593907c0-a952-4ce2-a792-fa5c25e0a816 | underdog | Marvin Harrison | Receptions | under | 0.04586912171191271 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|03c2a9b4-d39f-4076-b24e-67268d520050 | underdog | Omari Hayes | Receptions | under | 0.04582196406732275 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|c97e7a45-2914-4f89-a1d9-e4aefb0675fd | underdog | Max Gilbert | XP Made | over | 0.045560676594453065 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|38cc4909-3b70-4b1a-8795-eacdebdc7f63 | underdog | Isaiah Mozee | Rush Yards | under | 0.045527451956121956 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|a1b0629b-fd33-48ca-9b1e-625c9da78585 | underdog | Malik Washington | Pass TDs | under | 0.045388387951214026 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|56e8eb86-0cbf-469f-8c79-3ef93f017dea | underdog | Denzel Boston | Receptions | under | 0.045152048025238756 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ae810589-81e6-4ea2-8235-0aef0fd1070e | underdog | Joey Slye | Kicking Points | under | 0.04505178064548698 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|1d9a87ef-476e-42de-b171-52da98ca6e93 | underdog | Cameron Dicker | Kicking Points | under | 0.045033047920349456 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|99b4b3cd-d31a-44f2-b2e0-d467b194fa13 | underdog | Raleek Brown | Receptions | over | 0.04497461810941972 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|78c07d75-953d-4627-8898-e0a1e9304e2c | underdog | Makhilyn Young | Rush Yards | over | 0.044951919440831434 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|f0780ba2-8037-4cc2-a253-38e5dd6c1369 | underdog | Brendan Baird | XP Made | under | 0.04490246123339292 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|8aa26f4f-6c4a-4c9b-bbb8-477e19ee6923 | underdog | Griffin Wilde | Receptions | under | 0.04484180164367657 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| prizepicks|16941203 | prizepicks | Denzel Boston | Rec Targets | under | 0.044751666931493794 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16906356 | prizepicks | DeJuan Williams | Rush Atts | under | 0.04472446734389435 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|b89e1abe-f2d8-423e-8ba3-13c3ae2269dc | underdog | Chase Hendricks | Receiving Yards | under | 0.04454002770132093 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|2fd3b25f-aae4-417f-9d95-7162bc43f705 | underdog | Brian Rowe | Receiving Yards | over | 0.04452429303055938 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|09fb6589-e5be-4da1-8c03-7b3b6b342d57 | underdog | Jared Curtis | Rush Yards | over | 0.044487657953625304 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| underdog|1f7f7044-5b58-4a4d-9b16-261d3cdb43ec | underdog | Travis Kelce | Receptions | under | 0.04401834231992152 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2a667d99-c4ca-40b7-95cc-6ea4f971d830 | underdog | Jordan Mason | Receiving Yards | over | 0.043920136945038935 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6a359aa0-6068-4eb0-8c11-237d31a4d274 | underdog | Chuba Hubbard | Receiving Yards | under | 0.04371106231349298 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16942019 | prizepicks | Davis Allen | Rec Targets | under | 0.043658638267208616 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|e7e3d83f-5c49-4028-820f-7df3a05ac6d2 | underdog | Demond Williams | Pass Yards | under | 0.043586752516204696 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|d29a2cd3-5b1a-4d86-888e-80dcf04c666d | underdog | Tommy Tremble | Receiving Yards | over | 0.043567053228045105 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|cc162aca-2976-49a7-bbf7-edcbd50d88eb | underdog | Isaiah Marshall | Rush Yards | under | 0.04354884867712727 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|06aa0f5f-6f09-44bd-a64c-29b236608b45 | underdog | Scott Starzyk | FG Made | over | 0.043538923860573675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|3af42ed6-ba31-4421-b3db-8a1a5c702d31 | underdog | Noah Jennings | Receptions | over | 0.04309994548487195 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| prizepicks|16934565 | prizepicks | Taylor Fritz | Total Games | over | 0.04290846956186811 | 2026-11-13T12:14:20Z | 2026-11-13T11:00:00.000-05:00 |
| underdog|05d61698-c97c-4c5b-9d89-defe3d868ba6 | underdog | Kevin Jennings | Rush Yards | over | 0.042850054600276355 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|7329e355-2a86-45ec-82e8-9c94abd631d1 | underdog | Craig Dandridge | Receiving Yards | over | 0.04273914522921507 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|dd9ccb7a-bffb-4472-be26-448ceee6db64 | underdog | Keaton Mitchell | Receptions | under | 0.04260594560207376 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0d111317-5c99-4d56-b5f5-63bae031a649 | underdog | Deshaun Watson | Pass TDs | under | 0.04236385864477632 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b03c56fa-f1b4-4ed3-8f2c-6e053fa36930 | underdog | Justice Hill | Receiving Yards | under | 0.042334380979668684 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|741b63a8-a778-45dc-8a3c-618f25571627 | underdog | Harrison Butker | FG Made | under | 0.04233008949187933 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|aac8322b-1ee8-46b4-92bf-a2afefe76f97 | underdog | Braden Pegan | Receiving Yards | under | 0.04226457688012075 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16932981 | prizepicks | Bianca Andreescu | Total Games | over | 0.042047604343236844 | 2026-11-13T01:09:17Z | 2026-11-13T11:10:00.000-05:00 |
| underdog|95c05909-55d3-4c40-baa2-21c12deb1a59 | underdog | Justin Herbert | Rush Yards | under | 0.04188540886632808 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0ef8efe3-b6d5-4ed4-b722-1eeab13065a6 | underdog | Lincoln Kienholz | Pass TDs | under | 0.04176370900092663 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|96a329b5-38e7-4b8b-a27e-6589f2d3bc55 | underdog | CJ Baxter | Rush Yards | under | 0.04174879097274642 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|94cc4393-ed78-41f3-bde5-b30173c95a06 | underdog | J'Koby Williams | Receiving Yards | over | 0.041689854183781794 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|55cb13c1-ee46-47e8-b0ce-5d68bc2910db | underdog | Connor Calvert | XP Made | over | 0.04166023250717721 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|b96e5afb-b999-4933-8781-cd4c11d325c9 | underdog | Jack Bech | Receptions | under | 0.04163575481719084 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|42d3755e-92d9-474a-802d-e950a7184b31 | underdog | Jonathan Dimas | XP Made | under | 0.04162851872089324 | 2026-11-11T16:13:16Z | 2026-11-14T03:15:00Z |
| underdog|79e5a165-4bcb-4fa2-ba0d-6d6d063dcefa | underdog | Collin Dixon | Receiving Yards | under | 0.04153024391434135 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|2fa9e2b4-614d-4a17-9548-927d0f196189 | underdog | Derrick Henry | Receptions | under | 0.04138130744755619 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|b519b161-4417-4dbb-8e1c-64a49cbe1b03 | underdog | Jayden Maiava | Pass Yards | under | 0.04136793364471936 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|992f3e80-6aa2-4ce0-bca9-9bd0cba69874 | underdog | Ashton Jeanty | Receptions | under | 0.041325909181133325 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c84b896f-85cf-4660-b039-6206a109df86 | underdog | Harrison Butker | Kicking Points | under | 0.04132208878674781 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16941197 | prizepicks | Ty Johnson | Rec Targets | under | 0.040992064808991424 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6819d4f5-78f7-4d71-bcf0-4b996192def2 | underdog | Carson Bruhn | Receiving Yards | over | 0.040828624494910315 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| prizepicks|16941179 | prizepicks | Bijan Robinson | Rec Targets | under | 0.040803121509780604 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6c901193-65b8-4432-bdf1-ea670655b227 | underdog | Amare Thomas | Receiving Yards | under | 0.04060844427005095 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|63f35c03-cf3a-4a60-9e48-e6b9aee69d0c | underdog | Jordan Love | Pass TDs | under | 0.04051564232645721 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e5538a7e-bc11-4b87-8ff5-8b9b27f1d395 | underdog | Luke Reynolds | Receiving Yards | under | 0.040421230293381405 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|f3acd35c-51ac-4b98-81d7-5f632298e45c | underdog | Pierre Strong Jr. | Rush Yards | under | 0.040405873993211716 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|92b63877-4f72-4f8e-a611-63ae37339cc6 | underdog | Randy Pittman | Receiving Yards | over | 0.04030313051643297 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|1c3138ba-e932-4be6-bd5a-586926b125e7 | underdog | JC French | Pass Yards | under | 0.040254892901353534 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|3868c985-c2f4-42c2-b08d-83a91201a94b | underdog | Devin Duvernay | Receptions | under | 0.03988605673509471 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|38a660e4-afcb-4a9a-88da-cbc720d6058c | underdog | Blake Corum | Receiving Yards | over | 0.03956691390896483 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|e1b62a44-6489-415e-b6fb-d10b9253bfcf | underdog | Dilin Jones | Receiving Yards | over | 0.039459116156089324 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|2d8123a0-f708-4858-8cb8-b23ea13fb087 | underdog | Terrance Carter | Receptions | under | 0.03939426269801527 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|bb750385-cd4b-427e-99bb-aa1c719550b9 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.03931795414340944 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|07a0eb6c-d8d9-46bf-aac3-dfed58d52aa7 | underdog | Braelon Allen | Receptions | over | 0.039314624923994734 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d8b03841-950e-438e-b854-d18417ae6d47 | underdog | Bear Bachmeier | Rush Yards | under | 0.03919720056348952 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|6c560866-cf1c-44ab-9966-4b44e38e0a59 | underdog | Ashton Daniels | Pass Yards | under | 0.03911652285612899 | 2026-11-13T12:14:20Z | 2026-11-14T00:00:00Z |
| underdog|b84a5c5e-8fa6-4e58-aabd-2b3b66cf8875 | underdog | Khalil Herbert | Rush + Rec Yards | under | 0.038922242891002434 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|0106a59e-fd6f-4578-88fb-91e093b9efe4 | underdog | JJ Buchanan | Receiving Yards | over | 0.038881092754730284 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|aee66ab0-3674-4803-b10b-149664415874 | underdog | Benjamin Hall | Rush Yards | over | 0.038759772213096344 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|1595ffba-834e-4175-adbb-a3eeb0fb4aa9 | underdog | Jamal Polite | Receiving Yards | under | 0.03865774848185577 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|f02d9522-37a0-4485-909f-dc4967cad1b9 | underdog | KJ Jackson | Pass TDs | over | 0.038539211710092114 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|03361ce4-9586-4b1b-b660-d9a3da6d9a64 | underdog | Ethan Moczulski | XP Made | over | 0.03851062357902946 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|a8ce8a0d-b252-405b-97ec-d2c24fe29262 | underdog | Dalton Kincaid | Receiving Yards | under | 0.03848081974045625 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16941193 | prizepicks | DJ Moore | Rec Targets | under | 0.038224949027769295 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|531bbc2b-a0fc-421b-9794-9c94e078b465 | underdog | Jaden Craig | Pass TDs | under | 0.03810788009385202 | 2026-11-13T01:09:17Z | 2026-11-14T19:00:00Z |
| prizepicks|16942054 | prizepicks | Jadarian Price | Rec Targets | under | 0.03801035045808776 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|ae1c8874-c0a0-434d-a31d-809ff3d59e49 | underdog | Kenneth Walker III | Receiving Yards | under | 0.03781672498542721 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|a5a6d1c9-ded0-4642-a1f5-1ea9ec0675f8 | underdog | Aidan Mizell | Receiving Yards | over | 0.03779757086546476 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|388d3b79-b0a7-42d3-872a-d1e8c8f7f0d2 | underdog | Alonza Barnett | Pass TDs | under | 0.037747158672632786 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|eb0c88d6-d923-40ca-88bc-5a021ff1d132 | underdog | Khalil Herbert | Receptions | under | 0.03766464527669133 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|75ffc63c-3cc6-43ae-ba87-535a1aceff33 | underdog | John Metchie III | Receiving Yards | over | 0.03741480683775811 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|024cff8f-3c0b-41d3-b64f-ea8842dfe2e7 | underdog | Ashton Jeanty | Rush Yards | under | 0.03729288076056669 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|0f7dad73-375a-486a-860d-abe788d5ec97 | underdog | Lawayne McCoy | Receiving Yards | over | 0.03715294032923011 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| prizepicks|16941228 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.03714571278625545 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6c77a458-f11c-43b3-8941-1f4df51219c8 | underdog | Bam Knight | Receptions | over | 0.03712161464621744 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|fa9bddc8-e6d7-4bba-8ace-9ab2de5ab31e | underdog | Darren Waller | Receiving Yards | under | 0.037039947520251415 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|227bd3df-840a-46d1-83f7-70fc731d166a | underdog | Keon Coleman | Receiving Yards | under | 0.037012574051386804 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|0ef521b5-0ad2-4c7e-9e7c-dc67d6ecf2e3 | underdog | Jack Foley | Receiving Yards | over | 0.03698391328619555 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|55df2acd-8cfd-43ed-b969-86957bc28871 | underdog | Carlos Hernandez | Receiving Yards | under | 0.03697154863642449 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|d511305a-9523-4792-b762-5612b2c2f9bd | underdog | Kyler Kasper | Receiving Yards | under | 0.03692640538945968 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|4d82b7f0-d383-413f-97c1-7d74814849b1 | underdog | Geno Smith | Pass TDs | over | 0.03690270527418432 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|a98832ad-cc1c-4f28-9746-8d27fb8ec062 | underdog | Joe Burrow | Rush Yards | over | 0.03676432878965474 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|160f76fd-f374-4e88-b8cd-db6a5cad7742 | underdog | Ty Clark | Rush Yards | under | 0.03667004373890259 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|d5e53e5c-71f4-4086-99fb-69639e63e727 | underdog | Mateen Bhaghani | FG Made | over | 0.036598637318603355 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|e651acf4-4d9b-4e70-bf0a-715a88f6ef9b | underdog | Devaughn Vele | Receiving Yards | over | 0.03657711025657884 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|9cd574f3-89de-4e8a-9ceb-5e892f3875dc | underdog | Rashod Bateman | Receptions | over | 0.036295203210838234 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| prizepicks|16942041 | prizepicks | Darnell Washington | Rec Targets | under | 0.03624850473786778 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863708 | prizepicks | Darnell Washington | Rec Targets | under | 0.03622440116764336 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|0fbebad7-ef4b-4c1e-b622-c8921e501f7f | underdog | King Miller | Rush Yards | over | 0.036196766847854 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|584121f2-3498-45db-86d2-51230f6e6643 | underdog | Asaad Waseem | Receiving Yards | over | 0.036152712041357615 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|7e214067-4ba0-412c-845a-dce679ce43cc | underdog | Scott Starzyk | XP Made | over | 0.03604303058757463 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|3ad66695-0f4c-4c6a-97c6-7d98b2e40493 | underdog | Raleek Brown | Receiving Yards | over | 0.035838088505037335 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|33c569ea-e2cc-4587-bc5d-c61aea1dfe3a | underdog | Devaughn Vele | Receptions | over | 0.03560111354860207 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|ca192d14-582f-4fba-95e0-d881ceb4d344 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.03558440453192235 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16863713 | prizepicks | Chase Brown | Rec Targets | under | 0.03548427625308703 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|f9718fc2-efda-4a87-aef5-4567c95c0b12 | underdog | Elic Ayomanor | Receiving Yards | under | 0.03545112441580822 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|274f14ba-1d4b-469e-8cfb-8fcd873ebcb8 | underdog | Andre Szmyt | Kicking Points | under | 0.035194355906048136 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d3533652-67c2-4228-8da4-9887e1218937 | underdog | Noah Gray | Receptions | over | 0.03516926483455424 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e26f9cb4-89d5-4281-afff-4284cbf3b089 | underdog | Nate Sheppard | Receptions | over | 0.03510892119689096 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|ae363647-2d9e-4fd4-b548-fc834f69a4fd | underdog | Bijan Robinson | Receptions | under | 0.0351075871491785 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|15e7da85-b67a-45cf-aab7-f91b96bcec06 | underdog | Ryan Hopkins | Pass TDs | over | 0.03505060031602475 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|e9f2c10c-6978-4134-9666-1cdc9df3a448 | underdog | Will Reichard | Kicking Points | under | 0.03483187705738011 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|49e5e566-fec7-49d8-bb3b-24a3821ca1f7 | underdog | Andrew Rappleyea | Receptions | over | 0.03469525675099577 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|0d992edd-d005-49b6-bc13-742d0c606adb | underdog | Gunnar Helm | Receiving Yards | under | 0.03448784863389276 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0a57bc4e-1488-4cda-8a52-5cd7829cfc1c | underdog | Legend Glasker | Receptions | under | 0.034235584291332 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|8200630e-636a-4386-88ce-5c93a62a968e | underdog | Jadan Baugh | Rush Yards | under | 0.034216745542511307 | 2026-11-13T01:09:17Z | 2026-11-14T23:15:00Z |
| underdog|c41bdf61-ec11-47ea-aa1a-d7caf74b5490 | underdog | Javonte Williams | Receiving Yards | under | 0.03421399617321885 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| prizepicks|16941236 | prizepicks | Emmett Johnson | Rec Targets | under | 0.034180503318125166 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|79628351-e183-4617-9674-6f3bd2f44202 | underdog | Trent Mosley | Receptions | under | 0.03411216452257926 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|89bf8183-bd08-4703-ace9-5a6a0f2494b9 | underdog | Jaylen Warren | Rush Yards | under | 0.034088465358187325 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|5eed7261-a329-46a9-8b9b-e6510e877a59 | underdog | Rico Dowdle | Receiving Yards | under | 0.03408492305432431 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|f04cdcb8-a7b9-444b-82cd-d9c4f68b5331 | underdog | Braelon Allen | Rush Yards | over | 0.03360981687067632 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16941209 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.03352020748434126 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|6b057709-d6dc-4521-be96-04631e1d5383 | underdog | Devin McCuin | Receptions | over | 0.03350696128296665 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|1ceddca8-fe53-49f8-831a-62aa046bb636 | underdog | Wan'Dale Robinson | Receptions | under | 0.033293997712305456 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b7e99795-da26-48e8-8250-77ae145b57a0 | underdog | Omar Cooper | Receptions | over | 0.033145857239147036 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e5a1d8cc-9fd0-4363-a0ec-b6077999af5f | underdog | Savion Williams | Receptions | under | 0.03308677892440648 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3519633c-2f5b-401f-81ff-3f7c72260009 | underdog | Jordan Faison | Receiving Yards | under | 0.03280421092792818 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|1532deaf-e39a-42f6-9444-fb37fb0c6508 | underdog | Jordan Love | Rush Yards | under | 0.03279240845654863 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fbe01566-8f78-4ecb-bd88-bba2642ed39a | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.032788269210784704 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| prizepicks|16863704 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.032604420063334416 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|ccea17c8-e390-4da5-badf-d4cc345723dd | underdog | Jared Curtis | Pass TDs | under | 0.03245948310828595 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|6497b72f-8917-4fb8-bf75-fee9b6802c4b | underdog | Mitchell Evans | Receptions | over | 0.032392458273830194 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2d8bee1d-b82e-473c-9380-c1fd773a61e6 | underdog | Marquis Johnson | Receiving Yards | under | 0.032032730753339234 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|6cc86369-a1f7-4361-91da-ad05d8e0835f | underdog | Mike Washington | Rush + Rec Yards | under | 0.03200244448616896 | 2026-11-11T16:13:16Z | 2026-11-15T21:05:00Z |
| underdog|851cf522-a813-4638-b05f-952b6fc93c69 | underdog | Beau Pribula | Pass TDs | over | 0.031912057643647795 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|025f64b9-c0b3-46a3-a947-ad3479490326 | underdog | Adonai Mitchell | Receiving Yards | under | 0.031903411083543554 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|8206c911-50a1-4311-a9ab-a4bce1c90765 | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.03176549797720041 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|7e7631f5-e3d4-46ed-b5f1-266bf3d7b45a | underdog | Jalen Coker | Receptions | under | 0.031714257024792025 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e15b1902-efc1-481a-ac83-fb2fee335221 | underdog | Ashton Jeanty | Receiving Yards | over | 0.031645254793110755 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|02db5ac0-d83a-4739-b360-6691e089d776 | underdog | Aaron Jones | Rush Yards | over | 0.03155148511107231 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|792b0d48-a54c-4ebf-9850-d82cd32eb4e1 | underdog | Mario Craver | Receptions | over | 0.03154931517292969 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|cf92e490-1049-4ec5-990b-051a43679abb | underdog | Bam Knight | Rush + Rec Yards | under | 0.03150072274009241 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|4e3d83a3-32df-4adc-a6cb-19c47ccd3314 | underdog | Mike Washington | Rush Yards | under | 0.031494264716392606 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|fc87e960-7746-4e65-90af-f9d3506e7fc4 | underdog | T.J. Hockenson | Receptions | under | 0.031480752318138516 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|7522f997-3caa-4e9a-8aea-1d2b2e4b9e9f | underdog | Tyler Allgeier | Rush Yards | under | 0.03139779528079756 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|0658238c-5e5a-4e3a-b337-a75de8881f51 | underdog | Kwazi Gilmer | Receptions | under | 0.03126132628636824 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|3c55b8d7-f72b-4d57-b825-1e0f75a1c9f1 | underdog | Fame Ijeboi | Rush Yards | over | 0.031074656707587134 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| prizepicks|16834647 | prizepicks | Javonte Williams | Rush Yards | under | 0.030973438538770326 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|b07aa94a-6957-4140-93d5-a6e918e23c20 | underdog | Omarion Miller | Receiving Yards | under | 0.03096398161420666 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|242c333e-4229-4bd6-981b-3f85497b6e4e | underdog | Brock Bowers | Receiving Yards | under | 0.0306330498389088 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|d649c6df-5a33-430f-ad49-de2a7613706b | underdog | Peyton Woodring | FG Made | over | 0.030478185796160684 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|f1fb25a0-6179-4fbc-935a-268c21e6a711 | underdog | Re'Shaun Sanford | Rush Yards | under | 0.03045602797791802 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|d34f0fb3-0376-4769-b33a-969afc12b085 | underdog | Bam Knight | Rush Yards | under | 0.03039824115306078 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|d86772b1-c024-41b8-93d5-7c5dc8255d49 | underdog | Miles Coleman | Receiving Yards | under | 0.030316694491087315 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|b357c9e8-27ef-4f86-9497-cac10d884f8c | underdog | Sam LaPorta | Receptions | under | 0.030234889226053996 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|320ad195-4f46-4b95-81e5-d49c528bc76f | underdog | Micah Gilbert | Receiving Yards | over | 0.030107857960482542 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
