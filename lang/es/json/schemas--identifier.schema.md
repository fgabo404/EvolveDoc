# `schemas/identifier.schema.json`

[JSON fuente](../../../schemas/identifier.schema.json) · [Index](../json-structures.md)

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
| `title` | `string` | 1/1 | Título del documento o esquema. | `"Future Evolve definition identity"` |
| `description` | `string` | 1/1 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `"Proposed future identifier envelope. Existing legacy catalogs are not migrated and do not conform to this envel…` |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"object"` |
| `required` | `array<string>` | 1/1 | Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo. | `["id", "tag"]` |
| `properties` | `object` | 1/1 | Esquemas por propiedad; no prohíbe campos extra sin additionalProperties. | `—` |

### `$.properties`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `object` | 1/1 | Subesquema que describe `id`; ver sus campos internos más abajo. | `—` |
| `tag` | `object` | 1/1 | Subesquema que describe `tag`; ver sus campos internos más abajo. | `—` |

### `$.properties.id`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^(BIO\|VAR\|REG\|TER\|SOL\|GEO\|PLT\|ANM\|FNG\|RES\|DEP\|DST\|TEC\|ITM\|RCP\|BLD\|IMP\|CAP\|EUR)#[0-9]{6}$"` |
| `not` | `object` | 1/1 | Subesquema que no debe cumplirse; aquí rechaza ID cero reservado. | `—` |

### `$.properties.id.not`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"#000000$"` |

### `$.properties.tag`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 1/1 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"string"` |
| `pattern` | `string` | 1/1 | Expresión regular para cadenas; no garantiza unicidad global. | `"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

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
