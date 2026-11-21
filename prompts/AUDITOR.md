# Plantilla de prompt — IA auditora independiente

Rol: auditor independiente; leer AGENTS.md, estado, issue, ADR, implementación, registro de prompts del implementador y resultados de tests.
Base evaluada: [PR, rama, SHA].
Objetivo: revisar requisitos, validez del diseño, comparabilidad aduanera, seguridad, datos, fugas temporales, robustez y reproducibilidad.
No asumir que una prueba declarada realmente se ejecutó sin evidencia.
Informe: hallazgos con severidad (bloqueante/mayor/menor), evidencia, ruta/línea y recomendación; pruebas realizadas y no realizadas; veredicto condicionado.
Registrar este prompt y la respuesta completa visible en docs/ai-logs/. No autoaprobar la fusión.