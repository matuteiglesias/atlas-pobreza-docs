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

### Census sample versus population frame

**Repository:** `matuteiglesias/samplerCensoARG`  
**Issue:** [#7 — Separate Census sample identity from population-frame calibration and projection semantics](https://github.com/matuteiglesias/samplerCensoARG/issues/7)

Target: preserve the strong deterministic sample/identity release while separating inclusion weights from later calibration/projection and removing poverty-threshold region semantics from intrinsic Census identity.

The 2026-08-27 audit recovered the historical projection mechanism: `censo_sampler/io.py` loads `data/info/proy_pop20012225.csv`, labels it as INDEC department population projections, computes year/2010 ratios and uses them to change department sampling fractions. Two different `proy_pop*` tables are committed, their provenance/transformation relationship is not governed, and one spans 2001–2025 even though the identifiable Census-2010 INDEC department-estimation publication covers 2010–2025. INDEC now also publishes a new Census-2022-based department estimation family for 2022–2035.

Therefore the committed projection tables are **legacy methodological evidence**, not current population-frame authority. A later-period frame must separately pin demographic source, geography vintage/relation, target date, calibration method and calibration weights. A CPV-2010 sample must never become a 2024/2025 population merely because one historical projection multiplier was applied.

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

Target: determine whether the durable concern is a governed Census-indicator aggregation producer, regression/archive evidence, or a smaller split of reusable measurement logic from obsolete presentation. The repository mixes radio-level person/household/dwelling indicator facts with local geography joins and HTML/GeoJSON outputs. Do not absorb it wholesale into `argentina-geography`: Census indicator semantics and geography authority are different concerns.

### Atlas system-state and live geometry transport truth

**Repository:** `matuteiglesias/argentina-poverty-atlas`  
**Issue:** [#19 — Reconcile W3 geography parent state and refresh Atlas system status after W2–W5](https://github.com/matuteiglesias/argentina-poverty-atlas/issues/19)

Target: the exact IGN 24-province parent now exists, while checked-in W3 state still says `blocked_upstream` and `SYSTEM.yaml` still describes a seed. Reconcile the truthful intermediate state without claiming Mapbox publication before provider/live-browser proof, and refresh system metadata to reflect the merged W2/W4/W5 product.

### Navigable engineering surface

**Repository:** `matuteiglesias/atlas-pobreza-docs`  
**Issue:** [#8 — Connect and verify the engineering docs on Vercel](https://github.com/matuteiglesias/atlas-pobreza-docs/issues/8)

Target: publish this same Docusaurus source on Vercel at a root URL, with GitHub Pages retained as fallback until there is a reason to retire it. Deployment state is not considered verified until the live URL and revision are inspected.

## Audited boundaries that should remain stable for now

### EPH acquisition

**Repository:** `matuteiglesias/microdatos-EPH-INDEC`

The acquisition boundary is already clean: one official EPH quarter is retrieved and converted into deterministic, provenance-bearing source tables. `SYSTEM.yaml` explicitly excludes analytical merging, feature engineering, deflation, targets and models. Do not expand this repository into the neutral analysis-frame producer merely because downstream preprocessing needs reconstruction.

### Poverty v2 scientific boundary

**Repository:** `matuteiglesias/indice-pobreza-UBA`

The current v2 boundary is already unusually close to the target architecture. `docs/UPSTREAM_HANDOFFS_V2.md` separately specifies a population frame, deployable welfare, poverty method, poverty lines and threshold-area binding; it explicitly rejects basket/poverty region as intrinsic Census-frame semantics and requires separate clocks for frame, welfare, lines and estimation. `src/poverty_pipeline/contracts_v2.py` keeps model, GIS, network and file I/O outside the semantic measurement boundary and enforces exact IDs, exact frame coverage, exact monetary-reference compatibility and exact threshold-area coverage.

Do **not** churn this producer merely to rename upstream repositories while `encuestador-de-hogares` and the line/frame producers are still settling. Revisit its producer topology when real upstream adapters exist. At that point, check whether the in-memory v2 contracts need additional serialized provenance fields for model/scoring lineage, projection/calibration semantics and line source/value status; the final v2 release already records exact parent release IDs and content hashes.

## Next audit targets

These are **not yet execution issues**. They are the next places where current implementation should be compared against the accepted architecture before deciding whether a short PR or a larger sprint is warranted.

1. **Population calibration product boundary** — the evidence now proves that the old sampler multipliers are not an acceptable modern authority. Determine whether the first real poverty run needs any later-period calibration at all; if yes, pin one exact demographic product and decide whether the calibration artifact belongs alongside the sampler or in a separate population-frame producer only after its semantics are proven.
2. **Public Atlas W6 real-release adapter** — after W3 transport truth is reconciled and a real Poverty v2 parent exists, prove one complete `poverty-estimate-release/v2` → Atlas adapter without importing producer code or adding browser scientific aggregation.
3. **Legacy geography inside Poverty** — the Poverty repository still contains historical shapefiles/electoral lookup material. Revisit deletion/archive policy only after every currently useful geography behavior is reproducible from governed `argentina-geography` releases; do not mix that cleanup with the v2 scientific boundary.
4. **Private historical `CensoARG_20102` evidence** — use only as archaeological evidence when a concrete unresolved method points there. It contains old Census/EPH/synthetic-population/Mapbox notebooks, but its existence is not evidence that any current authority should be recreated from it.

## Backlog discipline

Promote an item from this page into producer work only when:

- the current repository state has been inspected;
- the producer boundary is clear enough to name the missing capability;
- a short change can be expressed as a reviewable PR, or a heavier change is captured as an issue with explicit gates;
- the change reduces ambiguity, duplicate authority or integration code;
- no target-state documentation is presented as already implemented fact.

The goal is not to maximize repository activity. It is to make the scientific chain easier to understand, verify, continue and change safely.
