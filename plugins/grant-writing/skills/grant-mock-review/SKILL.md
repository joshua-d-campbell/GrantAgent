---
name: grant-mock-review
description: Simulate a study section / peer review of a draft grant — score it against the funder's actual criteria and write critiques as a skeptical reviewer would. Use when the user wants a mock review, red-team, pre-submission critique, "poke holes in this," a reviewer's-eye read, a predicted score or summary statement, or mentions study section, panel, or "reviewer 2." High-value once a full or near-full draft exists.
---

# Mock Review

Predict the review the proposal will actually receive. The value is adversarial: the useful posture is a fair but skeptical reviewer with a stack of applications, a weekend to read them, and no obligation to fund this one. This is where the no-flattery rule matters most — a mock review that softens problems wastes the exercise. Frame everything as "here is the case reviewers will make," including objections the model does not itself find persuasive; the goal is to predict the panel, not to be right.

Read `00_admin/project-config.md` for funder and mechanism, load the matching criteria and calibration notes from `references/review-criteria.md`, and assemble the current full draft. If the config names a target study section, cast the personas as members of that section — its stated scope defines what expertise the simulated reviewers do and do not have.

## Read like a reviewer, not an editor

Assigned reviewers form a provisional impact judgment from the Aims page and the opening of Significance, then read the Approach looking for reasons to confirm or lower it. Simulate that reading order and its consequences:

- Anything that takes effort to understand becomes a weakness ("the rationale for Aim 2 was unclear") — reviewers do not reread. If a persona has to work to get a point, record the misreading as the critique, because that is what the real reviewer will write.
- Figures, legends, and paragraph-opening sentences get read; dense middle prose gets skimmed. Flag load-bearing content that lives only in skimmed zones.
- Weaknesses drive scores. Strengths paragraphs in real summary statements are often terse and formulaic; spend the simulation's effort where the panel does.

## Run 2–3 reviewer personas

Produce distinct, independently written critiques — real reviews diverge, and suspicious convergence means the simulation is echoing itself rather than modeling three readers:

1. **Assigned reviewer 1 (in-field expert)**: knows the prior art; catches overclaims ("first to show" that isn't), missing citations to competing groups, and methods presented as routine that aren't.
2. **Assigned reviewer 2 (adjacent field)**: judges significance and clarity; punishes jargon, unexplained leaps, and aims whose payoff is stated only in field-internal terms. This persona proxies the unassigned members whose votes decide borderline applications.
3. **(Optional) Reviewer 3 / discussant**: feasibility, budget, timeline, fit to mechanism; the one who asks "what happens to Aims 2 and 3 if Aim 1's hypothesis is wrong?"

Give each persona at least one critique the author will consider a misreading. Real reviews contain them, and a misreading is a presentation failure: the fix belongs in the draft, not in arguing with the reviewer.

## Hunt the known killers

Check every draft explicitly for the critiques that most often sink applications:

- **Interdependent aims** — later aims contingent on a specific outcome of Aim 1.
- **Overambition** — more work than the timeline, budget, or team supports ("ambitious" in a review is not a compliment).
- **Descriptive, not hypothesis-driven** / "fishing expedition" — especially for omics-heavy or screening aims.
- **Missing alternatives and pitfalls** — no plan B where a method could plausibly fail.
- **Rigor gaps** — power/sample size handwaved, no blinding or randomization where expected, SABV ignored or contradicted by the design.
- **Expertise gap** — a pivotal method nobody on the team has published with, and no collaborator letter covering it.
- **Weak premise** — the cited support for the central hypothesis is thinner than the text implies.

## Score against the real criteria

Use the funder's actual instrument from the reference file (NIH simplified framework: Factor 1 and Factor 2 scored 1–9, Factor 3 sufficient/gaps, plus Overall Impact 1–9; NSF Intellectual Merit / Broader Impacts with adjectival ratings; DoD per the BAA, plus the Heilmeier questions for DARPA-type programs). Every score gets a number, the matching descriptor word, and a justification tied to named weaknesses. Do not cluster everything at 4–5 to stay safe; calibrate against the descriptor anchors in the reference file. Overall Impact is a judgment, not an average — one major Factor 2 weakness can outweigh strong significance, and Factor 3 gaps depress it without ever getting a number.

## Simulate the discussion

After the independent critiques, run the panel: reviewer 1 presents and states a score, the others say where they differ, and they argue the genuine disagreements — typically whether the innovation matters, whether the feasibility risk is fatal, and whether the work is incremental. Resolve to a final score range and state plainly whether the application would likely be **discussed or triaged (Not Discussed)** — roughly half of NIH applications are never discussed, and an honest ND call is worth more than a falsely precise percentile. Do not invent paylines or percentile predictions.

## Critique format (per persona)

Mirror a real summary statement: overall impact/merit paragraph with the bottom-line judgment; strengths (specific, located; do not manufacture strengths to balance the ledger); weaknesses by criterion, each with location and the reason it lowers the score, distinguishing fixable presentation problems from fundamental design problems — the second kind sink applications; minor/administrative issues last.

## Synthesis and triage

Consolidate into an action list ranked by score impact: what would most move Overall Impact, what is cosmetic, and what is unfixable this cycle (this feeds `grant-resubmission` strategy). Save to `09_final_assembly/mock-review_<date>.md`.
