---
name: grant-proofread-structure
description: High-level structural proofread of a full grant proposal — overall flow, missing elements, cross-section consistency, and transitions between major sections. Use when a full draft exists and the user wants a read-through for coherence, asks "does this hang together," wants to check nothing is missing before final polish, or roughly 2-4 weeks before deadline. Run BEFORE grant-proofread-detail; sentence-level editing is wasted on text that may still move.
---

# Structural Proofread

This pass reads the proposal the way a reviewer does — beginning to end, once — and reports on architecture, not sentences. Fixing structure after copyediting wastes the copyedit, so this skill runs first.

Read `00_admin/project-config.md`, the checklist, and the decision log (drift recorded there predicts inconsistencies). Assemble the current latest versions of every section in reading order.

## Pass 1 — Completeness against the checklist

Compare assembled documents against `00_admin/` checklist and the FOA's required elements. Report: missing documents, missing required subsections (e.g., NSF Broader Impacts heading, NIH rigor elements, Results from Prior NSF Support), and sections still at `draft` status this close to deadline.

## Pass 2 — The through-line

Read for the single argument the proposal should make. Check:

- The gap named in Significance is the gap the aims fill; the payoff promised on the aims page is the payoff Expected Outcomes deliver.
- Aims are identical (wording, order, numbering) across aims page, abstract, Approach headers, timeline, and budget justification.
- Hypotheses stated once and consistently — a central hypothesis that mutates between sections is a common artifact of long drafting.
- Numbers agree everywhere: sample sizes, effort, project period, costs, milestone dates.
- Nothing load-bearing appears only once (a method the budget pays for but the Approach never mentions; a collaborator with a letter but no role).

## Pass 3 — Transitions and reader experience

At each major section boundary, check the first paragraph orients the reader and connects to what preceded it. Within sections, check topic sentences carry the argument (a reviewer skimming only first sentences of paragraphs should still get the case). Flag: sections that open cold, background that never converges, repeated content (same preliminary data figure argued twice), and any place a non-specialist reviewer would lose the thread.

## Reporting format

Produce `09_final_assembly/structural-review_<date>.md`:

1. **Blocking issues** — missing elements, contradictions, broken through-line (each with location and specific fix)
2. **Consistency table** — aims/numbers/terms across documents, discrepancies marked
3. **Transition notes** — by section boundary
4. **Observations** — weaknesses that are judgment calls, stated neutrally with the trade-off

State findings as facts with locations ("Aim 3 headline on the aims page says 'validate'; Approach 3.0 says 'identify' — different scope claims"). No summary praise; the absence of a finding is the good news. After the user acts on the report, updated sections get new versions, and `grant-proofread-detail` runs next.
