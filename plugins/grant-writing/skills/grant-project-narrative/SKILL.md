---
name: grant-project-narrative
description: Write the NIH Project Narrative — the 3-sentence public health relevance statement published verbatim on RePORTER. Use whenever the user mentions project narrative, public health narrative, public health relevance statement, relevance statement, PHN, or "the relevance section" of an NIH application. Drafts in plain language for a lay reader and verifies the reading level with a bundled Flesch-Kincaid script (target grade 7-8). This is the fine-grained companion to grant-abstracts; use it whenever the narrative itself is the deliverable.
---

# NIH Project Narrative (Public Health Relevance Statement)

The Project Narrative is **not a condensed abstract** — that is the mistake that produces bad ones. It is a plain-language statement of why the work matters to public health, written for an intelligent non-scientist: a patient, an advocate, a journalist, a congressional staffer. If funded, it publishes verbatim on RePORTER, where those readers actually encounter it. Compressing technical text yields something short but still technical; this skill instead *transforms* — everyday words, one idea per sentence, relevance first.

Read `00_admin/project-config.md` first (run `grant-setup` if missing). Source material is the finished aims page and Research Strategy — the narrative is written near the end, after the science is settled. Files go to `06_abstracts_title/`, versioned per the shared schema. For the Project Summary/Abstract, lay abstracts, and the rest of the abstract family, use `grant-abstracts`.

## Targets — measured, not estimated

| Measure | Target |
|---|---|
| Length | **3 sentences maximum** (NIH asks for "two or three") |
| Flesch-Kincaid Grade Level | ~7–8; never above ~9 |
| Flesch Reading Ease | 60–70 (higher is fine) |
| Sentence length | ~15–20 words average; no sentence past ~25 |

The two scores pull in different directions, and the sentence cap sharpens the conflict: Grade Level responds most to sentence length, so the easiest grade-lowering fix — splitting a long sentence into two — is unavailable once the draft is at 3 sentences. Hold both constraints by **shortening words and cutting clauses**, never by adding a fourth sentence. Both targets matter; do not sacrifice one for the other.

## Method

1. **Extract, in plain terms.** From the aims/strategy, pull (a) the health problem and who it affects, (b) what the study does, (c) what could change for patients or public health if it works. These become the three sentences — problem, study, payoff — in that order. Lead with relevance, not with the science.
2. **Draft below the reading level from the start.** Swap every technical term for its everyday equivalent as you write, not in a later pass: "lung scarring" not "fibrotic remodeling," "which genes are turned on or off" not "gene expression," "a brushing of cells from inside the nose" not "nasal epithelial sampling." Spell out or drop every acronym. Active voice, concrete nouns, one idea per sentence. Cut any word that can go without changing meaning.
3. **Score the draft** with the bundled checker (zero dependencies, any Python 3):

   ```bash
   python3 scripts/check_readability.py --text "Paste the draft here."
   ```

   It reports both Flesch scores, the sentence count, and per-sentence lengths, and names the specific revision targets (the long sentence, the 4-syllable words) when a check fails. R users who prefer `quanteda` will find equivalent code in `references/readability.md`.
4. **Revise and re-score until every check passes.** Grade too high at 2 sentences: split one. Grade too high at 3: swap long words for short ones and cut clauses — the checker lists the words to attack first. Ease too low: the vocabulary is too latinate; replace multi-syllable words. Then read it aloud once — the formulas cannot hear clunky rhythm.
5. **Verify content**, not just form: problem, study, and payoff all present; no overpromise relative to the actual approach (state it factually if the payoff sentence claims more than the study can deliver); and the sanity test — could a non-scientist read it once and say back what the project does? Suggest the user actually try that on a colleague outside the field.

Refine interactively in conversation; only user-approved text goes to the file (shared convention 4). The reasoning about word swaps and scores stays in the chat — the document gets only the final narrative.

## Example — at target

> Thousands of people get a lung transplant each year, but for many the new lung slowly fails before doctors can spot the damage. This study tests whether a simple brushing of cells from the nose can reveal early warning signs deep in the lung. If it works, this easy test could help doctors act sooner and protect patients before the harm is permanent.

Scores: grade 8.7, ease 70, 3 sentences, longest 25 words. Note the fingerprints of the method: "get" not "receive," "spot" not "detect," no mention of the assay platform, and the payoff stated as a possibility ("if it works"), not a promise.

## Constraints that are easy to forget

- **Public record**: no proprietary or confidential information, no citations, no figure references, no hyperlinks. Anything the user would not want a journalist to quote does not belong here.
- The narrative is a **separate attachment** from the Project Summary/Abstract in the application package; do not merge them or reuse one as the other.
- NIH's instruction wording ("no more than two or three sentences, describe the relevance...") is from the SF424 R&R application guide — verify against the current guide and the specific FOA before relying on it (checked August 2026).
