# `schemas/resource.guide.schema.json`

[JSON fuente](../../../schemas/resource.guide.schema.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

Estas son palabras de JSON Schema, no campos del juego. El esquema permite propiedades adicionales salvo restricción explícita. Esta referencia describe el archivo de esquema, sin convertir su validación limitada en un contrato completo del dominio.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$schema` | `string` | 1/1 | URI del dialecto JSON Schema; no referencia a datos del juego. | `"https://json-schema.org/draft/2020-12/schema"` |
| `title` | `string` | 1/1 | Título del documento o esquema. | `"Evolve resource design guide"` |
| `description` | `string` | 1/1 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `"Structural contract for the resource guide. Does not validate cross-file references, scientific evidence, proce…` |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["schemaVersion", "contentVersion", "kind"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |
| `$defs` | `object` | 1/1 | Subesquemas reutilizables con nombre dentro de este esquema. | `—` |

### `$.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `object` | 1/1 | Subesquema que describe `schemaVersion`; ver sus campos internos más abajo. | `—` |
| `contentVersion` | `object` | 1/1 | Subesquema que describe `contentVersion`; ver sus campos internos más abajo. | `—` |
| `kind` | `object` | 1/1 | Subesquema que describe `kind`; ver sus campos internos más abajo. | `—` |
| `status` | `object` | 1/1 | Subesquema que describe `status`; ver sus campos internos más abajo. | `—` |
| `defaultLanguage` | `object` | 1/1 | Subesquema que describe `defaultLanguage`; ver sus campos internos más abajo. | `—` |
| `supportedLanguages` | `object` | 1/1 | Subesquema que describe `supportedLanguages`; ver sus campos internos más abajo. | `—` |
| `identityPolicy` | `object` | 1/1 | Subesquema que describe `identityPolicy`; ver sus campos internos más abajo. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subesquema que describe `runtimePolicy`; ver sus campos internos más abajo. | `—` |
| `resources` | `object` | 1/1 | Subesquema que describe `resources`; ver sus campos internos más abajo. | `—` |
| `sourceBindings` | `object` | 1/1 | Subesquema que describe `sourceBindings`; ver sus campos internos más abajo. | `—` |
| `sourceTagMappings` | `object` | 1/1 | Subesquema que describe `sourceTagMappings`; ver sus campos internos más abajo. | `—` |
| `processingLinks` | `object` | 1/1 | Subesquema que describe `processingLinks`; ver sus campos internos más abajo. | `—` |
| `unresolvedSources` | `object` | 1/1 | Subesquema que describe `unresolvedSources`; ver sus campos internos más abajo. | `—` |
| `reviewIssues` | `object` | 1/1 | Subesquema que describe `reviewIssues`; ver sus campos internos más abajo. | `—` |
| `summary` | `object` | 1/1 | Subesquema que describe `summary`; ver sus campos internos más abajo. | `—` |

### `$.properties.schemaVersion`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Valor JSON exacto admitido para la propiedad. | `"1.0.0"` |

### `$.properties.contentVersion`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.kind`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Valor JSON exacto admitido para la propiedad. | `"resource_catalog_design_guide"` |

### `$.properties.status`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.defaultLanguage`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Valor JSON exacto admitido para la propiedad. | `"en"` |

### `$.properties.supportedLanguages`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `array<string>` | 1/1 | Valor JSON exacto admitido para la propiedad. | `["en", "es"]` |

### `$.properties.identityPolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/runtimePolicy"` |

### `$.properties.resources`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.resources.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resource"` |

### `$.properties.sourceBindings`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.sourceBindings.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/sourceBinding"` |

### `$.properties.sourceTagMappings`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.sourceTagMappings.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/sourceTagMapping"` |

### `$.properties.processingLinks`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.processingLinks.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/processingLink"` |

### `$.properties.unresolvedSources`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.unresolvedSources.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/unresolvedSource"` |

### `$.properties.reviewIssues`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.reviewIssues.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/reviewIssue"` |

### `$.properties.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/summary"` |

### `$.$defs`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `localizedText` | `object` | 1/1 | Subesquema que describe `localizedText`; ver sus campos internos más abajo. | `—` |
| `resourceId` | `object` | 1/1 | Subesquema que describe `resourceId`; ver sus campos internos más abajo. | `—` |
| `inventory` | `object` | 1/1 | Subesquema que describe `inventory`; ver sus campos internos más abajo. | `—` |
| `resource` | `object` | 1/1 | Subesquema que describe `resource`; ver sus campos internos más abajo. | `—` |
| `sourceBinding` | `object` | 1/1 | Subesquema que describe `sourceBinding`; ver sus campos internos más abajo. | `—` |
| `sourceTagMapping` | `object` | 1/1 | Subesquema que describe `sourceTagMapping`; ver sus campos internos más abajo. | `—` |
| `processingLink` | `object` | 1/1 | Subesquema que describe `processingLink`; ver sus campos internos más abajo. | `—` |
| `unresolvedSource` | `object` | 1/1 | Subesquema que describe `unresolvedSource`; ver sus campos internos más abajo. | `—` |
| `reviewIssue` | `object` | 1/1 | Subesquema que describe `reviewIssue`; ver sus campos internos más abajo. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subesquema que describe `runtimePolicy`; ver sus campos internos más abajo. | `—` |
| `summary` | `object` | 1/1 | Subesquema que describe `summary`; ver sus campos internos más abajo. | `—` |

### `$.$defs.localizedText`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.localizedText.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subesquema que describe `en`; ver sus campos internos más abajo. | `—` |
| `es` | `object` | 1/1 | Subesquema que describe `es`; ver sus campos internos más abajo. | `—` |

### `$.$defs.localizedText.properties.en`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.$defs.localizedText.properties.es`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.$defs.resourceId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^RES#[0-9]{6}$"` |
| `not` | `object` | 1/1 | Subesquema que no debe cumplirse; aquí rechaza ID cero reservado. | `—` |

### `$.$defs.resourceId.not`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"#000000$"` |

### `$.$defs.inventory`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["storable", "quantityUnit", "perishable"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.inventory.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `storable` | `object` | 1/1 | Subesquema que describe `storable`; ver sus campos internos más abajo. | `—` |
| `quantityUnit` | `object` | 1/1 | Subesquema que describe `quantityUnit`; ver sus campos internos más abajo. | `—` |
| `perishable` | `object` | 1/1 | Subesquema que describe `perishable`; ver sus campos internos más abajo. | `—` |
| `storageRules` | `object` | 1/1 | Subesquema que describe `storageRules`; ver sus campos internos más abajo. | `—` |

### `$.$defs.inventory.properties.storable`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `true` |

### `$.$defs.inventory.properties.quantityUnit`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `["string", "null"]` |

### `$.$defs.inventory.properties.perishable`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `["boolean", "null"]` |

### `$.$defs.inventory.properties.storageRules`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.resource`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id", "tag", "name"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.resource.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `tag` | `object` | 1/1 | Subesquema que describe `tag`; ver sus campos internos más abajo. | `—` |
| `name` | `object` | 1/1 | Subesquema que describe `name`; ver sus campos internos más abajo. | `—` |
| `description` | `object` | 1/1 | Subesquema que describe `description`; ver sus campos internos más abajo. | `—` |
| `category` | `object` | 1/1 | Subesquema que describe `category`; ver sus campos internos más abajo. | `—` |
| `stage` | `object` | 1/1 | Subesquema que describe `stage`; ver sus campos internos más abajo. | `—` |
| `tags` | `object` | 1/1 | Subesquema que describe `tags`; ver sus campos internos más abajo. | `—` |
| `inventory` | `object` | 1/1 | Subesquema que describe `inventory`; ver sus campos internos más abajo. | `—` |
| `definitionStatus` | `object` | 1/1 | Subesquema que describe `definitionStatus`; ver sus campos internos más abajo. | `—` |

### `$.$defs.resource.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.resource.properties.tag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"` |

### `$.$defs.resource.properties.name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/localizedText"` |

### `$.$defs.resource.properties.description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/localizedText"` |

### `$.$defs.resource.properties.category`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.resource.properties.stage`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Conjunto explícito de valores JSON admitidos. | `["raw", "intermediate", "processed"]` |

### `$.$defs.resource.properties.tags`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.$defs.resource.properties.tags.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.resource.properties.inventory`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/inventory"` |

### `$.$defs.resource.properties.definitionStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceBinding`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["sourceCollection", "sourceId", "resourceId"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.sourceBinding.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `sourceCollection` | `object` | 1/1 | Subesquema que describe `sourceCollection`; ver sus campos internos más abajo. | `—` |
| `sourceId` | `object` | 1/1 | Subesquema que describe `sourceId`; ver sus campos internos más abajo. | `—` |
| `resourceId` | `object` | 1/1 | Subesquema que describe `resourceId`; ver sus campos internos más abajo. | `—` |
| `acquisitionTag` | `object` | 1/1 | Subesquema que describe `acquisitionTag`; ver sus campos internos más abajo. | `—` |
| `reviewStatus` | `object` | 1/1 | Subesquema que describe `reviewStatus`; ver sus campos internos más abajo. | `—` |
| `quantityPerAction` | `object` | 1/1 | Subesquema que describe `quantityPerAction`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |
| `requiresProcessing` | `object` | 1/1 | Subesquema que describe `requiresProcessing`; ver sus campos internos más abajo. | `—` |

### `$.$defs.sourceBinding.properties.sourceCollection`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Conjunto explícito de valores JSON admitidos. | `["plantSpeciesCandidates", "animalSpeciesCandidates", "agriculturalCropCandidates"]` |

### `$.$defs.sourceBinding.properties.sourceId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceBinding.properties.resourceId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.sourceBinding.properties.acquisitionTag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceBinding.properties.reviewStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceBinding.properties.quantityPerAction`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.sourceBinding.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.$defs.sourceBinding.properties.requiresProcessing`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |

### `$.$defs.sourceTagMapping`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["sourceTag", "targetKind", "resourceIds"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.sourceTagMapping.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `sourceTag` | `object` | 1/1 | Subesquema que describe `sourceTag`; ver sus campos internos más abajo. | `—` |
| `targetKind` | `object` | 1/1 | Subesquema que describe `targetKind`; ver sus campos internos más abajo. | `—` |
| `resourceIds` | `object` | 1/1 | Subesquema que describe `resourceIds`; ver sus campos internos más abajo. | `—` |
| `resolutionStatus` | `object` | 1/1 | Subesquema que describe `resolutionStatus`; ver sus campos internos más abajo. | `—` |
| `note` | `object` | 1/1 | Subesquema que describe `note`; ver sus campos internos más abajo. | `—` |

### `$.$defs.sourceTagMapping.properties.sourceTag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceTagMapping.properties.targetKind`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `enum` | `array<string>` | 1/1 | Conjunto explícito de valores JSON admitidos. | `["resource", "service", "unresolved_anatomical_alternative"]` |

### `$.$defs.sourceTagMapping.properties.resourceIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.$defs.sourceTagMapping.properties.resourceIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.sourceTagMapping.properties.resolutionStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.sourceTagMapping.properties.note`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.processingLink`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["processTag", "inputResourceIds", "outputResourceIds"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.processingLink.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `processTag` | `object` | 1/1 | Subesquema que describe `processTag`; ver sus campos internos más abajo. | `—` |
| `inputResourceIds` | `object` | 1/1 | Subesquema que describe `inputResourceIds`; ver sus campos internos más abajo. | `—` |
| `outputResourceIds` | `object` | 1/1 | Subesquema que describe `outputResourceIds`; ver sus campos internos más abajo. | `—` |
| `description` | `object` | 1/1 | Subesquema que describe `description`; ver sus campos internos más abajo. | `—` |
| `requiredTechnologyIds` | `object` | 1/1 | Subesquema que describe `requiredTechnologyIds`; ver sus campos internos más abajo. | `—` |
| `inputQuantities` | `object` | 1/1 | Subesquema que describe `inputQuantities`; ver sus campos internos más abajo. | `—` |
| `outputQuantities` | `object` | 1/1 | Subesquema que describe `outputQuantities`; ver sus campos internos más abajo. | `—` |
| `facilities` | `object` | 1/1 | Subesquema que describe `facilities`; ver sus campos internos más abajo. | `—` |
| `byproducts` | `object` | 1/1 | Subesquema que describe `byproducts`; ver sus campos internos más abajo. | `—` |
| `recipeId` | `object` | 1/1 | Subesquema que describe `recipeId`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |

### `$.$defs.processingLink.properties.processTag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.processingLink.properties.inputResourceIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.$defs.processingLink.properties.inputResourceIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.processingLink.properties.outputResourceIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.$defs.processingLink.properties.outputResourceIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.processingLink.properties.description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/localizedText"` |

### `$.$defs.processingLink.properties.requiredTechnologyIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `["array", "null"]` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.$defs.processingLink.properties.requiredTechnologyIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.processingLink.properties.inputQuantities`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.processingLink.properties.outputQuantities`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.processingLink.properties.facilities`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.processingLink.properties.byproducts`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"null"` |

### `$.$defs.processingLink.properties.recipeId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `array<string>` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `["string", "null"]` |

### `$.$defs.processingLink.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.$defs.unresolvedSource`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["resourceId", "reason"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.unresolvedSource.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceId` | `object` | 1/1 | Subesquema que describe `resourceId`; ver sus campos internos más abajo. | `—` |
| `reason` | `object` | 1/1 | Subesquema que describe `reason`; ver sus campos internos más abajo. | `—` |

### `$.$defs.unresolvedSource.properties.resourceId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `$ref` | `string` | 1/1 | Referencia a un subesquema reutilizable, no a una entidad del juego. | `"#/$defs/resourceId"` |

### `$.$defs.unresolvedSource.properties.reason`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.reviewIssue`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id", "resolution"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.reviewIssue.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `resolution` | `object` | 1/1 | Subesquema que describe `resolution`; ver sus campos internos más abajo. | `—` |

### `$.$defs.reviewIssue.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.reviewIssue.properties.resolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["loadAsGameDefinitions", "unknownValues", "sourceBindings"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.runtimePolicy.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `object` | 1/1 | Subesquema que describe `loadAsGameDefinitions`; ver sus campos internos más abajo. | `—` |
| `unknownValues` | `object` | 1/1 | Subesquema que describe `unknownValues`; ver sus campos internos más abajo. | `—` |
| `sourceBindings` | `object` | 1/1 | Subesquema que describe `sourceBindings`; ver sus campos internos más abajo. | `—` |
| `processingLinks` | `object` | 1/1 | Subesquema que describe `processingLinks`; ver sus campos internos más abajo. | `—` |
| `services` | `object` | 1/1 | Subesquema que describe `services`; ver sus campos internos más abajo. | `—` |
| `provenance` | `object` | 1/1 | Subesquema que describe `provenance`; ver sus campos internos más abajo. | `—` |

### `$.$defs.runtimePolicy.properties.loadAsGameDefinitions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.$defs.runtimePolicy.properties.unknownValues`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.runtimePolicy.properties.sourceBindings`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.runtimePolicy.properties.processingLinks`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.runtimePolicy.properties.services`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.runtimePolicy.properties.provenance`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.$defs.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["resourceCount", "sourceBindingCount", "processingLinkCount"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.$defs.summary.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `resourceCount` | `object` | 1/1 | Subesquema que describe `resourceCount`; ver sus campos internos más abajo. | `—` |
| `sourceBindingCount` | `object` | 1/1 | Subesquema que describe `sourceBindingCount`; ver sus campos internos más abajo. | `—` |
| `processingLinkCount` | `object` | 1/1 | Subesquema que describe `processingLinkCount`; ver sus campos internos más abajo. | `—` |
| `sourceTagMappingCount` | `object` | 1/1 | Subesquema que describe `sourceTagMappingCount`; ver sus campos internos más abajo. | `—` |
| `geologicalSourceCount` | `object` | 1/1 | Subesquema que describe `geologicalSourceCount`; ver sus campos internos más abajo. | `—` |
| `cropSourceCount` | `object` | 1/1 | Subesquema que describe `cropSourceCount`; ver sus campos internos más abajo. | `—` |

### `$.$defs.summary.properties.resourceCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

### `$.$defs.summary.properties.sourceBindingCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

### `$.$defs.summary.properties.processingLinkCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

### `$.$defs.summary.properties.sourceTagMappingCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

### `$.$defs.summary.properties.geologicalSourceCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

### `$.$defs.summary.properties.cropSourceCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |
| `minimum` | `integer` | 1/1 | Límite numérico inferior inclusivo. | `0` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

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
