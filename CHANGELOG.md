# Change log

## 2026-10-17 — Detailed fox resource choice

- Record user-selected option C for foxes: hide, meat, bones and animal fat. Allocate RES#000105 for bones; no changes to other animal outputs.
- Animal content becomes 0.5.0; resource content 0.3.0 (105 resources, 301 source bindings, 24 animal source tags). Structural versions remain unchanged.
- Acquisition workflow is the next open decision; quantities, timing, technology requirements and processing uses remain unresolved. Runtime stays disabled.
- Update bilingual references, diagrams and roadmap; remove the obsolete hide-only restriction from category validation.
- Elección confirmada: zorros con piel, carne, huesos y grasa; registrar el avance sin dar por terminada la forma de obtención ni el resto de animales.

## 2026-10-17 — Shared roadmap and task tracking

- Add English/Spanish roadmaps with one current focus, next design work, later simulation, deferred ideas and completed foundations.
- Link both versions from the project entrypoints and record the agreement to update them with each completed task, new pending item or changed decision.
- Track partial design separately from completed gameplay; no data or simulation behavior changes.
- Se añade una lista compartida de pendientes y avances para retomar el proyecto sin perder el enfoque.

## 2026-10-17 — General gameplay entity categories

- Follow the simpler entity scope: foxes provide hide without separate Arctic/corsac/fennec gameplay species. Group 18 animal cases and 15 plant cases only where existing output profiles match. Retain meaningful crop and wild/domestic distinctions.
- Preserve all 485 occurrence IDs, habitats and source text; remap current definition IDs and retain sourceDefinitionId plus 86 explicit retired-ID aliases. No previous IDs are reused.
- Current guides contain 109 plant and 101 animal entities, plus unchanged 21 crop groups. Deduplicate source bindings from 365 to 298 for the same 104 resources; do not add yields or processing requirements.
- General guide schema/content: 1.3.0/0.4.0; world 1.4.0/0.5.0; resources content 0.2.0. Scientific catalogs remain optional background (1.1.0/0.2.0), not gameplay subdivisions or unlock requirements.
- Refresh bilingual documentation, complete JSON examples, category diagrams and alias/provenance checks. Technology definitions and research example remain unchanged.
- Se simplifican casos equivalentes como zorros, osos, robles y pinos. Se conservan hábitats, recursos y procedencia; la clasificación científica queda como referencia opcional.

## 2026-10-17 — Biological identities and reference lineages

- Added 367 provider-matched taxon records, 77 biological reference forms, 25 documented lineage summaries and two explicitly excluded direct ancestry assumptions.
- Linked all 129 flora candidates, 134 fauna candidates and 21 crop groups to concrete taxon selections. Broad-group choices are representative and non-exhaustive; name matching does not validate original interpretation, native ranges, habitats or outputs.
- Added stable PLT/ANM/ALG/FNG/FRM allocations while retaining legacy candidate IDs, all 485 source occurrences and all resource/technology definitions. No implicit resource inheritance.
- Added bilingual complete mappings, biological reference diagrams, field-by-field JSON documentation, a nested structural schema and offline consistency checks.
- Plant/animal guide schema/content is 1.2.0/0.3.0; biological catalogs 1.0.0/0.1.0; world manifest 1.3.0/0.4.0. Runtime remains disabled; no quantities, durations, yields, balance or simulation behavior changes.
- Añadidos taxones y formas con evidencia, referencias bilingües y comprobaciones. Las selecciones representativas, distribución nativa y relaciones todavía no documentadas requieren revisión; no se afirma un árbol evolutivo completo.

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
