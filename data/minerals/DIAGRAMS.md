# Minerals — Complete reference diagrams

[Diagram index](../../lang/en/catalog-diagrams.md) · [English](DIAGRAMS.md) · [Español](DIAGRAMS.es.md)

[JSON](minerals.catalog.guide.json) · [Complete JSON structure](../../lang/en/json-structures.md)

Every catalog record is included. Several small diagrams in this file keep the reference readable. Arrows represent documented links, not yield, guaranteed presence or inferred evolution. Existing IDs are preserved.

Candidates do not have finalized taxonomy, ecology, products or processes. Only existing relationships are drawn. Potential product tags are not resource IDs or confirmed production quantities.

## Complete inventory

| id | Name |
| --- | --- |
| geological_clay | Clay |
| geological_alluvial_clay | Alluvial Clay |
| geological_estuarine_clay | Estuarine Clay |
| geological_fluvial_clay | Fluvial Clay |
| geological_glacial_clay | Glacial Clay |
| geological_sand | Sand |
| geological_calcareous_sand | Calcareous Sand |
| geological_silica_sand | Silica Sand |
| geological_sandstone | Sandstone |
| geological_limestone | Limestone |
| geological_limestone_in_carbonate_formations | Limestone in Carbonate Formations |
| geological_coastal_limestone | Coastal Limestone |
| geological_bituminous_coal | Bituminous Coal |
| geological_copper_bearing_deposit | Copper-Bearing Deposit |
| geological_chalcopyrite_copper_ore | Chalcopyrite Copper Ore |
| geological_sulfide_copper_ore | Sulfide Copper Ore |
| geological_seashells | Seashells |
| geological_tin_bearing_deposit | Tin-Bearing Deposit |
| geological_vein_cassiterite_tin_ore | Vein Cassiterite Tin Ore |
| geological_alluvial_cassiterite | Alluvial Cassiterite |
| geological_phosphorite | Phosphorite |
| geological_apatite_phosphorite | Apatite Phosphorite |
| geological_granite | Granite |
| geological_gravel | Gravel |
| geological_coastal_gravel | Coastal Gravel |
| geological_iron_bearing_deposit | Iron-Bearing Deposit |
| geological_hematite_iron_ore | Hematite Iron Ore |
| geological_magnetite_iron_ore | Magnetite Iron Ore |
| geological_iron_rich_laterite | Iron-Rich Laterite |
| geological_manganese_bearing_deposit | Manganese-Bearing Deposit |
| geological_pyrolusite_manganese_ore | Pyrolusite Manganese Ore |
| geological_nickel_bearing_deposit | Nickel-Bearing Deposit |
| geological_nickeliferous_laterite | Nickeliferous Laterite |
| geological_sulfide_nickel_ore | Sulfide Nickel Ore |
| geological_polymetallic_nodules | Polymetallic Nodules |
| geological_volcanic_obsidian | Volcanic Obsidian |
| geological_gold_bearing_quartz | Gold-Bearing Quartz |
| geological_alluvial_gold | Alluvial Gold |
| geological_vein_gold | Vein Gold |
| geological_pumice | Pumice |
| geological_slate | Slate |
| geological_silver_bearing_deposit | Silver-Bearing Deposit |
| geological_argentite_silver_ore | Argentite Silver Ore |
| geological_lead_bearing_deposit | Lead-Bearing Deposit |
| geological_galena_lead_ore | Galena Lead Ore |
| geological_basalt | Basalt |
| geological_volcanic_rock | Volcanic Rock |
| geological_rock_salt | Rock Salt |
| geological_deep_rock_salt | Deep Rock Salt |
| geological_sea_salt | Sea Salt |
| geological_sea_salt_in_suitable_saltworks | Sea Salt in Suitable Saltworks |
| geological_flint | Flint |
| geological_peat | Peat |
| geological_gypsum_in_evaporite_deposits | Gypsum in Evaporite Deposits |
| geological_deep_gypsum | Deep Gypsum |
| geological_coastal_gypsum | Coastal Gypsum |
| geological_surface_opal | Surface Opal |

## Relationships for every candidate

### Group 1

```mermaid
flowchart LR
    c0["Clay / geological_clay"]
    v1["African / tropical_forest_african"]
    b0["Tropical Forest / tropical_forest"]
    v4["Eurasian / temperate_forest_eurasian"]
    b1["Temperate Forest / temperate_forest"]
    v5["American / temperate_forest_american"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    v7["Boreal / temperate_forest_boreal"]
    v12["American / savanna_american"]
    b3["Savanna and Grasslands / savanna"]
    v13["Eurasian / savanna_eurasian"]
    v14["Australian / savanna_australian"]
    v23["Andean / alpine_andean"]
    b6["High Mountain and Alpine / alpine"]
    v26["African / alpine_african"]
    r0["Clay / RES#000047"]
    c1["Alluvial Clay / geological_alluvial_clay"]
    v0["American / tropical_forest_american"]
    v3["Oceanian / tropical_forest_oceanian"]
    v11["African / savanna_african"]
    r1["Clay / RES#000047"]
    c2["Estuarine Clay / geological_estuarine_clay"]
    v22["Coastal Wetlands / marine_coastal_wetlands"]
    b5["Marine / marine"]
    r2["Clay / RES#000047"]
    c3["Fluvial Clay / geological_fluvial_clay"]
    v2["Asian / tropical_forest_asian"]
    r3["Clay / RES#000047"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v1
    c0 -->|source occurrence| v12
    c0 -->|source occurrence| v13
    c0 -->|source occurrence| v14
    c0 -->|source occurrence| v23
    c0 -->|source occurrence| v26
    c0 -->|source occurrence| v4
    c0 -->|source occurrence| v5
    c0 -->|source occurrence| v6
    c0 -->|source occurrence| v7
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v0
    c1 -->|source occurrence| v11
    c1 -->|source occurrence| v3
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v22
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v2
    v0 -->|biomeId| b0
    v1 -->|biomeId| b0
    v11 -->|biomeId| b3
    v12 -->|biomeId| b3
    v13 -->|biomeId| b3
    v14 -->|biomeId| b3
    v2 -->|biomeId| b0
    v22 -->|biomeId| b5
    v23 -->|biomeId| b6
    v26 -->|biomeId| b6
    v3 -->|biomeId| b0
    v4 -->|biomeId| b1
    v5 -->|biomeId| b1
    v6 -->|biomeId| b1
    v7 -->|biomeId| b1
```

### Group 2

```mermaid
flowchart LR
    c0["Glacial Clay / geological_glacial_clay"]
    v9["Eurasian / tundra_eurasian"]
    b2["Tundra / tundra"]
    r0["Clay / RES#000047"]
    c1["Sand / geological_sand"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v16["African and Arabian / desert_african_and_arabian"]
    v17["Central Asian / desert_central_asian"]
    v18["Australian / desert_australian"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    b5["Marine / marine"]
    v22["Coastal Wetlands / marine_coastal_wetlands"]
    r1["Sand / RES#000048"]
    c2["Calcareous Sand / geological_calcareous_sand"]
    v19["Tropical Coast / marine_tropical_coast"]
    r2["Calcareous sand / RES#000049"]
    c3["Silica Sand / geological_silica_sand"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    r3["Silica sand / RES#000050"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v9
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v15
    c1 -->|source occurrence| v16
    c1 -->|source occurrence| v17
    c1 -->|source occurrence| v18
    c1 -->|source occurrence| v21
    c1 -->|source occurrence| v22
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v19
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v20
    v15 -->|biomeId| b4
    v16 -->|biomeId| b4
    v17 -->|biomeId| b4
    v18 -->|biomeId| b4
    v19 -->|biomeId| b5
    v20 -->|biomeId| b5
    v21 -->|biomeId| b5
    v22 -->|biomeId| b5
    v9 -->|biomeId| b2
```

### Group 3

```mermaid
flowchart LR
    c0["Sandstone / geological_sandstone"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    b1["Temperate Forest / temperate_forest"]
    v14["Australian / savanna_australian"]
    b3["Savanna and Grasslands / savanna"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v16["African and Arabian / desert_african_and_arabian"]
    v18["Australian / desert_australian"]
    r0["Sandstone / RES#000051"]
    c1["Limestone / geological_limestone"]
    v0["American / tropical_forest_american"]
    b0["Tropical Forest / tropical_forest"]
    v2["Asian / tropical_forest_asian"]
    v4["Eurasian / temperate_forest_eurasian"]
    v11["African / savanna_african"]
    v13["Eurasian / savanna_eurasian"]
    v25["European / alpine_european"]
    b6["High Mountain and Alpine / alpine"]
    r1["Limestone / RES#000052"]
    c2["Limestone in Carbonate Formations / geological_limestone_in_carbonate_formations"]
    v22["Coastal Wetlands / marine_coastal_wetlands"]
    b5["Marine / marine"]
    r2["Limestone / RES#000052"]
    c3["Coastal Limestone / geological_coastal_limestone"]
    v19["Tropical Coast / marine_tropical_coast"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    r3["Limestone / RES#000052"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v14
    c0 -->|source occurrence| v15
    c0 -->|source occurrence| v16
    c0 -->|source occurrence| v18
    c0 -->|source occurrence| v6
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v0
    c1 -->|source occurrence| v11
    c1 -->|source occurrence| v13
    c1 -->|source occurrence| v2
    c1 -->|source occurrence| v25
    c1 -->|source occurrence| v4
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v22
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v19
    c3 -->|source occurrence| v20
    c3 -->|source occurrence| v21
    v0 -->|biomeId| b0
    v11 -->|biomeId| b3
    v13 -->|biomeId| b3
    v14 -->|biomeId| b3
    v15 -->|biomeId| b4
    v16 -->|biomeId| b4
    v18 -->|biomeId| b4
    v19 -->|biomeId| b5
    v2 -->|biomeId| b0
    v20 -->|biomeId| b5
    v21 -->|biomeId| b5
    v22 -->|biomeId| b5
    v25 -->|biomeId| b6
    v4 -->|biomeId| b1
    v6 -->|biomeId| b1
```

### Group 4

```mermaid
flowchart LR
    c0["Bituminous Coal / geological_bituminous_coal"]
    v4["Eurasian / temperate_forest_eurasian"]
    b1["Temperate Forest / temperate_forest"]
    v13["Eurasian / savanna_eurasian"]
    b3["Savanna and Grasslands / savanna"]
    r0["Bituminous coal / RES#000053"]
    c1["Copper-Bearing Deposit / geological_copper_bearing_deposit"]
    v0["American / tropical_forest_american"]
    b0["Tropical Forest / tropical_forest"]
    v1["African / tropical_forest_african"]
    v2["Asian / tropical_forest_asian"]
    v3["Oceanian / tropical_forest_oceanian"]
    v5["American / temperate_forest_american"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    v7["Boreal / temperate_forest_boreal"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    v9["Eurasian / tundra_eurasian"]
    v10["Subantarctic / tundra_subantarctic"]
    v11["African / savanna_african"]
    v12["American / savanna_american"]
    v14["Australian / savanna_australian"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v16["African and Arabian / desert_african_and_arabian"]
    v17["Central Asian / desert_central_asian"]
    v18["Australian / desert_australian"]
    v23["Andean / alpine_andean"]
    b6["High Mountain and Alpine / alpine"]
    v24["Asian / alpine_asian"]
    v25["European / alpine_european"]
    v26["African / alpine_african"]
    r1["Copper-bearing material / RES#000054"]
    c2["Chalcopyrite Copper Ore / geological_chalcopyrite_copper_ore"]
    r2["Copper ore / RES#000055"]
    c3["Sulfide Copper Ore / geological_sulfide_copper_ore"]
    r3["Copper ore / RES#000055"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v13
    c0 -->|source occurrence| v4
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v0
    c1 -->|source occurrence| v1
    c1 -->|source occurrence| v10
    c1 -->|source occurrence| v11
    c1 -->|source occurrence| v12
    c1 -->|source occurrence| v13
    c1 -->|source occurrence| v14
    c1 -->|source occurrence| v15
    c1 -->|source occurrence| v16
    c1 -->|source occurrence| v17
    c1 -->|source occurrence| v18
    c1 -->|source occurrence| v2
    c1 -->|source occurrence| v23
    c1 -->|source occurrence| v24
    c1 -->|source occurrence| v25
    c1 -->|source occurrence| v26
    c1 -->|source occurrence| v3
    c1 -->|source occurrence| v4
    c1 -->|source occurrence| v5
    c1 -->|source occurrence| v6
    c1 -->|source occurrence| v7
    c1 -->|source occurrence| v8
    c1 -->|source occurrence| v9
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v10
    c2 -->|source occurrence| v12
    c2 -->|source occurrence| v15
    c2 -->|source occurrence| v17
    c2 -->|source occurrence| v2
    c2 -->|source occurrence| v23
    c2 -->|source occurrence| v24
    c2 -->|source occurrence| v3
    c2 -->|source occurrence| v5
    c2 -->|source occurrence| v6
    c2 -->|source occurrence| v9
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v0
    v0 -->|biomeId| b0
    v1 -->|biomeId| b0
    v10 -->|biomeId| b2
    v11 -->|biomeId| b3
    v12 -->|biomeId| b3
    v13 -->|biomeId| b3
    v14 -->|biomeId| b3
    v15 -->|biomeId| b4
    v16 -->|biomeId| b4
    v17 -->|biomeId| b4
    v18 -->|biomeId| b4
    v2 -->|biomeId| b0
    v23 -->|biomeId| b6
    v24 -->|biomeId| b6
    v25 -->|biomeId| b6
    v26 -->|biomeId| b6
    v3 -->|biomeId| b0
    v4 -->|biomeId| b1
    v5 -->|biomeId| b1
    v6 -->|biomeId| b1
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
    v9 -->|biomeId| b2
```

### Group 5

```mermaid
flowchart LR
    c0["Seashells / geological_seashells"]
    v19["Tropical Coast / marine_tropical_coast"]
    b5["Marine / marine"]
    r0["Shell or carapace / RES#000044"]
    c1["Tin-Bearing Deposit / geological_tin_bearing_deposit"]
    v2["Asian / tropical_forest_asian"]
    b0["Tropical Forest / tropical_forest"]
    v13["Eurasian / savanna_eurasian"]
    b3["Savanna and Grasslands / savanna"]
    v17["Central Asian / desert_central_asian"]
    b4["Desert / desert"]
    v23["Andean / alpine_andean"]
    b6["High Mountain and Alpine / alpine"]
    r1["Tin-bearing material / RES#000056"]
    c2["Vein Cassiterite Tin Ore / geological_vein_cassiterite_tin_ore"]
    r2["Tin ore / RES#000057"]
    c3["Alluvial Cassiterite / geological_alluvial_cassiterite"]
    r3["Tin ore / RES#000057"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v19
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v13
    c1 -->|source occurrence| v17
    c1 -->|source occurrence| v2
    c1 -->|source occurrence| v23
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v2
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v2
    v13 -->|biomeId| b3
    v17 -->|biomeId| b4
    v19 -->|biomeId| b5
    v2 -->|biomeId| b0
    v23 -->|biomeId| b6
```

### Group 6

```mermaid
flowchart LR
    c0["Phosphorite / geological_phosphorite"]
    v16["African and Arabian / desert_african_and_arabian"]
    b4["Desert / desert"]
    r0["Phosphorite / RES#000058"]
    c1["Apatite Phosphorite / geological_apatite_phosphorite"]
    r1["Phosphorite / RES#000058"]
    c2["Granite / geological_granite"]
    v5["American / temperate_forest_american"]
    b1["Temperate Forest / temperate_forest"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    v7["Boreal / temperate_forest_boreal"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    v9["Eurasian / tundra_eurasian"]
    v12["American / savanna_american"]
    b3["Savanna and Grasslands / savanna"]
    v23["Andean / alpine_andean"]
    b6["High Mountain and Alpine / alpine"]
    v24["Asian / alpine_asian"]
    v25["European / alpine_european"]
    r2["Granite / RES#000059"]
    c3["Gravel / geological_gravel"]
    v10["Subantarctic / tundra_subantarctic"]
    v17["Central Asian / desert_central_asian"]
    r3["Gravel / RES#000060"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v16
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v16
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v12
    c2 -->|source occurrence| v23
    c2 -->|source occurrence| v24
    c2 -->|source occurrence| v25
    c2 -->|source occurrence| v5
    c2 -->|source occurrence| v6
    c2 -->|source occurrence| v7
    c2 -->|source occurrence| v8
    c2 -->|source occurrence| v9
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v10
    c3 -->|source occurrence| v17
    c3 -->|source occurrence| v8
    c3 -->|source occurrence| v9
    v10 -->|biomeId| b2
    v12 -->|biomeId| b3
    v16 -->|biomeId| b4
    v17 -->|biomeId| b4
    v23 -->|biomeId| b6
    v24 -->|biomeId| b6
    v25 -->|biomeId| b6
    v5 -->|biomeId| b1
    v6 -->|biomeId| b1
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
    v9 -->|biomeId| b2
```

### Group 7

```mermaid
flowchart LR
    c0["Coastal Gravel / geological_coastal_gravel"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    b5["Marine / marine"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    r0["Gravel / RES#000060"]
    c1["Iron-Bearing Deposit / geological_iron_bearing_deposit"]
    v0["American / tropical_forest_american"]
    b0["Tropical Forest / tropical_forest"]
    v1["African / tropical_forest_african"]
    v2["Asian / tropical_forest_asian"]
    v4["Eurasian / temperate_forest_eurasian"]
    b1["Temperate Forest / temperate_forest"]
    v5["American / temperate_forest_american"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    v7["Boreal / temperate_forest_boreal"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    v9["Eurasian / tundra_eurasian"]
    v10["Subantarctic / tundra_subantarctic"]
    v11["African / savanna_african"]
    b3["Savanna and Grasslands / savanna"]
    v12["American / savanna_american"]
    v13["Eurasian / savanna_eurasian"]
    v14["Australian / savanna_australian"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v16["African and Arabian / desert_african_and_arabian"]
    v17["Central Asian / desert_central_asian"]
    v18["Australian / desert_australian"]
    v24["Asian / alpine_asian"]
    b6["High Mountain and Alpine / alpine"]
    v25["European / alpine_european"]
    v26["African / alpine_african"]
    r1["Iron-bearing material / RES#000061"]
    c2["Hematite Iron Ore / geological_hematite_iron_ore"]
    r2["Iron ore / RES#000062"]
    c3["Magnetite Iron Ore / geological_magnetite_iron_ore"]
    r3["Iron ore / RES#000062"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v20
    c0 -->|source occurrence| v21
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v0
    c1 -->|source occurrence| v1
    c1 -->|source occurrence| v10
    c1 -->|source occurrence| v11
    c1 -->|source occurrence| v12
    c1 -->|source occurrence| v13
    c1 -->|source occurrence| v14
    c1 -->|source occurrence| v15
    c1 -->|source occurrence| v16
    c1 -->|source occurrence| v17
    c1 -->|source occurrence| v18
    c1 -->|source occurrence| v2
    c1 -->|source occurrence| v24
    c1 -->|source occurrence| v25
    c1 -->|source occurrence| v26
    c1 -->|source occurrence| v4
    c1 -->|source occurrence| v5
    c1 -->|source occurrence| v6
    c1 -->|source occurrence| v7
    c1 -->|source occurrence| v8
    c1 -->|source occurrence| v9
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v0
    c2 -->|source occurrence| v1
    c2 -->|source occurrence| v11
    c2 -->|source occurrence| v12
    c2 -->|source occurrence| v14
    c2 -->|source occurrence| v15
    c2 -->|source occurrence| v16
    c2 -->|source occurrence| v18
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v10
    c3 -->|source occurrence| v13
    c3 -->|source occurrence| v17
    c3 -->|source occurrence| v24
    c3 -->|source occurrence| v25
    c3 -->|source occurrence| v26
    c3 -->|source occurrence| v4
    c3 -->|source occurrence| v5
    c3 -->|source occurrence| v7
    c3 -->|source occurrence| v8
    c3 -->|source occurrence| v9
    v0 -->|biomeId| b0
    v1 -->|biomeId| b0
    v10 -->|biomeId| b2
    v11 -->|biomeId| b3
    v12 -->|biomeId| b3
    v13 -->|biomeId| b3
    v14 -->|biomeId| b3
    v15 -->|biomeId| b4
    v16 -->|biomeId| b4
    v17 -->|biomeId| b4
    v18 -->|biomeId| b4
    v2 -->|biomeId| b0
    v20 -->|biomeId| b5
    v21 -->|biomeId| b5
    v24 -->|biomeId| b6
    v25 -->|biomeId| b6
    v26 -->|biomeId| b6
    v4 -->|biomeId| b1
    v5 -->|biomeId| b1
    v6 -->|biomeId| b1
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
    v9 -->|biomeId| b2
```

### Group 8

```mermaid
flowchart LR
    c0["Iron-Rich Laterite / geological_iron_rich_laterite"]
    v1["African / tropical_forest_african"]
    b0["Tropical Forest / tropical_forest"]
    v14["Australian / savanna_australian"]
    b3["Savanna and Grasslands / savanna"]
    r0["Iron-rich laterite / RES#000063"]
    c1["Manganese-Bearing Deposit / geological_manganese_bearing_deposit"]
    r1["Manganese-bearing material / RES#000064"]
    c2["Pyrolusite Manganese Ore / geological_pyrolusite_manganese_ore"]
    r2["Manganese ore / RES#000065"]
    c3["Nickel-Bearing Deposit / geological_nickel_bearing_deposit"]
    v3["Oceanian / tropical_forest_oceanian"]
    v7["Boreal / temperate_forest_boreal"]
    b1["Temperate Forest / temperate_forest"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    v9["Eurasian / tundra_eurasian"]
    r3["Nickel-bearing material / RES#000066"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v1
    c0 -->|source occurrence| v14
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v1
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v1
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v3
    c3 -->|source occurrence| v7
    c3 -->|source occurrence| v8
    c3 -->|source occurrence| v9
    v1 -->|biomeId| b0
    v14 -->|biomeId| b3
    v3 -->|biomeId| b0
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
    v9 -->|biomeId| b2
```

### Group 9

```mermaid
flowchart LR
    c0["Nickeliferous Laterite / geological_nickeliferous_laterite"]
    v3["Oceanian / tropical_forest_oceanian"]
    b0["Tropical Forest / tropical_forest"]
    r0["Nickel-bearing laterite / RES#000067"]
    c1["Sulfide Nickel Ore / geological_sulfide_nickel_ore"]
    v7["Boreal / temperate_forest_boreal"]
    b1["Temperate Forest / temperate_forest"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    r1["Nickel ore / RES#000068"]
    c2["Polymetallic Nodules / geological_polymetallic_nodules"]
    v19["Tropical Coast / marine_tropical_coast"]
    b5["Marine / marine"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    r2["Polymetallic nodules / RES#000069"]
    c3["Volcanic Obsidian / geological_volcanic_obsidian"]
    v5["American / temperate_forest_american"]
    r3["Obsidian / RES#000070"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v3
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v7
    c1 -->|source occurrence| v8
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v19
    c2 -->|source occurrence| v20
    c2 -->|source occurrence| v21
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v5
    v19 -->|biomeId| b5
    v20 -->|biomeId| b5
    v21 -->|biomeId| b5
    v3 -->|biomeId| b0
    v5 -->|biomeId| b1
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
```

### Group 10

```mermaid
flowchart LR
    c0["Gold-Bearing Quartz / geological_gold_bearing_quartz"]
    v6["South African and Australian / temperate_forest_south_african_and_australian"]
    b1["Temperate Forest / temperate_forest"]
    v11["African / savanna_african"]
    b3["Savanna and Grasslands / savanna"]
    v14["Australian / savanna_australian"]
    v18["Australian / desert_australian"]
    b4["Desert / desert"]
    v26["African / alpine_african"]
    b6["High Mountain and Alpine / alpine"]
    r0["Gold-bearing quartz / RES#000071"]
    c1["Alluvial Gold / geological_alluvial_gold"]
    v0["American / tropical_forest_american"]
    b0["Tropical Forest / tropical_forest"]
    v1["African / tropical_forest_african"]
    v3["Oceanian / tropical_forest_oceanian"]
    v12["American / savanna_american"]
    v23["Andean / alpine_andean"]
    r1["Gold-bearing sediment / RES#000072"]
    c2["Vein Gold / geological_vein_gold"]
    v24["Asian / alpine_asian"]
    r2["Gold ore / RES#000073"]
    c3["Pumice / geological_pumice"]
    r3["Pumice / RES#000074"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v11
    c0 -->|source occurrence| v14
    c0 -->|source occurrence| v18
    c0 -->|source occurrence| v26
    c0 -->|source occurrence| v6
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v0
    c1 -->|source occurrence| v1
    c1 -->|source occurrence| v11
    c1 -->|source occurrence| v12
    c1 -->|source occurrence| v23
    c1 -->|source occurrence| v3
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v0
    c2 -->|source occurrence| v11
    c2 -->|source occurrence| v14
    c2 -->|source occurrence| v18
    c2 -->|source occurrence| v24
    c2 -->|source occurrence| v26
    c2 -->|source occurrence| v3
    c2 -->|source occurrence| v6
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v26
    v0 -->|biomeId| b0
    v1 -->|biomeId| b0
    v11 -->|biomeId| b3
    v12 -->|biomeId| b3
    v14 -->|biomeId| b3
    v18 -->|biomeId| b4
    v23 -->|biomeId| b6
    v24 -->|biomeId| b6
    v26 -->|biomeId| b6
    v3 -->|biomeId| b0
    v6 -->|biomeId| b1
```

### Group 11

```mermaid
flowchart LR
    c0["Slate / geological_slate"]
    v7["Boreal / temperate_forest_boreal"]
    b1["Temperate Forest / temperate_forest"]
    v8["North American and Greenland / tundra_north_american_and_greenland"]
    b2["Tundra / tundra"]
    v24["Asian / alpine_asian"]
    b6["High Mountain and Alpine / alpine"]
    v25["European / alpine_european"]
    r0["Slate / RES#000075"]
    c1["Silver-Bearing Deposit / geological_silver_bearing_deposit"]
    v5["American / temperate_forest_american"]
    v12["American / savanna_american"]
    b3["Savanna and Grasslands / savanna"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v23["Andean / alpine_andean"]
    r1["Silver-bearing material / RES#000076"]
    c2["Argentite Silver Ore / geological_argentite_silver_ore"]
    r2["Silver ore / RES#000077"]
    c3["Lead-Bearing Deposit / geological_lead_bearing_deposit"]
    v4["Eurasian / temperate_forest_eurasian"]
    r3["Lead-bearing material / RES#000078"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v24
    c0 -->|source occurrence| v25
    c0 -->|source occurrence| v7
    c0 -->|source occurrence| v8
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v12
    c1 -->|source occurrence| v15
    c1 -->|source occurrence| v23
    c1 -->|source occurrence| v5
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v23
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v25
    c3 -->|source occurrence| v4
    v12 -->|biomeId| b3
    v15 -->|biomeId| b4
    v23 -->|biomeId| b6
    v24 -->|biomeId| b6
    v25 -->|biomeId| b6
    v4 -->|biomeId| b1
    v5 -->|biomeId| b1
    v7 -->|biomeId| b1
    v8 -->|biomeId| b2
```

### Group 12

```mermaid
flowchart LR
    c0["Galena Lead Ore / geological_galena_lead_ore"]
    v25["European / alpine_european"]
    b6["High Mountain and Alpine / alpine"]
    r0["Lead ore / RES#000079"]
    c1["Basalt / geological_basalt"]
    v10["Subantarctic / tundra_subantarctic"]
    b2["Tundra / tundra"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    b5["Marine / marine"]
    r1["Basalt / RES#000080"]
    c2["Volcanic Rock / geological_volcanic_rock"]
    v3["Oceanian / tropical_forest_oceanian"]
    b0["Tropical Forest / tropical_forest"]
    v26["African / alpine_african"]
    r2["Volcanic rock / RES#000081"]
    c3["Rock Salt / geological_rock_salt"]
    v15["American / desert_american"]
    b4["Desert / desert"]
    v16["African and Arabian / desert_african_and_arabian"]
    v17["Central Asian / desert_central_asian"]
    v24["Asian / alpine_asian"]
    r3["Rock salt / RES#000082"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v25
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v10
    c1 -->|source occurrence| v21
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v26
    c2 -->|source occurrence| v3
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v15
    c3 -->|source occurrence| v16
    c3 -->|source occurrence| v17
    c3 -->|source occurrence| v24
    v10 -->|biomeId| b2
    v15 -->|biomeId| b4
    v16 -->|biomeId| b4
    v17 -->|biomeId| b4
    v21 -->|biomeId| b5
    v24 -->|biomeId| b6
    v25 -->|biomeId| b6
    v26 -->|biomeId| b6
    v3 -->|biomeId| b0
```

### Group 13

```mermaid
flowchart LR
    c0["Deep Rock Salt / geological_deep_rock_salt"]
    v22["Coastal Wetlands / marine_coastal_wetlands"]
    b5["Marine / marine"]
    r0["Rock salt / RES#000082"]
    c1["Sea Salt / geological_sea_salt"]
    v19["Tropical Coast / marine_tropical_coast"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    r1["Sea salt / RES#000083"]
    c2["Sea Salt in Suitable Saltworks / geological_sea_salt_in_suitable_saltworks"]
    r2["Sea salt / RES#000083"]
    c3["Flint / geological_flint"]
    v4["Eurasian / temperate_forest_eurasian"]
    b1["Temperate Forest / temperate_forest"]
    v13["Eurasian / savanna_eurasian"]
    b3["Savanna and Grasslands / savanna"]
    r3["Flint / RES#000084"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v22
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v19
    c1 -->|source occurrence| v20
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v22
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v13
    c3 -->|source occurrence| v4
    v13 -->|biomeId| b3
    v19 -->|biomeId| b5
    v20 -->|biomeId| b5
    v22 -->|biomeId| b5
    v4 -->|biomeId| b1
```

### Group 14

```mermaid
flowchart LR
    c0["Peat / geological_peat"]
    v10["Subantarctic / tundra_subantarctic"]
    b2["Tundra / tundra"]
    r0["Peat / RES#000085"]
    c1["Gypsum in Evaporite Deposits / geological_gypsum_in_evaporite_deposits"]
    v22["Coastal Wetlands / marine_coastal_wetlands"]
    b5["Marine / marine"]
    r1["Gypsum / RES#000086"]
    c2["Deep Gypsum / geological_deep_gypsum"]
    r2["Gypsum / RES#000086"]
    c3["Coastal Gypsum / geological_coastal_gypsum"]
    v19["Tropical Coast / marine_tropical_coast"]
    v20["Temperate Coast and Sea / marine_temperate_coast_and_sea"]
    v21["Polar and Subpolar / marine_polar_and_subpolar"]
    r3["Gypsum / RES#000086"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v10
    c1 -->|extractedResourceId / proposed| r1
    c1 -->|source occurrence| v22
    c2 -->|extractedResourceId / proposed| r2
    c2 -->|source occurrence| v22
    c3 -->|extractedResourceId / proposed| r3
    c3 -->|source occurrence| v19
    c3 -->|source occurrence| v20
    c3 -->|source occurrence| v21
    v10 -->|biomeId| b2
    v19 -->|biomeId| b5
    v20 -->|biomeId| b5
    v21 -->|biomeId| b5
    v22 -->|biomeId| b5
```

### Group 15

```mermaid
flowchart LR
    c0["Surface Opal / geological_surface_opal"]
    v18["Australian / desert_australian"]
    b4["Desert / desert"]
    r0["Opal / RES#000087"]
    c0 -->|extractedResourceId / proposed| r0
    c0 -->|source occurrence| v18
    v18 -->|biomeId| b4
```

## Every source occurrence

This table retains every regional link and extraction method even when diagrams combine repeated arrows. Initial spawning remains disabled.

| id | definitionId | biomeId | variantId | extractionMethodId | sourceText |
| --- | --- | --- | --- | --- | --- |
| occurrence_0001 | geological_alluvial_clay | tropical_forest | tropical_forest_american | surface_collection | Arcilla aluvial |
| occurrence_0002 | geological_limestone | tropical_forest | tropical_forest_american | surface_collection | Caliza |
| occurrence_0003 | geological_alluvial_gold | tropical_forest | tropical_forest_american | surface_collection | Oro aluvial |
| occurrence_0004 | geological_copper_bearing_deposit | tropical_forest | tropical_forest_american | traditional_mining | Cobre |
| occurrence_0005 | geological_iron_bearing_deposit | tropical_forest | tropical_forest_american | traditional_mining | Hierro |
| occurrence_0006 | geological_vein_gold | tropical_forest | tropical_forest_american | traditional_mining | Oro en veta |
| occurrence_0007 | geological_sulfide_copper_ore | tropical_forest | tropical_forest_american | mechanized_mining | Cobre (sulfuros) |
| occurrence_0008 | geological_hematite_iron_ore | tropical_forest | tropical_forest_american | mechanized_mining | Hierro (hematita) |
| occurrence_0023 | geological_clay | tropical_forest | tropical_forest_african | surface_collection | Arcilla |
| occurrence_0024 | geological_iron_rich_laterite | tropical_forest | tropical_forest_african | surface_collection | Laterita ferruginosa |
| occurrence_0025 | geological_alluvial_gold | tropical_forest | tropical_forest_african | surface_collection | Oro aluvial |
| occurrence_0026 | geological_iron_bearing_deposit | tropical_forest | tropical_forest_african | traditional_mining | Hierro |
| occurrence_0027 | geological_copper_bearing_deposit | tropical_forest | tropical_forest_african | traditional_mining | Cobre |
| occurrence_0028 | geological_manganese_bearing_deposit | tropical_forest | tropical_forest_african | traditional_mining | Manganeso |
| occurrence_0029 | geological_hematite_iron_ore | tropical_forest | tropical_forest_african | mechanized_mining | Hierro (hematita) |
| occurrence_0030 | geological_pyrolusite_manganese_ore | tropical_forest | tropical_forest_african | mechanized_mining | Manganeso (pirolusita) |
| occurrence_0045 | geological_fluvial_clay | tropical_forest | tropical_forest_asian | surface_collection | Arcilla fluvial |
| occurrence_0046 | geological_limestone | tropical_forest | tropical_forest_asian | surface_collection | Caliza |
| occurrence_0047 | geological_alluvial_cassiterite | tropical_forest | tropical_forest_asian | surface_collection | Estaño aluvial (casiterita) |
| occurrence_0048 | geological_tin_bearing_deposit | tropical_forest | tropical_forest_asian | traditional_mining | Estaño |
| occurrence_0049 | geological_copper_bearing_deposit | tropical_forest | tropical_forest_asian | traditional_mining | Cobre |
| occurrence_0050 | geological_iron_bearing_deposit | tropical_forest | tropical_forest_asian | traditional_mining | Hierro |
| occurrence_0051 | geological_vein_cassiterite_tin_ore | tropical_forest | tropical_forest_asian | mechanized_mining | Estaño (casiterita en veta) |
| occurrence_0052 | geological_chalcopyrite_copper_ore | tropical_forest | tropical_forest_asian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0067 | geological_alluvial_clay | tropical_forest | tropical_forest_oceanian | surface_collection | Arcilla aluvial |
| occurrence_0068 | geological_volcanic_rock | tropical_forest | tropical_forest_oceanian | surface_collection | Roca volcánica |
| occurrence_0069 | geological_alluvial_gold | tropical_forest | tropical_forest_oceanian | surface_collection | Oro aluvial |
| occurrence_0070 | geological_copper_bearing_deposit | tropical_forest | tropical_forest_oceanian | traditional_mining | Cobre |
| occurrence_0071 | geological_vein_gold | tropical_forest | tropical_forest_oceanian | traditional_mining | Oro en veta |
| occurrence_0072 | geological_nickel_bearing_deposit | tropical_forest | tropical_forest_oceanian | traditional_mining | Níquel |
| occurrence_0073 | geological_nickeliferous_laterite | tropical_forest | tropical_forest_oceanian | mechanized_mining | Níquel (laterita niquelífera) |
| occurrence_0074 | geological_chalcopyrite_copper_ore | tropical_forest | tropical_forest_oceanian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0083 | geological_clay | temperate_forest | temperate_forest_eurasian | surface_collection | Arcilla |
| occurrence_0084 | geological_limestone | temperate_forest | temperate_forest_eurasian | surface_collection | Caliza |
| occurrence_0085 | geological_flint | temperate_forest | temperate_forest_eurasian | surface_collection | Sílex |
| occurrence_0086 | geological_iron_bearing_deposit | temperate_forest | temperate_forest_eurasian | traditional_mining | Hierro |
| occurrence_0087 | geological_copper_bearing_deposit | temperate_forest | temperate_forest_eurasian | traditional_mining | Cobre |
| occurrence_0088 | geological_lead_bearing_deposit | temperate_forest | temperate_forest_eurasian | traditional_mining | Plomo |
| occurrence_0089 | geological_magnetite_iron_ore | temperate_forest | temperate_forest_eurasian | mechanized_mining | Hierro (magnetita) |
| occurrence_0090 | geological_bituminous_coal | temperate_forest | temperate_forest_eurasian | mechanized_mining | Carbón mineral (hulla) |
| occurrence_0105 | geological_clay | temperate_forest | temperate_forest_american | surface_collection | Arcilla |
| occurrence_0106 | geological_granite | temperate_forest | temperate_forest_american | surface_collection | Granito |
| occurrence_0107 | geological_volcanic_obsidian | temperate_forest | temperate_forest_american | surface_collection | Obsidiana en zonas volcánicas |
| occurrence_0108 | geological_copper_bearing_deposit | temperate_forest | temperate_forest_american | traditional_mining | Cobre |
| occurrence_0109 | geological_iron_bearing_deposit | temperate_forest | temperate_forest_american | traditional_mining | Hierro |
| occurrence_0110 | geological_silver_bearing_deposit | temperate_forest | temperate_forest_american | traditional_mining | Plata |
| occurrence_0111 | geological_chalcopyrite_copper_ore | temperate_forest | temperate_forest_american | mechanized_mining | Cobre (calcopirita) |
| occurrence_0112 | geological_magnetite_iron_ore | temperate_forest | temperate_forest_american | mechanized_mining | Hierro (magnetita) |
| occurrence_0127 | geological_sandstone | temperate_forest | temperate_forest_south_african_and_australian | surface_collection | Arenisca |
| occurrence_0128 | geological_clay | temperate_forest | temperate_forest_south_african_and_australian | surface_collection | Arcilla |
| occurrence_0129 | geological_granite | temperate_forest | temperate_forest_south_african_and_australian | surface_collection | Granito |
| occurrence_0130 | geological_vein_gold | temperate_forest | temperate_forest_south_african_and_australian | traditional_mining | Oro en veta |
| occurrence_0131 | geological_copper_bearing_deposit | temperate_forest | temperate_forest_south_african_and_australian | traditional_mining | Cobre |
| occurrence_0132 | geological_iron_bearing_deposit | temperate_forest | temperate_forest_south_african_and_australian | traditional_mining | Hierro |
| occurrence_0133 | geological_gold_bearing_quartz | temperate_forest | temperate_forest_south_african_and_australian | mechanized_mining | Oro (cuarzo aurífero) |
| occurrence_0134 | geological_chalcopyrite_copper_ore | temperate_forest | temperate_forest_south_african_and_australian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0149 | geological_granite | temperate_forest | temperate_forest_boreal | surface_collection | Granito |
| occurrence_0150 | geological_slate | temperate_forest | temperate_forest_boreal | surface_collection | Pizarra |
| occurrence_0151 | geological_clay | temperate_forest | temperate_forest_boreal | surface_collection | Arcilla |
| occurrence_0152 | geological_iron_bearing_deposit | temperate_forest | temperate_forest_boreal | traditional_mining | Hierro |
| occurrence_0153 | geological_copper_bearing_deposit | temperate_forest | temperate_forest_boreal | traditional_mining | Cobre |
| occurrence_0154 | geological_nickel_bearing_deposit | temperate_forest | temperate_forest_boreal | traditional_mining | Níquel |
| occurrence_0155 | geological_magnetite_iron_ore | temperate_forest | temperate_forest_boreal | mechanized_mining | Hierro (magnetita) |
| occurrence_0156 | geological_sulfide_nickel_ore | temperate_forest | temperate_forest_boreal | mechanized_mining | Níquel (sulfuros) |
| occurrence_0171 | geological_gravel | tundra | tundra_north_american_and_greenland | surface_collection | Grava |
| occurrence_0172 | geological_slate | tundra | tundra_north_american_and_greenland | surface_collection | Pizarra |
| occurrence_0173 | geological_granite | tundra | tundra_north_american_and_greenland | surface_collection | Granito |
| occurrence_0174 | geological_iron_bearing_deposit | tundra | tundra_north_american_and_greenland | traditional_mining | Hierro |
| occurrence_0175 | geological_copper_bearing_deposit | tundra | tundra_north_american_and_greenland | traditional_mining | Cobre |
| occurrence_0176 | geological_nickel_bearing_deposit | tundra | tundra_north_american_and_greenland | traditional_mining | Níquel |
| occurrence_0177 | geological_magnetite_iron_ore | tundra | tundra_north_american_and_greenland | mechanized_mining | Hierro (magnetita) |
| occurrence_0178 | geological_sulfide_nickel_ore | tundra | tundra_north_american_and_greenland | mechanized_mining | Níquel (sulfuros) |
| occurrence_0189 | geological_gravel | tundra | tundra_eurasian | surface_collection | Grava |
| occurrence_0190 | geological_granite | tundra | tundra_eurasian | surface_collection | Granito |
| occurrence_0191 | geological_glacial_clay | tundra | tundra_eurasian | surface_collection | Arcilla glacial |
| occurrence_0192 | geological_iron_bearing_deposit | tundra | tundra_eurasian | traditional_mining | Hierro |
| occurrence_0193 | geological_copper_bearing_deposit | tundra | tundra_eurasian | traditional_mining | Cobre |
| occurrence_0194 | geological_nickel_bearing_deposit | tundra | tundra_eurasian | traditional_mining | Níquel |
| occurrence_0195 | geological_magnetite_iron_ore | tundra | tundra_eurasian | mechanized_mining | Hierro (magnetita) |
| occurrence_0196 | geological_chalcopyrite_copper_ore | tundra | tundra_eurasian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0207 | geological_basalt | tundra | tundra_subantarctic | surface_collection | Roca basáltica |
| occurrence_0208 | geological_gravel | tundra | tundra_subantarctic | surface_collection | Grava |
| occurrence_0209 | geological_peat | tundra | tundra_subantarctic | surface_collection | Turba |
| occurrence_0210 | geological_iron_bearing_deposit | tundra | tundra_subantarctic | traditional_mining | Hierro |
| occurrence_0211 | geological_copper_bearing_deposit | tundra | tundra_subantarctic | traditional_mining | Cobre |
| occurrence_0212 | geological_magnetite_iron_ore | tundra | tundra_subantarctic | mechanized_mining | Hierro (magnetita) |
| occurrence_0213 | geological_chalcopyrite_copper_ore | tundra | tundra_subantarctic | mechanized_mining | Cobre (calcopirita) |
| occurrence_0221 | geological_alluvial_clay | savanna | savanna_african | surface_collection | Arcilla aluvial |
| occurrence_0222 | geological_limestone | savanna | savanna_african | surface_collection | Caliza |
| occurrence_0223 | geological_alluvial_gold | savanna | savanna_african | surface_collection | Oro aluvial |
| occurrence_0224 | geological_iron_bearing_deposit | savanna | savanna_african | traditional_mining | Hierro |
| occurrence_0225 | geological_copper_bearing_deposit | savanna | savanna_african | traditional_mining | Cobre |
| occurrence_0226 | geological_vein_gold | savanna | savanna_african | traditional_mining | Oro en veta |
| occurrence_0227 | geological_hematite_iron_ore | savanna | savanna_african | mechanized_mining | Hierro (hematita) |
| occurrence_0228 | geological_gold_bearing_quartz | savanna | savanna_african | mechanized_mining | Oro (cuarzo aurífero) |
| occurrence_0240 | geological_clay | savanna | savanna_american | surface_collection | Arcilla |
| occurrence_0241 | geological_granite | savanna | savanna_american | surface_collection | Granito |
| occurrence_0242 | geological_alluvial_gold | savanna | savanna_american | surface_collection | Oro aluvial |
| occurrence_0243 | geological_copper_bearing_deposit | savanna | savanna_american | traditional_mining | Cobre |
| occurrence_0244 | geological_iron_bearing_deposit | savanna | savanna_american | traditional_mining | Hierro |
| occurrence_0245 | geological_silver_bearing_deposit | savanna | savanna_american | traditional_mining | Plata |
| occurrence_0246 | geological_chalcopyrite_copper_ore | savanna | savanna_american | mechanized_mining | Cobre (calcopirita) |
| occurrence_0247 | geological_hematite_iron_ore | savanna | savanna_american | mechanized_mining | Hierro (hematita) |
| occurrence_0262 | geological_clay | savanna | savanna_eurasian | surface_collection | Arcilla |
| occurrence_0263 | geological_limestone | savanna | savanna_eurasian | surface_collection | Caliza |
| occurrence_0264 | geological_flint | savanna | savanna_eurasian | surface_collection | Sílex |
| occurrence_0265 | geological_iron_bearing_deposit | savanna | savanna_eurasian | traditional_mining | Hierro |
| occurrence_0266 | geological_copper_bearing_deposit | savanna | savanna_eurasian | traditional_mining | Cobre |
| occurrence_0267 | geological_tin_bearing_deposit | savanna | savanna_eurasian | traditional_mining | Estaño |
| occurrence_0268 | geological_magnetite_iron_ore | savanna | savanna_eurasian | mechanized_mining | Hierro (magnetita) |
| occurrence_0269 | geological_bituminous_coal | savanna | savanna_eurasian | mechanized_mining | Carbón mineral (hulla) |
| occurrence_0278 | geological_clay | savanna | savanna_australian | surface_collection | Arcilla |
| occurrence_0279 | geological_sandstone | savanna | savanna_australian | surface_collection | Arenisca |
| occurrence_0280 | geological_iron_rich_laterite | savanna | savanna_australian | surface_collection | Laterita ferruginosa |
| occurrence_0281 | geological_iron_bearing_deposit | savanna | savanna_australian | traditional_mining | Hierro |
| occurrence_0282 | geological_copper_bearing_deposit | savanna | savanna_australian | traditional_mining | Cobre |
| occurrence_0283 | geological_vein_gold | savanna | savanna_australian | traditional_mining | Oro en veta |
| occurrence_0284 | geological_hematite_iron_ore | savanna | savanna_australian | mechanized_mining | Hierro (hematita) |
| occurrence_0285 | geological_gold_bearing_quartz | savanna | savanna_australian | mechanized_mining | Oro (cuarzo aurífero) |
| occurrence_0294 | geological_sand | desert | desert_american | surface_collection | Arena |
| occurrence_0295 | geological_sandstone | desert | desert_american | surface_collection | Arenisca |
| occurrence_0296 | geological_rock_salt | desert | desert_american | surface_collection | Sal gema |
| occurrence_0297 | geological_copper_bearing_deposit | desert | desert_american | traditional_mining | Cobre |
| occurrence_0298 | geological_silver_bearing_deposit | desert | desert_american | traditional_mining | Plata |
| occurrence_0299 | geological_iron_bearing_deposit | desert | desert_american | traditional_mining | Hierro |
| occurrence_0300 | geological_chalcopyrite_copper_ore | desert | desert_american | mechanized_mining | Cobre (calcopirita) |
| occurrence_0301 | geological_hematite_iron_ore | desert | desert_american | mechanized_mining | Hierro (hematita) |
| occurrence_0316 | geological_sand | desert | desert_african_and_arabian | surface_collection | Arena |
| occurrence_0317 | geological_sandstone | desert | desert_african_and_arabian | surface_collection | Arenisca |
| occurrence_0318 | geological_rock_salt | desert | desert_african_and_arabian | surface_collection | Sal gema |
| occurrence_0319 | geological_iron_bearing_deposit | desert | desert_african_and_arabian | traditional_mining | Hierro |
| occurrence_0320 | geological_copper_bearing_deposit | desert | desert_african_and_arabian | traditional_mining | Cobre |
| occurrence_0321 | geological_phosphorite | desert | desert_african_and_arabian | traditional_mining | Fosforita |
| occurrence_0322 | geological_hematite_iron_ore | desert | desert_african_and_arabian | mechanized_mining | Hierro (hematita) |
| occurrence_0323 | geological_apatite_phosphorite | desert | desert_african_and_arabian | mechanized_mining | Fosforita (apatita) |
| occurrence_0332 | geological_sand | desert | desert_central_asian | surface_collection | Arena |
| occurrence_0333 | geological_gravel | desert | desert_central_asian | surface_collection | Grava |
| occurrence_0334 | geological_rock_salt | desert | desert_central_asian | surface_collection | Sal gema |
| occurrence_0335 | geological_copper_bearing_deposit | desert | desert_central_asian | traditional_mining | Cobre |
| occurrence_0336 | geological_iron_bearing_deposit | desert | desert_central_asian | traditional_mining | Hierro |
| occurrence_0337 | geological_tin_bearing_deposit | desert | desert_central_asian | traditional_mining | Estaño |
| occurrence_0338 | geological_chalcopyrite_copper_ore | desert | desert_central_asian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0339 | geological_magnetite_iron_ore | desert | desert_central_asian | mechanized_mining | Hierro (magnetita) |
| occurrence_0348 | geological_sand | desert | desert_australian | surface_collection | Arena |
| occurrence_0349 | geological_sandstone | desert | desert_australian | surface_collection | Arenisca |
| occurrence_0350 | geological_surface_opal | desert | desert_australian | surface_collection | Ópalo superficial |
| occurrence_0351 | geological_iron_bearing_deposit | desert | desert_australian | traditional_mining | Hierro |
| occurrence_0352 | geological_copper_bearing_deposit | desert | desert_australian | traditional_mining | Cobre |
| occurrence_0353 | geological_vein_gold | desert | desert_australian | traditional_mining | Oro en veta |
| occurrence_0354 | geological_hematite_iron_ore | desert | desert_australian | mechanized_mining | Hierro (hematita) |
| occurrence_0355 | geological_gold_bearing_quartz | desert | desert_australian | mechanized_mining | Oro (cuarzo aurífero) |
| occurrence_0364 | geological_sea_salt | marine | marine_tropical_coast | surface_collection | Sal marina |
| occurrence_0365 | geological_calcareous_sand | marine | marine_tropical_coast | surface_collection | Arena calcárea |
| occurrence_0366 | geological_seashells | marine | marine_tropical_coast | surface_collection | Conchas marinas |
| occurrence_0367 | geological_coastal_limestone | marine | marine_tropical_coast | traditional_mining | Caliza costera |
| occurrence_0368 | geological_coastal_gypsum | marine | marine_tropical_coast | traditional_mining | Yeso costero |
| occurrence_0369 | geological_polymetallic_nodules | marine | marine_tropical_coast | mechanized_mining | Nódulos polimetálicos (manganeso, níquel y cobre) |
| occurrence_0377 | geological_sea_salt | marine | marine_temperate_coast_and_sea | surface_collection | Sal marina |
| occurrence_0378 | geological_silica_sand | marine | marine_temperate_coast_and_sea | surface_collection | Arena silícea |
| occurrence_0379 | geological_coastal_gravel | marine | marine_temperate_coast_and_sea | surface_collection | Grava costera |
| occurrence_0380 | geological_coastal_limestone | marine | marine_temperate_coast_and_sea | traditional_mining | Caliza costera |
| occurrence_0381 | geological_coastal_gypsum | marine | marine_temperate_coast_and_sea | traditional_mining | Yeso costero |
| occurrence_0382 | geological_polymetallic_nodules | marine | marine_temperate_coast_and_sea | mechanized_mining | Nódulos polimetálicos (manganeso, níquel y cobre) |
| occurrence_0390 | geological_coastal_gravel | marine | marine_polar_and_subpolar | surface_collection | Grava costera |
| occurrence_0391 | geological_basalt | marine | marine_polar_and_subpolar | surface_collection | Roca basáltica |
| occurrence_0392 | geological_sand | marine | marine_polar_and_subpolar | surface_collection | Arena |
| occurrence_0393 | geological_coastal_limestone | marine | marine_polar_and_subpolar | traditional_mining | Caliza costera |
| occurrence_0394 | geological_coastal_gypsum | marine | marine_polar_and_subpolar | traditional_mining | Yeso costero |
| occurrence_0395 | geological_polymetallic_nodules | marine | marine_polar_and_subpolar | mechanized_mining | Nódulos polimetálicos (manganeso, níquel y cobre) |
| occurrence_0404 | geological_estuarine_clay | marine | marine_coastal_wetlands | surface_collection | Arcilla estuarina |
| occurrence_0405 | geological_sand | marine | marine_coastal_wetlands | surface_collection | Arena |
| occurrence_0406 | geological_sea_salt_in_suitable_saltworks | marine | marine_coastal_wetlands | surface_collection | Sal marina (en salinas apropiadas) |
| occurrence_0407 | geological_gypsum_in_evaporite_deposits | marine | marine_coastal_wetlands | traditional_mining | Yeso (en depósitos evaporíticos) |
| occurrence_0408 | geological_limestone_in_carbonate_formations | marine | marine_coastal_wetlands | traditional_mining | Caliza (donde exista formación carbonatada) |
| occurrence_0409 | geological_deep_rock_salt | marine | marine_coastal_wetlands | mechanized_mining | Sal gema (en depósitos profundos apropiados) |
| occurrence_0410 | geological_deep_gypsum | marine | marine_coastal_wetlands | mechanized_mining | Yeso (en yacimientos profundos) |
| occurrence_0418 | geological_granite | alpine | alpine_andean | surface_collection | Granito |
| occurrence_0419 | geological_clay | alpine | alpine_andean | surface_collection | Arcilla |
| occurrence_0420 | geological_alluvial_gold | alpine | alpine_andean | surface_collection | Oro aluvial |
| occurrence_0421 | geological_copper_bearing_deposit | alpine | alpine_andean | traditional_mining | Cobre |
| occurrence_0422 | geological_silver_bearing_deposit | alpine | alpine_andean | traditional_mining | Plata |
| occurrence_0423 | geological_tin_bearing_deposit | alpine | alpine_andean | traditional_mining | Estaño |
| occurrence_0424 | geological_chalcopyrite_copper_ore | alpine | alpine_andean | mechanized_mining | Cobre (calcopirita) |
| occurrence_0425 | geological_argentite_silver_ore | alpine | alpine_andean | mechanized_mining | Plata (argentita) |
| occurrence_0436 | geological_granite | alpine | alpine_asian | surface_collection | Granito |
| occurrence_0437 | geological_slate | alpine | alpine_asian | surface_collection | Pizarra |
| occurrence_0438 | geological_rock_salt | alpine | alpine_asian | surface_collection | Sal gema |
| occurrence_0439 | geological_copper_bearing_deposit | alpine | alpine_asian | traditional_mining | Cobre |
| occurrence_0440 | geological_iron_bearing_deposit | alpine | alpine_asian | traditional_mining | Hierro |
| occurrence_0441 | geological_vein_gold | alpine | alpine_asian | traditional_mining | Oro en veta |
| occurrence_0442 | geological_magnetite_iron_ore | alpine | alpine_asian | mechanized_mining | Hierro (magnetita) |
| occurrence_0443 | geological_chalcopyrite_copper_ore | alpine | alpine_asian | mechanized_mining | Cobre (calcopirita) |
| occurrence_0453 | geological_limestone | alpine | alpine_european | surface_collection | Caliza |
| occurrence_0454 | geological_granite | alpine | alpine_european | surface_collection | Granito |
| occurrence_0455 | geological_slate | alpine | alpine_european | surface_collection | Pizarra |
| occurrence_0456 | geological_iron_bearing_deposit | alpine | alpine_european | traditional_mining | Hierro |
| occurrence_0457 | geological_copper_bearing_deposit | alpine | alpine_european | traditional_mining | Cobre |
| occurrence_0458 | geological_lead_bearing_deposit | alpine | alpine_european | traditional_mining | Plomo |
| occurrence_0459 | geological_magnetite_iron_ore | alpine | alpine_european | mechanized_mining | Hierro (magnetita) |
| occurrence_0460 | geological_galena_lead_ore | alpine | alpine_european | mechanized_mining | Plomo (galena) |
| occurrence_0470 | geological_volcanic_rock | alpine | alpine_african | surface_collection | Roca volcánica |
| occurrence_0471 | geological_pumice | alpine | alpine_african | surface_collection | Piedra pómez |
| occurrence_0472 | geological_clay | alpine | alpine_african | surface_collection | Arcilla |
| occurrence_0473 | geological_iron_bearing_deposit | alpine | alpine_african | traditional_mining | Hierro |
| occurrence_0474 | geological_copper_bearing_deposit | alpine | alpine_african | traditional_mining | Cobre |
| occurrence_0475 | geological_vein_gold | alpine | alpine_african | traditional_mining | Oro en veta |
| occurrence_0476 | geological_magnetite_iron_ore | alpine | alpine_african | mechanized_mining | Hierro (magnetita) |
| occurrence_0477 | geological_gold_bearing_quartz | alpine | alpine_african | mechanized_mining | Oro (cuarzo aurífero) |
