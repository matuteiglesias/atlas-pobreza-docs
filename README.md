# Atlas de Pobreza

Sitio de documentación para organizar métodos, referencias, prácticas operativas y artefactos reutilizables vinculados con la medición de pobreza y desigualdad.

> **Estado:** borrador de documentación (`0.1.x`). La estructura y el contenido fueron revisados para este README el 3 de agosto de 2026; el despliegue y los enlaces internos no fueron revalidados en esta actualización.

## Para qué sirve

El Atlas busca hacer visible el proceso completo que existe detrás de un indicador: fuentes, transformaciones, decisiones metodológicas, controles de calidad y formas de publicación. Está pensado como superficie de trabajo para equipos técnicos, investigadores y actores institucionales.

El sitio se organiza en seis áreas:

- **Métodos:** bloques para procesamiento, análisis y visualización.
- **Operación:** versionado, naming, logs, CI/CD y reproducibilidad.
- **Referencia:** fuentes, variables y estructuras de entrada.
- **Catálogo:** indicadores y otros artefactos publicados.
- **Pocket:** recetas breves y checklists operativos.
- **Playbooks:** flujos completos expresados como inputs, pasos, QA y outputs.

## Autoridad y límites

Este repositorio **posee la estructura editorial y la documentación publicada** del Atlas.

No es la fuente autoritativa de:

- microdatos o geometrías originales;
- pipelines de producción;
- valores de indicadores;
- resultados que pertenezcan a otros repositorios.

Cada documento debería identificar su fuente y, cuando corresponda, enlazar al repositorio productor.

## Trabajar localmente

Requiere Node.js y Yarn.

```bash
yarn
yarn start
```

Para verificar que el sitio puede compilarse:

```bash
yarn build
```

El contenido principal vive en `docs/`; `docs/index.md` es la entrada editorial del sitio.

## Estado conocido

- El sitio todavía contiene páginas planificadas o en borrador.
- Existen placeholders de procedencia —por ejemplo, `source_repo: <repo-url>`— que deben reemplazarse antes de considerar una página autoritativa.
- Una compilación correcta no demuestra que los datos o métodos enlazados estén actualizados.

## Criterio de mantenimiento

Un cambio debería mejorar al menos una de estas propiedades: procedencia, claridad metodológica, navegabilidad, reproducibilidad o conexión con un artefacto autoritativo. Evitar incorporar contenido sin dueño, fecha o estado verificable.

## Posible cambio de nombre

`atlas-site` es funcional pero genérico. Si esta superficie se consolida como producto estable, `atlas-pobreza-docs` o `poverty-atlas-docs` harían visible su función sin cambiar su alcance.
