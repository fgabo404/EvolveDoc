# Evolve — Design Documentation

Documentation and data contracts for a historical civilization simulation. This repository is the primary project reference; previous Drive copies are snapshots.

**[English documentation](lang/en/README.md) · [Documentación en español](lang/es/README.md)**

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
| Visual reference | [Diagrams](lang/en/visual-reference.md) | [Diagramas](lang/es/visual-reference.md) |
| Architecture and repository layout | [Structure](lang/en/repository.md) | [Estructura](lang/es/repository.md) |
| Stable ID and tag conventions | [Identifiers](lang/en/identifiers.md) | [Identificadores](lang/es/identifiers.md) |
| Complete JSON field references | [All JSON structures](lang/en/json-structures.md) | [Todas las estructuras JSON](lang/es/json-structures.md) |
| Agriculture contract | [Agriculture](lang/en/agriculture.technologies.md) | [Agricultura](lang/es/agriculture.technologies.md) |
| World and species guide | [World guide](lang/en/world.catalog.guide.md) | [Guía del mundo](lang/es/world.catalog.guide.md) |
| Simulation examples | [Examples](lang/en/simulation.md) | [Ejemplos](lang/es/simulation.md) |

## Current content

- 23 flat agriculture technologies; their existing IDs and gameplay configuration are preserved.
- 7 biomes, 27 regional variants and 485 source occurrences.
- 129 plant candidates, 134 animal candidates, 57 geological candidates and 21 agricultural crop candidates.
- Nomenclature contract: three-letter English prefix plus six digits, with a separate English `snake_case` tag. Migration of existing IDs is pending.
- A runnable research example, structural validation and bilingual documentation.

Candidates are not scientifically finalized species. Unknown values remain `null`, and guide catalogs are disabled for runtime generation. Evolution, domestication, yields, mineral processing and world-generation formulas still require design. No full engine or graphics is included.

## Run the checks and example

Requires Python 3.10 or later, with no third-party packages.

```sh
python tools/generate_json_reference.py --check
python tools/validate_repository.py
python simulation/examples/research_progress.py
python simulation/examples/research_progress.py --output /tmp/evolve-research-state.json
```

Definitions are read-only configuration. Generated state belongs to the individual game and is not committed. See [schema scope](schemas/README.md) for what validation does and does not guarantee.
