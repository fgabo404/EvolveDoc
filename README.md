# Evolve — Design Documentation

Documentation and data contracts for a historical civilization simulation. This repository is the primary project reference; previous Drive copies are snapshots.

**[English documentation](lang/en/README.md) · [Documentación en español](lang/es/README.md)**

**Current work and pending tasks: [Roadmap](ROADMAP.md) · [Pendientes y avances](ROADMAP.es.md)**

## Repository structure

```text
EvolveDoc/
├── README.md
├── lang/
│   ├── en/
│   └── es/
├── data/
│   ├── world/
│   ├── animals/
│   ├── plants/
│   ├── minerals/
│   ├── resources/
│   └── technologies/
├── schemas/
├── simulation/
│   └── examples/
└── tools/
```

`resources` is the English technical name for the requested resource directory. `lang` currently stores documentation; visible names remain inline `{ "en": "...", "es": "..." }` maps in JSON until localization is extracted.

## Start here

| Reference | English | Español |
| --- | --- | --- |
| Complete catalog diagrams | [All catalogs](lang/en/catalog-diagrams.md) | [Todos los catálogos](lang/es/catalog-diagrams.md) |
| Visual reference | [Diagrams](lang/en/visual-reference.md) | [Diagramas](lang/es/visual-reference.md) |
| Architecture and repository layout | [Structure](lang/en/repository.md) | [Estructura](lang/es/repository.md) |
| Stable ID and tag conventions | [Identifiers](lang/en/identifiers.md) | [Identificadores](lang/es/identifiers.md) |
| Complete JSON field references | [All JSON structures](lang/en/json-structures.md) | [Todas las estructuras JSON](lang/es/json-structures.md) |
| General plant and animal entities | [Categories](lang/en/biology.md) | [Categorías](lang/es/biology.md) |
| Animal materials and acquisition | [All animals](lang/en/animal-products.md) | [Todos los animales](lang/es/animal-products.md) |
| Resource catalog | [Resources](lang/en/resources.md) | [Recursos](lang/es/resources.md) |
| Agriculture contract | [Agriculture](lang/en/agriculture.technologies.md) | [Agricultura](lang/es/agriculture.technologies.md) |
| World and species guide | [World guide](lang/en/world.catalog.guide.md) | [Guía del mundo](lang/es/world.catalog.guide.md) |
| Simulation examples | [Examples](lang/en/simulation.md) | [Ejemplos](lang/es/simulation.md) |

## Current content

- General gameplay categories: 33 selected animal/plant groups replace regional/species variants, with 86 explicit retired-ID aliases. Scientific background is optional.
- Material/acquisition reference for all 101 current animals: 498 material links and 17 methods; quantities and operational rules remain deferred.
- 106 resources, 594 possible source links and 28 transformation endpoint guides; units, yields and recipes remain unresolved.
- 23 flat agriculture technologies; their existing IDs and gameplay configuration are preserved.
- 7 biomes, 27 regional variants and 485 source occurrences.
- 109 plant entity candidates, 101 animal entity candidates, 57 geological candidates and 21 agricultural crop candidates.
- Nomenclature contract: three-letter English prefix plus six digits, with a separate English `snake_case` tag. New resources, taxa and forms have allocated IDs; legacy candidate/technology IDs are retained.
- A runnable research example, structural validation and bilingual documentation.

Gameplay identities use general categories such as foxes, bears, oaks and pines when scientific subdivisions add no gameplay value. Crop identities and useful wild/domestic differences remain separate. All original source occurrences are preserved. Scientific catalogs remain optional background; they do not create mandatory entity subdivisions. Guide catalogs remain runtime-disabled while operational rules, yields and formulas are deferred. No full engine or graphics is included.

## Run the checks and example

Requires Python 3.10 or later, with no third-party packages.

```sh
python tools/generate_json_reference.py --check
python tools/generate_biology_reference.py --check
python tools/validate_repository.py
python simulation/examples/research_progress.py
python simulation/examples/research_progress.py --output /tmp/evolve-research-state.json
```

Definitions are read-only configuration. Generated state belongs to the individual game and is not committed. See [schema scope](schemas/README.md) for what validation does and does not guarantee.
