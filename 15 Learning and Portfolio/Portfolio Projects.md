---
type: area
area: learning
status: active
---
# Portfolio Projects

> [!info] Snapshot
> **What this covers:** data projects that show employers what Bradley can do. Each project gets its own note in `15 Learning and Portfolio/Projects/` from the **Project** template (`type: project`, `area: learning`, with a `repo` link if it's on GitHub), so it shows under Active projects on [[Home]].
> **Good projects for applications:** a clear question, a real dataset, cleaning, analysis, a chart or dashboard, and a short write-up of what was found.

## Projects
```base
filters:
  and:
    - file.inFolder("15 Learning and Portfolio/Projects")
    - type == "project"
views:
  - type: table
    name: Projects
    order:
      - file.name
      - status
      - deadline
      - repo
      - file.mtime
```

## Ideas
Extensions for [[Money Buys Points]] are listed in that note.
- Graduate dashboard: reframe as "I found the hidden hiring rule" (see [[What Gets International Graduates Hired]]).
Suggestions only, to pick from or ignore. They play to the maths and sports science background:
- Football or other sports performance data (for example, what predicts results, or player comparison).
- A personal fitness or training dataset analysed over time (links with [[Fitness]]).
- Reselling profitability: what sells, margins by platform and category (data from [[Reselling]]).
- A Power BI or Tableau dashboard on a public dataset.

## Status log
- 13-11-2026: hub created
- 13-11-2026: imported [[Money Buys Points]] (in progress, main Data School dashboard) and [[What Gets International Graduates Hired]] (finished) from the Tableau Claude project.
- 16-11-2026: portfolio website ([bradleyduke48-creator.github.io](https://bradleyduke48-creator.github.io/), repo on the `bradleyduke48-creator` GitHub account) redesigned and pushed: white and teal, both Tableau dashboards plus 8 university projects (Commercial Business Analysis and Design of Experiments added), skills listed without levels, Bershka added, reselling left off. Bradley asked for no charts or figures on project cards. Reselling profitability dashboard could go on later as a project.
- 24-11-2026: started [[Reselling Dashboard]], a private Power BI dashboard (not for the portfolio) to learn Power BI on the reselling data.
- 25-11-2026: started [[Spending Dashboard]], a private Power BI dashboard on personal and reselling spending.
