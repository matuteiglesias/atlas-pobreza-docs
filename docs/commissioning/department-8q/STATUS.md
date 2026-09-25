---
title: "Commissioning status — department poverty × 8 quarters"
status: cloud-implementation-complete-local-real-data-pending
as_of: 2026-09-25
---

# Commissioning status

The bounded cloud-development graph is complete through D6. The bundle remains active because the real-data critical path D3b → D3c → I1 still requires local governed parents that are not available in GitHub/cloud execution.

No fixture or partial public artifact is being substituted for that missing real-data proof.

## Completed and merged

| Work packet | State | Evidence |
|---|---|---|
| D1 — 525-department geography | real-source-proven | `argentina-geography` main `5b8ee5f9ccaa6a7b1bd94127c37733782cc70c68`; exact 525 Census-2010 identities, governed display labels, deterministic WGS84 display derivative |
| D2 — generic predictive producer | fixture-proven / merged | `indice-pobreza-UBA` main includes PR #33, merge `8567f4dbdd196036c72191542980ca439738c40b` |
| D3a — 8Q batch + reconciliation mechanics | fixture-proven / merged | `indice-pobreza-UBA` PR #34, merge `1b8cc418c52bd9a85fb0a9c4e314dc0802b48af1`; exact 8-period orchestration and department→province→ARG numerator/denominator reconciliation |
| D4 — Atlas verified release-set ingest | fixture-proven / merged | `argentina-poverty-atlas` PR #26, merge `90a614ef172e25cf1a8c53f419666128c4d45f60`; canonical synthetic 50,496-fact projection |
| D5 — 525-feature Mapbox transport | provider-proven / merged | `argentina-poverty-atlas` main `a317bc91fe3b426a686bcffd3cf7db59873e9dcc`; Mapbox provider read-back exact 525/525 |
| D6 — geography-level + 8Q UI | CI-proven / merged | `argentina-poverty-atlas` PR #27, merge `13357bb7912cd644c94054813653bb343337b7a6`; level/period state, department lookup, URL repair, generic table/detail/trend/map |
| I1 consumer seam | implemented / not real-data-proven | Atlas `POVERTY_BATCH_ROOT` consumes D3a `releases/` + `province-oracles/`, requires governed department geography labels, and cross-checks province/department national cells before projection |

## D1 / D5 immutable evidence

The governed department geography and published transport are pinned to:

- upstream geography commit: `5b8ee5f9ccaa6a7b1bd94127c37733782cc70c68`;
- dataset: `arggeo.indec.census.2010.department-footprint`;
- release: `derived-2010-national-c9184f47fd46`;
- exact official Census source snapshot SHA-256: `c9184f47fd46c8a47e2c15e5c734b7b6ceb660ce737e18430691f6fbff3c53e8`;
- canonical GeoParquet SHA-256: `7b6664f59d0f4f82937d52ca8fe01a22b1f4dc40d83bc49c608dfd1b40b390c5`;
- display GeoJSON SHA-256: `399033eb5bd79337959f2d3483f6843c71551726723308a6bcc4c7889fe27df8`;
- exact 525-ID set SHA-256: `f2c1195789c5d556db3379dd89310b0b6cea4df84ef6efa14cc814dbfc831144`;
- Mapbox tileset: `matuteiglesias2.arg-dept-indec2010-c9184f47fd46`;
- Mapbox source layer: `Argentina departments - INDEC Census 2010 c9184f47fd46`;
- publication proof: exact `525/525` `geography_id` recovery; geometry payload contains no poverty values.

## Remaining local critical path

D3b must resolve and hash the accepted real parents for every quarter. D3c then runs the already-merged batch runner and must produce exactly:

- 8 independent department releases;
- 6,312 facts per quarter;
- 50,496 facts over all eight quarters;
- PASS department→province reconciliation for every universe/concept/FGT cell;
- PASS department→ARG reconciliation;
- `batch_manifest.json`, `parent_resolution_report.json`, `reconciliation_report.json`, and `checksums.sha256`.

The GitHub/cloud estate currently provides governed evidence for the 2024-Q3 chain, plus target-year sampling machinery, but does not expose a complete governed 2025 semantic-plane + predictive-welfare parent chain. Therefore D3b/D3c and the real I1 proof remain **pending local evidence**, not failed and not substituted.

## Closeout rule

Do not archive this directory yet. Archive only after the local D3b/D3c run and I1 verify:

1. eight real periods;
2. exact 525/525 scientific-to-geometry join;
3. zero dropped/extra/fuzzy IDs;
4. no browser scientific recomputation;
5. durable architecture docs updated with the resulting real release identities.
