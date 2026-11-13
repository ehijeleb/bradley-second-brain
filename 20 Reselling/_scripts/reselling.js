// Reselling views, rendered by the Dataview plugin (needs "Enable JavaScript queries").
//
//   dv.view("20 Reselling/_scripts/reselling", { view: "summary" })  profit by month + totals
//   dv.view("20 Reselling/_scripts/reselling", { view: "stock" })    items not sold yet
//   dv.view("20 Reselling/_scripts/reselling", { view: "check" })    lines that need fixing
//
// Data:
//   [[Stock]]               one line per item:
//     - Nike Air Max 90, size 9 [bought:: 02-11-2026] [cost:: 25.00] [from:: Vinted] [state:: listed]
//     when it sells, add:  [sold:: 10-11-2026] [price:: 45.00] [fees:: 2.50] [postage:: 3.20] [platform:: eBay]
//   [[Reselling expenses]]  one line per cost that isn't an item:
//     - 05-11-2026 Postage bags [exp:: Supplies] [amt:: 6.99]
//
// Keep this file synchronous: Dataview rewrites view files that use async syntax.

const VIEW = (typeof input !== "undefined" && input && input.view) || "summary";
const CURRENCY = "£";
const LOCALE = "en-GB";

const money = n => (n < 0 ? "-" : "") + CURRENCY +
  Math.abs(n).toLocaleString(LOCALE, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const num = v => {
  if (v === null || v === undefined || v === "") return null;
  if (typeof v === "number") return v;
  const cleaned = String(v).replace(/[^0-9.\-]/g, "");
  if (!/\d/.test(cleaned)) return null;
  const n = Number(cleaned);
  return Number.isFinite(n) ? n : null;
};
const str = v => (v === null || v === undefined ? "" : String(v).trim());
const label = text => str(text)
  .replace(/[[(][^[\]()]*?::[^[\]()]*[\])]/g, "")
  .replace(/^(\d{2}[-/.]\d{2}[-/.]\d{4}|\d{4}-\d{2}-\d{2})\s*/, "")
  .replace(/\s+/g, " ")
  .trim();

// Returns a JS Date (local midnight) from "DD-MM-YYYY", "YYYY-MM-DD" or a Dataview/Luxon date.
function toDate(v) {
  if (v === null || v === undefined || v === "") return null;
  if (v && typeof v.toJSDate === "function") return v.toJSDate();
  const s = String(v).trim();
  let m = s.match(/^(\d{2})[-/.](\d{2})[-/.](\d{4})/);
  if (m) return new Date(Number(m[3]), Number(m[2]) - 1, Number(m[1]));
  m = s.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (m) return new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]));
  return null;
}
const monthOf = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0");
const monthName = key => {
  const [y, mo] = key.split("-").map(Number);
  return new Date(y, mo - 1, 1).toLocaleString(LOCALE, { month: "long", year: "numeric" });
};
const ddmmyyyy = d => d ? String(d.getDate()).padStart(2, "0") + "-" +
  String(d.getMonth() + 1).padStart(2, "0") + "-" + d.getFullYear() : "";

function lists(name) {
  const page = dv.page("20 Reselling/" + name);
  return page ? page.file.lists.array() : [];
}

const problems = [];

const items = lists("Stock")
  .filter(l => l.cost !== undefined || l.bought !== undefined || l.sold !== undefined)
  .map(l => {
    const it = {
      name: label(l.text) || "(no name)",
      bought: toDate(l.bought),
      cost: num(l.cost),
      from: str(l.from),
      state: str(l.state).toLowerCase(),
      sold: toDate(l.sold),
      price: num(l.price),
      fees: num(l.fees) || 0,
      postage: num(l.postage) || 0,
      platform: str(l.platform),
      line: l.line,
    };
    if (it.cost === null) problems.push(["Stock", it.name, "no cost"]);
    if (l.sold !== undefined && str(l.sold) !== "" && !it.sold) problems.push(["Stock", it.name, "sold date not DD-MM-YYYY"]);
    if (it.sold && it.price === null) problems.push(["Stock", it.name, "sold but no price"]);
    if (!it.sold && it.price !== null) problems.push(["Stock", it.name, "has a price but no sold date"]);
    return it;
  });

const expenses = lists("Reselling expenses")
  .filter(l => l.amt !== undefined || l.exp !== undefined)
  .map(l => {
    const m = str(l.text).match(/^(\d{2}[-/.]\d{2}[-/.]\d{4}|\d{4}-\d{2}-\d{2})/);
    const e = { name: label(l.text), date: m ? toDate(m[1]) : null, amt: num(l.amt), cat: str(l.exp) || "Other" };
    if (!e.date) problems.push(["Expenses", e.name, "line doesn't start with a DD-MM-YYYY date"]);
    if (e.amt === null) problems.push(["Expenses", e.name, "no amount"]);
    return e;
  });

if (VIEW === "summary") {
  const months = {};
  const row = k => months[k] || (months[k] = { sold: 0, sales: 0, cogs: 0, fees: 0, exp: 0 });
  for (const it of items) {
    if (!it.sold || it.price === null) continue;
    const r = row(monthOf(it.sold));
    r.sold += 1; r.sales += it.price; r.cogs += it.cost || 0; r.fees += it.fees + it.postage;
  }
  for (const e of expenses) {
    if (!e.date || e.amt === null) continue;
    row(monthOf(e.date)).exp += e.amt;
  }
  const keys = Object.keys(months).sort().reverse();
  const tot = { sold: 0, sales: 0, cogs: 0, fees: 0, exp: 0 };
  const rows = keys.map(k => {
    const r = months[k];
    for (const f in tot) tot[f] += r[f];
    return [monthName(k), r.sold, money(r.sales), money(r.cogs), money(r.fees), money(r.exp),
      "**" + money(r.sales - r.cogs - r.fees - r.exp) + "**"];
  });
  if (!rows.length) {
    dv.paragraph("No sales or expenses logged yet. Add items to [[Stock]] and costs to [[Reselling expenses]].");
  } else {
    rows.push(["**Total**", tot.sold, money(tot.sales), money(tot.cogs), money(tot.fees), money(tot.exp),
      "**" + money(tot.sales - tot.cogs - tot.fees - tot.exp) + "**"]);
    dv.table(["Month", "Sold", "Sales", "Cost of items sold", "Fees & postage", "Other expenses", "Profit"], rows);
  }
  const unsold = items.filter(it => !it.sold && it.state !== "kept");
  const tied = unsold.reduce((t, it) => t + (it.cost || 0), 0);
  dv.paragraph(`**Stock on hand:** ${unsold.length} item${unsold.length === 1 ? "" : "s"}, ${money(tied)} spent on them.`);
  if (problems.length) dv.paragraph(`⚠ ${problems.length} line(s) need fixing: see "Check these lines" below.`);
}

if (VIEW === "stock") {
  const today = new Date();
  const unsold = items.filter(it => !it.sold && it.state !== "kept")
    .sort((a, b) => (a.bought ? a.bought.getTime() : 0) - (b.bought ? b.bought.getTime() : 0));
  if (!unsold.length) dv.paragraph("Nothing in stock.");
  else dv.table(["Item", "Bought", "Cost", "From", "State", "Days held"], unsold.map(it => [
    it.name, ddmmyyyy(it.bought), it.cost === null ? "" : money(it.cost), it.from, it.state || "in stock",
    it.bought ? Math.floor((today - it.bought) / 86400000) : "",
  ]));
}

if (VIEW === "check") {
  if (!problems.length) dv.paragraph("All lines look fine.");
  else dv.table(["Note", "Item", "Problem"], problems);
}
