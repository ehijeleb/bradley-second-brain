---
type: project
area: learning
status: active
deadline: 
waiting_on: 
repo: 
---
# Spending Dashboard

> [!info] Snapshot
> **What:** a private Power BI dashboard on all of Bradley's spending, with personal spending and reselling kept apart: personal spending against the [[Finance]] budgets each month, reselling stock and costs, income, and savings (LISA) over time. Second Power BI build after [[Reselling Dashboard]].
> **Who:** Bradley. Private (built 25-11-2026).
> **Where things live:** personal spending and income in the month notes in `30 Personal/Finance/`, budgets and savings balances in [[Finance]], reselling in [[Stock]] and [[Reselling expenses]]. Export script `30 Personal/Finance/_scripts/export_spending.py` writes four CSVs to `30 Personal/Finance/Exports/`. The dashboard is `30 Personal/Finance/Exports/Power BI/Spending dashboard.pbip`.

## Next actions
- [ ] Open it on the laptop (see Opening it) and check the numbers below
- [ ] Log every purchase as it happens: personal ones in that month's Budget note, reselling stock in [[Stock]], other reselling costs in [[Reselling expenses]]
- [ ] Add a LISA balance to "Savings balances" in [[Finance]] after each payday
- [ ] Set a house deposit target (amount and date) so the Savings page can show progress towards it

## Opening it
1. In Obsidian, pull (Ctrl+P, **Obsidian Git: Pull**) and wait for "Pulled".
2. In the Terminal in `bradleys-brain`: `python "30 Personal/Finance/_scripts/export_spending.py"`
3. Double-click `30 Personal\Finance\Exports\Power BI\Spending dashboard.pbip`, then **Refresh** on the Home tab, then Ctrl+S.
4. After each new purchase: pull, export, Refresh.

## Checking it opened right
With the 25-11-2026 data and the Month slicer on **Nov 2026**: Income £2,481.19, Personal spend £496.45, Personal budget left £92.55 (budgets total £589), Reselling stock bought £5,593.82, Reselling costs £35.00. Personal vs stock page: Stock going back £907.68, Stock refunded £150.00. Savings page: LISA £790.00, growth £100.54 since 13-11-2026.

## What's in it
- **Overview:** cards for income, personal spend, personal budget left, stock bought and reselling costs; a Month slicer; personal spending against budget by category; a stacked column of personal and reselling spending by month; every payment in a table.
- **Personal vs stock:** cards for personal, stock bought, stock going back, stock refunded and reselling costs; a donut of where the money went; spending by category and by card or account; personal spending by group (Essentials, Lifestyle and so on).
- **Savings:** latest LISA balance, growth since the first check, and balances over time.

## Data
- **Spending.csv:** one row per payment out. Kind is `Personal`, `Reselling stock` or `Reselling costs`. Stock keeps its state, so returned stock (refunded) and returning stock (refund due) can be split out.
- **Income.csv:** payments in. Wages logged without an `amt` are left out (the export can't work them out); log wages with `amt`.
- **Budgets.csv:** the categories and monthly budgets from [[Finance]].
- **Savings.csv:** the "Savings balances" lines in [[Finance]].
- Personal spending is logged from 10-11-2026, so earlier months show income only.

## Measures (Spending table)
- `Personal spend`, `Stock bought`, `Reselling costs`: the total of Amount filtered by Kind.
- `Stock refunded` and `Stock going back`: stock by state (`returned`, `returning`).
- `Budget = SUM ( Budgets[Monthly budget] ) * MAX ( 1, [Months logged] )`, where Months logged counts months with any personal spending, so a single month compares against one month's budget.
- `LISA balance = CALCULATE ( LASTNONBLANKVALUE ( Savings[Date], SUM ( Savings[Balance] ) ), Savings[Account] = "Moneybox LISA" )`.

## Ideas
- House deposit progress once there's a target.
- LISA paid in this tax year against the £4,000 allowance (needs contributions logged, not just balances).
- Credit card page: what's on each card before the statement date.

## Decisions
- 25-11-2026: one dashboard for personal and reselling spending, split by Kind, as Bradley asked. Reselling stays in [[Stock]], not in the month notes, so nothing is counted twice.
- 25-11-2026: savings tracked as balance checks in [[Finance]], since LISA payments are transfers and not logged as spending.
- Rebuild scripts for both dashboards: `15 Learning and Portfolio/_scripts/` (they overwrite any changes made in Power BI, so only use them to start again).

## Status log
- 25-11-2026: hub created. Export script and Power BI project built (60 payments out, 5 in, 12 budgets, 2 savings balances). Not yet opened in Power BI.

## Links
- [[Finance]] · [[Stock]] · [[Reselling Dashboard]] · [[Skills Roadmap]]

> [!warning] No secrets
> Never paste passwords, account numbers, login details or API keys here. Note where they live instead.
