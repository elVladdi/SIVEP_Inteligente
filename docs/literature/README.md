# Revisión de literatura: inteligencia artificial, riesgo y valoración aduanera

**Colección analizada:** ocho publicaciones de 2023–2026 sobre gestión de riesgos, comparación de descripciones comerciales, clasificación arancelaria, anomalías de valor, priorización de controles y fundamentos jurídicos de la valoración aduanera.

**Ámbito de análisis:** investigación bibliográfica vinculada con el problema de identificación de mercancías comparables y uso de antecedentes históricos en **[SIVEP Inteligente](../../README.md)**.

> **Nota de alcance.** Esta es una revisión crítica y temática de ocho fuentes examinadas en texto completo; no es una revisión sistemática ni un metaanálisis. Las contribuciones a SIVEP descritas aquí constituyen **relaciones analíticas entre la literatura y el problema de investigación**, no decisiones de implementación. Cada artículo dispone de una [ficha ampliada](#2-estudios-revisados) con sus datos, metodología, resultados y limitaciones.

## 1. Objeto de la revisión

La revisión examina cómo la literatura especializada aborda cinco problemas relacionados: **(i)** la identificación de mercancías o registros comparables a partir de descripciones heterogéneas; **(ii)** el análisis de valores históricos y detección de anomalías; **(iii)** la priorización de operaciones según el riesgo; **(iv)** la explicabilidad y trazabilidad de las recomendaciones; y **(v)** los límites jurídicos e institucionales al utilizar antecedentes de valoración.

Estos problemas están relacionados, pero no son intercambiables. La **similitud textual** entre dos registros no demuestra necesariamente la **identidad o similitud comercial y jurídica** de sus mercancías. Una **anomalía estadística** tampoco acredita una **subvaloración aduanera**, y una predicción de precio no sustituye un valor histórico cuya procedencia y admisibilidad deban verificarse.

Las publicaciones se examinan a partir de su pregunta de investigación, fuentes de datos, métodos, resultados reportados, limitaciones de validez y contribución al estudio de **referencias históricas de valor en declaraciones aduaneras**. La comparabilidad de sus métricas se analiza en función de la tarea evaluada, no del valor absoluto de los porcentajes.

## 2. Estudios revisados

### 2.1. [Vijayakumar (2025) — India: gestión del riesgo aduanero basada en datos](01-vijayakumar-2025-india.md)

**Problema.** La Aduana india debe identificar operaciones de riesgo en grandes volúmenes comerciales y relacionar registros que describen mercancías y operadores de formas diferentes.

**Método.** El estudio describe un *Import Valuation Anomaly Model* que utiliza **agrupamiento textual**, **detección de comunidades** y **algoritmos de distancia** para vincular nuevas declaraciones con grupos históricos de mercancías presuntamente idénticas o similares. La comparación contempla, de manera conceptual, proveedor, país de origen, periodo y cantidad. El trabajo también presenta soluciones de normalización de proveedores y análisis de redes.

**Resultados y evidencia.** Se documenta una arquitectura de identificación de grupos y generación de alertas para revisión; **no se publican** parámetros precisos de clustering, función de distancia ni métricas específicas del modelo de valoración.

**Contribución.** Ofrece un antecedente operativo de **búsqueda histórica contextualizada de mercancías** para análisis de posible subvaloración. Su principal límite es que **la comparabilidad de los productos no se valida mediante un protocolo reproducible**.

### 2.2. [Alqaryouti et al. (2024) — Dubái: anomalías mediante distancias y densidad](02-alqaryouti-2024-dubai.md)

**Problema.** Identificar declaraciones cuyo valor resulta anómalo respecto de antecedentes aduaneros, reduciendo la necesidad de examinar todas las operaciones manualmente.

**Método.** Sobre un histórico de **500 000 declaraciones de 2018**, los autores agrupan inicialmente por código HS, emplean **distancias euclidianas** para localizar observaciones alejadas y aplican **Local Outlier Factor (LOF)** como segunda comprobación basada en densidad local.

**Resultados y evidencia.** Informan una **exactitud máxima de 86 %** bajo las condiciones experimentales descritas, particularmente al seleccionar grupos arancelarios más poblados. La evaluación incluye muestras balanceadas y la definición de la métrica denominada *precision* presenta una ambigüedad terminológica.

**Contribución.** Aporta un algoritmo explícito para **detección de valores atípicos** y evidencia sobre la influencia del tamaño del histórico. No establece que compartir un código HS equivalga a tratarse de mercancías idénticas o similares.

### 2.3. [Chan, Ng y Chung (2023) — Hong Kong: descripción comercial y rangos de valor](03-chan-ng-chung-2023-hong-kong.md)

**Problema.** Los rangos de valor definidos exclusivamente por código arancelario pueden ser demasiado amplios cuando incluyen productos de distinta naturaleza, calidad y precio.

**Método.** Los autores entrenan representaciones **Word2Vec** sobre más de **diez millones de descripciones comerciales únicas** y emplean redes convolucionales con compuertas y **regresión probabilística** para evaluar códigos, valores unitarios y valores totales. Las distribuciones de valor se condicionan a características de cada producto.

**Resultados y evidencia.** Se reporta **F1 de 80,8 %** para anomalías del valor unitario en el capítulo 8; el **F1 de 81,6 %** del módulo de valor total corresponde a una evaluación con anomalías simuladas. Los ejemplos de monedas de oro y plata ilustran el problema de emplear un solo rango de precios por código.

**Contribución.** Demuestra la utilidad de considerar **descripciones específicas de mercancías** para identificar desviaciones. Su finalidad es la calidad de las estadísticas de comercio, no la determinación jurídica de valores aduaneros; las distribuciones estimadas no son antecedentes documentales individuales.

### 2.4. [Alwanin et al. (2026) — Clasificación de fraude y priorización económica](04-alwanin-2026-dxgba.md)

**Problema.** La detección de fraude no garantiza que los controles se concentren en las operaciones de mayor impacto económico.

**Método.** El estudio desarrolla **DXGBA**, un enfoque de *gradient boosting* con objetivos conjuntos de clasificación y regresión, y utiliza **SHAP** para interpretar predicciones. Evalúa variantes de remuestreo y representaciones adicionales sobre **54 000 declaraciones sintéticas generadas con CTGAN**.

**Resultados y evidencia.** Reporta **F1 de 49,23 %** para la configuración destacada y una concentración del **87,98 % de la magnitud económica evaluada** al seleccionar el **10 %** de operaciones. Esta segunda cifra pertenece a una simulación: **no representa tributos efectivamente recuperados**. El artículo contiene además ambigüedades sobre la proporción de fraudes y la variable monetaria de regresión.

**Contribución.** Introduce la **priorización de controles bajo capacidad limitada** como un problema distinto de detectar anomalías. No presenta un algoritmo de identificación de mercancías equivalentes a partir de sus descripciones.

### 2.5. [Morgero y Macedo da Silva (2025) — Artículo 17 y prácticas latinoamericanas](05-morgero-macedo-2025-articulo-17.md)

**Problema.** Compatibilizar las facultades de verificación de la administración con los métodos y garantías del **Acuerdo de Valoración de la OMC**, especialmente ante discrepancias de precios y dificultades para hallar antecedentes de mercancías idénticas o similares.

**Método.** Revisión jurídica y documental, entrevista especializada y cuestionario respondido por **siete países latinoamericanos, incluido Perú**.

**Resultados y evidencia.** El estudio identifica diferencias en la composición de bases de valoración: algunos países utilizan principalmente valores examinados, mientras otros incorporan valores simplemente declarados. Para Perú se mencionan **valores declarados, analizados y en evaluación**. La investigación no mide el rendimiento de algoritmos.

**Contribución.** Establece una distinción esencial entre el uso del histórico para **gestión de riesgos** y el uso de antecedentes en **métodos de valoración**. Reafirma que una diferencia de precios no rechaza automáticamente el valor de transacción. Es el principal antecedente jurídico-institucional de esta colección.

### 2.6. [Bayona (2025) — OMC: correspondencia de líneas arancelarias con NLP](06-bayona-2025-transposicion-hs.md)

**Problema.** Relacionar líneas arancelarias de **SA 2017 y SA 2022**, incluidas descripciones nacionales que cambian entre revisiones.

**Método.** Proceso de tres rondas: **correlaciones determinísticas**, **coincidencia textual exacta** y comparación de los casos pendientes mediante **TF-IDF** o **Sentence-BERT**, ambos con **similitud coseno**, bajo restricciones de correlación arancelaria.

**Resultados y evidencia.** Para dos economías, con **7 946** y **9 802** líneas, se informan exactitudes globales de **99,6 % y 98,8 %**. Estos porcentajes corresponden al **proceso completo**, mayoritariamente resuelto por las primeras dos rondas, no al rendimiento aislado de SBERT. El análisis de errores muestra que correspondencias equivocadas pueden obtener una similitud coseno de hasta **0,98**.

**Contribución.** Proporciona una comparación experimental de enfoques **léxicos y semánticos**, con especial atención a números, negaciones y términos técnicos discriminantes. El objeto de estudio son **líneas arancelarias**, no mercancías de declaraciones.

### 2.7. [Kim, Kim y Choi (2025) — Corea del Sur: recuperación híbrida THE-RAG](07-kim-kim-choi-2025-the-rag.md)

**Problema.** Recomendar subpartidas HS6 a partir de descripciones técnicas y documentación arancelaria organizada jerárquicamente.

**Método.** Los autores proponen **THE-RAG**, con recuperación densa mediante embeddings, búsqueda **BM25**, **reranking** y generación mediante LLM. La recuperación opera en dos niveles: primero capítulos HS y después subpartidas. Se comparan tamaños de fragmentos documentales y distintos modelos de lenguaje.

**Resultados y evidencia.** En **100 casos**, la mejor exactitud **Top-3 HS6** alcanza **60 %**; en una ampliación a **1 000 casos** alcanza **49,3 %**, frente a **30,4 %** sin RAG para la comparación señalada. Los resultados dependen del tamaño del contexto y del modelo empleado.

**Contribución.** Describe una arquitectura técnica de **recuperación híbrida y reordenamiento**, útil para comprender complementariedades entre coincidencias léxicas y semánticas. Evalúa **clasificación de códigos HS**, no identificación de mercancías comparables ni valores históricos.

### 2.8. [Outram y Swartz (2026) — IA integrada en la gestión fronteriza](08-outram-swartz-2026-fronteras.md)

**Problema.** Los análisis limitados a cada declaración omiten relaciones entre productos, fabricantes, proveedores y cadenas internacionales de suministro que pueden explicar riesgos o discrepancias.

**Método.** El artículo describe sistemas que combinan **canonicalización de entidades y productos**, grafos comerciales, modelos predictivos y explicaciones respaldadas por datos. La **figura 7, página 181**, muestra un ejemplo de neumáticos que relaciona embarques históricos potencialmente comparables con una distribución estimada de valores.

**Resultados y evidencia.** Los autores comunican un **40 % de mercancías encaminadas por una vía verde acelerada** en un despliegue y estimaciones de ingresos potenciales omitidos en otra economía. No publican un protocolo independiente y reproducible para las métricas específicas del componente de valoración.

**Contribución.** Es el antecedente **funcional integrado** más cercano a una plataforma que reúna identificación de productos, antecedentes, análisis de valores y explicaciones. Su debilidad principal es la ausencia de detalle sobre algoritmos y validación de la identidad o similitud de mercancías.

## 3. Cuadro comparativo general de los ocho estudios

| N.º | Estudio y ámbito | Pregunta central | Método principal | Base empírica | Resultado comunicado | Limitación para el análisis de mercancías comparables |
|---|---|---|---|---|---|---|
| **1** | Vijayakumar (2025), India | ¿Cómo localizar operaciones históricas relevantes para riesgo de valoración? | Clustering textual, comunidades, distancias | Experiencia institucional | Modelo conceptual de comparación y alertas | No informa algoritmo específico ni métricas de comparabilidad |
| **2** | Alqaryouti et al. (2024), Dubái | ¿Qué valores declarados son estadísticamente atípicos? | Distancia euclidiana y LOF en grupos HS | 500 000 declaraciones; pruebas balanceadas | Hasta **86 %** de exactitud | HS común no demuestra mercancía equivalente |
| **3** | Chan et al. (2023), Hong Kong | ¿Cómo detectar valores anómalos según el producto? | Word2Vec, GCNN y regresión probabilística | Declaraciones; capítulos 71 y 8 | **F1 80,8 %** en valor unitario, cap. 8 | Predicción estadística sin recuperación de antecedentes individuales |
| **4** | Alwanin et al. (2026) | ¿Cómo priorizar fraude según impacto económico? | DXGBA, remuestreo, SHAP | **54 000 registros sintéticos** | **F1 49,23 %**; **87,98 %** económico al revisar 10 %, en simulación | No compara descripciones ni acredita recuperación fiscal |
| **5** | Morgero y Macedo da Silva (2025), América Latina | ¿Qué condiciones regulan las verificaciones y referencias de valor? | Revisión normativa, entrevista, encuesta | **7 países**, incluido Perú | Diferencias en confiabilidad y uso de históricos | Evidencia cualitativa, sin algoritmo |
| **6** | Bayona (2025), OMC | ¿Cómo transponer líneas arancelarias entre versiones del SA? | Reglas, exact match, TF-IDF, SBERT | 7 946 y 9 802 líneas; revisión humana | **99,6 % y 98,8 %** en el proceso completo | La tarea es transposición de nomenclaturas, no matching de DAM |
| **7** | Kim, Kim y Choi (2025), Corea | ¿Cómo recomendar códigos HS con recuperación documental? | Dense retrieval, BM25, reranking, LLM | **100 y 1 000** casos oficiales | **Top-3 HS6 49,3 %** en 1 000 casos | Clasificación HS y recuperación de documentos, no de valores |
| **8** | Outram y Swartz (2026), gestión fronteriza | ¿Cómo integrar riesgo, valor y cadenas de suministro? | Canonicalización, grafos, IA explicable | Demostraciones y despliegues reportados | **40 %** en vía verde, según autores | Falta metodología reproducible del modelo de valoración |

**Interpretación de las métricas.** La exactitud en transposición arancelaria, el F1 de detección de anomalías, la cobertura económica y la exactitud Top-3 de códigos HS **no son métricas comparables entre sí**. Cada una corresponde a una tarea, muestra y criterio de éxito diferentes. Ningún porcentaje de esta tabla mide directamente la precisión de identificar mercancías idénticas o similares en registros SIVEP.

## 4. Cuadro de aportación de cada artículo al análisis de SIVEP Inteligente

La aportación se entiende aquí como **conocimiento, evidencia o limitación relevante para el problema de investigación**; no como aprobación de una técnica, requisito de desarrollo o secuencia de implementación.

| N.º | Estudio | Aporte documentado | Relevancia específica para el problema de SIVEP | Alcance de la evidencia |
|---|---|---|---|---|
| **1** | Vijayakumar (2025) | Agrupamiento de descripciones y comparación histórica contextualizada | Fundamenta el problema de **identificar operaciones previas con mercancías potencialmente comparables** | Arquitectura conceptual, sin evaluación específica de matching |
| **2** | Alqaryouti et al. (2024) | Distancias y densidad local para identificar valores atípicos | Evidencia la diferencia entre **pertenecer a una misma categoría HS** y formar un grupo estadísticamente homogéneo | Evaluación de anomalías, no de equivalencia de productos |
| **3** | Chan et al. (2023) | Modelos de valor condicionados a descripciones comerciales | Fundamenta la importancia de **características particulares de cada mercancía** al interpretar diferencias de precio | Resultados predictivos; no determina referencias legales |
| **4** | Alwanin et al. (2026) | Clasificación conjunta y ordenación por impacto monetario | Aporta criterios de evaluación de la **utilidad operativa y capacidad de selección de riesgos** | Simulación con datos sintéticos |
| **5** | Morgero y Macedo da Silva (2025) | Distinción jurídica entre alerta, verificación y utilización de antecedentes | Delimita la **confiabilidad del valor histórico, la duda razonable y el papel del especialista** | Análisis normativo y cualitativo de prácticas latinoamericanas |
| **6** | Bayona (2025) | Comparación de TF-IDF/SBERT y documentación de errores por semejanza superficial | Aporta fundamentos para **interpretar puntuaciones textuales sin confundirlas con identidad de mercancía** | Experimento de transposición de nomenclaturas |
| **7** | Kim, Kim y Choi (2025) | Recuperación léxica y semántica combinada con reordenamiento | Aporta una referencia metodológica para la **búsqueda y ordenación de información comercial o normativa relacionada** | Evaluación de clasificación HS, no de comparabilidad para valoración |
| **8** | Outram y Swartz (2026) | Integración de identificación, contexto comercial, antecedentes y análisis de valores | Documenta una **representación funcional integral** cercana al problema de referencias de valoración | Demostraciones con algoritmos y validación parcialmente no divulgados |

En conjunto, los estudios **1, 6, 7 y 8** aportan antecedentes de recuperación y relación de productos; los **2 y 3** se concentran en la interpretación estadística de valores; el **4** analiza la selección económica de riesgos; y el **5** establece consideraciones sobre la utilización jurídica e institucional de los antecedentes. Estas contribuciones son **complementarias, no equivalentes**.

## 5. Síntesis y discusión de la evidencia

### 5.1. Similitud textual, comparabilidad y clasificación arancelaria

Los trabajos de Vijayakumar, Bayona, Kim y colegas, y Outram y Swartz coinciden en que la heterogeneidad de descripciones dificulta encontrar correspondencias entre registros comerciales. Sin embargo, estudian **objetos distintos**: agrupamiento histórico para riesgos, transposición de líneas arancelarias, recomendación de códigos HS y canonicalización de cadenas comerciales, respectivamente.

La comparación textual constituye un mecanismo útil de **búsqueda de candidatos**, pero no resuelve por sí sola la evaluación de **marca, modelo, capacidades, especificaciones, condición de la mercancía y otros atributos discriminantes**. Bayona proporciona evidencia particularmente ilustrativa: puntuaciones coseno elevadas también pueden corresponder a decisiones incorrectas.

### 5.2. El código HS como contexto, no como prueba de identidad

En el artículo de Dubái, el HS agrupa las operaciones sobre las que se calculan distancias. En Bayona y THE-RAG, la estructura arancelaria reduce el espacio de búsqueda. Estas funciones son técnicamente útiles, pero **un mismo código puede contener mercancías de precios y características muy diferentes**. El caso presentado por Chan y colegas ilustra precisamente esa heterogeneidad dentro de una categoría.

Por tanto, los estudios ofrecen evidencia a favor de **combinar información arancelaria con características del producto**, sin equiparar clasificación arancelaria con comparabilidad para los métodos de valoración.

### 5.3. Valor histórico frente a valor predicho

Alqaryouti y colegas identifican anomalías dentro de grupos históricos; Chan y colegas predicen distribuciones de valor; Outram y Swartz presentan un sistema que relaciona operaciones potencialmente comparables con valores plausibles. Los tres enfoques son diferentes:

- **Valor histórico documentado:** registro de una operación, cuya procedencia y estado de verificación deben examinarse.
- **Valor estadísticamente esperado:** salida de un modelo o distribución ajustada a datos.
- **Alerta de discrepancia:** señal para examen basada en una comparación, que no equivale a una determinación jurídica.

La investigación de Morgero y Macedo da Silva proporciona el fundamento para mantener separadas estas categorías, particularmente en relación con el valor de transacción y las verificaciones amparadas por el artículo 17.

### 5.4. Calidad de datos, validación y supervisión

Los resultados de recuperación y predicción dependen de la representación de los registros, la disponibilidad de antecedentes y la validación utilizada. El estudio de Dubái muestra sensibilidad al tamaño de los grupos; THE-RAG registra diferencias al cambiar el tamaño del contexto y al ampliar la muestra; y la investigación de DXGBA evidencia el efecto de optimizar métricas de detección en un conjunto sintético.

Los artículos no justifican interpretar una puntuación semántica, una anomalía o una probabilidad de fraude como una conclusión autónoma sobre la valoración legal. La **evidencia trazable y la evaluación del especialista** son elementos coherentes con los límites documentados en la colección.

### 5.5. Vacío de conocimiento identificado

**Dentro de estos ocho estudios no se documenta una validación reproducible y específica de la identificación de mercancías idénticas o similares en descripciones de DAM peruanas, acompañada de una verificación independiente de la idoneidad de sus valores históricos para los métodos de valoración.**

Esta es una **limitación del conjunto bibliográfico revisado**, no una afirmación de inexistencia de trabajos en toda la literatura mundial ni una declaración de originalidad científica absoluta.

## 6. Alcance y calidad de la evidencia

| Naturaleza de la publicación | Estudios | Qué permite concluir | Qué no permite concluir |
|---|---|---|---|
| Investigación experimental sobre problemas aduaneros o comerciales | **2, 3, 4 y 7** | Comportamiento de métodos en los datos y tareas evaluados | Desempeño equivalente en DAM de Perú o en valoración jurídica |
| Descripción institucional o arquitectura tecnológica | **1 y 8** | Funciones desarrolladas o reportadas y sus casos de uso | Exactitud independiente y replicabilidad de componentes no divulgados |
| Análisis jurídico-institucional cualitativo | **5** | Diferencias normativas y prácticas comunicadas por especialistas | Efectividad estadística de algoritmos o representatividad de todas las aduanas |
| Documento de trabajo técnico con verificación humana | **6** | Comparación de métodos de correspondencia en nomenclaturas | Exactitud para mercancías idénticas/similares de declaraciones de importación |

**Observaciones de lectura crítica.** Las fichas individuales conservan cuestiones relevantes para interpretar los resultados: la definición inconsistente de *precision* en el artículo 2; la composición sintética y algunas ambigüedades de etiquetas/variables en el artículo 4; una discrepancia menor entre cifras narradas y recuentos en el artículo 6; rotulaciones inconsistentes de modelo en tablas del artículo 7; y limitaciones de divulgación experimental y vinculación comercial de los autores en el artículo 8.

Los ocho textos se leyeron como **fuentes de alcance desigual**. Los porcentajes se reproducen bajo las condiciones comunicadas por sus autores; las inferencias que conectan esas publicaciones con SIVEP están identificadas como análisis de relevancia y no como resultados experimentales del proyecto.

## 7. Referencias bibliográficas y fichas ampliadas

| N.º | Referencia | Texto completo de la revisión | Publicación |
|---|---|---|---|
| 1 | Vijayakumar, S. (2025). *Technology-centric and Data-Driven Customs Risk Management for Supply Chain Security*. *World Customs Journal, 19*(1), 38–63. | [Ficha 1](01-vijayakumar-2025-india.md) | https://doi.org/10.55596/001c.131745 |
| 2 | Alqaryouti, O., Siyam, N., Shaalan, K., & Alhosban, F. (2024). *Customs Valuation Assessment Using Cluster-Based Approach*. *International Journal of Information Technology, 16*, 4243–4252. | [Ficha 2](02-alqaryouti-2024-dubai.md) | https://doi.org/10.1007/s41870-024-01821-1 |
| 3 | Chan, B., Ng, I., & Chung, N. (2023). *Anomaly Detection in Trade Declarations Using Deep Learning Techniques*. *Statistical Journal of the IAOS, 39*, 825–834. | [Ficha 3](03-chan-ng-chung-2023-hong-kong.md) | https://doi.org/10.3233/SJI-230081 |
| 4 | Alwanin, R., Ben Ismail, M. M., & Bchir, O. (2026). *Customs Fraud Detection Using a Gradient Boosting Approach for Joint Classification and Risk Estimation*. *Scientific Reports, 16*, artículo 3432. | [Ficha 4](04-alwanin-2026-dxgba.md) | https://doi.org/10.1038/s41598-025-33382-z |
| 5 | Morgero, K., & Macedo da Silva, A. C. D. (2025). *Contemporary Application of Article 17 of the Customs Valuation Agreement in Latin American Countries*. *World Customs Journal, 19*(1), 3–20. | [Ficha 5](05-morgero-macedo-2025-articulo-17.md) | https://doi.org/10.55596/001c.127239 |
| 6 | Bayona, P. (2025). *Beyond Six Digits: Automated Tariff Line HS Transposition Using Natural Language Processing*. *WTO Staff Working Paper ERSD-2025-04*. | [Ficha 6](06-bayona-2025-transposicion-hs.md) | Documento de trabajo OMC ERSD-2025-04 |
| 7 | Kim, H., Kim, G., & Choi, K. (2025). *Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework*. *The Journal of Information Systems, 34*(3), 167–189. | [Ficha 7](07-kim-kim-choi-2025-the-rag.md) | https://doi.org/10.5859/KAIS.2025.34.3.167 |
| 8 | Outram, M., & Swartz, P. (2026). *Modern Border Management: Leveraging AI Systems for Strategic Advantage*. *World Customs Journal, 20*(1), 167–189. | [Ficha 8](08-outram-swartz-2026-fronteras.md) | https://doi.org/10.55596/001c.159458 |

**Delimitación del corpus.** El séptimo estudio de esta colección es el trabajo de **Kim, Kim y Choi (2025)** sobre THE-RAG. El artículo *An Ensemble Deep Learning Framework for Automated HS Code Classification in International Trade* no forma parte de los ocho textos completos analizados.

---

*La revisión presenta evidencia bibliográfica y sus límites interpretativos. Ninguna cifra corresponde a una evaluación de desempeño de SIVEP ni puede utilizarse por sí sola para sustentar una decisión sobre el valor en aduana.*
