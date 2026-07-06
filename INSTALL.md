# Installing the Grant Writing Skills

The `grant-writing` plugin gives Claude over 20 skills for research grant writing — from project setup and Specific Aims through mock review, format checking, and resubmission. Installing takes about two minutes and requires no technical setup.

## Claude desktop app (recommended for most users)

1. Open the Claude desktop app and go to **Settings → Capabilities** (the plugins/skills section — naming may vary slightly by version).
2. Find the option to **add a plugin marketplace** and enter: `<GITHUB-USERNAME>/GrantAgent`
3. Locate **grant-writing** in the `grant-agent` marketplace and click **Install**.
4. Done. Start a conversation and say "I'm starting a new NIH R01" — the `grant-setup` skill will take it from there.

## Claude Code (terminal users)

```
/plugin marketplace add <GITHUB-USERNAME>/GrantAgent
/plugin install grant-writing@grant-agent
```

## Updates

When the skills are improved, updates flow from this repository automatically (Claude Code refreshes with `/plugin marketplace update`). You never need to re-copy files.

## Notes

- The skills expect each grant to live in its own project folder; the `grant-setup` skill creates the folder structure the other skills rely on. Share that *grant folder* with your collaborators via Google Drive/OneDrive as usual — it is separate from this skill installation.
- Questions or improvements: open an issue on this repository or email the maintainer.

---
*Maintainer note: replace `<GITHUB-USERNAME>` above with the actual GitHub account after pushing this repo. Repo must be public, or colleagues need repo access (they'll authenticate with their GitHub account).*
