---
name: grant-abstracts
description: Write grant abstracts and summaries — NIH Project Summary/Abstract (30 lines), NSF Project Summary (Overview/Intellectual Merit/Broader Impacts), lay abstracts for foundations and CDMRP, and public-facing summaries. Use whenever the user mentions abstract, summary, or lay summary for a grant. For the NIH Project Narrative (public health relevance statement) specifically, use the dedicated grant-project-narrative skill; use this skill for the rest of the family or when several documents are needed together.
---

# Abstracts and Summaries

Abstracts are written near the end, from the finished aims and approach — but they are read first, by every reviewer including those who read nothing else carefully, and they become the public record of funded work. A grant may need several distinct ones; identify which from the FOA before writing.

Read `00_admin/project-config.md`, final aims, and the style profile. Files go to `06_abstracts_title/`, versioned.

## The abstract family

| Type | Audience | Register |
|---|---|---|
| NIH Project Summary/Abstract (≤30 lines) | Reviewers + public (RePORTER) | Technical but broad-scientist-readable |
| NIH Project Narrative (≤3 sentences) | Public | Plain language, public-health relevance — **hand off to `grant-project-narrative`**, which has the method and readability checker |
| NSF Project Summary (1 page, 3 labeled parts) | Reviewers | Overview + Intellectual Merit + Broader Impacts; third person recommended; proposal returned without review if a part is missing |
| Lay abstract (CDMRP, many foundations) | Patients, advocates, boards | No jargon; disease/societal impact first; CDMRP consumer reviewers score it |
| Technical abstract (DoD) | Program + peer reviewers | Mission relevance explicit |

## Construction method

Compression is the right method for **reviewer-facing** abstracts, where the audience shares the field's vocabulary — do not write them fresh; compress existing approved text so no inconsistency can creep in. It is the wrong method for **public-facing** documents (Project Narrative, lay abstracts), which need *transformation* into plain language, not compression — a condensed technical paragraph is still technical. The narrative has its own skill (`grant-project-narrative`); lay abstracts stay here but follow the transformation logic in step 3.

For reviewer-facing abstracts:

1. Extract: the gap sentence (Significance), objective + hypothesis (aims page ¶2), one sentence per aim (aims block headlines), payoff sentence (aims page final ¶).
2. Assemble to the target length, then rewrite transitions for flow.
3. Check register against the audience. For lay abstracts, apply a hard jargon pass: every term a non-scientist would not know is replaced or explained; readability target roughly 8th–10th grade — verify with the checker rather than estimating: `python3 ../grant-project-narrative/scripts/check_readability.py --max-grade 10 --max-sentences 99 --text "..."` (its `references/readability.md` has the jargon-swap patterns too). Read the result aloud logic: one idea per sentence.
4. Verify hard limits from the FOA (line counts, character counts, headings) — these are return-without-review items at NSF and form-validation failures at NIH. Count NIH's 30 lines in the final formatted document (submission font and margins), not in the working draft; line count is a property of formatting.

Refine each abstract interactively in conversation; write only user-approved text to files.

## Public-record and routing constraints

- NIH Summary/Abstract and Project Narrative publish verbatim on RePORTER if funded. No proprietary or confidential information, no citations, no figure references, no hyperlinks (unless the FOA explicitly permits them). Anything the user would not want a competitor or journalist to read does not belong here.
- At NIH, the title and abstract drive CSR referral and reviewer assignment. Put the field-orienting terms — disease, model system, methodology — in the first few lines so the application lands in the intended study section. If the user has a target study section, check the abstract's vocabulary signals it; if the assignment matters enough, remind them a cover letter can request it.

## Drift check

State factually where the abstract overpromises relative to the approach, or where aims in the abstract have drifted from the current aims version — abstracts written late catch drift, which is useful; resolve drift in the source documents, not by papering over it in the abstract.

Lay-abstract drafts benefit from a test on a non-expert: suggest the user send it to a colleague outside the field and ask them to repeat back the project in one sentence.
