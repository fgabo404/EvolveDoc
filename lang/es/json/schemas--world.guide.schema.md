# `schemas/world.guide.schema.json`

[JSON fuente](../../../schemas/world.guide.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Título del documento o esquema. | `"world_catalog_design_guide envelope"` |
| `description` | `string` | 1/1 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `"Preliminary structural envelope only; not a full field-level or semantic schema."` |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["schemaVersion", "kind", "runtimePolicy"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `object` | 1/1 | Subesquema que describe `schemaVersion`; ver sus campos internos más abajo. | `—` |
| `kind` | `object` | 1/1 | Subesquema que describe `kind`; ver sus campos internos más abajo. | `—` |
| `runtimePolicy` | `object` | 1/1 | Subesquema que describe `runtimePolicy`; ver sus campos internos más abajo. | `—` |
| `biomes` | `object` | 1/1 | Subesquema que describe `biomes`; ver sus campos internos más abajo. | `—` |
| `regionalVariants` | `object` | 1/1 | Subesquema que describe `regionalVariants`; ver sus campos internos más abajo. | `—` |
| `resourceOccurrences` | `object` | 1/1 | Subesquema que describe `resourceOccurrences`; ver sus campos internos más abajo. | `—` |

### `$.properties.schemaVersion`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.kind`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `string` | 1/1 | Valor JSON exacto admitido para la propiedad. | `"world_catalog_design_guide"` |

### `$.properties.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["loadAsGameDefinitions"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties.runtimePolicy.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `object` | 1/1 | Subesquema que describe `loadAsGameDefinitions`; ver sus campos internos más abajo. | `—` |

### `$.properties.runtimePolicy.properties.loadAsGameDefinitions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `const` | `boolean` | 1/1 | Valor JSON exacto admitido para la propiedad. | `false` |

### `$.properties.biomes`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.biomes.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties.biomes.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |

### `$.properties.biomes.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.regionalVariants`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.regionalVariants.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties.regionalVariants.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |

### `$.properties.regionalVariants.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

### `$.properties.resourceOccurrences`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"array"` |
| `items` | `object` | 1/1 | Esquema aplicado a elementos de un arreglo. | `—` |

### `$.properties.resourceOccurrences.items`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties.resourceOccurrences.items.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |

### `$.properties.resourceOccurrences.items.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "world_catalog_design_guide envelope",
  "description": "Preliminary structural envelope only; not a full field-level or semantic schema.",
  "type": "object",
  "required": [
    "schemaVersion",
    "kind",
    "runtimePolicy",
    "biomes",
    "regionalVariants",
    "resourceOccurrences"
  ],
  "properties": {
    "schemaVersion": {
      "type": "string"
    },
    "kind": {
      "const": "world_catalog_design_guide"
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
    "biomes": {
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
    },
    "regionalVariants": {
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
    },
    "resourceOccurrences": {
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
