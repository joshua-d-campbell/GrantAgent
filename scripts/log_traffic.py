#!/usr/bin/env python3
"""Snapshot GitHub Traffic API data into CSVs so history outlives the 14-day window.

The Traffic API (/traffic/clones and /traffic/views) returns only the last 14 days,
and the counts for recent days keep changing until each day closes. This script
UPSERTS by date — newer fetches overwrite the stored row for a given day — so the
CSVs accumulate an accurate long-term record.

Env vars:
  GITHUB_REPOSITORY  "owner/repo"  (provided automatically in GitHub Actions)
  TRAFFIC_TOKEN      a token with read access to repo traffic (see ANALYTICS.md)
"""

import csv
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ.get("TRAFFIC_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    sys.exit("No token: set TRAFFIC_TOKEN (preferred) or GITHUB_TOKEN.")

OUT_DIR = Path(__file__).resolve().parent.parent / "traffic"
OUT_DIR.mkdir(exist_ok=True)


def fetch(endpoint):
    url = f"https://api.github.com/repos/{REPO}/traffic/{endpoint}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # 403 usually means the token lacks push/admin access to traffic data.
        sys.exit(f"GitHub API {e.code} for {endpoint}: {e.read().decode()[:300]}")


def upsert(filename, day_key, rows, fieldnames):
    """Merge new daily rows into the CSV, keyed by date (newer wins)."""
    path = OUT_DIR / filename
    merged = {}
    if path.exists():
        with path.open() as f:
            for row in csv.DictReader(f):
                merged[row["date"]] = row
    for r in rows:
        date = r[day_key][:10]  # ISO timestamp -> YYYY-MM-DD
        merged[date] = {
            "date": date,
            fieldnames[1]: r["count"],
            fieldnames[2]: r["uniques"],
        }
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for date in sorted(merged):
            w.writerow(merged[date])
    print(f"{filename}: {len(merged)} total days on record")


clones = fetch("clones")
views = fetch("views")
upsert("clones.csv", "timestamp", clones.get("clones", []),
       ["date", "clones", "unique_cloners"])
upsert("views.csv", "timestamp", views.get("views", []),
       ["date", "views", "unique_visitors"])
