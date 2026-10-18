# G-Evolve — Diseño visual del mundo (v0.1)

**Estado:** propuesta visual aprobada por el diseñador (17 de octubre de 2026).  
**Nombre del estilo:** Hand-Drawn Isometric Hex World — mundo continuo con cuadrícula hexagonal sutil.

## Concepto aprobado

El mapa se percibe como un paisaje continuo, orgánico y vivo. Los hexágonos estructuran la simulación, pero su cuadrícula es discreta y puede destacarse en las vistas tácticas. El terreno se dibuja con estética isométrica minimalista de líneas finas y colores suaves. Los bosques, cursos de agua, costas, montañas y caminos cruzan visualmente los límites de los hexágonos, sin parecer fichas sueltas.

## Elevación progresiva

La elevación **no** queda limitada a cuatro alturas físicas. Cada hexágono mantiene una elevación numérica de alta resolución; los rangos o pisos altitudinales se usan para clasificar y representar regiones. Por ejemplo, 0–10, 11–20, 21–40, 41–60, 61–80 y 81–100 son **rangos ilustrativos, no reglas ni umbrales aprobados**. El sistema debe poder ampliar la resolución y el máximo. La altura absoluta y la pendiente entre hexágonos son propiedades diferentes: una meseta alta puede ser llana y un desnivel local puede ser un acantilado.

El catálogo existente `data/world/world.catalog.guide.json` conserva sus cuatro `elevationLevels` como clasificación preliminar; esta propuesta de elevación detallada requiere su posterior revisión, sin sobrescribir todavía las definiciones actuales.

## Generación del mundo y biomas

1. Generar masas continentales, océanos y posición geográfica.
2. Generar elevación detallada y formas de relieve conectadas.
3. Derivar condiciones ambientales, incluyendo temperatura, humedad, agua y suelo.
4. Asignar biomas y tipos ecológicos en función del conjunto de condiciones, **no solo de la altitud**. La región biogeográfica filtra después las especies potenciales.
5. Distribuir flora, fauna y recursos de acuerdo con los catálogos y las restricciones geográficas.

**Biomas del catálogo actual (7):** bosque tropical, bosque templado, tundra, sabana, desierto, marino y alta montaña/alpino. El catálogo conserva **27 variantes regionales históricas** como datos y referencias, pero ya no se consideran la taxonomía objetivo del diseño. Se propone reemplazar la subdivisión meramente continental por **tipos de ecosistema definidos ecológicamente**, con ecorregiones de referencia y regiones biogeográficas como dimensiones separadas. Los umbrales climáticos, la abundancia y la distribución concreta siguen pendientes de diseño y balance.

## Clasificación ecológica de biomas — decisión de diseño (v0.2)

**Decisión aprobada el 17 de octubre de 2026:** Las variantes de G-Evolve no deben clasificarse simplemente como «americano», «africano», «asiático» u «oceánico». Estas etiquetas indican procedencia geográfica, no un tipo de ecosistema. Los bocetos se desarrollarán **uno por tipo ecológico**, no uno por continente.

**Modelo propuesto:**

- **Bioma:** categoría amplia existente (por ejemplo `tropical_forest`).
- **Tipo de ecosistema / subtipo ecológico:** formación distinguida por lluvia, estacionalidad, vegetación, inundación, suelo y condiciones de altitud (por ejemplo selva tropical lluviosa de tierras bajas; bosque tropical estacional o seco; bosque tropical montano o nublado; bosque inundable). Son candidatos a validar, no una lista definitiva.
- **Ecorregión:** unidad territorial real que sirve de ejemplo y de referencia ecológica (por ejemplo bosques húmedos de la Amazonía). La Amazonía no es una clasificación universal ni todo su territorio forma un único ecosistema.
- **Región biogeográfica:** factor independiente que limita especies nativas; dos lugares con el mismo tipo de ecosistema pueden albergar flora y fauna diferentes.

**Primera ficha visual a desarrollar:** *Selva tropical húmeda de tierras bajas*, inspirada en ejemplos amazónicos, sin codificar «americana» como subtipo ecológico.

**Compatibilidad:** mantener los IDs y las 27 variantes regionales actuales en `data/world/world.catalog.guide.json` y sus referencias hasta diseñar una migración con alias y validación de las 485 apariciones. No alterar el JSON ejecutable/guía durante esta actualización documental. No asignar todavía umbrales cuantitativos ni reclasificar especies automáticamente.

**Fuentes de referencia de clasificación:** WWF / Olson et al. (2001), *Terrestrial Ecoregions of the World*; categorías de bosques tropicales y subtropicales húmedos, secos y de coníferas. Véase https://www.worldwildlife.org/biomes/ y https://ecoregion.net/ .

## Reglas visuales

- **Cuadrícula hexagonal siempre visible y reconocible** sobre tierra y agua, también en la vista normal. Líneas continuas, finas y con contraste suficiente para identificar cada hexágono; pueden intensificarse en acciones tácticas, pero no desaparecer. Evitar que vegetación, texturas o efectos oculten sistemáticamente la malla.
- **Relieve progresivo claramente marcado** con diferencias de alturas legibles, perfiles, paredes y pendientes isométricas. Numerosas cotas crean laderas, mesetas, barrancos, valles y cordilleras; no limitar el mundo a cuatro alturas ni convertir todos los desniveles en plataformas artificiales.
- **Mapa despejado y no saturado:** vegetación, rocas, fauna y otros elementos dibujados en grupos representativos con espacios libres, sin tapar la cuadrícula ni impedir identificar relieve y tipo de terreno.
- Biomas diferenciados por vegetación, densidad, color y textura, con transiciones naturales.
- Ríos y caminos continuos; costas irregulares; geografía conectada.
- Recursos visibles como indicios representativos, con detalle consultable mediante selección y capas temáticas.
- Asentamientos y actividades humanas modifican progresivamente el paisaje.
- No confundir la representación visual con las cantidades lógicas de árboles, depósitos o animales.

## Revisión visual aprobada — grid y relieve (v0.3, 18 de octubre de 2026)

La última revisión visual aprobada de la referencia enfatiza **hexágonos delineados claramente en toda la superficie** (incluyendo el océano), con relieve de alturas múltiples bien visible y un paisaje sin sobrecarga de detalles. La prioridad visual es: **lectura de cada hexágono → lectura de alturas → lectura del bioma y sus elementos**. Se mantiene el estilo *Hand-Drawn Isometric Hex World with Progressive Elevation*.

Esta regla **sustituye** la sugerencia anterior de hacer casi invisible la grilla en la vista normal. El primer subtipo ecológico usado para calibrar el estilo es *Selva tropical lluviosa de tierras bajas*; los ejemplos que mezclan otros biomas son pruebas de estilo generales, no representaciones definitivas de un solo subtipo.

**Referencia PNG generada en la conversación:** `g_evolve_hexagonal_tropical_world_map.png` (pendiente de incorporación binaria al repositorio). La aprobación del estilo y su registro textual no equivalen a subir la imagen.

## Referencia artística aprobada

**Boceto:** «G-Evolve — Concepto de Mundo: terreno, biomas y generación procedural de un mundo continuo», aprobado en conversación. Incluye un paisaje isométrico con los siete biomas, una sección ilustrativa de relieve progresivo y ejemplo de cuadrícula sutil.

**Archivo de imagen original generado:** `g_evolve_procedural_biome_world_map.png` (pendiente de incorporar como archivo binario al repositorio). Este documento preserva las decisiones aprobadas, pero **no declara la imagen cargada en GitHub** hasta que se confirme su subida.

## Estado de implementación

Esta especificación es documentación conceptual; no activa definiciones ejecutables. El catálogo existente continúa siendo la fuente de IDs y relaciones. La elevación numérica, las pendientes, los algoritmos de transición y los límites geográficos serán objeto de validación y simulación antes de programar.
