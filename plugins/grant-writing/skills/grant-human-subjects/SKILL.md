---
name: grant-human-subjects
description: Complete the PHS Human Subjects and Clinical Trials Information form — study records, the clinical-trial questionnaire, eligibility criteria, inclusion enrollment reports, recruitment and retention plans, the Protection of Human Subjects attachment, data and safety monitoring plans, sIRB plans, and the protocol synopsis for clinical trials. Use whenever the user mentions the human subjects form, a study record, enrollment targets or inclusion enrollment reports, recruitment plans, DSMP or DSMB, single IRB, protocol synopsis, or preparing the clinical trials sections of an NIH application.
---

# PHS Human Subjects and Clinical Trials Information Form

This form restates the Approach's design decisions in regulatory structure, which dictates its timing: run it **after** the study design and enrollment numbers are settled in the Approach — drafting it earlier produces rework and, worse, inconsistencies between the form and the research plan that reviewers and validation systems both catch. Much of the form is enforced at submission validation (a required field left blank stops the application), and the rest is rated by reviewers as protections and inclusion considerations, where "unacceptable" bars award until resolved.

Read `00_admin/project-config.md`, the final Approach (design, sample sizes, statistical plan), and the timeline. `grant-compliance-sections` owns the upstream determination (is this human-subjects research? a clinical trial?) and the cross-cutting compliance view; this skill owns the form itself. Files go to `07_compliance/`, one file per study record, versioned. Verify field names and requirements against the current form version and application guide — the FORMS packages change periodically.

## Step 0 — Study inventory and classification

One study record per study; get the boundaries right before drafting (two arms of one protocol are one study; two protocols are two records). For each study, walk the NIH four-question clinical-trial test with the user — human participants? prospectively assigned to an intervention? designed to evaluate the intervention's effect? a health-related biomedical or behavioral outcome? — all four yes means clinical trial, which activates Section 4, the DSMP requirement, clinical-trial-permitting FOA eligibility, and ClinicalTrials.gov registration obligations at award. Check exemption categories where claimed, and for human-subjects work that depends on earlier aims' results, propose a **delayed onset** justification instead of a speculative study record.

## Step 1 — Population, eligibility, enrollment (Section 2)

- **Conditions and eligibility criteria**: inclusion and exclusion criteria stated precisely enough to operationalize — these are read as a test of whether the team has actually planned the study.
- **Age range and inclusion across the lifespan**: any exclusion of children or older adults needs scientific justification, not convenience.
- **Inclusion of women and minorities + the Inclusion Enrollment Report**: the planned-enrollment table by sex/gender, race, and ethnicity. The totals must equal the Approach's n exactly, and the distribution should reflect the condition's epidemiology or the catchment population — a table that doesn't will draw an inclusion comment. Justify any single-sex design (coordinate with the SABV check in `grant-compliance-sections`).
- **Recruitment and retention**: where participants come from, at what rate, and what retains them. Do the arithmetic explicitly: accrual rate × recruitment window ≥ target n, with the sources named (clinic volume, registry size). Implausible enrollment is one of the most common clinical-study critiques, and it is checkable — check it.
- **Study timeline and first-enrollment date**: consistent with `grant-timeline-milestones`.

## Step 2 — Protection and monitoring (Section 3)

- **Protection of Human Subjects attachment**, in its required structure: (1) risks to participants — population characteristics, sources of materials, foreseeable risks including privacy/data risks; (2) adequacy of protection — consent process, protections against each named risk, data security; (3) potential benefits to participants and others; (4) importance of the knowledge to be gained. Each named risk in (1) needs a matching protection in (2) — orphan risks are the standard incompleteness flag.
- **Data and Safety Monitoring Plan**: required for every clinical trial, scaled to risk — who monitors (PI, independent safety officer, or DSMB for higher-risk/multi-site trials), what triggers review, stopping rules (coordinate with the statistical plan), and adverse-event reporting paths.
- **Single IRB (sIRB) plan** for multi-site domestic studies; reliance agreements are slow, so flag the lead time to the user.

## Step 3 — Protocol synopsis (clinical trials only, Section 4)

Primary and secondary outcomes stated quantitatively and matching the Approach's success criteria verbatim; interventions and comparators; design elements (allocation, masking, intervention model); the statistical design and power — **the same numbers as the Approach and any `grant-approach-experiment` review, exactly**; FDA IND/IDE status where applicable; and the dissemination plan. Any divergence between Section 4 and the Research Strategy is a reviewer catch with credibility cost, because it suggests the two were written separately.

## Cross-checks before assembly

Reconcile the quartet: enrollment n ↔ power analysis in the Approach ↔ per-participant costs in the budget ↔ recruitment window in the timeline. Then confirm no required field is blank (validation-blocking), note ClinicalTrials.gov registration/reporting obligations in the decision log so they're staffed at award, and route substantive compliance judgments to the IRB and grants office — the skill drafts and checks completeness; it does not adjudicate compliance. Findings on design weaknesses (underpowered arms, infeasible accrual) go back to `grant-approach`; a skeptical read of the whole package is `grant-mock-review`'s job.
