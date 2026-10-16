# Mundo — Diagramas completos de referencia

[Índice gráfico](../../lang/es/catalog-diagrams.md) · [English](DIAGRAMS.md) · [Español](DIAGRAMS.es.md)

[JSON](world.catalog.guide.json) · [Estructura completa del JSON](../../lang/es/json-structures.md)

Todos los registros del catálogo están incluidos. Se usan varios diagramas pequeños en este mismo archivo para facilitar la consulta. Las flechas representan vínculos documentados, no rendimiento, presencia garantizada ni evolución deducida. Los IDs actuales se conservan.

## Todos los biomas y variantes

Las cantidades son registros del documento, no poblaciones o depósitos ya generados. La distribución regional exacta y la probabilidad siguen pendientes.

### Bosque tropical / `tropical_forest`

```mermaid
flowchart LR
    biome["Bosque tropical / tropical_forest"]
    v0["Americano (selvas húmedas y bosques secos) / tropical_forest_american"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Africano (selvas y bosques secos) / tropical_forest_african"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Asiático (selvas y bosques estacionales) / tropical_forest_asian"]
    v2 -->|biomeId| biome
    o2_0["animal: 7 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 7 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Oceánico (Nueva Guinea y Melanesia) / tropical_forest_oceanian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Bosque templado / `temperate_forest`

```mermaid
flowchart LR
    biome["Bosque templado / temperate_forest"]
    v0["Euroasiático (bosques templados y mediterráneos) / temperate_forest_eurasian"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Americano (bosques templados y mediterráneos) / temperate_forest_american"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Sudafricano y australiano (matorrales y bosques regionales) / temperate_forest_south_african_and_australian"]
    v2 -->|biomeId| biome
    o2_0["animal: 7 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 7 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Boreal (taiga de Eurasia y Norteamérica) / temperate_forest_boreal"]
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
    v0["Norteamérica y Groenlandia / tundra_north_american_and_greenland"]
    v0 -->|biomeId| biome
    o0_0["animal: 5 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Euroasiática / tundra_eurasian"]
    v1 -->|biomeId| biome
    o1_0["animal: 5 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 5 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Subantártica / tundra_subantarctic"]
    v2 -->|biomeId| biome
    o2_0["animal: 3 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 7 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
```

### Sabana / `savanna`

```mermaid
flowchart LR
    biome["Sabana / savanna"]
    v0["Africana (sabanas tropicales) / savanna_african"]
    v0 -->|biomeId| biome
    o0_0["animal: 6 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Americana (sabanas y praderas) / savanna_american"]
    v1 -->|biomeId| biome
    o1_0["animal: 7 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 7 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Euroasiática (praderas y estepas) / savanna_eurasian"]
    v2 -->|biomeId| biome
    o2_0["animal: 4 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Australiana (sabanas tropicales) / savanna_australian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Desierto / `desert`

```mermaid
flowchart LR
    biome["Desierto / desert"]
    v0["Americano (Norteamérica y Sudamérica) / desert_american"]
    v0 -->|biomeId| biome
    o0_0["animal: 7 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 7 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Africano y arábigo / desert_african_and_arabian"]
    v1 -->|biomeId| biome
    o1_0["animal: 4 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 4 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Asiático central / desert_central_asian"]
    v2 -->|biomeId| biome
    o2_0["animal: 4 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Australiano / desert_australian"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

### Marinos / `marine`

```mermaid
flowchart LR
    biome["Marinos / marine"]
    v0["Costero tropical / marine_tropical_coast"]
    v0 -->|biomeId| biome
    o0_0["animal: 4 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 6 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 3 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Costero y mar templado / marine_temperate_coast_and_sea"]
    v1 -->|biomeId| biome
    o1_0["animal: 4 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 6 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 3 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Polar y subpolar / marine_polar_and_subpolar"]
    v2 -->|biomeId| biome
    o2_0["animal: 5 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 6 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 3 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Humedales costeros (manglares y marismas) / marine_coastal_wetlands"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 7 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 3 source occurrences"]
    o3_2 -->|variantId| v3
```

### Alta montaña y pisos alpinos / `alpine`

```mermaid
flowchart LR
    biome["Alta montaña y pisos alpinos / alpine"]
    v0["Andino / alpine_andean"]
    v0 -->|biomeId| biome
    o0_0["animal: 5 source occurrences"]
    o0_0 -->|variantId| v0
    o0_1["geological: 8 source occurrences"]
    o0_1 -->|variantId| v0
    o0_2["plant: 5 source occurrences"]
    o0_2 -->|variantId| v0
    v1["Asiático (Himalaya y Tíbet) / alpine_asian"]
    v1 -->|biomeId| biome
    o1_0["animal: 5 source occurrences"]
    o1_0 -->|variantId| v1
    o1_1["geological: 8 source occurrences"]
    o1_1 -->|variantId| v1
    o1_2["plant: 4 source occurrences"]
    o1_2 -->|variantId| v1
    v2["Europeo (Alpes y Pirineos) / alpine_european"]
    v2 -->|biomeId| biome
    o2_0["animal: 5 source occurrences"]
    o2_0 -->|variantId| v2
    o2_1["geological: 8 source occurrences"]
    o2_1 -->|variantId| v2
    o2_2["plant: 4 source occurrences"]
    o2_2 -->|variantId| v2
    v3["Africano (Etiopía y África oriental) / alpine_african"]
    v3 -->|biomeId| biome
    o3_0["animal: 4 source occurrences"]
    o3_0 -->|variantId| v3
    o3_1["geological: 8 source occurrences"]
    o3_1 -->|variantId| v3
    o3_2["plant: 4 source occurrences"]
    o3_2 -->|variantId| v3
```

## `worldRules`

| Campo | Valor |
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

| Campo | Valor |
| --- | --- |
| biomeCount | `7` |
| regionalVariantCount | `27` |
| plantCandidateCount | `129` |
| animalCandidateCount | `134` |
| geologicalCandidateCount | `57` |
| sourceOccurrenceCount | `485` |
| agriculturalCropCandidateCount | `21` |

## `elevationLevels`

| id | Nombre | Reglas adicionales |
| --- | --- | --- |
| 0 | Nivel del mar | `{"ordinaryLandTraversal": "depends_on_land_or_water_surface"}` |
| 1 | Nivel medio | `{"ordinaryLandTraversal": true}` |
| 2 | Nivel alto | `{"ordinaryLandTraversal": true, "movementAndConstructionRestrictions": null}` |
| 3 | Cumbres infranqueables | `{"ordinaryLandTraversal": false, "conventionalSettlementsAllowed": false}` |

## `geographicModifiers`

| id | Nombre | Reglas adicionales |
| --- | --- | --- |
| river_floodplain | Río y llanura aluvial | `{}` |
| inland_wetland | Humedal, lago y pantano | `{}` |
| coast | Costa y litoral | `{}` |
| oasis | Oasis | `{}` |
| volcanic_terrain | Terreno volcánico | `{}` |
| slope_soil | Pendiente y suelo | `{}` |

## Orden de generación propuesto

1. `generate_terrain_water_static_climate_and_biogeographic_regions`
2. `assign_biomes_and_geographic_modifiers`
3. `generate_geological_provinces_and_candidate_deposits`
4. `distribute_native_wild_species_using_region_and_habitat`
5. `evaluate_soil_fertility_and_cultivation_suitability`
6. `apply_visibility_discovery_and_exploitation_capabilities`
7. `validate_alternative_development_trade_and_expansion_paths`

Las 485 apariciones individuales están completas en los archivos de [plantas](../plants/DIAGRAMS.es.md), [animales](../animals/DIAGRAMS.es.md) y [minerales](../minerals/DIAGRAMS.es.md), sin duplicar todo el inventario aquí. Las políticas de casillas, yacimientos y revisión están en la [estructura completa](../../lang/es/json/data--world--world.catalog.guide.md).
