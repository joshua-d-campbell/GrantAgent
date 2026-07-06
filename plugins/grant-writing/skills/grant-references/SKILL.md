---
name: grant-references
description: Verify and manage citations in a grant proposal — every background claim referenced, every reference real and accurate, bibliography formatted per agency rules. Use when the user mentions references, citations, bibliography, EndNote/Zotero/BibTeX for a grant, or before submission to confirm all sections relying on prior work are correctly cited.
---

# References

Two failure classes matter: substantive claims without citations (reads as unsupported assertion or, worse, unacknowledged borrowing) and citations that do not support the claim they anchor (a reviewer who checks one bad citation distrusts the rest). This skill audits both, then handles formatting.

Read `00_admin/project-config.md` for the citation manager and format in use. Work from the latest versions of all narrative documents; bibliography lives in `08_references/`.

## Pass 1 — Coverage audit

Walk each document and flag sentences that assert prior findings, quantitative facts (prevalence, rates, costs), method provenance, or "others have shown" content without a citation. Significance and the rationale subsections of the Approach are the dense zones; Innovation's prior-art claims must each be anchored. Report as a list: location, claim, why it needs support. Also flag over-citation — strings of 5+ citations on routine statements consume space without persuading.

## Pass 2 — Accuracy audit

For each citation, verify what is checkable:

- The reference exists: real authors, journal, year, DOI/PMID. Verify against PubMed/Crossref when web tools are available. This matters doubly for any citation that entered via an LLM at any point — fabricated references in a federal application are a serious integrity problem. Any reference that cannot be verified is reported as unverified, never silently retained.
- The reference supports the claim: where the abstract is accessible, check the claim against it; where only the user knows the paper, put it on their check-list with the specific claim quoted.
- Currency: background resting on superseded work (e.g., pre-2020 epidemiology for a "current burden" claim) is flagged.
- Self-citation balance: expected for establishing the team's foundation, conspicuous when it displaces the field's key papers.

## Pass 3 — Formatting

- Agency rules: NIH Bibliography & References Cited has no page limit and does not count against the Research Strategy; NSF References Cited likewise separate from the 15 pages (verify current PAPPG). Citations must include full author lists or the agency-permitted et al. convention — check current instructions.
- Style consistent throughout (numbered vs author-year per the user's choice and FOA); every in-text citation resolves to a bibliography entry and vice versa (script this check when format allows — BibTeX and Word field codes are both parseable).
- Public-access compliance: NIH-funded prior work by the team must show PMCIDs where required.

## Deliverable

`08_references/reference-audit_<date>.md`: uncited claims, unverified references, claim-support mismatches for user review, formatting corrections. Fixes are applied to new document versions with user approval.
