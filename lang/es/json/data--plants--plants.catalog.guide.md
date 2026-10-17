# `data/plants/plants.catalog.guide.json`

[JSON fuente](../../../data/plants/plants.catalog.guide.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"1.2.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.3.0"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"plant_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Candidatos al mismo nivel; los grupos generales todavía no son especies exactas aceptadas. | `—` |
| `agriculturalCropCandidates` | `array<object>` | 1/1 | Grupos agrícolas vinculados a taxones/formas seleccionados; ancestros y reglas productivas siguen parcialmente pendientes. | `—` |
| `biologicalCatalogFile` | `string` | 1/1 | Archivo biológico relacionado; conserva los IDs de candidatos anteriores. | `"plants.biological.catalog.json"` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.speciesCandidates[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 129/129 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"plant_dwarf_birch"` |
| `kind` | `string` | 129/129 | Discriminador que identifica el documento o categoría del candidato. | `"plant"` |
| `name` | `object` | 129/129 | Nombre visible mediante claves de idioma. | `—` |
| `taxonomy` | `object` | 129/129 | Identidad científica, evidencia y revisión. | `—` |
| `definitionStatus` | `string` | 129/129 | Madurez del registro; los candidatos no son definiciones ejecutables. | `"design_guide_only"` |
| `nativeRegionIds` | `array<?>` | 129/129 | Referencias a regiones nativas; vacío significa pendiente, no distribución mundial. | `[]` |
| `biomeVariantIds` | `array<string>` | 129/129 | Referencias a variantes regionales que enumeran este candidato. | `["tundra_eurasian"]` |
| `ecology` | `object` | 129/129 | Requisitos ambientales; los valores cuantitativos están pendientes. | `—` |
| `propagation` | `object` | 129/129 | Métodos de reproducción y materiales requeridos, todavía en diseño. | `—` |
| `domestication` | `object` | 129/129 | Elegibilidad, relaciones con ancestros/formas y criterios de selección. | `—` |
| `potentialProducts` | `array<object> \| null` | 129/129 | Usos potenciales de la fuente; no son productos, cantidades o desbloqueos confirmados. | `—` |
| `potentialUseMethods` | `array<?>` | 129/129 | Métodos de uso potenciales de la fuente, no acciones ya autorizadas del juego. | `[]` |
| `cultivationResearch` | `object` | 129/129 | Relación ilustrativa con investigación por especie; null indica vínculo no definido. | `—` |
| `sourceLabel` | `string` | 129/129 | Etiqueta original en español para trazabilidad, no texto localizado de interfaz. | `"Abedul enano"` |
| `initialPresencePolicy` | `string` | 129/129 | Restricciones que deben resolverse antes de la aparición inicial. | `"resolve_native_region_and_habitat_before_spawning"` |
| `taxonResolution` | `object` | 129/129 | Selección explícita de taxones y formas de referencia; no es regla de aparición ni producción. | `—` |

### `$.speciesCandidates[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 129/129 | Texto visible en inglés. | `"Dwarf Birch"` |
| `es` | `string` | 129/129 | Texto visible en español. | `"Abedul enano"` |

### `$.speciesCandidates[].taxonomy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 129/129 | Nombre científico de la fuente o del registro aceptado del proveedor; null en la fuente original significa pendiente allí. | `"Nothofagus dombeyi"` |
| `nameEvidence` | `string` | 129/129 | Evidencia del nombre científico registrado o de su ausencia. | `"not_supplied"` |
| `resolutionStatus` | `string` | 129/129 | Tarea pendiente para resolver el candidato o restricción regional. | `"linked_to_taxon_catalog_source_interpretation_still_requires_review"` |
| `verified` | `boolean` | 129/129 | Indica si existe verificación científica; los candidatos actuales no están verificados. | `false` |

### `$.speciesCandidates[].ecology`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 129/129 | Límites de temperatura en grados Celsius; null todavía no tiene estructura interna definida. | `null` |
| `moistureRange` | `null` | 129/129 | Límites de humedad; unidades y estructura pendientes. | `null` |
| `elevationRangeM` | `null` | 129/129 | Límites de elevación en metros; valores y estructura pendientes. | `null` |
| `waterRequirements` | `null` | 129/129 | Necesidades de agua; pendiente no significa que no necesite agua. | `null` |
| `soilRequirements` | `null` | 129/129 | Restricciones de suelo pendientes de estructura. | `null` |
| `habitatRestrictionsStatus` | `string` | 129/129 | Explicación técnica sobre restricciones de hábitat pendientes. | `"See source occurrences; quantitative constraints remain undefined."` |

### `$.speciesCandidates[].propagation`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 129/129 | Métodos de reproducción admitidos; null significa pendiente. | `null` |
| `materialResourceIds` | `null` | 129/129 | Referencias a recursos de reproducción; null significa relaciones pendientes. | `null` |

### `$.speciesCandidates[].domestication`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 129/129 | Elegibilidad del candidato para este mecanismo y revisión necesaria. | `"requires_species_review"` |
| `wildAncestorId` | `null` | 129/129 | Referencia al ancestro silvestre elegido, sin deducirlo automáticamente. | `null` |
| `domesticatedFormId` | `null` | 129/129 | Referencia a la forma domesticada; no concede domesticación instantánea. | `null` |
| `criteria` | `null` | 129/129 | Criterios de domesticación todavía no modelados. | `null` |

### `$.speciesCandidates[].cultivationResearch`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 129/129 | Referencia a una definición tecnológica o importación externa declarada. | `"species_cultivation"` |
| `speciesId` | `string` | 129/129 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"plant_dwarf_birch"` |
| `eligibility` | `string` | 129/129 | Elegibilidad del candidato para este mecanismo y revisión necesaria. | `"Only instantiate after the exact species is confirmed cultivable; flora presence alone does not imply agricultu…` |

### `$.speciesCandidates[].taxonResolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 129/129 | Referencias de taxones elegidos; las selecciones de grupos no son exhaustivas. | `["PLT#000025"]` |
| `formIds` | `array<string>` | 129/129 | Formas biológicas relacionadas; no son las formas aprobadas para aparecer en esa ubicación. | `[]` |
| `selectionMode` | `string` | 129/129 | Indica interpretación específica o selección representativa de especies/cultivos. | `"specific_name_interpretation"` |
| `interpretationStatus` | `string` | 129/129 | Estado de interpretación de la etiqueta original, independiente del cotejo del nombre científico. | `"proposed_requires_native_range_and_habitat_review"` |
| `inheritResourceBindings` | `boolean` | 129/129 | False: los taxones/formas no heredan automáticamente productos del candidato. | `false` |

### `$.speciesCandidates[].potentialProducts[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 20/20 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000021"` |
| `status` | `string` | 20/20 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"proposed_requires_species_and_action_review"` |
| `requiredTechnologyIds` | `null` | 20/20 | Referencias tecnológicas del producto; null significa pendiente, no ningún requisito. | `null` |
| `yield` | `null` | 20/20 | Rendimiento; unidad, fórmula y cantidad pendientes. | `null` |

### `$.agriculturalCropCandidates[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 21/21 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"wheat"` |
| `name` | `object` | 21/21 | Nombre visible mediante claves de idioma. | `—` |
| `cropUseTag` | `string` | 21/21 | Grupo de uso agrícola del juego, no especie botánica. | `"cereal"` |
| `sourceOriginHint` | `null \| string` | 21/21 | Indicación de origen de la fuente, no una regla verificada de distribución nativa. | `"Southwest Asia"` |
| `scientificName` | `null` | 21/21 | Nombre científico de la fuente o del registro aceptado del proveedor; null en la fuente original significa pendiente allí. | `null` |
| `resolutionStatus` | `string` | 21/21 | Tarea pendiente para resolver el candidato o restricción regional. | `"select_exact_species_and_wild_ancestor"` |
| `wildAncestorCandidateIds` | `array<?>` | 21/21 | Posibles ancestros pendientes de revisión científica. | `[]` |
| `cultivationResearch` | `object` | 21/21 | Relación ilustrativa con investigación por especie; null indica vínculo no definido. | `—` |
| `products` | `array<object>` | 21/21 | Productos agrícolas pendientes de recursos y recetas. | `—` |
| `ecologicalConstraints` | `null` | 21/21 | Reglas ambientales del cultivo pendientes de formalización. | `null` |
| `sourceSection` | `string` | 21/21 | Sección de la fuente de la que se extrajo la entrada. | `"5. Initial agricultural and plant catalog"` |
| `taxonResolution` | `object` | 21/21 | Selección explícita de taxones y formas de referencia; no es regla de aparición ni producción. | `—` |

### `$.agriculturalCropCandidates[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 21/21 | Texto visible en inglés. | `"Wheat"` |
| `es` | `string` | 21/21 | Texto visible en español. | `"Trigo"` |

### `$.agriculturalCropCandidates[].cultivationResearch`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 21/21 | Referencia a una definición tecnológica o importación externa declarada. | `"species_cultivation"` |
| `speciesId` | `string` | 21/21 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"wheat"` |

### `$.agriculturalCropCandidates[].products[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 24/24 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000007"` |
| `status` | `string` | 24/24 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"proposed_requires_species_and_action_review"` |
| `requiredTechnologyIds` | `null` | 24/24 | Referencias tecnológicas del producto; null significa pendiente, no ningún requisito. | `null` |
| `yield` | `null` | 24/24 | Rendimiento; unidad, fórmula y cantidad pendientes. | `null` |

### `$.agriculturalCropCandidates[].taxonResolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 21/21 | Referencias de taxones elegidos; las selecciones de grupos no son exhaustivas. | `["PLT#000173", "PLT#000175", "PLT#000176"]` |
| `formIds` | `array<string>` | 21/21 | Formas biológicas relacionadas; no son las formas aprobadas para aparecer en esa ubicación. | `["FRM#000001", "FRM#000002", "FRM#000003"]` |
| `selectionMode` | `string` | 21/21 | Indica interpretación específica o selección representativa de especies/cultivos. | `"explicit_crop_taxa_selection"` |
| `interpretationStatus` | `string` | 21/21 | Estado de interpretación de la etiqueta original, independiente del cotejo del nombre científico. | `"crop_group_resolved_to_selected_taxa_ancestry_review_not_complete"` |
| `inheritResourceBindings` | `boolean` | 21/21 | False: los taxones/formas no heredan automáticamente productos del candidato. | `false` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.2.0",
  "contentVersion": "0.3.0",
  "status": "design_guide_requires_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "null means unresolved; it is not zero or unrestricted."
  },
  "kind": "plant_catalog_design_guide",
  "speciesCandidates": [
    {
      "id": "plant_dwarf_birch",
      "kind": "plant",
      "name": {
        "en": "Dwarf Birch",
        "es": "Abedul enano"
      },
      "taxonomy": {
        "scientificName": null,
        "nameEvidence": "not_supplied",
        "resolutionStatus": "linked_to_taxon_catalog_source_interpretation_still_requires_review",
        "verified": false
      },
      "definitionStatus": "design_guide_only",
      "nativeRegionIds": [],
      "biomeVariantIds": [
        "tundra_eurasian"
      ],
      "ecology": {
        "temperatureRangeC": null,
        "moistureRange": null,
        "elevationRangeM": null,
        "waterRequirements": null,
        "soilRequirements": null,
        "habitatRestrictionsStatus": "See source occurrences; quantitative constraints remain undefined."
      },
      "propagation": {
        "methods": null,
        "materialResourceIds": null
      },
      "domestication": {
        "eligibility": "requires_species_review",
        "wildAncestorId": null,
        "domesticatedFormId": null,
        "criteria": null
      },
      "potentialProducts": null,
      "potentialUseMethods": [],
      "cultivationResearch": {
        "technologyId": "species_cultivation",
        "speciesId": "plant_dwarf_birch",
        "eligibility": "Only instantiate after the exact species is confirmed cultivable; flora presence alone does not imply agricultural use."
      },
      "sourceLabel": "Abedul enano",
      "initialPresencePolicy": "resolve_native_region_and_habitat_before_spawning",
      "taxonResolution": {
        "taxonIds": [
          "PLT#000025"
        ],
        "formIds": [],
        "selectionMode": "specific_name_interpretation",
        "interpretationStatus": "proposed_requires_native_range_and_habitat_review",
        "inheritResourceBindings": false
      }
    }
  ],
  "agriculturalCropCandidates": [
    {
      "id": "wheat",
      "name": {
        "en": "Wheat",
        "es": "Trigo"
      },
      "cropUseTag": "cereal",
      "sourceOriginHint": "Southwest Asia",
      "scientificName": null,
      "resolutionStatus": "select_exact_species_and_wild_ancestor",
      "wildAncestorCandidateIds": [],
      "cultivationResearch": {
        "technologyId": "species_cultivation",
        "speciesId": "wheat"
      },
      "products": [
        {
          "resourceId": "RES#000007",
          "status": "proposed_requires_species_and_action_review",
          "requiredTechnologyIds": null,
          "yield": null
        }
      ],
      "ecologicalConstraints": null,
      "sourceSection": "5. Initial agricultural and plant catalog",
      "taxonResolution": {
        "taxonIds": [
          "PLT#000173",
          "PLT#000175",
          "PLT#000176",
          "PLT#000171"
        ],
        "formIds": [
          "FRM#000001",
          "FRM#000002",
          "FRM#000003",
          "FRM#000004"
        ],
        "selectionMode": "explicit_crop_taxa_selection",
        "interpretationStatus": "crop_group_resolved_to_selected_taxa_ancestry_review_not_complete",
        "inheritResourceBindings": false
      }
    }
  ],
  "biologicalCatalogFile": "plants.biological.catalog.json"
}
```
