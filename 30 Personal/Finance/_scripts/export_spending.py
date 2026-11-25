"""Export personal and reselling spending to CSV files for the Power BI spending dashboard.

Run from the vault folder:
    python "30 Personal/Finance/_scripts/export_spending.py"

Reads the month notes and [[Finance]] in "30 Personal/Finance/", plus [[Stock]] and [[Reselling expenses]],
and writes (overwriting the last export) to "30 Personal/Finance/Exports/":
    Spending.csv   every payment out: personal purchases, reselling stock and reselling costs, with a Kind column
    Income.csv     every payment in
    Budgets.csv    personal categories, groups and monthly budgets from [[Finance]]
    Savings.csv    savings balances logged under "Savings balances" in [[Finance]]
The notes are the main copy; the CSVs are a snapshot for Power BI (open the .pbip, then Refresh).
Standard library only, nothing to install.
"""
import csv
import datetime as dt
import importlib.util
import pathlib
import re

VAULT = pathlib.Path(__file__).resolve().parents[3]
FIN = VAULT / "30 Personal" / "Finance"
OUT = FIN / "Exports"
FIELD = re.compile(r"\[(\w+)::\s*([^\]]*)\]")
DATE_AT_START = re.compile(r"^(\d{2}-\d{2}-\d{4})\s+")

# Reuse the reselling export's parsing and category rules, so both dashboards agree.
_spec = importlib.util.spec_from_file_location("export_reselling", VAULT / "20 Reselling" / "_scripts" / "export_reselling.py")
resell = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(resell)
parse_date, parse_money, category_of, shop_of = resell.parse_date, resell.parse_money, resell.category_of, resell.shop_of


def fields(line):
    return {k.lower(): v.strip() for k, v in FIELD.findall(line)}


def label(line):
    text = FIELD.sub("", line)
    text = re.sub(r"\([^)]*pending[^)]*\)", "", text, flags=re.I)
    return re.sub(r"\s+", " ", DATE_AT_START.sub("", text.strip())).strip()


def bullets(path):
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- ") and "::" in line:
            yield line[2:]


def month_of(d):
    return d.replace(day=1) if d else None


def write(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v.isoformat() if isinstance(v, dt.date)
                            else f"{v:.2f}" if isinstance(v, float) else v) for k, v in r.items()})


def main():
    warnings = []
    budgets, groups, savings = [], {}, []
    for line in bullets(FIN / "Finance.md"):
        f = fields(line)
        if "category" in f:
            groups[f["category"]] = f.get("group", "Other")
            budgets.append({"Category": f["category"], "Group": f.get("group", "Other"),
                            "Monthly budget": parse_money(f.get("budget")) or 0.0})
        elif "saving" in f:
            d = parse_date(DATE_AT_START.match(line).group(1)) if DATE_AT_START.match(line) else None
            bal = parse_money(f.get("balance"))
            if not d or bal is None:
                warnings.append(f"Savings line needs a DD-MM-YYYY date and a balance: {line}")
                continue
            savings.append({"Date": d, "Account": f["saving"], "Balance": bal})

    spending, income = [], []
    for note in sorted(FIN.glob("????-?? Budget.md")):
        for line in bullets(note):
            f = fields(line)
            m = DATE_AT_START.match(line)
            d = parse_date(m.group(1)) if m else None
            amt = parse_money(f.get("amt"))
            if "cat" in f:
                if not d or amt is None:
                    warnings.append(f"{note.stem}: needs a date and amt: {line}")
                    continue
                if f["cat"] not in groups:
                    warnings.append(f"{note.stem}: category '{f['cat']}' isn't in Finance: {line}")
                spending.append({"Date": d, "Month": month_of(d), "Description": label(line), "Kind": "Personal",
                                 "Category": f["cat"], "Group": groups.get(f["cat"], "Other"), "Amount": amt,
                                 "Paid with": f.get("from", ""), "Stock state": ""})
            elif "income" in f:
                if not d or amt is None:
                    if amt is None:
                        warnings.append(f"{note.stem}: income without amt (worked out in Obsidian, left out here): {line}")
                    continue
                income.append({"Date": d, "Month": month_of(d), "Description": label(line),
                               "Type": f["income"], "Amount": amt})

    for line in bullets(VAULT / "20 Reselling" / "Stock.md"):
        f = fields(line)
        d, amt = parse_date(f.get("bought")), parse_money(f.get("cost"))
        if not d or amt is None:
            continue
        name = FIELD.sub("", line).strip()
        spending.append({"Date": d, "Month": month_of(d), "Description": name, "Kind": "Reselling stock",
                         "Category": category_of(name), "Group": "Reselling", "Amount": amt,
                         "Paid with": f.get("paid", ""), "Stock state": (f.get("state") or "in stock").lower()})
    for line in bullets(VAULT / "20 Reselling" / "Reselling expenses.md"):
        f = fields(line)
        m = DATE_AT_START.match(line)
        d, amt = (parse_date(m.group(1)) if m else None), parse_money(f.get("amt"))
        if not d or amt is None:
            continue
        spending.append({"Date": d, "Month": month_of(d), "Description": label(line), "Kind": "Reselling costs",
                         "Category": f.get("exp", "Other"), "Group": "Reselling", "Amount": amt,
                         "Paid with": "", "Stock state": ""})

    spending.sort(key=lambda r: r["Date"])
    for i, r in enumerate(spending, start=1):
        r["ID"] = f"S{i:04d}"
    write(OUT / "Spending.csv", ["ID", "Date", "Month", "Description", "Kind", "Category", "Group", "Amount", "Paid with", "Stock state"], spending)
    write(OUT / "Income.csv", ["Date", "Month", "Description", "Type", "Amount"], sorted(income, key=lambda r: r["Date"]))
    write(OUT / "Budgets.csv", ["Category", "Group", "Monthly budget"], budgets)
    write(OUT / "Savings.csv", ["Date", "Account", "Balance"], sorted(savings, key=lambda r: r["Date"]))
    kinds = {}
    for r in spending:
        kinds[r["Kind"]] = kinds.get(r["Kind"], 0) + 1
    print(f"Wrote {len(spending)} payments out ({', '.join(f'{v} {k.lower()}' for k, v in kinds.items())}), "
          f"{len(income)} payments in, {len(budgets)} budgets, {len(savings)} savings balances to {OUT.relative_to(VAULT)}")
    for w in warnings:
        print("  check:", w)


if __name__ == "__main__":
    main()
