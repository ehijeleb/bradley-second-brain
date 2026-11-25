"""Generate the Spending dashboard as a Power BI project (PBIP: TMDL model + PBIR report)."""
import json, pathlib, shutil, sys, uuid

OUT = pathlib.Path(sys.argv[1]); THEME = pathlib.Path(sys.argv[2])
NAME = "Spending dashboard"
SM = OUT / f"{NAME}.SemanticModel"; RP = OUT / f"{NAME}.Report"
SCH = "https://developer.microsoft.com/json-schemas/fabric"
VIS = f"{SCH}/item/report/definition/visualContainer/2.4.0/schema.json"
EXPORTS = r"C:\Users\hp\bradleys-brain\30 Personal\Finance\Exports" + "\\"
if OUT.exists():
    shutil.rmtree(OUT)

tag = lambda: str(uuid.uuid4())
def write(p, t):
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t, encoding="utf-8", newline="\n")
def wjson(p, o): write(p, json.dumps(o, indent=2, ensure_ascii=False) + "\n")
q = lambda n: n if n.replace("_", "").isalnum() else "'" + n.replace("'", "''") + "'"

GBP = r"\£#,0.00;-\£#,0.00;\£#,0.00"; DATE = "dd-mm-yyyy"
T, D, M, I = ("string", "type text"), ("dateTime", "type date"), ("decimal", "Currency.Type"), ("int64", "Int64.Type")

TABLES = {
    "Spending": ("Spending.csv", [("ID", T), ("Date", D), ("Month", D), ("Description", T), ("Kind", T), ("Category", T),
                                  ("Group", T), ("Amount", M), ("Paid with", T), ("Stock state", T)]),
    "Income": ("Income.csv", [("Date", D), ("Month", D), ("Description", T), ("Type", T), ("Amount", M)]),
    "Budgets": ("Budgets.csv", [("Category", T), ("Group", T), ("Monthly budget", M)]),
    "Savings": ("Savings.csv", [("Date", D), ("Account", T), ("Balance", M)]),
}
MEASURES = {"Spending": [
    ("Total spent", "SUM ( Spending[Amount] )", GBP),
    ("Personal spend", 'CALCULATE ( [Total spent], Spending[Kind] = "Personal" )', GBP),
    ("Stock bought", 'CALCULATE ( [Total spent], Spending[Kind] = "Reselling stock" )', GBP),
    ("Stock refunded", 'CALCULATE ( [Total spent], Spending[Kind] = "Reselling stock", Spending[Stock state] = "returned" )', GBP),
    ("Stock going back", 'CALCULATE ( [Total spent], Spending[Kind] = "Reselling stock", Spending[Stock state] = "returning" )', GBP),
    ("Reselling costs", 'CALCULATE ( [Total spent], Spending[Kind] = "Reselling costs" )', GBP),
    ("Months logged", "COUNTROWS ( FILTER ( VALUES ( Calendar[Month number] ), CALCULATE ( [Personal spend] ) > 0 ) )", "0"),
    ("Budget", "SUM ( Budgets[Monthly budget] ) * MAX ( 1, [Months logged] )", GBP),
    ("Budget left", "[Budget] - [Personal spend]", GBP),
    ("% of budget used", "DIVIDE ( [Personal spend], [Budget] )", "0%;-0%;0%"),
    ("Income", "SUM ( Income[Amount] )", GBP),
    ("Left after personal spending", "[Income] - [Personal spend]", GBP),
    ("LISA balance", 'CALCULATE ( LASTNONBLANKVALUE ( Savings[Date], SUM ( Savings[Balance] ) ), Savings[Account] = "Moneybox LISA" )', GBP),
    ("LISA growth since first check", 'VAR firstBal = CALCULATE ( FIRSTNONBLANKVALUE ( Savings[Date], SUM ( Savings[Balance] ) ), Savings[Account] = "Moneybox LISA" ) RETURN [LISA balance] - firstBal', GBP),
]}

def table_tmdl(name, file, cols, measures):
    L = [f"table {q(name)}", f"\tlineageTag: {tag()}", ""]
    for n, dax, fmt in measures:
        L += [f"\tmeasure {q(n)} = {dax}", f"\t\tformatString: {fmt}", f"\t\tlineageTag: {tag()}", ""]
    for n, (dt, _m) in cols:
        L += [f"\tcolumn {q(n)}", f"\t\tdataType: {dt}"]
        if dt == "dateTime": L.append(f"\t\tformatString: {DATE}")
        if dt == "decimal": L.append(f"\t\tformatString: {GBP}")
        L += [f"\t\tlineageTag: {tag()}", f"\t\tsummarizeBy: {'sum' if dt == 'decimal' else 'none'}", f"\t\tsourceColumn: {n}", "",
              "\t\tannotation SummarizationSetBy = Automatic", ""]
    types = ", ".join('{"%s", %s}' % (n, m) for n, (_d, m) in cols)
    mq = ["let",
          f'    Source = Csv.Document(File.Contents(#"Exports folder" & "{file}"), [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]),',
          "    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),",
          '    Blanks = Table.TransformColumns(Promoted, {}, each if _ = "" then null else _),',
          f'    Typed = Table.TransformColumnTypes(Blanks, {{{types}}}, "en-GB")', "in", "    Typed"]
    L += [f"\tpartition {q(name)} = m", "\t\tmode: import", "\t\tsource ="] + ["\t\t\t\t" + x for x in mq]
    L += ["", "\tannotation PBI_ResultType = Table", ""]
    return "\n".join(L)

def calendar_tmdl():
    cols = [("Date", "dateTime", DATE, None), ("Month", "string", None, "Month number"), ("Month number", "int64", "0", None)]
    L = ["table Calendar", f"\tlineageTag: {tag()}", "\tdataCategory: Time", ""]
    for n, dt, fmt, sort in cols:
        L += [f"\tcolumn {q(n)}", f"\t\tdataType: {dt}"] + (["\t\tisKey"] if n == "Date" else [])
        if fmt: L.append(f"\t\tformatString: {fmt}")
        L += [f"\t\tlineageTag: {tag()}", "\t\tsummarizeBy: none", f"\t\tsourceColumn: [{n}]"]
        if sort: L.append(f"\t\tsortByColumn: {q(sort)}")
        L += ["", "\t\tannotation SummarizationSetBy = Automatic", ""]
    L += ["\tpartition Calendar = calculated", "\t\tmode: import", "\t\tsource = ```",
          "\t\t\t\tADDCOLUMNS (", "\t\t\t\t    CALENDAR ( DATE ( 2026, 8, 1 ), DATE ( 2027, 12, 31 ) ),",
          '\t\t\t\t    "Month", FORMAT ( [Date], "mmm yyyy" ),',
          '\t\t\t\t    "Month number", YEAR ( [Date] ) * 100 + MONTH ( [Date] )', "\t\t\t\t)", "\t\t\t\t```", ""]
    return "\n".join(L)

wjson(SM / "definition.pbism", {"$schema": f"{SCH}/item/semanticModel/definitionProperties/1.0.0/schema.json", "version": "4.0", "settings": {}})
write(SM / "definition/database.tmdl", "database\n\tcompatibilityLevel: 1550\n")
write(SM / "definition/model.tmdl", "\n".join(
    ["model Model", "\tculture: en-GB", "\tdefaultPowerBIDataSourceVersion: powerBI_V3", "\tsourceQueryCulture: en-GB",
     "\tdataAccessOptions", "\t\tlegacyRedirects", "\t\treturnErrorValuesAsNull", "",
     'annotation PBI_QueryOrder = ["Exports folder","Spending","Income","Budgets","Savings"]', "",
     "annotation __PBI_TimeIntelligenceEnabled = 0", "", 'annotation PBI_ProTooling = ["DevMode"]', ""]
    + [f"ref table {t}" for t in list(TABLES) + ["Calendar"]] + [""]))
write(SM / "definition/expressions.tmdl",
      f"expression 'Exports folder' = \"{EXPORTS}\" meta [IsParameterQuery = true, Type = \"Text\", IsParameterQueryRequired = true]\n"
      f"\tlineageTag: {tag()}\n\n\tannotation PBI_ResultType = Text\n")
rels = [("Spending.Date", "Calendar.Date"), ("Income.Date", "Calendar.Date"), ("Savings.Date", "Calendar.Date"),
        ("Spending.Category", "Budgets.Category")]
write(SM / "definition/relationships.tmdl", "\n".join(f"relationship {tag()}\n\tfromColumn: {a}\n\ttoColumn: {b}\n" for a, b in rels))
for t, (f, cols) in TABLES.items():
    write(SM / f"definition/tables/{t}.tmdl", table_tmdl(t, f, cols, MEASURES.get(t, [])))
write(SM / "definition/tables/Calendar.tmdl", calendar_tmdl())

# ---------- report ----------
wjson(OUT / f"{NAME}.pbip", {"$schema": f"{SCH}/pbip/pbipProperties/1.0.0/schema.json", "version": "1.0",
                             "artifacts": [{"report": {"path": f"{NAME}.Report"}}], "settings": {"enableAutoRecovery": True}})
wjson(RP / "definition.pbir", {"$schema": f"{SCH}/item/report/definitionProperties/2.0.0/schema.json", "version": "4.0",
                               "datasetReference": {"byPath": {"path": f"../{NAME}.SemanticModel"}}})
wjson(RP / "definition/version.json", {"$schema": f"{SCH}/item/report/definition/versionMetadata/1.0.0/schema.json", "version": "2.0.0"})
tn = THEME.stem
wjson(RP / "definition/report.json", {
    "$schema": f"{SCH}/item/report/definition/report/3.0.0/schema.json",
    "themeCollection": {"baseTheme": {"name": tn, "reportVersionAtImport": {"visual": "2.4.0", "page": "2.0.0", "report": "3.0.0"}, "type": "SharedResources"}},
    "resourcePackages": [{"name": "SharedResources", "type": "SharedResources", "items": [{"name": tn, "path": f"BaseThemes/{tn}.json", "type": "BaseTheme"}]}],
    "settings": {"useStylableVisualContainerHeader": True, "defaultDrillFilterOtherVisuals": True, "allowChangeFilterTypes": True, "useEnhancedTooltips": True}})
dst = RP / "StaticResources/SharedResources/BaseThemes" / THEME.name; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy(THEME, dst)

lit = lambda v: {"expr": {"Literal": {"Value": v}}}
def col(t, c): return {"field": {"Column": {"Expression": {"SourceRef": {"Entity": t}}, "Property": c}}, "queryRef": f"{t}.{c}", "nativeQueryRef": c}
def meas(m, t="Spending"): return {"field": {"Measure": {"Expression": {"SourceRef": {"Entity": t}}, "Property": m}}, "queryRef": f"{t}.{m}", "nativeQueryRef": m}
def agg(t, c, label=None): return {"field": {"Aggregation": {"Expression": {"Column": {"Expression": {"SourceRef": {"Entity": t}}, "Property": c}}, "Function": 0}},
                                   "queryRef": f"Sum({t}.{c})", "nativeQueryRef": label or f"Sum of {c}"}
CARD = {"labels": [{"properties": {"labelDisplayUnits": lit("1D")}}], "categoryLabels": [{"properties": {"show": lit("false")}}]}
DROPDOWN = {"data": [{"properties": {"mode": lit("'Dropdown'")}}]}
counter = [0]; PAGES = []
def page(pid, display):
    d = RP / "definition/pages" / pid
    wjson(d / "page.json", {"$schema": f"{SCH}/item/report/definition/page/2.0.0/schema.json", "name": pid, "displayName": display,
                            "displayOption": "FitToPage", "height": 720, "width": 1280})
    PAGES.append(pid); return d
def vis(pd, vtype, x, y, w, h, roles, title, objects=None):
    counter[0] += 1; name = f"s{counter[0]:02d}" + uuid.uuid4().hex[:12]
    v = {"$schema": VIS, "name": name,
         "position": {"x": x, "y": y, "z": counter[0] * 1000, "width": w, "height": h, "tabOrder": counter[0] * 1000},
         "visual": {"visualType": vtype, "query": {"queryState": {r: {"projections": p} for r, p in roles.items()}},
                    "visualContainerObjects": {"title": [{"properties": {"show": lit("true"), "text": lit(f"'{title}'")}}]},
                    "drillFilterOtherVisuals": True}}
    if objects: v["visual"]["objects"] = objects
    wjson(pd / "visuals" / name / "visual.json", v)

p = page("overview", "Overview")
for i, (m, t) in enumerate([("Income", "Income"), ("Personal spend", "Personal spend"), ("Budget left", "Personal budget left"),
                            ("Stock bought", "Reselling stock bought"), ("Reselling costs", "Reselling costs")]):
    vis(p, "card", 16 + i * 212, 8, 200, 122, {"Values": [meas(m)]}, t, CARD)
vis(p, "slicer", 1076, 8, 188, 122, {"Values": [col("Calendar", "Month")]}, "Month", DROPDOWN)
vis(p, "clusteredBarChart", 16, 142, 616, 300, {"Category": [col("Budgets", "Category")], "Y": [meas("Personal spend"), meas("Budget")]},
    "Personal spending against budget")
vis(p, "columnChart", 648, 142, 616, 300, {"Category": [col("Calendar", "Month")], "Y": [meas("Total spent")], "Series": [col("Spending", "Kind")]},
    "Personal and reselling, by month")
vis(p, "tableEx", 16, 454, 1248, 254, {"Values": [col("Spending", "ID"), col("Spending", "Date"), col("Spending", "Description"), col("Spending", "Kind"),
                                                   col("Spending", "Category"), col("Spending", "Paid with"), agg("Spending", "Amount", "Amount")]},
    "Every payment")

p = page("split", "Personal vs stock")
for i, (m, t) in enumerate([("Personal spend", "Personal"), ("Stock bought", "Stock bought"), ("Stock going back", "Stock going back"),
                            ("Stock refunded", "Stock refunded"), ("Reselling costs", "Reselling costs")]):
    vis(p, "card", 16 + i * 212, 8, 200, 122, {"Values": [meas(m)]}, t, CARD)
vis(p, "slicer", 1076, 8, 188, 122, {"Values": [col("Calendar", "Month")]}, "Month", DROPDOWN)
vis(p, "donutChart", 16, 142, 400, 300, {"Category": [col("Spending", "Kind")], "Y": [meas("Total spent")]}, "Where the money went")
vis(p, "clusteredBarChart", 432, 142, 832, 300, {"Category": [col("Spending", "Category")], "Y": [meas("Total spent")], "Series": [col("Spending", "Kind")]},
    "By category")
vis(p, "clusteredBarChart", 16, 454, 616, 254, {"Category": [col("Spending", "Paid with")], "Y": [meas("Personal spend"), meas("Stock bought")]},
    "By card or account")
vis(p, "clusteredBarChart", 648, 454, 616, 254, {"Category": [col("Spending", "Group")], "Y": [meas("Personal spend")]}, "Personal spending by group")

p = page("savings", "Savings")
for i, (m, t) in enumerate([("LISA balance", "LISA balance (latest check)"), ("LISA growth since first check", "LISA growth since first check")]):
    vis(p, "card", 16 + i * 636, 8, 612, 122, {"Values": [meas(m)]}, t, CARD)
vis(p, "lineChart", 16, 142, 1248, 400, {"Category": [col("Savings", "Date")], "Y": [agg("Savings", "Balance", "Balance")], "Series": [col("Savings", "Account")]},
    "Savings balances over time")

wjson(RP / "definition/pages/pages.json", {"$schema": f"{SCH}/item/report/definition/pagesMetadata/1.0.0/schema.json", "pageOrder": PAGES, "activePageName": PAGES[0]})
print("built", OUT)
