# Evolve — Design and Simulation Reference

[Roadmap and pending work — read when resuming](../../ROADMAP.md)

[Plants and animals: gameplay categories](biology.md)

[Resource catalog and relationships](resources.md)

[Complete diagrams for every catalog](catalog-diagrams.md)

[Simple visual reference](visual-reference.md)

Complete nested JSON structures, types and examples: [JSON reference](json-structures.md).

Last documented update: 2026-10-17 (America/Guatemala).

This folder is the shared project reference for design, implementation and review. These Markdown documents are written for people and development tools alike; there is no separate agent-specific instruction file.

## 1. Start here

| File | Purpose |
| --- | --- |
| [agriculture.technologies.json](../../data/technologies/agriculture.technologies.json) | Machine-readable agriculture definitions. |
| [agriculture.technologies.md](../en/agriculture.technologies.md) | English technical reference. |
| [agriculture.technologies.es.md](../es/agriculture.technologies.md) | Spanish technical reference. |

The current agriculture configuration contains 23 peer technology definitions in a flat list. Its schema version is `2.0.0`; its content version is `0.3.0`. These numbers describe that configuration, not the release version of Evolve or the version of the wider design notebook.

## 2. Confirmed architectural direction

Build a headless, turn-based simulation first. Validate game behavior before investing in graphics or UI. The simulation will be developed independently from the future presentation layer. A graphics engine and implementation language have not yet been selected.

There are two categories of data:

- `GameDefinitions`: read-only configuration describing technologies, resources, species, conditions, costs and possible effects.
- `GameState`: mutable per-game data describing turns, civilizations, discoveries, inventory and research progress.

`SimulationEngine` is the code that interprets definitions and updates state. It is not a third JSON data category.

Separate JSON files may organize each category. The number of files is independent of the architectural distinction.

## 3. Technical conventions

- Technical identifiers, field names, enum values, events and code are in English.
- Player-visible `name` and `description` are language maps with `en` and `es`.
- IDs are stable; translated text is never an identity or dependency.
- Documentation is maintained in English and Spanish.
- Current fallback policy: requested language, then `defaultLanguage`, then owner ID.
- No graphics or layout coordinates belong in technology progression state.

## 4. Research and species

A research instance is identified by `(civilizationId, technologyId, speciesId)`.

- Civilization-scoped technologies use `speciesId: null`.
- Species-scoped technologies maintain independent progress for each species.
- Wheat and maize can share a cultivation definition while retaining different discoveries, requirements and progress.
- Research cost is expressed in points; estimated turns depend on the current research output.
- `order` orders presentation. Explicit prerequisites determine actual dependencies and permit parallel development.

Knowing a technique, possessing materials and operating an installation are separate conditions. Losing seed inventory does not erase cultivation knowledge. Learning pottery does not create pots. Learning domestication management does not instantly domesticate a species.

## 5. What exists today

- Agriculture configuration and its documented runtime contract.
- Bilingual names and descriptions.
- Declared external technology and catalog references.
- Internal checks for JSON validity, IDs and prerequisite cycles.
- Reference documentation, examples and known integration limitations.

## 6. What remains provisional or unimplemented

- Costs, eureka thresholds and numerical balance.
- Formal JSON Schema.
- Approved runtime catalogs: species, resource balance/storage, items, recipes and sites; design guides do not complete their runtime behavior.
- External technology definitions and full cross-branch validation.
- Simulation code, save/load and migrations.
- Soil, reproduction, domestication and production calculations.
- The exact phase order within a turn.
- Graphics engine, implementation language and UI.

The configuration defines a proposed executable contract; it is not proof that an evaluator or simulation already exists.

## 7. Open decisions before implementation

1. Normalize distinct and grouped eureka counters into explicit structured modes.
2. Define the initial `GameState` schema, version compatibility and save migration policy.
3. Specify ownership, access and local resource/equipment contexts.
4. Define turn phases and when newly completed technologies affect production.
5. Implement and validate each condition, event and effect handler.
6. Resolve wild ancestors, crop identities and propagation methods in the species catalog.

The detailed agriculture references explain these limitations. Do not infer missing behavior from a display label.

## 8. Documentation and change management

For each change, record its purpose, affected definitions, compatibility impact and validation. Keep English and Spanish documentation aligned.

Distinguish confirmed decisions, prototype configuration and unresolved design questions. Preserve existing stable IDs. A field-type change requires consumer updates even when a version number appears minor.

The EvolveDoc Git repository is now the primary reference. Drive files are previous snapshots and are not automatically synchronized. Use commits for changes and preserve stable IDs. See [identifier conventions](identifiers.md) and [repository structure](repository.md).

## 9. Suggested next milestone

Validate a small headless scenario with two civilizations and wheat/maize knowledge:

1. Load definitions and resolve dependencies.
2. Initialize independent civilization and species state.
3. Process research output and one eureka.
4. Check local conditions before using a capability.
5. Save and reload without duplicating rewards or changing definitions.

This is a proposed implementation checkpoint, not a completed feature.


## 10. Flat definitions and world catalog guide

Agriculture schema `2.0.0` removes technology node containers. Explicit prerequisite graphs remain authoritative; display order is not a sequential research gate. Stable technology IDs are retained.

`world.catalog.guide.json` is a structured conversion of the supplied world-generation document. It retains every listed regional flora, fauna and mining occurrence. It is a design guide, not a fully resolved species catalog. Unresolved taxonomy, ranges and balance use `null`, never invented values. It must not be loaded as playable world-generation data before review. The original source document is unchanged.

### World catalog files

- [world.catalog.guide.json](../../data/world/world.catalog.guide.json)
- [world.catalog.guide.en.md](../en/world.catalog.guide.md)
- [world.catalog.guide.es.md](../es/world.catalog.guide.md)


## Repository examples

[Simulation examples](../../simulation/README.md) demonstrate independent research by species using the real agriculture definition. They are educational fixtures, not a complete engine. The world guide is split into linked catalogs as described in [repository structure](repository.md).

Entity guides use general categories such as foxes and oaks, retaining useful gameplay distinctions. Scientific taxonomy is optional. See [entities](biology.md).
