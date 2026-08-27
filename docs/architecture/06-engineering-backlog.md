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

### EPH-only model science

**Repository:** `matuteiglesias/income-modeling-eph`  
**Issue:** [#28 — Make income-modeling-eph strictly EPH-only and retire Census deployment responsibility](https://github.com/matuteiglesias/income-modeling-eph/issues/28)

Target: remove Census observability/scoring responsibility from ordinary EPH model science while preserving the staged-transport ideas as migration evidence. The reusable EPH handoff should remain an immutable analysis/preprocessed artifact; Census deployment moves to the transport instrument.

### Semantic EPH↔Census authority

**Repository:** `matuteiglesias/eph-censo-aligner`  
**Issue:** [#7 — Recast aligner as pure semantic EPH↔Census authority for the transport layer](https://github.com/matuteiglesias/eph-censo-aligner/issues/7)

Target: mappings, losses, vintages and deployment-observability classes remain here; statistical transport validity does not. Ordinary `income-modeling-eph` should not require Census-aware integration.

### Census sample versus population frame

**Repository:** `matuteiglesias/samplerCensoARG`  
**Issue:** [#7 — Separate Census sample identity from population-frame calibration and projection semantics](https://github.com/matuteiglesias/samplerCensoARG/issues/7)

Target: preserve the strong deterministic sample/identity release while separating inclusion weights from later calibration/projection and removing poverty-threshold region semantics from intrinsic Census identity.

### Survey-to-Census welfare inference

**Repository:** `matuteiglesias/encuestador-de-hogares`  
**PR:** [#4 — Revive encuestador as the EPH-Census inference boundary](https://github.com/matuteiglesias/encuestador-de-hogares/pull/4)

Target: make this the statistical-transport instrument: deployment DAG, staged OOF training, support/domain-shift diagnostics, exact Census scoring and a resolved household-welfare release. The current PR is design/evidence only; runtime proof remains a later bounded wave.

### Monetary semantics and conversion

**Repository:** `matuteiglesias/IPC-Argentina`  
**Issue:** [#12 — Promote IPC-Argentina into the monetary-semantics and conversion authority](https://github.com/matuteiglesias/IPC-Argentina/issues/12)

Target: one owner for named monetary references and governed conversion artifacts. Downstream systems should not independently implement deflation, rebasing, projection or source splicing.

### Poverty lines and threshold areas

**Repository:** `matuteiglesias/canastasINDEC`  
**Issue:** [#13 — Define the governed poverty-lines release and threshold-area boundary](https://github.com/matuteiglesias/canastasINDEC/issues/13)

Target: modernize from the historical derived basket CSV toward exact source-backed threshold releases; keep monetary conversion delegated to IPC and keep threshold-area identity separate from Census/geography identity.

### Atlas system-state and live geometry transport truth

**Repository:** `matuteiglesias/argentina-poverty-atlas`  
**Issue:** [#19 — Reconcile W3 geography parent state and refresh Atlas system status after W2–W5](https://github.com/matuteiglesias/argentina-poverty-atlas/issues/19)

Target: the exact IGN 24-province parent now exists, while checked-in W3 state still says `blocked_upstream` and `SYSTEM.yaml` still describes a seed. Reconcile the truthful intermediate state without claiming Mapbox publication before provider/live-browser proof, and refresh system metadata to reflect the merged W2/W4/W5 product.

### Navigable engineering surface

**Repository:** `matuteiglesias/atlas-pobreza-docs`  
**Issue:** [#8 — Connect and verify the engineering docs on Vercel](https://github.com/matuteiglesias/atlas-pobreza-docs/issues/8)

Target: publish this same Docusaurus source on Vercel at a root URL, with GitHub Pages retained as fallback until there is a reason to retire it. Deployment state is not considered verified until the live URL and revision are inspected.

## Audited boundaries that should remain stable for now

### Poverty v2 scientific boundary

**Repository:** `matuteiglesias/indice-pobreza-UBA`

The current v2 boundary is already unusually close to the target architecture. `docs/UPSTREAM_HANDOFFS_V2.md` separately specifies a population frame, deployable welfare, poverty method, poverty lines and threshold-area binding; it explicitly rejects basket/poverty region as intrinsic Census-frame semantics and requires separate clocks for frame, welfare, lines and estimation. `src/poverty_pipeline/contracts_v2.py` keeps model, GIS, network and file I/O outside the semantic measurement boundary and enforces exact IDs, exact frame coverage, exact monetary-reference compatibility and exact threshold-area coverage.

Do **not** churn this producer merely to rename upstream repositories while `encuestador-de-hogares` and the line/frame producers are still settling. Revisit its producer topology when real upstream adapters exist. At that point, check whether the in-memory v2 contracts need additional serialized provenance fields for model/scoring lineage, projection/calibration semantics and line source/value status; the final v2 release already records exact parent release IDs and content hashes.

## Next audit targets

These are **not yet execution issues**. They are the next places where current implementation should be compared against the accepted architecture before deciding whether a short PR or a larger sprint is warranted.

1. **EPH neutral analysis-frame ownership** — determine whether source-faithful EPH analytical preparation remains naturally inside `income-modeling-eph` or eventually deserves a more neutral release/producer boundary. Do not create a new repository before repeated consumer pressure exists.
2. **Geography→threshold-area relation** — the basket method already says its six region IDs are basket regions and that Buenos Aires cannot be assigned wholesale because Gran Buenos Aires/Pampeana require subprovincial classification. Determine the exact source evidence and whether the mapping belongs as an `argentina-geography` relation/interpretation release or as a line-application binding with governed geography parents. Do not create a geometry product merely to encode a poverty policy.
3. **Population calibration evidence** — if later-period Census-derived population frames are needed, identify the exact population projection/calibration authority and evidence before implementing a generic weighting layer.
4. **Public Atlas W6 real-release adapter** — after W3 transport truth is reconciled and a real Poverty v2 parent exists, prove one complete `poverty-estimate-release/v2` → Atlas adapter without importing producer code or adding browser scientific aggregation.
5. **Legacy geography inside Poverty** — the Poverty repository still contains historical shapefiles/electoral lookup material. Revisit deletion/archive policy only after every currently useful geography behavior is reproducible from governed `argentina-geography` releases; do not mix that cleanup with the v2 scientific boundary.

## Backlog discipline

Promote an item from this page into producer work only when:

- the current repository state has been inspected;
- the producer boundary is clear enough to name the missing capability;
- a short change can be expressed as a reviewable PR, or a heavier change is captured as an issue with explicit gates;
- the change reduces ambiguity, duplicate authority or integration code;
- no target-state documentation is presented as already implemented fact.

The goal is not to maximize repository activity. It is to make the scientific chain easier to understand, verify, continue and change safely.
