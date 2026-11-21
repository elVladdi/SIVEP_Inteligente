# Interacción coordinator-0006 — enrutamiento bidireccional entre agentes

> **RECTIFICACIÓN RETROSPECTIVA (ADR-0008, 2026-11-21).** Este archivo con nombre histórico coordinator-0006.md se creó **durante la CONFIGURACIÓN del proyecto**, antes de activar formalmente ninguna IA. **NO** es respuesta de una IA Coordinadora operativa, ni debe usarse para reanudar una sesión de agente. Algunos textos pueden ser reconstrucciones y no constituyen transcripciones literales verificadas. Se conserva la ruta para preservar enlaces y trazabilidad; ver docs/project-setup/README.md.


- Fecha: 2026-11-21 (hora UTC exacta no conservada)
- Etiqueta histórica (incorrecta): coordinator; proveedor OpenAI; modelo GPT-6; clasificación válida: CONFIGURACIÓN, sin rol de agente activado
- Issue: #7
- PR: #4; rama `docs/agent-bootstrap-and-handoffs`
- Prompt de rol referenciado: `prompts/COORDINATOR.md` (versión de la rama de publicación; el mensaje del usuario fue la instrucción directa, no una activación desde ruta)
- Seguridad: PUBLICABLE
- Estado: documentación entregada, revisión independiente pendiente

## Prompt completo

```text
Igual para la IA de Coordinación con quien trabajaré más directamente, así como lo hago contigo, le diré que deje los prompts donde corresponde para la IA que corresponde. Pero, de igual forma si la IA de auditoría cree que la de coordinación debe hacer algo adicional, esta debe crear el prompt para que la IA de coordinación lo lea. Todas la IAs deben saber de donde leer prompts, donde dejar las respuestas de esos prompts y dónde dejar prompts para otras IA, correcto ?
```

## Respuesta completa visible

# Protocolo bidireccional de trabajo entre las tres IA

**Correcto.** El sistema de SIVEP Inteligente debe permitir que **Coordinación, Desarrollo y Auditoría intercambien prompts de tarea en todas las direcciones**. La Coordinación no será el único agente autorizado para solicitar trabajo: por ejemplo, si Auditoría detecta una deficiencia que debe resolver Coordinación, deja una solicitud completa en el buzón de Coordinación. Lo mismo aplica a Desarrollo cuando requiera una aclaración o una nueva revisión.

El funcionamiento queda organizado en **cuatro ubicaciones distintas**:

| Función | Ruta del repositorio |
|---|---|
| Instrucciones permanentes de cada rol | `prompts/COORDINATOR.md`, `prompts/DEVELOPER.md`, `prompts/AUDITOR.md` |
| Prompts que una IA deja para otra | `prompts/inbox/coordinator/`, `prompts/inbox/developer/`, `prompts/inbox/auditor/` |
| Índice de encargos, estados y vínculos | `prompts/ROUTING_INDEX.md` |
| Respuestas completas de las IA | `docs/ai-logs/YYYY-MM-DD/<id-unico>.md` |

Cada agente debe **leer su prompt permanente de rol**, consultar el índice y su buzón, verificar la tarea asignada, ejecutar el trabajo autorizado y dejar la respuesta íntegra en la bitácora. Si la respuesta implica una nueva actuación de otro agente, deberá **crear un nuevo archivo de prompt en el buzón correspondiente** y actualizar el índice; no basta con escribir la solicitud dentro de la respuesta o en el chat.

## Ejemplo de interacción recíproca

1. La IA coordinadora solicita a Desarrollo implementar una búsqueda de mercancías comparables.
2. Desarrollo publica código, pruebas y su respuesta completa; solicita auditoría mediante un prompt en `prompts/inbox/auditor/`.
3. Auditoría revisa la solución. Si identifica que falta definir un criterio metodológico, crea un prompt en `prompts/inbox/coordinator/` explicando el hallazgo y la decisión pendiente.
4. Coordinación analiza el requerimiento y, si el criterio necesita aprobación, prepara la propuesta para el responsable humano.
5. Una vez autorizado, Coordinación genera una nueva tarea para Desarrollo y, posteriormente, solicita otra auditoría.

**Regla de gobierno:** cualquier IA puede pedir acciones a otra, pero crear un prompt **no equivale a aprobarlo ni a ejecutarlo automáticamente**. Los encargos fuera del alcance autorizado quedan como `PROPOSED` hasta obtener aprobación. Cada agente debe poder verificar si está `READY`, `IN_PROGRESS`, `ANSWERED` o bloqueado. Auditoría no puede autorizar unilateralmente cambios de alcance ni aprobar su propio trabajo.

Esta decisión se documentó en [ADR-0007](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/decisions/ADR-0007-AGENT-ROUTING.md), [protocolo de enrutamiento](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/operations/ROUTING_PROTOCOL.md), [plantilla de tarea](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/TASK_TEMPLATE.md) e [índice de solicitudes](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/ROUTING_INDEX.md). También actualicé los tres prompts iniciales y sus instrucciones comunes en el [PR #4](https://github.com/elVladdi/SIVEP_Inteligente/pull/4), ligado al [issue #7](https://github.com/elVladdi/SIVEP_Inteligente/issues/7).

**Estado actual:** documentación implementada en rama de trabajo. Falta auditoría independiente y revisión humana antes de fusionar a `main`. Los agentes **no se activan entre sí automáticamente** por dejar un archivo; el responsable tendrá que iniciar la IA destinataria o, más adelante, incorporar una automatización autorizada. El repositorio público solo contiene documentos aptos para publicación.

## Artefactos
- `docs/decisions/ADR-0007-AGENT-ROUTING.md`
- `docs/operations/ROUTING_PROTOCOL.md`
- `prompts/ROUTING_INDEX.md`
- `prompts/TASK_TEMPLATE.md`
- `prompts/inbox/` para cada rol
- `prompts/examples/auditor-to-coordinator-DEMO.md`
- `docs/operations/checkpoints/2026-11-21/coord-20261121-001-CP03.md`
