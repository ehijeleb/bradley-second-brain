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
> **Where things live:** data in [[Stock]] and [[Reselling expenses]]. Export script `20 Reselling/_scripts/export_reselling.py` writes `20 Reselling/Exports/Items.csv` and `Expenses.csv`. The dashboard is a Power BI project in `20 Reselling/Exports/Power BI/`: open `Reselling dashboard.pbip`.

## Next actions
- [ ] Open the dashboard on the laptop and check it against "Checking it opened right" below
- [ ] Read "How it's built" with the file open: find each step in Power Query, Model view and the measures
- [ ] Learning exercises: add conditional formatting to Days held (14+ amber, 30+ red), a drill-through from Category to a detail page, and a credit card page (Capital tied up by Paid with)
- [ ] Refresh routine after each Stock update (Step 6), then set the Power BI level in [[Skills Roadmap]]

## Open questions
- Built by Claude in a cloud session as text files (PBIP format) without Power BI, so it's never been opened. The report files pass Microsoft's published schemas; the model files couldn't be checked. If Power BI shows an error on opening, paste or screenshot it here and it can be fixed.

## Opening it
1. Install **Power BI Desktop** (free, Microsoft Store) if it isn't already.
2. Run the export script so the CSVs are up to date.
3. Double-click `20 Reselling/Exports/Power BI/Reselling dashboard.pbip`. If Power BI won't open it, turn on "Power BI Project (.pbip) save option", "Store semantic model using TMDL format" and "Store reports using enhanced metadata format (PBIR)" under File, Options and settings, Options, Preview features (if they're listed), then restart Power BI.
4. Click **Refresh** on the Home ribbon. The data loads from `C:\Users\hp\bradleys-brain\20 Reselling\Exports\`. If the vault is somewhere else: Transform data, Edit parameters, Exports folder (keep the trailing backslash).
5. Save with Ctrl+S. It stays as a project folder (no .pbix). Obsidian Git syncs it; the data cache and local settings are ignored.

## Checking it opened right
With the 24-11-2026 data, the Overview cards should read: Net profit **-£9.98** (£25.02 profit less the £35 House of Resell membership), Capital tied up **£4,096.17** (12 items in stock or listed), Refunds due **£1,057.68** (14 items going back), Items held **12**, Sell-through **14.3%** (2 of 14). If a number differs, check the export first.

## Data
Run `python "20 Reselling/_scripts/export_reselling.py"` from the vault folder whenever [[Stock]] changes. It prints any lines to check.

**Items.csv** (one row per Stock line): Item ID, Item, Category, Shop, Paid with, State, Bought, Cost, Sold, Price, Fees, Postage, Platform, Profit, Margin, Days held.
- Category comes from keyword rules at the top of the script (Gaming, LEGO, Trading cards, Music merch, Fashion, Food and drink). New kinds of item export as Other until a rule is added.
- Profit = Price - Cost - Fees - Postage, sold items only. Margin = Profit / Cost.
- Days held = sold date (or today, if unsold) minus bought date.
- Order and confirmation numbers are stripped from Shop.

**Expenses.csv**: Date, Expense, Type, Amount.

At 24-11-2026: 28 items, 2 sold (£25.02 profit), 1 expense (£35).

## How it's built
All of this is already in the file. Read each step with Power BI open to learn what it does, and try rebuilding a measure or visual yourself.

### Step 1: loading the data
1. Items and Expenses load from the CSVs through a text parameter, `Exports folder` (Transform data shows the steps).
2. Power Query steps: read the CSV, promote headers, turn blanks into nulls, set types. Column types: Bought and Sold = Date; Cost, Price, Fees, Postage, Profit = Fixed decimal number; Margin = Percentage; Days held = Whole number. Expenses: Date = Date, Amount = Fixed decimal number.

*Learning point:* Power Query is the cleaning step (like the data prep for [[Money Buys Points]]). Every change is recorded under Applied Steps and replays on refresh.

### Step 2: date table and relationships
1. Calendar is a calculated table (Modelling, New table):
```
Calendar =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2026, 11, 1 ), DATE ( 2027, 12, 31 ) ),
    "Month", FORMAT ( [Date], "mmm yyyy" ),
    "Month number", YEAR ( [Date] ) * 100 + MONTH ( [Date] ),
    "Week starting", [Date] - WEEKDAY ( [Date], 2 ) + 1
)
```
2. Month is sorted by Month number, and the table is marked as a date table.
3. Model view: `Calendar[Date]` links to `Items[Bought]`, `Items[Sold]` and `Expenses[Date]`. Power BI only allows one active link between two tables, so the Sold one shows as a dotted (inactive) line. That's intended: the measures switch it on when they need it.

*Learning point:* this is a star schema, one date table filtering two fact tables. It's the most common Power BI interview topic.

### Step 3: measures
All in the Items table.
```
Spent = SUM ( Items[Cost] )
Items bought = COUNTROWS ( Items )
Items held = CALCULATE ( COUNTROWS ( Items ), Items[State] IN { "in stock", "listed" } )
Capital tied up = CALCULATE ( SUM ( Items[Cost] ), Items[State] IN { "in stock", "listed" } )
Refunds due = CALCULATE ( SUM ( Items[Cost] ), Items[State] = "returning" )
Held over 30 days = CALCULATE ( [Items held], Items[Days held] > 30 )

Items sold = CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold", USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )
Revenue = CALCULATE ( SUM ( Items[Price] ), USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )
Gross profit = CALCULATE ( SUM ( Items[Profit] ), USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )
Cost of sold = CALCULATE ( SUM ( Items[Cost] ), Items[State] = "sold", USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )
Margin % = DIVIDE ( [Gross profit], [Cost of sold] )
Avg days to sell = CALCULATE ( AVERAGE ( Items[Days held] ), Items[State] = "sold" )

Other costs = SUM ( Expenses[Amount] )
Net profit = [Gross profit] - [Other costs]
Sell-through % = DIVIDE ( CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold" ), CALCULATE ( COUNTROWS ( Items ), Items[State] IN { "in stock", "listed", "sold" } ) )
```
Spent, Capital tied up, Refunds due, Revenue, Gross profit, Other costs and Net profit are formatted as £ with 2 decimals; Margin % and Sell-through % as percentages.

*Learning points:* `CALCULATE` changes the filter a measure runs under, like a Tableau calculation with a filter built in. `USERELATIONSHIP` uses the inactive Sold link, so sales land in the month they sold, not the month bought. `DIVIDE` avoids divide-by-zero errors. Try writing each measure yourself before looking.

### Step 4: Overview page
1. Five **Card** visuals: Net profit, Capital tied up, Refunds due, Items held, Sell-through %.
2. **Stacked bar**: Category on the axis, Spent as the value, State in the legend. Shows where the money is sitting.
3. **Clustered column**: Date[Month] on the axis, Gross profit and Expenses as values.
4. **Table**: Item ID, Item, Shop, Paid with, State, Cost, Days held, filtered to in stock, listed or returning. Exercise: add conditional formatting on Days held (Background colour, rules: 14+ amber, 30+ red), to match the weekly review's "held over 30 days".
5. **Slicers**: Category and Paid with.

### Step 5: Sales page
1. **Bar**: Platform by Gross profit, with Margin % in the tooltip.
2. **Scatter**: Cost on X, Profit on Y, Item ID in Values, Category as legend. Shows whether bigger buys earn bigger profits.
3. **Table**: sold items with Bought, Sold, Days held, Price, Profit, Margin.
4. Exercise: add a **drill-through**: right-click a category on the Overview bar to jump to a page filtered to that category.

This page fills up once the PS5 Pros, Switches and X-Mansions sell.

### Step 6: refresh routine
1. After updating [[Stock]]: run the export script, open the .pbip, Home, **Refresh**.
2. Power BI remembers the file path. If the vault moves, use Transform data, Data source settings, Change source.
3. Note in [[Skills Roadmap]] what you learnt and set the Power BI level.

## Ideas
- Credit card view: Capital tied up by Paid with, to check what needs paying off before the statement.
- Return deadlines on the stock table, once returns are recorded.
- Expected profit on held stock, using a target price per item.
- Once there are 15 to 20 sales, an anonymised version could still go in the portfolio.

## Decisions
- 24-11-2026: private dashboard, built in Power BI rather than Tableau, to learn Power BI.
- 24-11-2026: Bradley asked Claude to build it; the build steps stay as a guide to reading it.
- 24-11-2026: data goes through a CSV export rather than Power BI reading the Markdown directly, so [[Stock]] stays the main copy and the CSVs are easy to check.

## Status log
- 24-11-2026: hub created. Export script written and first export run (28 items, 1 expense).
- 24-11-2026: returning and returned states added to [[Stock]] (Reselling chat); export now includes a Refunded date. Dashboard built as a Power BI project in `20 Reselling/Exports/Power BI/` (Overview and Sales pages). Not yet opened in Power BI.

## Links
- [[Stock]] · [[Reselling]] · [[Reselling expenses]] · [[Skills Roadmap]] · [[Portfolio Projects]]

> [!warning] No secrets
> Never paste passwords, account numbers, login details or API keys here. Note where they live instead.
