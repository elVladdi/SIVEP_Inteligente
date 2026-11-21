# ADR-0003 — Trabajo multiagente y trazabilidad completa

Estado: **Aceptada**. Fecha: 2026-11-21. Fuente: acuerdo del responsable del proyecto.

## Decisión
Existirán tres funciones: **IA coordinadora**, **IA de desarrollo** (ej.: Codex) e **IA auditora independiente** (ej.: Claude), complementadas por colaboradores humanos. **Cada prompt entregado a cualquiera de las IA y cada respuesta visible correspondiente se deben documentar** y vincular a la versión y tarea a la que pertenecen.

## Implementación
- Registrar todos los ciclos, incluidas iteraciones y solicitudes de corrección, en docs/ai-logs/ bajo identificador estable.
- Conservar texto completo de los intercambios aptos para publicación; incluir nombre de función, proveedor, modelo si se conoce, fecha, issue, commit, salida y auditoría.
- Los intercambios restringidos se custodian íntegros fuera del repositorio público en un entorno autorizado; en GitHub queda constancia de existencia, acceso responsable y referencia no sensible.
- Los informes de cambios y PR deben enlazar registros; la herramienta scripts/record_ai_interaction.py facilita el registro, pero no captura chats externos por sí sola.
- No incluir razonamiento interno privado ni instrucciones de sistema no expuestas legítimamente.

## Consecuencias y riesgo
La trazabilidad no depende de la memoria de una conversación particular. Puede requerirse carga manual de intercambios de plataformas sin integración. El responsable humano valida decisiones y publicaciones.