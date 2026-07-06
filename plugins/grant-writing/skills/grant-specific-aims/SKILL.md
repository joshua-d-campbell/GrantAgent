---
name: grant-specific-aims
description: Draft and refine the Specific Aims page (NIH) or project overview/objectives (NSF, DoD, foundations) of a research grant. Use whenever the user wants to outline their grant's aims, objectives, hypotheses, or overall scope; asks for feedback on which ideas are innovative vs. already done; or wants a one-page overview to circulate to colleagues. This is the standard second step after grant-setup and drives every later section.
---

# Specific Aims

Produce a first-draft aims page that communicates scope clearly enough to circulate to colleagues. It does not need to be perfect — the study design gets refined during budgeting and the Approach. What it must do is state the problem, the gap, the proposal, and the payoff.

Read `00_admin/project-config.md` first (run `grant-setup` if missing). Apply the tone rules and the style profile.

## Elicit before drafting

Interview the user, in their own terms:

1. What is the central problem and why does it matter now?
2. What is known, and what is the specific gap or barrier to progress?
3. What is the central hypothesis or research question? What preliminary data support it?
4. What are the 2–4 aims? For each: the question, the rough approach, the expected outcome.
5. What changes if the project succeeds (scientific and, where relevant, clinical/societal impact)?
6. Who reviews this (study section, program, foundation board)? Calibrate technicality accordingly.

## Page anatomy (single page)

- **Opening paragraph**: hook establishing importance; what is known; the gap/critical need. End with the consequence of the gap remaining unfilled.
- **Second paragraph**: long-term goal, the overall objective *of this proposal*, central hypothesis, rationale, and why this team/environment.
- **Aims block**: each aim gets a bolded headline (outcome-oriented, not method-oriented — "Determine whether X drives Y," not "Perform RNA-seq on Z"), 2–4 sentences of approach, a working hypothesis or expected outcome where appropriate.
- **Payoff paragraph**: expected overall outcomes, positive impact, and what the results enable next. Significance and impact stated simply and clearly — this is the most important element of the page; reviewers outside the immediate subfield must be able to repeat the argument in study section.

Structural quality checks: aims must be related but not interdependent (aim 2 must survive if aim 1's hypothesis is wrong); each aim testable within the project period; scope matched to mechanism and budget.

For NSF, adapt: objectives instead of aims, explicit Intellectual Merit and Broader Impacts sentences. For DoD/CDMRP, tie aims to the announcement's focus areas and military relevance. Read `references/agency-variants.md` when working on a non-NIH proposal.

## Innovation feedback (required, not optional)

After the draft exists, give the user a factual novelty assessment:

- For each aim, state what appears innovative and what has already been done, citing the closest published work you can identify. Use literature search tools if available; otherwise state clearly which claims need a literature check by the user.
- Distinguish: new question, new method, new application of existing method, incremental extension.
- Neutral tone. "Aim 2's approach has been applied in system X (author, year); the novelty here is limited to the model system" is the correct register — not softened, not harsh.

## Working method

Refine text interactively in conversation. Iterate paragraph by paragraph; only user-approved text goes into the document (`01_aims/`, versioned per the schema, e.g., `specific-aims_v01_<date>_draft.docx`). When aims change materially later (budget, approach development), this file gets a new version and the change is recorded in `00_admin/decision-log.md`.

Suggest circulating the `internal` version to colleagues once the user judges the scope stable, and remind them the title (`grant-title`) comes next.
