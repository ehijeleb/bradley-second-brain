"""Generate the Reselling dashboard as a Power BI project (PBIP: TMDL model + PBIR report)."""
import json, pathlib, shutil, sys, uuid

OUT = pathlib.Path(sys.argv[1])
THEME = pathlib.Path(sys.argv[2])
NAME = "Reselling dashboard"
SM = OUT / f"{NAME}.SemanticModel"
RP = OUT / f"{NAME}.Report"
SCH = "https://developer.microsoft.com/json-schemas/fabric"
VIS_SCHEMA = f"{SCH}/item/report/definition/visualContainer/2.4.0/schema.json"

if OUT.exists():
    shutil.rmtree(OUT)

def tag():
    return str(uuid.uuid4())

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")

def wjson(path, obj):
    write(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

# ---------------- semantic model (TMDL) ----------------
GBP = r"\£#,0.00;-\£#,0.00;\£#,0.00"
PCT = "0.0%;-0.0%;0.0%"
DATE = "dd-mm-yyyy"

ITEM_COLS = [  # name, model type, M type, format, summarize
    ("Item ID", "string", "type text", None, "none"),
    ("Item", "string", "type text", None, "none"),
    ("Category", "string", "type text", None, "none"),
    ("Shop", "string", "type text", None, "none"),
    ("Paid with", "string", "type text", None, "none"),
    ("State", "string", "type text", None, "none"),
    ("Bought", "dateTime", "type date", DATE, "none"),
    ("Cost", "decimal", "Currency.Type", GBP, "sum"),
    ("Sold", "dateTime", "type date", DATE, "none"),
    ("Price", "decimal", "Currency.Type", GBP, "sum"),
    ("Fees", "decimal", "Currency.Type", GBP, "sum"),
    ("Postage", "decimal", "Currency.Type", GBP, "sum"),
    ("Platform", "string", "type text", None, "none"),
    ("Refunded", "dateTime", "type date", DATE, "none"),
    ("Profit", "decimal", "Currency.Type", GBP, "sum"),
    ("Margin", "double", "type number", PCT, "none"),
    ("Days held", "int64", "Int64.Type", "0", "none"),
]
EXP_COLS = [
    ("Date", "dateTime", "type date", DATE, "none"),
    ("Expense", "string", "type text", None, "none"),
    ("Type", "string", "type text", None, "none"),
    ("Amount", "decimal", "Currency.Type", GBP, "sum"),
]

MEASURES = [  # name, DAX, format
    ("Spent", "SUM ( Items[Cost] )", GBP),
    ("Items bought", "COUNTROWS ( Items )", "0"),
    ("Items held", 'CALCULATE ( COUNTROWS ( Items ), Items[State] IN { "in stock", "listed" } )', "0"),
    ("Capital tied up", 'CALCULATE ( SUM ( Items[Cost] ), Items[State] IN { "in stock", "listed" } )', GBP),
    ("Refunds due", 'CALCULATE ( SUM ( Items[Cost] ), Items[State] = "returning" )', GBP),
    ("Held over 30 days", "CALCULATE ( [Items held], Items[Days held] > 30 )", "0"),
    ("Items sold", 'CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold", USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )', "0"),
    ("Revenue", "CALCULATE ( SUM ( Items[Price] ), USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )", GBP),
    ("Gross profit", "CALCULATE ( SUM ( Items[Profit] ), USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )", GBP),
    ("Cost of sold", 'CALCULATE ( SUM ( Items[Cost] ), Items[State] = "sold", USERELATIONSHIP ( Calendar[Date], Items[Sold] ) )', GBP),
    ("Margin %", "DIVIDE ( [Gross profit], [Cost of sold] )", PCT),
    ("Avg days to sell", 'CALCULATE ( AVERAGE ( Items[Days held] ), Items[State] = "sold" )', "0.0"),
    ("Other costs", "SUM ( Expenses[Amount] )", GBP),
    ("Net profit", "[Gross profit] - [Other costs]", GBP),
    ("Sell-through %", 'DIVIDE ( CALCULATE ( COUNTROWS ( Items ), Items[State] = "sold" ), CALCULATE ( COUNTROWS ( Items ), Items[State] IN { "in stock", "listed", "sold" } ) )', PCT),
]

def q(name):
    """Quote a TMDL object name if it isn't a plain identifier."""
    return name if name.replace("_", "").isalnum() else "'" + name.replace("'", "''") + "'"

def column_block(name, dtype, fmt, summ, source):
    lines = [f"\tcolumn {q(name)}", f"\t\tdataType: {dtype}"]
    if fmt:
        lines.append(f"\t\tformatString: {fmt}")
    lines += [f"\t\tlineageTag: {tag()}", f"\t\tsummarizeBy: {summ}", f"\t\tsourceColumn: {source}", "",
              "\t\tannotation SummarizationSetBy = Automatic", ""]
    return lines

def csv_partition(table, file, cols):
    types = ", ".join('{"%s", %s}' % (c[0], c[2]) for c in cols)
    m = [
        "let",
        f'    Source = Csv.Document(File.Contents(#"Exports folder" & "{file}"), [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]),',
        "    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),",
        '    Blanks = Table.TransformColumns(Promoted, {}, each if _ = "" then null else _),',
        f'    Typed = Table.TransformColumnTypes(Blanks, {{{types}}}, "en-GB")',
        "in",
        "    Typed",
    ]
    out = [f"\tpartition {q(table)} = m", "\t\tmode: import", "\t\tsource ="]
    out += ["\t\t\t\t" + l for l in m]
    return out + [""]

def csv_table(table, file, cols, measures=()):
    lines = [f"table {q(table)}", f"\tlineageTag: {tag()}", ""]
    for name, dax, fmt in measures:
        lines += [f"\tmeasure {q(name)} = {dax}", f"\t\tformatString: {fmt}", f"\t\tlineageTag: {tag()}", ""]
    for name, dtype, _m, fmt, summ in cols:
        lines += column_block(name, dtype, fmt, summ, name)
    lines += csv_partition(table, file, cols)
    lines += ["\tannotation PBI_ResultType = Table", ""]
    return "\n".join(lines)

def calendar_table():
    cols = [
        ("Date", "dateTime", DATE, None),
        ("Month", "string", None, "Month number"),
        ("Month number", "int64", "0", None),
        ("Week starting", "dateTime", DATE, None),
    ]
    lines = ["table Calendar", f"\tlineageTag: {tag()}", "\tdataCategory: Time", ""]
    for name, dtype, fmt, sort in cols:
        lines += [f"\tcolumn {q(name)}", f"\t\tdataType: {dtype}"]
        if name == "Date":
            lines.append("\t\tisKey")
        if fmt:
            lines.append(f"\t\tformatString: {fmt}")
        lines += [f"\t\tlineageTag: {tag()}", "\t\tsummarizeBy: none", f"\t\tsourceColumn: [{name}]"]
        if sort:
            lines.append(f"\t\tsortByColumn: {q(sort)}")
        lines += ["", "\t\tannotation SummarizationSetBy = Automatic", ""]
    lines += [
        "\tpartition Calendar = calculated",
        "\t\tmode: import",
        "\t\tsource = ```",
        "\t\t\t\tADDCOLUMNS (",
        "\t\t\t\t    CALENDAR ( DATE ( 2026, 11, 1 ), DATE ( 2027, 12, 31 ) ),",
        '\t\t\t\t    "Month", FORMAT ( [Date], "mmm yyyy" ),',
        '\t\t\t\t    "Month number", YEAR ( [Date] ) * 100 + MONTH ( [Date] ),',
        '\t\t\t\t    "Week starting", [Date] - WEEKDAY ( [Date], 2 ) + 1',
        "\t\t\t\t)",
        "\t\t\t\t```",
        "",
        "\tannotation PBI_Id = " + uuid.uuid4().hex,
        "",
    ]
    return "\n".join(lines)

wjson(SM / "definition.pbism", {
    "$schema": f"{SCH}/item/semanticModel/definitionProperties/1.0.0/schema.json",
    "version": "4.0", "settings": {}})
write(SM / "definition" / "database.tmdl", "database\n\tcompatibilityLevel: 1550\n")
write(SM / "definition" / "model.tmdl", "\n".join([
    "model Model",
    "\tculture: en-GB",
    "\tdefaultPowerBIDataSourceVersion: powerBI_V3",
    "\tsourceQueryCulture: en-GB",
    "\tdataAccessOptions",
    "\t\tlegacyRedirects",
    "\t\treturnErrorValuesAsNull",
    "",
    'annotation PBI_QueryOrder = ["Exports folder","Items","Expenses"]',
    "",
    "annotation __PBI_TimeIntelligenceEnabled = 0",
    "",
    'annotation PBI_ProTooling = ["DevMode"]',
    "",
    "ref table Items",
    "ref table Expenses",
    "ref table Calendar",
    "",
    "",
]))
write(SM / "definition" / "expressions.tmdl", "\n".join([
    "expression 'Exports folder' = \"C:\\Users\\hp\\bradleys-brain\\20 Reselling\\Exports\\\" meta [IsParameterQuery = true, Type = \"Text\", IsParameterQueryRequired = true]",
    f"\tlineageTag: {tag()}",
    "",
    "\tannotation PBI_ResultType = Text",
    "",
]))
write(SM / "definition" / "relationships.tmdl", "\n".join([
    f"relationship {tag()}",
    "\tfromColumn: Items.Bought",
    "\ttoColumn: Calendar.Date",
    "",
    f"relationship {tag()}",
    "\tisActive: false",
    "\tfromColumn: Items.Sold",
    "\ttoColumn: Calendar.Date",
    "",
    f"relationship {tag()}",
    "\tfromColumn: Expenses.Date",
    "\ttoColumn: Calendar.Date",
    "",
]))
write(SM / "definition" / "tables" / "Items.tmdl", csv_table("Items", "Items.csv", ITEM_COLS, MEASURES))
write(SM / "definition" / "tables" / "Expenses.tmdl", csv_table("Expenses", "Expenses.csv", EXP_COLS))
write(SM / "definition" / "tables" / "Calendar.tmdl", calendar_table())

# ---------------- report (PBIR) ----------------
wjson(OUT / f"{NAME}.pbip", {
    "$schema": f"{SCH}/pbip/pbipProperties/1.0.0/schema.json",
    "version": "1.0",
    "artifacts": [{"report": {"path": f"{NAME}.Report"}}],
    "settings": {"enableAutoRecovery": True}})
wjson(RP / "definition.pbir", {
    "$schema": f"{SCH}/item/report/definitionProperties/2.0.0/schema.json",
    "version": "4.0",
    "datasetReference": {"byPath": {"path": f"../{NAME}.SemanticModel"}}})
wjson(RP / "definition" / "version.json", {
    "$schema": f"{SCH}/item/report/definition/versionMetadata/1.0.0/schema.json", "version": "2.0.0"})
theme_name = THEME.stem
wjson(RP / "definition" / "report.json", {
    "$schema": f"{SCH}/item/report/definition/report/3.0.0/schema.json",
    "themeCollection": {"baseTheme": {"name": theme_name,
                                      "reportVersionAtImport": {"visual": "2.4.0", "page": "2.0.0", "report": "3.0.0"},
                                      "type": "SharedResources"}},
    "resourcePackages": [{"name": "SharedResources", "type": "SharedResources",
                          "items": [{"name": theme_name, "path": f"BaseThemes/{theme_name}.json", "type": "BaseTheme"}]}],
    "settings": {"useStylableVisualContainerHeader": True, "defaultDrillFilterOtherVisuals": True,
                 "allowChangeFilterTypes": True, "useEnhancedTooltips": True},
})
dst = RP / "StaticResources" / "SharedResources" / "BaseThemes" / THEME.name
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(THEME, dst)

def lit(v):
    return {"expr": {"Literal": {"Value": v}}}

def col(table, c):
    return {"field": {"Column": {"Expression": {"SourceRef": {"Entity": table}}, "Property": c}},
            "queryRef": f"{table}.{c}", "nativeQueryRef": c}

def meas(m, table="Items"):
    return {"field": {"Measure": {"Expression": {"SourceRef": {"Entity": table}}, "Property": m}},
            "queryRef": f"{table}.{m}", "nativeQueryRef": m}

def agg(table, c, fn=0, label=None):
    names = {0: "Sum", 1: "Avg", 3: "Min", 4: "Max"}
    return {"field": {"Aggregation": {"Expression": {"Column": {"Expression": {"SourceRef": {"Entity": table}}, "Property": c}},
                                      "Function": fn}},
            "queryRef": f"{names[fn]}({table}.{c})", "nativeQueryRef": label or f"{names[fn]} of {c}"}

def state_filter(states):
    return {"filters": [{
        "name": "f" + uuid.uuid4().hex[:18],
        "field": {"Column": {"Expression": {"SourceRef": {"Entity": "Items"}}, "Property": "State"}},
        "type": "Categorical",
        "filter": {"Version": 2,
                   "From": [{"Name": "i", "Entity": "Items", "Type": 0}],
                   "Where": [{"Condition": {"In": {
                       "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "i"}}, "Property": "State"}}],
                       "Values": [[{"Literal": {"Value": f"'{s}'"}}] for s in states]}}}]},
        "howCreated": "User"}]}

counter = {"n": 0}

def visual(page_dir, vtype, x, y, w, h, roles, title, filters=None, extra_objects=None):
    counter["n"] += 1
    name = f"v{counter['n']:02d}" + uuid.uuid4().hex[:12]
    v = {
        "$schema": VIS_SCHEMA,
        "name": name,
        "position": {"x": x, "y": y, "z": counter["n"] * 1000, "width": w, "height": h, "tabOrder": counter["n"] * 1000},
        "visual": {
            "visualType": vtype,
            "query": {"queryState": {role: {"projections": projs} for role, projs in roles.items()}},
            "visualContainerObjects": {"title": [{"properties": {"show": lit("true"), "text": lit(f"'{title}'")}}]},
            "drillFilterOtherVisuals": True,
        },
    }
    if extra_objects:
        v["visual"]["objects"] = extra_objects
    if filters:
        v["filterConfig"] = filters
    wjson(page_dir / "visuals" / name / "visual.json", v)

PAGES = []

def page(pid, display):
    d = RP / "definition" / "pages" / pid
    wjson(d / "page.json", {"$schema": f"{SCH}/item/report/definition/page/2.0.0/schema.json",
                            "name": pid, "displayName": display, "displayOption": "FitToPage",
                            "height": 720, "width": 1280})
    PAGES.append(pid)
    return d

# Overview
p = page("overview", "Overview")
cards = ["Net profit", "Capital tied up", "Refunds due", "Items held", "Sell-through %"]
for i, m in enumerate(cards):
    visual(p, "card", 16 + i * 252, 12, 240, 110, {"Values": [meas(m)]}, m)
visual(p, "barChart", 16, 134, 616, 290,
       {"Category": [col("Items", "Category")], "Y": [meas("Spent")], "Series": [col("Items", "State")]},
       "Where the money went (spent by category and state)")
visual(p, "clusteredColumnChart", 648, 134, 616, 290,
       {"Category": [col("Calendar", "Month")], "Y": [meas("Gross profit"), meas("Other costs")]},
       "Profit and other costs by month")
visual(p, "tableEx", 16, 436, 1000, 272,
       {"Values": [col("Items", "Item ID"), col("Items", "Item"), col("Items", "Shop"), col("Items", "Paid with"),
                   col("Items", "State"), agg("Items", "Cost", 0, "Cost"), col("Items", "Days held")]},
       "Stock and items going back", filters=state_filter(["in stock", "listed", "returning"]))
visual(p, "slicer", 1032, 436, 232, 130, {"Values": [col("Items", "Paid with")]}, "Paid with")
visual(p, "slicer", 1032, 578, 232, 130, {"Values": [col("Items", "Category")]}, "Category")

# Sales
p = page("sales", "Sales")
visual(p, "clusteredBarChart", 16, 12, 616, 330,
       {"Category": [col("Items", "Platform")], "Y": [meas("Gross profit")], "Tooltips": [meas("Margin %"), meas("Items sold")]},
       "Gross profit by platform")
visual(p, "scatterChart", 648, 12, 616, 330,
       {"Category": [col("Items", "Item ID")], "X": [agg("Items", "Cost", 0, "Cost")],
        "Y": [agg("Items", "Profit", 0, "Profit")], "Series": [col("Items", "Category")]},
       "Cost against profit (one dot per sold item)", filters=state_filter(["sold"]))
visual(p, "tableEx", 16, 354, 1248, 354,
       {"Values": [col("Items", "Item ID"), col("Items", "Item"), col("Items", "Platform"), col("Items", "Bought"),
                   col("Items", "Sold"), col("Items", "Days held"), agg("Items", "Price", 0, "Price"),
                   agg("Items", "Profit", 0, "Profit"), col("Items", "Margin")]},
       "Sold items", filters=state_filter(["sold"]))

wjson(RP / "definition" / "pages" / "pages.json", {
    "$schema": f"{SCH}/item/report/definition/pagesMetadata/1.0.0/schema.json",
    "pageOrder": PAGES, "activePageName": PAGES[0]})
print("built", OUT)
