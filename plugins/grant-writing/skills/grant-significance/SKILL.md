---
name: grant-significance
description: Draft the Significance section of a research grant — the case that the problem matters and the field will change if the work succeeds. Use when the user is writing or revising Significance or Background & Significance (NIH Research Strategy), the importance/impact framing of an NSF Project Description, disease relevance for DoD/CDMRP, or asks how to make a compelling case for why their research matters or how to counter an "incremental" or "low impact" critique.
---

# Significance

Significance argues that the problem is important, the current state of the field is inadequate, and the proposed work will improve scientific knowledge, technical capability, or clinical practice. It is an argument, not a literature review — every cited fact must be load-bearing.

Read `00_admin/project-config.md`, the current aims version, and the style profile first. Length is set by the grant type: within an NIH 12-page Research Strategy, Significance typically runs 1.5–3 pages; a 6-page R21 compresses it to ~1 page; NSF distributes the same content across the Project Description opening and Broader Impacts. Check the FOA and ask the user what allocation they want.

## The argument structure

Build in this order; each paragraph should advance the argument or be cut:

1. **The problem and its scale** — disease burden, scientific bottleneck, technological gap. Quantify (prevalence, cost, error rates). Neutral, cited facts.
2. **State of the field** — what is known, briefly; the strongest existing work acknowledged fairly. Reviewers in the field will know if prior work is misrepresented.
3. **The critical gap or barrier** — precisely what is unknown or impossible today, and *why it has persisted* (technical barrier, missing model, unexamined assumption). This sentence family is the core of the section.
4. **What this project changes** — how the expected outcomes fill the gap; the immediate field-level consequences and the downstream trajectory (new therapeutic targets, enabled measurements, revised framework).
5. **Rigor of the premise** (NIH) — the key prior data the project rests on, and their strength/limitations, stated candidly. Under the simplified review framework this feeds Factor 1 scoring.

Close with a short paragraph mapping expected outcomes onto the aims (one clause per aim), so Significance and the aims page read as one continuous argument rather than a literature essay followed by an unrelated plan.

## How reviewers use this section

- The assigned advocate lifts sentences from Significance into the written critique. Provide liftable material: a one-sentence problem statement, a one-sentence gap, a one-sentence payoff — each quotable without surrounding context.
- Secondary reviewers are often outside the subfield and read fast. Make the gap statement visually findable (bold or a labeled sentence) and state field-internal stakes in plain language rather than assuming them.
- The most common Factor 1 criticism is "incremental." Adjectives do not answer it; evidence does — cite others naming the barrier, show what its persistence costs the field, and quantify the advance over the best current alternative.

## Register and common failures

- Compelling ≠ promotional. The case is made with magnitude, mechanism, and consequence — not adjectives ("critical," "novel," "transformative" carry no information; delete unless quantified).
- State weaknesses of the premise where they exist; proposing the work as the way to resolve them is stronger than hiding them.
- Failure modes to check: significance that argues the *topic* matters but not *this project*; gap statements that are actually convenience statements ("no one has done X" — reviewers ask "is X worth doing?"); background that never converges on the aims.

## Agency notes

- NIH: address importance explicitly — expected advances in knowledge/capability; if clinical, the path to practice. Do not restate Innovation here.
- NSF: importance = Intellectual Merit; societal framing belongs in Broader Impacts (separate, mandatory, scored equally — plan concrete, assessable activities, not gestures).
- DoD/CDMRP: military or disease-specific relevance is a named criterion; tie explicitly to the announcement's focus areas.
- Foundations: mission fit is the significance argument; quote the foundation's own mission language and show alignment factually.

## Method

Outline first (one sentence per paragraph), get user approval on the argument skeleton, then draft paragraph by paragraph interactively. Only approved text enters `02_research_plan/significance_v<NN>_<date>_draft.<ext>`. Track citations inline in a consistent placeholder format (e.g., `[Smith 2024]`) for `grant-references` to resolve later.
