---
name: grant-approach
description: Draft the Approach / Research Design section of a grant — the experimental plan, rationales, preliminary data placement, expected outcomes, pitfalls and alternatives. Use whenever the user is writing the Approach (NIH), Research Plan/Technical Approach (NSF/DoD), methods sections, aim-by-aim experimental design, or asks how to structure rationales, rigor, power analysis, or alternative strategies. This is the longest section and is worked one subsection at a time.
---

# Approach

The Approach is where most proposals are won or lost — under the NIH simplified framework it alone constitutes Factor 2 (Rigor and Feasibility), scored 1–9. It is too large to draft in one pass. Work one subsection at a time, and **write the rationales first**: if the rationale for an aim is weak, no amount of methods detail rescues it, and discovering that early is cheap.

Read `00_admin/project-config.md`, current aims, Significance/Innovation drafts, and the style profile. Files go to `02_research_plan/approach_<aim>_v<NN>_<date>_draft.<ext>` (per-aim files until assembly).

## Step 1 — Agree on the outline

Propose an outline and get user sign-off before writing prose. Default per-aim template:

```
Aim N: <headline from aims page — must match verbatim>
  N.1 Rationale                 <- write first, across ALL aims
  N.2 Preliminary data          <- what supports feasibility of THIS aim
  N.3 Experimental design       <- what, in what system, with what controls
  N.4 Expected outcomes & interpretation
  N.5 Potential pitfalls & alternative approaches
  N.6 Rigor: replicates, power, blinding/randomization, sex as a biological
      variable (NIH), statistical plan
```

Plus a short preamble (overall strategy, timeline pointer) and, where applicable, a shared "General methods" block to avoid repetition. Adjust for the mechanism — an R21 compresses; a DoD SOW-driven proposal organizes by task.

## Step 2 — Rationales first (all aims)

For each aim, draft the rationale as a self-contained argument: the observation/premise → the inference → why *this* experiment discriminates between hypotheses → what the field gains from either outcome. Test it with the user: if the hypothesis is wrong, is the aim still informative? If not, redesign now. Only after all rationales stand does methods drafting begin.

## Step 3 — Draft subsections interactively

One subsection per exchange. For each:

- **Design**: enough detail that a knowledgeable reviewer can judge feasibility — key controls, sample sizes with justification, decision criteria. Cite established methods instead of describing them; spend the page budget on what is new or risky.
- **Preliminary data**: each figure must earn its space by de-risking a specific step. State what each figure shows factually; note where data are thin rather than overstating.
- **Expected outcomes**: predicted results, how they'll be interpreted, and quantitative success criteria where possible.
- **Pitfalls & alternatives**: real risks (not strawmen), with concrete alternatives and decision points. Reviewers read this subsection as a proxy for the PI's judgment.

Flag scope problems factually as they emerge ("Aim 3 as designed requires ~18 months of sequential mouse cohorts; the timeline allocates 8").

## Step 4 — Cross-checks before assembly

- Aims page ↔ Approach consistency: same aims, same order, same headlines; update aims (new version + decision-log entry) if design drifted.
- Budget ↔ design: sample counts and personnel match `03_budget/`.
- Figures/tables numbered and referenced; every method with a citation placeholder for `grant-references`.
- Timeline: hand off milestone structure to `grant-timeline-milestones`.

Agency variants (NSF Project Description structure, DoD SOW/task organization, Heilmeier catechism): read `references/agency-variants.md` when the funder is not NIH.
