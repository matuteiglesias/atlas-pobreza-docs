---
title: Current state and migration
sidebar_position: 5
status: current
owners: [poverty-ecosystem-engineering]
---

# Current state and migration

This page distinguishes the **architecture we are converging toward** from the parts that are already implemented on real or deterministic inputs. It is intentionally conservative: a clean boundary on paper does not make an upstream source or scientific inference valid.

## State matrix — 2026-08-27

| Component | Current state | What is already solid | What remains before consequential real use |
| --- | --- | --- | --- |
| `microdatos-EPH-INDEC` | current / offline-proven | EPH acquisition and raw-format conversion boundary; source provenance artifact | uncommon historical formats and exact future source vintages |
| `income-modeling-eph` | current / active | EPH preprocessing characterization, leakage controls, modeling datasets, experiments and diagnostics | become strictly EPH-only; reconstruct one source-backed neutral analysis frame; resolve exact monetary lineage |
| `eph-censo-aligner` | proposed / fixture-proven | directional mapping machinery, loss reporting, deployment-feature vocabulary | approve a real EPH/Census vintage pair, wording/universe/category-loss review, real feature release |
| `samplerCensoARG` | current / fixture-implemented; target-year method documented | deterministic household sample identity, household membership, reproducible selection, release packaging; historical department-size sampling idea recovered | implement governed target-year population-by-department input, correct probability semantics, split overloaded weight fields, remove threshold-region semantics from intrinsic sample identity |
| `encuestador-de-hogares` | active-bounded design merged; runtime pending | PR #4 merged the survey-to-Census inference boundary and deployment DAG; historical cascade preserved as evidence | synthetic end-to-end proof, approved real feature plane, transport validation, exact welfare concept and monetary lineage; PR #5 retires stale automation |
| `IPC-Argentina` | maintenance / proposed authority expansion | price-product families, observed/derived/projected classification, release envelope | current official-source snapshots, reviewed methodology, approved monetary-conversion release; historical EPH monetary lineage remains unresolved |
| `canastasINDEC` | maintenance / partial | historical derived regional basket artifact and dependency history | methodological repair, exact source/IPC compatibility, governed poverty-line release |
| `indice-pobreza-UBA` | current / v2 fixture-proven | lean poverty method, adult-equivalence semantics, threshold/FGT boundaries, deterministic v2 release, Atlas consumer contract | exact real Census sample/frame semantics, exact deployable welfare, governed poverty lines/binding, uncertainty inputs if intervals are to be published |
| `argentina-geography` | approved / active | exact source snapshots, stable native IDs, Geography Releases, factual relations and downstream handoffs | consumer-specific new releases only as needed, including threshold-area binding tracked in #36 |
| `GeoCenso-Visualizer` | legacy capability under audit | substantial radio-level Census indicator tables and historical geography/presentation logic exist | decide whether indicator measurement is reproducible and worth reviving separately from geography/presentation |
| `argentina-poverty-atlas` | current / active product | public-product boundary, fixture-driven UI, exact-ID geography integration, runtime choropleth architecture | reconcile W3/system state, consume first real governed poverty release and finish product operations |
| `atlas-pobreza-docs` | current engineering authority | architecture-first Docusaurus surface, cross-repo backlog, CI and dual-host deployment configuration | keep architecture synchronized with producer evidence; complete external Vercel connection/verification |

## Immediate architecture deltas

### 1. Make `income-modeling-eph` genuinely EPH-only

The repo should be free to pursue the best scientifically valid EPH models without Census feature constraints. Census-specific staged code that currently survives there is migration evidence for `encuestador-de-hogares`, not the final authority.

The source-facing boundary should converge toward:

```text
versioned raw EPH quarters
        ↓
neutral EPH analysis frame
        ↓
modeling dataset / feature views
        ↓
experiments / model evidence
```

The neutral frame should not inherit target-derived ranks, model filters, log targets, synthetic replacement sampling, or implicit monetary conversion merely because historical annual files contained them.

### 2. Keep target-year population adjustment inside the sampler

The earlier provisional architecture treated department population adjustment as a possible downstream calibration concern. The recovered method and owner decision now sharpen that:

```text
CPV-2010 household donor frame
+
exact population-by-department for target year y
        ↓
department-specific household selection probability
        ↓
large synthetic target-year-composition sample
```

The primary unit is the household; all persons in selected households are retained. The target-year population source changes department mass only. Other dimensions remain donor-frame distributions and rely on sufficiently large random sampling for statistical balance.

No separate generic population-calibration product is currently required.

The implementation still needs repair before consequential use. In particular, the current release path overloads `sample_weight`, while target-year composition requires a clean distinction between selection probability, optional donor-frame inverse-probability weight, and the actual downstream analysis weight. Using `1 / p` mechanically can undo the intended geographic rebalancing.

### 3. Revive `encuestador-de-hogares` around statistical transport

The historical project is no longer being revived as a monolithic preprocessing/training/automation application. Its modern purpose is narrower and stronger:

```text
approved EPH analysis frame
+
approved EPH/Census semantic feature plane
+
exact Census household sample
+
approved monetary semantics
        -> staged transport model
        -> deployable household welfare
```

PR #4 is merged. Until a deterministic synthetic transport/welfare release passes and real parents are reviewed, runtime/scientific inference remains pending.

### 4. Promote monetary semantics out of hidden preprocessing

`IPC-Argentina` should evolve from a historical composite-index producer toward the explicit owner of approved monetary-reference conversions used by research systems. It must still preserve the distinction between official source observations and analytical composites or projections.

### 5. Preserve the Poverty v2 thin boundary

Do not move Census scoring, deflation, semantic crosswalks, geography processing, or target-year sampling into `indice-pobreza-UBA`. The fact that Poverty currently waits on upstream real releases is evidence that the boundary is working, not a reason to absorb those concerns.

### 6. Keep the public Atlas a consumer

`argentina-poverty-atlas` may select and present released facts, but it must not generate new scientific estimands to compensate for missing producer capability. Capabilities declared by the poverty release govern what the UI may expose.

## Suggested proof sequence

This is a dependency-aware sequence, not a commitment to immediate execution:

1. finish sampler contract hardening for target-year household sampling, including exact population-by-department parent and unambiguous weight semantics;
2. clean the remaining Census responsibility out of `income-modeling-eph` while preserving reusable staged-training evidence;
3. reconstruct one source-backed neutral EPH analysis frame from exact quarterly EPH parents;
4. establish a deterministic synthetic end-to-end transport fixture across EPH, aligner, Census sample, monetary reference, and welfare release;
5. approve one real EPH/Census semantic feature plane;
6. approve exact monetary conversion lineage for the training target and released welfare;
7. produce one exact real Census household sample under a declared sampling target period/design;
8. run transport support/domain-shift and cascade diagnostics and promote one model only if evidence supports it;
9. emit one governed household-welfare release;
10. bind one governed poverty-line release and threshold-area mapping;
11. produce the first real `poverty-estimate-release@2` and let the public Atlas consume it without producer-code imports.

## Open scientific decisions

The architecture deliberately does not decide these by software convention:

- exact EPH and Census vintages for the first real transport experiment;
- the approved current deployment DAG after variable-level review;
- whether stage outputs should be hard classes, probabilities, draws, or another representation;
- the final terminal welfare concept and person-to-household aggregation rule;
- exact population-by-department source/vintage for the first target-year Census sample;
- acceptable sample size / QA evidence for the working assumption of balance across non-department dimensions;
- authorized downstream analysis-weight semantics for target-year samples;
- acceptable evidence for transport under temporal/structural shift;
- the approved monetary reference and conversion method;
- the governed poverty-line source/method and area binding;
- how upstream predictive uncertainty, if defensible, is propagated to Poverty.

These are scientific decisions and should remain visible until evidence closes them.

## Status discipline

When this page is updated, do not rewrite history. Record a component as implemented only when the producer repository exposes evidence: a merged contract, deterministic proof, exact release identity, QA, or reviewed method. Architecture can lead implementation, but it cannot pretend implementation has already followed.
