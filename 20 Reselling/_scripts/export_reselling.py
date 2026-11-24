"""Export the reselling notes to CSV files for the Power BI dashboard.

Run from the vault folder:
    python "20 Reselling/_scripts/export_reselling.py"

Reads [[Stock]] and [[Reselling expenses]] and writes (overwriting the last export):
    20 Reselling/Exports/Items.csv      one row per item in Stock
    20 Reselling/Exports/Expenses.csv   one row per expense
The notes are the main copy; the CSVs are a snapshot for Power BI (open the .pbix, then Refresh).
Standard library only, nothing to install.

Dates are written YYYY-MM-DD so Power BI reads them as dates whatever the locale.
Order and confirmation numbers in brackets after the shop name are dropped.
"""
import csv
import datetime as dt
import pathlib
import re

VAULT = pathlib.Path(__file__).resolve().parents[2]
STOCK = VAULT / "20 Reselling" / "Stock.md"
EXPENSES = VAULT / "20 Reselling" / "Reselling expenses.md"
OUT = VAULT / "20 Reselling" / "Exports"

FIELD = re.compile(r"\[(\w+)::\s*([^\]]*)\]")

# First match wins. Add a rule when a new kind of item turns up (unmatched items export as "Other").
CATEGORIES = [
    (r"playstation|ps5|dualsense|switch|xbox|nintendo", "Gaming"),
    (r"lego", "LEGO"),
    (r"topps|panini|pok[eé]mon|riftbound|card", "Trading cards"),
    (r"taylor swift", "Music merch"),
    (r"dress|jacket|trainer|shoe|nike|adidas|h&m", "Fashion"),
    (r"red bull|advent calendar", "Food and drink"),
]


def parse_date(text):
    text = (text or "").strip()
    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def parse_money(text):
    cleaned = re.sub(r"[^0-9.\-]", "", text or "")
    try:
        return round(float(cleaned), 2) if cleaned else None
    except ValueError:
        return None


def bullet_lines(path):
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- ") and "::" in line:
            yield line[2:]


def category_of(name):
    low = name.lower()
    for pattern, cat in CATEGORIES:
        if re.search(pattern, low):
            return cat
    return "Other"


def shop_of(text):
    shop = re.sub(r"\s*\([^)]*\)", "", text or "").strip()
    return re.split(r",\s*", shop)[0] if shop else ""


def fmt(value):
    if value is None:
        return ""
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def export_items(today):
    rows, warnings = [], []
    for n, line in enumerate(bullet_lines(STOCK), start=1):
        f = {k.lower(): v.strip() for k, v in FIELD.findall(line)}
        name = FIELD.sub("", line).strip()
        bought = parse_date(f.get("bought"))
        sold = parse_date(f.get("sold"))
        refunded = parse_date(f.get("refunded"))
        cost = parse_money(f.get("cost"))
        price = parse_money(f.get("price"))
        fees = parse_money(f.get("fees")) or 0.0
        postage = parse_money(f.get("postage")) or 0.0
        state = (f.get("state") or "in stock").lower()
        if sold and state != "sold":
            state = "sold"
        profit = round(price - (cost or 0) - fees - postage, 2) if sold and price is not None else None
        end = sold or refunded or today
        days = (end - bought).days if bought else None
        if cost is None:
            warnings.append(f"{name}: no cost")
        if not bought:
            warnings.append(f"{name}: bought date missing or not DD-MM-YYYY")
        if f.get("refunded") and not refunded:
            warnings.append(f"{name}: refunded date not DD-MM-YYYY")
        if f.get("sold") and not sold:
            warnings.append(f"{name}: sold date not DD-MM-YYYY")
        cat = category_of(name)
        if cat == "Other":
            warnings.append(f"{name}: no category rule, exported as Other")
        rows.append({
            "Item ID": f"I{n:03d}",
            "Item": name,
            "Category": cat,
            "Shop": shop_of(f.get("from")),
            "Paid with": f.get("paid", ""),
            "State": state,
            "Bought": bought,
            "Cost": cost,
            "Sold": sold,
            "Price": price,
            "Fees": fees if sold else None,
            "Postage": postage if sold else None,
            "Platform": f.get("platform", ""),
            "Refunded": refunded,
            "Profit": profit,
            "Margin": f"{profit / cost:.4f}" if profit is not None and cost else None,
            "Days held": days,
        })
    write(OUT / "Items.csv", rows)
    return rows, warnings


def export_expenses():
    rows, warnings = [], []
    for line in bullet_lines(EXPENSES):
        f = {k.lower(): v.strip() for k, v in FIELD.findall(line)}
        text = FIELD.sub("", line).strip()
        m = re.match(r"^(\S+)\s+(.*)$", text)
        date = parse_date(m.group(1)) if m else None
        what = m.group(2) if m else text
        amount = parse_money(f.get("amt"))
        if not date:
            warnings.append(f"Expense '{text}': date missing or not DD-MM-YYYY")
        if amount is None:
            warnings.append(f"Expense '{text}': no amt")
        rows.append({"Date": date, "Expense": what, "Type": f.get("exp", ""), "Amount": amount})
    write(OUT / "Expenses.csv", rows, ["Date", "Expense", "Type", "Amount"])
    return rows, warnings


def write(path, rows, header=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    header = header or (list(rows[0]) if rows else [])
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in rows:
            w.writerow({k: fmt(v) for k, v in r.items()})


def main():
    today = dt.date.today()
    items, w1 = export_items(today)
    expenses, w2 = export_expenses()
    print(f"Wrote {len(items)} items and {len(expenses)} expenses to {OUT.relative_to(VAULT)}")
    for msg in w1 + w2:
        print("  check:", msg)


if __name__ == "__main__":
    main()
