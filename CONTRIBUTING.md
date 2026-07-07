# Contributing to GrantAgent

Contributions are welcome — new skills, refinements to existing ones, agency-reference updates, and corrections from real proposal experience are all valuable. Before writing anything substantial, please open an issue describing what you have in mind.

## Contributor License Agreement (CLA)

GrantAgent is distributed to the public under the [PolyForm Noncommercial License 1.0.0](LICENSE) and may also be offered by the maintainer under separate commercial license terms. To make that dual-licensing model possible, every contribution must be covered by the agreement below.

**By submitting a contribution to this repository (via pull request or otherwise), you agree that:**

1. **Originality.** The contribution is your original work, or you otherwise have the right to submit it under these terms, and it does not knowingly infringe any third party's rights.
2. **License grant.** You grant Joshua D. Campbell a perpetual, worldwide, non-exclusive, royalty-free, irrevocable, sublicensable, and transferable license to use, reproduce, modify, distribute, publicly display, and relicense your contribution, in whole or in part, under any license terms, including commercial terms.
3. **You keep your copyright.** You retain ownership of your contribution and remain free to use it for any other purpose.
4. **No warranty or obligation.** You provide the contribution as-is, and the maintainer is not obligated to include it in the project.

To confirm agreement, include this line in your first pull request description:

> I have read and agree to the Contributor License Agreement in CONTRIBUTING.md.

Pull requests without this confirmation cannot be merged.

## Contribution guidelines

- Skills live in `plugins/grant-writing/skills/<skill-name>/SKILL.md`, with lookup material in a `references/` subfolder. Read the [shared conventions and authoring guidance](plugins/grant-writing/skills/README.md) first — trigger-rich descriptions, lean bodies, shared state via the project config, and rationale-over-commandment phrasing are what keep the suite coherent.
- Agency facts (page limits, review criteria, effort rules) must carry a verify-against-the-FOA hedge and a note of when they were checked — agency rules change.
- If you add or remove a skill, update the skills README table, the workflow figure (`plugins/grant-writing/docs/workflow.svg`, copied to `docs/workflow.svg`), and the skill count on the landing page (`docs/index.html`).
- Test with 2–3 realistic prompts before submitting, and note in the PR what you tested.
