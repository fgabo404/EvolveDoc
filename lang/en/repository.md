# Repository structure and responsibilities

[Resource catalog and relationships](resources.md)

Complete nested JSON structures, types and examples: [JSON reference](json-structures.md).

This is a documentation repository with structured design catalogs and small educational simulations. Its root represents `evolve/`; no redundant nested `evolve` directory is needed.

| Directory | Responsibility |
| --- | --- |
| `lang/en`, `lang/es` | Human-readable design and technical documentation in both languages. These are not yet extracted UI translation catalogs. |
| `data/world` | Biomes, regional variants, elevation, geographic rules, source occurrences and catalog links. |
| `data/animals` | Animal gameplay categories, regional occurrences, useful domestication distinctions and outputs. |
| `data/plants` | Plant/crop gameplay categories; propagation, useful forms and outputs. |
| `data/minerals` | Geological candidates; future deposits, extraction, processing and requirements. |
| `data/resources` | 105 material definitions with source links and proposed transformation endpoints; quantities and recipes remain unresolved. |
| `data/technologies` | Flat technology definitions, requirements, research costs and eurekas. |
| `schemas` | Initial structural contracts and their explicit limits. |
| `simulation` | Fixtures and runnable demonstrations; not the production engine. |
| `tools` | Repository consistency checks. |

## Catalog composition

Load `data/world/world.catalog.guide.json` for world design. Resolve its `catalogFiles` relative to that file. Plant and animal files contain `speciesCandidates`; the plants file also contains `agriculturalCropCandidates`. The minerals file contains `geologicalResourceCandidates`. The world file retains all 485 `resourceOccurrences`; their `definitionId` references resolve across these catalogs.

World schema/content is 1.4.0/0.5.0; plant/animal guides are 1.3.0/0.4.0; minerals remain 1.1.0/0.2.0; resources are 1.0.0/0.3.0. Generalized entries retain retired-ID aliases and original occurrences. Agriculture remains 2.0.0/0.3.0 unchanged.

`null` means unresolved. An empty mapping is not worldwide distribution. All guide catalogs remain runtime-disabled. Candidate classification follows the source: for example, lichens remain under flora pending scientific review.

## Architecture

`GameDefinitions` describes possibilities and is read-only during a game. `GameState` stores mutable discoveries, inventory, populations and research progress. The future `SimulationEngine` interprets definitions. Multiple JSON files do not create extra architectural layers.

Keep biological lineage, selective breeding/domestication and technical improvements separate; none is implied by a higher level number. Mineral evolution means extraction and processing capabilities, not biological evolution. Product IDs and recipes must be explicitly defined before yields are enabled.

## Change policy

Git is the primary reference from this migration onward. Drive is not automatically synchronized. Update both documentation languages together. Commit configuration changes with purpose, validation and compatibility notes. Preserve unresolved questions rather than inventing taxonomy or balance. Do not commit real saved games, credentials or generated caches.

Current granularity uses [general gameplay categories](biology.md). Scientific taxonomy is optional; grouped IDs retain aliases and provenance.

Animal content: 0.5.0 after selecting detailed fox outputs; structure remains 1.3.0.
