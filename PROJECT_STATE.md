# Estado del proyecto — SIVEP Inteligente

Fecha de actualización: 2026-11-21. Estado: F0, preparación metodológica. No hay modelo ni acceso operativo implementado.

## Situación de activación de agentes

**CONFIGURACIÓN.** Ninguna IA Coordinadora, Desarrolladora ni Auditora ha sido activada aún. Esta conversación es diseño/configuración del proyecto: se responde directamente en chat, sin aplicar el contrato de respuesta por URL o registrar cada turno como conversación operativa. Se documentan decisiones y cambios en ADR/issues/PR.

**OPERACIÓN** requerirá que el responsable solicite de forma explícita activar el rol y leer/ejecutar el prompt correspondiente. ADR-0008 y docs/operations/ACTIVATION_PROTOCOL.md regulan el inicio. Los registros históricos coordinator-0001 a coordinator-0006 se reclasifican como configuración.

## Decisiones vigentes
- SIVEP es la fuente histórica prevista; se espera trabajar con datos del formato B de las DAM peruanas.
- El sistema ofrece referencias y alertas al especialista, quien conserva la decisión final.
- Usos: riesgo anticipado de subvaloración, ranking explicable de antecedentes, priorización de DAM canal verde en control posterior, y trazabilidad de valores históricos.
- Primera prioridad científica: determinar cómo identificar mercancías idénticas, similares y no comparables.
- Desarrollo colaborativo: IA coordinadora, IA desarrolladora (por ejemplo Codex), IA auditora independiente (por ejemplo Claude), colaboradores humanos y responsable final.
- **Todos los prompts y respuestas visibles de las tres funciones de IA deben registrarse** en este repositorio antes de cerrar una tarea; consultar docs/ai-logs/README.md y ADR-0003.
- Repositorio público: no almacenar información real o sensible de SIVEP/DAM.

## Pendiente de validación o decisión
- Familia piloto de mercancías; nivel de partida SA 6, NANDINA 8 o nacional 10 dígitos.
- Diccionario preciso de campos SIVEP/formato B y permisos de acceso.
- Protocolo jurídico-técnico de comparabilidad; selección de modelos y métricas.
- Estrategia de despliegue, licencia, responsables y controles de seguridad.
- Mecanismo de captura automática de prompts y respuestas en las plataformas externas, sujeto a sus capacidades y permisos.

## Inicio y continuidad multi-IA
- [prompts/README.md](prompts/README.md): prompts iniciales portables para coordinadora, desarrolladora y auditora.
- [docs/operations/ACTIVE_WORK.md](docs/operations/ACTIVE_WORK.md): tareas abiertas y asignaciones cuando existan; contrastar con GitHub.
- [docs/operations/HANDOFF_PROTOCOL.md](docs/operations/HANDOFF_PROTOCOL.md): relevo por issue, rama, SHA, PR, pruebas, pendientes y logs.
- Issues iniciales: #1 (literatura), #2 (inventario conceptual) y #3 (toma de registros IA); sin asignación exclusiva de implementación confirmada.

## Continuidad de sesiones
- Aprobado: modos INICIO y CONTINUACIÓN para cualquier rol, modelo y chat (incluido un nuevo chat del mismo proyecto ChatGPT).
- [SESSION_INDEX.md](docs/operations/SESSION_INDEX.md): índice de checkpoints; [SESSION_CONTINUITY.md](docs/operations/SESSION_CONTINUITY.md): protocolo; [checkpoints/](docs/operations/checkpoints/): estados verificables por sesión.
- Issue #5: implementar protocolo y puntos de control; PR #4: integración pendiente de auditoría y fusión.
- El estado no registrado no puede recuperarse con certeza; la captura de chats externos sigue requiriendo integraciones o exportación manual.

## Política de entrada y salida
- ADR-0006: el usuario únicamente indica la ruta del prompt. El agente la lee y verifica su versión SHA. La respuesta sustantiva completa se publica en `docs/ai-logs/` y, en el chat, solo se devuelve su enlace verificado (salvo instrucción contraria).
- [OUTPUT_PROTOCOL.md](docs/operations/OUTPUT_PROTOCOL.md) establece excepciones, seguridad, publicación y el registro de prompts/respuestas. Issue #6, PR #4: implantación documental pendiente de auditoría/fusión.

## Comunicación bidireccional entre agentes
- Aprobado ADR-0007: los tres agentes pueden emitir prompts completos para cualquiera de los otros dos según su autorización.
- **Entrada a cada destinatario:** `prompts/inbox/<rol-destino>/REQ-YYYYMMDD-NNN.md`; índice `prompts/ROUTING_INDEX.md`.
- **Respuestas completas:** `docs/ai-logs/YYYY-MM-DD/<id-unico>.md`, enlazadas desde el índice.
- Protocolo `docs/operations/ROUTING_PROTOCOL.md`; issue #7. Guardar un prompt no ejecuta otra IA automáticamente.

## Próximos pasos
1. Revisión bibliográfica y normativa crítica; matriz de evidencias y límites de aplicación.
2. Diseño de protocolo de etiquetado de mercancías por expertos.
3. Inventario y clasificación de datos disponibles (sin publicar registros).
4. Abrir issues de investigación y definir criterios de aceptación.

**Fuente de verdad:** acuerdos aprobados en ADR, estado versionado, issues y PR. El contexto de chat no equivale a una decisión formal.