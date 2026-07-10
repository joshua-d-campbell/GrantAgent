---
name: grant-references
description: Verify and manage citations in a grant proposal — every background claim referenced, every reference real and accurate, bibliography formatted per agency rules. Use when the user mentions references, citations, bibliography, EndNote/Zotero/BibTeX for a grant, asks whether citations are real or worries about fabricated/hallucinated references, or before submission to confirm all sections relying on prior work are correctly cited.
---

# References

Two failure classes matter: substantive claims without citations (reads as unsupported assertion or, worse, unacknowledged borrowing) and citations that do not support the claim they anchor (a reviewer who checks one bad citation distrusts the rest). This skill audits both, then handles formatting.

Read `00_admin/project-config.md` for the reference manager and format in use. Work from the latest versions of all narrative documents. There is no separate references folder: the bibliography lives inside the manuscripts, managed by the team's tool (Zotero/EndNote/Mendeley fields in Word; a `.bib` file alongside the LaTeX source). Audit the documents and the manager's output where they live; report findings to `08_final_assembly/`.

## Pass 0 — Get machine-readable citations first

How citations are stored determines how reliably they can be audited; get this right before any pass.

**LaTeX**: `\cite{...}` keys and the `.bib` file are plain text — read them directly.

**Word with a reference manager**: citations are *field codes*, not text. Plain-text extraction (pandoc, python-docx) returns only the field's cached display string — sometimes dropping or fragmenting it — and that cached string can be stale relative to the library. Do not audit from extracted plain text. Instead, a .docx is a zip: read `word/document.xml` and pull the fields directly — `ADDIN ZOTERO_ITEM CSL_CITATION` (Zotero) and `ADDIN CSL_CITATION` (Mendeley) embed full CSL JSON per citation; `ADDIN EN.CITE` (EndNote) embeds XML records. These carry title, authors, year, and usually DOI for every cited item — authoritative for what was actually inserted, and a better input to Pass 2 verification than parsing formatted strings. Also ask the user for a library export (`.bib`, RIS, or EndNote XML) and reconcile fields against it.

**Hand-typed citations** (no fields) are the fallback case: regex the display text. A document that mixes fielded and hand-typed citations is itself a finding — hand-typed entries won't renumber or restyle when the manager updates, which is how "[23]" ends up pointing at the wrong paper after a late insertion.

Before auditing, have the user refresh fields and regenerate the bibliography in the manager — a stale generated bibliography is the most common source of false orphan findings.

## Pass 1 — Coverage audit

Walk each document and flag sentences that assert prior findings, quantitative facts (prevalence, rates, costs), method provenance, or "others have shown" content without a citation. Significance and the rationale subsections of the Approach are the dense zones; Innovation's prior-art claims must each be anchored. Report as a list: location, claim, why it needs support. Also flag over-citation — strings of 5+ citations on routine statements consume space without persuading.

**Placeholder sweep.** Investigators mark to-be-added citations with ad-hoc placeholders; every one must be found, because a placeholder that survives to submission reads as an unfinished application. Read the investigator's own convention from `project-config.md` (recorded by `grant-setup`), then also sweep case-insensitively for the common families:

- Bare markers: `(ref)`, `(refs)`, `[ref]`, `(REF?)`, `(cite)`, `(citation)`, `(citation needed)`, `(CN)`
- Identifier-bearing: `(PMID: 12345678)`, bare `PMID 12345678`, `[ref: 12345]`, `(DOI: 10.xxxx/…)`, accession numbers standing in for citations
- LaTeX: `\cite{?}`, `\cite{TODO}`, `\cite{xxx}`, commented-out `% add ref`, rendered `[?]` / `??`
- Generic to-do markers near claims: `TODO`, `XXX`, `FIXME`, `***`; in Word, highlighted text (`w:highlight` in document.xml) — a common self-flagging habit worth asking the user about

These families are seeds, not a complete list — after the regex sweep, scan flagged-adjacent text for anything else that looks like a stand-in rather than a real citation, and add the user's variants to the config for next time. Identifier-bearing placeholders are *resolvable*, not just findings: look up the PMID/DOI (PubMed esummary, Crossref), present the resolved reference for approval, and insert it through the reference manager — never by typing formatted text (Pass 2 ground rule applies). Bare placeholders go on the findings list with location and the claim they anchor. The deliverable states the placeholder count explicitly, including when it is zero.

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
- Style consistent throughout (numbered vs author-year per the user's choice and FOA); every in-text citation resolves to a bibliography entry and vice versa. Script this: parse `.bib` entry keys against `\cite{...}` occurrences for LaTeX; for Word, diff the field-code items from Pass 0 against the generated bibliography (fall back to regexing display strings only for hand-typed citations). Orphans in either direction are findings.
- Public-access compliance: the team's own papers arising from NIH funding must show PMCIDs where the policy requires them (scope changed with the 2024 policy update — verify current requirements). Look up missing PMCIDs via the NCBI ID Converter API rather than asking the user to hunt.

## Deliverable

`08_final_assembly/reference-audit_<date>.md`: uncited claims; placeholder count and locations (explicitly zero when clean); the verification classification per reference with counts; claim-support mismatches for user review; formatting corrections. Fixes are applied to new document versions with user approval. References still classified *not found* or *claim unchecked* stay flagged in every subsequent audit until resolved — an unresolved flag near the deadline is a decision for the user, never a silent default.
