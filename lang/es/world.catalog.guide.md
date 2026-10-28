# Evolve — Guía de diseño del catálogo del mundo

[Catálogo de recursos y relaciones](resources.md)

[Referencia gráfica sencilla](visual-reference.md)

Estructuras JSON completas, tipos y ejemplos: [referencia de JSON](json-structures.md).

Conversión estructurada de la copia adjunta de Documentacion Evolve. El documento original se leyó para extraer su contenido y no se modificó.

## Organización en el repositorio

La guía combinada se divide ahora entre `data/world`, `data/plants`, `data/animals` y `data/minerals`. La tabla siguiente describe las colecciones lógicas entre esos archivos. Las rutas de `catalogFiles` son relativas a `data/world/world.catalog.guide.json`. El esquema del mundo `1.1.0` y contenido `0.2.0` reflejan esta separación; se conservan los IDs y las 485 apariciones. Los candidatos agrícolas están en el catálogo de plantas.

## 1. Propósito y límites

Este JSON sirve para concretar especies, condiciones de generación y recursos. Todavía no es un catálogo jugable. `runtimePolicy.loadAsGameDefinitions` es falso: el motor no debe generar candidatos ni interpretar valores desconocidos como condiciones sin restricciones.

Las colecciones son planas y se relacionan por IDs. Los nombres visibles usan `{en, es}`; IDs y reglas internas siguen en inglés. `sourceText` y `sourceLabel` conservan el texto español original para trazabilidad, no como interfaz del juego.

## 2. Colecciones

| Campo | Significado |
| --- | --- |
| `biomes` | Siete categorías generales de bioma. |
| `biomeSubtypes` | Veintidós subtipos ecológicos, sin asignaciones de contenido. |
| `speciesCandidates` | Entradas de flora y fauna, incluidos grupos que deben concretarse. |
| `geologicalResourceCandidates` | Materiales y menas del documento. Extraer un depósito no concede automáticamente metal refinado. |
| `resourceOccurrences` | Cada aparición documentada de flora, fauna y minería, con texto fuente, ID y método de extracción cuando corresponde; no se asigna automáticamente a subtipos. |
| `agriculturalCropCandidates` | Los 21 cultivos o grupos agrícolas de la sección 5, pendientes de resolver por especie. |
| `hexDefinitionGuide` | Propiedades propuestas para hexágonos y separación entre generación y estado. |
| `depositDefinitionGuide` | Campos de depósitos cuyas cantidades y reglas siguen pendientes. |
| `generationPipeline` | Orden de generación expresado como pasos técnicos. |
| `reviewIssues` | Contradicciones del documento y dudas de integración. |
| `speciesCompletionChecklist` | Trabajo necesario para convertir cada candidato en definición jugable. |

## Estructura oficial de biomas y subtipos

Siete biomas principales y veintidós subtipos ecológicos sin división continental. JSON activo: `data/world/biomes.json`. Copia anterior: `data/world/Old/biomes.old.json`.

### 1. Desierto

- Arenoso (dunas)
- Rocoso (cañones y mesetas)
- Salar

### 2. Bosque

- Tropical (selva)
- Subtropical
- Templado
- Boreal (taiga)
- Pantano arbolado (Everglades)

### 3. Llanuras

- Sabana
- Pradera
- Estepa
- Humedal abierto (Pantanal)

### 4. Marino

- Arrecife
- Estuario o litoral
- Manglar
- Océano abierto (alta mar)

### 5. Tundra

- Tundra

### 6. Montaña

- Alpino
- Rocoso
- Acantilados

### 7. Polo

- Polo Norte
- Polo Sur

**Cumbres:** por encima del nivel 100 son infranqueables y no constituyen un subtipo de Montaña. Su representación lógica está pendiente de definir.

**Pendiente:** no se asignan flora, fauna, minerales, recursos, probabilidades ni rangos ecológicos a estos subtipos.

## 3. Identidad y taxonomía

Los IDs de candidatos identifican entradas de diseño; no son nombres científicos aceptados. Los subtipos ecológicos se definen por condiciones ambientales y terreno, no por procedencia continental. No fusionar entidades diferentes solo por parecido.

Solo se incluyen nombres científicos binomiales escritos explícitamente en el documento. `verified: false` indica que no se ha validado taxonomía. Las categorías generales como acacias y zorros son identidades válidas del juego. La taxonomía científica es opcional y no exige subdividirlas.

Los IDs agrícolas `wheat` y `maize` son vínculos propuestos para investigación. Falta diseñar sus relaciones jugables con las formas silvestres; la taxonomía es opcional. No se equipara automáticamente maíz doméstico con cualquier teosinte ni trigo doméstico con cualquier trigo silvestre.

## 4. Contenido conservado

Se conservan las 485 apariciones históricas, sin vínculos activos a biomas o subtipos. La estructura vigente contiene siete biomas y veintidós subtipos.

Tres líneas explicativas después de la última lista de flora alpina se guardan como notas de distribución, no como plantas. Las etapas mineras siguen siendo apariciones por método. No se fusionan automáticamente materiales similares.

La procedencia incluye el ID exacto del documento y la huella de la copia adjunta. Esta conversión se basa en esa copia; no afirma haber verificado una revisión actual del documento conectado.

## 5. Valores pendientes

`null` significa no resuelto; no significa cero, ningún requisito, distribución mundial o capacidad aprobada. Las listas vacías de regiones o ancestros son vínculos pendientes.

Todas las apariciones tienen `runtimeEnabled: false`, `guaranteedPresence: false` y probabilidad desconocida. No se inventaron abundancias, crecimiento, rangos de fertilidad, tiempos de domesticación ni rendimientos.

Los productos animales registran posibilidades de la fuente y decisiones explícitas del juego, como los productos detallados de zorros. No son desbloqueos ni rendimientos garantizados. `antlers_or_horns` requiere decidir el recurso del juego, sin conceder ambos por defecto. Algunos productos vegetales y todos los cultivos ya tienen vínculos propuestos de recursos; los requisitos de obtención y cantidades siguen pendientes; no se exige especie científica exacta. Son propuestas adicionales de diseño, no afirmaciones textuales de la fuente.

## Propuesta vigente — escala altimétrica y compatibilidad de biomas (2026-10-27)

**Decisión aprobada de diseño:** cada hexágono podrá representar una elevación lógica entera entre **0 y 100**, equivalente linealmente a **0–4,000 metros sobre el nivel del mar**, con **40 m por nivel** (`metros = nivel × 40`). El nivel 0 es la referencia del nivel del mar, sin implicar por sí solo que una celda sea océano: la superficie tierra/agua se conserva como atributo independiente. La profundidad marina no queda definida en esta escala.

**Principio aprobado:** la altitud limita la **compatibilidad** de los biomas, pero no los determina por sí sola. La selección posterior también deberá considerar temperatura, humedad y ubicación geográfica. La tectónica genera el relieve y, posteriormente, un clasificador ambiental determina el bioma compatible.

**Rangos por subtipo pendientes:** se retiró la tabla provisional para los siete biomas anteriores. Se conserva la escala de 0 a 100 y la equivalencia de 40 m por nivel.

## Sistema polar mixto y propuesta de rangos (2026-10-27)

**Aprobado:** el Polo es el séptimo bioma y tiene los subtipos Polo Norte y Polo Sur. Se adopta **núcleo polar permanente + transición climática exterior**; una celda polar puede ser agua sin convertirse en tierra. La tundra sigue siendo un bioma distinto. Los subtipos de Polo son una clasificación del entorno; la cubierta de hielo física queda para una capa futura.

**Límites numéricos propuestos, aún sin aprobación individual:** núcleo permanente 80°–90° en cada hemisferio; transición dependiente de temperatura y elevación entre 65°–80°. Los rangos de latitud de la tabla son **absolutos** (N o S), excepto Polo Norte y Polo Sur, que especifican hemisferio.

**Escala aprobada:** nivel 0–100 equivalente a 0–4,000 metros, 40 m por nivel. Cumbres superiores a 100 infranqueables, sin pertenecer a ningún subtipo; el modo de codificar alturas superiores a 100 permanece pendiente.

**Tabla de compatibilidad propuesta** (NO representa restricciones aprobadas ni parámetros de ejecución):

| Bioma | Subtipo | Nivel Evolve | Altitud equivalente | Latitud |
| --- | --- | --- | --- | --- |
| Desierto | Arenoso (dunas) | 0–40 | 0–1600 m | 10°–50° N/S |
| Desierto | Rocoso (cañones y mesetas) | 10–60 | 400–2400 m | 15°–55° N/S |
| Desierto | Salar | 0–95 | 0–3800 m | 10°–50° N/S |
| Bosque | Tropical (selva) | 0–30 | 0–1200 m | 0°–23° N/S |
| Bosque | Subtropical | 10–50 | 400–2000 m | 15°–35° N/S |
| Bosque | Templado | 5–60 | 200–2400 m | 30°–60° N/S |
| Bosque | Boreal (taiga) | 0–35 | 0–1400 m | 50°–70° N/S |
| Bosque | Pantano arbolado (Everglades) | 0–5 | 0–200 m | 15°–35° N/S |
| Llanuras | Sabana | 0–40 | 0–1600 m | 5°–30° N/S |
| Llanuras | Pradera | 10–45 | 400–1800 m | 25°–55° N/S |
| Llanuras | Estepa | 10–50 | 400–2000 m | 30°–60° N/S |
| Llanuras | Humedal abierto (Pantanal) | 0–10 | 0–400 m | 5°–35° N/S |
| Marino | Arrecife | 0–0 | 0–0 m | 0°–35° N/S |
| Marino | Estuario o litoral | 0–0 | 0–0 m | 0°–75° N/S |
| Marino | Manglar | 0–0 | 0–0 m | 0°–35° N/S |
| Marino | Océano abierto (alta mar) | 0–0 | 0–0 m | 0°–75° N/S |
| Tundra | Tundra | 0–60 | 0–2400 m | 55°–80° N/S |
| Montaña | Alpino | 40–90 | 1600–3600 m | 0°–75° N/S |
| Montaña | Rocoso | 30–100 | 1200–4000 m | 0°–75° N/S |
| Montaña | Acantilados | 0–100 | 0–4000 m | 0°–75° N/S |
| Polo | Polo Norte | 0–80 | 0–3200 m | 65°–90° N |
| Polo | Polo Sur | 0–100 | 0–4000 m | 65°–90° S |

La altura y la latitud solo delimitan posibles candidatos. El bioma definitivo también requerirá temperatura, humedad, pendiente, costa y agua según corresponda. En el caso marino, el nivel 0 significa la superficie del mar; no define profundidad. **No se han asignado fauna, flora, minerales, recursos ni probabilidades de aparición.**

## 6. Reglas del mundo

La configuración de elevaciones, sus rangos y las reglas para asignar biomas se redefinirán desde cero. No utilizar reglas anteriores como parámetros ejecutables.

Clima geográfico, agua, suelo y origen nativo condicionan especies. Estaciones y desastres dinámicos quedan fuera del alcance inicial. Los minerales se distribuyen por geología, no por una lista obligatoria de cada bioma.

Las entradas marinas requieren profundidad, hábitat y región adecuados. Los nódulos polimetálicos no son recursos costeros someros automáticamente accesibles. La minería mecanizada pertenece a contenido futuro fuera del alcance medieval inicial.

Los dromedarios domésticos o asilvestrados solo aparecen por introducción según la fuente, no como fauna silvestre nativa inicial. Otras dudas, como las palmeras datileras cultivadas, siguen señaladas. Los líquenes conservan su ubicación en flora por trazabilidad, sin afirmar una clasificación botánica.

## 7. Relación con agricultura

La configuración tecnológica pasa a estructura `2.0.0` y contenido `0.3.0`: una lista plana `technologies`, con IDs estables y `order` global. La posición no crea requisitos. La investigación se identifica por `(civilizationId, technologyId, speciesId)`.

Esta guía no resuelve todas las dependencias externas. Presencia silvestre, descubrimiento, conocimiento de cultivo, domesticación y producción siguen siendo estados separados. Una planta accesible no es automáticamente comestible, cultivable ni domesticable.

## 8. Cómo completar cada candidato

Elegir categoría del juego; conservar reglas regionales de hábitat; distinguir formas silvestres y domésticas útiles; definir ecología y reproducción; especificar productos y recetas; vincular tecnologías; revisar época y región; finalmente balancear y probar.

Tras esas revisiones se podrán promover registros aprobados a `species.json` y definiciones ejecutables del mundo. Al dividir o fusionar candidatos deben conservarse IDs o establecerse alias y migraciones explícitas. Los registros con valores pendientes no son contenido final del simulador.

## 9. Validación realizada

Se comprobó cobertura de apariciones, traducciones, IDs únicos, referencias, recuentos de biomas y variantes y concordancia con las listas enumeradas. No se han validado taxonomía científica, distribución exacta, catálogos externos ni simulación.


## 10. Resumen de conversión

```json
{
  "biomeCount": 7,
  "regionalVariantCount": 27,
  "plantCandidateCount": 109,
  "animalCandidateCount": 101,
  "geologicalCandidateCount": 57,
  "sourceOccurrenceCount": 485,
  "agriculturalCropCandidateCount": 21
}
```

## Actualización de recursos

Mundo usa esquema/contenido 1.4.0/0.5.0. Plantas usan 1.3.0/0.4.0 y animales 1.4.0/0.6.0; minerales conservan 1.1.0/0.2.0. Las 485 apariciones conservan sus IDs; las definiciones agrupadas tienen alias y procedencia explícita. `extractedResourceId` identifica material obtenido, no metal refinado automático.

La [granularidad vigente](biology.md) usa entidades generales y alias de IDs; la referencia científica es opcional.
