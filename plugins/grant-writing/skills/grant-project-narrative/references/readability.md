# Readability reference — formulas, R alternatives, revision tactics

Lookup material for `grant-project-narrative`. The bundled `scripts/check_readability.py`
is the default checker (no dependencies); this file covers the formulas it implements,
R equivalents for users who prefer them, and the revision playbook when scores miss.

## The formulas

- **Flesch-Kincaid Grade Level** = 0.39 × (words ÷ sentences) + 11.8 × (syllables ÷ words) − 15.59
- **Flesch Reading Ease** = 206.835 − 1.015 × (words ÷ sentences) − 84.6 × (syllables ÷ words)

Both are driven by only two ratios: **words-per-sentence** and **syllables-per-word**.
Grade Level weights sentence length heavily; Reading Ease weights vocabulary (syllables)
heavily. That is why a narrative can sit in the right Ease band (60-70) and still grade
too high — one long sentence does it — and why the two fastest fixes are always: split or
trim a long sentence, and swap a long word for a short one.

Syllable counting is heuristic in every implementation (vowel groups with silent-e
handling), so tools disagree by a few tenths. Treat scores as a guide; the targets have
tolerance built in (aim for 7-8, fail only above ~9).

## R alternatives

```r
# Option A: quanteda
library(quanteda)
library(quanteda.textstats)
text <- "Paste the narrative here."
textstat_readability(text, measure = c("Flesch.Kincaid", "Flesch"))
# Flesch.Kincaid -> grade level (target ~7-8)
# Flesch         -> reading ease (target 60-70)
```

```r
# Option B: koRpus (requires a tokenizer)
library(koRpus)
library(koRpus.lang.en)
tagged <- tokenize("Paste the narrative here.", lang = "en")
readability(tagged, index = c("Flesch.Kincaid", "Flesch"))
```

## Jargon swap patterns

The pattern generalizes: name the thing by what a patient would see, feel, or do — not by
the field's term for it.

| Field term | Everyday equivalent |
|---|---|
| fibrotic remodeling | lung scarring |
| gene expression | which genes are turned on or off |
| nasal epithelial sampling | a brushing of cells from inside the nose |
| chronic allograft dysfunction | the new organ slowly stops working |
| biomarker | warning sign / early signal |
| non-invasive diagnostic | a simple test that does not require surgery |
| therapeutic target | a place where a new drug could act |
| cohort | group of patients |
| mortality / morbidity | deaths / serious illness |
| intervention | treatment |

Acronyms: spell out on first use or, better, avoid entirely — three sentences leave no
room to amortize a definition.

## Revision playbook, by failure mode

- **Grade too high, fewer than 3 sentences**: split the longest sentence at its
  conjunction ("but," "and," "which"). This is the single highest-yield fix.
- **Grade too high, already at 3 sentences**: the split is unavailable. Attack
  syllables-per-word (swap "receive" → "get," "detect" → "spot," "utilize" → "use") and
  cut modifier clauses ("in order to," "it is important to note that," stacked adjectives).
  The checker lists the 4+-syllable words to start with.
- **Ease below 60**: vocabulary is too latinate even if sentences are short — same word
  swaps as above; Ease responds mostly to syllables.
- **A sentence over 25 words**: usually two ideas fused; move one idea to the sentence
  where it belongs, or cut it — three sentences cannot carry every nuance, and the
  narrative is not the abstract.
- **Everything passes but it reads clunky**: the formulas cannot hear rhythm. Read it
  aloud; vary sentence openings; make sure the actor is the subject ("This study tests..."
  not "It will be investigated whether...").

## Revision checklist

- [ ] 3 sentences maximum.
- [ ] States the public-health problem, what the study does, and why it matters — in that order.
- [ ] No unexplained acronyms; no field jargon.
- [ ] Every sentence under ~25 words; average ~15-20.
- [ ] Active voice; concrete, everyday words; no word that could be cut.
- [ ] Flesch-Kincaid grade ~7-8 (≤9); Reading Ease ≥60 — verified by script, not estimated.
- [ ] Payoff stated as a possibility grounded in the approach, not a promise beyond it.
- [ ] No confidential information, citations, figure references, or hyperlinks (RePORTER publishes it verbatim).
- [ ] A non-scientist could read it once and repeat back what the project does.
