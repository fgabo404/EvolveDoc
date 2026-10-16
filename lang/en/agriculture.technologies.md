# Evolve — Agriculture Technology Configuration

[Simple visual reference](visual-reference.md)

Complete nested JSON structures, types and examples: [JSON reference](json-structures.md).

Technical reference for `agriculture.technologies.json`.

- Configuration schema version: `2.0.0`.
- Agriculture content version: `0.3.0`.
- Status: prototype; all numerical balance is provisional.
- Scope: definition data only. No game engine, save-game implementation, formal JSON Schema, graphics or UI is included.

## 1. Start here: the architecture

There are two categories of data and one system that executes their rules:

| Component | Responsibility | Changes during a turn? |
| --- | --- | --- |
| `GameDefinitions` | Technologies, conditions, costs, events and possible capabilities. | No. Treat a loaded ruleset as read-only. |
| `GameState` | Civilization progress, inventory, species discoveries, farms and current turn. | Yes. |
| `SimulationEngine` | Validates commands, evaluates conditions, processes events and updates state. | Executes the turn. |

This JSON belongs to `GameDefinitions`. Its structure may be shared by every civilization. Each civilization has separate research instances in `GameState`.

Example: the definition says species cultivation costs 100 research points. A civilization has earned 30 points for wheat. The engine adds that turn's research output to its wheat instance. Neither the definition nor another civilization's progress changes.

The names and fields in this file form an Evolve-specific configuration contract. They are not a universal game-engine standard. Merely loading JSON does not implement its rules.

## 2. Flat technology catalog

All 23 definitions are peers in the root `technologies` array. There are no `branches` or `nodes` containers. Root `id`, `name` and `description` identify the agriculture catalog.

`order` is a global display position from 1 to 23. Array position and order do not create prerequisites. Irrigation, drainage and ploughing can still develop in parallel according to explicit dependencies. Stable technology IDs and species-specific research identities are unchanged.

## 3. Top-level fields

| Field | Meaning |
| --- | --- |
| `schemaVersion` | Version of this configuration's structural contract. It does not imply a separate JSON Schema file already exists. |
| `contentVersion` | Version of the agriculture definitions and balance. |
| `kind` | Identifies this document as `technology_definitions`. |
| `status` | Current maturity: `prototype`. |
| `defaultLanguage` | Fallback language: `en`. |
| `supportedLanguages` | Available languages: `en`, `es`. |
| `localization` | Visible-field format, fallback and future catalog extraction rules. |
| `balance` | Provisional numeric assumptions. |
| `runtimeContract` | Rules the future runtime must implement. Several are explanatory strings, not executable expressions. |
| `externalReferences` | Imports that other catalogs must provide. |
| `manufacturingAlternatives` | Relationships between container techniques, material tags and outputs. Not complete manufacturing recipes. |
| `id`, `name`, `description` | Catalog identity and localized visible labels. |
| `technologies` | Flat list of peer technology definitions. |
| `speciesGroupBindings` | Associates crop-use tags with the species-cultivation technology. |
| `scopeExamples` | Illustrative instance bindings for wheat and maize. Not species definitions or saved progress. |
| `designNotes` | Non-executable design explanations. |
| `requiredRuntimeHandlers` | Inventory of condition, event and effect handlers required by the configuration. |

## 4. Anatomy of a technology

| Field | Meaning |
| --- | --- |
| `id` | Stable, unique identifier, such as `species_cultivation`. References use this field, never `name`. |
| `order` | Global display order; does not imply a dependency on earlier entries. |
| `name` | Localized player-visible name: `{ "en": "...", "es": "..." }`. |
| `description` | Localized player-visible description with `en` and `es`. |
| `scope` | `civilization` or `species`. |
| `prerequisites` | Technologies that must be completed. |
| `research` | Acquisition mode, research cost and start/continuation conditions. |
| `usageConditions` | Conditions required at the actual site/action to use the unlocked capability. |
| `eurekas` | Event-driven research boosts. Empty array means no boost. |
| `effects` | Capabilities unlocked on completion. |
| `designNotes` | Clarifications for designers and programmers. |

### Actual example: initial capability

```json
{
  "id": "basic_foraging",
  "level": 1,
  "name": {
    "en": "Basic Foraging",
    "es": "Recolección básica"
  },
  "description": {
    "en": "Gather food from accessible edible wild plants.",
    "es": "Recoge alimentos de plantas silvestres comestibles accesibles."
  },
  "scope": "civilization",
  "prerequisites": {
    "all": []
  },
  "research": {
    "mode": "initial_grant",
    "cost": 0,
    "pointUnit": "research_point",
    "startConditions": {
      "all": []
    },
    "ongoingConditions": {
      "all": []
    },
    "onConditionFailure": "pause_keep_progress"
  },
  "usageConditions": {
    "all": [
      {
        "type": "workers_assigned",
        "minimumCount": 1
      },
      {
        "type": "accessible_edible_plants"
      }
    ]
  },
  "eurekas": [],
  "effects": [
    {
      "type": "unlock_capability",
      "capabilityId": "basic_foraging",
      "scope": "civilization",
      "activation": "while_usage_conditions_met"
    }
  ],
  "designNotes": []
}
```

`basic_foraging` has no technology prerequisite. It is granted during civilization initialization using `initial_grant`, with cost zero. It is not research that must spend a turn in a queue.

Its use still requires assigned workers and edible plants. Having no technology prerequisite never means food appears without resources.

The engine must register the initial completion and its capability once. Initialization must not rerun on save loading as a second grant.

## 5. Conditions: `all`, `any` and typed leaves

- `{ "all": [...] }`: every child must be satisfied.
- `{ "any": [...] }`: at least one child must be satisfied.
- `{ "all": [] }`: no condition; evaluates to true.
- `{ "any": [] }`: invalid; reject the configuration.
- A typed leaf asks a runtime handler a concrete question.

Do not store `"None"` as a technology reference. The UI may display “None” for an empty `all`, but the engine evaluates the expression.

### Example: alternative container technologies

```json
{
  "any": [
    {
      "type": "technology_completed",
      "technologyId": "basketry",
      "scope": "civilization"
    },
    {
      "type": "technology_completed",
      "technologyId": "woodworking",
      "scope": "civilization"
    },
    {
      "type": "technology_completed",
      "technologyId": "pottery",
      "scope": "civilization"
    }
  ]
}
```

Basketry, woodworking or pottery can satisfy this prerequisite. All three are not required.

### Three moments of evaluation

| Field | Evaluation context | When |
| --- | --- | --- |
| `prerequisites` | Civilization and optional research species. | Starting research and admitting deferred boosts. |
| `research.startConditions` | Civilization and optional research species. | Starting research. |
| `research.ongoingConditions` | Active research instance. | Each research update. |
| `usageConditions` | Civilization plus actual action/site/species. | Attempting or continuing the relevant action. |

All current `ongoingConditions` are empty. Therefore losing a research specimen after starting does not currently pause research. This is the actual configuration, not a hidden assumption that every start condition is checked again each turn.

If future ongoing conditions fail, `pause_keep_progress` preserves progress. Losing usage resources never deletes completed knowledge.

## 6. General knowledge versus species knowledge

`civilization` scope creates one research instance per civilization, with `speciesId: null`. Examples: `initial_sowing`, `gathering_tools` and `channel_irrigation`.

`species` scope creates one instance per civilization and species. Examples: `plant_knowledge`, `species_cultivation` and `initial_selection`.

The research identity is the tuple:

`(civilizationId, technologyId, speciesId)`

Use a tuple or nested dictionaries internally instead of an unescaped concatenated string.

### Species example

```json
{
  "technologyId": "species_cultivation",
  "speciesId": "wheat"
}
```

```json
{
  "technologyId": "species_cultivation",
  "speciesId": "maize"
}
```

These refer to one shared definition but two independent progress records. Completing wheat cultivation does not complete maize cultivation.

`$speciesId` is a placeholder resolved from the current instance. It is never the literal name of a species to store in a save.

Prerequisite scope has a separate meaning from technology scope:

| Prerequisite scope | Meaning |
| --- | --- |
| `civilization` | Check the shared civilization technology. |
| `current_species` | Check the prerequisite for this same species. |
| `any_species` | At least one species instance of that prerequisite is complete. |

For `species_cultivation`, the civilization must know `initial_sowing` and must know `seed_handling` for the current species. The generic sowing technique alone does not enable every crop.

Species identities, wild ancestors, propagation methods, cultivation compatibility and domestication criteria still need `species` definitions. The example IDs `wheat` and `maize` are illustrative references to resolve there.

## 7. Research points and turns

The JSON defines cost; it does not define a permanent number of turns.

- `initial_grant`: acquired during initialization with zero cost.
- `points`: acquired by accumulating research points.
- `cost`: total required points.
- `pointUnit`: currently `research_point`.

Illustration: a cost of 100 with 10 points per turn takes 10 turns from zero. If 30 points are already accumulated, 70 remain, so the current estimate is 7 turns. These estimates assume output and conditions remain constant and no new boost is awarded.

The engine should calculate turns remaining using the current rate. If the rate is zero, report no current completion estimate; do not divide by zero. Clamp progress to cost.

`balance.defaultResearchCost` is descriptive metadata in this prototype. Each definition already contains an explicit cost. Changing the default alone does not rewrite existing explicit costs.

Similarly, `defaultEurekaFraction` does not override each explicit reward. The current numeric values are placeholders for testing.

## 8. Resources, equipment and manufacturing

Availability checks do not consume anything. Resource consumption belongs to action/recipe execution.

`resource_tag_available` checks a tagged resource or item in the specified location, with the configured minimum amount:

- `inventory`: the inventory relevant to the action. Ownership and accessibility must be defined by the engine.
- `site_equipment`: equipment assigned to the actual operating site.

A container technology does not grant free containers. Manufacturing one may require:

| Alternative | Material inputs | Additional requirements |
| --- | --- | --- |
| `basketry` | `flexible_plant_fiber` | Manufacturing recipe and work. |
| `woodworking` | `wood` | `woodworking_tool`, recipe and work. |
| `pottery` | `clay`, `water`, `kiln_fuel` | `firing_facility`, recipe and work. |

These are tags and capability relationships, not a finished recipe catalog. Exact item IDs, quantities, processing duration, fuel compatibility and historically appropriate firing facilities remain to be defined.

Current equipment checks require at least one suitable item. They do not establish how many workers it can support, wear rates or efficiency bonuses. Those belong to production/equipment rules and balance.

Plot and equipment checks must refer to the same relevant operating context. Having a tool in a distant settlement should not satisfy a local equipment check unless transport rules make it available.

## 9. Eurekas

An eureka is a one-time research reward per research instance. It is not a technology prerequisite.

### Actual example

```json
{
  "id": "propagation_material_reserved",
  "eventType": "propagation_material_reserved",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 10
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

Interpretation: accumulate 10 reserved units of propagation material for the current species, then make a one-time reward equal to 25% of base research cost eligible. With cost 100, the reward is 25 points. It does not change the cost to 75.

Current policy:

1. Track relevant events since game start, including before research becomes available.
2. Filter events by their owning civilization and, where present, current species.
3. Prevent duplicate processing using `eventId`.
4. Preserve eligibility while the technology is locked.
5. Deliver the reward once prerequisites and start conditions are satisfied.
6. Round down the points and clamp total progress to research cost.
7. Record the claim in `GameState`; reloading cannot grant it again.

Quantity events supply their positive amount. Occurrence events supply `amount: 1`.

The file contains two exceptional distinct-count rules: crop alternation counts distinct compatible species, and line comparison counts distinct line IDs. Although their current `counter.mode` is `sum_amount`, `runtimeContract.eurekaPolicy.distinctCounters` specifies these exceptions. Before implementing a general-purpose evaluator, normalize these into explicit machine-readable counter modes or implement the documented special handlers. A naive sum of event amounts is insufficient.

Likewise, `counterGroup: plotId` means repeated harvests of the same plot, not harvests summed across unrelated plots. That grouping must survive serialization of progress.

Starting-condition checks for eureka delivery must not be mistaken for a permanent barrier to completing an already-active research project; the engine should define that lifecycle precisely during implementation.

## 10. Effects and local application

The only effect type currently used is `unlock_capability`.

Completion gives the relevant civilization/species permission to use a capability. Each use must still satisfy `usageConditions`. Rebuilding derived permissions after loading must be idempotent: the same completed technology must not stack twice.

The current file does not include numeric production modifiers, resource recipes, soil equations or genetic trait simulation. It enables capabilities that those future systems will implement.

In particular:

- Researching irrigation does not construct channels.
- Researching traction does not create trained animals.
- Researching domestication management does not instantly mark a plant population domesticated.
- Researching selection does not improve every existing field automatically.

Actual domestication and inherited traits belong to species/population simulation and state. `specialized_varieties` additionally requires a domesticated species when its capability is used.

## 11. External references and integration

The following technology IDs are declared imports, not definitions supplied by this file:
- `stone_tools`
- `basketry`
- `woodworking`
- `pottery`
- `water_management`
- `canal_construction`
- `animal_traction`
- `metal_tools`
- `cutting_tools`

The other required catalogs are `species`, `resources`, `items`, `recipes` and `sites`.

The complete loader must resolve imports before a simulation starts. A misspelled or missing prerequisite is an error, not a condition automatically treated as true. Unknown event, condition and effect types must also fail explicitly.

`requiredRuntimeHandlers` lists the 26 condition types, 17 event types and one effect type currently referenced. The list declares required behavior; it does not implement it.

## 12. What belongs in a save

Do not edit the technology definition to insert civilization progress. A save should reference the definition by ID and retain the minimum authoritative state needed to resume.

The following is a proposed state example, not an implemented or finalized save schema:

```json
{
  "saveSchemaVersion": "0.1.0",
  "contentVersion": "0.3.0",
  "turn": 12,
  "civilizations": [
    {
      "id": "civilization_001",
      "activeResearch": {
        "technologyId": "species_cultivation",
        "speciesId": "wheat"
      },
      "researchInstances": [
        {
          "technologyId": "species_cultivation",
          "speciesId": "wheat",
          "accumulatedResearch": 30,
          "completedOnTurn": null,
          "eurekaProgress": {
            "propagation_material_reserved": {
              "amount": 4,
              "claimed": false
            }
          }
        }
      ]
    }
  ]
}
```

Availability and estimated turns can be derived from definitions plus current state. If costs are copied into a save to freeze a ruleset, that must be an explicit versioning decision; do not accidentally create two conflicting authorities.

Inventory, discovered species, workers, equipment and farm state are referenced by conditions but are stored in their own parts of `GameState`. Completing a research and delivering its boost should be committed consistently so an interrupted save cannot repeat either transition.

## 13. Suggested runtime sequence

This is an implementation proposal, not executable code supplied by the JSON:

1. Load and validate a compatible ruleset.
2. Build technology indexes and reverse prerequisite links.
3. Resolve all imports and validate the combined prerequisite graph.
4. Create initial civilization state and grant initial capabilities once.
5. Accept a research command only after checking identity, prerequisites and start conditions.
6. Resolve gameplay events in a stable order and update eureka counters.
7. Deliver eligible, unclaimed boosts; update active research with that turn's available research output.
8. Complete research when its progress reaches cost and register its scoped capability once.
9. Evaluate site usage independently when actions are attempted or continued.
10. Save authoritative state, including claimed rewards and event-processing continuity.

We still need to choose whether a technology completed during a turn affects production in that same turn or the next one. Do not let incidental system execution order decide.

## 14. Validation performed versus work remaining

Already performed when creating the configuration:

- JSON parsing and serialization round trip.
- Unique technology IDs.
- Every internal prerequisite resolves locally or is explicitly declared external.
- `current_species` references originate from species-scoped technologies.
- No internal prerequisite cycles.

Not yet implemented or proven:

- A formal JSON Schema and exhaustive field validation.
- External catalog resolution, including cycles introduced by other branches.
- Condition evaluators, event tracking and capability execution.
- Save/load behavior and migrations.
- Quantitative production, trait inheritance and domestication.
- Gameplay balance and scenario tests.

An acyclic graph alone does not prove a research is reachable: resource constraints, eureka events and action unlocks can still create gameplay deadlocks. Eurekas are optional boosts, not mandatory gates.

## 15. Technology reference

| Order | ID | Name | Scope |
| --- | --- | --- | --- |
| 1 | `basic_foraging` | Basic Foraging | `civilization` |
| 2 | `plant_knowledge` | Plant Knowledge | `species` |
| 3 | `gathering_tools` | Gathering Tools | `civilization` |
| 4 | `gathering_containers` | Gathering Containers | `civilization` |
| 5 | `seed_handling` | Seed Handling | `species` |
| 6 | `wild_plant_management` | Wild Plant Management | `species` |
| 7 | `initial_sowing` | Initial Sowing | `civilization` |
| 8 | `species_cultivation` | Species Cultivation | `species` |
| 9 | `soil_preparation` | Soil Preparation | `civilization` |
| 10 | `channel_irrigation` | Channel Irrigation | `civilization` |
| 11 | `agricultural_drainage` | Agricultural Drainage | `civilization` |
| 12 | `organic_manuring` | Organic Manuring | `civilization` |
| 13 | `animal_drawn_plough` | Animal-Drawn Plough | `civilization` |
| 14 | `improved_ploughs` | Improved Ploughs | `civilization` |
| 15 | `fallow_management` | Fallow Management | `civilization` |
| 16 | `crop_alternation` | Crop Alternation | `civilization` |
| 17 | `reproductive_reserve` | Reproductive Reserve | `species` |
| 18 | `initial_selection` | Initial Selection | `species` |
| 19 | `progressive_domestication` | Progressive Domestication | `species` |
| 20 | `line_comparison` | Line Comparison | `species` |
| 21 | `specialized_varieties` | Specialized Varieties | `species` |
| 22 | `vegetative_propagation` | Vegetative Propagation | `species` |
| 23 | `grafting` | Grafting | `species` |

## 16. Next implementation checkpoint

Use a small headless simulation to verify this configuration before expanding it:

1. Grant basic foraging to two civilizations.
2. Discover wheat for one civilization and maize for the other.
3. Maintain separate species knowledge and research records.
4. Check that an unlocked capability still fails without local resources.
5. Track and claim one eureka, then save and reload without granting it twice.
6. Complete research, remove propagation material and verify knowledge remains while new sowing is blocked.

This configuration is a first contract for that prototype, not a complete agriculture simulation.


## 17. Localization

All player-visible `name` and `description` fields are language maps. This includes catalog names/descriptions, technology names/descriptions and species-group names. Technical identifiers and rules stay in English.

```json
{
  "id": "basic_foraging",
  "name": {
    "en": "Basic Foraging",
    "es": "Recolección básica"
  },
  "description": {
    "en": "Gather food from accessible edible wild plants.",
    "es": "Recoge alimentos de plantas silvestres comestibles accesibles."
  }
}
```

These are objects keyed by language codes, not arrays. To render a field, resolve the requested language, then `defaultLanguage`, then the owner's stable `id`. Empty or whitespace-only strings count as missing. The future runtime must implement this resolver; the configuration alone cannot switch UI languages.

Never store a translated name as a prerequisite or save key. A language change must not alter research identity, progress, event counters or effects. Player language belongs to user preferences, not the technology definition or civilization research state.

`designNotes`, contract explanations and balance notes are developer-facing English text and must not be displayed directly to players. Player-visible prerequisite summaries, action names, resource names, event descriptions and validation messages will need equivalent localization in their owning catalogs or the future UI; this file does not provide them all.

Schema `2.0.0` uses a flat `technologies` array. It removes `branches`, `nodes` and per-node `level`, replacing that position with global `order`. A consumer of the previous hierarchy must be adapted. Localization remains `{en, es}`. Stable technology IDs, costs, prerequisites, conditions and effects are unchanged. There is still no formal JSON Schema file included.

Later, extract translations into `en.json` and `es.json` using stable keys such as `technology.basic_foraging.name`. This is a content-format migration, separate from gameplay progression. Existing saves remain linked by technology/species IDs, subject to the normal content-version compatibility policy.
