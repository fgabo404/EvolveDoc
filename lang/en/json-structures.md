# Complete JSON structure reference

[Simple visual reference](visual-reference.md)

Every JSON source currently tracked under `data`, `simulation` and `schemas` has a reference below, with all nested fields, observed types, meaning and examples. This is generated from current files; `null` internals and empty-array element types remain explicitly unresolved.

- [`data/animals/animals.biological.catalog.json`](json/data--animals--animals.biological.catalog.md)
- [`data/animals/animals.catalog.guide.json`](json/data--animals--animals.catalog.guide.md)
- [`data/minerals/minerals.catalog.guide.json`](json/data--minerals--minerals.catalog.guide.md)
- [`data/plants/plants.biological.catalog.json`](json/data--plants--plants.biological.catalog.md)
- [`data/plants/plants.catalog.guide.json`](json/data--plants--plants.catalog.guide.md)
- [`data/resources/resources.catalog.guide.json`](json/data--resources--resources.catalog.guide.md)
- [`data/technologies/agriculture.technologies.json`](json/data--technologies--agriculture.technologies.md)
- [`data/world/world.catalog.guide.json`](json/data--world--world.catalog.guide.md)
- [`simulation/examples/research.initial-state.json`](json/simulation--examples--research.initial-state.md)
- [`schemas/animal.guide.schema.json`](json/schemas--animal.guide.schema.md)
- [`schemas/biological.catalog.schema.json`](json/schemas--biological.catalog.schema.md)
- [`schemas/identifier.schema.json`](json/schemas--identifier.schema.md)
- [`schemas/mineral.guide.schema.json`](json/schemas--mineral.guide.schema.md)
- [`schemas/plant.guide.schema.json`](json/schemas--plant.guide.schema.md)
- [`schemas/resource.guide.schema.json`](json/schemas--resource.guide.schema.md)
- [`schemas/world.guide.schema.json`](json/schemas--world.guide.schema.md)

## Maintenance

Run `python tools/generate_json_reference.py` after JSON structure changes; run with `--check` to detect outdated or missing references. Keep field explanations in both languages. The generator fails when it finds a new property without an explanation. This complements, rather than replaces, the conceptual agriculture/world documentation and schema validation.
