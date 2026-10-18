# `data/world/world.catalog.guide.json`

[JSON fuente](../../../data/world/world.catalog.guide.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"1.4.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.5.0"` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"world_catalog_design_guide"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"source_converted_requires_species_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `source` | `object` | 1/1 | Procedencia de la copia del documento original. | `—` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `worldRules` | `object` | 1/1 | Decisiones generales de generación del mundo. | `—` |
| `elevationLevels` | `array<object>` | 1/1 | Categorías de elevación independientes del bioma. | `—` |
| `geographicModifiers` | `array<object>` | 1/1 | Categorías geográficas que influyen en hábitat y acceso. | `—` |
| `biomes` | `array<object>` | 1/1 | Categorías de bioma de interfaz; no bastan para decidir apariciones. | `—` |
| `regionalVariants` | `array<object>` | 1/1 | Variantes regionales/de hábitat relacionadas con su bioma. | `—` |
| `resourceOccurrences` | `array<object>` | 1/1 | Apariciones de la fuente relacionadas con candidatos, variantes y métodos de extracción. | `—` |
| `generationPipeline` | `array<string>` | 1/1 | Pasos ordenados de diseño, no código ejecutable del generador. | `["generate_terrain_water_static_climate_and_biogeographic_regions", "assign_biomes_and_geographic_modifiers", "g…` |
| `speciesCompletionChecklist` | `array<string>` | 1/1 | Tareas de revisión antes de aprobar una definición candidata. | `["choose_general_gameplay_entity_and_stable_id", "preserve_regional_habitat_rules_and_source_provenance", "group…` |
| `reviewIssues` | `array<object>` | 1/1 | Contradicciones de la fuente y preguntas de diseño pendientes. | `—` |
| `sourceDistributionNotes` | `array<string>` | 1/1 | Notas originales de distribución, no especies adicionales. | `["Los siete biomas son categorías de interfaz; cada subtipo mantiene clima, terreno, hábitat y región propios.",…` |
| `agricultureSectionSource` | `array<string>` | 1/1 | Sección agrícola original conservada para trazabilidad. | `["5. Catálogo agrícola y vegetal inicial", "Los recursos agrícolas deben distinguir tres estados conceptuales: (…` |
| `summary` | `object` | 1/1 | Conteos para comprobar integridad de los catálogos. | `—` |
| `hexDefinitionGuide` | `object` | 1/1 | Nombres propuestos de campos de casilla y separación de estado; no es esquema implementado. | `—` |
| `depositDefinitionGuide` | `object` | 1/1 | Campos propuestos de yacimiento; no es una definición terminada. | `—` |
| `catalogFiles` | `object` | 1/1 | Ubicaciones de catálogos relacionados, relativas al JSON guía del mundo. | `—` |
| `repositoryPackaging` | `object` | 1/1 | Metadatos de separación de la guía combinada. | `—` |

### `$.source`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `title` | `string` | 1/1 | Título del documento o esquema. | `"Documentacion Evolve"` |
| `format` | `string` | 1/1 | Formato de la copia fuente o de la representación de idiomas. | `"docx_snapshot"` |
| `connectorFileId` | `string` | 1/1 | Identificador exacto de la fuente en el conector, conservado para trazabilidad. | `"11FrriHGZ9AKnrXFND-VNWzmNKJo_U2aCS9OFZyWo9c8"` |
| `sha256` | `string` | 1/1 | Huella SHA-256 de la copia del documento fuente. | `"151ea42d39ce1bc9d26d76e18dc1a9d8a5fbb9f888519c240d99fe7793271308"` |
| `snapshotOnly` | `boolean` | 1/1 | True indica extracción de la copia adjunta, sin verificar una revisión en vivo. | `true` |
| `originalDocumentModified` | `boolean` | 1/1 | Indica si se modificó el documento fuente; aquí es false. | `false` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `reason` | `string` | 1/1 | Explicación de la restricción de ejecución. | `"This is a gameplay design guide, not an executable world generator. General categories are valid; scientific sp…` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved; it never means zero, none, unrestricted or approved."` |
| `visibleText` | `string` | 1/1 | Política que distingue texto visible traducido y procedencia original. | `"name and description use language maps; sourceText and sourceLabel preserve verbatim Spanish provenance and mus…` |
| `flatCollections` | `string` | 1/1 | Política de colecciones al mismo nivel relacionadas mediante IDs. | `"All definitions are stored in flat collections and connected by stable IDs."` |
| `preserveSpeciesResearch` | `string` | 1/1 | Regla para conservar identidad de investigación al precisar taxonomía. | `"Gameplay entity IDs remain stable. Generalized sources keep explicit aliases and provenance; scientific taxonom…` |
| `wildAndDomestic` | `string` | 1/1 | Regla que separa presencia silvestre, cultivo, domesticación y producción. | `"Wild presence, cultivation knowledge, domestication and established crop production are separate states."` |
| `distribution` | `string` | 1/1 | Regla que exige regiones nativas y hábitats verificados para aparición. | `"Biome compatibility does not imply universal native distribution."` |
| `geology` | `string` | 1/1 | Regla que controla minerales independientemente de etiquetas de bioma. | `"Mineral distribution is controlled by geology, not mandatory biome resource lists."` |
| `miningStages` | `string` | 1/1 | Interpretación de métodos de extracción sin inventar épocas exclusivas. | `"Extraction methods describe capabilities, not exclusive material eras."` |
| `scope` | `string` | 1/1 | Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto. | `"Mechanized mining and seabed nodules remain future content outside the initial medieval scope."` |
| `biologicalGranularity` | `string` | 1/1 | La aparición mundial usa categorías del juego y no especies científicas obligatorias. | `"World occurrences reference gameplay categories; optional scientific catalogs do not split entities or expand s…` |

### `$.worldRules`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `hexagonalMap` | `boolean` | 1/1 | Indica si el mapa utiliza casillas hexagonales. | `true` |
| `dynamicWeatherEnabled` | `boolean` | 1/1 | Indica si incluye tiempo atmosférico dinámico; actualmente false. | `false` |
| `seasonsEnabled` | `boolean` | 1/1 | Indica si incluye estaciones; actualmente false. | `false` |
| `dynamicClimateDisastersEnabled` | `boolean` | 1/1 | Indica si incluye desastres climáticos dinámicos; actualmente false. | `false` |
| `staticEnvironmentalConditionsUsed` | `boolean` | 1/1 | Indica si condiciones ambientales estáticas restringen la generación. | `true` |
| `maximumRegionalVariantsPerBiome` | `integer` | 1/1 | Máximo actual de variantes regionales por bioma, no probabilidad de aparición. | `4` |
| `resourceDiscoverySeparateFromExistence` | `boolean` | 1/1 | Los recursos pueden existir antes de que una civilización los descubra. | `true` |
| `potentialCultivationSeparateFromEstablishedCrops` | `boolean` | 1/1 | Poder cultivar no implica que ya exista un cultivo establecido. | `true` |

### `$.elevationLevels[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `integer` | 4/4 | Categoría numérica de elevación 0–3, no un ID de entidad con prefijo. | `0` |
| `name` | `object` | 4/4 | Nombre visible mediante claves de idioma. | `—` |
| `ordinaryLandTraversal` | `boolean \| string` | 4/4 | Transitabilidad o restricción explicativa; actualmente booleano o texto. | `"depends_on_land_or_water_surface"` |
| `movementAndConstructionRestrictions` | `null` | 1/4 | Restricciones explicativas de movimiento y construcción. | `null` |
| `conventionalSettlementsAllowed` | `boolean` | 1/4 | Indica si permite asentamientos convencionales en este nivel. | `false` |

### `$.elevationLevels[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 4/4 | Texto visible en inglés. | `"Sea Level"` |
| `es` | `string` | 4/4 | Texto visible en español. | `"Nivel del mar"` |

### `$.geographicModifiers[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 6/6 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"river_floodplain"` |
| `name` | `object` | 6/6 | Nombre visible mediante claves de idioma. | `—` |

### `$.geographicModifiers[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 6/6 | Texto visible en inglés. | `"River and Floodplain"` |
| `es` | `string` | 6/6 | Texto visible en español. | `"Río y llanura aluvial"` |

### `$.biomes[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"tropical_forest"` |
| `name` | `object` | 7/7 | Nombre visible mediante claves de idioma. | `—` |
| `interfaceCategoryOnly` | `boolean` | 7/7 | True indica categoría de interfaz, no definición completa de hábitat. | `true` |

### `$.biomes[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 7/7 | Texto visible en inglés. | `"Tropical Forest"` |
| `es` | `string` | 7/7 | Texto visible en español. | `"Bosque tropical"` |

### `$.regionalVariants[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 27/27 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"tropical_forest_american"` |
| `biomeId` | `string` | 27/27 | Referencia a la definición de bioma. | `"tropical_forest"` |
| `name` | `object` | 27/27 | Nombre visible mediante claves de idioma. | `—` |
| `nativeRegionIds` | `array<?>` | 27/27 | Referencias a regiones nativas; vacío significa pendiente, no distribución mundial. | `[]` |
| `resolutionStatus` | `string` | 27/27 | Tarea pendiente para resolver el candidato o restricción regional. | `"regional_constraints_require_definition"` |

### `$.regionalVariants[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 27/27 | Texto visible en inglés. | `"American"` |
| `es` | `string` | 27/27 | Texto visible en español. | `"Americano (selvas húmedas y bosques secos)"` |

### `$.resourceOccurrences[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 485/485 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"occurrence_0001"` |
| `definitionId` | `string` | 485/485 | Referencia a la definición candidata, no al ID de una población generada. | `"geological_alluvial_clay"` |
| `kind` | `string` | 485/485 | Discriminador que identifica el documento o categoría del candidato. | `"geological"` |
| `biomeId` | `string` | 485/485 | Referencia a la definición de bioma. | `"tropical_forest"` |
| `variantId` | `string` | 485/485 | Referencia a una variante regional. | `"tropical_forest_american"` |
| `extractionMethodId` | `null \| string` | 485/485 | Identificador de etapa de extracción de la fuente, no una receta verificada. | `"surface_collection"` |
| `sourceText` | `string` | 485/485 | Texto original en español de la aparición; se conserva para auditoría, no para interfaz. | `"Arcilla aluvial"` |
| `constraintsStatus` | `string` | 485/485 | Avance al convertir restricciones cualitativas en condiciones ejecutables. | `"qualitative_source_constraints_preserved_pending_formalization"` |
| `spawnProbability` | `null` | 485/485 | Probabilidad de aparición pendiente; null no es cero ni aparición segura. | `null` |
| `guaranteedPresence` | `boolean` | 485/485 | Indica presencia garantizada; false no implica imposibilidad. | `false` |
| `runtimeEnabled` | `boolean` | 485/485 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |
| `sourceDefinitionId` | `string` | 92/485 | Identidad original antes de generalizar; definitionId apunta a la categoría vigente del juego. | `"animal_mesoamerican_white_tailed_deer"` |

### `$.reviewIssues[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"regional_variant_count"` |
| `sourceClaim` | `integer` | 2/7 | Conteo declarado por la fuente; comparar con actualCount. | `26` |
| `actualCount` | `integer` | 2/7 | Conteo obtenido de los registros enumerados. | `27` |
| `resolution` | `string` | 7/7 | Interpretación documentada o siguiente acción de revisión. | `"Use the enumerated 27 variants; retain the discrepancy for review."` |

### `$.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `biomeCount` | `integer` | 1/1 | Cantidad de biomas. | `7` |
| `regionalVariantCount` | `integer` | 1/1 | Cantidad de variantes regionales. | `27` |
| `plantCandidateCount` | `integer` | 1/1 | Cantidad de candidatos vegetales regionales. | `109` |
| `animalCandidateCount` | `integer` | 1/1 | Cantidad de candidatos animales. | `101` |
| `geologicalCandidateCount` | `integer` | 1/1 | Cantidad de candidatos geológicos. | `57` |
| `sourceOccurrenceCount` | `integer` | 1/1 | Cantidad de apariciones de la fuente. | `485` |
| `agriculturalCropCandidateCount` | `integer` | 1/1 | Cantidad de candidatos agrícolas. | `21` |

### `$.hexDefinitionGuide`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `definitionFields` | `array<string>` | 1/1 | Nombres propuestos de campos estáticos; estas cadenas no son propiedades anidadas reales. | `["terrainType", "elevationLevel", "surfaceType"]` |
| `stateFields` | `array<string>` | 1/1 | Nombres propuestos de campos mutables de instancia; tipos pendientes. | `["presentPopulationIds", "presentDepositIds", "discoveryByCivilization"]` |
| `numericRanges` | `null` | 1/1 | Rangos numéricos pendientes de diseño. | `null` |
| `separation` | `string` | 1/1 | Explica la separación entre definiciones reutilizables y estado del mapa generado. | `"The actual generated map and its discoveries belong to GameState; catalog definitions and generation constraint…` |

### `$.depositDefinitionGuide`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `fields` | `array<string>` | 1/1 | Nombres de campos propuestos, no registros ya instanciados. | `["materialId", "reserveAmount", "grade"]` |
| `numericalValues` | `null` | 1/1 | Parámetros numéricos del yacimiento pendientes. | `null` |
| `depletionAndRegenerationRules` | `null` | 1/1 | Reglas de agotamiento y renovación de reservas pendientes. | `null` |
| `stateSeparation` | `string` | 1/1 | Explica por qué reservas y descubrimiento pertenecen a la partida. | `"Actual reserves and discovery belong to each deposit instance in GameState."` |

### `$.catalogFiles`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `plantCandidates` | `string` | 1/1 | Ruta relativa a la guía de plantas y cultivos. | `"../plants/plants.catalog.guide.json"` |
| `animalCandidates` | `string` | 1/1 | Ruta relativa a la guía de animales. | `"../animals/animals.catalog.guide.json"` |
| `geologicalCandidates` | `string` | 1/1 | Ruta relativa a la guía geológica. | `"../minerals/minerals.catalog.guide.json"` |
| `resources` | `string` | 1/1 | Registros de recursos en la raíz, o ruta relativa al catálogo dentro de catalogFiles. | `"../resources/resources.catalog.guide.json"` |
| `plantBiology` | `string` | 1/1 | Ruta relativa del manifiesto mundial al catálogo biológico de flora. | `"../plants/plants.biological.catalog.json"` |
| `animalBiology` | `string` | 1/1 | Ruta relativa del manifiesto mundial al catálogo biológico de fauna. | `"../animals/animals.biological.catalog.json"` |

### `$.repositoryPackaging`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `layout` | `string` | 1/1 | Organización: catálogos al mismo nivel relacionados por IDs. | `"flat_linked_catalogs"` |
| `change` | `string` | 1/1 | Descripción del cambio de organización. | `"Candidate collections were moved without renaming IDs; occurrence references resolve across the linked catalogs."` |
| `sourceOccurrenceCount` | `integer` | 1/1 | Cantidad de apariciones de la fuente. | `485` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.4.0",
  "contentVersion": "0.5.0",
  "kind": "world_catalog_design_guide",
  "status": "source_converted_requires_species_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "source": {
    "title": "Documentacion Evolve",
    "format": "docx_snapshot",
    "connectorFileId": "11FrriHGZ9AKnrXFND-VNWzmNKJo_U2aCS9OFZyWo9c8",
    "sha256": "151ea42d39ce1bc9d26d76e18dc1a9d8a5fbb9f888519c240d99fe7793271308",
    "snapshotOnly": true,
    "originalDocumentModified": false
  },
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "reason": "This is a gameplay design guide, not an executable world generator. General categories are valid; scientific species resolution is optional.",
    "unknownValues": "null means unresolved; it never means zero, none, unrestricted or approved.",
    "visibleText": "name and description use language maps; sourceText and sourceLabel preserve verbatim Spanish provenance and must not be displayed as localized game text.",
    "flatCollections": "All definitions are stored in flat collections and connected by stable IDs.",
    "preserveSpeciesResearch": "Gameplay entity IDs remain stable. Generalized sources keep explicit aliases and provenance; scientific taxonomy does not split research identities automatically.",
    "wildAndDomestic": "Wild presence, cultivation knowledge, domestication and established crop production are separate states.",
    "distribution": "Biome compatibility does not imply universal native distribution.",
    "geology": "Mineral distribution is controlled by geology, not mandatory biome resource lists.",
    "miningStages": "Extraction methods describe capabilities, not exclusive material eras.",
    "scope": "Mechanized mining and seabed nodules remain future content outside the initial medieval scope.",
    "biologicalGranularity": "World occurrences reference gameplay categories; optional scientific catalogs do not split entities or expand spawns. Original sourceDefinitionId/sourceText preserve provenance."
  },
  "worldRules": {
    "hexagonalMap": true,
    "dynamicWeatherEnabled": false,
    "seasonsEnabled": false,
    "dynamicClimateDisastersEnabled": false,
    "staticEnvironmentalConditionsUsed": true,
    "maximumRegionalVariantsPerBiome": 4,
    "resourceDiscoverySeparateFromExistence": true,
    "potentialCultivationSeparateFromEstablishedCrops": true
  },
  "elevationLevels": [
    {
      "id": 0,
      "name": {
        "en": "Sea Level",
        "es": "Nivel del mar"
      },
      "ordinaryLandTraversal": "depends_on_land_or_water_surface"
    },
    {
      "id": 1,
      "name": {
        "en": "Middle Elevation",
        "es": "Nivel medio"
      },
      "ordinaryLandTraversal": true
    },
    {
      "id": 2,
      "name": {
        "en": "High Elevation",
        "es": "Nivel alto"
      },
      "ordinaryLandTraversal": true,
      "movementAndConstructionRestrictions": null
    },
    {
      "id": 3,
      "name": {
        "en": "Impassable Summits",
        "es": "Cumbres infranqueables"
      },
      "ordinaryLandTraversal": false,
      "conventionalSettlementsAllowed": false
    }
  ],
  "geographicModifiers": [
    {
      "id": "river_floodplain",
      "name": {
        "en": "River and Floodplain",
        "es": "Río y llanura aluvial"
      }
    }
  ],
  "biomes": [
    {
      "id": "tropical_forest",
      "name": {
        "en": "Tropical Forest",
        "es": "Bosque tropical"
      },
      "interfaceCategoryOnly": true
    }
  ],
  "regionalVariants": [
    {
      "id": "tropical_forest_american",
      "biomeId": "tropical_forest",
      "name": {
        "en": "American",
        "es": "Americano (selvas húmedas y bosques secos)"
      },
      "nativeRegionIds": [],
      "resolutionStatus": "regional_constraints_require_definition"
    }
  ],
  "resourceOccurrences": [
    {
      "id": "occurrence_0001",
      "definitionId": "geological_alluvial_clay",
      "kind": "geological",
      "biomeId": "tropical_forest",
      "variantId": "tropical_forest_american",
      "extractionMethodId": "surface_collection",
      "sourceText": "Arcilla aluvial",
      "constraintsStatus": "qualitative_source_constraints_preserved_pending_formalization",
      "spawnProbability": null,
      "guaranteedPresence": false,
      "runtimeEnabled": false
    }
  ],
  "generationPipeline": [
    "generate_terrain_water_static_climate_and_biogeographic_regions",
    "assign_biomes_and_geographic_modifiers",
    "generate_geological_provinces_and_candidate_deposits",
    "distribute_native_wild_species_using_region_and_habitat",
    "evaluate_soil_fertility_and_cultivation_suitability",
    "apply_visibility_discovery_and_exploitation_capabilities",
    "validate_alternative_development_trade_and_expansion_paths"
  ],
  "speciesCompletionChecklist": [
    "choose_general_gameplay_entity_and_stable_id",
    "preserve_regional_habitat_rules_and_source_provenance",
    "group_cosmetic_or_scientific_variants_without_gameplay_differences",
    "retain_useful_wild_and_domestic_distinctions",
    "define_ecological_compatibility",
    "define_propagation_and_cultivation_or_animal_management",
    "define_material_resources_and_products",
    "define_technology_requirements_and_scope",
    "define_domestication_criteria_where_relevant",
    "defer_quantities_durations_and_balance_until_simulation_design"
  ],
  "reviewIssues": [
    {
      "id": "regional_variant_count",
      "sourceClaim": 26,
      "actualCount": 27,
      "resolution": "Use the enumerated 27 variants; retain the discrepancy for review."
    },
    {
      "id": "biome_count",
      "sourceClaim": 10,
      "actualCount": 7,
      "resolution": "The pending-decisions paragraph says ten; the detailed catalog and latest history specify seven."
    },
    {
      "id": "broad_taxa",
      "resolution": "Keep regional groups as candidates; do not silently choose a species."
    },
    {
      "id": "possible_duplicate_taxa",
      "resolution": "Similar names and habitat-qualified duplicates retain separate candidate IDs until verified and merged explicitly."
    },
    {
      "id": "marine_nodules",
      "resolution": "Do not infer coastal shallow-water availability from their placement in marine UI variants; require verified seabed geology and future extraction."
    },
    {
      "id": "tundra_lichens",
      "resolution": "Lichens are retained under the source flora category for traceability; scientific classification must be resolved separately."
    },
    {
      "id": "fauna_products",
      "resolution": "Potential outputs are not verified yields or automatic unlocks; milk, eggs, pearls and work require species-appropriate conditions."
    }
  ],
  "sourceDistributionNotes": [
    "Los siete biomas son categorías de interfaz; cada subtipo mantiene clima, terreno, hábitat y región propios.",
    "Bosque tropical húmedo y bosque tropical seco no comparten automáticamente especies ni rendimientos.",
    "La taiga, el matorral mediterráneo, la sabana tropical y la estepa templada conservan condiciones ecológicas distintas."
  ],
  "agricultureSectionSource": [
    "5. Catálogo agrícola y vegetal inicial",
    "Los recursos agrícolas deben distinguir tres estados conceptuales: (A) planta silvestre presente en el mapa; (B) especie conocida y susceptible de domesticación o cultivo; (C) cultivo domesticado y producido por la civilización. Una planta cultivable no se convierte automáticamente en alimento agrícola disponible.",
    "5.1. Granos y cereales",
    "Trigo y cebada: origen y difusión vinculados históricamente al sudoeste asiático; aptos para regiones templadas o mediterráneas adecuadas. Arroz: ambientes cálidos y húmedos o con agua gestionada, con origen y difusión regionales propios. Maíz: origen mesoamericano y posterior expansión. Sorgo y mijo: alternativas relevantes en entornos cálidos y relativamente secos.",
    "5.2. Tubérculos y raíces",
    "Papa: domesticación andina y aptitud para determinados ambientes de altura o templados frescos. Yuca/mandioca: origen sudamericano y aptitud tropical. Otros tubérculos locales podrán añadirse al catálogo regional.",
    "5.3. Legumbres y hortalizas",
    "Frijoles, lentejas, garbanzos, guisantes y calabazas son familias o especies con orígenes y necesidades diferentes. La lista definitiva deberá distinguir especies concretas, regiones nativas y técnicas agrícolas.",
    "5.4. Frutales, productos especiales y fibras",
    "Vid, olivo, higuera y palmera datilera para regiones compatibles; cacao en zonas tropicales americanas adecuadas; café en ambientes tropicales de altura y regiones históricas de origen; caña de azúcar en climas cálidos y húmedos; algodón y otras fibras según especie y región. Su presencia silvestre, domesticación y circulación por comercio se definirán por separado.",
    "5.5. Reglas para especies y distribución",
    "Cada especie vegetal tendrá, como mínimo, nombre, categoría, región de origen, condiciones ecológicas, estado silvestre o domesticado, productos posibles y conocimientos requeridos. El comercio, las migraciones y la exploración podrán introducir especies en regiones donde no son nativas, siempre que las condiciones permitan cultivarlas. No se asume que todos los biomas del mundo compartan las mismas especies."
  ],
  "summary": {
    "biomeCount": 7,
    "regionalVariantCount": 27,
    "plantCandidateCount": 109,
    "animalCandidateCount": 101,
    "geologicalCandidateCount": 57,
    "sourceOccurrenceCount": 485,
    "agriculturalCropCandidateCount": 21
  },
  "hexDefinitionGuide": {
    "definitionFields": [
      "terrainType",
      "elevationLevel",
      "surfaceType",
      "biomeId",
      "regionalVariantId",
      "staticTemperature",
      "staticMoisture",
      "freshwaterAvailability",
      "soilCharacteristics",
      "fertility",
      "biogeographicRegionId",
      "geologicalProvinceId",
      "geographicModifierIds"
    ],
    "stateFields": [
      "presentPopulationIds",
      "presentDepositIds",
      "discoveryByCivilization",
      "territorialControl",
      "constructionIds"
    ],
    "numericRanges": null,
    "separation": "The actual generated map and its discoveries belong to GameState; catalog definitions and generation constraints belong to GameDefinitions."
  },
  "depositDefinitionGuide": {
    "fields": [
      "materialId",
      "reserveAmount",
      "grade",
      "accessibility",
      "discoveryState",
      "extractionTechnologyIds",
      "processingRecipeIds"
    ],
    "numericalValues": null,
    "depletionAndRegenerationRules": null,
    "stateSeparation": "Actual reserves and discovery belong to each deposit instance in GameState."
  },
  "catalogFiles": {
    "plantCandidates": "../plants/plants.catalog.guide.json",
    "animalCandidates": "../animals/animals.catalog.guide.json",
    "geologicalCandidates": "../minerals/minerals.catalog.guide.json",
    "resources": "../resources/resources.catalog.guide.json",
    "plantBiology": "../plants/plants.biological.catalog.json",
    "animalBiology": "../animals/animals.biological.catalog.json"
  },
  "repositoryPackaging": {
    "layout": "flat_linked_catalogs",
    "change": "Candidate collections were moved without renaming IDs; occurrence references resolve across the linked catalogs.",
    "sourceOccurrenceCount": 485
  }
}
```

## Campos futuros propuestos de casilla y yacimiento

Estos nombres solo aparecen como cadenas en listas de la guía. Sus tipos finales, anidamiento y unidades/rangos aún no están definidos; esta tabla no es un esquema ejecutable. La casilla o yacimiento generado pertenece a GameState, incluso para valores que no cambian tras generarse.

| Lista guía | Campo propuesto | Significado | Tipo/madurez |
| --- | --- | --- | --- |
| `hexDefinitionGuide.definitionFields` | `terrainType` | Categoría de terreno. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `elevationLevel` | Categoría de elevación. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `surfaceType` | Superficie terrestre o acuática. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `biomeId` | Referencia de bioma. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `regionalVariantId` | Referencia de variante regional. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `staticTemperature` | Condiciones térmicas estáticas. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `staticMoisture` | Condiciones estáticas de humedad. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `freshwaterAvailability` | Disponibilidad de agua dulce. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `soilCharacteristics` | Propiedades del suelo. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `fertility` | Parámetros de fertilidad. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `biogeographicRegionId` | Referencia de región biogeográfica. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `geologicalProvinceId` | Referencia de provincia geológica. | Pendiente; solo diseño |
| `hexDefinitionGuide.definitionFields` | `geographicModifierIds` | Referencias de modificadores geográficos. | Pendiente; solo diseño |
| `hexDefinitionGuide.stateFields` | `presentPopulationIds` | Poblaciones presentes en casilla. | Pendiente; solo diseño |
| `hexDefinitionGuide.stateFields` | `presentDepositIds` | Yacimientos presentes en casilla. | Pendiente; solo diseño |
| `hexDefinitionGuide.stateFields` | `discoveryByCivilization` | Descubrimientos por civilización. | Pendiente; solo diseño |
| `hexDefinitionGuide.stateFields` | `territorialControl` | Control territorial actual. | Pendiente; solo diseño |
| `hexDefinitionGuide.stateFields` | `constructionIds` | Construcciones de la casilla. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `materialId` | Material asociado al yacimiento. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `reserveAmount` | Reserva restante del yacimiento. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `grade` | Concentración/calidad del material. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `accessibility` | Restricciones de acceso. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `discoveryState` | Estado de descubrimiento del yacimiento. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `extractionTechnologyIds` | Referencias tecnológicas de extracción. | Pendiente; solo diseño |
| `depositDefinitionGuide.fields` | `processingRecipeIds` | Referencias a recetas de procesamiento. | Pendiente; solo diseño |
