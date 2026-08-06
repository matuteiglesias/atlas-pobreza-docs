# Deployment status

**Audited:** 2026-08-06
**Source branch:** `main`  
**Deployment:** GitHub Pages Actions workflow
**Canonical URL:** <https://matuteiglesias.github.io/atlas-pobreza-docs/>
**Classification:** deployment configuration repaired; publication occurs after the workflow succeeds on `main`.

## What is configured

The Docusaurus production URL, repository metadata, edit links, and asset base path all target the renamed `atlas-pobreza-docs` repository. The Pages workflow builds the current source and deploys its artifact whenever `main` is updated.

The former `/atlas-site/` deployment path is intentionally unsupported. GitHub Pages must be configured in repository settings with **Source: GitHub Actions** so that `.github/workflows/deploy-pages.yml` owns publication instead of the stale `gh-pages` build.

## Verification

```bash
python scripts/verify_deployment_config.py
```

The command checks both that starter metadata is absent and that the renamed repository's exact GitHub Pages values are present.

## Failure behavior

Do not treat a successful local build as proof of deployment. Confirm that the Pages workflow completed successfully and that the canonical URL serves the commit being released.
