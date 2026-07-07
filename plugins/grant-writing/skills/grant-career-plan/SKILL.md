---
name: grant-career-plan
description: Develop the career-development components of a training or career award — candidate background and career goals, training gap analysis, career development activities and timeline, mentor and advisory team assembly, mentor statements, institutional commitment requirements, referee letter strategy, and the RCR training plan. Use whenever the grant is a career development award (NIH K01/K08/K23/K25/K99-R00, NSF CAREER, foundation career or early-career awards), or the user mentions a career plan, candidate statement, mentoring team, mentor statement, training plan, protected time, or K-award reference letters.
---

# Career Development Plan

On a career award the applicant *is* the project: reviewers fund a trajectory, not just a study, and they weight the candidate, the mentoring, and the training plan as heavily as the science. The document set stands or falls on one coherence chain: **stated training gaps → chosen development activities → mentor expertise covering each gap → research plan as the training vehicle → the five-year career goal**. Every classic career-award critique is a break in that chain — a named training area no mentor covers, an activity unconnected to the goal, a research plan sized for a funded lab rather than one trainee.

Read `00_admin/project-config.md` first (run `grant-setup` if missing) and confirm the award type is recorded as career-development. Career-award files live in `10_career/` (add the folder to the standard structure if absent), versioned per the schema. Agency differences are substantial — read `references/agency-variants.md` for the mechanism in play before drafting.

## Maintain the training map

Create `10_career/training-map.md` early: one row per training gap — the gap, the activity that closes it, the mentor or resource that covers it, the aim that exercises it, the year it happens. This table is the audit instrument for the whole document set; every section below reads from and writes to it, and the final coherence check walks it row by row.

## Step 1 — Candidate and career goals

Elicit: career stage and prior training, key publications, and the specific independent identity five years out ("an independent PI studying X using Y approaches" — a goal a reviewer can picture, not "continue growing as a scientist"). Draft the candidate background as a trajectory narrative, not CV prose: prior work framed as deliberate preparation, gaps named plainly as the next steps. Candidates often resist stating gaps; push back — on a career award an applicant with no training gaps has no case for the mechanism, and reviewers read honest gap analysis as self-awareness, not weakness.

## Step 2 — Gap analysis and development activities

Keep gaps concrete and few (typically 3–4): specific techniques or fields, plus professional skills (lab leadership, grant and personnel management, responsible mentoring). Every activity maps to a gap and carries a time allocation and year — named coursework, technique training in a specific lab, structured writing programs. Generic filler ("attend seminars," "read the literature") carries no weight and dilutes the real plan. Build the timeline with training front-loaded, research effort growing across years, and explicit independence markers: first corresponding-author paper, first R01 (or equivalent) submission, transition milestones.

## Step 3 — Mentor team

The team is designed against the gap list, not assembled from availability:

- **Primary mentor**: active funding, a mentoring track record with named placed trainees, and expertise that *overlaps but is not identical to* the candidate's independent direction — if the plan is indistinguishable from the mentor's program, reviewers ask what the candidate will own. Address the eventual scientific separation explicitly.
- **Co-mentors and advisors**: each mapped to a specific gap in the training map. A gap with no covering mentor, or a mentor with no assigned gap, is the flag reviewers find first.
- **Structure**: meeting cadences (primary mentor weekly/biweekly; advisory committee 1–2×/year with stated milestones reviewed), and who adjudicates if advice conflicts.

Draft the **mentor statement** here — it is a scored plan, not a courtesy letter: the mentor's assessment of the candidate, the plan for this candidate (cadence, milestones, transition-to-independence steps, what the mentor cedes to the candidate and when), lab/data resources committed, and the mentor's mentoring history. Write it in the mentor's plausible voice; follow `grant-letters-of-support` drafting conventions (early drafts, tracker, signer edits), but this document is owned here.

## Step 4 — Institutional commitment and referees

The chair/institutional letter has required content, not sentiment: the protected-effort percentage stated numerically (typically 75% for NIH K mechanisms; some clinician tracks 50% — the FOA rules), space, resources, reduced clinical/teaching load, and a statement the position is not contingent on the award. For NSF CAREER the departmental letter has solicitation-prescribed elements — deviation risks return without review.

For NIH K awards, plan the **referee letters** at project start: 3–5 letters submitted independently by referees through eRA Commons by the deadline, from people who can speak to the candidate's potential and are *not* the mentors or others named in the application. Missing letters can bar review, and referees are the least controllable dependency in the whole application — choose them, brief them with a one-page summary of the training map, and set them a deadline two weeks early (coordinate with the long-lead tracking from `grant-setup`).

## Step 5 — RCR training plan

NIH requires a responsible-conduct-of-research instruction plan described across five components: format, subject matter, faculty participation, duration, and frequency (the working convention is at least eight face-to-face contact hours; online-only does not satisfy it). Describe the candidate's specific participation, not the institution's catalog. Other funders vary — see the variants file.

## Sizing the research plan

The research plan is the training vehicle: scoped to what one trainee can execute, and designed so the aims *exercise the new skills* being trained — an aim requiring only techniques the candidate already has undercuts the training rationale, and an R01-sized plan signals poor calibration (see the career-award note in `grant-specific-aims`'s agency variants; draft with `grant-approach` as usual, with this constraint in the conversation).

## Coherence audit before assembly

Walk the training map row by row: every gap has an activity, a covering mentor, and an aim that uses it; every activity appears in the timeline and, where it costs money, in the budget; the mentor statement's commitments (cadence, resources, milestones) match the candidate's plan verbatim — reviewers cross-read these documents and inconsistencies read as a team that hasn't talked. Then run `grant-mock-review` with the career-award criteria (its references file has the instrument). Record scope or team changes in `00_admin/decision-log.md`.

## References

- `references/agency-variants.md` — NIH K series (mechanisms, effort rules, referee letters, K99/R00 phasing), NSF CAREER (education-plan integration, departmental letter), foundation career awards. Read before drafting for any specific mechanism.
