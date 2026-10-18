# Evolve — Referencia de diseño y simulación

[Plantas y animales: categorías del juego](biology.md)

[Catálogo de recursos y relaciones](resources.md)

[Diagramas completos de cada catálogo](catalog-diagrams.md)

[Referencia gráfica sencilla](visual-reference.md)

Estructuras JSON completas, tipos y ejemplos: [referencia de JSON](json-structures.md).

Última actualización documentada: 2026-10-17 (America/Guatemala).

Esta carpeta es la referencia compartida para diseñar, implementar y revisar el proyecto. Los Markdown sirven tanto para personas como para herramientas de desarrollo; no existe un archivo de instrucciones exclusivo para agentes.

## 1. Punto de entrada

| Archivo | Propósito |
| --- | --- |
| [agriculture.technologies.json](../../data/technologies/agriculture.technologies.json) | Definiciones agrícolas que interpretará el motor. |
| [agriculture.technologies.md](../en/agriculture.technologies.md) | Referencia técnica en inglés. |
| [agriculture.technologies.es.md](../es/agriculture.technologies.md) | Referencia técnica en español. |

La configuración actual contiene 23 tecnologías al mismo nivel en una lista plana. Su versión estructural es `2.0.0` y su versión de contenido es `0.3.0`. Estos números no son la versión de lanzamiento de Evolve ni la del cuaderno general de diseño.

## 2. Dirección arquitectónica acordada

Primero se desarrollará una simulación por turnos sin depender de gráficos. Se validará el funcionamiento del juego antes de trabajar en la presentación y la interfaz. El motor gráfico y el lenguaje de implementación siguen pendientes.

Existen dos categorías de datos:

- `GameDefinitions`: configuración de solo lectura con tecnologías, recursos, especies, condiciones, costes y efectos posibles.
- `GameState`: estado de cada partida, con turnos, civilizaciones, descubrimientos, inventarios y progreso.

`SimulationEngine` es el código que interpreta las definiciones y actualiza el estado. No es una tercera categoría de archivos JSON.

Cada categoría puede repartirse entre varios archivos; su cantidad no cambia esta separación.

## 3. Convenciones técnicas

- Los IDs, propiedades, enumeraciones, eventos y código se escriben en inglés.
- Los campos visibles `name` y `description` contienen traducciones `en` y `es`.
- Los IDs son estables. Nunca se usan traducciones como identidad o dependencia.
- La documentación se mantiene en inglés y español.
- Respaldo de idioma: idioma solicitado, después `defaultLanguage` y finalmente el ID.
- Los gráficos y las coordenadas de diseño no forman parte del progreso tecnológico.

## 4. Investigación y especies

Cada investigación se identifica por `(civilizationId, technologyId, speciesId)`.

- Las tecnologías generales usan `speciesId: null`.
- Las tecnologías por especie mantienen progreso independiente.
- Trigo y maíz pueden compartir una definición de cultivo sin compartir sus descubrimientos ni su progreso.
- Los costes se expresan en puntos. Los turnos estimados dependen de la producción actual de investigación.
- `order` ordena la presentación; los requisitos explícitos determinan las dependencias y permiten avances paralelos.

Conocer una técnica, disponer de materiales y operar una instalación son comprobaciones distintas. Perder semillas no borra el conocimiento del cultivo. Investigar alfarería no crea vasijas. Investigar manejo de domesticación no domestica una especie instantáneamente.

## 5. Lo que existe actualmente

- Configuración de agricultura y contrato documentado para el futuro motor.
- Nombres y descripciones bilingües.
- Dependencias externas declaradas.
- Comprobaciones internas de JSON, IDs y ciclos de requisitos.
- Documentación, ejemplos y limitaciones de integración conocidas.

## 6. Lo provisional o todavía no implementado

- Costes, umbrales de eurekas y balance numérico.
- JSON Schema formal.
- Catálogos ejecutables aprobados: especies, balance/almacenamiento de recursos, objetos, recetas y lugares; las guías no completan su comportamiento operativo.
- Tecnologías externas y validación completa entre ramas.
- Código del simulador, guardado/carga y migraciones.
- Cálculos de suelo, reproducción, domesticación y producción.
- Orden exacto de resolución de cada turno.
- Motor gráfico, lenguaje de programación e interfaz.

La configuración propone un contrato de funcionamiento. No significa que el evaluador o la simulación ya estén implementados.

## 7. Decisiones pendientes antes de implementar

1. Expresar los contadores distintos y agrupados de eurekas mediante modos estructurados explícitos.
2. Definir el primer esquema de `GameState`, su compatibilidad y migraciones.
3. Concretar propiedad, accesibilidad y contexto local de recursos y equipos.
4. Fijar las fases del turno y cuándo afecta la nueva tecnología a la producción.
5. Implementar y validar cada condición, evento y efecto.
6. Definir ancestros silvestres, identidades de cultivos y propagación en el catálogo de especies.

Las referencias técnicas agrícolas detallan estas limitaciones. Una etiqueta visible no sustituye una regla todavía pendiente.

## 8. Mantenimiento de la documentación

Registrar en cada cambio su propósito, definiciones afectadas, impacto de compatibilidad y validación. Mantener alineadas las versiones en inglés y español.

Distinguir decisiones confirmadas, configuración de prototipo y preguntas abiertas. Conservar los IDs estables. Cambiar el tipo de un campo exige adaptar sus lectores, aunque el número de versión parezca menor.

El repositorio Git EvolveDoc es ahora la referencia principal. Los archivos de Drive son versiones anteriores y no se sincronizan automáticamente. Los cambios se registran con commits, conservando los IDs. Consulta [identificadores](identifiers.md) y [estructura](repository.md).

## 9. Siguiente hito propuesto

Validar un escenario pequeño sin gráficos con dos civilizaciones y conocimiento de trigo/maíz:

1. Cargar las definiciones y resolver sus dependencias.
2. Inicializar estados independientes por civilización y especie.
3. Procesar investigación y un eureka.
4. Comprobar condiciones locales antes de usar una capacidad.
5. Guardar y cargar sin duplicar recompensas ni modificar definiciones.

Es una propuesta de primer hito, no una función terminada.


## 10. Definiciones planas y guía del mundo

La versión estructural `2.0.0` elimina los contenedores de nodos tecnológicos. Los requisitos explícitos siguen definiendo el grafo; el orden visible no obliga a investigar secuencialmente. Se conservan los IDs.

`world.catalog.guide.json` convierte el documento de generación del mundo en una guía estructurada. Conserva todas las apariciones regionales de flora, fauna y minería. Todavía no es un catálogo de especies resuelto: taxonomía, rangos y balance pendientes usan `null`, sin inventar valores. No debe cargarse como generación jugable antes de revisar estos datos. El documento fuente permanece intacto.

### Archivos del catálogo del mundo

- [world.catalog.guide.json](../../data/world/world.catalog.guide.json)
- [world.catalog.guide.en.md](../en/world.catalog.guide.md)
- [world.catalog.guide.es.md](../es/world.catalog.guide.md)

## Ejemplos del repositorio

Los [ejemplos de simulación](../../simulation/README.md) muestran investigación independiente por especie con la definición agrícola real. Son ejemplos educativos, no un motor completo. La guía del mundo está dividida en catálogos relacionados; consulta la [estructura](repository.md).

La guía usa categorías generales como zorros y robles. Solo se conservan diferencias útiles para el juego. La taxonomía científica es opcional. Ver [entidades](biology.md).
