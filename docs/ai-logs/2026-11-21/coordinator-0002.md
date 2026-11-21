# Interacción coordinator-0002 — arranque universal de agentes

- Fecha UTC: 2026-11-21 (hora exacta no conservada en esta transcripción)
- Función: coordinator
- Proveedor: OpenAI
- Modelo: GPT-6
- Tarea: definición de prompts de primer contacto y handoffs
- Issue vinculado: #3 (trazabilidad multi-plataforma)
- PR vinculado: https://github.com/elVladdi/SIVEP_Inteligente/pull/4
- Rama: docs/agent-bootstrap-and-handoffs
- SHA de entrega previo al registro: c0b2dd7aa2fd9a4ee0cf9b0a0d39270e3cb5df00
- Clasificación: PUBLICABLE
- Registrado por: IA coordinadora
- Nota: texto completo del mensaje de usuario y de la respuesta pública visible. No incluye mensajes internos de herramientas ni razonamiento interno.

## Prompt del usuario

````text
Listo, debes crear las instrucciones iniciales parar cada agente IA (Coordinación, desarrollo, auditoría) para que desde cualquier modelo de IA lea eso como primer prompt y sepa su papel y desde donde debe tomar el papel. Por ejemplo, puedo estar trabajando con CODEX como IA de desarrollo, pero por alguna decisión cambio Claude Code, entonces debe ser capaz de leer el prompt que le asigna el rol, conocer sobre lo que se está trabajando y en qué punto de desarrollo está el proyecto.
````

## Respuesta completa visible (mensajes parciales + respuesta final)

````markdown
He creado los **tres prompts universales de inicio** en una rama de trabajo del repositorio `SIVEP_Inteligente`. Están diseñados para que el rol de cada IA sea independiente del modelo o proveedor utilizado.

| Agente | Instrucciones de inicio | Función |
|---|---|---|
| **IA coordinadora** | [COORDINATOR.md](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/COORDINATOR.md) | Recuperar el estado del proyecto, coordinar tareas y preparar instrucciones para otras IA. |
| **IA desarrolladora** | [DEVELOPER.md](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/DEVELOPER.md) | Retomar una implementación, inspeccionar el código existente, ejecutar pruebas y continuar el desarrollo. |
| **IA auditora** | [AUDITOR.md](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/AUDITOR.md) | Examinar independientemente los cambios, las pruebas, la metodología y sus resultados. |

**Cómo se utilizarán:** al iniciar una conversación en ChatGPT, Codex, Claude Code u otra IA, se copiará el contenido completo del archivo correspondiente como primer prompt. El agente deberá consultar GitHub para reconstruir el estado vigente, en vez de depender de la memoria de conversaciones anteriores.

También incorporé un [protocolo de continuidad](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/operations/HANDOFF_PROTOCOL.md) y una plantilla de traspaso por tarea. Así, si se reemplaza Codex por Claude Code, el nuevo agente podrá identificar el último commit, la tarea en desarrollo, las pruebas realizadas y lo que falta implementar.

**Estado en GitHub:** los cambios están publicados en el [pull request #4](https://github.com/elVladdi/SIVEP_Inteligente/pull/4), pendientes de auditoría independiente y tu aprobación antes de incorporarlos a `main`. Los tres prompts ya pueden utilizarse desde la rama propuesta.

También adapté `CLAUDE.md` para que Claude Code **no asuma automáticamente el papel de auditor**: podrá actuar como desarrollador cuando reciba el prompt correspondiente.

La solicitud y esta respuesta quedaron incluidas en el [registro de interacción](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/ai-logs/2026-11-21/coordinator-0002.md), vinculado al PR.
````

## Artefactos
- prompts/COORDINATOR.md
- prompts/DEVELOPER.md
- prompts/AUDITOR.md
- prompts/README.md
- docs/operations/ACTIVE_WORK.md
- docs/operations/HANDOFF_PROTOCOL.md
- docs/operations/handoffs/TEMPLATE.md
- CLAUDE.md
- README.md, AGENTS.md, PROJECT_STATE.md, docs/operations/WORKFLOW.md y docs/ai-logs/README.md
- Revisión y aprobación humana: pendiente.
