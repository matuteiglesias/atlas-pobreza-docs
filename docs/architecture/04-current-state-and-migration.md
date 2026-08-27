---
title: Current state and migration
sidebar_position: 5
status: current
owners: [poverty-ecosystem-engineering]
---

# Current state and migration

This page distinguishes the **architecture we are converging toward** from the parts that are already implemented on real or deterministic inputs. It is intentionally conservative: a clean boundary on paper does not make an upstream source or scientific inference valid.

## State matrix — 2026-08-26

| Component | Current state | What is already solid | What remains before consequential real use |
| --- | --- | --- | --- |
| `microdatos-EPH-INDEC` | current / offline-proven | EPH acquisition and raw-format conversion boundary; source provenance artifact | uncommon historical formats and exact future source vintages |
| `income-modeling-eph` | current / active | EPH preprocessing, leakage controls, modeling datasets, experiments and diagnostics | remove remaining Census-specific provisional concerns; resolve exact monetary lineage; clarify neutral analysis-frame boundary |
| `eph-censo-aligner` | proposed / fixture-proven | directional mapping machinery, loss reporting, deployment-feature vocabulary | approve a real EPH/Census vintage pair, wording/universe/category-loss review, real feature release |
| `samplerCensoARG` | current / fixture-implemented | deterministic sample identity, household membership, probability/weights, release packaging | exact authorized CPV source identity, exact geography binding; any later population calibration must be separately specified |
| `encuestador-de-hogares` | proposed active-bounded boundary; runtime pending | historical cascade recovered; target survey-to-Census inference boundary and deployment DAG documented in PR #4 | merge boundary, synthetic end-to-end proof, approved real feature plane, transport validation, exact welfare concept and monetary lineage |
| `IPC-Argentina` | maintenance / proposed authority expansion | price-product families, observed/derived/projected classification, release envelope | current official-source snapshots, reviewed methodology, approved monetary-conversion release; historical EPH monetary lineage remains unresolved |
| `canastasINDEC` | maintenance / partial | historical derived regional basket artifact and dependency history | methodological repair, exact source/IPC compatibility, governed poverty-line release |
| `indice-pobreza-UBA` | current / v2 fixture-proven | lean poverty method, adult-equivalence semantics, threshold/FGT boundaries, deterministic v2 release, Atlas consumer contract | exact real population frame, exact deployable welfare, governed poverty lines/binding, uncertainty inputs if intervals are to be published |
| `argentina-geography` | approved / active | exact source snapshots, stable native IDs, Geography Releases, factual relations and downstream handoffs | consumer-specific new releases only as needed |
| `argentina-poverty-atlas` | current / active-seed | public-product boundary, fixture-driven UI, exact-ID geography integration, runtime choropleth architecture | consume first real governed poverty release and finish product polish/operations |
| `atlas-pobreza-docs` | this change establishes target authority | Docusaurus surface and useful retrieved/reference material already exist | keep architecture synchronized with accepted cross-repo decisions; progressively classify/promote subordinate pages |

## Immediate architecture deltas

### 1. Make `income-modeling-eph` genuinely EPH-only

The repo should be free to pursue the best scientifically valid EPH models without Census feature constraints. Census-specific staged code that currently survives there is migration evidence for `encuestador-de-hogares`, not the final authority.

### 2. Revive `encuestador-de-hogares` around statistical transport

The historical project is no longer being revived as a monolithic preprocessing/training/automation application. Its modern purpose is narrower and stronger:

```text
approved EPH analysis frame
+
approved EPH/Census semantic feature plane
+
exact Census population/sample frame
+
approved monetary semantics
        -> staged transport model
        -> deployable household welfare
```

The first committed design packet lives in `encuestador-de-hogares` PR #4. Until merged and fixture-proven, treat this as target architecture.

### 3. Promote monetary semantics out of hidden preprocessing

`IPC-Argentina` should evolve from a historical composite-index producer toward the explicit owner of approved monetary-reference conversions used by research systems. It must still preserve the distinction between official source observations and analytical composites or projections.

### 4. Preserve the Poverty v2 thin boundary

Do not move Census scoring, deflation, semantic crosswalks, or geography processing into `indice-pobreza-UBA`. The fact that Poverty currently waits on upstream real releases is evidence that the boundary is working, not a reason to absorb those concerns.

### 5. Keep the public Atlas a consumer

`argentina-poverty-atlas` may select and present released facts, but it must not generate new scientific estimands to compensate for missing producer capability. Capabilities declared by the poverty release govern what the UI may expose.

## Suggested proof sequence

This is a dependency-aware sequence, not a commitment to immediate execution:

1. merge/review the `encuestador-de-hogares` inference-boundary design;
2. clean the remaining Census responsibility out of `income-modeling-eph` while preserving reusable staged-training evidence;
3. establish a deterministic synthetic end-to-end transport fixture across EPH, aligner, Census sample, monetary reference, and welfare release;
4. approve one real EPH/Census semantic feature plane;
5. approve exact monetary conversion lineage for the training target and released welfare;
6. produce one exact real Census frame/sample with governed geography identity;
7. run transport support/domain-shift and cascade diagnostics and promote one model only if evidence supports it;
8. emit one governed household-welfare release;
9. bind one governed poverty-line release and threshold-area mapping;
10. produce the first real `poverty-estimate-release@2` and let the public Atlas consume it without producer-code imports.

## Open scientific decisions

The architecture deliberately does not decide these by software convention:

- exact EPH and Census vintages for the first real transport experiment;
- the approved current deployment DAG after variable-level review;
- whether stage outputs should be hard classes, probabilities, draws, or another representation;
- the final terminal welfare concept and person-to-household aggregation rule;
- whether/how an old Census frame is calibrated to a later population target;
- acceptable evidence for transport under temporal/structural shift;
- the approved monetary reference and conversion method;
- the governed poverty-line source/method and area binding;
- how upstream predictive uncertainty, if defensible, is propagated to Poverty.

These are scientific decisions and should remain visible until evidence closes them.

## Status discipline

When this page is updated, do not rewrite history. Record a component as implemented only when the producer repository exposes evidence: a merged contract, deterministic proof, exact release identity, QA, or reviewed method. Architecture can lead implementation, but it cannot pretend implementation has already followed.
