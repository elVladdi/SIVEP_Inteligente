# Artículo 2 — Alqaryouti et al. (2024): detección de anomalías de valoración por distancias y densidad

## Ficha bibliográfica

**Referencia:** Alqaryouti, O., Siyam, N., Shaalan, K., & Alhosban, F. (2024). *Customs valuation assessment using cluster-based approach*. **International Journal of Information Technology, 16**(7), 4243–4252.  
**DOI:** https://doi.org/10.1007/s41870-024-01821-1  
**Contexto:** Dubai Customs, declaraciones de importación de 2018.  
**Tipo de evidencia:** propuesta matemática con experimentación cuantitativa basada en datos aduaneros; no evalúa identificación de mercancías idénticas/similares.  
**Fuente examinada:** PDF proporcionado. Referencias principales: algoritmo de dos etapas y Figuras 2–4, pp. 4246–4250.

## 1. ¿Qué problema intentaron resolver?

La revisión manual de valores declarados es costosa y difícil de aplicar a grandes cantidades de operaciones. Los autores intentan detectar automáticamente **valores atípicos**, de manera que la administración pueda concentrar el análisis en declaraciones que se apartan de sus antecedentes.

El trabajo propone comparar operaciones dentro de un **mismo código HS**, representarlas como puntos multidimensionales y distinguir las diferencias extremas de patrones históricos legítimos. La distinción central es entre **anomalía estadística** y **operación normal respecto de su vecindario**, no entre mercancías jurídicamente idénticas o similares.

## 2. Datos y preprocesamiento

Los autores informan **500 000 registros de Dubai Customs correspondientes a 2018**, con una distribución descrita de **90 % de declaraciones normales y 10 % riesgosas**.

Elementos empleados:
- **Código HS:** agrupación inicial.
- **País de origen, valor de la mercancía y valor CIF:** espacio de características para análisis por distancias y densidad.
- **Exclusiones y filtros:** se apartan ciertas operaciones exentas y grupos sin observaciones suficientes, según el protocolo descrito.

Para la prueba se construyen **diez muestras de 200 casos**, cada una con **100 normales y 100 anómalos**. La prevalencia artificialmente balanceada importa porque la exactitud y los valores predictivos cambiarían con la frecuencia real de declaraciones irregulares.

No debe suponerse que asignar un número entero al país de origen lo convierte en una variable métrica; una distancia euclidiana sobre códigos nominales necesita transformación justificada.

## 3. Algoritmo propuesto

### Etapa A — distancia respecto del grupo

Todas las operaciones con un código HS se consideran integrantes de un grupo histórico. Para una declaración entrante, los autores calculan una distancia euclidiana respecto del centro y una distancia media a otras operaciones del grupo. Estas se normalizan y combinan en una puntuación:

```text
S = (d_c / m_c) × (d_n / m_d)
```

Aquí, `d_c` representa distancia al centro, `d_n` distancia media al resto del grupo y `m_c` y `m_d` magnitudes máximas de referencia. La regla descrita es:

- **S ≤ 1:** operación normal en esta etapa.
- **S > 1:** candidato anómalo que se envía a segunda evaluación.

Para una reproducción debe consultarse el pseudocódigo exacto del PDF; esta fórmula es una síntesis de la puntuación utilizada, no un estándar aduanero.

### Etapa B — *Local Outlier Factor* (LOF)

A los candidatos de la etapa anterior se les aplica **LOF**, que estima el aislamiento de una observación en comparación con la densidad local de sus vecinos. Esto permite que una operación alejada de la media del grupo no sea necesariamente tratada como anómala si está acompañada por otras operaciones semejantes.

La segunda etapa puede **revertir** la clasificación preliminar de la primera; por tanto, el sistema no es simplemente un umbral único de precio.

La salida del procedimiento es **normal / anómalo**. No produce una determinación jurídicamente vinculante del valor en aduana ni acredita por sí mismo fraude.

## 4. Resultados experimentales

El trabajo compara el efecto de limitarse a grupos de HS con suficiente cantidad de declaraciones y el efecto de incrementar las muestras utilizadas en la evaluación.

| Resultado informado | Magnitud |
|---|---:|
| Exactitud máxima reportada al seleccionar 10 % de grupos HS más poblados | **86 %** |
| “Precision” reportada para esa condición | **84 %** |
| Exactitud para una muestra de 200 casos | 71 % |
| Exactitud para diez muestras / 2 000 casos | 86 % |

Las **Figuras 3 y 4** muestran que los grupos con más antecedentes permiten resultados más favorables y que los resultados de la evaluación mejoran al acumular muestras hasta el diseño final.

**Precaución terminológica:** el texto describe “precision” en un pasaje como la proporción de mercancías efectivamente manipuladas que fueron detectadas, formulación propia de **recall**. Sin una matriz de confusión completa no se debe asumir que el 84 % equivale necesariamente a TP/(TP+FP). En nuestra matriz se utilizará la expresión **«precisión denominada así por los autores»**.

## 5. Fortalezas

1. Explica una combinación concreta de distancia y densidad, frente a publicaciones que solo mencionan “IA”.
2. Utiliza registros aduaneros y proporciona condiciones y cifras experimentales.
3. Introduce el problema de la **densidad del histórico**: un algoritmo no se comporta igual en grupos muy poblados que en subpartidas con pocas observaciones.
4. Permite diseñar una línea base implementable con herramientas estadísticas habituales.

## 6. Limitaciones de validez

- **No utiliza descripción comercial:** compartir HS no implica que los productos tengan igual marca, modelo, calidad o valor.
- **Homogeneidad no probada:** se asume un grupo HS, no se construye un conjunto etiquetado por especialistas como mercancía idéntica/similar.
- **Escala y codificación:** las distancias monetarias y el origen requieren normalización/codificación precisa.
- **Muestra de evaluación balanceada:** puede ocultar una carga real de falsos positivos más alta.
- **Comparación limitada:** no se informa una batería extensa frente a cuantiles robustos, Isolation Forest o modelos supervisados.
- **Temporalidad:** no demuestra evaluación retrospectiva con únicamente datos existentes antes de cada DAM analizada.
- **Confiabilidad jurídica:** el histórico no se segmenta de forma plenamente documentada por valor declarado, analizado o determinado.

## 7. Aporte metodológico y límites de la evidencia

El artículo desarrolla un procedimiento en **dos etapas** que combina distancias respecto de operaciones agrupadas por código HS y densidad local mediante LOF. La segunda etapa puede reconsiderar señales de anomalía generadas en la primera.

Los resultados dependen de grupos HS relativamente poblados y muestras de prueba balanceadas. El estudio no utiliza etiquetas de mercancías idénticas o similares ni aporta datos y parámetros suficientes para reproducir de manera independiente las cifras reportadas.

## 8. Conclusión

**Aporte principal:** detección de **anomalías estadísticas de valor** combinando distancias y LOF. La clasificación normal/anómala no acredita identidad o similitud de mercancías ni constituye una determinación legal del valor.

**Relacionados:** [1 — India](01-vijayakumar-2025-india.md), [3 — Hong Kong](03-chan-ng-chung-2023-hong-kong.md), [5 — artículo 17](05-morgero-macedo-2025-articulo-17.md).

---
*Los porcentajes corresponden a condiciones experimentales específicas del estudio y no equivalen a una determinación legal del valor.*
