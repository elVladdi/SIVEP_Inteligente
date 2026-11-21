# ADR-0008 — Configuración no equivale a activación operativa

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-21
- **Origen:** corrección explícita del responsable («No eres la IA coordinadora aún») y solicitud «Corrige el GIT».
- **Issue:** #8
- **PR:** #4 (pendiente de auditoría y fusión)

## Problema
Durante el diseño del proyecto se aplicaron prematuramente las reglas destinadas a la IA Coordinadora formal: respuestas fuera del chat, logs etiquetados como IA Coordinadora y checkpoints de supuestas sesiones operativas.

## Decisión
1. **CONFIGURACIÓN** es el estado predeterminado mientras se debaten, editan y corrigen las especificaciones. Aquí se **responde en el chat**, salvo pedido contrario. Los cambios relevantes sí pueden documentarse en GitHub con issues, PR y ADR.
2. **OPERACIÓN** se inicia únicamente mediante una instrucción humana expresa de **activar un rol, leer y ejecutar su prompt**. Compartir o consultar una ruta no basta.
3. Solo después de la activación aplican la respuesta externa predeterminada, la bitácora por interacción y checkpoints operativos; la instrucción directa del responsable prevalece sobre el formato de respuesta.
4. Reclasificar los registros coordinator-0001 a coordinator-0006 y checkpoints históricos CP01..CP03 como **documentación de configuración previa a la activación**; conservar el historial sin presentarlo como sesión formal ni transcripción necesariamente literal.
5. El índice de sesiones operativas permanece **vacío** hasta una activación formal real. La primera activación recibe ID nuevo y CP01. La desactivación puede solicitarse expresamente.

## Consecuencias
ADR-0005/0006/0007 siguen vigentes, pero **su operación presupone activación expresa**. Las conversaciones de diseño no reciben automáticamente el tratamiento operativo de una IA. Ver docs/operations/ACTIVATION_PROTOCOL.md.
