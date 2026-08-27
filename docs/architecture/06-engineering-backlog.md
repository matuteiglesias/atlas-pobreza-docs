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

### Navigable engineering surface

**Repository:** `matuteiglesias/atlas-pobreza-docs`  
**Issue:** [#8 — Connect and verify the engineering docs on Vercel](https://github.com/matuteiglesias/atlas-pobreza-docs/issues/8)

Target: publish this same Docusaurus source on Vercel at a root URL, with GitHub Pages retained as fallback until there is a reason to retire it. Deployment state is not considered verified until the live URL and revision are inspected.

## Next audit targets

These are **not yet execution issues**. They are the next places where current implementation should be compared against the accepted architecture before deciding whether a short PR or a larger sprint is warranted.

1. **`indice-pobreza-UBA` topology after welfare inference is accepted** — its v2 scientific boundary is strong, but current upstream metadata still reflects some legacy/direct model relationships. Re-check only after the inference boundary is accepted so the producer contract does not churn unnecessarily.
2. **`argentina-poverty-atlas` system-state metadata** — W2–W5 have materially advanced beyond the original seed status. Reconcile `SYSTEM.yaml`, W3 live-transport truth and the remaining W6 real-release adapter gate from current `main`.
3. **EPH neutral analysis-frame ownership** — determine whether source-faithful EPH analytical preparation remains naturally inside `income-modeling-eph` or eventually deserves a more neutral release/producer boundary. Do not create a new repository before repeated consumer pressure exists.
4. **Geography→threshold-area relation** — decide which exact `argentina-geography` release/relation should carry the mapping from governed Census/administrative geography to poverty-line areas, without making either provider or Poverty own an implicit canonical geography.
5. **Population calibration evidence** — if later-period Census-derived population frames are needed, identify the exact population projection/calibration authority and evidence before implementing a generic weighting layer.

## Backlog discipline

Promote an item from this page into producer work only when:

- the current repository state has been inspected;
- the producer boundary is clear enough to name the missing capability;
- a short change can be expressed as a reviewable PR, or a heavier change is captured as an issue with explicit gates;
- the change reduces ambiguity, duplicate authority or integration code;
- no target-state documentation is presented as already implemented fact.

The goal is not to maximize repository activity. It is to make the scientific chain easier to understand, verify, continue and change safely.
