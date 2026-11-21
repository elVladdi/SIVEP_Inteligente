# ADR-0007 — Prompts recíprocos y bandejas por rol

- Estado: **Aceptada**
- Fecha: 2026-11-21
- Origen: instrucción del responsable: Coordinación, Desarrollo y Auditoría deben saber dónde leer y dejar prompts, dónde guardar sus respuestas, y cualquier IA puede solicitar acciones de otra, incluida Auditoría → Coordinación.
- Issue: #7; PR relacionado: #4

## Decisión
1. Mantener **prompts permanentes de rol** `prompts/{COORDINATOR,DEVELOPER,AUDITOR}.md` y **prompts de tarea** separados.
2. Cada solicitud entre IA se guarda íntegra en `prompts/inbox/<rol-destino>/REQ-YYYYMMDD-NNN.md`, según `prompts/TASK_TEMPLATE.md`, y se indexa con estado, autor, destinatario, issue, referencia de Git y ruta en `prompts/ROUTING_INDEX.md`.
3. Cada respuesta completa se guarda en `docs/ai-logs/YYYY-MM-DD/<id>.md`, vinculada al ID, ruta+SHA de solicitud y resultados; actualizar el índice **solo tras verificar publicación**.
4. Se permiten solicitudes en **todas las direcciones** entre roles: Coordinación ↔ Desarrollo, Coordinación ↔ Auditoría y Desarrollo ↔ Auditoría.
5. Una solicitud nueva fuera de alcance o que cambia un acuerdo requiere autorización: estado PROPOSED. Una solicitud ya cubierta por un issue/PR autorizado puede marcarse READY. Auditoría no puede autoaprobar sus hallazgos o decidir cambios de alcance unilateralmente.
6. El chat solo muestra el enlace a la respuesta completa por defecto (ADR-0006). Depositar una solicitud **no activa automáticamente** ninguna IA. Seguir `docs/operations/ROUTING_PROTOCOL.md`.

## Consecuencias
Los agentes pueden colaborar y pedir correcciones recíprocamente sin depender de la memoria de un chat; las responsabilidades y decisiones humanas conservan sus límites. El índice requiere mantenimiento verificable y permisos de GitHub. El repositorio público no almacena datos reales o restringidos de SIVEP/DAM.
