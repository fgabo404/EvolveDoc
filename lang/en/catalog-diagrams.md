# Complete diagrams by catalog

One dedicated file beside each catalog JSON, divided into small diagrams. GitHub renders them in the normal Markdown view.

- [technologies](../../data/technologies/DIAGRAMS.md)
- [world](../../data/world/DIAGRAMS.md)
- [plants](../../data/plants/DIAGRAMS.md)
- [animals](../../data/animals/DIAGRAMS.md)
- [minerals](../../data/minerals/DIAGRAMS.md)
- [resources](../../data/resources/DIAGRAMS.md)

Current coverage: 23 technologies, 9 external technology imports, 7 biomes, 27 regional variants, 129 plant candidates, 134 animal candidates, 57 geological candidates, 21 crop candidates and all 485 source occurrences. Resources: 104 materials, 365 source bindings and 25 transformation guides pending review.

Diagrams show relationships; accompanying tables retain parameters and repeated occurrences. They do not invent biological evolution, domestication, outputs or processing. Field-by-field structures remain in the [JSON reference](json-structures.md).

Update with `python tools/generate_catalog_diagrams.py`; verify with `--check`.
