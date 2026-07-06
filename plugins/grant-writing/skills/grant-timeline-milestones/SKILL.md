---
name: grant-timeline-milestones
description: Develop project timelines, milestones, and Gantt charts for grant proposals — mapping aims and tasks to project years, defining go/no-go decision points and deliverables. Use whenever the user mentions timelines, milestones, Gantt charts, project periods, quarters, deliverables schedules, or a reviewer/FOA requires a milestone plan (common for DoD, U-mechanisms, and clinical projects).
---

# Timeline and Milestones

A timeline converts the Approach into a feasibility argument: reviewers use it to judge whether the team can actually execute the plan in the project period. Build it from the Approach's per-aim designs, not aspirationally.

Read `00_admin/project-config.md` (project period, mechanism) and the current Approach drafts. Output goes to `02_research_plan/timeline_v<NN>_<date>_draft.<ext>`; the figure is usually embedded near the end of the Approach.

## Step 1 — Decompose into scheduled units

For each aim, list tasks with duration estimates and dependencies (which tasks are sequential vs parallel, which share personnel or equipment). Include the non-experimental time that plans routinely omit: IRB/IACUC approvals (and DoD HRPO/ACURO second-level review, which adds months), hiring and training, animal colony expansion, equipment procurement, data analysis, and manuscript/report writing.

## Step 2 — Sanity-check the load

Cross-check against the budget's effort allocations: a year in which three aims run heavy experiments simultaneously with 1.2 FTE of staff is a factual inconsistency — report it and help rebalance (stagger aims, adjust scope, or revisit effort). Front-loading everything into years 1–2 and back-loading "analysis and dissemination" is a recognized weak pattern; so is a timeline with no slack for failure and iteration. Start year 1 with the ramp reviewers expect — hiring, approvals, training: heavy experimental milestones in the first two quarters read as naive and undercut the credibility of everything after them. The timeline is where "overambitious" critiques get anchored; a visibly staggered, slack-bearing schedule is the main defense.

## Step 3 — Define milestones, not just bars

Milestones are verifiable events, ideally quantitative: "Aim 1 cohort enrollment complete (n=120), month 18," "Assay validated at CV<15%, month 9." Keep them within the team's control — "manuscript submitted" works, "manuscript accepted" and "hypothesis confirmed" do not; result-contingent branches are decision points, not milestones. For each, define the decision rule where relevant — what happens if missed (the alternative from the pitfalls subsection). DoD and NIH U/cooperative mechanisms often require formal go/no-go milestones; write them so an outside monitor could adjudicate them. For DoD, distinguish milestones (progress markers) from deliverables (items owed to the sponsor — reports, data, prototypes per the SOW) and schedule both.

## Step 4 — Render the Gantt

Produce the chart in a format matching the document workflow: a table (rows = tasks grouped by aim; columns = quarters or half-years; milestones as symbols) renders reliably in both Word and LaTeX and survives PDF conversion. Offer a script-generated figure (e.g., matplotlib) when the user wants a graphical version; keep source in the folder so revisions are cheap. Keep it readable at final print size — 11pt page, likely half-page figure.

## Consistency duties

Timeline ↔ Approach ↔ budget must agree on scope and pacing. When any of the three changes, update the others (new versions + decision-log entry). Recruit `grant-mock-review` late in drafting to test whether the timeline reads as feasible to a skeptic.
