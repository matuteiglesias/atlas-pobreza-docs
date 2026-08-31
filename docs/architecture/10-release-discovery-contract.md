---
title: Cross-repository release discovery contract
sidebar_position: 11
status: proven-first-edge
owners: [poverty-ecosystem-engineering]
---

# Cross-repository release discovery contract

This document defines the smallest cross-repository transport contract needed for the poverty ecosystem to converge without sibling checkouts, mutable `main` URLs, or human copy/paste.

The contract is intentionally **not** a shared runtime, workflow engine, package, registry service, or scientific authority. Producers keep ownership of their artifact schemas and scientific manifests. Consumers keep ownership of eligibility and compatibility rules. This contract only standardizes how an already-built release is made durably discoverable and how a consumer pins the exact bytes it chose.

The first live proof is `IPC-Argentina` publishing `research.argentina-monetary-conversion/v1` as a content-addressed GitHub prerelease. The next proof is a consumer independently discovering, verifying and copying that release before building its own candidate.

## Design rule

The ecosystem should compose as:

```text
producer authority
      |
      v
validate producer artifact
      |
      v
publish immutable-by-contract release identity
      |
      v
small discovery envelope + durable bytes
      |
      v
consumer discovers eligible candidates
      |
      v
consumer copies + verifies exact bytes
      |
      v
consumer records exact parent lock
      |
      v
consumer builds its own candidate
```

There is no central executor in this path.

## Three layers, three authorities

Release distribution has three distinct metadata layers. They must not be collapsed.

### 1. Transport metadata

Examples: GitHub release tag, target commit, publication timestamp, asset identifier, object-store key.

This metadata answers **where can the exact bytes be retrieved?** It is operational, not scientific.

### 2. Discovery envelope

A small machine-readable envelope, currently `ecosystem-release-discovery/v1`, answers **what artifact is this parcel claiming to transport, and how can the parcel be verified before opening it?**

The envelope should remain small. It is an index label, not a second scientific manifest.

### 3. Artifact manifest

The manifest inside the artifact remains producer-owned and scientifically authoritative. It answers **what exact artifact is this, how was it produced, which parents and methods justify it, what QA passed, and what limitations remain?**

Consumers MUST validate the inner producer manifest after transport verification. A valid outer checksum does not make a scientifically ineligible artifact acceptable.

## `ecosystem-release-discovery/v1`

The first proven envelope uses the following logical fields.

```json
{
  "schema": "ecosystem-release-discovery/v1",
  "producer": "matuteiglesias/example-producer",
  "artifact_type": "research.example-artifact/v1",
  "release_id": "example-release-content-id",
  "status": "candidate",
  "created_at": "2026-08-31T00:00:00Z",
  "method_id": "research.example-method/v1",
  "parent": {},
  "github_release": {
    "tag": "candidate-example-release-content-id",
    "asset_name": "example-release-content-id.zip",
    "asset_sha256": "...",
    "manifest_sha256": "..."
  }
}
```

The currently proven fields are intentionally narrower than a universal schema. New artifact families MAY add artifact-specific discovery hints when they materially improve safe candidate selection, but consumers must never depend on undeclared producer internals.

### Required logical fields

Every durable discovery envelope MUST identify:

- `schema`;
- `producer` repository identity;
- `artifact_type`;
- exact `release_id`;
- explicit release `status`;
- creation time when defined by the producer;
- one durable locator family;
- checksum of the transported bytes;
- checksum or independently verifiable identity of the producer manifest;
- parent identity information sufficient to reject obvious lineage mismatches before expensive processing.

When method, monetary reference, geography identity, sample identity, or another semantic discriminator is essential for safe consumer discovery, the producer SHOULD expose that discriminator in the discovery envelope as a selection hint. The consumer still validates the authoritative inner manifest.

## Allowed locator families

### GitHub Release assets

Preferred for small and moderate public artifacts.

The producer publishes:

- a release/tag keyed by exact release identity;
- `discovery.json`;
- one deterministic artifact archive;
- checksums in the discovery envelope and/or inner manifest.

A producer encountering an existing tag MUST verify the existing bytes rather than overwrite them. A mismatch is a hard publication failure.

### Immutable object storage

Use for large public artifacts that are awkward as GitHub Release assets.

The discovery envelope remains durably available from the producer surface and records an immutable, versioned object locator plus checksum. Floating object aliases such as `latest` are not scientific identities.

### Local-only durable custody

Allowed where privacy, licensing, or operational sensitivity forbids public bytes. The same release identity, checksums and parent semantics still apply. A downstream consumer must have an explicitly governed way to resolve the locator in its permitted environment.

Local-only is not permission to use an undocumented developer path.

## Candidate publication is not scientific promotion

Transport state and scientific state are independent.

A producer MAY automatically publish a validated `candidate` before a separate maturity or review gate. Publication means:

> these exact bytes exist under this exact identity and can be reproduced or inspected later.

It does NOT mean:

> downstream science should automatically accept these bytes.

The ecosystem vocabulary remains explicit, for example:

```text
synthetic
candidate
reviewed
approved
superseded
rejected
```

Transitions to `reviewed` or `approved` require the producer's declared scientific governance. A transport workflow must never promote status merely because publication succeeded.

## Consumer discovery policy

A consumer owns candidate selection.

Every consumer that polls upstream releases SHOULD define two modes.

### Convergence mode

Select the newest eligible release under an explicit declared ordering and eligibility policy.

If the selected newest candidate fails verification or scientific compatibility, the job SHOULD fail with a named reason. It MUST NOT silently walk backward through older releases until one happens to pass unless that fallback policy is itself explicitly governed.

This prevents a broken upstream candidate from silently causing downstream computation on stale data.

### Reproduction mode

Accept an explicit release ID/tag/locator override and resolve exactly that parent. This mode is used for reproducing historical downstream releases and debugging.

## Consumer copy-and-pin rule

A consumer must not compute consequential output directly against mutable remote state.

The bounded handoff is:

```text
1. resolve exact discovery envelope
2. download exact transport asset
3. verify transport checksum
4. unpack safely into an isolated directory
5. verify inner producer manifest and checksums
6. apply consumer-specific eligibility rules
7. copy/retain the exact parent under consumer run custody
8. write an exact parent lock
9. build downstream candidate from that lock
```

The parent lock SHOULD record at least:

- producer;
- artifact type;
- release ID;
- upstream status observed;
- durable transport locator;
- transport checksum;
- producer manifest checksum;
- locally retained/copied path or object identity;
- retrieval time;
- consumer selection policy/mode;
- any artifact-specific semantic identity required by the consumer.

Downstream manifests then refer to the exact parent lock/release identity, not to `main`, a branch, or an Actions run.

## Safe archive handling

Consumers MUST treat downloaded archives as untrusted transport containers even when they originate from a controlled producer.

A consumer loader should reject:

- absolute archive members;
- `..` traversal/path escape;
- unexpected symlink/device members where the archive format permits them;
- multiple ambiguous top-level release roots when one exact root is required;
- inner release IDs that disagree with the discovery envelope;
- checksum mismatches.

A consumer should unpack only after verifying the outer asset checksum where practical.

## Idempotence

The release graph is expected to run repeatedly.

Producer rule:

```text
same scientifically identical release
    -> same release identity
    -> same deterministic transport bytes
    -> verify existing publication, do not replace
```

Consumer rule:

```text
same selected exact parents
    -> no unnecessary parent rewrite
    -> deterministic candidate identity where the producer semantics support it
```

A scheduled poll that discovers no newer eligible parent is a healthy no-op.

## Actions artifacts are run evidence, not release identity

GitHub Actions artifacts remain useful for:

- debugging;
- logs and intermediate QA;
- acceptance evidence;
- short-lived reproduction during a workflow incident.

They are not the durable scientific handoff because retention is finite and the locator is tied to an execution run rather than the producer's release identity.

A release MAY be represented both as an Actions artifact and a durable release asset. The former records execution evidence; the latter is the cross-repository transport.

## Polling is the correctness baseline

Every automated consumer SHOULD have a scheduled polling path capable of discovering durable releases without receiving a producer event.

Optional `repository_dispatch` may reduce latency after publication, but it carries only a notification such as artifact type/release ID. It is never the release transport and never the only recovery path.

```text
producer publication
      |
      +---- optional dispatch(release_id) ----> consumer
      |
      +---- durable release ------------------> consumer scheduled poll
```

The consumer independently resolves and verifies the durable release in either case.

## Large-artifact policy

Artifact size changes physical transport, not identity semantics.

For large EPH/Census/geography products:

- keep a small durable discovery envelope;
- keep exact scientific manifest/checksums;
- place bytes in a durable immutable object location if GitHub Releases are inconvenient;
- retain content checksum and exact object/version identity;
- never substitute a floating download URL for a release ID.

Large artifacts do not justify sibling repository checkouts or hidden shared filesystems as the default cross-repository API.

## First adoption sequence

The protocol is being proven consumer-first rather than abstracted into shared code.

### Edge A — monetary conversion -> baskets

`IPC-Argentina` has already proven producer publication for `research.argentina-monetary-conversion/v1` using a deterministic archive plus `discovery.json` in a content-addressed GitHub prerelease.

The next gate belongs to `canastasINDEC`:

1. discover one exact eligible IPC release;
2. copy and verify it independently;
3. pin the exact parent;
4. use its already-existing v2 consumer path;
5. publish the resulting basket candidate under its own identity.

This edge is the first full producer -> consumer -> producer proof.

### Edge B — EPH acquisition -> income preprocessing

`microdatos-EPH-INDEC` should publish a successful exact-quarter acquisition durably rather than only as a short-lived Actions artifact.

`income-modeling-eph` should then discover/copy exact EPH quarter releases and create an explicit source-set lock for the preprocessing release it builds.

This is deliberately the second proof because it exercises the same protocol across a different data family and likely a larger transport payload.

### Later edges

Only after two independent edges work should the same interface propagate through:

```text
EPH/preprocessing + alignment + Census sample + monetary conversion
    -> encuestador transport/welfare

welfare + population frame + poverty lines + method + area binding
    -> Poverty v2

poverty-estimate-release@2 + geography release
    -> public Atlas
```

Each repository remains free to reject a newer candidate at its own scientific gate.

## No shared runtime yet

Do not create a central `release-bus`, estate SDK, generic DAG executor, or registry service merely because the protocol is repeated.

Repository-local discovery/verification code is acceptable while the interface is young. Extract shared implementation only when multiple independent current consumers exhibit the same stable code and changing it independently becomes a demonstrated maintenance burden.

The contract is shared. The runtime is not.

## Operational maturity gate

The durable handoff seam is considered proven when all of the following are true for at least two independent producer-consumer edges:

1. producer artifacts are available after Actions artifact expiry;
2. discovery does not read a floating `main` data URL;
3. consumer independently verifies transport and inner manifest identity;
4. consumer records exact parent release ID and checksums;
5. rerunning against unchanged parents is idempotent;
6. an invalid newest candidate fails visibly rather than silently falling back;
7. candidate publication remains distinct from scientific approval;
8. downstream code imports no producer runtime merely to obtain released data;
9. scheduled polling can recover without dispatch;
10. the same protocol works for both a small artifact family and a materially different data family.

At that point cross-repository release discovery is infrastructure rather than an architectural hypothesis.
