---
title: Release discovery live proof
sidebar_position: 12
status: proven-two-edge
owners: [poverty-ecosystem-engineering]
---

# Release discovery live proof

The operational maturity gate defined in [Cross-repository release discovery contract](./10-release-discovery-contract.md) is now satisfied by two independent producer-consumer families.

This page records **implementation evidence**, not a new protocol. `ecosystem-release-discovery/v1` remains the architecture contract; producer manifests remain scientifically authoritative; consumer repositories retain their own eligibility rules.

## Proof A — monetary conversion → regional baskets

Producer: `matuteiglesias/IPC-Argentina`

Consumer: `matuteiglesias/canastasINDEC`

Live parent:

```text
candidate-arg-monetary-conversion-v1-0ed3539a8d52e013
```

Observed proof:

- IPC publishes `research.argentina-monetary-conversion/v1` as a content-addressed GitHub prerelease with `discovery.json` plus a deterministic asset;
- canastas independently discovers the producer prerelease without a sibling checkout or mutable `main` data URL;
- the consumer checks producer, artifact type, method, monetary reference, asset SHA-256 and producer manifest SHA-256 before materialization;
- the consumer persists `ecosystem-consumer-lock/v1` before calling its existing v2 scientific builder;
- the live proof built and independently validated regional-basket candidate `regional-baskets-v2-price-ac462f0e2191391a`;
- the same run produced Poverty-input candidate `poverty-baskets-v2-price-2024q1-73985143d8278cfb`;
- candidate status and inherited provenance warnings remain explicit;
- the one-shot merge proof trigger was removed; Monday polling plus manual dispatch remain.

The successful proof run is `canastasINDEC` Actions run `33356595201`.

## Proof B — EPH acquisition → income-modeling custody

Producer: `matuteiglesias/microdatos-EPH-INDEC`

Consumer: `matuteiglesias/income-modeling-eph`

Live parent:

```text
candidate-eph-2026-q1-beff9b8299d5
```

Observed producer proof:

- the live 2026-Q1 INDEC acquisition/materialization completed successfully;
- producer identity was repaired so stable source identity is separate from volatile retrieval-run evidence;
- the normalized release, stable source manifest and exact retained official source archive are packaged deterministically;
- the durable asset is about 6.7 MB, proving GitHub Releases are adequate for the current quarterly EPH transport size;
- an existing content-addressed tag is verified byte-for-byte rather than overwritten;
- candidate publication remains separate from downstream scientific approval.

The producer proof run is `microdatos-EPH-INDEC` Actions run `33357446554`.

Observed consumer proof:

- `income-modeling-eph` independently discovers the newest durable `candidate-eph-*` prerelease;
- it downloads `discovery.json` first, then exactly the declared transport asset;
- it verifies the outer checksum before extraction;
- archive traversal, special-member and root-identity checks are fail-closed;
- the consumer verifies the producer output manifest, stable source manifest, exact retained official archive, release/period identities and each normalized file checksum;
- it writes `eph-upstream-parent-lock/v1` under consumer custody;
- reproduction mode accepts an exact tag separately from convergence mode;
- convergence mode does not silently walk backward to an older release if the selected newest candidate is invalid;
- the consumer imports no producer runtime;
- the one-shot merge proof trigger was removed; Tuesday polling plus manual exact-tag reproduction remain.

The successful consumer proof run is `income-modeling-eph` Actions run `33358100454`.

This proof intentionally stops before quarterly → annual EPH preprocessing. The remaining `income-modeling-eph` work is scientific/source-reconstruction work tracked in issues #24 and #29, including native person/household identity, survey-design fields and a neutral analysis-frame contract.

## Operational maturity gate result

| Gate | Proof |
| --- | --- |
| Durable producer artifact survives Actions retention | GitHub prereleases in IPC and EPH producers |
| No floating `main` data identity | Both consumers resolve content-addressed release tags/assets |
| Independent transport + inner-manifest verification | Proven in canastas and income-modeling |
| Exact parent identity/checksum recorded | `ecosystem-consumer-lock/v1` and `eph-upstream-parent-lock/v1` |
| Idempotent exact-parent behavior | Producer byte verification plus consumer exact-parent locks/tests |
| Invalid newest candidate is visible | Both convergence consumers fail closed rather than silently selecting stale data |
| Candidate != scientific approval | Explicit in both producer and consumer workflows |
| No producer runtime import | Both consumers implement foreign-artifact boundaries locally |
| Scheduled polling works without dispatch | Monday canastas and Tuesday income-modeling polling paths |
| Different data families/sizes | Small monetary-conversion artifact and ~6.7 MB EPH quarter release |

**Result:** cross-repository durable release discovery is now **proven infrastructure**, not an architectural hypothesis.

## What this does not authorize

The two-edge proof is an engineering result only. It does not resolve downstream scientific gates.

In particular, it does not authorize:

- automatic promotion from `candidate` to `reviewed` or `approved`;
- a shared release-bus runtime or generic estate SDK;
- automatic EPH quarterly → annual preprocessing semantics;
- welfare-model training population, EPH survey-weight or OOF policies;
- target-period Census-state calibration;
- poverty-line, poverty-estimation or uncertainty choices;
- publication of a consequential Atlas poverty release before its exact scientific parents exist.

The next work should therefore propagate the already-proven contract only when a downstream scientific artifact has an actual governed parent to consume.

## Current frontier after the transport proof

```text
price lane
IPC durable release
    -> canastas exact parent + real basket candidate
    -> durable basket publication still required before a downstream poller can rely on it

income / welfare lane
EPH durable release
    -> income-modeling exact parent
    -> source-backed neutral EPH analysis frame still scientifically unresolved
    -> EPH→Census transport/welfare remains gated by training population, weights,
       grouped OOF and target-period-state decisions

convergence
exact population frame + exact deployable welfare + governed poverty lines/method/bindings
    -> poverty-estimate-release@2
    -> public Atlas + exact geography release
```

This is the desired shape: the **transport uncertainty has been removed**, exposing the real remaining scientific and product gates instead of hiding them behind repository plumbing.
