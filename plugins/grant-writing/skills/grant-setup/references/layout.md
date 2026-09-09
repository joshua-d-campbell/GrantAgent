# Layout: placement rules and migration (shared convention 12)

Read in `grant-setup` Step 2, and whenever any skill meets a grant folder without `_agent/`.

## Why

The first real application under this suite ended with 42 markdown files spread across the folders: human admin documents (FOA, office checklist, submission form) buried among AI logs and working notes in `00_admin/`; 20 figure-source files and scripts in the admin folder instead of with the narrative; audit reports filling `08_final_assembly/` while the submitted PDFs sat in section folders; three `_to_delete/` folders nobody had been told about. Nothing was wrong with any single write — no rule said where files go. This file is that rule.

## The rule

*A file goes where the person who needs it will look for it, and files only the AI needs go under `_agent/`.*

`_agent/` sits outside the numbered sequence on purpose: the underscore sorts it first and marks it as not a submission component, while it stays visible in Finder and OneDrive (a dot-folder would be hidden, and `.claude/` already means something else).

## Placement by file type

| What | Where |
|---|---|
| Config, style profile, tracker, decision log, version log, FOA summary, auto-generated checklist | `_agent/` |
| Skill working notes (aims strategy, overlap map, prior-review analysis, notation table, training map, letter tracker, study-section profile) | `_agent/notes/` |
| Section drafts before approval, title candidates | `_agent/drafts/<component>/` — archive or delete once the text is in the document |
| Audit and review reports (mock-review, structural-review, detail-review, format-check, reference-audit, condense-review, notation-audit, experiment-review, math-review, resubmission-response) | `_agent/reports/`, dated |
| Human admin documents: FOA/PA PDFs, general application instructions, office checklist, submission forms (PSF etc.), sponsor correspondence | `00_admin/` (FOA material in `00_admin/foa/`) — the AI writes here only when ingesting the FOA or copying an office file |
| Documents to be submitted | their numbered component folder: working copy + checkpoints; superseded checkpoints in that folder's `_archive/` |
| Rolling pre-write backup (convention 11) | `<component>/_archive/<document>.pre-write.bak` |
| Figure/table files as inserted (Fig1…, Table1…) | `<component>/figures/`, one file per figure |
| Figure sources (.ai, .svg, .tex, .pptx) and scripts that draw concept figures | `<component>/figures/src/` |
| Analyses that compute figures | `<component>/preliminary_data/<aim>/` with `data/`, `scripts/`, `results/`, and `RUNBOOK.md` — the one markdown file allowed outside `_agent/`, because it documents the analysis for a human reproducing it |
| The submission package: PDFs under the funder's required attachment names | `08_final_assembly/` — nothing else |
| Prior proposals and papers for the style corpus | `99_prior_grants/` |

Never create a `_to_delete/` folder in a shared drive without telling the user it exists and must be emptied by hand.

## Pre-0.20 folders

A folder with `00_admin/project-config.md` and no `_agent/` was set up under the old layout (config, logs, and reports in `00_admin/` and `08_final_assembly/`). Until the user accepts migration: read the config where it is; create `_agent/` and write all *new* AI files there; leave existing files in place; record `Layout: legacy` in the config. A folder the user declares final (submitted) is never migrated — it is a record of what was submitted.

## Migration (on request only)

Show the user the full mapping before moving anything. Then **move** (never copy), and rewrite paths in `project-config.md`, `CLAUDE.md`, and `README.md`:

- `00_admin/{project-config,style-profile,tracker,decision-log,version-log}.md`, `00_admin/foa/foa-summary.md`, auto-generated checklist → `_agent/`
- other `00_admin/*.md` working notes → `_agent/notes/`
- figure sources and figure scripts anywhere in `00_admin/` → `<component>/figures/src/`
- `08_final_assembly/*.md` reports → `_agent/reports/`; submitted PDFs found in component folders → `08_final_assembly/` under their attachment names (copy, since the component keeps its final checkpoint)
- section-draft `.md` files in component folders → `_agent/drafts/<component>/`
- `02_*/notation.md`, `09_career/training-map.md`, `05_support_letters/letter-tracker.md`, `00_admin/study-section-profile.md` → `_agent/notes/`
- `06_*/title-candidates*.md` → `_agent/drafts/06_abstracts_title/`
- final figure files loose in `preliminary_data/` → `<component>/figures/`; their sources → `figures/src/`
- superseded checkpoints → the component's `_archive/` per the checkpoint policy (keep the working copy, the last checkpoint sent to readers, and any `final`)

Human documents stay where they are. Append a decision-log entry recording the migration and the suite version, and set `Layout: 0.20` in the config.
