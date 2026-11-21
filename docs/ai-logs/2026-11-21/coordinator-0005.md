# Interacción coordinator-0005 — inicio por ruta y respuesta externa

> **RECTIFICACIÓN RETROSPECTIVA (ADR-0008, 2026-11-21).** Este archivo con nombre histórico coordinator-0005.md se creó **durante la CONFIGURACIÓN del proyecto**, antes de activar formalmente ninguna IA. **NO** es respuesta de una IA Coordinadora operativa, ni debe usarse para reanudar una sesión de agente. Algunos textos pueden ser reconstrucciones y no constituyen transcripciones literales verificadas. Se conserva la ruta para preservar enlaces y trazabilidad; ver docs/project-setup/README.md.


- Fecha: 2026-11-21 (hora UTC exacta no conservada)
- Etiqueta histórica (incorrecta): Coordinación; proveedor OpenAI; modelo GPT-6; clasificación válida: CONFIGURACIÓN, sin rol de agente activado
- Issue: #6
- PR: #4; rama docs/agent-bootstrap-and-handoffs
- Archivo de rol consultado para esta implementación: `prompts/COORDINATOR.md` en la versión base `2e05d90109b722974e06b51e553507cb6dd5457f` (consulta verificada).
- Entrada de este turno: instrucción directa del usuario en el chat actual; no fue una invocación mediante ruta.
- Seguridad: solo contenido publicable

## Prompt completo

```text
para que quede claro, los promps no se copiaran en los chats nuevos solo se dará la ruta donde debe leer el prompts y prompts. Igualmente la IA debe saber dónde dejar la respuesta. En el chat, a menos que le diga lo contario, solo debe responder la ubicación de la respuesta completa.
```

## Respuesta completa visible

# Entrada por ruta y respuesta completa en el repositorio

He incorporado tu instrucción como **ADR-0006 — Entrada por ruta y respuesta fuera del chat** en el repositorio SIVEP Inteligente. La implementación está documentada en el [issue #6](https://github.com/elVladdi/SIVEP_Inteligente/issues/6) y forma parte del [PR #4](https://github.com/elVladdi/SIVEP_Inteligente/pull/4), todavía pendiente de revisión y fusión a `main`.

**Reglas aprobadas:**

1. **No se copia el prompt al chat.** Al iniciar cualquier agente, el usuario indica solamente la ruta/URL de `prompts/COORDINATOR.md`, `prompts/DEVELOPER.md` o `prompts/AUDITOR.md`, con modo INICIO/CONTINUACIÓN o issue cuando corresponda. La IA debe leer el archivo directamente y verificar la versión SHA.
2. **Cada respuesta completa se guarda en el repositorio:** un archivo Markdown por interacción en `docs/ai-logs/YYYY-MM-DD/<id-unico>.md`. Allí se registran el prompt recibido, la ruta+SHA de las instrucciones de rol y la respuesta sustantiva íntegra, con referencias a pruebas, código y decisiones.
3. **El chat solo mostrará la ubicación de la respuesta completa:** una vez publicada y verificada en GitHub, la IA responde únicamente con el enlace al registro, sin resumen ni reproducción del texto. Si pides expresamente otra forma de respuesta, se seguirá esa indicación y se mantendrá el registro.
4. **Continuidad:** al abrir otro chat del mismo modelo o cambiar de IA, basta dar la ruta del prompt de rol. Los checkpoints, ADR, issues y PR conservan el estado y las decisiones aprobadas.

Un ejemplo de inicio, después de fusionar el PR a `main`, sería: `Lee y sigue https://github.com/elVladdi/SIVEP_Inteligente/blob/main/prompts/DEVELOPER.md. Modo CONTINUACIÓN; issue #N.` Mientras el PR siga abierto, usar su rama `docs/agent-bootstrap-and-handoffs`.

**Documentos:** [guía de inicio por ruta](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/prompts/README.md), [protocolo de entrada/salida](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/operations/OUTPUT_PROTOCOL.md), [política de bitácora](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/ai-logs/README.md) y [ADR-0006](https://github.com/elVladdi/SIVEP_Inteligente/blob/docs/agent-bootstrap-and-handoffs/docs/decisions/ADR-0006-PATH-ONLY-IO.md).

**Limitación:** no se puede garantizar publicación si la IA no tiene permisos GitHub, ni capturar automáticamente conversaciones de otras plataformas sin integración. Los contenidos restringidos de SIVEP no se publican en el repositorio público; en tales casos se informa el impedimento o se usa almacenamiento autorizado. La auditoría independiente y fusión de PR #4 siguen pendientes.


## Nota sobre el mensaje breve de chat

El chat solo comunica el enlace verificado a la sección anterior; la respuesta íntegra es la que aparece en este documento.
