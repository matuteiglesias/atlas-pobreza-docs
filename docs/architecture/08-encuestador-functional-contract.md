---
title: EncUESTADOR — transport functional contract
sidebar_position: 9
status: current-design
owners: [poverty-ecosystem-engineering]
---

# `encuestador-de-hogares`: transport functional contract

The revived encuestador is the scientific nucleus that relates EPH evidence to an exact Census-derived scoring population.

Its function is now deliberately narrower than the historical monolith:

> **Infer a declared target-period household welfare quantity for the exact households in one governed Census-derived sample, using target-period EPH evidence and an approved EPH/Census semantic information plane, while making temporal assumptions, transport error and lineage explicit.**

It owns statistical transport. It does not own the systems that manufacture the source evidence around it.

## Inputs

The target interface asks for five governed inputs.

```text
1. neutral EPH training evidence
2. approved EPH/Census semantic feature plane
3. exact Census sample + aligned scoring frame
4. exact monetary-reference/conversion release
5. transport study specification
```

The EPH input is observation evidence, not the `income-modeling-eph` flagship model or its current positive-income modeling dataset.

The Census input is an exact sample namespace from `samplerCensoARG`; inference may not resample or silently change it.

The semantic feature plane comes from `eph-censo-aligner`; the encuestador does not become authority over source-variable meaning merely because it fits a model.

The monetary parent comes from `IPC-Argentina`; the encuestador resolves the model target into final welfare but does not define the price index.

## Statistical operation

A transport study may compare three families:

```text
direct shared-information -> terminal welfare
hurdle / two-part welfare
staged dependency DAG
```

The direct model is a mandatory baseline. Historical RFC1→RFC4 complexity is retained only if it improves final-welfare evidence under honest out-of-fold training and transport diagnostics.

Every learned intermediate used downstream must be generated out-of-fold. Once exact EPH household identity exists, the approved fold policy must prevent members of the same household from leaking across folds.

## Semantic equivalence is not temporal equivalence

This distinction emerged from the historical quarterly inference code and materially changes the modern boundary.

A feature may be semantically shared between EPH and Census while its Census value is stale for a later welfare period.

The legacy notebook already responded to this problem by changing Census `CONDACT` counts toward quarter-specific unemployment before RFC1 scoring. That row mutation is not an approved modern method, but it is evidence that the original scientific idea included **target-period state updating**, not just static missing-variable imputation.

The modern encuestador therefore owns an orthogonal transport-time classification such as:

```text
donor_vintage_proxy
target_period_latent
deterministic_target_period_derived
target_period_anchor
time_stable_or_invariant
forbidden_temporal_input
```

`eph-censo-aligner` answers whether two concepts are comparable. The encuestador answers whether a donor-vintage Census value can legitimately participate in a target-period transport model and under what assumption.

Any aggregate target-period calibration is optional transport science. It must be versioned and diagnosed, must operate on a distinct inferred/latent state, and must never overwrite the meaning of the donor Census observation.

## Clocks

A real run must keep at least these clocks distinct:

```text
eph_training_period
census_frame_vintage
sampling_target_period
welfare_period
monetary_reference_period
```

For example, one annual target-year Census sample can be scored at multiple quarters. Reusing stable sampler IDs across quarters yields synthetic repeated snapshots, not observed longitudinal records.

## Outputs

The modern boundary has two canonical external products.

### Transport model release

```text
research.eph-census-transport-model@1
```

This is the scientific transport claim. It records exact parents, training population, fold/weighting policy, temporal-role assumptions, model/DAG, optional calibration anchors, OOF evidence, ablations, support/domain-shift diagnostics, monetary semantics and limitations.

### Household welfare release

```text
research.household-welfare@1
```

This is the downstream Poverty handoff.

Conceptually:

```text
sample_household_id
welfare_period
welfare_amount
currency
price_reference
welfare_concept
estimation_status
transport_model_release_id
```

The welfare amount is linear and household-level. Adult equivalence, poverty lines and FGT remain downstream.

Person-level stage outputs can remain restricted/internal audit evidence. Poverty should not need to understand classifiers, intermediate latent states or model-native log scales.

## Household welfare remains an open scientific choice

The historical system predicted person `P47T` and several monetary components. The obvious candidate is to sum predicted person total income over the exact Census household, but this is not approved merely by convention.

The transport study should be able to compare:

```text
person total-income prediction -> household sum
vs.
direct household total-income target
vs.
explicitly justified hybrid
```

The selected construction must account for every household member and carry missing/invalid prediction policy explicitly.

## Weight boundary

These quantities are different systems:

```text
EPH survey / expansion weight
!= Census selection probability
!= donor-frame inverse-probability quantity
!= Poverty analysis weight
```

The encuestador owns only how the EPH survey design is used for transport fitting, calibration and evaluation. It preserves sampler design lineage but does not reinterpret it as model-training or poverty weight.

## Repository-local authority

The producer-local contract is being formalized in `encuestador-de-hogares` PR #8:

- `contracts/functional_interface.yaml`;
- `docs/FUNCTIONAL_CONTRACT.md`;
- modern README front door;
- hardened `SYSTEM.yaml`.

The heavy follow-ups are intentionally issues rather than hidden inside the docs change:

- `encuestador-de-hogares#6` — training population, EPH survey design and household-aware OOF;
- `encuestador-de-hogares#7` — variable-level transport-time roles and target-period state calibration.

## Boundary summary

```text
income-modeling-eph
    asks: what predicts income inside EPH?

samplerCensoARG
    asks: which Census households/persons are represented?

encuestador-de-hogares
    asks: what target-period welfare can be inferred for those exact units from EPH evidence?

indice-pobreza-UBA
    asks: given household welfare + method + lines + frame semantics, what poverty estimand follows?
```

This is the intended mature decomposition of the original EPH↔Census idea.
