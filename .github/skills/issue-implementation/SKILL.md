---
name: issue-implementation
description: Procedimiento para implementar un issue aprobado de forma incremental, protegida por pruebas y con PR auditable.
---

# Issue Implementation

## Precondiciones

No comenzar si faltan:

```text
issue aprobado
spec aprobada
impacto/arquitectura aprobada
```

## Procedimiento

1. Lee issue, spec y documentación técnica relacionada.
2. Verifica branch base y estado limpio del repositorio.
3. Identifica el comportamiento que debe preservarse.
4. Crea o completa pruebas de caracterización cuando sea necesario.
5. Ejecuta baseline y registra resultados.
6. Implementa el cambio mínimo necesario.
7. Ejecuta pruebas relevantes tras cambios significativos.
8. Mantén problemas secundarios fuera del scope.
9. Registra riesgos residuales y decisiones realizadas durante implementación.
10. Prepara commits con una intención clara.
11. Ejecuta validaciones disponibles antes del PR.
12. Prepara un PR con evidencia real.

## Reglas

- no reescribir el sistema completo;
- no modificar contratos fuera del scope;
- no desactivar gates para conseguir verde;
- no inventar resultados de pruebas;
- no resolver automáticamente hallazgos secundarios;
- no hacer merge automáticamente;
- no usar secretos ni datos reales.

## Hallazgos secundarios

Cuando aparezca un nuevo problema:

```text
registrar candidato
-> describir evidencia
-> proponer backlog
-> continuar con el issue actual
```

## Salida de PR

Debe poder explicar:

```text
qué cambió
por qué cambió
qué se preservó
cómo se probó
qué no se resolvió
cómo revertir
```
