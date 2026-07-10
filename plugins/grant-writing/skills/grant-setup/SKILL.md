---
name: grant-setup
description: Initialize a new research grant proposal project — folder structure, funding announcement ingestion, submission checklist, versioning schema, writing-style profile from prior grants, and interaction ground rules. Use this whenever the user says they are starting a new grant, proposal, R01/R21/K-award, NSF proposal, DoD white paper, or foundation application, mentions a funding opportunity announcement (FOA/NOFO/PA/RFA/BAA), asks to "set up" anything grant-related, or wants a GitHub repo / LaTeX project created for a proposal. Also use when another grant skill finds no project-config.md.
---

# Grant Project Setup

Set up the infrastructure for a grant proposal so every later stage (aims, budget, approach, review) has a consistent home. Run this once per proposal; it produces the `project-config.md` contract that all other grant skills depend on.

Scope check first: this suite supports single-project research grants, career awards, and fellowships from NIH, NSF, DoD, and US foundations. If the mechanism is a training grant (T32/T35), a multi-project program grant (P01/P50/U54, centers), a post-award document (RPPR, JIT), or a non-US funder, say so plainly — these are out of scope and half-supporting them misleads. Individual components (one project within a P01, a biosketch, a budget) can still use the matching skills, stated as such.

## Interaction ground rules (apply to this and every subsequent session)

Record these in the config so all future sessions honor them:

- Use rigorous, neutral scientific language in every interaction.
- Never flatter the user ("this is a great idea," "excellent"). State facts.
- Present strengths and weaknesses in neutral tones, each with a stated reason.
- Push back directly, with evidence, when a plan has a scientific or strategic weakness. A grant reviewer will not be polite; being candid now is the useful behavior.

## Step 1 — Gather the essentials

Ask the user for (accept partial answers; record gaps as open items):

1. **Funding announcement**: FOA/NOFO/PA/RFA/BAA number or URL, funder, mechanism (e.g., NIH R01, NSF CAREER, DoD CDMRP), due date. Fetch or copy the announcement text into `00_admin/foa/`. Extract into `00_admin/foa/foa-summary.md`: page limits, review criteria (quote them verbatim — later sections are drafted against them), budget cap, required documents, eligibility constraints, and any letter-of-intent or pre-application requirement with its own deadline (these often fall weeks before the full deadline and are the most commonly missed date; drafted with `grant-loi-preproposal`). The FOA overrides the agency's general guide wherever they differ; where the FOA is silent, verify against the current guide rather than memory.
2. **Eligibility and submission status**: confirm any career-stage, citizenship (common in DoD; required for NRSA fellowships and NSF GRFP), or institutional eligibility gates before drafting effort is spent — an eligibility miss voids everything else. Ask whether this is a new submission or a resubmission; if resubmission, put the prior reviews in `00_admin/foa/` and note that `grant-resubmission` runs alongside the drafting skills.
3. **Deadline map**: work backward from the sponsor deadline. Ask for the internal grants-office deadline — institutions typically require the complete application days before the sponsor date, so the internal date is the real deadline. Flag long-lead items now: subaward documents (need the partner institution's grants office to sign off), letters of support, biosketches/Other Support from external collaborators, and — for career-development awards and fellowships — referee letters, which referees submit themselves and are the least controllable dependency in the application. These routinely take 2–4 weeks and cannot be compressed at the end.
4. **Team**: PI(s), co-investigators, collaborators, institutions. Record who submits — an authorized institutional official via Grants.gov/ASSIST, Research.gov, eBRAP, or a foundation portal, almost never the PI personally — and confirm the PI has active credentials in that system (eRA Commons, SciENcv, etc.).
5. **Grant administration checklist**: Ask whether their sponsored programs / grants office provided one. If yes, copy it into `00_admin/`. If not, generate one from the FOA's required-documents list plus the agency defaults in `references/agency-checklists.md`, and label it clearly as auto-generated pending office confirmation.
6. **Document format**: Microsoft Word or LaTeX. Record the choice; it determines file templates and how approved text is inserted. Also ask which reference manager the team uses (Zotero, EndNote, Mendeley, or hand-maintained BibTeX for LaTeX) — citations live inside the manuscripts via the manager, not in a separate folder, and `grant-references` needs to know the toolchain to audit them. For multi-author documents, recommend a shared library (Zotero group library, EndNote shared library, or the `.bib` in the repo) — citations inserted from co-authors' personal libraries fragment on merge and produce duplicate bibliography entries. Also ask how the PI marks citations still to be added — every investigator has a habit: `(ref)`, `(PMID: 123456)`, `[ref: 123455]`, highlighting, `TODO` — and record it; `grant-references` and `grant-format-check` sweep for exactly this convention so no placeholder reaches submission.
7. **Storage location**: local folder, Google Drive, OneDrive, or a GitHub repository. Computational faculty writing NSF proposals commonly pair LaTeX with a GitHub repo as the shared home — if the user mentions either, ask about the other. For GitHub: record the repo URL, confirm it is **private**, and note how collaborators edit (direct commits, PRs, or Overleaf–GitHub sync). Storage choice determines the versioning mode in Step 3.

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
├── 08_final_assembly/   # assembled docs, audit reports, cover letter
└── 99_prior_grants/     # researcher's previous proposals (style corpus)
```

Adjust names to the mechanism (e.g., add `02_research_plan/broader_impacts/` for NSF), but keep the numbered ordering — it mirrors the workflow.

### GitHub repositories

Use the same structure at the repo root. Additionally:

- Add a `.gitignore` for LaTeX build artifacts (`*.aux`, `*.log`, `*.bbl`, `*.blg`, `*.out`, `*.synctex.gz`, `*.fls`, `*.fdb_latexmk`). Committing the compiled PDF is the user's choice — some teams commit it at status transitions so non-LaTeX collaborators can read without building; record the choice.
- Git access is repo-wide — per-folder permissions are impossible. Sensitive material therefore stays out of the repo: detailed budgets with salary data (`03_budget/`) and `99_prior_grants/` live in a local or drive folder unless the user explicitly accepts that all repo collaborators see them. Record where each excluded folder actually lives in the config.
- A `README.md` at repo root pointing to `00_admin/project-config.md` helps collaborators who arrive via GitHub rather than via these skills.

### Permissions (shared drives)

If the folder lives on Google Drive or OneDrive, the model usually cannot set permissions itself. Produce a concrete instruction list for the user instead:

- All investigators and collaborators: edit access to `01_aims/`, `02_research_plan/`, `06_abstracts_title/`
- Budget folder (`03_budget/`): PI + grants administrator only (salary data is sensitive)
- `99_prior_grants/`: PI only unless stated otherwise
- Grants office contact: access to `00_admin/` and `03_budget/`

If a Drive/OneDrive connector is available, offer to set these directly.

For GitHub, translate the same access tiers into collaborator invitations: investigators get write access; the grants office contact rarely works in GitHub, so plan to deliver budget and admin documents by another channel rather than adding them to the repo.

## Step 3 — Establish versioning

Record the versioning mode in the config and use it for every document. The mode follows the storage choice:

**Filename mode** (local, Drive, OneDrive): `<document>_v<NN>_<YYYY-MM-DD>_<status>.<ext>` — status ∈ `draft`, `internal`, `shared`, `final`. Increment `NN` each editing session; never overwrite an existing version. Log each new version in `00_admin/version-log.md` (file, date, one-line summary of changes).

**Git mode** (GitHub repo): git history *is* the version log — do not duplicate it with versioned filenames. Use stable filenames (`01_aims/specific-aims.tex`), commit at the end of each editing session with a message summarizing the change, and mark status transitions (`draft` → `internal` → `shared` → `final`) with annotated tags (e.g., `aims-internal-2026-07-12`) or the team's existing branch/PR convention. Never rewrite pushed history. Skip `version-log.md`; the decision log is still kept — commit messages record *what* changed, the decision log records *why*. Wherever another skill says "new version per the schema," in git mode that means a commit (plus a tag if the status changed).

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

First, record which suite version is shaping this application: read `version` from the installed grant-writing plugin's `.claude-plugin/plugin.json` (the plugin directory two levels above this skill's folder). If it cannot be located, record `unknown` — never guess. This matters most long after submission: a revision a year later can check what methodology version the original was written under, and the repository's git tags let anyone retrieve that exact version.

Create `00_admin/project-config.md`:

```markdown
# Project Config — <short name>
- Suite version: grant-writing <X.Y.Z> (recorded <YYYY-MM-DD>)
- Suite version history: none   # appended on upgrade: "<old> → <new> on <date> — <context, e.g. mid-draft, resubmission>"
- Session-start rule: compare the installed grant-writing plugin version (its .claude-plugin/plugin.json) against Suite version above; if different, update it, append the change to the history line, and add a decision-log entry
- Funder / mechanism / FOA: ...
- Award type: research | career-development | fellowship   # K/CAREER/foundation career; F30/F31/F32/GRFP
- New submission | resubmission
- Due dates: sponsor ... / internal grants-office ... / LOI-pre-app ...
- Submission system + submitting official: ...
- Document format: Word | LaTeX
- Reference manager: Zotero | EndNote | Mendeley | BibTeX (.bib) | none yet
- Citation placeholder convention: ...   # how the PI marks to-be-added citations, e.g. "(PMID: <id>)", "(ref)"
- Storage: local | Google Drive | OneDrive | GitHub repo <URL, private, edit workflow>
- Excluded from repo (git mode): 03_budget/ at <location>, 99_prior_grants/ at <location>
- Team: ...
- Page limits: ...         # from FOA summary
- Target study section / IC: ...   # decide early — shapes the writing; grant-cover-letter-assignment finalizes the request
- Budget cap / type: ...   # modular vs detailed, direct cost cap
- Versioning: filename schema | git (commits + status tags)
- Tone rules: neutral scientific register, no flattery, strengths/weaknesses stated factually
- Text flow: refine interactively in conversation; only user-approved text enters documents
- Checklist: 00_admin/<checklist file> (office-provided | auto-generated)
- Style profile: 00_admin/style-profile.md (present | pending)
- Open items: ...
```

Also create an empty `00_admin/decision-log.md` and — in filename mode only — `00_admin/version-log.md`.

## Step 6 — Confirm and hand off

Summarize what was created, list open items (missing FOA details, unconfirmed checklist, empty style corpus), and state the natural next step: drafting the Specific Aims (`grant-specific-aims`) — or for NSF, the Project Summary skeleton. For career-development awards, `grant-career-plan` starts alongside the aims: mentors and referees need the most lead time of anything in the application.

## References

- `references/agency-checklists.md` — default document checklists per funder (NIH, NSF, DoD, foundations). Read when auto-generating a checklist in Step 1.5.
