---
title: Last documentation refresh
status: current
owners: [poverty-ecosystem-engineering]
---

# Last documentation refresh — 2026-09-28

## Scope

Performed a cross-ecosystem consolidation pass after the Sep-27 Poverty commissioning closure. The goal was to remove stale control state, freeze repository ownership, and ensure dated release/commissioning programs no longer masquerade as the current work queue.

## Decisions

- `docs/architecture/01-system-map.md` now contains the canonical human-readable division of labor.
- Scientific commissioning status is explicitly delegated to `indice-pobreza-UBA/science/commissioning/registry.json`.
- Public spatial coverage is province + department; EPH agglomerates remain a validation/benchmark geography.
- The logical code/contract envelope is 2022-Q1..2025-Q4, but actual predictive materialization is tracked separately through the capability census.
- Sep-25 generic poverty commissioning is closed/superseded by the terminal registry; closed science reruns only on explicit triggers.
- Completed Atlas delivery waves and merged producer/consumer PRs were removed from the active engineering backlog.
- Weekly automation is now documented as a dependency cascade and liveness/safety system, not a standing mandate to rerun closed experiments.

## Current active integration backlog

1. 2022–2025 capability census and authorized province/department backfill.
2. External benchmark package with direct-comparability and methodological-sensitivity classes kept separate.
3. Aggregate uncertainty decision; `not_supplied` remains authoritative.
4. Bounded CPV-2022 donor-vintage sensitivity.
5. Publication permission/indexability.
6. Monetary approval where a consumer requires approved mode.

## Historical material retained

The Sep-24 public Atlas controller and Sep-25 poverty-estimate commissioning controller remain in `release-control/` as provenance. Dated work packets, marathons and experiment notes remain inspectable, but are subordinate to producer contracts, the Poverty commissioning registry and the current-state pages.

## Repository hygiene actions

This refresh also initiates cleanup of producer-local issues/PRs whose original DoD is now satisfied or superseded. Current scientific/product questions are deliberately not closed merely to reduce issue count.

## Verification

Changes were pushed directly to `main` as requested. Repository CI/build status should be treated as the mechanical verification layer; this refresh does not manufacture new real-data evidence or scientific conclusions.
