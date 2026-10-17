# Plantas, animales y formas biológicas

[Plantas: catálogo completo, correspondencias y ramas](../../data/plants/BIOLOGY.es.md) · [Animales: catálogo completo, correspondencias y ramas](../../data/animals/BIOLOGY.es.md)

Este diseño precisa las identidades biológicas sin fijar cantidades, tiempos, probabilidades, rendimientos ni fórmulas de simulación. Las colecciones siguen al mismo nivel y se relacionan por IDs.

## Qué representa cada objeto

| Colección | Significado | Ejemplo |
| --- | --- | --- |
| `speciesCandidates` | Etiqueta original, su procedencia y las apariciones regionales existentes. Puede describir un grupo. | Robles, trigo silvestre, jabalí. |
| `taxa` | Identidad científica aceptada por un proveedor explícito, con rango y evidencia del cotejo. | `Quercus robur`, `Sus scrofa`. |
| `biologicalForms` | Forma cultivada, domesticada, población ancestral de referencia o grupo de cultivo. No es un individuo ni una población de partida. | Conejo silvestre y doméstico pueden compartir taxón. |
| `lineageRelations` | Relación histórica entre formas; distingue domesticación, selección, hibridación, aporte ancestral e introgresión. | Dos aportes ancestrales para trigo panadero. |
| `excludedLineageRelations` | Supuesto directo que no debe introducirse como hecho. | Przewalski → caballo doméstico moderno. |
| `evidenceSources` | Bibliografía de relaciones, enlazada mediante `sourceKey`. | Estudio genómico de domesticación. |

`taxonResolution` vincula cada candidato a sus `taxonIds` y `formIds`. Sus formas son referencias asociadas: no indican que un animal doméstico deba aparecer inicialmente donde se enumeró su pariente silvestre. `selectionMode` distingue una interpretación específica de una selección representativa no exhaustiva. Los IDs anteriores no se eliminan ni se sustituyen silenciosamente.

Los grupos agrícolas también seleccionan taxones concretos. Así, trigo puede contener escanda menor, escanda mayor, trigo duro y trigo panadero; arroz asiático y africano quedan separados. Una forma cultivada de referencia registra la identidad de diseño, sin afirmar que su domesticación ancestral ya esté investigada.

## Identidades permanentes

- `PLT`: taxón vegetal; `ANM`: taxón animal; `ALG`: alga; `FNG`: hongo, incluidos los liquenizados.
- `FRM`: forma biológica, grupo de cultivo o población de referencia.
- Cada prefijo tiene una secuencia independiente de seis cifras. Las formas de ambas carpetas comparten una sola secuencia FRM. Los IDs asignados están en estos JSON: conservarlos al ampliar el catálogo; nunca recalcularlos ordenando nombres.
- `VAR` sigue significando variante regional del mundo. Una variedad botánica es un taxón con rango `VARIETY`; un grupo de cultivares usa `FRM` y `formKind: "cultivar_group"`. No son equivalentes.

La carpeta de plantas conserva la flora original e incluye algas y líquenes. `organismGroup`, el reino y el prefijo impiden tratar un liquen como planta botánica. Las etiquetas latinas se mantienen iguales en `name.en` y `name.es`; los nombres comunes originales permanecen bilingües en sus candidatos. No se inventan traducciones específicas para nombres comunes ambiguos.

## Cómo leer los parentescos

La rama de trigo distingue domesticación de escandas, selección de trigo duro y origen híbrido de trigo panadero. `hybrid_origin` requiere conjuntamente los `parentFormIds`: no son alternativas ni una receta jugable. Los grupos de cebada de dos y seis hileras son selección dentro del cultivo, no especies nuevas ni cultivares modernos con nombre.

El maíz distingue domesticación desde teocintle del Balsas y aporte genético posterior de teocintle mexicano. La introgresión no se interpreta como otra domesticación. En animales, uro se ramifica hacia linajes taurinos y cebuinos; el cebú no es una mejora del ganado taurino. Las poblaciones silvestres actuales pueden ser representantes de un complejo ancestral, no la población fundadora exacta.

No se añade una relación solo porque dos especies pertenezcan al mismo género o se parezcan. Los ancestros desconocidos, razas y cultivares históricos sin evidencia permanecen pendientes. El catálogo registra 25 resúmenes de relaciones, no el árbol evolutivo completo de todos los organismos.

## Evidencia y límites

Los nombres científicos seleccionados se cotejaron con GBIF: coincidencia `EXACT`, puntuación del proveedor al menos 95 y rango de especie/subespecie/variedad; los sinónimos enlazan al taxón aceptado. La puntuación no mide certeza de que la etiqueta original represente esa especie. Cada registro guarda proveedor, clave, URL, consulta y fecha. Camelus ferus usa el catálogo GBIF Catalogue of Life XR indicado en su registro; los tratamientos taxonómicos pueden diferir entre autoridades.

Esto valida el cotejo de nombres, no la selección original completa. Cada elección representativa necesita revisar distribución nativa, hábitat, introducciones históricas y productos. Las 485 apariciones originales conservan su significado de procedencia; no se duplican para generar automáticamente todas las especies seleccionadas.

`inheritResourceBindings: false` impide heredar automáticamente productos de grupos generales. Madera sigue siendo recurso, no especie. Para convertir una forma concreta en fuente de leche, fibra o semillas se revisarán sus vínculos propios, además de anatomía, sexo y etapa de vida cuando corresponda. Las cadenas de transformación de recursos permanecen en su catálogo.

Las referencias de cultivo sin relación de ascendencia documentada están pendientes de revisión, no carecen de ancestros. No hay razas animales ni cultivares históricos individuales enumerados todavía. Las formas y relaciones no se cargan como reglas ejecutables: `loadAsGameDefinitions` y `runtimeEnabled` permanecen en `false`.

## Estructura, ejemplos y comprobaciones

Los contratos completos, objetos internos y ejemplos están en:

- [JSON de plantas](json/data--plants--plants.biological.catalog.md).
- [JSON de animales](json/data--animals--animals.biological.catalog.md).
- [Esquema biológico](json/schemas--biological.catalog.schema.md).
- [JSON de candidatos vegetales](json/data--plants--plants.catalog.guide.md).
- [JSON de candidatos animales](json/data--animals--animals.catalog.guide.md).

El esquema estructural cubre todos los objetos actuales. El verificador propio comprueba IDs, referencias, nombres cotejados almacenados, límites de ejecución, bibliografía, cobertura y ausencia de ciclos en ascendencia/selección. No consulta servicios en vivo ni demuestra por sí mismo una hipótesis científica. La integración con un motor general de JSON Schema continúa separada.

```sh
python tools/generate_json_reference.py
python tools/generate_biology_reference.py
python tools/generate_catalog_diagrams.py
python tools/validate_repository.py
```

El ejemplo de investigación conserva sus alias anteriores de trigo/maíz. Antes de implementar progreso definitivo por especie se elegirá el taxón o forma correspondiente y se diseñará la migración. Este cambio no modifica partidas ni cantidades de producción.
