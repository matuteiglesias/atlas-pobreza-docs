---
title: Contracts and release chain
sidebar_position: 3
status: current
owners: [poverty-ecosystem-engineering]
---

# Contracts and release chain

The ecosystem integrates through **versioned artifacts**, not through shared working directories or sibling runtime imports. Each producer owns the transformation into its exported semantic boundary; each consumer validates the contract before using the artifact.

## Contract envelope

Unless a producer defines a stricter format, a scientific release should expose the equivalent of:

```text
release/
├── manifest.json
├── data.parquet | data.csv
├── qa.json
├── LIMITATIONS.md
└── checksums.sha256
```

The manifest must be sufficient to recover:

- artifact type and schema version;
- exact producer revision/release identity;
- exact parent artifact identities;
- entity level and stable identifier namespace;
- temporal coverage and relevant reference periods;
- measure semantics and units;
- method/version identity;
- files and hashes;
- status and limitations.

The consumer must not infer any of these from filenames or directory location.

## Main artifact chain

### EPH source and analysis

`microdatos-EPH-INDEC` produces a versioned EPH source artifact:

```text
artifact:publicdata.eph-microdata@1
```

`income-modeling-eph` consumes that source and currently produces:

```text
artifact:research.eph-annual-preprocessed@1
artifact:research.eph-modeling-dataset@1
artifact:research.eph-income-model@1
```

The target architecture narrows the public meaning of the first artifact: it should be a model-neutral EPH analysis frame. Experiment-specific feature engineering, target transforms, split assignments, and model views remain downstream inside `income-modeling-eph`.

Current caution: the tracked annual inputs are characterized historical artifacts, not yet a source-reproducible modern analysis-frame producer. Their monetary reference and exact historical preprocessing lineage remain partly unresolved. The target contract must not be described as current source-backed production until those parents are reconstructed.

### Census household sample and optional target-year composition

`samplerCensoARG` produces:

```text
artifact:research.census-sample@1
```

The current and target architecture keep the **household sample** as the primary Census-derived handoff. A separate post-sampling population-calibration product is not required by the present poverty/inference design.

The sampler may operate in two scientifically distinct modes:

```text
A. donor-frame sample
   CPV-2010 -> deterministic household sample

B. target-year department-composition sample
   CPV-2010
   + exact population-by-department release for year y
   -> department-specific household selection probabilities
   -> synthetic sample whose department mix approximates y
```

In both modes, the selected records remain Census-2010 donor households/persons. Target-year population information changes **department mass only**; it does not independently update age, education, employment, household size, housing, or other within-department distributions.

A target-year sample release should make at least the following explicit:

```yaml
frame_vintage: 2010
sampling_target_period: <year/date or null>
population_by_department_parent: <exact release id or null>
selection_unit: household
selection_algorithm: <exact method id>
base_sampling_fraction: <value>
selection_probability_field: selection_probability
```

When a target-year population parent is used, the release should preserve source and target department populations and the exact relative-size/probability formula used.

#### Weight contract

Do not overload one generic `sample_weight` field.

The contract must distinguish:

```text
selection_probability
optional design_inverse_probability_weight
optional analysis_weight
```

This distinction is not cosmetic. If department probabilities are intentionally changed to produce a target-year geographic composition, applying `1 / selection_probability` mechanically as the downstream analysis weight would approximately undo that rebalancing and recover donor-frame composition instead.

The consumer therefore receives an explicit authorized analysis-weight semantic or intentionally consumes the realized synthetic-sample composition. No downstream system may infer the intended estimand from a generic weight column.

`contract:population-frame` remains useful as a **semantic adapter expected by Poverty**, but it need not be a separately produced calibration artifact. It may be satisfied directly from one exact governed Census sample release plus its declared design/analysis semantics.

### Semantic alignment

`eph-censo-aligner` currently names its release:

```text
artifact:research.eph-census-crosswalk@1
```

Despite the historical name, this is **not a geographic crosswalk**. It is a directional variable/semantic alignment release. It should declare, for each candidate deployment feature, one of:

```text
shared_observable
derived_shared
stage_target
unsupported
research_only
```

A real-vintage release must also preserve question wording, universe, direction, category losses, recode provenance, and reviewer status.

### Survey-to-Census inference

The revived `encuestador-de-hogares` boundary produces:

```text
artifact:research.eph-census-transport-model@1
artifact:research.household-welfare@1
```

The transport-model release owns the deployment DAG, stage estimators, out-of-fold training policy, support/domain-shift diagnostics, model evidence, and exact training/scoring parents.

The welfare release is deliberately simpler. Poverty should receive a resolved welfare concept rather than a model-native prediction column. At minimum it should make explicit:

```yaml
entity:
  level: household
  id_namespace: <exact census-sample namespace>

measure:
  concept: household_total_income
  amount_field: welfare_amount
  currency: ARS
  price_reference: <declared reference>

time:
  frame_vintage: <census vintage>
  sampling_target_period: <sample target period, if any>
  welfare_period: <target period>

lineage:
  census_sample_release: <exact id>
  transport_model_release: <exact id>
  monetary_conversion_release: <exact id>
```

If the scientific design retains person-level predictions, they are diagnostic/intermediate outputs unless a downstream contract explicitly consumes them.

### Monetary conversion

`IPC-Argentina` is the target owner of monetary-reference semantics. A future approved conversion artifact should look conceptually like:

```text
artifact:research.argentina-monetary-conversion@1
```

It must identify source reference, target reference, factor/method, parent price release, period classification (`observed`, `derived`, `interpolated`, `projected`, etc.), and review status.

Modeling and poverty code should consume the declared conversion result. They should not reproduce IPC logic or guess the price reference of an old annual file.

### Poverty lines and threshold binding

Poverty requires two concerns that must remain distinct from generic monetary conversion:

```text
contract:poverty-lines
contract:threshold-area-binding
```

A poverty-line release answers **what monetary threshold applies for a declared concept, area, and period**. A threshold-area binding answers **which threshold area applies to each population unit**. Neither is the same as geography identity itself.

Current evidence sharpens the target split:

- `canastasINDEC` has an approved candidate method around six source-native basket-region IDs (`gran_buenos_aires`, `pampeana`, `noroeste`, `noreste`, `cuyo`, `patagonia`) and exact official-source nominal CBA/CBT inputs. Its modern target is the governed **threshold value** release, not geographic membership. Legacy backfill/mean-imputation/repeated-tail outputs remain compatibility evidence only.
- `argentina-geography` is the natural candidate owner of the source-backed **territorial interpretation/binding** from an exact governed Census geography to those six region IDs. This should be a tabular interpretation/crosswalk release, not a dissolved six-region geometry unless a consumer later needs geometry. The first concrete work is tracked in `argentina-geography#36`.

This split matters especially in Buenos Aires: official INDEC regional nomenclature places CABA and specified Buenos Aires partidos in Gran Buenos Aires, while the remainder of Buenos Aires belongs to Pampeana. A province-only lookup is therefore insufficient.

The target release chain is consequently:

```text
exact Census geography release
        ↓
reviewed geography→threshold-area binding

exact CBA/CBT source snapshots
        +
(optional) exact monetary-conversion release
        ↓
governed poverty-lines release
```

Poverty consumes both artifacts and joins by stable IDs. The sampler does not own the six-region classification and the basket producer does not own Census geography.

### Poverty release

`indice-pobreza-UBA` v2 consumes:

```text
contract:population-frame
contract:deployable-household-welfare
artifact:research.poverty-method@1
contract:poverty-lines
contract:threshold-area-binding
```

and produces:

```text
artifact:poverty-estimate-release@2
```

For the current architecture, `contract:population-frame` should be understood as a semantic view over one exact `research.census-sample@1` release plus the authorized design/analysis semantics required by the estimand. It does not imply a separate post-sampling calibration producer.

The release contains governed poverty facts, capabilities, geography-join contract, QA, limitations, manifest, and checksums. It does not carry model runtime or geometry.

Current v2 code already enforces a strong in-memory semantic boundary: exact frame/welfare ID coverage, exact monetary-reference equality, exact threshold-area coverage, and no model/GIS/network/file-I/O logic inside the contract module. Producer topology should be updated only when real upstream adapters are accepted, not merely to follow proposed repository names.

### Geography and Atlas

`argentina-geography` produces governed Geography Releases:

```text
artifact:arggeo.geography-release@1
```

It can also produce separately governed relation/crosswalk/interpretation releases when a concrete consumer needs an Argentina-specific territorial mapping. Those interpretation products do not replace source-native geography identities.

`argentina-poverty-atlas` consumes an exact poverty estimate release plus an exact geography release and joins them by governed ID. It must not derive new scientific poverty estimates in the browser.

## Cross-repository integration rule

The preferred dependency is:

```text
consumer -> artifact contract -> immutable release
```

not:

```text
consumer -> sibling repository checkout -> internal Python function
```

Small duplicated validation code is acceptable when it prevents the estate from acquiring a premature shared-framework dependency. Extract common code only after repeated **semantics**, not merely repeated syntax, have been proven.
