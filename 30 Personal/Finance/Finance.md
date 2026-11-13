---
type: area
area: personal
status: active
currency: "£"
locale: en-GB
hourly_wage: 
---
# Finance

> [!info] How this works
> One note per month in this folder (`2026-10 Budget`, `2026-11 Budget`, ...). Log one line per purchase and per payment in, and each month's summary works itself out from the settings below. For a new month, create a note here named `YYYY-MM Budget` and insert the **Finance month** template.
> Needs the **Dataview** community plugin with **Enable JavaScript queries** turned on. The calculations live in `_scripts/finance.js`.
> Amounts are fine here (the vault's GitHub repository is private), but never put account numbers, sort codes, card numbers or logins in the vault.

> [!note] Starts blank
> The categories below have no budgets yet and there's no wage split. Set your own, or ask Claude to set them up from a budget spreadsheet or bank export.

## Year overview
```dataviewjs
await dv.view("30 Personal/Finance/_scripts/finance", { view: "year" })
```

## How to log
A purchase, under **Expenses** in the month note. The category must match one below exactly; `from` (optional) is the account it came out of:
```
- 25-10-2026 Supermarket [cat:: Groceries] [amt:: 23.49] [from:: Current account]
```
Money in, under **Income**. Use `Wages` or `Other` (or add your own type); `amt` is the amount that arrived:
```
- 25-10-2026 Employer [income:: Wages] [amt:: 1500.00]
```
- `hours`, `gross` and `deductions` are optional on wages. Leave `amt` out and it's worked out as hours × hourly wage − deductions (set `hourly_wage` at the top).
- **Don't log transfers** between your own accounts. They aren't spending.
- A mistyped line (unknown category, missing amount) shows up under "Check these lines" in that month's summary.

## Settings
Edit these and every month updates. Keep the `[key:: value]` parts as they are; anything after them is a note.

### Accounts and where your wages go
Give an account a `pct` to split your wages between accounts; the percentages must add up to 100. Accounts without a `pct` are just places money is paid from.
- [account:: Current account]

### Categories and monthly budgets
A budget of 0 means no monthly budget yet (or one-off costs).
- [category:: Rent & Bills] [group:: Essentials] [budget:: 0]
- [category:: Groceries] [group:: Essentials] [budget:: 0]
- [category:: Transport] [group:: Essentials] [budget:: 0]
- [category:: Phone & Subscriptions] [group:: Essentials] [budget:: 0]
- [category:: Health & Fitness] [group:: Health] [budget:: 0]
- [category:: Eating Out] [group:: Lifestyle] [budget:: 0]
- [category:: Going Out] [group:: Lifestyle] [budget:: 0]
- [category:: Shopping] [group:: Lifestyle] [budget:: 0]
- [category:: Holiday & Travel] [group:: Goals] [budget:: 0]
- [category:: Gifts] [group:: Goals] [budget:: 0]
- [category:: Other] [group:: Other] [budget:: 0]

## Recurring
- 

## Goals
- 

## Status log
- 13-11-2026: Finance set up, blank
