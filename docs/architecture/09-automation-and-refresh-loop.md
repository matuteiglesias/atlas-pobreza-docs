---
title: Automation and refresh loop
sidebar_position: 10
status: current
owners: [poverty-ecosystem-engineering]
---

# Automation and refresh loop

Automation exists to detect changed parents, preserve liveness and surface bounded failures. It must not turn every closed scientific question into a recurring pipeline.

## Operating rule

```text
source/reference changed?
        ↓
producer emits or validates an immutable candidate
        ↓
consumer preflight checks compatibility
        ↓
candidate/result changes only if its governed parent or explicit rerun trigger changed
```

A green weekly job proves the scope stated by that workflow. It is not a recomputed official poverty statistic and it does not upgrade research/publication permissions.

## Weekly dependency cascade

### Monday — source/reference maturity

- `microdatos-EPH-INDEC`: bounded EPH release/source probe.
- `canastasINDEC`: basket source probe.
- `IPC-Argentina`: monetary/source candidate maintenance.

These jobs discover and validate upstream evidence. They do not force downstream recomputation when nothing material changed.

### Tuesday — reusable scientific parents

- `income-modeling-eph`: source/analysis-frame maturity and eligible EPH parents.
- `samplerCensoARG`: target-year sample contract/maturity.
- `eph-censo-aligner`: semantic-plane maturity after compatible sample/source parents exist.

### Wednesday — transport and Poverty

- `encuestador-de-hogares`: bounded real acceptance/transport maturity where declared parents are available.
- `indice-pobreza-UBA`: deterministic release/commissioning smoke and registry integrity.

Closed Telescope/D/L questions are not standing Wednesday jobs. They rerun only when their explicit `science/commissioning/registry.json` trigger fires.

### Thursday — cross-repo documentation safety pass

`atlas-pobreza-docs` checks build/configuration and refreshes current architecture only when a producer boundary, artifact contract, scientific conclusion, maturity state or downstream capability materially changed.

### Atlas — event-driven

`argentina-poverty-atlas` is a terminal consumer. A new map/public projection is triggered by an eligible governed Poverty release or a concrete presentation/runtime change, not by a calendar obligation.

## Current closed programs

The following are retained as provenance, not active automation DAGs:

- `poverty-atlas-public-2026-09-24` — commissioned with a known cartographic limitation;
- `poverty-estimate-commissioning-2026-09-25` — superseded by terminal statuses in the Poverty commissioning registry.

Do not resume their READY/WAITING node states as if they were today’s queue.

## Large local data boundary

Hosted CI should validate contracts, deterministic fixtures and bounded portable evidence. It must not pretend to reconstruct large local Census/EPH evidence that is intentionally outside hosted CI. Real-data reruns must preserve exact parent identities and leave a durable receipt/index when the result matters.

## Release discovery

Prefer:

```text
producer publishes immutable candidate
        ↓
consumer discovers/pins exact candidate
        ↓
compatibility + permission check
```

over sibling-repository imports or a central mutable release bus.

## Failure classes

Useful failure classes remain bounded, for example:

```text
source_unavailable_or_ambiguous
source_schema_changed
candidate_build_failed
semantic_review_incomplete
identity_or_join_gate_failed
monetary_approval_missing
transport_trigger_or_parent_changed
poverty_parent_missing_or_incompatible
aggregate_uncertainty_not_supplied
public_consumer_contract_drift
```

Do not weaken a scientific gate to make scheduled automation green.

## Weekly human output

The useful weekly summary is small:

1. what parent/evidence materially changed;
2. which bounded candidate/release became possible or invalid;
3. which human/scientific decision is actually required;
4. what stale work can be closed/superseded.

If none of those happened, no new research task is required.
