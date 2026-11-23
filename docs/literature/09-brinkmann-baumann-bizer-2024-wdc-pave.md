# Artículo 9 — Brinkmann, Baumann y Bizer (2024): extracción y normalización de atributos de productos

## Ficha bibliográfica y naturaleza de la evidencia

- **Referencia:** Brinkmann, A., Baumann, N., & Bizer, C. (2024). *Using LLMs for the Extraction and Normalization of Product Attribute Values*. **ADBIS 2024**, pp. 217–230 (versión examinada arXiv:2403.02130v4, 15 de julio de 2024).
- **Fuente:** https://arxiv.org/abs/2403.02130
- **Institución:** Universidad de Mannheim, Alemania.
- **Tipo:** investigación experimental sobre extracción y normalización de características de productos de comercio electrónico; **no** identifica directamente mercancías idénticas/similares para valoración aduanera.
- **Fuente primaria examinada:** PDF de 14 páginas suministrado para esta revisión. Secciones 2–4, Tablas 1–8 y Figura 1.

## 1. Pregunta de investigación

Los títulos y descripciones de productos contienen características útiles, pero de forma no estandarizada: abreviaturas de fabricantes, denominaciones heterogéneas, medidas en distintas unidades, identificadores con guiones y atributos ausentes. Los autores examinan si los LLM pueden recuperar **pares atributo–valor** y convertir esos valores a representaciones uniformes, incluso en categorías diversas y con relativamente pocos ejemplos etiquetados.

El estudio separa tres tareas que no deben confundirse:

1. **Extracción:** identificar el valor presente en el texto para cada atributo del esquema.
2. **Extracción y normalización conjunta:** localizar el valor y devolverlo directamente en forma normalizada.
3. **Normalización independiente:** dado un valor ya extraído, expresarlo en la forma normalizada pertinente.

Una salida de extracción correcta no garantiza que la normalización también lo sea; la segunda operación puede requerir conocimiento de unidades, equivalencias de nombres o niveles de generalización.

## 2. Datos: WDC-PAVE

El conjunto **WDC-PAVE** fue construido a partir del corpus Web Data Commons de productos en sitios web que emplean `schema.org`. Los autores revisaron manualmente los atributos y conservaron versiones extraídas y normalizadas.

| Categoría | Productos | Pares atributo–valor |
|---|---:|---:|
| Hogar y jardín | 142 | 1.136 |
| Computadoras y accesorios | 174 | 1.914 |
| Alimentación | 32 | 160 |
| Productos de oficina | 118 | 1.180 |
| Joyería | 99 | 297 |
| **Total** | **565** | **4.687** |

El corpus procede de **59 sitios web**, incluye **37 atributos distintos**, **2.011 valores únicos** y **1.244 valores únicos tras normalizar**. Aproximadamente **45 %** de los pares contienen **`n/a`**, porque el atributo no aparece en el título o la descripción: esto importa para medir falsas extracciones o valores inventados.

La partición indicada es de **211 productos / 1.750 pares para entrenamiento y ejemplos** y **354 productos / 2.937 pares para prueba**; se estratifica por categoría. La evaluación no demuestra generalización a DAM en español ni a nuevos sitios comerciales independientes.

## 3. Las cuatro operaciones de normalización

La Tabla 2 diferencia:

| Operación | Ejemplo funcional | Riesgo para la comparabilidad |
|---|---|---|
| **Expansión de nombres** | `HP` → `Hewlett-Packard` | Confundir marcas o razones sociales distintas |
| **Generalización** | `Neon Lime Green` → `Green` | **Perder especificidad del producto** |
| **Conversión de unidades** | `20 lb` → `9,06 kg` | Errores numéricos o de unidad |
| **Transformación de cadena** | Retirar guiones de un identificador | Unir o modificar modelos distintos |

La Figura 1 ilustra un disco duro descrito como `3TB ... 7.2K rpm ... 3.5-inch`: se identifican atributos y se normaliza, entre otros, la velocidad a **7.200 rpm**. El esquema permite comparar representaciones heterogéneas del mismo atributo, pero **no comprueba identidad de dos productos**.

**Nota de auditoría:** la Tabla 2 contiene un ejemplo de conversión de `0.31 oz` a `879 g`, que no corresponde a una conversión ordinaria de onzas de masa. Debe registrarse como posible error editorial, no reutilizarse como equivalencia correcta.

## 4. Modelos y procedimiento

Se comparan **GPT-3.5 Turbo** (`gpt-3.5-turbo-16k-0613`) y **GPT-4** (`gpt-4-0613`) con **SU-OpenTag, AVEQA y MAVEQA**. Los LLM se aplican por prompting, **sin fine-tuning** en este experimento.

El prompt puede incorporar nombres y definiciones de atributos, formato JSON, **valores de ejemplo** y **demostraciones resueltas**. Para seleccionar demostraciones relacionadas con el producto consultado, se utilizan embeddings `text-embedding-ada-002` y similitud coseno. Este uso de embeddings consiste en recuperar **ejemplos de extracción**, no en verificar identidad comercial entre mercancías.

El protocolo mide **precisión, recall y F1** de atributos con correspondencia a la anotación de referencia. También analiza tokens, tiempo y costo en ciertas configuraciones de demostraciones.

## 5. Resultados

### Extracción directa

| Sistema | Mejor F1 comunicado |
|---|---:|
| **GPT-4** | **90,54 %** |
| GPT-3.5 Turbo | 88,02 % |
| AVEQA | 80,83 % |
| MAVEQA | 65,10 % |
| SU-OpenTag | 60,44 % |

La configuración destacada de GPT-4 usa **diez valores de ejemplo y diez demostraciones**. La ventaja frente a AVEQA es de **9,71 puntos porcentuales**, bajo las condiciones y tamaños de entrenamiento del estudio; no es una comparación universal de modelos.

### Extracción y normalización conjunta con GPT-4

| Valores de ejemplo | Demostraciones | F1 |
|---:|---:|---:|
| 0 | 0 | 74,19 % |
| 10 | 0 | 85,60 % |
| 10 | 3 | 91,18 % |
| **10** | **5** | **91,32 %** |
| 10 | 10 | 91,31 % |

**Resultado central:** el mejor F1 de **91,32 %** corresponde a extracción y normalización conjunta, y más demostraciones no garantizan mejora adicional.

### Resultados según operación de normalización

| Operación | Extracción + normalización conjuntas | Normalización de valores previamente extraídos |
|---|---:|---:|
| Expansión de nombres | 98,27 % | 99,12 % |
| Generalización | 88,56 % | 90,72 % |
| **Conversión de unidades** | **83,50 %** | **97,89 %** |
| Transformación de cadenas | 95,19 % | 99,32 % |

La normalización independiente con GPT-4 alcanza hasta **96,21 % F1** (diez valores y diez demostraciones). La conversión de unidades es especialmente sensible cuando se combina con extracción, dato compatible con la conveniencia de validar cálculos por métodos distintos de una generación libre.

## 6. Limitaciones y amenazas a la validez

1. **Procedencia:** textos de comercio electrónico en inglés, no de declaraciones aduaneras; la transferencia entre dominios no fue evaluada.
2. **Escala y categorías:** 565 productos y cinco categorías; representatividad aduanera no demostrada.
3. **Etiqueta y métrica:** F1 de atributos, **no** Precision@k de productos comparables.
4. **Ausencias:** el tratamiento correcto de `n/a` resulta esencial para evitar alucinación de características.
5. **Pérdida de información:** generalización de atributos puede eliminar diferencias materiales entre versiones de un producto.
6. **Errores numéricos:** algunas conversiones son difíciles incluso para GPT-4.
7. **Sin correspondencia entre productos:** no construye pares etiquetados *idéntico/similar/no comparable*.
8. **Reproducibilidad:** versiones de API y corpus condicionan los resultados; no se certifica estabilidad bajo modelos posteriores.

## 7. Contribución científica y límites de interpretación

El artículo separa empíricamente **extracción**, **normalización conjunta** y **normalización de valores previamente extraídos**. Esa distinción permite identificar fallos específicos en conversiones, generalizaciones y ausencia de información en las descripciones.

La normalización no siempre conserva todas las características del producto: una categoría de color más general, la alteración de un identificador o un cálculo de unidades incorrecto pueden modificar información relevante. El estudio **no etiqueta pares de productos como idénticos o similares**, y sus métricas F1 no son medidas de correspondencia entre mercancías.

## 8. Relación con el corpus revisado

Complementa el [artículo 10](10-brinkmann-shraga-bizer-2024-extractgpt.md), que estudia principalmente extracción y valores no vistos, el [6](06-bayona-2025-transposicion-hs.md), que muestra los límites de la similitud coseno, y el [15](15-yang-et-al-2025-hscodecomp.md), que documenta fallos al **interpretar** atributos incluso cuando están disponibles.

**Conclusión:** evidencia experimental pertinente para **extracción y normalización**, no para identidad comercial/jurídica de mercancías ni selección de referencias de valoración.
