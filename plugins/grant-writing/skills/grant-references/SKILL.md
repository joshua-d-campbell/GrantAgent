---
name: grant-references
description: Verify and manage citations in a grant proposal — every background claim referenced, every reference real and accurate, bibliography formatted per agency rules. Use when the user mentions references, citations, bibliography, EndNote/Zotero/BibTeX for a grant, asks whether citations are real or worries about fabricated/hallucinated references, or before submission to confirm all sections relying on prior work are correctly cited.
---

# References

Two failure classes matter: substantive claims without citations (reads as unsupported assertion or, worse, unacknowledged borrowing) and citations that do not support the claim they anchor (a reviewer who checks one bad citation distrusts the rest). This skill audits both, then handles formatting.

Read `00_admin/project-config.md` for the citation manager and format in use. Work from the latest versions of all narrative documents; bibliography lives in `08_references/`.

## Pass 1 — Coverage audit

Walk each document and flag sentences that assert prior findings, quantitative facts (prevalence, rates, costs), method provenance, or "others have shown" content without a citation. Significance and the rationale subsections of the Approach are the dense zones; Innovation's prior-art claims must each be anchored. Report as a list: location, claim, why it needs support. Also flag over-citation — strings of 5+ citations on routine statements consume space without persuading.

## Pass 2 — Accuracy audit

Ground rule first: never add, complete, or repair a citation from memory. Model memory produces plausible-but-wrong metadata — real authors on the wrong paper, real papers with the wrong year — and that is exactly how fabricated references enter federal applications, where they are an integrity problem, not a typo. Every citation the audit marks *verified* was matched this session against a live lookup or the user's exported library; every citation added or corrected comes from the same sources. If web tools are unavailable, say so and mark everything unverified — do not approximate.

Verification procedure, per entry:

1. Query Crossref (`https://api.crossref.org/works?query.bibliographic=<title>&rows=3`) and/or PubMed E-utilities (esearch on title, then esummary). Batch these with a script when the bibliography is parseable.
2. Require a match on title (near-exact), first-author surname, year (±1 tolerates epub/print splits), and journal. Resolve the DOI or PMID.
3. Check retraction and correction status (Crossref returns `update-to` metadata; the Retraction Watch database is folded into Crossref). A proposal resting a claim on a retracted paper is a credibility hit reviewers do catch.
4. Classify: **verified** · **verified with corrections** (list the metadata fixes) · **not found** (possible fabrication — the user produces the paper or the citation comes out; never substitute a plausible alternative silently) · **exists, claim unchecked** (abstract/full text inaccessible — goes on the user's checklist with the specific claim quoted).

Beyond existence:

- The reference supports the claim: where the abstract is accessible, check the claim against it; a citation that exists but says something else is the failure reviewers punish hardest.
- Currency: background resting on superseded work (e.g., pre-2020 epidemiology for a "current burden" claim) is flagged.
- Self-citation balance: expected for establishing the team's foundation, conspicuous when it displaces the field's key papers.

## Pass 3 — Formatting

- Agency rules: NIH Bibliography & References Cited has no page limit and does not count against the Research Strategy; NSF References Cited likewise separate from the 15 pages (verify current PAPPG). Citations must include full author lists or the agency-permitted et al. convention — check current instructions.
- Style consistent throughout (numbered vs author-year per the user's choice and FOA); every in-text citation resolves to a bibliography entry and vice versa. Script this: parse `.bib` entry keys against `\cite{...}` occurrences for LaTeX; for Word, extract bracketed numbers or author-year strings from the exported text and diff against the bibliography list. Orphans in either direction are findings.
- Public-access compliance: the team's own papers arising from NIH funding must show PMCIDs where the policy requires them (scope changed with the 2024 policy update — verify current requirements). Look up missing PMCIDs via the NCBI ID Converter API rather than asking the user to hunt.

## Deliverable

`08_references/reference-audit_<date>.md`: uncited claims; the verification classification per reference with counts; claim-support mismatches for user review; formatting corrections. Fixes are applied to new document versions with user approval. References still classified *not found* or *claim unchecked* stay flagged in every subsequent audit until resolved — an unresolved flag near the deadline is a decision for the user, never a silent default.
