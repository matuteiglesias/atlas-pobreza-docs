---
title: Public Atlas release control — 2026-09-24
sidebar_position: 11
status: current
owners: [poverty-ecosystem-engineering]
---

# Public Atlas release control — 2026-09-24

This page is the human/agent runbook for the bounded release
`poverty-atlas-public-2026-09-24`.

The machine-readable state is
[`release-control/poverty-atlas-public-2026-09-24.yaml`](https://github.com/matuteiglesias/atlas-pobreza-docs/blob/main/release-control/poverty-atlas-public-2026-09-24.yaml).

## Objective

Ship the existing Argentina Poverty Atlas as a public research product that:

- consumes a previously accepted real `poverty-estimate-release/v2`;
- renders the already-published governed 24-province Mapbox transport;
- is deployed at a public production URL;
- is verified from outside the build environment;
- becomes indexable only after the external audit passes.

The release remains a **research estimate**, not official poverty statistics.

## Why this is a release DAG, not a development program

The scientific and software seams needed for publication already exist on canonical
producer/consumer branches:

- `indice-pobreza-UBA#27` merged the bounded predictive province/national
  release producer;
- `argentina-poverty-atlas#23` merged strict detached real-release ingest;
- `argentina-poverty-atlas#24` merged a verified published W3 Mapbox transport;
- `argentina-poverty-atlas#25` made production fail closed when no real release
  is available.

The remaining work is therefore boundary convergence:

```text
accepted real release                         production-provider path
        |                                              |
   R1 locate PASS                               R4 preflight BLOCKED
        |                                              |
        v                                              v
   R2 verify READY                            R4A establish Vercel target READY
        |                                              |
        v                                              v
   R3 vendor WAITING                          R4B browser token WAITING
        |                                              |
        +----------------------+-----------------------+
                               |
                               v
                         R6 production deploy
                               |
                               v
                      R5 deployed map proof
                               |
                               v
                         R7 external audit
                               |
                               v
                    R8 indexability cutover
                               |
                               v
                         R9 final proof
```

The initial parallel discovery has completed. R1 passed. R4 correctly stopped
because the authenticated Vercel scope contains no Poverty Atlas project; the
similarly named Economic Atlas is explicitly not a substitute. The next bounded
parallel pair is therefore **R2 + R4A**. R3 may start only after R2 passes, and
R4B may start only after R4A establishes the exact production target/origin.

## Executor classes

### Cloud AI agent — controller and independent verifier

The cloud agent owns the control bundle, evidence interpretation, scope discipline,
cross-repository status, and external verification. It does not invent local
filesystem state, Mapbox account state, Vercel state, or scientific release facts.

### Local Codex agent — authorized machine-local executor

Local Codex may inspect `/home/matias`, mounted data volumes, repository
worktrees, authenticated CLIs and local immutable artifacts. It executes bounded
machine-local work and returns structured evidence. It must not widen a failing
release gate into a redesign.

### Human operator — authority edge

Human action is reserved for credentials, account authorization, or a genuine
scientific ambiguity that cannot be resolved from governed evidence. A blocked
agent should request **one exact action**, not hand the whole problem back to the
operator.

## State model

Every node is exactly one of:

- **PASS** — acceptance conditions are met and evidence is recorded.
- **READY** — predecessors are satisfied and the launch prompt is complete.
- **WAITING** — a declared predecessor has not passed.
- **BLOCKED** — one exact external/human action is required.
- **FAIL** — a hard invariant failed.
- **CANCELLED** — the controller intentionally abandoned the node.

A plausible-looking artifact is not PASS. A green build is not deployment proof.
A published tileset is not browser-runtime proof.

## Attempt and scope budget

Each node gets at most two bounded implementation attempts. After a second failure,
the executor returns `BLOCKED` with:

1. the exact failing invariant;
2. the evidence collected;
3. the smallest required external/human action;
4. confirmation that no broader scope was taken.

The controller repairs the failing node only.

During this release, do **not** introduce a new poverty method, estimation period,
Census vintage, model-training run, weighting policy, frontend redesign,
architecture refactor, browser-side poverty computation, row-level public data,
or opportunistic replacement of an accepted parent.

## R0 — scope freeze: PASS

R0 inspected current producer/consumer evidence on 2026-09-24.

### Poverty producer

`indice-pobreza-UBA` main is anchored at
`a27a5a9486f1410d0472c5a1fda912e3daf55992` for this control decision.
PR #27 and the subsequent maintenance pulse are merged. The bounded producer can
write/verify the research-only provincial/national `poverty-estimate-release/v2`.

This does **not** prove which local detached release should be published. R1 owns
that identification.

### Atlas

`argentina-poverty-atlas` main is anchored at
`0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e`.

The following integration capabilities are canonical:

- strict detached real-release ingest;
- verified published province W3 transport;
- production failure if no real Poverty release is available.

The W3 manifest records:

- transport: `province-w3`;
- tileset: `matuteiglesias2.arg-prov-ign-b9fcf6f90f28`;
- source layer: `Argentina provinces IGN b9fcf6f90f28`;
- identity property: `geography_id`;
- 24 published province features;
- exact match to the governed 24-ID set;
- no poverty values embedded in geometry.

Still unproved at R0:

- the exact accepted local real release path;
- a dedicated active browser token;
- the canonical production deployment;
- the external deployed map/data join;
- indexability. The Atlas HTML still declares `noindex,follow`.

### Mapbox token interpretation

The 2026-09-24 probe using the upload credential received HTTP 404 while trying to
inventory public tokens. That means only that the upload credential did not
provide the attempted inventory result. It must **not** be interpreted as evidence
that no browser token exists.

Mapbox's current guidance is to use a separate browser token with public
`styles:read` and `fonts:read` scopes and to apply URL restrictions. Secret
upload scopes must never enter the browser.

The user has confirmed that the Mapbox credential named/noted
`argentina-poverty-atlas-publisher` is **not public**. R4 therefore treats it as a
known provider-side credential and categorically excludes it from
`VITE_MAPBOX_PUBLIC_TOKEN`. If its actual secret scopes include token
administration, secure local tooling may use it server-side to discover/create a
separate restricted `pk.*` token; otherwise the node should stop with one exact
human action rather than weakening the browser boundary.

## Evidence output contract for executors

Every executor should return a compact object equivalent to:

```yaml
node: R1_locate_release
outcome: PASS | FAIL | BLOCKED
attempt: 1
evidence:
  - description: ...
    ref: path | commit | command | provider-object
invariants_checked:
  - name: ...
    result: pass | fail
mutations:
  - none
next_node_unblocked: R2_verify_release | null
blocker:
  required_actor: human | cloud_controller | null
  exact_action: null
```

Do not paste secrets, large datasets, or row-level records into the report.

# Launch prompt — R1 locate accepted release

Use this prompt in a **local Codex agent** with access to the user's normal local
repositories and mounted data volumes.

> **Node:** `R1_locate_release`  
> **Release:** `poverty-atlas-public-2026-09-24`  
> **Mode:** read-only. Do not modify repositories, releases or data.
>
> Your mission is to locate the exact previously accepted real
> `poverty-estimate-release/v2` that is eligible to feed the public Argentina
> Poverty Atlas. Do not regenerate anything merely because a path is inconvenient.
>
> Start by reading the current local `indice-pobreza-UBA` main and the evidence
> around the merged predictive province/national producer (historically PR #27).
> Use producer manifests, checksums, run evidence, git history and acceptance
> records to identify the accepted release. Search authorized local storage
> including the user's normal repository/data roots and mounted volumes.
>
> A directory name is not evidence. A newer timestamp is not evidence. If multiple
> real candidates exist, compare their manifest identity/parents/checksums to the
> producer's accepted local run and either identify one uniquely or return
> `BLOCKED` with the candidate set and the exact missing discriminator.
>
> The candidate must identify itself as `poverty-estimate-release/v2`, carry
> `scientific_status=research_estimate`, preserve
> `uncertainty_status=not_supplied`, and correspond to the governed
> 24-province + national predictive release path. Synthetic/fixture releases are
> ineligible.
>
> Do not vendor the release yet. Do not recalculate poverty, retrain/rescore,
> refresh upstream parents, edit manifests, repair checksums, or choose a newer
> scientific candidate.
>
> On PASS, return only a compact evidence report containing:
>
> - exact absolute release directory;
> - release ID;
> - manifest SHA-256;
> - producer commit/run evidence tying this directory to the accepted run;
> - file inventory;
> - scientific and uncertainty status;
> - how competing candidates, if any, were ruled out;
> - commands/checks used, with no row-level data.
>
> Outcome must be exactly `PASS`, `FAIL`, or `BLOCKED`. Use at most two
> bounded attempts. After the second failed attempt, stop and report the smallest
> missing external fact rather than widening scope.

## R1 controller decision — PASS

The local executor returned PASS on 2026-09-24 with the following identity:

```yaml
release_id: poverty-estimate-release-2024-q3-province-predictive-v1
artifact_contract: poverty-estimate-release/v2
absolute_directory: /home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1
manifest_sha256: aad3e32e234e30693bf16866ca36f64ec4a0278aea7077a97ef7a49f12b65583
scientific_status: research_estimate
uncertainty_status: not_supplied
producer_commit: af05290e8d1e96e5ccf7ff4901f000df2e11675e
```

Acceptance evidence includes producer/run lineage, a passed run QA with 24
provinces + one national aggregate + 300 facts, the ecosystem battle-test record,
and successful checksum validation for all members listed by
`checksums.sha256`. Bounded metadata search found no competing real
`poverty-estimate-release/v2` candidate. Directory naming was explicitly not
used as authority.

R2 is therefore **READY**.

# Launch prompt — R2 verify the accepted release

Use this in a local Codex agent. This node is read-only with respect to the
accepted release and live Atlas worktree.

> **Node:** `R2_verify_release`  
> **Release program:** `poverty-atlas-public-2026-09-24`  
> **Mode:** read-only verification; temporary scratch files/builds are allowed.
>
> The controller has accepted R1. Verify this exact immutable candidate:
>
> ```text
> /home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1
> ```
>
> Expected embedded release ID:
> `poverty-estimate-release-2024-q3-province-predictive-v1`.
>
> Expected manifest SHA-256:
> `aad3e32e234e30693bf16866ca36f64ec4a0278aea7077a97ef7a49f12b65583`.
>
> Do not regenerate, repair, rewrite or replace this release.
>
> Verify the producer release itself first:
>
> 1. recompute the manifest SHA-256 and require the expected value;
> 2. run `sha256sum -c checksums.sha256` from the release directory and require
>    every listed member to pass;
> 3. require `release_manifest.json` to declare
>    `schema_version=poverty-estimate-release/v2`,
>    `artifact_type=poverty-estimate-release/v2`,
>    `scientific_status=research_estimate`, and
>    `uncertainty_status=not_supplied`;
> 4. require `run_qa.json` to be passed;
> 5. inspect only aggregate metadata/tables needed for this gate.
>
> Then prove the exact consumer contract:
>
> - exactly 300 facts;
> - exactly 24 unique `province_2010` geography IDs plus national
>   `geography_id=ARG`;
> - province IDs must be exact two-character governed IDs and must agree exactly
>   across facts, capabilities, and `geography_join_contract.json`;
> - join semantics must be `exact_governed_id` and numeric coercion must be
>   forbidden;
> - universes must be exactly the intended persons/households surface;
> - concepts must be poverty/indigence;
> - estimands must be FGT0/FGT1/FGT2;
> - fact keys must be unique;
> - estimates must be finite proportions in [0,1];
> - every fact must retain `uncertainty_status=not_supplied`;
> - the release must remain explicitly research-only / not official statistics.
>
> The publication allowlist is exactly:
>
> ```text
> poverty_estimates.csv
> capabilities.json
> geography_join_contract.json
> release_manifest.json
> run_qa.json
> LIMITATIONS.md
> checksums.sha256
> ```
>
> Extra producer evidence may exist in the source directory, but R3 must never
> vendor it. Confirm that this seven-file boundary contains aggregate release
> material only and does not include Census/EPH/person/household row-level
> microdata, predictive-welfare draws, or person-level predictions.
>
> Finally run the **actual Atlas strict ingest implementation** against this
> source in a temporary scratch checkout/copy of
> `matuteiglesias/argentina-poverty-atlas` anchored at
> `0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e`.
>
> Do not run the ingest in the live Atlas worktree because it writes generated
> projection files. Create a scratch checkout or archive, install dependencies if
> needed, then run the repository-native ingest with:
>
> ```bash
> POVERTY_RELEASE_REQUIRED=1 \
> POVERTY_RELEASE_DIR="/home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1" \
> node scripts/ingest-poverty-release.mjs
> ```
>
> Require the ingest to accept exactly this release and report 300 facts. Inspect
> the generated aggregate projection only enough to confirm release ID, 24
> province identities, ARG, and research/uncertainty semantics. Do not treat
> scratch generated output as a new authoritative release.
>
> Return:
>
> ```yaml
> node: R2_verify_release
> outcome: PASS | FAIL | BLOCKED
> attempt: 1
> source:
>   release_id: ...
>   manifest_sha256: ...
> producer_validation:
>   checksums: pass | fail
>   run_qa: pass | fail
> consumer_contract:
>   fact_count: ...
>   province_count: ...
>   national_id: ...
>   exact_geography_match: true | false
>   universes: [...]
>   concepts: [...]
>   estimands: [...]
>   duplicate_fact_keys: ...
>   invalid_estimates: ...
>   scientific_status: ...
>   uncertainty_status: ...
> public_boundary:
>   eligible_files: [...]
>   row_level_material_present: false | true
> atlas_strict_ingest:
>   result: pass | fail
> mutations:
>   - none_to_live_release_or_atlas_worktree
> next_node_unblocked: R3_vendor_release | null
> blocker: null | ...
> ```
>
> R2 is PASS only if every invariant is green. Do not weaken the Atlas validator,
> edit the source release, or substitute a nearby candidate.

# Launch prompt — R3 vendor and verify the release

Launch only after the controller accepts an R2 PASS.

> **Node:** `R3_vendor_release`  
> **Release program:** `poverty-atlas-public-2026-09-24`  
> **Mode:** bounded write in `argentina-poverty-atlas`; no deploy.
>
> Use the exact R2-approved source:
>
> ```text
> /home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1
> ```
>
> Start from the release-control Atlas base
> `0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e`, which contains merged PRs
> #23, #24 and #25. Do not silently base this release on an older checkout.
>
> First inspect the user's normal Atlas checkout. If it is dirty, detached,
> intentionally old, or based on a different commit, do not overwrite or clean
> away unrelated work. Create a dedicated clean git worktree from the anchored
> commit instead.
>
> Create a release branch, preferably:
> `release/poverty-atlas-public-2026-09-24`.
>
> Run the repository-native vendor operation exactly once:
>
> ```bash
> ./scripts/vendor-poverty-release.sh \
>   /home/matias/data/poverty-integration-20260911/ecosystem-battle-test/poverty-release/poverty-estimate-release-2024-q3-province-v1
> ```
>
> That script is expected to:
>
> - copy only the seven allowed producer files into `data/releases/active`;
> - invoke the strict ingest;
> - generate the public aggregate projection/catalog and
>   `src/data/activeRelease.ts`;
> - run `npm run verify`;
> - run `git diff --check`.
>
> After it succeeds, independently inspect the diff.
>
> Allowed change classes are:
>
> 1. the seven files under `data/releases/active/`;
> 2. generated aggregate browser projection under
>    `public/data/releases/<release_id>/` and `public/data/catalog.json`;
> 3. generated `src/data/activeRelease.ts`;
> 4. no other change unless mechanically required by a concrete failing
>    acceptance gate, in which case stop and report rather than widening scope.
>
> Explicitly reject:
>
> - row-level Census or EPH material;
> - person/household predictive-welfare source payloads;
> - secrets or `.env` material;
> - scientific/methodological changes;
> - Mapbox/Vercel configuration changes;
> - `noindex` removal;
> - UI redesign/refactor.
>
> Re-run or confirm:
>
> ```bash
> npm run verify
> VERCEL_ENV=production npm run build
> python3 scripts/check_no_mapbox_secrets.py
> git diff --check
> ```
>
> The production-mode build must select the vendored real release and must not
> fall back to fixture data. A missing browser Mapbox token is not a reason to
> modify source here; R4B owns that credential.
>
> Verify from generated/public aggregate files that the active release ID is
> exactly `poverty-estimate-release-2024-q3-province-predictive-v1`, with 300
> facts and the governed 24 province IDs + ARG.
>
> Commit the bounded result on the release branch. Do not merge it and do not
> deploy it.
>
> Return:
>
> ```yaml
> node: R3_vendor_release
> outcome: PASS | FAIL | BLOCKED
> attempt: 1
> atlas_base_commit: 0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e
> branch: ...
> commit: ...
> active_release_id: poverty-estimate-release-2024-q3-province-predictive-v1
> vendored_input_files: [...]
> generated_projection_files: [...]
> verification:
>   vendor_script: pass | fail
>   npm_verify: pass | fail
>   production_build: pass | fail
>   mapbox_secret_scan: pass | fail
>   diff_check: pass | fail
> safety:
>   row_level_data_added: false | true
>   secrets_added: false | true
>   science_changed: false | true
>   noindex_changed: false | true
> next_node_unblocked: R6_production_deploy | null
> blocker: null | ...
> ```
>
> PASS requires a clean bounded commit and all verification gates green.

## R4 controller decision — split required

The R4 preflight correctly returned **BLOCKED** because the authenticated Vercel
scope contains no canonical Poverty Atlas project. The only apparent Atlas
candidate, `atlas-economico-ar`, was inspected and is the unrelated Argentina
Economic Atlas.

The cloud controller therefore authorizes one new bounded node before token work:
R4A.

# Launch prompt — R4A establish the Vercel production target

> **Node:** `R4A_establish_production_target`  
> **Release program:** `poverty-atlas-public-2026-09-24`  
> **Mode:** bounded Vercel project configuration; no production deploy.
>
> The previous R4 attempt proved that no existing Argentina Poverty Atlas project
> is visible in the authenticated Vercel scope and that
> `atlas-economico-ar` is categorically the wrong product.
>
> You are now authorized to establish **one dedicated Vercel project for
> `matuteiglesias/argentina-poverty-atlas`**, preferably named
> `argentina-poverty-atlas`.
>
> Do not mutate any unrelated Vercel project.
>
> Use the authenticated Vercel CLI/API. Prefer provider/project APIs over
> guessing. The Vercel CLI's authenticated `vercel api` interface may be used
> for exact project/domain inspection without handling a separate token.
>
> Requirements:
>
> 1. re-check that a Poverty Atlas project has not appeared since the previous
>    inventory;
> 2. if still absent, create exactly one dedicated project;
> 3. link the local Atlas repository/worktree to that exact project;
> 4. record project name, project ID and owning scope;
> 5. keep local `.vercel/` metadata uncommitted/ignored;
> 6. do **not** run `vercel --prod`, `vercel deploy --prod`, or otherwise
>    publish the product in this node;
> 7. do not enable a Git auto-deploy path if doing so would immediately attempt
>    production from main before R3 has vendored the real release;
> 8. inspect project/domain metadata for the exact production origin.
>
> The canonical origin must come from Vercel's own returned project/domain state.
> Do not infer `https://argentina-poverty-atlas.vercel.app` merely from the
> project name.
>
> If Vercel reserves/reports an exact production domain before the first deploy,
> record it and PASS.
>
> If Vercel cannot expose or reserve an exact production origin until a first
> deployment exists, do not create a permissive guessed Mapbox restriction.
> Return `BLOCKED` with that exact provider limitation; the controller can then
> insert a bounded bootstrap-deployment edge if necessary.
>
> Return:
>
> ```yaml
> node: R4A_establish_production_target
> outcome: PASS | FAIL | BLOCKED
> attempt: 1
> vercel:
>   scope: ...
>   project_name: ...
>   project_id: ...
>   linked_repository: matuteiglesias/argentina-poverty-atlas
>   canonical_origin: ...
>   origin_source: provider_reported | unavailable_predeploy
> deployment_triggered: false
> git_autodeploy_enabled: false | true
> unrelated_projects_mutated: false
> local_vercel_metadata_committed: false
> next_node_unblocked: R4B_browser_token | null
> blocker: null | ...
> ```
>
> Do not touch Mapbox token configuration yet. R4B owns the browser credential
> after this node establishes the exact origin.

## R4B residue after R4A

Once R4A passes, resume browser-token work against the **exact provider-reported
origin**. The known `argentina-poverty-atlas-publisher` credential remains
server-side/non-browser. R4B either proves/creates a separate restricted public
`pk.*` token and stores it as production `VITE_MAPBOX_PUBLIC_TOKEN`, or asks
for one exact human Mapbox action.


# Launch prompt — R4 establish browser credential

Use this prompt in a **local Codex agent** with access to the Atlas checkout and
authenticated local tooling. It may request a narrow human credential action.

> **Node:** `R4_browser_token`  
> **Release:** `poverty-atlas-public-2026-09-24`  
> **Mode:** credential/configuration preflight. Never print token values.
>
> Your mission is to establish whether the production Atlas has a dedicated,
> browser-safe Mapbox credential and, if necessary, reduce the missing work to one
> exact human authorization/configuration step.
>
> Read current `argentina-poverty-atlas` main first. Treat these as fixed
> provider facts for this node unless direct canonical evidence contradicts them:
>
> - Mapbox account/username: `matuteiglesias2`;
> - transport: `province-w3`, status `published`;
> - tileset: `matuteiglesias2.arg-prov-ign-b9fcf6f90f28`;
> - style: `mapbox://styles/mapbox/standard`;
> - frontend environment variable: `VITE_MAPBOX_PUBLIC_TOKEN`;
> - known non-browser Mapbox credential: `argentina-poverty-atlas-publisher`.
>
> The user has confirmed that `argentina-poverty-atlas-publisher` is not a public
> token. Never place it in the Vite/browser environment. You may inspect its
> metadata/scopes through secure local tooling without printing the token and use
> it server-side for Tokens API work only if it actually has the necessary token
> administration scopes. Otherwise do not try to repurpose it.
>
> First identify the canonical production Vercel project/origin from local
> `.vercel/project.json`, authenticated Vercel CLI metadata, or other
> non-secret deployment configuration. Do not create an unrelated new project
> merely because discovery is inconvenient.
>
> Inspect whether `VITE_MAPBOX_PUBLIC_TOKEN` already exists in the production
> environment **without echoing or logging its value**. Never substitute
> `MAPBOX_UPLOAD_TOKEN`; the upload credential and browser credential are
> different roles.
>
> The earlier GitHub probe using the upload credential returned HTTP 404 while
> trying to enumerate public tokens. Do not interpret that as proof that a browser
> token does not exist.
>
> A production browser credential must be a dedicated Mapbox public `pk.*`
> token. Current Mapbox guidance requires public `styles:read` and
> `fonts:read` for web map display and recommends URL restrictions. No secret
> scope may be exposed to the browser. The production token must be restricted to
> the canonical production origin; do not weaken this by authorizing broad
> unrelated origins merely to make testing convenient.
>
> If a suitable token already exists, validate it without revealing it. Prefer
> behavioral checks using the intended production Referer and the actual Standard
> style / published W3 transport. Confirm URL restriction metadata through the
> account/API only if the available credential has authority to inspect it; do
> not infer absence from a Tokens API authorization failure.
>
> If no suitable token exists, or current local credentials cannot create one,
> return `BLOCKED` with exactly one human Mapbox action:
>
> 1. create a dedicated production public token;
> 2. enable only the public scopes needed for this Atlas (at minimum
>    `styles:read`, `fonts:read`);
> 3. restrict it to the canonical production origin;
> 4. store it as production `VITE_MAPBOX_PUBLIC_TOKEN` in Vercel, not git.
>
> If token creation is possible through already-authorized secure local tooling,
> you may perform it, but never write token bytes to source, shell history,
> reports or logs.
>
> PASS requires:
>
> - canonical production origin identified;
> - dedicated public `pk.*` token exists;
> - production URL restriction confirmed;
> - token stored as production `VITE_MAPBOX_PUBLIC_TOKEN`;
> - safe preflight can read the Mapbox Standard style and the published W3
>   province transport with the intended Referer;
> - report contains no credential value.
>
> Return a compact structured evidence report and outcome exactly `PASS`,
> `FAIL`, or `BLOCKED`. Use at most two bounded attempts.

## Why R5 follows R6

A provider publication proof is already available, but the gate we still need is
the **deployed browser runtime**. Therefore R5 deliberately depends on R6. We do
not create a permissive localhost token or pretend a provider-side TileJSON check
proves the production browser.

## R2–R9 acceptance summary

| Node | PASS means |
| --- | --- |
| R2 | the located release passes checksums, 300-fact schema, 24-province identity, status/uncertainty and public-safety gates |
| R3 | only the seven aggregate files are vendored and full Atlas verification passes |
| R6 | the exact intended real-release revision is live at the canonical production URL |
| R5 | the deployed browser initializes Mapbox and joins the governed 24 provinces to real release facts |
| R7 | an outside-world audit proves metrics, selectors, map, methodology, downloads and runtime health |
| R8 | `noindex` is removed only after R7 and the cutover revision is deployed |
| R9 | the final indexable revision passes the outside-world audit again |

## Terminal state

The release closes only as:

```text
VERIFIED_PUBLIC_RESEARCH_ATLAS
```

with R7, R8 and R9 all PASS.

A failure at any node leaves the last known-good upstream evidence intact. The
controller does not trade scientific or publication invariants for speed.


## R2 controller decision — PASS

R2 passed on the exact R1-selected release. The native Atlas validator at
`0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e` accepted the release and projected
exactly 300 facts in a temporary scratch checkout.

Confirmed:

```yaml
release_id: poverty-estimate-release-2024-q3-province-predictive-v1
manifest_sha256: aad3e32e234e30693bf16866ca36f64ec4a0278aea7077a97ef7a49f12b65583
facts: 300
provinces: 24
national_id: ARG
universes: [households, persons]
concepts: [indigence, poverty]
estimands: [fgt0, fgt1, fgt2]
duplicate_fact_keys: 0
invalid_estimates: 0
scientific_status: research_estimate
uncertainty_status: not_supplied
row_level_material_present: false
atlas_strict_ingest: pass
```

R3 is therefore **READY**. The R3 packet above remains authoritative.

Because the Vercel project now has pre-existing Git auto-deploy enabled, R3 must
continue to stop at a bounded branch/commit. It must not merge to `main` or
manually promote/deploy. A branch preview, if Vercel creates one automatically,
is incidental evidence only and must not be treated as R6 production deployment.

## R4A controller decision — PASS

R4A established the dedicated Poverty Atlas Vercel target:

```yaml
scope: matias-projects-5c20d82c
project_name: pobreza-argentina
project_id: prj_tH3rINrRly9Ufgnf3bwJBiJiQQxW
linked_repository: matuteiglesias/argentina-poverty-atlas
canonical_origin: https://pobreza-argentina.vercel.app
origin_source: provider_reported
deployment_triggered_by_R4A: false
git_autodeploy_enabled: true
```

The existing Git integration had already attempted a production build and failed
with the expected PR-#25 fail-closed error because no real release was present.
That failure is useful evidence that the production safeguard is working; R4A did
not create that deployment and did not weaken the safeguard.

R4B is therefore **READY**.

# Launch prompt — R4B establish the public browser token

Use this prompt in local Codex. A narrow human Mapbox action is allowed if the
agent cannot create the token with already-authorized account tooling.

> **Node:** `R4B_browser_token`  
> **Release program:** `poverty-atlas-public-2026-09-24`  
> **Mode:** credential configuration only. Never reveal token bytes.
>
> R4A has passed. The exact Vercel target is:
>
> ```text
> Vercel scope: matias-projects-5c20d82c
> project: pobreza-argentina
> project ID: prj_tH3rINrRly9Ufgnf3bwJBiJiQQxW
> canonical origin: https://pobreza-argentina.vercel.app
> repository: matuteiglesias/argentina-poverty-atlas
> ```
>
> The existing Mapbox credential named/noted
> `argentina-poverty-atlas-publisher` is known to be non-public and is
> categorically forbidden from browser use.
>
> Your mission is to establish a **separate dedicated public `pk.*` token** for
> this Atlas and store it as production `VITE_MAPBOX_PUBLIC_TOKEN` in the exact
> Vercel project above.
>
> First inspect the production environment-variable inventory for
> `pobreza-argentina` without printing any values.
>
> If `VITE_MAPBOX_PUBLIC_TOKEN` already exists, determine safely whether it is a
> suitable public token. Do not echo it. If safe metadata inspection is not
> available, use behavioral proof rather than printing or decoding the token.
>
> The browser token must:
>
> - be a public `pk.*` token;
> - be separate from `argentina-poverty-atlas-publisher`;
> - include the public scopes needed by this web Atlas, including
>   `styles:read` and `fonts:read`;
> - contain no secret/write scopes;
> - be URL-restricted to the exact production origin
>   `https://pobreza-argentina.vercel.app` (include only the minimum provider
>   syntax needed for that origin);
> - be stored in Vercel production as `VITE_MAPBOX_PUBLIC_TOKEN`;
> - never be committed to git, printed in terminal output, pasted into a report,
>   or written into a source file.
>
> The intended provider resources are:
>
> ```text
> Mapbox account: matuteiglesias2
> style: mapbox://styles/mapbox/standard
> tileset: matuteiglesias2.arg-prov-ign-b9fcf6f90f28
> source layer: Argentina provinces IGN b9fcf6f90f28
> ```
>
> If already-authorized secure local tooling can create/configure the public token
> without exposing it, you may do so.
>
> Do not assume that the non-public publisher token has token-administration
> rights. The earlier Tokens API inventory attempt returned HTTP 404 and does not
> establish those rights.
>
> If token creation/configuration requires the human Mapbox dashboard, stop with
> one exact action:
>
> ```text
> In Mapbox -> Access tokens:
> create a new public token for the Poverty Atlas,
> enable only the required public web scopes (including styles:read and fonts:read),
> restrict it to https://pobreza-argentina.vercel.app,
> then add that token to Vercel project pobreza-argentina as
> VITE_MAPBOX_PUBLIC_TOKEN for Production.
> ```
>
> Do not ask the human to republish the W3 tileset or rotate the publisher token.
>
> Once the Vercel env exists, verify environment metadata without revealing the
> value.
>
> If possible without leaking the token, perform provider preflight using the
> exact production-origin Referer semantics against:
>
> 1. the Mapbox Standard style;
> 2. the published W3 province transport.
>
> Do not run or promote a production Atlas deployment in this node. R6 owns that.
>
> Return:
>
> ```yaml
> node: R4B_browser_token
> outcome: PASS | FAIL | BLOCKED
> attempt: 1
>
> vercel:
>   project_name: pobreza-argentina
>   project_id: prj_tH3rINrRly9Ufgnf3bwJBiJiQQxW
>   canonical_origin: https://pobreza-argentina.vercel.app
>
> browser_credential:
>   exists: true | false
>   usage: pk | unknown | null
>   required_public_scopes_confirmed: true | false
>   secret_or_write_scopes_present: false | true | unknown
>   exact_origin_restriction_confirmed: true | false
>   production_env_configured: true | false
>
> preflight:
>   standard_style: pass | fail | not_run
>   w3_transport: pass | fail | not_run
>
> secret_hygiene:
>   token_printed: false
>   token_committed: false
>
> next_node_unblocked: R6_production_deploy | null
>
> blocker:
>   required_actor: human | cloud_controller | null
>   exact_action: ...
> ```
>
> PASS requires the dedicated browser credential to be configured in production
> with the exact-origin restriction. If provider preflight is impossible without a
> real deployed browser runtime, record that limitation; R5 remains the definitive
> deployed-browser proof. Do not weaken the token restriction merely to obtain an
> early preflight.

## Convergence after R3 + R4B

R6 becomes READY only when both independent edges are green:

```text
R3 PASS
  real release vendored + production-mode build verified
        \
         +--> R6 production deployment
        /
R4B PASS
  exact-origin browser token configured
```

The pre-existing failed Vercel production build is not R6. R6 must deploy the
exact R3 commit/revision with the R4B production environment and then record the
deployed revision and canonical URL.


## R4B controller decision — BLOCKED on one human credential action

The local executor confirmed that the dedicated Vercel project has no production
`VITE_MAPBOX_PUBLIC_TOKEN` and that no secure local Mapbox token-administration
credential/tooling is available. No token was printed or committed, and the
publisher credential was not modified.

The remaining action is intentionally manual and singular:

1. create a separate Mapbox **public** token;
2. include the public web-map scopes `styles:read` and `fonts:read`;
3. set the allowed URL to exactly `https://pobreza-argentina.vercel.app`;
4. store it in Vercel project `pobreza-argentina` as Production
   `VITE_MAPBOX_PUBLIC_TOKEN`.

Mapbox does not support wildcard characters in URL restrictions. A protocol +
domain restriction authorizes subpaths, so no `/*` suffix is needed or valid.

After the human action, rerun R4B as a verification-only second attempt. It must
not ask the human to paste the token into chat or source control.


## R3 attempt 1 — bounded fixture-test blocker

R3's data and production gates passed, but `npm run verify` exposed two tests whose
assumptions were still tied to the synthetic fixture era.

Inspection at the anchored Atlas commit confirmed:

- `src/lib/atlasState.test.ts` treats `demo-2026-S1` as a supported active
  period. That test should derive a supported period from `defaultAtlasState`
  (or the active-release period list) rather than pinning a fixture-only literal.
- `src/map/runtimeJoin.test.ts` tests a runtime join against `fixtureRelease`
  but constructs the state by calling `parseAtlasState()`, whose validity domain
  correctly follows `activeRelease`. The fixture test should instead construct
  an `AtlasState` using a period from `fixtureRelease.metadata.periods`.

This is classified as a test-boundary correction. R3 attempt 2 is authorized to
change only those failing test assertions/state construction. Product code,
release data, validators, fixture generation and scientific semantics remain
frozen.


## R3 controller decision — PASS

R3 attempt 2 passed with the authorized two-test boundary correction and no
product/validator/science changes.

```yaml
branch: release/poverty-atlas-public-2026-09-24
commit: 9f37e9cdd4c8252e7481f71872ef6d4bb955dea4
vendor_and_ingest: pass
npm_verify: pass
production_mode_build: pass
secret_scan: pass
diff_check: pass
active_release_id: poverty-estimate-release-2024-q3-province-predictive-v1
fact_count: 300
row_level_data_added: false
secrets_added: false
science_changed: false
noindex_changed: false
```

The only non-generated source-tree changes are the two authorized fixture-era
test corrections.

## R4B controller decision — PASS

R4B attempt 2 passed after the human configured the production browser token.

```yaml
production_env_configured: true
usage: pk
required_public_scopes_confirmed: metadata_unavailable
exact_origin_restriction_confirmed: metadata_unavailable
token_printed: false
token_committed: false
publisher_credential_modified: false
production_deployment_triggered: false
```

The account metadata for scopes/restriction was not locally inspectable, so the
final deployed-browser proof remains R5. The credential boundary itself is green.

## R6 launch decision

R6 is READY. GitHub inspection before launch showed:

```text
origin/main = 0cbf1ea9d22d9dadb03daf019bf821f2c3008e1e
remote release/poverty-atlas-public-2026-09-24 = absent
open Atlas PRs = none
```

Because R3 commit `9f37e9c...` descends from the frozen main commit, the
preferred publication path is a non-force fast-forward of `main` to that exact
commit. This preserves the R3 SHA so Vercel can deploy the exact intended
revision rather than a newly-created merge/squash commit.


## R6 attempt 1 — routing-only failure

R6 published the exact R3 commit and Vercel reported the exact revision READY.
The real release is live and the aggregate data endpoints are correct, but a
direct request to `/explorar` returns HTTP 404.

Controller inspection of the deployed source at
`9f37e9cdd4c8252e7481f71872ef6d4bb955dea4` found:

- the application is a static Vite SPA;
- `App.tsx` renders the explorer when `window.location.pathname === "/explorar"`;
- navigation uses `history.pushState`, so in-app navigation works without a
  server request;
- the Vite build emits one root `index.html`;
- the repository has no `vercel.json` or other hosting rewrite config.

Therefore the 404 is a hosting-route gap, not an application-route, release-data,
or Vercel-build failure. A direct browser request reaches Vercel before the SPA
JavaScript can run, and there is no static `/explorar` file.

R6 attempt 2 is authorized for one routing-only repair:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/explorar",
      "destination": "/"
    }
  ]
}
```

Use an exact rewrite rather than a catch-all so the already-valid
`/data/*` public release surface remains explicit and unaffected. Rewrites are
transparent: Vercel serves the destination while preserving the visitor-visible
URL, allowing the SPA to observe `window.location.pathname === "/explorar"`.

No frontend, data, science, Mapbox, credential or indexability change is
authorized by this repair.


## R6 controller decision — PASS

R6 attempt 2 passed after one exact Vercel rewrite for `/explorar`.

```yaml
repair_commit: fbfbf8773fe4339e3414bd364b882e6da1cf51e3
final_main_sha: fbfbf8773fe4339e3414bd364b882e6da1cf51e3
vercel_deployment_id: dpl_BhWrb92CEbrQfpjwGVrw5QVwpDsS
vercel_status: READY
deployed_git_sha: fbfbf8773fe4339e3414bd364b882e6da1cf51e3
active_release_id: poverty-estimate-release-2024-q3-province-predictive-v1
public_fact_count: 300
fixture_fallback_observed: false
root: pass
explorar: pass
explorar_shareable_query: pass
catalog: pass
facts: pass
noindex_still_present: true
```

R5 is READY. R5 is browser-runtime proof, not another deployment/build check.


## R5 controller decision — PASS after oracle correction

The executor reported FAIL only because it could not find the literal
`Mapa listo` in visible page text. Controller inspection of the deployed
`MapboxChoropleth` implementation shows that this string is stored in internal
ready-state metadata but is not rendered by the ready branch. It was therefore
an invalid browser-visible acceptance oracle.

All substantive R5 gates passed:

- fresh production explorer loaded;
- live Mapbox runtime reached ready state;
- zero Mapbox auth errors, fatal console errors or failed required requests;
- exact W3 tileset/source observed;
- `geography_id` identity preserved;
- governed 24/24 province set matched;
- initial persons/poverty/fgt0 state matched public release facts;
- changed households/indigence/fgt2 state matched public release facts;
- same map runtime remained ready;
- all 24 territorial provinces present;
- no missing-join-to-zero corruption or unexpected no-data;
- selection preserved exact two-character geography identity;
- public `pk` credential present with no `sk`, upload or publisher credential exposure;
- no mutations.

R5 is therefore PASS. R7 external product audit is READY.


## R7 controller decision — PASS

The outside-world audit passed on production commit
`fbfbf8773fe4339e3414bd364b882e6da1cf51e3`:

- root, explorer and shareable explorer route are public and preserve state;
- active release identity and research/non-official status are visible;
- national values match the active release;
- poverty/indigence, persons/households and FGT0/1/2 selectors all work;
- all 24 governed province IDs are represented and selected values match;
- uncertainty limitation, geography join, methodology/lineage, parents and
  comparability are reachable;
- aggregate facts/metadata/catalog are public and facts count is 300;
- no misleading fixture/demo or stale transport wording is rendered;
- zero fatal console errors, Mapbox auth errors or required request failures;
- no secret/admin Mapbox credential exposure;
- `noindex` remains present exactly as intended before cutover.

R8 indexability cutover is READY.
