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
Optional `[paid:: NatWest current]` records which account or card paid for it.

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
- [x] Log the first purchase in [[Stock]] when it happens
- [ ] Note which platforms I have accounts on
- [x] Enter the Riftbound raffle (both bundles) by 16-11-2026 5pm. Done 15-11-2026. Register at playriftbound.com first. See [[House of Resell]].
- [x] **16-11-2026 13:00:** Topps Premier League Gold Hobby Box drop. Missed: the captcha wouldn't load at checkout. See [[House of Resell]].
- [x] House of Resell setup done 15-11-2026: Request Invites 1, 2 and 3, channel notifications, shop accounts (Topps, Argos, Asda, GAME, Very, Pokémon Center UK).
- [ ] Set up Currys and Sony PlayStation Direct accounts with payment saved. Sony: the existing account uses Mum's email and was playing up on 16-11-2026. Either get her to approve moving it to my own email (Account settings, Sign-in ID) or make a fresh account with my own email. Check the Pokémon Center UK newsletter is on.
- [ ] **17-11-2026:** last day to collect the LEGO X-Mansion from Smyths Thurrock (held 2 days from order). Ready for collection email arrived 16-11-2026 04:05 (order UK302470704). Bring the email and NatWest card.
- [ ] **18-11-2026 19:30:** X-Mansion handover to the eBay buyer at home (offered 16-11-2026, waiting for him to confirm). Shift ends 19:00. Scan his collection code to get paid.
- [ ] LEGO X-Mansion sold 16-11-2026 (eBay, £300 to Bradley, local collection). Agree a collection time with the buyer in eBay messages, then scan or enter his collection code at handover to get paid. Delete the 08-12 and 13-12 return calendar events.
- [ ] Lover rhinestone earbud case (order #TS1334668, £35.25 on NatWest, bought 16-11-2026): cancellation refused 16-11-2026, already being processed for shipment. Back in [[Stock]]. Options: list it on eBay while it ships, or return it within 14 days of delivery for a refund via the Royal Mail returns portal linked in support's reply (unopened, same condition). When it arrives, set a return deadline of delivery date + 14 days.
- [ ] Sherpa jacket (order #TS1334188): store terms say 14 days to cancel from the day after delivery (not 30). Check the dispatch email when it arrives and fix the 10-12 and 15-12 return reminders.
- [ ] Sherpa jacket: if unsold by 10-12-2026, take down the eBay listing and return it to the Taylor Swift UK Store. Last day 15-12-2026 (30 days from purchase, counted from the buy date to be safe). Calendar reminders sent.

## Notes
- 13-11-2026: no stock yet. Previous experience reselling shoes, about 2021 to 2023.
- 15-11-2026: reselling is paid from NatWest current for now. Once buying picks up, plan to move reselling to HSBC or the Amex, depending on the size of the purchase.
- 15-11-2026: sherpa jacket cost is £115 plus £5 delivery. Listed on eBay at £217.95, the cheapest price these jackets were going for.

## Check these lines
```dataviewjs
dv.view("20 Reselling/_scripts/reselling", { view: "check" })
```

## Status log
- 13-11-2026: hub created
- 13-11-2026: joined [[House of Resell]]. Starting from zero stock.
- 15-11-2026: first buy, Taylor Swift Take Me to the Lakes sherpa jacket (3XL) for £115 from the UK store, off a House of Resell monitor ping.
- 15-11-2026: sherpa jacket listed on eBay at £217.95.
- 15-11-2026: LEGO X-Mansion 76294 bought for £289.99 from Smyths (#smythstoys-instore ping), for collection at Smyths Thurrock. Paid from NatWest current. Listed on eBay at £310.
- 16-11-2026: X-Mansion sold on eBay, £300 to Bradley (buyer paid the Buyer Protection fee on top, collection so no postage). Profit £10.01 once collected and handed over.
- 15-11-2026: entered the Riftbound raffle (both bundles), winner emails 17-11-2026. Request Invites 1 done.
