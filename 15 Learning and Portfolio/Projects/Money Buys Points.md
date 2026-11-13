---
type: project
area: learning
status: active
deadline: 
waiting_on: 
repo: 
---
# Money Buys Points

> [!info] Snapshot
> **What:** Tableau Public dashboard asking whether Premier League transfer spend buys league points, in the same season and the next (2018-19 to 2022-23). Bradley's main dashboard for his Data School application.
> **Headline:** "CAN MONEY BUY POINTS? YES, A SEASON LATE."
> **Who:** Bradley. Feedback from Lauren Whitfield (GRB recruiter, see [[Contacts and Recruiters]]).
> **Where things live:** [Tableau Public](https://public.tableau.com/app/profile/bradley.duke/viz/MoneyBuysPoints/MoneyBuysPoints). Latest workbook "Money Buys Points - monochrome design.twbx". Data, mockups and build plan in Bradley's Tableau Claude project.

## Next actions
- [ ] Annotate charts: S1 (Man City vs Southampton), S3b (2022-23), S6 (the gap). Shade 2022-23 on S3a and S3b
- [ ] Rewrite the default tooltips
- [ ] Delete unused sheets, including the stale "Dashboard 1" duplicate
- [ ] Publish the monochrome version and check it on Tableau Public (5 background images, header icons)
- [ ] Rewrite "Why I built this" in my own words
- [ ] Write the short note about me
- [x] Submit the Data School application (see [[APP-002 The Data School - Data School]])
- [ ] Optional: decide on the compact cut (drop sections 05 and 08)
- [ ] Interview prep: 2-minute walkthrough, answers on data limitations, a process for an unseen dataset

## Open questions
- Which version is live at the main link (v1, v2 or monochrome)? v2 is also on the profile as MoneyBuysPointsv2/Dashboard1.
- Current size: 1000 x 5175 (28-10-2026) or 7,763px at 1200 wide (27-10-2026)?
- Which planned charts, calculated fields, sets, the outlier parameter and the club picker are actually built, and how many sheets?
- Top-5 spender figure: +4.4 vs -3.7 points (p = 0.007) or +3.7 vs -3.6 (p = 0.015). Pick one definition.
- Transfermarkt and Wikipedia source URLs not recorded. Start date not known.

## Question and data
- **Question:** does a club's gross transfer spend predict its league points in the same season, and the season after?
- **Dataset:** `premier_league_spend_2018_2023_v3.csv`, 100 club-seasons (20 clubs x 5 seasons), 20 columns. Gross spend and income from Transfermarkt (EUR m, nominal, both windows, loan fees included), collected by hand. Points and positions from final league tables; 2023-24 points (after Everton -8 and Forest -4) used as next-season points for 2022-23. Helper file `season_r.csv`.
- **Tools:** Tableau Public Desktop. Python for the regression models and tests, done together with Claude: be ready to explain each test in interview. HTML mockups as design templates.

## What's built
- **Data prep:** rebuilt from scratch on 26-09-2026 after a row-by-row check of v1 found 6 wrong and 13 doubtful figures and a sample skewed to top-10 finishers. Big six reconciled to Transfermarkt five-season totals. v3 (02-10-2026) added net spend, relative spend, previous and next season points, expected points and residuals.
- **Tableau techniques:** calculated fields (expected points, residual, trend group, bands, cost per point, next-season prediction), FIXED LODs (season average spend, seasons in league, club cost per point), WINDOW_CORR table calc for season r, combined Top 8 / Bottom 8 set, pivoted data source, highlight action club picker.
- **Layout:** header with four KPI cards, three part banners, eight numbered sections (scatter with trend and band, strip plot, dumbbell, spend bars over season r, cost-per-point heat table, slope chart, controlled-effect scatter, bump chart), verdict cards, "Why I built this", sources footer. Monochrome with one red accent.

## Key findings
- **Same season:** r = 0.23, R² = 0.05 (n = 100), about +0.5 points per extra EUR 10m. In 2022-23 Man City (EUR 155m) won the league and Southampton (EUR 154m) finished bottom.
- **Top spender won 0 of 5 titles.** Champions averaged EUR 111m against EUR 302m for the top spender. Liverpool won 2019-20 with 99 points on EUR 10.4m.
- **Over and underperformers:** 7 of the top 8 against the trend were Liverpool or Man City, and 7 of the bottom 8 were relegated. Chelsea 2022-23 finished 37 points below what EUR 630m predicts.
- **Cost per point:** league EUR 1.90m. Liverpool 1.22m, Man City 1.60m, Chelsea 3.93m.
- **Season r:** 0.37, 0.20, 0.60, 0.58, 0.02. 2022-23 r falls to 0.02 (0.25 without Chelsea).
- **A season late:** for the 85 club-seasons that stayed up, r with same-season points 0.16 against next-season 0.39 (Williams test p = 0.004). Controlling for this season's points, spend adds about +5.9 points per EUR 100m next season (p = 0.001, clustered by club), R² 49% to 57%.
- **Regression to the mean:** clubs 15+ points above trend dropped 7.5 the next season; clubs 10+ below that stayed up rose 6.3.
- **Not supported:** diminishing returns (log R² 4.2% against linear 5.1%) and net spend (r = 0.07). Transfer income r = 0.31 against gross spend r = 0.23.
- **Limitations to own:** five seasons is a small sample, fees ignore wages, spend is nominal, and only the 2020-21 and 2021-22 season correlations are significant at 5%.

## Ideas
- Extend to 2013-14 to 2024-25 (about 240 club-seasons) and test the lag out of sample.
- Match results from football-data.co.uk for a title race chart and a before and after Christmas test.
- Add wages (club accounts, Capology via FBref) for a transfers vs wages panel.
- Player-level transfers and minutes to test whether new signings play more in year 2.
- "Spending stripes" banner, one stripe per season.
- Relative spend as the scatter's x-axis (already in v3).
- "Selling predicts points as well as buying" angle.
- Five-season total spend vs average points (r = 0.50, 14 clubs), kept back for interview.
- Fit the controlled model live in Tableau with MODEL_QUANTILE.
- Do relegated and promoted clubs show that spending protects you from the drop?

## Decisions
- 26-09-2026: rebuilt the data because v1 clashed with known transfers and was mostly top-10 finishers. Switched to EUR m nominal from Transfermarkt, nominal stated as a limitation.
- Headline moved to "Yes, a season late" because the controlled lag model supports it far more strongly than the old "until it doesn't" line, and the "sweet spot" finding disappeared with clean data.
- ±15 points against trend as the beat or fell short threshold. No claims about diminishing returns or net spend. Chelsea caveat on the 2022-23 finding.
- 28-10-2026: monochrome plus one red accent, picked from three options because the strongest DS60 finals went calmer. Red used only for the headline answer, hero KPI, named clubs and the S7 trend line.
- Custom fonts as PNG images, everything else Tableau Book / Bold, because Tableau Public only renders Tableau and web-safe fonts.
- More chart types, less text (target 9 charts across 7 types), after benchmarks showed final vizzes get shorter and denser.

## Status log
- 24-09-2026: feedback from Lauren Whitfield on v1 (question headline, clear sections, conclusion and sources at the bottom, neutral background, colour-blind-safe palette).
- 26-09-2026: data rebuilt (100 club-seasons). Self-score 5/4/5/4/5/3/3.
- 02-10-2026: v2 published with v3 data. Self-score 6/7/5/4/8/5/6 (point of view, story flow, chart choice, design craft, analytical depth, personality, technical polish).
- 07-10-2026: design spec written. Target score 9/9/8/9/9/8/8.
- 28-10-2026: monochrome colour scheme.
- 01-11-2026: Data School application not yet submitted.
- 13-11-2026: imported from Bradley's Tableau Claude project. Bradley confirmed the Data School application is submitted.

## Links
- [Tableau Public](https://public.tableau.com/app/profile/bradley.duke/viz/MoneyBuysPoints/MoneyBuysPoints)
- Build plan and visual template: Claude artifacts in the Tableau project (may be private).
- [[Portfolio Projects]] · [[Job Hunt]] · [[CV and Interview Prep]]

> [!warning] No secrets
> Never paste passwords, account numbers, login details or API keys here. Note where they live instead.
