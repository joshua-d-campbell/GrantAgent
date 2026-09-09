---
name: grant-proofread-detail
description: Detailed line-level proofread of grant documents — spelling, grammar, punctuation, figure/table reference integrity, typographic consistency (figure-reference styling, heading hierarchy, emphasis), letter-of-support reconciliation (every named collaborator, consultant, core, or site has a letter; every letter is referenced), abbreviation consistency, and numeric accuracy. Use for final polish after structural review, when the user asks to proofread, copyedit, check figures and tables, check that headings or figure references are formatted consistently, or check that the letters of support match the proposal, or in the last days before a deadline. Run AFTER grant-proofread-structure.
---

# Detailed Proofread

Line-level pass on near-final text. Run only after `grant-proofread-structure` — copyediting text that may still move is wasted work. Read `_agent/project-config.md` and `_agent/style-profile.md`; work through every document headed for submission, one at a time, in reading order.

## Checks per document

**Language.** Spelling (including field terms and gene/protein capitalization conventions), grammar, punctuation, subject-verb agreement in long sentences, dangling modifiers, tense consistency (proposed work in future/present per the style profile), singular/plural of data/criteria/spectra per the user's convention, and variant consistency — one spelling per term throughout ("healthcare/health care", "wildtype/wild-type", US vs UK spellings), resolved per the style profile.

**Voice and punctuation against the style profile.** The profile's closing *Directives* list is a checklist; verify each document against it item by item and report departures with the directive number. Punctuation constraints the profile records (em-dash limits, colon positions, serial comma, hyphenation) are counted, not judged — they are the constraints that drift most in text drafted across sessions, and the ones a reviewer registers as "not written by one person."

**Figures and tables.**
- Every figure/table is cited in the text at least once, before or near its placement; every in-text citation ("Fig. 3B") points to a panel that exists and shows what the sentence claims.
- Numbering is sequential without gaps or duplicates; caption numbering matches in-text numbering (drift here is the single most common late-edit casualty).
- Captions are self-contained: system, n, error bars defined, statistical test named where stats are shown.
- Legibility at print size: font in figures ≥ roughly 8pt equivalent at final scale; flag suspect panels for the user to check visually.

**Letters of support.** A cross-reference check with the same shape as the figure/table one, run across the assembled set rather than per document, because the two sides live in different files. Build two rosters: (a) every collaborator, consultant, core facility, shared instrument, subaward site, data provider, or partner organization named as contributing something in the narrative *and* the supporting documents — budget justification, facilities and resources, multi-PI plan, biosketch personal statements, timeline, human-subjects recruitment sites; (b) every signed letter (signed copies in `05_support_letters/signed/`, assembled into `08_final_assembly/` under the FOA's attachment name), with `_agent/notes/letter-tracker.md` as the index. Then diff in both directions:
- Every entity in (a) has a letter in (b). A resource the budget pays for or the Approach relies on with no letter is a Factor 3 gap reviewers notice; a late edit that added a core or a site is the usual cause.
- Every letter in (b) is anchored to a specific mention in (a) — a signer whose role was cut from the Approach after the letter came in is the most common late-edit casualty, and an orphan letter invites "why is this person not a collaborator?"
- Where both exist, the details agree: name spelling, degree, title, affiliation; and every quantitative commitment (effort, hours, samples, access, meeting cadence) matches the budget and text. Also confirm the letter is signed, dated within the application period, and — for NSF — in the bare single-sentence collaboration format (check the solicitation).
Career-award mentor and institutional-commitment letters have their own rules; check them for the same anchoring and consistency, but defer content questions to `grant-career-plan`.

**Abbreviations.** Each abbreviation defined at first use in each *separately-read* document (abstract, aims, research strategy are read independently); defined once and used consistently thereafter; no two expansions of the same abbreviation; delete abbreviations used fewer than ~3 times.

**Numbers.** Recompute simple arithmetic in the text (percentages, totals, fold-changes); check sample sizes and dollar figures against the budget spreadsheet; units present and consistent (SI usage per field convention).

**Typographic consistency.** Sections drafted in separate sessions and pasted together arrive with different visual conventions, and reviewers read the seams as carelessness. Check that each document uses one scheme throughout:
- Figure/table references styled one way — bold or not, color or not, "Fig." vs "Figure", parenthetical vs in-sentence. The style profile rarely pins this down; take the dominant form in the document as the reference and flag the minority.
- Headings in one style per level — numbering scheme, case, weight, underline, font size, color, spacing before/after — with a consistent hierarchy (no level skipped, no two levels visually identical). Aim headings in the Approach match each other and repeat the aims-page wording verbatim (`grant-proofread-structure` checks the wording; this pass checks the look).
- Emphasis (bold/italic/underline of key terms, hypotheses, deliverables) follows the style profile's stated convention and is not accumulated from different drafting sessions — a document that bolds hypotheses in Aim 1 and italicizes them in Aim 3 has two conventions.
Treat the majority pattern as the convention unless the style profile says otherwise; report the minority instances by location.

**Mechanics of the format.** Word: broken cross-references (grayed "Error! Reference source not found"), leftover tracked changes and comments. LaTeX: unresolved `??` references, missing citations `[?]`, overfull lines that push text into margins.

## Script what is scriptable

Regex catches what tired eyes miss; write throwaway scripts rather than checking these by reading. Get plain text first (`pandoc file.docx -t plain` or python-docx; LaTeX sources read directly), then:

One extraction caveat: reference-manager citations (Zotero/EndNote/Mendeley) are field codes, and plain-text extraction shows only their cached display string — or drops them entirely. Never flag "missing citation" from extracted text alone; confirm against `word/document.xml` (citation audits belong to `grant-references`, which reads the fields directly).

- **Punctuation constraints**: from the style profile's punctuation section, count each constrained mark in the narrative text — em dashes (U+2014, distinguishing en dashes U+2013 in ranges), colons outside the exempt structural positions the profile lists (aim titles, inline labels, figure-panel letters), and any other recorded rule — and report counts per document against the profile's limit, with each hit's sentence.
- **Figure/table integrity**: extract in-text references (`(Fig(?:ure)?s?\.?|Table)\s*S?\d+[A-Za-z]?`) and caption openers (lines starting with the same pattern); diff the sets. Report references without captions, captions never cited, and numbering gaps/duplicates.
- **Abbreviations**: collect candidate tokens (2–8 chars containing ≥2 capitals, e.g. `\b(?=\w*[A-Z]\w*[A-Z])[A-Za-z0-9-]{2,8}\b`), find each token's first occurrence per document, check for a nearby parenthetical definition, and count total uses. The <3-uses deletion candidates fall out of the counts.
- **Letters of support**: extract capitalized multi-word names and organization tokens (`Dr\.|Prof\.|Core|Facility|Center|Institute|University|Hospital`) from the plain text of every assembled document, plus every signer/organization in the letter tracker and the letter PDFs (`pdftotext`); set-diff both ways and list matches whose surrounding numbers (hours, %, n, $) disagree. Name variants ("J. Smith" / "Jane Smith") are the main false-positive source — normalize before diffing.
- **Typography**: for Word, parse `word/document.xml` — for every run matching the figure-reference regex, collect its run properties (`w:b`, `w:i`, `w:color`, `w:u`) and tabulate the combinations; for every paragraph with a heading `w:pStyle` (or direct formatting that makes it look like one — bold, larger `w:sz`, spacing), tabulate style-per-level and flag paragraphs formatted as headings without a heading style. For LaTeX, confirm every figure reference goes through the same macro (`\figref`, `\ref`, `\cref`) and grep for hand-made headings (a `\textbf{...}` line standing alone, `\noindent\textbf`) that bypass `\section`/`\subsection`. The minority combination in each table is the candidate list.
- **Numbers**: extract `n\s*=\s*\d+`, percentages, and dollar amounts with surrounding context; compare against the budget spreadsheet and against each other. Recompute stated totals and percentages.
- **Word mechanics**: a .docx is a zip — inspect `word/document.xml` for `w:ins`/`w:del` (leftover tracked changes) and `w:commentRangeStart` (comments); grep extracted text for `Error! Reference`.
- **LaTeX mechanics**: grep the compile log for `Overfull \hbox`, `Citation .* undefined`, `Reference .* undefined`; grep output-adjacent text for `??`.

Script output is a candidate list, not a finding: confirm every hit by reading the actual sentence before reporting it. False positives near a deadline cost the user time they do not have.

## Method and reporting

For the language pass, work in small chunks (2–3 pages per pass) — line-level error detection degrades over long stretches. Quote the current text verbatim in every finding; never reconstruct it from memory.

Deliver findings as a correction list per document (`_agent/reports/detail-review_<date>.md`): location, current text, proposed correction, severity (error vs. style suggestion). Style suggestions that conflict with the style profile are not offered. Apply corrections only with user approval, in the working copy — line-level fixes are not a checkpoint; corrections the user defers go into `_agent/tracker.md` as `minor` items against their document (`Origin: proofread-detail`) so they survive to the next session without being re-found. Documents that pass cleanly are listed as checked with no findings — no further commentary.
