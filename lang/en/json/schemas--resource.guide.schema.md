# `schemas/resource.guide.schema.json`

[Source JSON](../../../schemas/resource.guide.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Document or schema title. | `"Evolve resource design guide"` |
| `description` | `string` | 1/1 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `"Structural contract for the resource guide. Does not validate cross-file references, scientific evidence, proce…` |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["schemaVersion", "contentVersion", "kind"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |
| `$defs` | `object` | 1/1 | Named reusable subschemas within this JSON Schema document. | `—` |

### `$.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `object` | 1/1 | Subschema describing `schemaVersion`; see its nested fields below. | `—` |
| `contentVersion` | `object` | 1/1 | Subschema describing `contentVersion`; see its nested fields below. | `—` |
| `kind` | `object` | 1/1 | Subschema describing `kind`; see its nested fields below. | `—` |
| `status` | `object` | 1/1 | Subschema describing `status`; see its nested fields below. | `—` |
| `defaultLanguage` | `object` | 1/1 | Subschema describing `defaultLanguage`; see its nested fields below. | `—` |
| `supportedLanguages` | `object` | 1/1 | Subschema describing `supportedLanguages`; see its nested fields below. | `—` |
| `identityPolicy` | `object` | 1/1 | Subschema describing `identityPolicy`; see its nested fields below. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subschema describing `runtimePolicy`; see its nested fields below. | `—` |
| `resources` | `object` | 1/1 | Subschema describing `resources`; see its nested fields below. | `—` |
| `sourceBindings` | `object` | 1/1 | Subschema describing `sourceBindings`; see its nested fields below. | `—` |
| `sourceTagMappings` | `object` | 1/1 | Subschema describing `sourceTagMappings`; see its nested fields below. | `—` |
| `processingLinks` | `object` | 1/1 | Subschema describing `processingLinks`; see its nested fields below. | `—` |
| `unresolvedSources` | `object` | 1/1 | Subschema describing `unresolvedSources`; see its nested fields below. | `—` |
| `reviewIssues` | `object` | 1/1 | Subschema describing `reviewIssues`; see its nested fields below. | `—` |
| `summary` | `object` | 1/1 | Subschema describing `summary`; see its nested fields below. | `—` |

### `$.properties.schemaVersion`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Exact allowed JSON value for the property. | `"1.0.0"` |

### `$.properties.contentVersion`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.kind`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Exact allowed JSON value for the property. | `"resource_catalog_design_guide"` |

### `$.properties.status`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.defaultLanguage`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Exact allowed JSON value for the property. | `"en"` |

### `$.properties.supportedLanguages`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `array<string>` | 1/1 | Exact allowed JSON value for the property. | `["en", "es"]` |

### `$.properties.identityPolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.properties.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/runtimePolicy"` |

### `$.properties.resources`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.resources.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resource"` |

### `$.properties.sourceBindings`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.sourceBindings.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/sourceBinding"` |

### `$.properties.sourceTagMappings`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.sourceTagMappings.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/sourceTagMapping"` |

### `$.properties.processingLinks`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.processingLinks.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/processingLink"` |

### `$.properties.unresolvedSources`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.unresolvedSources.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/unresolvedSource"` |

### `$.properties.reviewIssues`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.properties.reviewIssues.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/reviewIssue"` |

### `$.properties.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/summary"` |

### `$.$defs`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `localizedText` | `object` | 1/1 | Subschema describing `localizedText`; see its nested fields below. | `—` |
| `resourceId` | `object` | 1/1 | Subschema describing `resourceId`; see its nested fields below. | `—` |
| `inventory` | `object` | 1/1 | Subschema describing `inventory`; see its nested fields below. | `—` |
| `resource` | `object` | 1/1 | Subschema describing `resource`; see its nested fields below. | `—` |
| `sourceBinding` | `object` | 1/1 | Subschema describing `sourceBinding`; see its nested fields below. | `—` |
| `sourceTagMapping` | `object` | 1/1 | Subschema describing `sourceTagMapping`; see its nested fields below. | `—` |
| `processingLink` | `object` | 1/1 | Subschema describing `processingLink`; see its nested fields below. | `—` |
| `unresolvedSource` | `object` | 1/1 | Subschema describing `unresolvedSource`; see its nested fields below. | `—` |
| `reviewIssue` | `object` | 1/1 | Subschema describing `reviewIssue`; see its nested fields below. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subschema describing `runtimePolicy`; see its nested fields below. | `—` |
| `summary` | `object` | 1/1 | Subschema describing `summary`; see its nested fields below. | `—` |

### `$.$defs.localizedText`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.localizedText.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subschema describing `en`; see its nested fields below. | `—` |
| `es` | `object` | 1/1 | Subschema describing `es`; see its nested fields below. | `—` |

### `$.$defs.localizedText.properties.en`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.$defs.localizedText.properties.es`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `minLength` | `integer` | 1/1 | Minimum permitted string length. | `1` |

### `$.$defs.resourceId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^RES#[0-9]{6}$"` |
| `not` | `object` | 1/1 | Subschema that must not validate; rejects the reserved zero ID here. | `—` |

### `$.$defs.resourceId.not`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"#000000$"` |

### `$.$defs.inventory`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["storable", "quantityUnit", "perishable"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.inventory.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `storable` | `object` | 1/1 | Subschema describing `storable`; see its nested fields below. | `—` |
| `quantityUnit` | `object` | 1/1 | Subschema describing `quantityUnit`; see its nested fields below. | `—` |
| `perishable` | `object` | 1/1 | Subschema describing `perishable`; see its nested fields below. | `—` |
| `storageRules` | `object` | 1/1 | Subschema describing `storageRules`; see its nested fields below. | `—` |

### `$.$defs.inventory.properties.storable`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `true` |

### `$.$defs.inventory.properties.quantityUnit`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `["string", "null"]` |

### `$.$defs.inventory.properties.perishable`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `["boolean", "null"]` |

### `$.$defs.inventory.properties.storageRules`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.resource`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id", "tag", "name"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.resource.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `tag` | `object` | 1/1 | Subschema describing `tag`; see its nested fields below. | `—` |
| `name` | `object` | 1/1 | Subschema describing `name`; see its nested fields below. | `—` |
| `description` | `object` | 1/1 | Subschema describing `description`; see its nested fields below. | `—` |
| `category` | `object` | 1/1 | Subschema describing `category`; see its nested fields below. | `—` |
| `stage` | `object` | 1/1 | Subschema describing `stage`; see its nested fields below. | `—` |
| `tags` | `object` | 1/1 | Subschema describing `tags`; see its nested fields below. | `—` |
| `inventory` | `object` | 1/1 | Subschema describing `inventory`; see its nested fields below. | `—` |
| `definitionStatus` | `object` | 1/1 | Subschema describing `definitionStatus`; see its nested fields below. | `—` |

### `$.$defs.resource.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.resource.properties.tag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |
| `pattern` | `string` | 1/1 | Regular expression constraining strings; not a global uniqueness guarantee. | `"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"` |

### `$.$defs.resource.properties.name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/localizedText"` |

### `$.$defs.resource.properties.description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/localizedText"` |

### `$.$defs.resource.properties.category`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.resource.properties.stage`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Explicit set of allowed JSON values. | `["raw", "intermediate", "processed"]` |

### `$.$defs.resource.properties.tags`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.$defs.resource.properties.tags.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.resource.properties.inventory`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/inventory"` |

### `$.$defs.resource.properties.definitionStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceBinding`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["sourceCollection", "sourceId", "resourceId"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.sourceBinding.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceCollection` | `object` | 1/1 | Subschema describing `sourceCollection`; see its nested fields below. | `—` |
| `sourceId` | `object` | 1/1 | Subschema describing `sourceId`; see its nested fields below. | `—` |
| `resourceId` | `object` | 1/1 | Subschema describing `resourceId`; see its nested fields below. | `—` |
| `acquisitionTag` | `object` | 1/1 | Subschema describing `acquisitionTag`; see its nested fields below. | `—` |
| `reviewStatus` | `object` | 1/1 | Subschema describing `reviewStatus`; see its nested fields below. | `—` |
| `quantityPerAction` | `object` | 1/1 | Subschema describing `quantityPerAction`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |
| `requiresProcessing` | `object` | 1/1 | Subschema describing `requiresProcessing`; see its nested fields below. | `—` |

### `$.$defs.sourceBinding.properties.sourceCollection`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Explicit set of allowed JSON values. | `["plantSpeciesCandidates", "animalSpeciesCandidates", "agriculturalCropCandidates"]` |

### `$.$defs.sourceBinding.properties.sourceId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceBinding.properties.resourceId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.sourceBinding.properties.acquisitionTag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceBinding.properties.reviewStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceBinding.properties.quantityPerAction`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.sourceBinding.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.$defs.sourceBinding.properties.requiresProcessing`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"boolean"` |

### `$.$defs.sourceTagMapping`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["sourceTag", "targetKind", "resourceIds"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.sourceTagMapping.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceTag` | `object` | 1/1 | Subschema describing `sourceTag`; see its nested fields below. | `—` |
| `targetKind` | `object` | 1/1 | Subschema describing `targetKind`; see its nested fields below. | `—` |
| `resourceIds` | `object` | 1/1 | Subschema describing `resourceIds`; see its nested fields below. | `—` |
| `resolutionStatus` | `object` | 1/1 | Subschema describing `resolutionStatus`; see its nested fields below. | `—` |
| `note` | `object` | 1/1 | Subschema describing `note`; see its nested fields below. | `—` |

### `$.$defs.sourceTagMapping.properties.sourceTag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceTagMapping.properties.targetKind`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Explicit set of allowed JSON values. | `["resource", "service", "unresolved_anatomical_alternative"]` |

### `$.$defs.sourceTagMapping.properties.resourceIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.$defs.sourceTagMapping.properties.resourceIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.sourceTagMapping.properties.resolutionStatus`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.sourceTagMapping.properties.note`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.processingLink`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["processTag", "inputResourceIds", "outputResourceIds"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.processingLink.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `processTag` | `object` | 1/1 | Subschema describing `processTag`; see its nested fields below. | `—` |
| `inputResourceIds` | `object` | 1/1 | Subschema describing `inputResourceIds`; see its nested fields below. | `—` |
| `outputResourceIds` | `object` | 1/1 | Subschema describing `outputResourceIds`; see its nested fields below. | `—` |
| `description` | `object` | 1/1 | Subschema describing `description`; see its nested fields below. | `—` |
| `requiredTechnologyIds` | `object` | 1/1 | Subschema describing `requiredTechnologyIds`; see its nested fields below. | `—` |
| `inputQuantities` | `object` | 1/1 | Subschema describing `inputQuantities`; see its nested fields below. | `—` |
| `outputQuantities` | `object` | 1/1 | Subschema describing `outputQuantities`; see its nested fields below. | `—` |
| `facilities` | `object` | 1/1 | Subschema describing `facilities`; see its nested fields below. | `—` |
| `byproducts` | `object` | 1/1 | Subschema describing `byproducts`; see its nested fields below. | `—` |
| `recipeId` | `object` | 1/1 | Subschema describing `recipeId`; see its nested fields below. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subschema describing `runtimeEnabled`; see its nested fields below. | `—` |

### `$.$defs.processingLink.properties.processTag`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.processingLink.properties.inputResourceIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.$defs.processingLink.properties.inputResourceIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.processingLink.properties.outputResourceIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"array"` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.$defs.processingLink.properties.outputResourceIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.processingLink.properties.description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/localizedText"` |

### `$.$defs.processingLink.properties.requiredTechnologyIds`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `["array", "null"]` |
| `items` | `object` | 1/1 | Schema applied to array elements. | `—` |

### `$.$defs.processingLink.properties.requiredTechnologyIds.items`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.processingLink.properties.inputQuantities`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.processingLink.properties.outputQuantities`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.processingLink.properties.facilities`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.processingLink.properties.byproducts`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"null"` |

### `$.$defs.processingLink.properties.recipeId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `["string", "null"]` |

### `$.$defs.processingLink.properties.runtimeEnabled`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.$defs.unresolvedSource`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["resourceId", "reason"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.unresolvedSource.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceId` | `object` | 1/1 | Subschema describing `resourceId`; see its nested fields below. | `—` |
| `reason` | `object` | 1/1 | Subschema describing `reason`; see its nested fields below. | `—` |

### `$.$defs.unresolvedSource.properties.resourceId`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Reference to a reusable subschema, not a game entity reference. | `"#/$defs/resourceId"` |

### `$.$defs.unresolvedSource.properties.reason`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.reviewIssue`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["id", "resolution"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.reviewIssue.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subschema describing `id`; see its nested fields below. | `—` |
| `resolution` | `object` | 1/1 | Subschema describing `resolution`; see its nested fields below. | `—` |

### `$.$defs.reviewIssue.properties.id`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.reviewIssue.properties.resolution`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["loadAsGameDefinitions", "unknownValues", "sourceBindings"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.runtimePolicy.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `object` | 1/1 | Subschema describing `loadAsGameDefinitions`; see its nested fields below. | `—` |
| `unknownValues` | `object` | 1/1 | Subschema describing `unknownValues`; see its nested fields below. | `—` |
| `sourceBindings` | `object` | 1/1 | Subschema describing `sourceBindings`; see its nested fields below. | `—` |
| `processingLinks` | `object` | 1/1 | Subschema describing `processingLinks`; see its nested fields below. | `—` |
| `services` | `object` | 1/1 | Subschema describing `services`; see its nested fields below. | `—` |
| `provenance` | `object` | 1/1 | Subschema describing `provenance`; see its nested fields below. | `—` |

### `$.$defs.runtimePolicy.properties.loadAsGameDefinitions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Exact allowed JSON value for the property. | `false` |

### `$.$defs.runtimePolicy.properties.unknownValues`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.runtimePolicy.properties.sourceBindings`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.runtimePolicy.properties.processingLinks`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.runtimePolicy.properties.services`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.runtimePolicy.properties.provenance`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"string"` |

### `$.$defs.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"object"` |
| `required` | `array<string>` | 1/1 | Property names required by this schema; presence in an example alone does not make a field required. | `["resourceCount", "sourceBindingCount", "processingLinkCount"]` |
| `properties` | `object` | 1/1 | Schemas for named properties; does not forbid other fields without additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Whether properties not declared by the object schema are allowed. | `false` |

### `$.$defs.summary.properties`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `resourceCount` | `object` | 1/1 | Subschema describing `resourceCount`; see its nested fields below. | `—` |
| `sourceBindingCount` | `object` | 1/1 | Subschema describing `sourceBindingCount`; see its nested fields below. | `—` |
| `processingLinkCount` | `object` | 1/1 | Subschema describing `processingLinkCount`; see its nested fields below. | `—` |
| `sourceTagMappingCount` | `object` | 1/1 | Subschema describing `sourceTagMappingCount`; see its nested fields below. | `—` |
| `geologicalSourceCount` | `object` | 1/1 | Subschema describing `geologicalSourceCount`; see its nested fields below. | `—` |
| `cropSourceCount` | `object` | 1/1 | Subschema describing `cropSourceCount`; see its nested fields below. | `—` |

### `$.$defs.summary.properties.resourceCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

### `$.$defs.summary.properties.sourceBindingCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

### `$.$defs.summary.properties.processingLinkCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

### `$.$defs.summary.properties.sourceTagMappingCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

### `$.$defs.summary.properties.geologicalSourceCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

### `$.$defs.summary.properties.cropSourceCount`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"integer"` |
| `minimum` | `integer` | 1/1 | Inclusive numeric lower bound. | `0` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evolve resource design guide",
  "description": "Structural contract for the resource guide. Does not validate cross-file references, scientific evidence, processing feasibility, quantities or gameplay balance.",
  "type": "object",
  "required": [
    "schemaVersion",
    "contentVersion",
    "kind",
    "status",
    "defaultLanguage",
    "supportedLanguages",
    "identityPolicy",
    "runtimePolicy",
    "resources",
    "sourceBindings",
    "sourceTagMappings",
    "processingLinks",
    "unresolvedSources",
    "reviewIssues",
    "summary"
  ],
  "properties": {
    "schemaVersion": {
      "const": "1.0.0"
    },
    "contentVersion": {
      "type": "string"
    },
    "kind": {
      "const": "resource_catalog_design_guide"
    },
    "status": {
      "type": "string"
    },
    "defaultLanguage": {
      "const": "en"
    },
    "supportedLanguages": {
      "const": [
        "en",
        "es"
      ]
    },
    "identityPolicy": {
      "type": "string"
    },
    "runtimePolicy": {
      "$ref": "#/$defs/runtimePolicy"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "sourceBindings": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sourceBinding"
      }
    },
    "sourceTagMappings": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sourceTagMapping"
      }
    },
    "processingLinks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/processingLink"
      }
    },
    "unresolvedSources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/unresolvedSource"
      }
    },
    "reviewIssues": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/reviewIssue"
      }
    },
    "summary": {
      "$ref": "#/$defs/summary"
    }
  },
  "additionalProperties": false,
  "$defs": {
    "localizedText": {
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
    "resourceId": {
      "type": "string",
      "pattern": "^RES#[0-9]{6}$",
      "not": {
        "pattern": "#000000$"
      }
    },
    "inventory": {
      "type": "object",
      "required": [
        "storable",
        "quantityUnit",
        "perishable",
        "storageRules"
      ],
      "properties": {
        "storable": {
          "const": true
        },
        "quantityUnit": {
          "type": [
            "string",
            "null"
          ]
        },
        "perishable": {
          "type": [
            "boolean",
            "null"
          ]
        },
        "storageRules": {
          "type": "null"
        }
      },
      "additionalProperties": false
    },
    "resource": {
      "type": "object",
      "required": [
        "id",
        "tag",
        "name",
        "description",
        "category",
        "stage",
        "tags",
        "inventory",
        "definitionStatus"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/resourceId"
        },
        "tag": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"
        },
        "name": {
          "$ref": "#/$defs/localizedText"
        },
        "description": {
          "$ref": "#/$defs/localizedText"
        },
        "category": {
          "type": "string"
        },
        "stage": {
          "enum": [
            "raw",
            "intermediate",
            "processed",
            "refined"
          ]
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inventory": {
          "$ref": "#/$defs/inventory"
        },
        "definitionStatus": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "sourceBinding": {
      "type": "object",
      "required": [
        "sourceCollection",
        "sourceId",
        "resourceId",
        "acquisitionTag",
        "reviewStatus",
        "quantityPerAction",
        "runtimeEnabled",
        "requiresProcessing"
      ],
      "properties": {
        "sourceCollection": {
          "enum": [
            "plantSpeciesCandidates",
            "animalSpeciesCandidates",
            "agriculturalCropCandidates",
            "geologicalResourceCandidates"
          ]
        },
        "sourceId": {
          "type": "string"
        },
        "resourceId": {
          "$ref": "#/$defs/resourceId"
        },
        "acquisitionTag": {
          "type": "string"
        },
        "reviewStatus": {
          "type": "string"
        },
        "quantityPerAction": {
          "type": "null"
        },
        "runtimeEnabled": {
          "const": false
        },
        "requiresProcessing": {
          "type": "boolean"
        }
      },
      "additionalProperties": false
    },
    "sourceTagMapping": {
      "type": "object",
      "required": [
        "sourceTag",
        "targetKind",
        "resourceIds",
        "resolutionStatus",
        "note"
      ],
      "properties": {
        "sourceTag": {
          "type": "string"
        },
        "targetKind": {
          "enum": [
            "resource",
            "service",
            "unresolved_anatomical_alternative"
          ]
        },
        "resourceIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/resourceId"
          }
        },
        "resolutionStatus": {
          "type": "string"
        },
        "note": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "processingLink": {
      "type": "object",
      "required": [
        "processTag",
        "inputResourceIds",
        "outputResourceIds",
        "description",
        "requiredTechnologyIds",
        "inputQuantities",
        "outputQuantities",
        "facilities",
        "byproducts",
        "recipeId",
        "runtimeEnabled"
      ],
      "properties": {
        "processTag": {
          "type": "string"
        },
        "inputResourceIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/resourceId"
          }
        },
        "outputResourceIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/resourceId"
          }
        },
        "description": {
          "$ref": "#/$defs/localizedText"
        },
        "requiredTechnologyIds": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "inputQuantities": {
          "type": "null"
        },
        "outputQuantities": {
          "type": "null"
        },
        "facilities": {
          "type": "null"
        },
        "byproducts": {
          "type": "null"
        },
        "recipeId": {
          "type": [
            "string",
            "null"
          ]
        },
        "runtimeEnabled": {
          "const": false
        }
      },
      "additionalProperties": false
    },
    "unresolvedSource": {
      "type": "object",
      "required": [
        "resourceId",
        "reason"
      ],
      "properties": {
        "resourceId": {
          "$ref": "#/$defs/resourceId"
        },
        "reason": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "reviewIssue": {
      "type": "object",
      "required": [
        "id",
        "resolution"
      ],
      "properties": {
        "id": {
          "type": "string"
        },
        "resolution": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "runtimePolicy": {
      "type": "object",
      "required": [
        "loadAsGameDefinitions",
        "unknownValues",
        "sourceBindings",
        "processingLinks",
        "services",
        "provenance"
      ],
      "properties": {
        "loadAsGameDefinitions": {
          "const": false
        },
        "unknownValues": {
          "type": "string"
        },
        "sourceBindings": {
          "type": "string"
        },
        "processingLinks": {
          "type": "string"
        },
        "services": {
          "type": "string"
        },
        "provenance": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "summary": {
      "type": "object",
      "required": [
        "resourceCount",
        "sourceBindingCount",
        "processingLinkCount",
        "sourceTagMappingCount",
        "geologicalSourceCount",
        "cropSourceCount"
      ],
      "properties": {
        "resourceCount": {
          "type": "integer",
          "minimum": 0
        },
        "sourceBindingCount": {
          "type": "integer",
          "minimum": 0
        },
        "processingLinkCount": {
          "type": "integer",
          "minimum": 0
        },
        "sourceTagMappingCount": {
          "type": "integer",
          "minimum": 0
        },
        "geologicalSourceCount": {
          "type": "integer",
          "minimum": 0
        },
        "cropSourceCount": {
          "type": "integer",
          "minimum": 0
        }
      },
      "additionalProperties": false
    }
  }
}
```
