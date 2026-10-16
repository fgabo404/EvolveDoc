# `data/technologies/agriculture.technologies.json`

[Source JSON](../../../data/technologies/agriculture.technologies.json) · [Index](../json-structures.md)

## Reading this reference

This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.

`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.

A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.

## Root and nested objects

### `$`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Version of the structural contract, not the game's release. | `"2.0.0"` |
| `contentVersion` | `string` | 1/1 | Version of the catalog content and provisional balance. | `"0.3.0"` |
| `kind` | `string` | 1/1 | Discriminator identifying this document or candidate category. | `"technology_definitions"` |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"prototype"` |
| `balance` | `object` | 1/1 | Provisional research costs and eureka balance. | `—` |
| `runtimeContract` | `object` | 1/1 | Contract the future evaluator must implement; descriptive strings are not executable code. | `—` |
| `externalReferences` | `object` | 1/1 | Imports another catalog must provide before a full simulation. | `—` |
| `manufacturingAlternatives` | `array<object>` | 1/1 | Container-making techniques and material tags; not full crafting recipes. | `—` |
| `speciesGroupBindings` | `array<object>` | 1/1 | Crop-use categories linked to the shared cultivation technology. | `—` |
| `scopeExamples` | `array<object>` | 1/1 | Illustrative technology/species bindings, not saved progress. | `—` |
| `designNotes` | `array<string>` | 1/1 | Developer notes and unresolved design details. | `["No graphics or UI state is included.", "Detailed species definitions, recipes, actual domestication state and …` |
| `requiredRuntimeHandlers` | `object` | 1/1 | Condition, event, effect and capability types needed by the full evaluator. | `—` |
| `defaultLanguage` | `string` | 1/1 | Default language for visible-text fallback. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Language codes available in this document. | `["en", "es"]` |
| `localization` | `object` | 1/1 | Representation and fallback rules for visible text. | `—` |
| `id` | `string` | 1/1 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"agriculture"` |
| `name` | `object` | 1/1 | Player-visible label using language keys. | `—` |
| `description` | `object` | 1/1 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `technologies` | `array<object>` | 1/1 | Flat list of peer technology definitions; no nested levels or nodes. | `—` |

### `$.balance`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `status` | `string` | 1/1 | Maturity, review state or current example research status; read the containing object. | `"provisional"` |
| `defaultResearchCost` | `integer` | 1/1 | Default prototype cost measured in research points. | `100` |
| `defaultEurekaFraction` | `number` | 1/1 | Default share of base cost granted by a eureka. | `0.25` |
| `note` | `string` | 1/1 | Developer clarification; not localized UI text. | `"All numeric costs, counters and boost values are illustrative starting values, not approved balance."` |

### `$.runtimeContract`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `definitionDataIsReadOnly` | `boolean` | 1/1 | Definitions must not be modified during simulation. | `true` |
| `saveStateStoredSeparately` | `boolean` | 1/1 | Mutable progress belongs in a separate game state. | `true` |
| `conditionGrammar` | `string` | 1/1 | Grammar for all/any groups and typed condition leaves. | `"An expression is {all:[expressions]}, {any:[expressions]} or a typed leaf. Empty all evaluates true. Empty any …` |
| `prerequisiteScope` | `object` | 1/1 | Meaning of civilization/current-species/any-species prerequisite resolution. | `—` |
| `researchInstanceKey` | `array<string>` | 1/1 | Fields identifying one independent research instance. | `["civilizationId", "technologyId", "speciesId"]` |
| `speciesIdRule` | `string` | 1/1 | How species binding is required or null according to scope. | `"Required for species scope; null for civilization scope. Resolve $speciesId from the current instance, never fr…` |
| `researchStartAndContinuation` | `string` | 1/1 | When to evaluate prerequisites, start conditions and ongoing conditions. | `"Check prerequisites and startConditions before starting. While active, check ongoingConditions each turn. Losin…` |
| `resourceRule` | `string` | 1/1 | Availability checks do not consume inventory; actions and recipes define consumption. | `"Availability conditions do not consume resources. Consumption is defined by action and recipe definitions. Rese…` |
| `eurekaPolicy` | `object` | 1/1 | Tracking, reward, grouping and deduplication policy for eurekas. | `—` |
| `effectRule` | `string` | 1/1 | Completion unlocks capabilities; use still checks operational conditions. | `"Completion unlocks scoped capabilities. Their use still requires usageConditions. Generational, soil and produc…` |
| `unsupportedRulePolicy` | `string` | 1/1 | Reject unknown rule types and unresolved references. | `"Reject unknown condition, event or effect types. Never silently treat unresolved references as satisfied."` |
| `integrationStatus` | `string` | 1/1 | Implementation boundary of the configuration contract. | `"Configuration contract only. No SimulationEngine implementation is included."` |
| `orderMeaning` | `string` | 1/1 | Order affects display only, never implicit research dependencies. | `"Global display order only. Explicit prerequisites define dependencies; adjacent entries are not automatically d…` |

### `$.runtimeContract.prerequisiteScope`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `civilization` | `string` | 1/1 | Shared civilization research instance, not one instance per species. | `"The shared civilization research instance."` |
| `current_species` | `string` | 1/1 | Resolve the prerequisite for the current research species. | `"The same speciesId as the current research instance."` |
| `any_species` | `string` | 1/1 | At least one species instance must satisfy the prerequisite. | `"At least one completed research instance for any species in the civilization."` |

### `$.runtimeContract.eurekaPolicy`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `historyWindow` | `string` | 1/1 | How far back gameplay event history is tracked. | `"since_game_start"` |
| `trackedBeforeResearchAvailable` | `boolean` | 1/1 | Whether eureka events are tracked while research remains locked. | `true` |
| `eventOwner` | `string` | 1/1 | Field identifying the civilization that owns an event. | `"civilizationId"` |
| `speciesFilter` | `string` | 1/1 | Rule binding eureka history to the current species when applicable. | `"current research instance when $speciesId is present"` |
| `counterUnit` | `string` | 1/1 | Event amount semantics; occurrence events contribute one. | `"Each gameplay event supplies a positive amount; occurrence events use amount=1."` |
| `grouping` | `string` | 1/1 | Restricts counting to the same matching entity rather than summing different groups. | `"A counterGroup filter restricts accumulation to one matching entity; do not sum across groups."` |
| `distinctCounters` | `object` | 1/1 | Special counters requiring distinct species or lines; not yet fully normalized in configuration. | `—` |
| `rewardTiming` | `string` | 1/1 | When an eligible eureka may grant its reward. | `"Store eligibility even while locked; grant once after prerequisites and startConditions are satisfied."` |
| `rewardRounding` | `string` | 1/1 | Formula rounding eureka points down from base cost. | `"floor(baseResearchCost * fractionOfBaseCost)"` |
| `progressLimit` | `string` | 1/1 | Cap progress at cost without bypassing prerequisites. | `"Clamp at research cost. An eureka cannot bypass prerequisites or start conditions."` |
| `deduplication` | `string` | 1/1 | Event IDs and claimed rewards prevent duplicate credit. | `"Each event has a unique eventId; each reward is claimed once per research instance and eureka ID."` |

### `$.runtimeContract.eurekaPolicy.distinctCounters`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `compatible_crop_species_harvested` | `string` | 1/1 | Count distinct compatible species, not repeated harvest events. | `"distinct speciesId in a compatible sequence"` |
| `separate_crop_line_harvest_completed` | `string` | 1/1 | Count distinct lines within the current species. | `"distinct lineId within the current species"` |

### `$.externalReferences`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyIds` | `array<string>` | 1/1 | Technology identifiers imported from external branches. | `["stone_tools", "basketry", "woodworking"]` |
| `requiredCatalogs` | `array<string>` | 1/1 | Catalog kinds the complete loader must resolve. | `["species", "resources", "items"]` |
| `note` | `string` | 1/1 | Developer clarification; not localized UI text. | `"These are declared imports. The complete game loader must resolve them before starting a simulation. They are n…` |

### `$.manufacturingAlternatives[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 3/3 | Reference to a technology definition or declared external import. | `"basketry"` |
| `inputTags` | `array<string>` | 3/3 | Material categories required by this manufacturing alternative. | `["flexible_plant_fiber"]` |
| `outputTag` | `string` | 3/3 | Category of item produced by the alternative. | `"gathering_container"` |
| `equipmentTags` | `array<string>` | 1/3 | Equipment categories required at the operating site. | `["woodworking_tool"]` |
| `siteFeatures` | `array<string>` | 1/3 | Required set of site features. | `["firing_facility"]` |

### `$.speciesGroupBindings[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"cereal"` |
| `name` | `object` | 7/7 | Player-visible label using language keys. | `—` |
| `speciesTag` | `string` | 7/7 | Category tag used to group candidate species. | `"cereal"` |
| `cultivationTechnologyId` | `string` | 7/7 | Reference to the cultivation technology used by this group. | `"species_cultivation"` |

### `$.speciesGroupBindings[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 7/7 | English visible text. | `"Cereals"` |
| `es` | `string` | 7/7 | Spanish visible text. | `"Cereales"` |

### `$.scopeExamples[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 2/2 | Reference to a technology definition or declared external import. | `"species_cultivation"` |
| `speciesId` | `string` | 2/2 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"wheat"` |

### `$.requiredRuntimeHandlers`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `conditionTypes` | `array<string>` | 1/1 | Names of condition handlers required by the catalog. | `["accessible_edible_plants", "accessible_land_available", "alternative_food_supply_available"]` |
| `eventTypes` | `array<string>` | 1/1 | Names of gameplay event handlers required by eurekas. | `["compatible_crop_species_harvested", "crop_generation_completed", "crop_harvest_completed"]` |
| `effectTypes` | `array<string>` | 1/1 | Names of supported completion-effect handlers. | `["unlock_capability"]` |
| `capabilityIds` | `array<string>` | 1/1 | Capability identifiers unlocked by the technology catalog. | `["agricultural_drainage", "animal_drawn_plough", "basic_foraging"]` |

### `$.localization`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `format` | `string` | 1/1 | Format of the source snapshot or localization representation. | `"inline_language_map"` |
| `visibleFields` | `array<string>` | 1/1 | Fields that require language-map values. | `["name", "description"]` |
| `fallbackOrder` | `array<string>` | 1/1 | Fallback sequence when requested-language text is missing. | `["requested_language", "defaultLanguage", "id"]` |
| `missingValuePolicy` | `string` | 1/1 | Behavior when no requested/default translation exists. | `"Treat an absent, empty or whitespace-only translation as missing."` |
| `identityPolicy` | `string` | 1/1 | Localized text must not be used as identity or dependency. | `"Never use translated text as an ID, dependency, event type or save key."` |
| `futureExtraction` | `string` | 1/1 | Plan to move inline localized text into separate language files later. | `"Preserve stable IDs when moving translations to external language catalogs. Each field can later use a key such…` |
| `technicalTextPolicy` | `string` | 1/1 | Technical strings remain English and are not player-facing translations. | `"designNotes, runtimeContract, balance notes and external reference notes are developer-facing English text, not…` |

### `$.name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 1/1 | English visible text. | `"Agriculture"` |
| `es` | `string` | 1/1 | Spanish visible text. | `"Agricultura"` |

### `$.description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 1/1 | English visible text. | `"Forage, cultivate and improve plant species through knowledge, equipment and local practice."` |
| `es` | `string` | 1/1 | Spanish visible text. | `"Recolecta, cultiva y mejora especies vegetales mediante conocimientos, equipos y prácticas locales."` |

### `$.technologies[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 23/23 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"basic_foraging"` |
| `name` | `object` | 23/23 | Player-visible label using language keys. | `—` |
| `description` | `object` | 23/23 | Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text. | `—` |
| `scope` | `string` | 23/23 | Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object. | `"civilization"` |
| `prerequisites` | `object` | 23/23 | Technology dependency expression evaluated before research can start. | `—` |
| `research` | `object` | 23/23 | Acquisition mode, cost and research start/continuation rules. | `—` |
| `usageConditions` | `object` | 23/23 | Local operational requirements for using an unlocked capability. | `—` |
| `eurekas` | `array<object>` | 23/23 | Event-driven research boosts; empty means no configured boost. | `[]` |
| `effects` | `array<object>` | 23/23 | Completion effects; current catalog only unlocks capabilities. | `—` |
| `designNotes` | `array<string>` | 23/23 | Developer notes and unresolved design details. | `[]` |
| `order` | `integer` | 23/23 | Presentation position; explicit prerequisites determine actual progression. | `1` |

### `$.technologies[].name`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 23/23 | English visible text. | `"Basic Foraging"` |
| `es` | `string` | 23/23 | Spanish visible text. | `"Recolección básica"` |

### `$.technologies[].description`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `en` | `string` | 23/23 | English visible text. | `"Gather food from accessible edible wild plants."` |
| `es` | `string` | 23/23 | Spanish visible text. | `"Recoge alimentos de plantas silvestres comestibles accesibles."` |

### `$.technologies[].prerequisites`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 22/23 | All child expressions must pass; an empty list evaluates true. | `[]` |
| `any` | `array<object>` | 1/23 | At least one expression must pass; an empty list is invalid in the contract. | `—` |

### `$.technologies[].research`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `mode` | `string` | 23/23 | Research acquisition mode or eureka counter mode; read the containing object. | `"initial_grant"` |
| `cost` | `integer` | 23/23 | Base research cost in pointUnit, not a fixed number of turns. | `0` |
| `pointUnit` | `string` | 23/23 | Unit used by research cost and progress. | `"research_point"` |
| `startConditions` | `object` | 23/23 | Conditions required to start research; not repeated as ongoing requirements unless explicitly listed. | `—` |
| `ongoingConditions` | `object` | 23/23 | Conditions checked each active turn; failure pauses and retains progress. | `—` |
| `onConditionFailure` | `string` | 23/23 | Policy applied when ongoing conditions fail. | `"pause_keep_progress"` |

### `$.technologies[].research.startConditions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 23/23 | All child expressions must pass; an empty list evaluates true. | `[]` |

### `$.technologies[].research.ongoingConditions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `all` | `array<?>` | 23/23 | All child expressions must pass; an empty list evaluates true. | `[]` |

### `$.technologies[].usageConditions`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 23/23 | All child expressions must pass; an empty list evaluates true. | `—` |

### `$.technologies[].usageConditions.all[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 81/81 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"workers_assigned"` |
| `minimumCount` | `integer` | 23/81 | Minimum number of workers or entities required by the typed condition. | `1` |
| `speciesId` | `string` | 29/81 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"$speciesId"` |
| `tag` | `string` | 9/81 | English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs. | `"gathering_tool"` |
| `location` | `string` | 9/81 | Context in which an availability condition must be satisfied, such as the operating site. | `"site_equipment"` |
| `minimumAmount` | `integer` | 14/81 | Minimum accessible material quantity; not an automatic consumption amount. | `1` |
| `feature` | `string` | 5/81 | Required site feature identifier. | `"accessible_water_source"` |
| `minimumSpeciesCount` | `integer` | 1/81 | Minimum number of distinct compatible species. | `2` |
| `minimumLineCount` | `integer` | 1/81 | Minimum number of distinct crop lines. | `2` |
| `method` | `string` | 1/81 | Propagation/use method required by the typed condition. | `"vegetative_propagation"` |

### `$.technologies[].effects[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 23/23 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"unlock_capability"` |
| `capabilityId` | `string` | 23/23 | Identifier of the capability unlocked by this effect. | `"basic_foraging"` |
| `scope` | `string` | 23/23 | Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object. | `"civilization"` |
| `activation` | `string` | 23/23 | When the capability is operational; usage conditions still apply. | `"while_usage_conditions_met"` |

### `$.technologies[].prerequisites.all[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 36/36 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"technology_completed"` |
| `technologyId` | `string` | 36/36 | Reference to a technology definition or declared external import. | `"basic_foraging"` |
| `scope` | `string` | 36/36 | Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object. | `"civilization"` |

### `$.technologies[].research.startConditions.all[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 22/22 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"species_discovered"` |
| `speciesId` | `string` | 22/22 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"$speciesId"` |

### `$.technologies[].eurekas[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `id` | `string` | 22/22 | Stable identity of this definition or fixture civilization; never use a translated name as identity. | `"plant_gathered"` |
| `eventType` | `string` | 22/22 | Gameplay event type to match. | `"plant_gathered"` |
| `filters` | `object` | 22/22 | Constraints restricting which events contribute to a eureka. | `—` |
| `counter` | `object` | 22/22 | Accumulation mode and threshold. | `—` |
| `reward` | `object` | 22/22 | Research-point reward, not automatic prerequisite completion. | `—` |
| `repeatable` | `boolean` | 22/22 | Whether the eureka can grant again; false means once per research instance and eureka ID. | `false` |

### `$.technologies[].eurekas[].filters`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `speciesId` | `string` | 11/22 | Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope. | `"$speciesId"` |
| `itemTag` | `string` | 4/22 | Item-category filter for crafting events. | `"stone_gathering_tool"` |
| `siteFeature` | `string` | 2/22 | Site-feature event filter. | `"accessible_water_source"` |
| `resourceTag` | `string` | 1/22 | English resource-category tag; not a resolved resource ID. | `"livestock_manure"` |
| `counterGroup` | `string` | 1/22 | Event field used to restrict accumulation to one entity, e.g. one plot. | `"plotId"` |

### `$.technologies[].eurekas[].counter`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `mode` | `string` | 22/22 | Research acquisition mode or eureka counter mode; read the containing object. | `"sum_amount"` |
| `target` | `integer` | 22/22 | Counter threshold in the event's counting unit. | `20` |

### `$.technologies[].eurekas[].reward`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 22/22 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"add_research_points"` |
| `fractionOfBaseCost` | `number` | 22/22 | Fraction of the technology's base research cost granted as points. | `0.25` |

### `$.technologies[].prerequisites.any[]`

| Field | Current JSON type | Seen | Meaning | Sample value |
| --- | --- | --- | --- | --- |
| `type` | `string` | 3/3 | Condition/reward/effect discriminator, or JSON Schema type in schema documents. | `"technology_completed"` |
| `technologyId` | `string` | 3/3 | Reference to a technology definition or declared external import. | `"basketry"` |
| `scope` | `string` | 3/3 | Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object. | `"civilization"` |

## Complete example document with reduced repeated arrays

Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.

```json
{
  "schemaVersion": "2.0.0",
  "contentVersion": "0.3.0",
  "kind": "technology_definitions",
  "status": "prototype",
  "balance": {
    "status": "provisional",
    "defaultResearchCost": 100,
    "defaultEurekaFraction": 0.25,
    "note": "All numeric costs, counters and boost values are illustrative starting values, not approved balance."
  },
  "runtimeContract": {
    "definitionDataIsReadOnly": true,
    "saveStateStoredSeparately": true,
    "conditionGrammar": "An expression is {all:[expressions]}, {any:[expressions]} or a typed leaf. Empty all evaluates true. Empty any is invalid.",
    "prerequisiteScope": {
      "civilization": "The shared civilization research instance.",
      "current_species": "The same speciesId as the current research instance.",
      "any_species": "At least one completed research instance for any species in the civilization."
    },
    "researchInstanceKey": [
      "civilizationId",
      "technologyId",
      "speciesId"
    ],
    "speciesIdRule": "Required for species scope; null for civilization scope. Resolve $speciesId from the current instance, never from translated names.",
    "researchStartAndContinuation": "Check prerequisites and startConditions before starting. While active, check ongoingConditions each turn. Losing access to specimens does not erase knowledge or progress.",
    "resourceRule": "Availability conditions do not consume resources. Consumption is defined by action and recipe definitions. Research effects never create equipment or plants.",
    "eurekaPolicy": {
      "historyWindow": "since_game_start",
      "trackedBeforeResearchAvailable": true,
      "eventOwner": "civilizationId",
      "speciesFilter": "current research instance when $speciesId is present",
      "counterUnit": "Each gameplay event supplies a positive amount; occurrence events use amount=1.",
      "grouping": "A counterGroup filter restricts accumulation to one matching entity; do not sum across groups.",
      "distinctCounters": {
        "compatible_crop_species_harvested": "distinct speciesId in a compatible sequence",
        "separate_crop_line_harvest_completed": "distinct lineId within the current species"
      },
      "rewardTiming": "Store eligibility even while locked; grant once after prerequisites and startConditions are satisfied.",
      "rewardRounding": "floor(baseResearchCost * fractionOfBaseCost)",
      "progressLimit": "Clamp at research cost. An eureka cannot bypass prerequisites or start conditions.",
      "deduplication": "Each event has a unique eventId; each reward is claimed once per research instance and eureka ID."
    },
    "effectRule": "Completion unlocks scoped capabilities. Their use still requires usageConditions. Generational, soil and production systems implement actual outcomes. Restore capabilities idempotently when loading a save.",
    "unsupportedRulePolicy": "Reject unknown condition, event or effect types. Never silently treat unresolved references as satisfied.",
    "integrationStatus": "Configuration contract only. No SimulationEngine implementation is included.",
    "orderMeaning": "Global display order only. Explicit prerequisites define dependencies; adjacent entries are not automatically dependent."
  },
  "externalReferences": {
    "technologyIds": [
      "stone_tools",
      "basketry",
      "woodworking",
      "pottery",
      "water_management",
      "canal_construction",
      "animal_traction",
      "metal_tools",
      "cutting_tools"
    ],
    "requiredCatalogs": [
      "species",
      "resources",
      "items",
      "recipes",
      "sites"
    ],
    "note": "These are declared imports. The complete game loader must resolve them before starting a simulation. They are not implemented by this file."
  },
  "manufacturingAlternatives": [
    {
      "technologyId": "basketry",
      "inputTags": [
        "flexible_plant_fiber"
      ],
      "outputTag": "gathering_container"
    }
  ],
  "speciesGroupBindings": [
    {
      "id": "cereal",
      "name": {
        "en": "Cereals",
        "es": "Cereales"
      },
      "speciesTag": "cereal",
      "cultivationTechnologyId": "species_cultivation"
    }
  ],
  "scopeExamples": [
    {
      "technologyId": "species_cultivation",
      "speciesId": "wheat"
    }
  ],
  "designNotes": [
    "No graphics or UI state is included.",
    "Detailed species definitions, recipes, actual domestication state and local farm improvements belong to their respective catalogs and GameState.",
    "Plant knowledge and seed handling progress independently per species.",
    "Irrigation, drainage, manuring and ploughing can develop in parallel according to explicit prerequisites.",
    "No storage technology universally requires pottery.",
    "The same species may have multiple crop-use tags.",
    "The two example species IDs must be resolved against the future species catalog.",
    "Technology definitions are flat. Node and branch containers have been removed; stable technology IDs, scopes and explicit prerequisites remain authoritative."
  ],
  "requiredRuntimeHandlers": {
    "conditionTypes": [
      "accessible_edible_plants",
      "accessible_land_available",
      "alternative_food_supply_available",
      "any_viable_propagation_material_available",
      "compatible_crop_sequence_available",
      "compatible_grafting_material_available",
      "compatible_plot_available",
      "cultivable_land_available",
      "cultivated_plot_available",
      "draft_animals_supported",
      "observable_trait_variation_available",
      "propagation_storage_available",
      "reproducing_crop_population_available",
      "resource_tag_available",
      "selectable_crop_lines_available",
      "separate_identified_crop_lines_available",
      "site_feature_available",
      "species_discovered",
      "species_domesticated",
      "species_material_accessible",
      "species_plants_accessible",
      "species_propagation_material_available",
      "species_supports_method",
      "technology_completed",
      "trained_draft_animals_available",
      "workers_assigned"
    ],
    "eventTypes": [
      "compatible_crop_species_harvested",
      "crop_generation_completed",
      "crop_harvest_completed",
      "draft_plough_team_assembled",
      "graftable_orchard_established",
      "item_crafted",
      "land_surveyed",
      "plant_gathered",
      "plot_established",
      "plot_harvest_completed",
      "propagation_material_collected",
      "propagation_material_reserved",
      "resource_produced",
      "separate_crop_line_harvest_completed",
      "target_trait_reproduced",
      "useful_plant_trait_observed",
      "vegetative_plant_established"
    ],
    "effectTypes": [
      "unlock_capability"
    ],
    "capabilityIds": [
      "agricultural_drainage",
      "animal_drawn_plough",
      "basic_foraging",
      "channel_irrigation",
      "crop_alternation",
      "fallow_management",
      "gathering_containers",
      "gathering_tools",
      "grafting",
      "improved_ploughs",
      "initial_selection",
      "initial_sowing",
      "line_comparison",
      "organic_manuring",
      "plant_knowledge",
      "progressive_domestication",
      "reproductive_reserve",
      "seed_handling",
      "soil_preparation",
      "specialized_varieties",
      "species_cultivation",
      "vegetative_propagation",
      "wild_plant_management"
    ]
  },
  "defaultLanguage": "en",
  "supportedLanguages": [
    "en",
    "es"
  ],
  "localization": {
    "format": "inline_language_map",
    "visibleFields": [
      "name",
      "description"
    ],
    "fallbackOrder": [
      "requested_language",
      "defaultLanguage",
      "id"
    ],
    "missingValuePolicy": "Treat an absent, empty or whitespace-only translation as missing.",
    "identityPolicy": "Never use translated text as an ID, dependency, event type or save key.",
    "futureExtraction": "Preserve stable IDs when moving translations to external language catalogs. Each field can later use a key such as technology.<id>.name. No external language catalogs or resolver implementation are included yet.",
    "technicalTextPolicy": "designNotes, runtimeContract, balance notes and external reference notes are developer-facing English text, not player-visible strings."
  },
  "id": "agriculture",
  "name": {
    "en": "Agriculture",
    "es": "Agricultura"
  },
  "description": {
    "en": "Forage, cultivate and improve plant species through knowledge, equipment and local practice.",
    "es": "Recolecta, cultiva y mejora especies vegetales mediante conocimientos, equipos y prácticas locales."
  },
  "technologies": [
    {
      "id": "basic_foraging",
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
      "designNotes": [],
      "order": 1
    },
    {
      "id": "gathering_containers",
      "name": {
        "en": "Gathering Containers",
        "es": "Recipientes de recolección"
      },
      "description": {
        "en": "Enable equipped workers to carry more gathered food.",
        "es": "Permite que los trabajadores equipados transporten más alimentos recolectados."
      },
      "scope": "civilization",
      "prerequisites": {
        "any": [
          {
            "type": "technology_completed",
            "technologyId": "basketry",
            "scope": "civilization"
          }
        ]
      },
      "research": {
        "mode": "points",
        "cost": 100,
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
          }
        ]
      },
      "eurekas": [
        {
          "id": "item_crafted",
          "eventType": "item_crafted",
          "filters": {
            "itemTag": "gathering_container"
          },
          "counter": {
            "mode": "sum_amount",
            "target": 1
          },
          "reward": {
            "type": "add_research_points",
            "fractionOfBaseCost": 0.25
          },
          "repeatable": false
        }
      ],
      "effects": [
        {
          "type": "unlock_capability",
          "capabilityId": "gathering_containers",
          "scope": "civilization",
          "activation": "while_usage_conditions_met"
        }
      ],
      "designNotes": [
        "Any one container technology is sufficient. Raw materials are consumed by manufacturing recipes, not by researching or using this technology."
      ],
      "order": 4
    },
    {
      "id": "species_cultivation",
      "name": {
        "en": "Species Cultivation",
        "es": "Cultivo por especie"
      },
      "description": {
        "en": "Apply sowing and crop care to one discovered species.",
        "es": "Aplica la siembra y el cuidado de cultivos a una especie descubierta."
      },
      "scope": "species",
      "prerequisites": {
        "all": [
          {
            "type": "technology_completed",
            "technologyId": "initial_sowing",
            "scope": "civilization"
          }
        ]
      },
      "research": {
        "mode": "points",
        "cost": 100,
        "pointUnit": "research_point",
        "startConditions": {
          "all": [
            {
              "type": "species_discovered",
              "speciesId": "$speciesId"
            }
          ]
        },
        "ongoingConditions": {
          "all": []
        },
        "onConditionFailure": "pause_keep_progress"
      },
      "usageConditions": {
        "all": [
          {
            "type": "species_discovered",
            "speciesId": "$speciesId"
          }
        ]
      },
      "eurekas": [
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
      ],
      "effects": [
        {
          "type": "unlock_capability",
          "capabilityId": "species_cultivation",
          "scope": "species",
          "activation": "while_usage_conditions_met"
        }
      ],
      "designNotes": [
        "Wheat and maize use separate research instances identified by technologyId and speciesId. Wild ancestors and domesticated crops must be distinguished in the species catalog."
      ],
      "order": 8
    }
  ]
}
```

## Condition and eureka variants

These are exact leaf/filter examples taken from the current file. Different `type` values accept different fields; the union table above does not permit arbitrary field combinations. Every configured condition and eureka event type appears below.

### `accessible_edible_plants`

```json
[
  {
    "type": "accessible_edible_plants"
  }
]
```

### `accessible_land_available`

```json
[
  {
    "type": "accessible_land_available"
  }
]
```

### `alternative_food_supply_available`

```json
[
  {
    "type": "alternative_food_supply_available"
  }
]
```

### `any_viable_propagation_material_available`

```json
[
  {
    "type": "any_viable_propagation_material_available"
  }
]
```

### `compatible_crop_sequence_available`

```json
[
  {
    "type": "compatible_crop_sequence_available",
    "minimumSpeciesCount": 2
  }
]
```

### `compatible_grafting_material_available`

```json
[
  {
    "type": "compatible_grafting_material_available",
    "speciesId": "$speciesId"
  }
]
```

### `compatible_plot_available`

```json
[
  {
    "type": "compatible_plot_available",
    "speciesId": "$speciesId"
  }
]
```

### `cultivable_land_available`

```json
[
  {
    "type": "cultivable_land_available"
  }
]
```

### `cultivated_plot_available`

```json
[
  {
    "type": "cultivated_plot_available"
  }
]
```

### `draft_animals_supported`

```json
[
  {
    "type": "draft_animals_supported"
  }
]
```

### `observable_trait_variation_available`

```json
[
  {
    "type": "observable_trait_variation_available",
    "speciesId": "$speciesId"
  }
]
```

### `propagation_storage_available`

```json
[
  {
    "type": "propagation_storage_available",
    "speciesId": "$speciesId"
  }
]
```

### `reproducing_crop_population_available`

```json
[
  {
    "type": "reproducing_crop_population_available",
    "speciesId": "$speciesId"
  }
]
```

### `resource_tag_available`

```json
[
  {
    "type": "resource_tag_available",
    "tag": "gathering_tool",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "gathering_container",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "soil_working_tool",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "suitable_organic_fertilizer",
    "location": "inventory",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "wooden_plough",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "compatible_draft_harness",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "improved_plough",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "grafting_tool",
    "location": "site_equipment",
    "minimumAmount": 1
  },
  {
    "type": "resource_tag_available",
    "tag": "grafting_binding",
    "location": "inventory",
    "minimumAmount": 1
  }
]
```

### `selectable_crop_lines_available`

```json
[
  {
    "type": "selectable_crop_lines_available",
    "speciesId": "$speciesId"
  }
]
```

### `separate_identified_crop_lines_available`

```json
[
  {
    "type": "separate_identified_crop_lines_available",
    "speciesId": "$speciesId",
    "minimumLineCount": 2
  }
]
```

### `site_feature_available`

```json
[
  {
    "type": "site_feature_available",
    "feature": "accessible_water_source"
  },
  {
    "type": "site_feature_available",
    "feature": "operational_irrigation_channels"
  },
  {
    "type": "site_feature_available",
    "feature": "viable_drainage_outlet"
  },
  {
    "type": "site_feature_available",
    "feature": "operational_drainage_channels"
  },
  {
    "type": "site_feature_available",
    "feature": "compatible_plough_soil"
  }
]
```

### `species_discovered`

```json
[
  {
    "type": "species_discovered",
    "speciesId": "$speciesId"
  }
]
```

### `species_domesticated`

```json
[
  {
    "type": "species_domesticated",
    "speciesId": "$speciesId"
  }
]
```

### `species_material_accessible`

```json
[
  {
    "type": "species_material_accessible",
    "speciesId": "$speciesId"
  }
]
```

### `species_plants_accessible`

```json
[
  {
    "type": "species_plants_accessible",
    "speciesId": "$speciesId"
  }
]
```

### `species_propagation_material_available`

```json
[
  {
    "type": "species_propagation_material_available",
    "speciesId": "$speciesId",
    "minimumAmount": 1
  }
]
```

### `species_supports_method`

```json
[
  {
    "type": "species_supports_method",
    "speciesId": "$speciesId",
    "method": "vegetative_propagation"
  }
]
```

### `technology_completed`

```json
[
  {
    "type": "technology_completed",
    "technologyId": "basic_foraging",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "stone_tools",
    "scope": "civilization"
  },
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
  },
  {
    "type": "technology_completed",
    "technologyId": "plant_knowledge",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "seed_handling",
    "scope": "any_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "initial_sowing",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "seed_handling",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "water_management",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "canal_construction",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "plant_knowledge",
    "scope": "any_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "soil_preparation",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "animal_traction",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "animal_drawn_plough",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "metal_tools",
    "scope": "civilization"
  },
  {
    "type": "technology_completed",
    "technologyId": "species_cultivation",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "reproductive_reserve",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "initial_selection",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "line_comparison",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "progressive_domestication",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "vegetative_propagation",
    "scope": "current_species"
  },
  {
    "type": "technology_completed",
    "technologyId": "cutting_tools",
    "scope": "civilization"
  }
]
```

### `trained_draft_animals_available`

```json
[
  {
    "type": "trained_draft_animals_available"
  }
]
```

### `workers_assigned`

```json
[
  {
    "type": "workers_assigned",
    "minimumCount": 1
  }
]
```

### Eureka event: `compatible_crop_species_harvested`

```json
{
  "id": "compatible_crop_species_harvested",
  "eventType": "compatible_crop_species_harvested",
  "filters": {},
  "counter": {
    "mode": "sum_amount",
    "target": 2
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `crop_generation_completed`

```json
{
  "id": "crop_generation_completed",
  "eventType": "crop_generation_completed",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 3
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `crop_harvest_completed`

```json
{
  "id": "crop_harvest_completed",
  "eventType": "crop_harvest_completed",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `draft_plough_team_assembled`

```json
{
  "id": "draft_plough_team_assembled",
  "eventType": "draft_plough_team_assembled",
  "filters": {},
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `graftable_orchard_established`

```json
{
  "id": "graftable_orchard_established",
  "eventType": "graftable_orchard_established",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `item_crafted`

```json
{
  "id": "item_crafted",
  "eventType": "item_crafted",
  "filters": {
    "itemTag": "stone_gathering_tool"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `land_surveyed`

```json
{
  "id": "land_surveyed",
  "eventType": "land_surveyed",
  "filters": {
    "siteFeature": "excess_soil_water"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `plant_gathered`

```json
{
  "id": "plant_gathered",
  "eventType": "plant_gathered",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 20
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `plot_established`

```json
{
  "id": "plot_established",
  "eventType": "plot_established",
  "filters": {
    "siteFeature": "accessible_water_source"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `plot_harvest_completed`

```json
{
  "id": "plot_harvest_completed",
  "eventType": "plot_harvest_completed",
  "filters": {
    "counterGroup": "plotId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 3
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `propagation_material_collected`

```json
{
  "id": "propagation_material_collected",
  "eventType": "propagation_material_collected",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 5
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `propagation_material_reserved`

```json
{
  "id": "propagation_material_reserved",
  "eventType": "propagation_material_reserved",
  "filters": {},
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

### Eureka event: `resource_produced`

```json
{
  "id": "resource_produced",
  "eventType": "resource_produced",
  "filters": {
    "resourceTag": "livestock_manure"
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

### Eureka event: `separate_crop_line_harvest_completed`

```json
{
  "id": "separate_crop_line_harvest_completed",
  "eventType": "separate_crop_line_harvest_completed",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 2
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `target_trait_reproduced`

```json
{
  "id": "target_trait_reproduced",
  "eventType": "target_trait_reproduced",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 3
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `useful_plant_trait_observed`

```json
{
  "id": "useful_plant_trait_observed",
  "eventType": "useful_plant_trait_observed",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```

### Eureka event: `vegetative_plant_established`

```json
{
  "id": "vegetative_plant_established",
  "eventType": "vegetative_plant_established",
  "filters": {
    "speciesId": "$speciesId"
  },
  "counter": {
    "mode": "sum_amount",
    "target": 1
  },
  "reward": {
    "type": "add_research_points",
    "fractionOfBaseCost": 0.25
  },
  "repeatable": false
}
```
