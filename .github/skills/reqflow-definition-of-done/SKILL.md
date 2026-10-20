---
name: reqflow-definition-of-done
description: Criterios transversales para evaluar si un cambio de ReqFlow es funcional, seguro, verificable y revisable.
---

# ReqFlow Definition of Done

## Propósito

Evaluar evidencia del cambio sin declarar automáticamente que todo el caso está completo.

## Criterios del caso

### Contratos preservados

El alcance funcional relevante continúa operando y los contratos protegidos no cambian sin decisión explícita.

```text
POST /auth/login
GET/POST /api/tasks
GET /api/summary
POST /api/requirements
```

### CI en verde

Build y pruebas reproducibles. No se aceptan bypass para conseguir un check verde.

### Cobertura crítica >= 85 %

Los módulos priorizados deben demostrar cobertura suficiente cuando este gate corresponda a la etapa de evaluación.

No inventes cobertura si no existe un reporte.

### Dependencias controladas

No incorporar vulnerabilidades High/Critical sin decisión explícita y documentada.

### Secure coding

Según el componente y alcance:

- SQL parametrizado cuando aplique;
- auth/authz del lado servidor;
- secretos fuera del código;
- archivos controlados.

### PR auditable

Debe incluir evidencia, decisiones, trade-offs, riesgos residuales y estrategia de rollback.

## Guardrails no negociables

- ejecución exclusivamente en entorno de laboratorio;
- no utilizar datos o secretos reales;
- no desactivar tests, CodeQL, SCA o quality gates para forzar merge;
- no aceptar resultados generados por IA sin comprenderlos y validarlos;
- no ejecutar pruebas ofensivas contra sistemas externos.

## Forma de evaluar

Para cada criterio responde únicamente con uno de:

```text
CUMPLIDO - citar evidencia
PENDIENTE DE OTRO GATE - indicar cuál
NO APLICA AL ALCANCE - justificar
FALTA EVIDENCIA - indicar qué falta
BLOQUEADO - explicar causa
```

No conviertas ausencia de evidencia en aprobación.
