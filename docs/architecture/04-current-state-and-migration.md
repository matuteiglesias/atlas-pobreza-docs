---
title: Current state and migration
sidebar_position: 5
status: current
owners: [poverty-ecosystem-engineering]
---

# Current state and migration

**Current as of 2026-09-28.** This page is the cross-repository status index. For a concrete artifact, its producer manifest/contract wins. For scientific commissioning state, `indice-pobreza-UBA/science/commissioning/registry.json` wins.

## State matrix

| Component | Current state | What is solid | Remaining bounded work |
| --- | --- | --- | --- |
| `microdatos-EPH-INDEC` | current acquisition authority | governed quarter releases and batch envelope | ordinary source drift; canonical batch parser repair on default branch |
| `income-modeling-eph` | current EPH-only research authority | real-data-proven neutral `research.eph-analysis-frame@1`, strong identity/design fields, grouped splits, income-study boundary | approved monetary parent for studies that require it; legacy Census code remains historical/provisional evidence |
| `samplerCensoARG` | current Census frame/sample authority | vintage-neutral frame/sample v2, target-year household sampling, separated probability/weight semantics, 2022–2025 code envelope | real CPV-2022 sampler-side proof and later donor-vintage sensitivity |
| `eph-censo-aligner` | current semantic authority | policy-driven real EPH 2024-Q3 ↔ CPV-2010 semantic plane; pure semantic boundary | CPV-2022-specific semantic review when needed |
| `encuestador-de-hogares` | current EPH→Census welfare inference authority | household-safe OOF/transport machinery, predictive welfare handoff, material support caveats made explicit | trigger-driven transport research only; no standing expansion queue |
| `IPC-Argentina` | current analytical monetary-reference authority | immutable candidate conversion products and scheduled source maintenance | approval status remains distinct from candidate availability |
| `canastasINDEC` | current poverty-threshold input producer | governed basket candidate path and bounded quarter slicing | durable line/release evolution remains producer-local |
| `indice-pobreza-UBA` | current poverty measurement/release authority | v2 method/FGT/release contracts, province/department producers, capability permissions, closed Q3 commissioning registry | 2022–2025 materialization census; aggregate uncertainty remains not supplied |
| `argentina-geography` | current geography authority | governed province/department identities and geometry transport parents | source/provider updates and explicit future relations only |
| `argentina-poverty-atlas` | current terminal public consumer | strict Poverty v2 ingest, capability-gated presentation, commissioned province/department geometry/runtime | research_public/indexability remains an explicit publication decision |
| `atlas-pobreza-docs` | current ecosystem docs authority | ownership, handoffs, status, weekly operating model | keep status synchronized; do not recreate producer science here |

## Commissioning closure

The 2024-Q3 commissioning family is **closed for its declared questions**:

- Telescope A: `closed_pass` — observed EPH poverty truth.
- Telescope B: `closed_pass` — same-household observed → OOF point → predictive bridge.
- Telescope C: `diagnostic_only` — EPH→Census transport decomposition.
- D-1: `diagnostic_only` — source-separation/transport-risk evidence.
- L1/L2/L3: `closed_pass`.
- L4: `closed_negative` — true labor helps welfare prediction, but the commissioned transportable labor bridge does not recover that gain.

Closed questions rerun only when their explicit registry trigger fires. The former Q8 classifier, old Q4 labor reconstruction and `ajustar_empleo` are historical/superseded evidence. Generic raking/IPF, density-ratio weighting, L5, Telescope D and a broad joint-distribution program are not an implied queue.

## Temporal and geographic coverage

The governed software/contracts now support a logical envelope of **2022-Q1 through 2025-Q4** where required parents exist.

Already broad:

- Telescope A: 16-quarter observed EPH poverty evidence.
- L1: 16-quarter labor truth/official benchmark reproduction.
- target-year sampler: 2022–2025 contract support.
- Poverty batch/config plumbing: 16-quarter envelope.
- Atlas period handling: period-driven rather than year-specific.

Not yet implied by those statements: every 2022/23 predictive welfare parent, province release, department release and Atlas projection is materialized. The authoritative next operational artifact is the period-by-capability census defined by `indice-pobreza-UBA/docs/CODEX_BACKFILL_2022_2023_VERTICALS.md`.

Public spatial coverage is **province + department**. The commissioned identity gates cover 24 provinces and 525 departments. EPH agglomerates are a validation/benchmark surface and do not become a third administrative Atlas geography by default.

## Publication state

The old Sep-24 Atlas release-control program completed its runtime/public-product commissioning with a known low-zoom cartographic limitation. No further provider/Mapbox work is active without a concrete rendering failure.

Public presentation remains capability-gated. An estimate existing is not the same as its interpretation being authorized. Population counts, uncertainty intervals, rankings and significance claims remain unavailable unless an upstream Poverty release explicitly authorizes them. Indexability/research-public cutover is therefore a publication decision, not an architecture repair.

## Active cross-repository work

1. Build/refresh the exact 2022–2025 capability matrix from real manifests and materialize only scientifically authorized missing province/department releases.
2. Keep cross-repo docs synchronized with producer truth; stale delivery waves and merged integration PRs are not active backlog.
3. Maintain a first-class external benchmark package: direct INDEC/EPH comparability, clearly separated methodological sensitivities, and small-area literature comparisons.
4. Decide aggregate uncertainty only through a new governed representation; until then retain `uncertainty_status=not_supplied`.
5. Treat CPV-2022 as a bounded donor-vintage sensitivity program, not a rewrite of sampler/aligner architecture.

## Historical control material

`release-control/poverty-atlas-public-2026-09-24.yaml` and `release-control/poverty-estimate-commissioning-2026-09-25.yaml` are retained as execution provenance. They are **not current work queues**. Dated work packets, commissioning marathons and historical notebooks are likewise subordinate to producer contracts, the Poverty registry, this page and the active backlog.

## Status discipline

Precedence for current claims:

```text
exact producer release manifest / contract
        ↓
indice-pobreza-UBA/science/commissioning/registry.json
        ↓
this current-state page + 01-system-map.md
        ↓
producer README/SYSTEM boundary docs
        ↓
dated release-control files, work packets, experiment notes and historical snapshots
```
