# Uso de Claude y Claude Code en SIVEP Inteligente

**Durante CONFIGURACIÓN no asumir rol operativo:** revisar o editar este documento no activa a Claude como IA Auditora/Desarrolladora. El responsable debe ordenar explícitamente la activación del rol y ejecución del prompt. Responder directamente en chat durante la configuración. Ver ADR-0008.

**Este archivo NO asigna automáticamente el rol de auditor.** Claude/Claude Code pueden actuar como IA desarrolladora o auditora, según el primer prompt y la asignación expresos del responsable.

1. Obtener **la ruta/URL** del prompt del rol, no su copia en el chat. Leer `AGENTS.md`, `PROJECT_STATE.md`, `docs/operations/ACTIVE_WORK.md`, ADR y `docs/operations/HANDOFF_PROTOCOL.md`.
2. Si el rol indicado es **desarrollo**, aplicar íntegramente `prompts/DEVELOPER.md`; si es **auditoría**, aplicar `prompts/AUDITOR.md`; si es **coordinación**, aplicar `prompts/COORDINATOR.md`.
3. Si no hay rol ni issue explícitos, informar lo que se verificó y solicitar la asignación antes de modificar o aprobar código.
4. Publicar respuesta sustantiva íntegra junto al prompt recibido en `docs/ai-logs/`; en el chat **solo enlazar la respuesta verificada**, salvo indicación contraria. Ver `docs/operations/OUTPUT_PROTOCOL.md`.
5. Mantener la confidencialidad y registrar todos los prompts y respuestas visibles conforme a `docs/ai-logs/README.md`.

**La plataforma no determina el rol; los requisitos, la fase y la tarea activa se obtienen del repositorio.**
