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

Los IDs de candidatos identifican entradas de diseño; no son nombres científicos aceptados. Las variantes regionales revisadas se agrupan cuando sus productos coinciden, con alias y procedencia conservada. No fusionar entidades diferentes solo por parecido.

Solo se incluyen nombres científicos binomiales escritos explícitamente en el documento. `verified: false` indica que no se ha validado taxonomía. Las categorías generales como acacias y zorros son identidades válidas del juego. La taxonomía científica es opcional y no exige subdividirlas.

Los IDs agrícolas `wheat` y `maize` son vínculos propuestos para investigación. Falta diseñar sus relaciones jugables con las formas silvestres; la taxonomía es opcional. No se equipara automáticamente maíz doméstico con cualquier teosinte ni trigo doméstico con cualquier trigo silvestre.

## 4. Contenido conservado

Se conservan las 485 apariciones del catálogo. El documento enumera 27 variantes, aunque después menciona 26; un apartado pendiente dice diez biomas, mientras que el catálogo detallado contiene siete. La guía conserva lo enumerado y registra estas contradicciones.

Tres líneas explicativas después de la última lista de flora alpina se guardan como notas de distribución, no como plantas. Las etapas mineras siguen siendo apariciones por método. No se fusionan automáticamente materiales similares.

La procedencia incluye el ID exacto del documento y la huella de la copia adjunta. Esta conversión se basa en esa copia; no afirma haber verificado una revisión actual del documento conectado.

## 5. Valores pendientes

`null` significa no resuelto; no significa cero, ningún requisito, distribución mundial o capacidad aprobada. Las listas vacías de regiones o ancestros son vínculos pendientes.

Todas las apariciones tienen `runtimeEnabled: false`, `guaranteedPresence: false` y probabilidad desconocida. No se inventaron abundancias, crecimiento, rangos de fertilidad, tiempos de domesticación ni rendimientos.

Los productos animales solo transcriben aprovechamientos potenciales del documento. No son desbloqueos ni rendimientos garantizados. `antlers_or_horns` requiere decidir el recurso del juego, sin conceder ambos por defecto. Algunos productos vegetales y todos los cultivos ya tienen vínculos propuestos de recursos; los requisitos de obtención y cantidades siguen pendientes; no se exige especie científica exacta. Son propuestas adicionales de diseño, no afirmaciones textuales de la fuente.

## 6. Reglas del mundo

Elevación y bioma son independientes. Los niveles 0–2 permiten tránsito terrestre ordinario según superficie y restricciones; el nivel 3 bloquea el paso ordinario y los asentamientos convencionales. El nivel del mar distingue tierra de agua.

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

Mundo usa esquema/contenido 1.4.0/0.5.0. Plantas y animales usan 1.3.0/0.4.0; minerales conservan 1.1.0/0.2.0. Las 485 apariciones conservan sus IDs; las definiciones agrupadas tienen alias y procedencia explícita. `extractedResourceId` identifica material obtenido, no metal refinado automático.

La [granularidad vigente](biology.md) usa entidades generales y alias de IDs; la referencia científica es opcional.
