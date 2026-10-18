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
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"1.3.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.5.0"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"animal_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Entidades candidatas al mismo nivel; las categorías generales son válidas y no requieren especie científica. | `—` |
| `biologicalCatalogFile` | `string` | 1/1 | Archivo biológico relacionado; conserva los IDs de candidatos anteriores. | `"animals.biological.catalog.json"` |
| `entityAliases` | `array<object>` | 1/1 | IDs regionales/específicos retirados que apuntan a una entidad general del juego. | `—` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved; it is not zero or unrestricted."` |
| `classificationPolicy` | `string` | 1/1 | Usa entidades generales salvo diferencias de recursos o comportamiento; la ciencia es opcional. | `"Use general gameplay entities when specific species add no meaningful resource or behavior distinction. Scienti…` |

### `$.speciesCandidates[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 101/101 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"ANM#000170"` |
| `kind` | `string` | 101/101 | Discriminador que identifica el documento o categoría del candidato. | `"animal"` |
| `name` | `object` | 101/101 | Nombre visible mediante claves de idioma. | `—` |
| `taxonomy` | `object` | 101/101 | Identidad científica, evidencia y revisión. | `—` |
| `definitionStatus` | `string` | 101/101 | Madurez del registro; los candidatos no son definiciones ejecutables. | `"general_gameplay_category_design_guide"` |
| `nativeRegionIds` | `array<?>` | 101/101 | Referencias a regiones nativas; vacío significa pendiente, no distribución mundial. | `[]` |
| `biomeVariantIds` | `array<string>` | 101/101 | Referencias a variantes regionales que enumeran este candidato. | `["temperate_forest_boreal"]` |
| `ecology` | `object` | 101/101 | Requisitos ambientales; los valores cuantitativos están pendientes. | `—` |
| `propagation` | `object` | 101/101 | Métodos de reproducción y materiales requeridos, todavía en diseño. | `—` |
| `domestication` | `object` | 101/101 | Elegibilidad, relaciones con ancestros/formas y criterios de selección. | `—` |
| `potentialProducts` | `array<object>` | 101/101 | Usos potenciales de la fuente; no son productos, cantidades o desbloqueos confirmados. | `[]` |
| `potentialUseMethods` | `array<string>` | 101/101 | Métodos de uso potenciales de la fuente, no acciones ya autorizadas del juego. | `["hunting"]` |
| `cultivationResearch` | `null` | 101/101 | Relación ilustrativa con investigación por especie; null indica vínculo no definido. | `null` |
| `sourceLabel` | `string` | 101/101 | Etiqueta original en español para trazabilidad, no texto localizado de interfaz. | `"Alce euroasiático"` |
| `initialPresencePolicy` | `string` | 101/101 | Restricciones que deben resolverse antes de la aparición inicial. | `"resolve_native_region_and_habitat_before_spawning"` |
| `taxonResolution` | `object` | 101/101 | Referencias científicas opcionales; no son requisito de identidad, aparición o acceso a recursos. | `—` |
| `tag` | `string` | 18/101 | Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales. | `"moose"` |
| `sourceVariants` | `array<object>` | 18/101 | Etiquetas originales y referencias regionales reunidas en una entidad del juego. | `—` |

### `$.speciesCandidates[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 101/101 | Texto visible en inglés. | `"Moose"` |
| `es` | `string` | 101/101 | Texto visible en español. | `"Alces"` |

### `$.speciesCandidates[].taxonomy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 101/101 | Nombre científico de la fuente o del registro aceptado del proveedor; null en la fuente original significa pendiente allí. | `"Gallus gallus"` |
| `nameEvidence` | `string` | 101/101 | Evidencia del nombre científico registrado o de su ausencia. | `"gameplay_category_not_scientific_species"` |
| `resolutionStatus` | `string` | 101/101 | Tarea pendiente para resolver el candidato o restricción regional. | `"scientific_species_not_required_for_gameplay_category"` |
| `verified` | `boolean` | 101/101 | Indica si existe verificación científica; los candidatos actuales no están verificados. | `false` |

### `$.speciesCandidates[].ecology`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 101/101 | Límites de temperatura en grados Celsius; null todavía no tiene estructura interna definida. | `null` |
| `moistureRange` | `null` | 101/101 | Límites de humedad; unidades y estructura pendientes. | `null` |
| `elevationRangeM` | `null` | 101/101 | Límites de elevación en metros; valores y estructura pendientes. | `null` |
| `waterRequirements` | `null` | 101/101 | Necesidades de agua; pendiente no significa que no necesite agua. | `null` |
| `soilRequirements` | `null` | 101/101 | Restricciones de suelo pendientes de estructura. | `null` |
| `habitatRestrictionsStatus` | `string` | 101/101 | Explicación técnica sobre restricciones de hábitat pendientes. | `"General gameplay category. Preserve regional source occurrences; do not spawn every historical form or infer wo…` |

### `$.speciesCandidates[].propagation`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 101/101 | Métodos de reproducción admitidos; null significa pendiente. | `null` |
| `materialResourceIds` | `null` | 101/101 | Referencias a recursos de reproducción; null significa relaciones pendientes. | `null` |

### `$.speciesCandidates[].domestication`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 101/101 | Elegibilidad del candidato para este mecanismo y revisión necesaria. | `"requires_gameplay_domestication_design"` |
| `wildAncestorId` | `null` | 101/101 | Referencia al ancestro silvestre elegido, sin deducirlo automáticamente. | `null` |
| `domesticatedFormId` | `null` | 101/101 | Referencia a la forma domesticada; no concede domesticación instantánea. | `null` |
| `criteria` | `null` | 101/101 | Criterios de domesticación todavía no modelados. | `null` |

### `$.speciesCandidates[].potentialProducts[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceTag` | `string` | 222/222 | Tag en inglés de categoría del recurso; no es ID resuelto. | `"meat"` |
| `status` | `string` | 222/222 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"potential_from_source"` |
| `requiredTechnologyIds` | `null` | 222/222 | Referencias tecnológicas del producto; null significa pendiente, no ningún requisito. | `null` |
| `yield` | `null` | 222/222 | Rendimiento; unidad, fórmula y cantidad pendientes. | `null` |
| `resourceId` | `string` | 205/222 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000029"` |

### `$.speciesCandidates[].taxonResolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 101/101 | Referencias de taxones elegidos; las selecciones de grupos no son exhaustivas. | `["ANM#000001", "ANM#000002"]` |
| `formIds` | `array<string>` | 101/101 | Formas biológicas relacionadas; no son las formas aprobadas para aparecer en esa ubicación. | `[]` |
| `selectionMode` | `string` | 101/101 | Indica interpretación específica o selección representativa de especies/cultivos. | `"optional_scientific_reference"` |
| `interpretationStatus` | `string` | 101/101 | Estado de interpretación de la etiqueta original, independiente del cotejo del nombre científico. | `"not_required_for_gameplay_identity_or_resource_access"` |
| `inheritResourceBindings` | `boolean` | 101/101 | False: los taxones/formas no heredan automáticamente productos del candidato. | `false` |

### `$.speciesCandidates[].sourceVariants[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 51/51 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"animal_eurasian_moose"` |
| `name` | `object` | 51/51 | Nombre visible mediante claves de idioma. | `—` |
| `sourceLabel` | `string` | 51/51 | Etiqueta original en español para trazabilidad, no texto localizado de interfaz. | `"Alce euroasiático"` |
| `biomeVariantIds` | `array<string>` | 51/51 | Referencias a variantes regionales que enumeran este candidato. | `["temperate_forest_boreal"]` |

### `$.speciesCandidates[].sourceVariants[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 51/51 | Texto visible en inglés. | `"Eurasian Moose"` |
| `es` | `string` | 51/51 | Texto visible en español. | `"Alce euroasiático"` |

### `$.entityAliases[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `previousId` | `string` | 51/51 | ID anterior conservado para compatibilidad y procedencia; no reutilizar. | `"animal_corsac_fox"` |
| `entityId` | `string` | 51/51 | ID de entidad del juego; puede representar una categoría general y no una especie científica. | `"ANM#000169"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.3.0",
  "contentVersion": "0.5.0",
  "status": "design_guide_requires_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "null means unresolved; it is not zero or unrestricted.",
    "classificationPolicy": "Use general gameplay entities when specific species add no meaningful resource or behavior distinction. Scientific taxonomy is optional background, not an unlock or entity identity requirement. Preserve distinctions for crops, wild/domestic forms and other actual gameplay differences."
  },
  "kind": "animal_catalog_design_guide",
  "speciesCandidates": [
    {
      "id": "ANM#000170",
      "kind": "animal",
      "name": {
        "en": "Moose",
        "es": "Alces"
      },
      "taxonomy": {
        "scientificName": null,
        "nameEvidence": "gameplay_category_not_scientific_species",
        "resolutionStatus": "scientific_species_not_required_for_gameplay_category",
        "verified": false
      },
      "definitionStatus": "general_gameplay_category_design_guide",
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
        "habitatRestrictionsStatus": "General gameplay category. Preserve regional source occurrences; do not spawn every historical form or infer worldwide presence."
      },
      "propagation": {
        "methods": null,
        "materialResourceIds": null
      },
      "domestication": {
        "eligibility": "requires_gameplay_domestication_design",
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
          "ANM#000001",
          "ANM#000002"
        ],
        "formIds": [],
        "selectionMode": "optional_scientific_reference",
        "interpretationStatus": "not_required_for_gameplay_identity_or_resource_access",
        "inheritResourceBindings": false
      },
      "tag": "moose",
      "sourceVariants": [
        {
          "id": "animal_eurasian_moose",
          "name": {
            "en": "Eurasian Moose",
            "es": "Alce euroasiático"
          },
          "sourceLabel": "Alce euroasiático",
          "biomeVariantIds": [
            "temperate_forest_boreal"
          ]
        }
      ]
    }
  ],
  "biologicalCatalogFile": "animals.biological.catalog.json",
  "entityAliases": [
    {
      "previousId": "animal_corsac_fox",
      "entityId": "ANM#000169"
    }
  ]
}
```
