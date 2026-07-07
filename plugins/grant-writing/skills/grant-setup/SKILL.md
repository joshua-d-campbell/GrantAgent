---
name: grant-setup
description: Initialize a new research grant proposal project — folder structure, funding announcement ingestion, submission checklist, versioning schema, writing-style profile from prior grants, and interaction ground rules. Use this whenever the user says they are starting a new grant, proposal, R01/R21/K-award, NSF proposal, DoD white paper, or foundation application, mentions a funding opportunity announcement (FOA/NOFO/PA/RFA/BAA), or asks to "set up" anything grant-related. Also use when another grant skill finds no project-config.md.
---

# Grant Project Setup

Set up the infrastructure for a grant proposal so every later stage (aims, budget, approach, review) has a consistent home. Run this once per proposal; it produces the `project-config.md` contract that all other grant skills depend on.

## Interaction ground rules (apply to this and every subsequent session)

Record these in the config so all future sessions honor them:

- Use rigorous, neutral scientific language in every interaction.
- Never flatter the user ("this is a great idea," "excellent"). State facts.
- Present strengths and weaknesses in neutral tones, each with a stated reason.
- Push back directly, with evidence, when a plan has a scientific or strategic weakness. A grant reviewer will not be polite; being candid now is the useful behavior.

## Step 1 — Gather the essentials

Ask the user for (accept partial answers; record gaps as open items):

1. **Funding announcement**: FOA/NOFO/PA/RFA/BAA number or URL, funder, mechanism (e.g., NIH R01, NSF CAREER, DoD CDMRP), due date. Fetch or copy the announcement text into `00_admin/foa/`. Extract into `00_admin/foa/foa-summary.md`: page limits, review criteria (quote them verbatim — later sections are drafted against them), budget cap, required documents, eligibility constraints, and any letter-of-intent or pre-application requirement with its own deadline (these often fall weeks before the full deadline and are the most commonly missed date). The FOA overrides the agency's general guide wherever they differ; where the FOA is silent, verify against the current guide rather than memory.
2. **Eligibility and submission status**: confirm any career-stage, citizenship (common in DoD; required for NRSA fellowships and NSF GRFP), or institutional eligibility gates before drafting effort is spent — an eligibility miss voids everything else. Ask whether this is a new submission or a resubmission; if resubmission, put the prior reviews in `00_admin/foa/` and note that `grant-resubmission` runs alongside the drafting skills.
3. **Deadline map**: work backward from the sponsor deadline. Ask for the internal grants-office deadline — institutions typically require the complete application days before the sponsor date, so the internal date is the real deadline. Flag long-lead items now: subaward documents (need the partner institution's grants office to sign off), letters of support, biosketches/Other Support from external collaborators, and — for career-development awards and fellowships — referee letters, which referees submit themselves and are the least controllable dependency in the application. These routinely take 2–4 weeks and cannot be compressed at the end.
4. **Team**: PI(s), co-investigators, collaborators, institutions. Record who submits — an authorized institutional official via Grants.gov/ASSIST, Research.gov, eBRAP, or a foundation portal, almost never the PI personally — and confirm the PI has active credentials in that system (eRA Commons, SciENcv, etc.).
5. **Grant administration checklist**: Ask whether their sponsored programs / grants office provided one. If yes, copy it into `00_admin/`. If not, generate one from the FOA's required-documents list plus the agency defaults in `references/agency-checklists.md`, and label it clearly as auto-generated pending office confirmation.
6. **Document format**: Microsoft Word or LaTeX. Record the choice; it determines file templates and how approved text is inserted.
7. **Storage location**: local folder, Google Drive, or OneDrive.

## Step 2 — Create the directory structure

```
<grant-short-name>/
├── 00_admin/            # config, checklist, FOA, decision log, version log
│   └── foa/
├── 01_aims/
├── 02_research_plan/    # significance, innovation, approach
├── 03_budget/
├── 04_biosketches/
├── 05_support_letters/
├── 06_abstracts_title/
├── 07_compliance/       # DMSP, human subjects, facilities, etc.
├── 08_references/
├── 09_final_assembly/
└── 99_prior_grants/     # researcher's previous proposals (style corpus)
```

Adjust names to the mechanism (e.g., add `02_research_plan/broader_impacts/` for NSF), but keep the numbered ordering — it mirrors the workflow.

### Permissions (shared drives)

If the folder lives on Google Drive or OneDrive, the model usually cannot set permissions itself. Produce a concrete instruction list for the user instead:

- All investigators and collaborators: edit access to `01_aims/`, `02_research_plan/`, `06_abstracts_title/`
- Budget folder (`03_budget/`): PI + grants administrator only (salary data is sensitive)
- `99_prior_grants/`: PI only unless stated otherwise
- Grants office contact: access to `00_admin/` and `03_budget/`

If a Drive/OneDrive connector is available, offer to set these directly.

## Step 3 — Establish versioning

Record this schema in the config and use it for every document:

`<document>_v<NN>_<YYYY-MM-DD>_<status>.<ext>` — status ∈ `draft`, `internal`, `shared`, `final`. Increment `NN` each editing session; never overwrite an existing version. Log each new version in `00_admin/version-log.md` (file, date, one-line summary of changes).

## Step 4 — Ingest prior grants → style profile

Ask the user to place previous proposals in `99_prior_grants/`. Read them and write `00_admin/style-profile.md` covering, with examples quoted from the corpus:

- Sentence length and paragraph density; use of topic sentences
- Voice (active/passive ratio), person ("we" vs. impersonal), tense conventions
- Hedging habits ("may," "suggests") vs. assertive claims
- Transition and signposting style; use of bold/italic emphasis
- Terminology preferences and field-specific phrasing
- Figure caption style

Drafting skills recapitulate this profile. If no prior grants are provided, note that the profile is absent and drafting will use standard scientific register until samples arrive.

## Step 5 — Write project-config.md

Create `00_admin/project-config.md`:

```markdown
# Project Config — <short name>
- Funder / mechanism / FOA: ...
- Award type: research | career-development | fellowship   # K/CAREER/foundation career; F30/F31/F32/GRFP
- New submission | resubmission
- Due dates: sponsor ... / internal grants-office ... / LOI-pre-app ...
- Submission system + submitting official: ...
- Document format: Word | LaTeX
- Team: ...
- Page limits: ...         # from FOA summary
- Budget cap / type: ...   # modular vs detailed, direct cost cap
- Versioning: <schema above>
- Tone rules: neutral scientific register, no flattery, strengths/weaknesses stated factually
- Text flow: refine interactively in conversation; only user-approved text enters documents
- Checklist: 00_admin/<checklist file> (office-provided | auto-generated)
- Style profile: 00_admin/style-profile.md (present | pending)
- Open items: ...
```

Also create an empty `00_admin/decision-log.md` and `00_admin/version-log.md`.

## Step 6 — Confirm and hand off

Summarize what was created, list open items (missing FOA details, unconfirmed checklist, empty style corpus), and state the natural next step: drafting the Specific Aims (`grant-specific-aims`) — or for NSF, the Project Summary skeleton. For career-development awards, `grant-career-plan` starts alongside the aims: mentors and referees need the most lead time of anything in the application.

## References

- `references/agency-checklists.md` — default document checklists per funder (NIH, NSF, DoD, foundations). Read when auto-generating a checklist in Step 1.5.
