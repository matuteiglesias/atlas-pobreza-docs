---
title: "Agent seeds — department poverty × 8 quarters"
status: proposed-working-reference
---

# Agent seeds

These are intentionally short. Each agent must read `README.md`, `SPEC.md`, `WORK_GRAPH.yaml` and `AGENT_PROTOCOL.md` before acting.

## D1 — argentina-geography

```text
Implement work packet D1 from atlas-pobreza-docs/docs/commissioning/department-8q.

Goal: produce or reuse a governed deterministic CPV-2010 department geometry release with the exact governed 525 zero-preserving five-digit IDs, province parent identity, names, geometry, checksums and QA. Keep geometry free of poverty values. Do not dissolve geography in the Atlas.

First inspect current argentina-geography products; reuse an eligible 525-department product if one already exists. Otherwise add the smallest producer-owned derivation and tests. Work on a dedicated branch/PR. Return the AGENT_PROTOCOL handoff block.
```

## D2 — indice-pobreza-UBA

```text
Implement D2 from the department-8q commissioning bundle.

Generalize the current real predictive province release producer into a bounded geography-generic predictive-v2 producer supporting province_2010 and department_2010 profiles. Preserve scientific method, residual representation, weights and detached poverty-estimate-release/v2 semantics. Add department golden tests and province regressions.

Do not broadly refactor legacy aggregation.py/old CLI unless a failing test proves it is on this path. Preserve zero-padded IDs. Dedicated PR; return the standard handoff block.
```

## D3a — indice-pobreza-UBA

```text
Implement D3a only: governed eight-period batch spec/runner mechanics, fixture execution, batch manifest and reconciliation engine tests. No real workstation paths, no real-data claims. Parent verification must happen before each child build. One-period detached releases remain the scientific unit.

Use 2024-Q1..2025-Q4 canonical fixture periods and assert the 6,300 + 12 per-period arithmetic for the 525 profile.
```

## D4 — argentina-poverty-atlas

```text
Implement D4 from the commissioning bundle.

Make Poverty release ingest geography-generic for province_2010 and department_2010, verify arrays/directories of independent one-period releases, and build a presentation-only atlas-poverty-release-set/v1 projection across eight periods. Preserve fail-closed exact joins and no browser scientific aggregation.

Use synthetic/golden releases; do not wait for real local parents. Preserve existing province ingest behavior.
```

## D5 — argentina-poverty-atlas

```text
Implement D5 after D1's geometry contract is available.

Mirror the existing province W3 geometry transport with a governed department transport. Verify the parent release/checksum, exact 525-ID inventory, geometry-only payload, source layer and feature_id_property=geography_id. Adapt the existing publication workflow rather than creating a second transport system.
```

## D6 — argentina-poverty-atlas

```text
Implement D6 after D4/D5 contracts are usable.

Refactor province-only UI/state into the minimum geography-generic surface required for Province/Departamento switching, eight-quarter selection, province-filtered department lookup, exact 5-digit place state, and trends over verified periods. Keep URL state shareable and repair stale place IDs when the level changes.

Do not redesign unrelated visual style and do not aggregate scientific facts in the browser.
```

## Local Codex — D3b/D3c/I1

```text
Execute LOCAL_REAL_DATA_RUNBOOK.md from the department-8q commissioning bundle.

Use the merged/reviewed D2/D3a code. Resolve accepted local parents for 2024-Q1..2025-Q4 without guessing directories; verify them; run one microscope quarter first; then materialize all eight department releases, reconciliation evidence and the batch manifest. Keep raw/private/heavy parents local.

After D4/D5/D6 are available, verify the Atlas against the eight real releases and exact 525 geometry IDs. If real data exposes a code defect, reduce it to a synthetic producer regression and patch through a normal PR.
```
