---
name: grant-cover-letter-assignment
description: Draft the NIH cover letter and PHS Assignment Request Form — institute/center assignment preferences, study section targeting, needed reviewer expertise, and reviewer exclusions. Use whenever the user mentions a cover letter, assignment request, study section choice or request, CSR referral, which institute to target, excluding a reviewer, competing labs on a panel, or reviewer expertise, typically as the application nears submission.
---

# Cover Letter and Assignment Request (NIH)

Two documents PIs routinely conflate, with different audiences and rules. The **PHS Assignment Request Form** carries all assignment preferences — institute/center, study section, reviewer exclusions, needed expertise — and is read only by referral and scientific review staff, never by reviewers. The **cover letter** is for administrative matters only (late submission explanation, changed/corrected applications, prior-approval documentation for $500K+ direct costs in any year, and similar); assignment requests placed there instead of the form is the classic error. Both are optional, both are worth doing deliberately: assignment is where an application can land in front of the right audience or the wrong one, and it is decided before any reviewer reads a word.

Read `00_admin/project-config.md` first. Files go to `08_final_assembly/`, versioned per the schema. This skill runs near the end — the expertise and exclusion content should be extracted from the *final* aims and Approach — but the study-section choice itself belongs early (see below).

## Choose the study section early, finalize the request late

The target study section shapes how the proposal should be written — framing, aims emphasis, how much methods detail reviewers will expect — so make the choice around the aims stage and record it in the config (`Target study section / IC`). If the user arrives here without one, help choose now and note the late-choice risk factually. Ways to ground the choice:

- **NIH RePORTER**: search funded projects closest to this proposal and see which study sections reviewed them — the highest-signal evidence, since it shows where similar science actually succeeds.
- **CSR study section descriptions**: match the proposal's core questions to the section's stated scope; a proposal at the boundary of two sections is worth an explicit request.
- **CSR's Assisted Referral Tool (ART)** suggests sections from abstract text — offer it to the user as a cross-check.
- **The program officer**: encourage the user to ask — POs know where applications like this one get traction, and the conversation builds a relationship that matters later.

When the config names a target section, `grant-mock-review` should cast its personas as members of that section — note this handoff.

## The Assignment Request Form, field by field

Draft each from the final application, concise and factual (these are short structured fields, not essays):

1. **Institute/center assignments** (request and do-not-assign): based on mission fit — and note dual assignment is worth requesting when the science genuinely spans two ICs, since paylines and portfolio priorities differ. Check the FOA first: many FOAs fix the IC, making this field moot.
2. **Study section assignments** (request and do-not-assign): the choice made above, by exact CSR name and code.
3. **Individuals who should not review**: reviewer exclusions, sparingly used. Elicit from the user who has *directly competing* work — same question, same system, a race to publication — and help them reason about it from the literature (the user confirms; the skill does not assert conflicts on its own authority). Keep the list short (a handful at most — long lists read as paranoia and complicate panel assembly), state the competitive basis in a phrase, and set expectations: SROs honor reasonable exclusions but are not obligated to. Personal or scientific disagreement is not a basis reviewers will find credible; direct competition is.
4. **Needed expertise**: extract from the final Approach — the 2–4 methodological and domain areas a fair review requires (e.g., "single-cell transcriptomics; Bayesian hierarchical models; mouse models of acute lung injury"). This field guards against the common failure mode of no panel member being equipped to judge the proposal's central method.

Record the requests in `00_admin/decision-log.md` — on resubmission, `grant-resubmission` needs to know what was requested last time and whether the assignment worked out.

## The cover letter (only when needed)

Include one only for its sanctioned purposes; check the current application guide's list. Common legitimate uses: late application explanation, changed/corrected submission note, documentation of agency approval for $500K+ direct costs in any year, required attachments per the FOA, video/unusual-materials declaration. One page, addressed to the Division of Receipt and Referral, factual and brief. If the only content would be assignment preferences, there should be no cover letter — that content belongs on the form.

## Cross-checks

- Expertise fields ↔ final Approach: every named expertise area corresponds to a load-bearing method in the application.
- Exclusions ↔ references: excluding someone whose work the proposal cites heavily invites referral-staff skepticism — flag the tension to the user rather than resolving it silently.
- Verify current form fields and cover-letter rules against the application guide — both have changed before and this skill's specifics should be confirmed at time of use.

Agency note: this is an NIH mechanism. NSF has no reviewer-exclusion form with this structure, but proposers may suggest and request non-reviewers in Research.gov (single-copy documents); DoD per the BAA. For those funders, offer the same strategic reasoning and put the output where the funder's process expects it.
