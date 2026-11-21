# Índice de solicitudes entre IA

**Fuente de navegación de prompts de tarea, no reemplaza GitHub Issues/PR.** Al comenzar, cada agente consulta su bandeja `prompts/inbox/<rol>/`, este índice y la rama+SHA real. Ver [protocolo](../docs/operations/ROUTING_PROTOCOL.md).

| ID | De → Para | Issue / PR | Estado | Prompt de tarea | Respuesta verificada | Observación |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Sin solicitudes operativas registradas todavía. |

**Estados:** PROPOSED, READY, IN_PROGRESS, ANSWERED, BLOCKED, CANCELLED. Las tareas **PROPOSED** requieren autorización; ni el auditor ni el ejecutor se autoaprueban. No crear solicitudes de prueba en las bandejas operativas: utilizar `prompts/examples/`.

**Al crear un prompt:** usar `prompts/TASK_TEMPLATE.md` y colocarlo en `prompts/inbox/coordinator/`, `prompts/inbox/developer/` o `prompts/inbox/auditor/`. Al responder, la IA deja la respuesta completa en `docs/ai-logs/` y reemplaza la fila del índice con enlace verificable. Si el trabajo requiere a otra IA, crear un **nuevo prompt** dirigido a su bandeja.
