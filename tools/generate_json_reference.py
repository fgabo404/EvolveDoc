"""Generate exhaustive bilingual documentation from the current JSON snapshots.

Tables describe observed structure, not inferred requiredness or final schemas.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Each entry explains an actual property; executable conditions and final schemas remain separate.
TEXT = r'''
schemaVersion|Version of the structural contract, not the game's release.|Versión del contrato estructural, no del lanzamiento del juego.
contentVersion|Version of the catalog content and provisional balance.|Versión del contenido del catálogo y del balance provisional.
kind|Discriminator identifying this document or candidate category.|Discriminador que identifica el documento o categoría del candidato.
status|Maturity, review state or current example research status; read the containing object.|Madurez, revisión o estado de investigación del ejemplo; depende del objeto contenedor.
defaultLanguage|Default language for visible-text fallback.|Idioma predeterminado para el texto visible.
supportedLanguages|Language codes available in this document.|Códigos de idioma disponibles.
runtimePolicy|Rules and restrictions for interpreting this guide.|Reglas y restricciones para interpretar esta guía.
loadAsGameDefinitions|False blocks promotion of this guide to playable definitions.|False impide tratar esta guía como definiciones jugables.
unknownValues|Explains that unresolved null values are not zero or unrestricted.|Aclara que null pendiente no equivale a cero o sin restricciones.
id|Stable identity of this definition or fixture civilization; never use a translated name as identity.|Identidad estable de la definición o civilización del ejemplo; nunca usar nombres traducidos.
name|Player-visible label using language keys.|Nombre visible mediante claves de idioma.
description|Explanation; in game definitions visible descriptions are language maps, while schema descriptions are developer text.|Explicación; en definiciones visibles es un mapa de idiomas y en esquemas es texto técnico.
en|English visible text.|Texto visible en inglés.
es|Spanish visible text.|Texto visible en español.
speciesCandidates|Flat candidate records; broad groups are not yet accepted exact species.|Candidatos al mismo nivel; los grupos generales todavía no son especies exactas aceptadas.
agriculturalCropCandidates|Crop groups awaiting exact species, ancestors and production definitions.|Grupos agrícolas pendientes de especie exacta, ancestros y producción.
geologicalResourceCandidates|Source materials and geological forms awaiting deposit and processing design.|Materiales y formas geológicas pendientes de yacimientos y procesamiento.
taxonomy|Scientific identity, evidence and review information.|Identidad científica, evidencia y revisión.
scientificName|Scientific name only when provided by the source; null means unresolved and does not identify a taxon.|Nombre científico si aparece en la fuente; null significa pendiente y no identifica un taxón.
nameEvidence|Evidence supporting the recorded scientific name or its absence.|Evidencia del nombre científico registrado o de su ausencia.
resolutionStatus|Task still required to resolve a candidate or regional restriction.|Tarea pendiente para resolver el candidato o restricción regional.
verified|Whether scientific verification has been performed; current candidates are not verified.|Indica si existe verificación científica; los candidatos actuales no están verificados.
definitionStatus|Readiness of this record; source candidates are not runtime definitions.|Madurez del registro; los candidatos no son definiciones ejecutables.
nativeRegionIds|References to native regions; empty means unresolved, not worldwide distribution.|Referencias a regiones nativas; vacío significa pendiente, no distribución mundial.
biomeVariantIds|References to regional variants listing this candidate.|Referencias a variantes regionales que enumeran este candidato.
ecology|Environmental requirements; quantitative values remain unresolved.|Requisitos ambientales; los valores cuantitativos están pendientes.
temperatureRangeC|Temperature bounds in degrees Celsius; null has no finalized inner structure.|Límites de temperatura en grados Celsius; null todavía no tiene estructura interna definida.
moistureRange|Moisture bounds; units and structure remain unresolved.|Límites de humedad; unidades y estructura pendientes.
elevationRangeM|Elevation bounds in meters; values and structure remain unresolved.|Límites de elevación en metros; valores y estructura pendientes.
waterRequirements|Species water requirements; unresolved, not absence of a requirement.|Necesidades de agua; pendiente no significa que no necesite agua.
soilRequirements|Species soil constraints, awaiting a structured definition.|Restricciones de suelo pendientes de estructura.
habitatRestrictionsStatus|Developer explanation of unresolved habitat restrictions.|Explicación técnica sobre restricciones de hábitat pendientes.
propagation|Reproduction/propagation methods and required materials, still under design.|Métodos de reproducción y materiales requeridos, todavía en diseño.
methods|Supported propagation methods; null is unresolved.|Métodos de reproducción admitidos; null significa pendiente.
materialResourceIds|References to propagation resources; null means unresolved links.|Referencias a recursos de reproducción; null significa relaciones pendientes.
domestication|Eligibility, ancestor/form relationships and selection criteria.|Elegibilidad, relaciones con ancestros/formas y criterios de selección.
eligibility|Whether and under what review a candidate may use this mechanism.|Elegibilidad del candidato para este mecanismo y revisión necesaria.
wildAncestorId|Reference to the selected wild ancestor, not automatically inferred.|Referencia al ancestro silvestre elegido, sin deducirlo automáticamente.
domesticatedFormId|Reference to a domesticated form; does not grant instant domestication.|Referencia a la forma domesticada; no concede domesticación instantánea.
criteria|Domestication criteria, not yet modeled.|Criterios de domesticación todavía no modelados.
potentialProducts|Potential source uses; not confirmed outputs, quantities or unlocks.|Usos potenciales de la fuente; no son productos, cantidades o desbloqueos confirmados.
requiredTechnologyIds|Technology references needed for this output; null means unresolved, not none.|Referencias tecnológicas del producto; null significa pendiente, no ningún requisito.
yield|Output yield; units, formula and amount remain unresolved.|Rendimiento; unidad, fórmula y cantidad pendientes.
potentialUseMethods|Potential source use methods, not authorized gameplay actions.|Métodos de uso potenciales de la fuente, no acciones ya autorizadas del juego.
cultivationResearch|Illustrative link to per-species research; null means no binding specified.|Relación ilustrativa con investigación por especie; null indica vínculo no definido.
technologyId|Reference to a technology definition or declared external import.|Referencia a una definición tecnológica o importación externa declarada.
speciesId|Species/crop binding; $speciesId resolves from the current research instance; null denotes civilization scope.|Vínculo de especie/cultivo; $speciesId se resuelve desde la investigación actual; null indica ámbito de civilización.
sourceLabel|Exact Spanish source label for provenance, not a localized UI field.|Etiqueta original en español para trazabilidad, no texto localizado de interfaz.
initialPresencePolicy|Constraints to resolve before initial spawning.|Restricciones que deben resolverse antes de la aparición inicial.
cropUseTag|Gameplay crop-use group, not a botanical species.|Grupo de uso agrícola del juego, no especie botánica.
sourceOriginHint|Source geographic origin hint; not a verified native-range rule.|Indicación de origen de la fuente, no una regla verificada de distribución nativa.
wildAncestorCandidateIds|Possible ancestor links pending scientific review.|Posibles ancestros pendientes de revisión científica.
products|Crop outputs awaiting resource definitions and recipes.|Productos agrícolas pendientes de recursos y recetas.
ecologicalConstraints|Crop environmental rules awaiting formalization.|Reglas ambientales del cultivo pendientes de formalización.
sourceSection|Source section from which this entry was extracted.|Sección de la fuente de la que se extrajo la entrada.
geologyConstraints|Geological requirements pending formalization; biome alone is insufficient.|Requisitos geológicos pendientes; el bioma por sí solo no basta.
refinedOutputResourceId|Reference to a processed resource; extraction does not directly grant refined metal.|Referencia al recurso procesado; extraer no concede metal refinado directamente.
surfaceAndOreDistinction|Rule distinguishing surface material, ore and processed output.|Regla que distingue material superficial, mena y producto procesado.
source|Provenance of the supplied document snapshot.|Procedencia de la copia del documento original.
title|Document or schema title.|Título del documento o esquema.
format|Format of the source snapshot or localization representation.|Formato de la copia fuente o de la representación de idiomas.
connectorFileId|Exact source connector identifier, retained for provenance.|Identificador exacto de la fuente en el conector, conservado para trazabilidad.
sha256|SHA-256 fingerprint of the source document snapshot.|Huella SHA-256 de la copia del documento fuente.
snapshotOnly|True means extraction used the attached snapshot, not a live revision check.|True indica extracción de la copia adjunta, sin verificar una revisión en vivo.
originalDocumentModified|Whether conversion modified the original source document; false here.|Indica si se modificó el documento fuente; aquí es false.
reason|Explanation of the runtime restriction.|Explicación de la restricción de ejecución.
visibleText|Policy distinguishing localized visible text from raw source provenance.|Política que distingue texto visible traducido y procedencia original.
flatCollections|Policy requiring flat collections linked by IDs.|Política de colecciones al mismo nivel relacionadas mediante IDs.
preserveSpeciesResearch|Rule preserving research identity when taxonomy is refined.|Regla para conservar identidad de investigación al precisar taxonomía.
wildAndDomestic|Rule separating wild presence, cultivation, domestication and production.|Regla que separa presencia silvestre, cultivo, domesticación y producción.
distribution|Rule requiring verified native regions and habitats for spawning.|Regla que exige regiones nativas y hábitats verificados para aparición.
geology|Rule controlling mineral placement independently from biome labels.|Regla que controla minerales independientemente de etiquetas de bioma.
miningStages|Interpretation of extraction methods without inventing exclusive eras.|Interpretación de métodos de extracción sin inventar épocas exclusivas.
scope|Research/effect scope, or a descriptive boundary in runtimePolicy; read the containing object.|Ámbito de investigación/efecto o límite descriptivo de runtimePolicy; depende del objeto.
worldRules|High-level world-generation decisions.|Decisiones generales de generación del mundo.
hexagonalMap|Whether the map uses hexagonal tiles.|Indica si el mapa utiliza casillas hexagonales.
dynamicWeatherEnabled|Whether dynamic weather is included; currently false.|Indica si incluye tiempo atmosférico dinámico; actualmente false.
seasonsEnabled|Whether seasons are included; currently false.|Indica si incluye estaciones; actualmente false.
dynamicClimateDisastersEnabled|Whether dynamic climate disasters are included; currently false.|Indica si incluye desastres climáticos dinámicos; actualmente false.
staticEnvironmentalConditionsUsed|Whether static environmental conditions constrain generation.|Indica si condiciones ambientales estáticas restringen la generación.
maximumRegionalVariantsPerBiome|Current maximum regional variants per biome, not a spawn probability.|Máximo actual de variantes regionales por bioma, no probabilidad de aparición.
resourceDiscoverySeparateFromExistence|Resources may exist before a civilization discovers them.|Los recursos pueden existir antes de que una civilización los descubra.
potentialCultivationSeparateFromEstablishedCrops|Cultivability does not imply an already established crop.|Poder cultivar no implica que ya exista un cultivo establecido.
elevationLevels|Elevation categories independent of biome.|Categorías de elevación independientes del bioma.
ordinaryLandTraversal|Passability flag or explanatory restriction; currently boolean or string.|Transitabilidad o restricción explicativa; actualmente booleano o texto.
conventionalSettlementsAllowed|Whether conventional settlements are permitted at this level.|Indica si permite asentamientos convencionales en este nivel.
movementAndConstructionRestrictions|Explanatory movement and construction restrictions.|Restricciones explicativas de movimiento y construcción.
geographicModifiers|Geographic feature categories affecting habitat and access.|Categorías geográficas que influyen en hábitat y acceso.
biomes|Interface biome categories, not sufficient ecological placement rules.|Categorías de bioma de interfaz; no bastan para decidir apariciones.
interfaceCategoryOnly|True means this biome label is a UI category rather than a complete habitat definition.|True indica categoría de interfaz, no definición completa de hábitat.
regionalVariants|Regional/habitat variants linked to their parent biome.|Variantes regionales/de hábitat relacionadas con su bioma.
biomeId|Reference to a biome definition.|Referencia a la definición de bioma.
resourceOccurrences|Individual source listings linked to candidates, variants and extraction methods.|Apariciones de la fuente relacionadas con candidatos, variantes y métodos de extracción.
definitionId|Reference to the candidate definition; not an individual world population ID.|Referencia a la definición candidata, no al ID de una población generada.
variantId|Reference to a regional variant.|Referencia a una variante regional.
extractionMethodId|Extraction-stage identifier from the source; not a verified recipe.|Identificador de etapa de extracción de la fuente, no una receta verificada.
sourceText|Exact Spanish source occurrence text; preserve for audit, not game UI.|Texto original en español de la aparición; se conserva para auditoría, no para interfaz.
constraintsStatus|Progress in converting qualitative source restrictions into executable conditions.|Avance al convertir restricciones cualitativas en condiciones ejecutables.
spawnProbability|Spawn probability, currently unresolved; null is not zero or guaranteed.|Probabilidad de aparición pendiente; null no es cero ni aparición segura.
guaranteedPresence|Whether this record guarantees presence; false does not imply impossibility.|Indica presencia garantizada; false no implica imposibilidad.
runtimeEnabled|Whether this occurrence may be used by generation; currently false.|Indica si la aparición puede usarse en generación; actualmente false.
generationPipeline|Ordered design steps, not executable generator code.|Pasos ordenados de diseño, no código ejecutable del generador.
speciesCompletionChecklist|Review tasks before promoting a candidate to an approved definition.|Tareas de revisión antes de aprobar una definición candidata.
reviewIssues|Recorded source discrepancies and unresolved design questions.|Contradicciones de la fuente y preguntas de diseño pendientes.
sourceClaim|Count claimed by the source; compare with actualCount.|Conteo declarado por la fuente; comparar con actualCount.
actualCount|Count obtained from the enumerated source records.|Conteo obtenido de los registros enumerados.
resolution|Documented interpretation or next review action.|Interpretación documentada o siguiente acción de revisión.
sourceDistributionNotes|Verbatim source distribution notes, not extra species.|Notas originales de distribución, no especies adicionales.
agricultureSectionSource|Verbatim source agriculture section retained for provenance.|Sección agrícola original conservada para trazabilidad.
summary|Counts used to check catalog completeness.|Conteos para comprobar integridad de los catálogos.
biomeCount|Number of biome records.|Cantidad de biomas.
regionalVariantCount|Number of regional variants.|Cantidad de variantes regionales.
plantCandidateCount|Number of regional plant candidate records.|Cantidad de candidatos vegetales regionales.
animalCandidateCount|Number of animal candidate records.|Cantidad de candidatos animales.
geologicalCandidateCount|Number of geological candidate records.|Cantidad de candidatos geológicos.
sourceOccurrenceCount|Number of source occurrence records.|Cantidad de apariciones de la fuente.
agriculturalCropCandidateCount|Number of crop candidate records.|Cantidad de candidatos agrícolas.
hexDefinitionGuide|Proposed tile field names and state separation; not an implemented tile schema.|Nombres propuestos de campos de casilla y separación de estado; no es esquema implementado.
definitionFields|Names of proposed static fields; these strings are not actual nested properties.|Nombres propuestos de campos estáticos; estas cadenas no son propiedades anidadas reales.
stateFields|Names of proposed mutable instance fields; types are still pending.|Nombres propuestos de campos mutables de instancia; tipos pendientes.
numericRanges|Numerical ranges awaiting design.|Rangos numéricos pendientes de diseño.
separation|Explains the boundary between reusable definitions and generated map state.|Explica la separación entre definiciones reutilizables y estado del mapa generado.
depositDefinitionGuide|Proposed deposit fields; not a completed deposit definition.|Campos propuestos de yacimiento; no es una definición terminada.
fields|Names of proposed fields, not instantiated records.|Nombres de campos propuestos, no registros ya instanciados.
numericalValues|Numerical deposit parameters awaiting design.|Parámetros numéricos del yacimiento pendientes.
depletionAndRegenerationRules|Rules for reserve depletion and renewal, still unresolved.|Reglas de agotamiento y renovación de reservas pendientes.
stateSeparation|Explains why reserves and discovery belong to game state.|Explica por qué reservas y descubrimiento pertenecen a la partida.
catalogFiles|Sibling catalog locations resolved relative to the world-guide JSON file.|Ubicaciones de catálogos relacionados, relativas al JSON guía del mundo.
plantCandidates|Relative path to the plant and crop guide.|Ruta relativa a la guía de plantas y cultivos.
animalCandidates|Relative path to the animal guide.|Ruta relativa a la guía de animales.
geologicalCandidates|Relative path to the geological guide.|Ruta relativa a la guía geológica.
repositoryPackaging|Metadata describing the split from the combined guide.|Metadatos de separación de la guía combinada.
layout|Packaging strategy: flat linked catalogs.|Organización: catálogos al mismo nivel relacionados por IDs.
change|Description of the packaging change.|Descripción del cambio de organización.
balance|Provisional research costs and eureka balance.|Costos provisionales de investigación y balance de eurekas.
defaultResearchCost|Default prototype cost measured in research points.|Costo predeterminado del prototipo en puntos de investigación.
defaultEurekaFraction|Default share of base cost granted by a eureka.|Fracción predeterminada del costo base concedida por eureka.
note|Developer clarification; not localized UI text.|Aclaración técnica; no es texto traducido de interfaz.
runtimeContract|Contract the future evaluator must implement; descriptive strings are not executable code.|Contrato que implementará el evaluador; las cadenas descriptivas no son código ejecutable.
definitionDataIsReadOnly|Definitions must not be modified during simulation.|Las definiciones no cambian durante la simulación.
saveStateStoredSeparately|Mutable progress belongs in a separate game state.|El avance mutable pertenece a un estado de partida separado.
conditionGrammar|Grammar for all/any groups and typed condition leaves.|Gramática para grupos all/any y condiciones con tipo.
prerequisiteScope|Meaning of civilization/current-species/any-species prerequisite resolution.|Significado de requisitos de civilización, especie actual o cualquier especie.
civilization|Shared civilization research instance, not one instance per species.|Investigación compartida de civilización, no una por especie.
current_species|Resolve the prerequisite for the current research species.|Resolver el requisito para la especie de la investigación actual.
any_species|At least one species instance must satisfy the prerequisite.|Al menos una especie debe cumplir el requisito.
researchInstanceKey|Fields identifying one independent research instance.|Campos que identifican una investigación independiente.
speciesIdRule|How species binding is required or null according to scope.|Cómo vincular especie o usar null según el ámbito.
researchStartAndContinuation|When to evaluate prerequisites, start conditions and ongoing conditions.|Cuándo evaluar requisitos, inicio y continuación.
resourceRule|Availability checks do not consume inventory; actions and recipes define consumption.|Comprobar disponibilidad no consume inventario; el consumo corresponde a acciones y recetas.
eurekaPolicy|Tracking, reward, grouping and deduplication policy for eurekas.|Política de seguimiento, recompensa, agrupación y deduplicación de eurekas.
historyWindow|How far back gameplay event history is tracked.|Desde cuándo se considera el historial de eventos.
trackedBeforeResearchAvailable|Whether eureka events are tracked while research remains locked.|Indica si registra eventos de eureka antes de habilitar investigación.
eventOwner|Field identifying the civilization that owns an event.|Campo que identifica a la civilización propietaria del evento.
speciesFilter|Rule binding eureka history to the current species when applicable.|Regla que vincula el historial de eureka con la especie actual.
counterUnit|Event amount semantics; occurrence events contribute one.|Significado de la cantidad del evento; las ocurrencias aportan uno.
grouping|Restricts counting to the same matching entity rather than summing different groups.|Restringe el conteo a una entidad coincidente en vez de sumar grupos distintos.
distinctCounters|Special counters requiring distinct species or lines; not yet fully normalized in configuration.|Contadores especiales de especies o líneas distintas; configuración todavía no normalizada.
compatible_crop_species_harvested|Count distinct compatible species, not repeated harvest events.|Contar especies compatibles distintas, no cosechas repetidas.
separate_crop_line_harvest_completed|Count distinct lines within the current species.|Contar líneas distintas dentro de la especie actual.
rewardTiming|When an eligible eureka may grant its reward.|Cuándo una eureka elegible puede entregar recompensa.
rewardRounding|Formula rounding eureka points down from base cost.|Fórmula que redondea hacia abajo puntos de eureka a partir del costo base.
progressLimit|Cap progress at cost without bypassing prerequisites.|Limitar avance al costo sin omitir requisitos.
deduplication|Event IDs and claimed rewards prevent duplicate credit.|Los IDs de evento y recompensas reclamadas evitan duplicación.
effectRule|Completion unlocks capabilities; use still checks operational conditions.|Completar desbloquea capacidades; utilizarlas requiere condiciones operativas.
unsupportedRulePolicy|Reject unknown rule types and unresolved references.|Rechazar tipos desconocidos y referencias pendientes.
integrationStatus|Implementation boundary of the configuration contract.|Límite de implementación del contrato de configuración.
orderMeaning|Order affects display only, never implicit research dependencies.|Order solo ordena presentación, no crea requisitos implícitos.
externalReferences|Imports another catalog must provide before a full simulation.|Importaciones que otro catálogo debe resolver antes de una simulación completa.
technologyIds|Technology identifiers imported from external branches.|Identificadores tecnológicos importados de otras ramas.
requiredCatalogs|Catalog kinds the complete loader must resolve.|Tipos de catálogo que deberá resolver el cargador completo.
manufacturingAlternatives|Container-making techniques and material tags; not full crafting recipes.|Técnicas de recipientes y tags de materiales; no son recetas completas.
inputTags|Material categories required by this manufacturing alternative.|Categorías de material requeridas por esta alternativa.
outputTag|Category of item produced by the alternative.|Categoría del objeto producido por la alternativa.
speciesGroupBindings|Crop-use categories linked to the shared cultivation technology.|Categorías de uso agrícola vinculadas a la tecnología común de cultivo.
speciesTag|Category tag used to group candidate species.|Tag de categoría para agrupar especies candidatas.
cultivationTechnologyId|Reference to the cultivation technology used by this group.|Referencia a la tecnología de cultivo utilizada por este grupo.
scopeExamples|Illustrative technology/species bindings, not saved progress.|Vínculos ilustrativos de tecnología/especie, no avance guardado.
designNotes|Developer notes and unresolved design details.|Notas técnicas y detalles de diseño pendientes.
requiredRuntimeHandlers|Condition, event, effect and capability types needed by the full evaluator.|Tipos de condición, evento, efecto y capacidad requeridos por el evaluador completo.
conditionTypes|Names of condition handlers required by the catalog.|Nombres de manejadores de condiciones requeridos.
eventTypes|Names of gameplay event handlers required by eurekas.|Nombres de manejadores de eventos utilizados por eurekas.
effectTypes|Names of supported completion-effect handlers.|Nombres de manejadores de efectos al completar.
capabilityIds|Capability identifiers unlocked by the technology catalog.|Identificadores de capacidades desbloqueadas por tecnologías.
localization|Representation and fallback rules for visible text.|Representación y reglas de respaldo del texto visible.
visibleFields|Fields that require language-map values.|Campos que requieren valores por idioma.
fallbackOrder|Fallback sequence when requested-language text is missing.|Secuencia de respaldo cuando falta traducción del idioma solicitado.
missingValuePolicy|Behavior when no requested/default translation exists.|Comportamiento cuando no existe traducción solicitada o predeterminada.
technicalTextPolicy|Technical strings remain English and are not player-facing translations.|Las cadenas técnicas permanecen en inglés y no son traducciones visibles.
futureExtraction|Plan to move inline localized text into separate language files later.|Plan para extraer después textos localizados a archivos de idioma.
identityPolicy|Localized text must not be used as identity or dependency.|El texto traducido no se utiliza como identidad o dependencia.
technologies|Flat list of peer technology definitions; no nested levels or nodes.|Lista de tecnologías al mismo nivel; sin niveles ni nodos anidados.
order|Presentation position; explicit prerequisites determine actual progression.|Posición de presentación; los requisitos explícitos determinan progreso.
prerequisites|Technology dependency expression evaluated before research can start.|Expresión de dependencias tecnológicas evaluada antes de iniciar investigación.
all|All child expressions must pass; an empty list evaluates true.|Todas las expresiones deben cumplirse; una lista vacía equivale a true.
any|At least one expression must pass; an empty list is invalid in the contract.|Al menos una expresión debe cumplirse; lista vacía inválida según contrato.
type|Condition/reward/effect discriminator, or JSON Schema type in schema documents.|Discriminador de condición/recompensa/efecto, o tipo JSON Schema en esquemas.
research|Acquisition mode, cost and research start/continuation rules.|Modo de adquisición, costo y reglas de inicio/continuación.
mode|Research acquisition mode or eureka counter mode; read the containing object.|Modo de adquisición de investigación o de contador; depende del objeto.
cost|Base research cost in pointUnit, not a fixed number of turns.|Costo base en pointUnit, no cantidad fija de turnos.
pointUnit|Unit used by research cost and progress.|Unidad del costo y avance de investigación.
startConditions|Conditions required to start research; not repeated as ongoing requirements unless explicitly listed.|Condiciones para iniciar; no se repiten para continuar salvo declaración explícita.
ongoingConditions|Conditions checked each active turn; failure pauses and retains progress.|Condiciones por turno activo; al fallar pausa conservando avance.
onConditionFailure|Policy applied when ongoing conditions fail.|Política aplicada cuando fallan condiciones de continuación.
usageConditions|Local operational requirements for using an unlocked capability.|Requisitos operativos locales para usar capacidad desbloqueada.
eurekas|Event-driven research boosts; empty means no configured boost.|Bonificaciones por eventos; vacío significa sin eureka configurada.
eventType|Gameplay event type to match.|Tipo de evento del juego que debe coincidir.
filters|Constraints restricting which events contribute to a eureka.|Restricciones de eventos que pueden contribuir a una eureka.
counter|Accumulation mode and threshold.|Modo de acumulación y umbral.
target|Counter threshold in the event's counting unit.|Umbral del contador en la unidad del evento.
reward|Research-point reward, not automatic prerequisite completion.|Recompensa de puntos; no completa requisitos automáticamente.
fractionOfBaseCost|Fraction of the technology's base research cost granted as points.|Fracción del costo base tecnológico concedida como puntos.
repeatable|Whether the eureka can grant again; false means once per research instance and eureka ID.|Indica repetición; false significa una vez por investigación e ID de eureka.
effects|Completion effects; current catalog only unlocks capabilities.|Efectos al completar; el catálogo actual solo desbloquea capacidades.
capabilityId|Identifier of the capability unlocked by this effect.|Identificador de la capacidad desbloqueada.
activation|When the capability is operational; usage conditions still apply.|Cuándo funciona la capacidad; siguen aplicando condiciones de uso.
minimumCount|Minimum number of workers or entities required by the typed condition.|Cantidad mínima de trabajadores o entidades requerida por la condición.
minimumAmount|Minimum accessible material quantity; not an automatic consumption amount.|Cantidad mínima de material disponible; no consumo automático.
minimumLineCount|Minimum number of distinct crop lines.|Cantidad mínima de líneas agrícolas distintas.
minimumSpeciesCount|Minimum number of distinct compatible species.|Cantidad mínima de especies compatibles distintas.
resourceTag|English resource-category tag; not a resolved resource ID.|Tag en inglés de categoría del recurso; no es ID resuelto.
method|Propagation/use method required by the typed condition.|Método de reproducción/uso requerido por la condición.
feature|Required site feature identifier.|Identificador de característica requerida del sitio.
siteFeature|Site-feature event filter.|Filtro de evento por característica del sitio.
siteFeatures|Required set of site features.|Conjunto de características requeridas del sitio.
equipmentTags|Equipment categories required at the operating site.|Categorías de equipo requeridas en el sitio operativo.
location|Context in which an availability condition must be satisfied, such as the operating site.|Contexto donde debe cumplirse disponibilidad, por ejemplo el sitio operativo.
itemTag|Item-category filter for crafting events.|Filtro de categoría de objeto en eventos de fabricación.
counterGroup|Event field used to restrict accumulation to one entity, e.g. one plot.|Campo del evento que restringe acumulación a una entidad, por ejemplo una parcela.
turn|Current mutable game turn; zero is the fixture's initial state.|Turno mutable actual; cero es el estado inicial del ejemplo.
speciesBindings|Explanations of fixture aliases, not botanical definitions.|Explicaciones de alias del ejemplo, no definiciones botánicas.
wheat|Illustrative wheat crop-group alias, not a resolved exact species.|Alias ilustrativo del grupo trigo, no especie exacta resuelta.
maize|Illustrative maize crop-group alias, not a resolved exact species.|Alias ilustrativo del grupo maíz, no especie exacta resuelta.
civilizations|Independent civilization state records in this example.|Estados independientes de civilizaciones del ejemplo.
discoveredSpeciesIds|Species/crop aliases already discovered by this civilization.|Alias de especies/cultivos descubiertos por esta civilización.
accessibleMaterialSpeciesIds|Species/crop aliases with material accessible to this civilization.|Alias de especies/cultivos con material accesible a esta civilización.
started|Whether research has passed its initial gates and begun.|Indica si pasó condiciones iniciales y comenzó investigación.
completed|Whether the research instance reached its defined cost.|Indica si la investigación alcanzó su costo definido.
points|Accumulated mutable research points, capped at the definition cost.|Puntos mutables acumulados, limitados al costo de la definición.
pointsPerTurn|Fixture allocation per research attempt; no civilization-wide budget allocator is implemented.|Asignación del ejemplo por intento; no implementa presupuesto científico total.
$schema|JSON Schema dialect URI; not a reference to game data.|URI del dialecto JSON Schema; no referencia a datos del juego.
required|Property names required by this schema; presence in an example alone does not make a field required.|Propiedades obligatorias según esquema; aparecer en un ejemplo no vuelve obligatorio un campo.
properties|Schemas for named properties; does not forbid other fields without additionalProperties.|Esquemas por propiedad; no prohíbe campos extra sin additionalProperties.
items|Schema applied to array elements.|Esquema aplicado a elementos de un arreglo.
const|Exact allowed JSON value for the property.|Valor JSON exacto admitido para la propiedad.
pattern|Regular expression constraining strings; not a global uniqueness guarantee.|Expresión regular para cadenas; no garantiza unicidad global.
not|Subschema that must not validate; rejects the reserved zero ID here.|Subesquema que no debe cumplirse; aquí rechaza ID cero reservado.
tag|English snake_case technical label; future IDs and tags are not yet applied to legacy catalogs.|Etiqueta técnica en inglés snake_case; IDs y tags futuros aún no aplicados a catálogos actuales.
resources|Resource records at the root, or the relative resource-catalog path inside catalogFiles.|Registros de recursos en la raíz, o ruta relativa al catálogo dentro de catalogFiles.
sourceBindings|Possible source-to-resource links; never automatic production or a complete acquisition recipe.|Posibles vínculos de origen a recurso; nunca producción automática ni receta completa.
processingLinks|Proposed transformation endpoints; additional inputs and actual recipes are still unresolved.|Extremos propuestos de transformación; insumos adicionales y recetas reales pendientes.
sourceTagMappings|Explicit mappings of existing animal-product tags; services and ambiguous anatomy remain separate.|Equivalencias explícitas de tags animales; servicios y anatomía ambigua permanecen separados.
unresolvedSources|Resources whose exact acquisition source or subsystem remains undefined.|Recursos cuyo origen exacto o sistema de obtención está pendiente.
resourceCount|Number of resource definitions.|Cantidad de definiciones de recursos.
sourceBindingCount|Number of possible source-to-resource relations.|Cantidad de relaciones posibles de origen a recurso.
processingLinkCount|Number of proposed transformation guides.|Cantidad de guías propuestas de transformación.
sourceTagMappingCount|Number of original animal tags explicitly classified or mapped.|Cantidad de tags animales originales clasificados o vinculados.
geologicalSourceCount|Number of geological candidates with material mappings.|Cantidad de candidatos geológicos vinculados con materiales.
cropSourceCount|Number of agricultural candidates with proposed products.|Cantidad de candidatos agrícolas con productos propuestos.
resourceId|Reference to a resource definition, distinct from a species or deposit ID.|Referencia a un recurso, distinta del ID de especie o yacimiento.
extractedResourceId|Material obtained through a future acquisition action; never an automatic refined metal output.|Material obtenido mediante futura acción; nunca metal refinado automático.
category|English resource category used for organizing the catalog.|Categoría del recurso en inglés para organizar el catálogo.
stage|Material stage: raw, intermediate, processed or refined; does not encode a numeric technology level.|Estado del material: raw, intermediate, processed o refined; no es nivel tecnológico numérico.
tags|English classification tags; compatibility and substitution still require explicit action rules.|Tags de clasificación en inglés; compatibilidad y sustitución requieren reglas explícitas.
inventory|Inventory eligibility and unresolved storage metadata, not current stock amounts.|Elegibilidad para inventario y almacenamiento pendiente, no existencias actuales.
storable|True identifies a material eligible for inventory; services are excluded.|True identifica un material apto para inventario; excluye servicios.
quantityUnit|Inventory measurement unit; null means the unit is not yet chosen.|Unidad de medida de inventario; null indica unidad pendiente.
perishable|Whether deterioration applies; null means unresolved, not nonperishable.|Indica deterioro; null significa pendiente, no imperecedero.
storageRules|Storage requirements and deterioration rules, still undefined.|Requisitos de almacenamiento y deterioro pendientes.
sourceCollection|Symbolic collection key resolving to plants, animals, crops or geology; not a resource ID.|Clave de colección para plantas, animales, cultivos o geología; no es ID de recurso.
sourceId|Existing source candidate ID, preserved without migrating its identity.|ID actual del candidato de origen, conservado sin migración.
acquisitionTag|Descriptive acquisition guide tag; not an implemented action or recipe ID.|Tag descriptivo de obtención; no es ID de acción o receta implementada.
reviewStatus|Review still required before a source output is authorized.|Revisión pendiente antes de autorizar un producto del origen.
quantityPerAction|Output per action, still unresolved; not zero or guaranteed yield.|Cantidad por acción pendiente; no significa cero ni rendimiento garantizado.
requiresProcessing|True means this source relation includes further processing; it is not a direct harvesting output.|True indica procesamiento posterior en la relación; no es producto directo de recolección.
sourceTag|Original animal-product or service tag retained for traceability.|Tag original de producto animal o servicio conservado para trazabilidad.
targetKind|Whether the original tag represents a resource, service or unresolved anatomical alternative.|Indica si el tag representa recurso, servicio o alternativa anatómica pendiente.
resourceIds|Explicit linked resource IDs; empty for services or unresolved alternatives.|IDs de recursos vinculados; vacío para servicios o alternativas pendientes.
processTag|Unique technical name of a proposed transformation guide; not a recipe implementation.|Nombre técnico único de guía de transformación; no es receta implementada.
inputResourceIds|Resource endpoints entering the guide; this is not a complete list of required recipe inputs.|Recursos de entrada de la guía; no son una lista completa de insumos de receta.
outputResourceIds|Resource endpoints produced after the still-undefined process, not automatic outputs.|Recursos finales del proceso pendiente, no productos automáticos.
inputQuantities|Input amounts still undefined; stoichiometry and recipe balance are not supplied.|Cantidades de entrada pendientes; no define estequiometría ni balance de receta.
outputQuantities|Output amounts and recovery still undefined.|Cantidades de salida y recuperación pendientes.
facilities|Required facilities and equipment, still undefined.|Instalaciones y equipo requeridos pendientes.
byproducts|Secondary outputs, residues and losses, still undefined.|Productos secundarios, residuos y pérdidas pendientes.
recipeId|Future recipe reference; null means this guide is not an executable recipe.|Referencia futura de receta; null indica que la guía no es receta ejecutable.
services|Policy excluding work, draft and transport services from stored inventory.|Política que excluye trabajo, tracción y transporte del inventario.
provenance|Keep species, original material, viability and quality in future inventory lots.|Conservar especie, material original, viabilidad y calidad en futuros lotes.
$defs|Named reusable subschemas within this JSON Schema document.|Subesquemas reutilizables con nombre dentro de este esquema.
$ref|Reference to a reusable subschema, not a game entity reference.|Referencia a un subesquema reutilizable, no a una entidad del juego.
additionalProperties|Whether properties not declared by the object schema are allowed.|Indica si admite propiedades no declaradas en el esquema del objeto.
enum|Explicit set of allowed JSON values.|Conjunto explícito de valores JSON admitidos.
minimum|Inclusive numeric lower bound.|Límite numérico inferior inclusivo.
minLength|Minimum permitted string length.|Longitud mínima de una cadena.
'''
DESCRIPTIONS={}
for line in TEXT.strip().splitlines():
    key,en,es=line.split('|',2)
    if key in DESCRIPTIONS:
        raise ValueError(f'Duplicate field explanation: {key}')
    DESCRIPTIONS[key]={'en':en,'es':es}

SOURCES=sorted((ROOT/'data').rglob('*.json'))+sorted((ROOT/'simulation/examples').rglob('*.json'))+sorted((ROOT/'schemas').glob('*.json'))


def json_type(value):
    if value is None: return 'null'
    if isinstance(value,bool): return 'boolean'
    if isinstance(value,int): return 'integer'
    if isinstance(value,float): return 'number'
    if isinstance(value,str): return 'string'
    if isinstance(value,list): return 'array'
    return 'object'


def inventory(value):
    groups=defaultdict(list)
    def walk(item,path):
        if isinstance(item,dict):
            groups[path].append(item)
            for key,child in item.items():walk(child,f'{path}.{key}')
        elif isinstance(item,list):
            for child in item:walk(child,path+'[]')
    walk(value,'$')
    return groups


def field_type(values):
    types=sorted({json_type(v) for v in values})
    if 'array' in types:
        itemtypes=sorted({json_type(i) for v in values if isinstance(v,list) for i in v})
        types[types.index('array')]='array<'+(' | '.join(itemtypes) or '?')+'>'
    return ' | '.join(types)


def describe(key,lang,path):
    # Schema property-map keys name a subschema, rather than being game values.
    if path.endswith('.properties') or path.endswith('.$defs'):
        return (f'Subschema describing `{key}`; see its nested fields below.' if lang=='en' else f'Subesquema que describe `{key}`; ver sus campos internos más abajo.')
    if key not in DESCRIPTIONS:
        raise ValueError(f'Undocumented field: {path}.{key}')
    if key=='research' and 'civilizations[]' in path:
        return {'en':'Mutable research instance records, separate from the technology definition.','es':'Registros mutables de investigación, separados de la definición tecnológica.'}[lang]
    if key=='id' and path=='$.elevationLevels[]':
        return {'en':'Numeric elevation category 0–3, not an entity ID with a prefix.','es':'Categoría numérica de elevación 0–3, no un ID de entidad con prefijo.'}[lang]
    return DESCRIPTIONS[key][lang]


def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')


def sample(values):
    for v in values:
        if not isinstance(v,(dict,list)) and v is not None:
            rendered=json.dumps(v,ensure_ascii=False)
            return rendered if len(rendered)<=115 else rendered[:112]+'…'
    for v in values:
        if isinstance(v,list):
            if not v:return '[]'
            if not isinstance(v[0],(dict,list)):
                rendered=json.dumps(v[:3],ensure_ascii=False)
                return rendered if len(rendered)<=115 else rendered[:112]+'…'
    return 'null' if all(v is None for v in values) else '—'


def shorten(value,path='$'):
    """Keep every object key; reduce repeated records, never replace null with invented structure."""
    if isinstance(value,dict):return {k:shorten(v,path+'.'+k) for k,v in value.items()}
    if isinstance(value,list):
        if not value:return []
        if path=='$.technologies':
            selected=[x for x in value if x['id'] in {'basic_foraging','species_cultivation','gathering_containers'}]
            return [shorten(x,path+'[]') for x in selected]
        if path in {'$.elevationLevels','$.reviewIssues','$.civilizations'}:
            return [shorten(x,path+'[]') for x in value]
        if path.endswith('.research') and all(isinstance(x,dict) and 'completed' in x for x in value):return value
        if isinstance(value[0],dict):return [shorten(value[0],path+'[]')]
        # Keep scalar arrays intact: these include guide field names, handler inventories and policies.
        return value
    return value


def code(value):return '```json\n'+json.dumps(value,ensure_ascii=False,indent=2)+'\n```'


def slug(path):return str(path.relative_to(ROOT)).replace('/','--').removesuffix('.json')


def tech_supplement(data,lang):
    heading='Condition and eureka variants' if lang=='en' else 'Variantes de condiciones y eurekas'
    intro=('These are exact leaf/filter examples taken from the current file. Different `type` values accept different fields; the union table above does not permit arbitrary field combinations. Every configured condition and eureka event type appears below.' if lang=='en' else 'Son ejemplos exactos de condiciones/filtros del archivo actual. Cada `type` admite campos distintos; la tabla de unión anterior no permite combinaciones arbitrarias. Se muestran todos los tipos de condición y evento de eureka configurados.')
    conditions={};eurekas={}
    def collect(v):
        if isinstance(v,dict):
            if v.get('type') in data['requiredRuntimeHandlers']['conditionTypes']:
                conditions.setdefault(v['type'],[])
                if v not in conditions[v['type']]:conditions[v['type']].append(v)
            for x in v.values():collect(x)
        elif isinstance(v,list):
            for x in v:collect(x)
    collect(data['technologies'])
    for t in data['technologies']:
        for e in t['eurekas']:eurekas.setdefault(e['eventType'],e)
    text=f'\n## {heading}\n\n{intro}\n'
    for typ,examples in sorted(conditions.items()):
        text+=f'\n### `{typ}`\n\n'+code(examples)+'\n'
    for typ,e in sorted(eurekas.items()):text+=f'\n### Eureka event: `{typ}`\n\n'+code(e)+'\n'
    return text


def guide_fields(data,lang):
    if 'hexDefinitionGuide' not in data:return ''
    descriptions={
     'terrainType':('Terrain category.','Categoría de terreno.'),'elevationLevel':('Elevation category.','Categoría de elevación.'),'surfaceType':('Land or water surface.','Superficie terrestre o acuática.'),'biomeId':('Biome reference.','Referencia de bioma.'),'regionalVariantId':('Regional variant reference.','Referencia de variante regional.'),'staticTemperature':('Static thermal conditions.','Condiciones térmicas estáticas.'),'staticMoisture':('Static moisture conditions.','Condiciones estáticas de humedad.'),'freshwaterAvailability':('Freshwater availability.','Disponibilidad de agua dulce.'),'soilCharacteristics':('Soil properties.','Propiedades del suelo.'),'fertility':('Fertility parameters.','Parámetros de fertilidad.'),'biogeographicRegionId':('Biogeographic region reference.','Referencia de región biogeográfica.'),'geologicalProvinceId':('Geological province reference.','Referencia de provincia geológica.'),'geographicModifierIds':('Geographic modifier references.','Referencias de modificadores geográficos.'),'presentPopulationIds':('Populations present on the tile.','Poblaciones presentes en casilla.'),'presentDepositIds':('Deposit instances present on the tile.','Yacimientos presentes en casilla.'),'discoveryByCivilization':('Per-civilization discoveries.','Descubrimientos por civilización.'),'territorialControl':('Current territorial ownership/control.','Control territorial actual.'),'constructionIds':('Constructions on the tile.','Construcciones de la casilla.'),'materialId':('Material associated with a deposit.','Material asociado al yacimiento.'),'reserveAmount':('Remaining deposit reserve.','Reserva restante del yacimiento.'),'grade':('Material concentration/quality.','Concentración/calidad del material.'),'accessibility':('Access restrictions.','Restricciones de acceso.'),'discoveryState':('Deposit discovery status.','Estado de descubrimiento del yacimiento.'),'extractionTechnologyIds':('Extraction technology references.','Referencias tecnológicas de extracción.'),'processingRecipeIds':('Processing recipe references.','Referencias a recetas de procesamiento.')}
    text='\n## '+('Proposed future tile and deposit fields' if lang=='en' else 'Campos futuros propuestos de casilla y yacimiento')+'\n\n'
    text+=('These names currently occur only as strings in guide lists. Their final types, nesting and numeric units/ranges are not yet specified; this table is not an executable schema. A generated tile or deposit instance belongs to GameState, even for values fixed after generation.\n\n' if lang=='en' else 'Estos nombres solo aparecen como cadenas en listas de la guía. Sus tipos finales, anidamiento y unidades/rangos aún no están definidos; esta tabla no es un esquema ejecutable. La casilla o yacimiento generado pertenece a GameState, incluso para valores que no cambian tras generarse.\n\n')
    text+='| '+('Guide list | Proposed field | Meaning | Type/readiness' if lang=='en' else 'Lista guía | Campo propuesto | Significado | Tipo/madurez')+' |\n| --- | --- | --- | --- |\n'
    for owner,key in [('hexDefinitionGuide','definitionFields'),('hexDefinitionGuide','stateFields'),('depositDefinitionGuide','fields')]:
        for name in data[owner][key]:
            text+=f'| `{owner}.{key}` | `{name}` | {descriptions[name][lang=="es"]} | '+('TBD; design only' if lang=='en' else 'Pendiente; solo diseño')+' |\n'
    return text


def render(path,lang):
    data=json.loads(path.read_text());groups=inventory(data);rel=path.relative_to(ROOT).as_posix()
    out=f'# `{rel}`\n\n'
    out+=('[Source JSON]' if lang=='en' else '[JSON fuente]')+f'(../../../{rel}) · [Index](../json-structures.md)\n\n'
    out+=('## Reading this reference\n\n' if lang=='en' else '## Cómo leer esta referencia\n\n')
    out+=('This reference inventories **every current object property**, including nested objects and all object-array variants. `$` is the root; `[]` means any array element. Tables combine the actual records at that path. They describe the current snapshot, not a promise that missing fields are valid.\n\n' if lang=='en' else 'Esta referencia enumera **todas las propiedades actuales**, incluidos objetos internos y variantes de objetos en arreglos. `$` indica raíz y `[]` cualquier elemento del arreglo. Las tablas reúnen los registros reales de cada ruta. Describen la versión actual; no prometen que omitir campos sea válido.\n\n')
    out+=('`Seen` is the number of objects containing that field divided by the number observed at the path. It is **not requiredness**. Only explicit JSON Schema `required` lists or the documented runtime contract define requirements. `array<?>` means no elements exist from which to infer an item type.\n\n' if lang=='en' else '`Presencia` cuenta objetos con el campo respecto de objetos observados en esa ruta. **No significa obligatoriedad**. Solo `required` explícito del esquema o el contrato documentado define requisitos. `array<?>` indica que no hay elementos para conocer su tipo.\n\n')
    out+=('A field seen only as `null` has no implemented inner structure. Do not invent range objects, products, quantities or unrestricted availability. Sample values are examples, not exhaustive enums or balance approvals. Source Spanish strings are provenance; code and identifiers stay English.\n\n' if lang=='en' else 'Un campo observado solo como `null` todavía no tiene estructura interna implementada. No inventar objetos de rangos, productos, cantidades o disponibilidad sin restricciones. Los valores de muestra no son enums exhaustivos ni balance aprobado. Las cadenas originales en español son procedencia; código e identificadores permanecen en inglés.\n\n')
    if rel.startswith('schemas/'):
        out+=('These are JSON Schema keywords, not game-definition fields. The envelope allows additional properties unless explicitly restricted. This document describes the schema file itself; it does not turn its limited validation into a full domain contract.\n\n' if lang=='en' else 'Estas son palabras de JSON Schema, no campos del juego. El esquema permite propiedades adicionales salvo restricción explícita. Esta referencia describe el archivo de esquema, sin convertir su validación limitada en un contrato completo del dominio.\n\n')
    out+=('## Root and nested objects\n' if lang=='en' else '## Raíz y objetos internos\n')
    for group,objects in groups.items():
        out+=f'\n### `{group}`\n\n'
        out+='| '+('Field | Current JSON type | Seen | Meaning | Sample value' if lang=='en' else 'Campo | Tipo JSON actual | Presencia | Significado | Valor de muestra')+' |\n| --- | --- | --- | --- | --- |\n'
        keys=list(dict.fromkeys(k for obj in objects for k in obj))
        for key in keys:
            values=[obj[key] for obj in objects if key in obj]
            out+=f'| `{key}` | `{cell(field_type(values))}` | {len(values)}/{len(objects)} | {cell(describe(key,lang,group))} | `{cell(sample(values))}` |\n'
    out+='\n## '+('Complete example document with reduced repeated arrays' if lang=='en' else 'Ejemplo de documento completo con arreglos repetidos reducidos')+'\n\n'
    out+=('Valid JSON copied from actual records. Repeated object arrays are shortened for readability; object keys and scalar lists of the retained records are preserved. This sample does not guarantee cross-reference closure because records may refer to omitted entries. Use the source JSON and sibling catalogs for loading or validation.\n\n' if lang=='en' else 'JSON válido copiado de registros reales. Los arreglos repetidos de objetos se reducen para lectura; se conservan claves y listas escalares de los registros elegidos. El ejemplo no garantiza referencias completas porque puede apuntar a entradas omitidas. Para cargar o validar, utilizar el JSON fuente y catálogos relacionados.\n\n')
    out+=code(shorten(data))+'\n'
    if 'technologies' in data:out+=tech_supplement(data,lang)
    out+=guide_fields(data,lang)
    return out


def expected_documents():
    result={}
    for lang in ['en','es']:
        index=('# Complete JSON structure reference\n\n' if lang=='en' else '# Referencia completa de estructuras JSON\n\n')
        index+=('[Simple visual reference](visual-reference.md)\n\n' if lang=='en' else '[Referencia gráfica sencilla](visual-reference.md)\n\n')
        index+=('Every JSON source currently tracked under `data`, `simulation` and `schemas` has a reference below, with all nested fields, observed types, meaning and examples. This is generated from current files; `null` internals and empty-array element types remain explicitly unresolved.\n\n' if lang=='en' else 'Cada JSON actual de `data`, `simulation` y `schemas` tiene una referencia con todos los campos internos, tipos observados, significado y ejemplos. Se genera desde los archivos actuales; estructuras internas de `null` y tipos de arreglos vacíos siguen explícitamente pendientes.\n\n')
        for path in SOURCES:
            target=f'lang/{lang}/json/{slug(path)}.md'
            result[target]=render(path,lang)
            index+=f'- [`{path.relative_to(ROOT).as_posix()}`](json/{slug(path)}.md)\n'
        index+=('\n## Maintenance\n\nRun `python tools/generate_json_reference.py` after JSON structure changes; run with `--check` to detect outdated or missing references. Keep field explanations in both languages. The generator fails when it finds a new property without an explanation. This complements, rather than replaces, the conceptual agriculture/world documentation and schema validation.\n' if lang=='en' else '\n## Mantenimiento\n\nEjecutar `python tools/generate_json_reference.py` después de cambiar estructuras JSON; usar `--check` para detectar referencias desactualizadas o faltantes. Mantener explicaciones de campos en ambos idiomas. El generador falla si encuentra una propiedad nueva sin explicación. Complementa la documentación conceptual de agricultura/mundo y la validación de esquemas.\n')
        result[f'lang/{lang}/json-structures.md']=index
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args();documents=expected_documents();outdated=[]
    for rel,content in documents.items():
        path=ROOT/rel
        if args.check:
            if not path.exists() or path.read_text()!=content:outdated.append(rel)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    if outdated:raise SystemExit('Missing or outdated JSON references: '+', '.join(outdated))
    print(f'{"Checked" if args.check else "Generated"} {len(documents)} bilingual documents for {len(SOURCES)} JSON sources.')


if __name__=='__main__':main()
