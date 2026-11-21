# Inicio de agentes por ruta y respuestas fuera del chat

**No copiar los prompts al chat.** Basta compartir la URL/ruta del archivo de rol. La IA debe abrirlo, leer las instrucciones y verificar su SHA antes de ejecutar cualquier tarea.

| Rol | Prompt de arranque | Uso |
|---|---|---|
| Coordinación | [COORDINATOR.md](COORDINATOR.md) | Estado, acuerdos, asignaciones |
| Desarrollo (Codex, Claude Code u otro) | [DEVELOPER.md](DEVELOPER.md) | Código, pruebas y PR |
| Auditoría | [AUDITOR.md](AUDITOR.md) | Revisión independiente |

## Ejemplos de mensajes mínimos

- `Lee y ejecuta https://github.com/elVladdi/SIVEP_Inteligente/blob/main/prompts/COORDINATOR.md. Modo INICIO.`
- `Lee y ejecuta https://github.com/elVladdi/SIVEP_Inteligente/blob/main/prompts/DEVELOPER.md. Modo CONTINUACIÓN; issue #N.`
- `Lee y ejecuta https://github.com/elVladdi/SIVEP_Inteligente/blob/main/prompts/AUDITOR.md. Audita PR #N.`

**Hasta fusionar el PR #4**, utiliza la rama `docs/agent-bootstrap-and-handoffs` en lugar de `main`.

**Salida por defecto:** cada IA deja el prompt recibido (incluida ruta/URL), la versión SHA del prompt de rol consultado y su **respuesta sustantiva completa** en `docs/ai-logs/YYYY-MM-DD/<id-unico>.md`. Tras comprobar que el archivo está publicado, en el chat devuelve **solo la URL verificada** a `#respuesta-completa-visible`. El usuario puede pedir explícitamente otra forma de respuesta. Si no hay permisos de escritura, informar sin inventar enlaces.

Consulta [OUTPUT_PROTOCOL.md](../docs/operations/OUTPUT_PROTOCOL.md), [SESSION_CONTINUITY.md](../docs/operations/SESSION_CONTINUITY.md) y [AGENTS.md](../AGENTS.md). El acceso al repo, issues, PR, checkpoints y ADR permite continuar un chat en otro modelo sin depender de memoria anterior. Nunca publicar datos sensibles en este repositorio público.

## Intercambio de solicitudes entre roles
No confundir el **prompt permanente de rol** con un **prompt de tarea**. Para cada solicitud de una IA a otra, guardar un archivo en `prompts/inbox/coordinator/`, `prompts/inbox/developer/` o `prompts/inbox/auditor/` según destinatario, y registrarlo en `prompts/ROUTING_INDEX.md`. La IA destinataria lee su buzón y responde con archivo completo en `docs/ai-logs/`; el índice enlaza solicitud/respuesta. **Cualquier par de roles** puede intercambiar solicitudes dentro de la autorización vigente. Consulte [ROUTING_PROTOCOL.md](../docs/operations/ROUTING_PROTOCOL.md) y [TASK_TEMPLATE.md](TASK_TEMPLATE.md).
