# Work packet — establish one truthful Atlas deployment

## Decision required

Choose one canonical production identity:

- repository: `atlas-pobreza-docs`;
- production URL and base path;
- deployment owner: GitHub Pages or another named platform;
- whether the existing `gh-pages` history is retained or replaced.

## Implementation scope

- replace all Docusaurus starter metadata;
- set the canonical URL, `baseUrl`, repository links and edit links;
- remove tutorial and blog content not owned by the Atlas;
- align locale and navigation with the actual documentation;
- build from a clean checkout;
- deploy from one declared branch or workflow;
- verify the final URL, assets, navigation and broken links;
- record the deployed commit SHA.

## Acceptance

```bash
python scripts/verify_deployment_config.py
yarn build
```

both pass, followed by an HTTP check of the chosen production URL and at least one internal route.

## Integration boundary

This repository publishes documentation. It must link to authoritative producer repositories for data, methods and generated indicators rather than copying undocumented outputs into the site.
