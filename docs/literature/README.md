# Revisión de literatura — SIVEP Inteligente

**Estado:** revisión documental inicial de ocho publicaciones (2023–2026), basada en los **PDF completos** utilizados en esta conversación.  
**Proyecto:** [SIVEP Inteligente](../../README.md) — recuperación auditable de mercancías idénticas o similares para apoyar el análisis de valores históricos.  
**Fecha de elaboración de esta versión:** 21 de noviembre de 2026.  
**Fase:** CONFIGURACIÓN / revisión de literatura. **No se ha activado formalmente ninguna IA operativa ni se ha elegido aún una familia piloto o algoritmo definitivo.**

> **Distinción obligatoria:** recomendar una DAM histórica, detectar un valor estadísticamente atípico y determinar jurídicamente el valor en aduana **son operaciones diferentes**. La decisión corresponde al especialista y al procedimiento aplicable. Un antecedente declarado no es automáticamente un valor verificado ni una referencia legal admisible.

## 1. Objetivo y preguntas orientadoras

Examinar estudios sobre gestión del riesgo aduanero, búsqueda textual, detección de anomalías, clasificación de mercancías, predicción de valores y marco jurídico de valoración para identificar **qué técnicas merece la pena someter a evaluación experimental con antecedentes SIVEP**.

Preguntas que guían el análisis:
1. **Comparabilidad:** ¿cómo localizar registros de mercancías realmente **idénticas, similares o no comparables**, sin confundir similitud lingüística con equivalencia técnica/jurídica?
2. **Valor:** ¿cómo analizar y explicar diferencias de valores entre antecedentes **válidos y comparables**, sin imponer precios mínimos automáticos?
3. **Uso:** ¿cómo apoyar al especialista en selección temprana, dudas razonables y control posterior, distinguiendo evidencia de decisión administrativa?
4. **Calidad y trazabilidad:** ¿cómo controlar procedencia, estado de verificación, temporalidad, sesgo de selección y errores críticos?

La revisión **no es todavía una revisión sistemática**: estos ocho trabajos fueron seleccionados para una lectura temática; no se ha ejecutado un protocolo PRISMA, búsqueda exhaustiva, diagrama de exclusiones ni evaluación bibliométrica independiente de impacto editorial.

## 2. Índice de artículos — resumen ejecutivo de cada publicación

### 1. [Vijayakumar (2025) — India: gestión de riesgos con técnicas textuales](01-vijayakumar-2025-india.md)

Describe el *Import Valuation Anomaly Model* de la Aduana india: agrupamiento textual y detección de comunidades para identificar conjuntos de mercancías presuntamente idénticas o similares; comparación de una nueva descripción mediante distancias; utilización de antecedentes del mismo proveedor/origen y época/cantidad semejantes; generación de una **alerta** ante discrepancias relevantes. También describe normalización de proveedores y analítica de redes.

**Lo que aporta:** la arquitectura conceptual más directa de **recuperación histórica para alertas de valoración**.  
**Lo que no demuestra:** algoritmo exacto, umbrales, etiquetas de comparabilidad ni métricas del modelo de valoración.

### 2. [Alqaryouti et al. (2024) — Dubái: distancias + LOF](02-alqaryouti-2024-dubai.md)

Utiliza **500 000 declaraciones de 2018**, agrupadas por HS; detecta puntos atípicos mediante distancias y comprueba su densidad local mediante **Local Outlier Factor**. Reporta hasta **86 % de exactitud**, con precauciones sobre la métrica llamada “precision” y una evaluación balanceada.

**Lo que aporta:** una línea base concreta de **detección de anomalías de valores**.  
**Lo que no resuelve:** identificar mercancías idénticas/similares mediante descripción; **compartir HS no garantiza comparabilidad**.

### 3. [Chan, Ng y Chung (2023) — Hong Kong: NLP y valor probabilístico](03-chan-ng-chung-2023-hong-kong.md)

Aprende representaciones de descripciones comerciales con **Word2Vec**, emplea redes convolucionales con compuertas y predice **distribuciones de valor unitario y total** condicionadas al producto. Reporta, entre otros resultados, **F1 = 80,8 %** para anomalías de valor unitario en capítulo 8 y **F1 = 81,6 %** para valor total en una prueba con anomalías simuladas.

**Lo que aporta:** evidencia para estimar **rangos específicos de producto**, evitando rangos excesivamente amplios por código.  
**Lo que no proporciona:** DAM comparables individuales ni una referencia legal de valoración.

### 4. [Alwanin et al. (2026) — DXGBA: clasificación y riesgo económico](04-alwanin-2026-dxgba.md)

Entrena **DXGBA**, un enfoque multitarea inspirado en XGBoost, para clasificar fraude y estimar una magnitud económica. Usa **54 000 registros sintéticos** generados por CTGAN. Reporta **F1 = 0,4923** y concentración del **87,98 % de la magnitud económica del experimento** al seleccionar el **10 %** de operaciones.

**Lo que aporta:** priorización por **capacidad de revisión e impacto potencial**.  
**Límite decisivo:** resultado **simulado**, no recaudación real; contiene ambigüedades documentales sobre prevalencia de fraude y variable monetaria objetivo.

### 5. [Morgero y Macedo da Silva (2025) — Artículo 17 y América Latina](05-morgero-macedo-2025-articulo-17.md)

Analiza la facultad de comprobar veracidad/exactitud bajo el **artículo 17 del Acuerdo de Valoración de la OMC**. Incluye siete países, **Perú** entre ellos. Diferencia bases históricas usadas para **gestión de riesgos** de antecedentes aptos para **métodos de valoración**. Para Perú refiere valores declarados, analizados y en evaluación, sin identificar técnicamente la base por la sigla SIVEP.

**Lo que aporta:** **requisitos jurídico-operativos** y necesidad de categorizar la confiabilidad del histórico.  
**Lo que no ofrece:** algoritmos de matching ni métricas cuantitativas.

### 6. [Bayona (2025) — OMC: transposición arancelaria con TF-IDF y SBERT](06-bayona-2025-transposicion-hs.md)

Propone **tres rondas**: relaciones determinísticas, coincidencias exactas y, para casos difíciles, **TF-IDF + coseno** frente a **Sentence-BERT + coseno**. En dos economías procesa **7 946** y **9 802** líneas, con exactitudes globales de **99,6 %** y **98,8 %**, respectivamente, contando también las rondas determinísticas.

**Lo que aporta:** **diseño comparativo y línea base de recuperación textual**.  
**Hallazgo crítico:** incluso una **similitud coseno de 0,98** puede conducir a correspondencia incorrecta. Compara líneas arancelarias, **no** mercancías históricas.

### 7. [Kim, Kim y Choi (2025) — Corea: THE-RAG híbrido](07-kim-kim-choi-2025-the-rag.md)

Desarrolla **THE-RAG**, que combina recuperación densa, **BM25** y reranking en dos etapas jerárquicas. En 100 casos obtiene **Top-3 HS6 de 60 %** con Gemini 1.5 Flash; en una prueba ampliada de **1 000 casos**, **49,3 %** frente a **30,4 %** sin RAG.

**Lo que aporta:** arquitectura implementable de **búsqueda híbrida + reordenamiento + evaluación por configuraciones**.  
**Límites:** mide clasificación HS, no identidad de mercancías; no aísla experimentalmente el aporte de cada recuperador.

### 8. [Outram y Swartz (2026) — IA y cadena comercial integrada](08-outram-swartz-2026-fronteras.md)

Expone una plataforma que canonicaliza productos y empresas, construye redes comerciales, identifica embarques históricos y compara valores declarados con **distribuciones de valor plausibles**. La **Figura 7** muestra un ejemplo de neumáticos muy próximo al objetivo funcional de SIVEP. Comunica **40 % de mercancías en vía verde acelerada** y estimaciones económicas de **US$ 1 100 millones** anuales en un escenario, sin protocolo abierto suficiente para reproducirlas.

**Lo que aporta:** **referencia de arquitectura funcional integrada**.  
**Límites:** algoritmos propietarios/no detallados y resultados de despliegue o potencial económico **reportados**, no validación independiente del matching.

---

## 3. Cuadro comparativo general de los ocho trabajos

| Nº | Publicación, año y ámbito | Problema principal | Técnicas / enfoque | Datos y evidencia | Resultado destacable, interpretado correctamente | Límite más relevante |
|---|---|---|---|---|---|---|
| **1** | Vijayakumar, 2025; India; *World Customs Journal* | Riesgo y posible subvaloración | Clustering textual, comunidades, distancias y análisis contextual | Experiencia institucional, sin prueba cuantitativa reproducible del módulo de valor | Arquitectura de comparación de declaraciones históricas y alertas | No revela algoritmo ni calidad de la comparabilidad |
| **2** | Alqaryouti et al., 2024; Dubái; *IJIT* | Valores declarados atípicos | Agrupación por HS, distancia euclidiana, LOF | 500 000 declaraciones de 2018; pruebas con muestras balanceadas | Hasta **86 % exactitud** | HS ≠ mercancía homogénea; no usa descripción |
| **3** | Chan et al., 2023; Hong Kong; *SJIAOS* | Errores estadísticos en códigos y valores | Word2Vec, GCNN, regresión probabilística | Registros de comercio, dos capítulos; parte de simulación | **F1 80,8 %** en anomalía de valor unitario (cap. 8) | Intervalo predictivo ≠ referencia documental |
| **4** | Alwanin et al., 2026; *Scientific Reports* | Fraude y prioridad económica | DXGBA/XGBoost multitarea, SMOTE, SHAP | **54 000 registros sintéticos** | **F1 49,23 %**; **87,98 %** de magnitud económica al revisar 10 % en simulación | No prueba recaudación real; no empareja productos |
| **5** | Morgero y Macedo da Silva, 2025; 7 países latinoamericanos; *World Customs Journal* | Duda razonable, artículo 17 y calidad de antecedentes | Revisión normativa, encuesta, entrevista | Evidencia cualitativa; incluye Perú | Diferencia antecedentes declarados, analizados y en evaluación | No propone IA ni evaluación algorítmica |
| **6** | Bayona, 2025; OMC; working paper | Correspondencia de líneas SA2017/SA2022 | Reglas, exact match, TF-IDF, SBERT y coseno | 7 946 / 9 802 líneas y verificación humana | **99,6 % / 98,8 % global**, mayormente por rondas determinísticas | Transposición arancelaria, no comparabilidad de DAM |
| **7** | Kim, Kim y Choi, 2025; Corea; *Journal of Information Systems* | Recomendación de HS6 | Dense + BM25 + rerank + LLM, dos etapas | Casos oficiales; pruebas de 100 y 1 000 | **49,3 % Top-3 HS6** en 1 000 casos con THE-RAG frente a 30,4 % sin RAG | No mide recuperación de mercancías; depende de chunk y LLM |
| **8** | Outram y Swartz, 2026; *World Customs Journal* | Riesgo integrado con cadenas comerciales | Canonicalización, grafos, IA y rangos de valoración | Casos ilustrativos y despliegues reportados | **40 % en vía verde** reportado; potencial económico ilustrativo | Sin detalle de modelos ni validación pública del comparador |

**Advertencia de comparabilidad de cifras:** accuracy, F1, Top-3, exactitud de transposición, cobertura de riesgo e impacto económico **miden tareas y poblaciones diferentes**. No es válido ordenar los ocho artículos por el valor numérico mayor ni inferir que el 99,6 % de transposición del artículo 6 supera al 49,3 % de clasificación del artículo 7 en una misma tarea.

## 4. Cuadro de aportación de cada artículo al proyecto SIVEP Inteligente

**Etapas de diseño, todavía no aprobadas como arquitectura definitiva:**

- **A — Datos:** normalización de DAM, extracción de atributos y estado de confiabilidad del histórico.
- **B — Comparabilidad:** recuperar y validar mercancías idénticas, similares o no comparables.
- **C — Valor:** analizar valores históricos comparables y anomalías/intervalos, distinguiendo evidencia documental y estimación.
- **D — Riesgo:** priorizar operaciones para control y control posterior.
- **E — Gobernanza:** explicación, procedimiento jurídico, trazabilidad y supervisión.

| Artículo | Etapa(s) más pertinente(s) | Aporte específico que podríamos incorporar | Experimento / requisito sugerido | Prioridad para **primer experimento de comparabilidad** |
|---|---|---|---|---|
| **1. India** | A, B, C | Agrupamiento textual de históricos y comparación contextual por proveedor, origen, tiempo y cantidad | **Clustering previo vs búsqueda directa**; filtros duros vs ponderados | **Alta** |
| **2. Dubái** | C | Distancia euclidiana + LOF para detectar valores atípicos | Comparar LOF con cuantiles/MAD/Isolation Forest **tras** matching | **Baja** (fase posterior) |
| **3. Hong Kong** | A, C | Descripciones → distribuciones probabilísticas de valores unitarios y totales | Entrenar estimaciones condicionadas; medir calibración y cobertura | **Media** (atributos; valor después) |
| **4. DXGBA** | D, E | Ranking por fraude e impacto; explicaciones SHAP | Priorizar por capacidad y evaluar riesgo económico verificado | **Baja** (fase posterior) |
| **5. Artículo 17** | A, B, C, E | Separar referencias de **riesgo** de referencias para **métodos de valoración**; confiabilidad de valores | Requisitos de campos de SIVEP, validez del antecedente y supervisión experta | **Muy alta como condición transversal** |
| **6. Bayona** | A, B | Reglas + coincidencia exacta + TF-IDF/SBERT + coseno; análisis de errores técnicos | **Baseline léxico frente a semántico**; preservar números/modelos; medir falsos positivos críticos | **Muy alta** |
| **7. THE-RAG** | A, B, E | Recuperación híbrida BM25+dense y reordenamiento, con distintas configuraciones | **BM25 vs embeddings vs fusión+rerranking**; ablaciones; explicación separada | **Muy alta** |
| **8. Outram–Swartz** | A, B, C, D, E | Arquitectura integral con canonicalización, antecedentes y valor estimado | Validar la cadena completa por módulos; grafos como posible ampliación | **Alta como referencia funcional**, no como algoritmo |

**Lectura conjunta:** el [artículo 5](05-morgero-macedo-2025-articulo-17.md) define límites de uso; los [artículos 6](06-bayona-2025-transposicion-hs.md) y [7](07-kim-kim-choi-2025-the-rag.md) sugieren estrategias experimentales para **recuperación**; el [1](01-vijayakumar-2025-india.md) y el [8](08-outram-swartz-2026-fronteras.md) articulan el caso de uso. Los [2](02-alqaryouti-2024-dubai.md), [3](03-chan-ng-chung-2023-hong-kong.md) y [4](04-alwanin-2026-dxgba.md) ofrecen alternativas **posteriores** de análisis de valor y priorización.

## 5. Síntesis crítica transversal

### 5.1. Lo que esta revisión SÍ respalda

1. **El código arancelario puede reducir candidatos, pero no garantizar comparabilidad comercial.**
2. **El texto de las DAM contiene señales útiles**; sus atributos técnicos deben preservarse y verificarse.
3. **Una búsqueda por palabras y una por embeddings son alternativas complementarias** que merecen comparación experimental.
4. **La similitud coseno alta no es probabilidad de identidad ni prueba jurídica de similitud.**
5. **Una referencia histórica y una estimación estadística no son equivalentes.**
6. **Los valores no revisados y los analizados deben distinguirse** en la fuente y en la salida del sistema.
7. **Las métricas deben corresponder a la fase real:** retrieval, matching, anomalía, priorización o decisión experta.
8. **La intervención del especialista sigue siendo necesaria**, incluso si el algoritmo proporciona antecedentes y explicaciones.

### 5.2. Vacío específico detectado

**Ninguno de estos ocho artículos demuestra de forma reproducible un algoritmo que determine la identidad o similitud jurídicamente relevante de mercancías a partir de descripciones de DAM peruanas y al mismo tiempo valide la idoneidad del valor histórico como antecedente.**

No significa que tal tecnología no exista; significa que **no está demostrada en este conjunto bibliográfico**. Esa ausencia justifica diseñar un experimento propio, pero no permite afirmar originalidad absoluta sin una búsqueda más exhaustiva.

## 6. Primera línea experimental sugerida — todavía por decidir

| Bloque | Variantes candidatas | Métricas mínimas |
|---|---|---|
| Selección de familia y ventana de datos | SA6/NANDINA8/subpartida nacional y fechas; decisión pendiente | Cobertura del histórico, heterogeneidad, registros utilizables |
| Normalización y atributos | Descripción normalizada; extracción de marca/modelo/composición/capacidad; reglas exactas | Calidad de atributos, tasa de ausencia/contradicción |
| Recuperación | Coincidencia exacta; BM25; TF-IDF; embeddings; híbrido; agrupamiento opcional | Recall@5/10/20, Precision@5, latencia |
| Reranking/comparabilidad | Reglas estructuradas; ranking híbrido; reranker opcional | Errores críticos de identidad, F1 por clase, cobertura y abstención |
| Etiquetado experto | Idéntica / similar / no comparable; razones por atributo y acuerdo entre especialistas | Concordancia, etiquetas disputadas, prueba temporal |
| Valores (fase posterior) | Estadísticos robustos; LOF; intervalos probabilísticos | Cobertura, calibración, falsos positivos de alerta |
| Priorización (fase posterior) | Ranking por riesgo/impacto | Precision@capacidad, costo operativo, resultados de revisión |

**Restricciones para un experimento defendible:**
- Crear **conjunto de evaluación experto** independiente del ajuste de algoritmos.
- No permitir que una DAM consulte antecedentes **posteriores a su propia fecha** en evaluaciones retrospectivas.
- Evitar fugas por registros duplicados entre entrenamiento/evaluación.
- No entrenar etiquetas «no fraude» usando exclusivamente declaraciones **no revisadas**.
- Evaluar por **familia de mercancías** y atributos discriminantes, no solo mediante un promedio global.
- Registrar versión del corpus, normas aplicables, algoritmo, métricas, errores y decisiones humanas.

## 7. Calidad de las fuentes y política de revisión

| Tipo de fuente | Artículos | Precaución |
|---|---|---|
| Revistas académicas con evaluación experimental | **2, 3, 4, 7** | Revisar muestras, métricas, definiciones y reproducibilidad; 4 usa datos sintéticos |
| Revista aduanera: exposición institucional/estratégica | **1 y 8** | No inferir métricas no publicadas ni replicabilidad de ejemplos |
| Revista aduanera: estudio jurídico-cualitativo | **5** | No convertir respuestas de especialistas en pruebas de efectividad estadística |
| Documento de trabajo institucional | **6** | Citar como working paper de su autora, no como norma oficial ni necesariamente como peer review |

**Trazabilidad:** cada ficha individual identifica DOI o institución, datos, apartado o tabla cuando son relevantes, interpretación, limitaciones y **propuestas propias claramente diferenciadas**. Los PDFs revisados se mantuvieron como fuentes suministradas; **no se suben sus textos completos al repositorio público**. Las cifras de cada ficha deben revisarse contra el artículo original si se reutilizan en tesis o publicación.

### Observaciones editoriales que conviene conservar

- **Artículo 2:** “precision” no es descrita de manera terminológicamente consistente.
- **Artículo 4:** discrepancia sobre prevalencia de fraude y ambigüedad entre `Item price` e ingresos tributarios; 87,98 % tabulado frente a otra cifra textual.
- **Artículo 6:** pequeño desajuste entre porcentaje narrado y ciertos recuentos de la ronda 3 de economía A.
- **Artículo 7:** inconsistencia en etiquetas de modelo en las Tablas 5 y 6.
- **Artículo 8:** resultados operativos reportados y relación de los autores con proveedor tecnológico; ausencia de protocolo externo completo.

## 8. Próximas decisiones, NO tomadas aún

1. Selección de **familia piloto** y nivel arancelario de delimitación (SA6, NANDINA8 o subpartida nacional).
2. Identificación de campos disponibles en el **formato B de DAM/SIVEP**, procedencia y estados de valores.
3. Protocolo experto para distinguir **idénticas / similares / no comparables** y documentar desacuerdos.
4. Línea base experimental y métricas obligatorias.
5. Revisión adicional de trabajos específicamente sobre *product matching*, *entity resolution*, *record linkage* y descripciones comerciales de productos, para contrastar la originalidad y ampliar los métodos posibles.

## 9. Referencias y enlaces rápidos

| Nº | Publicación | Fuente |
|---|---|---|
| 1 | Vijayakumar (2025), *World Customs Journal* | https://doi.org/10.55596/001c.131745 |
| 2 | Alqaryouti et al. (2024), *International Journal of Information Technology* | https://doi.org/10.1007/s41870-024-01821-1 |
| 3 | Chan et al. (2023), *Statistical Journal of the IAOS* | https://doi.org/10.3233/SJI-230081 |
| 4 | Alwanin et al. (2026), *Scientific Reports* | https://doi.org/10.1038/s41598-025-33382-z |
| 5 | Morgero y Macedo da Silva (2025), *World Customs Journal* | https://doi.org/10.55596/001c.127239 |
| 6 | Bayona (2025), *WTO Staff Working Paper ERSD-2025-04* | Publicación de la OMC identificada por su número de documento |
| 7 | Kim, Kim y Choi (2025), *The Journal of Information Systems* | https://doi.org/10.5859/KAIS.2025.34.3.167 |
| 8 | Outram y Swartz (2026), *World Customs Journal* | https://doi.org/10.55596/001c.159458 |

**Numeración editorial:** el séptimo artículo de esta colección es **THE-RAG (Kim, Kim y Choi, 2025)**. El artículo *An Ensemble Deep Learning Framework for Automated HS Code Classification in International Trade* no se incluye porque no se consiguió su PDF y el responsable sustituyó explícitamente esa selección.

---
*Material de revisión académica elaborado durante la CONFIGURACIÓN del proyecto. No implica activación de una IA Coordinadora, uso operativo de SIVEP, aprobación de arquitectura ni conclusión jurídica sobre un valor declarado.*
