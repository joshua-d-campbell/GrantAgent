# CLAUDE.md — Orientation for AI sessions working on this repo

This file is read automatically at the start of a session. It explains what the
GrantAgent repository is and the conventions any AI (or human) must follow when
changing it. Read it before editing anything. If a rule here conflicts with what
you infer from the code, this file wins — or ask the maintainer.

## Two different "config" files — do not confuse them

1. **This file (`/CLAUDE.md`)** governs the *repository* — how the skill suite is
   built, versioned, and kept consistent. It is meta-level: about developing GrantAgent.
2. **`00_admin/project-config.md`** is a per-*grant* file that the skills themselves
   create inside an individual proposal folder. It records that grant's funder,
   deadline, page limits, and document conventions. It has nothing to do with this repo;
   it lives in a researcher's grant directory, not here.

If a task is "add a skill / fix the landing page / cut a release," it concerns this file.
If a task is "help me write my R01," it concerns `project-config.md` and the skills.

## What this repository is

A **Claude plugin marketplace**. Structure:

- `/.claude-plugin/marketplace.json` — the marketplace catalog (name: `grant-agent`).
- `/plugins/grant-writing/` — the single plugin (name: `grant-writing`), version in
  its `.claude-plugin/plugin.json`.
- `/plugins/grant-writing/skills/grant-*/SKILL.md` — the skills. **These directories are
  the single source of truth for what the suite contains.** Everything else (counts,
  tables, the landing page, the diagram) is *derived* and must be reconciled to them.
- `/plugins/grant-writing/skills/README.md` — shared conventions + authoring guide +
  the workflow table. Read it before writing or editing any skill.
- `/docs/` — the GitHub Pages site (`index.html`, `whatsnew.html`, `workflow.svg`),
  served from the `main` branch `/docs` folder at
  https://joshua-d-campbell.github.io/GrantAgent/.
- `/scripts/`, `/.github/workflows/` — analytics logging (see Analytics below).
- Root docs: `README.md`, `INSTALL.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `ANALYTICS.md`, `LICENSE`.

Distribution facts: repo is `joshua-d-campbell/GrantAgent`, **public**. Users install via
`joshua-d-campbell/GrantAgent` → install `grant-writing@grant-agent`. Keeping the repo
public is intentional (methodology only; no proposal content or personal data).

## THE CRITICAL INVARIANT: adding, removing, or renaming a skill

The skill directories are canonical; several other surfaces describe them and drift out
of sync easily (they currently disagree — see Known Issues). Whenever you add, remove, or
rename a skill, update **all** of these in the same commit:

1. `plugins/grant-writing/skills/README.md` — the workflow table (row + phase number).
2. `.claude-plugin/marketplace.json` — the plugin `description` (skill list / count).
3. `docs/index.html` — the skill count (appears in the `<meta name="description">` and
   the hero `.tag`) **and** the skill grid/cards listing.
4. `docs/whatsnew.html` — add a "what's new" entry.
5. `docs/workflow.svg` — the workflow diagram (and its copy, if one exists under the
   plugin's own `docs/`). Regenerate or hand-edit so the new skill appears.
6. `CHANGELOG.md` — a dated entry.
7. `plugins/grant-writing/.claude-plugin/plugin.json` — bump the version (see Versioning).

**Canonical skill count = number of `plugins/grant-writing/skills/grant-*/` directories
that contain a `SKILL.md`.** As of this writing that is **30**. Never state a count that
you have not just verified against the directories; run the consistency check below.

### Consistency check (run before committing a skill change)

```bash
# canonical count
ls -d plugins/grant-writing/skills/grant-*/ | while read d; do [ -f "$d/SKILL.md" ] && echo "$d"; done | wc -l
# where counts are asserted (reconcile all of these to the number above)
grep -rniE '[0-9]+ (claude )?skills|over 20 skills' --include=*.md --include=*.json --include=*.html . | grep -v .git/
# every SKILL.md has valid frontmatter with name == directory name
for f in plugins/grant-writing/skills/grant-*/SKILL.md; do
  d=$(basename $(dirname "$f")); grep -q "^name: $d$" "$f" || echo "NAME MISMATCH: $f";
done
```

## Versioning — two schemas, both real

- **Suite/plugin version** (semver in `plugin.json`): major = breaking change to a shared
  contract (e.g., the config format or folder layout the skills depend on); minor = a new
  skill; patch = refinements and agency-fact updates. Bump on every release; the plugin is
  pinned to this string, so users only get updates when it changes.
- **Document version schema** used *inside* grants (defined in the skills README):
  `<document>_v<NN>_<YYYY-MM-DD>_<status>.<ext>`, status ∈ draft/internal/shared/final.
  This is a convention the skills apply to a researcher's files, not to this repo's files.

## Authoring & product conventions (summary — full detail in skills/README.md)

- **Descriptions are the trigger mechanism.** Write trigger-rich, slightly "pushy"
  `description` frontmatter; keep SKILL.md bodies lean (<~150 lines) and push lookup
  material to a `references/` subfolder.
- **Explain the why**, don't stack all-caps MUSTs. These models follow reasoning better
  than commandments.
- **Neutral tone, no flattery** is a product-wide rule the skills enforce toward users
  (no "great idea"; state strengths/weaknesses as facts). Keep this consistent if you
  edit skill prose.
- **Reasoning vs. document text** (shared convention 4): skills deliver method-selection
  reasoning to the user in conversation, but only reviewer-necessary justification enters
  document text. Preserve this distinction in any drafting skill you touch.
- **Agency facts carry a verify-against-the-current-FOA/guide hedge** and a note of when
  they were checked. Rules change (NIH simplified review framework Jan 2025; NSF PAPPG
  24-1 + supplements). Never assert a page limit or policy as timeless fact.

## Analytics

- **Clones/views history**: `.github/workflows/traffic-stats.yml` runs `scripts/log_traffic.py`
  daily, upserting `traffic/*.csv`. Requires repo secret `TRAFFIC_TOKEN` (fine-grained PAT,
  this repo only, Administration: Read). See `ANALYTICS.md`.
- **Page views**: GoatCounter, site code `camplab`, snippet in `docs/index.html`,
  dashboard at https://camplab.goatcounter.com. Counts landing-page views only, not installs.

## Environment gotchas

- **Git lock files**: this workspace's sandbox often cannot delete `.git/*.lock` after a
  commit, which blocks the next git operation. If a commit fails with a lock error, the
  fix is `rm -f .git/*.lock` run from the user's own terminal. Prefer having the user run
  git commands locally; edit files rather than committing from the sandbox when possible.
- **Commits**: stage intentionally; `git add -A` sweeps in everything. Use a descriptive
  summary line plus a body listing what changed.

## Known issues / open items (update as resolved)

- **Skill-count drift**: the surfaces in the Critical Invariant currently disagree
  (directories 30, README 25, CHANGELOG 22, marketplace "over 20", landing page 30).
  Reconcile all to 30 on the next skill change.
- **Skill-count wording**: `docs/index.html` uses a hard number; consider whether to keep
  exact counts everywhere or move to "30+" to reduce future drift. Exact is more
  impressive but higher-maintenance — maintainer's call.
- **Testing status**: skills were drafted and refined but not yet run through formal eval
  loops. High-value first candidates: grant-specific-aims, grant-approach, grant-mock-review.
```
