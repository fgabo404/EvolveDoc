# Referencia completa de estructuras JSON

[Referencia gráfica sencilla](visual-reference.md)

Cada JSON actual de `data`, `simulation` y `schemas` tiene una referencia con todos los campos internos, tipos observados, significado y ejemplos. Se genera desde los archivos actuales; estructuras internas de `null` y tipos de arreglos vacíos siguen explícitamente pendientes.

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

## Mantenimiento

Ejecutar `python tools/generate_json_reference.py` después de cambiar estructuras JSON; usar `--check` para detectar referencias desactualizadas o faltantes. Mantener explicaciones de campos en ambos idiomas. El generador falla si encuentra una propiedad nueva sin explicación. Complementa la documentación conceptual de agricultura/mundo y la validación de esquemas.
