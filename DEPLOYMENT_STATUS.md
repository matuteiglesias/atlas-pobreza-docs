# Deployment status

**Audited:** 2026-08-04  
**Source branch:** `main`  
**Legacy publication branch:** `gh-pages`  
**Classification:** documentation draft; legacy build exists, but the current source is not deployment-ready.

## What is configured

The repository contains a Docusaurus application and can be tested locally with the commands documented in the README.

## What is not production-ready

`docusaurus.config.js` on `main` still contains starter values including:

- `My Site`;
- `Dinosaurs are cool`;
- `https://your-docusaurus-site.example.com`;
- `organizationName: facebook`;
- `projectName: docusaurus`;
- edit links to the upstream Docusaurus template.

The `gh-pages` branch contains an older build for the former `atlas-site` path. Its generated landing page still exposes tutorial copy and starter metadata. That branch is not evidence that the renamed repository and current source are deployed coherently.

External HTTP reachability was not independently verified during this audit.

## Verification

```bash
python scripts/verify_deployment_config.py
```

The command is expected to fail until placeholder production metadata is removed.

## Failure behavior

Until the repair packet is completed:

- do not call the public site current or production-ready;
- do not treat a successful local build as proof of deployment;
- do not publish new authoritative poverty results only through this surface;
- link directly to producing repositories for claims and data.
