---
title: "Commissioning bundle — department poverty × 8 quarters"
status: cloud-implementation-complete-local-real-data-pending
owners: [poverty-ecosystem-engineering]
---

# Department poverty × 8 quarters — bounded development bundle

This directory is a **temporary commissioning surface** for spec-driven development across the Argentina poverty ecosystem. It is intentionally more operational than the permanent architecture docs. It should seed autonomous agents, coordinate cross-repository contracts, and then be archived once the feature set is commissioned and the durable architecture has been promoted to authoritative documentation.

Cloud implementation is now complete through D6; see `STATUS.md` for merged evidence and the remaining D3b/D3c/I1 real-data lane. This bundle is **not yet evidence that the eight-quarter real-data commissioning is complete**.

## Mission

Extend the already-working predictive poverty publication path from its current province-first, one-period shape to:

- exact CPV-2010 department identity;
- eight periods: `2024-Q1` through `2025-Q4`;
- one geography-generic predictive release producer;
- one governed 525-department geometry parent;
- eight immutable one-period Poverty releases;
- one verified Atlas presentation projection over those releases;
- Province / Departamento switching, exact joins, quarter selection and trends;
- real-data commissioning performed locally without pushing private/heavy parents into cloud execution.

## Start here

1. `STATUS.md` — current implemented / proven / pending commissioning state.\n2. `SPEC.md` — frozen product and contract requirements.
3. `WORK_GRAPH.yaml` — machine-readable DAG, ownership, lanes and gates.
4. `AGENT_PROTOCOL.md` — rules for autonomous agents.
5. `ACCEPTANCE_MATRIX.md` — executable definition of done.
6. `LOCAL_REAL_DATA_RUNBOOK.md` — the local Codex-only real-data lane.
7. `AGENT_SEEDS.md` — copy/paste seeds for per-repository agents.

## Baseline observed when this bundle was cut

These SHAs are **orientation anchors, not eternal pins**. Every implementation agent must refresh `main` before editing and record drift in its PR.

| Repository | Observed `main` |
|---|---|
| `matuteiglesias/atlas-pobreza-docs` | `2fef6cd5cbaa72be167595b2f566f67ccbd96128` |
| `matuteiglesias/indice-pobreza-UBA` | `5e594002642eaafd19d0378eb90bd5ff0be0b7ec` |
| `matuteiglesias/argentina-poverty-atlas` | `75c56678bb80646a2bb1eef3632074cff08e332d` |
| `matuteiglesias/argentina-geography` | `71ac7d5a08fe55775d7d84fd5f3a18608bb64d67` |
| `matuteiglesias/samplerCensoARG` | `b5810255db51aa5d33eb3368cbcd4f94194e48d0` |
| `matuteiglesias/encuestador-de-hogares` | `2b3f78ec387f78acc03168b443e4039c66ee0068` |

## Execution lanes

### Cloud-safe by default

Cloud agents may implement and test code that needs only repository contents, public source data, synthetic fixtures, deterministic golden artifacts, GitHub Actions and existing publication credentials:

- D1 — governed department geometry release in `argentina-geography`;
- D2 — geography-generic predictive release producer in `indice-pobreza-UBA`;
- D3a — batch-spec / runner mechanics against fixtures only;
- D4 — Atlas multi-release ingest / release-set projection;
- D5 — department geometry transport and exact-ID proof;
- D6 — geography-generic UI, lookup, state and trend surfaces;
- contract tests, fixture generation, CI, docs and static typing for all of the above.

### Local-only real-data lane

Local Codex owns any step that requires paths or artifacts not guaranteed to exist in GitHub/cloud workspaces:

- discovery and verification of the accepted 2024 and 2025 Census sample parents;
- local semantic-plane / population-frame handoffs;
- real predictive welfare artifacts;
- quarter-specific basket slices when not published as cloud-consumable detached parents;
- eight real department release builds;
- department → province and department → national reconciliation against real outputs;
- materialized real-data evidence that should not be uploaded as raw/private/heavy parents.

The local lane may consume cloud-merged code. It must not become a second implementation fork.

## Non-negotiable invariants

- No new poverty method, residual model or income model.
- No quarter-specific Census resampling: target-year samples are reused across the four quarters of their year.
- No geography feature added to P1-R merely to obtain departments.
- No separate department estimator or Atlas-side scientific aggregation.
- No geometry embedded in Poverty estimate releases.
- No poverty values embedded in geometry transport.
- No fuzzy geography joins.
- No numeric coercion of zero-preserving IDs.
- No copy/paste family of eight period scripts.
- No refactor of unrelated legacy aggregation code unless a failing acceptance test proves it is on the predictive-v2 path.
- No cloud upload of local-only Census / welfare / semantic-plane parents.

## Concurrency policy

Start D1 and D2 in parallel. D4 may begin against fixtures as soon as D2's proposed contract is stable. D5 depends on D1's geometry contract. D6 may scaffold generic types/state against fixtures but does not claim completion until D4 and D5 are integrated. D3b/D3c are local and wait for D2/D3a code to land.

Prefer small numbers of dependency-aware PRs over many speculative branches.

## Lifecycle

This bundle is complete when all gates in `ACCEPTANCE_MATRIX.md` are satisfied on real data and the public Atlas path is verified. At that point:

1. promote durable contracts and final state into `docs/architecture/`;
2. retain only a compact commissioning record if useful;
3. archive or delete this directory in a dedicated docs PR.

Do not let this temporary packet become a second permanent architecture authority.
