# Plantas y animales: categorías del juego

Usamos el detalle necesario para jugar. **Zorros** es una entidad que proporciona **piel**: no hace falta crear zorro ártico, rojo, corsac o fénec como entidades distintas. Una diferencia de color, región o nombre científico no exige otra ficha.

## Cuándo agrupar y cuándo conservar diferencias

Agrupar cuando solo cambia el nombre regional o científico y los recursos y usos registrados coinciden. Conservar diferencias cuando cambien productos, acciones o progresión: trigo y maíz siguen separados; un animal silvestre y su forma domesticada pueden requerir fichas diferentes. No fusionar especies solo por parecido. Tampoco fusionar plantas con sus recursos.

En esta revisión se agruparon 18 casos animales y 15 vegetales. Por ejemplo, zorros, osos, ciervos, canguros, robles y pinos. No se fusionaron todas las aves, todos los árboles ni todos los alimentos. Los elefantes africanos y asiáticos conservan categorías separadas porque sus usos registrados difieren; cualquier cambio posterior se decidirá por jugabilidad.

## Estructura

| Campo | Función |
| --- | --- |
| `id` / `tag` | Identidad permanente de la categoría, independiente del idioma y la taxonomía. |
| `name` | Nombre visible con `en` y `es`. |
| `biomeVariantIds` | Hábitats referenciados por las apariciones regionales; no significa presencia universal. |
| `potentialProducts` | Recursos obtenibles según el diseño; cantidades y requisitos operativos pendientes. |
| `sourceVariants` | Etiquetas originales que se reunieron en una categoría. Solo procedencia, no subentidades jugables. |
| `entityAliases` | Correspondencias de IDs anteriores hacia una sola entidad vigente. |
| `taxonResolution` | Referencia científica opcional; no crea subespecies jugables ni requisitos. |

Las colecciones siguen planas. `speciesCandidates` conserva su nombre técnico por compatibilidad, pero admite categorías generales. Del mismo modo, el campo técnico `speciesId` de investigación podrá identificar el cultivo o entidad del juego elegido; no obliga a usar una especie científica. No se cambia todavía el ejemplo de simulación ni sus alias de trigo/maíz.

## Ejemplo: zorros

Fragmento de los campos principales del registro real; el JSON completo y todos sus objetos se documentan en la referencia de estructura.

```json
{
  "id": "ANM#000169",
  "tag": "foxes",
  "name": {
    "en": "Foxes",
    "es": "Zorros"
  },
  "potentialProducts": [
    {
      "resourceTag": "hide",
      "status": "potential_from_source",
      "requiredTechnologyIds": null,
      "yield": null,
      "resourceId": "RES#000031"
    }
  ]
}
```

Los cinco IDs anteriores de zorros apuntan a `ANM#000169`. Sus seis variantes regionales de hábitat conservan sus apariciones. Solo existe un vínculo de producto hacia `RES#000031` (piel sin curtir). Agrupar no crea animales nuevos ni permite colocarlos en todo el mapa.

## Compatibilidad y alcance

Los IDs antiguos quedan retirados y no se reutilizan. Cada aparición mundial conserva su ID y texto original; `definitionId` apunta a la categoría general y `sourceDefinitionId` conserva la identidad anterior cuando hubo agrupación. Los vínculos de recursos se redirigieron y se eliminaron duplicados: 298 vínculos vigentes para los mismos 104 materiales.

Hay 109 entidades vegetales, 101 animales y los mismos 21 grupos agrícolas. Se conservan las 485 apariciones del documento y todos los cultivos, recursos y tecnologías. No se añadieron rendimientos, tiempos, costes ni recetas. Las reglas operativas pendientes mantienen los catálogos deshabilitados para ejecución.

## Referencias

- [Plants](../../data/plants/DIAGRAMS.es.md)
- [Animals](../../data/animals/DIAGRAMS.es.md)
- [JSON structures](json-structures.md)

Los catálogos científicos anteriores se conservan como antecedentes opcionales. No dirigen la identidad de entidades ni exigen completar especies, variedades botánicas o ancestros científicos para avanzar con el diseño. Las relaciones de domesticación útiles podrán adaptarse posteriormente a las categorías del juego.

- [Optional science: plants](../../data/plants/BIOLOGY.es.md)
- [Optional science: animals](../../data/animals/BIOLOGY.es.md)
