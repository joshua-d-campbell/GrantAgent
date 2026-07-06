---
name: grant-title
description: Develop or refine the title of a research grant proposal. Use when the user wants title options, asks whether their title is effective, or has just finished a Specific Aims draft (titles are written after aims stabilize). Also use when checking title character limits for NIH (200 characters), NSF, or other funders.
---

# Grant Title

Write the title after the Specific Aims page exists — the title is a compression of the aims, not a starting point. Read `00_admin/project-config.md` and the current aims version first.

## What a good title does

Reviewers and program officers see the title before anything else; assignment to a study section or program can be influenced by it. A strong title:

- Names the scientific problem and the approach or system, concretely
- Is understandable to reviewers adjacent to the subfield
- Contains the searchable keywords a program officer would use to route it
- Avoids: unexplained acronyms, cleverness at the expense of clarity, vague framing ("Studies of...", "Toward an understanding of..."), and overclaiming ("A cure for...")

## Constraints (verify against the FOA)

- NIH: 200 characters including spaces; resubmissions historically kept the same title so reviewers recognize the application — confirm current guidance
- NSF: concise titles; solicitation may prescribe prefixes (e.g., "CAREER:", "Collaborative Research:", "EAGER:") — these are mandatory when applicable
- DoD/foundations: per announcement; quad charts and public databases truncate long titles

## Method

1. Extract from the aims page: the central question, system/model, method class, and payoff.
2. Generate 6–10 candidate titles spanning styles: declarative ("X drives Y in Z"), mechanistic question framing, method-forward, impact-forward.
3. For each candidate, state factually its strengths and weaknesses: character count, keyword coverage, audience readability, assignment implications. No ranking by enthusiasm — give the user the trade-offs.
4. Check the chosen title against the character limit and any required prefixes.
5. Record the final title in `00_admin/project-config.md` and save candidates considered to `06_abstracts_title/title-candidates.md` (versioned) — earlier candidates often become paper titles or resurface in resubmission.
