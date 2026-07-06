---
name: grant-proofread-detail
description: Detailed line-level proofread of grant documents — spelling, grammar, punctuation, figure/table reference integrity, abbreviation consistency, and numeric accuracy. Use for final polish after structural review, when the user asks to proofread, copyedit, or check figures and tables, or in the last days before a deadline. Run AFTER grant-proofread-structure.
---

# Detailed Proofread

Line-level pass on near-final text. Run only after `grant-proofread-structure` — copyediting text that may still move is wasted work. Read `00_admin/project-config.md`; work through every document headed for submission, one at a time, in reading order.

## Checks per document

**Language.** Spelling (including field terms and gene/protein capitalization conventions), grammar, punctuation, subject-verb agreement in long sentences, dangling modifiers, tense consistency (proposed work in future/present per the style profile), singular/plural of data/criteria/spectra per the user's convention.

**Figures and tables.**
- Every figure/table is cited in the text at least once, before or near its placement; every in-text citation ("Fig. 3B") points to a panel that exists and shows what the sentence claims.
- Numbering is sequential without gaps or duplicates; caption numbering matches in-text numbering (drift here is the single most common late-edit casualty).
- Captions are self-contained: system, n, error bars defined, statistical test named where stats are shown.
- Legibility at print size: font in figures ≥ roughly 8pt equivalent at final scale; flag suspect panels for the user to check visually.

**Abbreviations.** Each abbreviation defined at first use in each *separately-read* document (abstract, aims, research strategy are read independently); defined once and used consistently thereafter; no two expansions of the same abbreviation; delete abbreviations used fewer than ~3 times.

**Numbers.** Recompute simple arithmetic in the text (percentages, totals, fold-changes); check sample sizes and dollar figures against the budget spreadsheet; units present and consistent (SI usage per field convention).

**Mechanics of the format.** Word: broken cross-references (grayed "Error! Reference source not found"), leftover tracked changes and comments. LaTeX: unresolved `??` references, missing citations `[?]`, overfull lines that push text into margins.

## Method and reporting

Work in small chunks (2–3 pages per pass) — line-level error detection degrades over long stretches. Where the format allows, offer programmatic help: scripted extraction of figure references vs. figure captions for matching, spell-check runs, cross-reference validation.

Deliver findings as a correction list per document (`09_final_assembly/detail-review_<date>.md`): location, current text, proposed correction, severity (error vs. style suggestion). Style suggestions that conflict with the style profile are not offered. Apply corrections only with user approval, writing new versions per the schema. Documents that pass cleanly are listed as checked with no findings — no further commentary.
