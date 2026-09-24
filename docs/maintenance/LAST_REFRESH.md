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

## Release-control advancement — 2026-09-24 later pass

After the initial R0 bundle merged, the local executor returned:

- **R1 PASS** — the accepted detached real release was uniquely identified as
  `poverty-estimate-release-2024-q3-province-predictive-v1` at
  `/home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1`, with manifest SHA-256
  `aad3e32e234e30693bf16866ca36f64ec4a0278aea7077a97ef7a49f12b65583`.
- **R4 BLOCKED** — authenticated Vercel inventory contains no canonical Poverty
  Atlas project; `atlas-economico-ar` was explicitly verified as the unrelated
  Argentina Economic Atlas.

The controller therefore:

1. advanced R2 to **READY** and added a read-only verification packet that runs
   the actual Atlas strict ingest in scratch;
2. added the bounded R3 vendoring/build packet;
3. split the R4 residue into **R4A** (establish one dedicated Vercel project and
   exact provider-reported origin) followed by **R4B** (establish the separate
   restricted public Mapbox token against that exact origin).

No production deployment, token creation, indexability change or scientific
change is claimed by this advancement.


## Release-control advancement — R2 and R4A passed

The next executor results were accepted:

- **R2 PASS** — the exact accepted release passed producer checksums/QA and the
  native Atlas strict ingest at the anchored Atlas commit. The public contract is
  exactly 300 facts, 24 provinces + `ARG`, households/persons,
  poverty/indigence, FGT0/1/2, `research_estimate`,
  `uncertainty_status=not_supplied`, with no row-level material in the seven-file
  publication boundary.
- **R4A PASS** — the dedicated Vercel target is
  `pobreza-argentina` / `prj_tH3rINrRly9Ufgnf3bwJBiJiQQxW` in scope
  `matias-projects-5c20d82c`, with provider-reported canonical origin
  `https://pobreza-argentina.vercel.app`.

The project's pre-existing Git auto-deploy had already produced the expected
fail-closed production failure before a real release was vendored. This is not
treated as a release failure and was not changed by R4A.

The active parallel pair is now **R3 + R4B**.


## Release-control advancement — R4B blocked correctly

R4B attempt 1 stopped without weakening credential policy. The dedicated Vercel
project has no production `VITE_MAPBOX_PUBLIC_TOKEN`, and the local environment
has no safe Mapbox token-administration path. The publisher credential remains
server-side and unchanged.

One human action remains: create a dedicated public Mapbox token with
`styles:read` + `fonts:read`, restrict it to
`https://pobreza-argentina.vercel.app`, and store it in Vercel Production as
`VITE_MAPBOX_PUBLIC_TOKEN`. R4B attempt 2 then becomes verification-only.


## Release-control convergence — R3 + R4B passed

- **R3 PASS (attempt 2):** bounded Atlas release commit
  `9f37e9cdd4c8252e7481f71872ef6d4bb955dea4` on
  `release/poverty-atlas-public-2026-09-24`. Vendoring/strict ingest,
  `npm run verify`, production-mode build, secret scan and diff check all pass.
  No product code, validator, science, row-level publication or noindex change
  occurred beyond the two explicitly authorized fixture-era test corrections.
- **R4B PASS (attempt 2):** Production `VITE_MAPBOX_PUBLIC_TOKEN` is configured
  as a public `pk` token; no token bytes were printed or committed and the
  publisher credential was unchanged. Provider account metadata for scopes/URL
  restriction was unavailable locally, so deployed-browser proof remains R5.

R6 is READY. Cloud inspection immediately before launch found Atlas
`origin/main` still at the frozen base
`0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e`, no remote release branch and no
open Atlas PRs. Preferred publication is therefore a non-force fast-forward of
`main` to the exact R3 commit, preserving revision identity for Vercel.


## Release-control advancement — R6 passed

R6 attempt 2 passed on production commit
`fbfbf8773fe4339e3414bd364b882e6da1cf51e3` and Vercel deployment
`dpl_BhWrb92CEbrQfpjwGVrw5QVwpDsS`. The real release is active with 300 public
aggregate facts, root/explorer/shareable deep links and data endpoints pass, and
`noindex` remains intentionally closed.

R5 browser-runtime proof is now READY.
