# World — Complete reference diagrams

[Diagram index](../../lang/en/catalog-diagrams.md) · [English](DIAGRAMS.md) · [Español](DIAGRAMS.es.md)

[JSON](world.catalog.guide.json) · [Complete JSON structure](../../lang/en/json-structures.md)

Every catalog record is included. Several small diagrams in this file keep the reference readable. Arrows represent documented links, not yield, guaranteed presence or inferred evolution. Existing IDs are preserved.

## All biomes and variants

Counts describe source listings, not generated populations or deposits. Exact native distribution and spawn probabilities remain unresolved.

### Tropical Forest / `tropical_forest`

```mermaid
flowchart LR
    biome["Tropical Forest / tropical_forest"]
    v0["American / tropical_forest_american"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["African / tropical_forest_african"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Asian / tropical_forest_asian"]
    v2 -->|biomeId| biome
    o2_0["animal: 7 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 7 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Oceanian / tropical_forest_oceanian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Temperate Forest / `temperate_forest`

```mermaid
flowchart LR
    biome["Temperate Forest / temperate_forest"]
    v0["Eurasian / temperate_forest_eurasian"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["American / temperate_forest_american"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["South African and Australian / temperate_forest_south_african_and_australian"]
    v2 -->|biomeId| biome
    o2_0["animal: 7 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 7 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Boreal / temperate_forest_boreal"]
    v3 -->|biomeId| biome
    o3_0["animal: 7 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 7 source occurrences"]
    o3_2 -->|variantId| v3
```

### Tundra / `tundra`

```mermaid
flowchart LR
    biome["Tundra / tundra"]
    v0["North American and Greenland / tundra_north_american_and_greenland"]
    v0 -->|biomeId| biome
    o0_0["animal: 5 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Eurasian / tundra_eurasian"]
    v1 -->|biomeId| biome
    o1_0["animal: 5 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 5 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Subantarctic / tundra_subantarctic"]
    v2 -->|biomeId| biome
    o2_0["animal: 3 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 7 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
```

### Savanna and Grasslands / `savanna`

```mermaid
flowchart LR
    biome["Savanna and Grasslands / savanna"]
    v0["African / savanna_african"]
    v0 -->|biomeId| biome
    o0_0["animal: 6 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["American / savanna_american"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Eurasian / savanna_eurasian"]
    v2 -->|biomeId| biome
    o2_0["animal: 4 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Australian / savanna_australian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Desert / `desert`

```mermaid
flowchart LR
    biome["Desert / desert"]
    v0["American / desert_american"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["African and Arabian / desert_african_and_arabian"]
    v1 -->|biomeId| biome
    o1_0["animal: 4 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 4 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Central Asian / desert_central_asian"]
    v2 -->|biomeId| biome
    o2_0["animal: 4 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Australian / desert_australian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Marine / `marine`

```mermaid
flowchart LR
    biome["Marine / marine"]
    v0["Tropical Coast / marine_tropical_coast"]
    v0 -->|biomeId| biome
    o0_0["animal: 4 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 6 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 3 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    v1 -->|biomeId| biome
    o1_0["animal: 4 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 6 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 3 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Polar and Subpolar / marine_polar_and_subpolar"]
    v2 -->|biomeId| biome
    o2_0["animal: 5 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 6 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 3 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Coastal Wetlands / marine_coastal_wetlands"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 7 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 3 source occurrences"]
    o3_2 -->|variantId| v3
```

### High Mountain and Alpine / `alpine`

```mermaid
flowchart LR
    biome["High Mountain and Alpine / alpine"]
    v0["Andean / alpine_andean"]
    v0 -->|biomeId| biome
    o0_0["animal: 5 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Asian / alpine_asian"]
    v1 -->|biomeId| biome
    o1_0["animal: 5 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 4 source occurrences"]
    o1_2 -->|variantId| v1
    v2["European / alpine_european"]
    v2 -->|biomeId| biome
    o2_0["animal: 5 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["African / alpine_african"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

## `worldRules`

| Field | Value |
| --- | --- |
| hexagonalMap | `true` |
| dynamicWeatherEnabled | `false` |
| seasonsEnabled | `false` |
| dynamicClimateDisastersEnabled | `false` |
| staticEnvironmentalConditionsUsed | `true` |
| maximumRegionalVariantsPerBiome | `4` |
| resourceDiscoverySeparateFromExistence | `true` |
| potentialCultivationSeparateFromEstablishedCrops | `true` |

## `summary`

| Field | Value |
| --- | --- |
| biomeCount | `7` |
| regionalVariantCount | `27` |
| plantCandidateCount | `109` |
| animalCandidateCount | `101` |
| geologicalCandidateCount | `57` |
| sourceOccurrenceCount | `485` |
| agriculturalCropCandidateCount | `21` |

## `elevationLevels`

| id | Name | Additional rules |
| --- | --- | --- |
| 0 | Sea Level | `{"ordinaryLandTraversal": "depends_on_land_or_water_surface"}` |
| 1 | Middle Elevation | `{"ordinaryLandTraversal": true}` |
| 2 | High Elevation | `{"ordinaryLandTraversal": true, "movementAndConstructionRestrictions": null}` |
| 3 | Impassable Summits | `{"ordinaryLandTraversal": false, "conventionalSettlementsAllowed": false}` |

## `geographicModifiers`

| id | Name | Additional rules |
| --- | --- | --- |
| river_floodplain | River and Floodplain | `{}` |
| inland_wetland | Inland Wetland, Lake or Swamp | `{}` |
| coast | Coast and Shoreline | `{}` |
| oasis | Oasis | `{}` |
| volcanic_terrain | Volcanic Terrain | `{}` |
| slope_soil | Slope and Soil | `{}` |

## Proposed generation order

1. `generate_terrain_water_static_climate_and_biogeographic_regions`
2. `assign_biomes_and_geographic_modifiers`
3. `generate_geological_provinces_and_candidate_deposits`
4. `distribute_native_wild_species_using_region_and_habitat`
5. `evaluate_soil_fertility_and_cultivation_suitability`
6. `apply_visibility_discovery_and_exploitation_capabilities`
7. `validate_alternative_development_trade_and_expansion_paths`

All 485 individual occurrences are retained in the [plants](../plants/DIAGRAMS.md), [animals](../animals/DIAGRAMS.md) and [minerals](../minerals/DIAGRAMS.md) files without repeating the complete inventory here. Tile/deposit and review policies are in the [complete structure](../../lang/en/json/data--world--world.catalog.guide.md).
