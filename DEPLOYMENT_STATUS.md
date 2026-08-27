# Deployment status

**Audited:** 2026-08-27  
**Source branch:** `main` after the engineering-authority PR merges  
**Deployment targets:** Vercel static deployment + GitHub Pages fallback  
**GitHub Pages URL:** <https://matuteiglesias.github.io/atlas-pobreza-docs/>  
**Classification:** repository is configured to build the same Docusaurus source for either host; an actual production Vercel project must still be connected and verified.

## Preferred navigation deployment: Vercel

`vercel.json` declares the bounded static contract:

- install with `npm ci`;
- build with `npm run build`;
- publish `build/`.

`docusaurus.config.js` detects Vercel's `VERCEL_PROJECT_PRODUCTION_URL` / `VERCEL_URL` and uses `/` as the base path there. `SITE_URL` and `BASE_URL` remain explicit overrides if a custom domain or non-root deployment is required.

This means the repository can be imported into Vercel without forking its documentation or maintaining a second build configuration. The Vercel project connection itself is external deployment state and is not claimed by this repository until a deployment URL and successful build have been inspected.

## GitHub Pages fallback

Without Vercel environment variables, Docusaurus retains the GitHub Pages values:

- URL: `https://matuteiglesias.github.io`
- base URL: `/atlas-pobreza-docs/`
- repository: `matuteiglesias/atlas-pobreza-docs`

The Pages workflow can therefore remain as a fallback/publication channel. The former `/atlas-site/` path remains unsupported.

## Verification

Before promoting a deployment, run:

```bash
npm ci
npm run build
```

For GitHub Pages-specific configuration also run:

```bash
python scripts/verify_deployment_config.py
```

For a Vercel deployment, inspect the produced deployment and verify at minimum:

1. `/` loads the engineering front door;
2. architecture pages and sidebar navigation work on direct URLs;
3. static assets resolve from `/` rather than `/atlas-pobreza-docs/`;
4. no broken-link build failures are hidden;
5. the deployed commit matches the intended branch/revision.

## Failure behavior

A successful local build is necessary but not proof of public deployment. A configured Vercel project is also not proof that the current commit is live. The production URL and deployed revision must be inspected before this document records a deployment as verified.
