---
name: grant-multi-pi-plan
description: Draft the Multiple PD/PI Leadership Plan for grants with more than one principal investigator — governance, roles by aim, decision-making and conflict resolution, resource allocation, and the case for why this team: complementary expertise, synergies, and collaboration history. Use whenever an application designates multiple PIs/PDs, or the user mentions multi-PI, MPI, dual-PI, co-PI leadership, leadership plan, contact PI, or how to divide roles, credit, or budget between investigators. Also covers project-coordination/management plans for NSF collaborative and DoD multi-institution proposals.
---

# Multiple PI Leadership Plan

Reviewers read the leadership plan as a proxy for whether the team will actually function — and most plans give them nothing, because most are boilerplate ("the PIs will meet weekly and resolve disagreements collegially") that could be pasted into any application. The document has two jobs: the compliance job (governance mechanics the funder requires) and the strategic job (the argument that *this specific combination* of PIs is worth more than a single PI with co-investigators). The second job is where the plan earns points, and it is the one boilerplate forfeits.

Read `00_admin/project-config.md` first (run `grant-setup` if missing). Files go to `07_compliance/leadership-plan_v<NN>_<YYYY-MM-DD>_<status>.<ext>`, versioned per the schema. NIH requires this attachment whenever multiple PD/PIs are designated; keep it concise (~1 page is conventional — verify any limit in the FOA).

## Step 1 — The case for this team

Elicit per PI, then build a complementarity map (PI → distinct expertise → aims led → what no one else on the team could contribute):

- **Complementary, not redundant.** If two PIs cover the same ground, reviewers ask why this is multi-PI rather than PI-plus-co-investigator — surface the overlap to the user and either sharpen the distinction or question the structure. The strongest plans read as an intersection argument: the project exists *because* these fields meet.
- **Collaboration history.** Joint publications, prior co-funded grants, co-mentored trainees, shared datasets or resources — cite them specifically (reviewers check). A team with no history is a known reviewer concern, not a disqualifier: compensate with concrete integration mechanisms already in motion (a pilot collaboration, exchanged personnel, a joint preliminary-data figure), not promises.
- **Synergy shown, not asserted.** "Synergistic" is an empty word in review; a sentence like "Aim 2 requires Dr. A's models to be constrained by Dr. B's measurements, and neither lab can do this alone" is the argument.

## Step 2 — Governance

Each element concrete enough that an outsider could apply it:

- **Roles and responsibilities** by aim and by function (scientific leads per aim; administrative, data, and compliance leads named).
- **Contact PI** identified, with the explicit note that the role is administrative (the funder's communication conduit), not scientific seniority.
- **Decision-making**: how routine decisions are made (domain authority by aim) versus major ones (scope changes, budget reallocation, personnel — consensus with a stated fallback).
- **Conflict resolution**: a named, credible mechanism — typically an agreed third party (department chair, external advisor) if the PIs deadlock. "We do not anticipate conflicts" is the signature of a weak plan; reviewers know every long collaboration has them.
- **Communication and data flow**: meeting cadences (aim teams, all-PI), and for multi-site teams the shared infrastructure for data, protocols, and records.
- **Change processes**: publication and authorship expectations, adding or replacing a PI, succession if a PI departs, and (where relevant) IP handling.

## Step 3 — Resources

The budget split by PI and site must match the stated roles — a PI who leads two of three aims on 15% of the budget invites a question no narrative answers. Coordinate allocations with `grant-budget-justification` and multi-site facilities with `grant-facilities-resources`.

## Cross-checks before assembly

- Aims page: aim leadership here matches the aims and Approach exactly.
- Biosketches: each PI's personal statement should reinforce the same complementarity story — this plan and the biosketches must read as one narrative (coordinate with `grant-biosketch-support`).
- Budget: splits consistent, effort figures match the personnel plan.
- Record structural decisions (contact PI, aim leadership, splits) in `00_admin/decision-log.md` — they surface again at just-in-time and award negotiation.

## Agency notes (verify against the FOA/solicitation)

- **NIH**: required attachment for any application designating multiple PD/PIs; reviewers evaluate it and cite weak governance in critiques. All PD/PIs share authority and responsibility; the contact PI is administrative.
- **NSF**: a single proposal has one PI plus co-PIs and needs no leadership plan; *collaborative proposals* (linked submissions from multiple institutions) and some solicitations require a Project Management or Coordination Plan — the same content logic applies, organized by institution.
- **DoD**: per the BAA; multi-institution efforts typically need a management plan with an organizational chart and SOW tasks assigned per site.
