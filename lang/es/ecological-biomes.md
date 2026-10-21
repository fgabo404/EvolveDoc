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
5. **Pantano arbolado** — `forest_swamp` (tipo visual de bosque anegado; referencia: bosques pantanosos de los Everglades, Florida).

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

## Jerarquía aprobada: Tundra

**Categoría principal:** `tundra` — **Tundra**, sin subdivisiones aprobadas por ahora. Las variantes ártica, euroasiática y subantártica anteriores se conservan solo como antecedentes del catálogo heredado. Tundra describe vegetación y condiciones ecológicas; no se confunde con el hielo permanente de los polos.

## Nuevos biomas polares aprobados

1. **Ártico** — `arctic` (ID conceptual; región del extremo norte del mundo de juego).
2. **Antártico** — `antarctic` (ID conceptual; región del extremo sur del mundo de juego).

Se incluyen como categorías **jugables/geográficas polares** para estructurar el mapa. El hielo, la tundra, los mares polares y las superficies rocosas siguen siendo atributos/ecosistemas que pueden coexistir; no suponer que todo el Ártico es hielo terrestre ni que el Antártico carece de mar. Definir posteriormente sus condiciones de terreno y clima.

### Topología del mapa aprobada

Como en el mapa mundial de Civilization VI, el mundo de G-Evolve tendrá **continuidad este-oeste**: al salir por el borde derecho se vuelve por el izquierdo, y viceversa (envoltura cilíndrica horizontal). **Norte y sur no se conectan entre sí**: son los extremos polares del mapa, reservados respectivamente para las regiones Ártica y Antártica. Esta decisión define topología, no distancias, anchuras o extensión garantizada de hielo. La cuadrícula hexagonal visible y el relieve progresivo se mantienen.

No modificar por ahora los JSON heredados ni sus especies, flora o recursos: la migración se realizará tras cerrar todo el modelo de biomas.

## Sabana y praderas (`savanna`)

1. **Sabana húmeda** — `savanna_humid_savanna`
2. **Sabana seca** — `savanna_dry_savanna`
3. **Pradera templada** — `savanna_temperate_grassland`
4. **Estepa semiárida** — `savanna_steppe`

## Jerarquía aprobada: Llanuras

**Categoría principal:** `plains` — **Llanuras** (categoría de diseño jugable; geomorfológicamente una llanura es relieve, no un bioma estrictamente ecológico).

1. **Sabana** — `plains_savanna`
2. **Pradera** — `plains_grassland`
3. **Estepa** — `plains_steppe`
4. **Humedal abierto** — `plains_wetland` (referencia visual: pastizales, lagunas y planicies inundables del Pantanal)

**Decisión aprobada:** Para la clasificación visual de G-Evolve, el **pantano arbolado** aparece en Bosque y el **humedal abierto** en Llanuras. Ecológicamente ambos pueden ser humedales: esta división prioriza la fisonomía y jugabilidad, no implica que todos los Everglades sean bosques pantanosos ni que todo el Pantanal sea pastizal abierto. Los humedales pueden aparecer fuera de las llanuras; sus condiciones hídricas se modelarán de forma independiente. IDs conceptuales, sin migración de JSON ni especies por ahora.

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

## Jerarquía aprobada: Marino

**Categoría principal:** `marine` — **Marino**.

1. **Arrecife** — `marine_reef`: formaciones de arrecife, incluyendo arrecifes coralinos; referencia visual de aguas claras y estructuras sumergidas. No todos los arrecifes son tropicales.
2. **Estuario o litoral** — `marine_estuary_littoral`: ambientes costeros de transición, desembocaduras y litoral. **Estuario y litoral no son sinónimos ecológicos**; se agrupan provisionalmente como un único tipo visual del juego, conservando la distinción para el modelado posterior.
3. **Manglar** — `marine_mangrove`: bosque costero de mangles en ambientes intermareales tropicales y subtropicales; transición entre tierra y mar.
4. **Océano abierto (alta mar)** — `marine_open_ocean`: aguas alejadas de la costa, de amplio alcance oceánico. Temperatura, profundidad y corrientes se tratarán como propiedades independientes.

**Alcance de primera versión:** conservar **Estuario o litoral** como un único tipo visual/jugable. Para la simulación inicial se representará mediante condiciones geográficas relativamente estáticas. La dinámica temporal del litoral (cambios de costa, erosión, sedimentación, mareas u otros procesos que se acuerden) se **aplaza para una versión posterior del juego**. Un estuario tampoco es físicamente inmutable; la distinción «fijo frente a dinámico» es una simplificación de alcance del desarrollo, no una afirmación científica. No crear por ahora mecánicas dinámicas ni separar ambos tipos.

**Decisión aprobada:** son cuatro tipos jugables de paisaje/ecosistema marino; la batimetría, salinidad, temperatura, oleaje, sustrato y régimen hídrico se simularán por separado. No se modifican todavía los catálogos JSON ni se migran especies, recursos o IDs históricos.

### Tipos anteriores de Marino (históricos; no vigentes)

1. **Costa tropical somera** — `marine_tropical_shallow_coast`
2. **Mar costero templado** — `marine_temperate_coastal_sea`
3. **Mar polar o subpolar** — `marine_polar_sea`
4. **Humedal costero (manglar o marisma)** — `marine_coastal_wetland`

## Jerarquía aprobada: Montaña

**Categoría de relieve/jugabilidad:** `mountain` — **Montaña**.

1. **Alpino** — `mountain_alpine`: paisajes de alta montaña, con accesibilidad dependiente de pendiente, superficie y condiciones locales; no presupone ausencia de tundra, bosques u otros ecosistemas.
2. **Cumbres** — `mountain_summit`: **infranqueables para tránsito terrestre ordinario** y sin asentamientos convencionales. Representan las formaciones culminantes que funcionan como barreras geográficas.

**Aclaración de diseño — jerarquía de alturas:** **todos los biomas poseen elevación numérica propia y pueden ocupar diferentes pisos altitudinales**; sin embargo, la categoría **Montaña** se reserva para representar los **rangos más altos del relieve mundial**. No se debe etiquetar automáticamente como Montaña cualquier hexágono elevado que tenga bosque, tundra o taiga. Esos ecosistemas pueden extenderse hacia zonas altas según el clima y la geografía, mientras que la categoría Montaña identifica los pisos superiores: **Alpino** y, en el extremo máximo, **Cumbres infranqueables**. Los rangos numéricos específicos y sus límites contextuales siguen pendientes; no existe una altura fija aprobada para cada categoría.

**Decisión aprobada:** el mundo tiene elevación numérica progresiva, no solo dos alturas físicas ni cuatro niveles fijos. La montaña es una **forma de relieve** y la cobertura ecológica se determina por clima, humedad, latitud, temperatura y características locales. Una ladera montañosa puede contener bosque boreal (taiga), tundra u otra cobertura coherente: **altura elevada no implica automáticamente bioma alpino**. La tundra no está obligatoriamente a gran altura: también existe en bajas altitudes de regiones polares. La taiga puede encontrarse tanto en tierras bajas frías como en laderas de montaña. Los umbrales altitudinales deben ser contextuales, no números globales invariables.

**Compatibilidad:** IDs conceptuales, sin cambiar `alpine` ni los JSON históricos hasta la migración integral acordada. La clasificación previa subalpino/pradera alpina/tundra alpina/piso nival queda como antecedente, no como jerarquía vigente.


## Compatibilidad y decisiones pendientes

- Este documento propone **27 subtipos**. No son una taxonomía científica formal exhaustiva ni una lista definitiva.
- **No se cambiaron** las 27 variantes regionales antiguas ni las 485 apariciones del catálogo de origen; requieren migración revisada con alias, sin mapeo automático continente → ecosistema.
- La taiga podría convertirse en bioma principal independiente; por ahora se conserva bajo bosque templado para respetar los siete grupos actuales.
- Manglares y marismas son transiciones costeras; su pertenencia definitiva al bioma marino debe revisarse.
- El desierto arenoso/rocoso expresa sustrato, mientras que hiperárido expresa aridez; podrían convertirse en modificadores combinables, evitando subtipos superpuestos.
- La tundra alpina se mantiene en alta montaña para evitar duplicarla con tundra de latitudes frías.
- Primer boceto a trabajar: **selva tropical lluviosa de tierras bajas**, con referencia amazónica solo como ejemplo geográfico, no como categoría universal.

## Regla aprobada de elevación y rangos habituales (20 de octubre de 2026)

- **Nivel 0**: referencia del nivel del mar; la transitabilidad depende de la superficie (agua o tierra).
- **Niveles 1–100**: escala de elevación del terreno terrestre **potencialmente transitable**; las pendientes, agua y obstáculos pueden imponer restricciones adicionales.
- **Niveles superiores a 100**: **Cumbres**, infranqueables para movimiento terrestre ordinario y sin asentamientos convencionales. **100 no es la altura máxima del mundo**.
- Cada bioma tendrá un **intervalo habitual de aparición** dentro de la escala de terreno correspondiente; son rangos preferentes para generación, **no fronteras ecológicas absolutas**. Condiciones de clima, latitud, humedad y suelo pueden permitir apariciones fuera del rango habitual cuando sea coherente.
- La correspondencia numérica de nivel a metros reales **queda por definir**: quedan descartados como reglas los intentos anteriores de igualar 100 al Everest o fijar sin aprobación 100 = 5,000 m.
- Las profundidades marinas se modelarán aparte del rango terrestre sin asignar niveles negativos automáticamente.
- Esta regla sustituye las propuestas anteriores de cumbres en 65–100 u 80–100.


## Rangos habituales de elevación — propuesta aprobada para simulación

**Regla aprobada:** los rangos de la tabla son **habituales o preferentes**, nunca límites rígidos de aparición. El generador podrá ubicar un bioma fuera de su intervalo cuando latitud, temperatura, humedad, suelo, régimen hídrico y geografía lo justifiquen. Los números son parámetros de diseño para los 100 niveles terrestres, **no conversiones científicas exactas en metros**. La escala en metros por nivel sigue pendiente.

| Categoría | Tipo | Nivel habitual | Referencia representativa |
|---|---|---:|---|
| Marino | Océano abierto (superficie) | 0 | Océano Pacífico |
| Marino | Arrecife (superficie) | 0–1 | Gran Barrera de Coral |
| Marino | Estuario / litoral | 0–3 | Bahía de Chesapeake |
| Marino | Manglar | 0–3 | Sundarbans |
| Bosque | Tropical (selva) | 2–25 | Amazonía |
| Bosque | Subtropical | 5–35 | Bosques subtropicales de China |
| Bosque | Templado | 5–35 | Europa central |
| Bosque | Boreal (taiga) | 5–30 | Siberia y Canadá |
| Bosque | Pantano arbolado | 0–8 | Everglades (sectores arbolados) |
| Llanuras | Sabana | 5–25 | Serengeti |
| Llanuras | Pradera | 5–30 | Grandes Praderas norteamericanas |
| Llanuras | Estepa | 10–40 | Mongolia |
| Llanuras | Humedal abierto | 0–12 | Pantanal (sectores abiertos) |
| Desierto | Arenoso | 5–25 | Dunas del Sahara |
| Desierto | Rocoso | 10–40 | Monument Valley, Merrick Butte |
| Desierto | Salar | 55–75 | Salar de Uyuni |
| Tundra | Tundra | 0–20 | Alaska ártica |
| Polar | Ártico (territorio) | 0–20 | Regiones terrestres árticas |
| Polar | Antártico (territorio) | 40–70 | Meseta interior antártica |
| Montaña | Alpino | 60–100 | Alpes y cordilleras elevadas |
| Montaña | Cumbres | 101+ | Cumbres infranqueables |

**Alcance e interpretación:** 0 es la referencia del nivel del mar; 1–100 corresponde a elevación terrestre potencialmente transitable (sujeta a pendientes y otros obstáculos); más de 100 corresponde a cumbres infranqueables. El agua marina se representa a nivel superficial 0 y sus profundidades se modelarán aparte. Ártico y Antártico son categorías geográficas determinadas por latitud, no por elevación; sus rangos describen únicamente ejemplos de terreno. Cumbres no tienen máximo superior definido.

**Excepciones coherentes:** bosques de montaña como los de Banff pueden alcanzar alturas mayores que el rango típico de taiga; praderas alpinas, tundras de altura y salares bajos también pueden generarse cuando las condiciones lo sustenten. No imponer exclusividad de altitud ni asignación automática basada solo en altura.

**Datos:** estos rangos aprobados pertenecen a la documentación conceptual del modelo. No editar todavía los JSON heredados de biomas, flora, fauna, minerales o recursos hasta cerrar la migración integral.

