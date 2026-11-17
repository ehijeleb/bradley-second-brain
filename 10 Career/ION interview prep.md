---
type: reference
area: career
---
# ION interview prep

> [!info] What this is
> Prep for the ION online interview for [[APP-001 ION Asset Architecture - Trading Operations Assistant]]: **Thursday 19-11-2026, 11:00, Google Meet, about 30 minutes** (link in Olivia's email). Briefing with Olivia Ross on Teams **Wednesday 18-11-2026, 09:15 to 09:30**. Made 16-11-2026, updated 17-11-2026 with ION's spec and guidelines ([[2026-11-17 Datatech - Interview Confirmation - Ion Asset Architecture UK Ltd]]).
> **Excel practice:** `10 Career/Exports/ION/ION Excel practice.xlsx` (sports trading data with planted errors, tasks and an answer key).
> Answers below use only real evidence from [[CV-v7]] and [[CV and Interview Prep]]. Lines marked **Bradley to fill** need a real example from you.

## Logistics
- **Clash on Wednesday:** the briefing runs 09:15 to 09:30, when you'd normally leave for a 10:00 shift. Take it from home and leave straight after, or take it on the move with headphones somewhere quiet.
- **Thursday:** interview 11:00 to about 11:30, shift at 12:30. ION's guidelines say interviews can run 30 minutes to 2 hours, and ask you to say up front if you have a hard stop (it won't count against you). Tell Olivia in the briefing, and say it politely at the start of the call if needed.
- Gym is planned for 09:30 to 10:30 on Thursday ([[Fitness]]). Worth moving it so you're not rushing back.
- Before the call: phone on silent, test the connection, laptop camera at eye level, quiet room, plain background. Treat it as face to face (Olivia's advice).
- Have open: [[CV-v7]] (the CV ION have), the spec, a pen and paper for working out.

## Ask Olivia in the briefing (Wed 09:15)
- Who's interviewing: someone from trading operations, a researcher or HR? (Round 1 is usually with someone from a similar background.)
- Will there be numerical questions, and are they mental arithmetic, written working, or both? Calculator allowed?
- Anything ION have said about your CV that they'll want to dig into?
- Tell her about the 12:30 shift, so the call can't run long, and ask her to pass that on.
- Next steps if it goes well (ION normally do several in-person rounds at the Gherkin).

## What ION is (from their guidelines, the only official source)
- **Ion Asset Architecture UK Limited**: a small team of researchers and software developers analysing and **trading sports markets**. Evidence-driven, highly automated. Floor 28, 30 St Mary Axe (the Gherkin).
- **Not** part of ION Group, ION Trading, ION Equity or any similar name: their FAQ says so directly. Don't mention ION Group or XTP. (The note here before 17-11-2026 guessed at an ION Group link. That was wrong.)
- No website on purpose: low profile. Use the guidelines and employees' LinkedIn profiles instead.
- Technology-first: everything is built in-house. Huge databases (nearly a trillion rows), a global low-latency network, grid computing, heavy automation in C#. Data types: market, reference, business, telemetry.
- Things they don't do: store data in spreadsheets, put business logic in SQL, run the business by email, hold meetings for the sake of it.
- Culture: flat hierarchy, no bureaucracy, about 10 hours a day in the office including lunch and gym, mostly office-based, 25 days' holiday plus bank holidays, gym membership, don't hire smokers, progression based on your input.

**What this means for you:** Excel matters for the role (the spec asks for it), but they don't use spreadsheets as a data store. Pitch Excel as checking and analysis, and stress learning their in-house tools and SQL quickly. "Ability to come to grips with new applications quickly" is in the spec.

## Every requirement in the spec: question and answer
For each one: the question they're likely to ask, then your answer from real evidence. Say it in your own words; don't read it out. **Bradley to fill** means only you have the detail.

**1. BSc, ideally maths or science**
*"Tell me about your degree. What did you enjoy most?"*
High 2:1 in Maths and Sports Science at Nottingham Trent. Firsts in Applied Statistics, Statistical Modelling and Performance Analysis; 2:1 in Probability and Statistical Inference. The best part was the dissertation, "Beating the Bookies": predicting Premier League results and comparing my model's probabilities with bookmaker odds. That's the closest thing in my degree to what ION does.

**2. Excel**
*"How would you rate your Excel? Give an example."*
Strong for reconciliations and analysis. In the finance internship I reconciled 200+ transactions a week and used pivot tables and VLOOKUP to find discrepancies in ledger data. In Performance Analysis I tagged 1,000+ match events and built a one-page dashboard with pivot tables and charts. Name what you haven't used (for example XLOOKUP, Power Query, macros) and say you'd pick them up quickly. See the Excel questions below.

**3. Picking up new applications quickly**
*"Tell me about a time you had to learn a new tool fast."*
Taught myself Tableau and published two dashboards ([[Money Buys Points]] and [[What Gets International Graduates Hired]]). At university I learned Dartfish for match tagging, plus Minitab, Statistica and MATLAB, as each module needed them. **Bradley to fill:** how long Tableau took you to get usable, and one thing you worked out on your own.

**4. Attention to detail**
*"Give an example of an error you spotted that others missed."*
Dissertation: while checking three seasons of match data (52 statistics per match), I found a previously unreported error in the source dataset, documented it and corrected for it before modelling. **Bradley to fill:** what exactly the error was and how you spotted it. This is your strongest answer, so know it cold.
Backups: in the match report, the pitch-zone data was wrong after the teams swapped ends at half-time, and I corrected it. On Money Buys Points I spotted errors in an earlier version and rebuilt it.
*"How do you make sure your own work is right?"* Check totals against a second source, sense-check extremes, re-check anything that looks too good, and check before sending, not after.

**5. Numeracy, including probabilities**
*Expect live questions: see the pop quiz and brainteasers below.*
Talking point: in the dissertation I turned bookmaker odds into implied probabilities, took out the margin, and compared them with my model's probabilities.

**6. Time zones and currencies**
*"Are you comfortable working across time zones and currencies?"*
Yes. Money Buys Points used Transfermarkt data in euros, so I worked in EUR (for example "6 points per EUR 100m"). In the NatWest vs FTSE project I worked with prices at 30-second, daily and monthly scales and left out non-trading days so they didn't distort the results, which is the same idea as knowing when each market is open. Following the NBA from the UK means always converting US times. **Bradley to fill:** any other real example (buying or selling abroad, travel).
*Be ready for:* "What time is it in New York now?" (5 hours behind in November) and "Name as many currencies as you can."

**7. Making informed trading decisions**
*"Tell me about a decision you made based on data or odds."*
The dissertation was this: if my model's probability for a result was higher than the bookmaker's implied probability, that's a value bet. I tested it over two live matchweeks. **Bradley to fill:** what the live test showed, even if the model lost. Saying honestly what didn't work is a good answer.
Judgement call: reselling (deciding what to buy at what price for a margin, see [[Reselling]]) is real trading-style decision-making. Use it only if you're comfortable talking about it.

**8. Organisation, structured approach, keeping colleagues updated**
*"How do you organise your work? How do you keep your team informed?"*
Finance internship: a weekly reconciliation routine and month-end close to a deadline. Captaining a football team: organising players and passing on information. **Bradley to fill:** a Bershka example (handing over to the next shift, telling a manager about a stock problem). Being honest that you track the job hunt, reselling and money in one system is also fair evidence of being structured.

**9. SQL**
*"What's your SQL like?"*
Be honest: basics, working through the W3Schools course. Your CV lists SQL, so don't contradict it, but don't oversell it. Know the basic shape of a query (below). Say you're keen to learn it properly on the job, as the spec allows.

**10. Interpersonal skills, mature and responsible**
*"Tell me about a difficult customer or colleague." "When were you trusted with responsibility?"*
Bershka: customer-facing every day. Coaching youth cricket: being responsible for young players. Jigsaw24 project: worked with commercially sensitive data under a confidentiality agreement and presented findings to the partner. **Bradley to fill:** one real Bershka story with a difficult customer or a busy period.

**11. Flexible hours, weekend rota, swapping weekdays for weekends at least 50% of the time**
*"Are you genuinely OK with this?"*
Yes, and you can show it: at Bershka you already work shifts that change week to week, including weekends, late finishes up to 22:00 and split shifts. Only say yes if it's true. They'll take a straight answer seriously.

**12. Initiative (they say this matters most)**
*"Tell me about something you started on your own."*
After graduating I built and published Money Buys Points on my own time: assembled a 100 club-season dataset from Transfermarkt and league tables, built it in Tableau, then rebuilt it when I found errors in the first version. In the finance internship I didn't just reconcile, I recommended process improvements. **Bradley to fill:** one of those improvements.
Careful: the Money Buys Points statistics were done with Claude's help. Say you led the analysis and be ready to explain what the regression shows, or leave the stats out.

## The role in one line
Support ION's researchers in running their trading strategies: monitor 24/7 trading platforms, spot errors and unusual behaviour, take corrective action, troubleshoot the trade cycle, and liaise with traders, counterparties and trading venues. Data quality and operations, not pure analysis. Strong Excel; SQL learnt on the job.

## Likely questions and your answers

**1. Tell me about yourself (60 seconds)**
"I graduated this year from Nottingham Trent with a high 2:1 in Maths and Sports Science. The common thread through my degree was working with data and checking it was right. My dissertation built a model to predict Premier League results from three seasons of match data and compared its probabilities with bookmaker odds, and while checking the data I found an error in the source dataset that hadn't been reported. Before that I interned in a college finance office, reconciling 200+ transactions a week and checking ledger data in Excel for discrepancies. I'm working at Bershka while I look for a role like this, where accuracy, numbers and sport come together."

**2. Why this role?**
It combines the three things you're best at: accuracy with data, probability and odds, and sport. Say you understand it's about data quality and spotting errors on a live platform, and that's what you want, not a pure analyst role.

**3. Why sports trading?**
Your dissertation compared model probabilities with bookmaker odds and tested them over two live matchweeks, so you've already worked with how markets price outcomes. Plus West Ham, NBA, captaining a football team.

**4. Tell me about a time you spotted an error**
- **Situation:** dissertation, three seasons of Premier League data, 52 statistics per match.
- **Task:** make sure the data was reliable before modelling.
- **Action:** checked it systematically and found figures that didn't match. **Bradley to fill:** what exactly was wrong and how you found it.
- **Result:** documented a previously unreported error in the source dataset and corrected for it.
Backup: performance analysis report, where you corrected the pitch-zone data after the teams swapped ends at half-time.

**5. Attention to detail under time pressure**
Finance internship: 200+ accounts payable and receivable transactions a week, month-end close, ledger checks with pivot tables and VLOOKUP. **Bradley to fill:** one specific discrepancy you found and what happened.

**6. How good is your Excel?**
Pivot tables, VLOOKUP, charts and dashboards, financial modelling, reconciliation and error checking. Give one example (the one-page match dashboard from 1,000+ tagged events). Be honest about anything you haven't used (for example XLOOKUP or Power Query) and say you're learning it. Practise with the workbook first.

**7. Are you OK with the shifts?**
Yes: 07:00-17:00, 09:00-19:00 and 14:00-00:00, about half of weekends, on site at the Gherkin. Already told Datatech you can start immediately. Only say yes if it's true.

**8. Tell me about a time you had to adapt quickly**
Sigma's Equalture feedback flagged cognitive flexibility, so have a strong example ready. **Bradley to fill:** a real one, for example a Bershka shift where plans changed, or a change in your football team mid-match as captain.

**9. Working under pressure / busy periods**
**Bradley to fill:** a real Bershka example (busy weekend, queue, stock problem).

**10. A mistake you made**
**Bradley to fill:** a real, small one, what you did about it, and what you check now because of it.

**11. Why ION?** (Olivia says they'll ask about interest in the organisation)
Small, evidence-driven team trading sports markets: the one place your maths, probability and sport all count. You like that it's technology-led and automated, so the job is about catching what the automation misses, and that the flat structure means progression depends on what you put in. Mention you read the guidelines (they wrote them instead of a website).

**12. A time you made a decision with incomplete information**
Ties to "comfortable making informed trading decisions". **Bradley to fill:** a real one (reselling buy decision, a call as football captain).

**13. Salary expectations**
In line with the advertised salary (up to £33,000 base).

## Quick numerical drill (in case they test odds)
- Implied probability = 1 / decimal odds. 2.00 = 50%. 1.50 = 66.7%. 4.00 = 25%.
- Fractional to decimal: add 1. 5/2 = 3.50 (28.6%). 1/4 = 1.25 (80%). Evens = 2.00.
- Overround: add up the implied probabilities for every outcome in a market. Home 2.10, Draw 3.40, Away 3.60 gives 47.6% + 29.4% + 27.8% = 104.8%, so 4.8% margin. Under 100% means the prices are wrong (an arbitrage), which is exactly the kind of error this role catches.
- Quick sense checks: odds can't be below 1.00; a favourite should have the lowest odds; a settled market shouldn't still be open after the result.

## How ION would use Excel (inferred)
Nothing from ION spells this out. This is worked out from the spec (strong Excel, time zones and currencies, spotting inconsistencies, insight into counterparty and market behaviour) and the guidelines (in-house tools, big databases, spreadsheets not used to store data).
- **Checking exports:** pulling trades, prices or settlement reports out of their in-house tools and checking them for errors, duplicates and gaps.
- **Reconciliations:** matching ION's own trade records against what a counterparty or exchange reports. This is the same job as your finance internship reconciliations.
- **Currencies:** turning positions or P&L in euros, dollars and so on into pounds.
- **Time zones:** checking that event start times and settlement times line up across markets.
- **Ad hoc analysis:** quick summaries of how a counterparty or market behaved (volumes, unusual prices) for the traders.
- **Not:** storing data or building big models. That lives in their databases and code.

## Technical questions they could ask
Glassdoor reports for ION ([UK interview page](https://www.glassdoor.co.uk/Interview/Ion-Asset-Architecture-Interview-Questions-E5366622.htm)) are few and anonymous. They mention lots of maths problems and brainteasers, a skills test in about a third of processes, "name as many currencies as you can", and being shown a list of dates and asked for patterns. Treat these as anecdotes.

**Excel (answer only with what you've really used)**
1. *How would you find duplicate trades in a list?* Conditional formatting, Highlight duplicates; or `=COUNTIF(A:A,A2)>1`; or Remove Duplicates on a copy, never the original.
2. *How would you check two lists match (our trades against the counterparty's)?* Look up each ID in the other list: `=VLOOKUP(A2,Other!A:C,3,FALSE)`, wrapped in `IFERROR(...,"Missing")`, then a column flagging any amount that differs. Then filter on the mismatches.
3. *VLOOKUP vs INDEX/MATCH vs XLOOKUP?* VLOOKUP only looks to the right and breaks if columns move. INDEX/MATCH and XLOOKUP can look left. Use FALSE / exact match for IDs. Only claim XLOOKUP if you've used it.
4. *Total stakes for one counterparty in one currency?* `=SUMIFS(Stake, Counterparty, "X", Currency, "EUR")`. COUNTIFS works the same way for counts.
5. *Summarise volume by market and day?* Pivot table: rows market, columns date, values sum of stake.
6. *Convert a time from New York to London?* Times are fractions of a day, so `=A2+5/24` (or `+TIME(5,0,0)`). Watch the clocks-change weeks, when the gap is 4 hours.
7. *Convert euros to pounds with a rate in one cell?* `=B2/$F$1`. The `$` keeps the rate cell fixed when you copy the formula down (an absolute reference).
8. *Flag unusual prices?* A column comparing each price with the average or the previous price, plus conditional formatting for anything outside a band. Or sort and look at the extremes.
9. *A number won't add up in a SUM. Why?* It's probably stored as text (left-aligned, green triangle). Fix with VALUE or Text to Columns.

**SQL (welcome, not required)**: be honest that you're learning. Know the shape: `SELECT market, SUM(stake) FROM trades WHERE trade_date = '2026-11-19' GROUP BY market;` and that a JOIN matches two tables on a shared ID, like VLOOKUP.

**Scenarios (likely for an operations role)**
- *At 2am you see a market still open after the match has finished. What do you do?* Check it against a second source, follow the procedure to stop or suspend it if there is one, escalate to the trader on call, record what happened and when. Don't guess.
- *A counterparty's report doesn't match ours.* Check our side first (timing, currency, duplicates), list the specific differences, then contact them with the evidence.
- *Two urgent problems at once.* Prioritise by money at risk and time left, tell the team which you're taking.

**Brainteasers reported on Glassdoor**
- A £100,000 house falls 30%. What rise gets it back? It's now £70,000 and needs £30,000: 30/70 = **42.9%**, not 30%.
- 8 coins, one heavier, a balance scale. Find it in **2 weighings**: weigh 3 against 3. If they balance, weigh the remaining 2. If not, take the heavy 3 and weigh 1 against 1: if they balance, it's the third.
- Name as many currencies as you can: GBP, EUR, USD, JPY, CHF, AUD, CAD, NZD, SEK, NOK, DKK, HKD, SGD, CNY, INR, ZAR, BRL, MXN, PLN, TRY, KRW.
- A list of dates: look for weekdays against weekends, gaps, duplicates, wrong formats (US vs UK), dates in the future, or a pattern like every 7 days.

## Numerical pop quiz (do tonight, no calculator)
Olivia: questions range from "working out" to quick fire. Cover the answers, then check.

**Quick fire**
1. 17 x 24
2. 15% of 340
3. 3/8 as a percentage
4. 1,000 divided by 8
5. Decimal odds 2.50 as an implied probability
6. Fractional odds 7/4 as decimal odds, then as a probability
7. £50 at decimal odds 3.20 wins. Total return and profit?
8. A 19:00 kick-off in New York. What time in London? (November)
9. A 20:45 kick-off in Madrid. What time in London?
10. 15:00 in Tokyo. What time in London?
11. Convert €200 to pounds at 1.15 euros to the pound
12. Convert $500 to pounds at 1.25 dollars to the pound
13. Spot the difference: `GBP 1,250.50` and `GBP 1,250.05`

**Working out**
14. Two independent events, probabilities 0.6 and 0.5. Probability both happen? At least one happens?
15. Probability of at least one head in 3 coin flips?
16. Probability two dice add up to 7?
17. A two-way market is priced 1.80 and 2.10. What's the overround?
18. You bet £10 at decimal odds 3.00 and the true probability is 40%. Expected value?
19. A team wins 60% of home games. Probability it wins its next two (assume independent)?
20. A three-way market: Home 2.00, Draw 3.50, Away 4.00. Is anything wrong?

> [!success]- Answers
> 1. 408
> 2. 51
> 3. 37.5%
> 4. 125
> 5. 1 / 2.5 = 40%
> 6. 7/4 + 1 = 2.75; 1 / 2.75 = 36.4%
> 7. Return £160, profit £110
> 8. 00:00 (midnight) London. New York is UTC-5 in November, UK is UTC+0
> 9. 19:45 (Madrid is one hour ahead)
> 10. 06:00 (Tokyo is nine hours ahead in November)
> 11. 200 / 1.15 = £173.91
> 12. 500 / 1.25 = £400
> 13. The pence are swapped: .50 against .05. A single character, as the spec says
> 14. Both: 0.6 x 0.5 = 0.30. At least one: 1 - (0.4 x 0.5) = 0.80
> 15. 1 - (1/2)^3 = 7/8 = 87.5%
> 16. 6/36 = 1/6, about 16.7%
> 17. 55.6% + 47.6% = 103.2%, so 3.2%
> 18. 0.4 x £20 profit - 0.6 x £10 = £8 - £6 = +£2
> 19. 0.6 x 0.6 = 36%
> 20. 50% + 28.6% + 25% = 103.6%. Nothing wrong: a normal 3.6% margin. (If it came out under 100%, that would be the error to flag)

**Tips:** say your working out loud. Sense-check every answer (a probability can't be over 100%; a currency conversion should move the right way). If you're unsure, say how you'd check it.

## Questions to ask them
- How do new starters learn the platform, and how long until you work on your own?
- What are the most common data errors the team catches?
- What does a typical shift look like for a Trading Assistant: how much is monitoring, and how much is project work?
- Which in-house tools would I learn first, and how much SQL does the operations team use day to day?
- What does progression look like from this role, for example into trading or data roles?
- How is performance measured in the first six months?

Back to [[CV and Interview Prep]] | [[APP-001 ION Asset Architecture - Trading Operations Assistant]]
