# Politics Pipeline Digest -- 2026-09-26T17:23:45Z

## Run summary
- Race-market ingestion: 434 races (74 on both venues, 94 Kalshi series matched)
- Polling ingestion: 5655 rows (435 House, 5220 state legislature)
- Estimation: 868 (race, party) rows written (from 434 races read)
- CLV logging: 0 newly flagged, 0 newly closed, 425 still open (425 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py politics size`, Session 5.4) -- this table is what to scan to pick a race/party worth sizing. `hours_to_resolution` matters here more than for the other two tracks: politics positions can sit open for weeks or months (Session 5.4's lockup dampener).

| flag_id | race_id | candidate_name | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | hours_to_resolution | first_flagged_at |
|---|---|---|---|---|---|---|---|---|
| polymarket|US-HOUSE-PA-10|DEM | US-HOUSE-PA-10 | Janelle Stelson | dem | 0.8648 | 0.775 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-08|DEM | US-HOUSE-CO-08 | Manny Rutinel | dem | 0.8698 | 0.78 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-05|DEM | US-HOUSE-MO-05 | Will the Democratic Party win the MO-05 House seat? | dem | 0.8648 | 0.775 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-05|REP | US-HOUSE-WA-05 | Will the Republican Party win the WA-05 House seat? | rep | 0.8648 | 0.775 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-07|DEM | US-HOUSE-OH-07 | Will the Democratic Party win the OH-07 House seat? | dem | 0.8598 | 0.77 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-32|REP | US-HOUSE-TX-32 | Jace Yarbrough | rep | 0.8698 | 0.78 | 0.0898 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IA-01|DEM | US-HOUSE-IA-01 | Christina Bohannan | dem | 0.8747 | 0.785 | 0.0897 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-07|DEM | US-HOUSE-PA-07 | Bob Brooks | dem | 0.8747 | 0.785 | 0.0897 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CO-08|DEM | US-HOUSE-CO-08 | Manny Rutinel | dem | 0.8747 | 0.785 | 0.0897 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-TX-28|DEM | US-HOUSE-TX-28 | Henry Cuellar | dem | 0.8546 | 0.765 | 0.0896 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IA-03|DEM | US-HOUSE-IA-03 | Sarah Trone Garriott | dem | 0.8546 | 0.765 | 0.0896 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-15|REP | US-HOUSE-OH-15 | Will the Republican Party win the OH-15 House seat? | rep | 0.8494 | 0.76 | 0.0894 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-PA-10|DEM | US-HOUSE-PA-10 | Janelle Stelson | dem | 0.8494 | 0.76 | 0.0894 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-PA-07|DEM | US-HOUSE-PA-07 | Bob Brooks | dem | 0.8843 | 0.795 | 0.0893 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-09|REP | US-HOUSE-NC-09 | Will the Republican Party win the NC-09 House seat? | rep | 0.8843 | 0.795 | 0.0893 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-IA-03|DEM | US-HOUSE-IA-03 | Sarah Trone Garriott | dem | 0.8441 | 0.755 | 0.0891 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-VA-02|DEM | US-HOUSE-VA-02 | Elaine Luria | dem | 0.889 | 0.8 | 0.089 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-AZ-01|DEM | US-HOUSE-AZ-01 | Amish Shah | dem | 0.8387 | 0.75 | 0.0887 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|STATE-LEG-MO-SENATE-8|REP | STATE-LEG-MO-SENATE-8 | Jon Patterson | rep | 0.8387 | 0.75 | 0.0887 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NV-02|REP | US-HOUSE-NV-02 | Will the Republican Party win the NV-02 House seat? | rep | 0.8333 | 0.745 | 0.0883 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-34|DEM | US-HOUSE-TX-34 | Vicente Gonzalez | dem | 0.8333 | 0.745 | 0.0883 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-TX-34|DEM | US-HOUSE-TX-34 | Vicente Gonzalez | dem | 0.8333 | 0.745 | 0.0883 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-02|DEM | US-HOUSE-VA-02 | Elaine Luria | dem | 0.9025 | 0.815 | 0.0875 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-AZ-06|DEM | US-HOUSE-AZ-06 | JoAnna Mendoza | dem | 0.9025 | 0.815 | 0.0875 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-02|REP | US-HOUSE-NJ-02 | Will the Republican Party win the NJ-02 House seat? | rep | 0.9025 | 0.815 | 0.0875 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-07|DEM | US-HOUSE-NJ-07 | Rebecca Bennett | dem | 0.9025 | 0.815 | 0.0875 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-11|REP | US-HOUSE-FL-11 | Will the Republican Party win the FL-11 House seat? | rep | 0.9111 | 0.825 | 0.0861 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-28|DEM | US-HOUSE-TX-28 | Henry Cuellar | dem | 0.9111 | 0.825 | 0.0861 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-06|DEM | US-HOUSE-AZ-06 | JoAnna Mendoza | dem | 0.9111 | 0.825 | 0.0861 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-08|REP | US-HOUSE-AZ-08 | Will the Republican Party win the AZ-08 House seat? | rep | 0.9111 | 0.825 | 0.0861 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-01|REP | US-HOUSE-NY-01 | Will the Republican Party win the NY-01 House seat? | rep | 0.8107 | 0.725 | 0.0857 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-10|REP | US-HOUSE-OH-10 | Will the Republican Party win the OH-10 House seat? | rep | 0.9153 | 0.83 | 0.0853 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NE-01|REP | US-HOUSE-NE-01 | Will the Republican Party win the NE-01 House seat? | rep | 0.9153 | 0.83 | 0.0853 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-13|REP | US-HOUSE-FL-13 | Anna Paulina Luna | rep | 0.8049 | 0.72 | 0.0849 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-06|REP | US-HOUSE-KY-06 | Will the Republican Party win the KY-06 House seat? | rep | 0.8049 | 0.72 | 0.0849 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-27|REP | US-HOUSE-FL-27 | Will the Republican Party win the FL-27 House seat? | rep | 0.9193 | 0.835 | 0.0843 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-14|REP | US-HOUSE-NC-14 | Will the Republican Party win the NC-14 House seat? | rep | 0.9193 | 0.835 | 0.0843 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-13|REP | US-HOUSE-NC-13 | Will the Republican Party win the NC-13 House seat? | rep | 0.9193 | 0.835 | 0.0843 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-05|REP | US-HOUSE-IN-05 | Will the Republican Party win the IN-05 House seat? | rep | 0.9193 | 0.835 | 0.0843 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-AZ-02|REP | US-HOUSE-AZ-02 | Eli Crane | rep | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-01|REP | US-HOUSE-MN-01 | Will the Republican Party win the MN-01 House seat? | rep | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-FL-13|REP | US-HOUSE-FL-13 | Anna Paulina Luna | rep | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-01|DEM | US-HOUSE-AZ-01 | Amish Shah | dem | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-WI-03|DEM | US-HOUSE-WI-03 | Rebecca Cooke | dem | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NJ-07|DEM | US-HOUSE-NJ-07 | Rebecca Bennett | dem | 0.799 | 0.715 | 0.084 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-07|REP | US-HOUSE-NC-07 | Will the Republican Party win the NC-07 House seat? | rep | 0.9233 | 0.84 | 0.0833 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|STATE-LEG-MO-SENATE-30|DEM | STATE-LEG-MO-SENATE-30 | Betsy Fogle | dem | 0.9233 | 0.84 | 0.0833 | 1206.9 | 2026-09-13T17:04:34Z |
| kalshi|STATE-LEG-CA-SENATE-26|DEM | STATE-LEG-CA-SENATE-26 | Sara Hernandez | dem | 0.9233 | 0.84 | 0.0833 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-16|REP | US-HOUSE-FL-16 | Will the Republican Party win the FL-16 House seat? | rep | 0.9233 | 0.84 | 0.0833 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-21|REP | US-HOUSE-NY-21 | Will the Republican Party win the NY-21 House seat? | rep | 0.7931 | 0.71 | 0.0831 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-05|REP | US-HOUSE-VA-05 | Will the Republican Party win the VA-05 House seat? | rep | 0.9272 | 0.845 | 0.0822 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WI-03|DEM | US-HOUSE-WI-03 | Rebecca Cooke | dem | 0.7871 | 0.705 | 0.0821 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-01|REP | US-HOUSE-SC-01 | Will the Republican Party win the SC-01 House seat? | rep | 0.7871 | 0.705 | 0.0821 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-23|REP | US-HOUSE-TX-23 | Will the Republican Party win the TX-23 House seat? | rep | 0.781 | 0.7 | 0.081 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-IA-01|DEM | US-HOUSE-IA-01 | Christina Bohannan | dem | 0.781 | 0.7 | 0.081 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-05|REP | US-HOUSE-CO-05 | Will the Republican Party win the CO-05 House seat? | rep | 0.7749 | 0.695 | 0.0799 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-03|REP | US-HOUSE-NC-03 | Will the Republican Party win the NC-03 House seat? | rep | 0.9348 | 0.855 | 0.0798 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-08|REP | US-HOUSE-MN-08 | Will the Republican Party win the MN-08 House seat? | rep | 0.9348 | 0.855 | 0.0798 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-01|REP | US-HOUSE-GA-01 | Will the Republican Party win the GA-01 House seat? | rep | 0.9348 | 0.855 | 0.0798 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-01|DEM | US-HOUSE-OH-01 | Greg Landsman | dem | 0.9366 | 0.8575 | 0.0791 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WI-01|REP | US-HOUSE-WI-01 | Bryan Steil | rep | 0.7687 | 0.69 | 0.0787 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-WI-01|REP | US-HOUSE-WI-01 | Bryan Steil | rep | 0.7687 | 0.69 | 0.0787 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-02|REP | US-HOUSE-AL-02 | Will the Republican Party win the AL-02 House seat? | rep | 0.7687 | 0.69 | 0.0787 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-TX-09|REP | US-HOUSE-TX-09 | Alex Mealer | rep | 0.9384 | 0.86 | 0.0784 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-09|REP | US-HOUSE-TX-09 | Alex Mealer | rep | 0.942 | 0.865 | 0.077 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-24|REP | US-HOUSE-TX-24 | Will the Republican Party win the TX-24 House seat? | rep | 0.942 | 0.865 | 0.077 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-03|DEM | US-HOUSE-WA-03 | Marie Gluesenkamp Perez | dem | 0.942 | 0.865 | 0.077 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-02|REP | US-HOUSE-NY-02 | Will the Republican Party win the NY-02 House seat? | rep | 0.942 | 0.865 | 0.077 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-TX-32|REP | US-HOUSE-TX-32 | Jace Yarbrough | rep | 0.9423 | 0.8655 | 0.0768 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AR-02|REP | US-HOUSE-AR-02 | Will the Republican Party win the AR-02 House seat? | rep | 0.9455 | 0.87 | 0.0755 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-05|REP | US-HOUSE-NC-05 | Will the Republican Party win the NC-05 House seat? | rep | 0.9455 | 0.87 | 0.0755 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-25|DEM | US-HOUSE-FL-25 | Will the Democratic Party win the FL-25 House seat? | dem | 0.7497 | 0.675 | 0.0747 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-02|REP | US-HOUSE-AZ-02 | Eli Crane | rep | 0.7497 | 0.675 | 0.0747 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-07|REP | US-HOUSE-FL-07 | Will the Republican Party win the FL-07 House seat? | rep | 0.7497 | 0.675 | 0.0747 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-22|DEM | US-HOUSE-CA-22 | Randy Villegas | dem | 0.9488 | 0.875 | 0.0738 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-04|DEM | US-HOUSE-NY-04 | Laura Gillen | dem | 0.9488 | 0.875 | 0.0738 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OK-05|REP | US-HOUSE-OK-05 | Will the Republican Party win the OK-05 House seat? | rep | 0.9488 | 0.875 | 0.0738 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-22|DEM | US-HOUSE-CA-22 | Randy Villegas | dem | 0.9488 | 0.875 | 0.0738 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-08|REP | US-HOUSE-OH-08 | Will the Republican Party win the OH-08 House seat? | rep | 0.9488 | 0.875 | 0.0738 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-WA-03|DEM | US-HOUSE-WA-03 | Marie Gluesenkamp Perez | dem | 0.9502 | 0.877 | 0.0732 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-05|REP | US-HOUSE-TN-05 | Will the Republican Party win the TN-05 House seat? | rep | 0.9521 | 0.88 | 0.0721 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-11|DEM | US-HOUSE-NC-11 | Jamie Ager | dem | 0.7367 | 0.665 | 0.0717 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-OH-01|DEM | US-HOUSE-OH-01 | Greg Landsman | dem | 0.955 | 0.8845 | 0.0705 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-02|REP | US-HOUSE-SC-02 | Will the Republican Party win the SC-02 House seat? | rep | 0.9553 | 0.885 | 0.0703 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NM-02|DEM | US-HOUSE-NM-02 | Gabe Vasquez | dem | 0.9553 | 0.885 | 0.0703 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-48|DEM | US-HOUSE-CA-48 | Will the Democratic Party win the CA-48 House seat? | dem | 0.9553 | 0.885 | 0.0703 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-10|REP | US-HOUSE-TX-10 | Will the Republican Party win the TX-10 House seat? | rep | 0.9553 | 0.885 | 0.0703 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|STATE-LEG-MO-SENATE-30|REP | STATE-LEG-MO-SENATE-30 | Melanie Stinnett | rep | 0.7302 | 0.66 | 0.0702 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-02|REP | US-HOUSE-MO-02 | Will the Republican Party win the MO-02 House seat? | rep | 0.7302 | 0.66 | 0.0702 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NH-01|DEM | US-HOUSE-NH-01 | Will the Democratic Party win the NH-01 House seat? | dem | 0.9572 | 0.888 | 0.0692 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NM-02|DEM | US-HOUSE-NM-02 | Gabe Vasquez | dem | 0.9581 | 0.8895 | 0.0686 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-PA-08|DEM | US-HOUSE-PA-08 | Paige Cognetti | dem | 0.7235 | 0.655 | 0.0685 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NE-02|DEM | US-HOUSE-NE-02 | Denise Powell | dem | 0.9584 | 0.89 | 0.0684 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-04|REP | US-HOUSE-FL-04 | Will the Republican Party win the FL-04 House seat? | rep | 0.9584 | 0.89 | 0.0684 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CO-03|REP | US-HOUSE-CO-03 | Jeff Hurd | rep | 0.7169 | 0.65 | 0.0669 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-26|REP | US-HOUSE-FL-26 | Will the Republican Party win the FL-26 House seat? | rep | 0.9614 | 0.895 | 0.0664 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NV-04|DEM | US-HOUSE-NV-04 | Steven Horsford | dem | 0.9614 | 0.895 | 0.0664 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-07|REP | US-HOUSE-TN-07 | Will the Republican Party win the TN-07 House seat? | rep | 0.9614 | 0.895 | 0.0664 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-45|DEM | US-HOUSE-CA-45 | Derek Tran | dem | 0.9614 | 0.895 | 0.0664 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-MI-10|DEM | US-HOUSE-MI-10 | Christina Hines | dem | 0.7102 | 0.645 | 0.0652 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-09|REP | US-HOUSE-FL-09 | Will the Republican Party win the FL-09 House seat? | rep | 0.7102 | 0.645 | 0.0652 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-03|REP | US-HOUSE-CO-03 | Jeff Hurd | rep | 0.7102 | 0.645 | 0.0652 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-17|DEM | US-HOUSE-NY-17 | Cait Conley | dem | 0.7102 | 0.645 | 0.0652 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-09|DEM | US-HOUSE-OH-09 | Marcy Kaptur | dem | 0.7102 | 0.645 | 0.0652 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-04|DEM | US-HOUSE-NY-04 | Laura Gillen | dem | 0.9643 | 0.9 | 0.0643 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NV-01|DEM | US-HOUSE-NV-01 | Dina Titus | dem | 0.9643 | 0.9 | 0.0643 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-MT-01|REP | US-HOUSE-MT-01 | Aaron Flint | rep | 0.7034 | 0.64 | 0.0634 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OK-01|REP | US-HOUSE-OK-01 | Will the Republican Party win the OK-01 House seat? | rep | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-03|REP | US-HOUSE-MO-03 | Will the Republican Party win the MO-03 House seat? | rep | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-PA-17|DEM | US-HOUSE-PA-17 | Chris Deluzio | dem | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-02|REP | US-HOUSE-FL-02 | Will the Republican Party win the FL-02 House seat? | rep | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-03|DEM | US-HOUSE-NY-03 | Tom Suozzi | dem | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-12|REP | US-HOUSE-GA-12 | Will the Republican Party win the GA-12 House seat? | rep | 0.9672 | 0.905 | 0.0622 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NE-02|DEM | US-HOUSE-NE-02 | Denise Powell | dem | 0.9677 | 0.906 | 0.0617 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-10|DEM | US-HOUSE-MI-10 | Christina Hines | dem | 0.6966 | 0.635 | 0.0616 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-08|DEM | US-HOUSE-PA-08 | Paige Cognetti | dem | 0.6966 | 0.635 | 0.0616 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NV-01|DEM | US-HOUSE-NV-01 | Dina Titus | dem | 0.9699 | 0.91 | 0.0599 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-06|REP | US-HOUSE-MN-06 | Will the Republican Party win the MN-06 House seat? | rep | 0.9699 | 0.91 | 0.0599 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-16|REP | US-HOUSE-PA-16 | Will the Republican Party win the PA-16 House seat? | rep | 0.9699 | 0.91 | 0.0599 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-04|REP | US-HOUSE-CO-04 | Will the Republican Party win the CO-04 House seat? | rep | 0.6897 | 0.63 | 0.0597 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NC-11|DEM | US-HOUSE-NC-11 | Jamie Ager | dem | 0.6897 | 0.63 | 0.0597 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-09|DEM | US-HOUSE-NJ-09 | Nellie Pou | dem | 0.9709 | 0.912 | 0.0589 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-23|REP | US-HOUSE-NY-23 | Will the Republican Party win the NY-23 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-05|REP | US-HOUSE-AZ-05 | Will the Republican Party win the AZ-05 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-27|REP | US-HOUSE-TX-27 | Will the Republican Party win the TX-27 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NV-03|DEM | US-HOUSE-NV-03 | Susie Lee | dem | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-06|REP | US-HOUSE-NC-06 | Will the Republican Party win the NC-06 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-09|REP | US-HOUSE-TN-09 | Will the Republican Party win the TN-09 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-25|REP | US-HOUSE-TX-25 | Will the Republican Party win the TX-25 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-05|REP | US-HOUSE-SC-05 | Will the Republican Party win the SC-05 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-08|REP | US-HOUSE-NC-08 | Will the Republican Party win the NC-08 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WI-06|REP | US-HOUSE-WI-06 | Will the Republican Party win the WI-06 House seat? | rep | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-45|DEM | US-HOUSE-CA-45 | Derek Tran | dem | 0.9725 | 0.915 | 0.0575 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-13|DEM | US-HOUSE-CA-13 | Adam Gray | dem | 0.9738 | 0.9175 | 0.0563 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-OH-09|DEM | US-HOUSE-OH-09 | Marcy Kaptur | dem | 0.6758 | 0.62 | 0.0558 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MT-01|REP | US-HOUSE-MT-01 | Aaron Flint | rep | 0.6758 | 0.62 | 0.0558 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-26|REP | US-HOUSE-TX-26 | Will the Republican Party win the TX-26 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-04|REP | US-HOUSE-WA-04 | Will the Republican Party win the WA-04 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-21|DEM | US-HOUSE-CA-21 | Jim Costa | dem | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WI-08|REP | US-HOUSE-WI-08 | Will the Republican Party win the WI-08 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-07|REP | US-HOUSE-GA-07 | Will the Republican Party win the GA-07 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-05|REP | US-HOUSE-TX-05 | Will the Republican Party win the TX-05 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-18|REP | US-HOUSE-FL-18 | Will the Republican Party win the FL-18 House seat? | rep | 0.975 | 0.92 | 0.055 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-01|DEM | US-HOUSE-NC-01 | Don Davis | dem | 0.6688 | 0.615 | 0.0538 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-27|DEM | US-HOUSE-CA-27 | George Whitesides | dem | 0.9763 | 0.9225 | 0.0538 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-15|REP | US-HOUSE-FL-15 | Will the Republican Party win the FL-15 House seat? | rep | 0.977 | 0.924 | 0.053 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-VA-10|DEM | US-HOUSE-VA-10 | Suhas Subramanyam | dem | 0.9772 | 0.9245 | 0.0527 | 1063.2 | 2026-09-19T16:49:26Z |
| kalshi|US-HOUSE-MN-02|DEM | US-HOUSE-MN-02 | Matt Little | dem | 0.9772 | 0.9245 | 0.0527 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-36|REP | US-HOUSE-TX-36 | Will the Republican Party win the TX-36 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-01|REP | US-HOUSE-MI-01 | Will the Republican Party win the MI-01 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-06|REP | US-HOUSE-VA-06 | Will the Republican Party win the VA-06 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-08|DEM | US-HOUSE-MI-08 | Kristen McDonald Rivet | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-02|DEM | US-HOUSE-MN-02 | Matt Little | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-22|REP | US-HOUSE-TX-22 | Will the Republican Party win the TX-22 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-38|REP | US-HOUSE-TX-38 | Will the Republican Party win the TX-38 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-03|DEM | US-HOUSE-NY-03 | Tom Suozzi | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-03|REP | US-HOUSE-TX-03 | Will the Republican Party win the TX-03 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-04|REP | US-HOUSE-SC-04 | Will the Republican Party win the SC-04 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-04|REP | US-HOUSE-TN-04 | Will the Republican Party win the TN-04 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-08|REP | US-HOUSE-TN-08 | Will the Republican Party win the TN-08 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-04|REP | US-HOUSE-MO-04 | Will the Republican Party win the MO-04 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-02|DEM | US-HOUSE-GA-02 | Will the Democratic Party win the GA-02 House seat? | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-02|REP | US-HOUSE-TX-02 | Will the Republican Party win the TX-02 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-05|REP | US-HOUSE-FL-05 | Will the Republican Party win the FL-05 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-12|REP | US-HOUSE-FL-12 | Will the Republican Party win the FL-12 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-21|DEM | US-HOUSE-CA-21 | Jim Costa | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-17|REP | US-HOUSE-FL-17 | Will the Republican Party win the FL-17 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-22|DEM | US-HOUSE-NY-22 | John Mannion | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-08|REP | US-HOUSE-FL-08 | Will the Republican Party win the FL-08 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-24|REP | US-HOUSE-NY-24 | Will the Republican Party win the NY-24 House seat? | rep | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OR-05|DEM | US-HOUSE-OR-05 | Janelle Bynum | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NM-03|DEM | US-HOUSE-NM-03 | Will the Democratic Party win the NM-03 House seat? | dem | 0.9775 | 0.925 | 0.0525 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NV-04|DEM | US-HOUSE-NV-04 | Steven Horsford | dem | 0.9777 | 0.9255 | 0.0522 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NH-02|DEM | US-HOUSE-NH-02 | Will the Democratic Party win the NH-02 House seat? | dem | 0.9787 | 0.9275 | 0.0512 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-IL-17|DEM | US-HOUSE-IL-17 | Eric Sorensen | dem | 0.9791 | 0.9285 | 0.0506 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-VA-07|DEM | US-HOUSE-VA-07 | Eugene Vindman | dem | 0.9793 | 0.929 | 0.0503 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-13|DEM | US-HOUSE-OH-13 | Emilia Sykes | dem | 0.9796 | 0.9295 | 0.0501 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-23|DEM | US-HOUSE-FL-23 | Lois Frankel | dem | 0.9798 | 0.93 | 0.0498 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-21|REP | US-HOUSE-FL-21 | Will the Republican Party win the FL-21 House seat? | rep | 0.9798 | 0.93 | 0.0498 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-19|DEM | US-HOUSE-NY-19 | Josh Riley | dem | 0.9798 | 0.93 | 0.0498 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-07|DEM | US-HOUSE-VA-07 | Eugene Vindman | dem | 0.9798 | 0.93 | 0.0498 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-31|REP | US-HOUSE-TX-31 | Will the Republican Party win the TX-31 House seat? | rep | 0.9798 | 0.93 | 0.0498 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-14|DEM | US-HOUSE-FL-14 | Will the Democratic Party win the FL-14 House seat? | dem | 0.6547 | 0.605 | 0.0497 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NJ-09|DEM | US-HOUSE-NJ-09 | Nellie Pou | dem | 0.98 | 0.9305 | 0.0495 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-23|REP | US-HOUSE-CA-23 | Will the Republican Party win the CA-23 House seat? | rep | 0.9805 | 0.9315 | 0.049 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NH-01|DEM | US-HOUSE-NH-01 | Stefany Shaheen | dem | 0.9807 | 0.932 | 0.0487 | 1254.8 | 2026-09-11T17:12:06Z |
| polymarket|US-HOUSE-NY-18|DEM | US-HOUSE-NY-18 | Pat Ryan | dem | 0.9809 | 0.9325 | 0.0484 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-OR-05|DEM | US-HOUSE-OR-05 | Janelle Bynum | dem | 0.9809 | 0.9325 | 0.0484 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-18|DEM | US-HOUSE-NY-18 | Pat Ryan | dem | 0.9816 | 0.934 | 0.0476 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-11|REP | US-HOUSE-NY-11 | Will the Republican Party win the NY-11 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-12|REP | US-HOUSE-TX-12 | Will the Republican Party win the TX-12 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-17|REP | US-HOUSE-TX-17 | Will the Republican Party win the TX-17 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-02|DEM | US-HOUSE-CA-02 | Will the Democratic Party win the CA-02 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-29|DEM | US-HOUSE-TX-29 | Will the Democratic Party win the TX-29 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-20|DEM | US-HOUSE-TX-20 | Will the Democratic Party win the TX-20 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-21|REP | US-HOUSE-TX-21 | Will the Republican Party win the TX-21 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OR-04|DEM | US-HOUSE-OR-04 | Will the Democratic Party win the OR-04 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AR-04|REP | US-HOUSE-AR-04 | Will the Republican Party win the AR-04 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|STATE-LEG-MD-SENATE-2|REP | STATE-LEG-MD-SENATE-2 | Paul Corderman | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-UT-03|REP | US-HOUSE-UT-03 | Celeste Maloy | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-07|DEM | US-HOUSE-CO-07 | Will the Democratic Party win the CO-07 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-05|REP | US-HOUSE-OH-05 | Will the Republican Party win the OH-05 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-02|REP | US-HOUSE-OH-02 | Will the Republican Party win the OH-02 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NM-01|DEM | US-HOUSE-NM-01 | Will the Democratic Party win the NM-01 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-03|REP | US-HOUSE-FL-03 | Will the Republican Party win the FL-03 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-11|REP | US-HOUSE-TX-11 | Will the Republican Party win the TX-11 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KS-04|REP | US-HOUSE-KS-04 | Will the Republican Party win the KS-04 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-08|REP | US-HOUSE-GA-08 | Will the Republican Party win the GA-08 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IA-04|REP | US-HOUSE-IA-04 | Will the Republican Party win the IA-04 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MS-02|DEM | US-HOUSE-MS-02 | Will the Democratic Party win the MS-02 House seat? | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-28|REP | US-HOUSE-FL-28 | Will the Republican Party win the FL-28 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-01|REP | US-HOUSE-MD-01 | Will the Republican Party win the MD-01 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-06|REP | US-HOUSE-TX-06 | Will the Republican Party win the TX-06 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-04|REP | US-HOUSE-IN-04 | Will the Republican Party win the IN-04 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-01|DEM | US-HOUSE-IN-01 | Frank Mrvan | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-16|REP | US-HOUSE-IL-16 | Will the Republican Party win the IL-16 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-17|DEM | US-HOUSE-IL-17 | Eric Sorensen | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-04|REP | US-HOUSE-KY-04 | Will the Republican Party win the KY-04 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-14|REP | US-HOUSE-OH-14 | Will the Republican Party win the OH-14 House seat? | rep | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-03|DEM | US-HOUSE-MI-03 | Hillary Scholten | dem | 0.982 | 0.935 | 0.047 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-MI-08|DEM | US-HOUSE-MI-08 | Kristen McDonald Rivet | dem | 0.9823 | 0.9355 | 0.0468 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-OH-13|DEM | US-HOUSE-OH-13 | Emilia Sykes | dem | 0.9827 | 0.9365 | 0.0462 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-13|DEM | US-HOUSE-CA-13 | Adam Gray | dem | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-07|DEM | US-HOUSE-TX-07 | Will the Democratic Party win the TX-07 House seat? | dem | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-06|REP | US-HOUSE-AL-06 | Will the Republican Party win the AL-06 House seat? | rep | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OK-04|REP | US-HOUSE-OK-04 | Will the Republican Party win the OK-04 House seat? | rep | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-17|DEM | US-HOUSE-PA-17 | Chris Deluzio | dem | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-LA-06|REP | US-HOUSE-LA-06 | Will the Republican Party win the LA-06 House seat? | rep | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KS-01|REP | US-HOUSE-KS-01 | Will the Republican Party win the KS-01 House seat? | rep | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-09|DEM | US-HOUSE-CA-09 | Josh Harder | dem | 0.9842 | 0.94 | 0.0442 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-FL-23|DEM | US-HOUSE-FL-23 | Lois Frankel | dem | 0.9846 | 0.941 | 0.0436 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-09|DEM | US-HOUSE-CA-09 | Josh Harder | dem | 0.9846 | 0.941 | 0.0436 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NC-01|DEM | US-HOUSE-NC-01 | Don Davis | dem | 0.6333 | 0.59 | 0.0433 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NV-03|DEM | US-HOUSE-NV-03 | Susie Lee | dem | 0.9848 | 0.9415 | 0.0433 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-47|DEM | US-HOUSE-CA-47 | Dave Min | dem | 0.9848 | 0.9415 | 0.0433 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-MI-03|DEM | US-HOUSE-MI-03 | Hillary Scholten | dem | 0.985 | 0.942 | 0.043 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-03|DEM | US-HOUSE-CA-03 | Ami Bera | dem | 0.9856 | 0.9435 | 0.0421 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-22|DEM | US-HOUSE-NY-22 | John Mannion | dem | 0.9858 | 0.944 | 0.0418 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AR-01|REP | US-HOUSE-AR-01 | Will the Republican Party win the AR-01 House seat? | rep | 0.986 | 0.9445 | 0.0415 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-41|DEM | US-HOUSE-CA-41 | Linda Sánchez | dem | 0.986 | 0.9445 | 0.0415 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-41|DEM | US-HOUSE-CA-41 | Linda Sánchez | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-10|DEM | US-HOUSE-WA-10 | Will the Democratic Party win the WA-10 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-19|REP | US-HOUSE-TX-19 | Will the Republican Party win the TX-19 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-UT-01|DEM | US-HOUSE-UT-01 | Ben McAdams | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-16|DEM | US-HOUSE-TX-16 | Will the Democratic Party win the TX-16 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-47|DEM | US-HOUSE-CA-47 | Dave Min | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-35|DEM | US-HOUSE-CA-35 | Will the Democratic Party win the CA-35 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-33|DEM | US-HOUSE-CA-33 | Will the Democratic Party win the CA-33 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-49|DEM | US-HOUSE-CA-49 | Mike Levin | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-42|DEM | US-HOUSE-CA-42 | Will the Democratic Party win the CA-42 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-31|DEM | US-HOUSE-CA-31 | Will the Democratic Party win the CA-31 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-02|DEM | US-HOUSE-WA-02 | Will the Democratic Party win the WA-02 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-20|REP | US-HOUSE-CA-20 | Will the Republican Party win the CA-20 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-ME-01|DEM | US-HOUSE-ME-01 | Will the Democratic Party win the ME-01 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-06|DEM | US-HOUSE-MD-06 | Will the Democratic Party win the MD-06 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-09|REP | US-HOUSE-MI-09 | Will the Republican Party win the MI-09 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-03|DEM | US-HOUSE-MN-03 | Will the Democratic Party win the MN-03 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-07|REP | US-HOUSE-MN-07 | Will the Republican Party win the MN-07 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-03|DEM | US-HOUSE-CA-03 | Ami Bera | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-09|DEM | US-HOUSE-IL-09 | Will the Democratic Party win the IL-09 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-13|DEM | US-HOUSE-IL-13 | Will the Democratic Party win the IL-13 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-09|REP | US-HOUSE-AZ-09 | Will the Republican Party win the AZ-09 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-06|DEM | US-HOUSE-WA-06 | Will the Democratic Party win the WA-06 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-39|DEM | US-HOUSE-CA-39 | Will the Democratic Party win the CA-39 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-03|REP | US-HOUSE-AL-03 | Will the Republican Party win the AL-03 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-38|DEM | US-HOUSE-CA-38 | Will the Democratic Party win the CA-38 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-10|DEM | US-HOUSE-VA-10 | Suhas Subramanyam | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-02|DEM | US-HOUSE-NC-02 | Will the Democratic Party win the NC-02 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-04|DEM | US-HOUSE-NC-04 | Will the Democratic Party win the NC-04 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-03|REP | US-HOUSE-SC-03 | Will the Republican Party win the SC-03 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-06|REP | US-HOUSE-TN-06 | Will the Republican Party win the TN-06 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-LA-03|REP | US-HOUSE-LA-03 | Will the Republican Party win the LA-03 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-08|REP | US-HOUSE-TX-08 | Will the Republican Party win the TX-08 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MA-02|DEM | US-HOUSE-MA-02 | Will the Democratic Party win the MA-02 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-05|REP | US-HOUSE-MI-05 | Will the Republican Party win the MI-05 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-01|DEM | US-HOUSE-NJ-01 | Will the Democratic Party win the NJ-01 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-03|REP | US-HOUSE-TN-03 | Will the Republican Party win the TN-03 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-09|REP | US-HOUSE-IN-09 | Will the Republican Party win the IN-09 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-06|REP | US-HOUSE-IN-06 | Will the Republican Party win the IN-06 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-LA-04|REP | US-HOUSE-LA-04 | Will the Republican Party win the LA-04 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NC-10|REP | US-HOUSE-NC-10 | Will the Republican Party win the NC-10 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-07|REP | US-HOUSE-MO-07 | Will the Republican Party win the MO-07 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-09|REP | US-HOUSE-GA-09 | Will the Republican Party win the GA-09 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KS-02|REP | US-HOUSE-KS-02 | Will the Republican Party win the KS-02 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-08|DEM | US-HOUSE-IL-08 | Will the Democratic Party win the IL-08 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-04|REP | US-HOUSE-TX-04 | Will the Republican Party win the TX-04 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-13|REP | US-HOUSE-TX-13 | Will the Republican Party win the TX-13 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-20|DEM | US-HOUSE-FL-20 | Will the Democratic Party win the FL-20 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-19|REP | US-HOUSE-FL-19 | Will the Republican Party win the FL-19 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-03|REP | US-HOUSE-GA-03 | Will the Republican Party win the GA-03 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MS-01|REP | US-HOUSE-MS-01 | Will the Republican Party win the MS-01 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-06|DEM | US-HOUSE-NY-06 | Will the Democratic Party win the NY-06 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MT-02|REP | US-HOUSE-MT-02 | Will the Republican Party win the MT-02 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MO-06|REP | US-HOUSE-MO-06 | Will the Republican Party win the MO-06 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-08|DEM | US-HOUSE-NJ-08 | Will the Democratic Party win the NJ-08 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-12|DEM | US-HOUSE-NJ-12 | Will the Democratic Party win the NJ-12 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-03|DEM | US-HOUSE-NJ-03 | Will the Democratic Party win the NJ-03 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-15|REP | US-HOUSE-PA-15 | Will the Republican Party win the PA-15 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-14|REP | US-HOUSE-PA-14 | Will the Republican Party win the PA-14 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-12|DEM | US-HOUSE-PA-12 | Will the Democratic Party win the PA-12 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-02|DEM | US-HOUSE-PA-02 | Will the Democratic Party win the PA-02 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-06|DEM | US-HOUSE-CO-06 | Will the Democratic Party win the CO-06 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CT-05|DEM | US-HOUSE-CT-05 | Jahana Hayes | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CT-02|DEM | US-HOUSE-CT-02 | Will the Democratic Party win the CT-02 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-27|DEM | US-HOUSE-CA-27 | George Whitesides | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-26|DEM | US-HOUSE-CA-26 | Will the Democratic Party win the CA-26 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-04|DEM | US-HOUSE-PA-04 | Will the Democratic Party win the PA-04 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OK-02|REP | US-HOUSE-OK-02 | Will the Republican Party win the OK-02 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OR-02|REP | US-HOUSE-OR-02 | Will the Republican Party win the OR-02 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-26|DEM | US-HOUSE-NY-26 | Will the Democratic Party win the NY-26 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-06|REP | US-HOUSE-OH-06 | Will the Republican Party win the OH-06 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-UT-04|REP | US-HOUSE-UT-04 | Will the Republican Party win the UT-04 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-UT-03|REP | US-HOUSE-UT-03 | Celeste Maloy | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-04|DEM | US-HOUSE-AZ-04 | Will the Democratic Party win the AZ-04 House seat? | dem | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-05|REP | US-HOUSE-AL-05 | Will the Republican Party win the AL-05 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-UT-02|REP | US-HOUSE-UT-02 | Blake Moore | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-01|REP | US-HOUSE-AL-01 | Will the Republican Party win the AL-01 House seat? | rep | 0.9862 | 0.945 | 0.0412 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-17|DEM | US-HOUSE-NY-17 | Cait Conley | dem | 0.626 | 0.585 | 0.041 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-TX-15|DEM | US-HOUSE-TX-15 | Bobby Pulido | dem | 0.626 | 0.585 | 0.041 | 1254.8 | 2026-09-11T17:12:06Z |
| kalshi|US-HOUSE-IN-01|DEM | US-HOUSE-IN-01 | Frank Mrvan | dem | 0.9866 | 0.946 | 0.0406 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-06|DEM | US-HOUSE-PA-06 | Will the Democratic Party win the PA-06 House seat? | dem | 0.9868 | 0.9465 | 0.0403 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NJ-05|DEM | US-HOUSE-NJ-05 | Josh Gottheimer | dem | 0.9868 | 0.9465 | 0.0403 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-UT-01|DEM | US-HOUSE-UT-01 | Ben McAdams | dem | 0.9872 | 0.9475 | 0.0397 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-06|DEM | US-HOUSE-NJ-06 | Will the Democratic Party win the NJ-06 House seat? | dem | 0.9873 | 0.948 | 0.0393 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-MI-07|DEM | US-HOUSE-MI-07 | William Lawrence | dem | 0.6188 | 0.58 | 0.0388 | 990.2 | 2026-09-22T17:47:10Z |
| polymarket|US-HOUSE-ID-02|REP | US-HOUSE-ID-02 | Will the Republican Party win the ID-02 House seat? | rep | 0.9877 | 0.949 | 0.0387 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-06|DEM | US-HOUSE-CA-06 | Will the Democratic Party win the CA-06 House seat? | dem | 0.9877 | 0.949 | 0.0387 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CT-05|DEM | US-HOUSE-CT-05 | Jahana Hayes | dem | 0.9879 | 0.9495 | 0.0384 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-HI-01|DEM | US-HOUSE-HI-01 | Will the Democratic Party win the HI-01 House seat? | dem | 0.9879 | 0.9495 | 0.0384 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-10|DEM | US-HOUSE-NJ-10 | Will the Democratic Party win the NJ-10 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-46|DEM | US-HOUSE-CA-46 | Will the Democratic Party win the CA-46 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-14|REP | US-HOUSE-TX-14 | Will the Republican Party win the TX-14 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-06|DEM | US-HOUSE-SC-06 | Will the Democratic Party win the SC-06 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-05|REP | US-HOUSE-KY-05 | Will the Republican Party win the KY-05 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-06|REP | US-HOUSE-FL-06 | Will the Republican Party win the FL-06 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-25|DEM | US-HOUSE-CA-25 | Will the Democratic Party win the CA-25 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-14|REP | US-HOUSE-GA-14 | Will the Republican Party win the GA-14 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MA-01|DEM | US-HOUSE-MA-01 | Will the Democratic Party win the MA-01 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-05|DEM | US-HOUSE-IL-05 | Will the Democratic Party win the IL-05 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-12|REP | US-HOUSE-OH-12 | Will the Republican Party win the OH-12 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-04|REP | US-HOUSE-OH-04 | Will the Republican Party win the OH-04 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CT-03|DEM | US-HOUSE-CT-03 | Will the Democratic Party win the CT-03 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-32|DEM | US-HOUSE-CA-32 | Will the Democratic Party win the CA-32 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CO-02|DEM | US-HOUSE-CO-02 | Will the Democratic Party win the CO-02 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-51|DEM | US-HOUSE-CA-51 | Will the Democratic Party win the CA-51 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-36|DEM | US-HOUSE-CA-36 | Will the Democratic Party win the CA-36 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AR-03|REP | US-HOUSE-AR-03 | Will the Republican Party win the AR-03 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-05|REP | US-HOUSE-CA-05 | Will the Republican Party win the CA-05 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-RI-01|DEM | US-HOUSE-RI-01 | Will the Democratic Party win the RI-01 House seat? | dem | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WI-07|REP | US-HOUSE-WI-07 | Will the Republican Party win the WI-07 House seat? | rep | 0.9881 | 0.95 | 0.0381 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-14|DEM | US-HOUSE-IL-14 | Will the Democratic Party win the IL-14 House seat? | dem | 0.9883 | 0.9505 | 0.0378 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-52|DEM | US-HOUSE-CA-52 | Will the Democratic Party win the CA-52 House seat? | dem | 0.9885 | 0.951 | 0.0375 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-CA-49|DEM | US-HOUSE-CA-49 | Mike Levin | dem | 0.9886 | 0.9515 | 0.0371 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MA-09|DEM | US-HOUSE-MA-09 | Will the Democratic Party win the MA-09 House seat? | dem | 0.9888 | 0.952 | 0.0368 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-RI-02|DEM | US-HOUSE-RI-02 | Will the Democratic Party win the RI-02 House seat? | dem | 0.9888 | 0.952 | 0.0368 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-VA-01|REP | US-HOUSE-VA-01 | Rob Wittman | rep | 0.6115 | 0.575 | 0.0365 | 1254.8 | 2026-09-11T17:12:06Z |
| kalshi|US-HOUSE-UT-02|REP | US-HOUSE-UT-02 | Blake Moore | rep | 0.989 | 0.9525 | 0.0365 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-12|DEM | US-HOUSE-MI-12 | Will the Democratic Party win the MI-12 House seat? | dem | 0.9892 | 0.953 | 0.0362 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-ID-01|REP | US-HOUSE-ID-01 | Will the Republican Party win the ID-01 House seat? | rep | 0.9895 | 0.954 | 0.0355 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-43|DEM | US-HOUSE-CA-43 | Will the Democratic Party win the CA-43 House seat? | dem | 0.9895 | 0.954 | 0.0355 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MN-04|DEM | US-HOUSE-MN-04 | Will the Democratic Party win the MN-04 House seat? | dem | 0.9897 | 0.9545 | 0.0352 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-02|DEM | US-HOUSE-MD-02 | Will the Democratic Party win the MD-02 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-11|DEM | US-HOUSE-IL-11 | Will the Democratic Party win the IL-11 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-10|DEM | US-HOUSE-IL-10 | Will the Democratic Party win the IL-10 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-30|DEM | US-HOUSE-CA-30 | Will the Democratic Party win the CA-30 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-11|REP | US-HOUSE-GA-11 | Will the Republican Party win the GA-11 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-HI-02|DEM | US-HOUSE-HI-02 | Will the Democratic Party win the HI-02 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-01|REP | US-HOUSE-FL-01 | Will the Republican Party win the FL-01 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-01|REP | US-HOUSE-TX-01 | Will the Republican Party win the TX-01 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-01|REP | US-HOUSE-KY-01 | Will the Republican Party win the KY-01 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KS-03|DEM | US-HOUSE-KS-03 | Will the Democratic Party win the KS-03 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-02|REP | US-HOUSE-KY-02 | Will the Republican Party win the KY-02 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-KY-03|DEM | US-HOUSE-KY-03 | Will the Democratic Party win the KY-03 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-02|REP | US-HOUSE-TN-02 | Will the Republican Party win the TN-02 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-SC-07|REP | US-HOUSE-SC-07 | Will the Republican Party win the SC-07 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-03|DEM | US-HOUSE-MD-03 | Will the Democratic Party win the MD-03 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MI-06|DEM | US-HOUSE-MI-06 | Will the Democratic Party win the MI-06 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-15|DEM | US-HOUSE-CA-15 | Will the Democratic Party win the CA-15 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-08|DEM | US-HOUSE-VA-08 | Will the Democratic Party win the VA-08 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-11|DEM | US-HOUSE-NJ-11 | Will the Democratic Party win the NJ-11 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-25|DEM | US-HOUSE-NY-25 | Will the Democratic Party win the NY-25 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-07|DEM | US-HOUSE-NY-07 | Will the Democratic Party win the NY-07 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-14|DEM | US-HOUSE-NY-14 | Will the Democratic Party win the NY-14 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OH-03|DEM | US-HOUSE-OH-03 | Will the Democratic Party win the OH-03 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AZ-07|DEM | US-HOUSE-AZ-07 | Will the Democratic Party win the AZ-07 House seat? | dem | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-15|REP | US-HOUSE-IL-15 | Will the Republican Party win the IL-15 House seat? | rep | 0.9899 | 0.955 | 0.0349 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-09|DEM | US-HOUSE-NY-09 | Will the Democratic Party win the NY-09 House seat? | dem | 0.9901 | 0.9555 | 0.0346 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-04|DEM | US-HOUSE-GA-04 | Will the Democratic Party win the GA-04 House seat? | dem | 0.9901 | 0.9555 | 0.0346 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NJ-04|REP | US-HOUSE-NJ-04 | Will the Republican Party win the NJ-04 House seat? | rep | 0.9902 | 0.956 | 0.0342 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-08|DEM | US-HOUSE-MD-08 | Will the Democratic Party win the MD-08 House seat? | dem | 0.9902 | 0.956 | 0.0342 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-OR-01|DEM | US-HOUSE-OR-01 | Will the Democratic Party win the OR-01 House seat? | dem | 0.9906 | 0.957 | 0.0336 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-04|DEM | US-HOUSE-CA-04 | Will the Democratic Party win the CA-04 House seat? | dem | 0.9906 | 0.957 | 0.0336 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-NY-19|DEM | US-HOUSE-NY-19 | Josh Riley | dem | 0.9906 | 0.957 | 0.0336 | 1063.2 | 2026-09-19T16:49:26Z |
| polymarket|US-HOUSE-IN-03|REP | US-HOUSE-IN-03 | Will the Republican Party win the IN-03 House seat? | rep | 0.9908 | 0.9575 | 0.0333 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-GA-10|REP | US-HOUSE-GA-10 | Will the Republican Party win the GA-10 House seat? | rep | 0.9909 | 0.958 | 0.0329 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MD-05|DEM | US-HOUSE-MD-05 | Will the Democratic Party win the MD-05 House seat? | dem | 0.9909 | 0.958 | 0.0329 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-08|DEM | US-HOUSE-CA-08 | Will the Democratic Party win the CA-08 House seat? | dem | 0.9909 | 0.958 | 0.0329 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-30|DEM | US-HOUSE-TX-30 | Will the Democratic Party win the TX-30 House seat? | dem | 0.9911 | 0.9585 | 0.0326 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-24|DEM | US-HOUSE-FL-24 | Will the Democratic Party win the FL-24 House seat? | dem | 0.9913 | 0.959 | 0.0323 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-08|DEM | US-HOUSE-NY-08 | Will the Democratic Party win the NY-08 House seat? | dem | 0.9913 | 0.959 | 0.0323 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NE-03|REP | US-HOUSE-NE-03 | Will the Republican Party win the NE-03 House seat? | rep | 0.9913 | 0.959 | 0.0323 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-09|DEM | US-HOUSE-WA-09 | Will the Democratic Party win the WA-09 House seat? | dem | 0.9913 | 0.959 | 0.0323 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-NY-20|DEM | US-HOUSE-NY-20 | Will the Democratic Party win the NY-20 House seat? | dem | 0.9913 | 0.959 | 0.0323 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-01|REP | US-HOUSE-PA-01 | Brian Fitzpatrick | rep | 0.5969 | 0.565 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-ME-02|REP | US-HOUSE-ME-02 | Paul LePage | rep | 0.5969 | 0.565 | 0.0319 | 1302.7 | 2026-09-09T17:16:40Z |
| kalshi|US-HOUSE-TX-35|DEM | US-HOUSE-TX-35 | Johnny C. Garcia | dem | 0.5969 | 0.565 | 0.0319 | 1206.9 | 2026-09-13T17:04:34Z |
| polymarket|US-HOUSE-OR-06|DEM | US-HOUSE-OR-06 | Will the Democratic Party win the OR-06 House seat? | dem | 0.9914 | 0.9595 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-PA-09|REP | US-HOUSE-PA-09 | Will the Republican Party win the PA-09 House seat? | rep | 0.9914 | 0.9595 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-PA-01|REP | US-HOUSE-PA-01 | Brian Fitzpatrick | rep | 0.5969 | 0.565 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CT-01|DEM | US-HOUSE-CT-01 | Will the Democratic Party win the CT-01 House seat? | dem | 0.9914 | 0.9595 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-FL-22|REP | US-HOUSE-FL-22 | Will the Republican Party win the FL-22 House seat? | rep | 0.5969 | 0.565 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TX-15|DEM | US-HOUSE-TX-15 | Bobby Pulido | dem | 0.5969 | 0.565 | 0.0319 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IN-02|REP | US-HOUSE-IN-02 | Will the Republican Party win the IN-02 House seat? | rep | 0.9916 | 0.96 | 0.0316 | 1307.9 | 2026-09-09T12:06:41Z |
| kalshi|US-HOUSE-WA-08|DEM | US-HOUSE-WA-08 | Kim Schrier | dem | 0.9916 | 0.96 | 0.0316 | 1063.2 | 2026-09-19T16:49:26Z |
| polymarket|US-HOUSE-OR-03|DEM | US-HOUSE-OR-03 | Will the Democratic Party win the OR-03 House seat? | dem | 0.9917 | 0.9605 | 0.0312 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-IL-04|DEM | US-HOUSE-IL-04 | Will the Democratic Party win the IL-04 House seat? | dem | 0.9917 | 0.9605 | 0.0312 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-MA-03|DEM | US-HOUSE-MA-03 | Will the Democratic Party win the MA-03 House seat? | dem | 0.9919 | 0.961 | 0.0309 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CA-50|DEM | US-HOUSE-CA-50 | Will the Democratic Party win the CA-50 House seat? | dem | 0.9919 | 0.961 | 0.0309 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-TN-01|REP | US-HOUSE-TN-01 | Will the Republican Party win the TN-01 House seat? | rep | 0.9921 | 0.9615 | 0.0306 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-09|REP | US-HOUSE-VA-09 | Will the Republican Party win the VA-09 House seat? | rep | 0.9921 | 0.9615 | 0.0306 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-AL-07|DEM | US-HOUSE-AL-07 | Will the Democratic Party win the AL-07 House seat? | dem | 0.9921 | 0.9615 | 0.0306 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-CT-04|DEM | US-HOUSE-CT-04 | Will the Democratic Party win the CT-04 House seat? | dem | 0.9921 | 0.9615 | 0.0306 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WA-07|DEM | US-HOUSE-WA-07 | Will the Democratic Party win the WA-07 House seat? | dem | 0.9922 | 0.962 | 0.0302 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-WV-01|REP | US-HOUSE-WV-01 | Will the Republican Party win the WV-01 House seat? | rep | 0.9922 | 0.962 | 0.0302 | 1307.9 | 2026-09-09T12:06:41Z |
| polymarket|US-HOUSE-VA-03|DEM | US-HOUSE-VA-03 | Will the Democratic Party win the VA-03 House seat? | dem | 0.9922 | 0.962 | 0.0302 | 1307.9 | 2026-09-09T12:06:41Z |
