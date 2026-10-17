# Change log

## 2026-10-16 — Documentation repository migration

- Made Git the primary documentation reference and organized English/Spanish Markdown under `lang`.
- Preserved agriculture schema 2.0.0/content 0.3.0 and all 23 technology definitions without gameplay changes.
- Split the source world guide into world, plant, animal and mineral catalogs; world schema 1.1.0/content 0.2.0 records the packaging change. Preserve all IDs, 485 occurrences and source provenance.
- Documented three-letter ID prefixes and a future migration plan; no existing ID has been renamed.
- Added preliminary envelope schemas, reference checks and a small species-specific research demonstration.
- Candidate taxonomy, ecology, yields, evolutionary relationships and numerical balance remain unresolved. This is not a completed game engine.

## 2026-10-16 — Complete JSON structure references

- Added English and Spanish field-by-field references for all 11 source JSON files, including nested objects, union variants, observed types, meanings and valid JSON examples.
- Included all configured condition types and eureka event examples, as well as proposed tile/deposit field names with unresolved types clearly marked.
- Linked references from catalog READMEs and conceptual documentation. Added a reproducible generator and stale-reference checks.
- No game definitions, IDs, costs, schemas or simulation behavior changed. References describe observed fields; they do not infer requiredness or invent structures for unresolved null values.

## 2026-10-16 — Simple visual references

- Added three compact Mermaid diagrams in English and Spanish: an illustrative plant/resource/technology example, existing world catalog references, and research definitions versus per-game progress.
- Linked diagrams from the main README, language entrypoints, world/agriculture documentation and JSON reference indexes.
- Diagrams are manual summaries; conceptual crop outputs are explicitly illustrative and no data definitions or simulation behavior changed.

## 2026-10-16 — Complete per-catalog reference diagrams

- Added dedicated DIAGRAMS.md / DIAGRAMS.es.md files beside every data catalog and bilingual indexes.
- Covered all 23 technologies with exact all/any prerequisite logic, scope, research/usage parameters and eurekas.
- Included every plant, animal, geological and crop candidate, plus every regional source occurrence in supporting tables. World diagrams include all biome variants and source counts.
- Kept resources explicitly pending and did not invent species evolution, products or processing chains.
- Added a reproducible diagram generator and stale-documentation checks; no JSON definitions or simulation behavior changed.

## 2026-10-17 — Initial linked resource catalog

- Added 104 bilingual material definitions with permanent RES IDs, 365 source bindings, 23 classified animal source tags and 25 proposed transformation endpoint guides.
- Linked every crop candidate and geological candidate, selected wild plants/trees, and unambiguous existing animal product tags. Preserved source tags, existing candidate IDs and all 485 regional source occurrences.
- Kept animal services and antlers-or-horns ambiguity outside inventory grants. Added requiresProcessing for processed source relations. No automatic refined-metal extraction, quantities, recipes or production unlocks.
- Added a complete resource structural schema, bilingual field reference, conceptual examples, full diagrams and domain reference checks.
- Versions: resources schema/content 1.0.0/0.1.0; plants/animals/minerals 1.1.0/0.2.0; world 1.2.0/0.3.0. Agriculture and simulation behavior are unchanged.
- Runtime remains disabled pending exact species, acquisition conditions, units, storage rules and scientific/balance review. Material provenance and seed viability must be preserved in future inventory lots.
