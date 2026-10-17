# `data/world/world.catalog.guide.json`

[Source JSON](../../../data/world/world.catalog.guide.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.3.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.4.0"` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"world_catalog_design_guide"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"source_converted_requires_species_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `source` | `object` | 1/1 | Provenance of the supplied document snapshot. | `—` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `worldRules` | `object` | 1/1 | High-level world-generation decisions. | `—` |
| `elevationLevels` | `array<object>` | 1/1 | Elevation categories independent of biome. | `—` |
| `geographicModifiers` | `array<object>` | 1/1 | Geographic feature categories affecting habitat and access. | `—` |
| `biomes` | `array<object>` | 1/1 | Interface biome categories, not sufficient ecological placement rules. | `—` |
| `regionalVariants` | `array<object>` | 1/1 | Regional/habitat variants linked to their parent biome. | `—` |
| `resourceOccurrences` | `array<object>` | 1/1 | Individual source listings linked to candidates, variants and extraction methods. | `—` |
| `generationPipeline` | `array<string>` | 1/1 | Ordered design steps, not executable generator code. | `["generate_terrain_water_static_climate_and_biogeographic_regions", "assign_biomes_and_geographic_modifiers", "g…` |
| `speciesCompletionChecklist` | `array<string>` | 1/1 | Review tasks before promoting a candidate to an approved definition. | `["resolve_to_individual_species_or_explicit_game_taxon", "verify_scientific_name_and_native_distribution", "spli…` |
| `reviewIssues` | `array<object>` | 1/1 | Recorded source discrepancies and unresolved design questions. | `—` |
| `sourceDistributionNotes` | `array<string>` | 1/1 | Verbatim source distribution notes, not extra species. | `["Los siete biomas son categorías de interfaz; cada subtipo mantiene clima, terreno, hábitat y región propios.",…` |
| `agricultureSectionSource` | `array<string>` | 1/1 | Verbatim source agriculture section retained for provenance. | `["5. Catálogo agrícola y vegetal inicial", "Los recursos agrícolas deben distinguir tres estados conceptuales: (…` |
| `summary` | `object` | 1/1 | Counts used to check catalog completeness. | `—` |
| `hexDefinitionGuide` | `object` | 1/1 | Proposed tile field names and state separation; not an implemented tile schema. | `—` |
| `depositDefinitionGuide` | `object` | 1/1 | Proposed deposit fields; not a completed deposit definition. | `—` |
| `catalogFiles` | `object` | 1/1 | Sibling catalog locations resolved relative to the world-guide JSON file. | `—` |
| `repositoryPackaging` | `object` | 1/1 | Metadata describing the split from the combined guide. | `—` |

### `$.source`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `title` | `string` | 1/1 | Document or schema title. | `"Documentacion Evolve"` |
| `format` | `string` | 1/1 | Format of the source snapshot or localization representation. | `"docx_snapshot"` |
| `connectorFileId` | `string` | 1/1 | Exact source connector identifier, retained for provenance. | `"11FrriHGZ9AKnrXFND-VNWzmNKJo_U2aCS9OFZyWo9c8"` |
| `sha256` | `string` | 1/1 | SHA-256 fingerprint of the source document snapshot. | `"151ea42d39ce1bc9d26d76e18dc1a9d8a5fbb9f888519c240d99fe7793271308"` |
| `snapshotOnly` | `boolean` | 1/1 | True means extraction used the attached snapshot, not a live revision check. | `true` |
| `originalDocumentModified` | `boolean` | 1/1 | Whether conversion modified the original source document; false here. | `false` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `reason` | `string` | 1/1 | Explanation of the runtime restriction. | `"This is a structured design guide, not a scientifically verified species catalog or executable world generator."` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"null means unresolved; it never means zero, none, unrestricted or approved."` |
| `visibleText` | `string` | 1/1 | Policy distinguishing localized visible text from raw source provenance. | `"name and description use language maps; sourceText and sourceLabel preserve verbatim Spanish provenance and mus…` |
| `flatCollections` | `string` | 1/1 | Policy requiring flat collections linked by IDs. | `"All definitions are stored in flat collections and connected by stable IDs."` |
| `preserveSpeciesResearch` | `string` | 1/1 | Rule preserving research identity when taxonomy is refined. | `"IDs must survive later taxonomy refinement or receive explicit alias/migration rules."` |
| `wildAndDomestic` | `string` | 1/1 | Rule separating wild presence, cultivation, domestication and production. | `"Wild presence, cultivation knowledge, domestication and established crop production are separate states."` |
| `distribution` | `string` | 1/1 | Rule requiring verified native regions and habitats for spawning. | `"Biome compatibility does not imply universal native distribution."` |
| `geology` | `string` | 1/1 | Rule controlling mineral placement independently from biome labels. | `"Mineral distribution is controlled by geology, not mandatory biome resource lists."` |
| `miningStages` | `string` | 1/1 | Interpretation of extraction methods without inventing exclusive eras. | `"Extraction methods describe capabilities, not exclusive material eras."` |
| `scope` | `string` | 1/1 | Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object. | `"Mechanized mining and seabed nodules remain future content outside the initial medieval scope."` |

### `$.worldRules`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `hexagonalMap` | `boolean` | 1/1 | Whether the map uses hexagonal tiles. | `true` |
| `dynamicWeatherEnabled` | `boolean` | 1/1 | Whether dynamic weather is included; currently false. | `false` |
| `seasonsEnabled` | `boolean` | 1/1 | Whether seasons are included; currently false. | `false` |
| `dynamicClimateDisastersEnabled` | `boolean` | 1/1 | Whether dynamic climate disasters are included; currently false. | `false` |
| `staticEnvironmentalConditionsUsed` | `boolean` | 1/1 | Whether static environmental conditions constrain generation. | `true` |
| `maximumRegionalVariantsPerBiome` | `integer` | 1/1 | Current maximum regional variants per biome, not a spawn probability. | `4` |
| `resourceDiscoverySeparateFromExistence` | `boolean` | 1/1 | Resources may exist before a civilization discovers them. | `true` |
| `potentialCultivationSeparateFromEstablishedCrops` | `boolean` | 1/1 | Cultivability does not imply an already established crop. | `true` |

### `$.elevationLevels[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `integer` | 4/4 | Numeric elevation category 0–3, not an entity ID with a prefix. | `0` |
| `name` | `object` | 4/4 | Player-visible label using language keys. | `—` |
| `ordinaryLandTraversal` | `boolean \| string` | 4/4 | Passability flag or explanatory restriction; currently boolean or string. | `"depends_on_land_or_water_surface"` |
| `movementAndConstructionRestrictions` | `null` | 1/4 | Explanatory movement and construction restrictions. | `null` |
| `conventionalSettlementsAllowed` | `boolean` | 1/4 | Whether conventional settlements are permitted at this level. | `false` |

### `$.elevationLevels[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 4/4 | English visible text. | `"Sea Level"` |
| `es` | `string` | 4/4 | Spanish visible text. | `"Nivel del mar"` |

### `$.geographicModifiers[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 6/6 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"river_floodplain"` |
| `name` | `object` | 6/6 | Player-visible label using language keys. | `—` |

### `$.geographicModifiers[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 6/6 | English visible text. | `"River and Floodplain"` |
| `es` | `string` | 6/6 | Spanish visible text. | `"Río y llanura aluvial"` |

### `$.biomes[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"tropical_forest"` |
| `name` | `object` | 7/7 | Player-visible label using language keys. | `—` |
| `interfaceCategoryOnly` | `boolean` | 7/7 | True means this biome label is a UI category rather than a complete habitat definition. | `true` |

### `$.biomes[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 7/7 | English visible text. | `"Tropical Forest"` |
| `es` | `string` | 7/7 | Spanish visible text. | `"Bosque tropical"` |

### `$.regionalVariants[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 27/27 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"tropical_forest_american"` |
| `biomeId` | `string` | 27/27 | Reference to a biome definition. | `"tropical_forest"` |
| `name` | `object` | 27/27 | Player-visible label using language keys. | `—` |
| `nativeRegionIds` | `array<?>` | 27/27 | References to native regions; empty means unresolved, not worldwide distribution. | `[]` |
| `resolutionStatus` | `string` | 27/27 | Task still required to resolve a candidate or regional restriction. | `"regional_constraints_require_definition"` |

### `$.regionalVariants[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 27/27 | English visible text. | `"American"` |
| `es` | `string` | 27/27 | Spanish visible text. | `"Americano (selvas húmedas y bosques secos)"` |

### `$.resourceOccurrences[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 485/485 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"occurrence_0001"` |
| `definitionId` | `string` | 485/485 | Reference to the candidate definition; not an individual world population ID. | `"geological_alluvial_clay"` |
| `kind` | `string` | 485/485 | Discriminator identifying this document or candidate category. | `"geological"` |
| `biomeId` | `string` | 485/485 | Reference to a biome definition. | `"tropical_forest"` |
| `variantId` | `string` | 485/485 | Reference to a regional variant. | `"tropical_forest_american"` |
| `extractionMethodId` | `null \| string` | 485/485 | Extraction-stage identifier from the source; not a verified recipe. | `"surface_collection"` |
| `sourceText` | `string` | 485/485 | Exact Spanish source occurrence text; preserve for audit, not game UI. | `"Arcilla aluvial"` |
| `constraintsStatus` | `string` | 485/485 | Progress in converting qualitative source restrictions into executable conditions. | `"qualitative_source_constraints_preserved_pending_formalization"` |
| `spawnProbability` | `null` | 485/485 | Spawn probability, currently unresolved; null is not zero or guaranteed. | `null` |
| `guaranteedPresence` | `boolean` | 485/485 | Whether this record guarantees presence; false does not imply impossibility. | `false` |
| `runtimeEnabled` | `boolean` | 485/485 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.reviewIssues[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"regional_variant_count"` |
| `sourceClaim` | `integer` | 2/7 | Count claimed by the source; compare with actualCount. | `26` |
| `actualCount` | `integer` | 2/7 | Count obtained from the enumerated source records. | `27` |
| `resolution` | `string` | 7/7 | Documented interpretation or next review action. | `"Use the enumerated 27 variants; retain the discrepancy for review."` |

### `$.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `biomeCount` | `integer` | 1/1 | Number of biome records. | `7` |
| `regionalVariantCount` | `integer` | 1/1 | Number of regional variants. | `27` |
| `plantCandidateCount` | `integer` | 1/1 | Number of regional plant candidate records. | `129` |
| `animalCandidateCount` | `integer` | 1/1 | Number of animal candidate records. | `134` |
| `geologicalCandidateCount` | `integer` | 1/1 | Number of geological candidate records. | `57` |
| `sourceOccurrenceCount` | `integer` | 1/1 | Number of source occurrence records. | `485` |
| `agriculturalCropCandidateCount` | `integer` | 1/1 | Number of crop candidate records. | `21` |

### `$.hexDefinitionGuide`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `definitionFields` | `array<string>` | 1/1 | Names of proposed static fields; these strings are not actual nested properties. | `["terrainType", "elevationLevel", "surfaceType"]` |
| `stateFields` | `array<string>` | 1/1 | Names of proposed mutable instance fields; types are still pending. | `["presentPopulationIds", "presentDepositIds", "discoveryByCivilization"]` |
| `numericRanges` | `null` | 1/1 | Numerical ranges awaiting design. | `null` |
| `separation` | `string` | 1/1 | Explains the boundary between reusable definitions and generated map state. | `"The actual generated map and its discoveries belong to GameState; catalog definitions and generation constraint…` |

### `$.depositDefinitionGuide`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `fields` | `array<string>` | 1/1 | Names of proposed fields, not instantiated records. | `["materialId", "reserveAmount", "grade"]` |
| `numericalValues` | `null` | 1/1 | Numerical deposit parameters awaiting design. | `null` |
| `depletionAndRegenerationRules` | `null` | 1/1 | Rules for reserve depletion and renewal, still unresolved. | `null` |
| `stateSeparation` | `string` | 1/1 | Explains why reserves and discovery belong to game state. | `"Actual reserves and discovery belong to each deposit instance in GameState."` |

### `$.catalogFiles`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `plantCandidates` | `string` | 1/1 | Relative path to the plant and crop guide. | `"../plants/plants.catalog.guide.json"` |
| `animalCandidates` | `string` | 1/1 | Relative path to the animal guide. | `"../animals/animals.catalog.guide.json"` |
| `geologicalCandidates` | `string` | 1/1 | Relative path to the geological guide. | `"../minerals/minerals.catalog.guide.json"` |
| `resources` | `string` | 1/1 | Resource records at the root, or the relative resource-catalog path inside catalogFiles. | `"../resources/resources.catalog.guide.json"` |
| `plantBiology` | `string` | 1/1 | Relative path from the world manifest to the flora biological catalog. | `"../plants/plants.biological.catalog.json"` |
| `animalBiology` | `string` | 1/1 | Relative path from the world manifest to the animal biological catalog. | `"../animals/animals.biological.catalog.json"` |

### `$.repositoryPackaging`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `layout` | `string` | 1/1 | Packaging strategy: flat linked catalogs. | `"flat_linked_catalogs"` |
| `change` | `string` | 1/1 | Description of the packaging change. | `"Candidate collections were moved without renaming IDs; occurrence references resolve across the linked catalogs."` |
| `sourceOccurrenceCount` | `integer` | 1/1 | Number of source occurrence records. | `485` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.3.0",
  "contentVersion": "0.4.0",
  "kind": "world_catalog_design_guide",
  "status": "source_converted_requires_species_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "source": {
    "title": "Documentacion Evolve",
    "format": "docx_snapshot",
    "connectorFileId": "11FrriHGZ9AKnrXFND-VNWzmNKJo_U2aCS9OFZyWo9c8",
    "sha256": "151ea42d39ce1bc9d26d76e18dc1a9d8a5fbb9f888519c240d99fe7793271308",
    "snapshotOnly": true,
    "originalDocumentModified": false
  },
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "reason": "This is a structured design guide, not a scientifically verified species catalog or executable world generator.",
    "unknownValues": "null means unresolved; it never means zero, none, unrestricted or approved.",
    "visibleText": "name and description use language maps; sourceText and sourceLabel preserve verbatim Spanish provenance and must not be displayed as localized game text.",
    "flatCollections": "All definitions are stored in flat collections and connected by stable IDs.",
    "preserveSpeciesResearch": "IDs must survive later taxonomy refinement or receive explicit alias/migration rules.",
    "wildAndDomestic": "Wild presence, cultivation knowledge, domestication and established crop production are separate states.",
    "distribution": "Biome compatibility does not imply universal native distribution.",
    "geology": "Mineral distribution is controlled by geology, not mandatory biome resource lists.",
    "miningStages": "Extraction methods describe capabilities, not exclusive material eras.",
    "scope": "Mechanized mining and seabed nodules remain future content outside the initial medieval scope."
  },
  "worldRules": {
    "hexagonalMap": true,
    "dynamicWeatherEnabled": false,
    "seasonsEnabled": false,
    "dynamicClimateDisastersEnabled": false,
    "staticEnvironmentalConditionsUsed": true,
    "maximumRegionalVariantsPerBiome": 4,
    "resourceDiscoverySeparateFromExistence": true,
    "potentialCultivationSeparateFromEstablishedCrops": true
  },
  "elevationLevels": [
    {
      "id": 0,
      "name": {
        "en": "Sea Level",
        "es": "Nivel del mar"
      },
      "ordinaryLandTraversal": "depends_on_land_or_water_surface"
    },
    {
      "id": 1,
      "name": {
        "en": "Middle Elevation",
        "es": "Nivel medio"
      },
      "ordinaryLandTraversal": true
    },
    {
      "id": 2,
      "name": {
        "en": "High Elevation",
        "es": "Nivel alto"
      },
      "ordinaryLandTraversal": true,
      "movementAndConstructionRestrictions": null
    },
    {
      "id": 3,
      "name": {
        "en": "Impassable Summits",
        "es": "Cumbres infranqueables"
      },
      "ordinaryLandTraversal": false,
      "conventionalSettlementsAllowed": false
    }
  ],
  "geographicModifiers": [
    {
      "id": "river_floodplain",
      "name": {
        "en": "River and Floodplain",
        "es": "Río y llanura aluvial"
      }
    }
  ],
  "biomes": [
    {
      "id": "tropical_forest",
      "name": {
        "en": "Tropical Forest",
        "es": "Bosque tropical"
      },
      "interfaceCategoryOnly": true
    }
  ],
  "regionalVariants": [
    {
      "id": "tropical_forest_american",
      "biomeId": "tropical_forest",
      "name": {
        "en": "American",
        "es": "Americano (selvas húmedas y bosques secos)"
      },
      "nativeRegionIds": [],
      "resolutionStatus": "regional_constraints_require_definition"
    }
  ],
  "resourceOccurrences": [
    {
      "id": "occurrence_0001",
      "definitionId": "geological_alluvial_clay",
      "kind": "geological",
      "biomeId": "tropical_forest",
      "variantId": "tropical_forest_american",
      "extractionMethodId": "surface_collection",
      "sourceText": "Arcilla aluvial",
      "constraintsStatus": "qualitative_source_constraints_preserved_pending_formalization",
      "spawnProbability": null,
      "guaranteedPresence": false,
      "runtimeEnabled": false
    }
  ],
  "generationPipeline": [
    "generate_terrain_water_static_climate_and_biogeographic_regions",
    "assign_biomes_and_geographic_modifiers",
    "generate_geological_provinces_and_candidate_deposits",
    "distribute_native_wild_species_using_region_and_habitat",
    "evaluate_soil_fertility_and_cultivation_suitability",
    "apply_visibility_discovery_and_exploitation_capabilities",
    "validate_alternative_development_trade_and_expansion_paths"
  ],
  "speciesCompletionChecklist": [
    "resolve_to_individual_species_or_explicit_game_taxon",
    "verify_scientific_name_and_native_distribution",
    "split_regional_groups_and_distinguish_wild_ancestors",
    "define_ecological_compatibility",
    "define_propagation_and_cultivation_or_animal_management",
    "define_material_resources_and_products",
    "define_technology_requirements_and_scope",
    "define_domestication_criteria_and_temporal_scope",
    "define_balance_and_validation_scenarios"
  ],
  "reviewIssues": [
    {
      "id": "regional_variant_count",
      "sourceClaim": 26,
      "actualCount": 27,
      "resolution": "Use the enumerated 27 variants; retain the discrepancy for review."
    },
    {
      "id": "biome_count",
      "sourceClaim": 10,
      "actualCount": 7,
      "resolution": "The pending-decisions paragraph says ten; the detailed catalog and latest history specify seven."
    },
    {
      "id": "broad_taxa",
      "resolution": "Keep regional groups as candidates; do not silently choose a species."
    },
    {
      "id": "possible_duplicate_taxa",
      "resolution": "Similar names and habitat-qualified duplicates retain separate candidate IDs until verified and merged explicitly."
    },
    {
      "id": "marine_nodules",
      "resolution": "Do not infer coastal shallow-water availability from their placement in marine UI variants; require verified seabed geology and future extraction."
    },
    {
      "id": "tundra_lichens",
      "resolution": "Lichens are retained under the source flora category for traceability; scientific classification must be resolved separately."
    },
    {
      "id": "fauna_products",
      "resolution": "Potential outputs are not verified yields or automatic unlocks; milk, eggs, pearls and work require species-appropriate conditions."
    }
  ],
  "sourceDistributionNotes": [
    "Los siete biomas son categorías de interfaz; cada subtipo mantiene clima, terreno, hábitat y región propios.",
    "Bosque tropical húmedo y bosque tropical seco no comparten automáticamente especies ni rendimientos.",
    "La taiga, el matorral mediterráneo, la sabana tropical y la estepa templada conservan condiciones ecológicas distintas."
  ],
  "agricultureSectionSource": [
    "5. Catálogo agrícola y vegetal inicial",
    "Los recursos agrícolas deben distinguir tres estados conceptuales: (A) planta silvestre presente en el mapa; (B) especie conocida y susceptible de domesticación o cultivo; (C) cultivo domesticado y producido por la civilización. Una planta cultivable no se convierte automáticamente en alimento agrícola disponible.",
    "5.1. Granos y cereales",
    "Trigo y cebada: origen y difusión vinculados históricamente al sudoeste asiático; aptos para regiones templadas o mediterráneas adecuadas. Arroz: ambientes cálidos y húmedos o con agua gestionada, con origen y difusión regionales propios. Maíz: origen mesoamericano y posterior expansión. Sorgo y mijo: alternativas relevantes en entornos cálidos y relativamente secos.",
    "5.2. Tubérculos y raíces",
    "Papa: domesticación andina y aptitud para determinados ambientes de altura o templados frescos. Yuca/mandioca: origen sudamericano y aptitud tropical. Otros tubérculos locales podrán añadirse al catálogo regional.",
    "5.3. Legumbres y hortalizas",
    "Frijoles, lentejas, garbanzos, guisantes y calabazas son familias o especies con orígenes y necesidades diferentes. La lista definitiva deberá distinguir especies concretas, regiones nativas y técnicas agrícolas.",
    "5.4. Frutales, productos especiales y fibras",
    "Vid, olivo, higuera y palmera datilera para regiones compatibles; cacao en zonas tropicales americanas adecuadas; café en ambientes tropicales de altura y regiones históricas de origen; caña de azúcar en climas cálidos y húmedos; algodón y otras fibras según especie y región. Su presencia silvestre, domesticación y circulación por comercio se definirán por separado.",
    "5.5. Reglas para especies y distribución",
    "Cada especie vegetal tendrá, como mínimo, nombre, categoría, región de origen, condiciones ecológicas, estado silvestre o domesticado, productos posibles y conocimientos requeridos. El comercio, las migraciones y la exploración podrán introducir especies en regiones donde no son nativas, siempre que las condiciones permitan cultivarlas. No se asume que todos los biomas del mundo compartan las mismas especies."
  ],
  "summary": {
    "biomeCount": 7,
    "regionalVariantCount": 27,
    "plantCandidateCount": 129,
    "animalCandidateCount": 134,
    "geologicalCandidateCount": 57,
    "sourceOccurrenceCount": 485,
    "agriculturalCropCandidateCount": 21
  },
  "hexDefinitionGuide": {
    "definitionFields": [
      "terrainType",
      "elevationLevel",
      "surfaceType",
      "biomeId",
      "regionalVariantId",
      "staticTemperature",
      "staticMoisture",
      "freshwaterAvailability",
      "soilCharacteristics",
      "fertility",
      "biogeographicRegionId",
      "geologicalProvinceId",
      "geographicModifierIds"
    ],
    "stateFields": [
      "presentPopulationIds",
      "presentDepositIds",
      "discoveryByCivilization",
      "territorialControl",
      "constructionIds"
    ],
    "numericRanges": null,
    "separation": "The actual generated map and its discoveries belong to GameState; catalog definitions and generation constraints belong to GameDefinitions."
  },
  "depositDefinitionGuide": {
    "fields": [
      "materialId",
      "reserveAmount",
      "grade",
      "accessibility",
      "discoveryState",
      "extractionTechnologyIds",
      "processingRecipeIds"
    ],
    "numericalValues": null,
    "depletionAndRegenerationRules": null,
    "stateSeparation": "Actual reserves and discovery belong to each deposit instance in GameState."
  },
  "catalogFiles": {
    "plantCandidates": "../plants/plants.catalog.guide.json",
    "animalCandidates": "../animals/animals.catalog.guide.json",
    "geologicalCandidates": "../minerals/minerals.catalog.guide.json",
    "resources": "../resources/resources.catalog.guide.json",
    "plantBiology": "../plants/plants.biological.catalog.json",
    "animalBiology": "../animals/animals.biological.catalog.json"
  },
  "repositoryPackaging": {
    "layout": "flat_linked_catalogs",
    "change": "Candidate collections were moved without renaming IDs; occurrence references resolve across the linked catalogs.",
    "sourceOccurrenceCount": 485
  }
}
```

## Proposed future tile and deposit fields

These names currently occur only as strings in guide lists. Their final types, nesting and numeric units/ranges are not yet specified; this table is not an executable schema. A generated tile or deposit instance belongs to GameState, even for values fixed after generation.

| Guide list | Proposed field | Meaning | Type/readiness |
| --- | --- | --- | --- |
| `hexDefinitionGuide.definitionFields` | `terrainType` | Terrain category. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `elevationLevel` | Elevation category. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `surfaceType` | Land or water surface. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `biomeId` | Biome reference. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `regionalVariantId` | Regional variant reference. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `staticTemperature` | Static thermal conditions. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `staticMoisture` | Static moisture conditions. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `freshwaterAvailability` | Freshwater availability. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `soilCharacteristics` | Soil properties. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `fertility` | Fertility parameters. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `biogeographicRegionId` | Biogeographic region reference. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `geologicalProvinceId` | Geological province reference. | TBD; design only |
| `hexDefinitionGuide.definitionFields` | `geographicModifierIds` | Geographic modifier references. | TBD; design only |
| `hexDefinitionGuide.stateFields` | `presentPopulationIds` | Populations present on the tile. | TBD; design only |
| `hexDefinitionGuide.stateFields` | `presentDepositIds` | Deposit instances present on the tile. | TBD; design only |
| `hexDefinitionGuide.stateFields` | `discoveryByCivilization` | Per-civilization discoveries. | TBD; design only |
| `hexDefinitionGuide.stateFields` | `territorialControl` | Current territorial ownership/control. | TBD; design only |
| `hexDefinitionGuide.stateFields` | `constructionIds` | Constructions on the tile. | TBD; design only |
| `depositDefinitionGuide.fields` | `materialId` | Material associated with a deposit. | TBD; design only |
| `depositDefinitionGuide.fields` | `reserveAmount` | Remaining deposit reserve. | TBD; design only |
| `depositDefinitionGuide.fields` | `grade` | Material concentration/quality. | TBD; design only |
| `depositDefinitionGuide.fields` | `accessibility` | Access restrictions. | TBD; design only |
| `depositDefinitionGuide.fields` | `discoveryState` | Deposit discovery status. | TBD; design only |
| `depositDefinitionGuide.fields` | `extractionTechnologyIds` | Extraction technology references. | TBD; design only |
| `depositDefinitionGuide.fields` | `processingRecipeIds` | Processing recipe references. | TBD; design only |
