---
title: System map
sidebar_position: 2
status: current
owners: [poverty-ecosystem-engineering]
---

# System map

The poverty ecosystem is organized as a chain of **source/reference authorities**, **scientific transformation instruments**, and **public consumers**. The repositories are intentionally not collapsed into one codebase: their separation corresponds to different scientific authorities.

## Target chain

```text
                         SOURCE / REFERENCE AUTHORITIES

 microdatos-EPH-INDEC       Argentina Geography       IPC-Argentina
        |                         |                         |
        |                         |                         |
        v                         |                         v
 income-modeling-eph              |                 monetary conversions
   EPH-only science               |                         |
        |                         |                         |
        +------------+            |                         |
                     |            |                         |
                     v            v                         |
                eph-censo-aligner                            |
                semantic feature plane                      |
                     |                                      |
 CPV-2010            |                                      |
 local source        |                                      |
     |                |                                      |
     v                |                                      |
 samplerCensoARG ----+                                      |
 population frame                                           |
     |                                                       |
     +----------------------+--------------------------------+
                            |
                            v
                  encuestador-de-hogares
                  EPH -> Census inference
                  transport model + welfare
                            |
                            v
                      indice-pobreza-UBA
                 method + lines + FGT estimates
                            |
                            v
                  poverty-estimate-release@2
                            |
                 +----------+-----------+
                 |                      |
                 v                      v
       argentina-poverty-atlas   engineering/docs surface
          public product          this repository
```

`canastasINDEC` participates beside IPC and Poverty as the current historical producer of derived regional basket artifacts. Its eventual contract is a governed poverty-line/threshold input, not a generic monetary-conversion service.

## Repository roles

| Repository | Engineering role | Owns | Explicitly does not own |
| --- | --- | --- | --- |
| `microdatos-EPH-INDEC` | EPH acquisition producer | source acquisition, raw-format conversion, source provenance | analytical merging, deflation, features, models |
| `income-modeling-eph` | EPH-only modeling instrument | EPH preprocessing, modeling datasets, target/features, leakage policy, model experiments and diagnostics | Census scoring, Census identity, poverty measurement |
| `eph-censo-aligner` | semantic alignment component | directional EPH/Census mappings, category losses, deployment-observability vocabulary | model validity, statistical transport, Census sampling |
| `samplerCensoARG` | Census sample/frame instrument | deterministic sample identity, person-household membership, inclusion probability, weights, sample QA | welfare inference, poverty method, geography authority |
| `encuestador-de-hogares` | survey-to-Census welfare inference | deployment DAG, staged transport learning, scoring, transport diagnostics, welfare handoff | EPH-only model science, semantic mapping, sample design, IPC, poverty |
| `IPC-Argentina` | price-reference / monetary semantics utility | versioned analytical price products and, target-state, governed monetary conversions | official IPC authority, basket semantics |
| `canastasINDEC` | poverty-threshold input producer | derived regional basket artifacts and their transformation history | official CBA/CBT authority, independent IPC truth |
| `indice-pobreza-UBA` | poverty measurement and estimation authority | poverty methodology, adult-equivalence semantics, household thresholds, classification, FGT estimands, poverty release | model training/scoring, source acquisition, geography, public rendering |
| `argentina-geography` | Argentina geography authority | exact source identity, native geography IDs, normalized Geography Releases and factual relations | poverty estimands, sampling, inference |
| `argentina-poverty-atlas` | public Atlas consumer | public information architecture, Mapbox presentation, navigation, lineage/methodology UX | new poverty estimands, model inference, geometry authority |
| `atlas-pobreza-docs` | ecosystem engineering documentation authority | cross-repo architecture, boundary map, contract registry, status and migration intent | producer implementation, scientific values, source truth |

## Important separation: EPH model science vs Census transport

Two valid modeling questions coexist:

1. **EPH-only science:** what model best explains or predicts income within EPH, using scientifically valid EPH features?
2. **EPH -> Census transport:** what can be inferred on a Census-derived frame when only a constrained, semantically aligned feature plane is observable?

A high-performing EPH model may be impossible to deploy on Census because its predictors do not exist there. That is not a failure; it is a different scientific question. `income-modeling-eph` owns the first. `encuestador-de-hogares` owns the second.

## Important separation: semantics vs statistical transport

`eph-censo-aligner` may establish that two variables are defensibly comparable, or that a Census variable can be deterministically derived. It does **not** establish that an EPH-trained conditional relationship transports to Census. Support, domain shift, staged error propagation, and transport-model validation belong to `encuestador-de-hogares`.

## Important separation: sampling vs projection vs inference

These are different operations:

```text
Census sampling
    !=
population calibration / projection
    !=
welfare inference
    !=
poverty estimation
```

A CPV-2010-derived frame remains a CPV-2010 frame even if weights or a welfare estimate target a later period. Each operation requires its own declared method and clock.
