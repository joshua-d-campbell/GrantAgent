# Changelog

All notable changes to the GrantAgent skill suite. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is semantic as applied to a skill suite: **major** = breaking changes to shared contracts (project-config fields, folder structure, versioning schema), **minor** = new skill added, **patch** = refinements and agency-fact updates.

Versions 0.1.0–0.8.0 were assigned retroactively; initial development happened as an intensive sprint on 2026-07-06/07. Version 1.0.0 is reserved for completion of the first eval pass (realistic-prompt testing of the priority skills).

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
