---
name: grant-budget-justification
description: Build a research grant budget and budget justification — personnel effort, supplies, equipment, travel, subawards, and the narrative justification. Use whenever the user mentions grant budgets, modular vs detailed budgets, person-months, effort percentages, budget caps, F&A/indirect costs, or needs to cost out a study design. Also use when refining study design forces budget changes or vice versa; this skill keeps the Specific Aims in sync.
---

# Budget and Justification

Budgeting is where the study design becomes concrete: you cannot price an experiment you have not specified. Expect this skill to force design decisions, and propagate those decisions back to the aims page.

Read `00_admin/project-config.md` (budget cap, mechanism, team) first. If the award type is a fellowship (NIH F series, NSF GRFP), stop: stipends, tuition/fees, and institutional allowances are formulaic at published levels — verify the current figures and skip the justification workflow below, which would produce the wrong document. Budget files live in `03_budget/`, versioned per the schema. The budget folder may have restricted permissions — salary figures are sensitive; do not copy them into shared narrative folders.

## Step 1 — Finalize the roster

Confirm with the user: PI(s), co-Is, postdocs, students, staff, consultants, subaward sites. For each person: role, effort, and which aims they serve. Express effort in person-months matched to the appointment type (calendar vs. academic + summer — a "10%" answer still has to be converted correctly). For NIH, salaries above the federal salary cap (Executive Level II) are budgeted at the cap; get the current cap figure from the grants office rather than asserting one. Flags to raise factually:

- Personnel with no clear aim assignment (reviewers notice)
- Key expertise claimed in the narrative but absent from the budget
- Effort below what the described role plausibly requires (e.g., PI at 1% on a large project)
- Multi-PI structures require a Leadership Plan (NIH) — note it on the checklist

## Step 2 — Refine the study design to costable line items

Walk each aim and extract countable quantities: number of experiments/samples/animals/participants, assays per sample, sequencing runs, compute hours, instrument time, fieldwork trips. Where the design is too vague to count, that is a design gap — send it back to the user as a specific question ("How many biological replicates per condition in Aim 2? The answer determines both the power analysis and the supplies line").

Build a spreadsheet in `03_budget/` (per-aim tabs; per-year columns; use the xlsx skill if available): personnel with fringe, equipment (≥$5K per-unit typically — verify institutional threshold), supplies, travel, publication costs, subawards, other direct costs, F&A. Get fringe and F&A rates from the user or their grants office — never guess rates.

## Step 3 — Budget/mechanism fit

- NIH modular (≤$250K direct/year, R01-class — verify threshold in the FOA): budget in $25K modules; justification covers personnel and any module-count variations only. Detailed line items still needed internally for the grants office. Consortium F&A is typically excluded when testing against NIH direct-cost thresholds — verify in the FOA/guide.
- NIH detailed (R&R form): full justification per category per year. If direct costs reach $500K or more in any year, NIH requires institute agreement before submission — have the user contact the program officer well ahead of the deadline (verify current policy and lead time).
- F&A applies to the negotiated base, usually MTDC — which typically excludes equipment, tuition, and each subaward beyond its first $25K. Compute from the institution's rate agreement, not the raw total; applying the rate to everything overstates the budget.
- NSF: budget justification limited to 5 pages; some categories restricted (voluntary committed cost-sharing prohibited; two months' salary convention across all NSF support — verify current PAPPG).
- DoD/foundations: use the announcement's forms; many foundations cap indirect costs — flag any gap between the foundation's rate and the institution's negotiated rate for the grants office.
- Escalation (typically ~3%/yr where allowed), and check the total against the FOA cap in year-1 and cumulative terms.

## Step 4 — Write the justification

For each line: what it is, why the project requires it, how the amount was calculated. The register is factual necessity, not persuasion ("Aim 1 requires 240 samples × 2 assays at $85/assay"). Personnel entries: name, role, effort, and the specific responsibilities tied to aims. Match every claim to the narrative — a reviewer cross-reading budget and Approach should find no orphans in either direction.

## Step 5 — Sync the aims

If costing forced design changes (reduced scope, dropped arm, different model), update the Specific Aims to match: new version in `01_aims/`, entry in `00_admin/decision-log.md` stating what changed and why. An aims page that promises more than the budget can deliver is a rigor problem reviewers catch.
