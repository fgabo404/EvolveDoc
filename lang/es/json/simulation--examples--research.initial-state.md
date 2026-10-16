# `simulation/examples/research.initial-state.json`

[JSON fuente](../../../simulation/examples/research.initial-state.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"0.1.0"` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"example_game_state"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"illustrative_fixture_not_a_save_contract"` |
| `turn` | `integer` | 1/1 | Turno mutable actual; cero es el estado inicial del ejemplo. | `0` |
| `speciesBindings` | `object` | 1/1 | Explicaciones de alias del ejemplo, no definiciones botánicas. | `—` |
| `civilizations` | `array<object>` | 1/1 | Estados independientes de civilizaciones del ejemplo. | `—` |

### `$.speciesBindings`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `wheat` | `string` | 1/1 | Alias ilustrativo del grupo trigo, no especie exacta resuelta. | `"Illustrative crop-group alias, not an exact botanical species."` |
| `maize` | `string` | 1/1 | Alias ilustrativo del grupo maíz, no especie exacta resuelta. | `"Illustrative crop-group alias, not a resolved native spawn definition."` |

### `$.civilizations[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 2/2 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"example_civilization_one"` |
| `discoveredSpeciesIds` | `array<string>` | 2/2 | Alias de especies/cultivos descubiertos por esta civilización. | `["wheat"]` |
| `accessibleMaterialSpeciesIds` | `array<string>` | 2/2 | Alias de especies/cultivos con material accesible a esta civilización. | `["wheat"]` |
| `research` | `array<object>` | 2/2 | Registros mutables de investigación, separados de la definición tecnológica. | `—` |

### `$.civilizations[].research[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 10/10 | Referencia a una definición tecnológica o importación externa declarada. | `"initial_sowing"` |
| `speciesId` | `null \| string` | 10/10 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"wheat"` |
| `started` | `boolean` | 10/10 | Indica si pasó condiciones iniciales y comenzó investigación. | `true` |
| `completed` | `boolean` | 10/10 | Indica si la investigación alcanzó su costo definido. | `true` |
| `points` | `integer` | 10/10 | Puntos mutables acumulados, limitados al costo de la definición. | `100` |
| `pointsPerTurn` | `integer` | 10/10 | Asignación del ejemplo por intento; no implementa presupuesto científico total. | `0` |
| `status` | `string` | 10/10 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"completed"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "0.1.0",
  "kind": "example_game_state",
  "status": "illustrative_fixture_not_a_save_contract",
  "turn": 0,
  "speciesBindings": {
    "wheat": "Illustrative crop-group alias, not an exact botanical species.",
    "maize": "Illustrative crop-group alias, not a resolved native spawn definition."
  },
  "civilizations": [
    {
      "id": "example_civilization_one",
      "discoveredSpeciesIds": [
        "wheat"
      ],
      "accessibleMaterialSpeciesIds": [
        "wheat"
      ],
      "research": [
        {
          "technologyId": "initial_sowing",
          "speciesId": null,
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "seed_handling",
          "speciesId": "wheat",
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "seed_handling",
          "speciesId": "maize",
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "species_cultivation",
          "speciesId": "wheat",
          "started": false,
          "completed": false,
          "points": 0,
          "pointsPerTurn": 40,
          "status": "pending"
        },
        {
          "technologyId": "species_cultivation",
          "speciesId": "maize",
          "started": false,
          "completed": false,
          "points": 0,
          "pointsPerTurn": 40,
          "status": "pending"
        }
      ]
    },
    {
      "id": "example_civilization_two",
      "discoveredSpeciesIds": [
        "maize"
      ],
      "accessibleMaterialSpeciesIds": [
        "maize"
      ],
      "research": [
        {
          "technologyId": "initial_sowing",
          "speciesId": null,
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "seed_handling",
          "speciesId": "wheat",
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "seed_handling",
          "speciesId": "maize",
          "started": true,
          "completed": true,
          "points": 100,
          "pointsPerTurn": 0,
          "status": "completed"
        },
        {
          "technologyId": "species_cultivation",
          "speciesId": "wheat",
          "started": false,
          "completed": false,
          "points": 0,
          "pointsPerTurn": 25,
          "status": "pending"
        },
        {
          "technologyId": "species_cultivation",
          "speciesId": "maize",
          "started": false,
          "completed": false,
          "points": 0,
          "pointsPerTurn": 25,
          "status": "pending"
        }
      ]
    }
  ]
}
```
