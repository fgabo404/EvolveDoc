# G-Evolve — Modelo de clasificación de biomas (v0.2.1)

**Versionado del modelo:** `0.2.0` introduce el modelo jerárquico `Bioma → tipo → subtipo ecológico`; `0.2.1` incorpora los tres tipos aprobados de Desierto sin alterar esa estructura. No incrementar la versión del modelo por cada commit documental; usar revisiones de documentación e historial Git para cambios editoriales. Los catálogos JSON heredados conservan sus versiones independientes y todavía requieren migración.

**Estado:** jerarquía de bosques aprobada para diseño; subtipos ecológicos previos pendientes de revisión y balance.  
**Fuente estructurada:** [ecological-subtypes.proposal.json](../../data/world/ecological-subtypes.proposal.json).

No clasificar subtipos por continente. Separar **bioma**, **tipo de ecosistema**, **ecorregión de referencia** y **región biogeográfica**. Esta última condiciona las especies nativas, sin modificar el tipo de ecosistema. La elevación progresiva, temperatura, humedad, agua y suelo intervienen en la generación, sin umbrales numéricos aprobados.

## Jerarquía aprobada: Bosque

**Categoría principal:** `forest` — **Bosque**.

1. **Tropical (selva)** — `tropical_forest` (ID histórico conservado).
2. **Subtropical** — `subtropical_forest` (ID conceptual nuevo; pendiente de asignación definitiva en catálogo operativo).
3. **Templado** — `temperate_forest` (ID histórico conservado).
4. **Boreal (taiga)** — `boreal_forest` (ID conceptual nuevo; separado de bosque templado).

**Decisión del 20 de octubre de 2026:** la jerarquía es `Bosque → tipo climático → subtipo de ecosistema`. La procedencia continental no define tipos forestales. Los detalles enumerados a continuación son propuestas anteriores y deben migrarse/revisarse, en particular la taiga, que ahora pertenece a Boreal y no a Templado.

**Compatibilidad:** no renombrar ni borrar IDs de los datos de mundo, variantes regionales, especies o apariciones hasta contar con un plan de alias/migración y validación. El JSON de subtipos ecológicos v0.1 queda como referencia histórica, no como jerarquía vigente aprobada.

## Propuestas de subtipos heredados (pendientes de revisión)

### Bosque tropical (`tropical_forest`)

1. **Selva tropical lluviosa de tierras bajas** — `tropical_forest_lowland_rainforest`
2. **Bosque tropical estacional o seco** — `tropical_forest_seasonal_dry_forest`
3. **Bosque tropical montano o nuboso** — `tropical_forest_montane_cloud_forest`
4. **Bosque tropical inundable** — `tropical_forest_flooded_tropical_forest`

### Bosque templado (`temperate_forest`)

1. **Bosque templado caducifolio** — `temperate_forest_temperate_deciduous`
2. **Bosque templado mixto** — `temperate_forest_temperate_mixed`
3. **Bosque templado siempreverde** — `temperate_forest_temperate_evergreen`
4. **Bosque boreal de coníferas (taiga)** — `temperate_forest_boreal_coniferous`

## Tundra (`tundra`)

1. **Tundra arbustiva ártica** — `tundra_arctic_shrub_tundra`
2. **Tundra de musgos y líquenes** — `tundra_arctic_moss_lichen`
3. **Tundra subantártica** — `tundra_subantarctic_tundra`

## Sabana y praderas (`savanna`)

1. **Sabana húmeda** — `savanna_humid_savanna`
2. **Sabana seca** — `savanna_dry_savanna`
3. **Pradera templada** — `savanna_temperate_grassland`
4. **Estepa semiárida** — `savanna_steppe`

## Jerarquía aprobada: Desierto

**Categoría principal:** `desert` — **Desierto**.

1. **Arenoso (dunas)** — `desert_sandy`: dunas, campos de arena, ondulaciones y valles secos.
2. **Rocoso (cañones y mesetas)** — `desert_rocky`: roca expuesta, cañones, mesas, buttes y escarpes erosionados. **Merrick Butte** es referencia morfológica y visual, no requisito regional.
3. **Salar** — `desert_salt_flat`: planicies salinas, costras de sal, depresiones y lagunas salobres ocasionales.

**Decisión aprobada:** estos tres son tipos de **paisaje/superficie para el diseño del mundo**, no clases climáticas científicas excluyentes. La aridez, temperatura, origen geográfico y elevación se modelarán por atributos separados. Los IDs nuevos son conceptuales; no se cambian los IDs ni las relaciones del JSON heredado hasta planificar una migración segura.

**Sustituye** para diseño la antigua propuesta de desiertos cálidos arenosos, rocosos, fríos e hiperáridos. Las antiguas entradas quedan como antecedentes, no como tres tipos vigentes.

## Subtipos anteriores de desierto (históricos; no vigentes)

1. **Desierto cálido arenoso** — `desert_hot_sandy_desert`
2. **Desierto rocoso** — `desert_rocky_desert`
3. **Desierto frío** — `desert_cold_desert`
4. **Desierto hiperárido** — `desert_hyperarid_desert`

## Marino (`marine`)

1. **Costa tropical somera** — `marine_tropical_shallow_coast`
2. **Mar costero templado** — `marine_temperate_coastal_sea`
3. **Mar polar o subpolar** — `marine_polar_sea`
4. **Humedal costero (manglar o marisma)** — `marine_coastal_wetland`

## Alta montaña y pisos alpinos (`alpine`)

1. **Piso subalpino** — `alpine_subalpine`
2. **Pradera alpina** — `alpine_alpine_meadow`
3. **Tundra alpina** — `alpine_alpine_tundra`
4. **Piso nival y cumbres** — `alpine_nival_summit`

## Compatibilidad y decisiones pendientes

- Este documento propone **27 subtipos**. No son una taxonomía científica formal exhaustiva ni una lista definitiva.
- **No se cambiaron** las 27 variantes regionales antiguas ni las 485 apariciones del catálogo de origen; requieren migración revisada con alias, sin mapeo automático continente → ecosistema.
- La taiga podría convertirse en bioma principal independiente; por ahora se conserva bajo bosque templado para respetar los siete grupos actuales.
- Manglares y marismas son transiciones costeras; su pertenencia definitiva al bioma marino debe revisarse.
- El desierto arenoso/rocoso expresa sustrato, mientras que hiperárido expresa aridez; podrían convertirse en modificadores combinables, evitando subtipos superpuestos.
- La tundra alpina se mantiene en alta montaña para evitar duplicarla con tundra de latitudes frías.
- Primer boceto a trabajar: **selva tropical lluviosa de tierras bajas**, con referencia amazónica solo como ejemplo geográfico, no como categoría universal.
