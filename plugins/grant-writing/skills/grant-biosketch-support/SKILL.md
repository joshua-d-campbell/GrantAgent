---
name: grant-biosketch-support
description: Prepare biosketches and support documents — NIH Biosketch (personal statement, contributions to science), NSF Biographical Sketch and Current & Pending (Other) Support via SciENcv, Other Support pages, and COA templates. Use whenever the user mentions biosketch, biographical sketch, personal statement, contributions to science, Other Support, current and pending, disclosure forms, common forms, SciENcv, or COA for any senior/key person on a grant.
---

# Biosketches and Support Documents

These documents answer review Factor 3 (NIH: Expertise and Resources) — whether this team can do this work. The high-leverage part is tailoring: a biosketch recycled from the last grant argues for the last grant. For multi-PI applications, coordinate the PIs' personal statements with `grant-multi-pi-plan` — the biosketches and the leadership plan must tell the same complementarity story.

Read `00_admin/project-config.md` for the team list and mechanism. Files go to `04_biosketches/`, one per person, versioned. Collect current CVs or prior biosketches from the user as source material. For NIH fellowship applications (F series), the applicant's biosketch uses the *fellowship* format, which adds a **Scholastic Performance** section (institutions, courses, and grades) — collect transcripts, and make the sponsor's personal statement speak to training *this* candidate, not to the sponsor's research program.

Everything factual — products, dates, positions, grant numbers, effort figures — comes from the user's CV, an ORCID/My Bibliography export, or a verified lookup. Never reconstruct a publication or award number from memory: a biosketch listing a product that does not exist as cited carries the same integrity weight as a fabricated reference. Where a product's metadata cannot be confirmed against a source, flag it rather than smoothing it.

## Format ground rules (verify before drafting — formats change)

Both agencies have been converging on the NSPM-33 Common Disclosure Forms generated in SciENcv (NSF adopted first; NIH announced adoption for biosketch and Other Support in 2025). Which format, certification, and signature rules apply depends on the deadline — check the FOA and the current agency guide before drafting, and treat the specifics below as defaults to verify:

- **NIH**: biosketch 5-page limit — Section A Personal Statement (with up to 4 relevant products and ongoing/completed support relevant to the application), B Positions, Scientific Appointments, and Honors, C Contributions to Science (up to 5 contributions, up to 4 products each). Other Support is separate, usually Just-in-Time, with PI signature/certification per current policy.
- **NSF**: Biographical Sketch and Current & Pending (Other) Support **must be generated in SciENcv** — the model drafts *content*, the user enters it in SciENcv. Also prepare the Collaborators & Other Affiliations (COA) spreadsheet per senior person; build the collaborator list by scripting coauthor extraction from a publication export for the template's lookback window (verify the current window in the template instructions) rather than recalling names.
- **DoD/foundations**: per announcement; often accept NIH-style biosketches or free-form CVs with page limits.

## Personal statement — the tailored core

For each key person, draft a personal statement that answers, specifically for *this* application: why this person, for this role, on this project. Structure: one paragraph on fit (expertise mapped to the aims they serve), one on relevant track record (productivity, prior collaborations with this team, mentorship if training is involved), citing the 4 most role-relevant products — not the 4 most prestigious. Explain gaps factually where useful (career interruptions may be addressed; keep it brief and neutral).

Flags to raise: personal statements that never mention the current project; co-I statements identical to their last grant (reviewers on standing sections see repeats); claimed expertise not evidenced by any listed product.

## Contributions to Science (NIH)

For each of up to 5 contributions: 2–4 sentences — the problem context, the person's specific advance, its influence on the field — then up to 4 products. Order so the contributions most relevant to this application come first. Write in the person's voice per available samples; these are personal documents.

## Other Support / Current & Pending

Accuracy here is a compliance matter, not a writing matter: undisclosed support — especially undisclosed foreign support — is the subject of federal enforcement actions against individual researchers. The model's role is organization and overlap analysis; disclosure decisions belong to the user and their grants office.

1. **Elicit the full candidate list.** Prompt the user beyond active grants, because the reportable scope is broader than most CVs: pending applications; foreign and domestic appointments and affiliations (paid or unpaid); in-kind support with research value (lab space, personnel, materials, data); consulting that involves research activity; institutional or startup funds where the current policy requires them. The exact scope is policy that changes — when an item is ambiguous, put it on the list with a note for the grants office. Err toward listing; the grants office removes, the model never does. Never omit an item to make the page look cleaner.
2. **Build the overlap table.** Each active/pending source × the proposed aims: scientific overlap (same question or experiments), budgetary overlap (same cost item funded twice), effort commitment. Sum each person's calendar months per year across everything; totals above 12 person-months, or aims overlapping a funded project, are reported verbatim to the user for their grants office.
3. **Draft overlap statements** for each flagged pair, factual and specific ("Aim 2 shares the mouse cohort with R01-XXXX Aim 3; no budgetary overlap — animals funded once").
4. **Note documentation requirements**: current NIH policy has required supporting documents such as copies of foreign contracts with English translations — verify what applies. Certification and signature are the researcher's act, not the model's output.
