# `data/resources/resources.catalog.guide.json`

[JSON fuente](../../../data/resources/resources.catalog.guide.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"1.0.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.2.0"` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"resource_catalog_design_guide"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"prototype_requires_species_action_and_balance_review"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `identityPolicy` | `string` | 1/1 | El texto traducido no se utiliza como identidad o dependencia. | `"New resource IDs use RES#000001 format and are permanent; tags are English snake_case. Existing species/technol…` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `resources` | `array<object>` | 1/1 | Registros de recursos en la raíz, o ruta relativa al catálogo dentro de catalogFiles. | `—` |
| `sourceBindings` | `array<object>` | 1/1 | Posibles vínculos de origen a recurso; nunca producción automática ni receta completa. | `—` |
| `sourceTagMappings` | `array<object>` | 1/1 | Equivalencias explícitas de tags animales; servicios y anatomía ambigua permanecen separados. | `—` |
| `processingLinks` | `array<object>` | 1/1 | Extremos propuestos de transformación; insumos adicionales y recetas reales pendientes. | `—` |
| `unresolvedSources` | `array<object>` | 1/1 | Recursos cuyo origen exacto o sistema de obtención está pendiente. | `—` |
| `reviewIssues` | `array<object>` | 1/1 | Contradicciones de la fuente y preguntas de diseño pendientes. | `—` |
| `summary` | `object` | 1/1 | Conteos para comprobar integridad de los catálogos. | `—` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved, not zero, none or unrestricted."` |
| `sourceBindings` | `string` | 1/1 | Posibles vínculos de origen a recurso; nunca producción automática ni receta completa. | `"Links are possible design outputs, not guaranteed products or completed taxonomy. They do not consume inventory…` |
| `processingLinks` | `string` | 1/1 | Extremos propuestos de transformación; insumos adicionales y recetas reales pendientes. | `"Endpoint guides only; additional inputs, recipes, facilities, time, fuel and losses remain unresolved. No execu…` |
| `services` | `string` | 1/1 | Política que excluye trabajo, tracción y transporte del inventario. | `"Draft, transport and work are services, not storable inventory resources."` |
| `provenance` | `string` | 1/1 | Conservar especie, material original, viabilidad y calidad en futuros lotes. | `"Resource IDs may aggregate compatible material categories; future GameState inventory lots must preserve source…` |

### `$.resources[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 104/104 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"RES#000001"` |
| `tag` | `string` | 104/104 | Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales. | `"wood"` |
| `name` | `object` | 104/104 | Nombre visible mediante claves de idioma. | `—` |
| `description` | `object` | 104/104 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `—` |
| `category` | `string` | 104/104 | Categoría del recurso en inglés para organizar el catálogo. | `"plant_material"` |
| `stage` | `string` | 104/104 | Estado del material: raw, intermediate, processed o refined; no es nivel tecnológico numérico. | `"raw"` |
| `tags` | `array<string>` | 104/104 | Tags de clasificación en inglés; compatibilidad y sustitución requieren reglas explícitas. | `["wood", "fuel_candidate"]` |
| `inventory` | `object` | 104/104 | Elegibilidad para inventario y almacenamiento pendiente, no existencias actuales. | `—` |
| `definitionStatus` | `string` | 104/104 | Madurez del registro; los candidatos no son definiciones ejecutables. | `"design_guide_requires_review"` |

### `$.resources[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 104/104 | Texto visible en inglés. | `"Wood"` |
| `es` | `string` | 104/104 | Texto visible en español. | `"Madera"` |

### `$.resources[].description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 104/104 | Texto visible en inglés. | `"Wood: a material definition for inventory and future production rules; amounts and processing requirements rema…` |
| `es` | `string` | 104/104 | Texto visible en español. | `"Madera: definición de material para inventario y futuras reglas de producción; cantidades y requisitos de proce…` |

### `$.resources[].inventory`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `storable` | `boolean` | 104/104 | True identifica un material apto para inventario; excluye servicios. | `true` |
| `quantityUnit` | `null` | 104/104 | Unidad de medida de inventario; null indica unidad pendiente. | `null` |
| `perishable` | `null` | 104/104 | Indica deterioro; null significa pendiente, no imperecedero. | `null` |
| `storageRules` | `null` | 104/104 | Requisitos de almacenamiento y deterioro pendientes. | `null` |

### `$.sourceBindings[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `sourceCollection` | `string` | 298/298 | Clave de colección para plantas, animales, cultivos o geología; no es ID de recurso. | `"agriculturalCropCandidates"` |
| `sourceId` | `string` | 298/298 | ID actual del candidato de origen, conservado sin migración. | `"wheat"` |
| `resourceId` | `string` | 298/298 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000007"` |
| `acquisitionTag` | `string` | 298/298 | Tag descriptivo de obtención; no es ID de acción o receta implementada. | `"crop_harvesting"` |
| `reviewStatus` | `string` | 298/298 | Revisión pendiente antes de autorizar un producto del origen. | `"proposed_requires_species_and_action_review"` |
| `quantityPerAction` | `null` | 298/298 | Cantidad por acción pendiente; no significa cero ni rendimiento garantizado. | `null` |
| `runtimeEnabled` | `boolean` | 298/298 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |
| `requiresProcessing` | `boolean` | 298/298 | True indica procesamiento posterior en la relación; no es producto directo de recolección. | `false` |

### `$.sourceTagMappings[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `sourceTag` | `string` | 23/23 | Tag original de producto animal o servicio conservado para trazabilidad. | `"animal_fat"` |
| `targetKind` | `string` | 23/23 | Indica si el tag representa recurso, servicio o alternativa anatómica pendiente. | `"resource"` |
| `resourceIds` | `array<string>` | 23/23 | IDs de recursos vinculados; vacío para servicios o alternativas pendientes. | `["RES#000032"]` |
| `resolutionStatus` | `string` | 23/23 | Tarea pendiente para resolver el candidato o restricción regional. | `"tag_linked_species_and_use_review_pending"` |
| `note` | `string` | 23/23 | Aclaración técnica; no es texto traducido de interfaz. | `"A linked source possibility is not a verified yield or permission to harvest."` |

### `$.processingLinks[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `processTag` | `string` | 25/25 | Nombre técnico único de guía de transformación; no es receta implementada. | `"wood_sawing"` |
| `inputResourceIds` | `array<string>` | 25/25 | Recursos de entrada de la guía; no son una lista completa de insumos de receta. | `["RES#000001"]` |
| `outputResourceIds` | `array<string>` | 25/25 | Recursos finales del proceso pendiente, no productos automáticos. | `["RES#000088"]` |
| `description` | `object` | 25/25 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `—` |
| `requiredTechnologyIds` | `null` | 25/25 | Referencias tecnológicas del producto; null significa pendiente, no ningún requisito. | `null` |
| `inputQuantities` | `null` | 25/25 | Cantidades de entrada pendientes; no define estequiometría ni balance de receta. | `null` |
| `outputQuantities` | `null` | 25/25 | Cantidades de salida y recuperación pendientes. | `null` |
| `facilities` | `null` | 25/25 | Instalaciones y equipo requeridos pendientes. | `null` |
| `byproducts` | `null` | 25/25 | Productos secundarios, residuos y pérdidas pendientes. | `null` |
| `recipeId` | `null` | 25/25 | Referencia futura de receta; null indica que la guía no es receta ejecutable. | `null` |
| `runtimeEnabled` | `boolean` | 25/25 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |

### `$.processingLinks[].description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 25/25 | Texto visible en inglés. | `"Wood can be prepared into planks; tools, losses and workflow remain undefined."` |
| `es` | `string` | 25/25 | Texto visible en español. | `"La madera puede prepararse como tablas; herramientas, pérdidas y proceso pendientes."` |

### `$.unresolvedSources[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 3/3 | Referencia a un recurso, distinta del ID de especie o yacimiento. | `"RES#000003"` |
| `reason` | `string` | 3/3 | Explicación de la restricción de ejecución. | `"World water access and collection actions are not yet defined as source entities."` |

### `$.reviewIssues[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 4/4 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"inventory_compatibility"` |
| `resolution` | `string` | 4/4 | Interpretación documentada o siguiente acción de revisión. | `"A generic grain or wood resource does not erase botanical identity, seed viability, preservation state or quali…` |

### `$.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceCount` | `integer` | 1/1 | Cantidad de definiciones de recursos. | `104` |
| `sourceBindingCount` | `integer` | 1/1 | Cantidad de relaciones posibles de origen a recurso. | `298` |
| `processingLinkCount` | `integer` | 1/1 | Cantidad de guías propuestas de transformación. | `25` |
| `sourceTagMappingCount` | `integer` | 1/1 | Cantidad de tags animales originales clasificados o vinculados. | `23` |
| `geologicalSourceCount` | `integer` | 1/1 | Cantidad de candidatos geológicos vinculados con materiales. | `57` |
| `cropSourceCount` | `integer` | 1/1 | Cantidad de candidatos agrícolas con productos propuestos. | `21` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.0.0",
  "contentVersion": "0.2.0",
  "kind": "resource_catalog_design_guide",
  "status": "prototype_requires_species_action_and_balance_review",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "identityPolicy": "New resource IDs use RES#000001 format and are permanent; tags are English snake_case. Existing species/technology IDs are not migrated. Never sort/reallocate these IDs.",
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "null means unresolved, not zero, none or unrestricted.",
    "sourceBindings": "Links are possible design outputs, not guaranteed products or completed taxonomy. They do not consume inventory or create items.",
    "processingLinks": "Endpoint guides only; additional inputs, recipes, facilities, time, fuel and losses remain unresolved. No executable recipes are provided.",
    "services": "Draft, transport and work are services, not storable inventory resources.",
    "provenance": "Resource IDs may aggregate compatible material categories; future GameState inventory lots must preserve source species/material, viability and quality before substitution."
  },
  "resources": [
    {
      "id": "RES#000001",
      "tag": "wood",
      "name": {
        "en": "Wood",
        "es": "Madera"
      },
      "description": {
        "en": "Wood: a material definition for inventory and future production rules; amounts and processing requirements remain provisional.",
        "es": "Madera: definición de material para inventario y futuras reglas de producción; cantidades y requisitos de procesamiento pendientes."
      },
      "category": "plant_material",
      "stage": "raw",
      "tags": [
        "wood",
        "fuel_candidate"
      ],
      "inventory": {
        "storable": true,
        "quantityUnit": null,
        "perishable": null,
        "storageRules": null
      },
      "definitionStatus": "design_guide_requires_review"
    }
  ],
  "sourceBindings": [
    {
      "sourceCollection": "agriculturalCropCandidates",
      "sourceId": "wheat",
      "resourceId": "RES#000007",
      "acquisitionTag": "crop_harvesting",
      "reviewStatus": "proposed_requires_species_and_action_review",
      "quantityPerAction": null,
      "runtimeEnabled": false,
      "requiresProcessing": false
    }
  ],
  "sourceTagMappings": [
    {
      "sourceTag": "animal_fat",
      "targetKind": "resource",
      "resourceIds": [
        "RES#000032"
      ],
      "resolutionStatus": "tag_linked_species_and_use_review_pending",
      "note": "A linked source possibility is not a verified yield or permission to harvest."
    }
  ],
  "processingLinks": [
    {
      "processTag": "wood_sawing",
      "inputResourceIds": [
        "RES#000001"
      ],
      "outputResourceIds": [
        "RES#000088"
      ],
      "description": {
        "en": "Wood can be prepared into planks; tools, losses and workflow remain undefined.",
        "es": "La madera puede prepararse como tablas; herramientas, pérdidas y proceso pendientes."
      },
      "requiredTechnologyIds": null,
      "inputQuantities": null,
      "outputQuantities": null,
      "facilities": null,
      "byproducts": null,
      "recipeId": null,
      "runtimeEnabled": false
    }
  ],
  "unresolvedSources": [
    {
      "resourceId": "RES#000003",
      "reason": "World water access and collection actions are not yet defined as source entities."
    }
  ],
  "reviewIssues": [
    {
      "id": "inventory_compatibility",
      "resolution": "A generic grain or wood resource does not erase botanical identity, seed viability, preservation state or quality. Model these in per-game inventory lots."
    },
    {
      "id": "food_safety",
      "resolution": "Raw crop resources are not automatically edible; preparation, preservation and nutritional rules remain undefined."
    },
    {
      "id": "future_extraction",
      "resolution": "Nickel materials, manganese materials and seabed nodules do not unlock historical extraction; world scope and technology restrictions still apply."
    },
    {
      "id": "ambiguous_animal_products",
      "resolution": "antlers_or_horns is deliberately unresolved; service tags do not become inventory items."
    }
  ],
  "summary": {
    "resourceCount": 104,
    "sourceBindingCount": 298,
    "processingLinkCount": 25,
    "sourceTagMappingCount": 23,
    "geologicalSourceCount": 57,
    "cropSourceCount": 21
  }
}
```
