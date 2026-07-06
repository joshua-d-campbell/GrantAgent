# Grant Writing Skill Suite

A suite of over 20 skills covering the full lifecycle of a federal research grant proposal (NIH, NSF, DoD, foundations). Each skill lives in its own directory with a `SKILL.md`.

## Workflow order

| Phase | Skill | Purpose |
|---|---|---|
| 1 | `grant-setup` | Folder structure, FOA ingestion, checklist, config, style profile |
| 2 | `grant-specific-aims` | Aims page drafting and innovation feedback |
| 3 | `grant-title` | Title development after aims stabilize |
| 4 | `grant-budget-justification` | Personnel, line items, justification; syncs aims |
| 5 | `grant-significance` | Significance section |
| 6 | `grant-innovation` | Innovation section |
| 7 | `grant-approach` | Approach, one subsection at a time, rationales first |
| 8 | `grant-letters-of-support` | Early letter drafts for collaborators |
| 9 | `grant-timeline-milestones` | Timeline, milestones, Gantt |
| 10 | `grant-abstracts` | Summary, narrative, lay abstracts |
| 11 | `grant-biosketch-support` | Biosketches, Other Support / Current & Pending |
| 12 | `grant-facilities-resources` | Facilities, equipment, environment docs |
| 13 | `grant-data-management-plan` | NIH DMSP / NSF DMP |
| 14 | `grant-compliance-sections` | Human subjects, vertebrate animals, rigor |
| 15 | `grant-mock-review` | Red-team study section simulation |
| 16 | `grant-math-notation` | Math/LaTeX notation audit for math-heavy proposals (per section or whole document) |
| 17 | `grant-proofread-structure` | High-level flow, missing elements, transitions |
| 18 | `grant-proofread-detail` | Spelling, grammar, figure/table references |
| 19 | `grant-references` | Citation completeness and accuracy |
| 20 | `grant-format-check` | Page limits, fonts, margins, attachments |
| 21 | `grant-resubmission` | Response to reviews, resubmission intro |

Order is a default, not a rule. Budget, letters, and admin documents proceed in parallel with the narrative.

## Shared conventions (all skills follow these)

### 1. Project config contract

`grant-setup` creates `00_admin/project-config.md` in the grant folder. **Every other skill reads this file first** and asks the user to run `grant-setup` if it is missing. It records: funder, mechanism, FOA number, deadline, document format (Word/LaTeX), personnel, page limits, versioning schema, and links to the checklist and style profile.

### 2. Interaction tone

All skills use rigorous, neutral scientific language:

- No flattery. Never "this is a great idea," "excellent work," or similar.
- State strengths and weaknesses as facts, in neutral tone, with reasons.
- No filler praise or encouragement. Substance only.
- Disagree directly, with evidence, when the science or strategy warrants it.

### 3. Versioning schema

`<document>_v<NN>_<YYYY-MM-DD>_<status>.<ext>`

- `NN`: zero-padded integer, incremented per editing session, never reused
- `status`: `draft` → `internal` (shared with team) → `shared` (external readers) → `final`
- Never overwrite a version; each session writes a new file
- Example: `specific-aims_v03_2026-07-12_internal.docx`

### 4. Text refinement flow

Refine text interactively in the AI conversation. Only user-approved text is placed into the document files. Skills never silently edit a document the user has not seen.

### 5. Writing style profile

`grant-setup` ingests prior grants from `99_prior_grants/` into `00_admin/style-profile.md`. All drafting skills read it and recapitulate the researcher's voice.

### 6. Decision log

Skills append significant decisions (scope changes, dropped aims, budget changes) to `00_admin/decision-log.md` with date and rationale, so late-stage skills can detect inconsistencies.

## Agency reference facts — currency

Agency rules change. Facts embedded in these skills were verified July 2026 where possible (NSF PAPPG 24-1 + Supplements NSF 26-200/26-202; NIH simplified review framework effective Jan 2025). Every skill instructs the model to verify limits and requirements against the specific FOA/NOFO and current agency guide before relying on them.

## Testing status

Drafted 2026-07-06. Eval loops (test prompts, baselines, reviewer feedback) deferred to follow-up sessions — recommended first candidates: `grant-specific-aims`, `grant-approach`, `grant-mock-review`.
