# Identifiers and tags

[Resource catalog and relationships](resources.md)

Complete nested JSON structures, types and examples: [JSON reference](json-structures.md).

Status: accepted naming direction; existing catalogs have NOT been migrated. Example numbers do not reserve IDs.

A final definition has `id: "PLT#000001"` and `tag: "triticum_aestivum"`. The prefix is exactly three uppercase English letters. The suffix is six decimal digits starting at 000001, allocated independently per prefix. `#` is part of the ID; it is not a URL anchor.

| Entity | Prefix | Example ID | Example tag |
| --- | --- | --- | --- |
| Biome | `BIO` | `BIO#000001` | `tropical_rainforest` |
| Regional Variant | `VAR` | `VAR#000001` | `amazon_rainforest` |
| Geographic Region | `REG` | `REG#000001` | `south_america` |
| Terrain | `TER` | `TER#000001` | `plain` |
| Soil | `SOL` | `SOL#000001` | `clay_soil` |
| Geological Formation | `GEO` | `GEO#000001` | `alluvial_deposit` |
| Plant Species | `PLT` | `PLT#000001` | `triticum_aestivum` |
| Animal Species | `ANM` | `ANM#000001` | `capra_aegagrus` |
| Fungus Species | `FNG` | `FNG#000001` | `agaricus_bisporus` |
| Resource | `RES` | `RES#000001` | `wheat_grain` |
| Deposit Type | `DEP` | `DEP#000001` | `copper_ore_deposit` |
| Distribution Rule | `DST` | `DST#000001` | `wild_wheat_distribution` |
| Technology | `TEC` | `TEC#000001` | `basic_foraging` |
| Item | `ITM` | `ITM#000001` | `stone_sickle` |
| Recipe | `RCP` | `RCP#000001` | `woven_basket` |
| Building | `BLD` | `BLD#000001` | `granary` |
| Improvement | `IMP` | `IMP#000001` | `irrigation_channel` |
| Capability | `CAP` | `CAP#000001` | `gather_wild_plants` |
| Eureka | `EUR` | `EUR#000001` | `repeated_plant_gathering` |

## Rules

- IDs are unique across definitions, permanent and never recycled. Deleting an entry retires its ID.
- Tags are English `snake_case`, unique within each entity type. Translations never identify entities.
- References use IDs, not names or translated labels. Numbers encode no order, level, geography or evolutionary relationship.
- Definitions and instances are different: a population has its own `instanceId` and a `definitionId` referencing its species. Instance format is a future save-game decision.
- Species, harvested resources, deposit types and spawn rules have different identities. Grain is not a plant, and an ore deposit is not refined metal.
- Broad source labels remain candidates until exact species or an explicit game taxon is resolved. Scientific-name examples here are illustrative, not verified world-generation assignments.
- Related species, domesticated forms and selected varieties need explicit relationships; do not infer them from numeric sequence.

## Migration plan

1. Review candidates; split or merge ambiguous taxa with recorded provenance.
2. Create an allocation registry with entity type, new ID, tag, legacy ID and status. Allocate IDs from that registry, never from array position.
3. Create an explicit old-to-new mapping for every referenced definition, including external imports; retain retired IDs.
4. Update definitions and references together. Validate uniqueness, resolution and prerequisite cycles.
5. Version the affected schemas and document compatibility. Only introduce save migrations when real saved games exist.

Until this migration is complete, existing IDs such as `species_cultivation`, `plant_dwarf_birch` and `tropical_forest` remain authoritative. Do not mix illustrative new IDs into active catalogs. Not every record needs this prefix system: schema versions, language codes, event type enums, review issue keys and elevation numbers are not entity definitions.

## Resource allocations now present

New resource definitions already use RES IDs. `data/resources/resources.catalog.guide.json` records the 104 initial allocations. This does not migrate the legacy species or technology IDs and does not reserve the illustrative IDs in the table above. Preserve allocated IDs; do not rerun allocation from array positions.
