# Estructura y responsabilidades del repositorio

[Catálogo de recursos y relaciones](resources.md)

Estructuras JSON completas, tipos y ejemplos: [referencia de JSON](json-structures.md).

Este repositorio reúne documentación, catálogos de diseño y simulaciones educativas pequeñas. La raíz equivale a `evolve/`; no se agrega otra carpeta `evolve` adentro.

| Carpeta | Responsabilidad |
| --- | --- |
| `lang/en`, `lang/es` | Documentación de diseño y técnica en ambos idiomas. Todavía no son catálogos extraídos de traducciones de la interfaz. |
| `data/world` | Biomas, variantes regionales, elevación, reglas geográficas, apariciones del documento y enlaces a catálogos. |
| `data/animals` | Candidatos de fauna; después especies exactas, poblaciones, domesticación y productos. |
| `data/plants` | Candidatos de flora y cultivos; después especies, ancestros, variedades, reproducción y productos. |
| `data/minerals` | Candidatos geológicos; después yacimientos, extracción, procesamiento y requisitos. |
| `data/resources` | 104 materiales con vínculos de origen y extremos de transformación; cantidades y recetas pendientes. |
| `data/technologies` | Tecnologías al mismo nivel, requisitos, costos de investigación y eurekas. |
| `schemas` | Contratos estructurales iniciales y sus límites. |
| `simulation` | Datos de ejemplo y demostraciones ejecutables; no el motor definitivo. |
| `tools` | Verificaciones de consistencia del repositorio. |

## Relación entre catálogos

La guía principal es `data/world/world.catalog.guide.json`. Sus rutas `catalogFiles` se resuelven respecto de ese archivo. Plantas y animales tienen `speciesCandidates`; plantas también tiene `agriculturalCropCandidates`. Minerales contiene `geologicalResourceCandidates`. El mundo conserva las 485 `resourceOccurrences`, cuyos `definitionId` apuntan a esos catálogos.

La separación conserva todos los registros originales sin otra copia combinada que compita como fuente principal. La separación inicial usó mundo 1.1.0/0.2.0. Los vínculos de recursos usan ahora mundo 1.2.0/0.3.0, guías de plantas/animales/minerales 1.1.0/0.2.0 y guía de recursos 1.0.0/0.1.0. Agricultura permanece sin cambios en 2.0.0/0.3.0.

`null` significa pendiente. Una lista regional vacía no permite aparición mundial. Los catálogos guía siguen deshabilitados para generación real. Se conserva la clasificación del documento: por ejemplo, los líquenes permanecen en flora hasta revisarlos.

## Arquitectura

`GameDefinitions` describe posibilidades y no cambia durante la partida. `GameState` guarda descubrimientos, inventarios, poblaciones y avances. El futuro `SimulationEngine` interpreta las definiciones. Tener varios JSON no implica agregar capas arquitectónicas.

Linaje biológico, selección/domesticación y mejoras técnicas deben ser relaciones separadas; no se deducen de niveles. La evolución de minerales se refiere a extracción y procesamiento, no a evolución biológica. Los productos y recetas deben definirse antes de activar rendimientos.

## Cambios

Git es la referencia principal desde esta migración. Drive no se sincroniza automáticamente. Actualizar ambos idiomas juntos y registrar propósito, validación y compatibilidad en los commits. Conservar dudas explícitas en lugar de inventar taxonomía o balance. No subir partidas reales, credenciales ni cachés generadas.
