---
title: Semantics, identities, and clocks
sidebar_position: 4
status: current
owners: [poverty-ecosystem-engineering]
---

# Semantics, identities, and clocks

The hardest failures in this ecosystem are rarely syntax errors. They are **semantic compression errors**: two different concepts are given the same field, clock, identifier, or status and later treated as interchangeable. This page records the cross-system distinctions that must remain explicit.

## Identity

Every release should declare the entity level and identifier namespace it expects.

Examples include:

- EPH household/person keys within an exact survey release;
- Census household/person IDs within an exact sample/frame release;
- `radio_2010_id`, department, and province identities tied to exact Geography Releases;
- household IDs preserved unchanged from Census sample through welfare inference into Poverty.

No downstream system may recreate identity from row order. No fuzzy or positional join is allowed in a scientific release.

## Geography identity vs threshold area

A geography ID answers **where/which governed geographic unit is this?** A poverty-threshold area answers **which basket/threshold regime applies to this unit?**

They may be related through a governed binding, but they are not the same object. `argentina-geography` owns geography identity; Poverty consumes a separate `threshold-area-binding` contract.

## EPH/Census feature classes

The deployment vocabulary is:

- `shared_observable` — defensibly observed on both source sides;
- `derived_shared` — constructible deterministically on both sides under an approved rule;
- `stage_target` — observed in EPH but absent from Census and therefore learned inside the transport graph;
- `unsupported` — not defensibly available for the current deployment design;
- `research_only` — valid for EPH science but forbidden as an external Census deployment feature.

This vocabulary belongs to semantic alignment. The statistical consequences of using the feature plane belong to the inference instrument.

## Deployment DAG

The historical `encuestador-de-hogares` cascade contained four broad waves. The modern abstraction is a dependency graph, not a fixed number of Random Forest stages.

For each learned node, the graph must declare:

```yaml
target: <semantic target>
depends_on: [<features or prior nodes>]
representation: hard_class | probabilities | continuous
estimator_family: <candidate family>
validation: <metrics and slices>
```

If a downstream node consumes an upstream learned node, training must use **out-of-fold predicted intermediates**, not the observed upstream labels. After model selection, stages may be refit on the full training frame for scoring.

This prevents a train/deployment mismatch in which downstream models learn from perfect labels that will not exist when the graph is applied to Census.

## Monetary semantics

A number such as `P47T = 100000` is incomplete without monetary reference.

The ecosystem distinguishes:

```text
source nominal amount
    -> approved monetary conversion
    -> declared reference amount
    -> optional statistical transform
    -> model prediction
    -> inverse/retransformation
    -> deployable welfare amount
```

A log target is a modeling representation, not a welfare concept. A poverty consumer must never need to infer whether it should apply `10 ** prediction`, which IPC vintage was used, or whether rounding/clipping occurred.

The historical EPH preparation normalized nine monetary variables to a January-2016 analytical reference through IPC-Argentina. That behavior is genealogy, not current monetary authority until an exact conversion release and lineage are approved.

## Separate clocks

At minimum, preserve these fields when relevant:

```yaml
training_period: <EPH period used to learn relationships>
frame_vintage: <Census vintage underlying donor units>
sampling_target_period: <period whose department person mass informs sampling, if any>
welfare_period: <period for which welfare is interpreted>
price_reference: <monetary reference period>
poverty_line_period: <period of threshold values>
geography_vintage: <exact geography release/vintage>
```

A valid example may legitimately have:

```yaml
frame_vintage: 2010
sampling_target_period: 2024
welfare_period: 2024-Q1
```

That does **not** make the units a 2024 Census. It means that Census-2010 donor households were sampled with department probabilities informed by a 2024 population-by-department source and then passed to a welfare inference targeting 2024-Q1.

## Target-year sampling semantics

The target-year department population adjustment belongs to `samplerCensoARG`, but two population quantities must stay separate:

```text
D[d]   = exact donor-frame person mass in department d
         measured from the exact Census donor frame

T[d,y] = exact target-year person population in department d
         supplied by one governed demographic release
```

The basic uncapped design is:

```text
selection_probability[d,y]
  = c * T[d,y] / D[d]
```

where `c` is a global sampling intensity.

The historical implementation used a single projection table's `population[d,y] / population[d,2010]` ratio. That is genealogy / a special approximation, not a requirement of the modern contract. The target demographic source does not need to supply the donor denominator; the donor frame is authoritative for its own person count.

The important unit distinction is:

```text
selection_unit = household
target_mass_unit = person
```

If household `h` has `n_h` donor persons and every household in department `d` is selected with probability `p[d,y]`, retaining all household members gives:

```text
E[selected_persons[d,y]]
  = p[d,y] * D[d]
  = c * T[d,y]
```

before probability bounds. Thus household cluster sampling preserves household integrity while targeting department-level **person mass in expectation**. It does not imply a target-year household-count distribution.

If `c*T[d,y]/D[d] > 1`, the requested intensity cannot be realized by the basic Bernoulli design. Any cap, certainty-stratum behavior or alternative must be named, observable in QA and reflected in the expected target-share diagnostics; silent clipping is not acceptable.

The information update is deliberately narrow: **department person mass changes; within-department joint distributions do not**. Age, education, employment, household size, housing, and other characteristics remain inherited from the Census donor frame unless another explicit scientific mechanism later updates them.

Equal household inclusion probability within each department also gives every donor person the same marginal inclusion probability within that department. For sufficiently large samples, donor-frame person/household characteristics should therefore remain statistically represented, while national marginals can shift mechanically because the department mixture changed. This is a sampling assumption to diagnose and disclose, not evidence of contemporaneous calibration on those dimensions.

## Demographic source authority

`samplerCensoARG` owns the use of `T[d,y]`, not the demographic estimate itself.

A target-year run must pin an exact population-by-department release and preserve its own source/method/vintage. Different target periods may legitimately use different approved demographic source families. The Census donor frame separately supplies `D[d]`.

Legacy committed population tables remain evidence until their provenance is exact. In particular, repository history shows that a later `proy_pop*` file replaced an older table in the historical sampler without the surrounding official-source comment being updated. A filename or current legacy code path is therefore not enough to promote demographic authority.

## Selection probability and analysis weights

Do not collapse these into one generic `weight` without lineage.

- **selection probability** — probability with which a donor household, and therefore each of its members, entered the sample;
- **design inverse-probability weight** — optional `1 / p` quantity for inference back toward the Census donor-frame design;
- **analysis weight** — weight, if any, authorized for the specific downstream estimand.

These can point in different directions. When department probabilities are intentionally changed to create a target-year person distribution, automatically applying `1 / p` downstream can undo that rebalancing.

For person-level target-year estimands, the selected person mass is already geographically rebalanced in expectation. Household-level estimands require separate care because target-year population-by-department values do not determine target-year household totals. The consumer may not infer the intended estimand from a historical `sample_weight` field.

## Welfare unit

The inference boundary must declare whether its terminal welfare concept is person-level or household-level and how any aggregation is performed. The preferred poverty handoff is household-level because the conversion from person predictions to household welfare is part of the inference model, not part of FGT mathematics.

Adult-equivalence or per-adult-equivalent treatment, when required by the poverty method, remains governed by the Poverty method contract rather than being hidden inside a model output.

## Evidence states

A successful pipeline run establishes software execution, not substantive validity. Preserve at least the distinction between:

```text
technical acceptance
source/semantic acceptance
model/transport validation
scientific release readiness
substantive result
public publication
```

Promotion between these states must be explicit.
