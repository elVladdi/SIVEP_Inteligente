# ADR-0005 — Continuidad de sesiones de IA mediante checkpoints

- Estado: **Aceptada**
- Fecha: 2026-11-21
- Aprobación: responsable humano, respuesta explícita «Aprobado» a propuesta de modos INICIO/CONTINUACIÓN y punto de control.
- Issue: #5

## Contexto
Los chats de IA pueden alcanzar límites de contexto; los proveedores y modelos pueden cambiar. La sola existencia de prompts de rol no garantiza la recuperación exacta de criterios y pasos no documentados.

## Decisión
1. En **cada nuevo chat** el agente determina modo **INICIO** o **CONTINUACIÓN**; en continuación valida el último punto de control de la sesión/tarea y el estado real de GitHub.
2. Persistir checkpoints versionados por sesión/hito que conserven objetivos, acuerdos **aprobados**, justificaciones explícitas, alternativas consideradas, resultados, pruebas, bloqueos, cambios y siguiente acción exacta.
3. Un índice de sesiones apunta a los últimos checkpoints y enlaza issues/PR. Los ADR conservan decisiones, los logs conservan prompts/respuestas completos visibles y los handoffs transfieren la implementación por issue.
4. Guardar puntos de control después de hitos y decisiones relevantes, y antes de terminar o cambiar de chat si es posible; no prometer guardado automático ni recuperación de texto perdido.
5. Ante conflicto, verificar SHA/PR/issue; cambiar acuerdos solo mediante nueva decisión documentada y aprobación humana.
6. Proteger información institucional: repositorio público, sin datos reales de SIVEP/DAM o contenido restringido.

## Consecuencias
Continúa en el mismo modelo o distinto proveedor con las mismas fuentes versionadas, aunque el chat previo no esté disponible. La fidelidad depende de la calidad y actualidad de registros; las interrupciones inesperadas pueden producir pérdida parcial no recuperable.

## Aclaración de alcance (ADR-0008)
Este ADR define el funcionamiento de **agentes formalmente activados**; no transforma retrospectivamente conversaciones de configuración en sesiones operativas. En configuración el asistente responde en el chat, sin la obligación de enviar solo un enlace o registrar cada turno como respuesta de agente. La activación exige orden humana expresa de leer y **ejecutar** el rol.
