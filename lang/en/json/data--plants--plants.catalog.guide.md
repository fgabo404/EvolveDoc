# `data/plants/plants.catalog.guide.json`

[Source JSON](../../../data/plants/plants.catalog.guide.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.3.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.4.0"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"plant_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Flat gameplay entity candidates; general categories are valid and need not resolve to scientific species. | `—` |
| `agriculturalCropCandidates` | `array<object>` | 1/1 | Crop groups linked to selected taxa/forms; ancestry coverage and production rules remain partial. | `—` |
| `biologicalCatalogFile` | `string` | 1/1 | Sibling biological catalog file; legacy candidate IDs remain unchanged. | `"plants.biological.catalog.json"` |
| `entityAliases` | `array<object>` | 1/1 | Retired regional/specific IDs mapped to one canonical gameplay entity. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it is not zero or unrestricted."` |
| `classificationPolicy` | `string` | 1/1 | Use general gameplay entities unless a distinction changes resources or behavior; science is optional. | `"Use general gameplay entities when specific species add no meaningful resource or behavior distinction. Scienti…` |

### `$.speciesCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 109/109 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"PLT#000191"` |
| `kind` | `string` | 109/109 | Discriminator identifying this document or candidate category. | `"plant"` |
| `name` | `object` | 109/109 | Player-visible label using language keys. | `—` |
| `taxonomy` | `object` | 109/109 | Scientific identity, evidence and review information. | `—` |
| `definitionStatus` | `string` | 109/109 | Readiness of this record; source candidates are not runtime definitions. | `"general_gameplay_category_design_guide"` |
| `nativeRegionIds` | `array<?>` | 109/109 | References to native regions; empty means unresolved, not worldwide distribution. | `[]` |
| `biomeVariantIds` | `array<string>` | 109/109 | References to regional variants listing this candidate. | `["tundra_eurasian", "temperate_forest_boreal"]` |
| `ecology` | `object` | 109/109 | Environmental requirements; quantitative values remain unresolved. | `—` |
| `propagation` | `object` | 109/109 | Reproduction/propagation methods and required materials, still under design. | `—` |
| `domestication` | `object` | 109/109 | Eligibility, ancestor/form relationships and selection criteria. | `—` |
| `potentialProducts` | `array<object> \| null` | 109/109 | Potential source uses; not confirmed outputs, quantities or unlocks. | `—` |
| `potentialUseMethods` | `array<?>` | 109/109 | Potential source use methods, not authorized gameplay actions. | `[]` |
| `cultivationResearch` | `object` | 109/109 | Illustrative link to per-species research; null means no binding specified. | `—` |
| `sourceLabel` | `string` | 109/109 | Exact Spanish source label for provenance, not a localized UI field. | `"Abedul enano"` |
| `initialPresencePolicy` | `string` | 109/109 | Constraints to resolve before initial spawning. | `"resolve_native_region_and_habitat_before_spawning"` |
| `taxonResolution` | `object` | 109/109 | Optional scientific background links; not required for gameplay identity, spawning or resource access. | `—` |
| `tag` | `string` | 15/109 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"birches"` |
| `sourceVariants` | `array<object>` | 15/109 | Original labels and regional source references merged into this single gameplay entity. | `—` |

### `$.speciesCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 109/109 | English visible text. | `"Birches"` |
| `es` | `string` | 109/109 | Spanish visible text. | `"Abedules"` |

### `$.speciesCandidates[].taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 109/109 | Scientific name in the source or accepted provider record; null in a legacy source means unresolved there. | `"Nothofagus dombeyi"` |
| `nameEvidence` | `string` | 109/109 | Evidence supporting the recorded scientific name or its absence. | `"gameplay_category_not_scientific_species"` |
| `resolutionStatus` | `string` | 109/109 | Task still required to resolve a candidate or regional restriction. | `"scientific_species_not_required_for_gameplay_category"` |
| `verified` | `boolean` | 109/109 | Whether scientific verification has been performed; current candidates are not verified. | `false` |

### `$.speciesCandidates[].ecology`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 109/109 | Temperature bounds in degrees Celsius; null has no finalized inner structure. | `null` |
| `moistureRange` | `null` | 109/109 | Moisture bounds; units and structure remain unresolved. | `null` |
| `elevationRangeM` | `null` | 109/109 | Elevation bounds in meters; values and structure remain unresolved. | `null` |
| `waterRequirements` | `null` | 109/109 | Species water requirements; unresolved, not absence of a requirement. | `null` |
| `soilRequirements` | `null` | 109/109 | Species soil constraints, awaiting a structured definition. | `null` |
| `habitatRestrictionsStatus` | `string` | 109/109 | Developer explanation of unresolved habitat restrictions. | `"General gameplay category. Preserve regional source occurrences; do not spawn every historical form or infer wo…` |

### `$.speciesCandidates[].propagation`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 109/109 | Supported propagation methods; null is unresolved. | `null` |
| `materialResourceIds` | `null` | 109/109 | References to propagation resources; null means unresolved links. | `null` |

### `$.speciesCandidates[].domestication`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 109/109 | Whether and under what review a candidate may use this mechanism. | `"requires_gameplay_domestication_design"` |
| `wildAncestorId` | `null` | 109/109 | Reference to the selected wild ancestor, not automatically inferred. | `null` |
| `domesticatedFormId` | `null` | 109/109 | Reference to a domesticated form; does not grant instant domestication. | `null` |
| `criteria` | `null` | 109/109 | Domestication criteria, not yet modeled. | `null` |

### `$.speciesCandidates[].cultivationResearch`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 109/109 | Reference to a technology definition or declared external import. | `"species_cultivation"` |
| `speciesId` | `string` | 109/109 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"plant_dwarf_birch"` |
| `eligibility` | `string` | 109/109 | Whether and under what review a candidate may use this mechanism. | `"Only instantiate after the exact species is confirmed cultivable; flora presence alone does not imply agricultu…` |

### `$.speciesCandidates[].taxonResolution`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 109/109 | References to the selected taxon definitions; group selections are non-exhaustive. | `["PLT#000025", "PLT#000026", "PLT#000027"]` |
| `formIds` | `array<string>` | 109/109 | Related biological reference forms; not the forms approved to spawn at this source occurrence. | `[]` |
| `selectionMode` | `string` | 109/109 | Whether a label is interpreted specifically or split into representative species/crop taxa. | `"optional_scientific_reference"` |
| `interpretationStatus` | `string` | 109/109 | Review state of the original label interpretation, independent of scientific name matching. | `"not_required_for_gameplay_identity_or_resource_access"` |
| `inheritResourceBindings` | `boolean` | 109/109 | False: selected taxa/forms do not inherit candidate resource outputs automatically. | `false` |

### `$.speciesCandidates[].sourceVariants[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 35/35 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"plant_dwarf_birch"` |
| `name` | `object` | 35/35 | Player-visible label using language keys. | `—` |
| `sourceLabel` | `string` | 35/35 | Exact Spanish source label for provenance, not a localized UI field. | `"Abedul enano"` |
| `biomeVariantIds` | `array<string>` | 35/35 | References to regional variants listing this candidate. | `["tundra_eurasian"]` |

### `$.speciesCandidates[].sourceVariants[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 35/35 | English visible text. | `"Dwarf Birch"` |
| `es` | `string` | 35/35 | Spanish visible text. | `"Abedul enano"` |

### `$.speciesCandidates[].potentialProducts[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 15/15 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000021"` |
| `status` | `string` | 15/15 | Maturity, review state or current example research status; read the containing object. | `"proposed_requires_species_and_action_review"` |
| `requiredTechnologyIds` | `null` | 15/15 | Technology references needed for this output; null means unresolved, not none. | `null` |
| `yield` | `null` | 15/15 | Output yield; units, formula and amount remain unresolved. | `null` |

### `$.agriculturalCropCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 21/21 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"wheat"` |
| `name` | `object` | 21/21 | Player-visible label using language keys. | `—` |
| `cropUseTag` | `string` | 21/21 | Gameplay crop-use group, not a botanical species. | `"cereal"` |
| `sourceOriginHint` | `null \| string` | 21/21 | Source geographic origin hint; not a verified native-range rule. | `"Southwest Asia"` |
| `scientificName` | `null` | 21/21 | Scientific name in the source or accepted provider record; null in a legacy source means unresolved there. | `null` |
| `resolutionStatus` | `string` | 21/21 | Task still required to resolve a candidate or regional restriction. | `"select_exact_species_and_wild_ancestor"` |
| `wildAncestorCandidateIds` | `array<?>` | 21/21 | Possible ancestor links pending scientific review. | `[]` |
| `cultivationResearch` | `object` | 21/21 | Illustrative link to per-species research; null means no binding specified. | `—` |
| `products` | `array<object>` | 21/21 | Crop outputs awaiting resource definitions and recipes. | `—` |
| `ecologicalConstraints` | `null` | 21/21 | Crop environmental rules awaiting formalization. | `null` |
| `sourceSection` | `string` | 21/21 | Source section from which this entry was extracted. | `"5. Initial agricultural and plant catalog"` |
| `taxonResolution` | `object` | 21/21 | Optional scientific background links; not required for gameplay identity, spawning or resource access. | `—` |

### `$.agriculturalCropCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 21/21 | English visible text. | `"Wheat"` |
| `es` | `string` | 21/21 | Spanish visible text. | `"Trigo"` |

### `$.agriculturalCropCandidates[].cultivationResearch`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 21/21 | Reference to a technology definition or declared external import. | `"species_cultivation"` |
| `speciesId` | `string` | 21/21 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"wheat"` |

### `$.agriculturalCropCandidates[].products[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceId` | `string` | 24/24 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000007"` |
| `status` | `string` | 24/24 | Maturity, review state or current example research status; read the containing object. | `"proposed_requires_species_and_action_review"` |
| `requiredTechnologyIds` | `null` | 24/24 | Technology references needed for this output; null means unresolved, not none. | `null` |
| `yield` | `null` | 24/24 | Output yield; units, formula and amount remain unresolved. | `null` |

### `$.agriculturalCropCandidates[].taxonResolution`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 21/21 | References to the selected taxon definitions; group selections are non-exhaustive. | `["PLT#000173", "PLT#000175", "PLT#000176"]` |
| `formIds` | `array<string>` | 21/21 | Related biological reference forms; not the forms approved to spawn at this source occurrence. | `["FRM#000001", "FRM#000002", "FRM#000003"]` |
| `selectionMode` | `string` | 21/21 | Whether a label is interpreted specifically or split into representative species/crop taxa. | `"explicit_crop_taxa_selection"` |
| `interpretationStatus` | `string` | 21/21 | Review state of the original label interpretation, independent of scientific name matching. | `"crop_group_resolved_to_selected_taxa_ancestry_review_not_complete"` |
| `inheritResourceBindings` | `boolean` | 21/21 | False: selected taxa/forms do not inherit candidate resource outputs automatically. | `false` |

### `$.entityAliases[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `previousId` | `string` | 35/35 | Retired source ID retained for compatibility and provenance; do not reuse. | `"plant_dwarf_birch"` |
| `entityId` | `string` | 35/35 | Canonical gameplay entity ID; may represent a general category rather than a scientific species. | `"PLT#000191"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.3.0",
  "contentVersion": "0.4.0",
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
  "kind": "plant_catalog_design_guide",
  "speciesCandidates": [
    {
      "id": "PLT#000191",
      "kind": "plant",
      "name": {
        "en": "Birches",
        "es": "Abedules"
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
        "tundra_eurasian",
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
          "PLT#000025",
          "PLT#000026",
          "PLT#000027"
        ],
        "formIds": [],
        "selectionMode": "optional_scientific_reference",
        "interpretationStatus": "not_required_for_gameplay_identity_or_resource_access",
        "inheritResourceBindings": false
      },
      "tag": "birches",
      "sourceVariants": [
        {
          "id": "plant_dwarf_birch",
          "name": {
            "en": "Dwarf Birch",
            "es": "Abedul enano"
          },
          "sourceLabel": "Abedul enano",
          "biomeVariantIds": [
            "tundra_eurasian"
          ]
        }
      ]
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
  "biologicalCatalogFile": "plants.biological.catalog.json",
  "entityAliases": [
    {
      "previousId": "plant_dwarf_birch",
      "entityId": "PLT#000191"
    }
  ]
}
```
