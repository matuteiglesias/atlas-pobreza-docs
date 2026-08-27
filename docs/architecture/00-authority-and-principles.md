---
title: Authority and engineering principles
sidebar_position: 1
status: current
owners: [poverty-ecosystem-engineering]
---

# Authority and engineering principles

This site is the **engineering documentation authority for the Argentina poverty research ecosystem**. Its job is to make the cross-repository system legible: which repository owns each scientific or technical concern, which artifacts cross boundaries, what semantics are preserved at each handoff, and which parts of the target architecture are already proven versus still proposed.

It is not a substitute for producer repositories. A producer remains authoritative for its own implementation, scientific method, release schema, QA, and data. This site is authoritative for the **accepted ecosystem-level architecture and integration intent**.

## Precedence

When sources disagree, use this order:

1. **Producer release and repository-local contract** for what a concrete artifact means and how it was produced.
2. **This architecture site** for the intended cross-repository boundary, integration sequence, and shared vocabulary.
3. **Working notes, retrieved documentation, notebooks, historical scripts, and examples** as supporting evidence only.

A mismatch between (1) and (2) is not resolved by silently choosing one. It is an engineering discrepancy to record and close.

## Core design rules

### Rich science inside; boring contracts between systems

Each scientific instrument may contain substantial domain logic. Cross-repository integration should remain small: immutable artifacts, manifests, exact identities, QA, limitations, and checksums. Downstream systems should not need sibling checkouts or private implementation details.

### One authority per semantic transition

Ask at every boundary: **who is allowed to change the meaning of this value?**

Examples:

- EPH acquisition owns the source snapshot, not income modeling.
- IPC owns an approved change of monetary reference, not the poverty kernel.
- the EPH–Census aligner owns semantic mapping, not statistical transport;
- the inference instrument owns survey-to-Census prediction and construction of a deployable welfare concept;
- Poverty owns poverty thresholds, classification, and FGT estimation;
- Argentina Geography owns geography identity and release semantics;
- the public Atlas owns presentation and interaction, not new scientific estimands.

### Artifacts, not sibling runtime imports

The target integration style is artifact-based. A repository may depend on another repository's **released output contract**; it should not require importing sibling production code to reproduce the scientific chain.

### Current state and target state must not be conflated

Documentation must say whether a boundary is:

- `current` — implemented and the present authority;
- `fixture-proven` — contract and behavior demonstrated on deterministic fixtures;
- `proposed` — target boundary agreed in design but not yet proven in production;
- `legacy` — retained for genealogy or compatibility only;
- `blocked` — cannot advance without an explicit scientific or source decision.

A target diagram is not evidence that a real release exists.

### Exact identity before convenience

Cross-repository joins use stable declared identifiers. No positional joins, fuzzy matching, implicit latest-version lookup, or silent provider substitution are acceptable in a scientific release.

### Clocks remain separate

The ecosystem may simultaneously carry:

- EPH source/training period;
- Census frame vintage;
- population calibration or target period;
- welfare estimation period;
- price reference period;
- poverty-line period;
- geography vintage.

These clocks may coincide, but software must not assume that they do.

### Uncertainty is propagated, never invented

A downstream instrument may propagate an upstream uncertainty representation when it is scientifically justified and explicitly contracted. It must not manufacture uncertainty merely because a downstream report expects intervals.

### Working documentation is subordinate

The pre-existing `metodos/`, `operacion/`, `referencia/`, `catalogo/`, `pocket/`, and `playbooks/` material is retained because parts remain useful. It is **working reference material**, not ecosystem architecture authority. A page can be promoted only after it identifies its owner, source, status, scope, and relationship to the architecture documented here.

## Engineering outcome

The desired system is not a single poverty pipeline. It is a set of small scientific instruments whose responsibilities are narrow enough to reason about independently and whose outputs compose into a reproducible chain.
