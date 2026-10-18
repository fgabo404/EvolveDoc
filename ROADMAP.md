# Evolve — Roadmap

[Español](ROADMAP.es.md) · [Project home](README.md)

Last updated: 2026-10-17 (America/Guatemala).

This is the shared list of current work, pending work and completed milestones. Read it when resuming the project. It applies to people and development tools alike. Detailed contracts stay in their existing documents; completed change history stays in [CHANGELOG.md](CHANGELOG.md).

## Now — Current focus

- [ ] Complete **entity → resource → acquisition method** for plants and animals. Review existing links and fill gaps. Distinguish gathering, felling, hunting, shearing and milking, including whether the source survives. Do not assign quantities, durations or regeneration yet.

References: [entity categories](lang/en/biology.md), [plants](data/plants/DIAGRAMS.md), [animals](data/animals/DIAGRAMS.md), [resources](lang/en/resources.md).

## Next — Finish the initial design

- [ ] Define useful wild/domestic relationships at gameplay category level. Preserve relevant crop differences; scientific species and exhaustive varieties are not required.
- [ ] Complete material transformation chains and acquisition requirements, including mineral extraction versus refining. The 25 current process guides are endpoints, not finished recipes.
- [ ] Define the necessary tools, containers, recipes and facilities and link them to resources and technologies. Existing external references are not completed catalogs.
- [ ] Review regional habitats and initial presence rules for entities. Keep wild presence, introduced animals and established crops distinct; no world emulation yet.
- [ ] Review cross-catalog IDs, missing references and documentation after those design decisions.

## Later — Simulation and operational rules

- [ ] Define quantities, units, durations, regeneration, consumption and numerical balance after the initial entity/resource design.
- [ ] Complete GameState, turn phases, save/load and compatibility rules.
- [ ] Implement technology conditions, eurekas, effects and species/entity-specific progress; the current research demo is only an example.
- [ ] Emulate a small initial world without graphics, with reproducible scenarios to check generation and resource evolution.
- [ ] Choose the implementation language and engine approach when simulation requirements are clear.

## Deferred ideas — Keep visible, outside the current focus

- [ ] Graphics, map rendering and user interface, after the simulation base.
- [ ] Dynamic weather, seasons and climate disasters; possible later expansion. Static habitat conditions remain part of world design.
- [ ] Nomadic populations, migration and their diplomacy/trade behavior; detailed rules remain pending.
- [ ] Broader city, economy, diplomacy and warfare systems; retain the historical simulation direction with a 4X format.

## Completed — Foundations, not final gameplay

- [x] Establish GitHub as the main reference and organize bilingual documentation.
- [x] Separate read-only GameDefinitions from per-game GameState conceptually.
- [x] Document 23 flat agriculture technologies with bilingual visible text, requirements and eurekas; implementation and balance remain pending.
- [x] Extract the initial world guide: 7 biomes, 27 regional variants and 485 preserved source occurrences.
- [x] Create initial plant, animal, crop, mineral and resource guides; these are design references, not runtime-ready catalogs.
- [x] Generalize 33 selected plant/animal cases with 86 retired-ID aliases; keep meaningful gameplay distinctions. Current guides contain 109 plant entities, 101 animal entities and 21 crop groups.
- [x] Define 104 initial resources, 298 current source links and 25 transformation endpoint guides. Full acquisition/processing rules remain pending.
- [x] Add complete current JSON field references, examples, catalog diagrams and consistency checks.
- [x] Add a small research-progress demonstration without graphics; no full simulation engine is implemented.
- [x] Create this shared roadmap and link both language versions from the README.

## Maintenance agreement

1. Read this list before continuing work; keep one current focus unless the user explicitly changes it.
2. Update both roadmap languages in the same change whenever work is completed, a decision changes or a pending item is added.
3. Mark a task complete only when its stated scope is finished. Record partial progress and remaining gaps explicitly.
4. Put new ideas under Next, Later or Deferred instead of silently replacing the current task. User instructions can change priorities.
5. Keep useful detail in the relevant documentation and completed implementation history in the changelog. No separate tracker is required.
