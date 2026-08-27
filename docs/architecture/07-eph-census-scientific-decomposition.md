---
title: EPH, Census sampling and transport science
sidebar_position: 8
status: current-design
owners: [poverty-ecosystem-engineering]
---

# EPH, Census sampling and transport science

This page records the current engineering interpretation of the scientific boundary between `income-modeling-eph`, `samplerCensoARG`, and `encuestador-de-hogares`.

The main lesson from repository archaeology is that **EPH income modeling and EPH→Census welfare transport are different scientific studies over a partially shared data substrate**. They should share a neutral EPH observation/analysis artifact, not a modeling dataset, feature contract, fitted model, or runtime import.

## The target decomposition

```text
exact EPH quarter releases
        |
        v
neutral EPH observation / analysis frame
        |
        +------------------------------+
        |                              |
        v                              v
EPH-only income study           semantic alignment
        |                              |
        v                              |
modeling dataset                       |
        |                              |
        v                              |
experiments / evidence                 |
                                       |
exact Census sample -------------------+
        |                              |
        +------------------------------+
                       |
                       v
             transport feature plane
                       |
                       v
              encuestador-de-hogares
         training population + deployment DAG
                       |
                       v
               household welfare
                       |
                       v
                   Poverty v2
```

The arrows do not imply sibling-repository imports. Cross-repository integration should happen through immutable artifacts with exact identity, manifests, QA, limitations and checksums.

## `income-modeling-eph` is logically more than one component

The repository can remain one GitHub repository for now, but its scientific surface is better understood as three internal components.

### A. EPH observation / analysis-frame preparation

This is the reusable data plane.

It should eventually reconstruct a source-backed frame from exact EPH household/person quarter releases while preserving:

- exact person and household identity;
- native EPH variable semantics;
- survey/design/expansion fields and their source definitions;
- source quarter/year and geography identity;
- deterministic reusable household-derived quantities where justified;
- optional monetary-reference views only through exact `IPC-Argentina` conversion lineage;
- manifests, QA and limitations.

It should not define a model-study cohort, income target, leakage policy, final feature view or train/test split.

The current `research.eph-annual-preprocessed@1` artifacts are historical evidence, not yet this neutral contract. They retain only `CODUSU` as identity, omit source-side `NRO_HOGAR` / `COMPONENTE` and EPH design fields such as `PONDERA` / `PONDIH`, and contain Census-shaped historical aliases plus target-derived fields.

A future artifact may be named something like `research.eph-analysis-frame@1`; the name remains provisional until one source-backed release proves the boundary.

### B. EPH income study

This component owns a particular scientific question.

The current feature contract defines approximately:

```text
INGRESO == 1
P47T > 0
PROP not missing
        |
        v
log10(P47T)
```

with explicit feature blocks, leakage exclusions, geography/time specifications and model families.

That is a legitimate EPH-only **conditional positive-income** study. It is not automatically the training population or welfare model required for Census transport.

This component can use observed EPH variables that are unavailable in Census. A strong EPH model is not required to be deployable on Census.

### C. Experiment / evidence / promotion machinery

The experiment runner, guards, split registry, diagnostics, run comparison, artifact collection and flagship freeze form a third logical component.

This machinery should operate against a declared study/modeling-dataset contract. It need not know how the source EPH frame was produced, and its scientific evidence should state exactly which split, weighting and target policy was used.

Keeping these components in one repository is currently cheaper than introducing new repositories. The boundary is conceptual and contract-first; physical extraction should happen only if independent consumers or maintenance pressure justify it.

## Native EPH semantics must be restored at the reusable boundary

The historical annual EPH artifacts inherited part of the old survey-to-Census preparation vocabulary. For example, EPH variables such as `CH04`, `CH06`, `IV1`, `IV3`, `II7`, etc. were materialized under Census-facing names such as `P02`, `P03`, `V01`, `H05`, `PROP`.

That was useful when one monolithic system tried to make EPH resemble Census before inference. It is not the correct neutral boundary for a strictly EPH-only scientific workspace.

The reusable EPH frame should therefore retain native EPH semantics (or explicitly governed EPH-side canonical concepts). `eph-censo-aligner` owns the later semantic mapping into a cross-source transport namespace.

This gives a cleaner relationship:

```text
native EPH frame -------------------+
                                    |
                                    v
                             semantic aligner
                                    |
                                    v
                        canonical transport concepts
                                    ^
                                    |
native Census sample ---------------+
```

The transport system no longer requires the EPH source artifact itself to speak Census vocabulary.

## EPH survey design is not Census sampling design

The upstream EPH source contains survey/expansion fields such as `PONDERA`, `PONDIH` and related income-weight fields. The current historical annual artifacts do not preserve them.

A modern neutral EPH frame should preserve source design fields. Consumers then make explicit decisions about whether a particular field enters:

- model fitting;
- probability calibration;
- evaluation metrics;
- descriptive estimates;
- subgroup diagnostics;
- or not at all.

That decision belongs to the scientific study, not to generic preprocessing.

The following quantities are separate concepts and must never share one generic `weight` semantic:

```text
EPH survey / expansion weight
        !=
Census sampler selection probability
        !=
donor-frame inverse-probability audit weight
        !=
poverty analysis weight
```

`samplerCensoARG` owns Census sample construction. `encuestador-de-hogares` owns how the EPH survey design enters transport training/evaluation. Poverty owns the final estimand and therefore the analysis-weight interpretation it accepts.

## Split policy is scientific state

The current EPH experiment split implementation randomizes individual rows. Current feature engineering also creates household-derived age composition and maximum education features.

Once exact household/person identity is restored, validation must be able to group by household so household members do not cross folds or train/test boundaries.

This matters twice:

1. for ordinary EPH income-model evidence;
2. for the staged transport model, where upstream learned features are generated out-of-fold.

The transport invariant therefore becomes stronger than merely “use OOF predictions”:

> intermediate predictions must be out-of-fold under an explicitly declared grouping/split policy that prevents household leakage for the approved training design.

Random-person splits can remain sensitivity/reference experiments, but they should not be the only unnamed canonical validation regime.

## `encuestador-de-hogares` owns a different training population

The transport system should consume the neutral EPH frame, not `research.eph-modeling-dataset@1`.

It owns its own:

- eligible EPH training population;
- stage target universes;
- hurdle/two-part structure for income/welfare;
- weighting/calibration policy;
- household-aware OOF policy;
- transport DAG;
- support/domain-shift diagnostics;
- scoring of the exact Census sample;
- person→household welfare construction.

The historical cascade's income-presence stage is useful evidence because a poverty-facing system cannot simply condition the Census population on already having positive income before prediction.

The first modern transport design should therefore ask a broader question than the current EPH-only positive-income model:

```text
shared / derived observables
        |
        v
person status / participation stages if useful
        |
        v
income-presence / hurdle stages if useful
        |
        v
conditional monetary amount
        |
        v
resolved person income / welfare
        |
        v
household welfare
```

The exact stages remain empirical decisions. Historical RFC1–RFC4 grouping is evidence, not architecture law.

## `samplerCensoARG` is orthogonal to model training

The sampler owns who is scored on the Census side.

For target-year mode it selects households with department-specific probabilities derived from donor person mass and exact target-year department person mass. It preserves all persons belonging to selected households.

The transport system receives that exact release and scores it. It does not resample, recalibrate or reinterpret the frame.

```text
samplerCensoARG
    exact sample household/person IDs
    selection probability
    frame_vintage
    sampling_target_period
            |
            v
encuestador-de-hogares
    score every released person
    preserve exact IDs
    construct household welfare
            |
            v
Poverty
    apply declared estimand / analysis semantics
```

A sampler probability must never be reused as an EPH model-fitting weight.

Likewise, `encuestador-de-hogares` should not invent the final poverty analysis weight. It carries forward sample/design lineage and produces welfare semantics.

## The two datasets that must not be confused

The ecosystem now needs two distinct EPH-derived artifacts:

### Neutral analysis frame

Reusable across scientific consumers.

Contains observations, identity, design metadata and reusable deterministic derivations.

### Study modeling dataset

Private to one scientific study.

Contains cohort filtering, target transforms, feature views, exclusions, split identity and any study-specific derived variables.

The current repository has historically collapsed some of these layers. Separating them is more important than immediately splitting the GitHub repository.

## Immediate producer work

The new evidence is tracked locally rather than turned into a new generic framework:

- `income-modeling-eph#29` — native EPH identity, survey design and internal component boundary for the future analysis frame;
- `income-modeling-eph#24/#25/#28` — source-backed preprocessing, entity identity/split integrity, and removal of Census deployment responsibility;
- `encuestador-de-hogares#6` — transport training population, EPH survey-design policy and household-aware OOF semantics;
- `samplerCensoARG#7` — governed target-year household sampling and explicit selection/weight semantics;
- `eph-censo-aligner#7` — semantic authority and canonical transport feature plane.

## Architecture test

A future engineer should be able to answer each question without opening unrelated model code:

| Question | Authority |
| --- | --- |
| What did INDEC EPH observe and how is the row identified? | EPH source + neutral EPH frame |
| What population does this EPH income experiment model? | EPH income-study contract |
| Which predictors/target/split/weights did that experiment use? | EPH study + experiment evidence |
| Which Census households/persons are to be scored? | `samplerCensoARG` |
| What EPH/Census concepts are semantically comparable? | `eph-censo-aligner` |
| What is the transport training population and staged DAG? | `encuestador-de-hogares` |
| How are EPH survey weights used in transport? | `encuestador-de-hogares` transport-model contract |
| What is the Census selection probability? | `samplerCensoARG` sample release |
| How do person predictions become household welfare? | `encuestador-de-hogares` |
| What analysis weight/estimand defines poverty? | Poverty method/frame contract |

If one repository must answer several unrelated rows of this table, the boundary should be re-examined.