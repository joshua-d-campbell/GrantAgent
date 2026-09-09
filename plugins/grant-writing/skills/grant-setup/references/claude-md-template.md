# CLAUDE.md template — session orientation for a grant folder

Copy the template below to `CLAUDE.md` at the root of the grant folder (the folder the user opens or connects as the project — for a GitHub repo, the repo root; commit it). Fill the bracketed fields from `project-config.md`. This is the only file in the grant folder that is read *before* the first message of a session, so it is the one place where "read the config, the style profile, and the tracker first" executes without depending on a skill firing.

Why it exists: every skill says "read `project-config.md` first," but that instruction lives inside skill bodies and runs only after a skill loads. A fresh chat opened in the grant folder has no skill loaded, so nothing tells the session that the folder is a grant project, that a config and style profile exist, or that the grant-writing skills are how work happens here. In practice this produced sessions that edited documents directly, in the model's default voice, without the config. The file below fixes that by putting the orientation in context from turn one.

Keep it short. It orients; it does not restate the skills or the config. Anything that changes per grant lives in `00_admin/`, and this file points there.

---

```markdown
# CLAUDE.md — <grant short name>

This folder is a research grant proposal (<funder> <mechanism>, due <sponsor date>; internal deadline <date>) managed with the **grant-writing** Claude plugin. Read this file's instructions before doing anything else in a session.

## At the start of every session, before responding

1. Read `00_admin/project-config.md` — the contract every skill depends on (funder, format, versioning mode, page limits, team, tone rules, tracker rules). Run its session-start rule (suite-version comparison).
2. Read `00_admin/style-profile.md` — the PI's writing voice. Every sentence of proposal prose produced in this session matches it; see "Voice" below.
3. Read `00_admin/tracker.md` — the one shared TODO list. Present the open items for the document the user names as the working checklist. Do not discuss items outside that document; log findings there instead (rules in the config).
4. If any of these files is missing, say so and run `grant-setup` before other work.

## Work through the skills, not around them

The grant-writing skills carry the method for each document. When the user's request matches a skill, invoke that skill rather than editing files directly — the skill reads the config and profile, follows the versioning mode, and routes findings to the tracker. Common routes:

| Task | Skill |
|---|---|
| Aims, objectives, hypotheses, aim architecture | `grant-specific-aims` |
| Significance / Innovation / Approach | `grant-significance`, `grant-innovation`, `grant-approach` (one experiment: `grant-approach-experiment`; one derivation/model: `grant-approach-math`) |
| Abstract, summary, lay abstract / NIH Project Narrative | `grant-abstracts` / `grant-project-narrative` |
| Title | `grant-title` |
| Budget and justification | `grant-budget-justification` |
| Biosketches, Other Support, C&P | `grant-biosketch-support` |
| Letters of support / collaboration | `grant-letters-of-support` |
| Facilities, equipment | `grant-facilities-resources` |
| Human subjects, vertebrate animals, rigor, SABV, biosafety | `grant-compliance-sections`, `grant-human-subjects` |
| Data management / sharing plan; resource sharing | `grant-data-management-plan`, `grant-resource-sharing` |
| Timeline, milestones, Gantt | `grant-timeline-milestones` |
| Multi-PI leadership plan | `grant-multi-pi-plan` |
| Career award / fellowship components | `grant-career-plan` |
| LOI, pre-proposal, white paper | `grant-loi-preproposal` |
| Cover letter, assignment request | `grant-cover-letter-assignment` |
| Too long / over the page limit | `grant-condense` |
| Citations, bibliography | `grant-references` |
| Math notation (LaTeX) | `grant-math-notation` |
| Mock study section, red-team | `grant-mock-review` |
| Full-draft coherence read | `grant-proofread-structure` (before `-detail`) |
| Line-level proofread, figure refs, letters reconciliation, typography | `grant-proofread-detail` |
| Page limits, fonts, margins, attachments, placeholders | `grant-format-check` |
| Responding to reviews / resubmission | `grant-resubmission` |
| Anything about the project setup, config, or a missing file | `grant-setup` |

## Voice

Proposal prose is the PI's, in the PI's voice. Before delivering any drafted or revised document text, check it against the *Directives* list at the end of `00_admin/style-profile.md`, item by item, and against any punctuation constraints recorded there (count them; do not estimate). Default model register — long em-dash asides, stacked adjectives, hedged-then-restated sentences — is a defect, not a style choice. The scientific ideas originate with the PI; the session collaborates on expression (see the config's authorship rule).

## Tone toward the user

Neutral scientific register. No flattery, no filler encouragement. State strengths and weaknesses as facts with reasons. Push back directly, with evidence, when the science or strategy has a weakness.

## Files

Layout and conventions are in `00_admin/project-config.md`. Before writing to any document, follow its *Write rules*: re-read from disk, check the fingerprint and the `~$` lock file, keep the rolling pre-write backup, log the write. When the user says they edited a file, re-read it in full before anything else. Versioning mode: <filename schema | git>. Document format: <Word | LaTeX>. Never overwrite an existing version in filename mode; never rewrite pushed history in git mode.
```
