---
title: Working-reference policy
sidebar_position: 6
status: current
owners: [poverty-ecosystem-engineering]
---

# Working-reference policy

This repository predates the present ecosystem architecture and contains useful material recovered from earlier retrieval, documentation, notebooks, and operational practice. That material is retained, but its authority is now subordinate to the engineering architecture.

## Existing sections

The following directories are treated as **working reference material** unless a page explicitly states a stronger reviewed status:

```text
metodos/
operacion/
referencia/
catalogo/
pocket/
playbooks/
```

They may still be valuable for:

- historical context;
- implementation examples;
- operational recipes;
- source-variable reminders;
- visual conventions;
- candidate playbooks;
- links to producer repositories.

They must not silently define a cross-repository boundary, artifact schema, scientific authority, or current release status.

## Promotion test

A working page may be promoted into architecture/reference authority only when it answers:

1. **Owner:** which repository/system is authoritative for the subject?
2. **Source:** which exact source, contract, release, or code path supports the statements?
3. **Scope:** what does the page claim, and what does it explicitly not claim?
4. **Status:** current, fixture-proven, proposed, legacy, or blocked?
5. **Time:** when was the claim last checked, and against which revision/release?
6. **Consistency:** does it agree with the architecture and the producer's current contract?

If not, retain it as a useful note and label it accordingly.

## No bulk rewrite requirement

The architecture migration does **not** require rewriting every old page before the site is useful. The first priority is a trustworthy front door and authoritative engineering map. Existing content can then be reviewed incrementally when it becomes relevant to an active consumer or scientific decision.

## Historical work packets

`CODEX_*`, `WORK_PACKET_*`, old deployment notes, and similar documents are execution/history evidence. They should not occupy the primary conceptual navigation. They remain linkable for archaeology and maintenance but are not the first place a new engineer should learn the system.
