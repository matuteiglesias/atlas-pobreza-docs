---
title: "Acceptance matrix — department poverty × 8 quarters"
status: proposed
---

# Acceptance matrix

This is the executable definition of done. Every row must have evidence before commissioning closes.

| Gate | Owner | Required proof |
|---|---|---|
| A0 — periods | coordinator | exact set is `2024-Q1 ... 2025-Q4`, or spec amended before real run |
| A1 — department inventory | D1/D2 | exactly 525 unique `^\d{5}$` IDs; no numeric coercion |
| A2 — province inventory | D2 | exactly 24 unique `^\d{2}$` IDs in canonical province mode |
| A3 — geography parent | D1 | 525 geometry features; exact department ID set; 1 province per department |
| A4 — scientific invariance | D2 | same poverty method, residual representation, weights, universes/concepts/estimands as province predictive path |
| A5 — one-period release | D2 | detached `poverty-estimate-release/v2` verifies for department fixture |
| A6 — per-period cardinality | D3c | 6,300 department + 12 national = 6,312 facts each |
| A7 — all-period cardinality | D3c | 50,400 department + 96 national = 50,496 facts total |
| A8 — release count | D3c | exactly 8 independently verified one-period department releases |
| A9 — department → province | D3a/D3c | persisted numerators and denominators reconcile for every period/universe/concept/estimand |
| A10 — province → national | D3a/D3c | persisted numerators and denominators reconcile to ARG |
| A11 — batch manifest | D3c | 8 period entries with release IDs, manifest hashes, counts and QA |
| A12 — Atlas ingest | D4 | province and department validation profiles; malformed sets fail closed |
| A13 — presentation projection | D4 | eight verified releases concatenate without scientific recomputation |
| A14 — department transport | D5 | published vector transport exposes exact governed 525 geography IDs |
| A15 — join purity | D5/I1 | zero fuzzy joins; zero dropped departments; zero extra geometry IDs |
| A16 — geometry payload | D1/D5 | no poverty values embedded |
| A17 — level selector | D6 | Province / Departamento mode switches one shared state model |
| A18 — period selector | D6 | exactly eight verified periods exposed in commissioned state |
| A19 — lookup UX | D6 | department selection supports province narrowing and keyboard operation |
| A20 — URL state | D6 | level/period/place/concept/universe/estimand round-trip through URL |
| A21 — incompatible state repair | D6 | changing geography level clears/repairs invalid place deterministically |
| A22 — trend | D6 | trend reads only verified release-set periods; no interpolation/manufacture |
| A23 — browser science boundary | D4/D6 | browser never recomputes poverty or aggregates departments |
| A24 — local privacy boundary | D3b/D3c | raw/private/heavy local parents are not added to Git history/cloud artifacts |
| A25 — real-data proof | I1 | eight real periods + exact geometry join validated end-to-end |
| A26 — regression | D2/D4/D6 | existing province path remains functional |
| A27 — closeout | I2 | durable docs updated and this bundle archived/deleted |

## Required arithmetic assertions

These values should appear in tests, but only in the bounded profile that declares the governed 525-ID inventory:

```text
facts_per_geography = 2 universes × 2 concepts × 3 estimands = 12

department_facts_per_period = 525 × 12 = 6,300
national_facts_per_period   = 12
total_facts_per_period      = 6,312

department_facts_8q = 6,300 × 8 = 50,400
national_facts_8q   = 12 × 8    = 96
total_facts_8q      = 50,496
```

Do not infer scientific completeness from cardinality alone.

## Negative tests that must exist somewhere in the chain

At minimum:

- one department ID loses a leading zero;
- duplicate department ID;
- one missing department;
- one extra department;
- household set mismatch between frame and welfare;
- geometry set mismatch;
- unsupported geography level;
- one period omitted from canonical release set;
- duplicate period;
- one release with incompatible capabilities;
- checksum mismatch;
- national ID not equal to `ARG`;
- uncertainty fields supplied while uncertainty status says absent;
- level change with stale incompatible `place`.

## Real-data evidence bundle

The local commissioning output should make review possible without reopening raw parents. Persist, at minimum:

```text
batch_manifest.json
reconciliation_report.json
parent_resolution_report.json
checksums.sha256
run_summary.md
```

The evidence should contain release IDs, hashes, row counts, exact-set checks and reconciliation diagnostics. It should not contain raw household/person records.
