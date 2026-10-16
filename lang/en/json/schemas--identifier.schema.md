# `schemas/identifier.schema.json`

[Source JSON](../../../schemas/identifier.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Document or schema title. | `"Future Evolve definition identity"` |
| `description` | `string` | 1/1 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `"Proposed future identifier envelope. Existing legacy catalogs are not migrated and do not conform to this envel…` |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id", "tag"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |

### `$.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `tag` | `object` | 1/1 | Subschema describing `tag`; see its nested fields below. | `—` |

### `$.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^(BIO\|VAR\|REG\|TER\|SOL\|GEO\|PLT\|ANM\|FNG\|RES\|DEP\|DST\|TEC\|ITM\|RCP\|BLD\|IMP\|CAP\|EUR)#[0-9]{6}$"` |
| `not` | `object` | 1/1 | Subschema that must not validate; rejects the reserved zero ID here. | `—` |

### `$.properties.id.not`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"#000000$"` |

### `$.properties.tag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Future Evolve definition identity",
  "description": "Proposed future identifier envelope. Existing legacy catalogs are not migrated and do not conform to this envelope. Not a complete entity schema.",
  "type": "object",
  "required": [
    "id",
    "tag"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^(BIO|VAR|REG|TER|SOL|GEO|PLT|ANM|FNG|RES|DEP|DST|TEC|ITM|RCP|BLD|IMP|CAP|EUR)#[0-9]{6}$",
      "not": {
        "pattern": "#000000$"
      }
    },
    "tag": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"
    }
  }
}
```
