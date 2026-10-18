# Plants and animals: gameplay categories

Use the detail needed for gameplay. **Foxes** are one entity providing **hide, meat, bones and animal fat**: Arctic, red, corsac and fennec foxes do not need separate gameplay entries. Color, region or scientific name alone does not require another definition.

## When to group and when to retain distinctions

Group regional/scientific variants when their recorded resources and uses match. Retain distinctions when outputs, actions or progression differ: wheat and maize remain separate, and wild/domesticated forms may need different definitions. Do not merge unrelated entities by appearance or merge plants with their resources.

This revision groups 18 animal cases and 15 plant cases, including foxes, bears, deer, kangaroos, oaks and pines. It does not merge all birds, trees or foods. African and Asian elephant categories remain separate because their recorded uses differ; future changes are gameplay decisions.

## Structure

| Field | Purpose |
| --- | --- |
| `id` / `tag` | Permanent gameplay identity, independent of language and taxonomy. |
| `name` | Visible label with `en` and `es`. |
| `biomeVariantIds` | Habitats referenced by regional occurrences, not universal presence. |
| `potentialProducts` | Designed obtainable resources; quantities and operating requirements remain deferred. |
| `sourceVariants` | Original labels combined into one category; provenance, not playable subentities. |
| `entityAliases` | Previous IDs mapped to one canonical entity. |
| `taxonResolution` | Optional scientific reference; creates neither playable subspecies nor requirements. |

Collections remain flat. The legacy technical collection name `speciesCandidates` now explicitly permits general categories. Likewise, research `speciesId` can identify the chosen crop or gameplay entity; it does not require a scientific species. The research demonstration and its wheat/maize aliases are unchanged.

## Example: foxes

Excerpt of the actual record’s main fields; the complete JSON and nested objects are documented in the structure reference.

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
      "resourceTag": "meat",
      "status": "biological_potential_gameplay_design",
      "requiredTechnologyIds": null,
      "yield": null,
      "resourceId": "RES#000029",
      "acquisitionMethodTags": [
        "butchering"
      ],
      "availabilityConstraints": [],
      "processingTag": null,
      "notes": {
        "en": "Useful biological material; availability depends on the actual source and collection method.",
        "es": "Material biológico aprovechable; depende de la fuente concreta y el método de obtención."
      },
      "evidenceSourceKeys": [
        "fao_byproducts"
      ]
    },
    {
      "resourceTag": "bones",
      "status": "biological_potential_gameplay_design",
      "requiredTechnologyIds": null,
      "yield": null,
      "resourceId": "RES#000105",
      "acquisitionMethodTags": [
        "butchering"
      ],
      "availabilityConstraints": [],
      "processingTag": null,
      "notes": {
        "en": "Useful biological material; availability depends on the actual source and collection method.",
        "es": "Material biológico aprovechable; depende de la fuente concreta y el método de obtención."
      },
      "evidenceSourceKeys": [
        "fao_byproducts"
      ]
    },
    {
      "resourceTag": "animal_fat",
      "status": "biological_potential_gameplay_design",
      "requiredTechnologyIds": null,
      "yield": null,
      "resourceId": "RES#000032",
      "acquisitionMethodTags": [
        "butchering"
      ],
      "availabilityConstraints": [],
      "processingTag": null,
      "notes": {
        "en": "Useful biological material; availability depends on the actual source and collection method.",
        "es": "Material biológico aprovechable; depende de la fuente concreta y el método de obtención."
      },
      "evidenceSourceKeys": [
        "fao_byproducts"
      ]
    },
    {
      "resourceTag": "hide",
      "status": "biological_potential_gameplay_design",
      "requiredTechnologyIds": null,
      "yield": null,
      "resourceId": "RES#000031",
      "acquisitionMethodTags": [
        "skinning"
      ],
      "availabilityConstraints": [],
      "processingTag": null,
      "notes": {
        "en": "Useful biological material; availability depends on the actual source and collection method.",
        "es": "Material biológico aprovechable; depende de la fuente concreta y el método de obtención."
      },
      "evidenceSourceKeys": [
        "fao_byproducts"
      ]
    }
  ]
}
```

The five previous fox IDs map to `ANM#000169`. Their occurrences in six regional habitat variants remain intact. The detailed option selected for foxes links hide (`RES#000031`), meat (`RES#000029`), bones (`RES#000105`) and animal fat (`RES#000032`). Material acquisition methods are now documented; future UI action grouping remains undecided. Grouping creates neither new animals nor permission to place them everywhere.

## Compatibility and scope

Old IDs are retired and never reused. Every world occurrence keeps its ID and original text; `definitionId` references the general category and `sourceDefinitionId` preserves the previous identity when grouping occurred. Resource links were redirected and deduplicated: 594 current bindings for 106 materials.

There are 109 plant entities, 101 animal entities and the same 21 crop groups. All 485 original occurrences, crops, resources and technologies are retained. No yields, durations, costs or recipes were added. Pending operational design keeps these catalogs runtime-disabled.

## References

- [Plants](../../data/plants/DIAGRAMS.md)
- [Animals](../../data/animals/DIAGRAMS.md)
- [JSON structures](json-structures.md)

Previous scientific catalogs remain optional background. They do not determine entity identity or require scientific species, botanical varieties or exact ancestors to complete game design. Useful domestication relations can later be adapted to gameplay categories.

- [Optional science: plants](../../data/plants/BIOLOGY.md)
- [Optional science: animals](../../data/animals/BIOLOGY.md)

Design decision updated: the detailed approach applies to all current animals with anatomy-specific outputs. Material uses, amounts and durations still require further design.

[Animal materials / Materiales animales](animal-products.md)
