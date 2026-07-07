---
name: grant-loi-preproposal
description: Draft letters of intent, pre-proposals, preliminary proposals, concept papers, and DoD white papers — the short documents that precede a full application. Use whenever the user mentions an LOI, letter or notice of intent, pre-proposal, preliminary proposal, pre-application, concept paper, white paper, a two-stage competition, or an internal limited-submission round. Handles both genres: administrative LOIs that notify program staff for reviewer planning, and competitive pre-proposals that determine who is invited to submit a full proposal.
---

# LOI and Pre-Proposal

Two very different documents share this name, and classifying which one is in front of you is the first job, because their economics are opposite. An **administrative LOI** is a notification: program staff use it to plan reviewer recruitment and panel load; nobody is persuaded by it, and it should cost an hour. A **competitive pre-proposal** is a first-stage review that eliminates most applicants; page for page it is the highest-stakes writing of the cycle. Treating the first like the second wastes a week; treating the second like the first ends the application.

Read `00_admin/project-config.md` first (run `grant-setup` if missing — setup extracts the LOI/pre-application deadline, which often falls weeks before the full deadline and is the most commonly missed date). Files go to `01_aims/loi-preproposal_v<NN>_<YYYY-MM-DD>_<status>.<ext>`, versioned per the schema. Whatever the document declares to the funder gets recorded in `00_admin/decision-log.md` — declared titles, personnel, and aims are commitments the full application may be checked against.

## Step 0 — Classify from the FOA

Determine and record in the config:

- **Required or optional?** An optional NIH LOI is still worth sending — it costs nearly nothing and helps the SRO recruit the right reviewers.
- **Binding or not?** Some funders allow the full application to drift from the LOI (title changes usually fine); others require the full proposal to match the pre-proposal's aims and team. Know which before writing a word.
- **Screened or not?** If it gates the full submission, what are the stated selection criteria, and what fraction advance (when published)?
- **Route and format**: email to a program officer vs. a portal; strict templates are common (DoD especially) and deviation is a rejection, not a style choice.

Everything below forks on these answers.

## Path A — Administrative LOI

Only completeness, accuracy, and the deadline matter. Gather exactly the fields the FOA lists — typically a descriptive title, PI and key personnel with institutions, the FOA number, an aims-level description, and sometimes anticipated budget or study-section suggestions. Draft from the current aims thinking; no selling, no polish beyond clarity. The accuracy that matters most is personnel and institutions, because program staff use them for reviewer conflict screening. Note in the decision log exactly what was declared, so later drift is caught deliberately rather than discovered by the funder.

## Path B — Competitive pre-proposal

A first-stage review has its own physics: reviewers read a large stack fast and must eliminate most of it. The classic failure is compression — a full proposal crammed into the page limit reads as poor judgment, not thoroughness. A pre-proposal is not a small proposal; it is a different document whose one goal is the invitation.

- **Structure** (adapt to any mandated template): the problem and why it matters *now* → the idea and what is new about it → the approach at aims level (what will be done, not protocol) → expected impact in the funder's terms → one team-credibility paragraph (key expertise, one or two signature results) → a feasibility signal (a pilot result, a unique resource).
- **Write for invitation, not specification.** Include what earns the invite; defer what the full proposal argues. But scope honestly — where the funder expects the full proposal to match, do not promise aims the team would want to change (decision log again).
- **Draft against the stated selection criteria verbatim** — extract them from the FOA first. For foundations, mission fit is usually scored explicitly, and generic fit language ("aligns with your mission of improving health") is the common kill; name the funder's specific priority and connect the work to it concretely.
- One schematic figure usually earns its space; dense text at the page limit rarely does.
- Before submission, red-team it: `grant-mock-review` against the first-stage criteria, with the personas told they must cut most of the stack.

## Variants

- **NSF preliminary proposals** (required by some divisions/solicitations): formal template, panel-reviewed, with invite/discourage outcomes — check whether the outcome is binding and whether a discouraged proposal may still submit.
- **DoD white papers**: often the expected first contact under a BAA, with the Heilmeier catechism as the natural skeleton (see `grant-mock-review`'s criteria references). Their purpose includes starting a conversation — encourage the PI to engage the program officer, whose feedback at this stage shapes or ends the full proposal.
- **Foundation LOIs**: usually gated and staff- or board-screened; lay-readable, mission-forward, short.
- **Internal limited-submission rounds**: when the funder caps applications per institution, the first competition is internal — a committee of smart non-specialists, an earlier deadline, and the research office's own template. Write the significance for an intelligent outsider, and treat the internal date as the real deadline (coordinate with `grant-setup`'s deadline map).

## Handoffs

Content feeds from `grant-specific-aims` (aims-level material is the core of both paths). On invitation, full-proposal drafting proceeds normally with the pre-proposal's declared commitments as constraints. If eliminated at this stage with feedback, treat the feedback as a review — `grant-resubmission` logic applies in miniature to the next cycle's attempt.
