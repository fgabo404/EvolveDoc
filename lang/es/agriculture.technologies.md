# Evolve — Configuración de tecnologías agrícolas

Estructuras JSON completas, tipos y ejemplos: [referencia de JSON](json-structures.md).

Referencia de `agriculture.technologies.json`. Versión de estructura: `2.0.0`. Versión de contenido: `0.3.0`.

Estado: prototipo. Los costes, cantidades y bonificaciones son provisionales. Este archivo contiene definiciones; todavía no incluye un motor de simulación ni un esquema formal JSON Schema.

## 1. Arquitectura

| Componente | Responsabilidad |
| --- | --- |
| `GameDefinitions` | Define tecnologías, condiciones, costes, eventos y capacidades. No cambia durante los turnos. |
| `GameState` | Guarda el turno, las civilizaciones, su progreso, inventarios, descubrimientos y explotaciones. |
| `SimulationEngine` | Interpreta las reglas y actualiza el estado. |

Este JSON pertenece a `GameDefinitions`. Una definición es compartida por todas las civilizaciones; el progreso de cada una se registra por separado. Leer el JSON no ejecuta automáticamente sus condiciones o efectos.

Ejemplo: cultivar una especie cuesta 100 puntos según la definición. Una civilización lleva 30 puntos en trigo. El motor añade su producción de investigación al registro del trigo, sin modificar la definición ni el progreso del maíz.

## 2. Catálogo plano de tecnologías

Las 23 tecnologías están al mismo nivel en `technologies`. Ya no existen contenedores `branches` ni `nodes`. Los campos raíz `id`, `name` y `description` identifican el catálogo agrícola.

`order` es una posición global de presentación de 1 a 23. El orden del arreglo no crea dependencias. Riego, drenaje y arado siguen pudiendo avanzar en paralelo según sus requisitos explícitos. Se conservan los IDs y la identidad de investigación por especie.

## 3. Campos principales

| Campo | Significado |
| --- | --- |
| `schemaVersion` | Versión del contrato estructural. No significa que ya exista un archivo JSON Schema. |
| `contentVersion` | Versión del contenido y balance. |
| `kind` | Tipo de archivo: `technology_definitions`. |
| `status` | Madurez del contenido: `prototype`. |
| `defaultLanguage` | Idioma de respaldo: `en`. |
| `supportedLanguages` | Idiomas disponibles: `en` y `es`. |
| `localization` | Formato de textos visibles, respaldo y futura extracción de traducciones. |
| `balance` | Valores numéricos provisionales. |
| `runtimeContract` | Reglas que deberá implementar el motor. Incluye explicaciones, no código ejecutable. |
| `externalReferences` | Dependencias que deberán proporcionar otros catálogos. |
| `manufacturingAlternatives` | Alternativas para fabricar recipientes; no son recetas completas. |
| `id`, `name`, `description` | Identidad y textos visibles del catálogo. |
| `technologies` | Lista plana de tecnologías al mismo nivel. |
| `speciesGroupBindings` | Relaciona grupos de cultivos con la investigación por especie. |
| `scopeExamples` | Ejemplos de vinculación de trigo y maíz; no son partidas guardadas. |
| `designNotes` | Notas técnicas internas. |
| `requiredRuntimeHandlers` | Condiciones, eventos y efectos que necesitarán código. |

## 4. Estructura de una tecnología

| Campo | Significado |
| --- | --- |
| `id` | Identificador estable en inglés. |
| `order` | Orden global de presentación, sin dependencias implícitas. |
| `name` | Nombre visible con traducciones `en` y `es`. |
| `description` | Descripción visible con traducciones `en` y `es`. |
| `scope` | Alcance: `civilization` o `species`. |
| `prerequisites` | Conocimientos previos necesarios. |
| `research` | Modo de adquisición, coste y condiciones de investigación. |
| `usageConditions` | Condiciones locales para utilizar lo aprendido. |
| `eurekas` | Bonificaciones por acontecimientos del juego. |
| `effects` | Capacidades habilitadas al completar la investigación. |
| `designNotes` | Aclaraciones para diseñadores y programadores. |

`basic_foraging` usa `initial_grant`: se concede una vez al inicializar una civilización y cuesta cero. Para utilizarlo siguen siendo necesarios trabajadores y plantas comestibles accesibles. Cargar una partida no debe volver a concederlo como una segunda recompensa.

## 5. Condiciones y requisitos

```json
{
  "any": [
    { "type": "technology_completed", "technologyId": "basketry", "scope": "civilization" },
    { "type": "technology_completed", "technologyId": "woodworking", "scope": "civilization" },
    { "type": "technology_completed", "technologyId": "pottery", "scope": "civilization" }
  ]
}
```

En este ejemplo basta con una tecnología de recipientes.

- `all`: deben cumplirse todas las condiciones.
- `any`: debe cumplirse al menos una.
- `all: []`: no hay requisito; equivale a verdadero.
- `any: []`: configuración inválida.
- Una condición con `type` consulta un evaluador del motor.

No se utiliza `"None"` como identificador. La interfaz puede mostrar «ninguno» cuando corresponda.

Se comprueban en momentos distintos:

| Condición | Momento |
| --- | --- |
| `prerequisites` | Antes de iniciar investigación y admitir bonificaciones pendientes. |
| `research.startConditions` | Antes de iniciar investigación. |
| `research.ongoingConditions` | Durante cada actualización de investigación activa. |
| `usageConditions` | Al intentar utilizar o mantener una capacidad en el lugar correspondiente. |

Actualmente todas las `ongoingConditions` están vacías. Perder un ejemplar después de iniciar la investigación no la pausa en esta configuración. Si se añaden condiciones continuas y fallan, `pause_keep_progress` conserva el avance.

## 6. Civilización y especie

`civilization` significa una investigación compartida dentro de esa civilización. Ejemplos: `initial_sowing`, `gathering_tools`, `channel_irrigation`.

`species` significa una investigación independiente por especie. Ejemplos: `plant_knowledge`, `species_cultivation`, `initial_selection`.

La identidad de una investigación es:

`(civilizationId, technologyId, speciesId)`

Para alcance general, `speciesId` es `null`. Para alcance por especie es obligatorio. Conviene usar tuplas o diccionarios anidados; no concatenar cadenas sin resolver posibles colisiones.

```json
[
  { "technologyId": "species_cultivation", "speciesId": "wheat" },
  { "technologyId": "species_cultivation", "speciesId": "maize" }
]
```

Ambos registros utilizan una misma definición, pero mantienen avances independientes. `$speciesId` es un marcador que se sustituye por la especie de la instancia actual.

El alcance de un requisito tiene tres opciones:

- `civilization`: comprobar la tecnología general.
- `current_species`: comprobarla para esta misma especie.
- `any_species`: basta con haberla completado para alguna especie.

Para cultivar trigo se necesita `initial_sowing` y `seed_handling` del trigo. La siembra general no habilita todos los cultivos. El catálogo de especies deberá definir ancestros silvestres, reproducción, compatibilidad y criterios de domesticación.

## 7. Investigación y turnos

`research.cost` expresa puntos, no turnos fijos. `initial_grant` concede una capacidad inicial; `points` requiere acumular investigación. La unidad actual es `research_point`.

Ejemplo provisional: coste de 100, avance de 30 y producción de 10 por turno. Quedan 70 puntos y una estimación de 7 turnos, si no cambia la producción ni aparece un eureka.

Los turnos restantes se calculan. Con producción cero no hay estimación de finalización; no se divide entre cero. El progreso se limita al coste.

`balance.defaultResearchCost` es metadato: cambiarlo no modifica los costes explícitos de cada tecnología. Lo mismo ocurre con `defaultEurekaFraction` frente a las recompensas explícitas.

## 8. Recursos y fabricación

Comprobar disponibilidad no consume materiales. Los consumos pertenecen a las acciones y recetas.

`resource_tag_available` busca recursos u objetos etiquetados:

- `inventory`: inventario pertinente según propiedad y accesibilidad.
- `site_equipment`: equipo asignado al lugar donde se realiza la acción.

| Alternativa | Materiales | Otros medios |
| --- | --- | --- |
| `basketry` | `flexible_plant_fiber` | Receta y trabajo. |
| `woodworking` | `wood` | `woodworking_tool`, receta y trabajo. |
| `pottery` | `clay`, `water`, `kiln_fuel` | `firing_facility`, receta y trabajo. |

Son etiquetas y relaciones, no un catálogo terminado de recetas. Faltan cantidades, duración, compatibilidades y balance. El método de cocción debe ser apropiado históricamente.

Los mínimos actuales de una unidad solo comprueban existencia. No determinan cuántos trabajadores equipa un objeto, su desgaste o sus bonificaciones. Tener una herramienta en otra ciudad no debería satisfacer una necesidad local sin las reglas de transporte correspondientes.

## 9. Eurekas

Un eureka es una recompensa de investigación, no un requisito obligatorio.

Ejemplo actual: `species_cultivation` observa `propagation_material_reserved` para la misma especie. Al acumular 10 unidades, puede conceder el 25 % del coste base: 25 puntos sobre un coste de 100. El coste sigue siendo 100; se añade progreso.

La política actual:

1. Contar eventos desde el inicio de la partida, incluso antes de habilitar una investigación.
2. Filtrar por civilización y especie cuando corresponda.
3. Evitar duplicados mediante `eventId`.
4. Conservar la elegibilidad mientras la tecnología esté bloqueada.
5. Conceder la recompensa una vez satisfechos los requisitos y condiciones iniciales.
6. Redondear hacia abajo y limitar el progreso al coste.
7. Guardar el cobro para no repetirlo al cargar la partida.

Los eventos de cantidad aportan su cantidad; los acontecimientos individuales usan `amount: 1`.

Hay dos excepciones documentadas: alternancia cuenta especies distintas compatibles y comparación de líneas cuenta líneas distintas. Aunque sus contadores actuales dicen `sum_amount`, el contrato describe estas excepciones. Antes del evaluador genérico deben normalizarse como modos explícitos o implementarse sus evaluadores particulares; sumar indiscriminadamente no es correcto.

`counterGroup: plotId` exige contar cosechas de una misma parcela. La agrupación también debe guardarse. La política de entrega del eureka no debe impedir terminar una investigación que ya está activa; ese ciclo debe concretarse en la implementación.

## 10. Efectos

El único tipo actual es `unlock_capability`. Desbloquea una capacidad general o por especie, cuya utilización sigue dependiendo de `usageConditions`.

Las capacidades deben restaurarse de forma idempotente: cargar dos veces no duplica el beneficio.

- Investigar riego no construye canales.
- Investigar tracción no crea animales entrenados.
- Investigar domesticación no transforma instantáneamente una población.
- Investigar selección no mejora automáticamente todas las parcelas.

Faltan modificadores numéricos, ecuaciones del suelo, recetas y simulación de características heredables. `specialized_varieties` exige una especie domesticada al aplicar su capacidad.

## 11. Dependencias externas

Estas tecnologías son referencias que deben proporcionar otros catálogos:

- `stone_tools`
- `basketry`
- `woodworking`
- `pottery`
- `water_management`
- `canal_construction`
- `animal_traction`
- `metal_tools`
- `cutting_tools`

También faltan los catálogos `species`, `resources`, `items`, `recipes` y `sites`. Una referencia inexistente o un tipo desconocido debe generar un error, nunca considerarse satisfecho por defecto.

`requiredRuntimeHandlers` enumera 26 condiciones, 17 tipos de eventos y un tipo de efecto. Enumerarlos no implementa su funcionamiento.

## 12. Estado de partida

La definición no recibe campos de progreso. `GameState` conserva civilización, tecnología, especie, puntos acumulados, turno de finalización, investigación activa y contadores/recompensas de eurekas.

Disponibilidad y turnos estimados pueden calcularse. Si se decide copiar costes para congelar reglas de una partida, debe existir una política de versiones explícita y una sola fuente de autoridad.

Inventario, trabajadores, descubrimientos y parcelas se guardan en sus partes correspondientes. La finalización y sus recompensas deben registrarse consistentemente para no duplicarlas tras un guardado interrumpido.

## 13. Secuencia propuesta del motor

1. Cargar y validar las definiciones.
2. Crear índices por ID y dependencias inversas.
3. Resolver catálogos externos y comprobar el grafo completo.
4. Inicializar civilizaciones y conceder capacidades iniciales una sola vez.
5. Validar los comandos de investigación.
6. Procesar eventos en orden estable y actualizar eurekas.
7. Aplicar bonificaciones elegibles y avanzar la investigación activa.
8. Registrar finalizaciones y capacidades sin duplicados.
9. Evaluar por separado los requisitos locales de cada acción.
10. Guardar el estado y la continuidad del procesamiento de eventos.

Falta decidir si una tecnología completada en un turno afecta la producción de ese mismo turno o del siguiente. El orden accidental del código no debe decidirlo.

## 14. Validación y pendientes

Comprobado: sintaxis JSON, serialización, IDs únicos, referencias internas resueltas o externas declaradas, alcance de requisitos por especie y ausencia de ciclos internos.

Pendiente: esquema formal, resolución de catálogos externos y sus ciclos, evaluadores de reglas, simulación, guardado/carga, migraciones y balance. Un grafo sin ciclos no garantiza que todas las investigaciones sean alcanzables: también hay que probar recursos, acciones y posibles bloqueos de juego.

## 15. Catálogo de tecnologías

| Orden | ID | Nombre en inglés | Nombre en español | Alcance |
| --- | --- | --- | --- | --- |
| 1 | `basic_foraging` | Basic Foraging | Recolección básica | `civilization` |
| 2 | `plant_knowledge` | Plant Knowledge | Conocimiento de plantas | `species` |
| 3 | `gathering_tools` | Gathering Tools | Herramientas de recolección | `civilization` |
| 4 | `gathering_containers` | Gathering Containers | Recipientes de recolección | `civilization` |
| 5 | `seed_handling` | Seed Handling | Manejo de semillas | `species` |
| 6 | `wild_plant_management` | Wild Plant Management | Manejo de plantas silvestres | `species` |
| 7 | `initial_sowing` | Initial Sowing | Siembra inicial | `civilization` |
| 8 | `species_cultivation` | Species Cultivation | Cultivo por especie | `species` |
| 9 | `soil_preparation` | Soil Preparation | Preparación del suelo | `civilization` |
| 10 | `channel_irrigation` | Channel Irrigation | Riego por canales | `civilization` |
| 11 | `agricultural_drainage` | Agricultural Drainage | Drenaje agrícola | `civilization` |
| 12 | `organic_manuring` | Organic Manuring | Abonado orgánico | `civilization` |
| 13 | `animal_drawn_plough` | Animal-Drawn Plough | Arado de tracción animal | `civilization` |
| 14 | `improved_ploughs` | Improved Ploughs | Arados mejorados | `civilization` |
| 15 | `fallow_management` | Fallow Management | Descanso del suelo | `civilization` |
| 16 | `crop_alternation` | Crop Alternation | Alternancia de cultivos | `civilization` |
| 17 | `reproductive_reserve` | Reproductive Reserve | Reserva para reproducción | `species` |
| 18 | `initial_selection` | Initial Selection | Selección inicial | `species` |
| 19 | `progressive_domestication` | Progressive Domestication | Domesticación progresiva | `species` |
| 20 | `line_comparison` | Line Comparison | Comparación de líneas | `species` |
| 21 | `specialized_varieties` | Specialized Varieties | Variedades especializadas | `species` |
| 22 | `vegetative_propagation` | Vegetative Propagation | Propagación vegetativa | `species` |
| 23 | `grafting` | Grafting | Injerto | `species` |

## 16. Primera prueba del simulador

Crear dos civilizaciones, conceder recolección básica, descubrir trigo para una y maíz para otra, investigar por separado y comprobar requisitos locales. Después, activar un eureka, guardar y cargar sin duplicar la recompensa. Finalmente, retirar semillas y verificar que el conocimiento permanece aunque no pueda sembrarse de nuevo.

## 17. Idiomas

Todos los `name` y `description` visibles utilizan objetos con claves de idioma:

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

Se aplica al catálogo, las tecnologías y los grupos de cultivos. Técnicamente son objetos, no arreglos. Los identificadores, condiciones, eventos y reglas siguen en inglés.

Orden de resolución: idioma solicitado → `defaultLanguage` → `id` del propietario. Una traducción ausente, vacía o compuesta solo por espacios se considera faltante. El motor deberá implementar esta resolución; todavía no existe una interfaz que cambie de idioma.

El idioma del jugador pertenece a sus preferencias. Cambiarlo no altera IDs, progreso, eventos ni efectos. Nunca se utiliza un nombre traducido como requisito o clave de guardado.

`designNotes`, contratos y notas de balance son texto interno en inglés; no deben mostrarse directamente al jugador. Los nombres de recursos, acciones, mensajes y resúmenes de requisitos necesitarán sus traducciones en los catálogos o interfaz correspondientes.

`schemaVersion: 2.0.0` utiliza `technologies` como lista plana. Se eliminan `branches`, `nodes` y `level`; se usa `order` para la posición global. Los lectores de la jerarquía anterior necesitan adaptarse. La localización continúa con `{en, es}`. Los IDs, costes, requisitos, condiciones y efectos permanecen intactos. Sigue pendiente un archivo JSON Schema formal.

Más adelante pueden extraerse textos a `en.json` y `es.json` mediante claves estables como `technology.basic_foraging.name`. Esa migración cambia el formato de contenido; las partidas siguen vinculadas por IDs, sujetas a la política general de compatibilidad de versiones.
