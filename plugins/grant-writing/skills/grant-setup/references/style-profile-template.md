# Style profile template

Write `00_admin/style-profile.md` from this template in `grant-setup` Step 4. The profile is the **only** carrier of the PI's voice between sessions: the corpus is read once at setup and not again, and the model retains nothing between chats. A profile that is thin or merely descriptive produces default-register prose no matter how faithfully later sessions read it. Two properties make a profile work:

1. **Paragraph-scale exemplars, quoted verbatim.** Models imitate prose far better than they follow adjectives. "Uses active voice, moderate hedging" constrains almost nothing; three real paragraphs constrain rhythm, clause structure, and density at once. Require at least two to three full paragraphs per register the grant will need (technical narrative, lay/public summary, figure caption, and any others the FOA calls for). Fragments and single sentences illustrate mechanics; they do not teach voice.
2. **A closing directives checklist.** Drafting skills verify their output against it item by item before delivering text. Write each directive as a checkable rule, not a description ("First person plural, active; *we will* for proposed work, *we have* for completed" — not "prefers active voice").

Separate the **portable core** (voice, which carries to the PI's next proposal) from the **project layer** (vocabulary, reviewer history, sweep lists — specific to this application). A new grant's setup can import the core from a prior profile and start a fresh project layer; do not let project-specific material silt into the core.

Punctuation constraints deserve their own section because they are the constraints models violate most reliably even with the rule in front of them. State each as a countable rule with the exempt positions listed, so `grant-proofread-detail` can script the check and drafting skills can count on their own output. If the PI issues a later punctuation rule, **reconcile it into the same section** — never append a second rule that a session could read as superseding or contradicting the first.

Keep proofreading material (habitual misspellings, term-pairing checks) in the project layer under its own heading. It is useful to `grant-proofread-detail`, but it is not voice, and mixing it into the voice sections dilutes both.

---

```markdown
# Writing Style Profile — <PI name>

Built <YYYY-MM-DD> from: <list each source document; public sources preferred — see grant-setup Step 4>. All quotations are verbatim from those documents. Portable core first; project layer at the end.

# Part 1 — Portable core (voice)

## Exemplar passages

Verbatim, 2–3 full paragraphs per register. Label each with source and register. These are the primary reference for drafting; the sections below annotate them.

### Technical narrative (Background / Significance)
> <paragraph 1>

> <paragraph 2>

### Technical narrative (Approach / Methods)
> <paragraph>

### Lay / public summary
> <paragraph>

### Figure caption
> <caption>

<add registers the FOA requires: impact statement, transition plan, broader impacts, …>

## Structure and signposting
- Aim/section template used, if fixed (e.g., Rationale → Prior work → Plan → Preliminary data → Methods → Expected results/pitfalls/alternatives)
- Heading style: noun phrase vs declarative purpose statement; formatting (italic/bold)
- Paragraph shape: length, topic-sentence habit, closing transition habit

## Sentence construction
- Typical length and rhythm; clause habits (parenthetical exemplification, appositive glosses on first use, inline numbered lists)
- Quoted examples of each habit

## Voice, person, tense
- Person and voice, with the approximate active/passive ratio and where passives cluster
- Tense boundary between completed and proposed work

## Claim strength and hedging
- Where the PI is assertive vs hedged (e.g., assertive on method capability, hedged on biological interpretation)
- Preferred hedges: … / Preferred assertions: …
- Distinctive rhetorical habits (e.g., enumerated critique of named prior work), with a quoted instance

## Emphasis and formatting
- Bold / italic / underline conventions and what each marks
- Figure-reference style ("(Fig. 2B)" parenthetical vs "Figure 2 shows")
- List style (inline vs broken out)

## Punctuation constraints
State each as a countable rule with exemptions. Example form:
- Em dashes (U+2014): <none | ≤N per page | unrestricted> in narrative prose. Replacements: period, comma, or `(e.g., …)` parenthetical. En dashes in ranges are not em dashes.
- Colons: only <before a list | in structural labels: aim titles, "Rationale:", figure-panel letters>.
- Other: serial comma, "e.g."/"i.e." comma convention, hyphenation of compound modifiers.
Record the date and origin of each rule. When a rule changes, edit it here; do not append a competing rule.

## Lay-audience register
- How the voice shifts for public/consumer readers (sentence length, analogy, scare-quoted jargon, term unpacking); quoted instance
- What must not bleed in from the technical register

## Figure captions
- Lead (analysis vs observation), density, panel-label convention, whether the statistical model is stated

# Part 2 — Project layer (this application)

## Terminology
- Controlled vocabulary with definitions as the PI uses them; boundaries between internal and clinical/reviewer-facing terms
- Abbreviations in use

## Reviewer history relevant to voice
- Prior critiques that bear on how text is written (tense signaling, vocabulary leakage, over/under-hedging), with the fix adopted

## Proofread sweep list
- Habitual misspellings and mis-typings, verbatim, for `grant-proofread-detail` to grep
- Term pairings to verify (e.g., module → marker gene)

# Directives for drafting in this voice
Checkable rules, one per line, covering person/voice/tense, headings, sentence habits, hedging, emphasis, punctuation, lay register, vocabulary boundary. Drafting skills verify output against this list before delivering text; `grant-proofread-detail` verifies against it in the final pass.
1. …
```
