---
title: "Local real-data runbook — department poverty × 8 quarters"
status: proposed
---

# Local real-data runbook

This lane exists because accepted real parent artifacts and their paths may live only on the workstation/local estate. It is intentionally separated from cloud development.

Run it only after D2 and D3a are merged or checked out at explicit reviewed SHAs.

## 0. Safety and workspace

Use a clean local integration workspace. Record:

```text
indice-pobreza-UBA SHA
samplerCensoARG SHA
encuestador-de-hogares SHA
canastas/basket producer SHA or release IDs
argentina-geography SHA
argentina-poverty-atlas SHA
```

Do not modify raw parents in place. Do not commit machine-specific absolute paths.

Use a local resolved-parent file ignored by Git, for example:

```text
.local/department-8q/resolved-parents.json
```

## 1. Resolve parents, do not guess them

For each of the eight periods, resolve and verify:

- target year (`2024` or `2025`);
- governed Census sample release;
- semantic/population-frame handoff required by the predictive Poverty producer;
- `research.household-welfare-predictive/v1` parent for that quarter;
- quarter basket slice;
- poverty method release.

Expected reuse:

```text
2024 Census target-year sample -> 2024-Q1,Q2,Q3,Q4
2025 Census target-year sample -> 2025-Q1,Q2,Q3,Q4
```

There should not be eight independent Census samples unless a producer contract explicitly requires that and this spec is amended.

For every parent, record:

```text
artifact/release ID
local path
manifest hash
payload checksum status
compatibility fields
household/person counts where applicable
```

If an accepted parent cannot be identified unambiguously, mark that period blocked. Do not pick the newest-looking directory.

## 2. Preflight identity

Before poverty computation, prove:

- household IDs in the frame are unique/non-empty;
- welfare household IDs are unique/non-empty;
- frame household set equals welfare household set;
- each household has exactly one `department_2010_id`;
- department IDs preserve five digits;
- represented department set equals the governed 525 inventory;
- department prefix gives a valid governed province;
- analysis-weight semantics match the accepted predictive path.

Persist the mismatch IDs if any check fails.

## 3. Dry-run one quarter

Use one quarter as a commissioning microscope before launching all eight. Prefer the quarter with the strongest existing province oracle (currently likely `2024-Q3`, subject to local evidence).

Run:

1. department release build;
2. detached release verifier;
3. cardinality checks;
4. department → province reconciliation;
5. national reconciliation.

Do not start the seven remaining runs until this chain is green.

## 4. Run all periods from one batch spec

Execute the governed batch runner against the **local resolved-parent map**.

Recommended operational policy:

- sequential or at most low bounded concurrency;
- one output directory per immutable period release;
- never overwrite a successful release in place;
- failed period does not invalidate already-verified sibling releases;
- final batch manifest is emitted only from verified children.

Expected release proof per period:

```text
525 departments
6,300 department facts
12 national facts
6,312 total facts
detached release verifier: pass
```

Expected eight-period proof:

```text
8 releases
50,400 department facts
96 national facts
50,496 total facts
```

## 5. Reconciliation

Use persisted `weighted_numerator` and `weighted_denominator` fields.

For each period × universe × concept × estimand:

```text
departments grouped by province prefix
  -> summed numerator
  -> summed denominator
  -> recomputed estimate
  -> compare with province oracle

all departments / provinces
  -> summed numerator
  -> summed denominator
  -> compare with ARG
```

If province releases are absent for a period, materialize a province oracle with the same generic producer and exact same parents. Label it as a reconciliation artifact according to producer conventions; do not ask the Atlas to create it.

Any tolerance must come from numeric representation policy, not from observed disagreement.

## 6. Persist reviewable evidence

Write a compact evidence directory such as:

```text
commissioning/department-8q-real/
  parent_resolution_report.json
  batch_manifest.json
  reconciliation_report.json
  run_summary.md
  checksums.sha256
```

The summary should include exact release IDs/hashes and any warnings. It must not include raw microdata rows.

Whether detached real Poverty releases themselves are committed/published is a release-control decision. Do not push them merely because the local run succeeded.

## 7. Feed real outputs into the Atlas

After D4/D5/D6 are available:

1. point Atlas ingest at the eight detached release roots;
2. verify each producer release independently;
3. build the presentation release-set projection;
4. verify exact 525-ID geometry join;
5. run browser/unit/integration tests locally;
6. if publication is authorized, use the existing governed publication path rather than inventing a local ad hoc deploy.

Required final evidence:

```text
8/8 periods
525/525 departments per period
0 dropped departments
0 extra departments
0 fuzzy joins
department -> province reconciliation PASS
department -> national reconciliation PASS
browser scientific aggregation FALSE
```

## 8. If real data exposes a code defect

Minimize the defect into a synthetic regression test in the owning producer repo, patch there, and resume from the failed gate.

Avoid local-only hotfix scripts. The real-data lane is a commissioning environment, not a shadow codebase.
