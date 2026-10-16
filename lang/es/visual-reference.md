# Referencia visual

Diagramas sencillos para consultar el diseño. Están guardados como bloques Mermaid dentro de Markdown: en GitHub, abrir este archivo en la vista normal para verlos; `Raw` muestra el texto editable.

[Documentación principal](README.md) · [Campos JSON y ejemplos](json-structures.md) · [English](../en/visual-reference.md)

## Ejemplo: planta, recurso y tecnología

Ejemplo conceptual, no una cadena de producción ya implementada. Las especies exactas de trigo silvestre, los recursos y sus rendimientos todavía deben definirse. El diagrama no enumera todos los requisitos de las tecnologías.

```mermaid
flowchart TD
    plant["Planta: trigo silvestre"]
    grain["Recurso: grano"]
    seed["Uso: material de siembra"]
    foraging["Tecnología: Recolección básica"]
    handling["Tecnología: Manejo de semillas"]
    cultivation["Tecnología: Cultivo por especie"]

    plant -->|proporciona| grain
    foraging -->|permite recolectar| grain
    grain -->|si es viable| seed
    handling -->|permite seleccionar y conservar| seed
    seed -->|material requerido| cultivation
```

Recolectar no equivale a domesticar. El grano debe ser viable y cumplir las condiciones de la acción para servir como material de siembra. Investigar no crea plantas ni consume materiales automáticamente.

## Catálogos del mundo

Relaciones que ya aparecen en los JSON. Las flechas representan referencias, no orden de generación. Plantas y animales conservan candidatos pendientes de resolver por especie.

```mermaid
flowchart TD
    world["world.catalog.guide.json"]
    biome["biomes: categorías de bioma"]
    variant["regionalVariants: variantes regionales"]
    occurrence["resourceOccurrences: apariciones de la fuente"]
    plant["plants.catalog.guide.json"]
    animal["animals.catalog.guide.json"]
    mineral["minerals.catalog.guide.json"]

    world -->|contiene| biome
    world -->|contiene| variant
    world -->|contiene| occurrence
    variant -->|biomeId| biome
    occurrence -->|variantId| variant
    occurrence -->|definitionId de planta| plant
    occurrence -->|definitionId de animal| animal
    occurrence -->|definitionId geológico| mineral
```

Cada aparición apunta a **un candidato** según su tipo; no a los tres catálogos a la vez. Las rutas a los archivos relacionados están en `catalogFiles`. Los registros siguen deshabilitados para generación real hasta completar su revisión.

## Definición y avance de investigación

La tecnología define reglas comunes; cada civilización conserva su propio avance. Cuando `scope` es `species`, también se separa por especie; cuando es `civilization`, `speciesId` es `null`.

```mermaid
flowchart TD
    definition["GameDefinitions: tecnología"]
    gates["prerequisites y research.startConditions"]
    state["GameState: investigación por civilización y especie"]
    progress["points y completed"]
    use["usageConditions: requisitos para utilizarla"]
    capability["Capacidad operativa"]

    definition -->|reglas para iniciar| gates
    gates -->|habilitan el inicio| state
    definition -->|cost y ongoingConditions| state
    state -->|guarda el avance| progress
    definition -->|reglas de uso| use
    progress -->|si se completó| capability
    use -->|si se cumplen| capability
```

La capacidad es operativa únicamente cuando se cumplen ambas condiciones: investigación completada y requisitos de uso satisfechos. El ejemplo ejecutable de `simulation/` demuestra el avance, sin implementar la operación de capacidades ni producción.

Para editar un diagrama, cambiar su bloque `mermaid` y guardar un commit. Los diagramas son resúmenes mantenidos manualmente; los JSON y sus referencias detalladas conservan los campos, requisitos y relaciones exactas.
