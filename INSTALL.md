# Installing the GrantAgent Grant-Writing Skills

This guide walks you through adding a set of grant-writing skills to Claude. Once installed, Claude can help you through the whole federal grant process — setting up your proposal files, drafting Specific Aims, building budgets, writing the Approach, running a mock study-section review, checking formatting, and more (over 20 skills in total).

You do **not** need to know how to code, and you do **not** need to install anything on your computer beyond the Claude app you already use. The whole process takes about five minutes.

If you get stuck at any point, skip to the [Troubleshooting](#troubleshooting) section at the bottom, or email the maintainer.

---

## What these skills are (30-second version)

A "skill" is a set of expert instructions that Claude loads when it recognizes you need it. You never call skills by name — you just describe what you're doing ("I'm starting an NIH R01"), and Claude pulls in the right skill automatically. Installing the **grant-writing** plugin gives Claude all of these grant skills at once. Think of it as teaching Claude how your grants office and an experienced senior colleague would approach each stage of a proposal.

---

## Before you start

You need two things:

1. **The Claude desktop app**, signed in to your account. (If you use Claude only in a web browser, the plugin/marketplace feature may not be available there — use the desktop app.)
2. **The location of the skills:** they live in a repository called `joshua-d-campbell/GrantAgent`. You'll type that exact text in one of the steps below. You do not need a GitHub account to install from a public repository.

---

## Installation — Claude desktop app (recommended for everyone)

Follow these steps in order.

**Step 1 — Open the plugins settings.**
Open the Claude desktop app and go to **Settings → Customize → Plugins**. (The exact menu wording can vary between app versions; if your menu differs, look for a "Plugins," "Capabilities," or "Extensions" section under Settings.)

**Step 2 — Add the marketplace.**
A "marketplace" is just the online location Claude fetches the skills from. Click **Add Marketplace** and enter exactly:

```
joshua-d-campbell/GrantAgent
```

Confirm/add it. Claude will connect to that location and show a marketplace named **grant-agent**.

**Step 3 — Install the plugin.**
In the **grant-agent** marketplace you'll see a plugin called **grant-writing**. Click **Install**. That single plugin contains all the grant skills — you don't install them one by one.

**Step 4 — You're done.**
Start a normal conversation and describe what you're working on, for example:

> *"I'm starting a new NIH R01 application. Can you help me set up?"*

Claude will recognize the task and begin with the `grant-setup` skill, which creates an organized folder for your proposal. From there, just work through your grant naturally — Claude brings in the right skill at each stage.

---

## Installation — Claude Code (only if you use the terminal)

If you're comfortable with a command line, you can install the same plugin with two commands:

```
/plugin marketplace add joshua-d-campbell/GrantAgent
/plugin install grant-writing@grant-agent
```

Most researchers should use the desktop app instructions above instead.

---

## How to use the skills after installing

You don't need to memorize skill names. Just talk to Claude about what you're doing, and it will reach for the relevant skill. A few examples of things you can say:

- *"Help me draft the Specific Aims page for this project."*
- *"Review this experiment in my Approach — are the controls and sample size adequate?"*
- *"My Research Strategy is over the 12-page limit. Help me cut it down."*
- *"Act as an NIH study section and critique my draft."*
- *"Check that every claim in my Significance section is properly cited."*

The best starting point for any new proposal is asking Claude to **set up the project** first — this creates a consistent folder structure and a settings file that all the other skills rely on.

---

## Getting the best results

A few habits make a large difference:

**Set up with the real solicitation.** When you start a project, give Claude the actual FOA/NOFO (or a link to it). Page limits, required sections, and review criteria then come from *your* solicitation rather than general knowledge — agency rules change often.

**Share a prior grant or two.** During setup, Claude builds a style profile from grants you've written before, so drafts come out in your voice instead of generic prose. Drop them in the project's prior-grants folder.

**One document per conversation.** Draft the Approach in one conversation, the budget in another. Long conversations that wander across several documents make Claude drift from the skill's instructions. Starting fresh is cheap — the project's settings file carries your deadline, format, and preferences over, so you never re-explain.

**Put lasting decisions in files, not in chat.** Conversations don't remember each other. Anything that must persist — a dropped aim, a tone preference, a scope change — belongs in the project folder, and the skills record these automatically (in the config file and decision log). If you notice yourself re-explaining the same thing each session, ask Claude to write it into the project config.

**Name the skill when Claude guesses wrong.** Describing your task is usually enough, but you can always be explicit: *"Use grant-mock-review on the current draft."*

**Get critiques from a fresh conversation.** A mock review is most honest when it comes from a conversation that didn't spend hours helping write the text. Start a new conversation for the review, or ask Claude to run it as a separate agent.

**Read before it lands.** The skills are built to show you text before placing it into your documents — take advantage of that rather than waving edits through.

**Run the finishing steps in order.** Condense to the page limit *before* line-by-line proofreading — there's no point polishing text that's about to be cut — and leave the format check for last.

**Corrected Claude the same way twice?** That correction belongs in the skill or the project config, not in every future conversation. Tell Claude to record it.

---

## Keeping the skills up to date

The skills improve over time. When updates are published to the repository, you'll get them automatically the next time the app refreshes the marketplace — you never re-download or re-copy anything. (In Claude Code, you can force a refresh with `/plugin marketplace update`.)

---

## A note on sharing grants with collaborators

There are two separate things, and it's worth keeping them straight:

- **The skills** (what you just installed) — these teach Claude *how* to help. Each collaborator installs them once, using this same guide.
- **Your actual grant files** — the folder Claude creates for a specific proposal. You share *that folder* with co-investigators the usual way (Google Drive, OneDrive, etc.). It is completely separate from the skill installation.

So if a collaborator wants to work on the proposal with Claude's help, they both install these skills **and** get access to your shared grant folder.

---

## Troubleshooting

**I can't find the Plugins settings.**
The path is **Settings → Customize → Plugins**, but menu names vary by app version — look for "Plugins," "Capabilities," or "Extensions." If none appear, make sure you're on the **desktop app** (not the browser) and that it's updated to the latest version.

**It won't accept `joshua-d-campbell/GrantAgent`.**
Type it exactly as shown, with the slash and no spaces, and no `https://` in front. If it still fails, the repository may be private — contact the maintainer to confirm it's public or to request access.

**I installed it but Claude doesn't seem to use the skills.**
Skills trigger on substantial, specific requests. Instead of "help with my grant," try "help me set up a new NIH R01 proposal and draft the Specific Aims." The more concretely you describe the stage you're at, the more reliably Claude reaches for the right skill.

**How do I know it worked?**
After installing, ask Claude directly: *"Which grant-writing skills do you have available?"* It can list them for you.
