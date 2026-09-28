---
title: Engineering backlog
sidebar_position: 7
status: active
owners: [poverty-ecosystem-engineering]
---

# Engineering backlog

This is the **small cross-repository backlog after the Sep-27 commissioning closure**. Producer-local implementation issues live in their own repositories. Historical delivery waves are not active just because their issue or runbook still exists.

## Active

### 1. 2022–2025 capability census and authorized backfill

**Primary owner:** `indice-pobreza-UBA` with producer-local execution in upstream repositories.

Create/refresh the exact period-by-capability matrix for 2022-Q1..2025-Q4 from real manifests. Materialize missing province and department releases only where current model/welfare/scoring contracts authorize them. A scientifically blocked cell remains visibly blocked; do not retrain or change science merely to fill the rectangle.

### 2. External benchmark package

**Primary owner:** `indice-pobreza-UBA/science/commissioning` as a diagnostic/observability consumer.

Maintain clearly separated benchmark classes:

- direct EPH/INDEC measurement comparability;
- methodological sensitivity/reference work;
- small-area/survey-to-Census literature comparisons.

Benchmarks are evidence, not calibration targets. Do not tune project estimates to match external headlines.

### 3. Aggregate uncertainty decision

**Owners:** `encuestador-de-hogares` + `indice-pobreza-UBA`.

The current predictive household distribution does not by itself justify aggregate confidence intervals. Keep `uncertainty_status=not_supplied` until a governed representation separates model/transport, sampling and threshold uncertainty.

### 4. CPV-2022 donor-vintage sensitivity

**Owners:** `samplerCensoARG` + `eph-censo-aligner` + `encuestador-de-hogares`.

Complete the bounded real CPV-2022 frame/sample and semantic review when needed, then compare donor-vintage sensitivity under the same target-period design. This is an experiment on a stable architecture, not a new parallel pipeline.

### 5. Publication permission/indexability

**Owners:** `indice-pobreza-UBA` for release capabilities; `argentina-poverty-atlas` for presentation.

Ordinary public statistical presentation/indexability requires an explicit upstream publication decision. Atlas must not infer permission from map readiness or from an estimate merely existing.

### 6. Monetary approval where a consumer requires approved mode

**Owner:** `IPC-Argentina`.

Candidate monetary products may remain healthy while an approved-mode gate is red. Consumers that require approved conversion must continue to fail closed rather than weakening producer semantics.

## Closed or superseded — do not carry as active backlog

- merge/normalize Poverty province producer PR #27 — merged;
- merge/normalize Atlas real-release ingest PR #23 — merged;
- Atlas W0/W3–W6 delivery waves — commissioned/superseded by current runtime and capability-gated product;
- Sep-25 generic poverty-estimate commissioning program — superseded by the terminal Poverty commissioning registry;
- old Q8 global source classifier — superseded by D-1;
- old Q4 labor reconstruction and `ajustar_empleo` — superseded by L1–L4;
- generic raking/IPF, density-ratio weighting, L5, Telescope D and a broad joint-distribution program — not authorized current work.

## Stable boundaries

Do not move responsibilities merely to remove repository count:

- EPH acquisition stays in `microdatos-EPH-INDEC`.
- EPH-only model research stays in `income-modeling-eph`.
- Census sample identity/design stays in `samplerCensoARG`.
- semantic EPH↔Census mapping stays in `eph-censo-aligner`.
- EPH→Census welfare inference stays in `encuestador-de-hogares`.
- poverty method/FGT/releases stay in `indice-pobreza-UBA`.
- geography stays in `argentina-geography`.
- public presentation stays in `argentina-poverty-atlas`.

Promote a new cross-repo item here only when a concrete missing capability or scientific question can be named, its owner is unambiguous, and completion will unlock a real consumer or remove a real ambiguity.
