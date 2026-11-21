# Artículo 8 — Outram y Swartz (2026): gestión fronteriza moderna e IA sobre cadenas comerciales

## Ficha bibliográfica

**Referencia:** Outram, M., & Swartz, P. (2026). *Modern Border Management: Leveraging AI Systems for Strategic Advantage*. **World Customs Journal, 20**(1), 167–189.  
**DOI:** https://doi.org/10.55596/001c.159458  
**Autores y afiliaciones:** Michael Outram (ex Commissioner de Australian Border Force) y Peter Swartz (Chief Science Officer de Altana; vinculado también a University of Victoria).  
**Tipo:** sección **Special Reports, Reviews and Commentaries**; exposición estratégica con demostraciones de una tecnología comercial, no estudio experimental independiente y completamente reproducible.  
**Fuente examinada:** PDF completo proporcionado; Figuras 1–2 (grafos), 5 (impacto económico), 6 (clasificación y explicación) y **7 (comparación de valores de neumáticos)**, pp. 176–181.

## 1. Problema planteado

Los autores sostienen que el control aduanero basado únicamente en los datos declarados en frontera pierde parte del contexto comercial. Las cadenas de suministro incluyen fabricantes, proveedores de varios niveles, intermediarios, operadores logísticos y otras entidades, con datos dispersos entre instituciones y sistemas.

Este entorno dificulta:
- Diferenciar operaciones legítimas de cadenas de suministro asociadas a infracciones.
- Reconocer empresas y productos escritos con diferentes denominaciones.
- Verificar clasificación y valoración en función de características y antecedentes reales.
- Priorizar la inspección con recursos limitados.
- Facilitar el despacho de operaciones de bajo riesgo.

La propuesta consiste en **ampliar la unidad analítica**: no evaluar solamente una declaración, sino relacionarla con su **producto, operadores y cadena comercial**.

## 2. Arquitectura conceptual

El artículo describe sistemas de IA que pueden:
1. Recibir información de declaraciones, embarques y otras fuentes.
2. **Canonicalizar** entidades: consolidar variantes de nombres, direcciones y descripciones de mercancías bajo representaciones consistentes.
3. Construir un **grafo** de productos, empresas y relaciones comerciales.
4. Aplicar modelos de análisis de riesgo, clasificación y valoración.
5. Presentar **explicaciones y evidencia** para justificar una recomendación.
6. Permitir análisis federado cuando los datos se encuentran en organizaciones distintas.

La canonicalización no constituye por sí sola un criterio de **mercancía idéntica**: estandarizar «denim pant» o reconocer una categoría HS ayuda al análisis, pero no demuestra identidad de marca, modelo, composición y demás características particulares.

### Normalización de entidades

La **Tabla 1, p. 175** presenta ejemplos multilingües de productos, nombres de empresas y direcciones. Un ejemplo de pantalón de mezclilla describe composición textil (90 % algodón, 7 % tencel, 3 % elastano), y el sistema asocia el texto a un código nacional. También se muestra una descripción en árabe de reactivos de grupos sanguíneos.

La lección aplicable a SIVEP es distinguir:
- **Normalización de la descripción comercial**.
- **Identidad/correspondencia de producto concreto**.
- **Clasificación arancelaria**.
- **Comparabilidad comercial y jurídica para valoración**.

Estos son problemas relacionados, pero no equivalentes.

### Grafos de cadena comercial

Las Figuras 1 y 2 muestran vínculos entre fabricantes, proveedores y otras entidades. Los autores utilizan estas relaciones para contextualizar alertas que serían difíciles de detectar examinando declaraciones de forma aislada.

**Limitación:** la publicación no identifica con suficiente precisión los algoritmos de *entity resolution*, construcción de grafos, entrenamiento y validación de enlaces.

## 3. Componente más próximo a SIVEP: detección de discrepancias de valoración

La **sección 5.2** y, principalmente, la **Figura 7, p. 181**, muestran un ejemplo asociado a **neumáticos**. El sistema reúne embarques históricos potencialmente comparables y presenta una **distribución estimada de valores plausibles**, que luego se contrasta con el valor declarado.

En términos funcionales:

```text
Producto y declaración
    ↓
Identificación/canonicalización y contexto de suministro
    ↓
Búsqueda de operaciones históricas comparables
    ↓
Estimación de valores plausibles y comparación con declaración
    ↓
Señal de posible discrepancia + explicación y antecedentes
    ↓
Revisión o facilitación según gestión de riesgos
```

Los autores afirman que las explicaciones pueden alinearse con métodos del **Acuerdo de Valoración de la OMC**, incluidos los referentes a mercancías idénticas o similares.

**Pero no se divulga**:
- El algoritmo exacto para decidir identidad/similitud entre embarques.
- Las características obligatorias ni sus pesos.
- El modelo que genera la distribución de precios.
- Los intervalos de calibración o umbrales de alerta.
- Las métricas de matching ni un conjunto de verdad de terreno.
- El código, los datos históricos o un experimento reproducible.

Por ello, la Figura 7 constituye una **demostración visual funcional**, no validación independiente de la eficacia del comparador o del modelo de valor.

## 4. Resultados operativos comunicados

### Facilitación del comercio

El artículo afirma que en una economía importante un sistema de puntuación de confianza posibilitó dirigir **40 % de las mercancías a un canal verde de paso acelerado**, manteniendo simultáneamente selección de riesgos. Una nota atribuye el resultado a despliegue operativo y pruebas retrospectivas frente a resultados de inspección.

**Precaución:** no se publican las matrices de confusión, el tamaño de los grupos de prueba o un protocolo completo para reproducir esa cifra. Debe citarse como **resultado reportado por los autores**, no como precisión comprobada del modelo.

### Estimación de ingresos potencialmente omitidos

La **Figura 5, p. 179**, presenta un análisis económico de una economía no identificada. Para una proporción de revisión del orden de **8,1 %**, se señala un potencial anual de aproximadamente **US$ 1 100 millones**. La figura examina escenarios y bandas de incertidumbre.

La cifra es un **potencial estimado** en el estudio; **no** hay prueba documental de que esa cantidad haya sido determinada en procedimientos firmes o efectivamente cobrada.

### Clasificación: exactitud y cobertura

La **Figura 6a** muestra el compromiso entre **porcentaje de clasificaciones automatizadas** y **exactitud**: al exigir mayor confianza y abstenerse en casos difíciles puede aumentar la exactitud del subconjunto automatizado.

En SIVEP, una decisión de **no recomendar antecedente** cuando la evidencia sea insuficiente puede ser tan importante como ofrecer un candidato de baja calidad.

## 5. IA generativa, explicaciones y fuentes

El artículo discute el uso combinado de modelos predictivos, sistemas de lenguaje, RAG y relaciones entre entidades. La **Figura 6b** ilustra explicaciones normativas de clasificación.

**Diferencia que debe mantenerse:** una explicación textual o un grafo plausible no sustituyen documentos verificables. Para SIVEP la salida debe anclar cada afirmación de comparabilidad a **atributos y DAM históricas concretas**, y separar una **estimación estadística** de un **valor declarado/verificado**.

## 6. Fortalezas y limitaciones

**Fortalezas:**
- Es una de las exposiciones funcionales más cercanas al objetivo integral de SIVEP.
- Conecta productos, operaciones, valores, contexto comercial y riesgo.
- Promueve evidencias, explicabilidad, cobertura selectiva y supervisión.
- Considera la interoperabilidad entre fuentes y sistemas.

**Limitaciones científicas:**
1. No hay una comparación pública y reproducible de algoritmos de similitud o regresión.
2. Las métricas del componente específico de valoración no se muestran separadamente.
3. Los resultados económicos son estimaciones; no equivalen a recaudación comprobada.
4. Falta documentación detallada de datos, validación, umbrales y muestras.
5. Las demostraciones corresponden a tecnología relacionada con afiliaciones de los propios autores; conviene reconocer esa **vinculación comercial** sin inferir que los resultados sean falsos.
6. La transferibilidad a un sistema peruano, sus procedimientos y su corpus sigue sin verificarse.

## 7. Transferencia posible a SIVEP Inteligente

**Aportes de arquitectura funcional:**
- Estandarización de mercancías y operadores.
- Recuperación de **DAM históricas comparables**.
- Visualización de antecedentes y rangos/distribuciones de valor.
- Ranking de anomalías con explicaciones.
- Política de **abstención y revisión humana**.
- Extensión futura a grafos de proveedores y cadenas de suministro, si existen datos institucionalmente disponibles.

**Qué no adoptaría en la primera versión:** reconstruir una red global de cadenas de suministro o desplegar RAG generativo en cada paso antes de demostrar que el recuperador encuentra mercancías comparables con suficiente precisión.

## 8. Experimentos propios sugeridos

1. Comparar búsqueda directa por descripción/atributos con un esquema de **canonicalización previa**.
2. Evaluar **qué contexto comercial** mejora el matching (proveedor, fabricante, origen, fecha, cantidad) y cuál introduce exclusiones o sesgos.
3. Comparar intervalos empíricos de los valores comparables con modelos predictivos, controlando cobertura y calibración.
4. Evaluar confianza y **abstención**: proporción de consultas atendidas con una precisión mínima predeterminada.
5. Medir por separado **recuperación**, **estimación de valor**, **alertamiento** y **priorización de control posterior**.
6. Mantener procedencia y condiciones de uso de cada antecedente según los requisitos del [artículo 5](05-morgero-macedo-2025-articulo-17.md).

## 9. Conclusión

El estudio es una **referencia sobresaliente de arquitectura funcional** para un sistema de valoración asistida por IA que incorpore cadenas comerciales. La **Figura 7** se aproxima especialmente al caso de uso de SIVEP. Sin embargo, la publicación **no permite seleccionar ni replicar el algoritmo de identificación de mercancías idénticas o similares**, y sus cifras operativas deben registrarse con sus limitaciones.

**Relacionados:** [1 — modelo de India](01-vijayakumar-2025-india.md), [3 — rangos por producto](03-chan-ng-chung-2023-hong-kong.md), [4 — priorización económica](04-alwanin-2026-dxgba.md), [5 — marco de valoración](05-morgero-macedo-2025-articulo-17.md).

---
*No son resultados obtenidos por SUNAT ni está demostrado que el sistema comercial descrito cumpla automáticamente todos los requisitos de valoración aduanera peruana.*
