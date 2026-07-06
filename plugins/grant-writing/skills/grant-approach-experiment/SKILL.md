---
name: grant-approach-experiment
description: Rigorously review a single proposed experiment in a grant's Approach section — its rationale, hypothesis, controls (or baselines/ablations), variables and confounds, sample size and power, statistical analysis plan, outcomes and interpretation, and feasibility. Works for wet-lab, computational/simulation, clinical, and engineering experiments. Use whenever the user wants one experiment (or one sub-aim's design) evaluated, asks whether an experiment is well designed, mentions controls, confounds, replicates, power analysis, statistical tests, or wants to stress-test the methods a reviewer will scrutinize. This is the fine-grained companion to grant-approach; use it to audit experiments one at a time.
---

# Single-Experiment Design Review

Under the NIH simplified framework, experimental rigor is the substance of Factor 2 (Rigor and Feasibility); at NSF and DoD it is where methodological reviewers concentrate. Reviewers do not fail proposals because the idea is uninteresting nearly as often as because a key experiment cannot answer the question it is posed to answer. This skill audits one experiment at a time, in depth, so those flaws surface before a reviewer finds them.

Read `00_admin/project-config.md` first (run `grant-setup` if missing). This is the fine-grained companion to `grant-approach`: use `grant-approach` for section structure and cross-aim logic, this skill to stress-test an individual experiment. Findings go to `02_research_plan/experiment-review_<aim>_<date>.md`; approved revisions flow back into the aim's Approach file per the versioning schema.

## Elicit the experiment fully before judging it

Do not review from a paragraph of prose alone — prose hides gaps. Draw out, asking only for what is missing:

- The question this specific experiment answers, and the hypothesis being tested (or, for a genuinely exploratory experiment, the objective and what will be learned regardless of outcome).
- Independent variable(s) manipulated; dependent variable(s)/readouts measured; everything held constant.
- The experimental system (model, cell line, cohort, dataset), groups/conditions, and the comparison being made.
- Controls planned. Replication structure. Intended analysis and success criterion.

State back a one-paragraph structured restatement of the experiment and get the user's confirmation. Misunderstanding the design produces useless findings; the restatement is cheap insurance.

The dimensions below use wet-lab vocabulary by default, but the logic is general — adapt the terms to the experiment type. For **computational/simulation** work: baselines and ablations play the role of controls, held-out test sets and multiple random seeds address replication and overfitting, and benchmark provenance and code/data availability are the feasibility-and-rigor concern. For **clinical/human-subjects** studies: recruitment feasibility, dropout/attrition, blinding, and inclusion criteria dominate. For **engineering/physical** experiments: reference standards, calibration, tolerances, and test conditions. Ask what kind of experiment it is and map accordingly rather than forcing biological framing.

## Audit dimensions

Report each as a finding with severity — **blocking** (the experiment cannot answer its question as designed), **should-fix** (weakens rigor or invites reviewer criticism), or **optional** (polish). Neutral tone; each finding names the specific weakness and why it matters.

### 1. Rationale and hypothesis
The rationale must chain: prior observation → gap/inference → why *this* experiment discriminates between competing explanations. Test the hypothesis for **falsifiability** — if no possible result could contradict it, it is not a hypothesis and reviewers read the experiment as a fishing expedition. Confirm the experiment actually tests the stated hypothesis rather than an adjacent, easier question.

### 2. Controls
The most common fatal flaw. Check for the controls the design requires, by type:

- **Negative controls** (vehicle, sham, scrambled sequence, untreated) — establish the baseline and that the effect is not artifactual.
- **Positive controls** — prove the assay can detect the effect when it is present; without one, a null result is uninterpretable (assay failure vs. true negative).
- **Comparison/reference condition** — the manipulation is measured against the right counterfactual, not a strawman.
- **Technical vs. biological controls**, batch/plate controls, isotype/loading controls as the assay demands.
- For interventions: blinding of outcome assessment and randomization of allocation — their absence is a named rigor criterion, not an optional nicety.

Flag any comparison where a control is missing and state precisely what confound it leaves open.

### 3. Variables and confounds
One independent variable manipulated at a time, or a factorial design that can separate main effects from interactions — not several things changing at once such that a result cannot be attributed. Hunt confounds explicitly: batch effects, cage/litter effects, sex, age, passage number, time-of-day, operator, order effects. Name each plausible confound and whether the design controls, randomizes, or blocks for it. Confirm the readout actually measures the construct claimed (measurement validity), not a proxy that could move for other reasons.

### 4. Sample size, power, replication
Distinguish biological replicates (independent units — the true n) from technical replicates (repeated measurement of one unit — not n; conflating them is a frequent, credibility-damaging error). Check whether an a priori power analysis is stated with its inputs — effect size and its source (pilot data? literature? assumption?), variance estimate, alpha, target power. Underpowered designs are the single most-cited rigor weakness; an experiment powered on an implausibly large effect size is flagged as such. For designs where formal power is not standard (some -omics, exploratory), confirm the justification for n is nonetheless principled.

### 5. Analysis plan and data handling
Sample size (dimension 4) is necessary but not sufficient — the analysis must match the design, and reviewers check this separately. Confirm the stated statistical test fits the data structure: paired vs. unpaired, parametric assumptions actually met or a stated alternative, and crucially, **clustered/nested/repeated-measures data analyzed with methods that respect the dependence** (mixed models, not treating correlated observations as independent — the analytic twin of the biological/technical replicate error). Check for a plan to handle **multiple comparisons** where many tests are run (a genome-wide screen or a panel of endpoints without correction is a standard reviewer objection). Confirm the **primary endpoint is designated in advance** and distinguished from secondary/exploratory ones. Look for pre-specified **data-handling rules** — outlier definition, inclusion/exclusion criteria, and (for staged or clinical work) stopping rules — since these prevent the post-hoc flexibility that reviewers read as a bias risk.

### 6. Outcomes and interpretation
Every plausible outcome must be interpretable in advance. Require, for the main result: what the expected outcome would mean, **and what a contradictory or null result would mean** — an experiment with no articulated interpretation of failure reads as a design that only "works" if the hypothesis is right. Confirm the success criterion is quantitative and pre-specified where possible ("≥2-fold change, p<0.05, n=8" rather than "we expect to see an increase"). Where a finding is load-bearing for the aim, check whether it is confirmed by an **orthogonal method** (a second, independent approach converging on the same conclusion) — orthogonal validation is a hallmark of rigor and its absence is a common criticism of single-method claims. Check that the experiment's output actually feeds the next experiment or aim it is supposed to enable.

### 7. Feasibility and rigor context
Is the experiment achievable with the stated timeline, budget, expertise, and preliminary data? Are key resources authenticated (cell lines, antibodies, organisms — coordinate with `grant-compliance-sections`)? Are relevant biological variables (sex, and others per field) incorporated or their exclusion justified? Are pitfalls acknowledged with concrete alternative approaches and decision points — reviewers read the pitfalls as a direct measure of the investigator's judgment.

## Synthesis

Close with a short triage: the blocking issues that must be resolved for the experiment to be sound, then should-fix items ranked by how much they reduce reviewer risk. Where a fix changes scope, sample size, or resources, note the downstream effects on `grant-budget-justification`, `grant-timeline-milestones`, and the aims page, and record material design changes in `00_admin/decision-log.md`. Apply revisions to the Approach text only with user approval.

For a whole-section pass or cross-aim interdependence, hand back to `grant-approach`; for a skeptical scoring read once the design is settled, `grant-mock-review`.
