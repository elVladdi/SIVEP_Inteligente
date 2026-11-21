# Interacción coordinator-0001 — adopción de trazabilidad IA

- Fecha UTC: 2026-11-21 (hora exacta no registrada)
- Rol: coordinator
- Proveedor: OpenAI
- Modelo: GPT-6
- Issue/tarea: #3
- Commit base: 90494c14eab90d75675a9a135f91ae12146fe4cd
- Registrado por: IA coordinadora
- Interacción anterior: primera aplicación de la nueva política
- Clasificación: PUBLIC
- Fuente: conversación del proyecto en ChatGPT
- Integridad: mensaje visible de usuario y respuesta final; no contiene razonamiento interno ni instrucciones ocultas.

## Prompt completo

````text
Listo, también todo prompt y respuesta de prompt de cualquiera de las tres IA que estamos estableciendo, debe quedar documentada en el repositorio.
````

## Respuesta completa visible

````text
De acuerdo. Queda establecido como requisito del proyecto: **toda interacción con cualquiera de las tres IA —coordinadora, desarrolladora o auditora— debe tener trazabilidad documental**, incluyendo las instrucciones enviadas, las respuestas recibidas y las iteraciones de corrección.

Ya incorporé esta decisión en el repositorio [SIVEP_Inteligente](https://github.com/elVladdi/SIVEP_Inteligente), en los archivos `AGENTS.md`, `PROJECT_STATE.md` y [ADR-0003 — Trabajo multiagente y trazabilidad completa](https://github.com/elVladdi/SIVEP_Inteligente/blob/main/docs/decisions/ADR-0003-AI-TRACEABILITY.md).

## 1. Qué registraremos

Cada intercambio tendrá los siguientes datos:

| Campo | Contenido |
|---|---|
| Identificación | ID único y fecha de ejecución |
| Responsable | IA utilizada, función y modelo, cuando se conozca |
| Contexto | Tarea, issue, rama y versión del código |
| Prompt | Instrucción completa enviada a la IA |
| Respuesta | Resultado completo visible de la IA |
| Implementación | Archivos modificados, pruebas y commits |
| Auditoría | Observaciones, correcciones y estado de aprobación |

No registraremos únicamente el último prompt exitoso. También conservaremos las instrucciones intermedias, los errores, las respuestas rechazadas y las correcciones, porque permiten reconstruir cómo evolucionó una solución.

**Límite de confidencialidad:** los intercambios publicables se guardarán íntegramente en GitHub; cuando contengan información restringida, el repositorio público conservará su registro de trazabilidad y el original deberá custodiarse en un entorno institucional autorizado.

## 2. Implementación disponible

He incorporado un [registrador de interacciones](https://github.com/elVladdi/SIVEP_Inteligente/blob/main/scripts/record_ai_interaction.py), una [guía para documentar prompts y respuestas](https://github.com/elVladdi/SIVEP_Inteligente/blob/main/docs/ai-logs/README.md) y las plantillas de trabajo para cada IA. Cada registro puede enlazarse con el issue, el commit y la auditoría correspondiente.

También quedaron abiertas tres tareas:

- [#1: Revisión bibliográfica y normativa](https://github.com/elVladdi/SIVEP_Inteligente/issues/1).
- [#2: Inventario de campos y calidad de SIVEP](https://github.com/elVladdi/SIVEP_Inteligente/issues/2).
- [#3: Integración del registro entre ChatGPT, Codex y Claude](https://github.com/elVladdi/SIVEP_Inteligente/issues/3).

Las [pruebas automáticas](https://github.com/elVladdi/SIVEP_Inteligente/actions/runs/44919082073) del registrador finalizaron correctamente.

**Limitación actual:** las conversaciones en otros chats o plataformas todavía no se capturan automáticamente. Hasta implementar esa integración, cada IA o colaborador deberá incorporar el texto visible del prompt y su respuesta mediante el registrador. Esta interacción es el primer registro de aplicación de la nueva regla.
````

## Artefactos y pruebas
- Política: docs/decisions/ADR-0003-AI-TRACEABILITY.md
- Implementación: scripts/record_ai_interaction.py
- CI: https://github.com/elVladdi/SIVEP_Inteligente/actions/runs/44919082073 (success)
- Issues relacionados: #1, #2 y #3.
- El registro no implica captura automática de otras sesiones.
