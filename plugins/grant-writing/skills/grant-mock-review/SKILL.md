---
name: grant-mock-review
description: Simulate a study section / peer review of a draft grant — score it against the funder's actual criteria and write critiques as a skeptical reviewer would. Use when the user wants a mock review, red-team, pre-submission critique, "poke holes in this," reviewer's-eye read, or wants to know how their draft would score before submitting. High-value once a full or near-full draft exists.
---

# Mock Review

Simulate the review the proposal will actually receive. The value is adversarial: the friendliest useful posture is a fair but skeptical reviewer with a large pile of applications and limited patience. This is where the no-flattery rule matters most — a mock review that softens problems wastes the exercise.

Read `00_admin/project-config.md` to get the funder and mechanism, then load the matching criteria from `references/review-criteria.md`. Assemble the current full draft.

## Run 2–3 reviewer personas

Real panels assign multiple reviewers with different expertise and different tempers. Produce distinct critiques from:

1. **Assigned reviewer (in-field expert)**: deep on methods and novelty; will know the prior art and catch overclaims.
2. **Assigned reviewer (adjacent field)**: judges significance and clarity; loses patience with jargon and unexplained leaps — proxies the reviewers who decide borderline scores.
3. **(Optional) Discussant/chair**: overall enthusiasm, budget, feasibility, fit to the mechanism.

Each persona reads the whole thing and writes independently; do not average them prematurely.

## Score against the real criteria

Use the funder's actual instrument (from the reference file):

- **NIH (simplified framework, 2025)**: assess Factor 1 (Importance of the Research — Significance & Innovation), Factor 2 (Rigor and Feasibility — Approach) with 1–9 scores, and Factor 3 (Expertise and Resources) as sufficient/insufficient with gaps named. Add an Overall Impact score (1–9) with a paragraph justifying it — this is the number that determines funding. Note additional review considerations (human subjects, vertebrate animals, budget) as acceptable/concern.
- **NSF**: Intellectual Merit and Broader Impacts, each with strengths/weaknesses and a rating (Excellent→Poor), plus a summary.
- **DoD**: score against the BAA's stated criteria and, for DARPA-type, run the Heilmeier questions explicitly.

## Critique format (per persona)

Mirror a real summary statement:

- **Overall impact/merit** paragraph: the bottom-line judgment and why.
- **Strengths**: specific, factual, located. Do not manufacture strengths to balance; if the draft is weak, the review says so.
- **Weaknesses**: by criterion, each with location and the reason it lowers the score. Distinguish fixable presentation problems from fundamental design problems — the second kind are the ones that sink applications.
- **Minor/administrative** issues last.

## Synthesis and triage

After the personas, produce a consolidated action list ranked by score impact: what changes would most move the Overall Impact score, what is cosmetic, and what is unfixable in this cycle (informing the resubmission strategy if needed). Save to `09_final_assembly/mock-review_<date>.md`.

Frame throughout as "here is the case reviewers would make," not the model's personal verdict — the point is to predict the panel, including objections the model might not itself find persuasive.
