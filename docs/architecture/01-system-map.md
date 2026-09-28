---
title: System map
sidebar_position: 2
status: current
owners: [poverty-ecosystem-engineering]
---

# System map

This page is the current cross-repository ownership map. Producer contracts remain authoritative for their own artifacts; scientific commissioning status is owned by `indice-pobreza-UBA/science/commissioning/registry.json`.

## Division of labor

| Question | Owner | Boundary |
| --- | --- | --- |
| Get/version EPH | `microdatos-EPH-INDEC` | acquisition, source custody, normalized quarter releases |
| Poverty CBA/CBT inputs | `canastasINDEC` | governed basket/threshold inputs; not poverty classification |
| Monetary reference/conversion | `IPC-Argentina` | analytical monetary references/conversions; not official IPC authority |
| Census donor frame + target-year sample | `samplerCensoARG` | donor-frame identity, household selection, membership and design metadata |
| EPH↔Census variable semantics | `eph-censo-aligner` | reviewed mappings/recodes and semantic planes; not transport validity |
| EPH→Census welfare inference | `encuestador-de-hogares` | transport study, Census scoring and governed household-welfare handoff |
| EPH-only income-model research | `income-modeling-eph` | neutral EPH frame, EPH study cohorts, model experiments/evidence |
| Poverty method, thresholds, FGT, releases | **`indice-pobreza-UBA`** | poverty/indigence method, estimation, release permissions and QA |
| Commissioning status | **`indice-pobreza-UBA/science/commissioning/registry.json`** | active/superseded/terminal scientific questions and rerun triggers |
| Geography IDs/geometries | `argentina-geography` | exact geography releases, IDs and relations |
| Public presentation | `argentina-poverty-atlas` | capability-gated web/Mapbox presentation; no browser-side poverty science |
| Cross-repo architecture/status | `atlas-pobreza-docs` | ownership, handoffs, current integration state and maintenance guidance |

## Current architecture

```text
microdatos-EPH-INDEC ───────┐
                            ├─> income-modeling-eph (EPH-only research)
                            │
samplerCensoARG ───────┐    │
                       ├─> eph-censo-aligner ─> encuestador-de-hogares
microdatos-EPH-INDEC ──┘                              │
IPC-Argentina ────────────────────────────────────────┤
                                                     v
canastasINDEC ───────────────────────────────> indice-pobreza-UBA
                                                     │
argentina-geography ─────────────────────────────────┤
                                                     v
                                           argentina-poverty-atlas
```

`income-modeling-eph` and `encuestador-de-hogares` answer different questions. A strong EPH-only model is evidence about the EPH information frontier; it is not automatic permission to score Census. Semantic alignment is likewise necessary but not sufficient for statistical transport.

## Current scientific state

- Telescope A is the observed EPH poverty truth surface and has governed evidence over 2022-Q1..2025-Q4.
- Telescope B is the within-EPH observed → OOF point → predictive bridge and is terminal for its declared scope.
- Telescope C and D-1 remain diagnostic transport evidence; they do not create Census outcome authority or production weights.
- L1-L4 are closed for the commissioned Q3 scope. The result is that observed labor contains welfare information, while the commissioned transportable labor reconstruction does not recover that gain.
- Generic raking/IPF, density-ratio weighting, L5, Telescope D and a broad joint-distribution programme are not active work.

## Current downstream edge

`indice-pobreza-UBA` and `argentina-poverty-atlas` now have their producer/consumer boundaries on default branches. The Atlas runtime and province/department geography transports have been commissioned. Remaining publication/indexability decisions are distinct from missing architecture and must follow upstream release capabilities.

## Coverage boundary

The code and contracts support a 2022-Q1..2025-Q4 logical envelope where governed parents exist. The public spatial target is **province + department**. Identity/transport gates are commissioned for 24 provinces and 525 departments. This does not assert that every predictive parent, Poverty release and Atlas projection has already been materialized for all 16 quarters; that state is tracked by the capability census/backfill workflow.

EPH agglomerates remain a validation/benchmark geography. They must not be confused with the public administrative province/department surface.

## Weight boundary

```text
EPH survey / expansion weight
!= Census selection_probability
!= donor-frame design_inverse_probability_weight
!= Poverty analysis semantics
```

No repository may silently promote one of these quantities into another role.
