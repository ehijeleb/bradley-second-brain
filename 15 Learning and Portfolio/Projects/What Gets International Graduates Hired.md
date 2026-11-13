---
type: project
area: learning
status: done
deadline: 
waiting_on: 
repo: 
---
# What Gets International Graduates Hired

> [!info] Snapshot
> **What:** Tableau Public dashboard asking what actually gets an international graduate hired. A second portfolio piece; [[Money Buys Points]] stays the main one for the Data School application.
> **Who:** Bradley.
> **Where things live:** [Tableau Public](https://public.tableau.com/app/profile/bradley.duke/viz/WhatGetsInternationalGraduatesHired/GraduateHiring). Data and notes in Bradley's Tableau Claude project.

## Optional improvements
Marked finished, but these would strengthen it:
- [ ] Fix the statistics (Bradley's wish, not urgent)
- [ ] Rewrite the default tooltips
- [ ] Replace Q1's 14 near-identical grey bars with a single dot strip
- [ ] Decide how to handle the synthetic, rule-generated data (maybe reframe as "I found the hidden hiring rule")
- [ ] Move key text out of the background image so it's editable and screen-reader friendly

## Open questions
- Dataset source, link and time period not recorded. Start date not known.
- Filters and interactivity not recorded.
- Finished, or still improving?

## Question and data
- **Dataset:** `dataset.csv` (from `archive.zip`), 300,000 synthetic international graduate records, loaded as a 9-column xlsx. Salaries labelled GBP as an assumption, since the source gives no currency.
- **Calculated fields:** Employed, Employment Rate, Has Advanced Degree, Has Strong Language, Has Edge, Keys Held, Keys Label, Graduation Window, Salary if Employed, Status Share. "Edge" means 2 of: top-ranked university, internship, graduated within 2 years. Medians cover employed graduates only.
- **Layout:** fixed 1200 x 2420, floating. Navy background image with cards, icons and headings, 8 live sheets on top. KPI strip, then five question sections (subject and home country, the three keys, who gets stuck, graduation window, median pay by qualification). Phone layout deleted so Tableau Public shows desktop. Alt text added.

## Key findings
- 52% employed, 25% back in education, 23% unemployed.
- Every subject and home country sits at 52% employed, so who they are doesn't decide it.
- Three keys decide it: an advanced degree, strong language (Advanced / Fluent) and an edge. Holding 0 / 1 / 2 / 3 keys means 4% / 34% / 84% / 100% employed. 9% hold all three, 16% none.
- Employment falls from 67% to 46% after year 2.
- Median pay (employed): Diploma £32.8K, Bachelor's £41.8K, Master's £57.9K, PhD £86.9K.
- **Caveat:** the data is synthetic and rule-generated (identical 52%s, a clean 100%). A reviewer will spot this, so own it.

## Decisions
- Headings and KPI text baked into a background image with live sheets floated on top, to get the Inter font and card design on Tableau Public.
- Design modelled on DS60 finalists' vizzes (navy page, rounded cards, question headings, KPI strip, section bands).

## Status log
- 09-11-2026: last worked on. Self-score 8/8/7/8/6/6/7 (point of view, story flow, chart choice, design craft, analytical depth, personality, technical polish).
- 13-11-2026: imported from Bradley's Tableau Claude project. Bradley wants to fix the statistics at some point; not urgent.

## Links
- [Tableau Public](https://public.tableau.com/app/profile/bradley.duke/viz/WhatGetsInternationalGraduatesHired/GraduateHiring)
- [[Portfolio Projects]]

> [!warning] No secrets
> Never paste passwords, account numbers, login details or API keys here. Note where they live instead.
