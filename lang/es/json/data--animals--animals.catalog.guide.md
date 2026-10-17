# `data/animals/animals.catalog.guide.json`

[JSON fuente](../../../data/animals/animals.catalog.guide.json) · [Index](../json-structures.md)

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
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"animal_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Candidatos al mismo nivel; los grupos generales todavía no son especies exactas aceptadas. | `—` |
| `biologicalCatalogFile` | `string` | 1/1 | Archivo biológico relacionado; conserva los IDs de candidatos anteriores. | `"animals.biological.catalog.json"` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.speciesCandidates[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 134/134 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"animal_eurasian_moose"` |
| `kind` | `string` | 134/134 | Discriminador que identifica el documento o categoría del candidato. | `"animal"` |
| `name` | `object` | 134/134 | Nombre visible mediante claves de idioma. | `—` |
| `taxonomy` | `object` | 134/134 | Identidad científica, evidencia y revisión. | `—` |
| `definitionStatus` | `string` | 134/134 | Madurez del registro; los candidatos no son definiciones ejecutables. | `"design_guide_only"` |
| `nativeRegionIds` | `array<?>` | 134/134 | Referencias a regiones nativas; vacío significa pendiente, no distribución mundial. | `[]` |
| `biomeVariantIds` | `array<string>` | 134/134 | Referencias a variantes regionales que enumeran este candidato. | `["temperate_forest_boreal"]` |
| `ecology` | `object` | 134/134 | Requisitos ambientales; los valores cuantitativos están pendientes. | `—` |
| `propagation` | `object` | 134/134 | Métodos de reproducción y materiales requeridos, todavía en diseño. | `—` |
| `domestication` | `object` | 134/134 | Elegibilidad, relaciones con ancestros/formas y criterios de selección. | `—` |
| `potentialProducts` | `array<object>` | 134/134 | Usos potenciales de la fuente; no son productos, cantidades o desbloqueos confirmados. | `[]` |
| `potentialUseMethods` | `array<string>` | 134/134 | Métodos de uso potenciales de la fuente, no acciones ya autorizadas del juego. | `["hunting"]` |
| `cultivationResearch` | `null` | 134/134 | Relación ilustrativa con investigación por especie; null indica vínculo no definido. | `null` |
| `sourceLabel` | `string` | 134/134 | Etiqueta original en español para trazabilidad, no texto localizado de interfaz. | `"Alce euroasiático"` |
| `initialPresencePolicy` | `string` | 134/134 | Restricciones que deben resolverse antes de la aparición inicial. | `"resolve_native_region_and_habitat_before_spawning"` |
| `taxonResolution` | `object` | 134/134 | Selección explícita de taxones y formas de referencia; no es regla de aparición ni producción. | `—` |

### `$.speciesCandidates[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 134/134 | Texto visible en inglés. | `"Eurasian Moose"` |
| `es` | `string` | 134/134 | Texto visible en español. | `"Alce euroasiático"` |

### `$.speciesCandidates[].taxonomy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 134/134 | Nombre científico de la fuente o del registro aceptado del proveedor; null en la fuente original significa pendiente allí. | `"Gallus gallus"` |
| `nameEvidence` | `string` | 134/134 | Evidencia del nombre científico registrado o de su ausencia. | `"not_supplied"` |
| `resolutionStatus` | `string` | 134/134 | Tarea pendiente para resolver el candidato o restricción regional. | `"linked_to_taxon_catalog_source_interpretation_still_requires_review"` |
| `verified` | `boolean` | 134/134 | Indica si existe verificación científica; los candidatos actuales no están verificados. | `false` |

### `$.speciesCandidates[].ecology`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 134/134 | Límites de temperatura en grados Celsius; null todavía no tiene estructura interna definida. | `null` |
| `moistureRange` | `null` | 134/134 | Límites de humedad; unidades y estructura pendientes. | `null` |
| `elevationRangeM` | `null` | 134/134 | Límites de elevación en metros; valores y estructura pendientes. | `null` |
| `waterRequirements` | `null` | 134/134 | Necesidades de agua; pendiente no significa que no necesite agua. | `null` |
| `soilRequirements` | `null` | 134/134 | Restricciones de suelo pendientes de estructura. | `null` |
| `habitatRestrictionsStatus` | `string` | 134/134 | Explicación técnica sobre restricciones de hábitat pendientes. | `"See source occurrences; quantitative constraints remain undefined."` |

### `$.speciesCandidates[].propagation`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 134/134 | Métodos de reproducción admitidos; null significa pendiente. | `null` |
| `materialResourceIds` | `null` | 134/134 | Referencias a recursos de reproducción; null significa relaciones pendientes. | `null` |

### `$.speciesCandidates[].domestication`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 134/134 | Elegibilidad del candidato para este mecanismo y revisión necesaria. | `"requires_species_review"` |
| `wildAncestorId` | `null` | 134/134 | Referencia al ancestro silvestre elegido, sin deducirlo automáticamente. | `null` |
| `domesticatedFormId` | `null` | 134/134 | Referencia a la forma domesticada; no concede domesticación instantánea. | `null` |
| `criteria` | `null` | 134/134 | Criterios de domesticación todavía no modelados. | `null` |

### `$.speciesCandidates[].potentialProducts[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceTag` | `string` | 295/295 | Tag en inglés de categoría del recurso; no es ID resuelto. | `"meat"` |
| `status` | `string` | 295/295 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"potential_from_source"` |
| `requiredTechnologyIds` | `null` | 295/295 | Referencias tecnológicas del producto; null significa pendiente, no ningún requisito. | `null` |
| `yield` | `null` | 295/295 | Rendimiento; unidad, fórmula y cantidad pendientes. | `null` |
| `resourceId` | `string` | 264/295 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000029"` |

### `$.speciesCandidates[].taxonResolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 134/134 | Referencias de taxones elegidos; las selecciones de grupos no son exhaustivas. | `["ANM#000001"]` |
| `formIds` | `array<string>` | 134/134 | Formas biológicas relacionadas; no son las formas aprobadas para aparecer en esa ubicación. | `[]` |
| `selectionMode` | `string` | 134/134 | Indica interpretación específica o selección representativa de especies/cultivos. | `"specific_name_interpretation"` |
| `interpretationStatus` | `string` | 134/134 | Estado de interpretación de la etiqueta original, independiente del cotejo del nombre científico. | `"proposed_requires_native_range_and_habitat_review"` |
| `inheritResourceBindings` | `boolean` | 134/134 | False: los taxones/formas no heredan automáticamente productos del candidato. | `false` |

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
  "kind": "animal_catalog_design_guide",
  "speciesCandidates": [
    {
      "id": "animal_eurasian_moose",
      "kind": "animal",
      "name": {
        "en": "Eurasian Moose",
        "es": "Alce euroasiático"
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
        "temperate_forest_boreal"
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
      "potentialProducts": [
        {
          "resourceTag": "meat",
          "status": "potential_from_source",
          "requiredTechnologyIds": null,
          "yield": null,
          "resourceId": "RES#000029"
        }
      ],
      "potentialUseMethods": [
        "hunting"
      ],
      "cultivationResearch": null,
      "sourceLabel": "Alce euroasiático",
      "initialPresencePolicy": "resolve_native_region_and_habitat_before_spawning",
      "taxonResolution": {
        "taxonIds": [
          "ANM#000001"
        ],
        "formIds": [],
        "selectionMode": "specific_name_interpretation",
        "interpretationStatus": "proposed_requires_native_range_and_habitat_review",
        "inheritResourceBindings": false
      }
    }
  ],
  "biologicalCatalogFile": "animals.biological.catalog.json"
}
```
