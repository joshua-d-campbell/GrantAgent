# Tracker template

Copy the template below into `00_admin/tracker.md` at setup. Seed the document-status table from the FOA's required-documents list (or the submission checklist), and enter setup's own gaps — missing FOA details, unconfirmed checklist, empty style corpus — as the first tracker items with `Origin: setup`. The operating rules live in `project-config.md` under *Tracker rules*; this file is the state those rules act on. There is exactly one tracker per grant.

What belongs here vs. elsewhere: the tracker holds *open work* — TODO items, deferred fixes, ripple items that must propagate. It does not hold rationale (that is `decision-log.md`) and it does not hold full findings (mock reviews and audit reports stay in `08_final_assembly/`; the tracker holds only the action items they generate, pointing back to the report). A decision-log entry that creates work spawns tracker items referencing it.

---

```markdown
# Work Tracker — <grant short name>

The shared TODO list for this proposal. Every session reads this file at start and
updates it the moment an item is found, resolved, or changed. Rules: see
`project-config.md` → Tracker rules. Rationale for changes goes to `decision-log.md`,
not here.

## Document status

| Document | Status | Last touched | Notes |
|---|---|---|---|
| Specific Aims | not started | — | |
| <every document from the FOA's required list> | not started | — | |

Status values mirror the versioning schema: `not started` → `in revision` → `drafted` → `internal` → `shared` → `final`.

## Open items

| ID | Document / section | Type | Description | Origin | Added |
|---|---|---|---|---|---|
| T-001 | <admin> | content | <e.g., FOA page limits not yet extracted> | setup | <YYYY-MM-DD> |

Types:
- `ripple` — a change elsewhere must propagate here (cut aim still in the timeline, renamed cohort, changed n)
- `minor` — mechanical: spelling, acronym drift, formatting
- `error` — factual or internal inconsistency
- `content` — substantive work still to do

Origin: what created the item — `setup`, a skill name (`mock-review`, `condense`), a decision-log entry date, a report filename.

## Resolved

| ID | Document / section | Description | Resolution | Closed |
|---|---|---|---|---|

Items move here with a one-line resolution note; they are never deleted from the file and their IDs are never reused.
```
