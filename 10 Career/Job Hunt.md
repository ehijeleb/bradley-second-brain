---
type: project
area: career
status: active
deadline: 
waiting_on: 
---
# Job Hunt

> [!info] Snapshot
> **What:** Bradley's search for a graduate role on a finance or technology route. **Primary target: data analyst.** Also open to adjacent roles where maths, data and sport or performance analysis are valued (data science, BI, sports or performance analysis, betting and trading analytics, insurance, actuarial, consultancies with sport or health clients).
> **Background:** 2:1 BSc Mathematics and Sports Science. Currently a sales assistant at [[Bershka]]. Based in London, willing to relocate.
> **Where things live:** one note per application in `10 Career/Applications/` (from the **Application** template). CVs and cover letters in [[CV and Interview Prep]]. People in [[Contacts and Recruiters]]. Skills in [[Skills Roadmap]], evidence in [[Portfolio Projects]].
> **Excel copy:** ask Claude for "an Excel export of my applications". It writes `10 Career/Exports/Application tracker.xlsx` from the notes (the notes are the main copy).

> [!todo] To fill in
> Bradley has already started applying. First time in: add each application so far (see [[Start here]]).

## Live applications
```base
filters:
  and:
    - type == "application"
    - file.inFolder("10 Career/Applications")
views:
  - type: table
    name: Live
    filters:
      and:
        - status != "done"
    order:
      - app_id
      - company
      - role
      - stage
      - date_applied
      - closing_date
      - next_step
      - deadline
      - fit_score
    sort:
      - property: app_id
        direction: ASC
  - type: table
    name: All
    order:
      - app_id
      - company
      - role
      - stage
      - date_applied
      - fit_score
      - cv_version
    sort:
      - property: app_id
        direction: ASC
```

## Next actions
- [ ] Log every application made so far (APP-001 onwards)
- [ ] Draft a target list of 10 to 15 less saturated employers (see "Suggesting companies")

## Waiting on
- [[APP-002 The Data School - Data School]]: outcome of the application.
- [[APP-001 ION Asset Architecture - Trading Operations Assistant]]: Datatech to send the full job description.

## Decisions
- 13-11-2026: tracker kept as notes in this vault, with an Excel export on request, so it syncs and shows on [[Home]].

## Status log
- 13-11-2026: hub created
- 13-11-2026: logged APP-001 ION Asset Architecture (via Datatech), Trading Operations Assistant, stage Recruiter screening. More applications still to add.
- 13-11-2026: logged APP-002 The Data School, stage Applied. Date applied not known yet.

---

## Rules for Claude

### Tone
Concise and direct. Plain, efficient answers. Short lists and headings where they help scanning, prose for reasoning. Flag tradeoffs and uncertainty rather than making silent choices. No flattery: honest assessment is more useful than encouragement. No em dashes.

### Assessing a job advert
When Bradley pastes an advert, give:
1. **Fit score out of 10**, with a one-line reason. Don't inflate scores.
2. **Requirements he clearly meets**, each with the evidence from his degree or experience.
3. **Gaps**, stated honestly, each marked as a dealbreaker, something to address in the application, or something to learn (link to [[Skills Roadmap]]).
4. **Realistic graduate target?** Or does it want experience he doesn't have yet.
5. **Two or three tailoring suggestions** for his CV or cover letter.

If a role is a poor fit, say so and explain why.

### Suggesting companies
Prioritise employers that are:
- hiring graduates or early-career staff in data, analytics, finance or technology;
- less saturated than the big household-name schemes, but big enough to have structured graduate progression;
- plausibly relevant to maths and sports science (sports analytics, performance data, betting and trading analytics, insurance, actuarial, consultancies with sport or health clients).

For each: the likely role type, why it could suit him, and how competitive it's likely to be. Flag anything you're not confident in and tell him to check the company's careers page.

**Accuracy:** schemes, deadlines and hiring change often. Search the web for current openings, deadlines and company details before recommending, and cite sources. Never present a role as open unless you've confirmed it.

### Rewriting CVs and cover letters
- Base every change on his real experience. Never invent achievements, skills, qualifications or metrics. If a requirement isn't evidenced, say so rather than writing it in.
- Mirror the advert's key terms where they genuinely match.
- Lead with the most relevant evidence; cut or shorten what doesn't support the role.
- CV: one page for graduate roles unless he says otherwise. Plain, specific wording; quantified outcomes only where he's given the figures.
- Cover letter: one page, each paragraph tied to a specific requirement in the advert. No generic phrases ("passionate about", "team player").
- Missing information (for example a project result): ask, don't estimate.
- Show the rewritten version in full, then brief bullets on the main changes and why.
- Flag judgement calls (for example reframing a sports science project as data work) so he can decide.
- Save versions in [[CV and Interview Prep]] with a version name (`CV-v1`, `CV-v2 data analyst`...) so applications can record which was used.

### Tracking applications
- **Only log a role once Bradley confirms he's applied.** Don't log roles he's considering.
- Each application gets a unique ID, `APP-001`, `APP-002`..., continuing from the highest existing number. Never reuse one.
- Create a note in `10 Career/Applications/` named `APP-001 Company - Role`, from `Templates/Application.md`, with these fields: ID, date applied, company, role title, location, advert link, closing date, fit score (from the assessment), stage (default "Applied"), CV version used, cover letter (yes or no), next step, notes.
- Closing date from the advert. If it isn't stated, leave it blank and ask.
- `stage` is one of Applied, Interview, Rejected, Offer, Withdrawn (or a more specific step like "Online test" or "Final interview"). Ask him for the stage when he updates you; never guess.
- Put the date of the next step or follow-up in `deadline` so it shows on [[Home]]. When an application ends (Rejected, Withdrawn, or an offer accepted or declined), set `status: done`.
- Before adding, check for a duplicate company and role and flag it.
- After adding or changing an application, add a dated line to this hub's Status log, and offer an updated Excel export (see Snapshot).
