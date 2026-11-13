// Budget views for the Finance folder, rendered by the Dataview plugin.
//
// Month note:  dv.view("30 Personal/Finance/_scripts/finance", { view: "month" })
// Hub note:    dv.view("30 Personal/Finance/_scripts/finance", { view: "year" })
//
// Settings (currency, locale, hourly wage, accounts, wage split, categories and budgets) live in
// the [[Finance]] hub as properties and inline fields. Month notes log one line per payment:
//   - 04-10-2026 Supermarket [cat:: Groceries] [amt:: 23.49] [from:: Current account]
//   - 25-10-2026 Employer [income:: Wages] [amt:: 1500.00]
//
// Keep this file synchronous: Dataview rewrites view files that use async syntax.

const HUB = "Finance";
const VIEW = (typeof input !== "undefined" && input && input.view) || "month";
const NEARLY_THERE = 0.8;

let CURRENCY = "£";
let LOCALE = "en-GB";

const money = n => (n < 0 ? "-" : "") + CURRENCY +
  Math.abs(n).toLocaleString(LOCALE, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const sum = xs => xs.reduce((t, x) => t + x.amt, 0);
const num = v => {
  if (v === null || v === undefined || v === "") return null;
  if (typeof v === "number") return v;
  // Amounts are logged like 23.49; strip currency symbols, spaces and thousands commas.
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

function monthKey(page) {
  const m = page.month;
  if (m && typeof m.toFormat === "function") return m.toFormat("yyyy-MM");
  const s = str(m);
  return /^\d{4}-\d{2}/.test(s) ? s.slice(0, 7) : null;
}

function monthLabel(key) {
  const [y, m] = key.split("-").map(Number);
  return new Date(y, m - 1, 1).toLocaleString(LOCALE, { month: "short", year: "numeric" });
}

function readSettings() {
  const hub = dv.page(HUB);
  if (!hub) return null;
  if (str(hub.currency)) CURRENCY = str(hub.currency);
  if (str(hub.locale)) LOCALE = str(hub.locale);
  const items = Array.from(hub.file.lists);
  const categories = items.filter(i => i.category).map(i => ({
    name: str(i.category),
    group: str(i.group) || "Other",
    budget: num(i.budget) || 0,
  }));
  const accounts = items.filter(i => i.account).map(i => ({ name: str(i.account), pct: num(i.pct) }));
  return {
    wage: num(hub.hourly_wage),
    categories,
    accounts,
    split: accounts.filter(a => a.pct !== null),
  };
}

// Splits a month note's list items into income and expenses, and notes anything malformed.
function readMonth(page, settings) {
  const known = new Set(settings.categories.map(c => c.name));
  const accounts = new Set(settings.accounts.map(a => a.name));
  const income = [], expenses = [], problems = [];
  for (const item of Array.from(page.file.lists)) {
    const what = label(item.text) || "(no description)";
    if (item.income !== undefined && item.income !== null) {
      let amt = num(item.amt);
      if (amt === null && num(item.hours) !== null) {
        const gross = num(item.gross) ?? num(item.hours) * (num(item.rate) ?? settings.wage ?? 0);
        amt = gross - (num(item.deductions) || 0);
      }
      if (amt === null) problems.push(`Income "${what}" has no amount: add [amt:: 0.00].`);
      else income.push({ type: str(item.income), amt });
    } else if (item.cat !== undefined && item.cat !== null) {
      const amt = num(item.amt);
      const cat = str(item.cat);
      if (amt === null) { problems.push(`"${what}" has no amount: add [amt:: 0.00].`); continue; }
      if (!known.has(cat)) problems.push(`"${what}" uses category "${cat}", which isn't in the [[${HUB}]] category list.`);
      const from = str(item.from);
      if (from && accounts.size && !accounts.has(from)) problems.push(`"${what}" is paid from "${from}", which isn't one of the accounts in [[${HUB}]].`);
      expenses.push({ cat, amt });
    } else if (item.amt !== undefined && item.amt !== null) {
      problems.push(`"${what}" has an amount but no [cat:: ] or [income:: ], so it isn't counted.`);
    }
  }
  const wages = sum(income.filter(i => i.type.toLowerCase() === "wages"));
  const moneyIn = sum(income);
  const moneyOut = sum(expenses);
  return { income, expenses, problems, wages, other: moneyIn - wages, moneyIn, moneyOut, left: moneyIn - moneyOut };
}

function status(budget, spent) {
  if (budget === 0) return spent > 0 ? "No budget set" : "–";
  if (Math.abs(spent - budget) < 0.005) return "✅ Spent as planned";
  if (spent > budget) return "❌ Over budget";
  if (spent >= NEARLY_THERE * budget) return "⚠️ Nearly there";
  return "✅ On track";
}

function renderMonth(settings) {
  const page = dv.current();
  const m = readMonth(page, settings);
  const splitTotal = settings.split.reduce((t, a) => t + a.pct, 0);
  if (settings.split.length && Math.round(splitTotal) !== 100) m.problems.push(`The wage split in [[${HUB}]] adds up to ${splitTotal}%, not 100%.`);

  if (m.problems.length) dv.paragraph("**Check these lines:**\n" + m.problems.map(p => `- ⚠️ ${p}`).join("\n"));

  dv.table(["Money in", "Money out", "Left over", "Wages"],
    [[money(m.moneyIn), money(m.moneyOut), money(m.left) + (m.left < 0 ? " ❌" : ""), money(m.wages)]]);
  if (m.left < 0) dv.paragraph("_Negative left over means more went out than came in this month._");

  if (settings.split.length) {
    dv.header(4, "Move your wages like this");
    dv.table(["Account", "%", "Move this month"],
      settings.split.map(a => [a.name, `${a.pct}%`, money(m.wages * a.pct / 100)]));
  }

  dv.header(4, "Spending vs budget");
  const rows = [];
  let budgetTotal = 0;
  for (const c of settings.categories) {
    const spent = sum(m.expenses.filter(e => e.cat === c.name));
    budgetTotal += c.budget;
    rows.push([c.name, c.group, c.budget ? money(c.budget) : "–", money(spent),
      c.budget ? money(c.budget - spent) : "", status(c.budget, spent)]);
  }
  const known = new Set(settings.categories.map(c => c.name));
  const stray = sum(m.expenses.filter(e => !known.has(e.cat)));
  if (stray) rows.push(["Unknown category", "", "–", money(stray), "", "⚠️ Fix the category"]);
  rows.push(["**Total**", "", `**${money(budgetTotal)}**`, `**${money(m.moneyOut)}**`, budgetTotal ? `**${money(budgetTotal - m.moneyOut)}**` : "", ""]);
  dv.table(["Category", "Group", "Budget", "Spent", "Left", "Status"], rows);
}

function renderYear(settings) {
  const months = Array.from(dv.pages())
    .filter(p => p.type === "finance" && monthKey(p) && !p.file.path.startsWith("Templates/"))
    .sort((a, b) => monthKey(a).localeCompare(monthKey(b)));
  if (!months.length) { dv.paragraph("No month notes yet. Create one named `YYYY-MM Budget` here and insert the **Finance month** template."); return; }

  let running = 0;
  const totals = { wages: 0, other: 0, moneyIn: 0, moneyOut: 0, left: 0 };
  const rows = months.map(p => {
    const m = readMonth(p, settings);
    running += m.left;
    for (const k of Object.keys(totals)) totals[k] += m[k];
    const flag = m.problems.length ? " ⚠️" : "";
    return [dv.fileLink(p.file.path, false, monthLabel(monthKey(p))) + flag, money(m.wages), money(m.other),
      money(m.moneyIn), money(m.moneyOut), money(m.left), money(running)];
  });
  rows.push(["**Total**", money(totals.wages), money(totals.other), money(totals.moneyIn),
    money(totals.moneyOut), `**${money(totals.left)}**`, ""]);
  dv.table(["Month", "Wages", "Other income", "Total in", "Spent", "Left over", "Running total"], rows);
  if (rows.some(r => String(r[0]).includes("⚠️"))) dv.paragraph("_⚠️ means that month has lines to check: open it to see which._");
}

const settings = readSettings();
if (!settings) {
  dv.paragraph(`⚠️ Can't find the [[${HUB}]] note, which holds the budget settings.`);
} else if (VIEW === "year") {
  renderYear(settings);
} else {
  renderMonth(settings);
}
