---
type: module
area: study
code: 
status: active
---
# {{title}}

> [!info] Snapshot
> **Lecturer / tutor:** 
> **Assessment split:** 
> **Course page:** 

## Assessments
_Any note in this folder with `type: assessment` shows up here._
```base
filters:
  and:
    - 'type == "assessment"'
    - file.inFolder(this.file.folder)
views:
  - type: table
    name: Assessments
    order:
      - file.name
      - deadline
      - status
    sort:
      - property: deadline
        direction: ASC
```

## Weeks
_One line per week: the key reading and the one idea worth keeping._
- 

## Key ideas
- 

## Status log
- {{date:DD-MM-YYYY}}: hub created
