---
type: project
area: learning
status: active
deadline: 
waiting_on: 
repo: 
---
# Reselling Dashboard

> [!info] Snapshot
> **What:** a private Power BI dashboard on Bradley's reselling: money spent, capital tied up in stock, profit by month, category and platform, and how long items sit. Also Bradley's first Power BI build, to move Power BI off "none" on [[Skills Roadmap]].
> **Who:** Bradley. Private, not for the portfolio (decided 24-11-2026).
> **Where things live:** data in [[Stock]] and [[Reselling expenses]]. Export script `20 Reselling/_scripts/export_reselling.py` writes `20 Reselling/Exports/Items.csv` and `Expenses.csv`. Save the Power BI file as `20 Reselling/Exports/Reselling dashboard.pbix`.

## Next actions
Work through the build steps below in order; each is about 20 to 40 minutes.
- [ ] Step 1: install Power BI Desktop and load the data
- [ ] Step 2: date table and relationships
- [ ] Step 3: measures
- [ ] Step 4: Overview page
- [ ] Step 5: Sales page
- [ ] Step 6: refresh routine, then write up what was learnt in [[Skills Roadmap]]
- [ ] Ask the Reselling chat to record returns in [[Stock]] (see Open questions)

## Open questions
- Returns aren't recorded in [[Stock]]: the H&M dress (returned 22-11-2026), the Taylor Swift items and the Red Bull calendars still show as `in stock` or `listed`, so capital tied up is overstated by about £1,330. Suggest new states `returning` and `returned` (and maybe `[refunded:: DD-MM-YYYY]`). That changes the Reselling format and its Dataview script, so do it in the Reselling chat. The export passes any state through, so the dashboard can filter them once they exist.

## Data
Run `python "20 Reselling/_scripts/export_reselling.py"` from the vault folder whenever [[Stock]] changes. It prints any lines to check.

**Items.csv** (one row per Stock line): Item ID, Item, Category, Shop, Paid with, State, Bought, Cost, Sold, Price, Fees, Postage, Platform, Profit, Margin, Days held.
- Category comes from keyword rules at the top of the script (Gaming, LEGO, Trading cards, Music merch, Fashion, Food and drink). New kinds of item export as Other until a rule is added.
- Profit = Price - Cost - Fees - Postage, sold items only. Margin = Profit / Cost.
- Days held = sold date (or today, if unsold) minus bought date.
- Order and confirmation numbers are stripped from Shop.

**Expenses.csv**: Date, Expense, Type, Amount.

At 24-11-2026: 28 items, 2 sold (£25.02 profit), 1 expense (£35).

## Build steps

### Step 1: install and load
1. Install **Power BI Desktop** (free) from the Microsoft Store on the laptop.
2. Run the export script.
3. Power BI: Home, Get data, Text/CSV, pick `Items.csv`, then **Transform Data** (this opens Power Query).
4. In Power Query, check each column's type icon: Bought and Sold = Date; Cost, Price, Fees, Postage, Profit = Fixed decimal number; Margin = Percentage; Days held = Whole number. Close and Apply.
5. Same again for `Expenses.csv` (Date = Date, Amount = Fixed decimal number).
6. Save as `Reselling dashboard.pbix` in `20 Reselling/Exports/`.

*Learning point:* Power Query is the cleaning step (like the data prep for [[Money Buys Points]]). Every change is recorded under Applied Steps and replays on refresh.

### Step 2: date table and relationships
1. Modelling, New table:
```
Date =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2026, 11, 1 ), DATE ( 2027, 12, 31 ) ),
    "Month", FORMAT ( [Date], "mmm yyyy" ),
    "Month number", YEAR ( [Date] ) * 100 + MONTH ( [Date] ),
    "Week starting", [Date] - WEEKDAY ( [Date], 2 ) + 1
)
```
2. Select the Month column, Column tools, Sort by column: Month number. Then Table tools, **Mark as date table**, using Date.
3. Model view: drag `Date[Date]` onto `Items[Bought]`, `Items[Sold]` and `Expenses[Date]`. Power BI only allows one active link between two tables, so the Sold one shows as a dotted (inactive) line. That's intended: the measures switch it on when they need it.

*Learning point:* this is a star schema, one date table filtering two fact tables. It's the most common Power BI interview topic.

### Step 3: measures
Home, New measure, one at a time. Put them in Items (or make an empty "Measures" table).
```
Spent = SUM ( Items[Cost] )
Items bought = COUNTROWS ( Items )
Items held = CALCULATE ( COUNTROWS ( Items ), Items[State] IN { "in stock", "listed" } )
Capital tied up = CALCULATE ( SUM ( Items[Cost] ), Items[State] IN { "in stock", "listed" } )
Held over 30 days = CALCULATE ( [Items held], Items[Days held] > 30 )

Items sold = CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold", USERELATIONSHIP ( 'Date'[Date], Items[Sold] ) )
Revenue = CALCULATE ( SUM ( Items[Price] ), USERELATIONSHIP ( 'Date'[Date], Items[Sold] ) )
Gross profit = CALCULATE ( SUM ( Items[Profit] ), USERELATIONSHIP ( 'Date'[Date], Items[Sold] ) )
Cost of sold = CALCULATE ( SUM ( Items[Cost] ), Items[State] = "sold", USERELATIONSHIP ( 'Date'[Date], Items[Sold] ) )
Margin % = DIVIDE ( [Gross profit], [Cost of sold] )
Avg days to sell = CALCULATE ( AVERAGE ( Items[Days held] ), Items[State] = "sold" )

Expenses = SUM ( Expenses[Amount] )
Net profit = [Gross profit] - [Expenses]
Sell-through % = DIVIDE ( CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold" ), [Items bought] )
```
Format Spent, Capital tied up, Revenue, Gross profit, Expenses and Net profit as £ with 2 decimals; Margin % and Sell-through % as percentages.

*Learning points:* `CALCULATE` changes the filter a measure runs under, like a Tableau calculation with a filter built in. `USERELATIONSHIP` uses the inactive Sold link, so sales land in the month they sold, not the month bought. `DIVIDE` avoids divide-by-zero errors. Try writing each measure yourself before looking.

### Step 4: Overview page
1. Four **Card** visuals: Net profit, Capital tied up, Items held, Sell-through %.
2. **Stacked bar**: Category on the axis, Spent as the value, State in the legend. Shows where the money is sitting.
3. **Clustered column**: Date[Month] on the axis, Gross profit and Expenses as values.
4. **Table**: Item, Shop, Cost, Days held, State, filtered to State is in stock or listed. Conditional formatting on Days held (Background colour, rules: 14+ amber, 30+ red), to match the weekly review's "held over 30 days".
5. **Slicers**: Category and Paid with.

### Step 5: Sales page
1. **Bar**: Platform by Gross profit, with Margin % in the tooltip.
2. **Scatter**: Cost on X, Profit on Y, Item ID in Values, Category as legend. Shows whether bigger buys earn bigger profits.
3. **Table**: sold items with Bought, Sold, Days held, Price, Profit, Margin.
4. Try a **drill-through**: right-click a category on the Overview bar to jump to a page filtered to that category.

This page fills up once the PS5 Pros, Switches and X-Mansions sell.

### Step 6: refresh routine
1. After updating [[Stock]]: run the export script, open the .pbix, Home, **Refresh**.
2. Power BI remembers the file path. If the vault moves, use Transform data, Data source settings, Change source.
3. Note in [[Skills Roadmap]] what you learnt and set the Power BI level.

## Ideas
- Credit card view: Capital tied up by Paid with, to check what needs paying off before the statement.
- Return deadlines on the stock table, once returns are recorded.
- Expected profit on held stock, using a target price per item.
- Once there are 15 to 20 sales, an anonymised version could still go in the portfolio.

## Decisions
- 24-11-2026: private dashboard, built in Power BI rather than Tableau, to learn Power BI.
- 24-11-2026: data goes through a CSV export rather than Power BI reading the Markdown directly, so [[Stock]] stays the main copy and the CSVs are easy to check.

## Status log
- 24-11-2026: hub created. Export script written and first export run (28 items, 1 expense).

## Links
- [[Stock]] · [[Reselling]] · [[Reselling expenses]] · [[Skills Roadmap]] · [[Portfolio Projects]]

> [!warning] No secrets
> Never paste passwords, account numbers, login details or API keys here. Note where they live instead.
