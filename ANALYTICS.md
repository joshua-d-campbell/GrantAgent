# Usage Analytics Setup

Two independent trackers, each needing a one-time setup step from you.

## 1. Clone / view history (GitHub Traffic → CSV)

GitHub's built-in traffic stats (repo **Insights → Traffic**) only keep the last 14 days. The `.github/workflows/traffic-stats.yml` workflow snapshots them daily into `traffic/clones.csv` and `traffic/views.csv`, upserting by date so the record accumulates indefinitely. Clone counts are the best available proxy for plugin installs (though they also include auto-update pulls, and GitHub gives no per-user identity).

**One-time setup — create a token.** The Traffic API needs a token with admin/read access to the repo; the default Actions token often returns 403 on these endpoints, so use a dedicated one:

1. GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Scope it to **only** the `GrantAgent` repository. Under **Repository permissions**, set **Administration: Read-only** (this is what unlocks traffic data). Give it a short expiry and set a calendar reminder to rotate it.
3. Copy the token.
4. In the `GrantAgent` repo → **Settings → Secrets and variables → Actions → New repository secret**. Name it exactly `TRAFFIC_TOKEN` and paste the value.

That's it. The workflow runs daily at 06:17 UTC and can also be triggered manually from the repo's **Actions** tab (**Log traffic stats → Run workflow**). If `TRAFFIC_TOKEN` is absent it falls back to the default token, which may or may not have traffic access depending on GitHub's current behavior.

To read the data later, open the CSVs on GitHub, or ask Claude to chart `traffic/clones.csv` over time.

## 2. Page visits (GoatCounter)

The landing page at `docs/index.html` (your GitHub Pages site) carries a GoatCounter snippet. GoatCounter is free for non-commercial use, cookieless, and needs no consent banner — a good fit for an academic audience.

**Status: configured.** The site code is `camplab`; the dashboard lives at <https://camplab.goatcounter.com> and the snippet is already in `docs/index.html`.

Remaining steps:

1. Confirm GitHub Pages is serving the page: repo **Settings → Pages → Source = Deploy from a branch**, branch `main`, folder `/docs`. Your page will be at `https://joshua-d-campbell.github.io/GrantAgent/`.
2. Visit the page once, then check the GoatCounter dashboard — the hit should appear within a minute. If it doesn't, confirm the site code in the snippet matches your GoatCounter account.

Note this counts *landing-page views*, which is separate from actual installs (people can install straight from Claude without ever opening the page). Read the two trackers together: GoatCounter for interest/reach, clone CSVs for adoption.
