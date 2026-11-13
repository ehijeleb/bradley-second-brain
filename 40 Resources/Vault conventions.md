---
type: reference
---
# Vault conventions

## Folders
| Folder | What goes in it |
| --- | --- |
| `00 Inbox` | Anything captured in a rush. Empty it daily. |
| `01 Daily` | Daily notes (Ctrl/Cmd+P, "Open today's daily note"). |
| `10 Career` | [[Job Hunt]] (applications in `Applications/`, Excel exports in `Exports/`), [[CV and Interview Prep]], [[Contacts and Recruiters]]. |
| `15 Learning and Portfolio` | [[Skills Roadmap]], [[Portfolio Projects]] (one note per project in `Projects/`). |
| `20 Reselling` | [[Reselling]], [[Stock]], [[Reselling expenses]]. |
| `25 Bershka` | [[Bershka]]: shifts and work notes. |
| `30 Personal` | Finance (the [[Finance]] hub and one note per month), health, trips, admin. |
| `40 Resources` | Reference material not tied to one area. |
| `90 Archive` | Finished or dropped things. Move, don't delete. |
| `Templates` | Insert with Ctrl/Cmd+P, "Templates: Insert template". |
| `Attachments` | Images and PDFs. New pastes land here. |

When something grows past a few notes, give it its own folder and keep the hub inside with the same name.

## Properties
Hubs, modules, assessments and projects have these at the top. They feed [[Home]].

| Property | Values |
| --- | --- |
| `type` | `project`, `area`, `application`, `tracker`, `meeting`, `daily`, `finance`, `reference`, `dashboard` |
| `area` | `career`, `learning`, `reselling`, `work`, `personal` |
| `stage` | applications only: Applied, Interview, Rejected, Offer, Withdrawn (or a specific step) |
| `status` | `active`, `waiting`, `paused`, `done` |
| `deadline` | `YYYY-MM-DD` (blank if none) |
| `waiting_on` | who or what you're blocked on (with `status: waiting`) |
| `repo` | GitHub URL, for code projects |

## Routine
- **Daily (2 min):** open today's note, write the top 3, dump thoughts into Captured.
- **Evening (5 min):** move anything in Captured or `00 Inbox` into its hub. Tick tasks.
- **Weekly (15 min):** go through [[Home]]. Update `status` and `deadline` on anything stale, archive finished things, add next week's deadlines.

## Rules
- No secrets: no passwords, API keys, account or card numbers, ID numbers. Write where they live instead.
- Link generously: `[[Project name]]` in a daily note is what makes the hub's backlinks a history of that project.
- Prefer updating a hub's Status log over starting a new note.
- Write dates in note text as DD-MM-YYYY (`- 25-10-2026: hub created`). Properties and date-named files stay year-first, because that's what sorts properly and feeds [[Home]].
