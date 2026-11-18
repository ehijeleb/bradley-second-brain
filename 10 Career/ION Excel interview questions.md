---
type: reference
area: career
---
# ION Excel interview questions

Built from what Olivia said on 18-11-2026 and the job description.

**What Olivia said about Excel**

- Drish will ask "a couple of questions on Excel, just to get an idea of how much experience you have", before deciding on the face-to-face round.
- They want to know what you can do with Excel functions, "particularly formulas".
- The face-to-face round has a task: rearrange a dataset using just formulas.
- They may ask how you'd sort thousands of dates, and what currencies you know.
- If you haven't done something: "I haven't had that before, but I'd like to learn it."

**What the job description says:** good Excel, attention to detail ("a single character can make all the difference"), spotting inconsistencies and errors, time zones and currencies, probabilities, picking up new applications quickly.

> This is a phone or video call, so you'll be **explaining** formulas, not typing them. Each answer below is how to say it out loud. Only claim what you've practised in the [[ION Excel functions practice.xlsx|ION Excel functions practice]] workbook or used before.

**Sections:** [[#1. Your experience|1. Experience]] · [[#2. The basics|2. Basics]] · [[#3. Arranging data with formulas (Olivia's face-to-face task)|3. Arranging data]] · [[#4. Lookups|4. Lookups]] · [[#5. Conditions and totals|5. Conditions]] · [[#6. Spotting errors and inconsistencies|6. Errors]] · [[#7. Dates and times|7. Dates]] · [[#8. Currencies|8. Currencies]] · [[#9. Odds and probability in Excel|9. Odds]] · [[#10. Scenarios|10. Scenarios]] · [[#11. If you don't know|11. If you don't know]]

---

## 1. Your experience

**How would you rate your Excel out of 10?**
"About a 7. I'm confident with lookups, conditional totals like SUMIFS, pivot tables and charts, and I've used them on real data in my internship and degree. I'm still building up the newer functions like XLOOKUP and the dynamic array ones." *(Only say 7 if you've done tonight's practice. Otherwise say 6.)*

**Tell me about the most useful thing you've done in Excel.**
"In my finance internship I reconciled over 200 transactions a week. I used VLOOKUP to match records between two lists and pivot tables to total them, so any discrepancy stood out straight away."

**Which functions do you use most?**
"VLOOKUP and INDEX/MATCH for finding things, SUMIFS and COUNTIFS for totals with conditions, IF and IFERROR for flagging problems, and pivot tables for summaries."

**Tell me about a time you used Excel to analyse data.**
Pick one: the match report (1,000+ events into a pivot-table dashboard), the share price project (built test data with RAND and SIN, checked trends with charts), or the business simulation (150+ survey responses).

**Have you used macros, VBA or Power Query?**
Be honest. If not: "Not yet. I've done my automation in formulas so far, but I know they're used for repetitive tasks and I'd like to learn them."

**What other tools do you use with data?**
"Python, R, Minitab and Statistica from my degree, and I taught myself Tableau and published two dashboards. SQL I'm learning now."

---

## 2. The basics

**What's the difference between a formula and a function?**
"A formula is anything you type that starts with an equals sign. A function is a ready-made calculation inside it, like SUM or VLOOKUP. So =SUM(A1:A10)*2 is a formula that uses the SUM function."

**What's the difference between A1 and $A$1?**
"A1 moves when you copy the formula to another cell. $A$1 stays fixed. You use it for things like an exchange rate in one cell that every row needs."

**What does a #N/A error mean? #VALUE? #DIV/0?**
"#N/A means a lookup didn't find what it was looking for. #VALUE means the wrong type of data, often text where a number should be. #DIV/0 means dividing by zero or by a blank cell."

**How do you stop errors showing?**
"Wrap the formula in IFERROR, like =IFERROR(VLOOKUP(...), "Missing"). But I'd want to know why it's erroring first, because an error is often telling you something is wrong with the data."

**What's a pivot table and when would you use one?**
"It summarises a big table without formulas: totals, counts or averages by category. For example, total stakes by counterparty and day. It's quick for spotting anything unusual."

**What's an Excel Table (Ctrl+T) and why use one?**
"It turns a range into a table that grows automatically when you add rows, so formulas and pivot tables pick up new data. It also adds filters and banded rows." *(Only if you've used it. It's a good thing to try tonight.)*

---

## 3. Arranging data with formulas (Olivia's face-to-face task)

**How would you sort a dataset using only formulas?**
"In newer Excel, SORT does it in one go: =SORT(range, column, -1) for largest first. In older Excel I'd use LARGE or SMALL to pull the values out in order, then INDEX with MATCH to bring back the rest of each row."

**Why sort with a formula instead of the Sort button?**
"The original data stays untouched, and the sorted version updates itself when the data changes. In operations that matters, because the data changes all the time."

**How would you show only the rows you want, using formulas?**
"FILTER in newer Excel, for example =FILTER(trades, currency="EUR"). In older Excel, a helper column that numbers the matching rows, then INDEX to pull them out one by one."

**How would you get a list of each counterparty once?**
"=UNIQUE(range). Or in older Excel, a pivot table, or COUNTIF to flag the first time each name appears."

**How would you find the top 5 trades?**
"=LARGE(stakes, 1) to 5 for the values, then INDEX/MATCH to get the trade IDs. Or SORT and TAKE in newer Excel."

**How would you rank values?**
"=RANK(value, range). 1 is the biggest by default."

**How would you split a code like T1001-EUR into two columns?**
"LEFT for the start and RIGHT for the end. If the lengths vary, use FIND to locate the dash: =LEFT(A2, FIND("-", A2)-1)."

**How would you join columns together?**
"With an ampersand, =A2 & " " & B2, or CONCAT."

**How would you turn a long list into a grid, like stakes by counterparty and day?**
"Put counterparties down the side and days across the top, then SUMIFS in each cell. Or a pivot table."

**How would you reorder or pick out columns using formulas?**
"INDEX with a column number pulls any column. In newer Excel, CHOOSECOLS picks the columns you want in the order you want."

**What can go wrong with INDEX/MATCH sorting?**
"If two values are the same, MATCH finds the first one twice. You fix that by adding a tiny tiebreaker, or by using SORT, which handles it."

---

## 4. Lookups

**What's the difference between VLOOKUP and INDEX/MATCH?**
"VLOOKUP looks for a value in the first column and returns something to its right. INDEX/MATCH can look left as well, and it doesn't break if someone inserts a column. XLOOKUP in newer Excel does both more simply."

**Why put FALSE at the end of a VLOOKUP?**
"FALSE means exact match. Without it, Excel can return the nearest value, which with trade IDs gives you the wrong trade without any error. A single character like that can make all the difference."

**A VLOOKUP returns #N/A but you can see the value is there. Why?**
"Usually extra spaces, or a number stored as text in one list and as a number in the other. TRIM fixes the spaces, and VALUE or Text to Columns fixes the numbers."

**How would you look something up using two conditions?**
"The simplest way is a helper column that joins the two, like trade ID & date, and look up on that. In newer Excel, XLOOKUP or FILTER can take both conditions."

**How would you look up a value in a grid, by row and column?**
"INDEX with two MATCHes: one MATCH for the row and one for the column."

---

## 5. Conditions and totals

**How would you total stakes for one counterparty in one currency?**
"=SUMIFS(stake, counterparty, "Exchange A", currency, "EUR"). SUMIFS adds up only the rows that meet every condition."

**And count them?**
"COUNTIFS, same idea."

**How would you flag stakes over £1,000?**
"=IF(stake>1000, "Check", ""), then filter on Check. Or conditional formatting to colour them."

**How would you check two things at once?**
"IF with AND, for example =IF(AND(stake>1000, currency="USD"), "Check", "")."

**What's the difference between COUNT, COUNTA and COUNTBLANK?**
"COUNT counts numbers, COUNTA counts any non-empty cell, COUNTBLANK counts empty ones. COUNTBLANK is useful for finding missing data."

---

## 6. Spotting errors and inconsistencies

The job is spotting inconsistencies, errors and unusual behaviour, so expect these.

**How would you find duplicate trades?**
"=COUNTIF(IDs, A2)>1 flags any ID that appears more than once. If a duplicate means the same trade on the same day, use COUNTIFS across both columns. Conditional formatting can highlight them too."

**How would you check our list of trades matches a counterparty's?**
"Look up each of our trade IDs in their list. Anything that comes back #N/A is missing from theirs. Then do it the other way round. For trades in both, compare the amounts and flag any differences. Then filter so you only see the problems."

**How would you find missing data?**
"COUNTBLANK on each column, or filter for blanks."

**How would you spot numbers stored as text?**
"They sit on the left of the cell, often with a green triangle, and they don't add up in a SUM. ISNUMBER returns FALSE for them. VALUE converts them."

**How would you clean messy text so lookups work?**
"TRIM removes extra spaces, and UPPER or PROPER makes the case consistent."

**How would you spot unusual values?**
"Sort or use LARGE and SMALL to look at the extremes. Compare each value to the average, or to the same counterparty's usual stake. Conditional formatting colours anything outside a range."

**How would you stop people typing wrong data in the first place?**
"Data validation: a drop-down list of allowed values, or a rule like a stake must be over zero."

**You've built a formula. How do you know it's right?**
"Check a few rows by hand, check the total against another source, and test an edge case like a blank or a zero."

---

## 7. Dates and times

Olivia said they may ask how you'd sort thousands of dates.

**How would you sort thousands of dates?**
"First I'd check they're real dates, because Excel stores dates as numbers and text that only looks like a date won't sort properly. Then check the format, because 03/04 is 3 April here but 4 March in the US. Then sort, either with the Sort button or =SORT(range). After that I'd check for duplicates, gaps and anything impossible, like dates in the future."

**How can you tell a date is stored as text?**
"It sits on the left of the cell, ISNUMBER returns FALSE, and it won't change when you change the date format. DATEVALUE or Text to Columns converts it."

**How would you find gaps in a list of dates?**
"Sort them, then subtract each date from the next one. Anything bigger than expected is a gap. A 0 is a duplicate."

**How would you find weekend dates?**
"=WEEKDAY(date, 2) gives Monday as 1 and Sunday as 7, so anything over 5 is a weekend."

**How would you group trades by month?**
"MONTH and YEAR in helper columns, then SUMIFS or a pivot table. Pivot tables can group dates by month themselves."

**How would you count working days between two dates?**
"NETWORKDAYS(start, end)."

**How would you convert a time from New York to London?**
"Excel stores times as fractions of a day, so add 5 hours as 5/24, or use TIME(5,0,0). The gap changes for a few weeks a year when the clocks change on different dates, so I'd keep the offset in its own cell rather than typing 5 into every formula."

**How would you work out how long something took?**
"End time minus start time, formatted as time. If it crosses midnight, add 1."

---

## 8. Currencies

**How would you convert a column of euros into pounds?**
"Put the exchange rate in one cell, then divide each amount by it, with dollar signs so the rate cell stays fixed when I fill down. If there are several currencies, I'd keep a small rates table and look up each row's rate with VLOOKUP."

**Why not type the rate into the formula?**
"If the rate changes, you'd have to change every formula and you'd probably miss one. One cell is one place to update."

**How would you total everything in pounds when trades are in three currencies?**
"Add a column that converts each trade into pounds, then SUM it. Or SUMIFS by currency, divide each by its rate, and add them up."

**How would you round to 2 decimal places?**
"=ROUND(value, 2). Formatting only changes how it looks; ROUND changes the actual number, which matters when you're comparing totals."

**What currencies do you know?**
GBP, EUR, USD, JPY, CHF, AUD, CAD, NZD, SEK, NOK, DKK, HKD, SGD, CNY, INR, KRW, ZAR, BRL, MXN, PLN, TRY.

---

## 9. Odds and probability in Excel

**How would you turn decimal odds into a probability?**
"=1/odds, formatted as a percentage. Odds of 2.50 give 40%."

**How would you check a market's prices add up sensibly?**
"Convert each outcome's odds to a probability and SUM them. A bit over 100% is the bookmaker's margin. Under 100% means something's wrong with the prices."

**How would you work out profit if a bet wins?**
"=stake*(odds-1). Wrapped in IF so it only counts if the result is Won."

**How would you work out expected value?**
"Probability of winning times the profit, minus probability of losing times the stake. In Excel that's one formula referring to those cells."

---

## 10. Scenarios

**You're given a spreadsheet of 10,000 trades and asked to check it. What do you do?**
"Make it a Table so I can filter. Check the totals and row count match what I expect. Then look for blanks, duplicates, text in number columns, dates that aren't real dates, and extreme values. Flag problems in a helper column so I can filter to them, and check the original file isn't changed."

**Excel is slow with a huge file. What would you do?**
"Avoid formulas over whole columns where I can, replace finished formulas with values in a copy, and use a pivot table instead of lots of SUMIFS. For really big data, that's where SQL or a database comes in."

**Someone's spreadsheet gives a different total to yours. How do you find out why?**
"Compare the row counts first, then subtotal by category to see where they split. Usually it's a missing row, a duplicate, or a filter left on."

---

## 11. If you don't know

Olivia's advice: be honest.

- "I haven't used that yet, but I'd like to learn it. Here's how I'd go about it..."
- "I'd normally check the exact syntax, but the idea is..."
- Explain the logic, even if you can't remember the function name. They want to see how you think.
- Never pretend. Excel is easy to test, and the face-to-face round will show exactly what you can do.

**Practise these in the workbook tonight:** VLOOKUP, INDEX/MATCH, SUMIFS, COUNTIF duplicates, LARGE + INDEX/MATCH sorting, the Dates sheet. If you have Microsoft 365, try SORT, FILTER and UNIQUE too.
