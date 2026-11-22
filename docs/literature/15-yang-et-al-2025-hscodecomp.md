# Artículo 15 — Yang et al. (2025): HSCodeComp y aplicación de reglas jerárquicas por agentes

## Identificación bibliográfica

- **Autores:** Yiqian Yang, Tian Lan, Qianghuai Jia, Li Zhu, Hui Jiang, Hang Zhu, Longyue Wang, Weihua Luo y Kaifu Zhang.
- **Título:** *HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application*.
- **Afiliación:** Alibaba International Digital Commerce.
- **Versión examinada:** **arXiv:2510.19631v1**, 22 de octubre de 2025; manuscrito fechado 23 de octubre de 2025, **38 páginas**.
- **Fuente:** https://arxiv.org/abs/2510.19631
- **Recursos declarados:** https://github.com/AIDC-AI/Marco-Search-Agent y https://huggingface.co/datasets/AIDC-AI/HSCodeComp
- **Tipo de evidencia:** creación de un **benchmark** y evaluación de modelos y agentes. No desarrolla un recuperador de DAM históricas ni evalúa valores de transacción.
- **Localización:** secciones 3–6, Tablas 1–6, Figuras 1–6 y anexos F–I.

## 1. Problema y objetivo científico

Los agentes de búsqueda pueden consultar páginas, documentos y bases de datos, pero **encontrar información relevante no equivale a aplicar correctamente una regla compleja**. La clasificación arancelaria exige resolver condiciones, excepciones, notas, relaciones jerárquicas y casos en que la función del producto prevalece sobre su apariencia comercial.

Los autores estudian si sistemas LLM/VLM y agentes con acceso a búsqueda **predicen correctamente un código arancelario nacional completo de diez dígitos**, utilizando descripciones reales con ruido y reglas especializadas.

Su contribución es un **instrumento de evaluación** para aplicación de normas, no un método nuevo que produzca automáticamente referencias de valoración.

## 2. Naturaleza y construcción de HSCodeComp

El benchmark consta de **632 productos**, de **32 categorías comerciales de primer nivel** y **27 capítulos HS**. Los campos potenciales de cada entrada son:

```text
x = (título, atributos, categoría de e-commerce,
     imagen, precio, moneda, URL)
```

La salida es **un único código de diez dígitos**. Los primeros seis corresponden a la estructura HS internacional; los cuatro siguientes pertenecen al sistema nacional usado en el experimento, vinculado a referencias **estadounidenses**. **No** es exactitud sobre las subpartidas nacionales NANDINA de Perú.

### Etiquetado por especialistas

El artículo describe:

1. Dos especialistas examinan página y producto.
2. Extraen características técnicas estructuradas.
3. Buscan antecedentes en bases como **CBP CROSS**.
4. Aplican reglas y excepciones arancelarias si no hay precedentes pertinentes.
5. Verifican existencia del código en **eWTP**.
6. Si discrepan, interviene especialista sénior; ciertos casos irresolubles se excluyen.

Un cuarto especialista revisó **10 %** del corpus y se reporta **2 % de desacuerdo**. Es evidencia de consistencia de anotación, pero no de corrección legal universal. La muestra se construye con **control de redundancias** y diversidad; no se demuestra que represente la frecuencia real de mercancías de un servicio de aduanas.

## 3. Sistemas comparados

Se examinan tres grupos:
- **Modelos sin herramientas:** 14 modelos fundacionales y variantes multimodales, entre ellos GPT-5, GPT-4o, Gemini 2.5 Pro, Claude Sonnet 4, DeepSeek y Qwen.
- **Agentes de código abierto:** **SmolAgents**, AWorld, AgentOrchestra, OWL, WebSailor y Cognitive Kernel, normalmente con GPT-5 como motor.
- **Agentes comerciales:** Gemini Deep Research, Manus y Grok DeepSearch; por limitaciones de acceso, evaluados sobre **49 casos**.

Los agentes pueden consultar herramientas de búsqueda; algunos reciben imágenes. La evaluación final requiere un **solo código**, sin una alternativa formal de **abstención por evidencia insuficiente**.

## 4. Métrica: exactitud del código, no calidad de retrieval

Se mide coincidencia exacta con la etiqueta de especialista en **2, 4, 6, 8 y 10 dígitos**.

| Sistema/condición | Exactitud HS10 |
|---|---:|
| **SmolAgents (GPT-5 + visión)** | **46,83 %** |
| SmolAgents (GPT-5, solo texto) | 42,72 % |
| AWorld (GPT-5) | 41,30 % |
| AgentOrchestra (GPT-5) | 41,30 % |
| OWL (GPT-5) | 37,34 % |
| WebSailor (GPT-5) | 35,44 % |
| GPT-5 directo multimodal, sin herramientas | 29,27 % |
| GPT-5 directo textual, sin herramientas | 28,96 % |

El artículo reporta **95 % de exactitud humana**, pero **no documenta un protocolo plenamente comparable** con las ejecuciones de modelos (muestra independiente, condiciones, participantes y puntuación). La diferencia 95 % frente a 46,83 % debe tratarse como **brecha reportada**, no como ensayo controlado de humano versus IA.

### Exactitud por granularidad — SmolAgents GPT-5 multimodal

| Nivel | Exactitud |
|---|---:|
| HS2 | **82,06 %** |
| HS4 | 72,06 % |
| HS6 | 62,38 % |
| 8 dígitos | 52,38 % |
| **10 dígitos** | **46,83 %** |

La caída de **35,23 puntos porcentuales** desde capítulo hasta código final ilustra que reconocer una familia no equivale a resolver condiciones técnicas decisivas.

### Comparación de agentes comerciales — solo **49 casos**

| Sistema | Exactitud HS10 |
|---|---:|
| SmolAgents GPT-5 | 42,86 % |
| AWorld GPT-5 | 42,86 % |
| Gemini Deep Research | 40,81 % |
| Manus | 30,61 % |
| Grok DeepSearch | 26,53 % |

**No mezclar** resultados de esta submuestra de 49 con los 632 casos para establecer jerarquías sin aclarar muestra y variabilidad.

## 5. Ablaciones y hallazgos relevantes

### 5.1. Reglas adicionales redactadas por expertos

| Agente | Sin reglas de decisión extra | Con reglas extra |
|---|---:|---:|
| SmolAgents | 46,83 % | 43,83 % |
| AWorld | 41,30 % | 42,95 % |
| WebSailor | 35,44 % | 35,43 % |

Proveer reglas **no garantiza que el agente las aplique correctamente**. Estos resultados no significan que deban ignorarse las normas originales; indican una limitación de su incorporación mediante prompts en esos sistemas.

### 5.2. Imágenes del producto

En SmolAgents, acceso a imagen aumenta HS10 de **42,72 %** a **46,83 %** (+4,11 pp). Los casos del anexo I ilustran presencia/ausencia de piezas, características superficiales y tipos de materiales. Otros modelos no muestran necesariamente la misma mejora.

El resultado es pertinente **solo si existe información visual disponible**, no para una DAM que contiene exclusivamente texto.

### 5.3. Contenido y razonamiento adicional

- Visitar páginas completas en cierta configuración reduce HS10 de **42,72 % a 42,09 %**: más contexto puede introducir ruido.
- WebSailor obtiene **40,82 %** con poco razonamiento previo, **37,34 %** con razonamiento intermedio y **35,44 %** con razonamiento extenso.
- Autorreflexión modifica **42,72 % → 42,57 %**, una disminución leve.
- Votación a través de **1, 2, 4, 8 y 16** ejecuciones no produce una mejora relevante en las figuras publicadas.

No debe inferirse de ello que **toda validación** o razonamiento humano sea inútil. Se examinan estrategias específicas de agentes, no verificaciones externas estructuradas de atributos o reglas.

## 6. Taxonomía de errores: contribución central

Los autores distinguen seis modos de fallo:

1. **Decisión prematura**, con búsqueda orientada a confirmar una hipótesis temprana equivocada.
2. **Procesamiento incorrecto de información**, como perder o alterar detalles del producto.
3. **Autocorrección innecesaria**, sustituyendo respuestas correctas por otras incorrectas.
4. **Alucinación de razonamiento** o de características no sustentadas.
5. **Aplicación equivocada de reglas** y excepciones.
6. **Falta de conocimiento técnico especializado**.

La Figura 4 agrega **códigos desactualizados**, **códigos inexistentes**, **códigos vigentes pero equivocados** y otros errores. Aproximadamente **75,3 %** de los fallos de agentes analizados corresponden a **códigos válidos pero incorrectos** bajo su referencia: **la existencia o vigencia de un dato no acredita pertinencia**.

### Casos concretos de anexos

**Guantes anunciados como nitrilo con atributo `Material: PVC` (Figura 16).** El agente prioriza el título y predice caucho (capítulo 40), mientras la referencia prioriza el campo PVC y el capítulo 39. **Cautela:** hay contradicción documental; el estudio no incorpora ensayo físico independiente que demuestre material real.

**Etiquetas adhesivas de PVC (Figura 15).** Los términos de marketing «decoración» y «scrapbooking» desvían la clasificación hacia impresos (49), en vez de atender la naturaleza y presentación física que fundamentan la referencia (39).

**Brazalete de silicona de advertencia médica (Figura 17).** Se interpreta apariencia de bisutería por encima de función, según los autores.

**Jaula de seguridad para montacargas (Tabla 8).** Diferentes agentes inventan o exageran funciones mecánicas, confunden accesorios con máquina independiente o sobrerrazonan una característica secundaria.

**Pistola pulverizadora (anexo H).** Acierto de partida general sin acertar en la división arancelaria completa.

Estos son ejemplos de **clasificación HS**, no reglas generales de valor en aduana ni validación jurídica independiente de todos los supuestos.

## 7. Limitaciones científicas

- 632 productos de un entorno e-commerce, con eliminación deliberada de redundancia: **no representa necesariamente un universo operativo de DAM**.
- El 95 % humano carece de protocolo completamente simétrico y divulgado.
- Solo una etiqueta HS10 por producto, sin medir explícitamente la capacidad de **abstenerse** ante datos incompletos.
- El sistema compara exactitud de clasificación, no calidad de antecedentes documentales recuperados ni su admisibilidad.
- Los resultados de agentes comerciales tienen **solo 49 casos**.
- No se publican intervalos de confianza para todos los resultados ni tamaño suficiente de subgrupos raros.
- El anexo F resume reglas mediante texto creado por expertos: **no reemplaza la norma oficial ni su interpretación jurídica**.
- El dataset disponible puede excluir **URL e imágenes**, lo que limita la réplica íntegra del experimento multimodal.
- El valor de producto `precio` es un atributo de e-commerce, **no** valor CIF, valor en aduana ni referencia de transacción ajustada.

## 8. Contribución a SIVEP Inteligente

**Pertinencia media para la primera pregunta de comparabilidad; alta como evidencia de fallos de agentes y aplicación de reglas.**

La enseñanza más relevante es la necesidad de diferenciar:
- Hechos comerciales **expresos** y sus fuentes.
- Atributos **inferidos** que pueden ser incorrectos.
- Antecedentes **existentes** que pueden ser **inaplicables**.
- Normas **recuperadas** frente a normas **correctamente aplicadas**.
- Una explicación **plausible** frente a una explicación **respaldada y revisable**.

Un antecedente histórico legítimo en SIVEP puede describir una mercancía comercialmente distinta, así como un código vigente puede ser incorrecto para un producto determinado. El benchmark no prueba una solución para esa diferencia, pero documenta por qué **la mera disponibilidad de información y un agente generativo no bastan**.

## 9. Relación con la colección

Se relaciona con [artículo 5 — derecho de valoración](05-morgero-macedo-2025-articulo-17.md), [9 y 10 — atributos de producto](09-brinkmann-baumann-bizer-2024-wdc-pave.md), [11 y 12 — explicaciones documentales](11-lee-et-al-2024-explainable-customs.md) y [13 — recuperación semántica](13-ravi-et-al-text2trade-mnrl-mcd.md).

**Conclusión:** benchmark valioso de **aplicación de reglas, error de razonamiento y validez de una clasificación**, pero sin pruebas directas de identificación de mercancías idénticas/similares ni utilización de referencias para valoración aduanera.
