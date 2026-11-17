# Pipeline Digest -- 2026-11-17T13:09:28Z

## Run summary
- Ingestion: 26681 rows (PrizePicks OK, Underdog OK)
- Estimation: 26681 rows estimated (from 26681 ingested props)
- CLV logging: 41 newly flagged, 0 newly closed, 59 still open (112244 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|877ec685-7884-4ca7-a1d1-102f72100fdb | underdog | Bo Nix | Pass Yards | under | 0.36397031639567623 | 2026-11-16T06:19:05Z | 2026-11-22T21:25:00Z |
| prizepicks|17078200 | prizepicks | Veronika Erjavec | Break Points Won | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-17T11:20:00.000-05:00 |
| prizepicks|17061845 | prizepicks | Caleb Williams | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061851 | prizepicks | Fernando Mendoza | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| underdog|f96dbdc5-7359-4f94-b0a5-8317553a7981 | underdog | Dak Prescott | Pass Yards | under | 0.3409571299146421 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17061847 | prizepicks | Dak Prescott | Pass Yards | under | 0.3384122654101879 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061840 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.3252779099272486 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061848 | prizepicks | Baker Mayfield | Pass Yards | under | 0.32165163671963637 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061852 | prizepicks | Bo Nix | Pass Yards | under | 0.3207875090752025 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| underdog|01811504-d4c8-4a5e-bac6-a89b5dadb8cb | underdog | Bryce Young | Pass Yards | under | 0.31954007592523936 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|4ef72cf9-5c76-4409-be95-318334eaf91e | underdog | Jared Goff | Pass Yards | under | 0.31148551840872585 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|bddd3744-cab4-4359-b5e3-ae2b40d46170 | underdog | C.J. Stroud | Pass Yards | under | 0.3036023309511531 | 2026-11-16T06:19:05Z | 2026-11-20T01:15:00Z |
| prizepicks|17061849 | prizepicks | Jared Goff | Pass Yards | under | 0.2998952886937002 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061850 | prizepicks | Bryce Young | Pass Yards | under | 0.27048235462730663 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061853 | prizepicks | Kirk Cousins | Pass Yards | under | 0.26028541200637423 | 2026-11-17T13:14:06Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17061844 | prizepicks | Tyler Shough | Pass Yards | under | 0.249596263938357 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|13469f60-059e-4666-bf92-526fcb0eeac0 | underdog | Jonah Coleman | Rush Yards | under | 0.23761066363613148 | 2026-11-16T06:19:05Z | 2026-11-22T21:25:00Z |
| prizepicks|17021667 | prizepicks | Despina Papamichail | Total Games Won | over | 0.2372983834583926 | 2026-11-16T06:19:05Z | 2026-11-17T08:00:00.000-05:00 |
| prizepicks|17062829 | prizepicks | Emeka Egbuka | Rec Yards | under | 0.22427633469269959 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062823 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.20121645364759722 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061963 | prizepicks | Jonah Coleman | Rush Yards | under | 0.1991404536452812 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17062826 | prizepicks | Colston Loveland | Rec Yards | under | 0.18934940884625828 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|c79b402a-d890-4544-b009-478b1f9ca04d | underdog | Jameson Williams | Receiving Yards | under | 0.15818549364248446 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|7366db87-6436-4261-a7ab-08d5c3ea89ae | underdog | Chuba Hubbard | Rush Yards | under | 0.13714694341105027 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|7e0bcf99-5689-440b-8ec6-baaa02f6f356 | underdog | Trey McBride | Receiving Yards | under | 0.13337858764715516 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17062831 | prizepicks | Jameson Williams | Rec Yards | under | 0.11872113566024023 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|1c3ab1ad-e32d-483c-ba65-a163b75164ae | underdog | Javonte Williams | Rush Yards | under | 0.11519863917518858 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17061964 | prizepicks | Jordan Mason | Rush Yards | under | 0.11062677387151276 | 2026-11-17T13:14:06Z | 2026-11-22T20:20:00.000-05:00 |
| underdog|c583c27f-e8e0-4e06-8609-970e1addd831 | underdog | Chris Olave | Receiving Yards | under | 0.10166774504769993 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17062824 | prizepicks | Luther Burden III | Rec Yards | under | 0.10137835357799285 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062819 | prizepicks | Saquon Barkley | Rec Yards | under | 0.09863869301169803 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| underdog|f8c9d406-3817-4490-8e0e-07418b74231d | underdog | Tetairoa McMillan | Receiving Yards | under | 0.09521537705048622 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|53fee2ec-04d5-4ef5-92ea-5ba4904244c8 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.0928074810363998 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| underdog|a425c224-5d29-4a46-a70b-3654d7085933 | underdog | Malik Nabers | Receiving Yards | under | 0.09180785896954857 | 2026-11-16T06:19:05Z | 2026-11-22T21:25:00Z |
| underdog|32993774-ad09-43b8-8200-74c3303de68b | underdog | Cam Skattebo | Rush Yards | under | 0.08865504786031486 | 2026-11-16T06:19:05Z | 2026-11-22T21:25:00Z |
| underdog|27fc11d1-30ad-4f1a-899e-b3dde57a705e | underdog | CeeDee Lamb | Receiving Yards | under | 0.0841787598496383 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17069903 | prizepicks | Cibastian Broughton | Pass Comp | under | 0.07703897220700162 | 2026-11-17T13:14:06Z | 2026-11-18T19:00:00.000-05:00 |
| prizepicks|17061961 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.07421460278652392 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17053608 | prizepicks | Arijanet Muric | Goalie Fantasy Score | under | 0.07351349210905256 | 2026-11-17T13:14:06Z | 2026-11-17T14:45:00.000-05:00 |
| underdog|d8b8533e-23fb-49eb-9469-929457ca0f41 | underdog | Tony Pollard | Rush Yards | under | 0.07124799057234155 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17062825 | prizepicks | Rome Odunze | Rec Yards | under | 0.06934931203037698 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062820 | prizepicks | Trey McBride | Rec Yards | under | 0.06498754344887514 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062817 | prizepicks | Pat Freiermuth | Rec Yards | under | 0.061571812750696786 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17053592 | prizepicks | Egil Selvik | Goalie Saves | under | 0.06087467181479178 | 2026-11-17T13:14:06Z | 2026-11-17T14:45:00.000-05:00 |
| prizepicks|17061832 | prizepicks | Jared Goff | Rush Yards | over | 0.060379424163094386 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061958 | prizepicks | Javonte Williams | Rush Yards | under | 0.05867691672271225 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062828 | prizepicks | George Pickens | Rec Yards | under | 0.057941658909858806 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062838 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.04762708868780563 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
| prizepicks|17061833 | prizepicks | Bryce Young | Rush Yards | under | 0.047291172718622376 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17055345 | prizepicks | Gonçalo Ramos | Shots | under | 0.04699524525314913 | 2026-11-17T13:14:06Z | 2026-11-17T14:45:00.000-05:00 |
| prizepicks|17048468 | prizepicks | Jeremiah Smith | Recs | under | 0.0451889882160037 | 2026-11-17T13:14:06Z | 2026-11-21T12:00:00.000-05:00 |
| prizepicks|17062821 | prizepicks | Travis Kelce | Rec Yards | under | 0.04278357094048435 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062822 | prizepicks | Chris Olave | Rec Yards | under | 0.04199283253040853 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17053602 | prizepicks | Egil Selvik | Goalie Fantasy Score | under | 0.03939610933048021 | 2026-11-17T13:14:06Z | 2026-11-17T14:45:00.000-05:00 |
| prizepicks|17062827 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0391841333439954 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061960 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.034137148515200666 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062834 | prizepicks | Tetairoa McMillan | Rec Yards | under | 0.03137015023617118 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17064400 | prizepicks | Benjamin Bonzi | Total Games | over | 0.030473121260471858 | 2026-11-17T13:14:06Z | 2026-11-17T12:00:00.000-05:00 |
| prizepicks|17062839 | prizepicks | Tee Higgins | Rec Yards | under | 0.03001893073314066 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
