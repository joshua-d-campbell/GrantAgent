---
name: grant-resource-sharing
description: Draft the NIH Resource Sharing Plan(s) — chiefly the Model Organism Sharing Plan for projects that produce novel/unique model organisms, plus related research-tool and material sharing statements and their MTA/intellectual-property handling. Use whenever the user mentions resource sharing, model organism sharing, sharing or distributing a unique/novel organism, mouse line, strain, reagent, cell line, or plasmid, a reagent request policy, research tools, MTAs, Bayh-Dole, or a Resource Sharing attachment. For sharing of data, software, or code, use grant-data-management-plan instead — this skill covers physical and biological resources, not data.
---

# Resource Sharing Plan (NIH)

NIH separates two sharing regimes, and getting an applicant into the right one is this skill's first job. **Data, software, and code** are governed by the Data Management and Sharing Policy (and, for genomic data, the Genomic Data Sharing Policy) — those belong to `grant-data-management-plan`. **Physical and biological research resources** — model organisms, strains, reagents, cell lines, vectors, and the tools to use them — are governed by the Model Organism Sharing Policy and the Research Tools Policy, and are described in the application's **Resource Sharing** section, which this skill owns. The NIH page for the model organism policy states plainly that the data policies "pertain to data," while the model organism policy covers the organisms and materials themselves; do not merge the two, and do not put data repositories here or model-organism distribution in the DMSP.

Read `00_admin/project-config.md` and the Approach (what novel organisms or materials the aims will generate). Output to `07_compliance/resource-sharing_v<NN>_<YYYY-MM-DD>_<status>.<ext>`. Verify current requirements against the FOA and the NIH sharing-policy pages at time of use — the sharing-policy pages have moved under grants.nih.gov, so a stale link is a signal to re-check. Facts here were verified against NIH's site July 2026: the Model Organism Sharing Policy (NOT-OD-04-042) page was last updated August 5, 2025, and the Genomic Data Sharing Policy interacts with this one (see below) but sits under the data-sharing regime — confirm the current GDS expectations for the relevant organism and data type rather than assuming, since institute-specific and FOA-specific requirements can add to both.

## Step 0 — Does a plan apply?

The Model Organism Sharing Policy applies to any NIH application or proposal that **will produce unique model organism research resources** — with **no cost threshold** and across grants, cooperative agreements, and contracts including SBIR/STTR. So the trigger is scientific, not budgetary: check the Approach for whether the work generates a novel organism or resource. If it does, a plan (or a justification for restricted/impossible sharing) is expected; if it plainly does not, say so rather than manufacturing a plan. Model organisms include non-human mammalian (mouse, rat) and non-mammalian (yeast, C. elegans, Arabidopsis, Drosophila, zebrafish, Xenopus) systems; related resources include genetically modified and mutant organisms, sperm/embryos, vectors, non-human ES cells, established cell lines, screen and mutagenesis protocols, and genetic/phenotypic data for mutant strains.

## Step 1 — Draft the sharing plan

A model organism sharing plan should specify:

- **Distribution mechanism and form** — how novel strains reach the community (mature organisms, sperm, eggs, embryos, or the vectors used to generate them), and whether a **repository** (e.g., a stock center such as JAX, MMRRC, BDSC, ZIRC, or the relevant organism's center) will be used versus distribution directly from the lab.
- **Timeframe** — a reasonable schedule for periodic deposition of materials and associated data; the working expectation is availability no later than publication of the findings that rely on the resource.
- **Contamination/infection risk** — where relevant, how risks are minimized in distribution.
- **Technology transfer and IP** — how the institution will keep the resource widely available and ensure any third-party rights are consistent with the NIH award, and the distribution instrument (typically an **MTA**, e.g., the UBMTA). Direct the user to their technology-transfer office for these, and coordinate with any `grant-letters-of-support` from a repository or distributor.

Scale the detail to the situation, following NIH's own model: a **simple plan** suffices for a project aiming to produce an organism it has not yet made; a **complex plan** is warranted when mice carry IP held by multiple parties. Where sharing will be restricted, the plan is replaced by a **specific, factual justification** — a bare "resources available on request" is the weak form NIH's move toward named mechanisms is meant to discourage; state the actual mechanism.

## Step 2 — Bayh-Dole and patented resources

Under Bayh-Dole the investigator and institution may elect to retain title to a subject invention (such as a novel mouse), but a **patented resource must still be made reasonably available** to the research community per the NIH Grants Policy Statement and Research Tools Policy. If the user anticipates patenting, the plan should acknowledge the retained-title right *and* the continuing availability obligation, not treat the patent as an exit from sharing.

## Boundary and cross-checks

- **Data/software/code → `grant-data-management-plan`.** If the project produces sequencing data, code, or other scientific data alongside organisms, that sharing is described in the DMSP, not here. A project can need both plans; state which resource goes to which document so nothing is double-covered or dropped.
- **Facilities vs. this skill.** `grant-facilities-resources` documents the equipment, cores, and institutional resources *available to perform* the work; this skill covers the novel resources the work *produces and will share*. When a user asks broadly about "resources," disambiguate which sense they mean before drafting.
- **Genomic data** from the organisms still triggers the Genomic Data Sharing Policy (controlled access, institutional certification) — handled in the DMSP, flagged here only so it is not forgotten.
- Resources named in the plan match what the Approach actually generates; any repository or distributor named is real and, if it must commit, has a letter (coordinate with `grant-letters-of-support`); distribution costs, if budgeted, appear in `grant-budget-justification`.
- The plan is a term of award and progress on it is weighed at renewal — do not promise distribution the lab will not sustain. Record the committed repositories, distribution timeframe, and any restriction/justification in `00_admin/decision-log.md`, so the commitment is visible at progress reporting and renewal. Route substantive IP and compliance questions to the technology-transfer and grants offices; the skill drafts and checks completeness, it does not adjudicate.

Agency note: this is an NIH mechanism. NSF handles materials/resource sharing through the Dissemination and Sharing of Research Results policy and any directorate- or solicitation-specific terms; DoD per the announcement. For those funders, apply the same reasoning and place the output where the funder's process expects it.
