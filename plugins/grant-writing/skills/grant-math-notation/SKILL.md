---
name: grant-math-notation
description: Audit and refine mathematical notation in math-heavy grant proposals written in LaTeX — symbol consistency, definitions before use, equation correctness checks, theorem/assumption numbering, and LaTeX mechanics. Use whenever a grant contains equations, theorems, algorithms, or mathematical models and the user wants notation checked, mentions LaTeX math, symbol consistency, undefined variables, equation references, or is preparing proposals for math-reviewer audiences (NSF DMS/CISE, DoD/DARPA, DOE, methods-heavy NIH). Also use to evaluate a single section's mathematics before it is merged into the full document.
---

# Mathematical Notation Audit (LaTeX)

Notation is how mathematical reviewers judge rigor before they judge ideas: a symbol that silently changes meaning between Section 2 and Aim 3, or a variable used before it is defined, reads as carelessness — and in a proposal claiming mathematical sophistication, carelessness is disqualifying. This skill audits sections one at a time or the assembled document, and maintains a single source of truth for the proposal's notation.

Read `00_admin/project-config.md` first (run `grant-setup` if missing; this skill assumes the LaTeX workflow — if the project is in Word, the same audit applies to equations but the scripted extraction below is replaced by manual passes). Reports go to `08_final_assembly/notation-audit_<date>.md`; the notation registry lives with the LaTeX source.

## The notation registry

Create and maintain `02_research_plan/notation.md` (or a `notation.tex` comment block): one row per symbol — symbol, meaning, type/domain (scalar, vector in ℝⁿ, operator, set, random variable), where first defined, typographic convention. Every audit updates this registry; every collision or redefinition is caught against it. For proposals dense enough to strain a reviewer's memory, offer to render the registry as a compact notation table in the document itself — reviewers of long technical proposals use these and their presence signals discipline.

## Audit passes (run per section or whole document)

### Pass 1 — Symbol inventory (scripted)

Extract every math token from the LaTeX source: inline `$...$`/`\(...\)`, display environments (`equation`, `align`, `gather`, ...), and custom macros. Build the inventory programmatically (regex or a lightweight parser such as `pylatexenc` — install if needed), recording each symbol's first occurrence and every subsequent use. Then check against the registry:

- **Defined before use**: every symbol introduced in prose ("where $\lambda$ denotes...") at or before first appearance. Flag with location.
- **One symbol, one meaning**: the same letter reused for different objects across sections (the classic: $k$ as index, kernel, and iteration count). Flag every collision with all locations.
- **One meaning, one symbol**: the same object denoted differently in different sections (drift from copy-pasting between papers — common when sections were drafted from different prior manuscripts).
- **Orphan symbols**: defined but never used again (delete the definition or the reviewer hunts for its purpose).

### Pass 2 — Typographic and structural consistency

- Conventions applied uniformly: vectors (bold vs. arrow), matrices, sets (`\mathbb`, `\mathcal`), transpose (`^T` vs `^\top` vs `'`), norms and inner products, expectation/probability operators, argmin/argmax as operators (`\operatorname` or defined macros), differential `d` upright vs. italic. Whichever convention the user holds, hold it everywhere; record it in the registry header.
- Multi-letter identifiers in `\text{}`/`\operatorname{}` (italic `loss` reads as $l \cdot o \cdot s \cdot s$).
- Variables in prose set in math mode ("the parameter λ" as `$\lambda$`, not a unicode character or roman lambda) — inconsistency here is visible in the compiled PDF.
- Theorem/lemma/assumption/algorithm environments: numbering scheme consistent, every one referenced at least once by `\ref`/`\cref`, and assumptions actually invoked where used ("under Assumption 2") — an assumption stated but never invoked draws the question of why it is there.

### Pass 3 — Mathematical sanity

Check what is checkable without refereeing the mathematics: index consistency (free vs. bound indices matching across equation sides; summation limits present or deliberately implicit), dimensional consistency where quantities carry units or shapes (matrix products conformable, norms of the right space), boundary/degenerate cases in stated conditions ($n \geq 1$ vs. $n > 1$ when $n=1$ appears later), and probability statements well-formed (conditioning stated, measures named where it matters). Report suspected *mathematical* errors factually and separately from notation findings — the user is the mathematical authority; the skill's job is to make sure every flag is precise enough to be adjudicated quickly. For substance-level review of a model, derivation, or proof plan during drafting, use `grant-approach-math`; this pass checks only well-formedness.

### Pass 4 — LaTeX mechanics (grant-specific)

- `\label`/`\ref`/`\eqref` integrity: unresolved `??`, equations numbered but never referenced (unnumber with `\nonumber` or `equation*` to reduce clutter), references to equations by hard-coded numbers.
- Macro hygiene: notation defined as macros in one shared preamble file rather than inline — this makes global notation changes one-line fixes and is the mechanism that keeps multi-author sections consistent. Offer to extract repeated constructions into macros.
- Grant format constraints: font-size floors apply to equations too — deeply nested sub/superscripts and shrunken inline fractions can fall below the agency's legibility requirement (coordinate with `grant-format-check`); overfull hboxes push math into margins, which is a compliance violation, not a cosmetic one.
- Compile check: build the document (or section scaffold) and confirm zero errors and no math-related warnings before reporting the audit clean.

## Reporting

Deliver findings as a table per pass: location (file:line and section), finding, severity (collision/undefined = blocking; convention drift = should-fix; style = optional), proposed fix. Apply fixes only with user approval, as new versions per the schema. When a fix changes a symbol globally, regenerate the registry and re-run Pass 1 — global renames are exactly where new collisions sneak in.

Run this audit before `grant-proofread-detail` (line-level proofreading assumes notation is stable) and whenever a new mathematical section is merged from a collaborator, since multi-author notation drift is the dominant source of collisions.
