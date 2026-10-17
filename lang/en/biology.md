# Plants, animals and biological forms

[Plants: complete catalog, mappings and branches](../../data/plants/BIOLOGY.md) · [Animals: complete catalog, mappings and branches](../../data/animals/BIOLOGY.md)

This design specifies biological identities without fixing quantities, durations, probabilities, yields or simulation formulas. Collections remain flat and reference each other by ID.

## What each object represents

| Collection | Meaning | Example |
| --- | --- | --- |
| `speciesCandidates` | Original source label, provenance and existing regional occurrences; may describe a group. | Oaks, wild wheat, wild boar. |
| `taxa` | Accepted scientific identity under an explicit provider, with rank and match evidence. | `Quercus robur`, `Sus scrofa`. |
| `biologicalForms` | Cultivated/domestic form, ancestral reference population or cultivar group; not an individual or game population. | Wild and domestic rabbits can share a taxon. |
| `lineageRelations` | Historical relation between forms, distinguishing domestication, selection, hybrid origin, ancestral contribution and introgression. | Two ancestral contributions to bread wheat. |
| `excludedLineageRelations` | Direct assumption that must not be introduced as fact. | Przewalski horse → modern domestic horse. |
| `evidenceSources` | Relationship bibliography referenced by `sourceKey`. | A domestication genomics study. |

`taxonResolution` links every candidate to selected `taxonIds` and related `formIds`. These forms are associated references, not instructions to initially spawn domestic animals wherever a wild relative was listed. `selectionMode` distinguishes specific interpretations from non-exhaustive representative choices. Legacy IDs are neither deleted nor silently replaced.

Crop groups also select concrete taxa. Wheat includes einkorn, emmer, durum and bread wheat; Asian and African rice remain separate. A cultivated reference form establishes design identity without asserting that ancestral domestication has already been reviewed.

## Permanent identities

- `PLT`: plant taxon; `ANM`: animal taxon; `ALG`: alga; `FNG`: fungus, including lichenized fungi.
- `FRM`: biological form, cultivar group or reference population.
- Each prefix has an independent six-digit sequence. Forms in both folders share one FRM sequence. These JSON files are the allocation registry: preserve IDs when expanding the catalog; never recalculate them by sorting names.
- `VAR` still means a world regional variant. A botanical variety is a taxon ranked `VARIETY`; a cultivar group uses `FRM` with `formKind: "cultivar_group"`. These are different concepts.

The plants folder retains source flora, including algae and lichens. Explicit `organismGroup`, kingdom and prefixes prevent treating a lichen as a botanical plant. Latin labels are identical in `name.en` and `name.es`; original bilingual common names remain in candidates. Specific translations are not invented for ambiguous common names.

## Reading ancestry

The wheat branch separates einkorn/emmer domestication, durum selection and bread wheat hybrid origin. A `hybrid_origin` jointly requires all `parentFormIds`: these are not alternatives or executable breeding recipes. Two-row and six-row barley are selected cultivar groups, not new species or named modern cultivars.

Maize separates domestication from Balsas teosinte and later gene flow from Mexican highland teosinte. Introgression is not interpreted as a second domestication. Aurochs ancestry branches toward taurine and indicine lineages; zebu is not an upgrade of taurine cattle. Living wild taxa may proxy ancestral complexes without identifying exact founding populations.

No relation is added merely because species share a genus or look similar. Unknown ancestors, breeds and historical cultivars without evidence remain unresolved. The catalog records 25 relationship summaries, not a complete evolutionary tree of every organism.

## Evidence and boundaries

Selected scientific names were matched through GBIF: `EXACT`, provider score at least 95, and species/subspecies/variety rank; synonyms resolve to accepted taxa. The score is not certainty that an original source label denotes that species. Every record stores provider, key, URL, query and date. Camelus ferus uses the explicitly named GBIF Catalogue of Life XR dataset; taxonomic treatments can differ across authorities.

This validates name matching, not the entire source interpretation. Every representative selection still requires native-range, habitat, historical-introduction and output review. All 485 original occurrences retain source provenance; they are not multiplied into automatic spawns of every selected species.

`inheritResourceBindings: false` blocks automatic inheritance of broad-group outputs. Wood remains a resource, not a species. Making a concrete form a source of milk, fiber or seed requires its own reviewed bindings, including anatomy, sex and life stage where relevant. Resource transformation chains remain in their own catalog.

Cultivated references without documented ancestry relations await review; they do not lack ancestors. Individual historical cultivars and animal breeds are not yet enumerated. Forms and relations remain non-executable: `loadAsGameDefinitions` and `runtimeEnabled` stay `false`.

## Structure, examples and checks

Complete contracts, nested objects and examples:

- [Plant JSON](json/data--plants--plants.biological.catalog.md).
- [Animal JSON](json/data--animals--animals.biological.catalog.md).
- [Biological schema](json/schemas--biological.catalog.schema.md).
- [Plant candidate JSON](json/data--plants--plants.catalog.guide.md).
- [Animal candidate JSON](json/data--animals--animals.catalog.guide.md).

The structural schema covers every current object. The custom checker verifies IDs, references, stored name-match evidence, runtime boundaries, bibliography, coverage and ancestry/selection acyclicity. It neither calls live services nor independently proves scientific hypotheses. General JSON Schema engine integration remains separate.

```sh
python tools/generate_json_reference.py
python tools/generate_biology_reference.py
python tools/generate_catalog_diagrams.py
python tools/validate_repository.py
```

The research demonstration retains its legacy wheat/maize aliases. Before implementing final species-specific progress, choose concrete taxon/form identities and design migration. This change does not modify game saves or production quantities.
