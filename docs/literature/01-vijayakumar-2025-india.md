# Artículo 1 — Vijayakumar (2025): gestión de riesgos aduaneros basada en tecnología y datos

## Ficha bibliográfica

**Referencia:** Vijayakumar, S. (2025). *Technology-centric and Data-Driven Customs Risk Management for Supply Chain Security*. **World Customs Journal, 19**(1), 38–63.  
**DOI:** https://doi.org/10.55596/001c.131745  
**Contexto:** Departamento de Ingresos y Aduana de la India; capacidades analíticas del National Customs Targeting Centre (NCTC).  
**Tipo de evidencia:** revisión aplicada e iniciativas institucionales; no constituye validación experimental reproducible del modelo de valoración.  
**Fuente examinada:** PDF del artículo proporcionado para esta revisión. Pasajes clave: §4.1.5 (modelo de anomalías de importación, p. 48), §5.1 (codificación de proveedores, pp. 50–52), conclusiones.

## 1. Problema investigado

El comercio internacional combina altos volúmenes de operaciones, mercancías muy diversas, documentos heterogéneos y riesgos que cambian con el tiempo. La revisión individual de todas las importaciones no es viable; utilizar únicamente reglas rígidas o información aislada de la declaración limita tanto la detección de fraude como la facilitación del comercio legítimo.

El artículo identifica, entre otros, riesgos de subvaloración, clasificación incorrecta y patrones comerciales atípicos. También aborda un problema estructural de calidad de datos: nombres y direcciones de proveedores aparecen escritos de formas diferentes, sin identificador único, lo que dificulta relacionar operaciones del mismo actor.

Para valoración existe una dificultad específica: **recuperar antecedentes verdaderamente comparables** y distinguir una discrepancia de valor explicable de una operación que merece mayor investigación.

## 2. Modelo de anomalías de valoración de importaciones

La sección 4.1.5 describe el **Import Valuation Anomaly Model**. Su funcionamiento puede reconstruirse en cinco pasos:

1. Utilizar una base histórica de declaraciones con descripciones comerciales y valores.
2. Crear conjuntos de mercancías presumiblemente idénticas o similares mediante **agrupamiento de textos (text clustering)** y **detección de comunidades (community detection)**.
3. Comparar la descripción de una declaración entrante con esos grupos mediante **algoritmos de distancia**, asociándola al grupo pertinente.
4. Examinar operaciones históricas cercanas en **época y cantidad**, con atención a **proveedor y país de origen**.
5. Generar una **alerta** cuando la operación declarada presenta un valor inferior al de antecedentes relevantes; el funcionario debe investigar.

Es importante no atribuir al artículo algoritmos que no especifica: **no publica el tipo exacto de agrupamiento, la medida de distancia, sus pesos, umbrales o criterios de adjudicación de la categoría jurídica “idéntica” o “similar”**.

### Lectura crítica del flujo

Un grupo con descripciones semejantes puede contener productos con diferentes precios: versiones, marcas, modelos, tamaños, composiciones o condiciones de venta. Un modelo semántico puede detectar semejanza temática sin acreditar identidad del producto. La correspondencia textual, por tanto, debe ser un **generador de candidatos**, no una determinación final de comparabilidad.

El artículo incorpora variables comerciales (fecha, cantidad, proveedor y origen), lo cual reduce comparaciones inadecuadas, pero tampoco especifica cómo efectuar ajustes de nivel comercial o volumen para una utilización jurídica de los antecedentes.

## 3. Otras soluciones descritas

La autora expone aplicaciones adicionales del NCTC:

- **Codificación de proveedores:** limpieza y estandarización de campos de texto libre; comparación de nombres y direcciones con técnicas como *Locality-Sensitive Hashing* y distancias de cadenas. Busca relacionar distintas denominaciones de una misma entidad.
- **Análisis de redes:** representación de vínculos entre importadores, proveedores y participantes de las cadenas comerciales.
- **Perfilamiento y anomalías conductuales:** agrupamiento, análisis temporal y detección de cambios inusuales en patrones de operadores.
- **Visión artificial y clasificación arancelaria:** ejemplos de uso de imágenes de inspección y NLP para problemas de control.

El mayor detalle documental sobre *supplier codification* **no debe confundirse con un método validado para identidad de mercancías**. El primero resuelve correspondencia de entidades empresariales; el segundo exige comparar atributos físicos y comerciales de productos.

## 4. Datos y resultados

| Elemento | Lo que documenta el artículo |
|---|---|
| Existencia conceptual del modelo de valoración | Sí |
| Datos reales aduaneros y contexto de gestión de riesgos | Sí, descritos institucionalmente |
| Número de declaraciones y período para valoración | No se especifica |
| Algoritmo de clustering y función de distancia específicos | No se especifican |
| Tamaño de grupos o reglas para asignar nuevos casos | No se especifican |
| Evaluación por expertos de mercancías idénticas/similares | No documentada |
| Precision, recall y falsos positivos del modelo de valoración | No documentados |
| Impacto fiscal verificado atribuible a alertas | No documentado |
| Código y protocolo reproducibles | No proporcionados |

**Resultado que podemos citar:** descripción de una capacidad de comparación histórica y generación de alertas mediante agrupamiento de descripciones. **Resultado que NO podemos citar:** una exactitud numérica para la detección de subvaloración.

## 5. Fortalezas y limitaciones

**Fortalezas:** caso de uso aduanero estrechamente relacionado con SIVEP; utilización de antecedentes; comparación contextualizada; separación entre alerta y revisión humana; integración de técnicas textuales y datos estructurados.

**Limitaciones:** detalle algorítmico insuficiente; ausencia de diseño experimental verificable; no distingue formalmente comparabilidad semántica, técnica y jurídica; sin evaluación de errores críticos. La existencia de un antecedente de mayor precio **no implica** por sí sola falsedad del valor declarado.

El trabajo debe clasificarse como **antecedente arquitectónico e institucional**, no como prueba de superioridad de una técnica concreta.

## 6. Aplicación posible a SIVEP Inteligente

**Componente respaldado:** recuperación de mercancías históricas y alertas preliminares, con evaluación posterior del especialista.

Experimentos propuestos por nuestro proyecto —**no realizados por Vijayakumar**—:

1. **Clustering previo frente a búsqueda directa:** comparar agrupamiento + recuperación dentro del grupo con BM25, búsqueda vectorial y recuperación híbrida sin clustering.
2. **Filtros comerciales:** evaluar país de origen, proveedor, cantidad y ventanas temporales como condiciones obligatorias o criterios de ranking. Medir la pérdida de antecedentes válidos al restringir demasiado.
3. **Validación experta:** construir pares *idéntica / similar / no comparable*, incluyendo textos semejantes de modelos distintos y textos diferentes del mismo modelo.
4. **Métricas:** Precision@5, Recall@10, tasa de falsos positivos críticos de identidad, cobertura y tiempo de recuperación; **sin usar el valor declarado como sustituto de la etiqueta de comparabilidad**.
5. **Trazabilidad:** conservar ID de DAM/serie, atributos coincidentes, discrepancias y estado de verificación del valor.

## 7. Conclusión para la revisión

Este es el antecedente más directo de la **idea funcional de recuperar mercancías históricas mediante clustering y distancias textuales para alertas de valoración**, pero no permite replicar su implementación ni comparar resultados cuantitativamente. SIVEP puede convertir esa idea en un experimento reproducible y verificable sobre DAM peruanas.

**Relacionados:** [Artículo 5 — requisitos jurídicos](05-morgero-macedo-2025-articulo-17.md), [Artículo 6 — comparación textual](06-bayona-2025-transposicion-hs.md), [Artículo 7 — recuperación híbrida](07-kim-kim-choi-2025-the-rag.md).

---
*Ficha de revisión documental; separa afirmaciones del artículo de propuestas propias. Ningún resultado constituye decisión automática sobre el valor en aduana.*
