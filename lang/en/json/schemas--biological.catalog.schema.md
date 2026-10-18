# `schemas/biological.catalog.schema.json`

[Source JSON](../../../schemas/biological.catalog.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Document or schema title. | `"Evolve biological reference catalog"` |
| `description` | `string` | 1/1 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `"Full structural contract for optional scientific background catalog 1.1.0. Gameplay categories are defined in t…` |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["biologicalForms", "contentVersion", "defaultLanguage"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `biologicalForms` | `object` | 1/1 | Subschema describing `biologicalForms`; see its nested fields below. | `—` |
| `contentVersion` | `object` | 1/1 | Subschema describing `contentVersion`; see its nested fields below. | `—` |
| `defaultLanguage` | `object` | 1/1 | Subschema describing `defaultLanguage`; see its nested fields below. | `—` |
| `evidenceSources` | `object` | 1/1 | Subschema describing `evidenceSources`; see its nested fields below. | `—` |
| `excludedLineageRelations` | `object` | 1/1 | Subschema describing `excludedLineageRelations`; see its nested fields below. | `—` |
| `kind` | `object` | 1/1 | Subschema describing `kind`; see its nested fields below. | `—` |
| `lineageRelations` | `object` | 1/1 | Subschema describing `lineageRelations`; see its nested fields below. | `—` |
| `reviewIssues` | `object` | 1/1 | Subschema describing `reviewIssues`; see its nested fields below. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subschema describing `runtimePolicy`; see its nested fields below. | `—` |
| `schemaVersion` | `object` | 1/1 | Subschema describing `schemaVersion`; see its nested fields below. | `—` |
| `status` | `object` | 1/1 | Subschema describing `status`; see its nested fields below. | `—` |
| `summary` | `object` | 1/1 | Subschema describing `summary`; see its nested fields below. | `—` |
| `supportedLanguages` | `object` | 1/1 | Subschema describing `supportedLanguages`; see its nested fields below. | `—` |
| `taxa` | `object` | 1/1 | Subschema describing `taxa`; see its nested fields below. | `—` |

### `$.properties.biologicalForms`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.biologicalForms.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["evidenceSourceKeys", "formKind", "id"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.biologicalForms.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `evidenceSourceKeys` | `object` | 1/1 | Subschema describing `evidenceSourceKeys`; see its nested fields below. | `—` |
| `formKind` | `object` | 1/1 | Subschema describing `formKind`; see its nested fields below. | `—` |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `literatureName` | `object` | 1/1 | Subschema describing `literatureName`; see its nested fields below. | `—` |
| `name` | `object` | 1/1 | Subschema describing `name`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |
| `status` | `object` | 1/1 | Subschema describing `status`; see its nested fields below. | `—` |
| `tag` | `object` | 1/1 | Subschema describing `tag`; see its nested fields below. | `—` |
| `taxonId` | `object` | 1/1 | Subschema describing `taxonId`; see its nested fields below. | `—` |

### `$.properties.biologicalForms.items.properties.evidenceSourceKeys`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.biologicalForms.items.properties.evidenceSourceKeys.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.biologicalForms.items.properties.formKind`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.biologicalForms.items.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^FRM#[0-9]{6}$"` |

### `$.properties.biologicalForms.items.properties.literatureName`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.biologicalForms.items.properties.name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.biologicalForms.items.properties.name.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subschema describing `en`; see its nested fields below. | `—` |
| `es` | `object` | 1/1 | Subschema describing `es`; see its nested fields below. | `—` |

### `$.properties.biologicalForms.items.properties.name.properties.en`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.properties.biologicalForms.items.properties.name.properties.es`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.properties.biologicalForms.items.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.properties.biologicalForms.items.properties.status`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.biologicalForms.items.properties.tag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.biologicalForms.items.properties.taxonId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.contentVersion`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.defaultLanguage`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.evidenceSources`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.evidenceSources.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["checkedOn", "sourceKey", "supports"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.evidenceSources.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `checkedOn` | `object` | 1/1 | Subschema describing `checkedOn`; see its nested fields below. | `—` |
| `sourceKey` | `object` | 1/1 | Subschema describing `sourceKey`; see its nested fields below. | `—` |
| `supports` | `object` | 1/1 | Subschema describing `supports`; see its nested fields below. | `—` |
| `title` | `object` | 1/1 | Subschema describing `title`; see its nested fields below. | `—` |
| `url` | `object` | 1/1 | Subschema describing `url`; see its nested fields below. | `—` |

### `$.properties.evidenceSources.items.properties.checkedOn`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.evidenceSources.items.properties.sourceKey`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.evidenceSources.items.properties.supports`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.evidenceSources.items.properties.title`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.evidenceSources.items.properties.url`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.excludedLineageRelations.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["childFormId", "evidenceSourceKeys", "parentFormId"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.excludedLineageRelations.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `childFormId` | `object` | 1/1 | Subschema describing `childFormId`; see its nested fields below. | `—` |
| `evidenceSourceKeys` | `object` | 1/1 | Subschema describing `evidenceSourceKeys`; see its nested fields below. | `—` |
| `parentFormId` | `object` | 1/1 | Subschema describing `parentFormId`; see its nested fields below. | `—` |
| `reason` | `object` | 1/1 | Subschema describing `reason`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |

### `$.properties.excludedLineageRelations.items.properties.childFormId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.evidenceSourceKeys`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.excludedLineageRelations.items.properties.evidenceSourceKeys.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.parentFormId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.reason`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["en", "es"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subschema describing `en`; see its nested fields below. | `—` |
| `es` | `object` | 1/1 | Subschema describing `es`; see its nested fields below. | `—` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties.en`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties.es`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |

### `$.properties.kind`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.lineageRelations.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["childFormIds", "description", "evidenceSourceKeys"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.lineageRelations.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `childFormIds` | `object` | 1/1 | Subschema describing `childFormIds`; see its nested fields below. | `—` |
| `description` | `object` | 1/1 | Subschema describing `description`; see its nested fields below. | `—` |
| `evidenceSourceKeys` | `object` | 1/1 | Subschema describing `evidenceSourceKeys`; see its nested fields below. | `—` |
| `exactAncestralPopulationResolved` | `object` | 1/1 | Subschema describing `exactAncestralPopulationResolved`; see its nested fields below. | `—` |
| `parentFormIds` | `object` | 1/1 | Subschema describing `parentFormIds`; see its nested fields below. | `—` |
| `relationType` | `object` | 1/1 | Subschema describing `relationType`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |
| `supportLevel` | `object` | 1/1 | Subschema describing `supportLevel`; see its nested fields below. | `—` |

### `$.properties.lineageRelations.items.properties.childFormIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.lineageRelations.items.properties.childFormIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["en", "es"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.lineageRelations.items.properties.description.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subschema describing `en`; see its nested fields below. | `—` |
| `es` | `object` | 1/1 | Subschema describing `es`; see its nested fields below. | `—` |

### `$.properties.lineageRelations.items.properties.description.properties.en`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.description.properties.es`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.evidenceSourceKeys`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.lineageRelations.items.properties.evidenceSourceKeys.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.exactAncestralPopulationResolved`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |

### `$.properties.lineageRelations.items.properties.parentFormIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.lineageRelations.items.properties.parentFormIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.relationType`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.lineageRelations.items.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |

### `$.properties.lineageRelations.items.properties.supportLevel`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.reviewIssues`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.reviewIssues.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id", "resolution"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.reviewIssues.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `resolution` | `object` | 1/1 | Subschema describing `resolution`; see its nested fields below. | `—` |

### `$.properties.reviewIssues.items.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.reviewIssues.items.properties.resolution`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["floraClassification", "identityPolicy", "lineagePolicy"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.runtimePolicy.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `floraClassification` | `object` | 1/1 | Subschema describing `floraClassification`; see its nested fields below. | `—` |
| `identityPolicy` | `object` | 1/1 | Subschema describing `identityPolicy`; see its nested fields below. | `—` |
| `lineagePolicy` | `object` | 1/1 | Subschema describing `lineagePolicy`; see its nested fields below. | `—` |
| `loadAsGameDefinitions` | `object` | 1/1 | Subschema describing `loadAsGameDefinitions`; see its nested fields below. | `—` |
| `resourceInheritance` | `object` | 1/1 | Subschema describing `resourceInheritance`; see its nested fields below. | `—` |
| `sourceInterpretation` | `object` | 1/1 | Subschema describing `sourceInterpretation`; see its nested fields below. | `—` |
| `unknownValues` | `object` | 1/1 | Subschema describing `unknownValues`; see its nested fields below. | `—` |
| `varietyPolicy` | `object` | 1/1 | Subschema describing `varietyPolicy`; see its nested fields below. | `—` |
| `gameplayIdentity` | `object` | 1/1 | Subschema describing `gameplayIdentity`; see its nested fields below. | `—` |

### `$.properties.runtimePolicy.properties.floraClassification`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.identityPolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.lineagePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.loadAsGameDefinitions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.properties.runtimePolicy.properties.resourceInheritance`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.sourceInterpretation`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.unknownValues`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.varietyPolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy.properties.gameplayIdentity`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.schemaVersion`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.status`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["biologicalFormCount", "cropCandidateCount", "excludedLineageRelationCount"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.summary.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `biologicalFormCount` | `object` | 1/1 | Subschema describing `biologicalFormCount`; see its nested fields below. | `—` |
| `cropCandidateCount` | `object` | 1/1 | Subschema describing `cropCandidateCount`; see its nested fields below. | `—` |
| `excludedLineageRelationCount` | `object` | 1/1 | Subschema describing `excludedLineageRelationCount`; see its nested fields below. | `—` |
| `lineageRelationCount` | `object` | 1/1 | Subschema describing `lineageRelationCount`; see its nested fields below. | `—` |
| `sourceCandidateCount` | `object` | 1/1 | Subschema describing `sourceCandidateCount`; see its nested fields below. | `—` |
| `taxonCount` | `object` | 1/1 | Subschema describing `taxonCount`; see its nested fields below. | `—` |

### `$.properties.summary.properties.biologicalFormCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.summary.properties.cropCandidateCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.summary.properties.excludedLineageRelationCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.summary.properties.lineageRelationCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.summary.properties.sourceCandidateCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.summary.properties.taxonCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.supportedLanguages`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.supportedLanguages.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.taxa.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id", "name", "nativeRangeReviewStatus"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.taxa.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `name` | `object` | 1/1 | Subschema describing `name`; see its nested fields below. | `—` |
| `nativeRangeReviewStatus` | `object` | 1/1 | Subschema describing `nativeRangeReviewStatus`; see its nested fields below. | `—` |
| `organismGroup` | `object` | 1/1 | Subschema describing `organismGroup`; see its nested fields below. | `—` |
| `reviewStatus` | `object` | 1/1 | Subschema describing `reviewStatus`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |
| `scientificName` | `object` | 1/1 | Subschema describing `scientificName`; see its nested fields below. | `—` |
| `tag` | `object` | 1/1 | Subschema describing `tag`; see its nested fields below. | `—` |
| `taxonRank` | `object` | 1/1 | Subschema describing `taxonRank`; see its nested fields below. | `—` |
| `taxonomy` | `object` | 1/1 | Subschema describing `taxonomy`; see its nested fields below. | `—` |

### `$.properties.taxa.items.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^(PLT\|ANM\|ALG\|FNG)#[0-9]{6}$"` |

### `$.properties.taxa.items.properties.name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.taxa.items.properties.name.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subschema describing `en`; see its nested fields below. | `—` |
| `es` | `object` | 1/1 | Subschema describing `es`; see its nested fields below. | `—` |

### `$.properties.taxa.items.properties.name.properties.en`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.properties.taxa.items.properties.name.properties.es`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.properties.taxa.items.properties.nativeRangeReviewStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.organismGroup`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.reviewStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.properties.taxa.items.properties.scientificName`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.tag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonRank`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `enum` | `array<string>` | 1/1 | Explicit set of allowed JSON values. | `["SPECIES", "SUBSPECIES", "VARIETY"]` |

### `$.properties.taxa.items.properties.taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["family", "genus", "kingdom"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.taxa.items.properties.taxonomy.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `family` | `object` | 1/1 | Subschema describing `family`; see its nested fields below. | `—` |
| `genus` | `object` | 1/1 | Subschema describing `genus`; see its nested fields below. | `—` |
| `kingdom` | `object` | 1/1 | Subschema describing `kingdom`; see its nested fields below. | `—` |
| `matchEvidence` | `object` | 1/1 | Subschema describing `matchEvidence`; see its nested fields below. | `—` |
| `provider` | `object` | 1/1 | Subschema describing `provider`; see its nested fields below. | `—` |
| `providerTaxonKey` | `object` | 1/1 | Subschema describing `providerTaxonKey`; see its nested fields below. | `—` |
| `referenceUrl` | `object` | 1/1 | Subschema describing `referenceUrl`; see its nested fields below. | `—` |
| `taxonomicStatus` | `object` | 1/1 | Subschema describing `taxonomicStatus`; see its nested fields below. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.family`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.genus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.kingdom`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["checkedOn", "confidence", "matchStatus"]` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `checkedOn` | `object` | 1/1 | Subschema describing `checkedOn`; see its nested fields below. | `—` |
| `confidence` | `object` | 1/1 | Subschema describing `confidence`; see its nested fields below. | `—` |
| `matchStatus` | `object` | 1/1 | Subschema describing `matchStatus`; see its nested fields below. | `—` |
| `matchType` | `object` | 1/1 | Subschema describing `matchType`; see its nested fields below. | `—` |
| `matchedScientificName` | `object` | 1/1 | Subschema describing `matchedScientificName`; see its nested fields below. | `—` |
| `queriedName` | `object` | 1/1 | Subschema describing `queriedName`; see its nested fields below. | `—` |
| `requestUrl` | `object` | 1/1 | Subschema describing `requestUrl`; see its nested fields below. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.checkedOn`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.confidence`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchType`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchedScientificName`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.queriedName`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.requestUrl`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.provider`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.providerTaxonKey`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.referenceUrl`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.taxonomicStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evolve biological reference catalog",
  "description": "Full structural contract for optional scientific background catalog 1.1.0. Gameplay categories are defined in the plant/animal guides, independently of taxonomic identity.",
  "type": "object",
  "properties": {
    "biologicalForms": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "evidenceSourceKeys": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "formKind": {
            "type": "string"
          },
          "id": {
            "type": "string",
            "pattern": "^FRM#[0-9]{6}$"
          },
          "literatureName": {
            "type": "string"
          },
          "name": {
            "type": "object",
            "required": [
              "en",
              "es"
            ],
            "properties": {
              "en": {
                "type": "string",
                "minLength": 1
              },
              "es": {
                "type": "string",
                "minLength": 1
              }
            },
            "additionalProperties": false
          },
          "runtimeEnabled": {
            "type": "boolean",
            "const": false
          },
          "status": {
            "type": "string"
          },
          "tag": {
            "type": "string"
          },
          "taxonId": {
            "type": "string"
          }
        },
        "required": [
          "evidenceSourceKeys",
          "formKind",
          "id",
          "literatureName",
          "name",
          "runtimeEnabled",
          "status",
          "tag",
          "taxonId"
        ],
        "additionalProperties": false
      }
    },
    "contentVersion": {
      "type": "string"
    },
    "defaultLanguage": {
      "type": "string"
    },
    "evidenceSources": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "checkedOn": {
            "type": "string"
          },
          "sourceKey": {
            "type": "string"
          },
          "supports": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "checkedOn",
          "sourceKey",
          "supports",
          "title",
          "url"
        ],
        "additionalProperties": false
      }
    },
    "excludedLineageRelations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "childFormId": {
            "type": "string"
          },
          "evidenceSourceKeys": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "parentFormId": {
            "type": "string"
          },
          "reason": {
            "type": "object",
            "properties": {
              "en": {
                "type": "string"
              },
              "es": {
                "type": "string"
              }
            },
            "required": [
              "en",
              "es"
            ],
            "additionalProperties": false
          },
          "runtimeEnabled": {
            "type": "boolean"
          }
        },
        "required": [
          "childFormId",
          "evidenceSourceKeys",
          "parentFormId",
          "reason",
          "runtimeEnabled"
        ],
        "additionalProperties": false
      }
    },
    "kind": {
      "type": "string"
    },
    "lineageRelations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "childFormIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "description": {
            "type": "object",
            "properties": {
              "en": {
                "type": "string"
              },
              "es": {
                "type": "string"
              }
            },
            "required": [
              "en",
              "es"
            ],
            "additionalProperties": false
          },
          "evidenceSourceKeys": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "exactAncestralPopulationResolved": {
            "type": "boolean"
          },
          "parentFormIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "relationType": {
            "type": "string"
          },
          "runtimeEnabled": {
            "type": "boolean"
          },
          "supportLevel": {
            "type": "string"
          }
        },
        "required": [
          "childFormIds",
          "description",
          "evidenceSourceKeys",
          "exactAncestralPopulationResolved",
          "parentFormIds",
          "relationType",
          "runtimeEnabled",
          "supportLevel"
        ],
        "additionalProperties": false
      }
    },
    "reviewIssues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "resolution": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "resolution"
        ],
        "additionalProperties": false
      }
    },
    "runtimePolicy": {
      "type": "object",
      "properties": {
        "floraClassification": {
          "type": "string"
        },
        "identityPolicy": {
          "type": "string"
        },
        "lineagePolicy": {
          "type": "string"
        },
        "loadAsGameDefinitions": {
          "type": "boolean",
          "const": false
        },
        "resourceInheritance": {
          "type": "string"
        },
        "sourceInterpretation": {
          "type": "string"
        },
        "unknownValues": {
          "type": "string"
        },
        "varietyPolicy": {
          "type": "string"
        },
        "gameplayIdentity": {
          "type": "string"
        }
      },
      "required": [
        "floraClassification",
        "identityPolicy",
        "lineagePolicy",
        "loadAsGameDefinitions",
        "resourceInheritance",
        "sourceInterpretation",
        "unknownValues",
        "varietyPolicy",
        "gameplayIdentity"
      ],
      "additionalProperties": false
    },
    "schemaVersion": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "summary": {
      "type": "object",
      "properties": {
        "biologicalFormCount": {
          "type": "integer"
        },
        "cropCandidateCount": {
          "type": "integer"
        },
        "excludedLineageRelationCount": {
          "type": "integer"
        },
        "lineageRelationCount": {
          "type": "integer"
        },
        "sourceCandidateCount": {
          "type": "integer"
        },
        "taxonCount": {
          "type": "integer"
        }
      },
      "required": [
        "biologicalFormCount",
        "cropCandidateCount",
        "excludedLineageRelationCount",
        "lineageRelationCount",
        "sourceCandidateCount",
        "taxonCount"
      ],
      "additionalProperties": false
    },
    "supportedLanguages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "taxa": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^(PLT|ANM|ALG|FNG)#[0-9]{6}$"
          },
          "name": {
            "type": "object",
            "required": [
              "en",
              "es"
            ],
            "properties": {
              "en": {
                "type": "string",
                "minLength": 1
              },
              "es": {
                "type": "string",
                "minLength": 1
              }
            },
            "additionalProperties": false
          },
          "nativeRangeReviewStatus": {
            "type": "string"
          },
          "organismGroup": {
            "type": "string"
          },
          "reviewStatus": {
            "type": "string"
          },
          "runtimeEnabled": {
            "type": "boolean",
            "const": false
          },
          "scientificName": {
            "type": "string"
          },
          "tag": {
            "type": "string"
          },
          "taxonRank": {
            "type": "string",
            "enum": [
              "SPECIES",
              "SUBSPECIES",
              "VARIETY"
            ]
          },
          "taxonomy": {
            "type": "object",
            "properties": {
              "family": {
                "type": "string"
              },
              "genus": {
                "type": "string"
              },
              "kingdom": {
                "type": "string"
              },
              "matchEvidence": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "checkedOn": {
                      "type": "string"
                    },
                    "confidence": {
                      "type": "integer"
                    },
                    "matchStatus": {
                      "type": "string"
                    },
                    "matchType": {
                      "type": "string"
                    },
                    "matchedScientificName": {
                      "type": "string"
                    },
                    "queriedName": {
                      "type": "string"
                    },
                    "requestUrl": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "checkedOn",
                    "confidence",
                    "matchStatus",
                    "matchType",
                    "matchedScientificName",
                    "queriedName",
                    "requestUrl"
                  ],
                  "additionalProperties": false
                }
              },
              "provider": {
                "type": "string"
              },
              "providerTaxonKey": {
                "type": "string"
              },
              "referenceUrl": {
                "type": "string"
              },
              "taxonomicStatus": {
                "type": "string"
              }
            },
            "required": [
              "family",
              "genus",
              "kingdom",
              "matchEvidence",
              "provider",
              "providerTaxonKey",
              "referenceUrl",
              "taxonomicStatus"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "id",
          "name",
          "nativeRangeReviewStatus",
          "organismGroup",
          "reviewStatus",
          "runtimeEnabled",
          "scientificName",
          "tag",
          "taxonRank",
          "taxonomy"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "biologicalForms",
    "contentVersion",
    "defaultLanguage",
    "evidenceSources",
    "excludedLineageRelations",
    "kind",
    "lineageRelations",
    "reviewIssues",
    "runtimePolicy",
    "schemaVersion",
    "status",
    "summary",
    "supportedLanguages",
    "taxa"
  ],
  "additionalProperties": false
}
```
