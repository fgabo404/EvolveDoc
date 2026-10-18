# Resources

The initial guide defines 105 storable materials, 301 possible source bindings and 25 processing endpoint guides. Species and deposits are sources; materials are inventory resources; work/transport are services. Unknown units, yields, recipes and storage rules remain unresolved. Runtime loading is disabled pending review.

La guía inicial define 105 materiales almacenables, 301 vínculos posibles de origen y 25 guías de transformación. Las especies y los yacimientos son orígenes; los materiales son recursos de inventario; trabajo y transporte son servicios. Unidades, rendimientos, recetas y almacenamiento permanecen pendientes. La ejecución está deshabilitada hasta revisarlos.

- [Resource JSON](resources.catalog.guide.json)
- [English documentation](../../lang/en/resources.md) · [Documentación en español](../../lang/es/resources.md)
- [Every JSON field](../../lang/en/json/data--resources--resources.catalog.guide.md) · [Todos los campos JSON](../../lang/es/json/data--resources--resources.catalog.guide.md)
- [Complete diagrams](DIAGRAMS.md) · [Diagramas completos](DIAGRAMS.es.md)
- [Structural schema](../../schemas/resource.guide.schema.json)

New resources use permanent RES identifiers. Grouped source IDs have explicit aliases; technology IDs are unchanged. Generic material IDs do not erase species, source material, seed viability or quality; preserve those in future GameState inventory lots.
