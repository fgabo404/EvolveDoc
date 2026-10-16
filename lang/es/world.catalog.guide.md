# Evolve — Guía de diseño del catálogo del mundo

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
| `biomes` | Siete categorías de bioma para la interfaz. |
| `regionalVariants` | Las 27 variantes regionales o de hábitat, vinculadas por `biomeId`. |
| `speciesCandidates` | Entradas de flora y fauna, incluidos grupos que deben concretarse. |
| `geologicalResourceCandidates` | Materiales y menas del documento. Extraer un depósito no concede automáticamente metal refinado. |
| `resourceOccurrences` | Cada aparición regional de flora, fauna y minería, con texto fuente, ID y método de extracción cuando corresponde. |
| `agriculturalCropCandidates` | Los 21 cultivos o grupos agrícolas de la sección 5, pendientes de resolver por especie. |
| `hexDefinitionGuide` | Propiedades propuestas para hexágonos y separación entre generación y estado. |
| `depositDefinitionGuide` | Campos de depósitos cuyas cantidades y reglas siguen pendientes. |
| `generationPipeline` | Orden de generación expresado como pasos técnicos. |
| `reviewIssues` | Contradicciones del documento y dudas de integración. |
| `speciesCompletionChecklist` | Trabajo necesario para convertir cada candidato en definición jugable. |

## 3. Identidad y taxonomía

Los IDs de candidatos identifican entradas de diseño; no son nombres científicos aceptados. Las variantes que podrían corresponder al mismo taxón se conservan hasta revisarlas. No deben fusionarse solo por tener nombres parecidos.

Solo se incluyen nombres científicos binomiales escritos explícitamente en el documento. `verified: false` indica que no se ha validado taxonomía. Acacias, peces regionales o parientes silvestres deben desglosarse o aceptarse expresamente como grupos de juego. Un nombre común en singular no garantiza una especie exacta.

Los IDs agrícolas `wheat` y `maize` son vínculos propuestos para investigación. Falta resolver su taxón, ancestro y relación con los candidatos silvestres. No se equipara automáticamente maíz doméstico con cualquier teosinte ni trigo doméstico con cualquier trigo silvestre.

## 4. Contenido conservado

Se conservan las 485 apariciones del catálogo. El documento enumera 27 variantes, aunque después menciona 26; un apartado pendiente dice diez biomas, mientras que el catálogo detallado contiene siete. La guía conserva lo enumerado y registra estas contradicciones.

Tres líneas explicativas después de la última lista de flora alpina se guardan como notas de distribución, no como plantas. Las etapas mineras siguen siendo apariciones por método. No se fusionan automáticamente materiales similares.

La procedencia incluye el ID exacto del documento y la huella de la copia adjunta. Esta conversión se basa en esa copia; no afirma haber verificado una revisión actual del documento conectado.

## 5. Valores pendientes

`null` significa no resuelto; no significa cero, ningún requisito, distribución mundial o capacidad aprobada. Las listas vacías de regiones o ancestros son vínculos pendientes.

Todas las apariciones tienen `runtimeEnabled: false`, `guaranteedPresence: false` y probabilidad desconocida. No se inventaron abundancias, crecimiento, rangos de fertilidad, tiempos de domesticación ni rendimientos.

Los productos animales solo transcriben aprovechamientos potenciales del documento. No son desbloqueos ni rendimientos garantizados. `antlers_or_horns` debe concretarse según especie, sin conceder ambos por defecto. Los productos vegetales quedan pendientes porque las listas regionales no los detallan sistemáticamente.

## 6. Reglas del mundo

Elevación y bioma son independientes. Los niveles 0–2 permiten tránsito terrestre ordinario según superficie y restricciones; el nivel 3 bloquea el paso ordinario y los asentamientos convencionales. El nivel del mar distingue tierra de agua.

Clima geográfico, agua, suelo y origen nativo condicionan especies. Estaciones y desastres dinámicos quedan fuera del alcance inicial. Los minerales se distribuyen por geología, no por una lista obligatoria de cada bioma.

Las entradas marinas requieren profundidad, hábitat y región adecuados. Los nódulos polimetálicos no son recursos costeros someros automáticamente accesibles. La minería mecanizada pertenece a contenido futuro fuera del alcance medieval inicial.

Los dromedarios domésticos o asilvestrados solo aparecen por introducción según la fuente, no como fauna silvestre nativa inicial. Otras dudas, como las palmeras datileras cultivadas, siguen señaladas. Los líquenes conservan su ubicación en flora por trazabilidad, sin afirmar una clasificación botánica.

## 7. Relación con agricultura

La configuración tecnológica pasa a estructura `2.0.0` y contenido `0.3.0`: una lista plana `technologies`, con IDs estables y `order` global. La posición no crea requisitos. La investigación se identifica por `(civilizationId, technologyId, speciesId)`.

Esta guía no resuelve todas las dependencias externas. Presencia silvestre, descubrimiento, conocimiento de cultivo, domesticación y producción siguen siendo estados separados. Una planta accesible no es automáticamente comestible, cultivable ni domesticable.

## 8. Cómo completar cada candidato

Elegir especie exacta o taxón de juego; verificar nombre científico y distribución; distinguir ancestros y formas domésticas; definir ecología y reproducción; especificar productos y recetas; vincular tecnologías; revisar época y región; finalmente balancear y probar.

Tras esas revisiones se podrán promover registros aprobados a `species.json` y definiciones ejecutables del mundo. Al dividir o fusionar candidatos deben conservarse IDs o establecerse alias y migraciones explícitas. Los registros con valores pendientes no son contenido final del simulador.

## 9. Validación realizada

Se comprobó cobertura de apariciones, traducciones, IDs únicos, referencias, recuentos de biomas y variantes y concordancia con las listas enumeradas. No se han validado taxonomía científica, distribución exacta, catálogos externos ni simulación.


## 10. Resumen de conversión

```json
{
  "biomeCount": 7,
  "regionalVariantCount": 27,
  "plantCandidateCount": 129,
  "animalCandidateCount": 134,
  "geologicalCandidateCount": 57,
  "sourceOccurrenceCount": 485,
  "agriculturalCropCandidateCount": 21
}
```
