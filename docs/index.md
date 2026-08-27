---
title: "Poverty Ecosystem Engineering"
sidebar_position: 1
slug: /
version: 1.0.0
status: current
owners: [poverty-ecosystem-engineering]
source_repo: https://github.com/matuteiglesias/atlas-pobreza-docs
source_path: docs/index.md
---

# Poverty Ecosystem Engineering

Este sitio es la **memoria de ingeniería y arquitectura cross-repo** del ecosistema argentino de medición de pobreza.

La pregunta central ya no es “¿en qué notebook está este cálculo?”, sino:

> **¿qué sistema tiene autoridad para transformar qué evidencia, bajo qué contrato, y qué debe quedar explícito cuando el resultado cruza al siguiente instrumento?**

El ecosistema se construye como una cadena de instrumentos científicos pequeños: adquisición EPH, modelado EPH, semántica EPH/Censo, sample/frame censal, inferencia survey-to-Census, semántica monetaria, líneas de pobreza, medición FGT, geografía y publicación en el Atlas.

## Empezar por la arquitectura

La sección **Engineering architecture** es la entrada autoritativa:

- [Authority and engineering principles](./architecture/00-authority-and-principles.md)
- [System map](./architecture/01-system-map.md)
- [Contracts and release chain](./architecture/02-contracts-and-release-chain.md)
- [Semantics, identities, and clocks](./architecture/03-semantics-identities-and-clocks.md)
- [Current state and migration](./architecture/04-current-state-and-migration.md)
- [Working-reference policy](./architecture/05-working-reference-policy.md)

La regla rectora es simple:

> **Rich science inside; boring contracts between systems.**

Los repos pueden contener ciencia sofisticada. Entre repos queremos artifacts versionados, IDs exactos, manifests, QA, limitaciones y checksums; no dependencias accidentales sobre código interno de un sibling.

## El sistema, en una línea

```text
EPH + Census + geography + monetary/threshold references
        -> semantically governed population and feature planes
        -> survey-to-Census welfare inference
        -> poverty measurement and estimation
        -> governed poverty release
        -> public Atlas
```

No todos estos arrows están hoy materializados con datos reales. La documentación distingue explícitamente **current**, **fixture-proven**, **proposed**, **legacy** y **blocked**.

## Material anterior: útil, pero subordinado

Las secciones históricas de Métodos, Operación, Referencia, Catálogo, Pocket y Playbooks se conservan como **working/reference material**. Surgieron de una etapa de retrieval y documentación anterior a la arquitectura actual. Algunas páginas son buenas ayudas prácticas; otras requieren revisión.

No definen por sí solas un boundary, un artifact contract ni una autoridad científica. Se van promoviendo cuando vuelven a ser relevantes y pueden enlazarse a evidencia actual.

## Para quién es

Este sitio sirve a:

- ingenieros que necesitan entender dónde debe vivir una nueva responsabilidad;
- investigadores que necesitan reconstruir lineage y supuestos antes de interpretar un resultado;
- maintainers y agentes que necesitan continuar el sistema sin depender de memoria oral;
- colaboradores que necesitan incorporarse sin recorrer años de scripts y notebooks históricos.

La documentación debe facilitar onboarding y continuation sin convertir el sitio en una segunda implementación de los sistemas que describe.
