# Protocolo de continuidad y traspaso entre IA

**Aplicación solo a roles activados formalmente** (ADR-0008). La CONFIGURACIÓN del sistema no es un handoff entre agentes y se responde normalmente en chat.

**Principio:** la tarea no reside en el historial de ChatGPT, Codex o Claude. Reside en el **issue, rama, commit SHA, PR, decisiones ADR, registros de interacciones y handoff versionado**.

## Antes de iniciar una sesión
1. Dar la ruta/URL del primer prompt del rol en `prompts/`; la IA debe abrirlo y verificarlo.
2. Leer AGENTS.md, PROJECT_STATE.md, ACTIVE_WORK.md y ADR pertinentes.
3. Verificar en GitHub el SHA de `main`, issue/PR concreto y último commit de la rama.
4. Leer `docs/operations/handoffs/ISSUE-<numero>.md`, si existe, y contrastarlo con la actividad real. Si está desactualizado, anotarlo.
5. Presentar contexto resumido y el siguiente paso antes de editar, coordinar o auditar.

## Antes de terminar o sustituir al agente
1. Registrar **cada prompt y respuesta completa visible** (incluido el prompt inicial, reintentos y correcciones) en `docs/ai-logs/` según su política.
2. Crear o actualizar `docs/operations/handoffs/ISSUE-<numero>.md` usando TEMPLATE.md. Incluir: tarea, estado, rama, SHA/PR, archivos, pruebas ejecutadas/resultados, pendientes, bloqueos, ADR y logs.
3. Actualizar `docs/operations/ACTIVE_WORK.md` para apuntar al issue, rama/PR y handoff; enlazarlo al PR.
4. La nueva IA lee esos archivos y **verifica los hechos** antes de continuar. No es necesario copiar la conversación anterior, pero sus interacciones publicables siguen conservadas en los logs.
5. Ningún handoff equivale a revisión independiente ni aprobación humana.

## Datos restringidos y ausencia de acceso
En un repo público no escribir datos reales SIVEP/DAM ni secretos. Para una conversación restringida, GitHub contiene solo metadatos y referencia a custodia institucional autorizada. Si el nuevo agente no puede consultar GitHub, suministrar el paquete mínimo (AGENTS, PROJECT_STATE, ACTIVE_WORK, ADR, issue/PR/diff, handoff y archivos necesarios) y marcar lo no verificado.

## Conflictos
Prevalecen decisiones humanas aprobadas y ADR aplicables para criterios, mientras que el **estado técnico actual** se verifica por commits, PR e issues. La discrepancia exige investigación, no suposición ni modificación silenciosa.
## Continuación en un nuevo chat del mismo modelo y proyecto
El procedimiento es el mismo que al cambiar de herramienta: indicar la **ruta del mismo prompt de rol** en el chat nuevo, usar **CONTINUACIÓN**, leer `docs/operations/SESSION_INDEX.md` y el checkpoint pertinente, cotejar con issue/PR/ADR/commit y seguir la acción pendiente. El handoff se crea **por issue**, el checkpoint **por sesión/hito**, y los logs conservan los turnos completos visibles. Véase `docs/operations/SESSION_CONTINUITY.md`.

## Respuesta de traspaso
En cada nuevo chat, el agente guarda prompt y respuesta completos en `docs/ai-logs/` y responde **solo con el enlace verificado** a la respuesta, salvo petición expresa. Véase `docs/operations/OUTPUT_PROTOCOL.md`.

## Solicitudes interagente al transferir una tarea
Antes del cambio de sesión, comprobar `prompts/ROUTING_INDEX.md`, enlazar prompts pendientes del buzón propio, respuestas existentes y nuevas solicitudes emitidas a otro rol; incluir las rutas en el handoff. No interpretar una solicitud depositada como ejecutada sin el estado ANSWERED y referencia verificable del resultado. Ver `docs/operations/ROUTING_PROTOCOL.md`.
