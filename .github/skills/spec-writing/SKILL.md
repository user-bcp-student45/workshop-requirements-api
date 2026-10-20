---
name: spec-writing
description: Procedimiento para convertir una necesidad o hallazgo aprobado en una spec verificable para un sistema existente.
---

# Spec Writing

## Cuándo usar

Cuando un hallazgo o necesidad ya fue aprobado y debe transformarse en una especificación versionable antes de diseñar la solución técnica.

## Procedimiento

1. Identifica el issue/hallazgo fuente y su evidencia.
2. Describe brevemente el comportamiento actual relevante.
3. Define el problema o necesidad confirmada.
4. Registra explícitamente qué comportamiento debe preservarse.
5. Define alcance y fuera de alcance.
6. Escribe criterios de aceptación verificables.
7. Registra riesgos, supuestos y preguntas abiertas.
8. Identifica contratos protegidos relacionados.
9. Evita prescribir implementación salvo que sea una restricción ya decidida.
10. Detente para revisión humana.

## Estructura sugerida

```markdown
# <título>

## Fuente
Issue / hallazgo / evidencia

## Contexto actual

## Problema confirmado

## Comportamiento a preservar

## Alcance

## Fuera de alcance

## Criterios de aceptación

## Contratos afectados/protegidos

## Riesgos, supuestos y preguntas abiertas
```

## Reglas

- no inventar requisitos;
- no incluir hallazgos no aprobados;
- no cambiar contratos de ReqFlow implícitamente;
- no convertir la spec en diseño de clases o implementación;
- usar lenguaje comprobable.
