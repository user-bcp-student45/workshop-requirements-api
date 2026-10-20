---
name: discovery-analysis
description: Procedimiento para investigar un sistema existente y producir hallazgos con evidencia sin modificarlo.
---

# Discovery Analysis

## Cuándo usar

Cuando la tarea requiera comprender un repositorio existente, mapear responsabilidades, identificar deuda/riesgos o preparar backlog antes de cambiar código.

## Procedimiento

1. Identifica el alcance exacto del repositorio o componente.
2. Lee README, estructura, configuración, contratos y tests relevantes.
3. Construye primero una imagen del comportamiento y responsabilidades existentes.
4. Formula hipótesis, pero no las declares hallazgos hasta encontrar evidencia.
5. Para cada hallazgo registra:
   - título;
   - evidencia concreta;
   - impacto;
   - prioridad propuesta;
   - contrato potencialmente afectado;
   - forma de validación.
6. Limita la salida a los hallazgos de mayor valor para evitar listas ruidosas.
7. Marca todos inicialmente como `CANDIDATO`.
8. Detente para revisión humana.

## Reglas

- no modificar código;
- no inventar CVEs ni vulnerabilidades;
- no asumir que una mala práctica genérica existe sin evidencia local;
- no revelar ubicaciones de fallas a partir de material de trainer no disponible al participante;
- no confundir preferencia estética con defecto;
- no crear issues automáticamente.

## Salida

```markdown
### <hallazgo>
- Estado: CANDIDATO
- Evidencia:
- Impacto:
- Prioridad propuesta:
- Contrato potencialmente afectado:
- Cómo validarlo:
```
