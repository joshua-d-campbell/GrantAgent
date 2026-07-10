---
name: grant-resubmission
description: Prepare a grant resubmission or revision after review — decode the summary statement/reviews, plan a point-by-point response, write the Introduction to Resubmission, and revise sections to address critiques. Use whenever the user has received reviews, a summary statement, pink sheets, scores, or panel feedback and wants to interpret them, respond, revise, or resubmit (NIH A1, NSF resubmission, or a not-funded proposal being reworked).
---

# Resubmission

Most funded grants are resubmissions. The task is not to defend the original — it is to demonstrate responsiveness while genuinely strengthening the science. Reviewers of a resubmission look first at whether the concerns were taken seriously; but the panel is not guaranteed to be the same people, so the target is a better application overall, not a reply brief addressed to three individuals.

Read `00_admin/project-config.md`. Collect the summary statement / reviews and the prior submitted version. Verify current resubmission rules (NIH: one resubmission (A1), a one-page Introduction to Resubmission, a time window for submitting it, and rules on when a reworked project may return as a "new" application — all have changed before; check the current policy and FOA). Work in a new project version, preserving the prior submission intact for reference (git mode: tag the submitted commit — e.g., `submitted-A0-<date>` — before any resubmission edits, so the diff against what reviewers actually read stays one command away).

## Step 0 — Read the summary statement between the lines

Reviewer language is conventionalized; decode it before triaging:

- **Discussed vs. Not Discussed** is the first signal. ND with middling criterion scores often means "no champion," not "fatally flawed" — usually fixable. Discussed with a poor Overall Impact score means the panel engaged and still declined; the resume of discussion holds the reason.
- **The resume of discussion** (discussed applications only) is the highest-value text: it records what the panel collectively cared about, which predicts what the next panel will care about. Weight it above any individual critique.
- **Score pattern**: strong Factor 1 with weak Factor 2 is the *good* pattern — approach problems are the most fixable. Weak Factor 1 (importance/significance) is the hard one: if the panel doubts the question matters, a cleaner methods section will not save it, and the honest conversation with the user is whether to reframe the project or redirect the effort.
- **Coded vocabulary**: "ambitious" = they don't believe the timeline; "descriptive" = no hypothesis; "incremental" = significance failure; "enthusiasm was dampened/diminished" = this issue drove the score; "the PI may wish to consider X" = do X; "unclear" = the reviewer's misreading is your presentation problem. Faint strengths ("the PI is productive," "the environment is excellent") with nothing said about the science signal low enthusiasm.
- **Prompt the user to call the program officer.** The PO attended the discussion and can say what actually dominated it, whether the panel's tone was salvage-or-abandon, and whether to resubmit or return as new. Do this before committing to a strategy.

## Step 1 — Decompose the reviews

Extract every distinct critique from every reviewer and the resume of discussion. Build a table: critique | reviewer | criterion affected | type (fundamental design / feasibility / presentation / factual error / preference) | severity (drove the score vs. minor). Where reviewers disagreed with each other, note it; you may side with one, but explain why.

## Step 2 — Decide the response strategy per critique

For each: **address** (change the science or plan), **clarify** (the point was misread — fix the presentation that allowed the misreading; never just write "the reviewer misunderstood"), or **rebut with evidence** (rare; only when the reviewer is factually wrong and it matters). Fundamental-design critiques usually require real change — cosmetic responses to substantive concerns are transparent and resented. Flag any critique that cannot be addressed within the mechanism; that feeds a go/no-go conversation with the user.

Because resubmissions frequently draw at least one new reviewer, also fix weaknesses nobody mentioned: a new reader reviews the whole application, and "new concerns on the A1" is a common, demoralizing outcome that broad revision partially insures against. Do not over-fit to one reviewer's stylistic preferences at the expense of the application.

## Step 3 — Write the Introduction to Resubmission (~1 page)

- One professional sentence acknowledging the review (convention, not flattery).
- Point-by-point, grouped by theme: state each concern concisely, then the specific change made and where it appears in the revised application.
- Neutral, non-defensive throughout — no litigating, no wounded pride. Concede real weaknesses that were fixed; that reads as maturity and buys credibility for the rare rebuttal.
- Mark changes in the body per current agency guidance (NIH policy on identifying changes has shifted over time — verify what the current cycle expects before choosing a marking scheme).

## Step 4 — Revise and re-run the pipeline

Apply substantive changes through the relevant section skills (new preliminary data → `grant-approach`; scope changes → `grant-specific-aims` + `grant-budget-justification`, with decision-log entries). Then re-run `grant-mock-review` on the revised draft twice over: once against the original critiques to confirm each is actually resolved, and once with a fresh persona who never saw the prior review, to catch what a new reviewer would raise. A resubmission that reintroduces old problems, or adds new ones while fixing old ones, is the failure mode this catches. Finish with the proofread and format checks.

## NSF and other funders

NSF has no formal resubmission mechanism: a declined proposal returns as a new proposal, likely with different reviewers, and there is no response-to-reviews document — but the PAPPG expects substantial revision of previously declined proposals and the program officer sees the history, so address the prior panel's critiques anyway. For DoD and foundations, ask the program manager/officer whether a response to prior review is expected and in what form.

Save the response analysis to `09_final_assembly/resubmission-response_<date>.md`.
