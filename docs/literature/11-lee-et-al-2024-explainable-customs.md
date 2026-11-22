# Artículo 11 — Lee et al.: clasificación aduanera explicable mediante evidencia documental

## Ficha bibliográfica

- **Referencia:** Lee, E., Kim, S., Kim, S., Jung, S., Kim, H., & Cha, M. *Explainable Product Classification for Customs*. La **versión examinada** es **arXiv:2311.10922v1 (18 de noviembre de 2023)**, 24 páginas; una publicación posterior aparece citada como **ACM Transactions on Intelligent Systems and Technology, 15(2), 2024**. Las cifras aquí proceden del **PDF de la versión arXiv**, no de una auditoría de cambios editoriales.
- **Fuente:** https://arxiv.org/abs/2311.10922
- **Instituciones:** KAIST, GIST, Korea Customs Service y Korea Customs Valuation and Classification Institute.
- **Objeto:** clasificación HS y recuperación de **frases normativas de sustento**; no búsqueda de transacciones históricas para valoración.
- **Pasajes principales:** Figura 5, Tabla 1, Tabla 2, Tabla 4, secciones 5–7 y Figuras 9–10.

## 1. Problema investigado

La clasificación de mercancías exige interpretar textos comerciales frente a la nomenclatura, notas explicativas, reglas y antecedentes. Un clasificador puede alcanzar alta exactitud y, aun así, entregar un código sin explicar **por qué** es pertinente.

Los autores investigan cómo vincular **recomendaciones de códigos HS** con **frases documentales** procedentes de manuales y decisiones previas, de manera que funcionarios aduaneros puedan examinar recomendaciones más allá de una puntuación numérica.

El estudio distingue dos resultados: calidad de **clasificación** y calidad de **recuperación de evidencias**. Una predicción correcta no demuestra que su explicación sea correcta ni que la evidencia recuperada sea suficiente.

## 2. Datos y cobertura

La investigación presenta **17.068 casos coreanos** de los capítulos **84, 85 y 90**, integrados por:

| Capítulo | Casos generales | Consejo HS | Comité HS |
|---|---:|---:|---:|
| 84 | 5.115 | 231 | 122 |
| 85 | 6.434 | 237 | 192 |
| 90 | 4.486 | 166 | 85 |
| **Total** | **16.035** | **634** | **399** |

Las **1.033 decisiones complejas** de Consejo/Comité incluyen fundamentos normativos para estudiar evidencia. Los autores agregan **209.635 casos internacionales**, traducidos al coreano y concentrados en los mismos capítulos.

El conjunto de clasificación contempla **163 partidas HS4** y **925 subpartidas HS6**; se reportan **201.435 ejemplos de entrenamiento, 5.000 de validación y 5.000 de prueba**. La investigación intenta mantener una secuencia temporal para evitar que decisiones posteriores se usen al evaluar anteriores.

**Limitación de reproducibilidad:** las cifras de fuentes descriptivas y conjuntos experimentales no se reconcilian exhaustivamente en el PDF; no debe inventarse una conciliación de exclusiones ni suponer acceso público a todos los casos.

## 3. Arquitectura

### Primera etapa: clasificación

Se comparan **LSTM, KoBERT, KoELECTRA y KLUE-RoBERTa** para transformar una descripción de producto en probabilidades de código HS. El modelo de clasificación es esencialmente **supervisado**, no una generación libre de códigos con un LLM conversacional.

### Segunda etapa: recuperación de fundamentos

Los autores recuperan frases del manual HS mediante dos señales:

1. **Similitud textual** entre descripción y frases de la norma, apoyada en embeddings de términos, coseno y ponderaciones IDF.
2. **Experiencia documental previa:** uso de frases en decisiones históricas sobre casos similares.

La combinación se expresa como:

```text
score(x, M) = similitud_textual(x, M) + λ × evidencia_experta(x, M)
```

En los experimentos se utiliza **λ = 0,3** y se examinan **diez antecedentes similares** para estimar la contribución de las decisiones de expertos.

El producto final consta de códigos candidatos y **fragmentos normativos existentes resaltados**. No supone que un LLM haya redactado libremente una explicación cuyo origen sea imposible de reconstruir.

## 4. Resultados de clasificación

| Modelo | Top-1 HS6 | Top-3 HS6 | Top-5 HS6 |
|---|---:|---:|---:|
| LSTM | 36,02 % | 53,46 % | 62,00 % |
| KoBERT | 78,88 % | 87,70 % | 90,06 % |
| KoELECTRA | 83,22 % | 90,99 % | 92,88 % |
| **KLUE-RoBERTa** | **86,06 %** | **93,98 %** | **95,25 %** |

**Top-3 HS6 = 93,98 %** corresponde a la tarea, capítulos, periodo y 925 clases del artículo. **No** es precisión del ranking de mercancías idénticas/similares ni medida de valoración.

### Diferencia entre casos generales y difíciles

| Casos | Top-1 HS6 | Top-3 HS6 |
|---|---:|---:|
| Generales | 86,31 % | 94,17 % |
| Complejos, Consejo/Comité | **58,70 %** | **73,17 %** |

La caída de **21 puntos porcentuales en Top-3** indica que una media favorable puede ocultar errores graves en operaciones que requieren juicio especializado.

## 5. ¿Qué calidad tienen las explicaciones?

Una prueba de decisión individual presentada para la partida **8472** obtuvo **precisión 0,75 y recall 0,75** para frases de evidencia recuperadas.

En **15 decisiones complejas** adicionales, no usadas en entrenamiento, el sistema alcanza **recall medio 0,69** respecto de frases utilizadas por especialistas. Los autores no informan una precisión media equivalente en este pequeño conjunto.

Debe evitarse presentar **69 % de recall documental** como exactitud del razonamiento jurídico o como fidelidad causal de las explicaciones al modelo de clasificación. Mide concordancia de frases recuperadas con una referencia experta delimitada.

## 6. Evaluación con especialistas aduaneros

El estudio incluye **32 funcionarios de aduanas** y una interfaz que presenta propuestas de códigos, puntuaciones y frases de sustento.

Se informa:
- **65,7 %** de participantes calificaron la utilidad con **4 o 5 sobre 5**.
- **Más del 85 %** puntuaron la exactitud percibida con **3 o más**, umbral que incluye una valoración neutral.
- Correlaciones entre utilidad y exactitud percibidas: **Pearson 0,82**, **Spearman 0,79**.
- Preferencia media: **3,17 códigos** y **6,74 frases de evidencia**.

**Auditoría editorial:** la introducción contiene una formulación de aproximadamente 85 % de utilidad, distinta del indicador de utilidad positiva **65,7 %** detallado en la encuesta. No deben mezclarse las preguntas y umbrales.

La evaluación prueba **utilidad percibida**, no una reducción de minutos de trabajo demostrada mediante experimento controlado. Los grupos de experiencia son reducidos y no representan por sí solos a todas las aduanas.

## 7. Exploración con un LLM generativo

La sección 7.3 añade diez casos exploratorios con ChatGPT: **4/5 aciertos** en un escenario con menos opciones y **3/5** en otro más amplio. Aparecen códigos inexistentes y errores de interpretación numérica.

Este ejercicio **no** constituye una comparación estadística formal con KLUE-RoBERTa, pero ilustra que una explicación plausible puede acompañar a una clasificación inventada.

## 8. Limitaciones

1. Clasificación de tres capítulos, no de toda la nomenclatura.
2. Código HS recomendado ≠ antecedente de valor legalmente comparable.
3. La recuperación de frases no prueba que representen la causa de la predicción.
4. Los 15 casos adicionales son pocos para validar exhaustivamente la explicación.
5. Estudio de usuarios sin control experimental de productividad.
6. Dependencia del idioma, las resoluciones disponibles y cambios de nomenclatura.
7. Datos/particiones no reconstruibles completamente solo con las cifras públicas.
8. Las normas y decisiones de **clasificación** no resuelven por sí solas el uso de valores históricos en valoración.

## 9. Aporte a SIVEP Inteligente

La contribución principal es **la separación entre modelo que recomienda y documentos que sustentan la recomendación**, junto con una evaluación independiente de evidencias y una prueba con profesionales.

La conexión con SIVEP se refiere a **evidencia trazable**: ID de DAM histórica, texto y atributos originales, coincidencias/diferencias, procedencia y estado de revisión del valor, y condiciones comerciales. Estas categorías son una **lectura de aplicabilidad**, no componentes implementados o medidos en el sistema coreano.

Un fundamento normativo citado puede ser verdadero y, sin embargo, insuficiente para justificar una referencia de valoración. Del mismo modo, un texto de explicación correcto no hace comparable por sí solo una mercancía.

## 10. Conclusión y vínculos

Este artículo posee pertinencia **muy alta para explicabilidad y evaluación con especialistas**; no prueba un método de identidad/similitud de mercancías.

Se relaciona con el [artículo 12](12-lee-et-al-2021-sentences-retrieval.md), antecedente de la misma línea investigadora; con [THE-RAG (7)](07-kim-kim-choi-2025-the-rag.md), que combina recuperación y generación; y con [artículo 5](05-morgero-macedo-2025-articulo-17.md), que delimita el uso de antecedentes para valoración.
