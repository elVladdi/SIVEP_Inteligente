# Flujo de trabajo supervisado y documentado

**Ámbito:** la coordinación multiagente y las obligaciones por turno de este documento solo rigen después de la **activación expresa de un rol**, según docs/operations/ACTIVATION_PROTOCOL.md (ADR-0008). En CONFIGURACIÓN el asistente responde en chat y puede editar GitHub, sin constituirse en IA Coordinadora.

## Participantes
- **Responsable humano:** aprueba objetivos, decisiones, resultados y autorización para compartir información.
- **IA coordinadora:** traduce requerimientos en tareas, genera prompts versionados, identifica bloqueos, consolida hallazgos; mantiene PROJECT_STATE.md y ADR.
- **IA desarrolladora:** implementa en rama acotada, prueba y propone cambios por PR.
- **IA auditora:** verifica de forma independiente diseño, pruebas, seguridad, resultados y trazabilidad.
- **Colaboradores humanos:** investigación, código, revisión y etiquetado experto autorizado.

## Ciclo obligatorio
1. Issue con propósito, entradas, salidas, restricciones, criterios y versión base.
2. Prompt del coordinador al desarrollador, registrado.
3. Respuesta del desarrollador y cada iteración, registradas.
4. Revisión por auditor con prompt y respuesta completos, registrados.
5. Correcciones, pruebas y registro de cada intercambio adicional.
6. Revisión humana, ADR si se adopta decisión, actualización de estado y cierre de issue.

## Trazabilidad de una respuesta
Cada respuesta pertenece a un registro de docs/ai-logs/ con identificador, rol, proveedor, modelo si consta, fecha, issue, versión base, prompt, respuesta, artefactos y clasificación de confidencialidad. Los pasos de otros chats no se importan automáticamente: requieren exportación o registro por el agente con acceso al repo.

## Puertas de calidad
Sin fusión si faltan pruebas, falta auditoría exigida, existe fuga de datos, los experimentos no son reproducibles o no están registradas las interacciones IA relevantes. El auditor no sustituye la aprobación humana.
## Arranque y sustitución de agente
El primer prompt de cada función está en `prompts/` y es independiente del proveedor. Todo nuevo agente reconstruye el contexto de `PROJECT_STATE.md`, `ACTIVE_WORK.md`, ADR, issue/PR y último handoff. El agente saliente debe registrar pruebas, SHA, pendientes y las rutas de las conversaciones; véase `docs/operations/HANDOFF_PROTOCOL.md`. Los handoffs no sustituyen la auditoría ni aprobación humana.

## Continuidad al agotar el contexto de un chat
Todo agente usa INICIO o CONTINUACIÓN, revisa `docs/operations/SESSION_INDEX.md` y guarda puntos de control al completar hitos, decisiones o antes de un relevo, conforme a `docs/operations/SESSION_CONTINUITY.md`. Un mismo modelo en un chat nuevo **no cuenta con acceso garantizado al texto no registrado**. Los checkpoints documentan estado, los logs documentan las conversaciones y los ADR conservan acuerdos aprobados.

## Entrada por ruta y salida documental
El usuario da la URL/ruta del prompt, sin copiar su contenido. El agente lo lee, verifica SHA, ejecuta la tarea y deposita su respuesta íntegra y prompt recibido en `docs/ai-logs/`. En el chat muestra **solo el enlace publicado** al contenido completo, salvo pedido contrario. Protocolo: `docs/operations/OUTPUT_PROTOCOL.md` y ADR-0006.

## Flujo de solicitudes recíprocas entre roles
La Coordinación puede pedir implementación o auditoría; Desarrollo puede pedir aclaraciones o revisión; Auditoría puede solicitar correcciones al desarrollador **o acciones adicionales a Coordinación**. La IA emisora guarda el prompt completo en `prompts/inbox/<destinatario>/`, lo indexa en `prompts/ROUTING_INDEX.md` con estado y issue y no asume ejecución automática. La IA receptora verifica permisos y estado READY, responde íntegramente en `docs/ai-logs/` y actualiza el índice. Si el auditor identifica un cambio de alcance o de decisión aprobada, solo propone la acción para validación humana; no se autoautoriza. Ver `docs/operations/ROUTING_PROTOCOL.md` y ADR-0007.
