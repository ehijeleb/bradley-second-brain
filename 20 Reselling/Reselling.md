---
type: area
area: reselling
status: active
---
# Reselling

> [!info] Snapshot
> **What:** buying items and reselling them for profit. Tracks stock, sales, fees, expenses and profit.
> **Where things live:** every item in [[Stock]] (one line each, updated when it sells). Costs that aren't items (postage bags, listing upgrades, travel to pick up) in [[Reselling expenses]]. The tables below work themselves out.
> **Platforms:** sells across several; resold shoes from about 2021 to 2023. Restarting November 2026.
> **Community:** [[House of Resell]] (Discord), joined 13-11-2026.
> Needs the **Dataview** plugin with **Enable JavaScript queries** turned on.

## Profit by month
```dataviewjs
dv.view("20 Reselling/_scripts/reselling", { view: "summary" })
```

## In stock
```dataviewjs
dv.view("20 Reselling/_scripts/reselling", { view: "stock" })
```

## How to log
**Bought something**, add a line in [[Stock]]:
```
- Nike Air Max 90, size 9 [bought:: 02-11-2026] [cost:: 25.00] [from:: Vinted] [state:: listed]
```
`state` is `in stock`, `listed`, `sold` or `kept` (kept items drop out of stock and profit).

**Sold it**, add to the same line:
```
[sold:: 10-11-2026] [price:: 45.00] [fees:: 2.50] [postage:: 3.20] [platform:: eBay]
```
`fees` and `postage` are what you paid (leave them out if the buyer paid). Profit = price − cost − fees − postage.

**Other costs**, in [[Reselling expenses]]:
```
- 05-11-2026 Postage bags [exp:: Supplies] [amt:: 6.99]
```

Reselling money also counts as income: when profit is taken out, log it in that month's budget under [[Finance]] as `[income:: Reselling]`.

## Next actions
- [ ] Log the first purchase in [[Stock]] when it happens
- [ ] Note which platforms I have accounts on

## Notes
- 13-11-2026: no stock yet. Previous experience reselling shoes, about 2021 to 2023.

## Check these lines
```dataviewjs
dv.view("20 Reselling/_scripts/reselling", { view: "check" })
```

## Status log
- 13-11-2026: hub created
- 13-11-2026: joined [[House of Resell]]. Starting from zero stock.
