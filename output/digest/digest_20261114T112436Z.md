# Pipeline Digest -- 2026-11-14T11:24:36Z

## Run summary
- Ingestion: 42219 rows (PrizePicks OK, Underdog OK)
- Estimation: 42219 rows estimated (from 42219 ingested props)
- CLV logging: 82 newly flagged, 0 newly closed, 981 still open (111872 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|7f283249-7197-4320-966d-81114f429326 | underdog | Brandon McManus | Kicking Points | under | 0.4606060606060607 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|31a33637-10de-42b7-9cb8-d9a87d355fdd | underdog | Riley Patterson | FG Made | under | 0.40062585991961885 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|e4938450-a97d-4adc-ac59-dac8885a7b89 | underdog | A.J. Brown | Receiving Yards | under | 0.4 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|fd4adea9-7044-4a68-9ede-279179122ec8 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-14T11:31:26Z | 2026-11-15T21:25:00Z |
| underdog|10123e10-e2a0-4364-8ff1-2ffcd06f991d | underdog | Austin Mack | Pass TDs | under | 0.4 | 2026-11-14T01:00:02Z | 2026-11-14T17:45:00Z |
| underdog|c6c07a22-7858-46d3-aaa3-096f53414f8f | underdog | Riley Patterson | Kicking Points | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|146a5d3b-156f-4cb2-9957-793d78599811 | underdog | Aaron Rodgers | Pass Yards | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|9f489a8a-0b3e-41c0-b6b9-8969628304ec | underdog | King Miller | Receiving Yards | over | 0.4 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|053c3e50-6f32-466c-a249-84cee7048674 | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|abbeb5c4-21e6-4875-8173-8f2e9eb69d19 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|a14ab79d-2c35-4572-b5e5-65f7e4f3d25f | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|02236b14-ee6c-4f53-aa2b-4cc4244da560 | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|42070c06-f98b-402f-b072-cf90401e5dfa | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|e6543c89-d139-402a-be7b-4d5cb96ea168 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|535cadaf-10da-48d4-b1a9-cd0e4727a968 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-14T11:31:26Z | 2026-11-15T21:25:00Z |
| underdog|651718aa-f819-4e2f-ad0b-6295b7832c86 | underdog | Drake Maye | Pass Yards | under | 0.38488538296258934 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|bf3b1159-fa11-42f9-ae28-7421be127235 | underdog | Eddy Pineiro | FG Made | under | 0.3826019825177006 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|08345c52-8552-4b04-813c-2f46ea4286f3 | underdog | Simi Fehoko | Receptions | under | 0.3799490814604448 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|893c220c-371b-4fe2-b7da-6d064755aa8a | underdog | Anthony Gould | Receiving Yards | under | 0.3703160814309572 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|e56b75d8-3fed-491a-a1d1-a413d8c592cc | underdog | Devin Duvernay | Receiving Yards | under | 0.3683165054929062 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| underdog|a5cda75b-9567-4c3b-86cb-d6ebb3e0d4fa | underdog | Cam Ward | Pass Yards | under | 0.36218425970416424 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|8fc25aea-1d6d-44a9-b09d-e9f462b2a8ec | underdog | Simi Fehoko | Receiving Yards | under | 0.3586416140950188 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|f23e8b67-27a1-486b-84c4-7189cabc9f1b | underdog | Anthony Gould | Receptions | under | 0.3555233950704253 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|9b68965c-3c26-46a8-baae-a65e2eecf9ad | underdog | Brandon McManus | FG Made | under | 0.35442585143255134 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16834516 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16864061 | prizepicks | Jack Endries | Rec Yards | over | 0.35094246505677495 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16966260 | prizepicks | Ørjan Nyland | Goalie Saves | under | 0.35094246505677495 | 2026-11-14T01:00:02Z | 2026-11-14T12:00:00.000-05:00 |
| prizepicks|16834515 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|1a25507b-8125-4524-83eb-bd6dc420d8a6 | underdog | Jared Goff | Pass Yards | under | 0.3501184306337788 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|7ba17254-22b1-4b2c-9b2c-4eacf8338ebe | underdog | Michael Penix | Pass Attempts | under | 0.3427792036855505 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4568ee13-4012-4f15-985e-2a26ef1de93e | underdog | Bryce Young | Pass Yards | under | 0.33548654238737186 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|da5d718b-0689-4175-821b-b2385d9da6ed | underdog | Zach Charbonnet | Receiving Yards | under | 0.33180319032411565 | 2026-11-11T16:13:16Z | 2026-11-15T21:05:00Z |
| underdog|307411bf-5514-4d3f-a60e-30bed16a85d7 | underdog | Patrick Mahomes | Pass Yards | under | 0.32995712217574935 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16942049 | prizepicks | Demarcus Robinson | Rec Targets | under | 0.32153436796155255 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|1ff670bf-2457-4528-8460-3c29b9abdc73 | underdog | Geno Smith | Pass Yards | under | 0.3188854735913441 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|0e868b69-ee8c-49e6-b214-1399cb18ea20 | underdog | Kirk Cousins | Pass Yards | under | 0.3137727685343159 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|f9978ce2-db4f-472d-ae6b-7ae2ed4383c0 | underdog | Brock Purdy | Pass Attempts | under | 0.3095759047079447 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|00efed34-b5f2-4951-abad-8c8793e5c954 | underdog | Joe Burrow | Pass Yards | under | 0.3079937259333765 | 2026-11-12T07:07:56Z | 2026-11-16T01:20:00Z |
| underdog|4737cea0-616e-4604-a6e5-fd14ac48e709 | underdog | Tutu Atwell | Receptions | under | 0.30768720817936746 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a4aff594-458d-4ab2-8741-d573c94fd29c | underdog | Tyler Shough | Pass Yards | under | 0.30396344221607396 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|0b9d4162-31be-483a-8356-d1c8f0f2836f | underdog | Daniel Jones | Pass Yards | under | 0.30211128314934943 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|04d9b629-2110-40ef-b134-82649932148a | underdog | Jacoby Brissett | Pass Yards | under | 0.2979783699769716 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|3b5f2984-eb35-471f-94d6-998914e68199 | underdog | Maddux Madsen | Pass Yards | under | 0.2909548585748869 | 2026-11-14T01:00:02Z | 2026-11-14T23:00:00Z |
| underdog|b5fb6661-40fc-4196-9686-d21c10809596 | underdog | Bryce Young | Pass Attempts | under | 0.2854974352714704 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2b554710-678c-443f-bb14-2208a77f507c | underdog | Justin Herbert | Pass Attempts | under | 0.2847606859755615 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|73782ef7-994d-49b5-96d3-9cf6e1c6ca31 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.28392287975724284 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| prizepicks|16941222 | prizepicks | Deion Burks | Rec Targets | under | 0.27909833862126254 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|29dc30cc-3894-4a38-921e-88a9b06af5b3 | underdog | Deshaun Watson | Pass Yards | under | 0.27908282270791485 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|2d56e29c-54ec-427c-845e-ef6730327906 | underdog | Ben Yurosek | Receptions | under | 0.27660329710590137 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16834509 | prizepicks | Geno Smith | Pass Yards | under | 0.2763361682548745 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|69ea800d-baf2-4ec2-aa6b-0f54999544c3 | underdog | Drake Maye | Pass Attempts | under | 0.27583197269825244 | 2026-11-13T19:43:07Z | 2026-11-15T14:30:00Z |
| underdog|c8b72634-2199-44b4-918c-14b8b75a5665 | underdog | Josh Allen | Pass Attempts | under | 0.27359287330136317 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4426e732-6666-4dad-8847-df60408b6e0e | underdog | Eddy Pineiro | Kicking Points | under | 0.27246339729437163 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|fe02ea87-dab7-429b-b9b8-8177dc9005b7 | underdog | Andy Borregales | Kicking Points | under | 0.2696627029124462 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|cc32a0a8-f5c4-4665-b91c-5b1deb8556ae | underdog | Colby Parkinson | Receiving Yards | under | 0.2664498982632588 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| prizepicks|16864050 | prizepicks | Brock Wright | Rec Yards | over | 0.26570772133930776 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|bcdde121-b386-493e-864c-4bcc61392f15 | underdog | Tutu Atwell | Receiving Yards | under | 0.2642699536334714 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a7f2cda3-7806-4825-94cb-3314772c5a43 | underdog | Mike Washington | Receiving Yards | over | 0.26259620989363885 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|3442d1a4-ca40-48d4-a305-81875ed6bf50 | underdog | Cam Ward | Pass Attempts | under | 0.2592641238477811 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|dd740bd3-6b74-45da-9756-483cfbb09d28 | underdog | Deshaun Watson | Pass Attempts | under | 0.25863657281386854 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| prizepicks|16941221 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.25598115127940624 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16864049 | prizepicks | Tyler Conklin | Rec Yards | over | 0.2534382625358713 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|fe8292b1-ce05-486d-b732-66142a05472c | underdog | Andy Borregales | FG Made | under | 0.2485620967855957 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|76ebd5e4-98e6-4e69-b5c3-e679ebe74a07 | underdog | Chase Brown | Rush + Rec Yards | under | 0.24835130844327968 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|ec741310-bec5-4831-8dd9-4b1fb6a20505 | underdog | C.J. Stroud | Pass Yards | under | 0.2470338347866693 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|7279c326-d7e6-469c-9dd8-f0ec2a171e89 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.24593076762155852 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|83373ed9-f9ce-45e1-9625-900830675049 | underdog | Luca Lombardo | XP Made | over | 0.24473454966597602 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|a52bd97f-61ee-41d6-b00b-7706385e2fdb | underdog | Kwity Paye | Sacks | over | 0.24305132922075998 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| underdog|6fd045da-e0dd-4ab0-8819-c11153822667 | underdog | Aaron Rodgers | Pass Attempts | under | 0.2422362767070224 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|c16e8dc1-4439-4474-8743-ea12fb445cc2 | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.24035945609588383 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|53e195bb-7857-44f8-9b4b-d4065f90f0ab | underdog | Drew Mestemaker | Pass Yards | under | 0.23646560375858827 | 2026-11-13T19:43:07Z | 2026-11-15T02:30:00Z |
| underdog|26d4ddfa-d9fc-4f08-86e6-a916620f7be4 | underdog | Jordan Love | Pass Yards | under | 0.2343087179750497 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|0fe2e633-f694-4097-83ad-e9cada46e27b | underdog | Jaylen Wright | Rush Yards | under | 0.23203924349154836 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|14b46430-d112-4bb9-8474-9f3e043c7262 | underdog | Kyle Pitts | Receiving Yards | under | 0.23074083814986768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|71eb1caa-770c-48a5-933a-3e9ada88c4d3 | underdog | Tait Reynolds | Total TDs | under | 0.2262771279989697 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|4a514069-20ab-41be-aeb3-e65c7fed2e72 | underdog | Chris Rodriguez | Receiving Yards | over | 0.22333565019602397 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|58450652-ec43-42a4-9351-a3efd501d9af | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.22331444437795633 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|c056f71a-3a42-40b4-96f9-d2609cc9beed | underdog | Joe Burrow | Pass Attempts | under | 0.22141583740196058 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|2dfe4a4e-673f-4b70-9848-bf6c7b6c6341 | underdog | Reggie Virgil | Receiving Yards | under | 0.22038234116811617 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|169cb841-cffa-4109-8027-3415c4f4b563 | underdog | George Kittle | Receptions | under | 0.2194077839592593 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|e8aeb4f5-a722-40e0-a568-9239a4140a93 | underdog | Malcolm Koonce | Sacks | over | 0.21622725378399718 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| prizepicks|16834513 | prizepicks | Tyler Shough | Pass Yards | under | 0.21404760098629738 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7d68e3e2-e22c-4ad5-b3fb-8afe750a6042 | underdog | Alonza Barnett | Pass Yards | under | 0.21305975192843163 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|900a6acc-8f2e-4a73-8d6c-9a35b225cafb | underdog | Jared Goff | Pass Attempts | under | 0.2123603264736973 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|18a61f36-9cc0-49bf-813a-2cbed646880a | underdog | Demarcus Robinson | Receptions | under | 0.2098129701184389 | 2026-11-13T01:09:17Z | 2026-11-15T21:25:00Z |
| underdog|43eab978-b035-4b9e-91fe-97a8d57d94cb | underdog | Cooper Barkate | Receptions | under | 0.20979341100184778 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|e361b0b3-846c-4d00-ab28-2acf28eed70b | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.2087967118476648 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|f41a0655-6887-4b1d-b1c5-4481335ee2e6 | underdog | Christian McCaffrey | Rush Yards | under | 0.2075382148708218 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|e94c9cd9-eb43-4a62-912e-a83f4184c727 | underdog | Trey McBride | Receptions | under | 0.20737779171812365 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|34ffe77e-d083-49fe-a233-c2a7085b1a55 | underdog | Jordan Addison | Receptions | under | 0.20675489884434617 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|5a53b201-38d0-4684-8a80-f3d1114348a4 | underdog | Cameron Heyward | Sacks | over | 0.20669437056666098 | 2026-11-14T11:31:26Z | 2026-11-16T01:20:00Z |
| underdog|ae9ffd9a-ad31-460f-b0d9-472730e245c3 | underdog | Demarcus Robinson | Receiving Yards | under | 0.20520961983923902 | 2026-11-13T01:09:17Z | 2026-11-15T21:25:00Z |
| underdog|e867dd92-2ce3-4e0e-8aa7-56b0042a3ae7 | underdog | Germie Bernard | Receiving Yards | under | 0.20503393613278686 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|081218b4-9196-449c-9fdf-62d2d39e0e03 | underdog | Zane Gonzalez | Kicking Points | under | 0.2048077405855635 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8cde15a-8b1a-4730-848f-163f3f890c7d | underdog | George Kittle | Receiving Yards | under | 0.20443082432893867 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|e8438e40-9c32-4ebf-8af6-bad7f136754e | underdog | Jaden Craig | Total TDs | under | 0.20406298794366962 | 2026-11-14T01:00:02Z | 2026-11-14T19:00:00Z |
| underdog|051a8c4f-8105-4095-aab4-7a5b0cba7371 | underdog | C.J. Stroud | Pass Attempts | under | 0.20323087968521425 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7457518e-951d-4df6-add8-fcb7647b8119 | underdog | Mason Graham | Sacks | over | 0.20316287224661062 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|65aed765-d701-4c7c-b180-c92353b6287f | underdog | Jadarian Price | Rush Yards | under | 0.2026452278850812 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|f90743a5-9d2a-47d3-a4e4-089c9764ad13 | underdog | Dak Prescott | Pass Attempts | under | 0.2011150399848315 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|306e7fdc-ff79-4617-b76c-a9f6f3f59c86 | underdog | Daniel Jones | Pass TDs | under | 0.20080324674994554 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f2ec1675-9567-4b92-b4f3-92577312bc62 | underdog | Zach Charbonnet | Rush + Rec Yards | under | 0.20021395939773834 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| underdog|291d4ec0-2767-40c9-accb-8a2011deec96 | underdog | Elina Svitolina | Double Faults | under | 0.199872902718082 | 2026-11-14T11:31:26Z | 2026-11-14T21:10:00Z |
| underdog|02c6a0d5-4829-41b0-b18c-a3035ecd53d6 | underdog | Jordan Addison | Receiving Yards | under | 0.1987559260199948 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|b786ee26-692a-4f4d-87d1-a8c475952d8a | underdog | Deion Burks | Receptions | under | 0.1984991277921363 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|a3ea499a-cc1b-4bff-835e-8399e8a4733f | underdog | Tait Reynolds | Pass TDs | under | 0.19843383215844468 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|8a1b591a-8990-49d6-b67d-de2ef4f6aacb | underdog | Rashee Rice | Receiving Yards | under | 0.1982963392264364 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|56f2e012-5686-4d16-bf10-08f311834b4c | underdog | Jordan Love | Pass Attempts | under | 0.19807843703295192 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|97f17a14-3d73-4de2-b8ed-5fe1812529d7 | underdog | Devonte Wyatt | Sacks | over | 0.1980309357726293 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|c0f8278e-1470-4d41-a99e-2b632f7a3dd9 | underdog | Keion White | Sacks | over | 0.19740278247508078 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| underdog|4965f49e-288a-4863-8f2f-88e6eda6d943 | underdog | Hank Brown | Pass Yards | under | 0.19694960176660092 | 2026-11-14T11:31:26Z | 2026-11-15T00:30:00Z |
| underdog|87bfd021-0498-4180-b485-15610037e2e5 | underdog | Kaelon Black | Receiving Yards | over | 0.1963921949855576 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|83b44129-9596-4ab7-910d-0d5b5037b4ab | underdog | Geno Smith | Pass Attempts | under | 0.19625166531744365 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|45eaa191-9cdc-463c-8d91-beefc80f7256 | underdog | Trevor Lawrence | Pass Attempts | under | 0.19395844303678533 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|2c882634-170d-487d-8fbc-f7e1fec2115d | underdog | Tyler Warren | Receiving Yards | under | 0.19170425617944387 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|0ca5f198-cc15-4b12-b643-c3388a576202 | underdog | Tank Dell | Receptions | under | 0.19110284381179832 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8bfeabc8-5299-494a-bfeb-85b8e61de674 | underdog | Daylyn Upshaw | Receptions | under | 0.1909920607875113 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|044d9395-ca07-47e3-965b-f69f71243988 | underdog | Gavin Bartholomew | Receiving Yards | under | 0.19019685411879628 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|83e0ce0a-e731-4131-8f28-240389524187 | underdog | Josh Sweat | Sacks | over | 0.18970753160340184 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| prizepicks|16864052 | prizepicks | Jackson Hawes | Rec Yards | over | 0.18803943875076268 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|13795d17-357b-4145-bf68-ab9d21ec0c81 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.1877159820005656 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| underdog|2b36f5f8-5526-4d66-ba23-4713e850c72c | underdog | Jordan Mason | Rush + Rec Yards | under | 0.18759340449541284 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|c64dabf7-5faa-4d07-be57-7dd60d80fc67 | underdog | Chimere Dike | Receptions | under | 0.1872288283239285 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|d48dcabf-d237-4d6e-94c9-99b511e722a9 | underdog | Alex Highsmith | Sacks | over | 0.1868490415408096 | 2026-11-14T11:31:26Z | 2026-11-16T01:20:00Z |
| underdog|e53d005a-db4d-40e9-b843-107136039d88 | underdog | Bo Jackson | Rush Yards | under | 0.18598061441788571 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| prizepicks|16941214 | prizepicks | Savion Williams | Rec Targets | under | 0.185837094416891 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|3d1b3b14-b375-41f9-a9dd-f8e6b2e61696 | underdog | Anthony Colandrea | Pass Yards | under | 0.18438146826760027 | 2026-11-13T12:14:20Z | 2026-11-14T17:30:00Z |
| underdog|f3819a2f-d9d4-46ed-8ace-41086707c9f9 | underdog | Zach Charbonnet | Rush Yards | under | 0.18429325508963512 | 2026-11-14T01:00:02Z | 2026-11-15T21:05:00Z |
| underdog|0c90304b-97a9-4467-9736-313bc4155ac0 | underdog | Khalil Herbert | Rush Yards | under | 0.18354154495685115 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|145d0e7c-ebc2-4247-b8cd-ed5b0d92a96b | underdog | Ja'Marr Chase | Receiving Yards | under | 0.1833658811737735 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|5c95b1fe-ebcb-4b5f-843c-0aa11d01e2f9 | underdog | Jackson Kleather | FG Made | over | 0.18306256848091473 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|336befd7-fc3b-4fc6-be96-8f9f930dd43f | underdog | Jared Goff | Pass TDs | under | 0.1828305718973564 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|eb1c3c80-366a-4251-99fb-356251e8356f | underdog | Evan McPherson | FG Made | under | 0.18227554836779813 | 2026-11-11T16:13:16Z | 2026-11-16T01:20:00Z |
| prizepicks|16971480 | prizepicks | J'Koby Williams | Rush Atts | under | 0.18223839587244062 | 2026-11-14T11:31:26Z | 2026-11-14T21:30:00.000-05:00 |
| underdog|08002729-32e7-4c29-b25d-22644abe6bad | underdog | Jack Bech | Receiving Yards | over | 0.18168505454405048 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| prizepicks|16834801 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1816833032066426 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|f1ae34e8-674a-4744-a233-47c5f2216dd4 | underdog | Cam Ward | Pass TDs | under | 0.18083709268551018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|90f47457-12c2-4ecb-9333-7a188e024c28 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.17845871751059827 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16864055 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.17800572418642757 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|8d28592f-7fdf-4f34-8494-86120f2f4fdc | underdog | Chimere Dike | Receiving Yards | under | 0.17766109320276413 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|607f5ae6-2116-4003-99af-5442503e0ae4 | underdog | Brock Purdy | Pass TDs | under | 0.17680376455348845 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|24e79c8b-21be-4eab-91a7-99b595453f06 | underdog | Derrick Barnes | Sacks | over | 0.17610433472070874 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|ab208bdb-ddee-40f9-a2ed-f481ef72f216 | underdog | Drake London | Receptions | under | 0.17466437471048346 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|11d87a7f-b9eb-4e9c-9cc7-8fb7eb3b0fb1 | underdog | Chris Jones | Sacks | over | 0.17428188307172288 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|604452e7-7084-4463-ad0b-330ec454af3d | underdog | Jermaine Johnson | Sacks | over | 0.1740195882208193 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|d86abc07-0c4e-46e2-8f7e-57df8c7e5255 | underdog | DJ Black | Receptions | under | 0.1737530018125807 | 2026-11-13T19:43:07Z | 2026-11-15T00:45:00Z |
| underdog|e6ed003a-0261-43f3-8539-8b3a5843dcf4 | underdog | Michael Hawkins | Rush Yards | under | 0.17369289774038532 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|bed83661-cc7d-4b22-9b07-e0978ada4d5d | underdog | Jameson Williams | Receiving Yards | under | 0.1733097016002607 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|ed754c45-0f3b-411b-b86d-b7b8d8acce60 | underdog | Walker Eget | Pass Yards | under | 0.1732760644135739 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|0e95f930-b883-466d-9f64-9b2c26ddc094 | underdog | Bear Bachmeier | Total TDs | under | 0.1722182141883244 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|9a273eba-2d5d-404c-b81f-93d6389c3340 | underdog | Ben Black | Receiving Yards | under | 0.17156866779821567 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|cb516925-3b8d-476b-a0a1-f86967eb258b | underdog | Deion Burks | Receiving Yards | under | 0.17072964581538708 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|b59c83a6-7075-4cc3-84dd-27157fa643ac | underdog | Jahan Dotson | Receptions | under | 0.17063963423916995 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|16f7ac78-0db9-439a-b28c-c528416128ed | underdog | Breece Hall | Rush + Rec Yards | under | 0.17060228312474868 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|d1cd77b9-ccb0-4e97-8338-6d8e64b9dc84 | underdog | Brevyn Spann-Ford | Receiving Yards | under | 0.17040535140271207 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|d56eca67-b486-424a-99ac-d916fbc55564 | underdog | Christian Barmore | Sacks | over | 0.17021982022032822 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| prizepicks|16864057 | prizepicks | Oscar Delp | Rec Yards | over | 0.16971647479255814 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16952737 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.1691097228703865 | 2026-11-13T19:43:07Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4e9d2b81-8437-409b-8ff4-2380820c1bc4 | underdog | Gianni Spetic | XP Made | over | 0.1690686381121324 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|ee9a0405-33bb-456d-a2ef-754c6c2c03a7 | underdog | Tyler Shough | Pass Attempts | under | 0.1678377974371722 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4ba517fa-f4dd-49ab-b862-8fd74aa58cdc | underdog | Bhayshul Tuten | Rush Yards | under | 0.16718566869469154 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16942016 | prizepicks | Tutu Atwell | Rec Targets | under | 0.16716285331431757 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|696c6b73-3e04-426b-a463-26276c4aee5c | underdog | Ryan Fitzgerald | FG Made | under | 0.16692795074675848 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c97d330b-3d6f-4b03-83d5-f93c56394bed | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.16641302347698494 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|b81b56da-fe21-4e55-9f3d-fb0b1d061257 | underdog | Daniel Jones | Pass Attempts | under | 0.16440373749700898 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|659b286c-687a-43f0-b782-5a1234a05458 | underdog | Quinshon Judkins | Receptions | over | 0.16431586645270752 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16941224 | prizepicks | Tyler Warren | Rec Targets | under | 0.16357413164889356 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|790e0cb3-2b38-4acd-b86b-71603ec45132 | underdog | Caden Buhr | FG Made | over | 0.163301765767505 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|3516e67e-fde8-433e-a27b-12e6ac6fc964 | underdog | Isaiah McGuire | Sacks | over | 0.16254502406395688 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|5d36bd96-4734-4512-af4a-75b1418c21b2 | underdog | Nico Collins | Receiving Yards | under | 0.16147686411017215 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16834640 | prizepicks | Woody Marks | Rush Yards | under | 0.16140868621854165 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|9a9b4886-cd1f-4523-9dc3-cd8753a51f8b | underdog | Kirk Cousins | Pass Attempts | under | 0.16130209940228557 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|267aa46e-9d55-48f1-9210-3f2ca1af46cf | underdog | Jaylen Raynor | Total TDs | under | 0.1609792387695148 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|43d067f1-bb0f-4c09-acf1-fa7919bc9723 | underdog | Jared Goff | Rush Yards | over | 0.16011142578061638 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|7bb23fe2-fc15-4d4c-a9e9-0ec60eb0bbeb | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.15979282473646705 | 2026-11-14T11:31:26Z | 2026-11-15T14:30:00Z |
| underdog|28e41540-e6d5-4ec1-b474-b3fb179168ec | underdog | Justin Herbert | Pass TDs | under | 0.1593713737739526 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|6b95f8da-eb5f-4b9c-bfb3-d1aaec355169 | underdog | Maliek Collins | Sacks | over | 0.15915185846375718 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16834646 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.15848722202295062 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f3733138-10af-46da-8e69-cf5ca4b940fc | underdog | Reggie Virgil | Receptions | under | 0.15825220568688703 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d4535591-3a5f-4c28-b756-d85acd4fdf77 | underdog | Jordan Mason | Rush Yards | under | 0.15679467436665007 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16864059 | prizepicks | Ian Thomas | Rec Yards | over | 0.15662706211871924 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|25185fe8-2e75-4f8e-a1b5-f6c471df1357 | underdog | Arch Manning | Pass TDs | over | 0.15631529903366037 | 2026-11-12T07:07:56Z | 2026-11-15T00:30:00Z |
| underdog|51482ef6-863b-47ca-8fe5-ddce1363c28f | underdog | Theo Melin Ohrstrom | Receiving Yards | over | 0.15614556650528089 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|34592e3c-3b83-4af7-bd2b-617a52ca4334 | underdog | Trey McBride | Receiving Yards | under | 0.15553372270182042 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|b470bd4b-1813-44ad-9c4c-e7d50bdbeae5 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15499103436448625 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| prizepicks|16941231 | prizepicks | Rashee Rice | Rec Targets | under | 0.1549150253690711 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|394b3afc-7a30-4b5a-931d-a5c759f033bb | underdog | Isaiah Marshall | Pass Yards | under | 0.15440860530377654 | 2026-11-14T11:31:26Z | 2026-11-14T20:30:00Z |
| underdog|896ec2df-285c-4557-8604-a14a40ba246f | underdog | Seth McGowan | Rush + Rec Yards | under | 0.15439980406728382 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|97a67afc-3f9f-4982-8bae-be868c2c4737 | underdog | Devon Dampier | Pass Yards | under | 0.15303323942761993 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|3c08b80e-f215-45f2-a1b8-54a7969c5531 | underdog | Brevyn Spann-Ford | Receptions | under | 0.15298682224983495 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|585b41b2-1294-443c-8440-2524471c4ddf | underdog | Laquon Treadwell | Receptions | under | 0.15250354276005051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3dcc3752-86c6-417f-a0f9-0584e4bc7e73 | underdog | Eric Wilson | Sacks | over | 0.15243839637020545 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|0b6b9464-f3ca-4d21-bb53-19e9a2f9619a | underdog | Karl Brooks | Sacks | over | 0.15173315822223826 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|c5c4fe7e-563e-4a77-ae50-060011c7dec8 | underdog | Xavier Hutchinson | Receptions | under | 0.1509666630300549 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|389ecff7-4b02-44e7-b033-0d28eb18f77c | underdog | Kevin Coleman | Receptions | under | 0.15079646702167293 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|af522396-84d1-406b-b37c-206c42ee1d80 | underdog | Jake Fette | Pass Yards | under | 0.15017672058611453 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| prizepicks|16942048 | prizepicks | George Kittle | Rec Targets | under | 0.14983085550655606 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|2e165ef5-272e-47fb-8214-52bc9d58510a | underdog | Amon-Ra St. Brown | Receptions | under | 0.14980442293467233 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|c6f5d95f-2b53-4656-bed1-792f520c72ba | underdog | Garrett Wilson | Receiving Yards | under | 0.14922011393352663 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16941176 | prizepicks | Reggie Virgil | Rec Targets | under | 0.14907298120417656 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|e3317ebd-1d1a-4ac2-8dc1-999860638691 | underdog | Jameson Williams | Receptions | under | 0.1486746602368635 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|4d7320f5-c604-482f-bc9d-eca5727ffd9f | underdog | John Metchie III | Receiving Yards | over | 0.14866705775674083 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|1a20f785-f85c-4e70-a420-adf5f0ed3164 | underdog | Ollie Gordon | Receptions | under | 0.148665850420447 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5211515d-7ad3-4eb4-b67f-a89b5e6b4abd | underdog | Laquon Treadwell | Receiving Yards | under | 0.1485527232635908 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|7d76e9dd-5308-4c1a-ba1c-ba61b79e4408 | underdog | Jayden Maiava | Pass TDs | over | 0.14850033842731425 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|3dd60339-cf17-45f0-b767-75c894f95225 | underdog | Cooper Barkate | Receiving Yards | under | 0.14832914398251418 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|e53bc5a3-348d-43d3-8fad-5ede923a2d5d | underdog | Thomas Castellanos | Pass TDs | under | 0.1481094584925654 | 2026-11-14T01:00:02Z | 2026-11-15T02:30:00Z |
| underdog|58103c82-771e-4fbe-bcb3-fbd7b42b077f | underdog | Matthew Stafford | Pass Yards | under | 0.1479404364360365 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|7577e97c-e510-4fc9-9822-7ea09e7f9048 | underdog | Maalik Murphy | Pass TDs | under | 0.14721193220902917 | 2026-11-13T19:43:07Z | 2026-11-14T23:00:00Z |
| underdog|61750b40-600e-4985-ba4f-4746992f5a79 | underdog | Pat Freiermuth | Receiving Yards | under | 0.14668230275794958 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|27fd84f6-aa6d-447b-83e6-8d9a957bbdd5 | underdog | George Pickens | Receiving Yards | under | 0.14657774052188666 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|bd5586fa-284e-4331-87b5-39a9a336cb92 | underdog | Isaiah Marshall | Pass TDs | under | 0.1455916479416146 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|2f449c27-45c9-41d0-b8fd-72225ef3ee30 | underdog | DK Metcalf | Receiving Yards | under | 0.14553269331212992 | 2026-11-13T19:43:07Z | 2026-11-16T01:20:00Z |
| underdog|86547c3d-b244-4af0-81ee-51d77f062ce3 | underdog | Derrick Henry | Rush Yards | under | 0.1446716010386574 | 2026-11-14T11:31:26Z | 2026-11-17T01:15:00Z |
| underdog|35aa2d03-9b78-4bc7-acea-60a2349ced2f | underdog | John Franklin-Myers | Sacks | over | 0.14409315313926113 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|7281e3b0-a702-402a-8b62-fc9add59bf36 | underdog | Chuba Hubbard | Rush Yards | under | 0.14389175335524607 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cf6cb602-6d19-4560-92cf-eba77e59abce | underdog | Byrum Brown | Pass Yards | under | 0.14379008226835766 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| prizepicks|16942028 | prizepicks | Hunter Henry | Rec Targets | under | 0.1433641205147107 | 2026-11-13T12:14:20Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|21ace0c9-85f0-43f3-9392-a8bbadc5666b | underdog | Trey Butkowski | XP Made | over | 0.14320322887137465 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|f2e836b0-0889-4532-817f-f54d419292c9 | underdog | Connor Hawkins | FG Made | over | 0.14287325912611332 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|7127040f-b7a9-4ae3-b4e7-93f37a4d19b0 | underdog | Nolan James | Rush Yards | under | 0.14228156260827163 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|4c42a4f7-59bd-4cc5-96de-2caa245cf96e | underdog | Ja'Marr Chase | Receptions | under | 0.14198666098231127 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8d8893ec-f444-46e0-bc6b-b229539f440a | underdog | Kyren Williams | Rush Yards | under | 0.14173771981934158 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|a8df2bfd-753f-497d-81c7-7d8c49469970 | underdog | Foster Moreau | Receptions | over | 0.14124636142536817 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|c14dec7d-e82b-46f4-a1fb-3c0d04a7e2d0 | underdog | Tyler Robles | FG Made | over | 0.14073377627119343 | 2026-11-13T01:09:17Z | 2026-11-14T21:15:00Z |
| underdog|fbacb3aa-1a1f-4fcc-aea9-63cdc8591a0f | underdog | Dierre Hill | Rush Yards | under | 0.13996174257805338 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|f1bb171f-0796-4a17-be53-1424b63680ac | underdog | Jordan Shipp | Receptions | under | 0.13924590886568067 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|fe324cdb-30f6-4ec0-b83b-b7cfbc3bb25f | underdog | Zay Flowers | Receptions | under | 0.13889916886043374 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|68f55017-c590-46a3-aaee-c0e9130f1e97 | underdog | Osa Odighizuwa | Sacks | over | 0.13854629601335877 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| underdog|26e51b8f-0825-4510-be2f-c6f7dc8ada19 | underdog | Christian Elliss | Sacks | over | 0.13849665280548948 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|12500889-7e9d-4e1a-a3da-b2ef18193e42 | underdog | Kingsley Enagbare | Sacks | over | 0.1384801140752856 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|aa70ba25-a303-4c52-9769-639de476cfcf | underdog | Javonte Williams | Receptions | under | 0.13847697518960522 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|e507b6eb-fa20-4628-97e6-d95892f64aed | underdog | Ruke Orhorhoro | Sacks | over | 0.1383721087451708 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
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
| underdog|f360ab27-deb2-4f72-b437-6349dc28e573 | underdog | Parker Washington | Receptions | under | 0.13510031202715655 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|170532ef-6942-4db9-8607-c52a3838bfe9 | underdog | James Cook | Rush + Rec Yards | under | 0.13472649314653207 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16952738 | prizepicks | Michael Penix Jr. | Pass+Rush+Rec TDs | under | 0.13469548275203003 | 2026-11-13T19:43:07Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|dd44d86a-d95b-4fe6-96b6-4554324e47d7 | underdog | Demon June | Rush Yards | under | 0.1342026981838974 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|2c1684b1-1e97-4966-8ae6-1629a8ff7ab8 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.133894591655363 | 2026-11-14T11:31:26Z | 2026-11-17T01:15:00Z |
| underdog|357567dd-807d-4205-8940-b5dbeb224c9d | underdog | Christian McCaffrey | Receiving Yards | under | 0.1337306969230765 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|43a17a67-8663-445c-9493-92e5c8ea3a10 | underdog | Princely Umanmielen | Sacks | over | 0.1328771677226246 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|f920fc38-4ed4-4387-86fa-f5a4a1829684 | underdog | Mason McKenzie | Pass TDs | over | 0.1327871832079719 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| prizepicks|16864054 | prizepicks | Jonnu Smith | Rec Yards | over | 0.13268296711964045 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|f0100902-2759-4817-a164-2c7d3cb0236d | underdog | Quinshon Judkins | Receiving Yards | over | 0.13251091684739158 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|338b9742-da48-46a2-bdaf-0fc978284c63 | underdog | Harrison Butker | Kicking Points | under | 0.1323161989221222 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|8033e91a-8918-4480-835b-e3a813bc5008 | underdog | Blake Corum | Rush + Rec Yards | under | 0.13222893877316322 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|8475bce1-90cf-43c8-9bdc-19e950db157a | underdog | AJ Barner | Receptions | under | 0.1321036071433428 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|ea58411a-8a00-4340-b4d2-ab4fb379da1b | underdog | Carson Hilbert | FG Made | over | 0.13204601822333079 | 2026-11-14T01:00:02Z | 2026-11-15T00:00:00Z |
| underdog|ad49c1a3-20cd-48ee-8447-3f9c6b778470 | underdog | Zach Charbonnet | Receptions | under | 0.13186048887942314 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|606f16ce-fb51-4f44-af6e-d6bbcf312123 | underdog | Parker Washington | Receiving Yards | under | 0.13139403359963797 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|7a1ed30d-da55-441c-b6f0-c5cf7618c573 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.13110361173012197 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b1cff4a1-76a7-403d-aa24-04a42a9ddf79 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.13091904108133545 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|668418d8-7c0f-4d71-8dfe-70e116c329d5 | underdog | Caleb Komolafe | Receiving Yards | over | 0.13076499471061398 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|01eab78a-e4c1-4cd6-a1bb-49da45615cde | underdog | DeForest Buckner | Sacks | over | 0.13071676114784714 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| prizepicks|16941180 | prizepicks | Drake London | Rec Targets | under | 0.13054552219056026 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16834805 | prizepicks | Tucker Kraft | Rec Yards | under | 0.13048896157966627 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5265ce9f-d1a4-4ac8-8168-2476d15b68b4 | underdog | Rashee Rice | Receptions | under | 0.13038787864818369 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|109fa5b2-b5e8-4b2c-85c5-7dd502f843ad | underdog | Landen Chambers | Rush Yards | under | 0.13001488815600604 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|6e81085a-3d8a-42e7-819c-98a47c132d00 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.12980647573211435 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|693fb5e3-148f-43fc-b054-d44605b4d1fb | underdog | Kimani Vidal | Receptions | under | 0.12943283574984177 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|a51976ae-665d-4e1e-9e7f-fe7fb5e0ba10 | underdog | Deebo Samuel | Receiving Yards | under | 0.12866658249865393 | 2026-11-13T12:14:20Z | 2026-11-15T21:25:00Z |
| underdog|da61ada7-6550-4585-84d2-1388eed99d50 | underdog | James Cook | Rush Yards | under | 0.12765289952620407 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|c7678b73-9c60-4770-9676-d99c5e6b71c7 | underdog | Khalil Shakir | Receptions | under | 0.12759270653403465 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2ed2c162-34df-4da8-a9cd-e8e1e22dd034 | underdog | Thomas Castellanos | Pass Yards | under | 0.1272924934668218 | 2026-11-13T19:43:07Z | 2026-11-15T02:30:00Z |
| underdog|0d93614d-67c7-48f7-ad74-14c605559df3 | underdog | Jessica Pegula | Double Faults | under | 0.1271681149701014 | 2026-11-14T11:31:26Z | 2026-11-14T20:00:00Z |
| underdog|6316e5dc-af73-4c98-8b96-f7165729f535 | underdog | Jaylen Warren | Receptions | under | 0.1263299336202357 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|fe07fee2-08b1-4240-a70a-60b787a36350 | underdog | Zeek Biggers | Sacks | over | 0.12474966275719135 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|4c2d1a8f-baf6-403c-b089-2c76412d7647 | underdog | Tait Reynolds | Pass Yards | under | 0.12460808002405188 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|b87fae6f-8b41-4480-9da9-e7877db19bb8 | underdog | Kaden Elliss | Sacks | over | 0.12459830755047041 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|7d4a66d7-5e66-4433-b339-05c2970ccb9f | underdog | Josh Allen | Pass TDs | under | 0.12444210905973119 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|8b7c93d9-5da5-47da-8d7a-930703f4b53d | underdog | George MacIntyre | Pass TDs | under | 0.12440835754503865 | 2026-11-14T11:31:26Z | 2026-11-14T20:00:00Z |
| underdog|9b61aff8-a93b-4671-b173-f7ca4286eead | underdog | Jakobi Meyers | Receiving Yards | under | 0.12435976055640752 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|64fe717c-14a9-4a4d-b286-fb2c31130ca5 | underdog | Jason Myers | FG Made | under | 0.12423824312528586 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d9b85c0b-6ba6-4644-ae85-235b94316cf8 | underdog | Foster Moreau | Receiving Yards | over | 0.12394009061461841 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|7e047dba-151c-4432-9416-d4e3155ae527 | underdog | Jordan Mason | Receptions | under | 0.12364698409171138 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|eace84de-3208-48c2-a13a-790770049e30 | underdog | Colby Parkinson | Receptions | under | 0.12317933713140317 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|7da7556c-a1f4-42ec-ad80-c12d0d953524 | underdog | John Metchie III | Receptions | under | 0.12299883356747898 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|70b3f383-cec3-4d9d-85e8-3a8526c40e46 | underdog | Linda Noskova | Double Faults | under | 0.12266405362822352 | 2026-11-14T11:31:26Z | 2026-11-14T21:10:00Z |
| prizepicks|16887420 | prizepicks | Dilin Jones | Rush Atts | under | 0.12214678937678047 | 2026-11-12T07:07:56Z | 2026-11-14T19:30:00.000-05:00 |
| underdog|517f516c-deb4-47ea-a5aa-7c4e67bf3c90 | underdog | Evan Stewart | Receiving Yards | over | 0.12209856116497286 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|7a9e2c86-7dba-4c5b-bb6a-3ef5749dc1c0 | underdog | Zane Gonzalez | FG Made | under | 0.1218622688697637 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cf37c889-4eca-4cd0-acdb-5ef3caf76c5b | underdog | Ka'imi Fairbairn | FG Made | under | 0.12158788342133897 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b74d6dd8-986c-4d47-a602-c9563892a472 | underdog | Seth McGowan | Receptions | under | 0.12157868635609315 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|72fe6ac3-c8a4-4975-82ee-49ae1fa185e1 | underdog | Luke Fahey | Pass TDs | under | 0.12089953822878752 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|954b8b3e-fa82-423c-b1d2-fb574b3c8937 | underdog | Jonathan Allen | Sacks | over | 0.12077842057126514 | 2026-11-14T01:00:02Z | 2026-11-16T01:20:00Z |
| underdog|59450b43-2430-40b2-87aa-bdea2257af7d | underdog | Blake Corum | Rush Yards | under | 0.12071235785906831 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|a5e30ad8-1103-42c0-a807-c001b30ff2c9 | underdog | Cam Little | FG Made | under | 0.12040122477593274 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|eba46761-2a28-4671-a700-8800e15e3cee | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.11977589403267419 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| underdog|61af56d0-7bbf-44b8-95db-df3abfd900b4 | underdog | Michael Salgado-Medina | FG Made | over | 0.11962802201761302 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|dd1d9caa-101d-491b-badf-bb1b87735495 | underdog | Jonathan Taylor | Receptions | under | 0.1194495485112097 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|b9a30083-4e27-4adb-bed7-b117feee5e5b | underdog | Davis Allen | Receiving Yards | under | 0.11926942043123134 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|48551e6e-707c-45df-bd3c-bd742dd16fc2 | underdog | Evan Stewart | Receptions | over | 0.1188898847151112 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| prizepicks|16941218 | prizepicks | Nico Collins | Rec Targets | under | 0.11882558222332162 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7d1eec2d-0448-4b94-b456-6922f66904df | underdog | Konata Mumpfield | Receiving Yards | under | 0.1188198417781472 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|5c14d724-6efd-4d24-a166-10baae0084d6 | underdog | Will Kacmarek | Receiving Yards | over | 0.11880052183859213 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|941cffba-4b42-4435-8769-a31cbd72dc50 | underdog | Tee Higgins | Receptions | under | 0.11877140010710996 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|fb0d5259-4127-471f-bcb2-d7a032b83cd4 | underdog | Jabree Coleman | Rush Yards | under | 0.11871348405852322 | 2026-11-14T11:31:26Z | 2026-11-15T00:45:00Z |
| underdog|4f27780f-bd9a-4e60-abfd-2eb01d96db19 | underdog | Anthony Colandrea | Total TDs | under | 0.11854315253801861 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|bf204c41-dc6c-45e7-ac59-b29e8b440e59 | underdog | Adonai Mitchell | Receptions | under | 0.11812295339085888 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|c8dd15d3-4419-45ae-a884-55bd1290a78f | underdog | Garrett Wilson | Receptions | under | 0.11792466411828051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16942023 | prizepicks | Greg Dulcich | Rec Targets | under | 0.11772120696406463 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c7c1feb1-0d59-4f4b-a9e9-7f9535f0df33 | underdog | Drew Mestemaker | Pass TDs | under | 0.11768525797870777 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|471b086b-8e30-4b89-8030-a31f346304fa | underdog | Bryce Young | Rush Yards | under | 0.11671082433541491 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16934020 | prizepicks | Aiden Flora | Rush Atts | under | 0.11622830763827319 | 2026-11-13T12:14:20Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|3614f11e-aa5b-4d51-9032-b3f195f419d5 | underdog | Jacobo Echeverria Lozano | XP Made | over | 0.1161780296945728 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|25d08474-3b4e-4586-bb57-ffc039de6e0e | underdog | Jordan Faison | Receptions | under | 0.11525488006273821 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|2420a1ae-3693-4c18-900e-a72641811872 | underdog | David Olano | FG Made | over | 0.11523648181086699 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| underdog|0a2342d7-fcd4-483d-811f-a38bd3ae4e17 | underdog | Gunnar Helm | Receiving Yards | under | 0.1150408506569418 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|9d897071-10ba-4671-9026-daa82f8482de | underdog | Jordan Shipp | Receiving Yards | under | 0.1148852323657562 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|d7f547b3-eadc-47d6-bf0a-4b53c60eedbf | underdog | Jonathan Taylor | Rush Yards | under | 0.11473469611979015 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|d43d3773-e882-455c-9611-324394a81f00 | underdog | Alim McNeill | Sacks | over | 0.11465860629992497 | 2026-11-14T11:31:26Z | 2026-11-15T14:30:00Z |
| underdog|4980e13b-b332-4cb3-b311-c8aada8c0159 | underdog | Kyle Pitts | Receptions | under | 0.11437219464215653 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|62113192-42d6-46c2-88b8-8fee013c0f3c | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.11359016998477156 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|5c625434-b11a-46c4-a6af-d0fc53c2f2a9 | underdog | Dak Prescott | Pass TDs | under | 0.11340998483490083 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|20ebc7f0-08e7-425c-99e6-1af2fd35d3fb | underdog | Dierre Hill | Receptions | over | 0.11330426194714777 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|7a6dd424-2fdc-466c-b847-16a47251614c | underdog | Connor Calvert | FG Made | over | 0.11328783871436227 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|7857c427-00ea-44f3-9c45-48f9e7f2c9b5 | underdog | Trevor Lawrence | Pass TDs | under | 0.11317375136374375 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|865ea4d0-9767-4b60-8c93-3d426d51d7a8 | underdog | Breece Hall | Rush Yards | under | 0.11314740643781795 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|2f0eb7c1-de78-4fe0-962d-72826e5d0d6f | underdog | Malik Washington | Receiving Yards | under | 0.11299206031990372 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|e47c2cc1-06cd-4da0-b694-f464ce24ea03 | underdog | Gunnar Helm | Receptions | under | 0.11286581357252512 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|2d0249ee-b511-4b0d-bdd1-0ad34ded2758 | underdog | Khalil Herbert | Receiving Yards | over | 0.11264275449455008 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d30c2651-ff31-4115-a5e9-3e40d4bc947f | underdog | Ryan Hopkins | Pass Yards | under | 0.1125057528061264 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|fcacd7b2-73fd-4c47-be91-f94adbc7fc22 | underdog | Jordan Onovughe | Receiving Yards | over | 0.1124377498067648 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|9861fb0a-1a44-4119-9006-6e9c7ea976cd | underdog | Cole Tabb | Receiving Yards | over | 0.11223545456037964 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|c521d73c-2a75-4a75-9c17-33b2205da002 | underdog | Rico Dowdle | Rush Yards | under | 0.11217901116890283 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|992fa67a-feec-4626-95dc-f2c04f2580cf | underdog | Matthew Stafford | Rush Yards | over | 0.11213733898109268 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|461f158a-b95d-4759-b48d-ca72ea246c1d | underdog | Jadarian Price | Receptions | under | 0.1116533229738974 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|91b1977e-d8e7-4457-b5ad-9586bf490e61 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.11163096056620292 | 2026-11-14T11:31:26Z | 2026-11-15T14:30:00Z |
| underdog|b54e3236-2070-4997-8320-39153255594b | underdog | Elic Ayomanor | Receptions | under | 0.11160954349764363 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5db956f1-b511-4050-a6b4-671177d5b7ee | underdog | Max Gilbert | FG Made | over | 0.11156379694782498 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| prizepicks|16941190 | prizepicks | Zay Flowers | Rec Targets | under | 0.1114495281356832 | 2026-11-13T12:14:20Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|3b01acf2-eefa-4496-a642-bf1c849db45d | underdog | Chris Bell | Receptions | under | 0.11116746721824522 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|adac7521-6111-4d97-b45a-c14c5cfdc224 | underdog | Derek Eusebio | Receptions | over | 0.11051004649755991 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|0c2c33b6-1936-40fb-bd23-2bd9de48b5e4 | underdog | George Pickens | Receptions | under | 0.11023621755123203 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|795d3d4c-63e3-48ec-97fb-8e15739dcc5b | underdog | T.J. Watt | Sacks | over | 0.11016378684724581 | 2026-11-14T11:31:26Z | 2026-11-16T01:20:00Z |
| underdog|611d5095-8649-470d-aad5-f9b1d3f8f85c | underdog | David Olano | XP Made | over | 0.11008098092875374 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| prizepicks|16870373 | prizepicks | Brock Bowers | Rec Targets | under | 0.10995797661937423 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|4291930c-2315-4596-8a5b-40abfdbeb026 | underdog | Chris Rodriguez | Receptions | under | 0.10885395637178386 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|f9eb0efb-93f0-4af4-a0bc-eb87572cd5e6 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.10859750013353275 | 2026-11-13T19:43:07Z | 2026-11-16T01:20:00Z |
| underdog|6822a773-5f4b-457d-a3c1-4ba92bff9865 | underdog | Junior Sherrill | Receptions | under | 0.10806956997685557 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|fd21faaf-bffa-4216-93db-e8f524c4e0f0 | underdog | Gianni Spetic | FG Made | over | 0.10755910381656675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| prizepicks|16897138 | prizepicks | Thomas Castellanos | Rush Atts | under | 0.10724354939051584 | 2026-11-12T07:07:56Z | 2026-11-14T21:30:00.000-05:00 |
| prizepicks|16942015 | prizepicks | Colby Parkinson | Rec Targets | under | 0.1069695868003464 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|4bd23df4-deb5-49bc-8c4b-86a313802ac5 | underdog | Mason Taylor | Receptions | under | 0.10673294964450386 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|ea72a765-c2a4-45fa-8d1c-4ed978abad0e | underdog | Chase Brown | Rush Yards | under | 0.10663476696726415 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|dc68a8d2-c3d7-43aa-8781-fe8a9f804595 | underdog | Elic Ayomanor | Receiving Yards | under | 0.10614450873436487 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|02dfa4d1-6864-4a3b-a333-800bb999bca2 | underdog | Kirk Cousins | Pass TDs | over | 0.10613134956836634 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0eaa92de-0816-4aff-85fc-7ef1239b1b37 | underdog | Michael Salgado-Medina | XP Made | over | 0.10593010970338057 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|325a8205-94f4-4430-8e00-d9d2ddc2a9ec | underdog | Mike Gesicki | Receptions | under | 0.10565045023732611 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|5dbfa23a-c4c1-4093-9622-d1d13476af6e | underdog | Chris Rodriguez | Rush Yards | under | 0.10550815408845216 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|ee19d5c8-bb25-43c9-8e93-ac1b2e8e0ad7 | underdog | Tyler Higbee | Receptions | under | 0.10523114864570438 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|480d1861-82b8-409d-bb49-477bddb38ae9 | underdog | Ed Oliver | Sacks | under | 0.10489262572682079 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|8428654c-c063-43d0-9f73-6596ad9246bd | underdog | Cameron Thomas | Sacks | over | 0.10486694263301588 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|a17384e1-9dfb-481a-855d-f46311d458a4 | underdog | Jekail Middlebrook | Rush Yards | under | 0.10476970716253864 | 2026-11-14T11:31:26Z | 2026-11-14T20:30:00Z |
| underdog|d38110fb-9347-4b11-a6e3-60bd2e87c040 | underdog | Khalil Shakir | Receiving Yards | under | 0.1045700477965894 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|32929e6f-aaa0-4762-a1f0-7200275873c2 | underdog | Wan'Dale Robinson | Receptions | under | 0.10441558917928029 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|0ff862cd-b707-4128-b7b5-1837380bc39e | underdog | Davis Allen | Receptions | under | 0.10399951412686148 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|9b902c48-bdaf-41d6-a2bc-2a1798df028c | underdog | Matt Gay | Kicking Points | over | 0.10370064668973422 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|5c74ecd3-760e-44dd-ab4a-274411af2d38 | underdog | Brandon Phelps | Receptions | over | 0.10365026556823337 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|077e30e4-9320-449b-a228-b1b97a8abd83 | underdog | Trey Smack | FG Made | under | 0.10289090955929303 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|846092aa-807d-43c4-80cd-af7dc9c3234b | underdog | Breece Hall | Receptions | under | 0.10276383668301403 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1bc7f79c-1245-49cc-b9b1-d570df008d5e | underdog | Maxx Crosby | Sacks | over | 0.10266892373716213 | 2026-11-14T11:31:26Z | 2026-11-15T21:05:00Z |
| underdog|e10888ed-ae51-49a0-ab78-3a968b873283 | underdog | Matthew Stafford | Pass Attempts | under | 0.10236489378726288 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c023c117-72dd-4dad-a61d-6a7b030f473d | underdog | DeSean Bishop | Rush Yards | under | 0.10219630920024292 | 2026-11-14T01:00:02Z | 2026-11-14T20:00:00Z |
| underdog|b58d4951-3cf7-4235-9f2b-f9836e774dae | underdog | Drake London | Receiving Yards | under | 0.1020493545084814 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|51820dd7-063c-4751-be38-84c9a6983fed | underdog | Christian McCaffrey | Receptions | under | 0.1016183424097532 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| prizepicks|16942021 | prizepicks | Caleb Douglas | Rec Targets | under | 0.1016082162097357 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|ebba22ce-6173-4b6e-b454-1df66a084a08 | underdog | Tyler Higbee | Receiving Yards | under | 0.10146410288215946 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|dd69b512-b698-428c-bd34-5a8e020ae6e3 | underdog | Tyler Bass | FG Made | under | 0.10117399188091525 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|100a4397-7582-4aa4-88f2-2c64bab4f3dd | underdog | Carlos Hernandez | Receptions | under | 0.10082058286217788 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|a25cd0ac-21c0-40d4-8f36-e6947567727d | underdog | Keenan Allen | Receiving Yards | over | 0.10008531629473594 | 2026-11-14T11:31:26Z | 2026-11-15T21:25:00Z |
| underdog|07a861fe-fc13-4bc3-899d-3e0b2a9e97fa | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.09905894288660622 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|33f52d98-d59c-4fe7-b20b-721acf881e4a | underdog | DJ Wonnum | Sacks | over | 0.0985839204264004 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|ffdf6928-c765-4901-bcf9-925978a42dfd | underdog | Jacoby Brissett | Pass Attempts | under | 0.09857496516557318 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|884fdc4f-47dc-4b69-af82-a384ad40965d | underdog | Kevin Coleman | Receiving Yards | under | 0.098453690351202 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|d60524c1-1768-41c7-a15d-2b08d4a7634c | underdog | Yamir Knight | Receptions | under | 0.09843093501159006 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|6f6e76ef-69e3-4315-83cb-ea6ec48daea1 | underdog | Chad Ryland | FG Made | over | 0.09807717467815241 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|5f95b22a-44d2-4c89-b35c-17c275ad8b09 | underdog | Gunner Stockton | Pass Yards | under | 0.09783371432939425 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|89777911-6168-4f57-8662-8d3f09ac1716 | underdog | Chris Boswell | FG Made | under | 0.09775400624264463 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|1dd0a184-61eb-43bf-8524-7b3978d5f9d6 | underdog | Alessio Milivojevic | Pass Yards | under | 0.09772997245008974 | 2026-11-14T01:00:02Z | 2026-11-14T21:15:00Z |
| underdog|954ad452-8bec-4840-bae5-048bcd6542d9 | underdog | Mitchell Evans | Receiving Yards | over | 0.09733725531537551 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|60b53d65-8a25-4ccb-b063-ef5c0f84afa7 | underdog | Thomas Castellanos | Rush Yards | under | 0.09664126615633595 | 2026-11-13T19:43:07Z | 2026-11-15T02:30:00Z |
| underdog|7d1b7f21-aa87-4f17-bf44-77c18f015227 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.09657686894256146 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|506821c8-a453-4a20-a85b-f97bfaa4e1fe | underdog | Zay Flowers | Receiving Yards | under | 0.09632328774235666 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0e196ee8-4db3-4fce-a18c-a14e74e12905 | underdog | Marcel Reed | Pass TDs | under | 0.09624315580046416 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|c3d405f2-f65d-4f28-9dab-86ac43a8d975 | underdog | Kenneth Walker III | Receptions | under | 0.0960980842757887 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|8ef9ae68-5181-46e4-b083-fe1c2dc728cc | underdog | Cardae Mack | Rush Yards | under | 0.09591445564927736 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|5d124f4c-22e7-4e63-aabe-d97f5d3a856e | underdog | Jakobi Meyers | Receptions | under | 0.09590453564859014 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|4dd1c032-49a9-4847-8314-d8ddb529ceae | underdog | KC Concepcion | Receiving Yards | under | 0.09574048321212925 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|46106a69-9bb4-4888-afc9-0dcbb0871db6 | underdog | Yannick Smith | Receptions | under | 0.09569703206960045 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|0e7ba887-a4fc-4178-a476-293a2ad6d3d8 | underdog | Travis Kelce | Receiving Yards | under | 0.09560697982090594 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|382be9ea-4cd8-4981-9243-ba13a3e9bca4 | underdog | Evan McPherson | Kicking Points | under | 0.09540198598918959 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|45ea8cf2-2e66-4230-a4fe-1bc4be7cfbd4 | underdog | Jaylen Raynor | Pass Yards | under | 0.09539041220737754 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|559bf06c-4552-47fe-915f-f700662d0a10 | underdog | Elijah Ponder | Sacks | over | 0.09496877075018534 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| prizepicks|16964065 | prizepicks | Elizabeth Mandlik | Total Games Won | over | 0.09466430448407948 | 2026-11-14T01:00:02Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|d2cdc210-fcc2-4276-9810-a70ee7020fdd | underdog | Bear Bachmeier | Pass Yards | under | 0.09458764346729465 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|1d37f459-f6d1-4307-99ec-bf177e3a6437 | underdog | Jason Sanders | FG Made | over | 0.09433045418762181 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fa4c7f93-3a59-4d24-a659-ab3a46d49e2b | underdog | Greg Dulcich | Receiving Yards | under | 0.09403894171268923 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|2ab602db-837a-4c6d-baf3-4ae491410bb2 | underdog | Josh Cuevas | Receiving Yards | over | 0.09390233366912559 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|f25cc4b1-d05b-4650-aa6c-9a9a1304580d | underdog | Rashid Shaheed | Receptions | under | 0.09383692899756757 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|60aaccb5-940f-4bc2-a9c2-5cd432a930b3 | underdog | Kenny Minchey | Pass Yards | under | 0.09378357249772407 | 2026-11-13T01:09:17Z | 2026-11-14T23:15:00Z |
| underdog|5c500fd7-4b60-43bf-9f00-634ec5ecfade | underdog | Josh Cuevas | Receptions | under | 0.09376007412754472 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|3d42fad4-14d1-4b6c-a87e-74f9a36ad66e | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.09346265131080267 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|abf6366a-98c0-4dca-a13b-5a0221de2afa | underdog | Trinidad Chambliss | Pass TDs | over | 0.09346167782668713 | 2026-11-11T22:47:13Z | 2026-11-14T21:15:00Z |
| underdog|069fa2d9-31cb-47ed-8437-b104c094f8fd | underdog | Byron Murphy | Sacks | over | 0.09314895490640263 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| underdog|f51c8941-84b9-4662-a1b2-dbb0c6b4e70d | underdog | CeeDee Lamb | Receiving Yards | under | 0.09269504099383397 | 2026-11-13T12:14:20Z | 2026-11-15T21:25:00Z |
| underdog|ae5450f4-879d-43e7-9896-44a93fb15d07 | underdog | Alessio Milivojevic | Pass TDs | under | 0.092497836794454 | 2026-11-13T01:09:17Z | 2026-11-14T21:15:00Z |
| underdog|f8f6356d-592e-4e3a-8d8b-6bfaa2874eef | underdog | Luke Fahey | Pass Yards | under | 0.09241833281916434 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| prizepicks|16864060 | prizepicks | Luke Farrell | Rec Yards | over | 0.0923962774082826 | 2026-11-11T06:09:33Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|24069c30-baca-4e53-9ced-30b0924548c3 | underdog | Sam LaPorta | Receiving Yards | under | 0.09218552607862607 | 2026-11-14T11:31:26Z | 2026-11-15T14:30:00Z |
| underdog|147243e6-fcee-4814-8b0f-73b49c924682 | underdog | Chris Olave | Receiving Yards | under | 0.09207479159828746 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|1459bce9-c246-4bcf-a79d-d9ee9ad81e61 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.09121419257612451 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|2a476ca9-7776-4f76-8971-c059647a2ee4 | underdog | Noah Fifita | Pass Yards | under | 0.09119247396933716 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|7ad20c2e-12ce-48dd-a775-79afd0935448 | underdog | Ryan Flournoy | Receptions | under | 0.09118425740313918 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|7aa6308c-d5e6-4a77-a069-483e31e47c22 | underdog | Willie Rodriguez | Receptions | under | 0.09080568724128812 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|cde77409-6c4b-4d8e-9073-074e686e1b6d | underdog | Cam Little | Kicking Points | under | 0.09049138686982805 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9fb20b9b-e4a4-4996-93b2-6f7f98f44641 | underdog | Mazeo Bennett | Receiving Yards | under | 0.09044506367074556 | 2026-11-13T19:43:07Z | 2026-11-15T00:45:00Z |
| underdog|15a63108-d724-478f-bfec-d81588b2c0f9 | underdog | Davion Gause | Receiving Yards | over | 0.09035519428718453 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| prizepicks|16834826 | prizepicks | DK Metcalf | Rec Yards | under | 0.09020306892719043 | 2026-11-10T12:33:48Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16941175 | prizepicks | Elijah Higgins | Rec Targets | under | 0.09009803240688008 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16942047 | prizepicks | Deebo Samuel Sr. | Rec Targets | under | 0.08983159220469517 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|0b15b928-adf6-4ddf-9f3b-acc5f9337db2 | underdog | Tyler Morris | Receiving Yards | over | 0.08926741515006886 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|f62cef0d-51f0-4d95-8e29-efa118a3c0be | underdog | Jaron-Keawe Sagapolutele | Pass TDs | over | 0.0892547976787258 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|cd0d7bef-42c3-4166-8982-bffd31d29f48 | underdog | Jamal Polite | Receptions | under | 0.08917605205192325 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|b4dc21f0-573a-4f25-812a-4eb8b58e4cda | underdog | Sedrick Alexander | Receiving Yards | over | 0.08901436844664978 | 2026-11-14T01:00:02Z | 2026-11-14T17:45:00Z |
| underdog|2ba1ff16-4919-49f3-8e39-492f6a8ca8d9 | underdog | Jeremiah Smith | Receptions | under | 0.08888656887837354 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|d697c338-a9ac-4d14-9b59-eaeebed9290d | underdog | Tank Dell | Receiving Yards | under | 0.08877048715423952 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|83338a1b-fbf4-4bf4-9849-801fec3812ae | underdog | Maason Smith | Sacks | over | 0.08846634355920002 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16897183 | prizepicks | Caleb Hawkins | Rush Atts | under | 0.08801035811918012 | 2026-11-13T12:14:20Z | 2026-11-14T21:30:00.000-05:00 |
| underdog|f9fc5b80-57fb-4d48-b0d6-01920f66516f | underdog | Rece Verhoff | FG Made | under | 0.08797576918997374 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|c9ea280a-ee38-45c6-9752-6d41fb2d3a28 | underdog | Travis Etienne Jr. | Rush Yards | under | 0.08792913192238727 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|9426ff07-fa03-43aa-b1c8-4ef2c985c88a | underdog | Lincoln Kienholz | Total TDs | under | 0.08780993604674592 | 2026-11-14T01:00:02Z | 2026-11-15T00:00:00Z |
| underdog|9ea2bc5d-65cf-4749-b4f2-ef74fea29512 | underdog | Arch Manning | Pass Yards | under | 0.0878083317921382 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|bddc04c9-fa19-4fa9-9acd-4b5e79f22d35 | underdog | Gavin Freeman | Receptions | under | 0.0876925176274097 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|7b9cbde9-983a-4d99-84fd-1e3dd0ea2c7f | underdog | Tre Tucker | Receiving Yards | over | 0.0875329970402473 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| prizepicks|16942042 | prizepicks | Germie Bernard | Rec Targets | under | 0.08682541820520961 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863709 | prizepicks | Germie Bernard | Rec Targets | under | 0.0868140274679029 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16834650 | prizepicks | Derrick Henry | Rush Yards | under | 0.08663217446763538 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|85c5a6a7-9a80-49fb-8f65-d7395e5c820b | underdog | KJ Jackson | Pass Yards | under | 0.08639422665538965 | 2026-11-14T11:31:26Z | 2026-11-15T00:45:00Z |
| underdog|0bfc6753-5f10-4e6f-9e3c-1785134a300d | underdog | Hank Brown | Pass TDs | under | 0.08611303327074238 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|828da51d-e687-4454-826f-bb1788d4eaeb | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.08597941891790728 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|7271a380-a961-4101-afbb-6871fdf84491 | underdog | Hunter Henry | Receiving Yards | under | 0.08579727034280116 | 2026-11-13T01:09:17Z | 2026-11-15T14:30:00Z |
| underdog|a0f28536-1ea4-460f-8056-53d93cf15ad8 | underdog | Dani Dennis-Sutton | Sacks | over | 0.08579135002694815 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|a091089e-dd58-45a1-b765-be78d0773ad4 | underdog | Victor Snow | Receptions | under | 0.08565875184490346 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|ce40b1e3-6ba5-4007-ac4f-42a31ede3e70 | underdog | DK Metcalf | Receptions | under | 0.08562083210511395 | 2026-11-13T19:43:07Z | 2026-11-16T01:20:00Z |
| underdog|ed941213-5d9f-43da-8049-26850111140c | underdog | Jacob Martin | Sacks | over | 0.0855163088372517 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16941181 | prizepicks | Jahan Dotson | Rec Targets | under | 0.08499685770574694 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|fe742815-78d4-49a8-89d4-b09df9d494f8 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.08495752665294976 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|2e347a2b-8cd6-4dee-b05e-a080b7eb5f86 | underdog | Elija Lofton | Receiving Yards | under | 0.08489231076511361 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|2241dc3b-3cce-4713-948a-899c19938a90 | underdog | Bhayshul Tuten | Receptions | under | 0.08488347843269772 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ab688298-7ac6-4998-bad8-ed8a0d01a1f4 | underdog | Konata Mumpfield | Receptions | under | 0.0847625992849359 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|81732dfb-43f2-47d9-8dc5-71d52ed63b8f | underdog | Javonte Williams | Rush + Rec Yards | under | 0.08435809140682626 | 2026-11-14T11:31:26Z | 2026-11-15T21:25:00Z |
| underdog|a9e7114f-4108-43da-97c7-bbe34afcbd6a | underdog | George MacIntyre | Pass Yards | under | 0.08432128549331452 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|095d7662-7876-4544-a661-85a9352bc8b9 | underdog | Darnell Washington | Receptions | under | 0.08429478520005662 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b59cb19d-8acc-407f-8dca-326a375b33eb | underdog | Tory Horton | Receiving Yards | over | 0.08418990069868826 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|6a800e8e-f81b-4bdb-9cee-fc7e90da63ae | underdog | Chuba Hubbard | Receptions | under | 0.08408782592218833 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|37738fae-4753-4e52-b227-99303a546958 | underdog | Caleb Hawkins | Rush Yards | under | 0.0840529047691323 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|2d6f2c26-3679-4462-b5f9-154fdf837d9a | underdog | Malik Washington | Receptions | under | 0.08380896020559803 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e4971822-0afb-4f50-93e5-4d1c7bd2e60c | underdog | Brian Thomas | Receptions | under | 0.08369582901305839 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|02d0bf59-fe34-4a76-a5bd-52ac1f684313 | underdog | Aidan Hutchinson | Sacks | under | 0.08362257452078503 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|30b534aa-3c8d-4e2a-8532-7046212f8423 | underdog | Keon Coleman | Receptions | over | 0.08351427326810018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|a54894a8-267b-4f00-88c5-65848dbe7540 | underdog | Eli Raridon | Receiving Yards | under | 0.08335423153287636 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|6d5c6e7a-9c71-4fd6-a60a-58523488f46f | underdog | Davis Warren | Pass Yards | under | 0.08292817370928895 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|eb6f844d-c01c-40e4-944e-3bd676bbd3dd | underdog | Tyjae Spears | Rush + Rec Yards | under | 0.08262861804974997 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|3e97264b-43a4-4255-b36f-62d65129f73f | underdog | Abu Sama | Rush Yards | under | 0.08254754810512499 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|a4aacc18-8ae5-4a08-85e4-0daa174b895b | underdog | Ahmad Miller | Rush Yards | under | 0.08199664123801942 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| prizepicks|16942017 | prizepicks | Konata Mumpfield | Rec Targets | under | 0.08195824652932926 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|c7c56531-74f0-4853-a9ed-870ad465ba64 | underdog | Tony Pollard | Receiving Yards | under | 0.08175200743705435 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|1c822beb-341f-4ef6-91e5-340df5d45d2e | underdog | Quinshon Judkins | Rush Yards | under | 0.08150218705697565 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|b4b14665-4501-496c-8be0-d530e6e1fbe5 | underdog | CeeDee Lamb | Receptions | under | 0.08142420706840037 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|f13d3a38-efe0-4a4f-bd87-12789e5c030b | underdog | Kayshon Boutte | Receptions | under | 0.08140187278468214 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|6c43a856-171c-43d0-a1dc-2c607f84dc04 | underdog | Javarius Green | Receptions | under | 0.08130193150872367 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|3a2140cc-34ac-432c-a338-20fc5d386a93 | underdog | Anthony Colandrea | Pass TDs | under | 0.0812395078517486 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| prizepicks|16942053 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.08114388361716462 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|879eaed1-2f48-4ebf-82ba-fffcc451343a | underdog | Pat Freiermuth | Receptions | under | 0.08099921416069444 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0948aa96-7ab1-4a01-8009-90f637fe281c | underdog | Walker Eget | Pass TDs | under | 0.08075629229645986 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| prizepicks|16834642 | prizepicks | Jonathan Taylor | Rush Yards | under | 0.08067797097966689 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|64d055b3-3192-41e1-a6e4-9b0938aef0d8 | underdog | Jeffrey Overton | Rush Yards | under | 0.08054528171123199 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|bd5637b7-25ee-4c3a-8711-293b1146d1b8 | underdog | Darian Mensah | Pass TDs | over | 0.08051796634389519 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|c4e5cef0-a68c-4f30-8bf1-e0db1f36c83b | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08046760762807637 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|dde71d32-70c4-401c-a3f3-0b410cc86777 | underdog | Jaylon Domingeaux | Receptions | over | 0.0803550329807054 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|23238e4a-a453-48b3-888b-37d8d5c24a0e | underdog | Caleb Douglas | Receiving Yards | under | 0.08033066710225367 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|67d69720-f75a-4a58-8666-e3e822ae68f8 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.08006957549511673 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|5e94977c-0093-48e8-becf-5e8910977a9b | underdog | Drake Maye | Rush Yards | under | 0.08004423976338015 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|695e2bf1-9362-4222-8c11-1c0b79b3279a | underdog | Trae'shawn Brown | Rush Yards | under | 0.07990006308548003 | 2026-11-14T11:31:26Z | 2026-11-14T17:45:00Z |
| underdog|6751175c-ff62-4777-924f-e7d17832e931 | underdog | Aiden Flora | Receiving Yards | over | 0.07986935749827329 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|950859b7-8ce4-4a6c-be8f-ece3e3fcdac6 | underdog | Seth McGowan | Rush Yards | under | 0.07978214294232122 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|0b2e9d13-d865-4ce4-8130-1811f8c75f1f | underdog | Jahmyr Gibbs | Receptions | under | 0.07974674760702072 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|28b73f9a-7464-4028-9994-b3e9777c631e | underdog | Juwan Johnson | Receptions | under | 0.07927138801736044 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2063a4a7-dfda-48db-b7cf-8db794e23b5a | underdog | Jaleel Skinner | Receptions | over | 0.07909948837131958 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|aec9f942-d44c-43ee-8847-b10728935f0d | underdog | Omarion Hampton | Receptions | over | 0.0790537300117724 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|5ff9624f-b7fe-4fc3-996a-59bb559a859d | underdog | Carl Granderson | Sacks | over | 0.0790173896789027 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|fcf60ef4-6d8a-4e5f-a5dc-ab09c139b1d7 | underdog | Olamide Zaccheaus | Receptions | under | 0.07875857917335316 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|8450e859-24f2-4721-9b6d-6aceb59b963a | underdog | Aaron Rodgers | Pass TDs | under | 0.07874658502524756 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|074b105f-1cfb-46eb-9d6c-f0bd8169e682 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.07864420027085584 | 2026-11-14T11:31:26Z | 2026-11-15T14:30:00Z |
| underdog|e783dc26-5825-408b-ba88-074ae8338f79 | underdog | Tyler Allgeier | Receptions | under | 0.07858479788991879 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16942030 | prizepicks | Chris Olave | Rec Targets | under | 0.07835608420773721 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|cbfc5710-542d-4425-a392-fc71c2d6b92a | underdog | Tyjae Spears | Receiving Yards | under | 0.07831100791175316 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|7802a2ce-f30a-457a-9eee-18da61262d1f | underdog | Fluff Bothwell | Rush Yards | under | 0.07802002745995362 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|238f90cc-3081-4edd-a3bb-d45650cbeb1c | underdog | Jamal Rule | Rush Yards | under | 0.07795938913876044 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| underdog|45d15fb5-1a6e-4a54-8963-4071dd6b2094 | underdog | Xavier Hutchinson | Receiving Yards | under | 0.07756880311663261 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16906374 | prizepicks | Ryan Hopkins | Pass Comp | under | 0.07753883763235836 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|422a000f-61d0-4476-a9ec-ab1ab6858642 | underdog | Calvin Ridley | Receiving Yards | under | 0.07733632883781583 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|b6f11e09-9689-4381-b880-65db73f14005 | underdog | Omarion Hampton | Receiving Yards | over | 0.07729965562532948 | 2026-11-13T12:14:20Z | 2026-11-17T01:15:00Z |
| underdog|e7f1bbea-2d7b-4c56-8e47-9e0b571c984f | underdog | Will Bettridge | FG Made | over | 0.07725741826529164 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|6f83a6e1-af08-4769-9124-29211f046a50 | underdog | Eli Raridon | Receptions | under | 0.0772421213134098 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|943b6125-955d-4c4e-a9cb-d4c65e6b426a | underdog | Aaron Rodgers | Rush Yards | over | 0.07712631679230819 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|18e1b2b8-d6db-474b-bbfb-ab7200988bd2 | underdog | LaNorris Sellers | Pass Yards | under | 0.07690782897298154 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|b60a1138-01f1-4292-b874-5acaf191af21 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.0767893063215298 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ff324564-0cfe-4e6b-8b13-98e37a82443f | underdog | Trey Butkowski | FG Made | over | 0.07662906801843594 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|7c1c2185-4ab7-48fe-81d4-d3b445978529 | underdog | Deone Walker | Sacks | over | 0.07657290086413776 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|2f3c01e8-56f2-4972-80d6-96a7c641e276 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.07651862763115314 | 2026-11-11T16:13:16Z | 2026-11-15T14:30:00Z |
| underdog|693f5fff-95ff-4e29-b913-be01aef304c7 | underdog | Savion Williams | Receiving Yards | under | 0.0763692412291278 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9afc918c-33f0-4d49-94c8-ae1c1087877a | underdog | London Humphreys | Receiving Yards | over | 0.07632980997810002 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|7ae4a121-284c-43db-86e2-7f31858b44a6 | underdog | Devon Dampier | Pass TDs | over | 0.07622647992486625 | 2026-11-14T11:31:26Z | 2026-11-15T03:30:00Z |
| underdog|93f57aed-6f22-4917-bbcd-a64859bd454f | underdog | KC Concepcion | Receptions | under | 0.07613263220312116 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|6ba2b1ae-03c1-4871-a293-9f020b838ef7 | underdog | Ryan Flournoy | Receiving Yards | under | 0.07576743796346319 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|921893b1-e130-4cc1-9e68-fae07083d8d6 | underdog | Tee Higgins | Receiving Yards | under | 0.07552956056808402 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|404cd02b-e2fd-478c-939f-ed1fbd564d3b | underdog | Dallas Turner | Sacks | over | 0.07550932402426869 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|81ff0621-4501-4f89-a90c-53b654828353 | underdog | Tucker Kraft | Receptions | under | 0.07531614878084558 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|5e509b77-232b-42d0-9461-5701bd8ae7a0 | underdog | Samaje Perine | Receiving Yards | over | 0.07517445268493195 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| underdog|38dc032f-4dc3-4bbc-bdb9-65f92b70964b | underdog | Trey'Dez Green | Receptions | under | 0.07508204181081723 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|4dfa0157-e1a7-41c5-98a2-53df06995587 | underdog | Brendan Baird | FG Made | under | 0.07501720483065888 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|0c1b8205-16c9-4bba-b677-32477bbf7cc6 | underdog | Aaron Jones | Receptions | under | 0.07498021252064768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|1453952e-59e2-4974-8658-e2590a469b1a | underdog | Terrance Carter | Receiving Yards | under | 0.0749423255246151 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|c80985d0-c9a8-4234-bacf-2457a77a7bd7 | underdog | J'Koby Williams | Rush Yards | under | 0.07474999394891191 | 2026-11-14T11:31:26Z | 2026-11-15T02:30:00Z |
| prizepicks|16941206 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.07461924310815837 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|e5206727-9425-4770-9044-4cb63c605a87 | underdog | AJ Surace | Pass Yards | under | 0.07437064016573691 | 2026-11-14T11:31:26Z | 2026-11-14T17:30:00Z |
| underdog|904b626c-0df7-4bcd-8080-cd2438332c7d | underdog | Deshaun Watson | Rush Yards | under | 0.0743514519962496 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|0face381-0dda-47ae-87d2-1a514d02083f | underdog | Derick Hall | Sacks | over | 0.0743513887837684 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| underdog|0ead5f73-1af7-4129-934d-61b78bc77ba6 | underdog | Michael Mayer | Receiving Yards | over | 0.07434375727428089 | 2026-11-14T01:00:02Z | 2026-11-15T21:05:00Z |
| prizepicks|16941211 | prizepicks | Christian Watson | Rec Targets | under | 0.07423664668190944 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|1d790904-3e3a-490f-9135-fab5363ea396 | underdog | Chas Nimrod | Receiving Yards | under | 0.07407940070248409 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|9edb572c-69d9-4a52-8796-04709d52e154 | underdog | CJ Bailey | Pass Yards | under | 0.07381177137083061 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|afdebcd1-3ede-4ccc-ba8b-38bedf613be4 | underdog | Kaleb Johnson | Rush Yards | under | 0.0736939585523988 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16941196 | prizepicks | Khalil Shakir | Rec Targets | under | 0.0734283027956808 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|80d5b669-4608-4a70-af3d-0ca04f2a9ce7 | underdog | Braylon Staley | Receptions | under | 0.07334461051353225 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|1401b805-b55d-4f62-9585-45359cf41b66 | underdog | Patrick Mahomes | Pass TDs | under | 0.07319579691346556 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0219878f-a384-4c52-b453-7cb58a2e9b2e | underdog | Aiden Flora | Rush Yards | under | 0.07317872744288989 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|15895332-a1f7-4ca9-9f82-51abcab141d4 | underdog | Seth McGowan | Receiving Yards | under | 0.07317673931460811 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|06ae6764-4717-4fd0-90d4-cba7d420c077 | underdog | Sam Leavitt | Pass TDs | over | 0.07311759928344974 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|5aa07c5c-3160-4bf9-bae2-17272d017de0 | underdog | Tetairoa McMillan | Receptions | under | 0.07291530262227885 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16905549 | prizepicks | Junior Sherrill | Recs | under | 0.07284919195932371 | 2026-11-13T19:43:07Z | 2026-11-14T12:45:00.000-05:00 |
| underdog|66f485b9-79ff-40e5-9f8c-b3a017a71ac4 | underdog | Josh Cameron | Receiving Yards | over | 0.07284114427975696 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|34ac34e6-d4e0-4ba8-a22c-f5c6d9b0280e | underdog | Tate Sandell | XP Made | under | 0.07284107376327742 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|f65d31f8-6cb0-46ef-973a-612d369e3cc2 | underdog | Lukas Van Ness | Sacks | over | 0.0725672770341067 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|afe168bf-abfa-4e5a-9c00-b1163353af0c | underdog | JC French | Pass TDs | over | 0.07241472236418672 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|605e756f-5384-4f51-aaa4-87065f484fb2 | underdog | Josh Cameron | Receptions | under | 0.07232114240259424 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|a0cd60d1-929a-4503-848a-8b24dad869a7 | underdog | Dylan Raiola | Pass Yards | under | 0.07204706439513853 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|3e20733d-2633-4f87-8c7a-ed7ad6b9b4b4 | underdog | Omarion Miller | Receptions | under | 0.07201565002220278 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|185f6ccf-34b2-4aec-b3ed-0da447604658 | underdog | Jaden Craig | Pass TDs | under | 0.07162693975196976 | 2026-11-14T11:31:26Z | 2026-11-14T19:00:00Z |
| underdog|240f7fc4-1be7-4400-bec4-3267b3e68253 | underdog | Que'Sean Brown | Receptions | under | 0.07144334670879293 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|4f12966c-d622-4729-8744-09690d6f161b | underdog | Travis Hunter | Receptions | over | 0.07136780630701439 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|858c7d02-f1ef-43e2-ac44-a0e9447d8e99 | underdog | Tommy Tremble | Receptions | under | 0.07126105154425799 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d4d98b9c-0bbb-480c-841a-373f26ae1956 | underdog | Jalen Coker | Receiving Yards | under | 0.07123604540034678 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1c15e340-89ec-4fd0-8f03-d90347d5a00f | underdog | Jaelan Phillips | Sacks | over | 0.07118874602145048 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|c25edc7c-0902-46d8-922f-add8b4542118 | underdog | Ethan Grunkemeyer | Pass TDs | under | 0.07113280126479149 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|ce0fce9b-aa9c-4627-95f3-7606f345a845 | underdog | Braelon Allen | Receiving Yards | over | 0.07107039823732642 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| prizepicks|16941213 | prizepicks | Tucker Kraft | Rec Targets | under | 0.07104685444251368 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|38ce3da9-a49a-4722-ab23-66b1495ba0bf | underdog | George Karlaftis | Sacks | over | 0.07097474079793781 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|7a75e646-5664-41bf-83d2-fea36aea9458 | underdog | AJ Barner | Receiving Yards | under | 0.07075613788298196 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|02b04d2b-d9c6-462a-881c-7997aade422d | underdog | Maddux Madsen | Pass TDs | under | 0.07074102268170901 | 2026-11-14T01:00:02Z | 2026-11-14T23:00:00Z |
| underdog|23aff467-3c88-4829-ad32-2dc97e30d278 | underdog | Germie Bernard | Receptions | under | 0.07070199720871251 | 2026-11-13T01:09:17Z | 2026-11-16T01:20:00Z |
| prizepicks|16863705 | prizepicks | Jameson Williams | Rec Targets | under | 0.07067193012939765 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|e37df23a-0d1d-42fa-8896-7804c239608a | underdog | Dexter Lawrence II | Sacks | over | 0.07049843260181399 | 2026-11-14T01:00:02Z | 2026-11-16T01:20:00Z |
| underdog|96b084f0-e61e-4d6f-bbda-ee645d2f7d65 | underdog | Jason Myers | Kicking Points | under | 0.07035458570297104 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|aee32036-687d-4ec2-a7c3-5c4d0aefbe83 | underdog | Trinidad Chambliss | Pass Yards | under | 0.07011473675684232 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|f672db56-528f-4fdf-bee7-517fbdbbdd90 | underdog | Reed Harris | Receptions | under | 0.07003957469693012 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|32afa744-a7db-46b1-8166-59407c4e4dd5 | underdog | Nico Collins | Receptions | under | 0.06991731066614237 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8dc776e9-341d-424e-97a4-cb1076f15650 | underdog | Darren Waller | Receptions | under | 0.06987874258747295 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3a0a1923-9d00-45fe-b0ce-7f76d9913a34 | underdog | Darian Mensah | Rush Yards | over | 0.06986848826057779 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|444c96b4-dd42-4e64-ad97-df649c6ba1b8 | underdog | Ty Johnson | Receiving Yards | over | 0.06976628340678936 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|9a649d02-5b36-484a-b1d9-300c0e301768 | underdog | Louis Brown | Receiving Yards | over | 0.06972313817026754 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|ac4d8a30-9225-43c8-88e7-08dcda48c633 | underdog | Nick Marsh | Receptions | under | 0.06969050600733206 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| prizepicks|16941225 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.06952431849126628 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|8a8d5c32-6204-422b-9179-0f25635b1073 | underdog | Jared Curtis | Pass Yards | under | 0.06945686667553497 | 2026-11-13T19:43:07Z | 2026-11-14T17:45:00Z |
| underdog|9fb692ca-1ded-474d-ace1-e954d47e3038 | underdog | Isaac TeSlaa | Receptions | under | 0.06945554268955467 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|b0a672c0-cb8f-42ef-a549-777c38acf50e | underdog | Dylan Edwards | Rush Yards | under | 0.06929821317703688 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|d6bed32c-6469-4376-b942-1c62e7fcca52 | underdog | Ed Small | Receiving Yards | over | 0.06916360221981077 | 2026-11-14T01:00:02Z | 2026-11-14T19:00:00Z |
| underdog|395db1b5-e1c1-4364-b8b1-17c6cae3c3ae | underdog | Travis Etienne Jr. | Receptions | over | 0.06877349021471646 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|44222ca6-7319-4558-9011-4baebd4dae89 | underdog | Chris Olave | Receptions | under | 0.06860046597796887 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ab5a705a-6a78-49b7-bcfd-7321ae88e69f | underdog | Kaelon Black | Receptions | under | 0.0685332352021717 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|3180a1cb-17a9-4893-9c4a-e637dc9b5b79 | underdog | Jadeveon Clowney | Sacks | under | 0.0685226038595419 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|68035ddd-5482-40b4-81db-7d0d29f063a7 | underdog | Travis Etienne Jr. | Receiving Yards | over | 0.06849287642566915 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|2f9b9eb9-ccb3-4449-9821-4dee9cb0e528 | underdog | Nate Boerkircher | Receiving Yards | over | 0.06839844091264013 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|99789fe0-d70f-467d-a5d9-80f7d15c596f | underdog | Dylan Sampson | Receiving Yards | under | 0.0682011693134934 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| prizepicks|16863716 | prizepicks | Tee Higgins | Rec Targets | under | 0.06814305302582702 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|22ad2b9b-330b-4bfc-9757-469be69da523 | underdog | Nate Frazier | Rush Yards | under | 0.06804890307193212 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|cc687153-6c15-4213-8e26-4c90c7def680 | underdog | Jonathan Taylor | Receiving Yards | under | 0.06802934736360589 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|552f50d8-049b-4344-bb84-7fd20c840255 | underdog | Sheldon Rankins | Sacks | under | 0.06798385220723746 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|b7573824-7d88-45cc-8bc1-9e98836c986d | underdog | Bijan Robinson | Receiving Yards | under | 0.06782521035230094 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|71956dda-ddc8-47dc-bac8-44dc9a09728d | underdog | Bijan Robinson | Rush Yards | under | 0.06774159981403793 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|5a206c6b-3727-49de-9356-621b148d89cd | underdog | Willie Rodriguez | Receiving Yards | under | 0.06767701019989358 | 2026-11-13T19:43:07Z | 2026-11-14T23:15:00Z |
| underdog|8c3f7ac7-8d55-46f5-bfaf-3c7bade226bd | underdog | Bradley Chubb | Sacks | over | 0.0674375588981781 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|67bb66e0-36f8-4bfb-b364-8db821ce624f | underdog | Daylyn Upshaw | Receiving Yards | under | 0.0674153490159497 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|d45e0141-f94b-4e14-95d6-6dd2b6675be6 | underdog | Kevin Jennings | Pass Yards | under | 0.06718237102327551 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|5b012f70-be11-417d-97f5-9f719acc7d51 | underdog | Keenan Allen | Receptions | over | 0.06690700447395598 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| underdog|75d6f3fa-7734-49c4-9e25-90076e135660 | underdog | Darian Mensah | Pass Yards | under | 0.06666845712800784 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|11524372-bbae-47eb-abc7-77f03ee31c7a | underdog | Dawson Knox | Receptions | under | 0.06664316355524857 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16963993 | prizepicks | Bianca Andreescu | Total Games | over | 0.06662320386382004 | 2026-11-14T01:00:02Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|e3895608-8c85-4816-aad0-fe8098f92933 | underdog | Dawson Knox | Receiving Yards | under | 0.06643222901337464 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d0e501b4-73fa-4c8a-bf7f-e2f0a9c113cd | underdog | Jaden Craig | Pass Yards | under | 0.06641777156078443 | 2026-11-14T01:00:02Z | 2026-11-14T19:00:00Z |
| underdog|88469ae0-7923-439e-8ecd-83506eac545d | underdog | Charlie Becker | Receptions | under | 0.06609322679226748 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|97733708-ed62-42d6-891a-4827e8fe144e | underdog | Noah Gray | Receiving Yards | over | 0.06572912691694155 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f5596fdf-42d3-4466-abd8-87dc98e9fbc2 | underdog | Dylan Sampson | Rush Yards | under | 0.06544891409344189 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|da515c1a-034b-411b-b82c-3127ec88aece | underdog | Kenny Darby | Receptions | under | 0.06543754998000173 | 2026-11-14T01:00:02Z | 2026-11-14T23:15:00Z |
| prizepicks|16834811 | prizepicks | Jalen Coker | Rec Yards | under | 0.0652772475778256 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|74c0873e-371f-437e-9de3-77eacadb9d01 | underdog | Tony Livingston | Receiving Yards | over | 0.06517859139566806 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|d46b29bf-ff46-403d-973b-039233786244 | underdog | Victor Snow | Receiving Yards | under | 0.0650538655404348 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|d4150a17-b459-4876-b557-7ba5873c9026 | underdog | Barryn Sorrell | Sacks | over | 0.06498589556022877 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|8a5a2942-cbf3-4389-befa-f6325f90a1a2 | underdog | Tyler Warren | Receptions | under | 0.06494609926234585 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|27ba9d6a-0872-4d4b-80e2-4bcf6e38f2fa | underdog | Beau Pribula | Pass Yards | under | 0.06463501056828735 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|270cae6b-42bc-4d4c-a08f-b5b4dca9623b | underdog | Lincoln Kienholz | Pass Yards | under | 0.06454473289674034 | 2026-11-13T19:43:07Z | 2026-11-15T00:00:00Z |
| underdog|b6c8147c-61d0-4fb3-86b0-a7a192137d3f | underdog | Marcel Reed | Pass Yards | under | 0.06440771322136041 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|e358c26d-804f-41f7-a7c8-d71580e77991 | underdog | Jadon Porter | Receiving Yards | over | 0.06438917757554774 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|7e0ca8ad-0431-4f72-95c2-3e4092579f75 | underdog | Cam Cook | Rush Yards | under | 0.06434583017147211 | 2026-11-14T01:00:02Z | 2026-11-14T22:30:00Z |
| underdog|aa25f9a8-4bd8-47a2-a186-2b8195262abf | underdog | Tristen Brown | Receiving Yards | over | 0.0643019368295239 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| prizepicks|16942039 | prizepicks | Breece Hall | Rec Targets | under | 0.06414825334372365 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|067410a9-e4e9-468e-ac1c-c09828fb5b19 | underdog | Matthew Golden | Receiving Yards | under | 0.06410870794329593 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3b3d0c4f-70c5-41e6-8a4b-b405eb8d0143 | underdog | Alonza Barnett | Rush Yards | under | 0.06407750546115587 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| prizepicks|16941201 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.064016928569531 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|654ab2db-8d09-44bd-859a-27ac3c17c838 | underdog | Brandon Dorlus | Sacks | over | 0.06390988477868764 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|4371c896-a43e-4bf0-8a98-208692654d46 | underdog | Jeremiah Cobb | Rush Yards | under | 0.06390755034298268 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|2ef3cdfc-603a-4a90-8dd1-c78a10783d71 | underdog | Greg Dulcich | Receptions | under | 0.06371545917699406 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2d6a7b3d-d370-410d-837e-d053168c7938 | underdog | Kenneth Walker III | Receiving Yards | under | 0.0635541581066561 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|06a81038-1f64-45f0-8636-e61f91d91087 | underdog | Braden Fiske | Sacks | under | 0.06344318175196384 | 2026-11-14T01:00:02Z | 2026-11-15T21:05:00Z |
| prizepicks|16942035 | prizepicks | Garrett Wilson | Rec Targets | under | 0.06335703964183648 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|85077f7c-e15c-40eb-8088-d650fec38122 | underdog | Josh Downs | Receiving Yards | over | 0.06326236895052828 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|c489387a-fbec-48c8-ba91-c6a7f48a4d0a | underdog | Tyler Shough | Pass TDs | under | 0.06300540300276691 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7f0d6a2b-7b34-4d47-984e-08b8cfd1a9f2 | underdog | Tory Horton | Receptions | under | 0.06292579500923501 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|3f30169a-f3de-40ab-8b5a-91c718d2f0d7 | underdog | Nolan James | Receiving Yards | over | 0.06272238102027128 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|f960ea82-4e69-48a3-91be-b64d22da79fa | underdog | Travis Etienne Jr. | Rush + Rec Yards | under | 0.0626714885567563 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|c3bb0883-e8e1-4684-8b48-77a6ced7a183 | underdog | Dilin Jones | Rush Yards | under | 0.0625715964061524 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|09467e0e-3d0e-486b-89a5-e6f753153d08 | underdog | Nicco Marchiol | Pass Yards | under | 0.06254896998290815 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16942052 | prizepicks | Zach Charbonnet | Rec Targets | under | 0.06241369652539952 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|707423ed-e4de-44d4-8f0a-f41859c3dcbb | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.06222463039349091 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16870372 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.06214267328538181 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16942020 | prizepicks | Tyler Higbee | Rec Targets | under | 0.06174816194012789 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|76a68710-9ef5-42b0-86d7-66fcc5b58d9c | underdog | Tre Tucker | Receptions | over | 0.06172070169914223 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|cc7bb479-db29-486f-8537-e96357f9df81 | underdog | Lee Beebe | Rush Yards | under | 0.061715445854283235 | 2026-11-14T11:31:26Z | 2026-11-14T20:30:00Z |
| prizepicks|16961013 | prizepicks | Taylor Fritz | Total Games | over | 0.061670395845261794 | 2026-11-13T19:43:07Z | 2026-11-14T07:00:00.000-05:00 |
| underdog|7f662455-94a7-4b44-98d9-3a1141a6e561 | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.06160934850898092 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| prizepicks|16941188 | prizepicks | Ja'Kobi Lane | Rec Targets | under | 0.06156634147713902 | 2026-11-13T12:14:20Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|4de48f44-f1fa-4bdb-a1c4-577be8473bfd | underdog | Braden Pegan | Receiving Yards | under | 0.061047160627757724 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|25507ed7-e0b7-476c-822f-cfdb87ed4361 | underdog | Denzel Boston | Receiving Yards | under | 0.06096609640716899 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|a8b6fbad-26c9-4f91-963e-25b9f62bb310 | underdog | Logan Hall | Sacks | over | 0.06090543290617789 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|6e0dcb16-0162-4770-816d-09f39e78c848 | underdog | Bo Jackson | Receiving Yards | over | 0.060886535252514085 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16941212 | prizepicks | Matthew Golden | Rec Targets | under | 0.06085890822970175 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|dacd015b-859e-4b90-abc2-437f8cc02b93 | underdog | Cameron Dicker | FG Made | under | 0.060825633187946426 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|9a6ddb65-3150-4e56-bb58-804becccedd4 | underdog | Drew Sample | Receptions | under | 0.060756054857090014 | 2026-11-14T11:31:26Z | 2026-11-16T01:20:00Z |
| underdog|2ca12ee0-e6d2-41c8-b151-acf00be8c9a3 | underdog | Noah Bennee | Receiving Yards | over | 0.0605452926650496 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|b3423be4-c1c8-4eca-b84d-eda9c307336d | underdog | Kenny Darby | Receiving Yards | under | 0.06042170971127514 | 2026-11-13T12:14:20Z | 2026-11-14T23:15:00Z |
| underdog|ead948fb-804f-417c-a11d-2dbb347f6920 | underdog | Isaac Brown | Receiving Yards | over | 0.06041480023198598 | 2026-11-13T19:43:07Z | 2026-11-15T00:00:00Z |
| underdog|15dacbb1-1137-4ecd-813a-83e3d65404ec | underdog | Chase Brown | Receiving Yards | under | 0.06031556029363805 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|d2aca639-0fcc-421f-bff6-1dc28f8b4fa4 | underdog | Dalton Kincaid | Receptions | under | 0.060234650924518074 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3c76afab-a6d6-4a28-b4f1-979d0ffab47e | underdog | Tait Reynolds | Rush Yards | under | 0.06017793149848305 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|1d364140-eb5e-41fe-a16d-55efaa68c2ba | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.060139440532555266 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|adcbbf83-2036-4e85-90fc-a6aa20a1e95a | underdog | Gavin Bartholomew | Receptions | under | 0.060035905587644156 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|64bd48a6-166e-4a28-842e-f7b60290df75 | underdog | Shazz Preston | Receiving Yards | over | 0.05984154913912987 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|11b4b2af-a1af-4863-a1d3-2077193d67fe | underdog | Drake Maye | Pass TDs | under | 0.05982086422742261 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|78748d91-4060-44ca-959a-a5962e13a530 | underdog | Brandon Aubrey | Kicking Points | under | 0.059463924496844345 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|e50a19f7-083f-429c-b20c-934273ce53a5 | underdog | Kaelon Black | Rush Yards | under | 0.05945473776156429 | 2026-11-13T19:43:07Z | 2026-11-15T21:25:00Z |
| underdog|267077c9-c684-4b2f-b77e-ccad312207fe | underdog | Mirra Andreeva | Double Faults | under | 0.05929251002147362 | 2026-11-14T11:31:26Z | 2026-11-14T20:00:00Z |
| underdog|bf6d8568-1c2e-4352-aa80-f22b9a01d700 | underdog | Elijah Higgins | Receptions | under | 0.05927277420068855 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|03538933-cc77-4d76-8cc1-f7f0c9302cc3 | underdog | Jordan Dwyer | Receiving Yards | under | 0.05924093284698162 | 2026-11-13T19:43:07Z | 2026-11-14T19:00:00Z |
| underdog|24457ce7-a29e-4e65-aaab-d2f2d38d5a63 | underdog | Mark Andrews | Receptions | over | 0.05909484948085142 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|ec32c6d7-3c06-4654-ba63-8d73984b0b57 | underdog | Bam Knight | Rush + Rec Yards | under | 0.059071338217762004 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| underdog|09922b6e-e917-4c32-8e83-1664e7f4b1e8 | underdog | Carson Hansen | Rush Yards | under | 0.05888276472852805 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|4d0fcffd-ad43-47a6-82aa-6629600c756c | underdog | Drew Lock | Pass TDs | under | 0.058702533200966744 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c677808c-3553-4196-8f6d-15a1e77726cf | underdog | Elijah Higgins | Receiving Yards | under | 0.05865899667004015 | 2026-11-14T01:00:02Z | 2026-11-15T21:05:00Z |
| underdog|f5777302-cf71-4ed0-a67e-fe6c6156946c | underdog | C.J. Stroud | Pass TDs | over | 0.058654369818583796 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4b1fed48-15ba-428c-bb91-a7555f1b384a | underdog | Tony Pollard | Rush + Rec Yards | under | 0.05854451151910145 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|290e195d-8e34-4596-b14f-bf19adc896d6 | underdog | Kyle Juszczyk | Receptions | over | 0.05854227335361084 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|e85a0b19-b548-4442-98b0-3ecfd04f953c | underdog | Chris Boswell | Kicking Points | under | 0.05833293094762393 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0b91d70f-0d9f-42b6-a4c3-7dcfdcbc4892 | underdog | Mike Matthews | Receptions | under | 0.058284766086376116 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|888fa28c-e758-43a2-8045-d5e4ca7f7e60 | underdog | Junior Sherrill | Receiving Yards | under | 0.05824464639264759 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| prizepicks|16941232 | prizepicks | Travis Kelce | Rec Targets | under | 0.05818111390825431 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|d6f5cd67-0f2d-42ea-b7a3-d1c84a3dd9bf | underdog | Gavin Grover | Receiving Yards | over | 0.058013040558561046 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|1924c720-cf67-43bb-bb8f-79079a113385 | underdog | Trey'Dez Green | Receiving Yards | under | 0.05790422789950067 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|3781f038-1e2d-4add-834e-b1c8ce30f9eb | underdog | Bryce Young | Pass TDs | under | 0.05761978630482656 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5e97417a-5e1a-46ec-a628-38d2ce6156ba | underdog | Spencer Shrader | FG Made | under | 0.05723488095356977 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|a738db07-e623-452a-a25e-f251ff8f2d6a | underdog | Tyrell Henry | Receptions | over | 0.05710980725141879 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|d574c7ec-e37c-4a11-9707-70d6710cd050 | underdog | Jake Bates | Kicking Points | under | 0.057056345727721 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|6f045679-096a-4592-9eb6-f1c464dac753 | underdog | Noah Fant | Receptions | under | 0.057003581476649634 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|0cbb61bb-97e0-4331-ab48-1ce1e85a07df | underdog | Dre'Mont Jones | Sacks | over | 0.056974240339294324 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|36b5231b-d5e6-4040-94cc-b2d96541bed8 | underdog | Dierre Hill | Receiving Yards | over | 0.056780139921930095 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|ad5e8781-bd90-4378-89a8-d05b327c7f69 | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.056683977237381056 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|1fcaea85-7de8-4228-8b8c-94bc768e0933 | underdog | Waymond Jordan | Rush Yards | over | 0.056657622533493046 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|450e6500-80eb-4a39-b11d-91501af45e2b | underdog | Gunner Stockton | Pass TDs | under | 0.05640008620207193 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|9db900b6-98c4-44c5-9401-d670160cd60b | underdog | Matthew Golden | Receptions | under | 0.05633066769825512 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9fa0670e-13e7-4104-aeea-e857d03806fd | underdog | Caleb Hawkins | Receptions | under | 0.05605749578102526 | 2026-11-13T19:43:07Z | 2026-11-15T02:30:00Z |
| prizepicks|16834814 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.05595171947998501 | 2026-11-10T12:33:48Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|7fc13d80-5c19-4981-95c0-1c5a9a22a74b | underdog | Walker Lyons | Receptions | under | 0.055913215695103435 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|f080a415-e7c5-4b6a-bf89-f005fdf79946 | underdog | Matt Gay | FG Made | over | 0.05586119946761431 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|214cbd24-84bb-458e-b1f4-1bd3a2149b36 | underdog | Brenton Strange | Receiving Yards | under | 0.05577611188639431 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f0b24d0a-f51d-4ec6-8f8f-ac17d8e0d0eb | underdog | Jalen Nailor | Receptions | over | 0.05545990463319178 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|f2067b31-0d16-4656-91cd-454d91ca62bd | underdog | Brandon Aubrey | FG Made | under | 0.05538164462438755 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|f9982662-f335-40b3-9dff-dcf0a72383a9 | underdog | Deebo Samuel | Receptions | under | 0.05533870914257788 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|fde40599-57e5-4b83-9581-b81f8aa6e84e | underdog | Calvin Ridley | Receptions | under | 0.055322844268543725 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16905893 | prizepicks | Malik Washington | Rush Atts | under | 0.05523106423632507 | 2026-11-13T01:09:17Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|c663a51d-c520-4cea-81f3-87cd1110c2a7 | underdog | Beau Pribula | Pass TDs | over | 0.05513883017098259 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|08944bde-db15-46d3-8aee-65d143957886 | underdog | Trey Smack | Kicking Points | under | 0.05510427899823733 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|8b780298-e7a8-48b4-b10b-6f6d3d35341b | underdog | Nico Brown | Receiving Yards | under | 0.05504485717670249 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|f77cdfc4-0b84-4c82-9242-02cb0fd152f6 | underdog | Demond Williams | Pass TDs | over | 0.05502559503905735 | 2026-11-13T12:14:20Z | 2026-11-14T21:15:00Z |
| underdog|f8b50df0-df15-4845-9173-0adba2cfe7e2 | underdog | Samaje Perine | Receptions | under | 0.05489044582304281 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|2fb6b68c-630e-4d2a-a229-4d0133bb4f00 | underdog | Creed Whittemore | Receiving Yards | over | 0.05483588486226332 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16874563 | prizepicks | John Mateer | Pass Comp | under | 0.05454068083947805 | 2026-11-14T11:31:26Z | 2026-11-14T16:15:00.000-05:00 |
| underdog|98dfd341-273b-4c60-be82-7a7749cedb88 | underdog | Andrew Van Ginkel | Sacks | over | 0.05452215182609643 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|db43e5f6-fe35-496a-8e90-59cf882cc5aa | underdog | Bam Knight | Rush Yards | under | 0.05450810672776485 | 2026-11-13T19:43:07Z | 2026-11-15T21:05:00Z |
| underdog|13fbd334-9803-480e-8228-8383196b05d7 | underdog | Charlie Becker | Receiving Yards | under | 0.054340862550077196 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|27a0288a-1bf9-436d-8d5b-8933d12fe652 | underdog | Jaleel Skinner | Receiving Yards | over | 0.054222974770846255 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|9b212fcf-8362-45e6-a560-d521a0c2e5b0 | underdog | Jackson Harris | Receptions | under | 0.054155095931503916 | 2026-11-14T11:31:26Z | 2026-11-15T00:30:00Z |
| underdog|222a6fcc-5de1-4ec8-927b-dcc58cba4bec | underdog | JC French | Total TDs | under | 0.05413624199125511 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| prizepicks|16864051 | prizepicks | Charlie Woerner | Rec Yards | over | 0.05401463087599445 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|09e85dc1-6ddb-434e-a936-6fd8aed43b03 | underdog | Andre Szmyt | FG Made | under | 0.05378693771750487 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bf0328b9-baf9-4e7f-86c3-4243ed90ce42 | underdog | Dylan Raiola | Pass TDs | over | 0.053647536822512054 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|c9e94429-e49a-4d7a-87b6-ed6884b65e96 | underdog | Christian Watson | Receiving Yards | under | 0.053404311395892634 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|522b5aab-5b20-463d-9161-d48a3646bcb4 | underdog | Raleek Brown | Rush Yards | under | 0.05337188176570529 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|5f5a3116-6c86-495f-b0cc-76ebd5261b14 | underdog | Justin Bowick | Receiving Yards | under | 0.053320411307768434 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16864058 | prizepicks | Eric Saubert | Rec Yards | over | 0.05300845751715566 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16834798 | prizepicks | Drake London | Rec Yards | under | 0.05299181956525634 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|79f7b6e9-6ede-4804-a488-b8307cf7f6ec | underdog | Raleek Brown | Receiving Yards | over | 0.05296563017571787 | 2026-11-14T11:31:26Z | 2026-11-15T00:30:00Z |
| prizepicks|16874417 | prizepicks | John Mateer | Rush Atts | under | 0.052868503995310734 | 2026-11-13T12:14:20Z | 2026-11-14T16:15:00.000-05:00 |
| underdog|115d1147-17ab-4f53-af6d-903795d66814 | underdog | Wayshawn Parker | Receiving Yards | over | 0.052795762377819244 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16942046 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.052792794428390244 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|2ce30bec-63fb-4dfe-8e38-4cd955159f2a | underdog | Kyren Williams | Receptions | under | 0.05275196940203419 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|90077d5d-1a1d-45eb-b5b7-2d1770fc7b48 | underdog | Braylon Staley | Receiving Yards | under | 0.05274413200052008 | 2026-11-13T12:14:20Z | 2026-11-14T20:00:00Z |
| underdog|83bde468-8247-4b83-9b7b-8e66878a0b19 | underdog | Griffin Wilde | Receiving Yards | over | 0.05250436186658791 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|a4120e53-6f5c-44ee-a542-5b51a4d2cd2d | underdog | Kyler Kasper | Receptions | under | 0.05243218968353769 | 2026-11-14T11:31:26Z | 2026-11-15T00:00:00Z |
| underdog|4cec3df3-17bb-4b74-9a57-c52695175cfc | underdog | Brian Thomas | Receiving Yards | over | 0.05238716839913293 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1a046fef-2ddc-4a9e-8ed1-2e90509c2587 | underdog | Tyler Bass | Kicking Points | under | 0.05211400342992334 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ace4785f-6ef0-4ad5-ae7f-fce811b5415d | underdog | Jonaz Walton | Rush Yards | under | 0.05209378389202124 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|b9b24f29-9b19-472a-92e3-17ff3637168b | underdog | Sam Leavitt | Pass Yards | under | 0.05206185419169984 | 2026-11-13T12:14:20Z | 2026-11-15T00:30:00Z |
| underdog|f48fdb97-2987-4a39-9762-8108b030233c | underdog | Jerry Jeudy | Receptions | over | 0.0520295111392754 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9fbae28f-0bd2-48f8-ba67-0c74a274bbe2 | underdog | Travis Hunter | Receiving Yards | over | 0.051953702465953044 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|a4cdc3ef-e490-44f7-9d22-9688f41616da | underdog | Jackson Kleather | XP Made | over | 0.051919363673327945 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|f14e99e8-1d2a-4b16-8e41-d2ba54c6570f | underdog | Tyjae Spears | Rush Yards | under | 0.05179772105101921 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|feaedf13-f1cb-4e76-92bf-d9d0f7f8348f | underdog | Darnell Washington | Receiving Yards | under | 0.051680680891570296 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|c81f7f2e-696e-4498-b8ca-7a5799d1ee5a | underdog | Matthew Stafford | Pass TDs | under | 0.05151171430881951 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|1cad5c50-a14c-4264-b134-2fea30d0ce4b | underdog | Michael Hawkins | Pass TDs | under | 0.05140454628829705 | 2026-11-11T22:47:13Z | 2026-11-14T22:30:00Z |
| underdog|2617048a-16d2-4090-93bd-da80e31dbd5d | underdog | Will Reichard | FG Made | under | 0.05137550778273203 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|788eeafc-d70a-4674-9706-fb65ca231536 | underdog | Rocco Becht | Pass Yards | under | 0.0510690370048652 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|0c5d98ac-142f-4545-8b6b-11be058d7f24 | underdog | Javonte Williams | Rush Yards | under | 0.05105554228214382 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|779186f4-0a66-41ee-98ea-ff215f170055 | underdog | Rocco Becht | Pass TDs | over | 0.0510381721794963 | 2026-11-14T01:00:02Z | 2026-11-15T00:00:00Z |
| underdog|8d83cc17-415e-4591-931c-8ae910da673c | underdog | Milton Williams | Sacks | over | 0.050963242707224854 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00Z |
| underdog|098448c6-792b-4aaf-8f02-ba09091cf1ab | underdog | Jacoby Brissett | Rush Yards | over | 0.05093240883796324 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|689de879-6d8b-4505-bc78-8695622f13c4 | underdog | JonAnthony Hall | Receiving Yards | over | 0.05085086084931212 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|3ca28cbe-3045-437d-b482-074b9e547595 | underdog | Justice Hill | Receptions | under | 0.050695143750179694 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|95bb1f37-aede-4d17-9905-18286a2f0b06 | underdog | Justin Bowick | Receptions | under | 0.05059544511891889 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|f3e48ad9-376f-490c-b4d2-0c6c94824acc | underdog | Mason McKenzie | Rush Yards | over | 0.05056922102502681 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|cd33d2fb-e1dd-42a2-9cd9-ba5d87ad4c6b | underdog | Ryan Wingo | Receptions | under | 0.0505654551818322 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|a99e747d-0500-40a7-9dc7-e1637572bc5c | underdog | Tate Sandell | FG Made | over | 0.050418940241491905 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| prizepicks|16941210 | prizepicks | Javonte Williams | Rec Targets | under | 0.050359638435533705 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|c340cde5-da10-40fd-b7f0-4f9e3c593374 | underdog | Arik Armstead | Sacks | over | 0.05028733689303222 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16960385 | prizepicks | Thiago Agustin Tirante | Total Games Won | over | 0.050259055411596476 | 2026-11-13T19:43:07Z | 2026-11-14T07:00:00.000-05:00 |
| underdog|4532362a-de26-4d7c-8925-848d6105a4b4 | underdog | Ollie Gordon | Receiving Yards | under | 0.05016806446484068 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|1c5fd9b2-1999-4144-9085-bcd7a7150d91 | underdog | Rece Verhoff | XP Made | over | 0.05016435267545344 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|6f3992ec-ac05-417d-a59f-5320790a1d41 | underdog | Peyton Woodring | XP Made | over | 0.050105935886552544 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|42c2cfee-02ed-4f7f-a137-6dbae4ccca98 | underdog | Chris Marshall | Receiving Yards | under | 0.049777652835880315 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| prizepicks|16942043 | prizepicks | Jaylen Warren | Rec Targets | under | 0.04961774127753471 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863710 | prizepicks | Jaylen Warren | Rec Targets | under | 0.04958776690173983 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|b38d0fe8-eeff-48b0-b233-c1b9ed0a7e6b | underdog | Ja'Cory Thomas | Receptions | over | 0.04930579434434934 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| prizepicks|16928013 | prizepicks | Jelani Thurman | Recs | under | 0.04925248529728332 | 2026-11-14T11:31:26Z | 2026-11-14T19:00:00.000-05:00 |
| underdog|0e47b5e3-2f9a-43f5-b530-f47623ccfa9d | underdog | Drew Sample | Receiving Yards | over | 0.049239250011618774 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|1af83c08-542a-4f5b-816c-ebd6ab059f57 | underdog | Keshaun Singleton | Receiving Yards | under | 0.04917398386031757 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|951caecc-29fa-49d5-805b-bf8f0f9cc838 | underdog | Nicco Marchiol | Pass TDs | over | 0.04913819551733667 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| prizepicks|16921156 | prizepicks | Brandon Tullis | Rush Atts | under | 0.049030937000035024 | 2026-11-13T01:09:17Z | 2026-11-14T16:15:00.000-05:00 |
| prizepicks|16898722 | prizepicks | CJ Baxter Jr. | Rush Atts | under | 0.04899163749296942 | 2026-11-12T07:07:56Z | 2026-11-14T18:15:00.000-05:00 |
| underdog|005fa26e-3f90-4f37-b964-8614d3ab6b93 | underdog | Tony Pollard | Rush Yards | under | 0.04887990433142231 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|a866c628-b0be-4b1d-97ea-bb7cbe41078a | underdog | Elija Lofton | Receptions | under | 0.048515481309444164 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|9cd6e319-56d8-4146-8720-122e222c0af3 | underdog | Kimani Vidal | Receiving Yards | under | 0.04845077626655159 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|320e4928-163a-4eb4-baca-1fffe8cf4cf0 | underdog | Jamal Roberts | Rush Yards | over | 0.04837798218349576 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|211f77ce-1c66-4c75-af18-84b141a89ac9 | underdog | Jack Cassidy | FG Made | under | 0.04832989049568459 | 2026-11-13T19:43:07Z | 2026-11-14T22:30:00Z |
| underdog|95231ceb-e90a-420c-98e0-a38f678fbb41 | underdog | Joe Burrow | Pass TDs | over | 0.04830047288438544 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|6acbfb7a-1667-4143-82f8-d566e5c26ae3 | underdog | Brock Bowers | Receptions | under | 0.04826815873810608 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|9989e1b9-b4e8-419b-a6df-1817c05c39eb | underdog | Mark Andrews | Receiving Yards | under | 0.04815263125185609 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|7c39f112-919c-49a0-afa7-1531cb9e8151 | underdog | Dylan Sampson | Receptions | under | 0.04803084524216095 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8ae7a0e-0afb-41bd-98a8-4bfa74cfc4b7 | underdog | Kirk Cousins | Rush Yards | over | 0.04794648374314203 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|13d92abe-98b8-4b84-8bee-5b401bb6eb1b | underdog | Tony Pollard | Receptions | under | 0.047800095308580204 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16938562 | prizepicks | Mazeo Bennett Jr. | Recs | under | 0.04779046094344863 | 2026-11-14T11:31:26Z | 2026-11-14T19:45:00.000-05:00 |
| prizepicks|16941223 | prizepicks | Laquon Treadwell | Rec Targets | under | 0.04764715308963674 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5ddca326-fb5c-4be7-9264-555c0deffac8 | underdog | Wyatt Young | Receiving Yards | under | 0.047495342258227824 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|cbb27715-4c5c-4930-9405-886767da9aa0 | underdog | Spencer Porath | FG Made | under | 0.04726926706009371 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|fa3dbec8-17a8-4172-a359-586dc7681702 | underdog | Tyren Hornes | Receptions | under | 0.0471609235795728 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|0ea9a1f4-b2c7-49f5-ae0a-5fb13ab0b949 | underdog | Jake Bates | FG Made | under | 0.04711758110912212 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|800287a0-b7f6-4110-811c-f7a7e20cbf4e | underdog | LaNorris Sellers | Pass TDs | under | 0.046971181551276 | 2026-11-13T19:43:07Z | 2026-11-15T00:45:00Z |
| underdog|fd31bc9e-cff4-44fb-ae49-6c536d56bce8 | underdog | Caleb Douglas | Receptions | under | 0.046873180612608145 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f388882e-bf96-4bf0-ab4f-c20217916353 | underdog | Harold Fannin | Receptions | under | 0.046638245325585026 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|238db346-0f78-4553-b19f-0a37b494309e | underdog | Demond Williams | Pass Yards | under | 0.04663058699182798 | 2026-11-13T19:43:07Z | 2026-11-14T21:15:00Z |
| underdog|d4acec1c-8f8f-4897-8e60-b7c7b956d82d | underdog | James Cook | Receptions | under | 0.0465337444974383 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e18e2b81-f40d-4c81-9fee-a10203692c8b | underdog | Brett Eskildsen | Receiving Yards | over | 0.04644721882940239 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|64bae3d3-f674-4a45-807a-d51d2feb6d54 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.046435927839737046 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| prizepicks|16899263 | prizepicks | Chuba Hubbard | Rush TDs | under | 0.04625994985710902 | 2026-11-11T22:47:13Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6c90d765-2043-4abc-be89-2441e45fdbc2 | underdog | Josh Downs | Receptions | over | 0.04620180299105142 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|865a0573-0fdb-4e32-9d47-6685e29820ae | underdog | Kenny Johnson | Receiving Yards | under | 0.04620077271724932 | 2026-11-14T11:31:26Z | 2026-11-15T02:30:00Z |
| underdog|49dbe735-a6e1-435e-b05b-067376ee32f9 | underdog | Joey Slye | FG Made | under | 0.04617041472475325 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0d7845b0-7f5f-4d31-91af-99fe5edf24ed | underdog | James Cook | Receiving Yards | over | 0.04596118738224697 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|03c2a9b4-d39f-4076-b24e-67268d520050 | underdog | Omari Hayes | Receptions | under | 0.04582196406732275 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|d4c7fb13-afc2-4d0f-ae8b-7b50322b7174 | underdog | Justice Haynes | Rush Yards | over | 0.04566559632737066 | 2026-11-14T11:31:26Z | 2026-11-14T17:30:00Z |
| underdog|5714f5d7-a18a-45cf-a0aa-b3e48a714d60 | underdog | Chop Robinson | Sacks | over | 0.045592643757164875 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|c97e7a45-2914-4f89-a1d9-e4aefb0675fd | underdog | Max Gilbert | XP Made | over | 0.045560676594453065 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|36512536-14fc-460a-b2f6-35156a7d9d72 | underdog | Brenton Cox | Sacks | over | 0.04551749632322721 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|56e8eb86-0cbf-469f-8c79-3ef93f017dea | underdog | Denzel Boston | Receptions | under | 0.045152048025238756 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ae810589-81e6-4ea2-8235-0aef0fd1070e | underdog | Joey Slye | Kicking Points | under | 0.04505178064548698 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|1d9a87ef-476e-42de-b171-52da98ca6e93 | underdog | Cameron Dicker | Kicking Points | under | 0.045033047920349456 | 2026-11-13T01:09:17Z | 2026-11-17T01:15:00Z |
| underdog|99b4b3cd-d31a-44f2-b2e0-d467b194fa13 | underdog | Raleek Brown | Receptions | over | 0.04497461810941972 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|f0780ba2-8037-4cc2-a253-38e5dd6c1369 | underdog | Brendan Baird | XP Made | under | 0.04490246123339292 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|8aa26f4f-6c4a-4c9b-bbb8-477e19ee6923 | underdog | Griffin Wilde | Receptions | under | 0.04484180164367657 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| prizepicks|16941203 | prizepicks | Denzel Boston | Rec Targets | under | 0.044751666931493794 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16906356 | prizepicks | DeJuan Williams | Rush Atts | under | 0.04472446734389435 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|b89e1abe-f2d8-423e-8ba3-13c3ae2269dc | underdog | Chase Hendricks | Receiving Yards | under | 0.04454002770132093 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|09fb6589-e5be-4da1-8c03-7b3b6b342d57 | underdog | Jared Curtis | Rush Yards | over | 0.044487657953625304 | 2026-11-13T12:14:20Z | 2026-11-14T17:45:00Z |
| underdog|1f7f7044-5b58-4a4d-9b16-261d3cdb43ec | underdog | Travis Kelce | Receptions | under | 0.04401834231992152 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6a359aa0-6068-4eb0-8c11-237d31a4d274 | underdog | Chuba Hubbard | Receiving Yards | under | 0.04371106231349298 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16942019 | prizepicks | Davis Allen | Rec Targets | under | 0.043658638267208616 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|115fb659-ec08-42f7-95d7-638da77e9cc6 | underdog | Spencer Porath | XP Made | under | 0.04365146949887411 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|d29a2cd3-5b1a-4d86-888e-80dcf04c666d | underdog | Tommy Tremble | Receiving Yards | over | 0.043567053228045105 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|cc162aca-2976-49a7-bbf7-edcbd50d88eb | underdog | Isaiah Marshall | Rush Yards | under | 0.04354884867712727 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| underdog|06aa0f5f-6f09-44bd-a64c-29b236608b45 | underdog | Scott Starzyk | FG Made | over | 0.043538923860573675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|91c91fcf-23a3-44e1-8373-d47ac7555c28 | underdog | Ashton Dulin | Receptions | under | 0.04333380385967567 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|d397bad9-9c29-4db3-89f1-1b3e1ebd6c03 | underdog | John Mateer | Rush Yards | under | 0.043315464447318264 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|3af42ed6-ba31-4421-b3db-8a1a5c702d31 | underdog | Noah Jennings | Receptions | over | 0.04309994548487195 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|50bf9fca-a738-42d6-b653-5eb41d137b44 | underdog | Jordan Watkins | Receptions | under | 0.04307267285244254 | 2026-11-14T01:00:02Z | 2026-11-15T21:25:00Z |
| underdog|14ae01bf-9857-4d2f-8e76-687932093fff | underdog | Myles Murphy | Sacks | over | 0.04303632378436262 | 2026-11-14T01:00:02Z | 2026-11-16T01:20:00Z |
| underdog|05d61698-c97c-4c5b-9d89-defe3d868ba6 | underdog | Kevin Jennings | Rush Yards | over | 0.042850054600276355 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|dd9ccb7a-bffb-4472-be26-448ceee6db64 | underdog | Keaton Mitchell | Receptions | under | 0.04260594560207376 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0d111317-5c99-4d56-b5f5-63bae031a649 | underdog | Deshaun Watson | Pass TDs | under | 0.04236385864477632 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b03c56fa-f1b4-4ed3-8f2c-6e053fa36930 | underdog | Justice Hill | Receiving Yards | under | 0.042334380979668684 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|741b63a8-a778-45dc-8a3c-618f25571627 | underdog | Harrison Butker | FG Made | under | 0.04233008949187933 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3405d67c-7d7c-41c2-9ba1-d12bd10bac31 | underdog | Jacob Harris | Receiving Yards | over | 0.042309309184291655 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|f14cb1a6-b888-4c95-bda9-956f9c85fc63 | underdog | Josh Hines-Allen | Sacks | under | 0.04228434612672083 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|1bf6b6e0-7afd-431b-99d0-9b9044aaa6fa | underdog | Joe Jackson | Rush Yards | over | 0.04211550474052239 | 2026-11-13T19:43:07Z | 2026-11-14T19:00:00Z |
| underdog|15aee1d7-2fe0-42c3-98c6-14884361a179 | underdog | Ashton Dulin | Receiving Yards | under | 0.041908175314722684 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|95c05909-55d3-4c40-baa2-21c12deb1a59 | underdog | Justin Herbert | Rush Yards | under | 0.04188540886632808 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|f3fb8543-cfbe-4af9-a504-dc8cf875946d | underdog | Jack Foley | Receiving Yards | over | 0.041884561255384645 | 2026-11-14T11:31:26Z | 2026-11-14T17:00:00Z |
| underdog|96a329b5-38e7-4b8b-a27e-6589f2d3bc55 | underdog | CJ Baxter | Rush Yards | under | 0.04174879097274642 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|94cc4393-ed78-41f3-bde5-b30173c95a06 | underdog | J'Koby Williams | Receiving Yards | over | 0.041689854183781794 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|55cb13c1-ee46-47e8-b0ce-5d68bc2910db | underdog | Connor Calvert | XP Made | over | 0.04166023250717721 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|b96e5afb-b999-4933-8781-cd4c11d325c9 | underdog | Jack Bech | Receptions | under | 0.04163575481719084 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|3ac37949-6a8b-4c13-933c-a2b9c2347ab2 | underdog | Henry To'oTo'o | Sacks | under | 0.04161136314625302 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|2fa9e2b4-614d-4a17-9548-927d0f196189 | underdog | Derrick Henry | Receptions | under | 0.04138130744755619 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|b519b161-4417-4dbb-8e1c-64a49cbe1b03 | underdog | Jayden Maiava | Pass Yards | under | 0.04136793364471936 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|992f3e80-6aa2-4ce0-bca9-9bd0cba69874 | underdog | Ashton Jeanty | Receptions | under | 0.041325909181133325 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|86f75d06-cc81-4f09-b15f-5e0a01e89d55 | underdog | Amante Martin | Rush Yards | under | 0.041296873065206796 | 2026-11-13T19:43:07Z | 2026-11-14T19:00:00Z |
| underdog|51179fe5-339b-45cf-98b1-d1fa3c49717a | underdog | Davion Gause | Rush Yards | under | 0.04108109493241252 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|22617c58-a117-4cec-b02f-aaf2a6d3e348 | underdog | Will Bettridge | XP Made | over | 0.04107482967554221 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|bc509bde-38be-4cfe-9f6c-2ce47dfc45e8 | underdog | Ty Clark | Rush Yards | under | 0.04104698803817841 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| prizepicks|16941197 | prizepicks | Ty Johnson | Rec Targets | under | 0.040992064808991424 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6819d4f5-78f7-4d71-bcf0-4b996192def2 | underdog | Carson Bruhn | Receiving Yards | over | 0.040828624494910315 | 2026-11-13T01:09:17Z | 2026-11-14T22:30:00Z |
| prizepicks|16941179 | prizepicks | Bijan Robinson | Rec Targets | under | 0.040803121509780604 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|2da91c82-7ea9-4347-be3c-34f62f198666 | underdog | Micah Ford | Receiving Yards | over | 0.040738463225132526 | 2026-11-14T01:00:02Z | 2026-11-15T00:30:00Z |
| underdog|63f35c03-cf3a-4a60-9e48-e6b9aee69d0c | underdog | Jordan Love | Pass TDs | under | 0.04051564232645721 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e5538a7e-bc11-4b87-8ff5-8b9b27f1d395 | underdog | Luke Reynolds | Receiving Yards | under | 0.040421230293381405 | 2026-11-13T01:09:17Z | 2026-11-15T00:30:00Z |
| underdog|f3acd35c-51ac-4b98-81d7-5f632298e45c | underdog | Pierre Strong Jr. | Rush Yards | under | 0.040405873993211716 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|92b63877-4f72-4f8e-a611-63ae37339cc6 | underdog | Randy Pittman | Receiving Yards | over | 0.04030313051643297 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|1c3138ba-e932-4be6-bd5a-586926b125e7 | underdog | JC French | Pass Yards | under | 0.040254892901353534 | 2026-11-13T01:09:17Z | 2026-11-14T17:00:00Z |
| underdog|d56bd308-ebf5-4302-b7e2-20fe3d4ea2f0 | underdog | Tyjae Spears | Receptions | under | 0.039987626315219016 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|e2ba9c86-988f-4106-ac0d-1cf7ee2d89a5 | underdog | Daunte Bacheyie | Receptions | over | 0.039970367512522864 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|4595c21b-9647-4bd2-93a6-4e60a1c16175 | underdog | Jack Foley | Receptions | over | 0.039907390349167016 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|3868c985-c2f4-42c2-b08d-83a91201a94b | underdog | Devin Duvernay | Receptions | under | 0.03988605673509471 | 2026-11-13T12:14:20Z | 2026-11-15T21:05:00Z |
| underdog|77fa1042-4be4-44ed-919f-a5406cdb88f2 | underdog | Brandon Phelps | Receiving Yards | over | 0.03987046222043 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|4c13ad61-01fc-4085-a6a0-4a96af27f074 | underdog | Will Kacmarek | Receptions | under | 0.03963488743783483 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|f031516f-4b17-4b60-a4c7-796d7df87f37 | underdog | Beau Pribula | Rush Yards | under | 0.039432516162914655 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|80e8ea34-6d17-4e8f-8a75-677596b6a5cc | underdog | Dalton Schultz | Receptions | over | 0.03943023171008658 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|2d8123a0-f708-4858-8cb8-b23ea13fb087 | underdog | Terrance Carter | Receptions | under | 0.03939426269801527 | 2026-11-13T01:09:17Z | 2026-11-15T02:30:00Z |
| underdog|bb750385-cd4b-427e-99bb-aa1c719550b9 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.03931795414340944 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|07a0eb6c-d8d9-46bf-aac3-dfed58d52aa7 | underdog | Braelon Allen | Receptions | over | 0.039314624923994734 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d8b03841-950e-438e-b854-d18417ae6d47 | underdog | Bear Bachmeier | Rush Yards | under | 0.03919720056348952 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|b7843c2a-a94b-44a3-bdb4-a0b3e3658e0a | underdog | Tony Livingston | Receptions | over | 0.03902725697014531 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|b84a5c5e-8fa6-4e58-aabd-2b3b66cf8875 | underdog | Khalil Herbert | Rush + Rec Yards | under | 0.038922242891002434 | 2026-11-13T12:14:20Z | 2026-11-15T18:00:00Z |
| underdog|0106a59e-fd6f-4578-88fb-91e093b9efe4 | underdog | JJ Buchanan | Receiving Yards | over | 0.038881092754730284 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|aee66ab0-3674-4803-b10b-149664415874 | underdog | Benjamin Hall | Rush Yards | over | 0.038759772213096344 | 2026-11-13T12:14:20Z | 2026-11-15T00:00:00Z |
| underdog|1595ffba-834e-4175-adbb-a3eeb0fb4aa9 | underdog | Jamal Polite | Receiving Yards | under | 0.03865774848185577 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|48dd0db4-72a2-4c19-9e26-97637dc7ca20 | underdog | Rodney Fields | Rush Yards | under | 0.03865564635491625 | 2026-11-13T19:43:07Z | 2026-11-14T19:00:00Z |
| underdog|4d502520-f37a-41e0-a867-9123d993a4bb | underdog | Jeremy Payne | Rush Yards | under | 0.038568779745354664 | 2026-11-14T01:00:02Z | 2026-11-14T19:00:00Z |
| underdog|f02d9522-37a0-4485-909f-dc4967cad1b9 | underdog | KJ Jackson | Pass TDs | over | 0.038539211710092114 | 2026-11-13T12:14:20Z | 2026-11-15T00:45:00Z |
| underdog|a8ce8a0d-b252-405b-97ec-d2c24fe29262 | underdog | Dalton Kincaid | Receiving Yards | under | 0.03848081974045625 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16941193 | prizepicks | DJ Moore | Rec Targets | under | 0.038224949027769295 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16942054 | prizepicks | Jadarian Price | Rec Targets | under | 0.03801035045808776 | 2026-11-13T12:14:20Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|686fd705-0b0b-42af-bb16-1efe034174c7 | underdog | Nyziah Hunter | Receiving Yards | under | 0.037899280695005144 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|dc4bc437-547f-4e91-8d7a-d011546a1c70 | underdog | Walker Lyons | Receiving Yards | under | 0.037832214678179876 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|dc772c81-1520-4bf3-9e86-85052e3c8fd8 | underdog | Boye Mafe | Sacks | over | 0.03775377328331919 | 2026-11-14T01:00:02Z | 2026-11-16T01:20:00Z |
| underdog|388d3b79-b0a7-42d3-872a-d1e8c8f7f0d2 | underdog | Alonza Barnett | Pass TDs | under | 0.037747158672632786 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|dafcd3c4-1ca5-4904-8e4a-cd470771d287 | underdog | Patrick Jones | Sacks | over | 0.03770990024618631 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|eb0c88d6-d923-40ca-88bc-5a021ff1d132 | underdog | Khalil Herbert | Receptions | under | 0.03766464527669133 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|d459f077-488d-4d27-9756-e2ad4d6cb490 | underdog | Craig Dandridge | Receiving Yards | over | 0.03764086223884311 | 2026-11-14T11:31:26Z | 2026-11-14T20:30:00Z |
| underdog|eb21d360-8f87-43c3-932f-99c50fe8664a | underdog | Byron Young | Sacks | over | 0.03752903468578739 | 2026-11-14T01:00:02Z | 2026-11-15T21:05:00Z |
| underdog|024cff8f-3c0b-41d3-b64f-ea8842dfe2e7 | underdog | Ashton Jeanty | Rush Yards | under | 0.03729288076056669 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| prizepicks|16941228 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.03714571278625545 | 2026-11-13T12:14:20Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|d0bf4b70-9545-47d2-bde8-ec1e76ceea24 | underdog | Mazeo Bennett | Receptions | under | 0.037122036789791535 | 2026-11-14T01:00:02Z | 2026-11-15T00:45:00Z |
| underdog|6c77a458-f11c-43b3-8941-1f4df51219c8 | underdog | Bam Knight | Receptions | over | 0.03712161464621744 | 2026-11-13T01:09:17Z | 2026-11-15T21:05:00Z |
| underdog|8efe3fb6-58f5-4373-88ae-4d6bbc1a0b2b | underdog | Isaiah Mozee | Rush Yards | under | 0.03710811644303835 | 2026-11-13T19:43:07Z | 2026-11-14T17:30:00Z |
| underdog|48f9ce4f-2465-4fe0-b417-fc1c8915bc81 | underdog | Bear Bachmeier | Pass TDs | under | 0.03706377955837836 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|fa9bddc8-e6d7-4bba-8ace-9ab2de5ab31e | underdog | Darren Waller | Receiving Yards | under | 0.037039947520251415 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|68307110-5279-4504-a3d9-6d37c57b1087 | underdog | Jordan Dwyer | Receptions | under | 0.03703936423477594 | 2026-11-14T01:00:02Z | 2026-11-14T19:00:00Z |
| underdog|55df2acd-8cfd-43ed-b969-86957bc28871 | underdog | Carlos Hernandez | Receiving Yards | under | 0.03697154863642449 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|d511305a-9523-4792-b762-5612b2c2f9bd | underdog | Kyler Kasper | Receiving Yards | under | 0.03692640538945968 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|4d82b7f0-d383-413f-97c1-7d74814849b1 | underdog | Geno Smith | Pass TDs | over | 0.03690270527418432 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|573c1e57-814e-4d93-87ee-3114b05d8378 | underdog | Ian Strong | Receiving Yards | over | 0.036875694367061396 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|a98832ad-cc1c-4f28-9746-8d27fb8ec062 | underdog | Joe Burrow | Rush Yards | over | 0.03676432878965474 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|84da88b3-b9cf-49a5-ac74-5fea3913775e | underdog | Bhayshul Tuten | Receiving Yards | over | 0.036454020844107315 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| prizepicks|16962239 | prizepicks | Jordan Dwyer | Recs | under | 0.03642092218915405 | 2026-11-14T11:31:26Z | 2026-11-14T14:00:00.000-05:00 |
| underdog|9cd574f3-89de-4e8a-9ceb-5e892f3875dc | underdog | Rashod Bateman | Receptions | over | 0.036295203210838234 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| prizepicks|16942041 | prizepicks | Darnell Washington | Rec Targets | under | 0.03624850473786778 | 2026-11-13T12:14:20Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16863708 | prizepicks | Darnell Washington | Rec Targets | under | 0.03622440116764336 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|0fbebad7-ef4b-4c1e-b622-c8921e501f7f | underdog | King Miller | Rush Yards | over | 0.036196766847854 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|584121f2-3498-45db-86d2-51230f6e6643 | underdog | Asaad Waseem | Receiving Yards | over | 0.036152712041357615 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|fc3f7dc6-6626-4be6-8dee-cf5acf248454 | underdog | Lawayne McCoy | Receptions | over | 0.03607754059505758 | 2026-11-13T19:43:07Z | 2026-11-15T00:00:00Z |
| underdog|7e214067-4ba0-412c-845a-dce679ce43cc | underdog | Scott Starzyk | XP Made | over | 0.03604303058757463 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|9228a5e8-d692-4ffc-8ae9-5f0f1825ce29 | underdog | Jeremiah Smith | Receiving Yards | under | 0.03578569435285306 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|bf9e370d-493a-4033-b337-fadf273c4605 | underdog | Daniel Bellinger | Receiving Yards | under | 0.035653924318333474 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|33c569ea-e2cc-4587-bc5d-c61aea1dfe3a | underdog | Devaughn Vele | Receptions | over | 0.03560111354860207 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|ca192d14-582f-4fba-95e0-d881ceb4d344 | underdog | Kenyon Sadiq | Receiving Yards | under | 0.03558440453192235 | 2026-11-13T01:09:17Z | 2026-11-15T18:00:00Z |
| underdog|38b0b194-69d4-4fe9-ac33-5f0245caa76c | underdog | TreyShun Hurry | Receptions | under | 0.035496057268130654 | 2026-11-13T19:43:07Z | 2026-11-15T00:00:00Z |
| prizepicks|16863713 | prizepicks | Chase Brown | Rec Targets | under | 0.03548427625308703 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|f0d39c37-b0df-4dbe-aeeb-068a7761f391 | underdog | Aaron Jones | Rush Yards | over | 0.03530477222712891 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|84247a92-284a-4261-a2c6-40278913648f | underdog | Byrum Brown | Rush Yards | under | 0.035304569145290454 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|f12ce9a6-0596-4a5f-9826-09c752e8ac48 | underdog | Kenneth Walker III | Rush Yards | under | 0.0352835662014076 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|274f14ba-1d4b-469e-8cfb-8fcd873ebcb8 | underdog | Andre Szmyt | Kicking Points | under | 0.035194355906048136 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d3533652-67c2-4228-8da4-9887e1218937 | underdog | Noah Gray | Receptions | over | 0.03516926483455424 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|92172efd-c990-41e1-b5cd-9bff906c1d49 | underdog | Legend Glasker | Receiving Yards | under | 0.035125799741391406 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|cdf4e8f2-86d6-4543-9b8e-099d5521aa0d | underdog | Chris Durr | Receptions | over | 0.035117802159062406 | 2026-11-14T01:00:02Z | 2026-11-14T17:00:00Z |
| underdog|ae363647-2d9e-4fd4-b548-fc834f69a4fd | underdog | Bijan Robinson | Receptions | under | 0.0351075871491785 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|51b763d4-6bbe-48ff-81f7-268172bd6d22 | underdog | Jacory Barney | Receptions | under | 0.03506771685023202 | 2026-11-14T11:31:26Z | 2026-11-14T17:30:00Z |
| underdog|4a5cdc82-4808-47a5-9b18-0d957bd6700a | underdog | Noah Fant | Receiving Yards | over | 0.03485197868324574 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|e9f2c10c-6978-4134-9666-1cdc9df3a448 | underdog | Will Reichard | Kicking Points | under | 0.03483187705738011 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|71695d60-9a36-4905-a360-64d286fd24f6 | underdog | CJ Bailey | Pass TDs | over | 0.03474944763527954 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| prizepicks|16964272 | prizepicks | Ben Shelton | Total Games | over | 0.03469975765932942 | 2026-11-14T01:00:02Z | 2026-11-15T14:30:00.000-05:00 |
| underdog|49e5e566-fec7-49d8-bb3b-24a3821ca1f7 | underdog | Andrew Rappleyea | Receptions | over | 0.03469525675099577 | 2026-11-13T01:09:17Z | 2026-11-15T00:00:00Z |
| underdog|44d086c9-4999-4536-b31a-4af7deef7084 | underdog | Derek Eusebio | Receiving Yards | over | 0.03452196124652973 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|0a57bc4e-1488-4cda-8a52-5cd7829cfc1c | underdog | Legend Glasker | Receptions | under | 0.034235584291332 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|8200630e-636a-4386-88ce-5c93a62a968e | underdog | Jadan Baugh | Rush Yards | under | 0.034216745542511307 | 2026-11-13T01:09:17Z | 2026-11-14T23:15:00Z |
| underdog|c41bdf61-ec11-47ea-aa1a-d7caf74b5490 | underdog | Javonte Williams | Receiving Yards | under | 0.03421399617321885 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|79628351-e183-4617-9674-6f3bd2f44202 | underdog | Trent Mosley | Receptions | under | 0.03411216452257926 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|89bf8183-bd08-4703-ace9-5a6a0f2494b9 | underdog | Jaylen Warren | Rush Yards | under | 0.034088465358187325 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|5eed7261-a329-46a9-8b9b-e6510e877a59 | underdog | Rico Dowdle | Receiving Yards | under | 0.03408492305432431 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|3c8ae112-9de5-44b6-9880-8239165a9b9a | underdog | Jack Cassidy | XP Made | over | 0.034048796167222284 | 2026-11-13T19:43:07Z | 2026-11-14T22:30:00Z |
| underdog|40f3c1be-4f00-4244-95fd-da9e8a7849a6 | underdog | Dilin Jones | Receiving Yards | over | 0.0340358814377133 | 2026-11-13T19:43:07Z | 2026-11-15T00:30:00Z |
| underdog|67037708-fc18-425d-8846-36f6c1d40fa0 | underdog | Ben Yurosek | Receiving Yards | under | 0.03394903474294475 | 2026-11-14T11:31:26Z | 2026-11-15T18:00:00Z |
| underdog|53134d2c-7551-43f4-a943-c3af824d1509 | underdog | Mark Bowman | Receiving Yards | over | 0.03380046616093235 | 2026-11-14T01:00:02Z | 2026-11-14T20:30:00Z |
| underdog|cdac848c-3b35-41a0-8422-20b834aa53b5 | underdog | Towns McGough | XP Made | under | 0.03380030896746378 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|7bb2c540-bf99-4d73-aba2-a5fdcc260362 | underdog | Byrum Brown | Total TDs | under | 0.03377355924595826 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|f04cdcb8-a7b9-444b-82cd-d9c4f68b5331 | underdog | Braelon Allen | Rush Yards | over | 0.03360981687067632 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16941209 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.03352020748434126 | 2026-11-13T12:14:20Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|0ba0603f-931f-42ff-964d-b3ebba3db580 | underdog | Ryan Hopkins | Pass TDs | under | 0.03351528965621331 | 2026-11-13T19:43:07Z | 2026-11-14T17:00:00Z |
| underdog|6b057709-d6dc-4521-be96-04631e1d5383 | underdog | Devin McCuin | Receptions | over | 0.03350696128296665 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|b7e99795-da26-48e8-8250-77ae145b57a0 | underdog | Omar Cooper | Receptions | over | 0.033145857239147036 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e5a1d8cc-9fd0-4363-a0ec-b6077999af5f | underdog | Savion Williams | Receptions | under | 0.03308677892440648 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3519633c-2f5b-401f-81ff-3f7c72260009 | underdog | Jordan Faison | Receiving Yards | under | 0.03280421092792818 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
| underdog|1532deaf-e39a-42f6-9444-fb37fb0c6508 | underdog | Jordan Love | Rush Yards | under | 0.03279240845654863 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16863704 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.032604420063334416 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|ccea17c8-e390-4da5-badf-d4cc345723dd | underdog | Jared Curtis | Pass TDs | under | 0.03245948310828595 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|6497b72f-8917-4fb8-bf75-fee9b6802c4b | underdog | Mitchell Evans | Receptions | over | 0.032392458273830194 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3e2b0506-60a8-47fd-8ee3-be33507fad64 | underdog | Ty Johnson | Receptions | under | 0.03215144399593095 | 2026-11-13T19:43:07Z | 2026-11-15T18:00:00Z |
| underdog|2d8bee1d-b82e-473c-9380-c1fd773a61e6 | underdog | Marquis Johnson | Receiving Yards | under | 0.032032730753339234 | 2026-11-13T12:14:20Z | 2026-11-14T17:00:00Z |
| underdog|6cc86369-a1f7-4361-91da-ad05d8e0835f | underdog | Mike Washington | Rush + Rec Yards | under | 0.03200244448616896 | 2026-11-11T16:13:16Z | 2026-11-15T21:05:00Z |
| underdog|025f64b9-c0b3-46a3-a947-ad3479490326 | underdog | Adonai Mitchell | Receiving Yards | under | 0.031903411083543554 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|8206c911-50a1-4311-a9ab-a4bce1c90765 | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.03176549797720041 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|7e7631f5-e3d4-46ed-b5f1-266bf3d7b45a | underdog | Jalen Coker | Receptions | under | 0.031714257024792025 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|c940fdd4-b5f0-4cd6-9f85-84d0f9a8453e | underdog | Chase Hendricks | Receptions | under | 0.03167892393674565 | 2026-11-13T19:43:07Z | 2026-11-14T20:30:00Z |
| underdog|e15b1902-efc1-481a-ac83-fb2fee335221 | underdog | Ashton Jeanty | Receiving Yards | over | 0.031645254793110755 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|792b0d48-a54c-4ebf-9850-d82cd32eb4e1 | underdog | Mario Craver | Receptions | over | 0.03154931517292969 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|4e3d83a3-32df-4adc-a6cb-19c47ccd3314 | underdog | Mike Washington | Rush Yards | under | 0.031494264716392606 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|0658238c-5e5a-4e3a-b337-a75de8881f51 | underdog | Kwazi Gilmer | Receptions | under | 0.03126132628636824 | 2026-11-13T01:09:17Z | 2026-11-14T17:30:00Z |
| prizepicks|16893229 | prizepicks | Carlos Hernandez | Recs | under | 0.031021000492780115 | 2026-11-13T19:43:07Z | 2026-11-14T12:00:00.000-05:00 |
| prizepicks|16834647 | prizepicks | Javonte Williams | Rush Yards | under | 0.030973438538770326 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|b07aa94a-6957-4140-93d5-a6e918e23c20 | underdog | Omarion Miller | Receiving Yards | under | 0.03096398161420666 | 2026-11-13T12:14:20Z | 2026-11-14T20:30:00Z |
| underdog|dba76811-b7a7-412f-8979-960a79824c3d | underdog | Braelon Allen | Rush + Rec Yards | over | 0.030774756545559168 | 2026-11-14T01:00:02Z | 2026-11-15T18:00:00Z |
| underdog|242c333e-4229-4bd6-981b-3f85497b6e4e | underdog | Brock Bowers | Receiving Yards | under | 0.0306330498389088 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|d649c6df-5a33-430f-ad49-de2a7613706b | underdog | Peyton Woodring | FG Made | over | 0.030478185796160684 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|b357c9e8-27ef-4f86-9497-cac10d884f8c | underdog | Sam LaPorta | Receptions | under | 0.030234889226053996 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|320ad195-4f46-4b95-81e5-d49c528bc76f | underdog | Micah Gilbert | Receiving Yards | over | 0.030107857960482542 | 2026-11-13T01:09:17Z | 2026-11-14T20:30:00Z |
