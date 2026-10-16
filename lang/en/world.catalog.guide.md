# Evolve — World Catalog Design Guide

[Simple visual reference](visual-reference.md)

Complete nested JSON structures, types and examples: [JSON reference](json-structures.md).

Structured conversion of the supplied Documentacion Evolve snapshot. The original document was read for extraction and was not modified.

## Repository packaging

The original combined guide is now split across `data/world`, `data/plants`, `data/animals` and `data/minerals`. The table below documents the logical collections across those files. `catalogFiles` paths resolve relative to `data/world/world.catalog.guide.json`. World schema `1.1.0` / content `0.2.0` describes this packaging change; IDs and all 485 occurrences are preserved. Crop candidates are in the plants catalog.

## 1. Purpose and boundaries

This JSON is the guide for resolving concrete species, world-generation conditions and resource definitions. It is not yet a playable species catalog. `runtimePolicy.loadAsGameDefinitions` is false. A loader must not silently spawn candidates or interpret unknown values as unrestricted conditions.

All collections are flat; IDs connect them. Player-visible names use `{en, es}`. Technical IDs and policies remain English. `sourceText` and `sourceLabel` intentionally retain the exact Spanish source for auditability; these are provenance, not game UI.

## 2. Collections

| Field | Meaning |
| --- | --- |
| `biomes` | Seven interface biome categories. |
| `regionalVariants` | The 27 enumerated regional/habitat variants, linked by `biomeId`. |
| `speciesCandidates` | Flora/fauna entries, including groups that still require splitting. |
| `geologicalResourceCandidates` | Materials, ore forms and contextual variants from the source; refined metal is not an automatic extraction output. |
| `resourceOccurrences` | Every regional flora/fauna/mining entry with its source text, linked candidate ID and extraction stage where applicable. |
| `agriculturalCropCandidates` | The 21 crops or crop groups named in source section 5, with explicit species-resolution tasks. |
| `hexDefinitionGuide` | Proposed tile properties, with static generation data distinguished from mutable state. |
| `depositDefinitionGuide` | Deposit properties whose actual values and state still require design. |
| `generationPipeline` | Generation order transcribed into technical steps. |
| `reviewIssues` | Source discrepancies, broad taxa and integration concerns. |
| `speciesCompletionChecklist` | Work required before a candidate can become a runtime species definition. |

## 3. Identity and taxonomy

Candidate IDs are traceable design-entry IDs, not accepted scientific names. Entries with the same likely taxon but different source qualifiers remain separate until reviewed. Do not merge records merely because their English names look similar.

Scientific names are populated only when the source explicitly gives a binomial. `verified: false` means no taxonomic validation was performed. Entries such as acacias, regional fish or wild crop relatives must be split or explicitly accepted as game-level groups before implementation. A vernacular singular name is not sufficient proof of exact taxonomy.

Agricultural crop IDs such as `wheat` and `maize` are prospective bindings for species research. Their exact taxon, wild ancestor and relationship to regional wild candidates are unresolved. Do not equate domesticated maize with every teosinte population or domesticated wheat with every wild wheat candidate.

## 4. What is preserved

All 485 catalog occurrences are retained. The original document enumerates 27 regional variants although later text says 26, and a pending paragraph says ten biomes although the detailed catalog contains seven. The guide uses the enumerated entries and records the contradictions.

Three explanatory lines placed after the last alpine flora list are preserved as distribution notes, not misclassified as plant species. Mining-stage entries remain method-specific occurrences. Similar material forms are not automatically merged.

The original source document is represented by its exact connector file ID and snapshot hash. This conversion used the attached snapshot, not a claim that a live source revision was verified.

## 5. Unknown values and readiness

`null` means unresolved. It never means zero, no requirement, no native restriction or approved capability. Empty region/ancestor reference lists are unfinished mappings, not worldwide distribution.

Every occurrence has `runtimeEnabled: false`, `guaranteedPresence: false` and an unknown spawn probability. No abundance, growth rate, fertility range, domestication duration or yield was invented.

Fauna product tags only transcribe potential uses in the document. They are not confirmed yields or automatic unlocks. `antlers_or_horns` must be resolved by species; never grant both by default. Plant products remain unresolved because the regional lists do not consistently specify outputs.

## 6. World-generation rules

Elevation is independent of biome. Levels 0–2 allow ordinary land traversal subject to surface and terrain constraints; level 3 blocks ordinary land passage and conventional settlements. Sea-level land and water are different surfaces.

Static climate, water, soil and native region constrain species. Climate events, seasons and dynamic disasters are excluded from the initial game. Geological provinces determine mineral availability independently from biome labels.

Marine entries need real depth, habitat and regional constraints. Polymetallic nodules must not appear as automatically accessible shallow coastal resources. Mechanized mining remains future content outside the initial medieval scope.

Domestic or feral dromedaries are introduced-only in the source and are not native wild initial spawns. Other ambiguities, including cultivated date palms, remain flagged. Lichens retain the source's flora placement for traceability without asserting a scientific plant classification.

## 7. Connection to agriculture

The technology file is now schema `2.0.0`, content `0.3.0`: a flat `technologies` array. Technologies use stable IDs and global `order`; array adjacency does not imply a prerequisite. Species research uses `(civilizationId, technologyId, speciesId)`.

This guide does not resolve every technology import. Native presence, discovery, cultivation knowledge, domestication and actual crop production remain separate. An accessible plant is not automatically edible, cultivable or domesticable.

## 8. Completion workflow

For each candidate: select an exact species or explicit game taxon; verify scientific name and native range; identify wild/domestic relationships; define ecological and propagation conditions; specify products and recipes; connect technology requirements; validate period and regional availability; then balance and test.

Only after those reviews should approved records be promoted into an executable `species.json`/world-definition catalog. Keep stable IDs or introduce explicit aliases and save migrations when merging or splitting candidates. Do not use null-filled guide records as final simulation content.

## 9. Validation performed

Checked source occurrence coverage, translation-map coverage, unique candidate IDs, valid occurrence references, biome/variant counts and agreement with the enumerated source lists. Scientific taxonomy, geographic ranges, external resources and runtime simulation have not been validated.


## 10. Conversion summary

```json
{
  "biomeCount": 7,
  "regionalVariantCount": 27,
  "plantCandidateCount": 129,
  "animalCandidateCount": 134,
  "geologicalCandidateCount": 57,
  "sourceOccurrenceCount": 485,
  "agriculturalCropCandidateCount": 21
}
```
