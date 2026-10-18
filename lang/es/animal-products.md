# Animales: recursos y formas de obtención

[Tabla completa de los 101 animales](../../data/animals/PRODUCTS.es.md) · [JSON completo](../../data/animals/animals.catalog.guide.json) · [Todos los campos y ejemplos](json/data--animals--animals.catalog.guide.md)

El criterio detallado se aplica a todos los animales del catálogo, no solo a los zorros. Cada entidad mantiene su nombre general y reúne los materiales útiles según su anatomía. La selección no pretende enumerar todos los tejidos o usos industriales posibles, ni afirmar que cada animal se aprovechaba habitualmente como alimento. No se añaden especies científicas como requisito.

## Referencia sencilla

| Grupo o caso | Materiales principales | Obtención o condición |
| --- | --- | --- |
| Mamíferos terrestres | Carne, piel, huesos y grasa | Despiece y desollado de un cuerpo aprovechable. |
| Ciervos y alces | Lo anterior y astas; tendones útiles | Astas de individuos que las tengan o ya desprendidas. |
| Antílopes, bisontes e íbices | Carne, piel, huesos, grasa, cuernos y tendones | Cuernos presentes; no se tratan como astas caídas. |
| Aves | Carne, huesos, grasa, plumas y huevos | Cuerpo muerto para tejidos; plumas caídas y huevos existentes por recolección. |
| Peces | Carne de pescado, huesos cuando hay esqueleto óseo, piel aprovechable y tejidos grasos | Preparación del pescado; aceite mediante extracción posterior. |
| Cangrejos y krill | Carne y caparazón/exoesqueleto | Captura y aprovechamiento; no producen huesos de vertebrado. |
| Moluscos y bivalvos | Carne, conchas y perlas condicionadas | No todos los individuos contienen perlas. Conchas vacías no conceden carne. |
| Tortugas | Carne, huesos, grasa, piel aprovechable, caparazón y huevos | El caparazón no es un material que se desprende y regenera como el pelaje. |
| Elefantes | Tejidos del cuerpo, colmillos y tendones | Marfil preparado mediante proceso y solo desde colmillos aptos. |
| Animales con fibra aprovechable | Fibra animal | Esquila controlada, peinado, material desprendido o recuperación del cuerpo, según la ficha. |
| Reno y dromedario bajo manejo | Leche y estiércol, además de materiales del cuerpo | Leche solo de hembras lactantes manejadas; no por encontrar animales silvestres. |

La tabla completa distingue excepciones: barbas solo en ballenas con esa anatomía; huevos de equidna como excepción biológica en bolsa; sin huevos recolectables para serpientes de cascabel; jirafas y okapis no reciben el recurso de cuerno queratinoso. El krill conserva revisión pendiente de viabilidad de captura y época, sin inventar técnicas históricas.

## Estructura de los objetos

- `potentialProducts[]`: recurso, métodos de obtención, condiciones de disponibilidad, proceso posterior si lo hay, notas bilingües y referencias.
- `acquisitionMethods[]`: métodos al mismo nivel, con `tag`, `name`, `description`, `sourceOutcome`, restricciones y ejecución deshabilitada.
- `productEvidenceSources[]`: fuentes de anatomía y usos generales; no certifican rendimientos ni aprovechamientos históricos para cada categoría.
- `serviceUseCandidates[]`: candidatos de transporte, tiro o trabajo separados de materiales. Entrenamiento e idoneidad siguen pendientes; no son productos de inventario.
- `productCoverage`: cobertura actual de 101 animales, 498 asociaciones de materiales, 17 métodos y 7 candidatos de servicio.

`availabilityConstraints` contiene etiquetas de diseño en inglés, no condiciones ejecutables. Algunas dependen del individuo, sexo, reproducción, material realmente presente o manejo. El resultado no es una bolsa garantizada con todos los productos de la ficha.

`sourceOutcome` distingue:

| Valor | Significado |
| --- | --- |
| `requires_dead_animal` | La operación material requiere un cuerpo muerto. |
| `consumes_animal` | El aprovechamiento consume al animal, como abrir y procesar un marisco. |
| `preserves_animal` | Método planteado para conservar al animal, con manejo adecuado. |
| `collects_discarded_material` | Recoge materiales ya desprendidos o deyecciones existentes. |
| `removes_egg_without_killing_adult` | Conserva al adulto, pero retirar un huevo fecundado afecta posibles crías. |

Estas operaciones describen cómo se obtiene el material. No fijan todavía si cazar y despiezar se resolverán con uno o varios clics/órdenes en la interfaz. No se crea un nuevo tipo de cadáver en GameState en esta revisión.

## Materia cruda y transformada

Piel no equivale a cuero curtido; grasa no equivale a aceite; tendón crudo no equivale a cuerda; colmillo no concede marfil preparado automáticamente.

`RES#000106` identifica tendones sin preparar. `RES#000105` continúa identificando huesos. Se conservan todas las asignaciones anteriores. El material genérico de concha/caparazón conserva su ID y debe conservar origen y composición antes de evaluar futuras recetas.

Los productos procesados apuntan mediante `processingTag` a una guía de transformación. Aceite animal, de pescado y de ballena requieren su proceso y origen correcto. `inputProvenancePolicy` impide interpretar grasa terrestre como grasa de pescado o cualquier diente como colmillo apto para marfil. `requiresProcessing: false` en un vínculo de materia cruda no elimina el despiece, desollado u otra operación de obtención.

Las 28 guías de transformación siguen sin cantidades, equipos, tiempos ni recetas ejecutables. No conceder simultáneamente toda la grasa cruda y el aceite derivado de esa misma grasa, ni contar el mismo pelaje como fibra extraída y como piel con pelo intacto.

## Alcance terminado y pendientes

Se completa la referencia inicial **animal → material → forma de obtención**, con condiciones cualitativas. No es una simulación productiva implementada ni una aprobación de todos los servicios animales. El catálogo actual contiene muchas formas silvestres: ovejas, cabras y otras formas domésticas adicionales se concretarán en la tarea de domesticación, sin inventar que sus materiales ya están cubiertos por esas entidades inexistentes.

Quedan pendientes cantidades, tiempos, consumo de cuerpos/materiales, reproducción, regeneración, tecnología/equipos concretos, conservación, aptitud alimentaria, balance y fases del turno. Todo permanece deshabilitado para ejecución. Plantas es el siguiente bloque del [roadmap](../../ROADMAP.es.md).

## Verificación y actualización

```sh
python tools/generate_animal_products.py
python tools/generate_json_reference.py
python tools/generate_catalog_diagrams.py
python tools/validate_repository.py
```

El verificador comprueba todas las asociaciones, métodos, referencias, traducciones, límites anatómicos y guías de productos procesados. No sustituye una revisión biológica individual ni demuestra una práctica histórica o idoneidad alimentaria. Fuentes y límites específicos están al final de la tabla completa.
