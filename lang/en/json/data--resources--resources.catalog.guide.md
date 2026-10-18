# `data/resources/resources.catalog.guide.json`

[Source JSON](../../../data/resources/resources.catalog.guide.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.1.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.4.0"` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"resource_catalog_design_guide"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"prototype_requires_species_action_and_balance_review"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `identityPolicy` | `string` | 1/1 | Localized text must not be used as identity or dependency. | `"New resource IDs use RES#000001 format and are permanent; tags are English snake_case. Existing species/technol…` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `resources` | `array<object>` | 1/1 | Resource records at the root, or the relative resource-catalog path inside catalogFiles. | `—` |
| `sourceBindings` | `array<object>` | 1/1 | Possible source-to-resource links; never automatic production or a complete acquisition recipe. | `—` |
| `sourceTagMappings` | `array<object>` | 1/1 | Explicit mappings of existing animal-product tags; services and ambiguous anatomy remain separate. | `—` |
| `processingLinks` | `array<object>` | 1/1 | Proposed transformation endpoints; additional inputs and actual recipes are still unresolved. | `—` |
| `unresolvedSources` | `array<object>` | 1/1 | Resources whose exact acquisition source or subsystem remains undefined. | `—` |
| `reviewIssues` | `array<object>` | 1/1 | Recorded source discrepancies and unresolved design questions. | `—` |
| `summary` | `object` | 1/1 | Counts used to check catalog completeness. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved, not zero, none or unrestricted."` |
| `sourceBindings` | `string` | 1/1 | Possible source-to-resource links; never automatic production or a complete acquisition recipe. | `"Links are possible design outputs, not guaranteed products or completed taxonomy. They do not consume inventory…` |
| `processingLinks` | `string` | 1/1 | Proposed transformation endpoints; additional inputs and actual recipes are still unresolved. | `"Endpoint guides only; additional inputs, recipes, facilities, time, fuel and losses remain unresolved. No execu…` |
| `services` | `string` | 1/1 | Policy excluding work, draft and transport services from stored inventory. | `"Draft, transport and work are services, not storable inventory resources."` |
| `provenance` | `string` | 1/1 | Keep species, original material, viability and quality in future inventory lots. | `"Resource IDs may aggregate compatible material categories; future GameState inventory lots must preserve source…` |

### `$.resources[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 106/106 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"RES#000001"` |
| `tag` | `string` | 106/106 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"wood"` |
| `name` | `object` | 106/106 | Player-visible label using language keys. | `—` |
| `description` | `object` | 106/106 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `category` | `string` | 106/106 | English resource category used for organizing the catalog. | `"plant_material"` |
| `stage` | `string` | 106/106 | Material stage: raw, intermediate, processed or refined; does not encode a numeric technology level. | `"raw"` |
| `tags` | `array<string>` | 106/106 | English classification tags; compatibility and substitution still require explicit action rules. | `["wood", "fuel_candidate"]` |
| `inventory` | `object` | 106/106 | Inventory eligibility and unresolved storage metadata, not current stock amounts. | `—` |
| `definitionStatus` | `string` | 106/106 | Readiness of this record; source candidates are not runtime definitions. | `"design_guide_requires_review"` |

### `$.resources[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 106/106 | English visible text. | `"Wood"` |
| `es` | `string` | 106/106 | Spanish visible text. | `"Madera"` |

### `$.resources[].description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 106/106 | English visible text. | `"Wood: a material definition for inventory and future production rules; amounts and processing requirements rema…` |
| `es` | `string` | 106/106 | Spanish visible text. | `"Madera: definición de material para inventario y futuras reglas de producción; cantidades y requisitos de proce…` |

### `$.resources[].inventory`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `storable` | `boolean` | 106/106 | True identifies a material eligible for inventory; services are excluded. | `true` |
| `quantityUnit` | `null` | 106/106 | Inventory measurement unit; null means the unit is not yet chosen. | `null` |
| `perishable` | `null` | 106/106 | Whether deterioration applies; null means unresolved, not nonperishable. | `null` |
| `storageRules` | `null` | 106/106 | Storage requirements and deterioration rules, still undefined. | `null` |

### `$.sourceBindings[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceCollection` | `string` | 594/594 | Symbolic collection key resolving to plants, animals, crops or geology; not a resource ID. | `"agriculturalCropCandidates"` |
| `sourceId` | `string` | 594/594 | Existing source candidate ID, preserved without migrating its identity. | `"wheat"` |
| `resourceId` | `string` | 594/594 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000007"` |
| `acquisitionTag` | `string` | 594/594 | Descriptive acquisition guide tag; not an implemented action or recipe ID. | `"crop_harvesting"` |
| `reviewStatus` | `string` | 594/594 | Review still required before a source output is authorized. | `"proposed_requires_species_and_action_review"` |
| `quantityPerAction` | `null` | 594/594 | Output per action, still unresolved; not zero or guaranteed yield. | `null` |
| `runtimeEnabled` | `boolean` | 594/594 | Whether this occurrence may be used by generation; currently false. | `false` |
| `requiresProcessing` | `boolean` | 594/594 | True means this source relation includes further processing; it is not a direct harvesting output. | `false` |
| `processingTag` | `null \| string` | 498/594 | Optional process guide required for a processed output; null for raw materials even when handling is needed. | `"fish_oil_extraction"` |

### `$.sourceTagMappings[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceTag` | `string` | 21/21 | Original animal-product or service tag retained for traceability. | `"animal_fat"` |
| `targetKind` | `string` | 21/21 | Whether the original tag represents a resource, service or unresolved anatomical alternative. | `"resource"` |
| `resourceIds` | `array<string>` | 21/21 | Explicit linked resource IDs; empty for services or unresolved alternatives. | `["RES#000032"]` |
| `resolutionStatus` | `string` | 21/21 | Task still required to resolve a candidate or regional restriction. | `"linked_to_material_acquisition_reference"` |
| `note` | `string` | 21/21 | Developer clarification; not localized UI text. | `"Availability and acquisition methods are defined per animal. No quantity, automatic yield or food-use permissio…` |

### `$.processingLinks[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `processTag` | `string` | 28/28 | Unique technical name of a proposed transformation guide; not a recipe implementation. | `"wood_sawing"` |
| `inputResourceIds` | `array<string>` | 28/28 | Resource endpoints entering the guide; this is not a complete list of required recipe inputs. | `["RES#000001"]` |
| `outputResourceIds` | `array<string>` | 28/28 | Resource endpoints produced after the still-undefined process, not automatic outputs. | `["RES#000088"]` |
| `description` | `object` | 28/28 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `requiredTechnologyIds` | `null` | 28/28 | Technology references needed for this output; null means unresolved, not none. | `null` |
| `inputQuantities` | `null` | 28/28 | Input amounts still undefined; stoichiometry and recipe balance are not supplied. | `null` |
| `outputQuantities` | `null` | 28/28 | Output amounts and recovery still undefined. | `null` |
| `facilities` | `null` | 28/28 | Required facilities and equipment, still undefined. | `null` |
| `byproducts` | `null` | 28/28 | Secondary outputs, residues and losses, still undefined. | `null` |
| `recipeId` | `null` | 28/28 | Future recipe reference; null means this guide is not an executable recipe. | `null` |
| `runtimeEnabled` | `boolean` | 28/28 | Whether this occurrence may be used by generation; currently false. | `false` |
| `inputProvenancePolicy` | `string` | 4/28 | Source/anatomy constraint on process input; generic resource IDs alone do not authorize a recipe. | `"ivory_bearing_tusks_only"` |

### `$.processingLinks[].description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 28/28 | English visible text. | `"Wood can be prepared into planks; tools, losses and workflow remain undefined."` |
| `es` | `string` | 28/28 | Spanish visible text. | `"La madera puede prepararse como tablas; herramientas, pérdidas y proceso pendientes."` |

### `$.unresolvedSources[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 3/3 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000003"` |
| `reason` | `string` | 3/3 | Explanation of the runtime restriction. | `"World water access and collection actions are not yet defined as source entities."` |

### `$.reviewIssues[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 4/4 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"inventory_compatibility"` |
| `resolution` | `string` | 4/4 | Documented interpretation or next review action. | `"A generic grain or wood resource does not erase botanical identity, seed viability, preservation state or quali…` |

### `$.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceCount` | `integer` | 1/1 | Number of resource definitions. | `106` |
| `sourceBindingCount` | `integer` | 1/1 | Number of possible source-to-resource relations. | `594` |
| `processingLinkCount` | `integer` | 1/1 | Number of proposed transformation guides. | `28` |
| `sourceTagMappingCount` | `integer` | 1/1 | Number of original animal tags explicitly classified or mapped. | `21` |
| `geologicalSourceCount` | `integer` | 1/1 | Number of geological candidates with material mappings. | `57` |
| `cropSourceCount` | `integer` | 1/1 | Number of agricultural candidates with proposed products. | `21` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.1.0",
  "contentVersion": "0.4.0",
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
      "resolutionStatus": "linked_to_material_acquisition_reference",
      "note": "Availability and acquisition methods are defined per animal. No quantity, automatic yield or food-use permission is implied."
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
      "id": "anatomy_and_provenance",
      "resolution": "Animal products distinguish horns/antlers and raw/processed materials. Honor animal availability constraints and input provenance policies; do not double count raw inputs and processed outputs."
    }
  ],
  "summary": {
    "resourceCount": 106,
    "sourceBindingCount": 594,
    "processingLinkCount": 28,
    "sourceTagMappingCount": 21,
    "geologicalSourceCount": 57,
    "cropSourceCount": 21
  }
}
```
