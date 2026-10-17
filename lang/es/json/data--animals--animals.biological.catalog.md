# `data/animals/animals.biological.catalog.json`

[JSON fuente](../../../data/animals/animals.biological.catalog.json) · [Index](../json-structures.md)

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
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"biological_taxon_catalog"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"taxonomy_names_verified_representative_choices_and_ecology_pending"` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Reglas y restricciones para interpretar esta guía. | `—` |
| `taxa` | `array<object>` | 1/1 | Taxones aceptados al mismo nivel; especies, subespecies o variedades botánicas según proveedor. | `—` |
| `biologicalForms` | `array<object>` | 1/1 | Poblaciones de referencia, formas domesticadas y grupos de cultivo; no instancias vivas. | `—` |
| `lineageRelations` | `array<object>` | 1/1 | Resúmenes históricos de ascendencia/selección con evidencia; no recetas ejecutables. | `—` |
| `excludedLineageRelations` | `array<object>` | 1/1 | Advertencias explícitas contra relaciones directas de ascendencia no justificadas. | `—` |
| `evidenceSources` | `array<object>` | 1/1 | Bibliografía que respalda relaciones seleccionadas y reglas taxonómicas. | `—` |
| `reviewIssues` | `array<object>` | 1/1 | Contradicciones de la fuente y preguntas de diseño pendientes. | `—` |
| `summary` | `object` | 1/1 | Conteos para comprobar integridad de los catálogos. | `—` |

### `$.runtimePolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False impide tratar esta guía como definiciones jugables. | `false` |
| `unknownValues` | `string` | 1/1 | Aclara que null pendiente no equivale a cero o sin restricciones. | `"A name match does not verify native distribution, ecology, resource outputs, domestication eligibility or histo…` |
| `identityPolicy` | `string` | 1/1 | El texto traducido no se utiliza como identidad o dependencia. | `"New taxon IDs use PLT, ANM, ALG or FNG prefixes; forms use FRM. Existing candidate/resource/technology IDs rema…` |
| `sourceInterpretation` | `string` | 1/1 | Distingue selecciones representativas de diseño e identificaciones únicas de la fuente. | `"Broad source groups have explicit non-exhaustive representative choices. These are design selections, not uniqu…` |
| `resourceInheritance` | `string` | 1/1 | Política que impide heredar automáticamente productos de grupos generales. | `"Candidate resource bindings do not automatically transfer to every selected taxon or form."` |
| `lineagePolicy` | `string` | 1/1 | La ascendencia documentada es independiente de transformaciones automáticas del juego. | `"Relations summarize evidence, not automatic gameplay transitions. Hybrid and introgression edges are not domest…` |
| `varietyPolicy` | `string` | 1/1 | Distingue especies, formas de referencia, grupos de cultivo y cultivares/razas con nombre. | `"Cultivar groups are not species, botanical varieties or named cultivars. No modern named cultivars or animal br…` |
| `floraClassification` | `string` | 1/1 | Aclara que flora incluye algas y hongos liquenizados clasificados explícitamente. | `"The plants folder includes source flora, including algae and lichenized fungi. Their scientific kingdom and ALG…` |

### `$.taxa[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 168/168 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"ANM#000001"` |
| `tag` | `string` | 168/168 | Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales. | `"alces_alces"` |
| `name` | `object` | 168/168 | Nombre visible mediante claves de idioma. | `—` |
| `scientificName` | `string` | 168/168 | Nombre científico de la fuente o del registro aceptado del proveedor; null en la fuente original significa pendiente allí. | `"Alces alces (Linnaeus, 1758)"` |
| `taxonRank` | `string` | 168/168 | Rango del proveedor: especie, subespecie o variedad; una forma es otra entidad. | `"SPECIES"` |
| `organismGroup` | `string` | 168/168 | Clasificación explícita de animal, planta, alga u hongo liquenizado. | `"animal"` |
| `taxonomy` | `object` | 168/168 | Identidad científica, evidencia y revisión. | `—` |
| `reviewStatus` | `string` | 168/168 | Revisión pendiente antes de autorizar un producto del origen. | `"taxon_name_matched_source_interpretation_and_ecology_pending"` |
| `nativeRangeReviewStatus` | `string` | 168/168 | Validar un nombre no valida la distribución nativa. | `"not_validated_by_name_match"` |
| `runtimeEnabled` | `boolean` | 168/168 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |

### `$.taxa[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 168/168 | Texto visible en inglés. | `"Alces alces"` |
| `es` | `string` | 168/168 | Texto visible en español. | `"Alces alces"` |

### `$.taxa[].taxonomy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `kingdom` | `string` | 168/168 | Reino biológico según el proveedor taxonómico indicado. | `"Animalia"` |
| `family` | `string` | 168/168 | Familia según el proveedor taxonómico; null si no está disponible. | `"Cervidae"` |
| `genus` | `string` | 168/168 | Género según el proveedor taxonómico. | `"Alces"` |
| `provider` | `string` | 168/168 | Conjunto taxonómico utilizado para esta versión. | `"GBIF Backbone"` |
| `providerTaxonKey` | `string` | 168/168 | Clave de taxón aceptado del proveedor como cadena; no es un ID de Evolve. | `"2440940"` |
| `taxonomicStatus` | `string` | 168/168 | Estado aceptado del taxón según el proveedor indicado. | `"ACCEPTED"` |
| `referenceUrl` | `string` | 168/168 | Registro público del proveedor para el taxón aceptado. | `"https://www.gbif.org/species/2440940"` |
| `matchEvidence` | `array<object>` | 168/168 | Evidencia de cotejo científico; no identifica de forma única un nombre común ambiguo. | `—` |

### `$.taxa[].taxonomy.matchEvidence[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `queriedName` | `string` | 168/168 | Nombre científico enviado al servicio taxonómico. | `"Alces alces"` |
| `matchedScientificName` | `string` | 168/168 | Nombre cotejado antes de resolver sinónimos; la identidad aceptada se registra aparte. | `"Alces alces (Linnaeus, 1758)"` |
| `matchType` | `string` | 168/168 | Resultado exacto/aproximado/rango superior; esta referencia solo admite EXACT. | `"EXACT"` |
| `matchStatus` | `string` | 168/168 | Estado del nombre consultado; puede ser SYNONYM aunque el taxón guardado sea ACCEPTED. | `"ACCEPTED"` |
| `confidence` | `integer` | 168/168 | Puntuación del proveedor; no es certeza porcentual de la interpretación original. | `99` |
| `requestUrl` | `string` | 168/168 | URL reproducible de consulta; los resultados pueden cambiar al actualizarse el proveedor. | `"https://api.gbif.org/v1/species/match?name=Alces+alces&strict=true&verbose=true"` |
| `checkedOn` | `string` | 168/168 | Fecha de consulta de la referencia; no es fecha de publicación. | `"2026-10-17"` |

### `$.biologicalForms[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 28/28 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"FRM#000050"` |
| `tag` | `string` | 28/28 | Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales. | `"wild_boar"` |
| `taxonId` | `string` | 28/28 | Referencia al taxón de esta forma biológica. | `"ANM#000148"` |
| `name` | `object` | 28/28 | Nombre visible mediante claves de idioma. | `—` |
| `formKind` | `string` | 28/28 | Categoría de forma; no implica especie nueva, raza ni capacidad desbloqueada. | `"wild_ancestral_proxy"` |
| `literatureName` | `string` | 28/28 | Nombre científico/histórico de la forma; puede diferir del nombre aceptado del proveedor. | `"Sus scrofa"` |
| `evidenceSourceKeys` | `array<string>` | 28/28 | Claves de bibliografía; vacío indica que aquí no se afirma un linaje específico. | `["pig_2015"]` |
| `status` | `string` | 28/28 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"reference_form_not_an_instance_or_unlock"` |
| `runtimeEnabled` | `boolean` | 28/28 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |

### `$.biologicalForms[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 28/28 | Texto visible en inglés. | `"Wild boar"` |
| `es` | `string` | 28/28 | Texto visible en español. | `"Jabalí"` |

### `$.lineageRelations[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `relationType` | `string` | 12/12 | Relación histórica: domesticación, selección, origen híbrido, aporte ancestral o introgresión. | `"domestication"` |
| `parentFormIds` | `array<string>` | 12/12 | Aportes conjuntos de origen híbrido; en otras relaciones, formas ancestrales/de referencia. | `["FRM#000050"]` |
| `childFormIds` | `array<string>` | 12/12 | Formas resultantes/receptoras; nunca poblaciones generadas automáticamente. | `["FRM#000051"]` |
| `evidenceSourceKeys` | `array<string>` | 12/12 | Claves de bibliografía; vacío indica que aquí no se afirma un linaje específico. | `["pig_2015"]` |
| `supportLevel` | `string` | 12/12 | Categoría de evidencia; un representante no identifica una población fundadora exacta. | `"supported_lineage_summary"` |
| `description` | `object` | 12/12 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `—` |
| `exactAncestralPopulationResolved` | `boolean` | 12/12 | False: no se especifican poblaciones fundadoras históricas exactas. | `false` |
| `runtimeEnabled` | `boolean` | 12/12 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |

### `$.lineageRelations[].description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 12/12 | Texto visible en inglés. | `"Ancestral lineage summary; actual populations, gene flow and historical husbandry remain distinct."` |
| `es` | `string` | 12/12 | Texto visible en español. | `"Resumen de linaje ancestral; poblaciones reales, flujo génico y manejo histórico permanecen distintos."` |

### `$.excludedLineageRelations[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `parentFormId` | `string` | 2/2 | Forma ancestral de referencia en un supuesto directo descartado. | `"FRM#000073"` |
| `childFormId` | `string` | 2/2 | Forma descendiente de referencia en un supuesto directo descartado. | `"FRM#000074"` |
| `reason` | `object` | 2/2 | Explicación de la restricción de ejecución. | `—` |
| `evidenceSourceKeys` | `array<string>` | 2/2 | Claves de bibliografía; vacío indica que aquí no se afirma un linaje específico. | `["horse_2021"]` |
| `runtimeEnabled` | `boolean` | 2/2 | Indica si la aparición puede usarse en generación; actualmente false. | `false` |

### `$.excludedLineageRelations[].reason`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 2/2 | Texto visible en inglés. | `"Do not represent Przewalski horses as the direct universal ancestors of modern domestic horses."` |
| `es` | `string` | 2/2 | Texto visible en español. | `"No representar a Przewalski como ancestro directo universal del caballo doméstico moderno."` |

### `$.evidenceSources[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `sourceKey` | `string` | 28/28 | Clave bibliográfica estable local al catálogo; no es ID de entidad. | `"gbif"` |
| `title` | `string` | 28/28 | Título del documento o esquema. | `"GBIF taxonomic matching documentation"` |
| `url` | `string` | 28/28 | URL pública de la fuente. | `"https://techdocs.gbif.org/en/openapi/v1/species"` |
| `checkedOn` | `string` | 28/28 | Fecha de consulta de la referencia; no es fecha de publicación. | `"2026-10-17"` |
| `supports` | `string` | 28/28 | Alcance de la afirmación respaldada por esta entrada bibliográfica. | `"Taxon names and backbone matching; not evidence of domestication or geographic suitability."` |

### `$.reviewIssues[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 4/4 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"native_range"` |
| `resolution` | `string` | 4/4 | Interpretación documentada o siguiente acción de revisión. | `"Review each selected taxon by region and habitat before enabling world generation."` |

### `$.summary`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `taxonCount` | `integer` | 1/1 | Cantidad de identidades taxonómicas distintas del proveedor en este catálogo. | `168` |
| `biologicalFormCount` | `integer` | 1/1 | Cantidad de formas biológicas de referencia en este catálogo. | `28` |
| `lineageRelationCount` | `integer` | 1/1 | Cantidad de relaciones de linaje de referencia registradas. | `12` |
| `excludedLineageRelationCount` | `integer` | 1/1 | Cantidad de supuestos de ascendencia directa explícitamente descartados. | `2` |
| `sourceCandidateCount` | `integer` | 1/1 | Cantidad de candidatos originales de especies/grupos cubiertos. | `134` |
| `cropCandidateCount` | `integer` | 1/1 | Cantidad de grupos agrícolas cubiertos. | `0` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

```json
{
  "schemaVersion": "1.0.0",
  "contentVersion": "0.1.0",
  "kind": "biological_taxon_catalog",
  "status": "taxonomy_names_verified_representative_choices_and_ecology_pending",
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "runtimePolicy": {
    "loadAsGameDefinitions": false,
    "unknownValues": "A name match does not verify native distribution, ecology, resource outputs, domestication eligibility or historical introduction.",
    "identityPolicy": "New taxon IDs use PLT, ANM, ALG or FNG prefixes; forms use FRM. Existing candidate/resource/technology IDs remain unchanged. Never reallocate IDs by sorting.",
    "sourceInterpretation": "Broad source groups have explicit non-exhaustive representative choices. These are design selections, not unique identifications of the original source or approved spawn lists.",
    "resourceInheritance": "Candidate resource bindings do not automatically transfer to every selected taxon or form.",
    "lineagePolicy": "Relations summarize evidence, not automatic gameplay transitions. Hybrid and introgression edges are not domestication edges. An extant species may only proxy an ancestral population.",
    "varietyPolicy": "Cultivar groups are not species, botanical varieties or named cultivars. No modern named cultivars or animal breeds are invented.",
    "floraClassification": "The plants folder includes source flora, including algae and lichenized fungi. Their scientific kingdom and ALG/FNG prefixes remain explicit."
  },
  "taxa": [
    {
      "id": "ANM#000001",
      "tag": "alces_alces",
      "name": {
        "en": "Alces alces",
        "es": "Alces alces"
      },
      "scientificName": "Alces alces (Linnaeus, 1758)",
      "taxonRank": "SPECIES",
      "organismGroup": "animal",
      "taxonomy": {
        "kingdom": "Animalia",
        "family": "Cervidae",
        "genus": "Alces",
        "provider": "GBIF Backbone",
        "providerTaxonKey": "2440940",
        "taxonomicStatus": "ACCEPTED",
        "referenceUrl": "https://www.gbif.org/species/2440940",
        "matchEvidence": [
          {
            "queriedName": "Alces alces",
            "matchedScientificName": "Alces alces (Linnaeus, 1758)",
            "matchType": "EXACT",
            "matchStatus": "ACCEPTED",
            "confidence": 99,
            "requestUrl": "https://api.gbif.org/v1/species/match?name=Alces+alces&strict=true&verbose=true",
            "checkedOn": "2026-10-17"
          }
        ]
      },
      "reviewStatus": "taxon_name_matched_source_interpretation_and_ecology_pending",
      "nativeRangeReviewStatus": "not_validated_by_name_match",
      "runtimeEnabled": false
    }
  ],
  "biologicalForms": [
    {
      "id": "FRM#000050",
      "tag": "wild_boar",
      "taxonId": "ANM#000148",
      "name": {
        "en": "Wild boar",
        "es": "Jabalí"
      },
      "formKind": "wild_ancestral_proxy",
      "literatureName": "Sus scrofa",
      "evidenceSourceKeys": [
        "pig_2015"
      ],
      "status": "reference_form_not_an_instance_or_unlock",
      "runtimeEnabled": false
    }
  ],
  "lineageRelations": [
    {
      "relationType": "domestication",
      "parentFormIds": [
        "FRM#000050"
      ],
      "childFormIds": [
        "FRM#000051"
      ],
      "evidenceSourceKeys": [
        "pig_2015"
      ],
      "supportLevel": "supported_lineage_summary",
      "description": {
        "en": "Ancestral lineage summary; actual populations, gene flow and historical husbandry remain distinct.",
        "es": "Resumen de linaje ancestral; poblaciones reales, flujo génico y manejo histórico permanecen distintos."
      },
      "exactAncestralPopulationResolved": false,
      "runtimeEnabled": false
    }
  ],
  "excludedLineageRelations": [
    {
      "parentFormId": "FRM#000073",
      "childFormId": "FRM#000074",
      "reason": {
        "en": "Do not represent Przewalski horses as the direct universal ancestors of modern domestic horses.",
        "es": "No representar a Przewalski como ancestro directo universal del caballo doméstico moderno."
      },
      "evidenceSourceKeys": [
        "horse_2021"
      ],
      "runtimeEnabled": false
    }
  ],
  "evidenceSources": [
    {
      "sourceKey": "gbif",
      "title": "GBIF taxonomic matching documentation",
      "url": "https://techdocs.gbif.org/en/openapi/v1/species",
      "checkedOn": "2026-10-17",
      "supports": "Taxon names and backbone matching; not evidence of domestication or geographic suitability."
    }
  ],
  "reviewIssues": [
    {
      "id": "native_range",
      "resolution": "Review each selected taxon by region and habitat before enabling world generation."
    },
    {
      "id": "legacy_scope",
      "resolution": "The current research demo still uses wheat/maize aliases. Choose concrete taxa/forms before implementing species-specific progress migration."
    },
    {
      "id": "resource_inheritance",
      "resolution": "Review source resource outputs at species/form level, including anatomical, sex and life-stage constraints."
    },
    {
      "id": "cultivars_and_breeds",
      "resolution": "Named historical cultivars and animal breeds require dedicated evidence; current forms and barley cultivar groups do not claim to enumerate them."
    }
  ],
  "summary": {
    "taxonCount": 168,
    "biologicalFormCount": 28,
    "lineageRelationCount": 12,
    "excludedLineageRelationCount": 2,
    "sourceCandidateCount": 134,
    "cropCandidateCount": 0
  }
}
```
