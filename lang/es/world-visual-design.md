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
4. Asignar biomas y variantes regionales en función del conjunto de condiciones, **no solo de la altitud**.
5. Distribuir flora, fauna y recursos de acuerdo con los catálogos y las restricciones geográficas.

**Biomas del catálogo actual (7):** bosque tropical, bosque templado, tundra, sabana, desierto, marino y alta montaña/alpino. El catálogo incluye **27 variantes regionales**. Los umbrales climáticos, la abundancia y la distribución concreta siguen pendientes de diseño y balance.

## Reglas visuales

- Paisaje continuo y cuadrícula hexagonal de baja prominencia; intensificar la cuadrícula al seleccionar, construir o mover.
- Relieve volumétrico con numerosas cotas, laderas, mesetas, barrancos, valles y cordilleras; evitar que los niveles se vean como plataformas artificiales salvo donde el relieve lo amerite.
- Biomas diferenciados por vegetación, densidad, color y textura, con transiciones naturales.
- Ríos y caminos continuos; costas irregulares; geografía conectada.
- Recursos visibles como indicios representativos, con detalle consultable mediante selección y capas temáticas.
- Asentamientos y actividades humanas modifican progresivamente el paisaje.
- No confundir la representación visual con las cantidades lógicas de árboles, depósitos o animales.

## Referencia artística aprobada

**Boceto:** «G-Evolve — Concepto de Mundo: terreno, biomas y generación procedural de un mundo continuo», aprobado en conversación. Incluye un paisaje isométrico con los siete biomas, una sección ilustrativa de relieve progresivo y ejemplo de cuadrícula sutil.

**Archivo de imagen original generado:** `g_evolve_procedural_biome_world_map.png` (pendiente de incorporar como archivo binario al repositorio). Este documento preserva las decisiones aprobadas, pero **no declara la imagen cargada en GitHub** hasta que se confirme su subida.

## Estado de implementación

Esta especificación es documentación conceptual; no activa definiciones ejecutables. El catálogo existente continúa siendo la fuente de IDs y relaciones. La elevación numérica, las pendientes, los algoritmos de transición y los límites geográficos serán objeto de validación y simulación antes de programar.
