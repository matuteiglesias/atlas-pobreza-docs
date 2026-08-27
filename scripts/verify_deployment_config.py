#!/usr/bin/env python3
"""Reject starter metadata and verify the dual-host Docusaurus deployment contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config_path = ROOT / "docusaurus.config.js"
vercel_path = ROOT / "vercel.json"

if not config_path.is_file():
    print("ERROR: docusaurus.config.js is missing", file=sys.stderr)
    raise SystemExit(1)
if not vercel_path.is_file():
    print("ERROR: vercel.json is missing", file=sys.stderr)
    raise SystemExit(1)

text = config_path.read_text(encoding="utf-8")
forbidden = {
    "My Site": "starter site title or branding",
    "Dinosaurs are cool": "starter tagline",
    "your-docusaurus-site.example.com": "placeholder production URL",
    "organizationName: 'facebook'": "upstream organization",
    "projectName: 'docusaurus'": "upstream project name",
    "github.com/facebook/docusaurus": "upstream edit or repository links",
}

# We intentionally support two hosts from one source tree. The exact GitHub
# Pages origin/base path must remain present as fallbacks, while Vercel's
# runtime-provided hostname switches the site to root `/`.
required = {
    "https://matuteiglesias.github.io": "GitHub Pages fallback origin",
    "/atlas-pobreza-docs/": "GitHub Pages fallback base URL",
    "VERCEL_PROJECT_PRODUCTION_URL": "Vercel production hostname support",
    "VERCEL_URL": "Vercel preview hostname support",
    "SITE_URL": "explicit site URL override",
    "BASE_URL": "explicit base URL override",
    "organizationName: 'matuteiglesias'": "GitHub Pages owner",
    "projectName: 'atlas-pobreza-docs'": "GitHub Pages repository",
    "title: 'Poverty Ecosystem Engineering'": "engineering-site title",
}

failures = [
    f"{description}: {needle!r}"
    for needle, description in forbidden.items()
    if needle in text
]
missing = [
    f"{description}: {needle!r}"
    for needle, description in required.items()
    if needle not in text
]

try:
    vercel = json.loads(vercel_path.read_text(encoding="utf-8"))
except (json.JSONDecodeError, OSError) as exc:
    print(f"ERROR: invalid vercel.json: {exc}", file=sys.stderr)
    raise SystemExit(1) from exc

expected_vercel = {
    "buildCommand": "npm run build",
    "outputDirectory": "build",
    "installCommand": "npm ci",
}
for key, expected in expected_vercel.items():
    if vercel.get(key) != expected:
        missing.append(f"Vercel {key} must be {expected!r}")

if failures or missing:
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    for failure in missing:
        print(f"ERROR: missing {failure}", file=sys.stderr)
    raise SystemExit(1)

print("Deployment configuration is valid for GitHub Pages fallback and Vercel root hosting")
