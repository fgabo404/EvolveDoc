# `schemas/biological.catalog.schema.json`

[JSON fuente](../../../schemas/biological.catalog.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Título del documento o esquema. | `"Evolve biological reference catalog"` |
| `description` | `string` | 1/1 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `"Full structural contract for optional scientific background catalog 1.1.0. Gameplay categories are defined in t…` |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["biologicalForms", "contentVersion", "defaultLanguage"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `biologicalForms` | `object` | 1/1 | Subesquema que describe `biologicalForms`; ver sus campos internos más abajo. | `—` |
| `contentVersion` | `object` | 1/1 | Subesquema que describe `contentVersion`; ver sus campos internos más abajo. | `—` |
| `defaultLanguage` | `object` | 1/1 | Subesquema que describe `defaultLanguage`; ver sus campos internos más abajo. | `—` |
| `evidenceSources` | `object` | 1/1 | Subesquema que describe `evidenceSources`; ver sus campos internos más abajo. | `—` |
| `excludedLineageRelations` | `object` | 1/1 | Subesquema que describe `excludedLineageRelations`; ver sus campos internos más abajo. | `—` |
| `kind` | `object` | 1/1 | Subesquema que describe `kind`; ver sus campos internos más abajo. | `—` |
| `lineageRelations` | `object` | 1/1 | Subesquema que describe `lineageRelations`; ver sus campos internos más abajo. | `—` |
| `reviewIssues` | `object` | 1/1 | Subesquema que describe `reviewIssues`; ver sus campos internos más abajo. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subesquema que describe `runtimePolicy`; ver sus campos internos más abajo. | `—` |
| `schemaVersion` | `object` | 1/1 | Subesquema que describe `schemaVersion`; ver sus campos internos más abajo. | `—` |
| `status` | `object` | 1/1 | Subesquema que describe `status`; ver sus campos internos más abajo. | `—` |
| `summary` | `object` | 1/1 | Subesquema que describe `summary`; ver sus campos internos más abajo. | `—` |
| `supportedLanguages` | `object` | 1/1 | Subesquema que describe `supportedLanguages`; ver sus campos internos más abajo. | `—` |
| `taxa` | `object` | 1/1 | Subesquema que describe `taxa`; ver sus campos internos más abajo. | `—` |

### `$.properties.biologicalForms`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.biologicalForms.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["evidenceSourceKeys", "formKind", "id"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.biologicalForms.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `evidenceSourceKeys` | `object` | 1/1 | Subesquema que describe `evidenceSourceKeys`; ver sus campos internos más abajo. | `—` |
| `formKind` | `object` | 1/1 | Subesquema que describe `formKind`; ver sus campos internos más abajo. | `—` |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `literatureName` | `object` | 1/1 | Subesquema que describe `literatureName`; ver sus campos internos más abajo. | `—` |
| `name` | `object` | 1/1 | Subesquema que describe `name`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |
| `status` | `object` | 1/1 | Subesquema que describe `status`; ver sus campos internos más abajo. | `—` |
| `tag` | `object` | 1/1 | Subesquema que describe `tag`; ver sus campos internos más abajo. | `—` |
| `taxonId` | `object` | 1/1 | Subesquema que describe `taxonId`; ver sus campos internos más abajo. | `—` |

### `$.properties.biologicalForms.items.properties.evidenceSourceKeys`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.biologicalForms.items.properties.evidenceSourceKeys.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.biologicalForms.items.properties.formKind`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.biologicalForms.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^FRM#[0-9]{6}$"` |

### `$.properties.biologicalForms.items.properties.literatureName`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.biologicalForms.items.properties.name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.biologicalForms.items.properties.name.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subesquema que describe `en`; ver sus campos internos más abajo. | `—` |
| `es` | `object` | 1/1 | Subesquema que describe `es`; ver sus campos internos más abajo. | `—` |

### `$.properties.biologicalForms.items.properties.name.properties.en`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.properties.biologicalForms.items.properties.name.properties.es`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.properties.biologicalForms.items.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.properties.biologicalForms.items.properties.status`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.biologicalForms.items.properties.tag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.biologicalForms.items.properties.taxonId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.contentVersion`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.defaultLanguage`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.evidenceSources`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.evidenceSources.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["checkedOn", "sourceKey", "supports"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.evidenceSources.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `checkedOn` | `object` | 1/1 | Subesquema que describe `checkedOn`; ver sus campos internos más abajo. | `—` |
| `sourceKey` | `object` | 1/1 | Subesquema que describe `sourceKey`; ver sus campos internos más abajo. | `—` |
| `supports` | `object` | 1/1 | Subesquema que describe `supports`; ver sus campos internos más abajo. | `—` |
| `title` | `object` | 1/1 | Subesquema que describe `title`; ver sus campos internos más abajo. | `—` |
| `url` | `object` | 1/1 | Subesquema que describe `url`; ver sus campos internos más abajo. | `—` |

### `$.properties.evidenceSources.items.properties.checkedOn`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.evidenceSources.items.properties.sourceKey`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.evidenceSources.items.properties.supports`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.evidenceSources.items.properties.title`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.evidenceSources.items.properties.url`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.excludedLineageRelations.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["childFormId", "evidenceSourceKeys", "parentFormId"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.excludedLineageRelations.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `childFormId` | `object` | 1/1 | Subesquema que describe `childFormId`; ver sus campos internos más abajo. | `—` |
| `evidenceSourceKeys` | `object` | 1/1 | Subesquema que describe `evidenceSourceKeys`; ver sus campos internos más abajo. | `—` |
| `parentFormId` | `object` | 1/1 | Subesquema que describe `parentFormId`; ver sus campos internos más abajo. | `—` |
| `reason` | `object` | 1/1 | Subesquema que describe `reason`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |

### `$.properties.excludedLineageRelations.items.properties.childFormId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.evidenceSourceKeys`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.excludedLineageRelations.items.properties.evidenceSourceKeys.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.parentFormId`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.reason`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["en", "es"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subesquema que describe `en`; ver sus campos internos más abajo. | `—` |
| `es` | `object` | 1/1 | Subesquema que describe `es`; ver sus campos internos más abajo. | `—` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties.en`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.reason.properties.es`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.excludedLineageRelations.items.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |

### `$.properties.kind`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.lineageRelations.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["childFormIds", "description", "evidenceSourceKeys"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.lineageRelations.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `childFormIds` | `object` | 1/1 | Subesquema que describe `childFormIds`; ver sus campos internos más abajo. | `—` |
| `description` | `object` | 1/1 | Subesquema que describe `description`; ver sus campos internos más abajo. | `—` |
| `evidenceSourceKeys` | `object` | 1/1 | Subesquema que describe `evidenceSourceKeys`; ver sus campos internos más abajo. | `—` |
| `exactAncestralPopulationResolved` | `object` | 1/1 | Subesquema que describe `exactAncestralPopulationResolved`; ver sus campos internos más abajo. | `—` |
| `parentFormIds` | `object` | 1/1 | Subesquema que describe `parentFormIds`; ver sus campos internos más abajo. | `—` |
| `relationType` | `object` | 1/1 | Subesquema que describe `relationType`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |
| `supportLevel` | `object` | 1/1 | Subesquema que describe `supportLevel`; ver sus campos internos más abajo. | `—` |

### `$.properties.lineageRelations.items.properties.childFormIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.lineageRelations.items.properties.childFormIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["en", "es"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.lineageRelations.items.properties.description.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subesquema que describe `en`; ver sus campos internos más abajo. | `—` |
| `es` | `object` | 1/1 | Subesquema que describe `es`; ver sus campos internos más abajo. | `—` |

### `$.properties.lineageRelations.items.properties.description.properties.en`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.description.properties.es`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.evidenceSourceKeys`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.lineageRelations.items.properties.evidenceSourceKeys.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.exactAncestralPopulationResolved`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |

### `$.properties.lineageRelations.items.properties.parentFormIds`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.lineageRelations.items.properties.parentFormIds.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.relationType`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.lineageRelations.items.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |

### `$.properties.lineageRelations.items.properties.supportLevel`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.reviewIssues`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.reviewIssues.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id", "resolution"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.reviewIssues.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `resolution` | `object` | 1/1 | Subesquema que describe `resolution`; ver sus campos internos más abajo. | `—` |

### `$.properties.reviewIssues.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.reviewIssues.items.properties.resolution`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["floraClassification", "identityPolicy", "lineagePolicy"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.runtimePolicy.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `floraClassification` | `object` | 1/1 | Subesquema que describe `floraClassification`; ver sus campos internos más abajo. | `—` |
| `identityPolicy` | `object` | 1/1 | Subesquema que describe `identityPolicy`; ver sus campos internos más abajo. | `—` |
| `lineagePolicy` | `object` | 1/1 | Subesquema que describe `lineagePolicy`; ver sus campos internos más abajo. | `—` |
| `loadAsGameDefinitions` | `object` | 1/1 | Subesquema que describe `loadAsGameDefinitions`; ver sus campos internos más abajo. | `—` |
| `resourceInheritance` | `object` | 1/1 | Subesquema que describe `resourceInheritance`; ver sus campos internos más abajo. | `—` |
| `sourceInterpretation` | `object` | 1/1 | Subesquema que describe `sourceInterpretation`; ver sus campos internos más abajo. | `—` |
| `unknownValues` | `object` | 1/1 | Subesquema que describe `unknownValues`; ver sus campos internos más abajo. | `—` |
| `varietyPolicy` | `object` | 1/1 | Subesquema que describe `varietyPolicy`; ver sus campos internos más abajo. | `—` |
| `gameplayIdentity` | `object` | 1/1 | Subesquema que describe `gameplayIdentity`; ver sus campos internos más abajo. | `—` |

### `$.properties.runtimePolicy.properties.floraClassification`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.identityPolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.lineagePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.loadAsGameDefinitions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.properties.runtimePolicy.properties.resourceInheritance`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.sourceInterpretation`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.unknownValues`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.varietyPolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.runtimePolicy.properties.gameplayIdentity`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.schemaVersion`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.status`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["biologicalFormCount", "cropCandidateCount", "excludedLineageRelationCount"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.summary.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `biologicalFormCount` | `object` | 1/1 | Subesquema que describe `biologicalFormCount`; ver sus campos internos más abajo. | `—` |
| `cropCandidateCount` | `object` | 1/1 | Subesquema que describe `cropCandidateCount`; ver sus campos internos más abajo. | `—` |
| `excludedLineageRelationCount` | `object` | 1/1 | Subesquema que describe `excludedLineageRelationCount`; ver sus campos internos más abajo. | `—` |
| `lineageRelationCount` | `object` | 1/1 | Subesquema que describe `lineageRelationCount`; ver sus campos internos más abajo. | `—` |
| `sourceCandidateCount` | `object` | 1/1 | Subesquema que describe `sourceCandidateCount`; ver sus campos internos más abajo. | `—` |
| `taxonCount` | `object` | 1/1 | Subesquema que describe `taxonCount`; ver sus campos internos más abajo. | `—` |

### `$.properties.summary.properties.biologicalFormCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.summary.properties.cropCandidateCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.summary.properties.excludedLineageRelationCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.summary.properties.lineageRelationCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.summary.properties.sourceCandidateCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.summary.properties.taxonCount`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.supportedLanguages`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.supportedLanguages.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.taxa.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id", "name", "nativeRangeReviewStatus"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.taxa.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `name` | `object` | 1/1 | Subesquema que describe `name`; ver sus campos internos más abajo. | `—` |
| `nativeRangeReviewStatus` | `object` | 1/1 | Subesquema que describe `nativeRangeReviewStatus`; ver sus campos internos más abajo. | `—` |
| `organismGroup` | `object` | 1/1 | Subesquema que describe `organismGroup`; ver sus campos internos más abajo. | `—` |
| `reviewStatus` | `object` | 1/1 | Subesquema que describe `reviewStatus`; ver sus campos internos más abajo. | `—` |
| `runtimeEnabled` | `object` | 1/1 | Subesquema que describe `runtimeEnabled`; ver sus campos internos más abajo. | `—` |
| `scientificName` | `object` | 1/1 | Subesquema que describe `scientificName`; ver sus campos internos más abajo. | `—` |
| `tag` | `object` | 1/1 | Subesquema que describe `tag`; ver sus campos internos más abajo. | `—` |
| `taxonRank` | `object` | 1/1 | Subesquema que describe `taxonRank`; ver sus campos internos más abajo. | `—` |
| `taxonomy` | `object` | 1/1 | Subesquema que describe `taxonomy`; ver sus campos internos más abajo. | `—` |

### `$.properties.taxa.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^(PLT\|ANM\|ALG\|FNG)#[0-9]{6}$"` |

### `$.properties.taxa.items.properties.name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["en", "es"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.taxa.items.properties.name.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `object` | 1/1 | Subesquema que describe `en`; ver sus campos internos más abajo. | `—` |
| `es` | `object` | 1/1 | Subesquema que describe `es`; ver sus campos internos más abajo. | `—` |

### `$.properties.taxa.items.properties.name.properties.en`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.properties.taxa.items.properties.name.properties.es`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `minLength` | `integer` | 1/1 | Longitud mínima de una cadena. | `1` |

### `$.properties.taxa.items.properties.nativeRangeReviewStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.organismGroup`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.reviewStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.runtimeEnabled`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"boolean"` |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.properties.taxa.items.properties.scientificName`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.tag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonRank`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `enum` | `array<string>` | 1/1 | Conjunto explícito de valores JSON admitidos. | `["SPECIES", "SUBSPECIES", "VARIETY"]` |

### `$.properties.taxa.items.properties.taxonomy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["family", "genus", "kingdom"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.taxa.items.properties.taxonomy.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `family` | `object` | 1/1 | Subesquema que describe `family`; ver sus campos internos más abajo. | `—` |
| `genus` | `object` | 1/1 | Subesquema que describe `genus`; ver sus campos internos más abajo. | `—` |
| `kingdom` | `object` | 1/1 | Subesquema que describe `kingdom`; ver sus campos internos más abajo. | `—` |
| `matchEvidence` | `object` | 1/1 | Subesquema que describe `matchEvidence`; ver sus campos internos más abajo. | `—` |
| `provider` | `object` | 1/1 | Subesquema que describe `provider`; ver sus campos internos más abajo. | `—` |
| `providerTaxonKey` | `object` | 1/1 | Subesquema que describe `providerTaxonKey`; ver sus campos internos más abajo. | `—` |
| `referenceUrl` | `object` | 1/1 | Subesquema que describe `referenceUrl`; ver sus campos internos más abajo. | `—` |
| `taxonomicStatus` | `object` | 1/1 | Subesquema que describe `taxonomicStatus`; ver sus campos internos más abajo. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.family`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.genus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.kingdom`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["checkedOn", "confidence", "matchStatus"]` |
| `additionalProperties` | `boolean` | 1/1 | Indica si admite propiedades no declaradas en el esquema del objeto. | `false` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `checkedOn` | `object` | 1/1 | Subesquema que describe `checkedOn`; ver sus campos internos más abajo. | `—` |
| `confidence` | `object` | 1/1 | Subesquema que describe `confidence`; ver sus campos internos más abajo. | `—` |
| `matchStatus` | `object` | 1/1 | Subesquema que describe `matchStatus`; ver sus campos internos más abajo. | `—` |
| `matchType` | `object` | 1/1 | Subesquema que describe `matchType`; ver sus campos internos más abajo. | `—` |
| `matchedScientificName` | `object` | 1/1 | Subesquema que describe `matchedScientificName`; ver sus campos internos más abajo. | `—` |
| `queriedName` | `object` | 1/1 | Subesquema que describe `queriedName`; ver sus campos internos más abajo. | `—` |
| `requestUrl` | `object` | 1/1 | Subesquema que describe `requestUrl`; ver sus campos internos más abajo. | `—` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.checkedOn`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.confidence`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"integer"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchType`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.matchedScientificName`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.queriedName`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.matchEvidence.items.properties.requestUrl`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.provider`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.providerTaxonKey`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.referenceUrl`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.taxa.items.properties.taxonomy.properties.taxonomicStatus`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

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
