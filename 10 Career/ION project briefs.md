---
type: reference
area: career
---
# ION project briefs

Everything you've done, one brief each. Know these and you can answer almost any question by picking the right project. Facts come from your CVs and project notes. Anything marked **check** needs confirming before you say it.

## Which project for which question

| If they ask about... | Use |
| --- | --- |
| Attention to detail, spotting errors | Dissertation data problem, Money Buys Points rebuild, match report half-time fix, finance internship |
| Numeracy and probability | Dissertation, Money Buys Points, share price project |
| Trends and patterns in data | Share price project, business simulation, Money Buys Points, match report |
| Excel | Finance internship, match report, share price project, business simulation |
| Learning new software fast | Tableau dashboards, Dartfish, Statistica, R, Minitab |
| Problem solving, troubleshooting | Dissertation rebuild, Money Buys Points rebuild |
| Trading decisions, odds | Dissertation (live bets), reselling |
| Time zones and currencies | Money Buys Points (euros), share price project (trading days and times) |
| Communicating, working with others | Jigsaw24, energy project, business simulation, football captain, Bershka |
| Responsibility, maturity | Jigsaw24 confidentiality, cricket coaching, finance internship |
| Initiative | Money Buys Points, graduate dashboard, portfolio website, reselling |
| Organisation and deadlines | Finance internship month-end, dissertation, reports with page limits |

---

## 1. Dissertation: Beating the Bookies (2025 to 2026)

**What:** a neural network (multi-layer perceptron) that predicts Premier League results, compared with bookmaker odds.

**What you did**

- Built the dataset: three seasons of Premier League matches, 52 statistics per match.
- Built and ran the model in Statistica and Python. Ran six experimental set-ups, 50 runs each.
- Turned bookmaker odds into implied probabilities and compared them with the model's.
- Tested it for real: placed actual bets on its predictions over two live matchweeks.
- Worked through the maths behind it (backpropagation, perceptron convergence).

**The problem you solved:** the dataset got corrupted while you were compiling it (statistics overlapping, some missing). You spotted it when checking the data before putting it into the model. FBref had just lost its Opta data, so your main source had gone. You rebuilt the dataset from several sources, matched them up, and finished.

**Numbers:** 3 seasons, 52 statistics, 6 set-ups, 50 runs, best mean AUC 0.9844, 2 live matchweeks.

**Shows:** attention to detail, problem solving under pressure, probability, odds, trading decisions, persistence.

**Check before Thursday**

- Your CV says you found "a previously unreported error in the source dataset". Is that the same as the corruption story, or a separate error in the original data? Know which.
- What the two live matchweeks showed (won or lost, and what you learned).
- The AUC of 0.9844 is very high for football. If asked, know whether the 52 statistics were from before the match or from the match itself. If they were from the match, say the model explains results rather than predicting them in advance. Being upfront about limits impresses people.

---

## 2. Performance Analysis: post-match report (module, First)

**What:** a full analysis of one football match, turned into a one-page dashboard.

**What you did**

- Tagged over 1,000 events from a full match in Dartfish.
- Noticed the pitch-zone data was wrong after the teams swapped ends at half-time, and corrected it.
- Used Excel pivot tables and charts to build a one-page dashboard of team and player performance.

**Numbers:** 1,000+ events, one page.

**Shows:** attention to detail (the half-time fix is a perfect small example), Excel, learning new software, spotting patterns.

---

## 3. Share price project: NatWest vs the FTSE (Mathematical Enterprise, and time series work)

**What:** testing ways to spot patterns in share prices, then using them on real data.

**What you did**

- Built test data in Excel with functions like RAND and SIN, and used charts to check its shape and trend.
- Wrote five rules for spotting patterns in time series.
- Collected around 60 NatWest and FTSE prices at 30-second, daily and monthly scales.
- Left out non-trading days so they didn't distort the results.
- Measured volatility to judge NatWest as a pension investment.
- Related time series work: ARIMA models in R and Minitab, with model selection rules from ACF and PACF diagnostics.

**Numbers:** about 60 prices, 3 time scales, 5 rules.

**Shows:** finding trends, Excel, financial markets, knowing when markets are open (time zones angle), careful data handling.

---

## 4. Business simulation: data analyst role (2024)

**What:** a group project building a business proposal. You were the data analyst.

**What you did**

- Designed a survey that got 150+ responses.
- Used Excel and statistical testing (hypothesis tests, error bounds) to find three significant trends in consumer behaviour.
- Used public databases to find market opportunities.
- Presented through reports, Excel charts, a group video pitch and an A1 poster.

**Numbers:** 150+ responses, 3 significant trends.

**Shows:** trends in data, telling real patterns from noise, Excel, teamwork, presenting.

---

## 5. Jigsaw24 industry project (2024 to 2026)

**What:** real consultancy work with a company, Jigsaw24.

**What you did**

- Analysed commercially sensitive business data under a confidentiality agreement.
- Used regression modelling in R to answer the company's business questions.
- Reported findings in a structured report, plus a short video reflection.

**Shows:** responsibility (trusted with confidential data), working with a real client, explaining results to non-specialists.

---

## 6. Energy consumption modelling (statistics module)

**What:** predicting industrial energy use.

**What you did**

- Compared five types of regression model (multiple linear, LASSO, ridge, PCR, PLS).
- Picked the best one by testing each on held-back data.
- Turned the results into plain-English recommendations for a non-specialist client, within a page limit.

**Shows:** choosing the right tool by testing, not guessing; explaining technical results simply; working to a tight brief.

---

## 7. Design of Experiments coursework

**What:** analysing experimental datasets.

**What you did:** used ANOVA, factorial design, GLMs and logistic regression, and checked each model's assumptions properly.

**Shows:** checking your work is valid before trusting it. Use briefly, as backup.

---

## 8. Money Buys Points: Tableau dashboard (personal project, 2026)

**What:** does Premier League transfer spending buy league points? Built on your own time, published on Tableau Public.

**What you did**

- Collected the data by hand: 100 club-seasons (20 clubs x 5 seasons, 2018-19 to 2022-23), spending from Transfermarkt in euros, points from league tables.
- Checked your first version row by row, found 6 wrong and 13 doubtful figures and a sample skewed to top-10 clubs, and rebuilt the dataset from scratch. Checked the big six against Transfermarkt's five-season totals.
- Built the dashboard in Tableau, teaching yourself calculated fields and other techniques as you went.

**Findings worth quoting**

- Spending explains only about 5% of points in the same season.
- The top spender won 0 of 5 titles. Liverpool won in 2019-20 spending about €10m.
- Spending matters more the next season: "Can money buy points? Yes, a season late."

**Shows:** initiative (most important to ION), attention to detail (the rebuild), working in euros, learning Tableau fast, sport.

**Careful:** the statistical tests were done with Claude's help. Say you led the analysis. Explain findings in plain English, or skip the stats.

---

## 9. What Gets International Graduates Hired: Tableau dashboard (personal project, 2026)

**What:** a second published dashboard: what decides whether an international graduate gets a job?

**What you did:** analysed 300,000 records in Tableau and built a full dashboard with calculated fields.

**Finding:** three things (an advanced degree, strong language skills and an edge such as an internship) took employment from 4% to 100%. Subject and home country made no difference.

**Careful:** the data was synthetic (generated), which is why the numbers are so clean. Say so if you mention it.

**Shows:** handling large datasets, learning Tableau, initiative.

---

## 10. Portfolio website (2026)

**What:** your own website showing both dashboards and eight university projects, published on GitHub Pages.

**Shows:** initiative, learning new tools. A good answer to "what have you done off your own back?"

---

## 11. Finance internship: USP College Finance Office (June to August 2023)

**What you did**

- Reconciled 200+ accounts payable and receivable transactions every week.
- Supported month-end close (journals, balance sheet reconciliations, accruals).
- Checked ledger data in Excel with pivot tables and VLOOKUP to find discrepancies, and recommended process improvements.
- Reviewed department spending to find savings.

**Numbers:** 200+ transactions a week; 2-day reduction in reporting turnaround; 15% cost reduction across four areas.

**Shows:** the closest thing on your CV to this job. Reconciliation, spotting discrepancies, Excel, deadlines, accuracy with money.

**Check:** be ready to say how the 2 days and 15% came about, and one improvement you suggested.

---

## 12. Bershka: sales assistant (July 2026 to now)

**What you do:** customer-facing sales at Bershka Lakeside, 40 hours a week on a changing rota: weekends, late finishes up to 22:00, split shifts.

**Shows:** flexibility with shifts and weekends, dealing with people, working under pressure on busy days.

**Have ready:** one real story about a busy shift or a difficult customer.

---

## 13. Reselling (about 2021 to 2023, restarted November 2026)

**What you do:** buy limited items and resell them for profit. You check recent sold prices, decide what to buy and at what price, and track stock, margins and return deadlines.

**Shows:** making decisions with money on the line using market prices, spotting opportunities, organisation. Your call whether to mention it.

---

## 14. Football captain and youth cricket coach

**What:** captain of a local football team; coach young cricket players.

**Shows:** leadership, keeping people informed, staying calm under pressure, responsibility for others. Plus your genuine love of sport (West Ham, NBA).
