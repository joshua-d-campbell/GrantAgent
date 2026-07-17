# Changelog

All notable changes to the GrantAgent skill suite. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is semantic as applied to a skill suite: **major** = breaking changes to shared contracts (project-config fields, folder structure, versioning schema), **minor** = new skill added, or a new suite-wide convention/capability affecting how all skills operate, **patch** = refinements and agency-fact updates.

Versions 0.1.0–0.8.0 were assigned retroactively; initial development happened as an intensive sprint on 2026-07-06/07. Version 1.0.0 is reserved for completion of the first eval pass (realistic-prompt testing of the priority skills).

## [0.14.1] — 2026-07-17

### Changed
- Style-corpus guidance (shared convention 5 + `grant-setup` Step 4) reworked around a privacy consideration: the style profile needs *voice*, not unpublished ideas, so setup now recommends already-public writing (published papers, review articles, RePORTER/NSF public grant text) as the default source and treats prior/unpublished grants as the user's informed choice. Setup states a plain, accurate data-path note before ingesting anything — files are transmitted to and processed on Anthropic's servers and retained; training use depends on the account (not on commercial plans by default; on consumer plans only when the model-improvement setting is on), while the transmission itself is the consideration for embargoed/confidential/IP material and institutional AI-use policies. The chosen source and any confidentiality constraint are recorded in `project-config.md` (new *Style corpus source* field); the landing-page tip and a new "Your material and your data" note reflect the same. (Anthropic policy verified July 2026.)

## [0.14.0] — 2026-07-17

### Added
- Shared convention 8 — **the applicant originates the ideas; the suite assists with expression.** Codifies the boundary behind NIH's "Apply Responsibly" policy ([NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html), effective the Sep 25 2025 receipt date): applications with sections "substantially developed by AI" are not considered the applicant's original ideas and will not be reviewed. Drafting skills elicit the researcher's own problem, aims, hypotheses, novelty, and design before drafting; offer options for the researcher to judge rather than finished scientific directions; keep the researcher the author of record (text lands only after their approval, per convention 4); and refuse to paper over a thin idea with manufactured novelty or significance.
- Concise "Your ideas, not mine" guardrail added to the four idea-bearing narrative skills — `grant-specific-aims`, `grant-significance`, `grant-innovation`, `grant-approach` — each pointing to convention 8 and tailored to the intellectual content that section carries.
- Landing page: a hero callout and a dedicated **Responsible AI use** section (with nav link) explaining the NIH policy — including the six-applications-per-PI-per-year limit — linking the announcement and NOT-OD-25-132, and describing how the suite is designed to assist writing without originating the science.

## [0.13.1] — 2026-07-10

### Added
- `grant-mock-review` grounds its reviewer personas in the target study section's real composition (NIH): fetch the public CSR roster, profile members via RePORTER/PubMed, and aggregate into a dated `00_admin/study-section-profile.md` — expertise clusters, methodological cultures, and gaps relevant to the application. Personas are cast as **archetypes drawn from the distribution**, never as named members: named simulation is inaccurate (caricature from publication records), strategically wrong (assignments are confidential; the closest experts are the likeliest conflicted out), and unfair to real colleagues. NSF panels are confidential — no roster grounding.
- `grant-cover-letter-assignment` shares the same profile: panel expertise gaps feed the needed-expertise field; roster members with directly competing work feed the exclusion conversation.

## [0.13.0] — 2026-07-10

### Added
- Suite version stamping (shared convention 7). `grant-setup` records the installed plugin version — read from the plugin's own `.claude-plugin/plugin.json`, never guessed — in `project-config.md` with the date. The config carries a session-start rule: any later session that finds a different installed version appends the upgrade to a version-history line (old → new, date, context) and the decision log. Detection lives in the config rather than in each skill body, since every skill reads the config first.
- Releases are now tagged in git (annotated `vX.Y.Z`), so the exact suite version recorded in a grant's config can be retrieved later — most useful when revising an application long after submission.

### Changed
- Semver policy amended: **minor** now covers new suite-wide conventions/capabilities affecting how all skills operate, not only new skills — this release is the first example.

## [0.12.5] — 2026-07-10

### Added
- Citation placeholder detection. `grant-references` gains a placeholder sweep in the coverage audit: explicit pattern families — bare markers (`(ref)`, `(cite)`), identifier-bearing (`(PMID: 123456)`, `[ref: 12345]`, DOIs), LaTeX leftovers (`\cite{TODO}`, `??`), and generic to-do markers including Word highlighting — treated as seeds, not an exhaustive list. Identifier-bearing placeholders are resolved via PubMed/Crossref and offered as real citations through the reference manager; the audit reports the placeholder count explicitly, including zero.
- `grant-setup` asks how the PI marks to-be-added citations and records the convention in `project-config.md`, since every investigator has their own habit.
- `grant-format-check` gains a last-gate placeholder grep on the assembled PDFs; any hit is a blocking issue.

## [0.12.4] — 2026-07-10

### Added
- `grant-references` Pass 0 — extract citations in machine-readable form before auditing. Reference-manager citations in Word are field codes, not text: plain-text extraction (pandoc/python-docx) returns only the cached display string and can drop or garble it. The skill now reads `word/document.xml` directly — Zotero/Mendeley fields embed full CSL JSON and EndNote embeds XML records (title, authors, year, DOI per citation), a more reliable verification input than parsing formatted strings. Mixed fielded/hand-typed citations are flagged as a finding (hand-typed entries silently break renumbering); fields are refreshed and the bibliography regenerated before auditing.

### Changed
- `grant-proofread-detail` warns against flagging "missing citations" from extracted plain text, for the same field-code reason.
- `grant-setup` recommends a shared library (Zotero group, EndNote shared, or the repo `.bib`) for multi-author documents — personal-library citations fragment on merge.

## [0.12.3] — 2026-07-10

### Removed
- **`08_references/` folder removed from the standard grant directory structure** — references live inside the manuscripts via the team's reference manager (Zotero, EndNote, Mendeley, or a `.bib` file alongside LaTeX source), so a separate folder had no real contents. `09_final_assembly/` is renumbered to `08_final_assembly/` and the career-award folder to `09_career/`. Grants set up under the old layout keep working (skills follow `project-config.md`), but new audit reports will target the new folder names.

### Added
- `grant-setup` now asks which reference manager the team uses and records it in `project-config.md` — `grant-references` always read this field, but nothing previously collected it.

### Changed
- `grant-references` audits citations where they live (Word fields or `.bib`) and files its reports to `08_final_assembly/`.

## [0.12.2] — 2026-07-10

### Added
- GitHub + LaTeX workflow support: `grant-setup` now offers a GitHub repository as the storage location (common for computational faculty writing NSF proposals in LaTeX), with a git versioning mode — stable filenames, one commit per editing session, annotated tags for status transitions — plus `.gitignore` guidance for LaTeX build artifacts, a private-repo check, and the rule that salary-bearing budgets and prior grants stay out of the repo (git access is repo-wide).

### Changed
- Skills README documents the two versioning modes (filename schema vs. git) as a shared convention; `grant-specific-aims` and `grant-multi-pi-plan` show both modes in their file-naming examples; `grant-resubmission` tags the submitted commit before resubmission edits so the diff against what reviewers read stays one command away.

## [0.12.1] — 2026-07-07

### Changed
- `grant-resource-sharing` refinements: currency hedge with a July 2026 verification date and note that the policy pages moved to grants.nih.gov; added trigger phrasing ("unique/novel organism," "mouse line," "reagent request policy"); reciprocal cross-reference with `grant-facilities-resources` disambiguating the two senses of "resources"; and a decision-log entry for committed repositories, timeframe, and restrictions (a term of award weighed at renewal).

## [0.12.0] — 2026-07-07

### Added
- `grant-resource-sharing` — NIH Resource Sharing Plan(s): the Model Organism Sharing Plan (no cost threshold; distribution form, repository, timeframe, MTA/tech-transfer, Bayh-Dole availability of patented resources) and related research-tool statements. Verified against the current Model Organism Sharing Policy (NOT-OD-04-042, NIH page updated August 2025).

### Changed
- Clear data-vs-resources boundary between `grant-resource-sharing` and `grant-data-management-plan`: data, software, and code stay with the DMSP; physical and biological resources move to the new skill; genomic data stays with the DMSP even when it comes from a shared organism.

## [0.11.0] — 2026-07-07

### Added
- `grant-human-subjects` — the PHS Human Subjects and Clinical Trials Information form, run after the Approach's design and enrollment numbers are settled: study records, clinical-trial classification, inclusion enrollment reports, recruitment feasibility arithmetic, the four-part protection attachment, DSMP, sIRB, and the protocol synopsis with numbers matching the Approach exactly.

### Changed
- `grant-compliance-sections` keeps the human-subjects determination and cross-cutting checks, handing the full form to the new skill.

## [0.10.0] — 2026-07-07

### Added
- `grant-cover-letter-assignment` — NIH cover letter and PHS Assignment Request Form: study section targeting (RePORTER/ART/program-officer grounding), institute assignment, needed-expertise extraction from the final Approach, and sparing, competition-based reviewer exclusions.
- Target study section field in the project config (chosen early, since it shapes the writing); `grant-mock-review` now casts personas as members of the named section.

## [0.9.0] — 2026-07-07

### Added
- `version` field in the plugin manifest, this changelog, and a live "What's new" page on the website that renders the changelog directly from the repository.

## [0.8.0] — 2026-07-07

### Added
- `grant-loi-preproposal` — LOIs, pre-proposals, and DoD white papers, distinguishing administrative notification LOIs from first-stage competitive screens.
- `grant-multi-pi-plan` — Multiple PD/PI Leadership Plan: complementarity case, governance, conflict resolution, resource splits.
- Explicit out-of-scope declarations (training/program grants, post-award, regulatory documents, submission mechanics, non-US funders) in the skills README, with a runtime scope check in `grant-setup`.

## [0.7.0] — 2026-07-07

### Added
- Fellowship support (NIH F30/F31/F32, NSF GRFP) in `grant-career-plan`: sponsor/co-sponsor statements, activities-by-year breakdown, F30 dual-degree and F32 variants, GRFP two-statement structure.
- Fellowship and GRFP review instruments in `grant-mock-review`'s criteria reference.

### Changed
- `grant-setup` gains a `fellowship` award type and NRSA/GRFP citizenship eligibility gate; `grant-budget-justification` stops before producing an R01-style budget for formulaic NRSA awards; `grant-biosketch-support` covers the fellowship biosketch's Scholastic Performance section.

## [0.6.0] — 2026-07-07

### Changed
- License changed from GPL-3.0 to PolyForm Noncommercial 1.0.0: free for academic, nonprofit, and government use; commercial use requires a separate license. Versions previously published under GPL-3.0 remain available under GPL-3.0 to anyone who obtained them.

### Added
- `CONTRIBUTING.md` with a Contributor License Agreement enabling dual licensing.

## [0.5.0] — 2026-07-07

### Added
- `grant-career-plan` — career development awards (NIH K series, NSF CAREER, foundation career awards): training-gap coherence chain, mentor team, mentor statements, institutional commitment, referee letters, RCR plan.
- K-award and NSF CAREER review instruments in `grant-mock-review`'s criteria reference; award-type field in the project config.

## [0.4.0] — 2026-07-07

### Added
- `grant-approach-math` — substance review of a single mathematical component (formulation–aim fit, assumptions, identifiability, complexity, sandbox verification, proof-feasibility fallbacks).
- Workflow diagram (SVG), GitHub Pages site, usage tips in the install guide, and skill-authoring guidance in the skills README.

## [0.3.0] — 2026-07-07

### Added
- `grant-approach-experiment` — deep design review of a single experiment: rationale, controls, confounds, power, analysis plan, interpretation, feasibility.
- `grant-condense` — cutting an over-length draft to the limit: structural cuts ranked by yield, then two-tier sentence tightening with running-total tracking.

### Changed
- Suite-wide convention separating reasoning (conversation) from document text (lean, justified prose); refinements to both new skills from review (power recomputation, measurement fallbacks, versioned report filenames).

## [0.2.0] — 2026-07-06

### Added
- `grant-math-notation` — notation audit for math-heavy proposals: symbol registry, consistency passes, LaTeX mechanics.

### Changed
- Refinement pass across all skills; count-agnostic wording; Office temp files ignored.

## [0.1.0] — 2026-07-06

### Added
- Initial suite of 22 skills covering the full proposal lifecycle: setup, aims, title, budget, significance, innovation, approach, letters, timeline, abstracts, biosketches, facilities, DMP, compliance, mock review, condensing, proofreading, references, format check, resubmission.
- Shared conventions: project-config contract, neutral interaction tone, versioning schema, approved-text-only flow, style profile from prior grants, decision log.
- Install guide for non-technical researchers.
