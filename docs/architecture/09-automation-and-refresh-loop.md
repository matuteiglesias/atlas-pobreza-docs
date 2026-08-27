---
title: Automation and refresh loop
sidebar_position: 10
status: current-design
owners: [poverty-ecosystem-engineering]
---

# Automation and refresh loop

The poverty ecosystem should not depend on a person remembering which repository to refresh after INDEC publishes a new quarter or a new price/basket observation appears.

The target operating model is an **eventually convergent release graph**: source repositories detect new exact evidence, producers build immutable candidates, consumers re-evaluate only the products affected by those parents, and failures expose the next missing engineering/scientific boundary.

Automation does not change scientific authority. A scheduled workflow is allowed to discover, materialize, validate and package evidence. It is not allowed to make an unresolved methodological choice disappear merely to keep the graph green.

## Two different questions

The scientific architecture asks:

> Which exact artifacts and semantic authorities justify this result?

The automation architecture asks:

> When one of those exact parents changes, which bounded executors should run so the ecosystem converges again?

They are related DAGs, but they are not the same DAG.

## The convergence protocol

Every maintained producer should converge toward the same small operational vocabulary:

```text
discover
   |
   v
materialize candidate
   |
   v
validate / QA / compatibility
   |
   v
publish immutable candidate identity
   |
   +------> notify direct consumers when possible
   |
   v
consumer detects newer exact parent
   |
   v
rebuild downstream candidate
   |
   v
promotion gate
```

The important separation is **candidate production vs promotion**.

A deterministic acquisition or computation can often be automated completely. A scientific promotion may still require explicit review. Keeping those states separate lets scheduled Actions run aggressively without silently changing the meaning of a published poverty result.

## Root triggers

There is no single global clock. Several independent source families can invalidate different parts of the graph.

| Root trigger | First producer | Main downstream consequences |
| --- | --- | --- |
| New EPH quarter | `microdatos-EPH-INDEC` | neutral EPH frame; EPH income-study evidence; transport-training candidate; potentially welfare/Poverty/Atlas |
| New price observation / source revision | `IPC-Argentina` | monetary conversion candidates; transport welfare reference; basket compatibility; potentially Poverty/Atlas |
| New official basket/poverty-line source | `canastasINDEC` | poverty-line candidate; Poverty/Atlas |
| New department population target | `samplerCensoARG` input authority | target-year Census household sample; scoring frame; welfare/Poverty/Atlas |
| New geography/relation release | `argentina-geography` | sampler/binding compatibility, threshold-area binding, Atlas geometry where affected |
| Method/code merge | local producer | rebuild local candidate; downstream only if a new promoted contract/release is emitted |

A new EPH quarter does **not** require re-sampling Census if the exact target-year sample remains the same. A new price observation does **not** imply semantic EPH/Census mappings changed. The automation graph should preserve those independences.

## Current scheduled skeleton

The first implementation intentionally puts existing bounded executors on staggered clocks before the complete durable release/dispatch layer exists.

All cron times below are UTC. GitHub scheduled workflows are best-effort and may be delayed; the ordering is a convergence hint, not a transactional guarantee.

| Clock | Repository | Current scheduled executor | Mature claim |
| --- | --- | --- | --- |
| Mon 09:17 | `microdatos-EPH-INDEC` | exact quarter acquisition/release probe | candidate source materialization only |
| Mon 09:37 | `IPC-Argentina` | source probe → source lock → candidate → current consumer preflight | price candidate maturity probe |
| Mon 10:07 | `canastasINDEC` | official source probe → source lock | basket source side only; exact price parent still required |
| Tue 10:47 | `income-modeling-eph` | annual validation → preprocessing fixture → flagship release preflight | EPH-science maturity gate, no expensive fit |
| Tue 11:17 | `eph-censo-aligner` | fixture check/test/smoke → require approved real-vintage mapping | semantic transport eligibility |
| Tue 11:47 | `samplerCensoARG` | deterministic sample-release fixture/check | sample contract health; real target-year path still #7 |
| Wed 12:17 | `encuestador-de-hogares` | governing-contract parse → require deterministic synthetic transport executor | intentionally red until first transport/welfare proof exists |
| Wed 13:17 | `indice-pobreza-UBA` | deterministic synthetic poverty-release smoke | Poverty v2 contract/release health |
| Wed 14:17 | `argentina-poverty-atlas` | lint/typecheck/test/build | public-consumer integrity |
| Thu | `atlas-pobreza-docs` | build/deployment verification | engineering-memory integrity |

The clocks are deliberately sparse. Source cadences are quarterly/monthly and the scientific graph is not a low-latency transaction system. Repository dispatch can later reduce latency without removing the scheduled safety net.

## Failure is evidence

The first scheduled generation is expected to reveal missing pieces. A red run should be classified rather than immediately patched away.

Useful failure classes include:

```text
source_unavailable_or_ambiguous
source_schema_changed
source_lock_failed
candidate_build_failed
candidate_stale_for_consumer
missing_durable_parent_distribution
semantic_review_incomplete
identity_or_join_gate_failed
monetary_reference_unresolved
sampling_design_incomplete
transport_synthetic_proof_missing
transport_support_or_domain_shift_failed
poverty_parent_missing_or_incompatible
public_consumer_contract_drift
```

An intentionally strict mature gate may remain red while fixture tests are green. That is preferable to representing `fixture-proven` as `real-release-ready`.

## Durable release discovery is the next infrastructure seam

Runner-local Actions artifacts are useful evidence, but they are not yet a complete cross-repository contract.

A mature producer must expose a durable immutable locator for each candidate/promoted release. The physical distribution can evolve:

```text
GitHub Release asset
or
immutable object-store path
or
another explicitly governed content-addressed store
```

The logical requirements do not change:

- exact release ID;
- parent release IDs/hashes;
- immutable data/object locator;
- manifest and checksums;
- release status (`candidate`, `reviewed`, `approved`, etc.);
- QA/limitations;
- no floating `main` URL as scientific identity.

Large releases do not need to be committed to Git. A manifest may point to an immutable external object while retaining all scientific identity locally.

## Polling plus dispatch, not dispatch alone

Cross-repository `repository_dispatch` is useful but requires a credential with permission to target another repository. The repository-scoped default `GITHUB_TOKEN` should not be treated as a system-wide message bus.

The target pattern is redundant:

```text
producer publishes exact candidate
        |
        +--> optional repository_dispatch to named consumers
        |
        +--> consumer's scheduled poll eventually discovers it anyway
```

If dispatch is introduced, use a narrowly scoped `ECOSYSTEM_DISPATCH_TOKEN` or dedicated GitHub App. Its absence must reduce latency, not correctness.

## Consumer locks

Each consequential downstream release should continue to pin exact parents.

The scheduled consumer asks:

```text
what exact parent(s) am I pinned to?
        vs
what eligible immutable candidate(s) now exist?
```

If there is no newer eligible parent, the job is a no-op.

If there is a newer parent, the consumer may automatically build a **candidate** and run compatibility/scientific gates. It should not silently rewrite an approved parent lock merely because a newer source exists.

This is especially important for:

- EPH source revisions;
- semantic mapping revisions;
- price composites/projection boundaries;
- Census target-year sampling design;
- transport-model promotion;
- poverty methodology/threshold revisions.

## Expected EPH-triggered chain

Once durable publication exists, a new EPH quarter should converge approximately as follows:

```text
microdatos EPH exact quarter release
        |
        v
neutral EPH analysis-frame candidate
        |
        +--> income-modeling-eph study/evidence candidate
        |
        +--> aligner compatibility check / feature-release candidate
                       |
                       v
                 encuestador
          transport-model candidate
                       |
                 household welfare
                       |
                       v
                    Poverty
                       |
                       v
                     Atlas
```

Several arrows are conditional:

- a schema-compatible EPH quarter may require no semantic mapping change;
- a transport model should not be retrained/promoted merely because data are newer if its scientific policy says otherwise;
- the exact Census sample can be reused across multiple welfare quarters;
- Poverty should rebuild only when all exact required parents are compatible.

## Expected price-triggered chain

```text
price source observation/revision
        |
        v
IPC monetary candidate
        |
        +--> encuestador monetary-reference compatibility
        |
        +--> canastas exact price parent (when method requires it)
                       |
                       v
                    Poverty
                       |
                       v
                     Atlas
```

Again, `newer` is not automatically `approved`.

## Automation permissions

Default scheduled jobs should use:

```text
contents: read
```

until a specific publishing operation is proven safe.

A source publisher that writes immutable releases may receive narrowly scoped `contents: write`. Cross-repository notification should use a separate narrow credential. Provider secrets (for example Mapbox) stay confined to the consumer/provider workflow that needs them.

Scheduled jobs should also use:

- explicit timeouts;
- concurrency guards;
- bounded source retrieval;
- deterministic temporary output directories;
- step summaries describing what green/red actually proves;
- no direct large-data write-back to `main`.

## Current bounded rollout

The first rollout is deliberately asymmetric.

Some repositories already have a real network-facing candidate executor (`microdatos-EPH-INDEC`, `IPC-Argentina`, `canastasINDEC`). They can probe real sources now.

Some have only deterministic fixtures for their current governed boundary (`samplerCensoARG`, Poverty v2). Their scheduled Actions keep those boundaries alive while the real parent path is implemented.

The aligner and encuestador have explicit mature gates that are expected to expose current incompleteness:

- aligner: no consequential transport until at least one real vintage has been scientifically approved;
- encuestador: no claim of runtime transport until a deterministic synthetic EPH→Census→household-welfare executor exists.

This is intentional. The scheduled graph is being used as an observability instrument for architecture maturity.

## Definition of mature system-wide maintenance

The ecosystem is operationally mature when:

1. every root data authority has a bounded scheduled discovery path;
2. successful source discoveries produce immutable candidate release identities;
3. every consumer can discover newer eligible parents without sibling checkout/import assumptions;
4. scheduled builds are idempotent when nothing changed;
5. parent changes rebuild candidates, not silently approve them;
6. scientific/semantic failures stay visible as red gates or explicit blocked states;
7. exact parent locks are preserved in every downstream release;
8. direct consumer notification is optional acceleration, with polling as recovery;
9. Poverty can consume exact frame + welfare + method + line + area-binding parents and emit a deterministic candidate release;
10. Atlas can update from a new governed poverty release without adding scientific logic.

The desired end state is not “all workflows are always green.” It is that **every red workflow identifies a bounded factual reason why the release graph cannot currently converge**.
