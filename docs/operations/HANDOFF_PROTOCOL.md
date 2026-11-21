# Protocolo de continuidad y traspaso entre IA

**Principio:** la tarea no reside en el historial de ChatGPT, Codex o Claude. Reside en el **issue, rama, commit SHA, PR, decisiones ADR, registros de interacciones y handoff versionado**.

## Antes de iniciar una sesión
1. Usar el primer prompt del rol en `prompts/`.
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