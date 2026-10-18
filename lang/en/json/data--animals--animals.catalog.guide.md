# `data/animals/animals.catalog.guide.json`

[Source JSON](../../../data/animals/animals.catalog.guide.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.4.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.6.0"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"animal_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Flat gameplay entity candidates; general categories are valid and need not resolve to scientific species. | `—` |
| `biologicalCatalogFile` | `string` | 1/1 | Sibling biological catalog file; legacy candidate IDs remain unchanged. | `"animals.biological.catalog.json"` |
| `entityAliases` | `array<object>` | 1/1 | Retired regional/specific IDs mapped to one canonical gameplay entity. | `—` |
| `productEvidenceSources` | `array<object>` | 1/1 | Primary reference bibliography for animal anatomy, material uses and acquisition design. | `—` |
| `acquisitionMethods` | `array<object>` | 1/1 | Flat human-readable material acquisition definitions; not implemented engine handlers or UI actions. | `—` |
| `serviceUseCandidates` | `array<object>` | 1/1 | Animal work/transport candidates, kept separate from inventory materials and not yet approved as trained services. | `—` |
| `productCoverage` | `object` | 1/1 | Counts for current animal material/method reference coverage. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it is not zero or unrestricted."` |
| `classificationPolicy` | `string` | 1/1 | Use general gameplay entities unless a distinction changes resources or behavior; science is optional. | `"Use general gameplay entities when specific species add no meaningful resource or behavior distinction. Scienti…` |
| `animalProductPolicy` | `string` | 1/1 | Scope and interpretation of animal materials, live collection and processed derivatives. | `"Materials reflect useful biological potential, not guaranteed equal outputs or universal food suitability. Broa…` |

### `$.speciesCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 101/101 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"ANM#000170"` |
| `kind` | `string` | 101/101 | Discriminator identifying this document or candidate category. | `"animal"` |
| `name` | `object` | 101/101 | Player-visible label using language keys. | `—` |
| `taxonomy` | `object` | 101/101 | Scientific identity, evidence and review information. | `—` |
| `definitionStatus` | `string` | 101/101 | Readiness of this record; source candidates are not runtime definitions. | `"general_gameplay_category_design_guide"` |
| `nativeRegionIds` | `array<?>` | 101/101 | References to native regions; empty means unresolved, not worldwide distribution. | `[]` |
| `biomeVariantIds` | `array<string>` | 101/101 | References to regional variants listing this candidate. | `["temperate_forest_boreal"]` |
| `ecology` | `object` | 101/101 | Environmental requirements; quantitative values remain unresolved. | `—` |
| `propagation` | `object` | 101/101 | Reproduction/propagation methods and required materials, still under design. | `—` |
| `domestication` | `object` | 101/101 | Eligibility, ancestor/form relationships and selection criteria. | `—` |
| `potentialProducts` | `array<object>` | 101/101 | Potential source uses; not confirmed outputs, quantities or unlocks. | `—` |
| `potentialUseMethods` | `array<string>` | 101/101 | Potential source use methods, not authorized gameplay actions. | `["hunting", "butchering", "skinning"]` |
| `cultivationResearch` | `null` | 101/101 | Illustrative link to per-species research; null means no binding specified. | `null` |
| `sourceLabel` | `string` | 101/101 | Exact Spanish source label for provenance, not a localized UI field. | `"Alce euroasiático"` |
| `initialPresencePolicy` | `string` | 101/101 | Constraints to resolve before initial spawning. | `"resolve_native_region_and_habitat_before_spawning"` |
| `taxonResolution` | `object` | 101/101 | Optional scientific background links; not required for gameplay identity, spawning or resource access. | `—` |
| `tag` | `string` | 18/101 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"moose"` |
| `sourceVariants` | `array<object>` | 18/101 | Original labels and regional source references merged into this single gameplay entity. | `—` |
| `anatomicalGroup` | `string` | 101/101 | Broad functional anatomy: mammal, bird, fish, reptile or shellfish; not a scientific species subdivision. | `"mammal"` |
| `productReviewStatus` | `string` | 101/101 | Material/acquisition design coverage; operational behavior, quantities and balance remain pending. | `"material_and_acquisition_reference_completed_operational_rules_pending"` |

### `$.speciesCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 101/101 | English visible text. | `"Moose"` |
| `es` | `string` | 101/101 | Spanish visible text. | `"Alces"` |

### `$.speciesCandidates[].taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 101/101 | Scientific name in the source or accepted provider record; null in a legacy source means unresolved there. | `"Gallus gallus"` |
| `nameEvidence` | `string` | 101/101 | Evidence supporting the recorded scientific name or its absence. | `"gameplay_category_not_scientific_species"` |
| `resolutionStatus` | `string` | 101/101 | Task still required to resolve a candidate or regional restriction. | `"scientific_species_not_required_for_gameplay_category"` |
| `verified` | `boolean` | 101/101 | Whether scientific verification has been performed; current candidates are not verified. | `false` |

### `$.speciesCandidates[].ecology`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 101/101 | Temperature bounds in degrees Celsius; null has no finalized inner structure. | `null` |
| `moistureRange` | `null` | 101/101 | Moisture bounds; units and structure remain unresolved. | `null` |
| `elevationRangeM` | `null` | 101/101 | Elevation bounds in meters; values and structure remain unresolved. | `null` |
| `waterRequirements` | `null` | 101/101 | Species water requirements; unresolved, not absence of a requirement. | `null` |
| `soilRequirements` | `null` | 101/101 | Species soil constraints, awaiting a structured definition. | `null` |
| `habitatRestrictionsStatus` | `string` | 101/101 | Developer explanation of unresolved habitat restrictions. | `"General gameplay category. Preserve regional source occurrences; do not spawn every historical form or infer wo…` |

### `$.speciesCandidates[].propagation`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 101/101 | Supported propagation methods; null is unresolved. | `null` |
| `materialResourceIds` | `null` | 101/101 | References to propagation resources; null means unresolved links. | `null` |

### `$.speciesCandidates[].domestication`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 101/101 | Whether and under what review a candidate may use this mechanism. | `"requires_gameplay_domestication_design"` |
| `wildAncestorId` | `null` | 101/101 | Reference to the selected wild ancestor, not automatically inferred. | `null` |
| `domesticatedFormId` | `null` | 101/101 | Reference to a domesticated form; does not grant instant domestication. | `null` |
| `criteria` | `null` | 101/101 | Domestication criteria, not yet modeled. | `null` |

### `$.speciesCandidates[].potentialProducts[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceTag` | `string` | 498/498 | English resource-category tag; not a resolved resource ID. | `"meat"` |
| `status` | `string` | 498/498 | Maturity, review state or current example research status; read the containing object. | `"biological_potential_gameplay_design"` |
| `requiredTechnologyIds` | `null` | 498/498 | Technology references needed for this output; null means unresolved, not none. | `null` |
| `yield` | `null` | 498/498 | Output yield; units, formula and amount remain unresolved. | `null` |
| `resourceId` | `string` | 498/498 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000029"` |
| `acquisitionMethodTags` | `array<string>` | 498/498 | References to this animal catalog's material acquisition definitions. | `["butchering"]` |
| `availabilityConstraints` | `array<string>` | 498/498 | English design-condition tags; not executable condition expressions or numeric thresholds. | `[]` |
| `processingTag` | `null \| string` | 498/498 | Optional process guide required for a processed output; null for raw materials even when handling is needed. | `"fish_oil_extraction"` |
| `notes` | `object` | 498/498 | Localized explanation of material availability and source-specific limitations. | `—` |
| `evidenceSourceKeys` | `array<string>` | 498/498 | Keys into this catalog bibliography; empty means no specific lineage claim is asserted here. | `["fao_byproducts"]` |

### `$.speciesCandidates[].potentialProducts[].notes`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 498/498 | English visible text. | `"Useful biological material; availability depends on the actual source and collection method."` |
| `es` | `string` | 498/498 | Spanish visible text. | `"Material biológico aprovechable; depende de la fuente concreta y el método de obtención."` |

### `$.speciesCandidates[].taxonResolution`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `taxonIds` | `array<string>` | 101/101 | References to the selected taxon definitions; group selections are non-exhaustive. | `["ANM#000001", "ANM#000002"]` |
| `formIds` | `array<string>` | 101/101 | Related biological reference forms; not the forms approved to spawn at this source occurrence. | `[]` |
| `selectionMode` | `string` | 101/101 | Whether a label is interpreted specifically or split into representative species/crop taxa. | `"optional_scientific_reference"` |
| `interpretationStatus` | `string` | 101/101 | Review state of the original label interpretation, independent of scientific name matching. | `"not_required_for_gameplay_identity_or_resource_access"` |
| `inheritResourceBindings` | `boolean` | 101/101 | False: selected taxa/forms do not inherit candidate resource outputs automatically. | `false` |

### `$.speciesCandidates[].sourceVariants[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 51/51 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"animal_eurasian_moose"` |
| `name` | `object` | 51/51 | Player-visible label using language keys. | `—` |
| `sourceLabel` | `string` | 51/51 | Exact Spanish source label for provenance, not a localized UI field. | `"Alce euroasiático"` |
| `biomeVariantIds` | `array<string>` | 51/51 | References to regional variants listing this candidate. | `["temperate_forest_boreal"]` |

### `$.speciesCandidates[].sourceVariants[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 51/51 | English visible text. | `"Eurasian Moose"` |
| `es` | `string` | 51/51 | Spanish visible text. | `"Alce euroasiático"` |

### `$.entityAliases[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `previousId` | `string` | 51/51 | Retired source ID retained for compatibility and provenance; do not reuse. | `"animal_corsac_fox"` |
| `entityId` | `string` | 51/51 | Canonical gameplay entity ID; may represent a general category rather than a scientific species. | `"ANM#000169"` |

### `$.productEvidenceSources[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceKey` | `string` | 15/15 | Stable bibliography key local to a biological catalog, not an entity ID. | `"fao_byproducts"` |
| `title` | `string` | 15/15 | Document or schema title. | `"Animal slaughter byproduct utilization"` |
| `url` | `string` | 15/15 | Public source URL. | `"https://www.fao.org/4/x6552e/X6552E10.htm"` |
| `checkedOn` | `string` | 15/15 | Date of the consulted reference snapshot; not publication date. | `"2026-10-17"` |
| `supports` | `string` | 15/15 | Scope of the claim supported by this bibliography entry. | `"General anatomy/material utilization; not evidence that every wild category is routinely harvested."` |

### `$.acquisitionMethods[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `tag` | `string` | 17/17 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"butchering"` |
| `name` | `object` | 17/17 | Player-visible label using language keys. | `—` |
| `description` | `object` | 17/17 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `sourceOutcome` | `string` | 17/17 | Whether the method requires a dead animal, consumes it, preserves it, collects discarded material or removes an egg. | `"requires_dead_animal"` |
| `availabilityConstraints` | `array<string>` | 17/17 | English design-condition tags; not executable condition expressions or numeric thresholds. | `[]` |
| `runtimeEnabled` | `boolean` | 17/17 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.acquisitionMethods[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 17/17 | English visible text. | `"Butchering"` |
| `es` | `string` | 17/17 | Spanish visible text. | `"Despiece"` |

### `$.acquisitionMethods[].description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 17/17 | English visible text. | `"Remove flesh, bones and raw fat from a usable carcass; not an automatic reward for sighting or killing."` |
| `es` | `string` | 17/17 | Spanish visible text. | `"Extrae carne, huesos y grasa cruda de un cuerpo aprovechable; no es recompensa automática por avistar o matar."` |

### `$.serviceUseCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `entityId` | `string` | 7/7 | Canonical gameplay entity ID; may represent a general category rather than a scientific species. | `"animal_woodland_caribou"` |
| `serviceTag` | `string` | 7/7 | Technical animal service candidate identifier; not a material resource. | `"draft_service"` |
| `status` | `string` | 7/7 | Maturity, review state or current example research status; read the containing object. | `"requires_separate_training_and_husbandry_design"` |
| `availabilityConstraints` | `array<string>` | 7/7 | English design-condition tags; not executable condition expressions or numeric thresholds. | `["suitable_individual", "controlled_training", "historical_suitability_review"]` |
| `runtimeEnabled` | `boolean` | 7/7 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.productCoverage`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `animalEntityCount` | `integer` | 1/1 | Number of current animal gameplay entities covered. | `101` |
| `materialLinkCount` | `integer` | 1/1 | Number of distinct entity/material associations in the animal guide. | `498` |
| `acquisitionMethodCount` | `integer` | 1/1 | Number of material acquisition method definitions. | `17` |
| `serviceCandidateCount` | `integer` | 1/1 | Number of unapproved work/transport service candidates. | `7` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.4.0",
  "contentVersion": "0.6.0",
  "status": "design_guide_requires_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "null means unresolved; it is not zero or unrestricted.",
    "classificationPolicy": "Use general gameplay entities when specific species add no meaningful resource or behavior distinction. Scientific taxonomy is optional background, not an unlock or entity identity requirement. Preserve distinctions for crops, wild/domestic forms and other actual gameplay differences.",
    "animalProductPolicy": "Materials reflect useful biological potential, not guaranteed equal outputs or universal food suitability. Broad groups keep anatomical/sex/life-stage constraints. Raw parts require carcass processing; live/shed collection is separate. Processed oil and ivory require explicit processing. No quantities, durations or engine workflow are implemented."
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
          "status": "biological_potential_gameplay_design",
          "requiredTechnologyIds": null,
          "yield": null,
          "resourceId": "RES#000029",
          "acquisitionMethodTags": [
            "butchering"
          ],
          "availabilityConstraints": [],
          "processingTag": null,
          "notes": {
            "en": "Useful biological material; availability depends on the actual source and collection method.",
            "es": "Material biológico aprovechable; depende de la fuente concreta y el método de obtención."
          },
          "evidenceSourceKeys": [
            "fao_byproducts"
          ]
        }
      ],
      "potentialUseMethods": [
        "hunting",
        "butchering",
        "skinning",
        "recover_hard_parts",
        "collect_shed_antlers",
        "recover_tendons"
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
      ],
      "anatomicalGroup": "mammal",
      "productReviewStatus": "material_and_acquisition_reference_completed_operational_rules_pending"
    }
  ],
  "biologicalCatalogFile": "animals.biological.catalog.json",
  "entityAliases": [
    {
      "previousId": "animal_corsac_fox",
      "entityId": "ANM#000169"
    }
  ],
  "productEvidenceSources": [
    {
      "sourceKey": "fao_byproducts",
      "title": "Animal slaughter byproduct utilization",
      "url": "https://www.fao.org/4/x6552e/X6552E10.htm",
      "checkedOn": "2026-10-17",
      "supports": "General anatomy/material utilization; not evidence that every wild category is routinely harvested."
    }
  ],
  "acquisitionMethods": [
    {
      "tag": "butchering",
      "name": {
        "en": "Butchering",
        "es": "Despiece"
      },
      "description": {
        "en": "Remove flesh, bones and raw fat from a usable carcass; not an automatic reward for sighting or killing.",
        "es": "Extrae carne, huesos y grasa cruda de un cuerpo aprovechable; no es recompensa automática por avistar o matar."
      },
      "sourceOutcome": "requires_dead_animal",
      "availabilityConstraints": [],
      "runtimeEnabled": false
    }
  ],
  "serviceUseCandidates": [
    {
      "entityId": "animal_woodland_caribou",
      "serviceTag": "draft_service",
      "status": "requires_separate_training_and_husbandry_design",
      "availabilityConstraints": [
        "suitable_individual",
        "controlled_training",
        "historical_suitability_review"
      ],
      "runtimeEnabled": false
    }
  ],
  "productCoverage": {
    "animalEntityCount": 101,
    "materialLinkCount": 498,
    "acquisitionMethodCount": 17,
    "serviceCandidateCount": 7
  }
}
```
