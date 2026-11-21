# Flujo de trabajo supervisado y documentado

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
