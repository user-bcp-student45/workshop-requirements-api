---
name: architecture-decision
description: Procedimiento para evaluar impacto técnico y registrar decisiones incrementales en un sistema existente.
---

# Architecture Decision

## Cuándo usar

Cuando una spec aprobada necesita traducirse en límites técnicos, estrategia de cambio o una decisión arquitectónica explícita.

## Procedimiento

1. Lee la spec aprobada y su evidencia.
2. Comprende la estructura actual antes de proponer cambios.
3. Identifica componentes, dependencias y contratos afectados.
4. Define el cambio mínimo capaz de cumplir la spec.
5. Favorece pasos pequeños y reversibles.
6. Define qué comportamiento debe protegerse con pruebas antes de modificar.
7. Enumera riesgos y trade-offs.
8. Si existe una decisión significativa, registra:
   - contexto;
   - opciones consideradas;
   - decisión;
   - consecuencias.
9. No generes ADR por rutina si no existe una decisión real.
10. Detente para revisión humana antes de implementación.

## Reglas brownfield

- una reescritura masiva no es la opción por defecto;
- una arquitectura idealizada no justifica romper contratos;
- mantener compatibilidad observable tiene prioridad salvo decisión explícita;
- no arreglar problemas fuera del alcance aprobado;
- separar deuda descubierta de deuda comprometida.

## Salida mínima

```markdown
## Impacto
## Componentes afectados
## Contratos protegidos
## Estrategia incremental
## Pruebas necesarias
## Riesgos / trade-offs
## Decisiones abiertas
```
