# Revisión de literatura: inteligencia artificial, riesgo y valoración aduanera

**Colección analizada:** quince trabajos de 2021–2026 sobre gestión de riesgos, comparación de descripciones comerciales, clasificación arancelaria, anomalías de valor, priorización de controles y fundamentos jurídicos de la valoración aduanera.

**Ámbito de análisis:** investigación bibliográfica vinculada con el problema de identificación de mercancías comparables y uso de antecedentes históricos en **[SIVEP Inteligente](../../README.md)**.

> **Nota de alcance.** Esta es una revisión crítica y temática de quince fuentes examinadas en texto completo; no es una revisión sistemática ni un metaanálisis. Las contribuciones a SIVEP descritas aquí constituyen **relaciones analíticas entre la literatura y el problema de investigación**, no decisiones de implementación. Cada artículo dispone de una [ficha ampliada](#2-estudios-revisados) con sus datos, metodología, resultados y limitaciones.

## 1. Objeto de la revisión

La revisión examina cómo la literatura especializada aborda siete problemas relacionados: **(i)** la extracción y normalización de atributos de productos; **(ii)** la recuperación de mercancías o registros a partir de descripciones heterogéneas; **(iii)** la aplicación de reglas de clasificación y sus errores; **(iv)** el análisis de valores históricos y detección de anomalías; **(v)** la priorización de operaciones según riesgo; **(vi)** la explicabilidad y trazabilidad de recomendaciones; y **(vii)** los límites jurídicos e institucionales al utilizar antecedentes de valoración.

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

### 2.9. [Brinkmann, Baumann y Bizer (2024) — extracción y normalización de atributos](09-brinkmann-baumann-bizer-2024-wdc-pave.md)

**Problema.** Las descripciones de comercio electrónico contienen atributos de productos con abreviaturas, unidades heterogéneas y numerosos valores ausentes.

**Método.** Evalúa LLM frente a extractores especializados sobre **WDC-PAVE: 565 productos, 4.687 pares atributo–valor y cinco categorías**; distingue extracción, normalización y su ejecución conjunta.

**Resultados y evidencia.** GPT-4 obtiene hasta **91,32 % de F1** en extracción y normalización conjunta. La conversión de unidades alcanza **83,50 %** en la tarea conjunta y **97,89 %** con valores previamente extraídos.

**Contribución.** Documenta cómo obtener y estandarizar **características técnicas estructuradas**, advirtiendo que generalizar puede perder información. No evalúa identidad de mercancías ni valoración.

### 2.10. [Brinkmann, Shraga y Bizer (2024) — ExtractGPT y valores no vistos](10-brinkmann-shraga-bizer-2024-extractgpt.md)

**Problema.** Extraer atributos desde productos de nuevas marcas y versiones cuando existen pocos datos etiquetados y muchos valores no observados.

**Método.** Compara prompts, esquemas de atributos, demostraciones, Llama, GPT y fine-tuning sobre **OA-Mine y AE-110K**.

**Resultados y evidencia.** ExtractGPT obtiene **84,9 % de F1 promedio** y **72,6 %** sobre valores no vistos en la configuración de datos reducidos; el segundo valor no representa precisión global.

**Contribución.** Aporta evidencia sobre **generalización a características nuevas** y límites del ajuste especializado; no estudia normalización como tarea principal ni comparabilidad legal de productos.

### 2.11. [Lee y colaboradores (versión 2023; edición 2024) — clasificación explicable para aduanas](11-lee-et-al-2024-explainable-customs.md)

**Problema.** Recomendar códigos HS sin fundamentos verificables resulta insuficiente para apoyar decisiones de especialistas.

**Método.** Clasificadores Transformer y recuperación de frases del manual HS apoyada en decisiones previas; evaluación de **925 subpartidas**, **5.000 casos de prueba** y una encuesta a **32 funcionarios**.

**Resultados y evidencia.** KLUE-RoBERTa alcanza **93,98 % Top-3 HS6**; la recuperación de evidencia presenta **recall medio de 0,69** en 15 casos complejos; **65,7 %** de funcionarios valoran positivamente la utilidad bajo el umbral explicitado.

**Contribución.** Separa **recomendación y evidencia documental**, e incorpora evaluación con expertos. No recupera transacciones de valor comparables.

### 2.12. [Lee y colaboradores (2021) — clasificación de mercancías con recuperación de frases](12-lee-et-al-2021-sentences-retrieval.md)

**Problema.** Clasificar productos del **capítulo 85** con apoyo documental a partir de descripciones comerciales.

**Método.** Tres etapas: **KoELECTRA HS4**, recuperación de frases normativas mediante **AIR** y KoELECTRA HS6; uso de casos históricos de clasificación.

**Resultados y evidencia.** La variante **sin frases** alcanza **95,5 % Top-3 HS6** y la variante **con frases**, **93,7 %**. Por tanto, añadir evidencia no mejora automáticamente la métrica de clasificación.

**Contribución.** Antecedente de la línea de investigación del artículo 11; muestra la necesidad de **evaluar separadamente el clasificador y el contexto agregado**.

### 2.13. [Ravi y colaboradores — Text2Trade y recuperación contrastiva](13-ravi-et-al-text2trade-mnrl-mcd.md)

**Problema.** Recuperar códigos HS asociados a descripciones comerciales sin depender únicamente de coincidencias literales, y examinar la estabilidad de los resultados.

**Método.** Bi-encoder **Sentence-BERT** especializado con **MNRL** y reordenamiento mediante **Monte Carlo Dropout (MCD)**; **171.247 registros de entrenamiento**.

**Resultados y evidencia.** El modelo sin MCD obtiene **97,0 % Recall@10 en 37.794 consultas**; la variante MNRL+MCD obtiene **97,8 % en solo 1.000 consultas**. Son pruebas distintas.

**Contribución.** Sustenta el aprendizaje contrastivo y la evaluación de ranking, pero las etiquetas son **códigos HS**, no productos idénticos o similares. La versión del PDF conserva metadatos editoriales de plantilla.

### 2.14. [Pain (2021) — clasificación HS desde documentos EDI](14-pain-2021-clasificacion-transfer-learning.md)

**Problema.** Los documentos comerciales EDI mezclan descripciones de mercancías con campos logísticos y datos no uniformes.

**Método.** Parser y preprocesamiento, seguido de NER, clasificadores con TF-IDF y búsqueda semántica mediante **USE, BERT, RoBERTa, InferSent y XLM-R**, sobre **33.019 transacciones** de cuatro transportistas.

**Resultados y evidencia.** El mejor conjunto obtiene **70,10 % de «precisión de recomendación@10»**, una **métrica particular semejante a Hit@10**, no Precision@10 estándar.

**Contribución.** Aporta evidencia sobre **limpieza de documentos y variabilidad de embeddings**; también muestra el riesgo de eliminar números o atributos esenciales para comparar mercancías. Es una **tesis de maestría**, no artículo de revista.

### 2.15. [Yang y colaboradores (2025) — HSCodeComp y aplicación de reglas](15-yang-et-al-2025-hscodecomp.md)

**Problema.** Los agentes de búsqueda pueden recuperar normas y antecedentes pero **aplicar incorrectamente reglas jerárquicas** ante descripciones comerciales incompletas o contradictorias.

**Método.** Benchmark de **632 productos**, 27 capítulos HS, anotación por especialistas y comparación de modelos LLM/VLM, agentes abiertos y comerciales.

**Resultados y evidencia.** El mejor agente alcanza **46,83 % de exactitud a diez dígitos**; los autores reportan **95 %** como referencia humana, aunque sin detallar un protocolo enteramente simétrico de comparación.

**Contribución.** Taxonomía de fallos: **atributos mal interpretados, decisiones prematuras, normas incorrectamente aplicadas y explicaciones plausibles pero falsas**. No estudia directamente la valoración aduanera.

## 3. Cuadro comparativo general de los quince estudios

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
| **9** | Brinkmann, Baumann y Bizer (2024); ADBIS | ¿Cómo extraer y normalizar características de productos? | LLM, prompting, normalización | 565 productos, 4.687 pares WDC-PAVE | **F1 91,32 %**, extracción y normalización conjunta | No mide identidad/comparabilidad de mercancías |
| **10** | Brinkmann, Shraga y Bizer (2024); ExtractGPT | ¿Cómo extraer valores de atributo no vistos? | GPT, Llama, prompting y fine-tuning | OA-Mine y AE-110K | **F1 84,9 %** general; **72,6 %** en valores nuevos con datos reducidos | Extracción ≠ correspondencia de productos |
| **11** | Lee et al. (2023/2024); Corea | ¿Cómo recomendar HS con evidencia para un funcionario? | Transformer y recuperación normativa | 925 subpartidas, 5.000 pruebas, 32 funcionarios | **Top-3 HS6 93,98 %**; evidencia recall 0,69 en 15 casos | Clasificación y frases normativas, no referencias de valor |
| **12** | Lee et al. (2021); Corea | ¿Cómo incorporar frases del manual en clasificación? | KoELECTRA, AIR, antecedentes | Capítulo 85, 265 subpartidas | **95,5 % Top-3 sin frases; 93,7 % con frases** | Añadir contexto no garantiza mejorar resultados |
| **13** | Ravi et al.; Text2Trade, manuscrito | ¿Cómo recuperar códigos y medir estabilidad del ranking? | SBERT, MNRL, MCD | 171.247 entrenamiento; 37.794 prueba | **97,0 % Recall@10** sin MCD en prueba completa; **97,8 %** con MCD en 1.000 | Matching de códigos, no de mercancías; versión no definitiva |
| **14** | Pain (2021); tesis, Canadá | ¿Cómo leer EDI ruidoso y recuperar códigos HS? | Parsing, limpieza, USE/XLM-R y STS | 33.019 transacciones de transportistas | **70,10 % «recomendación@10»** en mejor grupo | Métrica no convencional; limpieza puede perder atributos |
| **15** | Yang et al. (2025); HSCodeComp | ¿Pueden los agentes aplicar reglas jerárquicas? | Benchmark, LLM/VLM y agentes con búsqueda | 632 productos anotados | **46,83 % exactitud HS10**; humano 95 % reportado | No estima valor ni evalúa identidad de mercancías |

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
| **9** | Brinkmann, Baumann y Bizer | Extracción y normalización de atributos con medidas separadas | Evidencia sobre **qué características fueron expresadas y cómo se transforman** | WDC-PAVE; sin emparejamiento de mercancías |
| **10** | Brinkmann, Shraga y Bizer | Extracción con valores no observados y comparación entre corpus | Relevancia de **marca, modelo y capacidades nuevas** para representar productos | Comercio electrónico; no demuestra identidad comercial |
| **11** | Lee et al., clasificación explicable | Recuperación de sustento documental y evaluación con funcionarios | Demuestra la necesidad de **evidencias identificables y examinables** | Frases de clasificación HS; no valor histórico |
| **12** | Lee et al., recuperación de frases | Efectos comparados de agregar o no evidencia normativa | Distingue **calidad de la recomendación** y **utilidad de sus fundamentos** | Mismo programa investigador que 11; capítulo 85 |
| **13** | Ravi et al., Text2Trade | Especialización de embeddings y estabilidad de ranking | Distingue la **recuperación de candidatos** de su **comparabilidad comercial** | Etiquetas HS y resultados sobre pruebas de distinto tamaño |
| **14** | Pain, EDI | Preparación de descripciones ruidosas y comparación entre modelos STS | Muestra por qué la limpieza puede **conservar o eliminar atributos decisivos** | Tesis con documentos confidenciales y métrica singular |
| **15** | Yang et al., HSCodeComp | Evaluación de agentes en reglas, contradicciones y fallos interpretativos | Documenta el riesgo de **antecedentes válidos pero inaplicables** y explicaciones erróneas | Exactitud de clasificación HS10, no valoración |

En conjunto, los estudios **1, 6, 7, 8, 13 y 14** aportan antecedentes de búsqueda y relación de textos/productos; **9 y 10** documentan extracción de atributos; **11 y 12** distinguen clasificación y evidencia; **15** examina fallos de aplicación de reglas; **2 y 3** analizan valores; **4** investiga priorización; y **5** delimita el marco jurídico-institucional. Las contribuciones son **complementarias, no equivalentes**, y algunas publicaciones comparten autores y datos.

## 5. Síntesis y discusión de la evidencia

### 5.1. De texto no estructurado a atributos comparables

Los artículos **9 y 10** investigan la extracción de características, mientras que el **14** muestra las dificultades de depurar documentos comerciales EDI. En conjunto evidencian que reconocer una mercancía requiere una representación que preserve **marca, modelo, composición, capacidad, dimensiones, estado y otras características discriminantes**, cuando estas existan en las fuentes.

Una salida estructurada o JSON válida no garantiza extracción correcta. Normalizar unidades puede conservar información, pero **generalizar atributos o eliminar números** puede destruir diferencias relevantes. El artículo **15** demuestra además que los agentes pueden **interpretar mal atributos ya presentes**, particularmente ante contradicciones entre título y ficha técnica.

### 5.2. Similitud textual, embeddings y recuperación de códigos

Los estudios **1, 6, 7, 13 y 14** ilustran aproximaciones de clustering, TF-IDF, SBERT, BM25, recuperación híbrida, MNRL y similitud coseno. Sus objetivos y etiquetas no son iguales: agrupamiento para riesgo, **transposición de líneas arancelarias**, **clasificación HS** o **ranking de códigos**, no necesariamente correspondencia entre operaciones de la misma mercancía.

Bayona (6) documenta que un **coseno elevado puede corresponder a una relación incorrecta**. Text2Trade (13) demuestra que un bi-encoder especializado puede recuperar códigos con gran eficacia, pero un positivo definido por el **mismo HS** no acredita identidad comercial de dos productos que comparten clasificación.

El código arancelario puede ser **contexto para la búsqueda** sin constituir por sí solo un criterio suficiente para distinguir mercancías idénticas, similares o no comparables.

### 5.3. Documentos recuperados y aplicación de reglas

Los artículos **11 y 12** separan la predicción de códigos de las frases normativas que la sustentan. El 12 incluso muestra que incorporar frases **reduce la exactitud Top-3** bajo la configuración estudiada; el 11 evalúa de forma independiente la coincidencia de las evidencias con decisiones expertas y la utilidad percibida por funcionarios.

HSCodeComp (15) va más allá del ranking: muestra que agentes con búsqueda pueden recuperar reglas y antecedentes y **aplicarlos mal**, crear explicaciones plausibles pero falsas o priorizar un título comercial sobre un atributo técnico contradictorio. La existencia y vigencia de una referencia **no implican su pertinencia** para el caso.

El artículo **5** recuerda que los antecedentes empleados para **riesgo** y para **métodos de valoración** tienen exigencias distintas de confiabilidad y comparabilidad. La explicación por IA no equivale a una determinación jurídica.

### 5.4. Valor histórico, anomalía y selección de riesgos

El estudio de Dubái (2) busca anomalías dentro de grupos HS; Hong Kong (3) predice rangos específicos de producto; DXGBA (4) prioriza operaciones sobre **datos sintéticos**; y la exposición integrada de Outram y Swartz (8) relaciona antecedentes comerciales con estimaciones de valor.

Estas salidas no son intercambiables:

- **Valor histórico:** dato de transacción cuyo origen, condición y validación importan.
- **Estimación de valor:** resultado probabilístico o estadístico.
- **Alerta de anomalía:** indicio para revisar.
- **Decisión de valoración:** actuación del especialista bajo procedimiento y normas aplicables.

La ausencia de revisión aduanera no demuestra que un valor declarado sea falso ni que haya sido confirmado.

### 5.5. Comparación de cifras y calidad de evaluación

Los porcentajes informados miden tareas diferentes: **F1 de extracción de atributos (9–10)**, **Top-k de clasificación (7, 11–12)**, **Recall@k de códigos (13)**, **métricas particulares de recomendación (14)**, **exactitud HS10 (15)**, **anomalías de valor (2–3)** y **priorización económica sintética (4)**. No procede crear un ranking de «mejor IA» entre esos porcentajes.

Existen además relaciones de dependencia bibliográfica: los artículos **11 y 12** pertenecen a una línea de investigación de autores/instituciones compartidos; ello no proporciona dos validaciones independientes de una misma conclusión. La consistencia de la etiqueta, partición temporal, dificultad del caso y reproducibilidad condicionan todas las inferencias.

### 5.6. Vacío de conocimiento que permanece en el corpus

**Ninguno de los quince trabajos examinados presenta una validación reproducible, específica y conjunta de (i) identificación de mercancías idénticas o similares a partir de descripciones de DAM peruanas y (ii) idoneidad y trazabilidad de sus antecedentes históricos para los métodos de valoración.**

Esta afirmación se limita **al corpus de quince textos revisados**; no es una declaración de inexistencia mundial de estudios semejantes ni una prueba automática de originalidad científica.

## 6. Alcance y calidad de la evidencia

| Tipo de evidencia | Estudios | Conclusión legítima | Restricción |
|---|---|---|---|
| Estudios experimentales aduaneros, de clasificación o producto | **2, 3, 4, 7, 9, 10, 11, 12 y 15** | Resultados para la tarea, corpus y métricas publicados | No trasladar sin validación a DAM, identidad o valoración |
| Estudios institucionales o de arquitectura integrada | **1 y 8** | Casos de uso y funciones descritas por autores | La presentación no sustituye pruebas abiertas de cada algoritmo |
| Investigación jurídico-institucional cualitativa | **5** | Condiciones jurídicas y prácticas comunicadas en siete países | No mide eficacia computacional |
| Documento de trabajo técnico con verificación de correspondencias | **6** | Comparación TF-IDF/SBERT y reglas sobre líneas arancelarias | No estudia identidad de mercancías |
| Manuscrito de investigación con información editorial incompleta | **13** | Experimentos MNRL/MCD en muestras concretas | Estado editorial y reproducibilidad requieren cautela |
| **Tesis de maestría** | **14** | Estudio extenso sobre EDI y embeddings con datos operativos | Datos confidenciales y métrica de recomendación no convencional |

**Observaciones de auditoría bibliográfica:** (2) definición de “precision” ambigua; (4) datos sintéticos y variable económica discutible; (6) diferencia menor entre porcentaje narrado y recuentos; (7) rotulación inconsistente de modelo; (8) protocolos parciales de validación; (9) ejemplo de conversión numérica posiblemente erróneo; (11) discrepancia sobre porcentaje de utilidad; (12) empeoramiento Top-3 al añadir frases; (13) cifra de 97,8 % medida en 1.000 casos, no en la prueba completa, y metadatos de plantilla; (14) “precisión de recomendación” no equivalente a Precision@k; (15) referencia humana del 95 % sin protocolo experimental simétrico plenamente descrito.

Las fichas individuales identifican **qué resulta medido y qué es inferencia de aplicabilidad**. No se incorporan PDF completos, información comercial reservada ni datos aduaneros identificables al repositorio público.

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
| 9 | Brinkmann, A., Baumann, N., & Bizer, C. (2024). *Using LLMs for the Extraction and Normalization of Product Attribute Values*. *ADBIS 2024*, 217–230 (versión arXiv:2403.02130v4). | [Ficha 9](09-brinkmann-baumann-bizer-2024-wdc-pave.md) | https://arxiv.org/abs/2403.02130 |
| 10 | Brinkmann, A., Shraga, R., & Bizer, C. (2024). *ExtractGPT: Exploring the Potential of Large Language Models for Product Attribute Value Extraction* (arXiv:2310.12537v5). | [Ficha 10](10-brinkmann-shraga-bizer-2024-extractgpt.md) | https://arxiv.org/abs/2310.12537 |
| 11 | Lee, E., Kim, S., Kim, S., Jung, S., Kim, H., & Cha, M. *Explainable Product Classification for Customs*. Versión examinada arXiv:2311.10922v1 (2023); edición posterior referenciada en *ACM TIST* (2024). | [Ficha 11](11-lee-et-al-2024-explainable-customs.md) | https://arxiv.org/abs/2311.10922 |
| 12 | Lee, E., et al. (2021). *Classification of Goods Using Text Descriptions With Sentences Retrieval* (arXiv:2111.01663v1). | [Ficha 12](12-lee-et-al-2021-sentences-retrieval.md) | https://arxiv.org/abs/2111.01663 |
| 13 | Ravi, M., Howard, J., Kenneally, G., & Fleischer, A. *Text2Trade: A Semantic Search System with Monte Carlo Dropout Uncertainty Quantification for HS Code Retrieval*. Manuscrito examinado, indicación CHIIR '26 sin metadatos editoriales definitivos. | [Ficha 13](13-ravi-et-al-text2trade-mnrl-mcd.md) | Manuscrito suministrado; versión editorial no confirmada |
| 14 | Pain, K. (2021). *Harmonized System Code Classification Using Transfer Learning with Pre-Trained Weights*. Tesis de maestría, Dalhousie University. | [Ficha 14](14-pain-2021-clasificacion-transfer-learning.md) | Tesis suministrada |
| 15 | Yang, Y., Lan, T., Jia, Q., et al. (2025). *HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application* (arXiv:2510.19631v1). | [Ficha 15](15-yang-et-al-2025-hscodecomp.md) | https://arxiv.org/abs/2510.19631 |

**Delimitación del corpus.** El séptimo estudio de esta colección es el trabajo de **Kim, Kim y Choi (2025)** sobre THE-RAG. El artículo *An Ensemble Deep Learning Framework for Automated HS Code Classification in International Trade* no forma parte de los quince textos completos analizados.

---

*La revisión presenta evidencia bibliográfica y sus límites interpretativos. Ninguna cifra corresponde a una evaluación de desempeño de SIVEP ni puede utilizarse por sí sola para sustentar una decisión sobre el valor en aduana.*
