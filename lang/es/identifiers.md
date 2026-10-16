# Identificadores y tags

Estado: nomenclatura acordada; los catálogos existentes TODAVÍA NO están migrados. Los números de ejemplo no reservan IDs.

Una definición final tendrá `id: "PLT#000001"` y `tag: "triticum_aestivum"`. El prefijo contiene exactamente tres letras mayúsculas en inglés. El sufijo tiene seis dígitos desde 000001, con correlativo independiente por prefijo. `#` forma parte del ID; no es un ancla de URL.

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

## Reglas

- Los IDs son únicos entre definiciones, permanentes y nunca se reutilizan. Al eliminar una entrada, su ID queda retirado.
- Los tags están en inglés, usan `snake_case` y son únicos dentro de cada tipo. Las traducciones nunca identifican entidades.
- Las referencias usan IDs. El número no representa orden, nivel, geografía ni parentesco evolutivo.
- Una población generada tiene un `instanceId` propio y un `definitionId` que apunta a su especie. El formato de las instancias queda pendiente del diseño de partidas.
- Especie, recurso cosechado, tipo de yacimiento y regla de aparición son entidades distintas. Grano no es planta; mineral extraído no es metal refinado.
- Los nombres generales siguen siendo candidatos hasta resolver la especie o aceptar explícitamente un grupo del juego. Los nombres científicos de la tabla son ilustrativos, no asignaciones verificadas del mundo.
- Especies relacionadas, formas domesticadas y variedades necesitan relaciones explícitas; no se deducen del correlativo.

## Plan de migración

1. Revisar candidatos y registrar divisiones o fusiones de grupos ambiguos, conservando procedencia.
2. Crear un registro de asignaciones con tipo, nuevo ID, tag, ID anterior y estado. Nunca asignar IDs según la posición del arreglo.
3. Completar equivalencias para todas las definiciones referenciadas, incluidas las externas; conservar los IDs retirados.
4. Cambiar definiciones y referencias juntas; verificar unicidad, referencias y ciclos tecnológicos.
5. Versionar los esquemas afectados y documentar compatibilidad. Las migraciones de partidas se introducirán cuando existan partidas reales.

Mientras tanto, los IDs actuales como `species_cultivation`, `plant_dwarf_birch` y `tropical_forest` siguen siendo válidos. No mezclar los IDs ilustrativos nuevos con los catálogos. Versiones, códigos de idioma, tipos de evento, claves de revisión y niveles numéricos de elevación no son definiciones de entidades y no requieren estos prefijos.
