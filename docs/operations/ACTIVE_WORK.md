# Trabajo actual y referencia para cambios de IA

Actualización inicial: 2026-11-21. Este tablero es un índice; **siempre comprobar GitHub (issues, PR y SHA) antes de actuar**.

**Fase F0:** revisión de literatura, definición de comparabilidad y calidad de datos. No existe modelo entrenado ni acceso SIVEP operativo implementado.

| Issue | Trabajo | Estado inicial comprobado | Handoff |
|---|---|---|---|
| [#1](https://github.com/elVladdi/SIVEP_Inteligente/issues/1) | Literatura y normativa | Abierto; por desarrollar | No generado |
| [#2](https://github.com/elVladdi/SIVEP_Inteligente/issues/2) | Inventario conceptual de campos SIVEP/formato B | Abierto; pendiente de autorizaciones/detalle de datos | No generado |
| [#5](https://github.com/elVladdi/SIVEP_Inteligente/issues/5) | Continuación INICIO/CONTINUACIÓN y checkpoints | En elaboración; PR #4 | docs/operations/checkpoints/2026-11-21/coordinator-session-001-CP01.md |
| [#3](https://github.com/elVladdi/SIVEP_Inteligente/issues/3) | Trazabilidad de chats entre plataformas | Abierto; registrador manual existe | No generado |

**Ninguna tarea de desarrollo tiene asignación exclusiva confirmada al crear este archivo.** No elegir automáticamente un issue solo por su número. Cuando se asigne una tarea, indicar agente responsable, rama, PR, SHA, estado y ruta `docs/operations/handoffs/ISSUE-<numero>.md`. Actualizar por PR al iniciar, pausar, auditar o cerrar.

**Índice de sesiones:** [SESSION_INDEX.md](SESSION_INDEX.md) (consultar checkpoint pertinente y contrastar SHA). 

**Decisiones pendientes:** familia piloto, granularidad SA 6/NANDINA 8/nacional 10, campos reales y permisos, protocolo experto, modelos y métricas definitivas. Ver ADR.

Al retomar: prompt de rol → AGENTS.md → PROJECT_STATE.md → este tablero → issue/PR y último handoff → verificar SHA real.