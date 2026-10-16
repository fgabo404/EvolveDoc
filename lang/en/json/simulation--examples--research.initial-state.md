# `simulation/examples/research.initial-state.json`

[Source JSON](../../../simulation/examples/research.initial-state.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"0.1.0"` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"example_game_state"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"illustrative_fixture_not_a_save_contract"` |
| `turn` | `integer` | 1/1 | Current mutable game turn; zero is the fixture's initial state. | `0` |
| `speciesBindings` | `object` | 1/1 | Explanations of fixture aliases, not botanical definitions. | `—` |
| `civilizations` | `array<object>` | 1/1 | Independent civilization state records in this example. | `—` |

### `$.speciesBindings`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `wheat` | `string` | 1/1 | Illustrative wheat crop-group alias, not a resolved exact species. | `"Illustrative crop-group alias, not an exact botanical species."` |
| `maize` | `string` | 1/1 | Illustrative maize crop-group alias, not a resolved exact species. | `"Illustrative crop-group alias, not a resolved native spawn definition."` |

### `$.civilizations[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 2/2 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"example_civilization_one"` |
| `discoveredSpeciesIds` | `array<string>` | 2/2 | Species/crop aliases already discovered by this civilization. | `["wheat"]` |
| `accessibleMaterialSpeciesIds` | `array<string>` | 2/2 | Species/crop aliases with material accessible to this civilization. | `["wheat"]` |
| `research` | `array<object>` | 2/2 | Mutable research instance records, separate from the technology definition. | `—` |

### `$.civilizations[].research[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 10/10 | Reference to a technology definition or declared external import. | `"initial_sowing"` |
| `speciesId` | `null \| string` | 10/10 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"wheat"` |
| `started` | `boolean` | 10/10 | Whether research has passed its initial gates and begun. | `true` |
| `completed` | `boolean` | 10/10 | Whether the research instance reached its defined cost. | `true` |
| `points` | `integer` | 10/10 | Accumulated mutable research points, capped at the definition cost. | `100` |
| `pointsPerTurn` | `integer` | 10/10 | Fixture allocation per research attempt; no civilization-wide budget allocator is implemented. | `0` |
| `status` | `string` | 10/10 | Maturity, review state or current example research status; read the containing object. | `"completed"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

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
