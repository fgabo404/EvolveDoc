# `data/plants/plants.biological.catalog.json`

[Source JSON](../../../data/plants/plants.biological.catalog.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"1.1.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.2.0"` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"biological_taxon_catalog"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"optional_scientific_background_not_gameplay_entity_catalog"` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `runtimePolicy` | `object` | 1/1 | Rules and restrictions for interpreting this guide. | `—` |
| `taxa` | `array<object>` | 1/1 | Flat accepted taxon records; provider-specific species, subspecies or botanical varieties. | `—` |
| `biologicalForms` | `array<object>` | 1/1 | Flat reference populations, domesticated forms and cultivar groups; not live instances. | `—` |
| `lineageRelations` | `array<object>` | 1/1 | Evidence-backed historical ancestry/selection summaries; not executable game recipes. | `—` |
| `excludedLineageRelations` | `array<?>` | 1/1 | Explicit cautions against unsupported direct ancestor assumptions. | `[]` |
| `evidenceSources` | `array<object>` | 1/1 | Bibliography supporting selected lineage claims and taxonomic rules. | `—` |
| `reviewIssues` | `array<object>` | 1/1 | Recorded source discrepancies and unresolved design questions. | `—` |
| `summary` | `object` | 1/1 | Counts used to check catalog completeness. | `—` |

### `$.runtimePolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `loadAsGameDefinitions` | `boolean` | 1/1 | False blocks promotion of this guide to playable definitions. | `false` |
| `unknownValues` | `string` | 1/1 | Explains that unresolved null values are not zero or unrestricted. | `"A name match does not verify native distribution, ecology, resource outputs, domestication eligibility or histo…` |
| `identityPolicy` | `string` | 1/1 | Localized text must not be used as identity or dependency. | `"New taxon IDs use PLT, ANM, ALG or FNG prefixes; forms use FRM. Existing candidate/resource/technology IDs rema…` |
| `sourceInterpretation` | `string` | 1/1 | Boundary between representative design choices and uniquely identified source records. | `"Broad source groups have explicit non-exhaustive representative choices. These are design selections, not uniqu…` |
| `resourceInheritance` | `string` | 1/1 | Policy blocking automatic transfer of broad-group resource links to species/forms. | `"Candidate resource bindings do not automatically transfer to every selected taxon or form."` |
| `lineagePolicy` | `string` | 1/1 | Evidence-based ancestry is separate from automatic gameplay transformations. | `"Relations summarize evidence, not automatic gameplay transitions. Hybrid and introgression edges are not domest…` |
| `varietyPolicy` | `string` | 1/1 | Distinguishes species, reference forms, cultivar groups and named breeds/cultivars. | `"Cultivar groups are not species, botanical varieties or named cultivars. No modern named cultivars or animal br…` |
| `floraClassification` | `string` | 1/1 | Explains that the flora folder includes algae and lichenized fungi with explicit classification. | `"The plants folder includes source flora, including algae and lichenized fungi. Their scientific kingdom and ALG…` |
| `gameplayIdentity` | `string` | 1/1 | Scientific catalog is optional background; gameplay identities come from general entity guides. | `"Gameplay identity is defined by the general plant/animal guide. Scientific names are optional background and ne…` |

### `$.taxa[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 199/199 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"PLT#000001"` |
| `tag` | `string` | 199/199 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"acacia_acuminata"` |
| `name` | `object` | 199/199 | Player-visible label using language keys. | `—` |
| `scientificName` | `string` | 199/199 | Scientific name in the source or accepted provider record; null in a legacy source means unresolved there. | `"Acacia acuminata Benth."` |
| `taxonRank` | `string` | 199/199 | Provider rank: species, subspecies or variety; a form is a separate entity. | `"SPECIES"` |
| `organismGroup` | `string` | 199/199 | Explicit animal, plant, alga or lichenized fungus classification. | `"plant"` |
| `taxonomy` | `object` | 199/199 | Scientific identity, evidence and review information. | `—` |
| `reviewStatus` | `string` | 199/199 | Review still required before a source output is authorized. | `"taxon_name_matched_source_interpretation_and_ecology_pending"` |
| `nativeRangeReviewStatus` | `string` | 199/199 | Name validation does not validate native distribution. | `"not_validated_by_name_match"` |
| `runtimeEnabled` | `boolean` | 199/199 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.taxa[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 199/199 | English visible text. | `"Acacia acuminata"` |
| `es` | `string` | 199/199 | Spanish visible text. | `"Acacia acuminata"` |

### `$.taxa[].taxonomy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `kingdom` | `string` | 199/199 | Biological kingdom reported by the named taxonomy provider. | `"Plantae"` |
| `family` | `string` | 199/199 | Family reported by the taxonomy provider; null if unavailable. | `"Fabaceae"` |
| `genus` | `string` | 199/199 | Genus reported by the taxonomy provider. | `"Acacia"` |
| `provider` | `string` | 199/199 | Taxonomic authority dataset used for this snapshot. | `"GBIF Backbone"` |
| `providerTaxonKey` | `string` | 199/199 | Provider-specific accepted taxon key stored as string; not an Evolve ID. | `"2979180"` |
| `taxonomicStatus` | `string` | 199/199 | Accepted status of the stored taxon under the stated provider. | `"ACCEPTED"` |
| `referenceUrl` | `string` | 199/199 | Public provider record for the accepted taxon. | `"https://www.gbif.org/species/2979180"` |
| `matchEvidence` | `array<object>` | 199/199 | Scientific-name lookup evidence; does not identify an ambiguous original common name. | `—` |

### `$.taxa[].taxonomy.matchEvidence[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `queriedName` | `string` | 200/200 | Scientific name submitted to the taxonomic service. | `"Acacia acuminata"` |
| `matchedScientificName` | `string` | 200/200 | Name matched before synonym resolution; accepted identity is stored separately. | `"Acacia acuminata Benth."` |
| `matchType` | `string` | 200/200 | Exact/fuzzy/higher-rank result; this reference accepts only EXACT. | `"EXACT"` |
| `matchStatus` | `string` | 200/200 | Matched query status, which may be SYNONYM even when the stored taxon is ACCEPTED. | `"ACCEPTED"` |
| `confidence` | `integer` | 200/200 | Provider match score, not a percentage certainty of the original source interpretation. | `99` |
| `requestUrl` | `string` | 200/200 | Reproducible taxonomy query URL; results can change with provider updates. | `"https://api.gbif.org/v1/species/match?name=Acacia+acuminata&strict=true&verbose=true"` |
| `checkedOn` | `string` | 200/200 | Date of the consulted reference snapshot; not publication date. | `"2026-10-17"` |

### `$.biologicalForms[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 49/49 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"FRM#000001"` |
| `tag` | `string` | 49/49 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"cultivated_triticum_monococcum_subsp_monococcum"` |
| `taxonId` | `string` | 49/49 | Reference to the taxon underlying this biological form. | `"PLT#000173"` |
| `name` | `object` | 49/49 | Player-visible label using language keys. | `—` |
| `formKind` | `string` | 49/49 | Reference form category; does not imply a new species, breed or unlocked capability. | `"cultivated_population"` |
| `literatureName` | `string` | 49/49 | Scientific or historical label used for the reference form; may differ from accepted provider naming. | `"Triticum monococcum subsp. monococcum"` |
| `evidenceSourceKeys` | `array<string>` | 49/49 | Keys into this catalog bibliography; empty means no specific lineage claim is asserted here. | `[]` |
| `status` | `string` | 49/49 | Maturity, review state or current example research status; read the containing object. | `"reference_form_not_an_instance_or_unlock"` |
| `runtimeEnabled` | `boolean` | 49/49 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.biologicalForms[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 49/49 | English visible text. | `"Cultivated form: Triticum monococcum subsp. monococcum"` |
| `es` | `string` | 49/49 | Spanish visible text. | `"Forma cultivada: Triticum monococcum subsp. monococcum"` |

### `$.lineageRelations[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `relationType` | `string` | 13/13 | Historical relation: domestication, selection, hybrid origin, ancestral contribution or introgression. | `"domestication"` |
| `parentFormIds` | `array<string>` | 13/13 | Joint ancestral inputs for a hybrid origin; otherwise contributing/reference ancestor forms. | `["FRM#000036"]` |
| `childFormIds` | `array<string>` | 13/13 | Resulting/receiving reference forms, never automatically generated populations. | `["FRM#000001"]` |
| `evidenceSourceKeys` | `array<string>` | 13/13 | Keys into this catalog bibliography; empty means no specific lineage claim is asserted here. | `["einkorn_2023"]` |
| `supportLevel` | `string` | 13/13 | Evidence summary strength/category; a proxy does not identify an exact founding population. | `"supported_lineage_summary"` |
| `description` | `object` | 13/13 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `exactAncestralPopulationResolved` | `boolean` | 13/13 | False: exact historical founding populations are not specified. | `false` |
| `runtimeEnabled` | `boolean` | 13/13 | Whether this occurrence may be used by generation; currently false. | `false` |

### `$.lineageRelations[].description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 13/13 | English visible text. | `"Einkorn branch; not the only wild wheat lineage."` |
| `es` | `string` | 13/13 | Spanish visible text. | `"Rama de escanda menor; no es el único linaje de trigo silvestre."` |

### `$.evidenceSources[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `sourceKey` | `string` | 28/28 | Stable bibliography key local to a biological catalog, not an entity ID. | `"gbif"` |
| `title` | `string` | 28/28 | Document or schema title. | `"GBIF taxonomic matching documentation"` |
| `url` | `string` | 28/28 | Public source URL. | `"https://techdocs.gbif.org/en/openapi/v1/species"` |
| `checkedOn` | `string` | 28/28 | Date of the consulted reference snapshot; not publication date. | `"2026-10-17"` |
| `supports` | `string` | 28/28 | Scope of the claim supported by this bibliography entry. | `"Taxon names and backbone matching; not evidence of domestication or geographic suitability."` |

### `$.reviewIssues[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 4/4 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"native_range"` |
| `resolution` | `string` | 4/4 | Documented interpretation or next review action. | `"Review each selected taxon by region and habitat before enabling world generation."` |

### `$.summary`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `taxonCount` | `integer` | 1/1 | Number of distinct provider taxon identities in this catalog. | `199` |
| `biologicalFormCount` | `integer` | 1/1 | Number of biological reference forms in this catalog. | `49` |
| `lineageRelationCount` | `integer` | 1/1 | Number of accepted reference lineage relations. | `13` |
| `excludedLineageRelationCount` | `integer` | 1/1 | Number of explicitly excluded direct ancestry assumptions. | `0` |
| `sourceCandidateCount` | `integer` | 1/1 | Number of current gameplay candidates with optional scientific cross-references. | `109` |
| `cropCandidateCount` | `integer` | 1/1 | Number of covered crop group candidates. | `21` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "1.1.0",
  "contentVersion": "0.2.0",
  "kind": "biological_taxon_catalog",
  "status": "optional_scientific_background_not_gameplay_entity_catalog",
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
    "floraClassification": "The plants folder includes source flora, including algae and lichenized fungi. Their scientific kingdom and ALG/FNG prefixes remain explicit.",
    "gameplayIdentity": "Gameplay identity is defined by the general plant/animal guide. Scientific names are optional background and never mandatory unlock requirements."
  },
  "taxa": [
    {
      "id": "PLT#000001",
      "tag": "acacia_acuminata",
      "name": {
        "en": "Acacia acuminata",
        "es": "Acacia acuminata"
      },
      "scientificName": "Acacia acuminata Benth.",
      "taxonRank": "SPECIES",
      "organismGroup": "plant",
      "taxonomy": {
        "kingdom": "Plantae",
        "family": "Fabaceae",
        "genus": "Acacia",
        "provider": "GBIF Backbone",
        "providerTaxonKey": "2979180",
        "taxonomicStatus": "ACCEPTED",
        "referenceUrl": "https://www.gbif.org/species/2979180",
        "matchEvidence": [
          {
            "queriedName": "Acacia acuminata",
            "matchedScientificName": "Acacia acuminata Benth.",
            "matchType": "EXACT",
            "matchStatus": "ACCEPTED",
            "confidence": 99,
            "requestUrl": "https://api.gbif.org/v1/species/match?name=Acacia+acuminata&strict=true&verbose=true",
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
      "id": "FRM#000001",
      "tag": "cultivated_triticum_monococcum_subsp_monococcum",
      "taxonId": "PLT#000173",
      "name": {
        "en": "Cultivated form: Triticum monococcum subsp. monococcum",
        "es": "Forma cultivada: Triticum monococcum subsp. monococcum"
      },
      "formKind": "cultivated_population",
      "literatureName": "Triticum monococcum subsp. monococcum",
      "evidenceSourceKeys": [],
      "status": "reference_form_not_an_instance_or_unlock",
      "runtimeEnabled": false
    }
  ],
  "lineageRelations": [
    {
      "relationType": "domestication",
      "parentFormIds": [
        "FRM#000036"
      ],
      "childFormIds": [
        "FRM#000001"
      ],
      "evidenceSourceKeys": [
        "einkorn_2023"
      ],
      "supportLevel": "supported_lineage_summary",
      "description": {
        "en": "Einkorn branch; not the only wild wheat lineage.",
        "es": "Rama de escanda menor; no es el único linaje de trigo silvestre."
      },
      "exactAncestralPopulationResolved": false,
      "runtimeEnabled": false
    }
  ],
  "excludedLineageRelations": [],
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
    "taxonCount": 199,
    "biologicalFormCount": 49,
    "lineageRelationCount": 13,
    "excludedLineageRelationCount": 0,
    "sourceCandidateCount": 109,
    "cropCandidateCount": 21
  }
}
```
