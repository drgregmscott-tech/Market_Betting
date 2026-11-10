# Pipeline Digest -- 2026-11-10T12:31:03Z

## Run summary
- Ingestion: 21250 rows (PrizePicks OK, Underdog OK)
- Estimation: 21250 rows estimated (from 21250 ingested props)
- CLV logging: 386 newly flagged, 0 newly closed, 391 still open (110095 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|d16261fb-2c6f-4e0e-8880-5c0c40790431 | underdog | Aaron Rodgers | Pass Yards | under | 0.4 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|ba92e188-1305-44b2-a0eb-5960784146f1 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|4239b8d8-10aa-47ae-b337-22e4f80f92f4 | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ac75db5b-eb0b-4a85-a495-ce8e6abe8b3c | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|79672160-7023-4961-aa5f-4f759651cbb6 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|49807980-07fb-4254-b418-978f13601840 | underdog | Simi Fehoko | Receiving Yards | under | 0.3993192054006508 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|efb1059f-f136-4794-9a72-10de9d0a03a4 | underdog | Zach Charbonnet | Receiving Yards | under | 0.397859065932332 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|651718aa-f819-4e2f-ad0b-6295b7832c86 | underdog | Drake Maye | Pass Yards | under | 0.38488538296258934 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|bf3b1159-fa11-42f9-ae28-7421be127235 | underdog | Eddy Pineiro | FG Made | under | 0.3826019825177006 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|1c1ba708-d063-467b-8cf5-9860da400014 | underdog | Cam Ward | Pass Yards | under | 0.3824961951062982 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|08345c52-8552-4b04-813c-2f46ea4286f3 | underdog | Simi Fehoko | Receptions | under | 0.3799490814604448 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|dec5c203-a4db-4a81-9c3b-533a2f9747bd | underdog | Trevor Lawrence | Pass Yards | under | 0.3773869346733668 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ed52aba9-3e91-4691-b2a8-bfcde1e886ab | underdog | Michael Penix | Pass Attempts | under | 0.3738097977611652 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a86e03be-f695-4395-91c2-9e961f5dd064 | underdog | Stefon Diggs | Receiving Yards | under | 0.36120009761511573 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|9b68965c-3c26-46a8-baae-a65e2eecf9ad | underdog | Brandon McManus | FG Made | under | 0.35442585143255134 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|82b5b064-1df0-43cf-9b3e-7f9065dbebdb | underdog | Kirk Cousins | Pass Yards | under | 0.3523398022115709 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16834518 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16834519 | prizepicks | Justin Herbert | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| prizepicks|16834516 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16834515 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16834511 | prizepicks | Malik Willis | Pass Yards | under | 0.35049289149780605 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|1a25507b-8125-4524-83eb-bd6dc420d8a6 | underdog | Jared Goff | Pass Yards | under | 0.3501184306337788 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|b9435fd5-7f24-4097-8678-b955d06381e2 | underdog | Brandon McManus | Kicking Points | under | 0.34329896907216495 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|6ec00fee-ae89-42b7-a563-9216f15ce2ad | underdog | J.J. McCarthy | Pass Yards | under | 0.33214221319781534 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|b91f0195-7582-492f-b9cf-c3961e097353 | underdog | Jayden Daniels | Pass Yards | under | 0.3299367245883327 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|4b540f15-2c50-4b08-9287-75640b58c283 | underdog | Bryce Young | Pass Yards | under | 0.32343608075743624 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f9978ce2-db4f-472d-ae6b-7ae2ed4383c0 | underdog | Brock Purdy | Pass Attempts | under | 0.3095759047079447 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|b9826de6-517b-421f-aedc-9cd8b490bd07 | underdog | J.J. McCarthy | Pass TDs | under | 0.3081632653061225 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|596f0ab6-9140-4f56-a4cb-83ddc49c3a9c | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.3061762999558397 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| prizepicks|16834512 | prizepicks | Bryce Young | Pass Yards | under | 0.3052224897990242 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16834507 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.30077963572659205 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|15f7af6e-24f2-44fc-a87e-6ed7d7f7e7bb | underdog | Cam Ward | Pass Attempts | under | 0.29158019971115134 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|017de95e-24a8-4a55-9185-759ab5e39785 | underdog | Drake Maye | Pass Attempts | under | 0.2870204978984535 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|562e1836-2e61-40c1-9185-24bd5cd0ea66 | underdog | Jordan Love | Pass Yards | under | 0.2819158395036473 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16834509 | prizepicks | Geno Smith | Pass Yards | under | 0.2763361682548745 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4426e732-6666-4dad-8847-df60408b6e0e | underdog | Eddy Pineiro | Kicking Points | under | 0.27246339729437163 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|32431b7b-bc1f-4591-bb5c-40d5aa435fcf | underdog | Jayden Daniels | Pass Attempts | under | 0.27080781658432496 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|a33b18aa-3fe0-472a-aeff-89169e5f8929 | underdog | J.J. McCarthy | Pass Attempts | under | 0.26718574832054187 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|a3afb538-c385-463c-a16b-d6019554b469 | underdog | Bryce Young | Pass Attempts | under | 0.2666070331281989 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5bdf5d5e-500d-4fc9-be1d-735abbff4d0f | underdog | Deshaun Watson | Pass Yards | under | 0.25748581006210247 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c87d8ad8-a826-4ad7-ad27-0d1400b68a7e | underdog | Chase Brown | Rush + Rec Yards | under | 0.2569404038837313 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8614ca48-43d3-4bc8-9ed6-bb547f1ace74 | underdog | Joe Burrow | Pass Yards | under | 0.25576008038391973 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|67e20311-8c36-4f53-b2d6-a3d86f0b73fa | underdog | Malik Willis | Pass Attempts | under | 0.2557485151021238 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8cf0d860-c740-4aa8-b1fe-3ddfdeff4a17 | underdog | Antonio Williams | Receptions | under | 0.2540644281719815 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|e591af26-5ad6-4292-87b6-7cf00cdf80f7 | underdog | Deshaun Watson | Pass Attempts | under | 0.2529238482215044 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|95f2207f-7b52-4609-a8c3-40f32aad001f | underdog | Trey McBride | Receptions | under | 0.24959644719570862 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|024d53fe-7ffd-4c3f-945d-bd7f2f4cd99d | underdog | Tyler Shough | Pass Yards | under | 0.24665483230534302 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a79bfa01-59aa-42db-9edb-02ca40748c96 | underdog | Brock Bowers | Receiving Yards | under | 0.2369547095491017 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|eda5085f-4e00-486d-85fc-f0800f099adf | underdog | Joe Burrow | Pass Attempts | under | 0.23491606853910285 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|3d0914d2-e2f9-4bf9-ac0c-990ee663d5e8 | underdog | Jacoby Brissett | Pass Yards | under | 0.23375078896231527 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|91d23eb8-8b6f-4a0b-92e5-2d580cefac17 | underdog | George Kittle | Receiving Yards | under | 0.22822277415661296 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|35687887-1ee9-4560-8b37-e80f4f922af6 | underdog | C.J. Stroud | Pass Yards | under | 0.22809076425687402 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|90e26412-adf9-4ad1-ba33-508280ec4d42 | underdog | Germie Bernard | Receiving Yards | under | 0.22675091170249617 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|38aaa9d0-5d08-4a1a-903d-4fe0517bfc40 | underdog | Antonio Williams | Receiving Yards | under | 0.22356741518335665 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|2dfe4a4e-673f-4b70-9848-bf6c7b6c6341 | underdog | Reggie Virgil | Receiving Yards | under | 0.22038234116811617 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|6c6cccec-3ac6-4fef-97b2-c7412ed4ceea | underdog | Kyle Pitts | Receiving Yards | under | 0.22031633112583515 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|169cb841-cffa-4109-8027-3415c4f4b563 | underdog | George Kittle | Receptions | under | 0.2194077839592593 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|1d59abaf-41f5-4b96-a4ed-b899acfcff7b | underdog | Ollie Gordon | Receiving Yards | under | 0.21813366412209023 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16834513 | prizepicks | Tyler Shough | Pass Yards | under | 0.21404760098629738 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|900a6acc-8f2e-4a73-8d6c-9a35b225cafb | underdog | Jared Goff | Pass Attempts | under | 0.2123603264736973 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|7ab6fe1f-db93-4cad-8eda-7130eb629d23 | underdog | Aaron Rodgers | Pass Attempts | under | 0.20920808520190182 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|f56ab5cd-5f1b-4cfa-9d0b-04814d327fb1 | underdog | Woody Marks | Rush Yards | under | 0.20525939528062387 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|051a8c4f-8105-4095-aab4-7a5b0cba7371 | underdog | C.J. Stroud | Pass Attempts | under | 0.20323087968521425 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7516654f-3f76-4671-b129-8e4b8f411e28 | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.20276218950484037 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|f90743a5-9d2a-47d3-a4e4-089c9764ad13 | underdog | Dak Prescott | Pass Attempts | under | 0.2011150399848315 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|87bfd021-0498-4180-b485-15610037e2e5 | underdog | Kaelon Black | Receiving Yards | over | 0.1963921949855576 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|a30ba4c9-38bb-48fa-86e2-da07a6cebc7b | underdog | Jadyn Glasser | Pass TDs | under | 0.19580479982839094 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|af0f9f6b-1af3-4df6-9d03-0bedb90f0aa6 | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.19397346806442384 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|df028c43-0eee-4273-830e-703d5cb09224 | underdog | Rachaad White | Rush Yards | under | 0.19157154630314255 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|0ca5f198-cc15-4b12-b643-c3388a576202 | underdog | Tank Dell | Receptions | under | 0.19110284381179832 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|547810a9-bf75-407a-89ae-51d523fe2f92 | underdog | Cam Little | FG Made | under | 0.18990792795409317 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|1773beb2-6463-473c-9758-521aac3133f1 | underdog | Christian McCaffrey | Receiving Yards | under | 0.18698819476047657 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|b8c9a66b-80c4-49bb-aa02-5f7bc3f5d24a | underdog | Malik Willis | Pass TDs | under | 0.1868872183484781 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|322f86b2-2dd2-4810-9a77-27281eec611b | underdog | Jadyn Glasser | Pass Yards | under | 0.18632213869558645 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|ca8ee1a5-ee71-426e-911c-a3f15717d09d | underdog | Trey McBride | Receiving Yards | under | 0.18354292530410377 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|336befd7-fc3b-4fc6-be96-8f9f930dd43f | underdog | Jared Goff | Pass TDs | under | 0.1828305718973564 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| prizepicks|16834801 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1816833032066426 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|bf391676-2253-4281-925c-1f792252cac9 | underdog | Christian McCaffrey | Rush Yards | under | 0.17825982394026108 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|1e181e12-56a4-4cc4-bde1-a00efbe88740 | underdog | Stefon Diggs | Receptions | under | 0.17719685057933365 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|37248246-f00f-4981-be9d-48213b7eb191 | underdog | Kirk Cousins | Pass Attempts | under | 0.1767876498115326 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|fa866b4a-bfec-43b4-87e1-230c1299d45f | underdog | Marta Kostyuk | Double Faults | under | 0.17466785904515392 | 2026-11-10T12:33:48Z | 2026-11-10T20:00:00Z |
| underdog|ab208bdb-ddee-40f9-a2ed-f481ef72f216 | underdog | Drake London | Receptions | under | 0.17466437471048346 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|59038cf2-43de-418b-adf5-64a277177606 | underdog | Nico Collins | Receiving Yards | under | 0.17448857944120932 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bed83661-cc7d-4b22-9b07-e0978ada4d5d | underdog | Jameson Williams | Receiving Yards | under | 0.1733097016002607 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|1c595c69-237e-459e-8725-0baa3a1074b4 | underdog | Javonte Williams | Receiving Yards | under | 0.17315131905088377 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|88ee8093-6a82-455e-a595-8a33db563da3 | underdog | Trevor Lawrence | Pass Attempts | under | 0.17295149167523682 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b59c83a6-7075-4cc3-84dd-27157fa643ac | underdog | Jahan Dotson | Receptions | under | 0.17063963423916995 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7f8aca84-6236-4ecc-a073-d3842eb118b3 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.17051169105217812 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ee9a0405-33bb-456d-a2ef-754c6c2c03a7 | underdog | Tyler Shough | Pass Attempts | under | 0.1678377974371722 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|45b97525-837e-49e1-ab67-71c533621a28 | underdog | Parker Washington | Receiving Yards | under | 0.16769035739681737 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|5cf71cd9-66a9-45c7-9bf6-5686c2e9d6a7 | underdog | Zach Charbonnet | Rush + Rec Yards | under | 0.16730395974955514 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|696c6b73-3e04-426b-a463-26276c4aee5c | underdog | Ryan Fitzgerald | FG Made | under | 0.16692795074675848 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|659b286c-687a-43f0-b782-5a1234a05458 | underdog | Quinshon Judkins | Receptions | over | 0.16431586645270752 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b9338725-50fc-40f4-8453-1eca37fc7ec6 | underdog | Austin Ekeler | Receptions | under | 0.1614508530669193 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| prizepicks|16834640 | prizepicks | Woody Marks | Rush Yards | under | 0.16140868621854165 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c6dfbd99-fd13-4316-8739-6848da0fb430 | underdog | Devin Singletary | Rush Yards | under | 0.16134742662105228 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|d83327fe-b182-4215-9894-53b557ab8abc | underdog | Austin Ekeler | Rush Yards | under | 0.16043185030809792 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|43d067f1-bb0f-4c09-acf1-fa7919bc9723 | underdog | Jared Goff | Rush Yards | over | 0.16011142578061638 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|28e41540-e6d5-4ec1-b474-b3fb179168ec | underdog | Justin Herbert | Pass TDs | under | 0.1593713737739526 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| prizepicks|16834646 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.15848722202295062 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f3733138-10af-46da-8e69-cf5ca4b940fc | underdog | Reggie Virgil | Receptions | under | 0.15825220568688703 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16834797 | prizepicks | Rashee Rice | Rec Yards | under | 0.15730678889446847 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|b2c64b5f-e4d8-4af8-a6bf-a442057addd9 | underdog | Ollie Gordon | Rush Yards | under | 0.1561573685847356 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ed3615da-db62-4173-a8c4-eee0fb7fd836 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.15605244592623502 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d33e8d3e-52ac-4c3c-ad13-ffec4923f41e | underdog | Jadarian Price | Rush Yards | under | 0.1550757413132794 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|cf82fa2c-dab9-4d5b-a7f3-ab62d6f577bf | underdog | Matthew Stafford | Pass Yards | under | 0.1545738423813161 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|cddd4a3b-5c6d-4f33-99b7-b8698826ae94 | underdog | Katin Houser | Pass TDs | over | 0.15429254355884753 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|b95d2f57-7740-4476-a60e-dca281fb5487 | underdog | Devin Singletary | Rush + Rec Yards | under | 0.15380926159929698 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|97a67afc-3f9f-4982-8bae-be868c2c4737 | underdog | Devon Dampier | Pass Yards | under | 0.15303323942761993 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16834815 | prizepicks | Brock Bowers | Rec Yards | under | 0.15272158307530515 | 2026-11-10T12:33:48Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|c5c4fe7e-563e-4a77-ae50-060011c7dec8 | underdog | Xavier Hutchinson | Receptions | under | 0.1509666630300549 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2e165ef5-272e-47fb-8214-52bc9d58510a | underdog | Amon-Ra St. Brown | Receptions | under | 0.14980442293467233 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|e90cfcc5-5236-47d1-9959-1ebc12bca4d6 | underdog | Bhayshul Tuten | Rush Yards | under | 0.14924806003717772 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e3317ebd-1d1a-4ac2-8dc1-999860638691 | underdog | Jameson Williams | Receptions | under | 0.1486746602368635 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|1a20f785-f85c-4e70-a420-adf5f0ed3164 | underdog | Ollie Gordon | Receptions | under | 0.148665850420447 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|36662c72-eeb6-4098-8bda-06fdddb4bea7 | underdog | Jayden Daniels | Pass TDs | under | 0.1470544440824959 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|7ba301e0-86d5-483e-8dca-c9b8a18d0893 | underdog | Zach Charbonnet | Rush Yards | under | 0.145166077871979 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|4d0e9f33-30c1-4cbd-811b-3f0d61054bcb | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.14378965381475595 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|21ace0c9-85f0-43f3-9392-a8bbadc5666b | underdog | Trey Butkowski | XP Made | over | 0.14320322887137465 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|4c42a4f7-59bd-4cc5-96de-2caa245cf96e | underdog | Ja'Marr Chase | Receptions | under | 0.14198666098231127 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|7131ca1a-e22f-4632-8fb6-63129a1d8839 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.14128001043380056 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|8cf1b796-71c3-41fe-9bfc-c947b4dd970f | underdog | Dylan Sampson | Receptions | under | 0.1400167311068875 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|eca2d6e6-ea22-4cad-a866-f918f2ee77c2 | underdog | DK Metcalf | Receiving Yards | under | 0.1392606038704155 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|aa70ba25-a303-4c52-9769-639de476cfcf | underdog | Javonte Williams | Receptions | under | 0.13847697518960522 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| prizepicks|16834820 | prizepicks | Christian McCaffrey | Rec Yards | under | 0.1379306598172515 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f360ab27-deb2-4f72-b437-6349dc28e573 | underdog | Parker Washington | Receptions | under | 0.13510031202715655 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a4e5f72a-b0f9-437d-8eed-fe72a8786ed6 | underdog | Bijan Robinson | Receptions | under | 0.13450123154200033 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|846407d4-b764-4983-8cd7-df2f8d86efc0 | underdog | Rachaad White | Rush + Rec Yards | under | 0.13438874915938148 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|1b952c0b-561b-4612-8997-fa310f72e078 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.1331814183366642 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|78561eae-a89c-4493-8199-fece506a3fe9 | underdog | Jalen Buckley | Rush Yards | under | 0.13285817108480713 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|f0100902-2759-4817-a164-2c7d3cb0236d | underdog | Quinshon Judkins | Receiving Yards | over | 0.13251091684739158 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8475bce1-90cf-43c8-9bdc-19e950db157a | underdog | AJ Barner | Receptions | under | 0.1321036071433428 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|ad49c1a3-20cd-48ee-8447-3f9c6b778470 | underdog | Zach Charbonnet | Receptions | under | 0.13186048887942314 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c269c6d4-6142-4a3e-8070-f134ab849600 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.13176886954144162 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|6c8fb1bf-d574-4d06-b8ae-800a2f26f70e | underdog | Javonte Williams | Rush + Rec Yards | under | 0.13141661311916575 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|7a1ed30d-da55-441c-b6f0-c5cf7618c573 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.13110361173012197 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9be334e3-2b26-43b7-bd6c-0298f4af4fce | underdog | Justice Hill | Receiving Yards | under | 0.13105240860707623 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| prizepicks|16834805 | prizepicks | Tucker Kraft | Rec Yards | under | 0.13048896157966627 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|267fd95f-61f9-41c9-ab84-462c5918f643 | underdog | Zay Flowers | Receptions | under | 0.12835319508736753 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|b7e074c6-71f7-4056-b312-ef174fdec611 | underdog | Chig Okonkwo | Receiving Yards | under | 0.1276225423920111 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|8b8188cc-2c70-4e25-8780-207191b0a27d | underdog | Jadarian Price | Rush + Rec Yards | under | 0.12478565778112505 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|64fe717c-14a9-4a4d-b286-fb2c31130ca5 | underdog | Jason Myers | FG Made | under | 0.12423824312528586 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d089428b-65e7-465b-a22b-a541720e63b3 | underdog | Jayden Maiava | Pass TDs | over | 0.12386144498407786 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| prizepicks|16834809 | prizepicks | Tyler Warren | Rec Yards | under | 0.12377827571835343 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7da7556c-a1f4-42ec-ad80-c12d0d953524 | underdog | John Metchie III | Receptions | under | 0.12299883356747898 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f5a259bb-3160-42f7-8263-8e839fdce757 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.12232246611646624 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|9027508e-0f29-4af7-8017-6ba60afee0b5 | underdog | Derrick Henry | Rush Yards | under | 0.1220716163832134 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|6e5ee676-5587-4acc-9a23-4d4d6844bf66 | underdog | Chuba Hubbard | Rush Yards | under | 0.12201835230401836 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|cf37c889-4eca-4cd0-acdb-5ef3caf76c5b | underdog | Ka'imi Fairbairn | FG Made | under | 0.12158788342133897 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|941cffba-4b42-4435-8769-a31cbd72dc50 | underdog | Tee Higgins | Receptions | under | 0.11877140010710996 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|505a5448-6d1e-46c6-98b7-25df0210e7cc | underdog | Chuba Hubbard | Receiving Yards | under | 0.11651305043694171 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|50218199-1d27-4d93-8b4e-5cdfb72e67c5 | underdog | Broc Lowry | Pass Yards | under | 0.1150729307729903 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|15af648f-e21e-4026-b017-90289b48e4bb | underdog | CeeDee Lamb | Receptions | under | 0.11504505706140522 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|26fa6e2a-fad8-4b59-a8f2-07f9f380dbbd | underdog | Trey Butkowski | FG Made | under | 0.11470902398646865 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|4980e13b-b332-4cb3-b311-c8aada8c0159 | underdog | Kyle Pitts | Receptions | under | 0.11437219464215653 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a1446e01-4106-432d-b868-dfa71b55822d | underdog | J.J. McCarthy | Rush Yards | under | 0.11435810189473061 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|f8a4f538-aa21-4095-a5d7-7f3123037256 | underdog | Caleb Heavner | Pass Yards | under | 0.11394798901170622 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|0e96c17c-f25a-4ef5-9eba-ee6a5a943bd0 | underdog | Chase Brown | Rush Yards | under | 0.11357964455284286 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|5c625434-b11a-46c4-a6af-d0fc53c2f2a9 | underdog | Dak Prescott | Pass TDs | under | 0.11340998483490083 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|7a6dd424-2fdc-466c-b847-16a47251614c | underdog | Connor Calvert | FG Made | over | 0.11328783871436227 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|7857c427-00ea-44f3-9c45-48f9e7f2c9b5 | underdog | Trevor Lawrence | Pass TDs | under | 0.11317375136374375 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|cde7c70e-d481-4784-9d2e-2a93b9e2daa7 | underdog | Sam LaPorta | Receiving Yards | under | 0.11256764743862924 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|992fa67a-feec-4626-95dc-f2c04f2580cf | underdog | Matthew Stafford | Rush Yards | over | 0.11213733898109268 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|b54e3236-2070-4997-8320-39153255594b | underdog | Elic Ayomanor | Receptions | under | 0.11160954349764363 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3b01acf2-eefa-4496-a642-bf1c849db45d | underdog | Chris Bell | Receptions | under | 0.11116746721824522 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c8e62997-bf7f-4a47-a373-17ef73c7ca9a | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.10966519127430818 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|86e2fe10-1f76-458b-8c4f-20850a6c532b | underdog | Nick Poulos | Pass Yards | under | 0.10928186023409148 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|68bdebda-2809-43c9-9da8-016cba6e3b43 | underdog | Rashod Bateman | Receptions | under | 0.10710776791785359 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| prizepicks|16814516 | prizepicks | Laura Samson | Total Games | over | 0.10672876406480503 | 2026-11-10T12:33:48Z | 2026-11-10T12:20:00.000-05:00 |
| underdog|325a8205-94f4-4430-8e00-d9d2ddc2a9ec | underdog | Mike Gesicki | Receptions | under | 0.10565045023732611 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|ec70c19b-7291-4f35-9908-ad42b07c7250 | underdog | Brock Bowers | Receptions | under | 0.10562370878500471 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|be68fe9f-9661-44a4-a0a6-159ec51ada3a | underdog | Deshaun Watson | Rush Yards | under | 0.1055870104546599 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|dccb6e7d-029a-475b-ab4f-85d6cedff926 | underdog | Holden Geriner | Pass Yards | under | 0.10469471819604292 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|0596f1b7-efa6-4a5b-9155-5b701ed2e338 | underdog | Tony Pollard | Receiving Yards | under | 0.10347518890631369 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|6a941d47-82e3-491e-9755-22dea3004ecd | underdog | Malik Nabers | Receptions | under | 0.10346829848265682 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|a2ab359d-f95e-4274-a5d9-d5cdb046bed9 | underdog | DK Metcalf | Receptions | under | 0.10300602023686134 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|e10888ed-ae51-49a0-ab78-3a968b873283 | underdog | Matthew Stafford | Pass Attempts | under | 0.10236489378726288 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|b58d4951-3cf7-4235-9f2b-f9836e774dae | underdog | Drake London | Receiving Yards | under | 0.1020493545084814 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|51820dd7-063c-4751-be38-84c9a6983fed | underdog | Christian McCaffrey | Receptions | under | 0.1016183424097532 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|9eb37f45-e1cf-4180-af9e-cc15099ac71e | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10100699602094965 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|ef7881f8-c4d2-4023-87ab-e6d713e1901e | underdog | Chase Brown | Receptions | under | 0.10056774346872166 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8150638b-9a7e-427a-aba6-76704ed97855 | underdog | Ethan Moczulski | FG Made | over | 0.09839210553400768 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|6f6e76ef-69e3-4315-83cb-ea6ec48daea1 | underdog | Chad Ryland | FG Made | over | 0.09807717467815241 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|8b32f3be-fb2d-4575-9703-ece20cb7d845 | underdog | Holden Geriner | Pass TDs | under | 0.09771050871750353 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|954ad452-8bec-4840-bae5-048bcd6542d9 | underdog | Mitchell Evans | Receiving Yards | over | 0.09733725531537551 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|92efc1e0-6e09-45b5-9380-ed2ef9424766 | underdog | Noah Fifita | Pass Yards | under | 0.0962718991546474 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|cb3389d9-31f8-4dd5-a0a5-dd253ae2d3e6 | underdog | AJ Barner | Receiving Yards | under | 0.09611135344747002 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|df28531a-6ae3-4786-9a32-3157e1f129ab | underdog | Cibastian Broughton | Pass TDs | under | 0.09581634694211427 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|a0d2c31e-f6cb-4bee-81be-02dcf80d0449 | underdog | Carnell Tate | Receiving Yards | under | 0.09537210117181494 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4d223278-9894-42c8-b446-04f9eeed6373 | underdog | Chuba Hubbard | Receptions | under | 0.09417655117218815 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7262a512-4612-447b-a039-dad68aa3c88e | underdog | Cam Ward | Pass TDs | under | 0.09413625322979502 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|db4aa5a1-9ac8-4771-84cd-ae5337de377d | underdog | Jalen Coker | Receiving Yards | under | 0.09292621510911137 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a06cc096-a557-4d6f-beae-84bad24f4532 | underdog | Brock Purdy | Pass TDs | under | 0.09255192361854181 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|89ff9cd7-cdec-4b6a-a310-297fe12828e2 | underdog | Riley Neer | Receptions | under | 0.09205550171602683 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| prizepicks|16832526 | prizepicks | Aveion Chenault | Recs | under | 0.09160508160324898 | 2026-11-10T12:33:48Z | 2026-11-10T19:00:00.000-05:00 |
| underdog|1459bce9-c246-4bcf-a79d-d9ee9ad81e61 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.09121419257612451 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|cde77409-6c4b-4d8e-9073-074e686e1b6d | underdog | Cam Little | Kicking Points | under | 0.09049138686982805 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e564a712-42d2-4861-972a-290db5c57294 | underdog | Aveion Chenault | Receptions | under | 0.09034358528011865 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| prizepicks|16834826 | prizepicks | DK Metcalf | Rec Yards | under | 0.09020306892719043 | 2026-11-10T12:33:48Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|845e4dfd-760e-47fa-be35-653b69ab5d2a | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.09009346261702689 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|a031e4c8-4faf-44be-bf1f-3202c7ae5160 | underdog | Kenneth Walker III | Receiving Yards | under | 0.08901286872690384 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|95c6d2f2-23ef-4203-a9d8-04ebad281b7c | underdog | Joe Burrow | Pass TDs | under | 0.08853194239381257 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|60f56ef3-30f8-4f82-853c-39b4fb03c274 | underdog | Isaiah Likely | Receiving Yards | under | 0.08839971393428592 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|8df84f78-a4cb-4775-ba6c-780c5b66cf25 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.08765142486952304 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2c90967a-d709-406d-9794-fb62694b930b | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.08755420648445 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|e40d5b91-3ca7-447c-b787-4c1b15b72449 | underdog | Dylan Sampson | Rush Yards | under | 0.08751405697424308 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|78950a32-2063-461f-b320-9cef702332d1 | underdog | Jay Kastantin | Pass Yards | under | 0.08732137816004826 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| prizepicks|16834650 | prizepicks | Derrick Henry | Rush Yards | under | 0.08663217446763538 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|4694b5d1-f4d8-438f-bd98-1a80b241dc48 | underdog | Chris Olave | Receiving Yards | under | 0.08654435597157062 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|fb923c2d-7f6e-44ef-b625-019242f8db88 | underdog | Caleb Heavner | Rush Yards | under | 0.08638593310713394 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|f659570b-8335-4e5f-bb65-b61d018619f5 | underdog | Jason Wright | Pass TDs | under | 0.0849884977280535 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|2241dc3b-3cce-4713-948a-899c19938a90 | underdog | Bhayshul Tuten | Receptions | under | 0.08488347843269772 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f92298ed-1466-4be1-9206-06363975f1bb | underdog | Dru DeShields | Pass TDs | over | 0.08467564609455847 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|a43a1733-5f39-482c-ba00-79805845cf4e | underdog | Jacoby Brissett | Pass Attempts | under | 0.08429939067546144 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|095d7662-7876-4544-a661-85a9352bc8b9 | underdog | Darnell Washington | Receptions | under | 0.08429478520005662 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|7f654e7f-ce6f-4514-b607-3b45826bc886 | underdog | Carnell Tate | Receptions | under | 0.08352541400712155 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0a225afc-fca1-4959-82b0-c5702e9643ba | underdog | KC Concepcion | Receiving Yards | under | 0.08273359636168665 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|aea16027-a938-4fd9-8295-161c5d52bb3c | underdog | Jacoby Brissett | Rush Yards | under | 0.08273339673427216 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| prizepicks|16834642 | prizepicks | Jonathan Taylor | Rush Yards | under | 0.08067797097966689 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|0f1e3f4e-1c18-4ec3-91e6-25199faf4590 | underdog | Caleb Heavner | Pass TDs | under | 0.08045821472878856 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|5e94977c-0093-48e8-becf-5e8910977a9b | underdog | Drake Maye | Rush Yards | under | 0.08004423976338015 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|248d37e1-0a7e-4b96-8aee-f0a21de1bd98 | underdog | Javonte Williams | Rush Yards | under | 0.0800309734819954 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|0b2e9d13-d865-4ce4-8130-1811f8c75f1f | underdog | Jahmyr Gibbs | Receptions | under | 0.07974674760702072 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|28b73f9a-7464-4028-9994-b3e9777c631e | underdog | Juwan Johnson | Receptions | under | 0.07927138801736044 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|92bdb643-87dc-4f67-a671-989519ce3c1a | underdog | Germie Bernard | Receptions | under | 0.07870963918803697 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|e783dc26-5825-408b-ba88-074ae8338f79 | underdog | Tyler Allgeier | Receptions | under | 0.07858479788991879 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|256230b6-9261-4566-8fd2-01b0301be098 | underdog | Devaughn Vele | Receiving Yards | under | 0.07829594616473112 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0c41b978-dad0-4b27-b35a-3ac879f1cc46 | underdog | Keldric Luster | Pass Yards | under | 0.077954948972904 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|c56fb924-60e5-4a74-adb3-8288fc679008 | underdog | Drew Stevens | Kicking Points | under | 0.0778937129166114 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|8a1fb4d0-085d-4732-af62-3cb7479e1243 | underdog | Trevor Lawrence | Rush Yards | under | 0.07787191865224208 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|72630e1f-91a6-4eb1-b703-90feab5f3fc7 | underdog | Tommy Tremble | Receiving Yards | under | 0.07742498270766673 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|943b6125-955d-4c4e-a9cb-d4c65e6b426a | underdog | Aaron Rodgers | Rush Yards | over | 0.07712631679230819 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b25fcb52-8786-406a-858d-52e7672af5fc | underdog | Antonio Chadha | FG Made | over | 0.07704066761603501 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|909660e3-221a-4108-beba-6dd7a92bfc60 | underdog | Dru DeShields | Pass Yards | under | 0.07701950712652361 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|96c7816c-ba14-4c1e-8cbf-5e255475de1b | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.0768620027892164 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|103a7694-dc04-4e2f-8e0d-64af269becf7 | underdog | John Metchie III | Receiving Yards | under | 0.0768549590178017 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|349f44ca-236f-4cb1-9715-9ca2e7c59470 | underdog | Rico Dowdle | Rush Yards | under | 0.07683945378125656 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b60a1138-01f1-4292-b874-5acaf191af21 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.0767893063215298 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4172a2e0-cc73-4a02-8e18-e7b1e77ef4fa | underdog | Chig Okonkwo | Receptions | under | 0.07662959369636402 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|835bcc8b-d855-4b9f-bcde-c070fb794066 | underdog | Jalen Bonds | Rush Yards | under | 0.07662100318647524 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|93f57aed-6f22-4917-bbcd-a64859bd454f | underdog | KC Concepcion | Receptions | under | 0.07613263220312116 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|dab07cf5-55a4-424e-969c-45601f547deb | underdog | Tony Pollard | Rush + Rec Yards | under | 0.07550318088180052 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|abe8cd0c-a728-4772-b154-328bc6d32b84 | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.07548848536728658 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|4dfa0157-e1a7-41c5-98a2-53df06995587 | underdog | Brendan Baird | FG Made | under | 0.07501720483065888 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|f7da3175-c313-4994-a674-45d212b6de62 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.07440121910024278 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e6259375-13be-44ae-a842-9f3ad6880783 | underdog | Preston Bowman | Receptions | under | 0.07427454987445559 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|7fddc7b2-9d72-4ff1-b1b0-9b0333b60dbd | underdog | Gunnar Helm | Receptions | under | 0.07318955792213211 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|707d8339-a7f0-468c-a5f3-2b025bfa73d7 | underdog | Mateen Bhaghani | XP Made | over | 0.07183282096813365 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|01873d1d-8694-4f7b-9909-2b909cfb5573 | underdog | Kaelon Black | Rush Yards | under | 0.07157161024463843 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|858c7d02-f1ef-43e2-ac44-a0e9447d8e99 | underdog | Tommy Tremble | Receptions | under | 0.07126105154425799 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e213b35b-b6bc-4047-abc0-64ae1fa93373 | underdog | Kedrick Reescano | Rush Yards | over | 0.07085845022364523 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|76d03e72-77de-4f24-ba2e-b7eab08dbe1b | underdog | Tetairoa McMillan | Receiving Yards | under | 0.07080197982589909 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d3703433-0613-4609-8f73-ccbe69309032 | underdog | Dominic Zvada | FG Made | under | 0.07048776383240163 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|96b084f0-e61e-4d6f-bbda-ee645d2f7d65 | underdog | Jason Myers | Kicking Points | under | 0.07035458570297104 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|59d01cde-8219-4313-bd2e-4282a5c538fb | underdog | Drew Stevens | FG Made | under | 0.07032400194327204 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|32afa744-a7db-46b1-8166-59407c4e4dd5 | underdog | Nico Collins | Receptions | under | 0.06991731066614237 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8dc776e9-341d-424e-97a4-cb1076f15650 | underdog | Darren Waller | Receptions | under | 0.06987874258747295 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9fb692ca-1ded-474d-ace1-e954d47e3038 | underdog | Isaac TeSlaa | Receptions | under | 0.06945554268955467 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|edd8f0e4-7008-474c-8413-041ca06749b0 | underdog | Drew Sample | Receptions | over | 0.0693941433699456 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8f8128e1-4be9-470d-b74a-e8d698351827 | underdog | Denzel Boston | Receiving Yards | under | 0.06931845160473393 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0f5f2541-1db6-4c5c-8f7b-f83a3c899da1 | underdog | Theo Johnson | Receiving Yards | over | 0.06916896259016725 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|44222ca6-7319-4558-9011-4baebd4dae89 | underdog | Chris Olave | Receptions | under | 0.06860046597796887 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16834643 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.06853616926554917 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|ab5a705a-6a78-49b7-bcfd-7321ae88e69f | underdog | Kaelon Black | Receptions | under | 0.0685332352021717 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|13b657da-5328-4c06-8b7e-fb45924c9552 | underdog | Dylan Raiola | Pass Yards | under | 0.0669423266711292 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|28a6f2e6-c201-4e00-9b8a-71e36e17333b | underdog | Devon Dampier | Pass TDs | over | 0.06672449840713934 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|f8d9315a-5dca-4b15-b5b7-e7914231764e | underdog | Marcus Stokes | Pass Yards | under | 0.06616024309637814 | 2026-11-10T12:33:48Z | 2026-11-13T01:00:00Z |
| underdog|c2d4a91b-baa0-446d-9cd6-cc618c08a6b6 | underdog | Tee Higgins | Receiving Yards | under | 0.06613033755042519 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|df25d5cf-cc4b-4f9f-ade0-72454d22a32b | underdog | Katin Houser | Pass Yards | under | 0.06605989710274485 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| prizepicks|16848046 | prizepicks | Nick Poulos | Rush Atts | under | 0.06568145809905346 | 2026-11-10T12:33:48Z | 2026-11-10T20:00:00.000-05:00 |
| underdog|80fab1c6-fbfd-4c3c-83a2-195190e2daf4 | underdog | Chris Bell | Receiving Yards | under | 0.06560144467161422 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|77c3f597-0280-49a5-979d-04b569d0e16f | underdog | CeeDee Lamb | Receiving Yards | under | 0.06551409063833191 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|e811db7a-a5dd-43e4-b43c-57e8663d1217 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.06529718904725534 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| prizepicks|16834811 | prizepicks | Jalen Coker | Rec Yards | under | 0.0652772475778256 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|8a5cfa69-4d58-4a6c-869d-07765ef2ce82 | underdog | Gunnar Helm | Receiving Yards | under | 0.0650452273622022 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|95478354-d87f-4fe0-bbd3-2b078a160989 | underdog | Malik Nabers | Receiving Yards | under | 0.06465214038559375 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|d518fe9c-941a-43fb-9407-899a48add238 | underdog | Quinshon Judkins | Rush Yards | under | 0.06386753058086314 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|03043c1e-1e3f-4dfd-82ba-0f958a2d15b8 | underdog | Antonio Chadha | XP Made | over | 0.06383233498092222 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|2ef3cdfc-603a-4a90-8dd1-c78a10783d71 | underdog | Greg Dulcich | Receptions | under | 0.06371545917699406 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c489387a-fbec-48c8-ba91-c6a7f48a4d0a | underdog | Tyler Shough | Pass TDs | under | 0.06300540300276691 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|92524373-6c6c-46bc-bfb7-3ab6c5dab683 | underdog | Caleb Douglas | Receiving Yards | under | 0.06252991370499306 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4563e7d7-d71c-4679-a1ac-f8170fcba156 | underdog | Nick Poulos | Pass TDs | over | 0.06248628796258948 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| prizepicks|16828056 | prizepicks | Taylor Fritz | Total Games | over | 0.061670395845261794 | 2026-11-10T12:33:48Z | 2026-11-11T07:00:00.000-05:00 |
| underdog|12659fee-c7ce-42d1-9b1a-99636fb8605c | underdog | Ashton Daniels | Pass Yards | under | 0.06154591192626058 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|e7bed111-90fa-496f-81c0-283ae53df20b | underdog | Malik Washington | Receptions | under | 0.06146601296911136 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4704a96d-9c09-4526-aea0-fb35d6674ac1 | underdog | Jason Wright | Pass Yards | under | 0.0612870007810985 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|eab51049-4904-4da2-abf9-fb574ecb8a46 | underdog | Kevin Jennings | Pass Yards | under | 0.06123313057503299 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|2ca12ee0-e6d2-41c8-b151-acf00be8c9a3 | underdog | Noah Bennee | Receiving Yards | over | 0.0605452926650496 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|15dacbb1-1137-4ecd-813a-83e3d65404ec | underdog | Chase Brown | Receiving Yards | under | 0.06031556029363805 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|11b4b2af-a1af-4863-a1d3-2077193d67fe | underdog | Drake Maye | Pass TDs | under | 0.05982086422742261 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|24e603b1-25a1-45e2-b8f4-6b4a5ac21bb3 | underdog | Kirk Cousins | Pass TDs | over | 0.059688560959608505 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|17664d14-3314-4b7d-a0a5-cc975bb034c6 | underdog | Aveion Chenault | Receiving Yards | under | 0.059593153325432024 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|f83e44bb-cc3b-41ef-b1ad-8cb0d15c6a3c | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.05950858381511981 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|24457ce7-a29e-4e65-aaab-d2f2d38d5a63 | underdog | Mark Andrews | Receptions | over | 0.05909484948085142 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|4d0fcffd-ad43-47a6-82aa-6629600c756c | underdog | Drew Lock | Pass TDs | under | 0.058702533200966744 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|f5777302-cf71-4ed0-a67e-fe6c6156946c | underdog | C.J. Stroud | Pass TDs | over | 0.058654369818583796 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0fbff8a3-a7df-4613-aafc-fb8b686a2941 | underdog | Bijan Robinson | Rush Yards | under | 0.05846658082983813 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16832806 | prizepicks | Arthur Rinderknech | Break Points Won | under | 0.05833218159792952 | 2026-11-10T12:33:48Z | 2026-11-10T09:20:00.000-05:00 |
| underdog|3781f038-1e2d-4add-834e-b1c8ce30f9eb | underdog | Bryce Young | Pass TDs | under | 0.05761978630482656 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|fd00b38b-7865-4e20-99c8-c37b39336ee3 | underdog | Cibastian Broughton | Pass Yards | under | 0.056458836308733606 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|dc6a193c-e5a6-4f58-bc31-28677c954346 | underdog | Ty Dieffenbach | Pass Yards | under | 0.05610104740617827 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| prizepicks|16834814 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.05595171947998501 | 2026-11-10T12:33:48Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|52152886-deb7-483b-a6b2-a4f956b59162 | underdog | Jerry Jeudy | Receiving Yards | over | 0.055922448448904705 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f080a415-e7c5-4b6a-bf89-f005fdf79946 | underdog | Matt Gay | FG Made | over | 0.05586119946761431 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|214cbd24-84bb-458e-b1f4-1bd3a2149b36 | underdog | Brenton Strange | Receiving Yards | under | 0.05577611188639431 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d6e20642-ba8c-4e0a-b6c4-641e9e94c7ee | underdog | Cam Skattebo | Receptions | over | 0.055431027597783344 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|2fb6b68c-630e-4d2a-a229-4d0133bb4f00 | underdog | Creed Whittemore | Receiving Yards | over | 0.05483588486226332 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|8aa42eee-73db-4a15-8752-44ba1df5253a | underdog | Rico Dowdle | Receptions | under | 0.054539974245458644 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|9a5f7304-cd2e-4f6c-8aaf-43b9cc994501 | underdog | Greg Dulcich | Receiving Yards | under | 0.05453116028714167 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|70b36d26-19bf-47cb-8c7c-74e2bf018944 | underdog | Tyler Allgeier | Rush Yards | under | 0.05452468984304526 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|39260638-c2fa-4a7a-8cf8-5c4122745c58 | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.054455011232302786 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|09e85dc1-6ddb-434e-a936-6fd8aed43b03 | underdog | Andre Szmyt | FG Made | under | 0.05378693771750487 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|802e0e5e-871a-48df-aabb-7041fe42efb2 | underdog | Tony Pollard | Rush Yards | under | 0.053341825873326476 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16834798 | prizepicks | Drake London | Rec Yards | under | 0.05299181956525634 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|115d1147-17ab-4f53-af6d-903795d66814 | underdog | Wayshawn Parker | Receiving Yards | over | 0.052795762377819244 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|f48fdb97-2987-4a39-9762-8108b030233c | underdog | Jerry Jeudy | Receptions | over | 0.0520295111392754 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|72a879c4-8c31-41d0-8c5c-3efffd362fa4 | underdog | Bijan Robinson | Receiving Yards | under | 0.05189482215464891 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c81f7f2e-696e-4498-b8ca-7a5799d1ee5a | underdog | Matthew Stafford | Pass TDs | under | 0.05151171430881951 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|fadbfc09-db71-4ef8-826d-37562bfd53c3 | underdog | Darnell Mooney | Receptions | under | 0.05131724403966509 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|18a023c5-4ecc-4a21-8aaf-37db43e1f379 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.051123365189716385 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3ca28cbe-3045-437d-b482-074b9e547595 | underdog | Justice Hill | Receptions | under | 0.050695143750179694 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|e9fcab3a-dfe5-4a4d-909a-10526d50038e | underdog | Nick Poulos | Rush Yards | under | 0.0499842468763968 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|bea8bf51-750e-448b-9d91-4512048b9408 | underdog | Dwayne Early | Receiving Yards | over | 0.04979448157840116 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|f4a59eef-6da4-42f4-8242-bcdb0961744c | underdog | Broc Lowry | Rush Yards | under | 0.04969640814122123 | 2026-11-10T12:33:48Z | 2026-11-11T00:00:00Z |
| underdog|6b16efd1-84fa-476a-a511-2f5a08331fdc | underdog | Jaylen Warren | Receptions | under | 0.049659415578044985 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|ce556f93-4806-49a0-b6c1-b0965dd71817 | underdog | Michael Mayer | Receptions | over | 0.04962308231641188 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|0e47b5e3-2f9a-43f5-b530-f47623ccfa9d | underdog | Drew Sample | Receiving Yards | over | 0.049239250011618774 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b0cca6f8-4778-4c16-a13b-0a64187791a6 | underdog | Malachi Fields | Receptions | under | 0.049099800290027695 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| prizepicks|16834806 | prizepicks | Caleb Douglas | Rec Yards | under | 0.048911928496814694 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5783cebf-5d67-461e-97fb-7e0368bee770 | underdog | Cam Skattebo | Rush Yards | under | 0.04880324766171451 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|5c08e881-7bda-409d-81ea-cb2112afe8c4 | underdog | Kirk Cousins | Rush Yards | over | 0.04794648374314203 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|13d92abe-98b8-4b84-8bee-5b401bb6eb1b | underdog | Tony Pollard | Receptions | under | 0.047800095308580204 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|1def9b6e-8fea-42a1-9f7a-1846031c16cd | underdog | Tank Dell | Receiving Yards | under | 0.047762943478220854 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b22148b0-8c49-46d4-a7d4-880a9101cc1f | underdog | Ashton Jeanty | Rush Yards | under | 0.04744911618190628 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|39ad0a26-6667-458f-a3d3-fa4c98426b5b | underdog | Elic Ayomanor | Receiving Yards | under | 0.04737357878158632 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|64641355-2448-4bc7-961b-f5925181b3ec | underdog | Justice Hill | Rush + Rec Yards | under | 0.047312781733794496 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|492d7a4a-5e80-462d-8498-0157b894b60d | underdog | Theo Johnson | Receptions | under | 0.047168476751986876 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|62b73379-9080-4587-8208-f1ae3803bd84 | underdog | Kenneth Walker III | Rush Yards | under | 0.04707820073697511 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|fd31bc9e-cff4-44fb-ae49-6c536d56bce8 | underdog | Caleb Douglas | Receptions | under | 0.046873180612608145 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|e89f34aa-73c0-431e-b973-bc4330abf251 | underdog | Matt Gay | Kicking Points | over | 0.04669837646233033 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|f388882e-bf96-4bf0-ab4f-c20217916353 | underdog | Harold Fannin | Receptions | under | 0.046638245325585026 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|cca77000-2c1e-4dac-a5a5-e50bd3bf309d | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.046614779588552424 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|0954ce59-bee3-4a2d-bc77-5496d047c7b0 | underdog | Devin Singletary | Receptions | over | 0.04661474918471048 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|49dbe735-a6e1-435e-b05b-067376ee32f9 | underdog | Joey Slye | FG Made | under | 0.04617041472475325 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7734a52a-2a17-4fb7-881d-7d4ea165fae5 | underdog | Malik Washington | Receiving Yards | under | 0.04523547877059608 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|56e8eb86-0cbf-469f-8c79-3ef93f017dea | underdog | Denzel Boston | Receptions | under | 0.045152048025238756 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ae810589-81e6-4ea2-8235-0aef0fd1070e | underdog | Joey Slye | Kicking Points | under | 0.04505178064548698 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f0780ba2-8037-4cc2-a253-38e5dd6c1369 | underdog | Brendan Baird | XP Made | under | 0.04490246123339292 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|c12bbd3e-b4d8-4c62-b3db-85a679a9dfd7 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.04388335638391305 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b36f306c-d699-4184-8d28-66eb945fc1c2 | underdog | Elijah Higgins | Receiving Yards | under | 0.043442453369481826 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|05c252a1-ceab-4428-b6ec-304ee5261111 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.04327316157917138 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|22308371-b125-45e9-ab0d-d1b06ac85f23 | underdog | Kenneth Walker III | Receptions | under | 0.04263884385867134 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0d111317-5c99-4d56-b5f5-63bae031a649 | underdog | Deshaun Watson | Pass TDs | under | 0.04236385864477632 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|aac8322b-1ee8-46b4-92bf-a2afefe76f97 | underdog | Braden Pegan | Receiving Yards | under | 0.04226457688012075 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| prizepicks|16813617 | prizepicks | Bianca Andreescu | Total Games | over | 0.042047604343236844 | 2026-11-10T12:33:48Z | 2026-11-10T11:10:00.000-05:00 |
| underdog|55cb13c1-ee46-47e8-b0ce-5d68bc2910db | underdog | Connor Calvert | XP Made | over | 0.04166023250717721 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|2fa9e2b4-614d-4a17-9548-927d0f196189 | underdog | Derrick Henry | Receptions | under | 0.04138130744755619 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|992f3e80-6aa2-4ce0-bca9-9bd0cba69874 | underdog | Ashton Jeanty | Receptions | under | 0.041325909181133325 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c7d45fea-cf6a-4f77-aacf-3738a3162be0 | underdog | Riley Neer | Receiving Yards | under | 0.04118029525278821 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|49589898-ea13-496a-b58a-9a31bbc7cc6f | underdog | Matthew Golden | Receiving Yards | under | 0.04047737010655683 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d9cb7740-be27-4110-adb7-2c077ed34168 | underdog | Tre Tucker | Receptions | under | 0.04026187438627249 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16834495 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.039638724520605906 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|fe43e213-a4b5-42f2-9818-fe49eb5d3c33 | underdog | Jayden Daniels | Rush Yards | under | 0.03911272505860208 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|03361ce4-9586-4b1b-b660-d9a3da6d9a64 | underdog | Ethan Moczulski | XP Made | over | 0.03851062357902946 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|f736741c-7a0b-4bf8-9588-9565710baa42 | underdog | Dohnte Meyers | Receiving Yards | over | 0.038228133462906655 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|eeef5a4d-5185-4455-bbe8-393806c31d88 | underdog | C.J. Stroud | Rush Yards | over | 0.03821390228661814 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|9dd7c202-7b28-46bd-a054-da7dca89c2e5 | underdog | Isaiah Likely | Receptions | under | 0.03790936636152842 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|3f99a390-60d8-403b-a07e-cc93271c2871 | underdog | Rodney Nelson | Rush Yards | under | 0.037374132405903815 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|664077dc-05f4-4c14-9ba5-2de3864deb2c | underdog | Noah Fifita | Pass TDs | over | 0.037265444619400845 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|3a85fd75-3402-4e36-b75b-df3a8066ffda | underdog | Linda Noskova | Double Faults | under | 0.037236525846527924 | 2026-11-10T12:33:48Z | 2026-11-10T21:10:00Z |
| underdog|a98832ad-cc1c-4f28-9746-8d27fb8ec062 | underdog | Joe Burrow | Rush Yards | over | 0.03676432878965474 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|fe6e002d-b0bd-449a-9de8-611518ffd1b8 | underdog | Jadarian Price | Receiving Yards | over | 0.036609848197770134 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d5e53e5c-71f4-4086-99fb-69639e63e727 | underdog | Mateen Bhaghani | FG Made | over | 0.036598637318603355 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| prizepicks|16834796 | prizepicks | Travis Kelce | Rec Yards | under | 0.036326662949040744 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|79b74bf8-8298-4a06-afde-b7f1aaa8527a | underdog | Preston Bowman | Receiving Yards | under | 0.034739845267144354 | 2026-11-10T12:33:48Z | 2026-11-11T01:00:00Z |
| underdog|708ac890-b113-4281-a808-ffdbd879ef98 | underdog | Devon Dampier | Rush Yards | under | 0.034208087223052575 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|eda6defe-1ce6-482b-97c1-2f177b9337e9 | underdog | Cam Skattebo | Receiving Yards | over | 0.03385701304435074 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|1ceddca8-fe53-49f8-831a-62aa046bb636 | underdog | Wan'Dale Robinson | Receptions | under | 0.033293997712305456 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3d149e96-995b-46cd-a4f5-dc95cc6fc858 | underdog | Keldric Luster | Pass TDs | over | 0.03306737903585255 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|3dee59b6-4c83-4c54-8c2b-c498c966c5c4 | underdog | Zay Flowers | Receiving Yards | under | 0.03260350614698304 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|1b8e57f8-ea6f-4a94-880a-1b5f248aea9a | underdog | Malik Willis | Rush Yards | under | 0.03247839348753989 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|6497b72f-8917-4fb8-bf75-fee9b6802c4b | underdog | Mitchell Evans | Receptions | over | 0.032392458273830194 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|cdb95f79-a311-4b4f-bbef-491c98030f92 | underdog | Christian Watson | Receiving Yards | under | 0.03194088212723312 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|62a65f18-6469-4562-b357-1d489f303f2b | underdog | Keldric Luster | Rush Yards | under | 0.03177769874809522 | 2026-11-10T12:33:48Z | 2026-11-12T00:30:00Z |
| underdog|cc08f6ce-0930-4018-ab18-d4db61efc735 | underdog | Tre Tucker | Receiving Yards | under | 0.03139018544053451 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|2141e4e3-e6bd-419a-b8b6-ce264d9e74f3 | underdog | Charlie Becker | Receiving Yards | under | 0.03107999426582564 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| prizepicks|16834647 | prizepicks | Javonte Williams | Rush Yards | under | 0.030973438538770326 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|d6413fdc-080d-4ab7-be3c-31523f75b68b | underdog | Tyler Shough | Rush Yards | under | 0.030722620517749544 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d5c830e4-4c77-41ac-ae2d-f33dfe9339f1 | underdog | Mark Andrews | Receiving Yards | under | 0.030621074448929253 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|a7c56265-9690-4bae-ac17-c397a8ce4cf5 | underdog | Samaje Perine | Rush + Rec Yards | under | 0.03045247225247416 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b357c9e8-27ef-4f86-9497-cac10d884f8c | underdog | Sam LaPorta | Receptions | under | 0.030234889226053996 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
