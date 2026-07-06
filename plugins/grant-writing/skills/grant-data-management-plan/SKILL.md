---
name: grant-data-management-plan
description: Write a Data Management and Sharing Plan (NIH DMSP) or Data Management Plan (NSF DMP, DoD equivalents) — data types, standards, repositories, timelines, access controls, and preservation. Use whenever the user mentions DMSP, DMP, data sharing plan, data management, repositories (GEO, SRA, dbGaP, Dryad, Zenodo), FAIR data, or any funder data-plan requirement.
---

# Data Management and Sharing Plan

Required at NIH for essentially all research generating scientific data (policy effective January 2023) and at NSF for all proposals. Under the simplified review framework the NIH DMSP is not scored by the study section — program staff assess it — but weak plans generate administrative back-and-forth, the plan becomes a term of award, and noncompliance can affect future funding. Do not promise practices the lab will not follow.

Read `00_admin/project-config.md` and the Approach (data types come from the design). Output to `07_compliance/dmsp_v<NN>_<date>_draft.<ext>`. Verify current format and length guidance (NIH recommends ≤2 pages; NSF 2 pages) and any institute-specific expectations in the FOA.

## Elicit from the Approach and the user

1. **Data inventory**: for each aim — data types, estimated volume, formats (raw and processed), whether human-derived
2. Existing lab/institutional practice: LIMS, electronic notebooks, storage systems, institutional repository
3. Human-subjects constraints: consent language for sharing, de-identification capability, whether controlled access (dbGaP-style) is needed
4. Field norms: the repositories this subfield actually uses

## NIH DMSP structure (six elements)

1. **Data types**: what will be generated and which of it will be shared (scientific data = data needed to validate/replicate findings; the shared subset must be justified if narrower)
2. **Tools/software/code**: what's needed to work with the data; note open vs proprietary and access paths
3. **Standards**: metadata standards, ontologies, file formats — name field-specific ones (MIAME, BIDS, CDISC…) where they exist
4. **Preservation, access, timelines**: named repository per data type (GEO/SRA for sequencing, PDB, dbGaP for controlled human genomic data, generalist like Zenodo/Dryad otherwise); sharing no later than publication or end of award (NIH default expectation); retention period
5. **Access/reuse controls**: for human data — consent-based limits, controlled-access mechanism, who adjudicates; justify any restriction factually
6. **Oversight**: who in the team maintains compliance, how often reviewed

**Genomic data**: large-scale human genomic data trigger the NIH Genomic Data Sharing policy — generally controlled access (dbGaP or an approved equivalent) plus an institutional certification signed by the institution's official, not just the PI. Flag this early; the certification requires institutional sign-off and consent language that supports it.

Match the retention period to the named repository's actual policy — do not promise indefinite retention a repository does not guarantee.

Budget note: data curation and repository costs are allowable and must be incurred during the award; verify the current NIH guidance on where and under what label DMS costs appear in the budget justification, and coordinate line items with `grant-budget-justification`.

## NSF DMP

Same substance, organized per PAPPG/directorate guidance (directorates publish their own DMP expectations — check the relevant one): data types, standards, access and sharing policies, reuse/redistribution rights, archiving. NSF now frames this as the Data Management and Sharing Plan under recent PAPPG updates. Software/code sharing expectations are directorate-dependent.

## Consistency checks

Repository claims vs. computing described in Facilities; de-identification claims vs. the human-subjects section; sharing timeline vs. the project timeline; any "we will share on request" language — flag it, as NIH treats named repositories as the expectation, not request-based sharing.
