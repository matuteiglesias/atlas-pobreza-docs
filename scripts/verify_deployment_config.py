#!/usr/bin/env python3
"""Reject known Docusaurus starter metadata in production configuration."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = ROOT / "docusaurus.config.js"

if not config.is_file():
    print("ERROR: docusaurus.config.js is missing", file=sys.stderr)
    raise SystemExit(1)

text = config.read_text(encoding="utf-8")
forbidden = {
    "My Site": "starter site title or branding",
    "Dinosaurs are cool": "starter tagline",
    "your-docusaurus-site.example.com": "placeholder production URL",
    "organizationName: 'facebook'": "upstream organization",
    "projectName: 'docusaurus'": "upstream project name",
    "github.com/facebook/docusaurus": "upstream edit or repository links",
}

required = {
    "url: 'https://matuteiglesias.github.io'": "GitHub Pages origin",
    "baseUrl: '/atlas-pobreza-docs/'": "renamed repository base URL",
    "organizationName: 'matuteiglesias'": "GitHub Pages owner",
    "projectName: 'atlas-pobreza-docs'": "GitHub Pages repository",
}

failures = [
    f"{description}: {needle!r}"
    for needle, description in forbidden.items()
    if needle in text
]

if failures:
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    raise SystemExit(1)

missing = [
    f"{description}: {needle!r}"
    for needle, description in required.items()
    if needle not in text
]

if missing:
    for failure in missing:
        print(f"ERROR: missing {failure}", file=sys.stderr)
    raise SystemExit(1)

print("GitHub Pages deployment configuration is valid for atlas-pobreza-docs")
