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
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.0.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.1.0"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"plant_catalog_design_guide"` |
| `speciesCandidates` | `array<object>` | 1/1 | Flat candidate records; broad groups are not yet accepted exact species. | `—` |
| `agriculturalCropCandidates` | `array<object>` | 1/1 | Crop groups awaiting exact species, ancestors and production definitions. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.speciesCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 129/129 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"plant_dwarf_birch"` |
| `kind` | `string` | 129/129 | Discriminator identifying this document or candidate category. | `"plant"` |
| `name` | `object` | 129/129 | Player-visible label using language keys. | `—` |
| `taxonomy` | `object` | 129/129 | Scientific identity, evidence and review information. | `—` |
| `definitionStatus` | `string` | 129/129 | Readiness of this record; source candidates are not runtime definitions. | `"design_guide_only"` |
| `nativeRegionIds` | `array<?>` | 129/129 | References to native regions; empty means unresolved, not worldwide distribution. | `[]` |
| `biomeVariantIds` | `array<string>` | 129/129 | References to regional variants listing this candidate. | `["tundra_eurasian"]` |
| `ecology` | `object` | 129/129 | Environmental requirements; quantitative values remain unresolved. | `—` |
| `propagation` | `object` | 129/129 | Reproduction/propagation methods and required materials, still under design. | `—` |
| `domestication` | `object` | 129/129 | Eligibility, ancestor/form relationships and selection criteria. | `—` |
| `potentialProducts` | `null` | 129/129 | Potential source uses; not confirmed outputs, quantities or unlocks. | `null` |
| `potentialUseMethods` | `array<?>` | 129/129 | Potential source use methods, not authorized gameplay actions. | `[]` |
| `cultivationResearch` | `object` | 129/129 | Illustrative link to per-species research; null means no binding specified. | `—` |
| `sourceLabel` | `string` | 129/129 | Exact Spanish source label for provenance, not a localized UI field. | `"Abedul enano"` |
| `initialPresencePolicy` | `string` | 129/129 | Constraints to resolve before initial spawning. | `"resolve_native_region_and_habitat_before_spawning"` |

### `$.speciesCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 129/129 | English visible text. | `"Dwarf Birch"` |
| `es` | `string` | 129/129 | Spanish visible text. | `"Abedul enano"` |

### `$.speciesCandidates[].taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `scientificName` | `null \| string` | 129/129 | Scientific name only when provided by the source; null means unresolved and does not identify a taxon. | `"Nothofagus dombeyi"` |
| `nameEvidence` | `string` | 129/129 | Evidence supporting the recorded scientific name or its absence. | `"not_supplied"` |
| `resolutionStatus` | `string` | 129/129 | Task still required to resolve a candidate or regional restriction. | `"named_taxon_requires_verification"` |
| `verified` | `boolean` | 129/129 | Whether scientific verification has been performed; current candidates are not verified. | `false` |

### `$.speciesCandidates[].ecology`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `temperatureRangeC` | `null` | 129/129 | Temperature bounds in degrees Celsius; null has no finalized inner structure. | `null` |
| `moistureRange` | `null` | 129/129 | Moisture bounds; units and structure remain unresolved. | `null` |
| `elevationRangeM` | `null` | 129/129 | Elevation bounds in meters; values and structure remain unresolved. | `null` |
| `waterRequirements` | `null` | 129/129 | Species water requirements; unresolved, not absence of a requirement. | `null` |
| `soilRequirements` | `null` | 129/129 | Species soil constraints, awaiting a structured definition. | `null` |
| `habitatRestrictionsStatus` | `string` | 129/129 | Developer explanation of unresolved habitat restrictions. | `"See source occurrences; quantitative constraints remain undefined."` |

### `$.speciesCandidates[].propagation`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `methods` | `null` | 129/129 | Supported propagation methods; null is unresolved. | `null` |
| `materialResourceIds` | `null` | 129/129 | References to propagation resources; null means unresolved links. | `null` |

### `$.speciesCandidates[].domestication`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `eligibility` | `string` | 129/129 | Whether and under what review a candidate may use this mechanism. | `"requires_species_review"` |
| `wildAncestorId` | `null` | 129/129 | Reference to the selected wild ancestor, not automatically inferred. | `null` |
| `domesticatedFormId` | `null` | 129/129 | Reference to a domesticated form; does not grant instant domestication. | `null` |
| `criteria` | `null` | 129/129 | Domestication criteria, not yet modeled. | `null` |

### `$.speciesCandidates[].cultivationResearch`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 129/129 | Reference to a technology definition or declared external import. | `"species_cultivation"` |
| `speciesId` | `string` | 129/129 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"plant_dwarf_birch"` |
| `eligibility` | `string` | 129/129 | Whether and under what review a candidate may use this mechanism. | `"Only instantiate after the exact species is confirmed cultivable; flora presence alone does not imply agricultu…` |

### `$.agriculturalCropCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 21/21 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"wheat"` |
| `name` | `object` | 21/21 | Player-visible label using language keys. | `—` |
| `cropUseTag` | `string` | 21/21 | Gameplay crop-use group, not a botanical species. | `"cereal"` |
| `sourceOriginHint` | `null \| string` | 21/21 | Source geographic origin hint; not a verified native-range rule. | `"Southwest Asia"` |
| `scientificName` | `null` | 21/21 | Scientific name only when provided by the source; null means unresolved and does not identify a taxon. | `null` |
| `resolutionStatus` | `string` | 21/21 | Task still required to resolve a candidate or regional restriction. | `"select_exact_species_and_wild_ancestor"` |
| `wildAncestorCandidateIds` | `array<?>` | 21/21 | Possible ancestor links pending scientific review. | `[]` |
| `cultivationResearch` | `object` | 21/21 | Illustrative link to per-species research; null means no binding specified. | `—` |
| `products` | `null` | 21/21 | Crop outputs awaiting resource definitions and recipes. | `null` |
| `ecologicalConstraints` | `null` | 21/21 | Crop environmental rules awaiting formalization. | `null` |
| `sourceSection` | `string` | 21/21 | Source section from which this entry was extracted. | `"5. Initial agricultural and plant catalog"` |

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

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.0.0",
  "contentVersion": "0.1.0",
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
        "resolutionStatus": "named_taxon_requires_verification",
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
      "initialPresencePolicy": "resolve_native_region_and_habitat_before_spawning"
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
      "products": null,
      "ecologicalConstraints": null,
      "sourceSection": "5. Initial agricultural and plant catalog"
    }
  ]
}
```
