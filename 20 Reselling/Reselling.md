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
- [ ] **18-11-2026 21:00:** second LEGO X-Mansion (76294), Smyths click and collect at **Salford** (order UK302606348, ordered 16-11-2026, Apple Pay on NatWest current). Not in [[Stock]] yet: Smyths only take payment on collection. A friend in Manchester may collect, but Smyths ask for the ready-for-collection email, the payment method used and possibly photo ID of the person who ordered, so a friend may be refused. If nobody can collect, leave it: the order is cancelled automatically, £2 non-collection fee, the rest of the hold released within up to 5 working days. Or ask cshelpdesk@smythstoys.com to cancel it to try to avoid the fee.
- [ ] **17-11-2026:** last day to collect the LEGO X-Mansion from Smyths Thurrock (held 2 days from order). Ready for collection email arrived 16-11-2026 04:05 (order UK302470704). Bring the email and NatWest card.
- [ ] **17-11-2026 19:30:** X-Mansion handover to the eBay buyer at home (agreed 16-11-2026, he's coming from Brentwood). Home from the shift about 19:30. Collect the set from Smyths Thurrock before work. Send the address once the time is agreed. Scan his collection code to get paid.
- [ ] LEGO X-Mansion sold 16-11-2026 (eBay, £300 to Bradley, local collection). Agree a collection time with the buyer in eBay messages, then scan or enter his collection code at handover to get paid. Delete the 08-12 and 13-12 return calendar events.
- [ ] Lover rhinestone earbud case (order #TS1334668, £35.25 on NatWest, bought 16-11-2026): cancellation refused 16-11-2026, already being processed for shipment. Back in [[Stock]]. Listed on eBay 16-11-2026 at £50 (presale) to clear it. If unsold, return it within 14 days of delivery for a refund via the Royal Mail returns portal linked in support's reply (unopened, same condition). When it arrives: Bradley gives the delivery date, then send an .ics for the last return day at delivery + 14 days, with a check 4 days before.
- [ ] Topps Super Tin 3 (order #UK-1324768-S, £24.99 on NatWest): cancelled by Topps support 16-11-2026, full refund issued. Check the £24.99 lands on NatWest by 30-11-2026 (up to 10 business days). Removed from [[Stock]]. Lesson: check eBay sold prices before buying from a scraper ping.
- [ ] Acoustic Piano sweatpants L (£65 + £5.25, confirmation 0PMWR02UZ) and Acoustic Piano notebook (£25 + £5.25, released 16-11-2026, confirmation EDK48FMJZ), both bought 16-11-2026 from the Taylor Swift UK Store. eBay sold 16-11-2026: sweatpants £90.81 to £136.22 (L sold £136.22 + delivery on 30-10-2026); notebook has no sales yet, but other Acoustic Piano items sell £52 to £107. List both. Return window 14 days from delivery (cannot cancel once processing). Paid from NatWest current.
- [ ] Acoustic Piano Cozy Slippers, size 36 (£50 + £5.25 on NatWest, confirmation 8INK0407E, bought 16-11-2026). HOR #general-chat 16-11-2026 18:16 to 18:19: sold out in the USA, 3 UK sizes out of stock, "may be worth picking up a couple pairs", good Christmas gift. No eBay sales yet. List once a few sell, or as a presale. Return window 14 days from delivery.
- [ ] Topps NOW Ronaldo Final Farewell Pack (£18, confirmation M0CNZ0WRH, bought 16-11-2026): Topps NOW is printed to order, sale open until 23-11-2026 19:00, so the print run (and resale) depends on how many are ordered. Check eBay sold prices after 23-11-2026; sell sealed once prices settle.
- [ ] H&M x Elie Saab wedding dress, size 4 (£549.99 + £3.99 delivery = £553.98, Apple Pay, bought 17-11-2026 00:38 on the HOR #hm-online restock ping, delivery 2 to 3 working days): eBay UK **sold** 24-10 to 11-11: £832.90 (UK 8, 11 bids), £858.40 (UK 10, 14 bids), £839.98 (UK 8), then £561 and £486 from an Australian seller. Asking prices (£820 to £1,400) aren't sales. Size 4 is the smallest size, and tonight's restock adds supply, so expect about £650 to £800 rather than £1,000. List as soon as it arrives, BNWT, auction or BIN around £799 with offers. Check H&M's return window when it arrives as the fallback. Confirm which card Apple Pay used (assumed NatWest).
- [ ] Sherpa jacket (order #TS1334188): return window is 14 days from the day after delivery (store terms), not 30 days from purchase. When it arrives: Bradley gives the delivery date, then send a new .ics with a return check 4 days before and the last return day at delivery + 14 days, and he deletes the old 10-12 and 15-12 events. If unsold by the check, take down the eBay listing and return it.

## Notes
- 13-11-2026: no stock yet. Previous experience reselling shoes, about 2021 to 2023.
- 15-11-2026: reselling is paid from NatWest current for now. 16-11-2026: the Amex card hasn't arrived yet, so NatWest stays the reselling card until it does. Once buying picks up, plan to move reselling to HSBC or the Amex, depending on the size of the purchase.
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
- 15-11-2026: LEGO X-Mansion 76294 bought for £289.99 from Smyths (#smythstoys-instore ping), for collection at Smyths Thurrock. Paid from NatWest current. Both listed on eBay 16-11-2026.Listed on eBay at £310.
- 16-11-2026: X-Mansion sold on eBay, £300 to Bradley (buyer paid the Buyer Protection fee on top, collection so no postage). Profit £10.01 once collected and handed over.
- 15-11-2026: entered the Riftbound raffle (both bundles), winner emails 17-11-2026. Request Invites 1 done.
