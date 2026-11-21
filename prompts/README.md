# Arranque universal para los tres roles de IA

**Cada archivo siguiente es el primer prompt completo que debes copiar al iniciar una sesión nueva**, independientemente del proveedor:

| Rol | Prompt | Función |
|---|---|---|
| Coordinadora | [COORDINATOR.md](COORDINATOR.md) | Reconstruye estado, coordina y delega |
| Desarrollo (Codex, Claude Code, otro) | [DEVELOPER.md](DEVELOPER.md) | Retoma issue/PR, implementa y prueba |
| Auditoría (Claude, otro) | [AUDITOR.md](AUDITOR.md) | Revisa independencia y evidencias |

**Uso:** (1) abrir una sesión de la IA elegida; (2) copiar el archivo completo como primer prompt o instrucciones de agente; (3) facilitar acceso autorizado al repositorio; (4) indicar el issue/PR si se conoce, sin depender de ello para saber el estado general; (5) registrar prompt y respuesta completos conforme a `docs/ai-logs/README.md`.

El contexto vigente se reconstruye consultando `PROJECT_STATE.md`, `docs/operations/ACTIVE_WORK.md`, ADR, issues, PR y `docs/operations/handoffs/ISSUE-<numero>.md`. **No hay un SHA fijo en los prompts:** la IA debe verificar GitHub en cada inicio. Sin acceso debe solicitar el paquete documental mínimo; nunca simular la lectura.

**Ejemplo de traspaso:** Codex termina un trabajo en el issue #N, entrega commit/PR y handoff. Claude Code comienza con exactamente `DEVELOPER.md`, comprueba el issue y el SHA, revisa el handoff y continúa solo lo pendiente. Los logs permiten auditar lo ocurrido antes y después.