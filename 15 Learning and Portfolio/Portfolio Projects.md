---
type: area
area: learning
status: active
---
# Portfolio Projects

> [!info] Snapshot
> **What this covers:** data projects that show employers what Bradley can do. Each project gets its own note in `15 Learning and Portfolio/Projects/` from the **Project** template (`type: project`, `area: learning`, with a `repo` link if it's on GitHub), so it shows under Active projects on [[Home]].
> **Good projects for applications:** a clear question, a real dataset, cleaning, analysis, a chart or dashboard, and a short write-up of what was found.

> [!todo] To fill in
> First time in: Bradley's existing and planned projects (see [[Start here]]).

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
Suggestions only, to pick from or ignore. They play to the maths and sports science background:
- Football or other sports performance data (for example, what predicts results, or player comparison).
- A personal fitness or training dataset analysed over time (links with [[Fitness]]).
- Reselling profitability: what sells, margins by platform and category (data from [[Reselling]]).
- A Power BI or Tableau dashboard on a public dataset.

## Status log
- 13-11-2026: hub created
