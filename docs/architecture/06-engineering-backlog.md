---
title: Engineering backlog
sidebar_position: 7
status: active
owners: [poverty-ecosystem-engineering]
---

# Engineering backlog

This page tracks **cross-repository architecture work that has been discovered from current producer evidence**. It is not a generic roadmap and it does not replace repository-local issues or pull requests.

The authoritative execution detail lives in the linked producer issue/PR. This page records why each item matters to the integration architecture and what boundary it is intended to clarify.

## Active boundary work

### EPH-only model science and neutral analysis frame

**Repository:** `matuteiglesias/income-modeling-eph`  
**Issue:** [#28 — Make income-modeling-eph strictly EPH-only and retire Census deployment responsibility](https://github.com/matuteiglesias/income-modeling-eph/issues/28)

Target: remove Census observability/scoring responsibility from ordinary EPH model science while preserving the staged-transport ideas as migration evidence. The reusable EPH handoff should remain an immutable analysis/preprocessed artifact; Census deployment moves to the transport instrument.

A follow-up audit of the former preprocessing authority in `encuestador-de-hogares` sharpens that boundary. Historical `EPHARG_train*` production mixed source assembly with a synthetic replacement sample, Jan-2016 monetary normalization, income-presence targets and target-derived ranks. Current `income-modeling-eph` independently marks `AGLO_rk` / `Reg_rk` as leakage-suspect and cannot yet reconstruct the committed annual inputs from exact raw EPH releases.

The next source-backed contract should therefore distinguish:

```text
versioned raw EPH quarter releases
        ↓
neutral EPH analysis frame
        ↓
modeling dataset / feature views
        ↓
experiments / model evidence
```

The neutral frame should preserve exact person/household identity, merge cardinality, period, official EPH geography/agglomerate identity and source variables/mechanical harmonizations. It should not intrinsically carry the old replacement sample, target-derived ranks, model filters, log targets or an implicit monetary conversion. This remains a boundary inside `income-modeling-eph` for now; do not create a new producer until repeated non-model consumers justify one.

### Semantic EPH↔Census authority

**Repository:** `matuteiglesias/eph-censo-aligner`  
**Issue:** [#7 — Recast aligner as pure semantic EPH↔Census authority for the transport layer](https://github.com/matuteiglesias/eph-censo-aligner/issues/7)

Target: mappings, losses, vintages and deployment-observability classes remain here; statistical transport validity does not. Ordinary `income-modeling-eph` should not require Census-aware integration.

### Census target-year household sampling

**Repository:** `matuteiglesias/samplerCensoARG`  
**Issue:** [#7 — Implement governed target-year department-stratified household sampling](https://github.com/matuteiglesias/samplerCensoARG/issues/7)  
**Boundary PR:** [#8 — Define target-year household sampling semantics](https://github.com/matuteiglesias/samplerCensoARG/pull/8)

The corrected architecture keeps the department population adjustment **inside sampling**. The sampling unit is a Census donor household, every person in a selected household is retained, and the external target is **person mass by department**.

The modern design now separates two authorities:

```text
D[d]   = exact donor person mass measured from the exact Census donor frame
T[d,y] = exact target-year department population from a governed demographic release

p[d,y] = c * T[d,y] / D[d]
```

before explicit probability bounds. This gives `E[selected_persons[d,y]] = c*T[d,y]` while preserving household integrity. It also removes an unnecessary historical coupling: the target demographic source does not need to provide the donor `2010` denominator.

The target-year source changes department mass only. Within-department age, education, employment, household-size, housing and other distributions are not separately projected; their continued usefulness is an explicit large-sample/donor-frame assumption.

The implementation needs a heavier repair before consequential use:

- pin one exact population-by-department source release for each target-year run;
- measure and verify `D[d]` from the exact donor frame;
- separate `frame_vintage=2010` from `sampling_target_period`;
- implement the explicit `target/donor` selection-probability formula;
- make probability-bound behavior fail-closed or explicitly governed and observable;
- keep household as the primary sampling unit and retain all persons in selected households;
- split `selection_probability`, optional donor-frame inverse-probability weight and downstream `analysis_weight`;
- do not allow `1/p` to silently undo the geographic rebalancing;
- remove six-region poverty/basket semantics from intrinsic sample identity.

No separate generic post-sampling population-calibration product is currently required.

#### Population-source archaeology

The repository contains two legacy population tables with materially different values.

- `proy_pop200125.csv` was introduced in 2021. Historical notebook commentary points explicitly to INDEC's official department-estimate publication for 2010–2025.
- `proy_pop20012225.csv` was introduced in July 2025. The same commit changed the historical sampler to read this newer file but **did not update the surrounding provenance comment**, which continued to describe the older official 2010–2025 table.

Therefore the later file has unresolved repository provenance and cannot be promoted merely because legacy code reads it.

The engineering contract should support exact versioned demographic parents rather than hard-code one historical CSV family. Current INDEC also publishes a Census-2022-based department-estimate family for 2022–2035. A later target-year run can consume an appropriate exact current release while the Census donor frame independently supplies `D[d]`.

### Survey-to-Census welfare inference

**Repository:** `matuteiglesias/encuestador-de-hogares`  
**Merged design:** [#4 — Revive encuestador as the EPH-Census inference boundary](https://github.com/matuteiglesias/encuestador-de-hogares/pull/4)  
**Hygiene PR:** [#5 — Retire legacy preprocessing and retraining workflows](https://github.com/matuteiglesias/encuestador-de-hogares/pull/5)

Target: make this the statistical-transport instrument: deployment DAG, staged OOF training, support/domain-shift diagnostics, exact Census scoring and a resolved household-welfare release. PR #4 established the bounded design/evidence boundary. PR #5 removes three stale GitHub Actions definitions that still scheduled or chained the former preprocessing, retraining and ranking paths even though the new lifecycle explicitly keeps that monolithic automation disabled.

### Monetary semantics and conversion

**Repository:** `matuteiglesias/IPC-Argentina`  
**Issue:** [#12 — Promote IPC-Argentina into the monetary-semantics and conversion authority](https://github.com/matuteiglesias/IPC-Argentina/issues/12)

Target: one owner for named monetary references and governed conversion artifacts. Downstream systems should not independently implement deflation, rebasing, projection or source splicing.

### Poverty lines and threshold areas

**Repository:** `matuteiglesias/canastasINDEC`  
**Issue:** [#13 — Define the governed poverty-lines release and threshold-area boundary](https://github.com/matuteiglesias/canastasINDEC/issues/13)

Target: modernize from the historical derived basket CSV toward exact source-backed threshold releases; keep monetary conversion delegated to IPC and keep threshold-area identity separate from Census/geography identity.

### Geography → threshold-area binding

**Repository:** `matuteiglesias/argentina-geography`  
**Issue:** [#36 — Publish an exact CPV-2010 department → six INDEC poverty-region binding](https://github.com/matuteiglesias/argentina-geography/issues/36)

Target: publish the source-backed territorial interpretation needed by Poverty without turning the six basket regions into intrinsic Census identity. Official INDEC evidence makes the crucial Buenos Aires split explicit: Gran Buenos Aires contains CABA plus specified partidos, while the rest of Buenos Aires is Pampeana. Prefer a tabular interpretation/binding release over new dissolved region geometry.

### Census indicator aggregation archaeology

**Repository:** `matuteiglesias/GeoCenso-Visualizer`  
**Issue:** [#1 — Separate durable Census indicator aggregation from legacy geography/presentation code](https://github.com/matuteiglesias/GeoCenso-Visualizer/issues/1)

The audit now supports a narrower lifecycle direction than the repository name suggests.

`Preguntas/*` preserves a substantial radio-level indicator surface across person, household and dwelling universes: activity, age, education, NBI, housing/services/material quality, tenure, household size and related Census concepts. Historical notebooks correctly preserve the important aggregation rule: sum category counts and denominators first, then recompute shares at the new geography rather than summing percentages.

However `tutoriales.rst` explicitly records that the radio-level answer tables came from data scraped from REDATAM by a collaborator and calls that surface, strictly, non-official. Therefore the committed `Preguntas/*` files are **not an acceptable modern source authority** simply because they are rich and convenient.

Current direction:

```text
historical Census-indicator aggregate evidence
+ semantic/category reference
+ regression fixtures
```

not an automatically revived producer.

Do not absorb the indicator semantics into `argentina-geography`; geography remains a separate parent. If a named consumer later needs governed Census indicator facts, first reproduce one representative indicator from an exact authorized/source-backed Census input. Only then decide whether a small geometry-free `census-indicator-facts` producer is justified.

The current poverty/inference chain does not need these pre-aggregated radio tables to operate, so there is no architectural pressure to revive the runtime prematurely.

### Legacy electoral-crosswalk retirement

**Repository:** `matuteiglesias/censo2010-circuitos-electorales`  
**PR:** [#2 — Freeze historical crosswalk after Argentina Geography A9](https://github.com/matuteiglesias/censo2010-circuitos-electorales/pull/2)

This is now a clear supersession rather than an unresolved migration. `argentina-geography` A9 is recorded as `complete_evidence_ready`, publishes exact 2021/2025 radio↔circuit and section↔department relation products, and pins the old repository at commit `49d563434471a7a5416f7aa92890e0c70c849a3e` as regression evidence. The old largest-overlap / majority-count one-target policies survive as named historical behavior, not current relation truth.

PR #2 adds archive lifecycle/system metadata and redirects operational consumers upstream without deleting historical notebooks or snapshots. This is the intended pattern when the estate proves that a durable legacy capability has genuinely moved: **freeze duplicate authority, preserve evidence**.

### Atlas system-state and live geometry transport truth

**Repository:** `matuteiglesias/argentina-poverty-atlas`  
**Issue:** [#19 — Reconcile W3 geography parent state and refresh Atlas system status after W2–W5](https://github.com/matuteiglesias/argentina-poverty-atlas/issues/19)

Target: the exact IGN 24-province parent now exists, while checked-in W3 state still says `blocked_upstream` and `SYSTEM.yaml` still describes a seed. Reconcile the truthful intermediate state without claiming Mapbox publication before provider/live-browser proof, and refresh system metadata to reflect the merged W2/W4/W5 product.

### Navigable engineering surface

**Repository:** `matuteiglesias/atlas-pobreza-docs`  
**Issue:** [#8 — Connect and verify the engineering docs on Vercel](https://github.com/matuteiglesias/atlas-pobreza-docs/issues/8)

Target: publish this same Docusaurus source on Vercel at a root URL, with GitHub Pages retained as fallback until there is a reason to retire it. Repository build/deployment configuration is already present; deployment state is not considered verified until the live Vercel URL and revision are inspected.

## Audited boundaries that should remain stable for now

### EPH acquisition

**Repository:** `matuteiglesias/microdatos-EPH-INDEC`

The acquisition boundary is already clean: one official EPH quarter is retrieved and converted into deterministic, provenance-bearing source tables. `SYSTEM.yaml` explicitly excludes analytical merging, feature engineering, deflation, targets and models. Do not expand this repository into the neutral analysis-frame producer merely because downstream preprocessing needs reconstruction.

### Poverty v2 scientific boundary

**Repository:** `matuteiglesias/indice-pobreza-UBA`

The current v2 boundary is already unusually close to the target architecture. `docs/UPSTREAM_HANDOFFS_V2.md` separately specifies a population frame, deployable welfare, poverty method, poverty lines and threshold-area binding; it explicitly rejects basket/poverty region as intrinsic Census-frame semantics and requires separate clocks for frame, welfare, lines and estimation. `src/poverty_pipeline/contracts_v2.py` keeps model, GIS, network and file I/O outside the semantic measurement boundary and enforces exact IDs, exact frame coverage, exact monetary-reference compatibility and exact threshold-area coverage.

Do **not** churn this producer while the sampler/inference/line producers are still settling. Its `population-frame` contract can be satisfied by an exact Census sample release plus declared design/analysis semantics; the contract name does not require a separate calibration producer.

## Next audit targets

These are **not yet execution issues**. They are the next places where current implementation should be compared against the accepted architecture before deciding whether a short PR or a larger sprint is warranted.

1. **Public Atlas W6 real-release adapter** — after W3 transport truth is reconciled and a real Poverty v2 parent exists, prove one complete `poverty-estimate-release/v2` → Atlas adapter without importing producer code or adding browser scientific aggregation.
2. **Legacy geography inside Poverty** — the Poverty repository still contains historical shapefiles/electoral lookup material. Revisit deletion/archive policy only after every currently useful geography behavior is reproducible from governed `argentina-geography` releases; do not mix that cleanup with the v2 scientific boundary.
3. **Demographic parent adapter for sampler** — the source-family boundary is now understood well enough that the next work should be tied to a concrete target-year run: pin an exact INDEC population-by-department product, map its department identity to the exact donor geography, and expose `T[d,y]` as a small immutable parent artifact/input without making the sampler the demographic authority.
4. **Private historical `CensoARG_20102` evidence** — use only as archaeological evidence when a concrete unresolved method points there. It contains old Census/EPH/synthetic-population/Mapbox notebooks, but its existence is not evidence that any current authority should be recreated from it.

## Backlog discipline

Promote an item from this page into producer work only when:

- the current repository state has been inspected;
- the producer boundary is clear enough to name the missing capability;
- a short change can be expressed as a reviewable PR, or a heavier change is captured as an issue with explicit gates;
- the change reduces ambiguity, duplicate authority or integration code;
- no target-state documentation is presented as already implemented fact.

The goal is not to maximize repository activity. It is to make the scientific chain easier to understand, verify, continue and change safely.
