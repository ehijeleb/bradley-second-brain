---
type: area
area: personal
status: active
currency: "£"
locale: en-GB
hourly_wage: 14.96
---
# Finance

> [!info] How this works
> One note per month in this folder (`2026-10 Budget`, `2026-11 Budget`, ...). Log one line per purchase and per payment in, and each month's summary works itself out from the settings below. For a new month, create a note here named `YYYY-MM Budget` and insert the **Finance month** template.
> Needs the **Dataview** community plugin with **Enable JavaScript queries** turned on. The calculations live in `_scripts/finance.js`.
> Amounts are fine here (the vault's GitHub repository is private), but never put account numbers, sort codes, card numbers or logins in the vault.

> [!info] Snapshot (13-11-2026)
> **Pay:** [[Bershka]] (employer ITX UK Limited), £14.96 an hour from September 2026 (payslips; Bradley rounds it to £15), plus £1.50 at weekends. 40 hours a week. Pay period is the calendar month, paid on the 10th of the next month into NatWest.
> **Take-home:** gross has been £2,450 to £3,230 a month (August to October). Net was £2,060 to £2,620 on the old Month 1 tax code; it should be slightly higher from December on the correct code 1257L. Year-to-date 2026-27 gross £9,415.64, tax £1,090.40, NI £435.96.
> **No deductions yet** for student loan or workplace pension (see Tax).
> **Balances (13-11-2026):** NatWest current £4,270.00. Moneybox LISA £689.46. NatWest credit card £95.90 in credit (limit £3,704.10).
> **Owe:** £2,800 to university accommodation. **Owed to me:** £35 Dart Charge from Bershka; possible £800 tax refund.

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
- [account:: NatWest current] [pct:: 100]
- [account:: NatWest credit card] used for petrol and fast food to build credit history, paid off from NatWest current
- [account:: Moneybox LISA] savings only: £50 a week goes in automatically (a transfer, so not logged as spending)

### Categories and monthly budgets
A budget of 0 means no monthly budget yet (or one-off costs).
- [category:: Rent & Bills] [group:: Essentials] [budget:: 150] rent to parents
- [category:: Groceries] [group:: Essentials] [budget:: 20] occasional top-ups only
- [category:: Transport] [group:: Essentials] [budget:: 120] petrol about twice a month, on the credit card
- [category:: Phone & Subscriptions] [group:: Essentials] [budget:: 39] phone
- [category:: Health & Fitness] [group:: Health] [budget:: 50] gym, rising to £50; cancelling and switching
- [category:: Eating Out] [group:: Lifestyle] [budget:: 130] food at work when not meal prepping (about £10 a day) and fast food, mostly on the credit card
- [category:: Going Out] [group:: Lifestyle] [budget:: 50] estimate, adjust
- [category:: Shopping] [group:: Lifestyle] [budget:: 30] barely shops
- [category:: Holiday & Travel] [group:: Goals] [budget:: 0] one-off; see Goals
- [category:: Gifts] [group:: Goals] [budget:: 0] one-off; Christmas in December
- [category:: Debt repayment] [group:: Goals] [budget:: 0] university accommodation instalments
- [category:: Other] [group:: Other] [budget:: 0]

## Recurring
- 10th of each month: wages in from [[Bershka]] for the previous calendar month.
- Weekly: £50 NatWest to Moneybox LISA (transfer, don't log).
- Monthly: rent to parents £150 (day not recorded).
- Monthly: phone £39 (day not recorded).
- Monthly: gym, rising to £50 (cancelling; find a new membership).
- Monthly from 13-11-2026: [[House of Resell]] £35. Logged in [[Reselling expenses]], so not logged here too.
- Monthly: credit card spending about £250 (petrol and fast food). Log each purchase with `[from:: NatWest credit card]`; paying the card off is a transfer, don't log it.

## Debts and money owed
- **University accommodation: £2,800 owed.** Plan: pay in instalments on the Amex card when it arrives, depending on the limit. Things to weigh before deciding: interest if the Amex isn't cleared in full each month, and how much of the limit it uses (high use can lower a credit score). The NatWest balance could cover it outright. Not financial advice: check the terms of the Amex and the accommodation's payment options.
- **Owed to me: £35** Dart Charge from Bershka (Bluewater trip). Chase if not in the next payslip.
- **Tax refund: about £884.60** overpaid, expected back automatically on the December payslip. See Tax below.

## Tax
Imported 13-11-2026 from Bradley's tax refund chat. Sensitive details (NI number, bank details, HMRC login) stay on payslips and in the HMRC app, not here.
- **Tax year 2026-27.** Only employment: ITX UK Limited (Bershka), started 20-07-2026. No other taxable income since 06-04-2026.
- **Why overpaid:** HMRC put Bradley on 1255L Month 1 (non-cumulative) from 11-08-2026, so the allowance for April to July was never used. The September, October and November payslips were taxed on it.
- **Fixed:** estimated 2026-27 income updated to £21,000 on 11-11-2026. HMRC changed the code to **1257L cumulative from 11-11-2026**, the correct code.
- **Refund:** about £884.60 overpaid to 10-11-2026 (£1,090.40 paid against about £205.80 due). Expected on the December payslip as a negative tax line of roughly £500, so December take-home is about £885 higher than under the old code. Exact figure depends on November pay, including holiday 23-11-2026 to 27-11-2026.
- **If payroll doesn't refund it:** contact ITX payroll to apply the 11-11-2026 code notice. Failing that, HMRC reconciles after 05-04-2027 and sends a P800. HMRC: 0300 200 3300 or Help in the HMRC app.
- **National Insurance:** category A, correct on every payslip.
- **Pay history:** £13.50 an hour (July), £14.85 (August), £14.96 (September on).

| Pay date | Period | Code | Gross | Tax | NI | Net |
| --- | --- | --- | --- | --- | --- | --- |
| 10-08-2026 | July | 1257L | £822.00 | £0.00 | £0.00 | £822.00 |
| 10-09-2026 | August | 1255L M1 | £3,231.51 | £436.80 | £174.68 | £2,620.03 |
| 10-10-2026 | September | 1255L M1 | £2,454.69 | £281.60 | £112.53 | £2,060.56 |
| 10-11-2026 | October | 1255L M1 | £2,907.44 | £372.00 | £148.75 | £2,386.69 |

### Tax to-do
- [ ] Check the December payslip (about 10-12-2026): code 1257L with no M1 or X, and the refund shown
- [ ] If no refund on the December payslip, contact ITX payroll
- [ ] Check the HMRC account shows estimated income of £21,000
- [ ] Check whether untaxed savings interest is over £1,000 a year (if so, about £3.60 tax may be due)
- [ ] Find out the student loan plan and when repayments start. A course started in England from 01-08-2023 is usually Plan 5, repaid from the April after finishing, so likely April 2027. Check in the Student Loans Company account
- [ ] Ask Bershka whether workplace pension auto-enrolment applies (none deducted so far)
- [ ] Keep all 2026-27 payslips, and check the P60 when it arrives (after 05-04-2027)
- [ ] Optional: delete the 13-11-2026 "Check HMRC app" calendar event

## Credit cards
- **NatWest credit card:** limit £3,704.10. Used for regular small spending and paid in full to build a credit history.
- **Amex:** applied for, arriving soon. Limit not known yet.
## Goals
Proposed by Claude on 13-11-2026 from the figures above. Change or delete any of them.
- [ ] **Clear the £2,800 accommodation debt by 28-02-2027.** About £935 a month for three months fits within take-home after costs.
- [ ] **Keep a £2,000 emergency fund** in NatWest that isn't touched for spending, debt or stock. About 2 to 3 months of essential costs.
- [ ] **Christmas gifts: £150** in December. Placeholder, set your own figure.
- [ ] **February holiday: £600 set aside by 31-01-2027.** Placeholder until the trip is priced.
- [ ] **Reselling float: £300** kept separate for stock, so buying doesn't eat into living money. Profit goes back in until the float grows.
- [ ] **LISA: keep the £50 a week going** (about £2,600 a year, under the £4,000 yearly limit, earning the 25% government bonus). LISA money is for a first home or age 60; withdrawing for anything else costs a 25% charge.
- [ ] **New gym membership at or under £30 a month.**
## Status log
- 13-11-2026: Finance set up, blank
- 13-11-2026: filled in with Bradley: pay, accounts, balances, budgets, recurring payments, debts and proposed goals.
- 13-11-2026: tax refund details imported (about £884.60 due back on the December payslip). Hourly rate corrected to £14.96 from payslips.
