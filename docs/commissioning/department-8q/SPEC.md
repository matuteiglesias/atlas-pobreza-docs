---
title: "Spec — department poverty × 8 quarters"
status: proposed
owners: [poverty-ecosystem-engineering]
---

# Spec — department poverty × 8 quarters

## 1. Product contract

The commissioned system SHALL expose predictive poverty estimates for:

- geography levels: `province_2010` and `department_2010`;
- periods: `2024-Q1`, `2024-Q2`, `2024-Q3`, `2024-Q4`, `2025-Q1`, `2025-Q2`, `2025-Q3`, `2025-Q4`;
- universes: `households`, `persons`;
- concepts: `indigence`, `poverty`;
- estimands: `fgt0`, `fgt1`, `fgt2`;
- national companion geography: `national / ARG`.

The scientific release unit remains **one period × one declared geography level** under the existing detached `poverty-estimate-release/v2` family. Multi-period presentation is a consumer projection, not a new multi-period scientific estimator.

If a pre-existing governed batch manifest proves a different exact eight-period set, development MUST stop and this spec must be amended before real-data execution. Agents may not silently substitute periods.

## 2. Identity contract

### Department

```text
geography_level = department_2010
geography_id    = zero-preserving 5-digit CPV-2010 department/commune identifier
regex           = ^\d{5}$
expected set    = exact governed 525-ID commissioning inventory
```

### Province

```text
geography_level = province_2010
geography_id    = zero-preserving 2-digit jurisdiction identifier
regex           = ^\d{2}$
expected set    = exact governed 24-ID inventory
```

### National

```text
geography_level = national
geography_id    = ARG
```

For every department feature/fact:

```text
department_2010_id[:2] == province_2010_id
```

String identity is preserved end-to-end. Numeric geography coercion is forbidden.

## 3. Target flow

```text
samplerCensoARG
  yearly Census target samples (2024 / 2025)
          |
          | stable household identity + department identity
          v
encuestador-de-hogares
  quarter-specific welfare predictions
  geography-agnostic scientific model
          |
          v
indice-pobreza-UBA
  generic predictive geography producer
      | province_2010
      | department_2010
          |
          +--> eight immutable department releases
          |
          +--> province releases / reconciliation oracle
          v
argentina-poverty-atlas
  verifies detached releases
  + verifies governed geometry transport
  + builds presentation-only release set
          |
          v
browser
  level × period × geography × concept × universe × estimand
```

## 4. Producer requirements — `indice-pobreza-UBA`

### 4.1 Scope of refactor

Generalize the current real predictive producer represented by `scripts/build_predictive_province_release.py`. Do **not** use this task as permission to rewrite unrelated v1/legacy aggregation code.

A suitable end state is a producer equivalent to:

```text
scripts/build_predictive_geography_release.py
```

with explicit inputs for at least:

```text
--period
--geography-level
--geography-field
--expected-geographies
--welfare-release
--frame
--baskets
--method
--output
```

A compatibility wrapper for the existing province command MAY remain if it is thin and covered by regression tests.

### 4.2 Geography profiles

The producer MUST have a bounded profile registry rather than arbitrary user-supplied identity semantics:

```text
province_2010
  field: province_2010_id
  regex: ^\d{2}$
  exact inventory: governed 24 IDs

department_2010
  field: department_2010_id
  regex: ^\d{5}$
  exact inventory: governed 525 IDs
```

The implementation MAY parameterize fields/counts internally, but only versioned profiles may be accepted in production mode.

### 4.3 Scientific invariance

Changing geography changes only the declared `HouseholdDomain` / grouping identity. It MUST NOT change:

- poverty method;
- household poverty-line construction;
- residual distribution;
- predictive-welfare representation;
- unit analysis-weight policy;
- universes / concepts / estimands;
- detached release schema;
- national computation.

### 4.4 Fact cardinality

Per department release:

```text
525 departments
× 2 universes
× 2 concepts
× 3 estimands
= 6,300 department facts

+ 12 national facts
= 6,312 total release facts
```

Across eight quarters:

```text
50,400 department facts
+    96 national facts
= 50,496 total facts
```

Tests MUST preserve this distinction.

## 5. Batch requirements

Add one governed batch spec, not eight scripts. A recommended contract is:

```text
configs/releases/predictive-poverty-2024q1-2025q4.json
```

Each row SHALL identify:

- `period`;
- `target_year`;
- `census_sample_release` or resolvable parent reference;
- `semantic_plane_release` / frame parent where applicable;
- `predictive_welfare_release`;
- quarter basket slice;
- expected parent compatibility metadata.

The runner SHALL, per period:

1. verify parents before computation;
2. build exactly one department release;
3. verify the detached release;
4. reconcile department numerators/denominators to province;
5. reconcile province or department totals to national;
6. record release manifest hashes and QA evidence.

Its final coordination artifact is a batch manifest, not a replacement scientific release:

```text
artifact_type = department-poverty-batch-2024q1-2025q4/v1
period -> release_id
period -> release_manifest_sha256
period -> geography_count
period -> department_fact_count
period -> national_fact_count
period -> reconciliation status
```

Local absolute paths MUST NOT appear in a committed batch spec.

## 6. Reconciliation contract

For every period × universe × concept × estimand, use persisted scientific numerators and denominators, not estimates rounded through the UI.

For each province `p`:

```text
sum(N_department in p) == N_province
sum(D_department in p) == D_province
estimate_from_summed_components == province estimate
```

Then:

```text
sum(N_province) == N_ARG
sum(D_province) == D_ARG
```

Use the tightest exact/tolerance semantics supported by persisted numeric representation. The tolerance, if non-zero, MUST be explicit, justified once, and tested. It may not be chosen ad hoc per quarter.

If historical province releases are not available for all periods, the same generic producer MAY materialize province releases from the exact same parents as reconciliation oracles. The Atlas must never perform this aggregation.

## 7. Geography release — `argentina-geography`

The geography producer owns a deterministic, versioned department geometry release with:

- exactly 525 features;
- `department_2010_id`;
- `province_2010_id`;
- department display name;
- province display name;
- geometry;
- source/vintage metadata;
- CRS;
- checksums;
- coverage / topology QA appropriate to the repository.

Preferred identity derivation remains governed CPV-2010 identity. If the repository already contains an eligible 525-department release, reuse it rather than creating a duplicate product. If not, derive it in `argentina-geography`, not in the Atlas.

Acceptance:

```text
geometry ID set == governed Poverty department ID set
count == 525
duplicates == 0
missing == 0
each department maps to exactly one province
department_id[:2] == province_id
```

No poverty values may be embedded.

## 8. Atlas ingest and release-set projection

The Atlas SHALL keep verifying each detached Poverty release independently, then build a static presentation artifact equivalent to:

```text
schema_version   = atlas-poverty-release-set/v1
geography_level  = department_2010
periods          = 8
geographies      = 525
department_facts = 50,400
national_facts   = 96
facts_total      = 50,496
```

This projection may concatenate already-verified facts keyed by disjoint periods. It MUST NOT recompute poverty, aggregate departments, invent uncertainty or mutate producer facts.

Validation profiles:

```text
province_2010   -> ^\d{2}$ -> exact governed 24 IDs
department_2010 -> ^\d{5}$ -> exact governed 525 IDs
national        -> ARG
```

Existing hard-coded assumptions such as a single period, 24 geographies or province-only TypeScript literals must be replaced by declared profile/metadata semantics.

## 9. UI requirements

Refactor province-only concepts into geography-generic surfaces where practical:

```text
ProvinceMap     -> GeographyMap (or equivalent generic adapter)
ProvinceLookup  -> GeographyLookup
provinces       -> geographies
getProvince     -> getGeography
```

Required controls:

```text
Nivel:   Provincias | Departamentos
Periodo: 2024 T1 T2 T3 T4 | 2025 T1 T2 T3 T4
```

Department lookup MUST include a province filter or equivalently efficient narrowing; a raw flat 525-item interaction is not the target UX.

State must remain URL-addressable, equivalent to:

```text
?level=department_2010
&period=2025-Q2
&place=06028
&concept=poverty
&universe=persons
&estimand=fgt0
```

Changing level must deterministically repair/clear an incompatible selected place rather than leave stale cross-level identity in state.

Trend views may read the verified eight-period projection. They may not manufacture missing periods.

## 10. Geometry transport / Mapbox

Mirror the existing province geometry-transport pattern with a department transport. It MUST prove:

- parent geography release identity and checksum;
- exact expected 525-ID set;
- published feature count 525;
- `feature_id_property = geography_id`;
- source layer explicitly declared;
- geometry-only payload;
- no poverty values.

Publication credentials remain secret; browser credentials remain public/minimal/restricted as already governed by Atlas operations.

## 11. Failure behavior

All boundaries fail closed.

Examples:

- 524 or 526 department IDs → fail;
- ID `2001` where `02001` is required → fail;
- welfare household set differs from frame → fail;
- one period has a different capability cube → fail unless explicitly versioned;
- geometry set differs from estimate set → fail;
- checksum mismatch → fail;
- missing real parent → local run blocks that period; cloud agent does not substitute synthetic data and call it real;
- partial real release set → UI may expose it only under an explicitly partial/research configuration, never as the commissioned eight-quarter state.

## 12. Explicit non-goals

Out of scope for this bundle:

- new income-model training;
- changing P1-R feature design;
- new residual conditioning;
- uncertainty estimation not already supplied;
- Census 2022 geography migration;
- radio/fracción publication;
- official-statistics claims;
- nowcasting;
- backend spatial APIs;
- fuzzy/name-based identity resolution;
- general cleanup of all province-specific naming in unrelated pages;
- refactoring every legacy Poverty CLI;
- redesigning Atlas visual style beyond what is required for the new selectors and 525-geography usability.
