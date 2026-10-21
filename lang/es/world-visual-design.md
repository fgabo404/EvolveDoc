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


## Estándar oficial de bocetos conceptuales — Hex Grid First (20 de octubre de 2026)

**Estado: APROBADO. Aplicación predeterminada a todos los futuros bocetos de G-Evolve**, especialmente fichas de biomas, subtipos, relieve, terrenos, variaciones y láminas comparativas. Mantener la coherencia con el estilo global *Hand-Drawn Isometric Hex World with Progressive Elevation*, pero distinguir **boceto conceptual/editorial** de **mapa jugable continuo**.

### Referencia estética principal

**Lámina de referencia aprobada por el usuario:** «G-EVOLVE — BIOMAS DEL MUNDO», una *concept sheet* con varios dioramas hexagonales isométricos y rótulos editoriales de Bosque, Llanuras, Desierto, Marino, Tundra, Ártico, Antártico y Montaña. Fue generada en la conversación del 20 de octubre de 2026. **El PNG original no se ha incorporado aún al repositorio**: este archivo documenta el estilo de forma formal, sin atribuirle un archivo de imagen binario inexistente.

**Identidad:** concept sheet isométrico modular de biomas; ilustración digital dibujada a mano, limpia, elegante, natural, de detalle contenido. Vista 2.5D/isométrica superior con caras laterales visibles en las losetas, volúmenes suaves y contornos finos y definidos. Lámina editorial en blanco/crema con amplios espacios vacíos, titulares y etiquetas pequeñas, claras, alineadas, sin ornamentación excesiva. Colores suaves, ligeramente desaturados y diferenciados por ecosistema; sombras discretas. Apariencia de diorama ilustrado y atlas conceptual, no render fotorrealista, arte épico ni fotografía.

### REGLA ABSOLUTA: LA GRID ES PRIMERO Y NUNCA DESAPARECE

El rasgo **más importante y explícitamente solicitado** es que la **cuadrícula hexagonal esté MÁS VISIBLE, DELINEADA y REMARCADA que en la lámina original aprobada**. Mantener todo lo demás del estilo original.

**Orden obligatorio de construcción y lectura:**
1. **Trazar primero la grid hexagonal real:** hexágonos correctos, unidos, regulares y legibles; conforman la estructura base de cada bloque. Evitar pentágonos, polígonos irregulares, cuadrados o bordes incompatibles con una retícula hexagonal.
2. **Construir terreno y relieve encima de la grid**, conservando el perímetro superior de CADA celda y las separaciones entre celdas. Aplicar caras laterales para el espesor/elevación y diferencias de altura progresivas según el tema.
3. **Aplicar los colores, agua, texturas y biomas sin borrar la malla.** Las fronteras y contornos de hexágonos se deben leer también bajo agua, hielo, arena, pradera y bosque.
4. **Añadir muy pocos elementos característicos** —árboles, arbustos, hierba, rocas o detalles de agua— solamente para identificar el bioma, sin cubrir un porcentaje significativo del mosaico. Dejar superficies despejadas.
5. **Agregar las etiquetas editoriales al final**, sin sobreponer textos sobre las celdas; títulos de sección y nombres de subtipos con líneas-guía finas si ayudan.

**Contraste:** contorno fino-medio, limpio y distinguible del color del terreno; más oscuro/reforzado en los bordes entre hexágonos para una lectura inmediata, pero sin transformarlo en un tablero de líneas gruesas dominantes. La malla ha de permanecer legible a tamaño normal de visualización, sin necesidad de zoom. No sustituir la grid por una textura simulada o marcas hexagonales dibujadas al azar. La continuidad del agua, ríos y terrenos puede sugerirse con color y trazos fluidos, **sin hacer desaparecer los bordes de las celdas**.

### Composición obligatoria para bocetos

- Lámina *concept sheet* organizada en módulos independientes por bioma o tema; cada módulo presenta pequeños grupos de hexágonos isométricos conectados.
- Fondo claro blanco roto/crema, sin decoraciones ni fondos cargados.
- Jerarquía: título de la lámina → categoría → diorama hexagonal → etiquetas breves de subtipos o variantes.
- Densidad baja: **minimalismo gráfico, pocas piezas representativas**, bastante espacio negativo.
- No llenar cada casilla con objetos; la lectura prioritaria es **(1) hexágonos, (2) relieve/suelo y agua, (3) tipo de bioma, (4) elementos decorativos**.
- Conservar una escala/perspectiva y grosor de línea coherentes entre los módulos.
- Los bocetos son conceptuales y comparativos, no capturas de un mapa jugable definitivo.
- Si se pide **un solo bioma**, usar una sola composición hexagonal más grande, sin necesidad de introducir otras categorías; si se piden **varios**, usar módulos comparativos.
- En bocetos de elevación, mantener desniveles creíbles y progresivos, no una pila arbitraria de columnas hexagonales. En agua, representar hexágonos y costuras claramente.
- Los subtipos mostrados deben corresponder al catálogo conceptual vigente; no reintroducir clasificaciones antiguas o arbitrarias.

### Criterios de aceptación de futuros bocetos

Un boceto **se considera fallido** si: su grid no es claramente hexagonal; está oculta por bosque, océano o elementos; solo se ven siluetas externas de grandes bloques y no los hexágonos internos; los elementos decorativos saturan la lámina; parece fotorrealista o un mapa jugable terminado; o no conserva la estética suave y limpia de la lámina aprobada.

**Instrucción reutilizable para crear bocetos:**
> G-Evolve — lámina conceptual isométrica 2.5D de dioramas formados por HEXÁGONOS REALES UNIDOS. **Dibuja primero la cuadrícula hexagonal de cada mosaico, con TODOS los bordes internos marcados y VISIBLES** de forma nítida, en terreno, nieve y agua. Construye el suelo, alturas y biomas sobre esa grid, nunca ocultándola. Acabado hand-drawn digital suave, paleta natural ligeramente desaturada, caras laterales isométricas, fondo crema/blanco, composición editorial espaciosa, etiquetas discretas, muy pocos árboles/rocas/props. Mínimo ruido visual; leer primero las celdas, luego el relieve, finalmente la vegetación. Conservar el mismo estilo de la concept sheet «G-EVOLVE — BIOMAS DEL MUNDO» aprobada.

Esta sección especifica **el tratamiento de bocetos** y refuerza las reglas ya establecidas de hexágonos visibles para el mundo completo; prevalece sobre cualquier descripción histórica de cuadrícula «sutil», «casi invisible» o susceptible de ocultarse.


## Lámina de biomas seleccionada — grid remarcada (21 de octubre de 2026)

**Estado:** referencia visual preferida y aprobada por el usuario, después de pedir mayor uniformidad y contraste de la malla hexagonal.

**Imagen fuente de la conversación:** `a_clean_infographic_style_illustration_flat_isome.png` (PNG, 1536 × 1024). **Importante:** nombre del archivo original generado en la conversación; el binario todavía NO está cargado en GitHub, por lo que este apartado no representa una subida de imagen. Conservar el PNG para incorporarlo posteriormente a una carpeta de referencias gráficas.

**Título en la lámina:** «G-EVOLVE — BIOMAS DEL MUNDO», `CONCEPT SHEET / HEX GRID · V0.2.1`.

**Aspectos específicos aprobados:** lámina editorial sobre fondo crema, mosaicos de hexágonos isométricos por ecosistema, elementos paisajísticos muy escasos, vegetación y relieve sugeridos sin saturación, paleta suave pero definida, títulos discretos y rangos de elevación habituales de cada tipo. La grid de esta versión tiene **bordes internos más contrastados, uniformes y claramente dibujados**, con énfasis blanco o gris contra las superficies de agua, bosque, llanura, desierto, nieve y piedra. Esta referencia prevalece sobre los bocetos anteriores de grid menos visible.

**Invariantes para reproducciones:** comenzar dibujando una malla hexagonal exacta y regular; cada hexágono debe conservar bordes internos legibles; añadir terrenos y objetos encima sin cubrir sistemáticamente la retícula; conservar la misma presentación comparativa limpia, los nombres de los biomas y la estética isométrica hand-drawn. No convertir el esquema en un mapa cargado de árboles ni en una textura de celdas borrosas.
