# `data/minerals/minerals.catalog.guide.json`

[JSON fuente](../../../data/minerals/minerals.catalog.guide.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"1.0.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.1.0"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"design_guide_requires_resolution"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"mineral_catalog_design_guide"` |
| `geologicalResourceCandidates` | `array<object>` | 1/1 | Materiales y formas geológicas pendientes de yacimientos y procesamiento. | `—` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"null means unresolved; it is not zero or unrestricted."` |

### `$.geologicalResourceCandidates[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 57/57 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"geological_clay"` |
| `name` | `object` | 57/57 | Nombre visible mediante claves de idioma. | `—` |
| `definitionStatus` | `string` | 57/57 | Madurez del registro; los candidatos no son definiciones ejecutables. | `"source_candidate"` |
| `geologyConstraints` | `null` | 57/57 | Requisitos geológicos pendientes; el bioma por sí solo no basta. | `null` |
| `refinedOutputResourceId` | `null` | 57/57 | Referencia al recurso procesado; extraer no concede metal refinado directamente. | `null` |
| `surfaceAndOreDistinction` | `string` | 57/57 | Regla que distingue material superficial, mena y producto procesado. | `"No refined metal is granted directly by a deposit. Extraction and processing recipes remain separate."` |
| `sourceLabel` | `string` | 57/57 | Etiqueta original en español para trazabilidad, no texto localizado de interfaz. | `"Arcilla"` |

### `$.geologicalResourceCandidates[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 57/57 | Texto visible en inglés. | `"Clay"` |
| `es` | `string` | 57/57 | Texto visible en español. | `"Arcilla"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.0.0",
  "contentVersion": "0.1.0",
  "status": "design_guide_requires_resolution",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "null means unresolved; it is not zero or unrestricted."
  },
  "kind": "mineral_catalog_design_guide",
  "geologicalResourceCandidates": [
    {
      "id": "geological_clay",
      "name": {
        "en": "Clay",
        "es": "Arcilla"
      },
      "definitionStatus": "source_candidate",
      "geologyConstraints": null,
      "refinedOutputResourceId": null,
      "surfaceAndOreDistinction": "No refined metal is granted directly by a deposit. Extraction and processing recipes remain separate.",
      "sourceLabel": "Arcilla"
    }
  ]
}
```
