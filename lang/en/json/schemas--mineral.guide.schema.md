# `schemas/mineral.guide.schema.json`

[Source JSON](../../../schemas/mineral.guide.schema.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

These are JSON Schema keywords, not game-definition fields. The envelope allows additional properties unless explicitly restricted. This document describes the schema file itself; it does not turn its limited validation into a full domain contract.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$schema` | `string` | 1/1 | JSON Schema dialect URI; not a reference to game data. | `"https://json-schema.org/draft/2020-12/schema"` |
| `title` | `string` | 1/1 | Document or schema title. | `"mineral_catalog_design_guide envelope"` |
| `description` | `string` | 1/1 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `"Preliminary structural envelope only; not a full field-level or semantic schema."` |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["schemaVersion", "kind", "runtimePolicy"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |

### `$.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `object` | 1/1 | Subschema describing `schemaVersion`; see its nested fields below. | `—` |
| `kind` | `object` | 1/1 | Subschema describing `kind`; see its nested fields below. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subschema describing `runtimePolicy`; see its nested fields below. | `—` |
| `geologicalResourceCandidates` | `object` | 1/1 | Subschema describing `geologicalResourceCandidates`; see its nested fields below. | `—` |

### `$.properties.schemaVersion`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.kind`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Exact allowed JSON value for the property. | `"mineral_catalog_design_guide"` |

### `$.properties.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["loadAsGameDefinitions"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |

### `$.properties.runtimePolicy.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `object` | 1/1 | Subschema describing `loadAsGameDefinitions`; see its nested fields below. | `—` |

### `$.properties.runtimePolicy.properties.loadAsGameDefinitions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.properties.geologicalResourceCandidates`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.geologicalResourceCandidates.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |

### `$.properties.geologicalResourceCandidates.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |

### `$.properties.geologicalResourceCandidates.items.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "mineral_catalog_design_guide envelope",
  "description": "Preliminary structural envelope only; not a full field-level or semantic schema.",
  "type": "object",
  "required": [
    "schemaVersion",
    "kind",
    "runtimePolicy",
    "geologicalResourceCandidates"
  ],
  "properties": {
    "schemaVersion": {
      "type": "string"
    },
    "kind": {
      "const": "mineral_catalog_design_guide"
    },
    "runtimePolicy": {
      "type": "object",
      "required": [
        "loadAsGameDefinitions"
      ],
      "properties": {
        "loadAsGameDefinitions": {
          "const": false
        }
      }
    },
    "geologicalResourceCandidates": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "id"
        ],
        "properties": {
          "id": {
            "type": "string"
          }
        }
      }
    }
  }
}
```
