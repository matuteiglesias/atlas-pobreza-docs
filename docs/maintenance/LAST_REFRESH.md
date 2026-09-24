---
title: Last documentation refresh
status: current
owners: [poverty-ecosystem-engineering]
---

# Last documentation refresh — 2026-09-24

## Scope

Performed a bounded integration-state refresh for the public Atlas release and
created the control bundle `poverty-atlas-public-2026-09-24`.

This refresh does not reopen the Sep-11 scientific architecture. It updates only
the integration/publication claims whose producer evidence changed and freezes the
release DAG needed to get the existing research result onto the public Atlas.

## Producer repositories inspected

- `indice-pobreza-UBA`
- `argentina-poverty-atlas`
- `atlas-pobreza-docs`

Exact inspected refs are recorded in `carry_state.yaml`.

## Major state transitions recorded

1. `indice-pobreza-UBA#27` is merged. The bounded predictive
   province/national `poverty-estimate-release/v2` producer is now canonical
   mainline capability rather than validated pending integration.
2. `argentina-poverty-atlas#23` is merged. Strict detached real Poverty v2
   ingest is canonical mainline behavior.
3. `argentina-poverty-atlas#24` is merged. The W3 Mapbox province transport is
   recorded as published and inspected at the provider/vector-tile boundary with
   an exact governed 24-`geography_id` match.
4. `argentina-poverty-atlas#25` is merged. Production builds fail closed rather
   than silently publishing the synthetic fixture when no real release is
   supplied.
5. The remaining public frontier is release convergence, not missing
   architecture: locate the accepted detached release, verify it, vendor only the
   seven aggregate public files, establish the dedicated browser credential,
   deploy, audit from outside, and only then remove `noindex`.

## Release-control bundle added

- machine state:
  `release-control/poverty-atlas-public-2026-09-24.yaml`;
- human/agent runbook:
  `docs/architecture/10-public-atlas-release-control.md`.

R0 is recorded `PASS`. R1 (locate accepted release) and R4 (browser credential)
are `READY` and may be launched in parallel. Every downstream node remains
`WAITING` until its declared predecessors pass.

## Mapbox credential clarification

The user identified `argentina-poverty-atlas-publisher` as an existing Mapbox
credential and confirmed that it is **not a public token**. It is therefore
explicitly classified as provider-side/non-browser and must never be assigned to
`VITE_MAPBOX_PUBLIC_TOKEN`.

R4 must prove or create a separate restricted public `pk.*` credential for the
canonical production origin. The publisher credential may participate only in
secure provider-side token administration if its actual scopes authorize that.

## Claims deliberately not promoted

- The research chain is **not** official poverty statistics.
- The exact accepted detached local Poverty release has not been re-identified
  from local manifest/checksum/run evidence in this refresh.
- A dedicated browser-safe Mapbox token has not yet been proven.
- A canonical live Vercel production deployment has not yet been proven.
- Provider-side W3 publication proof is not browser-runtime proof.
- The Atlas remains intentionally non-indexable until the external production
  audit passes.
- `uncertainty_status=not_supplied` remains the truthful aggregate state.
- No new scientific method, period, Census vintage, weighting policy or model run
  was authorized by this refresh.

## Documentation surfaces changed

- `SYSTEM.yaml`
- `docs/architecture/02-contracts-and-release-chain.md`
- `docs/architecture/04-current-state-and-migration.md`
- `docs/architecture/09-automation-and-refresh-loop.md`
- `docs/architecture/10-public-atlas-release-control.md`
- `release-control/poverty-atlas-public-2026-09-24.yaml`
- `docs/maintenance/carry_state.yaml`
- `docs/maintenance/LAST_REFRESH.md`

## Verification

Final verification for this branch is:

```bash
npm ci
npm run build
python scripts/verify_deployment_config.py
```

The PR CI result records repository mechanics. It does not prove a scientific
release, a Mapbox credential, or the public Atlas runtime.
