---
title: "Agent protocol — department poverty commissioning"
status: proposed-working-reference
---

# Agent protocol

This packet is designed for autonomous implementation agents. The purpose is to let agents move quickly **inside a small contract box**, not to invite repo-wide redesign.

## 1. Before editing

Every agent MUST:

1. read the target repository's `AGENTS.md`, `SYSTEM.yaml` and local engineering instructions if present;
2. refresh `main` and record its starting SHA;
3. inspect the exact files named by its work packet plus their direct tests;
4. compare current implementation with `SPEC.md`;
5. stop only for a **material contract conflict**, not for ordinary implementation choices.

If main has drifted beyond the baseline in `README.md`, current producer evidence wins. The agent must preserve the bundle's user-facing invariants unless it finds a genuine incompatibility, in which case it reports the conflict rather than silently changing the spec.

## 2. Branch and PR discipline

Use one branch/PR per work packet and repository, for example:

```text
feat/department-geometry-release
feat/predictive-geography-producer
feat/department-8q-batch
feat/atlas-multirelease-geography
feat/department-mapbox-transport
feat/atlas-department-ui
```

A PR should be mergeable independently once its declared dependencies are satisfied. Do not mix opportunistic cleanup.

PR body MUST contain a handoff block:

```text
WORK_PACKET:
BASE_SHA:
HEAD_SHA:
CONTRACTS_TOUCHED:
TESTS_RUN:
FIXTURE_PROOF:
REAL_DATA_PROOF: none | local evidence reference
BLOCKERS:
FOLLOW_ON:
```

## 3. Test-first interpretation

Spec-driven development here means:

1. encode contract assertions/golden fixtures;
2. make the smallest implementation change that satisfies them;
3. preserve existing regressions;
4. add only the abstractions needed by the next dependent packet.

Do not create a generalized framework because it might be useful later.

## 4. Cloud data boundary

Cloud agents may use:

- committed fixtures;
- public upstream data;
- detached public/research releases already in GitHub;
- generated synthetic artifacts;
- GitHub Actions;
- existing repository secrets through their declared workflows.

Cloud agents MUST NOT require or request upload of local Census samples, local welfare artifacts, private semantic-plane data, or untracked workstation paths.

When real evidence is unavailable, use a fixture and label proof as fixture-only.

## 5. Local lane boundary

Local Codex executes `LOCAL_REAL_DATA_RUNBOOK.md` after D2/D3a code is available.

Local work may patch a producer if real data exposes a genuine bug, but the patch must return through a normal producer PR with a minimized synthetic regression whenever possible. Do not leave the only fix in an uncommitted local script.

## 6. Cross-repository authority

- `argentina-geography` owns geometry products and geography release evidence.
- `samplerCensoARG` owns Census sample mechanics/identity handoff.
- `encuestador-de-hogares` owns predictive welfare artifacts.
- `indice-pobreza-UBA` owns poverty estimation and detached estimate releases.
- `argentina-poverty-atlas` owns verification, presentation projection and browser UX.
- `atlas-pobreza-docs` owns this temporary cross-repo commissioning spec and later the durable architecture description.

Consumers may verify upstream contracts. They may not silently repair upstream identities or science.

## 7. Hard scope fences

Agents MUST NOT:

- retrain income models;
- change residual modeling;
- change the poverty method;
- add department identity as an ML feature;
- invent a new release schema merely to hold multiple periods;
- add Atlas-side department aggregation;
- dissolve radio geometry in the Atlas;
- join departments by display name;
- coerce geography IDs through numbers;
- publish raw local parents;
- refactor unrelated legacy paths;
- change official/research labeling semantics;
- treat green UI tests as scientific proof.

## 8. Failure handling

A failed exact-set check is a useful result. Preserve it.

If an agent finds:

- 524/526 department identities;
- conflicting department inventories;
- a non-zero-preserving parent;
- missing quarter parents;
- a different capability cube in one period;
- geometry/estimate set disagreement;
- reconciliation disagreement;

it must emit a compact blocker with exact IDs/hashes and stop the affected packet. It should continue unrelated tests if useful.

Do not normalize away the discrepancy.

## 9. Merge order

Preferred order:

```text
D1 ──────> D5 ──┐
                 ├─> D6 ──┐
D2 -> D3a -> D4 ┘         |
  \                       v
   -> local D3b -> D3c -> I1
```

D4 may merge before real releases exist if its fixture proof is complete. D5 may merge once the governed geometry parent exists. D6 may use fixtures but cannot be called fully commissioned until I1.

## 10. Completion semantics

Use these words precisely:

- **implemented** — code/contract exists;
- **fixture-proven** — deterministic synthetic/golden path passes;
- **real-data-proven** — accepted real parents executed and evidence persisted;
- **published** — detached/transport artifact is intentionally made consumable;
- **browser-proven** — deployed browser joined and rendered the governed surfaces;
- **commissioned** — all required acceptance gates are green.

No agent may promote one state into another without evidence.
