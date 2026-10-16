# Preliminary schemas

These JSON Schema Draft 2020-12 files describe initial envelopes, not complete domain schemas. No schema validator dependency is required or installed by this repository.

| Schema | Target | Scope |
| --- | --- | --- |
| `identifier.schema.json` | Future migrated definitions only | ID prefix/number and English tag shape; existing catalogs still use legacy IDs. |
| `world.guide.schema.json` | `data/world/world.catalog.guide.json` | Required envelope and collections. |
| `plant.guide.schema.json` | `data/plants/plants.catalog.guide.json` | Required envelope and collections. |
| `animal.guide.schema.json` | `data/animals/animals.catalog.guide.json` | Required envelope and collections. |
| `mineral.guide.schema.json` | `data/minerals/minerals.catalog.guide.json` | Required envelope and collections. |

`python tools/validate_repository.py` performs custom consistency checks: JSON parsing, unique catalog IDs, world references, summary counts, language maps, technology ordering/import declarations/cycles and relative Markdown links. It does **not** execute JSON Schema validation, validate every field, verify scientific taxonomy, resolve external technology definitions or prove simulation correctness.

Full agriculture and save-state schemas, ID allocation registry, external catalog resolution and schema-validator integration remain future work. The pre-existing agriculture documentation correctly states that a full agriculture JSON Schema is not implemented.

## Español

Los esquemas son contratos estructurales iniciales, no esquemas completos del dominio. El esquema de identificadores describe el formato futuro; no debe aplicarse todavía a los IDs actuales.

El verificador propio comprueba formato JSON, unicidad, referencias del mundo, conteos, traducciones, orden/importaciones/ciclos tecnológicos y enlaces Markdown. No ejecuta validación JSON Schema, no comprueba todos los campos ni valida taxonomía, tecnologías externas o balance. Los esquemas completos de agricultura y partidas y la integración con un validador formal quedan pendientes.
