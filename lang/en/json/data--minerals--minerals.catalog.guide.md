# `data/minerals/minerals.catalog.guide.json`

[Source JSON](../../../data/minerals/minerals.catalog.guide.json) · [Index](../json-structures.md)

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
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"mineral_catalog_design_guide"` |
| `geologicalResourceCandidates` | `array<object>` | 1/1 | Source materials and geological forms awaiting deposit and processing design. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.geologicalResourceCandidates[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 57/57 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"geological_clay"` |
| `name` | `object` | 57/57 | Player-visible label using language keys. | `—` |
| `definitionStatus` | `string` | 57/57 | Readiness of this record; source candidates are not runtime definitions. | `"source_candidate"` |
| `geologyConstraints` | `null` | 57/57 | Geological requirements pending formalization; biome alone is insufficient. | `null` |
| `refinedOutputResourceId` | `null` | 57/57 | Reference to a processed resource; extraction does not directly grant refined metal. | `null` |
| `surfaceAndOreDistinction` | `string` | 57/57 | Rule distinguishing surface material, ore and processed output. | `"No refined metal is granted directly by a deposit. Extraction and processing recipes remain separate."` |
| `sourceLabel` | `string` | 57/57 | Exact Spanish source label for provenance, not a localized UI field. | `"Arcilla"` |
| `extractedResourceId` | `string` | 57/57 | Material obtained through a future acquisition action; never an automatic refined metal output. | `"RES#000047"` |

### `$.geologicalResourceCandidates[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 57/57 | English visible text. | `"Clay"` |
| `es` | `string` | 57/57 | Spanish visible text. | `"Arcilla"` |

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
  "kind": "mineral_catalog_design_guide",
  "geologicalResourceCandidates": [
    {
      "id": "geological_clay",
      "name": {
        "en": "Clay",
        "es": "Arcilla"
      },
      "definitionStatus": "source_candidate",
      "geologyConstraints": null,
      "refinedOutputResourceId": null,
      "surfaceAndOreDistinction": "No refined metal is granted directly by a deposit. Extraction and processing recipes remain separate.",
      "sourceLabel": "Arcilla",
      "extractedResourceId": "RES#000047"
    }
  ]
}
```
