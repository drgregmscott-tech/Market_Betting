# Pipeline Digest -- 2026-10-18T04:20:08Z

## Run summary
- Ingestion: 29992 rows (PrizePicks OK, Underdog OK)
- Estimation: 29992 rows estimated (from 29992 ingested props)
- CLV logging: 148 newly flagged, 0 newly closed, 849 still open (103243 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|95ac9007-2c9b-4cf5-8892-db46d1e75d48 | underdog | Bryce Young | Pass Yards | under | 0.4692307692307692 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|9171eb1c-0f8a-464a-b7dd-82b15395199c | underdog | Daniel Jones | Pass Yards | under | 0.4641025641025641 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|51b2d1db-1a40-4dc0-8329-590c7fbfd37c | underdog | Bhayshul Tuten | Rush Yards | under | 0.4583756345177665 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|2fd919bf-4db7-4293-91d7-aa62423b3b0a | underdog | Jayden Daniels | Pass Yards | under | 0.4532994923857868 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|37204193-6127-433e-a27a-2840304a56d6 | underdog | Rico Dowdle | Receptions | under | 0.4510204081632654 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|62cb073b-2b16-4a1e-afe3-473ccc1712a9 | underdog | Aaron Rodgers | Pass Yards | under | 0.4482233502538072 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|bd1d8bc9-8db9-42b4-a944-b34294025b5c | underdog | Dak Prescott | Pass Yards | under | 0.4357142857142857 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|ccdd0e22-5f7f-4aa0-8e90-6d129e6873f8 | underdog | C.J. Stroud | Pass Yards | under | 0.4275095132104642 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|75ade92a-c724-43d5-abea-6c2a3f2816a9 | underdog | Brock Purdy | Pass Attempts | under | 0.4226130653266332 | 2026-10-16T04:33:49Z | 2026-10-20T00:15:00Z |
| underdog|4b6d59d8-b0bf-48e9-93d3-6c2fdb92b62e | underdog | Stefon Diggs | Receiving Yards | under | 0.411130384316266 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|558e93a8-af20-4e7f-a3bf-b4d53c831a53 | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|b5eb85fb-7ef9-4e81-8455-82ee7611bc66 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|772f574c-f68d-4b62-b864-7e9f124c7dd8 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9be84160-7fb1-4284-a17a-a04f2125c5de | underdog | Brock Purdy | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|129840ac-ed6e-4c46-b254-7cdef5ad22cf | underdog | Josh Allen | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|63160ab8-3724-4984-b8e7-8644d9a9dcfd | underdog | Justin Herbert | Pass Attempts | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|ef656b80-8ce1-466f-a93c-2df83565dd07 | underdog | Caleb Williams | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|8f20911c-0977-442e-8ea1-d56313c700db | underdog | Brock Bowers | Receiving Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|3f6a4e08-cdcb-4e3a-ad6e-22acec0014c9 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|74d1dae0-164a-4875-a184-d077b7641e61 | underdog | Aaron Rodgers | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|ccdcdb79-cb81-4b8a-9e5a-061fc12ce25a | underdog | Cam Ward | Pass Yards | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|015739b9-4e70-4bbb-a497-051cd57819d8 | underdog | Aaron Rodgers | Pass Attempts | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|6a8f139d-bab9-413e-b1aa-b0649b29b9b6 | underdog | Deshaun Watson | Pass Attempts | under | 0.4 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|24bd470e-5ff9-4938-8e22-a30d6d30d351 | underdog | Tyler Huntley | Rush Yards | under | 0.4 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|62243537-95c2-47b7-b97c-b916cc4f932e | underdog | Trevor Lawrence | Completions | under | 0.4 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|318ca308-be37-44e9-84f3-df144d4a4bc8 | underdog | Jalen Royals | Receiving Yards | under | 0.4 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|f4fe1dd0-1367-4afd-988f-49f3894b0f1b | underdog | Kirk Cousins | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|33fa465d-54b8-4270-a5f1-86fb6c199dbb | underdog | Kendre Miller | Rush + Rec Yards | under | 0.4 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|d999d013-7f1c-44f0-a3ef-388240580758 | underdog | Jacoby Brissett | Pass Yards | under | 0.3990868523006889 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|77b97767-248e-4dda-b829-806b9a567a91 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.397850431989636 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|5aeadea9-2987-42d4-87f5-9c6a1e2610ff | underdog | Michael Penix | Pass Attempts | under | 0.3953529458334468 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|46299aa2-7635-4c71-9d84-eb47e743ef7d | underdog | Geno Smith | Pass Yards | under | 0.3935585247557064 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|c5400d76-0c42-422b-a2ba-cc588efd8226 | underdog | Matthew Stafford | Pass Yards | under | 0.3893178531832612 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|439f721c-d9a1-4af5-aa10-1c2c1fc921e2 | underdog | Patrick Mahomes | Pass Yards | under | 0.3888093202184146 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|b290a7f7-2448-41b8-8395-aaf31553b5b0 | underdog | Christian McCaffrey | Receptions | under | 0.382768282723803 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|21a3bf23-bece-4735-9f8d-0c89f53e33ae | underdog | Nico Collins | Receptions | under | 0.3784872632706449 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|a1e56042-694a-4b8d-ac32-83c80b55412f | underdog | Rico Dowdle | Rush Yards | under | 0.3747452673855316 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|ad060ed6-2e7a-4455-8555-3e27047e4f12 | underdog | Jordan Love | Pass Yards | under | 0.3745565574821633 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|b7582a7b-1d30-47a1-984a-56546465c98b | underdog | Deshaun Watson | Pass Yards | under | 0.3666666666666667 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d3766fc5-3377-40e9-a5d2-f42164ff8eb3 | underdog | Jalon Daniels | Pass Yards | under | 0.3666097493735623 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|50252889-3a21-4531-8598-2fc199a73bb7 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3646000607706979 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|54c0ddbe-6f6b-4eab-8b34-18fdbeb12d53 | underdog | Josh Allen | Pass Yards | under | 0.3642857142857143 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|d225ea43-f349-4f52-8338-a3eb048d8163 | underdog | Braelon Allen | Receiving Yards | under | 0.3615384615384616 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|08d523b2-e50a-427a-a60e-2211a343a0cb | underdog | Deshaun Watson | Completions | under | 0.3591836734693877 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|fdafde04-0e51-4d37-bf96-ed0e87c3b393 | underdog | Justin Herbert | Pass Yards | under | 0.3568527918781726 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|aa428a1a-08ed-456f-827c-0e197631f997 | underdog | Kirk Cousins | Pass Yards | under | 0.3568527918781726 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| prizepicks|15683909 | prizepicks | Cam Ward | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15825150 | prizepicks | Ray Davis | Rush Yards | under | 0.3509424650567749 | 2026-10-18T04:33:13Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15683900 | prizepicks | Trevor Lawrence | Pass Yards | under | 0.3509424650567749 | 2026-10-15T04:38:48Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15683925 | prizepicks | Brock Purdy | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683924 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683903 | prizepicks | Bryce Young | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15683919 | prizepicks | Justin Herbert | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15683921 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3505090563735199 | 2026-10-15T04:38:48Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|c61f6639-a8c2-4e20-8354-9f795b44678d | underdog | Puka Nacua | Receiving Yards | under | 0.3495795126746557 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|876eb302-e79b-4a92-9421-28b5d75136e6 | underdog | C.J. Stroud | Completions | under | 0.3486878585873885 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|765536f2-5839-4303-8f76-5a2a4524feb6 | underdog | Jameis Winston | Pass Yards | under | 0.348546777600185 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|db1d13ee-0b8a-41bc-8a70-aba8c034ee79 | underdog | Trey McBride | Receptions | under | 0.342145746487567 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15723443 | prizepicks | George Kittle | Rec Targets | under | 0.341921366253107 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|be10a2a5-7289-440d-b587-e3455ebf962f | underdog | Cam Ward | Pass Attempts | under | 0.3387540233607855 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15683906 | prizepicks | Geno Smith | Pass Yards | under | 0.338311604119263 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15683899 | prizepicks | C.J. Stroud | Pass Yards | under | 0.3382107114340275 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15683917 | prizepicks | Jacoby Brissett | Pass Yards | under | 0.3378362389461798 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| prizepicks|15851449 | prizepicks | Jayden Daniels | Pass+Rush+Rec TDs | under | 0.3373929181917084 | 2026-10-17T04:25:02Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|6d3eb097-9fae-42e9-ae51-4bda536d6abf | underdog | Bam Knight | Receptions | under | 0.3370159721254852 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|02f8cc66-b21d-448c-a031-7e511e7bffb8 | underdog | MarShawn Lloyd | Rush + Rec Yards | under | 0.3366030142990036 | 2026-10-15T04:38:48Z | 2026-10-19T00:20:00Z |
| underdog|a125c3d4-a234-4ec5-b1a1-ea662989d557 | underdog | Michael Penix | Pass Yards | under | 0.3358974358974359 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|7158d325-e071-43c4-b806-d26b8619c04c | underdog | Cyrus Allen | Receptions | under | 0.3358974358974359 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|c67b981b-b23d-47db-adf6-b8f5f6a4e62b | underdog | Bryce Young | Pass Attempts | under | 0.3353909493099263 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d2db79fe-5f53-4dc9-8222-95da24cf53a4 | underdog | Drake Maye | Pass Yards | under | 0.3351945251646613 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|0ebc6cdc-af2f-4fe0-91cb-eda7363e7201 | underdog | Jalen Brooks | Receiving Yards | under | 0.3343434343434344 | 2026-10-16T04:33:49Z | 2026-10-18T20:05:00Z |
| underdog|0a3812e4-8dc2-47b0-9b32-3490fe349b39 | underdog | Cyrus Allen | Receiving Yards | under | 0.3336734693877551 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|9f2ba4f5-7ac8-406d-b89d-6d792a49e837 | underdog | Daniel Jones | Pass Attempts | under | 0.3335017344329285 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|f91f6288-1b31-4637-bad9-e887cc68a203 | underdog | Cyril Ngonge | Shots Attempted | under | 0.3307692307692308 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|73652f9d-4324-4e95-8866-6aab14c1dbc5 | underdog | Stefon Diggs | Receptions | under | 0.3285714285714286 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|1b70a58f-091a-43a2-90cc-bd3f18029851 | underdog | Luther Burden | Receiving Yards | under | 0.3281706035671761 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|12806d11-1e9e-4a32-8fc2-04028e5904ab | underdog | Daniel Jones | Pass TDs | under | 0.3266041330003657 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7ebc0057-5e8c-4445-9d57-4f16b8dc8a61 | underdog | Rachaad White | Rush Yards | under | 0.3257593259117504 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15780891 | prizepicks | Trey McBride | Rec Targets | under | 0.3234264073571732 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|f05c24fc-78c0-493b-8ce6-9feb3858682e | underdog | Jake Elliott | FG Made | under | 0.3225381400412137 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|db8979e7-b9c1-4ab7-b6f0-fb5b6319c547 | underdog | Tyler Shough | Pass Yards | under | 0.3215315703169221 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|26b1ce38-9ec6-40bc-a226-ae6f49269401 | underdog | Tyler Shough | Completions | under | 0.318659271946434 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|6f78287f-f313-4cac-be1f-ea808ea44528 | underdog | Cyril Ngonge | Shots on Target | under | 0.3162436548223351 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|a6851562-dcda-48d6-8159-45f2f5a7fa37 | underdog | Trevor Lawrence | Pass Attempts | under | 0.3158610361492696 | 2026-10-17T04:25:02Z | 2026-10-18T13:30:00Z |
| underdog|f89af6c6-e75c-473e-80e2-2b566253d4f5 | underdog | Jayden Daniels | Pass Attempts | under | 0.3149988412199163 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|58b5d29c-2d56-4c1a-966b-292e02495e88 | underdog | Pat Freiermuth | Receiving Yards | under | 0.3141555179995734 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|56db0e00-47df-49cf-bbb9-5483053087be | underdog | Mike Evans | Receiving Yards | under | 0.3131898190585049 | 2026-10-17T04:25:02Z | 2026-10-20T00:15:00Z |
| prizepicks|15851333 | prizepicks | Brock Purdy | Pass+Rush+Rec TDs | under | 0.3122548350258745 | 2026-10-17T04:25:02Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|3164163f-7617-40cb-aa56-0856f1e0584b | underdog | MarShawn Lloyd | Rush Yards | under | 0.311954300748184 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|89ccba43-8988-41eb-9a47-90e9764e0d41 | underdog | Jalen Nailor | Receiving Yards | under | 0.3086940844647535 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|72028630-5ab0-4b39-865b-851e65097487 | underdog | Drake Maye | Pass Attempts | under | 0.308375205762582 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|db134f85-1a29-40ce-b046-e6d955c3ef5c | underdog | Tyler Allgeier | Receiving Yards | under | 0.3060913705583756 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15683920 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.3055814338761505 | 2026-10-14T13:48:29Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15682636 | prizepicks | Nico Collins | Recs | under | 0.3053857655203934 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15853485 | prizepicks | Trey McBride | Recs | under | 0.3035924912586596 | 2026-10-17T04:25:02Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|76e1327a-8ef9-47e2-a4fd-e6915d169ac8 | underdog | Austin Ekeler | Receptions | under | 0.303061224489796 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|001117b4-e3d3-4baf-b815-43c0d9d0241b | underdog | Dawson Knox | Receiving Yards | under | 0.3010152284263959 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|33142e30-994f-4234-820f-32a53795bc9a | underdog | Rhamondre Stevenson | Rush Yards | under | 0.2997839502003937 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|897a3c30-9a33-448e-ba83-2f00b649c62e | underdog | Colby Parkinson | Receiving Yards | under | 0.2992094934886594 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|b3cf53a5-8a8d-4067-ba0a-b5c63cadc05a | underdog | Tyler Huntley | Pass Yards | under | 0.2975207005757123 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|ea423145-1184-4eb7-a8a1-bc5d373efcc4 | underdog | Xavier Worthy | Receiving Yards | under | 0.2945142885286981 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|37b6c45d-8682-4cfc-bf3a-9c524647fd13 | underdog | Ray Davis | Rush Yards | under | 0.293939393939394 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|9cb0793c-7471-4c3a-bbb7-1e6541c9efd9 | underdog | Kaleb Johnson | Receiving Yards | over | 0.2923149198915294 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| underdog|964dcae5-96e9-44b6-a27e-ee7fbadaf6a4 | underdog | Nico Collins | Receiving Yards | under | 0.2884463944318267 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|55d0d31c-3f7a-4482-8405-f9a5abe59b9a | underdog | Jake Ferguson | Receptions | under | 0.2876336994087167 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15780903 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.2868282283592709 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|55b47abf-32ed-45e5-a2ec-361f022d0ef9 | underdog | Jonathan Taylor | Rush Yards | under | 0.2867669174203633 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|957b9f0c-82e8-4b2e-91e9-c2d76ca35389 | underdog | Jacoby Brissett | Completions | under | 0.2816213188948928 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|03b6c7bf-e8dc-4440-9a9c-4781de9cc969 | underdog | Trey McBride | Receiving Yards | under | 0.2801520136261292 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|97c11e59-7366-45ed-8dd9-c1601951d2b2 | underdog | DK Metcalf | Receptions | under | 0.2796713355026623 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|d3c3a6e9-5929-4a3e-9088-35799b74f01c | underdog | Matthew Golden | Receptions | under | 0.2775508426244876 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|0b89692a-7da4-43b2-8841-0f0b7a8fa198 | underdog | Xavier Worthy | Receptions | under | 0.2757081291040957 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| prizepicks|15780892 | prizepicks | Jahan Dotson | Rec Targets | under | 0.2756063170022216 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|be56bdad-dd15-4403-bd8a-37130cef1ea1 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.274198166429233 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|2b2b7dd4-892c-46e4-8197-c10b937515c0 | underdog | Quentin Johnston | Receiving Yards | under | 0.2731481033073906 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|b2536732-be9c-4214-a6f4-2f81e42a3bd8 | underdog | Kendre Miller | Rush Yards | under | 0.2727581981048455 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|e588c048-2140-4bc6-8395-1fe1c4865ed9 | underdog | Patrick Mahomes | Completions | under | 0.2708723424371061 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|ccb589e7-381d-4bd3-8ce5-75c94cfddb54 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.2653277501016046 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|1f47c919-c527-40b5-ab71-cf31f50a0f41 | underdog | Kenny Gainwell | Rush + Rec Yards | under | 0.2642696387441816 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|64f22b4b-e554-429d-8ebf-23ecde0e4294 | underdog | Garrett Wilson | Receiving Yards | under | 0.2638139700223881 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|22fb7c91-776f-4678-8ea0-4782ab3c13f1 | underdog | Kayshon Boutte | Receiving Yards | under | 0.2632087138051393 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|4579712a-189f-472a-997c-6afb1156e5d4 | underdog | Jalon Daniels | Pass TDs | under | 0.2623837328593152 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|62b0a1fd-5554-468e-b71a-6536af05538b | underdog | Andy Borregales | Kicking Points | under | 0.2613710015278975 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|60fade79-aff3-4b68-aa9c-674492e039c7 | underdog | Kirk Cousins | Pass Attempts | under | 0.2583489615647822 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|336e268b-874d-4fa7-8ae6-67f79ef07dc2 | underdog | Geno Smith | Completions | under | 0.2581712370698833 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|a7876469-c0e7-4334-98d0-a505f8b8dc80 | underdog | Chris Godwin | Receiving Yards | under | 0.2567496945982092 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a3b24a84-1709-4681-9037-4a36553a61bf | underdog | Christian Pulisic | Shots Attempted | under | 0.2541696707404186 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|1464b0b8-b102-43a6-8a12-ba26d199aaa5 | underdog | Mike Evans | Receptions | under | 0.2538678668382569 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|2cb1c834-ede9-4df9-b962-c10aa177ea95 | underdog | Roschon Johnson | Rush Yards | under | 0.2538441165538871 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|81a2fcab-0a7b-4595-94f8-1b271019cd44 | underdog | Tucker Kraft | Receiving Yards | under | 0.2536667531167488 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|64fa3fb0-371a-4399-a470-4806cd9fa069 | underdog | Jameis Winston | Completions | under | 0.2532280767597126 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c5acba82-935e-474c-987f-00b0cf877447 | underdog | Cam Ward | Pass TDs | under | 0.2512320552021212 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3eba885b-cbea-4a99-beeb-b87dee119f64 | underdog | Brayan Rocchio | Total Bases | over | 0.2479370078740158 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15847764 | prizepicks | Mark Andrews | Rec Targets | under | 0.2478779977630991 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|af90435f-fdf2-4368-aab3-46a55f067a66 | underdog | George Kittle | Receiving Yards | under | 0.2469843361186776 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|7c99b3f0-2889-4f46-9fdc-a4851043a1f1 | underdog | Jacoby Brissett | Pass Attempts | under | 0.2460501997507972 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|d09b90b6-3ab5-4090-b15c-f1ccc808787a | underdog | Cade Otton | Receptions | under | 0.2423514232380079 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|65ef2c13-cfea-42a7-bdbf-93a8550656e2 | underdog | Drew Stevens | FG Made | under | 0.2421453388790657 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| prizepicks|15853484 | prizepicks | DK Metcalf | Recs | under | 0.2416959072778698 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|dd19def6-b779-45f9-a65a-7d64501bc735 | underdog | Quentin Johnston | Receptions | under | 0.241158486606428 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|996a220b-78df-492f-b574-56b82f208efa | underdog | Bryce Young | Rush Yards | under | 0.2405083178181394 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|47f621cf-65ad-4cf7-a06e-a6b003d77434 | underdog | Harold Fannin | Receiving Yards | under | 0.2401698147067272 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|ecd259a7-684f-4fc4-9de3-021052d9f72a | underdog | Austin Ekeler | Receiving Yards | over | 0.2398624069071242 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|bd6f77dd-9654-447d-a5b8-200ee5034760 | underdog | Patrick Mahomes | Pass Attempts | under | 0.2395328228878542 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|f797f059-a1fe-4002-984b-c8fcde57a8e9 | underdog | George Kittle | Receptions | under | 0.2391505701291185 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| prizepicks|15683901 | prizepicks | Tyler Shough | Pass Yards | under | 0.2390376714724932 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|3b44e427-0a34-4278-9647-5dd345b48a85 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.2384675225951728 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|84078f63-d932-45e1-8085-b2f10127c8da | underdog | Caleb Williams | Pass TDs | under | 0.2380544783775852 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7047f00e-c97b-41a5-9426-fc42ecf0639d | underdog | Javonte Williams | Rush Yards | under | 0.2372141038649273 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|3278d2d6-dee3-40eb-ae23-33648c5e2689 | underdog | Tony Pollard | Rush Yards | under | 0.2365680370000403 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|558d40fd-e8d3-4c4b-970e-26160aa67a11 | underdog | Andy Borregales | FG Made | under | 0.2361857173045409 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15847801 | prizepicks | Cade Otton | Rec Targets | under | 0.2340980190600178 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|1a6412e7-b8b2-4de7-ac3e-e7b6a496d3dd | underdog | Rachaad White | Rush + Rec Yards | under | 0.2333044840388567 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|4f039e12-933c-4cbf-8ce1-2398a5a7d6b0 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.2322813554208787 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|5b937d74-8bc4-4193-88e7-26b66a6f3df7 | underdog | Cam Skattebo | Rush Yards | under | 0.2321438168960393 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|587af320-781b-4741-92e5-04e6948efe32 | underdog | James Cook | Receiving Yards | under | 0.2318445501439744 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|a8e80302-8d45-4e80-9ad2-09fefb833a87 | underdog | Kayshon Boutte | Receptions | under | 0.2317193988254039 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15687729 | prizepicks | Trey McBride | Rec Yards | under | 0.2312870372875387 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|97293c96-b557-4318-a29e-8c57e631cc8f | underdog | Adrien Rabiot | Shots Attempted | under | 0.2296299627351812 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|9f3df295-cd38-4008-96cb-747a0cd26511 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.2273552877561371 | 2026-10-16T04:33:49Z | 2026-10-18T13:30:00Z |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9f90af16-920b-43e1-98f4-358f6abe9aa7 | underdog | Drew Stevens | Kicking Points | under | 0.2243861026972581 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|6bc10753-8297-457d-9518-25d4ee1eba65 | underdog | Devaughn Vele | Receiving Yards | under | 0.2240964216381492 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2452706d-bd2d-4083-aa3d-1ce7c6afd13a | underdog | Joey Slye | FG Made | under | 0.2223264379230971 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|86eef5f7-1c9f-400e-9e64-e332b3f79b80 | underdog | Brock Bowers | Receptions | under | 0.2210269090232406 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|3ce9570e-6224-4323-b856-ce4395e0d562 | underdog | Christian Watson | Receptions | under | 0.2209177914243855 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|8e715731-3f0d-44f7-bd65-92f30a2a3194 | underdog | Denzel Boston | Receptions | under | 0.2207129740681275 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|2235514b-6323-4f7a-a8b1-2e779c6ff76d | underdog | Woody Marks | Rush Yards | under | 0.2200136869245151 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|3c286002-320a-40da-90e0-2fb80b6cedb4 | underdog | Colston Loveland | Receiving Yards | under | 0.2198019977147625 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15687737 | prizepicks | Tucker Kraft | Rec Yards | under | 0.2190911706849104 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|eab58938-6da1-4e47-8b95-7bedef7d3321 | underdog | Tyler Warren | Receiving Yards | under | 0.2183291090453837 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|288a501d-2218-456e-b579-837f2ed8ab62 | underdog | KC Concepcion | Receiving Yards | under | 0.2173225179358877 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|88911d68-704d-41c3-afdb-ab87b0d9d340 | underdog | Kyren Williams | Rush Yards | under | 0.2169659386271212 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|d6ba81a0-ee4f-4042-a780-669f46885bf0 | underdog | Cameron Archer | Shots Attempted | under | 0.2167130465780551 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|89f4e5fd-aa0f-4725-bb01-b4467e84a52f | underdog | Jake Ferguson | Receiving Yards | under | 0.2160391354209354 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|8e23fa8c-9ef1-4e37-b3d9-c0d80d78d690 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.2159988775205912 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|15847773 | prizepicks | Denzel Boston | Rec Targets | under | 0.2146212805488722 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|5e43ac6c-63e7-410f-9265-d601fa11e0ad | underdog | Harrison Butker | FG Made | under | 0.214587288997989 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15847780 | prizepicks | Xavier Worthy | Rec Targets | under | 0.2144858553451326 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|0bb0d8c6-de62-4d8f-b2fd-9c0698322f40 | underdog | Jonnu Smith | Receiving Yards | over | 0.2128953898612049 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| underdog|87524ce9-39ae-4715-bbc9-6772bae3be7c | underdog | Woody Marks | Rush + Rec Yards | under | 0.2128701235736237 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|4966271a-7fe7-4e01-8ada-3d43f0e7aeec | underdog | Jalon Daniels | Pass Attempts | under | 0.2125309049009038 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|d42daadd-0519-42a1-8d43-b0972d9b89f8 | underdog | Chidera Ejuke | Shots Attempted | under | 0.2123932710072795 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| underdog|351db95d-f239-4fa0-8c57-a06f0d7572e3 | underdog | Jakobi Meyers | Receiving Yards | under | 0.2116111373551161 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|55135446-7d6b-4b06-940e-05edcab2eca3 | underdog | Geno Smith | Pass Attempts | under | 0.2099820096977522 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15865276 | prizepicks | Walter Benítez | Goalie Saves | under | 0.2092334520294531 | 2026-10-18T04:33:13Z | 2026-10-18T09:00:00.000-04:00 |
| underdog|4bde3da4-3710-45e9-9628-65c60268b6d0 | underdog | Yan Diomande | Shots on Target | under | 0.2075871885935983 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| underdog|7548004b-77ba-4f33-8568-df421731560b | underdog | DK Metcalf | Receiving Yards | under | 0.2059463905645467 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|02c693a5-9e1a-4d03-bb4e-b81f2f934889 | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.2055807759197376 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|22e7f08c-673a-40d5-9db8-3afc5bac20a2 | underdog | Daniel Carlson | FG Made | under | 0.2050604333166797 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|f141b6ee-8c44-43fe-98fd-54977396d246 | underdog | C.J. Stroud | Pass Attempts | under | 0.2050267870602162 | 2026-10-17T04:25:02Z | 2026-10-18T13:30:00Z |
| underdog|dc679d8f-b4f8-4421-8da4-89177cc127d2 | underdog | Darnell Washington | Receptions | under | 0.2045237698362181 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e1f1f3d3-ecd9-4c5a-887b-590de194681b | underdog | Pablo Pagis | Shots on Target | under | 0.2043874699843726 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|69bfc8c2-fae1-4e15-95fa-cf1f9f22fb01 | underdog | Juwan Johnson | Receiving Yards | under | 0.2034750253722937 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c1e51a5d-3fef-483b-8bbe-998958ea8781 | underdog | Tremaine Edmunds | Sacks | over | 0.2019840925817287 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|bbd58c2e-96a7-4138-a392-dba610056bd4 | underdog | Keenan Allen | Receiving Yards | under | 0.2018763061455277 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|98996094-5697-4eff-bf94-2d1a44236fb1 | underdog | Cade Otton | Receiving Yards | under | 0.2003715604441809 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|2241e611-67e0-476c-a3fc-6a3f0fd6d8a6 | underdog | Christian McCaffrey | Rush Yards | under | 0.1997397401763914 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|d79a2dc9-8fd9-482b-a1cd-829342024ae7 | underdog | Michael Wilson | Receiving Yards | under | 0.1995963998953762 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|f1ef8ef5-e398-454d-8097-cc5ecb56e4ca | underdog | Gunnar Helm | Receiving Yards | under | 0.1988442240792169 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b03fb4e6-13b7-45b2-9c97-c69989117ea4 | underdog | El Bilal Toure | Shots Attempted | under | 0.1988128603077319 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|43ddbffa-1a19-4b53-964b-421a762cd777 | underdog | Sheldon Rankins | Sacks | over | 0.1987339328577649 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|388ee26b-e09a-417b-8251-3f9b51a3f7fc | underdog | Ruke Orhorhoro | Sacks | over | 0.1971263312937586 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| prizepicks|15865457 | prizepicks | Oliver Baumann | Goalie Fantasy Score | under | 0.197049049472829 | 2026-10-18T04:33:13Z | 2026-10-18T11:30:00.000-04:00 |
| prizepicks|15853496 | prizepicks | Matthew Golden | Recs | under | 0.1967649826927433 | 2026-10-17T04:25:02Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|ed222574-5695-447d-b3eb-1881e6688bcd | underdog | Colby Parkinson | Receptions | under | 0.1957637012704456 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|b036d2b0-8349-46e6-9397-ac6048d88313 | underdog | Malik Nabers | Receiving Yards | under | 0.1956173604195319 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|e46f2c75-efcb-49d2-8ae7-d5b69c2fcd24 | underdog | Marvin Harrison | Receiving Yards | under | 0.1941604442781539 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15723434 | prizepicks | Drake London | Rec Targets | under | 0.1937930998385586 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|b7f7a37c-d5f4-4a43-8530-a04c69c6b14c | underdog | Austin Booker | Sacks | over | 0.1934650835762503 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15851473 | prizepicks | Cam Ward | Pass TDs | under | 0.1921134521481649 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|a0655086-c492-42a7-a691-848bb3c2821d | underdog | Oier Zarraga | Shots Attempted | under | 0.191979016047231 | 2026-10-18T04:33:13Z | 2026-10-18T10:30:00Z |
| underdog|3b1601ab-4da3-419a-ad2d-b8fc6a0c72d5 | underdog | D'Andre Swift | Rush Yards | under | 0.191933575853321 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| prizepicks|15847765 | prizepicks | Zay Flowers | Rec Targets | under | 0.1917945474216921 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|9f9d5757-685c-4d6f-96f7-b26272694512 | underdog | Jameis Winston | Pass Attempts | under | 0.1916782337083062 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|7256e676-627a-40ac-a9e4-3a7b4113b44a | underdog | Derrick Henry | Rush Yards | under | 0.1903353082826653 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|dd38c784-2201-44d7-8db0-602989b6df33 | underdog | Patrick Mahomes | Pass TDs | under | 0.1902228449795199 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|93428530-bedf-4a8b-90a2-1ac2ac543d3c | underdog | Austin Hooper | Receiving Yards | over | 0.1896624466307463 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|d1b9e310-3626-4c4b-93b9-afcc60573d90 | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.1895325847825839 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|bc8f8665-44a5-4fee-b33f-a100ab140bf7 | underdog | Braelon Allen | Receptions | under | 0.1890078110240539 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|9e0ab8b4-0f2c-4fd3-9658-06695888dcaa | underdog | Germie Bernard | Receptions | under | 0.1864004345721859 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|9bab758e-34cc-4fb3-8c31-200293b9885b | underdog | Jahan Dotson | Receptions | under | 0.1860641735232708 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|5349d44c-86c6-4858-8d42-fd22cb4b4144 | underdog | Trey Smack | Kicking Points | under | 0.1857794312901399 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|20084900-7684-47cf-87af-8b33e0b26606 | underdog | Akheem Mesidor | Sacks | over | 0.1855234938178657 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|a7151a40-c239-40f6-ab97-72b2ba31e88f | underdog | Ryan Flournoy | Receptions | under | 0.1852114442331075 | 2026-10-15T04:38:48Z | 2026-10-19T00:20:00Z |
| underdog|2d67b31b-426a-4d89-9411-34805433abde | underdog | Jordan Love | Pass Attempts | under | 0.1847182497807716 | 2026-10-16T04:33:49Z | 2026-10-19T00:20:00Z |
| underdog|fac7e2c6-beba-4af2-82e3-2410210f398a | underdog | Ted Hurst | Receiving Yards | over | 0.1845460243399048 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|ac431284-39d4-4eaa-93c8-0c7d717f3724 | underdog | CJ Donaldson | Rush Yards | under | 0.1843150257097658 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|61f137dd-f9df-4ebb-8e86-98db8db8725f | underdog | Braelon Allen | Rush + Rec Yards | under | 0.1841854424134562 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|260c2f3e-c694-4e71-8069-723dd7a5e1f4 | underdog | Keaton Mitchell | Receiving Yards | under | 0.1818287812022979 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|f2c130f3-8554-4655-9630-e15e61288513 | underdog | Adin Huntington | Sacks | over | 0.180071670037286 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|35f63def-4a3d-4ada-a3e4-2db2523344f5 | underdog | Malcolm Koonce | Sacks | over | 0.1793224687544823 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|f093053a-9984-4287-b61b-8877f650409f | underdog | Terry McLaurin | Receiving Yards | under | 0.1786940622638401 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|7ef41105-d820-4bef-9671-1fcf52c67ea4 | underdog | Alvin Kamara | Rush Yards | under | 0.1782589957308764 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|b3eec42f-7778-4279-9037-8b1faaa16fe6 | underdog | Chris Boswell | FG Made | under | 0.1781179386493 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|4a1a2473-8189-47db-af2d-b09c74cfa9a9 | underdog | Travis Kelce | Receiving Yards | under | 0.1780243089932398 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|f5d389a9-6382-4527-999b-2455ec093edd | underdog | Trey Smack | FG Made | under | 0.1778895553592853 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|cbe17bf2-6134-47ab-8593-df5097a89b38 | underdog | Kyle Pitts | Receiving Yards | under | 0.177761468938025 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|556cfe0e-8dbc-44f9-b74c-a5180c4a28a1 | underdog | Dak Prescott | Pass TDs | under | 0.1773583982428295 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15687727 | prizepicks | Tyler Warren | Rec Yards | under | 0.1771042324952298 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|6772e16a-1bdf-453a-a28b-0c748bbea7e0 | underdog | Tyler Loop | FG Made | under | 0.1770424297998158 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|348fcdfb-ac06-48c5-863c-d93dc02e8d06 | underdog | Tyler Huntley | Pass Attempts | under | 0.17648093551008 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|56ef781e-69f5-4c15-ba2f-c0373967b1a9 | underdog | Cairo Santos | FG Made | under | 0.1764682504265735 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2b638c80-9720-4cdd-aebf-7b5548d8cb19 | underdog | George Pickens | Receiving Yards | under | 0.1763502988084485 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|44297deb-d9d9-4e65-8f5c-0a24cc2920eb | underdog | Josh Downs | Receiving Yards | under | 0.1752931823371081 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|3005c7a2-7bf6-413d-a5d9-e48e2366cec1 | underdog | Dani Dennis-Sutton | Sacks | over | 0.1748527974565202 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|4425d876-aca2-4bcd-9b13-bc53ed006932 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.1746758986095545 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|16968f36-f60b-4f9d-b8d2-763e3c120d94 | underdog | Germie Bernard | Receiving Yards | under | 0.1745930643878693 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|814ee460-585c-4ad1-a936-c6436b44e3f3 | underdog | Cameron Thomas | Sacks | over | 0.1745254761903263 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|719cd5cb-7cbc-4fa1-965b-403e0a8fb6df | underdog | Denzel Boston | Receiving Yards | under | 0.1743570639527935 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|33b49686-70b6-4d7a-929f-8464f1df5f81 | underdog | Zachariah Branch | Receiving Yards | under | 0.1734890670839399 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|393bbdfb-4861-4029-a382-9bbdbe7ca088 | underdog | James Cook | Rush + Rec Yards | under | 0.1732532918133281 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15683996 | prizepicks | Tony Pollard | Rush Yards | under | 0.1730948228779903 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|e4a4fc66-4303-444a-a042-0fd7b0c1c3fd | underdog | Garrett Wilson | Receptions | under | 0.1729462976023883 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15780900 | prizepicks | Javonte Williams | Rec Targets | under | 0.172839087916253 | 2026-10-15T04:38:48Z | 2026-10-18T20:20:00.000-04:00 |
| prizepicks|15851098 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.1719002423718824 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|6d0f6de1-f8d0-4710-ad03-db8b6581deba | underdog | Tre Tucker | Receptions | under | 0.1718972339321287 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| prizepicks|15780913 | prizepicks | Devaughn Vele | Rec Targets | under | 0.1717434204275167 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|d4441fdc-3383-4945-bec4-cb7ce383c6cc | underdog | Blake Corum | Rush Yards | under | 0.1710876513389372 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|1172b325-6b55-4594-8b09-72d194621584 | underdog | Kenny Gainwell | Receptions | under | 0.1709756603793514 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15684002 | prizepicks | Javonte Williams | Rush Yards | under | 0.1702978224716673 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|926047f6-6919-45a0-b3ef-9cb03a59cc77 | underdog | Daniel Maldini | Shots Attempted | under | 0.1702392253406577 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|11a4e7fa-7b14-445d-832a-1ae8e64b713c | underdog | James Cook | Rush Yards | under | 0.1689159382095952 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|70f924d8-5beb-498c-bed1-313b001e69b2 | underdog | Matthew Stafford | Rush Yards | over | 0.167094951302097 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|62b748fa-2265-48e7-adc9-ee29cbac6774 | underdog | Quinnen Williams | Sacks | over | 0.1665277852787891 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| prizepicks|15865455 | prizepicks | Oliver Baumann | Goalie Saves | under | 0.1664539064237636 | 2026-10-18T04:33:13Z | 2026-10-18T11:30:00.000-04:00 |
| underdog|4efa3762-a676-4d5b-a1d1-3a3748385fcf | underdog | Joey Slye | Kicking Points | under | 0.1655511449168644 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|edd91651-25e0-40c7-a5df-a9a5e97e0ea6 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.1652386344384269 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|cdd0afaa-37cb-44a8-9b0f-6062b9ac7b04 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.1652008230262183 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|798d0814-996c-4b59-a797-8e59ac6267bd | underdog | Charles De Ketelaere | Shots Attempted | under | 0.1642402261747024 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|7e651f49-ebd8-4959-b034-0f744eeb6cbe | underdog | Bradley Chubb | Sacks | over | 0.1640663237105195 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| prizepicks|15687714 | prizepicks | Devaughn Vele | Rec Yards | under | 0.1635409176999198 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|0e4a16ef-8049-4981-bd38-f982402f18ef | underdog | Tyler Allgeier | Receptions | under | 0.1635336480283015 | 2026-10-17T04:25:02Z | 2026-10-18T20:05:00Z |
| underdog|defb1ea9-2f2e-493f-9489-ac22036e6926 | underdog | Jacob Martin | Sacks | over | 0.1635144331821845 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15847802 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.1635017830344741 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|6418499a-3f1a-427a-b75a-ab9b30d9ef67 | underdog | Jalen Royals | Receptions | under | 0.1630837861667569 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|3a141382-4531-4a2a-8e01-1c61560726d3 | underdog | Arik Armstead | Sacks | over | 0.1630079661915948 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|0d3c4ee1-ca6a-40eb-84b9-c8e3b65db064 | underdog | Josh Allen | Pass TDs | under | 0.1627144064890061 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|1836840b-7d56-4cff-848e-0d0a36af0caf | underdog | Jo Adell | Total Bases | over | 0.1627047803858641 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15847789 | prizepicks | Colby Parkinson | Rec Targets | under | 0.1625444821185782 | 2026-10-17T04:25:02Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|b1011fa5-ab4c-4310-9b46-4ae8ffcb2813 | underdog | Pat Freiermuth | Receptions | under | 0.1624330256402943 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|013933f9-7688-4806-bd95-a091bbc7fda0 | underdog | CJ Donaldson | Rush + Rec Yards | under | 0.1621679287747108 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|14996e29-0463-4ef6-b4f4-d2d2a3562e45 | underdog | Gustavo Varela | Shots Attempted | under | 0.161107508887347 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|b0f4c2e4-56c2-4e92-87d5-559f7bf6dc99 | underdog | Isac Lidberg | Shots Attempted | under | 0.1603759342621833 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|8426ffcc-54dd-46e7-815c-4c2d33a2c2f6 | underdog | Cameron Heyward | Sacks | over | 0.1592062096530985 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|12aee6ac-479d-4ced-9c58-6052536674d4 | underdog | Kaleb Johnson | Receptions | over | 0.1591361915023518 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| underdog|5ccd8c1c-4078-4c1e-9029-820aee35e94a | underdog | Terry McLaurin | Receptions | under | 0.1569422183629093 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15684004 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.1568613213703028 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|ace86639-0194-42ac-b31c-a95cfebe4138 | underdog | Arvell Reese | Sacks | over | 0.1560200642466723 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|a7d87597-5760-45f1-80bd-3998c0a80118 | underdog | Victor Mesa | Runs | over | 0.1558586762075134 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|8e6b4547-0422-442f-abb9-55686caf27af | underdog | Harrison Butker | Kicking Points | under | 0.1551636721561381 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|0eaefbd9-7d92-40f7-8f20-72362f00cba0 | underdog | Brian Robinson | Receiving Yards | over | 0.1551458817458766 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|f659de6c-1bd6-423f-935d-55d8524379fe | underdog | Tucker Kraft | Receptions | under | 0.1549622277027542 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|c242a3ff-edb7-4994-a134-6ebf8d455443 | underdog | Tyler Allgeier | Rush Yards | under | 0.1543590123027717 | 2026-10-17T04:25:02Z | 2026-10-18T20:05:00Z |
| underdog|f9f01d9d-4649-4d71-a406-82983c7a37e9 | underdog | Kingsley Enagbare | Sacks | over | 0.1542063107975032 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|7ca2d8ca-b26c-4dc3-bb49-db1ddb56b143 | underdog | Emeka Egbuka | Receiving Yards | under | 0.1530574072708483 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15780912 | prizepicks | Chris Olave | Rec Targets | under | 0.1529999045984812 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|3d35d1f0-d372-4c69-8dc0-d98e71209f6a | underdog | Deshaun Watson | Rush Yards | under | 0.1528328895313248 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15850806 | prizepicks | Ladd McConkey | Rec Targets | under | 0.152790440741203 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|d4056f53-7dd9-4f8c-a0d3-4761e1cfc3f8 | underdog | Christian Pulisic | Shots on Target | under | 0.1526905672871086 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|5377df92-8dad-4174-bfd5-3c4b13011dab | underdog | Zay Flowers | Receptions | under | 0.1526649177287347 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|5693a7a9-10ae-4fbc-9aa9-ca340cfc5634 | underdog | Parker Washington | Receiving Yards | under | 0.1516952925945273 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|2fa8f927-9bbb-4498-8148-e0d4249d23de | underdog | Charlie Kolar | Receiving Yards | under | 0.1514974397075691 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|fe7699d1-ef91-4af1-b659-848a9fc6f064 | underdog | Jonathan Taylor | Receptions | under | 0.1510995727170617 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15693996 | prizepicks | Jordan Love | Pass Attempts | under | 0.1509099959443077 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|787cfee7-e5f9-4073-86cb-7dde9bd9f920 | underdog | Rome Odunze | Receptions | under | 0.1503965933444857 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|225e14a5-6e0d-41dc-a0f7-2eebb1a6a47d | underdog | Kyren Williams | Rush + Rec Yards | under | 0.1501032642351486 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|64b096af-2c87-4cb7-9226-957a8f19a858 | underdog | Isaiah Davis | Rush Yards | under | 0.1500986431788202 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|08060a30-1919-4384-8fec-3664a3763d6b | underdog | Anhelina Kalinina | Double Faults | under | 0.1500166856541865 | 2026-10-18T04:33:13Z | 2026-10-18T04:30:00Z |
| underdog|0b9e15a9-6b9d-4c58-97bc-d92f418c1216 | underdog | Marvin Harrison | Receptions | under | 0.1496793293582651 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|b9124811-9067-49e8-a49f-16ad145f87a5 | underdog | Elic Ayomanor | Receptions | under | 0.1496107501484767 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|739c4399-99e6-40e7-b3fb-488352619922 | underdog | Kwity Paye | Sacks | over | 0.1489921056725202 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| prizepicks|15780919 | prizepicks | Calvin Ridley | Rec Targets | under | 0.1484375816644969 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15874224 | prizepicks | Stefon Diggs | Rec Targets | under | 0.1484182869513028 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|ba599ce7-3e45-49a3-9e54-67da41d570d5 | underdog | Josh Sweat | Sacks | over | 0.1481702398314603 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|f92bb267-f43f-4bc5-8e8d-39ccf32dc5d8 | underdog | Quinshon Judkins | Rush Yards | under | 0.1479890377462749 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15723441 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.147919974847375 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|c91b0b52-f16c-4741-9162-c7b415caa67b | underdog | Mason Taylor | Receptions | under | 0.1473123998249675 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|9dcf07e6-d358-4479-aa3a-72b18cb3d208 | underdog | Emeka Egbuka | Receptions | under | 0.147192188115118 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c8daf8e0-a220-4bf3-8012-86ff17ec6759 | underdog | Drake London | Receiving Yards | under | 0.1469107209479405 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c78d2d7e-fc7b-4045-960d-a83cf37fa511 | underdog | Braelon Allen | Rush Yards | under | 0.1464451461046729 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|4c93b1d0-67d8-4217-a3cc-8c4fadc1e5eb | underdog | Randal Kolo Muani | Shots on Target | under | 0.146371584074744 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|f0693d1f-77d2-4c6f-b113-72732d18aabe | underdog | Deone Walker | Sacks | over | 0.1463620423828019 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|f6e3d970-b1bc-4a40-8375-c832832a7e6d | underdog | Matthew Golden | Receiving Yards | under | 0.1463499623163882 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|854d1314-7df8-46b5-b6e5-98995ded8435 | underdog | Kyle Pitts | Receptions | under | 0.1462561148496879 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|307f6471-232a-406a-b1e0-d434edf5d9fa | underdog | Harold Fannin | Receptions | under | 0.1460900499920627 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|08138ecc-9a3a-4de5-bee8-ebf44bb6e218 | underdog | Ladd McConkey | Receiving Yards | under | 0.1460288583264317 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|cca2ed2f-db70-47b0-8341-12a426f87e82 | underdog | Jordan Love | Rush Yards | under | 0.1456011433595847 | 2026-10-15T04:38:48Z | 2026-10-19T00:20:00Z |
| prizepicks|15847769 | prizepicks | Chuba Hubbard | Rec Targets | under | 0.1453375534598217 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15780918 | prizepicks | Garrett Wilson | Rec Targets | under | 0.1447888649371511 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|da3204f8-50c1-4d25-a7b1-04cabc62f5f9 | underdog | Drake Maye | Pass TDs | under | 0.1445611797481127 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a7bd2b23-0b91-48d1-a35f-c6fdf0eb80c9 | underdog | Maxence Caqueret | Shots Attempted | under | 0.1445287009355309 | 2026-10-16T04:33:49Z | 2026-10-18T13:00:00Z |
| underdog|2be59240-69ee-4552-b9d2-af3c4d18e2e7 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1444614976184334 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|b8f991b1-6d42-4eca-8459-a97c54b98c18 | underdog | DeVonta Smith | Receiving Yards | under | 0.1442319326969706 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|fc83c18b-331a-4c3a-800e-84a83437f162 | underdog | Darren Waller | Receiving Yards | under | 0.1442073115479826 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|979374c1-a350-4ee7-b43e-db4ec981b56a | underdog | Darius Alexander | Sacks | under | 0.1441860465116279 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|783506bd-7504-4f20-abbb-7d0a44b68f7a | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.1438943023890713 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|821a7b9b-2f2a-49a4-91b5-7c3967f97b8a | underdog | Rhamondre Stevenson | Receptions | under | 0.143852018073898 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|22abbbd9-004a-4caf-9158-1210a35b4264 | underdog | Blake Corum | Rush + Rec Yards | under | 0.143617351343874 | 2026-10-17T04:25:02Z | 2026-10-18T20:05:00Z |
| underdog|1edbd709-9e5b-4071-9070-ea2ad5a88144 | underdog | Matthew Stafford | Pass TDs | under | 0.1434007846415811 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|aae23a7b-4d1f-4a0e-a93c-01448b17e9f4 | underdog | Tyler Warren | Receptions | under | 0.1431750538962589 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|4626afd9-b955-49c7-9d7d-784b4abe46a2 | underdog | Cam Little | Kicking Points | under | 0.1428729801196245 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|3965bd36-527e-4594-964f-60b0ed7be577 | underdog | Tyler Bass | Kicking Points | under | 0.1427145703959643 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|36f1f660-ed1d-4f1f-b5e8-ea3850ac8a9a | underdog | Malik Nabers | Receptions | under | 0.1426361824714577 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a9f52e1d-31a3-4e43-9a36-bf815f099b68 | underdog | Keinan Davis | Shots on Target | under | 0.14228872194442 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| underdog|5d4665f9-74a3-4a65-81ad-d3f749ebcecb | underdog | Chris Rodriguez | Receiving Yards | over | 0.1413236062697087 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|e51c7ebf-108e-4509-9e3a-2a684b2bb5f8 | underdog | Mark Andrews | Receiving Yards | under | 0.1406615144072164 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13976081 | prizepicks | Jalen Brunson | Rebounds | over | 0.1400370452709755 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|be0cfc2f-9087-4d8f-bb9c-153491bbdc7f | underdog | Rome Odunze | Receiving Yards | under | 0.1389101828136392 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|6e1288b7-8347-4087-aae0-ad3a667726b5 | underdog | Jalen Brooks | Receptions | under | 0.1386404103734755 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| underdog|017e6b0f-06ca-4394-a658-6a69c27baa4f | underdog | Wan'Dale Robinson | Receptions | under | 0.1382017927383453 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e368a210-c3d2-42ae-ad9e-d24d3f8e1835 | underdog | Cam Little | FG Made | under | 0.1379148774693905 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15780914 | prizepicks | Juwan Johnson | Rec Targets | under | 0.1378607992287116 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15847766 | prizepicks | Dalton Kincaid | Rec Targets | under | 0.1374896906268389 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|53eda10b-bf8c-4c6f-85bc-22a77273c413 | underdog | Brock Purdy | Pass TDs | under | 0.1373225827661014 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|c092aea7-be99-4d53-92a1-4287b0383d0d | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.1372262773722627 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| underdog|336272c0-48a1-46c6-b423-233bd0d5dc71 | underdog | Isaiah Likely | Receiving Yards | under | 0.1369634294565795 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2e8b6c23-5daa-4495-8d66-abb23106897c | underdog | C.J. Stroud | Pass TDs | under | 0.1362461611569514 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|4896f80d-1ab3-4fc0-9010-da8e659ab4f4 | underdog | Dallas Goedert | Receptions | under | 0.1362441192621287 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|c907f46a-2e4e-4dcc-a2b7-541fd6d3d654 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.1360626149331018 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15847771 | prizepicks | Jalen Coker | Rec Targets | under | 0.1358304898052958 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|db7dd896-e5a1-4272-a8f9-e206c468ff04 | underdog | Kirk Cousins | Pass TDs | under | 0.135607422106787 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|04a42d00-fef3-4785-8749-86d545d780e9 | underdog | MarShawn Lloyd | Receptions | under | 0.1354703699526813 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|e786d73e-4f83-4dbb-afbf-0931cb76d39d | underdog | KC Concepcion | Receptions | under | 0.1354000859722411 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|0e1dd9cb-4ac6-440c-ab72-589ce1b98411 | underdog | Jayden Daniels | Pass TDs | under | 0.1352637925651718 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|256f9f21-5a05-48e7-97c3-c2fb50ee0eb4 | underdog | CeeDee Lamb | Receiving Yards | under | 0.1351589551748778 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15853494 | prizepicks | Christian Watson | Recs | under | 0.1351215288543125 | 2026-10-17T04:25:02Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|7953d712-5486-480c-a01f-230ae90ec0fe | underdog | Amine Gouiri | Shots Attempted | under | 0.135080648820973 | 2026-10-16T04:33:49Z | 2026-10-18T13:00:00Z |
| underdog|a66691ae-d152-4253-a077-0c537bcd1542 | underdog | Ryan Fitzgerald | FG Made | under | 0.1350263003861453 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15850808 | prizepicks | Quentin Johnston | Rec Targets | under | 0.1345663658370324 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|eab957f9-6066-495d-af08-31e77a77a82b | underdog | Cairo Santos | Kicking Points | under | 0.1345165350732787 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|a0f696cf-0e87-4602-aae4-c01e2f047aaa | underdog | Daniel Carlson | Kicking Points | under | 0.1326359077820521 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|edbcc8b0-a15c-455e-9269-b75ae7cf7782 | underdog | Darnell Mooney | Receptions | under | 0.1326182860090983 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|62bca386-de5c-4a99-a3a8-ab50e4c7ca48 | underdog | DeVonta Smith | Receptions | under | 0.1326079739127544 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|e28679b2-79b4-439a-98e4-5784e0c4a6d5 | underdog | Brandon Aubrey | FG Made | under | 0.1322309173028082 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|e03e5d9c-a2d2-4c2d-85b0-9a58b94efee3 | underdog | Nick Folk | FG Made | under | 0.1315878843452703 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|cacb937b-5573-451d-b0be-69a2b0b60065 | underdog | Carnell Tate | Receiving Yards | under | 0.1315205412070208 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|98e704c2-ee80-41dd-8696-b926d68199f1 | underdog | Brenton Strange | Receptions | under | 0.1314302019946471 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|06608b98-dae4-4264-9356-49baaa077485 | underdog | Javonte Williams | Receptions | under | 0.131226019827754 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|aa16d9d2-ba4f-4ae2-b5d8-93534e748fa9 | underdog | Kimani Vidal | Receptions | under | 0.1309120655386291 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|9ddd90bd-b4e8-4aca-951b-19da86b4efb3 | underdog | Alvin Kamara | Rush + Rec Yards | under | 0.1308056672206613 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| prizepicks|15847785 | prizepicks | Tre Tucker | Rec Targets | under | 0.1303751415769006 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|15847774 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.1301253218943365 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|7f9f2285-0db9-46f2-a055-56a9af5056ba | underdog | Mark Andrews | Receptions | under | 0.1300715606645004 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|4507f75b-62a8-4d24-864c-b16306900ae6 | underdog | Mason Taylor | Receiving Yards | under | 0.12893507180889 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|15831722 | prizepicks | David de Gea | Goalie Saves | under | 0.1282253765035247 | 2026-10-17T04:25:02Z | 2026-10-18T09:00:00.000-04:00 |
| underdog|012f88fa-dbfc-4018-ad7d-3b5db19c4aa6 | underdog | Jake Elliott | Kicking Points | under | 0.1281943158954887 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| prizepicks|15727075 | prizepicks | Nick Folk | FG Made | under | 0.1279848948565908 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|c1b41d0e-94f1-4bfa-b41a-d0442ef792b8 | underdog | Jonathan Aranda | Total Bases | over | 0.1276993841116396 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|c3d8d8a1-a24f-402f-bc51-2d80ecc42496 | underdog | Malachi Fields | Receiving Yards | under | 0.1276186276712521 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|6e75dfba-c511-4e11-8e92-7187de64254f | underdog | Matthew Stafford | Pass Attempts | under | 0.1275798957866172 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|46798cc6-8aa3-43ce-af09-f7683d83c020 | underdog | Rueben Bain | Sacks | under | 0.1271062271062271 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|516e9821-b698-4d06-be1f-12c949cbaaba | underdog | Jalen Coker | Receptions | under | 0.127008450964096 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|cf78a44e-7e23-4e7a-b5dd-683c503f263e | underdog | Lassine Sinayoko | Shots Attempted | under | 0.1267965016605029 | 2026-10-18T04:33:13Z | 2026-10-18T15:15:00Z |
| underdog|5910468c-7a40-40a7-9c7a-822b40c930ae | underdog | Jadeveon Clowney | Sacks | over | 0.1267244566891236 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|6c3d3386-5e6d-45ca-bb2d-6b8f9ddb5fe6 | underdog | Darren Waller | Receptions | under | 0.1266185476584086 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0ad160cb-61ca-4f88-b6e1-385688a4a415 | underdog | Tyler Goodson | Receiving Yards | over | 0.1266180738693994 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| underdog|98eb4bd9-3ce4-4ead-9a67-8e8b017e1129 | underdog | Devaughn Vele | Receptions | under | 0.1241941386212868 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15874226 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.1239452842800243 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|0b212081-ba75-4774-b171-0e659a70b7b8 | underdog | Mitchell Evans | Receiving Yards | over | 0.123705558826677 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|115d6e48-ab34-4b34-a1b4-7e5531bd3ed7 | underdog | Roschon Johnson | Receiving Yards | over | 0.1232395995160587 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|02765c67-cf07-441f-ba67-bf575f2164d5 | underdog | Darius Cooper | Receiving Yards | over | 0.123154957314534 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|3afb27a3-15bc-4eaa-99d9-92f154467b27 | underdog | Jalon Daniels | Rush Yards | under | 0.1230930511245803 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|48803a8f-2252-443d-b2ac-6fc8a08b503c | underdog | Josh Maja | Shots on Target | under | 0.122712670505105 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|60be5b7a-e9d5-4c30-a9d2-4dd2f68522ab | underdog | Maliek Collins | Sacks | over | 0.1226547552543408 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|12a4bd26-aea2-4bc5-8bf6-80a2da1391f6 | underdog | Parker Washington | Receptions | under | 0.1226055683366299 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|cbc358c6-a231-4ed5-ae8d-ea54c4788fad | underdog | Nick Folk | Kicking Points | under | 0.1224895958421046 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|7fbb564b-5dd5-4133-be7d-49ff13a15498 | underdog | Isac Lidberg | Shots on Target | under | 0.1221446411506522 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|15687728 | prizepicks | DK Metcalf | Rec Yards | under | 0.1219425927990364 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|ef8b7afe-0b3f-4463-b0d6-676bbfeda84d | underdog | Aaron Rodgers | Rush Yards | over | 0.1218847680556042 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|c6771fa7-8a0a-4674-b34a-597d2d5084af | underdog | Chuba Hubbard | Receptions | under | 0.1217008955571709 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|795c9d09-fdb5-4b73-879b-4c1bdef593ca | underdog | Gustavo Varela | Shots on Target | under | 0.1216821892215763 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| prizepicks|15847775 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.1214999041559989 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|10b93328-026b-47bf-bfd8-f8b15aca5389 | underdog | Rassoul Ndiaye | Shots Attempted | over | 0.1211318755643113 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|adcaf360-93a2-4f55-9119-a65df8dfb1a1 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1208476483328063 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|9c3ad746-1376-4173-a364-a01ac7ca9168 | underdog | Lukas Van Ness | Sacks | over | 0.1206696724802429 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|e5d31b73-3312-4d80-bd21-fd95a686cced | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.1205725435568393 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|c3cd8549-9116-4fa8-b314-a8a76316cc13 | underdog | MarShawn Lloyd | Receiving Yards | under | 0.1196166359815052 | 2026-10-15T04:38:48Z | 2026-10-19T00:20:00Z |
| underdog|111430f8-7f07-467a-84be-620dba781de3 | underdog | Paul Mendy | Shots Attempted | under | 0.119250767652726 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|88fdb9fe-fb46-452b-8413-4837508895dc | underdog | Chris Olave | Receiving Yards | under | 0.1190278151800631 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e22c3eeb-8758-4db7-be02-2f6132883440 | underdog | Jalen Coker | Receiving Yards | under | 0.1189723975464867 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|167fafad-6e4e-4bfd-a2f8-9deb5260e801 | underdog | Omarion Hampton | Receiving Yards | over | 0.1188186627850744 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|7d4f9f65-df5a-4fb8-9244-6a8393a8f51d | underdog | Isaiah Williams | Receptions | under | 0.1183040508694249 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|f0953b25-349b-4f07-a55e-1d3b0b3ab112 | underdog | Justice Hill | Receptions | under | 0.117422104484156 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|13976095 | prizepicks | Cade Cunningham | 3PTM | over | 0.1168098507846668 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|e59b3ad1-738f-4c6c-8420-e5f29f3afc9e | underdog | Keaton Mitchell | Rush + Rec Yards | under | 0.1166591398283685 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|e7951ede-9a81-46ae-b047-1245e22c9633 | underdog | Tyler Bass | FG Made | under | 0.1158854415361276 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|3bfe6e8e-ecf0-4401-934c-b465a571b60b | underdog | Laquon Treadwell | Receiving Yards | under | 0.1140671035635229 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|7a6c047d-67df-434d-8d3f-413cf5e26ce5 | underdog | Adam Daghim | Shots Attempted | under | 0.1139170725235312 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|15847797 | prizepicks | Darnell Washington | Rec Targets | under | 0.1134070485495603 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|923a9016-3dff-40b2-b5ba-f1989e9adbc1 | underdog | Woody Marks | Receiving Yards | under | 0.1131482734714991 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|4f312116-4c30-4afb-8360-91988eec03a8 | underdog | Jurgen Ekkelenkamp | Shots Attempted | under | 0.1130963081715438 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| prizepicks|15831721 | prizepicks | Jean Butez | Goalie Saves | under | 0.1123784361908025 | 2026-10-17T04:25:02Z | 2026-10-18T09:00:00.000-04:00 |
| underdog|268e3409-919a-4f99-a317-228f55145227 | underdog | Kenny Gainwell | Receiving Yards | under | 0.1119350062186287 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|57ae8575-3971-4e6c-b018-7f47386290d7 | underdog | Luther Burden | Receptions | under | 0.1117894941841016 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|9a80bc3d-09a3-4074-a6c0-45a45290843f | underdog | Puka Nacua | Receptions | under | 0.1117839507567785 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|16defe0a-6f36-4aab-a4ae-d876f1776b8d | underdog | Derrick Henry | Receptions | under | 0.1117039066014773 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15868242 | prizepicks | Laura Samson | Break Points Won | under | 0.1112538901274202 | 2026-10-18T04:33:13Z | 2026-10-18T04:00:00.000-04:00 |
| prizepicks|15699170 | prizepicks | Drake London | Recs | under | 0.1112022024757409 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|e27752c1-170f-49a1-818c-40e9475bac2d | underdog | Ilan Kebbal | Shots Attempted | under | 0.1110817859817236 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|73cfc407-9b54-4eab-ad71-1b16cfe226ef | underdog | Nikola Vlasic | Shots Attempted | under | 0.1109519945595428 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|9485593e-258a-4a56-9128-468621084a4a | underdog | LeQuint Allen | Receptions | under | 0.1108885229368038 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| prizepicks|15780920 | prizepicks | Carnell Tate | Rec Targets | under | 0.1106824993385057 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|93d3ac90-33e0-4231-bb13-7a6aa04ddd7b | underdog | Isaiah Davis | Receptions | under | 0.1106203143902329 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|15780893 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.1099330749079683 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15851105 | prizepicks | Drake Maye | Pass+Rush+Rec TDs | under | 0.1098259627151443 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|da413d57-9ee6-4bc3-a881-ecf7bf1c325c | underdog | Jalen Nailor | Receptions | under | 0.1094252996539932 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|589292fd-e313-4970-be91-21aa1035d9d5 | underdog | Chuba Hubbard | Rush Yards | under | 0.1093312003771705 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|7ad9bc73-957d-4f3a-a792-66508eb73acf | underdog | Douglas Luiz | Shots on Target | over | 0.1085399487026215 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|873f9402-5bd9-4917-87dd-dfb8e8c13bf8 | underdog | Jaelan Phillips | Sacks | over | 0.1084579494114263 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|a2cf8e00-1c20-4780-86d4-c4645e8a59f8 | underdog | Remy Labeau Lascary | Shots Attempted | under | 0.1081974793746585 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|9abb2140-29d4-42da-a80e-171506b0f0f8 | underdog | TreVeyon Henderson | Receptions | under | 0.1077977848542074 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15868236 | prizepicks | Bianca Andreescu | Break Points Won | under | 0.1077092707909285 | 2026-10-18T04:33:13Z | 2026-10-18T08:00:00.000-04:00 |
| underdog|626cc581-a1d0-48f9-8da4-843c00b1e028 | underdog | Daniel Jones | Rush Yards | under | 0.1075336467742743 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|02cdea83-cb13-4c29-8124-4112a7c13999 | underdog | Dalton Kincaid | Receptions | under | 0.1072286887364567 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|d5bf3bde-4990-4ebd-ab5f-1973a350af23 | underdog | Hunter Henry | Receiving Yards | under | 0.1068398536123976 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|749f4601-55c5-4a60-a9fc-6e05a3390f25 | underdog | Patrick Mahomes | Rush Yards | under | 0.1065967228086042 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| prizepicks|15847796 | prizepicks | DK Metcalf | Rec Targets | under | 0.1062185182083227 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|be789bcf-5bbc-4971-ad86-b7d6c80a33a0 | underdog | Rassoul Ndiaye | Shots on Target | over | 0.1045779519184712 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| prizepicks|15683993 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.1041918917578245 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|94eb6fa4-a98b-487e-ae4d-898fb33841c1 | underdog | Kaelon Black | Receptions | under | 0.1036569699005706 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|e6a80532-7552-46c1-9332-1cb029eb9161 | underdog | Drake London | Receptions | under | 0.103534681513115 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d5fcefcb-dea3-4f94-8bbf-631892597b8b | underdog | Michael Mayer | Receiving Yards | under | 0.1033070471995536 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|ee5a2df0-4ad7-4193-8347-a04f6791f3d5 | underdog | Najee Harris | Receiving Yards | over | 0.1030373186154452 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|300d62a3-c4a6-4cfc-a384-040035313e2c | underdog | Keon Coleman | Receptions | under | 0.1029446876150849 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|0af93701-e9c4-411e-be3a-7e99700c097e | underdog | Ryan Fitzgerald | Kicking Points | under | 0.1026614021541227 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15683896 | prizepicks | Jordan Love | Rush Yards | under | 0.1023572340303807 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|09dec485-a3d7-4f98-9dcc-0efa97ad445f | underdog | Jason Sanders | FG Made | under | 0.1015815221805782 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|08b174b3-7a07-4127-b0e6-61f9db47054a | underdog | Danny Namaso | Shots Attempted | under | 0.1015496868865136 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|8f88a427-e4f3-4800-8f0b-e3f1f13de438 | underdog | Bhayshul Tuten | Receptions | under | 0.1014884388520287 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|82576bc0-8ed1-49d3-842d-4ac2acf08bfb | underdog | Bam Knight | Rush + Rec Yards | under | 0.1012336781369264 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| prizepicks|15866094 | prizepicks | Anhelina Kalinina | Double Faults | under | 0.1009591507109615 | 2026-10-18T04:33:13Z | 2026-10-18T00:10:00.000-04:00 |
| underdog|f8501c83-5fa1-4e69-8fb5-b4105f36fb31 | underdog | Jalen Carter | Sacks | over | 0.1008733349751748 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|bfe81690-371a-48d6-81ef-454935d7ccfb | underdog | Maxx Crosby | Sacks | over | 0.1004976007487231 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|161ee153-6abd-4d8a-96e4-4a679116b6e3 | underdog | Chuba Hubbard | Receiving Yards | under | 0.0998270164198714 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|47da247c-51fa-4afa-8c21-c7f2f481e173 | underdog | Khalil Mack | Sacks | over | 0.0995142012693416 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|06e01a07-89db-46c6-adef-058452c123c3 | underdog | Christian Watson | Receiving Yards | under | 0.0994499324066642 | 2026-10-16T04:33:49Z | 2026-10-19T00:20:00Z |
| underdog|6804a9f4-ae01-416c-ac9d-1424bcee2ab1 | underdog | Nick Fortes | Total Bases | over | 0.0994475138121546 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15851443 | prizepicks | Jameis Winston | Pass+Rush+Rec TDs | under | 0.0992514213427923 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|0ea213a8-5833-4e9b-b64f-54428b1674d8 | underdog | Ashton Jeanty | Receptions | under | 0.0989103072432955 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|81e3e26e-69f9-4a87-a81a-e0e633c42e0f | underdog | TreVeyon Henderson | Rush Yards | under | 0.0987949297493204 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|d16d44f2-4bbc-45ee-9448-11c392125ebb | underdog | Kendre Miller | Receiving Yards | over | 0.0987932043524197 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|86e35022-d576-43e1-8849-4e56956cacc1 | underdog | Franco Mastantuono | Shots on Target | under | 0.0981837053816472 | 2026-10-16T04:33:49Z | 2026-10-18T13:00:00Z |
| prizepicks|15723431 | prizepicks | Parker Washington | Rec Targets | under | 0.0979824115619523 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|8820e10f-f894-4451-9b09-791375061a62 | underdog | Justice Hill | Rush + Rec Yards | over | 0.0977748598840932 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|e95fb410-0ce6-495b-938f-1c7bfbf4ee9a | underdog | Josh Cuevas | Receptions | under | 0.0976235872665639 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|b6950ec7-7122-4177-99fb-f479a06180bb | underdog | Emmett Johnson | Rush Yards | under | 0.0975247443669429 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|3ac845f1-8327-45ec-b051-4f0fbc8ea37e | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0969873480647717 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|c12a3dfe-3f70-4553-a127-2a325e537ab9 | underdog | Hunter Henry | Receptions | under | 0.0968582661600458 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|c59674c5-54e6-4da9-ba4f-b65f38bc849d | underdog | Brandon Aubrey | Kicking Points | under | 0.0965614256298216 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15847786 | prizepicks | Charlie Kolar | Rec Targets | under | 0.096550170355525 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| prizepicks|15723438 | prizepicks | Christian Watson | Rec Targets | under | 0.0964687264954906 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|3052801d-b182-4b8f-8cfe-6c9ca4c58b26 | underdog | Carl Granderson | Sacks | over | 0.0961048404986865 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|e10d0fe8-f19a-44c9-8ade-96b044691678 | underdog | Santiago Pierotti | Shots Attempted | under | 0.0957614507528494 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| underdog|66e96097-8aa3-41ab-8847-c2d6427208c0 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.0956936640558731 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|7e007ebc-8dfe-4606-8cf1-8d1cfd59c9c2 | underdog | Darnell Mooney | Receiving Yards | under | 0.0953848471327593 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a6240fae-14ca-462d-9247-5f4adca64687 | underdog | Jurgen Ekkelenkamp | Shots on Target | under | 0.0953503354535273 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| underdog|48a64d45-2977-4b8b-a530-ff1494759df3 | underdog | Brevyn Spann-Ford | Receiving Yards | over | 0.095062827596205 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| underdog|dbe0dcf4-56e3-4931-8172-e369edccbfd9 | underdog | Xavier Hutchinson | Receptions | over | 0.0949286461752075 | 2026-10-16T04:33:49Z | 2026-10-18T13:30:00Z |
| underdog|34c5f3b9-0e89-4afb-b8e0-b4b84cf716e9 | underdog | Jacopo Fazzini | Shots Attempted | under | 0.094910178919513 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|efe1cb4f-a20e-4187-98fd-a32a70d4b029 | underdog | Khalil Shakir | Receptions | under | 0.0948702225954792 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|47d65f8b-769d-42ed-a141-d0528362c6c0 | underdog | Najee Harris | Rush + Rec Yards | under | 0.0944036111889631 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|09d727cd-6f88-46ae-80e9-1a945eec238b | underdog | Jonathan Taylor | Receiving Yards | under | 0.0943886262641457 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15687723 | prizepicks | Drake London | Rec Yards | under | 0.0940748748925212 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|7af97054-43ba-4b5b-8355-539ba6219adb | underdog | Noah Gray | Receptions | under | 0.0940644205029117 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| prizepicks|15847803 | prizepicks | Emeka Egbuka | Rec Targets | under | 0.0939474175469708 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15780921 | prizepicks | Elic Ayomanor | Rec Targets | under | 0.0938883366191728 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|636ca2e0-ed26-4bdf-a57a-8fe112df53e8 | underdog | DeMario Douglas | Receptions | under | 0.0937809705359719 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15847781 | prizepicks | Noah Gray | Rec Targets | under | 0.0933610853741664 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|0a2b1589-4881-4634-94f0-dd474301eb37 | underdog | Austin Ekeler | Rush Yards | under | 0.0931846876934673 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|356383b1-19db-43b3-a7a8-7338c7143bfa | underdog | Jacoby Brissett | Rush Yards | under | 0.0928608446286957 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|f2afc1ae-3ef5-4334-8278-aa3709cb9e96 | underdog | Ladd McConkey | Receptions | under | 0.0926498947432636 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|90d3d553-8a6f-416a-a938-69a505587133 | underdog | Carnell Tate | Receptions | under | 0.0925648120770283 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0b0fcbd2-c756-44fa-b59f-547f57d7b1ba | underdog | Deshaun Watson | Pass TDs | under | 0.09205750895952 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|bdb42823-0e98-4d24-b91f-2d2ec93c8d04 | underdog | Dalton Schultz | Receiving Yards | under | 0.0919137773943742 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|1d9fea58-b195-4947-b3e7-82d22592cef6 | underdog | Makai Lemon | Receiving Yards | under | 0.0918442191084162 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|1bc76d99-4e01-4cbd-ae9f-3c88279a8341 | underdog | Cam Ward | Rush Yards | under | 0.0917728657142905 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d81e2d1b-8b89-47e7-819c-7a43f87d9c63 | underdog | Tony Pollard | Receptions | under | 0.0915594796591671 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|bc7b8b71-b39b-4e00-8dfe-23de38f149f3 | underdog | Chris Rodriguez | Rush + Rec Yards | over | 0.0912708402911461 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|b04836a3-d0d0-489e-b574-e9fb3efdbe1c | underdog | Kendrick Bourne | Receiving Yards | under | 0.0910802931161529 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|1c216335-d759-47fd-977d-edf6648a4b7a | underdog | Chris Godwin | Receptions | under | 0.0908829282803141 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|5afe9842-0dce-4dd8-af0f-fe8cb03b92f5 | underdog | Ashton Jeanty | Rush Yards | under | 0.0907831438926858 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|0a828e80-1941-4a03-9c93-64b5ba95d7c7 | underdog | Nathaniel Lowe | Hits + Runs + RBIs | over | 0.0903403868457234 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|8fe32d62-3c59-4421-ad26-9bf7533924c2 | underdog | Chris Boswell | Kicking Points | under | 0.0900969810523529 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|e4ea7ddf-3222-4f4f-855a-edfd81fd678f | underdog | Javonte Williams | Receiving Yards | under | 0.0890453697711329 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| underdog|82bf6f8e-6dfb-4379-8df2-457f64fa58db | underdog | Cam Skattebo | Receptions | under | 0.0890453013136044 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9ed333b2-b775-4ce0-a80e-0b55b15e9fca | underdog | Alvin Kamara | Receptions | under | 0.0890160134731113 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|075f2d6a-0fd3-4d0a-8f49-c7d89a0a5189 | underdog | Nico Paz | Shots on Target | over | 0.0889946467410491 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00Z |
| underdog|283e7fbc-01aa-4eae-9e0d-27d72324e645 | underdog | Jaylen Warren | Receptions | under | 0.0888336011639515 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15865456 | prizepicks | Moritz Nicolas | Goalie Fantasy Score | under | 0.0879496416973769 | 2026-10-18T04:33:13Z | 2026-10-18T11:30:00.000-04:00 |
| underdog|cc906582-9f57-48e6-8abc-c97f7dffedd6 | underdog | Lassine Sinayoko | Shots on Target | over | 0.0878631259186616 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|898e1c6b-f7d4-4821-9f2f-a5e3812c5e4c | underdog | Santiago Pierotti | Shots on Target | over | 0.0877283024920822 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| underdog|1f71a5ce-8494-4c53-a246-efb34fb4290d | underdog | Sonay Kartal | Double Faults | under | 0.0875764385337222 | 2026-10-18T04:33:13Z | 2026-10-18T10:30:00Z |
| underdog|4042a485-9f28-4044-aec2-9e98911f4570 | underdog | Efton Chism | Receptions | under | 0.0872853110580094 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|e21f26b5-70a3-4d9b-867d-65eed2788a9f | underdog | Davide Frattesi | Shots on Target | over | 0.086942530376014 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| prizepicks|15724311 | prizepicks | Luther Burden III | Recs | under | 0.0867852920160726 | 2026-10-14T13:48:29Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|f14dbdc9-afce-4510-aa97-167837d3c860 | underdog | Diego Moreira | Shots on Target | under | 0.0866514512219092 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| prizepicks|15847798 | prizepicks | Germie Bernard | Rec Targets | under | 0.0866513230642185 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|f1c23326-42ee-4cf2-aef4-a0feeb4bce6b | underdog | Khalil Shakir | Receiving Yards | under | 0.0864184534241703 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|8b2c7af7-fc10-4ec4-a208-54057095b901 | underdog | Seth McGowan | Receiving Yards | over | 0.086331109238382 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15847778 | prizepicks | Travis Kelce | Rec Targets | under | 0.0861610850207802 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|6db7b0ae-c6ee-478d-a49d-129b4b1fd278 | underdog | Tijjani Noslin | Shots on Target | over | 0.0858902927484059 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|c8372399-fe27-487f-8ea7-949c2053718b | underdog | Chris Olave | Receptions | under | 0.0851341055103245 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|b751d2e4-3891-4aae-9105-6fe201c6bb48 | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.0850015808273789 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|7b157c5a-390b-4f53-a252-abf28305b510 | underdog | Darius Cooper | Receptions | over | 0.0849506680193942 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|ba0ee3d5-c791-4f65-b952-ad762a6d93b4 | underdog | Trevor Lawrence | Rush Yards | under | 0.0849368541794555 | 2026-10-17T04:25:02Z | 2026-10-18T13:30:00Z |
| underdog|1453e2a3-ccd7-4487-a786-01331c415ed9 | underdog | Bijan Robinson | Rush Yards | under | 0.0847719303932046 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|526220fb-7014-4d7d-9b7e-8de8007b8071 | underdog | Cameron Dicker | Kicking Points | under | 0.0843725941707534 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|eb3b6043-1837-47c5-ac63-e01ffe7c99bb | underdog | Kyle Williams | Receiving Yards | over | 0.0841866895095522 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|5ef2affe-7164-4942-b83d-24dbf6a50380 | underdog | Rashan Gary | Sacks | over | 0.0841498106392198 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| underdog|641169da-fc41-4daa-9392-28dd29556e29 | underdog | Dominic Zvada | Kicking Points | under | 0.0841094967458455 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15723439 | prizepicks | Matthew Golden | Rec Targets | under | 0.0838509495053801 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|87d04182-c17e-424a-851d-8a97bd45be5d | underdog | Bucky Irving | Rush + Rec Yards | under | 0.0838346223368627 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|85a86f85-c81e-494d-892c-919be8f8bb77 | underdog | Jeffery Simmons | Sacks | over | 0.0836317076233811 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|4a25317c-96bc-41ec-bcb4-c96381d32823 | underdog | Andre Szmyt | FG Made | under | 0.0835776067842513 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b713a044-fe53-4592-ab11-2f7a777c4611 | underdog | Jude Bellingham | Shots on Target | under | 0.0831069076745819 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| underdog|388c92b5-244d-4964-80bd-77b5c00dd30b | underdog | Elijah Higgins | Receiving Yards | over | 0.0830939998020973 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| underdog|dcfd88d0-6fed-4df9-a0e2-f45991b6ce1d | underdog | Rolando Mandragora | Shots Attempted | under | 0.0829025730753998 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|00b924f9-54cd-4cd3-9fb0-99579a5dbbc9 | underdog | Bucky Irving | Receptions | under | 0.0828432335053065 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15780899 | prizepicks | Rome Odunze | Rec Targets | under | 0.0822749023065505 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|07c1106f-d7b1-409a-8443-a586f438bce0 | underdog | Bijan Robinson | Receiving Yards | under | 0.0821952672016379 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0c458582-fcbc-431b-a883-d561d75af6c5 | underdog | Chase McLaughlin | FG Made | under | 0.0820147125331578 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|969f4a37-4b6d-4227-aeb1-e4c435a11a9b | underdog | Juwan Johnson | Receptions | under | 0.0816643289523625 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|c15a4608-6bef-4228-82de-0c0f71cc7745 | underdog | Najee Harris | Rush Yards | under | 0.0815314653507173 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|50b90400-9e6d-4b56-898d-0646639a028b | underdog | Tyjae Spears | Receiving Yards | under | 0.0803376295021978 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b4df8b86-127b-4e0d-907d-166fd70109f5 | underdog | Laiatu Latu | Sacks | over | 0.080283807387412 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|fdd9dac5-987d-41ad-8688-c23f9c2346c4 | underdog | Jerry Jeudy | Receiving Yards | under | 0.0798750843597522 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|15723427 | prizepicks | Brenton Strange | Rec Targets | under | 0.0797448193319028 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|f759fe44-b1fd-42fd-bf77-0a26d3e47522 | underdog | Victor Mesa | RBIs | over | 0.0795406847754392 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|499e7019-bb50-4369-90ad-882f26cebca4 | underdog | Quinshon Judkins | Receptions | under | 0.0794218811542114 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|a4bea3ce-f333-4f1a-a288-7594e88cdec1 | underdog | Dallas Goedert | Receiving Yards | under | 0.0789132872815342 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|f7d7efd9-706e-4f2a-b9fa-cf31dab88c6c | underdog | Maja Chwalinska | Double Faults | over | 0.0788614793726297 | 2026-10-18T04:33:13Z | 2026-10-18T10:30:00Z |
| underdog|4f3812c7-c049-4814-98c7-8230a8d7e67e | underdog | Quinshon Judkins | Receiving Yards | under | 0.0785824684009219 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|edc3892a-78be-46c7-a4ac-6e4e735594cc | underdog | Diego Moreira | Shots Attempted | under | 0.0780894584290043 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|a07e529b-25b9-4a6f-b042-ee3904f7d680 | underdog | Seth McGowan | Rush Yards | under | 0.0778596263323497 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|81ed5d97-0fb1-4167-9899-2b5bc2c55dd4 | underdog | Antonio Williams | Receptions | under | 0.0777888765836508 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|b74c79d0-9cd1-4af3-859a-2d382f8fefab | underdog | Brian Robinson | Rush + Rec Yards | under | 0.0777787547912999 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|dd7e6279-f267-4c18-a48d-b8df2c51f608 | underdog | Josh Allen | Rush Yards | under | 0.0777475753956967 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|90203be5-cce9-48da-9bcf-12691adea2aa | underdog | Byron Young | Sacks | under | 0.0776812385126114 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|c74b3197-a406-4454-99fe-6da596466cac | underdog | Brian Thomas | Receiving Yards | under | 0.0776225769357386 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|f3feba67-aa92-4921-af6c-11b768903356 | underdog | Nate Boerkircher | Receiving Yards | over | 0.0775591248529734 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|1db759f5-e818-4a58-bfe2-12e4c6bfa9eb | underdog | Chris Rodriguez | Rush Yards | under | 0.077119161083069 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|ee36553d-4b21-45f9-b605-6a5e3a1d8530 | underdog | Keon Coleman | Receiving Yards | under | 0.076720944771056 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|11100bdf-bc08-40cb-bebf-f74f9dcb03d9 | underdog | TreVeyon Henderson | Rush + Rec Yards | under | 0.076673124065128 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|00ba5c93-ccb9-456f-b9fb-cd0cf605742b | underdog | Jaylin Noel | Receptions | under | 0.0766177887027853 | 2026-10-16T04:33:49Z | 2026-10-18T13:30:00Z |
| prizepicks|15780904 | prizepicks | Josh Downs | Rec Targets | under | 0.0765832068199904 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15853474 | prizepicks | Rhamondre Stevenson | Recs | under | 0.0765542663192176 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15865331 | prizepicks | Guglielmo Vicario | Goalie Saves | under | 0.0762662614352663 | 2026-10-18T04:33:13Z | 2026-10-18T14:45:00.000-04:00 |
| underdog|0e08479a-ea1c-48a5-aed2-f030afe74b7f | underdog | Hugo Bolin | Shots Attempted | under | 0.0759922085968921 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|15687736 | prizepicks | Matthew Golden | Rec Yards | under | 0.0757899658036277 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|0a3eead5-29df-40d6-97fc-0b2974ab5d9c | underdog | Ted Hurst | Receptions | over | 0.0757545529160795 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| prizepicks|15853493 | prizepicks | Ryan Flournoy | Recs | under | 0.0757425794092204 | 2026-10-17T04:25:02Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|469087c6-072d-4f33-94db-a4d478463a4b | underdog | Justice Hill | Receiving Yards | under | 0.0756885526361618 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|f7cb8084-ab60-401d-8150-4bd58e4351bc | underdog | Woody Marks | Receptions | under | 0.0756857147176727 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|1b8838fe-e224-4ace-9ca4-f575c6981c65 | underdog | CJ Donaldson | Receiving Yards | under | 0.0753318613760584 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|79fafca0-392d-4fa7-a05a-e4e132b4938e | underdog | Kenny Gainwell | Rush Yards | under | 0.0752791090544141 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|d2fee148-2cf4-4a18-b85e-c7d01396ce1f | underdog | Adrien Thomasson | Shots on Target | over | 0.0749174116519088 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|7898ef01-f5e8-4506-9ab6-1c73a6b94973 | underdog | Ka'imi Fairbairn | FG Made | under | 0.074756436597449 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15853477 | prizepicks | Kyle Pitts Sr. | Recs | under | 0.0747536416333555 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|185ce854-7c03-4a00-99e2-bed542533611 | underdog | Omarion Hampton | Rush + Rec Yards | under | 0.074462326119139 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|40f1b776-36bb-4f04-81b4-27ba9629f3a5 | underdog | Rachaad White | Receiving Yards | under | 0.0742268388080018 | 2026-10-17T04:25:02Z | 2026-10-20T00:15:00Z |
| underdog|41e5c9cf-39c2-48ca-82cb-6a01c7982c56 | underdog | Samuel Chukwueze | Shots Attempted | under | 0.073966742563844 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|9c7c0c9b-154c-41f6-87e6-2d646475c02a | underdog | Trey Hendrickson | Sacks | under | 0.0738208605553927 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|fd4d2b82-f035-4b89-a206-e0e45a155158 | underdog | Kyren Williams | Receiving Yards | over | 0.0738184738121925 | 2026-10-16T04:33:49Z | 2026-10-18T20:05:00Z |
| prizepicks|15723429 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.0736296881640543 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15743189 | prizepicks | Parker Washington | Recs | under | 0.0735987917850155 | 2026-10-17T04:25:02Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|f5976780-3c0b-409f-aee0-1af0221260d7 | underdog | Tyler Higbee | Receptions | under | 0.0735716424142496 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15780896 | prizepicks | Colston Loveland | Rec Targets | under | 0.0731181999603665 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|5e01d90f-559d-4252-a72b-4ac8bb3cdf4f | underdog | Weston McKennie | Shots Attempted | under | 0.0729526070664482 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|1e0eeb9b-2926-4e3e-9aeb-78daec0f24ab | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.0729352353317847 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|df7c9230-c321-442e-9ac5-bcdee63d60d2 | underdog | Victor Mesa | Hits + Runs + RBIs | over | 0.0726854137451756 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|38baa9fd-5174-422d-99d3-d91bba1c496a | underdog | Dawson Knox | Receptions | under | 0.0724818872128977 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|bc066a1c-6c83-44dd-89ed-e78f53e7980e | underdog | Jahan Dotson | Receiving Yards | under | 0.0723198425457335 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15847793 | prizepicks | Malachi Fields | Rec Targets | under | 0.0722285429617983 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|fe9923d9-5ba0-451a-b036-9cc847754fcd | underdog | Tyler Shough | Rush Yards | under | 0.072211232209545 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|e58caf6d-23b1-4a07-adda-f2003e53ff55 | underdog | Lassana Coulibaly | Shots Attempted | over | 0.0721727264286407 | 2026-10-16T04:33:49Z | 2026-10-18T10:30:00Z |
| prizepicks|15780901 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.071327678066846 | 2026-10-15T04:38:48Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|394c596f-41d8-40de-8a46-b31d2eee1d1e | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.0712523869747466 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|0eb8a450-a086-492a-86da-cc9254299a8a | underdog | Jerry Jeudy | Receptions | under | 0.0709383525386926 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|13fa4e82-144e-485d-bd74-330177d72253 | underdog | Isaiah Davis | Receiving Yards | over | 0.0709244695008637 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|72087370-822d-44cc-af10-eef1d0b13caa | underdog | Kyren Williams | Receptions | over | 0.0706598600779713 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|ef0129f3-b541-4334-b9e6-6c575cb06872 | underdog | Brock Purdy | Rush Yards | under | 0.070348800774928 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|12f1c120-75c8-4a5a-b3f7-18b53aba9541 | underdog | Nick Fortes | Hits | over | 0.0702950605466726 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|2ca93a13-ed8a-4db4-bd66-f0969ef940f7 | underdog | Rashod Bateman | Receptions | under | 0.0697367128988782 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|d1a06206-a881-4dec-b17b-2fbfe3da50d8 | underdog | Kimani Vidal | Receiving Yards | under | 0.069682134798205 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|d2da65db-c7f3-432a-b0ae-a7d1cb2af39d | underdog | Ryan Flournoy | Receiving Yards | under | 0.069590938846595 | 2026-10-15T04:38:48Z | 2026-10-19T00:20:00Z |
| underdog|ed29c37c-cb4c-4728-ae93-103da38fb79c | underdog | Zay Flowers | Receiving Yards | under | 0.0693306605284327 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|9c712767-faac-4ec1-baab-1e97a9d2ab7d | underdog | Travis Hunter | Receiving Yards | over | 0.0690720257736068 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|fb840643-e805-4370-9e1c-4c0c42bb744c | underdog | Rashod Bateman | Receiving Yards | under | 0.0690370329438483 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15853475 | prizepicks | Chris Olave | Recs | under | 0.068801229603173 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|73bed078-560c-4da1-9a90-c522cc36ec9f | underdog | Davis Allen | Receptions | under | 0.0684696165222464 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| underdog|da171540-6111-407d-bf93-2c5d489f77cd | underdog | Wouter Burger | Shots on Target | over | 0.0682281167588793 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|15865333 | prizepicks | Guglielmo Vicario | Goalie Fantasy Score | under | 0.0680283791022992 | 2026-10-18T04:33:13Z | 2026-10-18T14:45:00.000-04:00 |
| underdog|578f7e5e-2fc5-4dd7-91ff-408345d16f37 | underdog | Kendre Miller | Receptions | under | 0.0679773914582534 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|d2d14f02-e826-4c77-b502-08be54a8cf1e | underdog | Jaylen Warren | Rush Yards | under | 0.0679341120144584 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|a13c34f7-0ed8-4f3e-84ce-ddb1e9b6f164 | underdog | Omarion Hampton | Rush Yards | under | 0.0677856333745934 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|36f4d7f9-6a4d-40ef-9974-811523e2ed46 | underdog | Gunnar Helm | Receptions | under | 0.0671645487138128 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15847772 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.0668668995080241 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|9c3bd401-2b71-4244-bb83-daf2a9dd063d | underdog | Roschon Johnson | Rush + Rec Yards | under | 0.0667986847074589 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|ba454ee5-adba-4085-a96f-d06e65b5b8f5 | underdog | Wael Mohya | Shots Attempted | under | 0.0666593959545643 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| underdog|43963736-4413-48cb-9fc3-ebef1b798524 | underdog | Dominic Zvada | FG Made | under | 0.066601134278204 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|c5cddea4-79dc-4e95-be93-230b39c7b228 | underdog | Drake Maye | Rush Yards | under | 0.0664808117781989 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|da748a09-9959-4027-bb19-3aa4704ecda3 | underdog | Douglas Luiz | Shots Attempted | over | 0.0663747306208701 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|4167a7ea-3a36-4051-bd62-892e94801fe2 | underdog | Roschon Johnson | Receptions | under | 0.0662361063048515 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|2f17fd0d-ad74-43be-aea5-e6900384daf7 | underdog | Tony Pollard | Receiving Yards | under | 0.0660331448301843 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|78fca0a4-5488-4843-8f6c-958cba15f4ac | underdog | Kaelon Black | Rush Yards | under | 0.0657007230138554 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|d13c3f2e-22ed-4d2a-8704-b345f6746b9f | underdog | Tim Lemperle | Shots Attempted | under | 0.0655246777854302 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| underdog|d74833d9-508a-42d3-9a60-bdc1e59d591f | underdog | Blake Corum | Receptions | under | 0.0650781095642691 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|82b30739-904c-49e7-82ce-5c0d246f5d9a | underdog | Mousa Al Tamari | Shots on Target | over | 0.0642470194096921 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|af0ebfcf-8824-48af-9544-9866de80c428 | underdog | Tre Tucker | Receiving Yards | under | 0.0641533022328364 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|e1818f2b-c03c-4fbe-aa2e-f749439133aa | underdog | Blake Corum | Receiving Yards | under | 0.0637542324125917 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|1f56743a-ae5e-4db3-b98e-c6b9bcd7b8f6 | underdog | Sota Nakamura | Shots on Target | under | 0.0633338758423267 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|d8a3e0c0-22c8-411f-8f13-fa2161827ae6 | underdog | Felix Correia | Shots on Target | over | 0.0631044115851889 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| underdog|ba96b11a-daea-454d-a8ae-59fc0ab57797 | underdog | Nate Boerkircher | Receptions | under | 0.0630830757411501 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|9fa54f3f-df55-47ee-8fc3-7b6962fd15c3 | underdog | Jameis Winston | Rush Yards | over | 0.0629221551802247 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|d5e6de3a-f38e-4e3d-869e-ba968eabf4a0 | underdog | Jason Sanders | Kicking Points | under | 0.062918205138056 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|986e82a3-b125-47ab-a45c-0791e9e8d860 | underdog | Federico Valverde | Shots on Target | under | 0.0624079829708859 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| prizepicks|15687738 | prizepicks | Christian Watson | Rec Yards | under | 0.0621131131326925 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| prizepicks|15868078 | prizepicks | Sonay Kartal | Break Points Won | under | 0.0618435637166766 | 2026-10-18T04:33:13Z | 2026-10-18T06:30:00.000-04:00 |
| underdog|4455e029-d324-4afc-afb8-7cde48560602 | underdog | Noah Gray | Receiving Yards | under | 0.0618076671458343 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|696de9a0-1686-4146-a1ba-7346ef15538a | underdog | Brenton Strange | Receiving Yards | under | 0.0614460641643638 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15865332 | prizepicks | Christos Mandas | Goalie Saves | under | 0.061406775308663 | 2026-10-18T04:33:13Z | 2026-10-18T14:45:00.000-04:00 |
| underdog|4559d970-ea87-4d58-bbff-6a6f2103ee47 | underdog | Bo Melton | Receptions | under | 0.0613982492448302 | 2026-10-18T04:33:13Z | 2026-10-19T00:20:00Z |
| underdog|9b416f0f-31c2-46a9-8880-47a15a556531 | underdog | Nick Fortes | Batter Walks | under | 0.0609425785482123 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15723436 | prizepicks | George Pickens | Rec Targets | under | 0.0604557293312356 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|960b77e8-c40b-418b-9a63-a69f476b23a4 | underdog | Tommy Tremble | Receptions | under | 0.0601813127841199 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|94ae336a-1e93-4a07-9b56-cefc8b1d24c4 | underdog | Tim Lemperle | Shots on Target | under | 0.0599423075392854 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| prizepicks|15874225 | prizepicks | Terry McLaurin | Rec Targets | under | 0.0597497378960204 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|7774b36c-193a-4b60-900e-41c97f496115 | underdog | Colston Loveland | Receptions | under | 0.0595050397856488 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|ea90d432-d44b-4bc3-96e2-5219ed0f5aec | underdog | Federico Valverde | Shots Attempted | under | 0.0593987834965795 | 2026-10-16T04:33:49Z | 2026-10-18T19:00:00Z |
| underdog|3a6e7f2a-9886-495d-9e99-d2d1210b6d1f | underdog | Brian Robinson | Rush Yards | under | 0.0593682800197614 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|002b7366-b5d4-490f-97d1-1519c83d3ecf | underdog | Josh Downs | Receptions | under | 0.0593145812120564 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|47115be8-1993-4f93-849e-53017cdfed37 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.0587595094818914 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b50fcc45-63f0-475f-afbb-12b59b62960a | underdog | El Bilal Toure | Shots on Target | under | 0.0587511652898692 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|d2f424ea-56c8-4273-87e2-2c395f9b0e30 | underdog | Justice Hill | Rush Yards | over | 0.0587397379903558 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|77ad535f-878d-4776-9f7d-6389d98bbd07 | underdog | Josh Cameron | Receiving Yards | under | 0.0584933099355893 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|c63e3ffc-2032-4a06-8ef2-08b03d124b14 | underdog | Romeo Doubs | Receptions | under | 0.0584141460287966 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|21ad007c-cd5d-45dd-82c0-c20c9a053cf1 | underdog | Chase McLaughlin | Kicking Points | under | 0.0582113702428559 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| prizepicks|15860552 | prizepicks | Alina Korneeva | Total Games | over | 0.0580417564948919 | 2026-10-18T04:33:13Z | 2026-10-18T01:20:00.000-04:00 |
| underdog|dfaaecbc-7beb-41ee-8832-5ff7843271ab | underdog | Samuel Chukwueze | Shots on Target | over | 0.0576858636269437 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|4ba2801d-c802-4d57-90a8-2f59d660ac94 | underdog | Bam Knight | Rush Yards | under | 0.0575712811619916 | 2026-10-18T04:33:13Z | 2026-10-18T20:05:00Z |
| underdog|88d12288-1451-4385-a596-6604aa8a8bf8 | underdog | Gustav Isaksen | Shots Attempted | under | 0.0573156586138339 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|e6df1e5a-2dea-451a-b095-f38f332c47a5 | underdog | Tyler Goodson | Receptions | over | 0.0570175113584239 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| prizepicks|15780889 | prizepicks | Kendrick Bourne | Rec Targets | under | 0.0568360672251555 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|4b3a7d57-7756-4d73-84c6-6c545b4fda0d | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.0567601516875453 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15874223 | prizepicks | DeVonta Smith | Rec Targets | under | 0.0565638607229133 | 2026-10-18T04:33:13Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|f3fadb3d-3f28-4736-ac1f-e870278f1568 | underdog | Matt Gay | Kicking Points | under | 0.0562253480882356 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|33611c35-750d-4b37-8611-d7419c681f6b | underdog | Davante Adams | Receptions | under | 0.0562005213775146 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|45840fcc-73e3-4a0e-b5d6-289d7e8131ad | underdog | Jaylen Warren | Receiving Yards | over | 0.0555091329077407 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|6a6b0c2f-5212-4f70-831a-9abf69bda05f | underdog | Austin Hooper | Receptions | over | 0.0554220252041881 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15780925 | prizepicks | Wan'Dale Robinson | Rec Targets | under | 0.0553624409546373 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|603ed9d9-3ddd-4797-8b01-4044010adb0a | underdog | D'Andre Swift | Receiving Yards | under | 0.0551364813322972 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| prizepicks|15780922 | prizepicks | Gunnar Helm | Rec Targets | under | 0.0550900798532351 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15718429 | prizepicks | Keenan Allen | Recs | under | 0.0546735205408628 | 2026-10-16T04:33:49Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|c3424e38-552a-443c-9fad-efc59c5531c2 | underdog | Dalton Kincaid | Receiving Yards | under | 0.0542832307488917 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|c68c56a6-7966-4b2f-a718-e65fdb108cf3 | underdog | Tez Johnson | Receiving Yards | over | 0.0541951169243843 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|990de442-0765-493a-9810-0b565a5db2ca | underdog | Tutu Atwell | Receiving Yards | over | 0.0540903705016898 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|5c32d1cb-8408-4afe-9bb0-e78c207dbed8 | underdog | Tyler Loop | Kicking Points | under | 0.0539584489818791 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|0efbaa6a-d00c-4fc4-87e1-6ef076eeb897 | underdog | Justin Herbert | Rush Yards | under | 0.0539116189840668 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| underdog|c2c49705-2708-4c79-a872-c434370ca078 | underdog | LeQuint Allen | Receiving Yards | over | 0.0538065893500936 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|0d36dc76-28b8-4abc-9d4b-2ddee0e7d405 | underdog | Charlie Kolar | Receptions | under | 0.0537571002560284 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|21db0775-6199-41c8-b8b6-32887b14ebd6 | underdog | Kamilla Rakhimova | Double Faults | under | 0.0533735167398961 | 2026-10-18T04:33:13Z | 2026-10-18T05:40:00Z |
| prizepicks|15847767 | prizepicks | DJ Moore | Rec Targets | under | 0.0533632708735497 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|ffb130ad-e6f0-40d1-ab71-bbe88bca3158 | underdog | Daniel Maldini | Shots on Target | under | 0.0533204928255294 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|9c337110-ce60-43b0-ba8f-598518ed7a56 | underdog | Kalif Raymond | Receptions | under | 0.0530127134226658 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|c9210d9a-c923-4118-a331-946d26988ac6 | underdog | Tyler Goodson | Rush Yards | under | 0.0530101235093533 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| prizepicks|15853479 | prizepicks | Jalen Coker | Recs | under | 0.0529845181476824 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15853492 | prizepicks | George Pickens | Recs | under | 0.0529503010135409 | 2026-10-17T04:25:02Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|66e27c22-2a07-483b-a30f-39ce1dfcf59c | underdog | Chase Young | Sacks | under | 0.0525378002454653 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|a208d476-d983-4f65-bb30-2575569187fe | underdog | Josh Cameron | Receptions | under | 0.0525247460995683 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|9dd77203-25a0-467f-b3b2-05c6d724740a | underdog | Travis Kelce | Receptions | under | 0.0519415931095141 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|6ef4dcb7-de41-4517-aa79-fb113064e5e1 | underdog | Elijah Higgins | Receptions | over | 0.0518899712452672 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| underdog|2ebe8bdb-3f29-4479-89e4-a69001e8f971 | underdog | Jacoby Brissett | Pass TDs | under | 0.0518051464257154 | 2026-10-15T04:38:48Z | 2026-10-18T20:05:00Z |
| underdog|416b82ff-795f-4d97-8df8-a9664f32525c | underdog | Tyler Shough | Pass TDs | under | 0.0513199434637003 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|2b897fd5-9224-46bc-80b5-de0a129f7493 | underdog | Martin Baturina | Shots on Target | over | 0.0509962948069832 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00Z |
| prizepicks|15847795 | prizepicks | Kenyon Sadiq | Rec Targets | under | 0.0508811932001737 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|15865338 | prizepicks | Laura Samson | Total Games | over | 0.0507221440890194 | 2026-10-18T04:33:13Z | 2026-10-18T04:00:00.000-04:00 |
| underdog|79e36883-a09c-45f4-92d2-bca0e1b90e1b | underdog | José Ramírez | Total Bases | over | 0.0505279034690799 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|4ccbd4db-d288-48b7-b08f-adc5183a3c6c | underdog | Cameron Dicker | FG Made | under | 0.0502901662275662 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15746218 | prizepicks | Michael Wilson | Recs | under | 0.0502399015358969 | 2026-10-16T04:33:49Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|ce7a5e3c-82c0-4407-a57b-d905114aba42 | underdog | Spencer Shrader | FG Made | under | 0.0502073963040488 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|a2e435e3-0dd5-444b-b53b-c2fcb872a9e9 | underdog | Pablo Pagis | Shots Attempted | under | 0.0501888274089293 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|47a99784-3853-4e91-b657-136b566ff70f | underdog | Greg Rousseau | Sacks | over | 0.0500604965378224 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|bff56b68-3f23-4362-b29f-d18771d60143 | underdog | Andre Szmyt | Kicking Points | under | 0.0498721080311491 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|7dcc233f-d5d8-481b-8c15-d8d61edb7ff1 | underdog | Michael Mayer | Receptions | under | 0.0496693096459766 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|71af39d9-f5da-46ee-a9a2-eee0e2a9e06f | underdog | Mike Washington | Rush Yards | under | 0.0496099130697238 | 2026-10-15T04:38:48Z | 2026-10-18T20:25:00Z |
| prizepicks|14007606 | prizepicks | LeBron James | Rebs+Asts | under | 0.04958671453074 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9e1d3eef-97f0-4cac-8275-be0ab10d777a | underdog | Dontayvion Wicks | Receptions | under | 0.0494948174680114 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|c57eb0e7-d434-4c5c-95bf-85724905ab5f | underdog | Josh Maja | Shots Attempted | under | 0.0490258815660714 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|4d9753e8-d388-4479-8dfb-3b4e8ade33aa | underdog | CJ Donaldson | Receptions | under | 0.0488428331817926 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|03a39e1f-2c41-4765-abc6-377676b30d78 | underdog | Pape Matar Sarr | Shots on Target | over | 0.0488343629542282 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|2e12b454-18f6-4ace-b2c6-c4f94c8b417c | underdog | Drew Rasmussen | Strikeouts | under | 0.048687003923807 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15853478 | prizepicks | Rome Odunze | Recs | under | 0.0486030735622941 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|bb7f6a50-1353-4685-ac75-68448c79ff55 | underdog | Ilan Kebbal | Shots on Target | under | 0.0485941810461353 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|eb808d02-92f8-42b6-8401-87af56758f91 | underdog | Davis Allen | Receiving Yards | over | 0.0482671786839454 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15865014 | prizepicks | Mattia Bellucci | Total Games Won | under | 0.0481533361077964 | 2026-10-18T04:33:13Z | 2026-10-19T02:00:00.000-04:00 |
| prizepicks|15851437 | prizepicks | Trevor Lawrence | Pass+Rush+Rec TDs | under | 0.0478205845744269 | 2026-10-17T04:25:02Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|f269ef94-3969-4300-8809-116312e25d3a | underdog | DeForest Buckner | Sacks | over | 0.0468107538927842 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|07f528aa-1f51-405f-a849-30268e82d0b5 | underdog | Kenneth Walker III | Rush Yards | under | 0.0461590986520688 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|f159812d-547e-401e-a4f4-df4fc9426766 | underdog | George Pickens | Receptions | under | 0.0460692547186782 | 2026-10-14T13:48:29Z | 2026-10-19T00:20:00Z |
| prizepicks|15780890 | prizepicks | Michael Wilson | Rec Targets | under | 0.045843534725518 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|bd2e0c0e-2124-4247-af62-0301707e1161 | underdog | Tijjani Noslin | Shots Attempted | under | 0.0452307945601901 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| underdog|ffabb40a-9893-4d44-b093-1bec4ce49757 | underdog | Donovan Ezeiruaku | Sacks | under | 0.0449755255864332 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| underdog|10433391-89fe-4b47-a42f-bf6820ab32f4 | underdog | Jaylin Noel | Receiving Yards | over | 0.0446635495372091 | 2026-10-16T04:33:49Z | 2026-10-18T13:30:00Z |
| underdog|841df5c3-928f-4d11-aab6-defeaa176c4a | underdog | Bijan Robinson | Receptions | under | 0.0446517709336508 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15869415 | prizepicks | Nishesh Basavareddy | Total Games | over | 0.0446136067780367 | 2026-10-18T04:33:13Z | 2026-10-18T09:00:00.000-04:00 |
| underdog|9ce51901-1f04-4470-8206-ac067e222644 | underdog | Emmett Johnson | Receiving Yards | over | 0.0443540445384683 | 2026-10-18T04:33:13Z | 2026-10-18T20:25:00Z |
| underdog|e2243e5d-06e3-46f4-9499-1a352345f13b | underdog | Mousa Al Tamari | Shots Attempted | under | 0.0438895872951524 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|48050135-8671-4987-82ba-b50ab9d2e54f | underdog | Davante Adams | Receiving Yards | under | 0.043510578091841 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15853489 | prizepicks | Kenneth Walker III | Recs | under | 0.0434600456931675 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|edac7bd8-d6a8-4b16-a80b-b26baaaa4958 | underdog | Oronde Gadsden | Receiving Yards | under | 0.0430553575678889 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|fe1e5fb5-d4b4-44d3-9d80-122ff5742fa2 | underdog | Noah Fant | Receiving Yards | over | 0.0429465724440805 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|65431a91-5bc9-46c8-814f-62cce9bf13f4 | underdog | Yandy Díaz | Hits | over | 0.04287290493018 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| prizepicks|15780917 | prizepicks | Malik Nabers | Rec Targets | under | 0.042775419427162 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|4cd07c9c-12c7-4c1d-8b76-f3c03b7d3a27 | underdog | Kenyon Sadiq | Receiving Yards | over | 0.0427510498722186 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|c3249cbc-cc87-4b1d-b18e-ed34a79c98db | underdog | Eli Raridon | Receptions | over | 0.0426446520630632 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|cf35b696-eddc-405d-a92c-9080b0b4184f | underdog | Kaelon Black | Receiving Yards | over | 0.0425272702416632 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15847768 | prizepicks | Ty Johnson | Rec Targets | under | 0.0423054327510473 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|3994b647-af16-4180-bb11-f4f9fe4b2217 | underdog | Pape Matar Sarr | Shots Attempted | under | 0.0422431040673977 | 2026-10-17T04:25:02Z | 2026-10-18T18:45:00Z |
| underdog|91ef73ee-52c7-413c-81fb-4499934487a6 | underdog | Darnell Washington | Receiving Yards | under | 0.0421896820002846 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| prizepicks|15847777 | prizepicks | Xavier Hutchinson | Rec Targets | over | 0.0421544124250162 | 2026-10-17T04:25:02Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|15868601 | prizepicks | Bianca Andreescu | Total Games | over | 0.0420476043432368 | 2026-10-18T04:33:13Z | 2026-10-18T08:00:00.000-04:00 |
| underdog|2c7f08e3-bfb9-46a9-a3c2-ad1a481fdbf8 | underdog | Keenan Allen | Receptions | under | 0.0417473935916945 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|1172a339-6e42-41db-b5a7-6289d2410330 | underdog | Chad Ryland | Kicking Points | under | 0.0415709371698413 | 2026-10-16T04:33:49Z | 2026-10-18T20:05:00Z |
| prizepicks|15723432 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.0415547959081805 | 2026-10-14T13:48:29Z | 2026-10-18T09:30:00.000-04:00 |
| underdog|96e6e0d1-1064-4ea5-a459-163db28b91c3 | underdog | Nikola Krstovic | Shots on Target | under | 0.0410886373627692 | 2026-10-16T04:33:49Z | 2026-10-18T16:00:00Z |
| underdog|142ab904-07db-433d-ac4c-190d4126fecb | underdog | Gustav Isaksen | Shots on Target | under | 0.0402920327284735 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| prizepicks|15687735 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0402737822356972 | 2026-10-14T13:48:29Z | 2026-10-18T20:20:00.000-04:00 |
| underdog|3d0a736e-03d9-4418-8ead-177da944ffc2 | underdog | Eli Raridon | Receiving Yards | over | 0.0400417126497323 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b1f0e992-35a3-4dff-96b8-a504f2fcce7e | underdog | Travis Hunter | Receptions | over | 0.04002510038514 | 2026-10-18T04:33:13Z | 2026-10-18T13:30:00Z |
| underdog|63640af5-084b-44de-b040-faf10a7c623f | underdog | Noah Fant | Receptions | over | 0.0399408583009843 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|c71bfb1f-9fe5-4fa8-b1e7-c90ece3d1efb | underdog | Mahdi Camara | Shots on Target | over | 0.0397501989774675 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| underdog|f8c97e4a-6d9a-4a49-9686-8c79e65da1b0 | underdog | Kenneth Walker III | Receptions | under | 0.0397300431017207 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15851441 | prizepicks | Bryce Young | Pass+Rush+Rec TDs | under | 0.0395459728184809 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|7fce83f3-17db-4207-ad69-4c60c75841a6 | underdog | D'Andre Swift | Receptions | under | 0.0393303221521266 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|79f72d24-e86e-4772-8190-c760fd0c2df4 | underdog | Ashton Jeanty | Receiving Yards | under | 0.0392619218921845 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|57338cc9-9f17-4205-a875-814d1331bdd3 | underdog | Chad Ryland | FG Made | over | 0.0391548933724004 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| prizepicks|15865378 | prizepicks | Yvon Mvogo | Goalie Saves | under | 0.0387855070296548 | 2026-10-18T04:33:13Z | 2026-10-18T11:15:00.000-04:00 |
| underdog|6ea66cd4-08ff-4b33-83da-abe835a33073 | underdog | Parker Messick | Strikeouts | over | 0.0387543088622515 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|63e4f558-e691-4a4e-aedd-db349ea0147f | underdog | Bucky Irving | Receiving Yards | over | 0.038663479094679 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|1891f133-cf4d-47ec-87a5-5a7ffdcea4b0 | underdog | Chris Rodriguez | Receptions | over | 0.0385949221897411 | 2026-10-15T04:38:48Z | 2026-10-18T13:30:00Z |
| underdog|f513be39-e382-4a1c-9a5e-5e111ba0c06f | underdog | Isaiah Williams | Receiving Yards | over | 0.0385473910265883 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|ce0c73f9-886f-4ae5-977d-cadf237bc71c | underdog | Chidera Ejuke | Shots on Target | under | 0.0384085456954744 | 2026-10-18T04:33:13Z | 2026-10-18T19:00:00Z |
| underdog|a38db0cd-4417-4124-8983-99261a89b4fb | underdog | Kenneth Walker III | Receiving Yards | under | 0.0383820727412239 | 2026-10-16T04:33:49Z | 2026-10-18T20:25:00Z |
| underdog|ab1513fc-4ed0-4535-a5fb-322ee593edf9 | underdog | Dontayvion Wicks | Receiving Yards | under | 0.0381483349982191 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
| underdog|9f409c6a-5b30-48ba-a483-df126606ffd6 | underdog | Steven Kwan | Total Bases | over | 0.0381016042780747 | 2026-10-18T04:33:13Z | 2026-10-18T21:08:00Z |
| underdog|ce632ff3-3b7e-4d35-8ee3-61fd26fdc581 | underdog | Cody White | Receiving Yards | over | 0.0380932043435536 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|3c1303af-42b9-446d-8beb-c5ee3629ba77 | underdog | Tez Johnson | Receptions | under | 0.0377767694316483 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| prizepicks|15847804 | prizepicks | Kenny Gainwell | Rec Targets | under | 0.0377573087106302 | 2026-10-17T04:25:02Z | 2026-10-18T13:00:00.000-04:00 |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|d04fd702-4b03-4c5c-a34e-c0a4b42ff141 | underdog | Mahdi Camara | Shots Attempted | over | 0.0372850547239344 | 2026-10-17T04:25:02Z | 2026-10-18T15:15:00Z |
| underdog|01503e06-b6ba-454c-86cb-0bfea8d7eff0 | underdog | Brian Thomas | Receptions | under | 0.036910613248958 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|958fce36-65a6-44d4-af90-bd1ce0f3ab75 | underdog | Rico Dowdle | Receiving Yards | under | 0.0364782243986889 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|3ec6b87c-1a9a-4383-9171-ff09f7c2c179 | underdog | Hugo Bolin | Shots on Target | over | 0.0363310277563035 | 2026-10-17T04:25:02Z | 2026-10-18T15:30:00Z |
| underdog|18333681-ad54-4a4b-88b0-b41154888adf | underdog | Barryn Sorrell | Sacks | over | 0.0363005656970971 | 2026-10-17T04:25:02Z | 2026-10-19T00:20:00Z |
| underdog|cd49903a-a5a8-46e6-9ae8-fa78b048795e | underdog | Kyle Williams | Receptions | over | 0.0360365920479348 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|0f90f52a-afc9-45bb-b8f8-cd3115279f0f | underdog | Trevor Lawrence | Pass TDs | over | 0.035966064711529 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| underdog|7cbe28b4-009c-4072-9ab1-492275f541d6 | underdog | Paul Mendy | Shots on Target | under | 0.0359344207126597 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|a06f36b6-a92c-4b71-a10c-f3066f2a7280 | underdog | Geno Smith | Rush Yards | under | 0.0358721917012619 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|c12b0b39-6eb1-4357-b953-9ff51cd946b9 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.0357727206142327 | 2026-10-14T13:48:29Z | 2026-10-18T13:30:00Z |
| prizepicks|15684001 | prizepicks | Kenneth Walker III | Rush Yards | under | 0.0356785788886101 | 2026-10-16T04:33:49Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|5de92a50-4505-4181-8bd2-c9d5a7941eb2 | underdog | Sofia Kenin | Double Faults | under | 0.0356524611077894 | 2026-10-18T04:33:13Z | 2026-10-18T04:30:00Z |
| prizepicks|15847782 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.0355905616998269 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|a95efdc8-8ab8-44cd-b190-49113d65f9db | underdog | Cam Skattebo | Receiving Yards | over | 0.0353583161194935 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|04d01ed3-7a09-4f34-96cf-d7366b6335ae | underdog | KaVontae Turpin | Receiving Yards | over | 0.0350926674701363 | 2026-10-16T04:33:49Z | 2026-10-19T00:20:00Z |
| underdog|36a58f0e-9c57-456e-9766-6f882ea39387 | underdog | KaVontae Turpin | Receptions | under | 0.0349258594461875 | 2026-10-16T04:33:49Z | 2026-10-19T00:20:00Z |
| prizepicks|15853472 | prizepicks | Kayshon Boutte | Recs | under | 0.034543197787151 | 2026-10-17T04:25:02Z | 2026-10-18T09:30:00.000-04:00 |
| prizepicks|13975911 | prizepicks | Jayson Tatum | Assists | over | 0.0344807325358837 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|1d73eb0a-2eb1-4b39-bed0-f70b4c11dceb | underdog | Jon Rowe | Shots on Target | over | 0.0343623327239439 | 2026-10-17T04:25:02Z | 2026-10-18T16:00:00Z |
| underdog|385b10d3-f9c7-4de2-b680-e4c86901e29a | underdog | Derrick Henry | Receiving Yards | over | 0.0341562213034437 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| prizepicks|15850807 | prizepicks | Omarion Hampton | Rec Targets | under | 0.0340306687967373 | 2026-10-17T04:25:02Z | 2026-10-18T16:25:00.000-04:00 |
| underdog|3ba63dd2-7ac4-4586-8202-250338135768 | underdog | Bryce Lance | Receiving Yards | under | 0.0339591436575282 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|2d3eed57-9146-45b9-8b24-0d35448c6059 | underdog | Bryce Lance | Receptions | under | 0.0336167432316125 | 2026-10-16T04:33:49Z | 2026-10-18T17:00:00Z |
| underdog|1ecd56dd-d414-4af6-af1b-7caa3969b0fa | underdog | Kendrick Bourne | Receptions | under | 0.0335777878673256 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|a592a26b-786f-4a94-9bfa-2799f2948348 | underdog | Danny Namaso | Shots on Target | over | 0.0331589197445674 | 2026-10-16T04:33:49Z | 2026-10-18T15:15:00Z |
| prizepicks|15869847 | prizepicks | Titouan Droguet | Total Games | over | 0.0328003587292179 | 2026-10-18T04:33:13Z | 2026-10-19T05:00:00.000-04:00 |
| underdog|0f51da2f-832e-40f8-afb6-a5a0424cd78f | underdog | Emmett Johnson | Rush + Rec Yards | over | 0.032190742164284 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|63d06bfb-5983-462d-baff-f00ede45fa2e | underdog | Davide Frattesi | Shots Attempted | over | 0.032060655714635 | 2026-10-16T04:33:49Z | 2026-10-18T18:45:00Z |
| prizepicks|15864403 | prizepicks | Aleksandar Vukic | Total Games Won | under | 0.0320274604455403 | 2026-10-18T04:33:13Z | 2026-10-19T02:00:00.000-04:00 |
| prizepicks|15683891 | prizepicks | Aaron Rodgers | Rush Yards | over | 0.0320109065817669 | 2026-10-15T04:38:48Z | 2026-10-18T13:00:00.000-04:00 |
| underdog|b051d0c3-2880-4821-9c0c-618dd1d5ca30 | underdog | Sinja Kraus | Double Faults | under | 0.0315464723221047 | 2026-10-18T04:33:13Z | 2026-10-18T04:30:00Z |
| underdog|8abe4f2f-87e6-40f9-a686-f14e3005fdca | underdog | Jameis Winston | Pass TDs | under | 0.0315338285615001 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|3102cc27-8b02-4d43-9580-6cc37f2729b4 | underdog | Cole Kmet | Receptions | over | 0.0313315921897401 | 2026-10-15T04:38:48Z | 2026-10-18T17:00:00Z |
| underdog|e4d6dfd2-e561-44ea-b1c7-3b6f06b5b1dd | underdog | James Cook | Receptions | under | 0.0313267407554888 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| prizepicks|15780909 | prizepicks | Puka Nacua | Rec Targets | under | 0.0312347385415049 | 2026-10-15T04:38:48Z | 2026-10-18T16:05:00.000-04:00 |
| underdog|8662a61b-52b6-48d9-b983-f630d2d532f3 | underdog | Matt Gay | FG Made | under | 0.0310485582065587 | 2026-10-14T13:48:29Z | 2026-10-18T20:25:00Z |
| underdog|f6e750b1-e3dd-4875-9720-b74d2eb11700 | underdog | Josh Cuevas | Receiving Yards | over | 0.0307114558979495 | 2026-10-18T04:33:13Z | 2026-10-18T17:00:00Z |
| underdog|7abd062d-029f-45dd-982b-23c0a1dda6bd | underdog | Calvin Ridley | Receiving Yards | under | 0.0304122734825799 | 2026-10-14T13:48:29Z | 2026-10-18T17:00:00Z |
| underdog|b0ddf116-5c23-4c23-ab0d-17740e9b6132 | underdog | Oronde Gadsden | Receptions | over | 0.0303683608662909 | 2026-10-17T04:25:02Z | 2026-10-18T20:25:00Z |
| underdog|26b6d028-3d76-4969-b84b-9dedb8029c38 | underdog | Michael Wilson | Receptions | under | 0.0300666672483528 | 2026-10-14T13:48:29Z | 2026-10-18T20:05:00Z |
| underdog|269918e1-2988-4cfc-ac35-16c4b905e171 | underdog | Felix Correia | Shots Attempted | under | 0.0300384237059014 | 2026-10-17T04:25:02Z | 2026-10-18T19:00:00Z |
| underdog|83ebe900-bc71-4106-b997-fdd66285669f | underdog | Isaiah Likely | Receptions | under | 0.0300250326725849 | 2026-10-17T04:25:02Z | 2026-10-18T17:00:00Z |
