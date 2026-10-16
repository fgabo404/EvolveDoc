# `data/technologies/agriculture.technologies.json`

[JSON fuente](../../../data/technologies/agriculture.technologies.json) · [Index](../json-structures.md)

## Cómo leer esta referencia

Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.

`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.

Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.

## Raíz y objetos internos

### `$`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `schemaVersion` | `string` | 1/1 | Versión del contrato estructural, no del lanzamiento del juego. | `"2.0.0"` |
| `contentVersion` | `string` | 1/1 | Versión del contenido del catálogo y del balance provisional. | `"0.3.0"` |
| `kind` | `string` | 1/1 | Discriminador que identifica el documento o categoría del candidato. | `"technology_definitions"` |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"prototype"` |
| `balance` | `object` | 1/1 | Costos provisionales de investigación y balance de eurekas. | `—` |
| `runtimeContract` | `object` | 1/1 | Contrato que implementará el evaluador; las cadenas descriptivas no son código ejecutable. | `—` |
| `externalReferences` | `object` | 1/1 | Importaciones que otro catálogo debe resolver antes de una simulación completa. | `—` |
| `manufacturingAlternatives` | `array<object>` | 1/1 | Técnicas de recipientes y tags de materiales; no son recetas completas. | `—` |
| `speciesGroupBindings` | `array<object>` | 1/1 | Categorías de uso agrícola vinculadas a la tecnología común de cultivo. | `—` |
| `scopeExamples` | `array<object>` | 1/1 | Vínculos ilustrativos de tecnología/especie, no avance guardado. | `—` |
| `designNotes` | `array<string>` | 1/1 | Notas técnicas y detalles de diseño pendientes. | `["No graphics or UI state is included.", "Detailed species definitions, recipes, actual domestication state and …` |
| `requiredRuntimeHandlers` | `object` | 1/1 | Tipos de condición, evento, efecto y capacidad requeridos por el evaluador completo. | `—` |
| `defaultLanguage` | `string` | 1/1 | Idioma predeterminado para el texto visible. | `"en"` |
| `supportedLanguages` | `array<string>` | 1/1 | Códigos de idioma disponibles. | `["en", "es"]` |
| `localization` | `object` | 1/1 | Representación y reglas de respaldo del texto visible. | `—` |
| `id` | `string` | 1/1 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"agriculture"` |
| `name` | `object` | 1/1 | Nombre visible mediante claves de idioma. | `—` |
| `description` | `object` | 1/1 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `—` |
| `technologies` | `array<object>` | 1/1 | Lista de tecnologías al mismo nivel; sin niveles ni nodos anidados. | `—` |

### `$.balance`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `status` | `string` | 1/1 | Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor. | `"provisional"` |
| `defaultResearchCost` | `integer` | 1/1 | Costo predeterminado del prototipo en puntos de investigación. | `100` |
| `defaultEurekaFraction` | `number` | 1/1 | Fracción predeterminada del costo base concedida por eureka. | `0.25` |
| `note` | `string` | 1/1 | Aclaración técnica; no es texto traducido de interfaz. | `"All numeric costs, counters and boost values are illustrative starting values, not approved balance."` |

### `$.runtimeContract`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `definitionDataIsReadOnly` | `boolean` | 1/1 | Las definiciones no cambian durante la simulación. | `true` |
| `saveStateStoredSeparately` | `boolean` | 1/1 | El avance mutable pertenece a un estado de partida separado. | `true` |
| `conditionGrammar` | `string` | 1/1 | Gramática para grupos all/any y condiciones con tipo. | `"An expression is {all:[expressions]}, {any:[expressions]} or a typed leaf. Empty all evaluates true. Empty any …` |
| `prerequisiteScope` | `object` | 1/1 | Significado de requisitos de civilización, especie actual o cualquier especie. | `—` |
| `researchInstanceKey` | `array<string>` | 1/1 | Campos que identifican una investigación independiente. | `["civilizationId", "technologyId", "speciesId"]` |
| `speciesIdRule` | `string` | 1/1 | Cómo vincular especie o usar null según el ámbito. | `"Required for species scope; null for civilization scope. Resolve $speciesId from the current instance, never fr…` |
| `researchStartAndContinuation` | `string` | 1/1 | Cuándo evaluar requisitos, inicio y continuación. | `"Check prerequisites and startConditions before starting. While active, check ongoingConditions each turn. Losin…` |
| `resourceRule` | `string` | 1/1 | Comprobar disponibilidad no consume inventario; el consumo corresponde a acciones y recetas. | `"Availability conditions do not consume resources. Consumption is defined by action and recipe definitions. Rese…` |
| `eurekaPolicy` | `object` | 1/1 | Política de seguimiento, recompensa, agrupación y deduplicación de eurekas. | `—` |
| `effectRule` | `string` | 1/1 | Completar desbloquea capacidades; utilizarlas requiere condiciones operativas. | `"Completion unlocks scoped capabilities. Their use still requires usageConditions. Generational, soil and produc…` |
| `unsupportedRulePolicy` | `string` | 1/1 | Rechazar tipos desconocidos y referencias pendientes. | `"Reject unknown condition, event or effect types. Never silently treat unresolved references as satisfied."` |
| `integrationStatus` | `string` | 1/1 | Límite de implementación del contrato de configuración. | `"Configuration contract only. No SimulationEngine implementation is included."` |
| `orderMeaning` | `string` | 1/1 | Order solo ordena presentación, no crea requisitos implícitos. | `"Global display order only. Explicit prerequisites define dependencies; adjacent entries are not automatically d…` |

### `$.runtimeContract.prerequisiteScope`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `civilization` | `string` | 1/1 | Investigación compartida de civilización, no una por especie. | `"The shared civilization research instance."` |
| `current_species` | `string` | 1/1 | Resolver el requisito para la especie de la investigación actual. | `"The same speciesId as the current research instance."` |
| `any_species` | `string` | 1/1 | Al menos una especie debe cumplir el requisito. | `"At least one completed research instance for any species in the civilization."` |

### `$.runtimeContract.eurekaPolicy`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `historyWindow` | `string` | 1/1 | Desde cuándo se considera el historial de eventos. | `"since_game_start"` |
| `trackedBeforeResearchAvailable` | `boolean` | 1/1 | Indica si registra eventos de eureka antes de habilitar investigación. | `true` |
| `eventOwner` | `string` | 1/1 | Campo que identifica a la civilización propietaria del evento. | `"civilizationId"` |
| `speciesFilter` | `string` | 1/1 | Regla que vincula el historial de eureka con la especie actual. | `"current research instance when $speciesId is present"` |
| `counterUnit` | `string` | 1/1 | Significado de la cantidad del evento; las ocurrencias aportan uno. | `"Each gameplay event supplies a positive amount; occurrence events use amount=1."` |
| `grouping` | `string` | 1/1 | Restringe el conteo a una entidad coincidente en vez de sumar grupos distintos. | `"A counterGroup filter restricts accumulation to one matching entity; do not sum across groups."` |
| `distinctCounters` | `object` | 1/1 | Contadores especiales de especies o líneas distintas; configuración todavía no normalizada. | `—` |
| `rewardTiming` | `string` | 1/1 | Cuándo una eureka elegible puede entregar recompensa. | `"Store eligibility even while locked; grant once after prerequisites and startConditions are satisfied."` |
| `rewardRounding` | `string` | 1/1 | Fórmula que redondea hacia abajo puntos de eureka a partir del costo base. | `"floor(baseResearchCost * fractionOfBaseCost)"` |
| `progressLimit` | `string` | 1/1 | Limitar avance al costo sin omitir requisitos. | `"Clamp at research cost. An eureka cannot bypass prerequisites or start conditions."` |
| `deduplication` | `string` | 1/1 | Los IDs de evento y recompensas reclamadas evitan duplicación. | `"Each event has a unique eventId; each reward is claimed once per research instance and eureka ID."` |

### `$.runtimeContract.eurekaPolicy.distinctCounters`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `compatible_crop_species_harvested` | `string` | 1/1 | Contar especies compatibles distintas, no cosechas repetidas. | `"distinct speciesId in a compatible sequence"` |
| `separate_crop_line_harvest_completed` | `string` | 1/1 | Contar líneas distintas dentro de la especie actual. | `"distinct lineId within the current species"` |

### `$.externalReferences`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyIds` | `array<string>` | 1/1 | Identificadores tecnológicos importados de otras ramas. | `["stone_tools", "basketry", "woodworking"]` |
| `requiredCatalogs` | `array<string>` | 1/1 | Tipos de catálogo que deberá resolver el cargador completo. | `["species", "resources", "items"]` |
| `note` | `string` | 1/1 | Aclaración técnica; no es texto traducido de interfaz. | `"These are declared imports. The complete game loader must resolve them before starting a simulation. They are n…` |

### `$.manufacturingAlternatives[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 3/3 | Referencia a una definición tecnológica o importación externa declarada. | `"basketry"` |
| `inputTags` | `array<string>` | 3/3 | Categorías de material requeridas por esta alternativa. | `["flexible_plant_fiber"]` |
| `outputTag` | `string` | 3/3 | Categoría del objeto producido por la alternativa. | `"gathering_container"` |
| `equipmentTags` | `array<string>` | 1/3 | Categorías de equipo requeridas en el sitio operativo. | `["woodworking_tool"]` |
| `siteFeatures` | `array<string>` | 1/3 | Conjunto de características requeridas del sitio. | `["firing_facility"]` |

### `$.speciesGroupBindings[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 7/7 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"cereal"` |
| `name` | `object` | 7/7 | Nombre visible mediante claves de idioma. | `—` |
| `speciesTag` | `string` | 7/7 | Tag de categoría para agrupar especies candidatas. | `"cereal"` |
| `cultivationTechnologyId` | `string` | 7/7 | Referencia a la tecnología de cultivo utilizada por este grupo. | `"species_cultivation"` |

### `$.speciesGroupBindings[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 7/7 | Texto visible en inglés. | `"Cereals"` |
| `es` | `string` | 7/7 | Texto visible en español. | `"Cereales"` |

### `$.scopeExamples[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `technologyId` | `string` | 2/2 | Referencia a una definición tecnológica o importación externa declarada. | `"species_cultivation"` |
| `speciesId` | `string` | 2/2 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"wheat"` |

### `$.requiredRuntimeHandlers`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `conditionTypes` | `array<string>` | 1/1 | Nombres de manejadores de condiciones requeridos. | `["accessible_edible_plants", "accessible_land_available", "alternative_food_supply_available"]` |
| `eventTypes` | `array<string>` | 1/1 | Nombres de manejadores de eventos utilizados por eurekas. | `["compatible_crop_species_harvested", "crop_generation_completed", "crop_harvest_completed"]` |
| `effectTypes` | `array<string>` | 1/1 | Nombres de manejadores de efectos al completar. | `["unlock_capability"]` |
| `capabilityIds` | `array<string>` | 1/1 | Identificadores de capacidades desbloqueadas por tecnologías. | `["agricultural_drainage", "animal_drawn_plough", "basic_foraging"]` |

### `$.localization`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `format` | `string` | 1/1 | Formato de la copia fuente o de la representación de idiomas. | `"inline_language_map"` |
| `visibleFields` | `array<string>` | 1/1 | Campos que requieren valores por idioma. | `["name", "description"]` |
| `fallbackOrder` | `array<string>` | 1/1 | Secuencia de respaldo cuando falta traducción del idioma solicitado. | `["requested_language", "defaultLanguage", "id"]` |
| `missingValuePolicy` | `string` | 1/1 | Comportamiento cuando no existe traducción solicitada o predeterminada. | `"Treat an absent, empty or whitespace-only translation as missing."` |
| `identityPolicy` | `string` | 1/1 | El texto traducido no se utiliza como identidad o dependencia. | `"Never use translated text as an ID, dependency, event type or save key."` |
| `futureExtraction` | `string` | 1/1 | Plan para extraer después textos localizados a archivos de idioma. | `"Preserve stable IDs when moving translations to external language catalogs. Each field can later use a key such…` |
| `technicalTextPolicy` | `string` | 1/1 | Las cadenas técnicas permanecen en inglés y no son traducciones visibles. | `"designNotes, runtimeContract, balance notes and external reference notes are developer-facing English text, not…` |

### `$.name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 1/1 | Texto visible en inglés. | `"Agriculture"` |
| `es` | `string` | 1/1 | Texto visible en español. | `"Agricultura"` |

### `$.description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 1/1 | Texto visible en inglés. | `"Forage, cultivate and improve plant species through knowledge, equipment and local practice."` |
| `es` | `string` | 1/1 | Texto visible en español. | `"Recolecta, cultiva y mejora especies vegetales mediante conocimientos, equipos y prácticas locales."` |

### `$.technologies[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 23/23 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"basic_foraging"` |
| `name` | `object` | 23/23 | Nombre visible mediante claves de idioma. | `—` |
| `description` | `object` | 23/23 | Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico. | `—` |
| `scope` | `string` | 23/23 | Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto. | `"civilization"` |
| `prerequisites` | `object` | 23/23 | Expresión de dependencias tecnológicas evaluada antes de iniciar investigación. | `—` |
| `research` | `object` | 23/23 | Modo de adquisición, costo y reglas de inicio/continuación. | `—` |
| `usageConditions` | `object` | 23/23 | Requisitos operativos locales para usar capacidad desbloqueada. | `—` |
| `eurekas` | `array<object>` | 23/23 | Bonificaciones por eventos; vacío significa sin eureka configurada. | `[]` |
| `effects` | `array<object>` | 23/23 | Efectos al completar; el catálogo actual solo desbloquea capacidades. | `—` |
| `designNotes` | `array<string>` | 23/23 | Notas técnicas y detalles de diseño pendientes. | `[]` |
| `order` | `integer` | 23/23 | Posición de presentación; los requisitos explícitos determinan progreso. | `1` |

### `$.technologies[].name`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 23/23 | Texto visible en inglés. | `"Basic Foraging"` |
| `es` | `string` | 23/23 | Texto visible en español. | `"Recolección básica"` |

### `$.technologies[].description`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `en` | `string` | 23/23 | Texto visible en inglés. | `"Gather food from accessible edible wild plants."` |
| `es` | `string` | 23/23 | Texto visible en español. | `"Recoge alimentos de plantas silvestres comestibles accesibles."` |

### `$.technologies[].prerequisites`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 22/23 | Todas las expresiones deben cumplirse; una lista vacía equivale a true. | `[]` |
| `any` | `array<object>` | 1/23 | Al menos una expresión debe cumplirse; lista vacía inválida según contrato. | `—` |

### `$.technologies[].research`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `mode` | `string` | 23/23 | Modo de adquisición de investigación o de contador; depende del objeto. | `"initial_grant"` |
| `cost` | `integer` | 23/23 | Costo base en pointUnit, no cantidad fija de turnos. | `0` |
| `pointUnit` | `string` | 23/23 | Unidad del costo y avance de investigación. | `"research_point"` |
| `startConditions` | `object` | 23/23 | Condiciones para iniciar; no se repiten para continuar salvo declaración explícita. | `—` |
| `ongoingConditions` | `object` | 23/23 | Condiciones por turno activo; al fallar pausa conservando avance. | `—` |
| `onConditionFailure` | `string` | 23/23 | Política aplicada cuando fallan condiciones de continuación. | `"pause_keep_progress"` |

### `$.technologies[].research.startConditions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 23/23 | Todas las expresiones deben cumplirse; una lista vacía equivale a true. | `[]` |

### `$.technologies[].research.ongoingConditions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `all` | `array<?>` | 23/23 | Todas las expresiones deben cumplirse; una lista vacía equivale a true. | `[]` |

### `$.technologies[].usageConditions`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `all` | `array<object>` | 23/23 | Todas las expresiones deben cumplirse; una lista vacía equivale a true. | `—` |

### `$.technologies[].usageConditions.all[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 81/81 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"workers_assigned"` |
| `minimumCount` | `integer` | 23/81 | Cantidad mínima de trabajadores o entidades requerida por la condición. | `1` |
| `speciesId` | `string` | 29/81 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"$speciesId"` |
| `tag` | `string` | 9/81 | Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales. | `"gathering_tool"` |
| `location` | `string` | 9/81 | Contexto donde debe cumplirse disponibilidad, por ejemplo el sitio operativo. | `"site_equipment"` |
| `minimumAmount` | `integer` | 14/81 | Cantidad mínima de material disponible; no consumo automático. | `1` |
| `feature` | `string` | 5/81 | Identificador de característica requerida del sitio. | `"accessible_water_source"` |
| `minimumSpeciesCount` | `integer` | 1/81 | Cantidad mínima de especies compatibles distintas. | `2` |
| `minimumLineCount` | `integer` | 1/81 | Cantidad mínima de líneas agrícolas distintas. | `2` |
| `method` | `string` | 1/81 | Método de reproducción/uso requerido por la condición. | `"vegetative_propagation"` |

### `$.technologies[].effects[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 23/23 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"unlock_capability"` |
| `capabilityId` | `string` | 23/23 | Identificador de la capacidad desbloqueada. | `"basic_foraging"` |
| `scope` | `string` | 23/23 | Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto. | `"civilization"` |
| `activation` | `string` | 23/23 | Cuándo funciona la capacidad; siguen aplicando condiciones de uso. | `"while_usage_conditions_met"` |

### `$.technologies[].prerequisites.all[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 36/36 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"technology_completed"` |
| `technologyId` | `string` | 36/36 | Referencia a una definición tecnológica o importación externa declarada. | `"basic_foraging"` |
| `scope` | `string` | 36/36 | Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto. | `"civilization"` |

### `$.technologies[].research.startConditions.all[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 22/22 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"species_discovered"` |
| `speciesId` | `string` | 22/22 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"$speciesId"` |

### `$.technologies[].eurekas[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `id` | `string` | 22/22 | Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos. | `"plant_gathered"` |
| `eventType` | `string` | 22/22 | Tipo de evento del juego que debe coincidir. | `"plant_gathered"` |
| `filters` | `object` | 22/22 | Restricciones de eventos que pueden contribuir a una eureka. | `—` |
| `counter` | `object` | 22/22 | Modo de acumulación y umbral. | `—` |
| `reward` | `object` | 22/22 | Recompensa de puntos; no completa requisitos automáticamente. | `—` |
| `repeatable` | `boolean` | 22/22 | Indica repetición; false significa una vez por investigación e ID de eureka. | `false` |

### `$.technologies[].eurekas[].filters`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `speciesId` | `string` | 11/22 | Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización. | `"$speciesId"` |
| `itemTag` | `string` | 4/22 | Filtro de categoría de objeto en eventos de fabricación. | `"stone_gathering_tool"` |
| `siteFeature` | `string` | 2/22 | Filtro de evento por característica del sitio. | `"accessible_water_source"` |
| `resourceTag` | `string` | 1/22 | Tag en inglés de categoría del recurso; no es ID resuelto. | `"livestock_manure"` |
| `counterGroup` | `string` | 1/22 | Campo del evento que restringe acumulación a una entidad, por ejemplo una parcela. | `"plotId"` |

### `$.technologies[].eurekas[].counter`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `mode` | `string` | 22/22 | Modo de adquisición de investigación o de contador; depende del objeto. | `"sum_amount"` |
| `target` | `integer` | 22/22 | Umbral del contador en la unidad del evento. | `20` |

### `$.technologies[].eurekas[].reward`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 22/22 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"add_research_points"` |
| `fractionOfBaseCost` | `number` | 22/22 | Fracción del costo base tecnológico concedida como puntos. | `0.25` |

### `$.technologies[].prerequisites.any[]`

| Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra |
| --- | --- | --- | --- | --- |
| `type` | `string` | 3/3 | Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas. | `"technology_completed"` |
| `technologyId` | `string` | 3/3 | Referencia a una definición tecnológica o importación externa declarada. | `"basketry"` |
| `scope` | `string` | 3/3 | Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto. | `"civilization"` |

## Ejemplo de documento completo con arreglos repetidos reducidos

JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.

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

## Variantes de condiciones y eurekas

Son ejemplos exactos de condiciones/filtros del archivo actual. Cada `type` admite campos distintos; la tabla de unión anterior no permite combinaciones arbitrarias. Se muestran todos los tipos de condición y evento de eureka configurados.

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
