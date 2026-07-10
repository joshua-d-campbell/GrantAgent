---
name: grant-proofread-structure
description: High-level structural proofread of a full grant proposal — overall flow, missing elements, cross-section consistency, and transitions between major sections. Use when a full draft exists and the user wants a read-through for coherence, asks "does this hang together," wants to check nothing is missing before final polish, or roughly 2-4 weeks before deadline. Run BEFORE grant-proofread-detail; sentence-level editing is wasted on text that may still move.
---

# Structural Proofread

This pass reads the proposal the way a reviewer does — beginning to end, once — and reports on architecture, not sentences. Fixing structure after copyediting wastes the copyedit, so this skill runs first.

Read `00_admin/project-config.md`, the checklist, and the decision log (drift recorded there predicts inconsistencies). Assemble the current latest versions of every section in the order a reviewer encounters them (abstract → aims → research strategy → supporting documents). If two versions of a section have the same status, confirm with the user which is current before proofreading the wrong one.

## Pass 0 — Scripted extraction

Before reading, convert everything to plain text (`pandoc file.docx -t plain` or python-docx; LaTeX sources read directly) and extract into one comparison file, per document:

- Aim headlines and any restatement of the aims (search "Aim", "AIM", numbered lists near "Specific")
- The hypothesis sentence(s) (search "hypothes")
- Every number with context: `n =`, percentages, dollar figures, person-months, dates, durations
- Key terms with known variants (cohort names, intervention names, gene/protein symbols)

Diff these across documents to seed Pass 2's consistency table. The scripts find candidates; the read-through confirms them in context — a wording difference between aims-page and Approach headers is only a finding if the scope actually differs, but a differing `n` is always a finding.



## Pass 1 — Completeness against the checklist

Compare assembled documents against `00_admin/` checklist and the FOA's required elements. Report: missing documents, missing required subsections (e.g., NSF Broader Impacts heading, NIH rigor elements, Results from Prior NSF Support), and sections still at `draft` status this close to deadline.

## Pass 2 — The through-line

Read for the single argument the proposal should make. Check:

- The gap named in Significance is the gap the aims fill; the payoff promised on the aims page is the payoff Expected Outcomes deliver.
- Aims are identical (wording, order, numbering) across aims page, abstract, Approach headers, timeline, and budget justification.
- Hypotheses stated once and consistently — a central hypothesis that mutates between sections is a common artifact of long drafting.
- Numbers agree everywhere: sample sizes, effort, project period, costs, milestone dates.
- Nothing load-bearing appears only once (a method the budget pays for but the Approach never mentions; a collaborator with a letter but no role).
- Every decision-log entry is fully propagated: a subaim dropped in week 3 that survives in the timeline or budget justification is exactly the inconsistency this pass exists to catch. Walk the log entry by entry.

## Pass 3 — Transitions and reader experience

At each major section boundary, check the first paragraph orients the reader and connects to what preceded it. Within sections, check topic sentences carry the argument (a reviewer skimming only first sentences of paragraphs should still get the case). Flag: sections that open cold, background that never converges, repeated content (same preliminary data figure argued twice), and any place a non-specialist reviewer would lose the thread.

## Reporting format

Produce `08_final_assembly/structural-review_<date>.md`:

1. **Blocking issues** — missing elements, contradictions, broken through-line (each with location and specific fix)
2. **Consistency table** — aims/numbers/terms across documents, discrepancies marked
3. **Transition notes** — by section boundary
4. **Observations** — weaknesses that are judgment calls, stated neutrally with the trade-off

Every finding cites document, location, and a verbatim quote of the current text, so the user can act without re-searching ("Aim 3 headline on the aims page says 'validate'; Approach 3.0 says 'identify' — different scope claims"). Quote from the file, never from memory of it — a misquoted finding costs the user's trust in the rest of the report. No summary praise; the absence of a finding is the good news. After the user acts on the report, updated sections get new versions, and `grant-proofread-detail` runs next.
