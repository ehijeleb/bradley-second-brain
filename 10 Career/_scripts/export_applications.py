"""Export the application notes to an Excel tracker.

Run from the vault folder:
    python "10 Career/_scripts/export_applications.py"

Reads every note in "10 Career/Applications/" and writes
"10 Career/Exports/Application tracker.xlsx" (overwriting the last export).
The notes are the main copy; the spreadsheet is a snapshot for sharing or opening in Excel.
Needs openpyxl once: python -m pip install openpyxl
"""
import datetime as dt
import pathlib
import re
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("openpyxl isn't installed. Run: python -m pip install openpyxl")

VAULT = pathlib.Path(__file__).resolve().parents[2]
SRC = VAULT / "10 Career" / "Applications"
OUT = VAULT / "10 Career" / "Exports" / "Application tracker.xlsx"

COLUMNS = [
    ("Application ID", "app_id"), ("Date applied", "date_applied"), ("Company", "company"),
    ("Role title", "role"), ("Location", "location"), ("Advert link", "advert"),
    ("Closing date", "closing_date"), ("Fit score", "fit_score"), ("Application status", "stage"),
    ("CV version used", "cv_version"), ("Cover letter", "cover_letter"),
    ("Next step or deadline", "next_step"), ("Next step date", "deadline"), ("Notes", None),
]


def frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not m:
        return {}, text
    props = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith((" ", "\t", "-")):
            props[k.strip()] = v.strip().strip('"').strip("'")
    return props, m.group(2)


def notes_section(body):
    m = re.search(r"^## Notes\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    if not m:
        return ""
    lines = [l.strip().lstrip("-").strip() for l in m.group(1).splitlines()]
    return "; ".join(l for l in lines if l)


def as_date(v):
    try:
        return dt.date.fromisoformat(v) if v else None
    except ValueError:
        return v


def main():
    rows = []
    for f in sorted(SRC.glob("*.md")):
        props, body = frontmatter(f.read_text(encoding="utf-8"))
        if props.get("type") != "application":
            continue
        row = []
        for _, key in COLUMNS:
            if key is None:
                row.append(notes_section(body))
            elif key in ("date_applied", "closing_date", "deadline"):
                row.append(as_date(props.get(key, "")))
            elif key == "fit_score":
                v = props.get(key, "")
                row.append(float(v) if re.fullmatch(r"\d+(\.\d+)?", v) else v)
            else:
                row.append(props.get(key, ""))
        rows.append(row)

    wb = Workbook()
    ws = wb.active
    ws.title = "Applications"
    ws.append([c for c, _ in COLUMNS])
    for row in rows:
        ws.append(row)
    header_fill = PatternFill("solid", fgColor="1F3864")
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = header_fill
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    widths = [14, 13, 22, 28, 16, 40, 13, 9, 18, 16, 12, 28, 14, 50]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for col in (2, 7, 13):
        for cell in ws.iter_cols(min_col=col, max_col=col, min_row=2):
            for c in cell:
                c.number_format = "DD-MM-YYYY"
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {len(rows)} application(s) to {OUT}")


if __name__ == "__main__":
    main()
