---
name: grant-approach
description: Draft the Approach / Research Design section of a grant — the experimental plan, rationales, preliminary data placement, expected outcomes, pitfalls and alternatives. Use whenever the user is writing the Approach (NIH), Research Plan/Technical Approach (NSF/DoD), methods sections, aim-by-aim experimental design, or asks how to structure rationales, rigor, power analysis, or alternative strategies. This is the longest section and is worked one subsection at a time.
---

# Approach

The Approach is where most proposals are won or lost — under the NIH simplified framework it alone constitutes Factor 2 (Rigor and Feasibility), scored 1–9. It is too large to draft in one pass. Work one subsection at a time, and **write the rationales first**: if the rationale for an aim is weak, no amount of methods detail rescues it, and discovering that early is cheap.

Read `00_admin/project-config.md`, current aims, Significance/Innovation drafts, and the style profile. Files go to `02_research_plan/approach_<aim>_v<NN>_<date>_draft.<ext>` (per-aim files until assembly).

## Your ideas, not mine (shared convention 8)

The experimental design, rationales, and choice of hypotheses are the applicant's own science, and NIH will reject sections "substantially developed by AI" as not their original ideas ([NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html), Sep 25 2025 receipt onward). The researcher supplies the experiments, systems, and predictions; you organize them into rationale-first subsections, judge feasibility and rigor, surface confounds and missing controls, and propose alternatives *for them to evaluate*. When a design gap has to be filled, offer options with trade-offs and let the researcher decide — do not silently author the experiment. Note that shared convention 4 (reasoning stays in chat, lean justified text in the document) already keeps method-selection reasoning out of the draft; convention 8 is the stronger point that the selection itself is the researcher's to make.

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

For each aim, draft the rationale as a self-contained argument: the observation/premise → the inference → why *this* experiment discriminates between hypotheses → what the field gains from either outcome. Test it with the user: if the hypothesis is wrong, is the aim still informative? If not, redesign now.

Check dependence *across* aims too: if Aims 2–3 can proceed only when Aim 1's hypothesis is confirmed, reviewers will call the structure fragile — a classic fatal flaw. Restructure so later aims survive plausible Aim 1 outcomes, or state explicitly why the dependence is acceptable. Only after all rationales stand does methods drafting begin.

## Step 3 — Draft subsections interactively

One subsection per exchange. For each:

- **Design**: enough detail that a knowledgeable reviewer can judge feasibility — key controls, sample sizes with power justification (underpowered designs are among the most cited rigor weaknesses; state effect-size assumptions and their source), decision criteria. Cite established methods instead of describing them; spend the page budget on what is new or risky.
- **Separate your reasoning from the document text** (shared convention 4): when you pick a method, assay, model system, or statistical test, tell the researcher in the conversation *why* you chose it — they need to vet the choice. But do not carry that justification into the draft by default. For a standard, uncontested choice the text names it and moves on ("Differential expression will be assessed by RNA-seq"); it does not argue for it. Put justification into the document only where a reviewer would otherwise question the choice — a non-obvious method, a contested approach, a design decision the rigor criteria specifically probe. When in doubt, draft the lean version and ask the researcher whether the justification is worth the space, rather than defaulting to the verbose one.
- **Preliminary data**: each figure must earn its space by de-risking a specific step. State what each figure shows factually; note where data are thin rather than overstating. An aim with no supporting data needs its feasibility carried some other way — published precedent, a collaborator letter (coordinate with `grant-letters-of-support`), or a phased design; name which.
- **Expected outcomes**: predicted results, how they'll be interpreted — including the interpretation if results contradict the hypothesis. Experiments with no informative negative outcome read as fishing expeditions. Quantitative success criteria where possible.
- **Pitfalls & alternatives**: real risks (not strawmen), with concrete alternatives and decision points. Reviewers read this subsection as a proxy for the PI's judgment.

Write for the skim: reviewers re-read a 12-page Approach in minutes before the meeting. One schematic per aim (design overview with decision points) is usually the best use of figure space; make decision criteria and sample sizes findable rather than buried in prose.

Flag scope problems factually as they emerge ("Aim 3 as designed requires ~18 months of sequential mouse cohorts; the timeline allocates 8").

## Step 4 — Cross-checks before assembly

- Aims page ↔ Approach consistency: same aims, same order, same headlines; update aims (new version + decision-log entry) if design drifted.
- Budget ↔ design: sample counts and personnel match `03_budget/`.
- Figures/tables numbered and referenced; every method with a citation placeholder for `grant-references`.
- Timeline: hand off milestone structure to `grant-timeline-milestones`.

Agency variants (NSF Project Description structure, DoD SOW/task organization, Heilmeier catechism): read `references/agency-variants.md` when the funder is not NIH.
