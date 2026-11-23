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
- [x] **18-11-2026 21:00:** second LEGO X-Mansion (76294), Smyths click and collect at **Salford** (order UK302606348, ordered 16-11-2026, Apple Pay on NatWest current). Not in [[Stock]] yet: Smyths only take payment on collection. A friend in Manchester may collect, but Smyths ask for the ready-for-collection email, the payment method used and possibly photo ID of the person who ordered, so a friend may be refused. If nobody can collect, leave it: the order is cancelled automatically, £2 non-collection fee, the rest of the hold released within up to 5 working days. Or ask cshelpdesk@smythstoys.com to cancel it to try to avoid the fee. 17-11-2026: the box was opened, so the friend was told not to take it. Not collected; check whether the £2 non-collection fee is charged. 18-11-2026: Smyths sent a 'ready to collect by 21:00' reminder; it lapses tonight. 18-11-2026 20:35: Smyths Salford left a voicemail. A staff member marked the order as collected by mistake, so the £289.99 may come out of NatWest; they'll hold the set until it's collected with ID. Check NatWest, and ask Smyths to cancel and refund (not collecting, box was opened). 19-11-2026: Smyths issued a refund, due in 1 to 5 working days, so by 26-11-2026 ([[2026-11-19 Smyths Toys - Refund issued (UK302606348)]]). Check NatWest for £289.99 back and no £2 fee.
- [x] **17-11-2026:** last day to collect the LEGO X-Mansion from Smyths Thurrock (held 2 days from order). Ready for collection email arrived 16-11-2026 04:05 (order UK302470704). Bring the email and NatWest card. Collected 17-11-2026.
- [x] **17-11-2026 19:30:** X-Mansion handover to the eBay buyer at home (agreed 16-11-2026, he's coming from Brentwood). Home from the shift about 19:30. Collect the set from Smyths Thurrock before work. Send the address once the time is agreed. Scan his collection code to get paid. Done 17-11-2026.
- [x] LEGO X-Mansion sold 16-11-2026 (eBay, £300 to Bradley, local collection). Agree a collection time with the buyer in eBay messages, then scan or enter his collection code at handover to get paid. Delete the 08-12 and 13-12 return calendar events. Handed over 17-11-2026.
- [ ] Lover rhinestone earbud case (order #TS1334668, £35.25 on NatWest, bought 16-11-2026): cancellation refused 16-11-2026, already being processed for shipment. Back in [[Stock]]. Listed on eBay 16-11-2026 at £50 (presale) to clear it. If unsold, return it within 14 days of delivery for a refund via the Royal Mail returns portal linked in support's reply (unopened, same condition). When it arrives: Bradley gives the delivery date, then send an .ics for the last return day at delivery + 14 days, with a check 4 days before. 18-11-2026: dispatched. Decided to return it as soon as it arrives: end the eBay listing now, then send it back unopened via the Royal Mail portal.
- [x] Topps Super Tin 3 (order #UK-1324768-S, £24.99 on NatWest): cancelled by Topps support 16-11-2026, full refund issued. Check the £24.99 lands on NatWest by 30-11-2026 (up to 10 business days). Refund landed 17-11-2026. Removed from [[Stock]]. Lesson: check eBay sold prices before buying from a scraper ping.
- [ ] Acoustic Piano sweatpants L (£65 + £5.25, confirmation 0PMWR02UZ) and Acoustic Piano notebook (£25 + £5.25, released 16-11-2026, confirmation EDK48FMJZ), both bought 16-11-2026 from the Taylor Swift UK Store. eBay sold 16-11-2026: sweatpants £90.81 to £136.22 (L sold £136.22 + delivery on 30-10-2026); notebook has no sales yet, but other Acoustic Piano items sell £52 to £107. List both. Return window 14 days from delivery (cannot cancel once processing). Paid from NatWest current. 17-11-2026: sweatpants listed; holding the notebook for now (listing has watchers) while checking stock levels. 18-11-2026: all dispatched. Decided to return the sweatpants as soon as they arrive: end the eBay listing now, send them back unopened. Sweatpants and slippers delivered 19-11-2026; last return day 03-12-2026 for both (slippers check 29-11-2026).
- [ ] Acoustic Piano Cozy Slippers, size 36 (£50 + £5.25 on NatWest, confirmation 8INK0407E, bought 16-11-2026). HOR #general-chat 16-11-2026 18:16 to 18:19: sold out in the USA, 3 UK sizes out of stock, "may be worth picking up a couple pairs", good Christmas gift. No eBay sales yet. List once a few sell, or as a presale. Return window 14 days from delivery. 17-11-2026: holding for now while checking stock levels.
- [ ] Topps NOW Ronaldo Final Farewell Pack (£18, confirmation M0CNZ0WRH, bought 16-11-2026): Topps NOW is printed to order, sale open until 23-11-2026 19:00, so the print run (and resale) depends on how many are ordered. Check eBay sold prices after 23-11-2026; sell sealed once prices settle.
- [ ] H&M x Elie Saab wedding dress, size 4 (£549.99 + £3.99 delivery = £553.98, Apple Pay, bought 17-11-2026 00:38 on the HOR #hm-online restock ping, delivery 2 to 3 working days): eBay UK **sold** 24-10 to 11-11: £832.90 (UK 8, 11 bids), £858.40 (UK 10, 14 bids), £839.98 (UK 8), then £561 and £486 from an Australian seller. Asking prices (£820 to £1,400) aren't sales. Size 4 is the smallest size. The restock sold out again by 00:41 (every size), so it was a small one and won't flood eBay much. Expect about £700 to £850 rather than £1,000. List as soon as it arrives, BNWT, auction or BIN around £799 with offers. Return fallback: Elie Saab collection items go back online only, within 14 days of delivery, not in store (checked 18-11-2026). List it the day it arrives. Paid with NatWest (confirmed).
- [ ] **18-11-2026 07:00 (Tesco, back before the 09:15 Olivia briefing; shift 10:00):** Red Bull Advent Calendar, HOR #instore-flips 17-11. Tesco about £25 on Clubcard (£45 without) in select stores, 30-day returns; resell about £50. Barcode 9002490299781 (check stock with the HOR bot). Also Costco £21.80 (90-day returns) and some NISA £25. His local Tesco said no Clubcard price planned; HOR will confirm tomorrow. Check eBay sold prices before buying several.
- [ ] Sherpa jacket (order #TS1334188): return window is 14 days from the day after delivery (store terms), not 30 days from purchase. When it arrives: Bradley gives the delivery date, then send a new .ics with a return check 4 days before and the last return day at delivery + 14 days, and he deletes the old 10-12 and 15-12 events. If unsold by the check, take down the eBay listing and return it. 18-11-2026: dispatched. Delivered 18-11-2026 (tracking FY508640105GB). Return check 28-11-2026, last return day 02-12-2026. New .ics sent; delete the old 10-12 and 15-12 events.
- [ ] **18-11-2026 onwards:** Red Bull Advent Calendar at Tesco stores, £25 with Clubcard (was £45), until 09-12-2026. Check eBay sold prices first (the ping only showed a £53.99 + £6.65 asking price), then pick some up if the margin holds after postage. See [[House of Resell]]. 18-11-2026: bought 2 on the Amex (the store limited it to 2), aiming for about £50 each. Then 4 more on the Amex, 6 in total. Keep the receipts for returns.
- [x] **By 23-11-2026:** Smyths delivery, order UK303047392 (GTA VI DualSense, white, ordered 18-11-2026 on Apple Pay). 1 controller, £74.99 on NatWest, added to [[Stock]]. Change its state to listed if you list it as a presale. eBay sold £94 to £100 + postage on 18-11-2026. See [[House of Resell]].
- [ ] **19-11-2026 14:00:** Topps Finest F1 Hobby Box EQL raffle (£265, resale £330 to £350, free returns). Entered via a friend's bot on the Revolut card. Watch for the win email and any card holds; if won, log in [[Stock]] with [paid:: Revolut]. See [[House of Resell]].
- [ ] **On arrival:** return all 6 Taylor Swift snow globes (3 Opalite Rock and Cactus, 3 The Fate of Ophelia; orders #05IY0LN5X, #WVXAQ6LN0, #WFA2EPUHA, £318.45 on NatWest). Decided 20-11-2026. End the eBay Opalite listing now. Keep them sealed, return via the Taylor Swift UK Store returns process, then remove from [[Stock]] once refunded.

## Returns
Return windows for everything in [[Stock]], checked 18-11-2026. "Verified" means it comes from the shop's own terms or support; "unconfirmed" means third-party guides only, so check the receipt or order email. Update the last day once delivery dates are known. Keep every receipt and order email, and keep items unopened with tags on.

18-11-2026: no online orders delivered yet (Taylor Swift items, H&M dress, Smyths controller). When each arrives, log the delivery date here and send an .ics for its last return day with a check 4 days before.

| Item | Shop | Window | Last day | Conditions | Confidence |
| --- | --- | --- | --- | --- | --- |
| LEGO X-Mansion x2 | Smyths Romford (in store, 17-11-2026) | 28 days from purchase | 15-12-2026 | Unopened, resaleable, receipt | Verified (Smyths returns page via search) |
| Red Bull Advent Calendar x6 | Tesco Extra (18-11-2026, Amex) | Not stated by Tesco for in-store food; guides say 30 days | Unconfirmed: check the receipt, aim to decide by 09-12-2026 | Receipt, back to an Extra or Superstore (not Express), before the best-before date, refund at £25 to the Amex | Unconfirmed |
| H&M x Elie Saab dress | H&M online | Returned 22-11-2026 | Refund pending (£553.98 on NatWest, less any return fee) | n/a | Done |
| Sherpa jacket | Taylor Swift UK Store (delivered 18-11-2026) | 14 days from the day after delivery | 02-12-2026 (check 28-11-2026) | Unworn, tags on | Verified (store terms) |
| Sweatpants | Taylor Swift UK Store (delivered 19-11-2026) | 14 days from the day after delivery | 03-12-2026 (check 29-11-2026) | Sealed, same condition | Assumed same as the sherpa |
| Slippers | Taylor Swift UK Store (delivered 19-11-2026) | 14 days from the day after delivery | 03-12-2026 (check 29-11-2026) | Unworn, tags on | Assumed same as the sherpa |
| Notebook | Taylor Swift UK Store (delivered 19-11-2026) | 14 days from the day after delivery | 03-12-2026 (check 29-11-2026) | Sealed in its wrap | Assumed same as the sherpa |
| Snow globes x6 | Taylor Swift UK Store (ordered 19-11-2026, not arrived) | 14 days from the day after delivery | Return straight away on arrival | Unopened, same condition | Assumed same as the sherpa |
| Switch 2 Zelda 40th console | Argos online (1562154254, ordered 23-11-2026, not arrived) | Argos usually 30 days if unopened | Set on delivery | Sealed, receipt or order email | Unconfirmed: check the order email |
| Earbud case | Taylor Swift UK Store (dispatched 18-11-2026) | 14 days from the day after delivery | Return straight away on arrival | Unopened; Royal Mail returns portal in support's reply | Verified (support) |
| Topps NOW Ronaldo pack | Topps UK | Printed to order; Topps' store policy says sales are final | No return | n/a | Unconfirmed for the UK site |

## Notes
- 13-11-2026: no stock yet. Previous experience reselling shoes, about 2021 to 2023.
- 15-11-2026: reselling is paid from NatWest current for now. 16-11-2026: the Amex card hasn't arrived yet, so NatWest stays the reselling card until it does. Once buying picks up, plan to move reselling to HSBC or the Amex, depending on the size of the purchase. 17-11-2026: the Amex arrived; first reselling buy on it 18-11-2026 (2 Red Bull advent calendars).
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
- 17-11-2026: X-Mansion collected from Smyths Thurrock and handed over to the eBay buyer. Topps Super Tin refund (£24.99) landed. Bought 2 more X-Mansions (£289.99 each, Smyths Romford click and collect, NatWest), listed on eBay at £320 payout each, messages already in. Holding the Acoustic Piano notebook and slippers for now (watchers on the listings).
- 18-11-2026: return windows for all stock added under Returns.
- 18-11-2026: all Taylor Swift Store orders dispatched. Returning the sweatpants and earbud case as soon as they arrive. Remove them from [[Stock]] once refunded.
- 18-11-2026: both X-Mansions also listed on Vinted at £320. Take the other listing down when one sells on either site.
- 18-11-2026: H&M x Elie Saab dress listed on Vinted (about £825, offers to about £780).
- 18-11-2026: sherpa jacket listed on Vinted (£195, offers to about £175).
- 18-11-2026: Acoustic Piano notebook listed on Vinted (about £45 to £55).
- 18-11-2026: Acoustic Piano slippers listed on Vinted (£80, offers to about £70).
- 18-11-2026: Vinted listings went up with stock photos. Vinted requires your own photos of the actual item, and items in hand, so swap in real photos (X-Mansions now, the rest on arrival).
- 18-11-2026: Vinted removed the dress listing for using stock photos (flagged as a duplicate) and warned that another breach could restrict listing ([[2026-11-18 Vinted Support - Listing removed (duplicate)]]). Re-list only with fresh photos of my own once it arrives. Dress back to in stock.
- 18-11-2026: X-Mansions, sherpa, notebook and slippers are all live on Vinted with stock photos, at risk after the warning. Plan: own photos on the X-Mansions now; delete the sherpa, notebook and slippers listings until they arrive.
- 18-11-2026: slippers are also listed on eBay. Bradley is keeping the Vinted stock-photo listings up for now (only the dress was removed).
- 18-11-2026: GTA VI controller listed on Vinted (stock photos). Controller and slippers listings are under Vinted review and can't be edited. To do at home: own photos on the X-Mansion listings.
- 18-11-2026: eBay removed the GTA VI controller listing under its Counterfeit items policy (presale, stock photos). Bradley is appealing with the Smyths order (UK303047392) as proof. Re-list with own photos once it arrives.
- 18-11-2026: second Vinted warning: listings hidden for copyrighted (stock) photos ([[2026-11-18 Vinted - Listings hidden (copyrighted images)]]). Hidden until own photos are added. Next breach may restrict listing. Rule from now: Vinted only with own photos of items in hand.
- 18-11-2026: all Vinted listings removed except the controller and slippers, still under Vinted review. Delete those two as soon as the review ends. eBay listings unchanged (controller removed, appeal pending).
- 18-11-2026: sherpa jacket delivered. Last return day 02-12-2026. Take own photos and re-list on Vinted.
- 18-11-2026: sherpa jacket re-listed on Vinted with own photos (sealed bag, tag, SKU sticker), about £195. Also on eBay at £217.95. End the other listing when one sells.
- 19-11-2026: sweatpants and slippers delivered. Sweatpants going back now. Slippers: re-list on Vinted with own photos; last return day 03-12-2026.
- 19-11-2026: notebook delivered too (sealed). Slippers label confirms US 5 / UK 3 / EU 36. Own photos taken for slippers and notebook.
- 19-11-2026: Revolut card set up for a friend's checkout bot, £1,000 loaded. Log bot buys in [[Stock]] with [paid:: Revolut].
- 19-11-2026: notebook, slippers and sweatpants listed on Vinted with own photos (£45, £80, £110). Sweatpants plan changed: sell, or return if unsold by 29-11-2026.
- 19-11-2026: Smyths refunded the Salford X-Mansion order (UK302606348), due on NatWest by 26-11-2026.
- 19-11-2026: 6 Taylor Swift snow globes from the UK store on NatWest current: 3 Opalite Rock and Cactus, 3 The Fate of Ophelia. Singles £55.25 each (#05IY0LN5X, #WVXAQ6LN0); 2 of each in one order for £207.95 (#WFA2EPUHA, cost split across 4). Resale not checked yet. Return window 14 days from the day after delivery.
- 20-11-2026: HOR (#online-flips, 19-11): the snow globes stayed in stock unusually long; Manny is holding (free returns) and says cancelling via live chat or email is quick. Check eBay sold prices before they arrive. HOR flip update 19-11: Riftbound T1 Player Bundle (£70) and Worlds 2026 Edition (£80) both resell about £130 to £140; Bradley's raffle result not logged yet.
- 19-11-2026: dress and GTA VI controller delivered. Controller listed on Vinted with own photos. Dress last return day 03-12-2026 (online only). All return dates sent as one .ics.
- 20-11-2026: decided to return all 6 snow globes as soon as they arrive.
- 21-11-2026: GTA VI controller held at £90 for a Vinted buyer until Wed 25-11-2026 (not marked reserved; sell to anyone who pays first). If unpaid, back on sale; last return day 17-12-2026.
- 22-11-2026: GTA VI controller sold on Vinted for £90 (£15.01 profit). Post with the Vinted label; film the packing.
- 22-11-2026: H&M x Elie Saab dress returned to H&M online. Watch for the refund on NatWest, then remove it from [[Stock]]. LEGO X-Mansion offers at £305 and £300; notebook offer £35.
- 23-11-2026: Switch 2 Zelda 40th Anniversary console from Argos, £429.99 on NatWest current (order 1562154254). Home delivery, someone must be in. HOR resale £530 to £550 (mid-November): check eBay sold prices before listing.
