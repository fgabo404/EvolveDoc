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
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.1.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.2.0"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"animal_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Flat candidate records; broad groups are not yet accepted exact species. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.speciesCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 134/134 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"animal_eurasian_moose"` |
| `kind` | `string` | 134/134 | Discriminator identifying this document or candidate category. | `"animal"` |
| `name` | `object` | 134/134 | Player-visible label using language keys. | `—` |
| `taxonomy` | `object` | 134/134 | Scientific identity, evidence and review information. | `—` |
| `definitionStatus` | `string` | 134/134 | Readiness of this record; source candidates are not runtime definitions. | `"design_guide_only"` |
| `nativeRegionIds` | `array<?>` | 134/134 | References to native regions; empty means unresolved, not worldwide distribution. | `[]` |
| `biomeVariantIds` | `array<string>` | 134/134 | References to regional variants listing this candidate. | `["temperate_forest_boreal"]` |
| `ecology` | `object` | 134/134 | Environmental requirements; quantitative values remain unresolved. | `—` |
| `propagation` | `object` | 134/134 | Reproduction/propagation methods and required materials, still under design. | `—` |
| `domestication` | `object` | 134/134 | Eligibility, ancestor/form relationships and selection criteria. | `—` |
| `potentialProducts` | `array<object>` | 134/134 | Potential source uses; not confirmed outputs, quantities or unlocks. | `[]` |
| `potentialUseMethods` | `array<string>` | 134/134 | Potential source use methods, not authorized gameplay actions. | `["hunting"]` |
| `cultivationResearch` | `null` | 134/134 | Illustrative link to per-species research; null means no binding specified. | `null` |
| `sourceLabel` | `string` | 134/134 | Exact Spanish source label for provenance, not a localized UI field. | `"Alce euroasiático"` |
| `initialPresencePolicy` | `string` | 134/134 | Constraints to resolve before initial spawning. | `"resolve_native_region_and_habitat_before_spawning"` |

### `$.speciesCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 134/134 | English visible text. | `"Eurasian Moose"` |
| `es` | `string` | 134/134 | Spanish visible text. | `"Alce euroasiático"` |

### `$.speciesCandidates[].taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 134/134 | Scientific name only when provided by the source; null means unresolved and does not identify a taxon. | `"Gallus gallus"` |
| `nameEvidence` | `string` | 134/134 | Evidence supporting the recorded scientific name or its absence. | `"not_supplied"` |
| `resolutionStatus` | `string` | 134/134 | Task still required to resolve a candidate or regional restriction. | `"named_taxon_requires_verification"` |
| `verified` | `boolean` | 134/134 | Whether scientific verification has been performed; current candidates are not verified. | `false` |

### `$.speciesCandidates[].ecology`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 134/134 | Temperature bounds in degrees Celsius; null has no finalized inner structure. | `null` |
| `moistureRange` | `null` | 134/134 | Moisture bounds; units and structure remain unresolved. | `null` |
| `elevationRangeM` | `null` | 134/134 | Elevation bounds in meters; values and structure remain unresolved. | `null` |
| `waterRequirements` | `null` | 134/134 | Species water requirements; unresolved, not absence of a requirement. | `null` |
| `soilRequirements` | `null` | 134/134 | Species soil constraints, awaiting a structured definition. | `null` |
| `habitatRestrictionsStatus` | `string` | 134/134 | Developer explanation of unresolved habitat restrictions. | `"See source occurrences; quantitative constraints remain undefined."` |

### `$.speciesCandidates[].propagation`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 134/134 | Supported propagation methods; null is unresolved. | `null` |
| `materialResourceIds` | `null` | 134/134 | References to propagation resources; null means unresolved links. | `null` |

### `$.speciesCandidates[].domestication`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 134/134 | Whether and under what review a candidate may use this mechanism. | `"requires_species_review"` |
| `wildAncestorId` | `null` | 134/134 | Reference to the selected wild ancestor, not automatically inferred. | `null` |
| `domesticatedFormId` | `null` | 134/134 | Reference to a domesticated form; does not grant instant domestication. | `null` |
| `criteria` | `null` | 134/134 | Domestication criteria, not yet modeled. | `null` |

### `$.speciesCandidates[].potentialProducts[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceTag` | `string` | 295/295 | English resource-category tag; not a resolved resource ID. | `"meat"` |
| `status` | `string` | 295/295 | Maturity, review state or current example research status; read the containing object. | `"potential_from_source"` |
| `requiredTechnologyIds` | `null` | 295/295 | Technology references needed for this output; null means unresolved, not none. | `null` |
| `yield` | `null` | 295/295 | Output yield; units, formula and amount remain unresolved. | `null` |
| `resourceId` | `string` | 264/295 | Reference to a resource definition, distinct from a species or deposit ID. | `"RES#000029"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.1.0",
  "contentVersion": "0.2.0",
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
        "resolutionStatus": "named_taxon_requires_verification",
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
      "initialPresencePolicy": "resolve_native_region_and_habitat_before_spawning"
    }
  ]
}
```
