---
name: grant-condense
description: Cut a grant proposal down to a page or word limit — identify sections and sentences to remove, then tighten remaining prose sentence by sentence without losing substance. Use whenever a draft runs over a page or word limit, the user says it is too long, needs to fit NIH/NSF page constraints or a foundation word cap, or asks to shorten, trim, condense, or cut a proposal or section after assembling separately drafted parts. Works section by section or across the whole document.
---

# Condensing a Grant to the Page Limit

Sections drafted independently almost always overrun when assembled — each was written to be complete on its own, so the assembled draft carries redundancy no single author saw. Cutting is not damage control; a tight proposal reads as disciplined thinking, and reviewers reading their tenth application reward density. The goal is to lose length, not substance.

Read `00_admin/project-config.md` first (page limit, mechanism, document format). Measure against the *formatted* document, not a word count — page limits are a property of the compiled PDF at the required font/margins, so verify the real overage first (coordinate with `grant-format-check`). In practice: for LaTeX, compile in the sandbox and count pages; for Word, ask the user for the formatted page count. Only if neither is possible, estimate words-per-page calibrated against the user's own document (count words on a known full page), never a generic constant. Word-limited sections (common at foundations) are measured directly by word count. Font, margin, and spacing manipulation is out of scope — it is mostly prohibited and belongs to `grant-format-check`; length must come out of the text. Work on a new version per the schema; never overwrite. Record any content the user decides to drop entirely in `00_admin/decision-log.md`, because a cut aim or dropped analysis often needs to disappear from the abstract, budget, and timeline too.

## Step 0 — Quantify the gap and set a target

State the overage concretely ("Research Strategy is 13.6 pages; limit 12 — roughly 1.6 pages, ~13%, to remove"). Knowing whether the task is a 3% trim or a 25% cut determines the approach: small overages come from sentence-level tightening alone; large ones require structural cuts first. Do the biggest, cheapest cuts before the fine work — there is no point polishing a paragraph that should be deleted.

## Step 1 — Structural cuts (largest yield, do first)

Read the whole document (or section) and find length that can leave with the least loss:

- **Redundancy across sections** — the dominant source of overrun. Background restated in Significance and again opening the Approach; a method described where it is introduced and again where it is used; the central hypothesis re-explained in every aim. Consolidate to one authoritative statement and cross-reference. Flag each with both locations and the recommended single home.
- **Over-explained routine methods** — established techniques described in protocol detail. Cite the method and state only what is nonstandard or critical. Reviewers assume competence in standard technique; spend the page budget on what is new or risky.
- **Low-yield content** — tangential background, over-hedged caveats, preliminary data figures that de-risk nothing the reviewer doubted, an aim or sub-aim that carries less weight than its length. Removing a weak aim is a strategic decision for the user, not a mechanical cut — surface it with the trade-off, do not delete it unilaterally.
- **Figures and tables** — each should earn its footprint; oversized figures and figures duplicating what the text already says are reclaimable space. Note that shrinking a figure can violate the font-size floor (coordinate with `grant-format-check`), so removal usually beats shrinking.

Present structural options as a ranked list — estimated recovery (in pages/words *and* as a fraction of the gap), what is lost, and a recommendation. For example:

| # | Cut | Est. recovery | What is lost | Recommendation |
|---|---|---|---|---|
| 1 | Consolidate hypothesis restatements (Sig. §2, Aim 1 & 3 openers) | ~0.4 pg (25% of gap) | nothing — cross-reference | do it |
| 2 | Drop Fig. 4 (duplicates Table 2) | ~0.3 pg (19%) | visual redundancy only | do it |
| 3 | Compress sub-aim 2.3 to one paragraph | ~0.5 pg (31%) | pilot analysis detail | user decision |

Let the user approve cuts before proceeding — deleting content is theirs to decide; tightening prose is where the skill does the mechanical work.

## Step 2 — Sentence-level tightening

Once structure is settled, tighten remaining prose. Work section by section and present edits in batches as concrete before/afters with the words saved, in two tiers: **mechanical edits** that cannot change meaning (one bulk approval per batch) and **edits touching a claim, hedge, or qualifier** (flagged individually). After each batch, report the running total against the Step 0 target ("recovered ~0.9 of 1.6 pages") so the user knows when to stop. High-yield patterns:

- **Nominalizations back to verbs** — "performed an analysis of" → "analyzed"; "is regulatory of" → "regulates."
- **Empty openers and filler** — "It is important to note that," "In order to" → "To," "due to the fact that" → "because," "a number of" → a number. Delete "very," "quite," "clearly," "novel/critical/important" where they assert rather than show.
- **Redundant pairs and throat-clearing** — "each and every," "future plans," restating the aim's purpose before stating it.
- **Passive to active** where it shortens and the actor matters ("it was observed that X increased" → "X increased").
- **Compression of long noun strings and prepositional chains** — "the mechanism by which the protein regulates the process of transcription" → "how the protein regulates transcription."
- **Merge or split** — two sentences repeating a subject often combine; one overloaded sentence sometimes loses more by being cut than split.

Preserve meaning exactly: never drop a hedge that carries scientific caution ("suggests" vs. "proves"), a quantitative qualifier, a control, or a citation to save words. If a proposed edit changes the claim's strength, flag it rather than making it silently.

## Step 3 — Verify and reconcile

After edits, re-measure the formatted document against the limit; iterate if still over. Then reconcile: if any content was removed in Step 1, check that the abstract, aims page, budget justification, timeline, and figure/equation references no longer point to it (hand to `grant-proofread-structure` for the full consistency pass). Confirm no citation, defined abbreviation, or cross-reference was orphaned by a cut. Run `grant-condense` before `grant-proofread-detail` — line-level copyediting of text that is about to be cut wastes the effort.

Neutral tone throughout: present cuts as facts with their trade-offs, not as judgments of the writing. The researcher decides what substance to sacrifice; the skill's job is to make sure length leaves before meaning does.
