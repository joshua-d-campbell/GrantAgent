---
name: grant-approach-math
description: Rigorously review a single mathematical component of a grant's Approach — a model formulation, derivation, estimator, algorithm, or theorem plan — for whether the math is right and answers the aim. Use whenever the user is developing the mathematics in an aim, asks whether a formulation, derivation, or proof strategy is sound, wants help choosing or stress-testing a model or estimator, or mentions assumptions, identifiability, well-posedness, convergence, or complexity claims. This is the math-content companion to grant-approach, analogous to grant-approach-experiment for experiments; use grant-math-notation for symbol and notation consistency, not this skill.
---

# Single-Component Mathematical Review

At NSF DMS/CISE, DoD/DARPA, DOE, and in methods-heavy NIH proposals, reviewers with mathematical training probe whether the formulation can actually deliver what the aim promises — a model that cannot be identified from the proposed data, or a "we will prove" attached to an open-problem-hard result, is as fatal as a missing control (verify review-framework specifics against the current FOA and agency guide). This skill audits one mathematical component at a time — a model, derivation, estimator, algorithm, or theorem plan — during drafting, so the flaw surfaces while it is still cheap to fix.

Read `00_admin/project-config.md` first (run `grant-setup` if missing). Division of labor: `grant-approach` owns section structure and cross-aim logic; this skill stress-tests one component's mathematical substance; `grant-math-notation` audits form (symbols, typography, LaTeX) later — do not duplicate its passes here. Findings go to `02_research_plan/math-review_<aim>-<component>_v<NN>_<YYYY-MM-DD>.md`; approved revisions flow back into the aim's Approach file per the versioning schema. Register any symbol introduced or changed during this review in `02_research_plan/notation.md` so `grant-math-notation` starts warm.

## Elicit the component fully before judging it

Prose hides gaps. Draw out, asking only for what is missing, batched into a single message; for genuinely minor gaps, proceed with a stated assumption:

- The scientific question the aim needs this mathematics to answer, and how the component's output feeds the rest of the aim.
- The objects: the model/estimator/algorithm/statement, its inputs and outputs, the data it will be fit to or run on.
- Every assumption, stated or implicit.
- The claim, and its current status: proven, proof sketched, conjectured, or supported only numerically.

State back a one-paragraph structured restatement and get the user's confirmation before auditing.

## Audit dimensions

Report each finding with severity — **blocking** (the mathematics cannot deliver what the aim requires), **should-fix** (weakens rigor or invites reviewer criticism), or **optional** (polish). Neutral tone; each finding names the specific weakness and why it matters.

### 1. Formulation ↔ aim
The mathematics must answer the actual scientific question, not an adjacent, easier one. Check that the quantities the model produces are the quantities the aim promises; that the objects are observable or estimable from data the proposal will actually have; and that simplifications (linearity, discretization, asymptotic regime) do not assume away the phenomenon of interest.

### 2. Assumptions
Every assumption explicit, plausible for the application domain, and invoked somewhere — an assumption stated but never used draws the question of why it is there. Hunt hidden assumptions: independence, stationarity, convexity, smoothness, boundedness, missing-at-random, correct model specification. For each load-bearing assumption, state what breaks when it fails and whether the proposal acknowledges it.

### 3. Claim–evidence chain
Each claim labeled honestly as proven, sketched, conjectured, or numerical — reviewers forgive a conjecture presented as a conjecture and punish one presented as a theorem. Check derivation steps that are checkable; flag any "it can be shown" that spans a nontrivial gap. Overclaiming ("we will prove X" where X would settle a known open problem) is a credibility risk to name directly.

### 4. Well-posedness and identifiability
Does a solution exist, is it unique (or is non-uniqueness handled), is it stable to perturbations in the data? Are the parameters identifiable from the stated data — sample size, design, and noise level — or only in an idealized limit? Probe degenerate and boundary cases ($n=1$, empty sets, zero variance, perfectly correlated predictors) against the stated conditions.

### 5. Algorithms and complexity
Correctness argument for the algorithm (invariant, termination); convergence conditions stated and consistent with the assumptions in dimension 2; complexity and scaling claims consistent with the data sizes and compute budget stated elsewhere in the proposal (coordinate with `grant-budget-justification` and `grant-facilities-resources` when they are not).

### 6. Computational verification
Verify what is verifiable in the sandbox rather than eyeballing: check algebra and calculus steps symbolically (SymPy), hunt counterexamples numerically for claimed inequalities or monotonicities, and run small simulations to sanity-check rates, coverage, or convergence claims. Show the computation with each flag. The user remains the mathematical authority — the skill's job is to make every flag precise enough to adjudicate quickly, and factual discrepancies found by computation are reported separately from judgment calls.

### 7. Feasibility and fallback
Is the proof strategy named, and does the team's track record support it? For theory aims, require the analog of pitfalls-and-alternatives: the weaker-but-still-publishable fallback if the general case resists (a restricted class, an extra regularity assumption, a numerical study in place of a theorem), and the decision point for retreating to it. An aim whose only outcome is "theorem or nothing" is the fragile-dependence flaw in mathematical form. Check timeline realism — theorem-proving time is the hardest to schedule, and reviewers know it.

## Synthesis

Structure the findings file consistently: (1) the confirmed restatement of the component, (2) findings grouped by audit dimension, each tagged blocking / should-fix / optional, with computations attached where run, (3) a triage — blocking issues first, then should-fix ranked by reviewer risk. Findings map onto `grant-approach`'s per-aim template: dimension 1 → N.1 Rationale; dimensions 2–6 → N.3 Experimental design and N.6 Rigor; dimension 7 → N.5 Pitfalls & alternatives.

Where a fix changes scope or resources, note downstream effects on `grant-budget-justification`, `grant-timeline-milestones`, and the aims page, and record material changes in `00_admin/decision-log.md`. Apply revisions to the Approach text only with user approval. For notation and typography, hand off to `grant-math-notation`; for the whole section, `grant-approach`; for a skeptical scoring read once the mathematics is settled, `grant-mock-review`.
