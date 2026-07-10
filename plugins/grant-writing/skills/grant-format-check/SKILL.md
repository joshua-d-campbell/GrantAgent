---
name: grant-format-check
description: Final compliance/format check of a grant before submission — page limits, margins, fonts, font size, line spacing, file formats, filename rules, and required-attachment completeness. Use in the last days before a deadline, when the user asks to check formatting or submission requirements, or before uploading to Grants.gov/ASSIST/Research.gov. Format violations cause automatic rejection without review.
---

# Format and Submission Compliance Check

Agencies reject non-compliant applications without review — a proposal one line over the page limit, or in the wrong font, does not reach a reviewer. This check is mechanical, absolute, and done last, against the specific FOA and current agency formatting rules.

Read `00_admin/project-config.md` and the FOA summary; pull exact requirements from the FOA and current agency application guide (do not rely on remembered limits — they change and vary by mechanism). Assemble the final document set.

## Build the requirement table

From the FOA/guide, extract the binding rules and record them, noting which source each came from — where the FOA and the general application guide conflict, the FOA wins. Then check each document against them:

- **Page limits** per component (Specific Aims, Research Strategy, Project Description, budget justification, DMSP, biosketch, etc.) — these differ by mechanism (R01 12 pp vs R21 6 pp; NSF 15 pp; NSF biosketch/C&P via SciENcv have their own limits).
- **Font**: NIH accepts Arial, Georgia, Helvetica, Palatino Linotype at ≥11 pt (text); figure/table/legend text no smaller than a legibility floor. NSF specifies allowed fonts/sizes in the PAPPG. Confirm the current list.
- **Margins**: NIH ≥0.5" all sides; NSF 1" — verify.
- **Line spacing / density**: NIH ~≤6 lines per inch; NSF single-spacing conventions.
- **File format**: flattened PDF for most attachments; filename conventions (no special characters; some systems truncate).
- **Other**: line numbering if required, header/footer rules, appendix restrictions (NIH strictly limits appendix material), URL/hyperlink prohibitions in the research plan.

## Verification method

Prefer measurement over eyeballing. Where the workflow allows, script the checks: extract per-attachment page counts from the PDFs; use PDF text/metadata to check embedded fonts and sizes; check margins and filenames programmatically. Report each item as pass/fail with the measured value against the requirement.

For page-limit failures, do not silently cut — report the overage precisely (e.g., "Research Strategy is 12.4 pp; limit 12") and route to `grant-proofread-structure` or the relevant section skill for the user to decide what tightens.

## Placeholder sweep

Grep the extracted text of every final PDF for citation placeholders: the PI's recorded convention from `project-config.md` plus the common families (`(ref)`, `PMID:` outside the bibliography, `[ref:`, `\cite{`-style leftovers, `??`, `TODO`, `XXX`). `grant-references` does the thorough audit earlier; this is the last-gate version on the assembled PDFs, where a hit is a blocking issue — a placeholder in front of reviewers reads as an unfinished application.

## Attachment completeness

Cross-check the assembled set against the `00_admin/` checklist and the FOA's required-documents list: every required attachment present, none prohibited included, signatures present where required (letters, Other Support flattened/signed per current policy), SciENcv-generated documents in the right format for NSF.

## Deliverable

`08_final_assembly/format-check_<date>.md`: a pass/fail table (requirement | measured | status) plus a blocking-issues list. Nothing here is a style opinion — every item is a binary compliance fact. Recommend the user's grants office run their own validation in the submission system (ASSIST/Workspace/Research.gov) as the final gate, since system-level validations catch registration and form errors this check cannot see. For NIH, remind the user to inspect the assembled application image in eRA Commons during the short post-submission viewing window (verify its current length) — the assembled image, not the uploaded files, is what reviewers receive, and assembly can garble figures or drop pages.
