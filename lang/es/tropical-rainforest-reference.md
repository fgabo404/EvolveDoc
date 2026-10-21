# G-Evolve — Selva tropical: ficha de diseño y referencia visual

**Estado:** referencia provisional aprobada para el prototipo PC el 21 de octubre de 2026. **Clasificación:** Bioma **Bosque** → tipo **Tropical (selva)** (`tropical_forest`).

## Referencia artística

- Imagen realizada en conversación: `mapa_hexagonal_de_selva_tropical.png` (boceto aprobado **de momento**, no arte definitivo).
- **Nota de archivo:** se conserva la identificación del boceto y su descripción aquí; la imagen PNG todavía **no está incorporada como archivo binario al repositorio GitHub**.
- Composición: paisaje tropical isométrico con hexágonos claramente trazados en tierra y mar, río continuo, costa, alturas progresivas, árboles dispersos y fauna representativa.
- **Advertencia de estilo:** el boceto es referencia de composición; en implementación reducir aún más la concentración de árboles, rocas y animales, conservando hexágonos visibles y terreno legible.

## Reglas del mundo

- Hexágonos visibles siempre; relieve progresivo de múltiples niveles y continuidad geográfica.
- No equivale a un mapa insular obligatorio: la selva puede extenderse en continentes continuos y ocupar distintas elevaciones compatibles con clima/agua/suelo.
- La presencia compatible de fauna/flora no implica que aparezca en todos los hexágonos, ni que todas las especies catalogadas sean nativas de una misma zona.
- La vegetación dibujada es una representación visual **dispersa** y no el número lógico de individuos simulados.
- Recursos geológicos definidos por depósitos y geología, no por apariciones garantizadas del bioma.
- No habilitar spawns por esta ficha: probabilidades, filtros ambientales y distribución real siguen pendientes de validación.

## Inventario agrupado del JSON de diseño

Fuente: `data/world/world.catalog.biomas-agrupados.v021.json`. Conserva IDs estables y asociaciones originales. Las categorías no se dividen por continentes.

### Flora (23 definiciones únicas)

- Cacao silvestre, en su distribución nativa — `plant_wild_cacao`
- Teosinte, en su distribución mesoamericana — `plant_mesoamerican_teosinte`
- Vainilla (Vanilla planifolia), Mesoamérica — `plant_mesoamerican_vanilla`
- Frijoles silvestres (Phaseolus spp.) — `plant_wild_beans`
- Castaña de Brasil, Amazonía — `plant_brazil_nut`
- Calabazas silvestres (Cucurbita spp.) — `plant_wild_squashes`
- Árbol del caucho (Hevea brasiliensis), Amazonía — `plant_amazonian_rubber_tree`
- Palma aceitera africana — `plant_african_oil_palm`
- Baobab africano — `plant_african_baobab`
- Nuez de cola (Cola spp.) — `plant_kola_trees`
- Acacias africanas — `PLT#000192`
- Rafia africana (Raphia spp.) — `plant_african_raffia_palms`
- Árboles de miombo (Brachystegia spp.), donde corresponda — `plant_miombo_trees`
- Árboles de maderas tropicales regionales — `plant_regional_tropical_timber_trees`
- Bananos silvestres (Musa spp.) — `PLT#000196`
- Teca en su distribución nativa — `plant_native_teak`
- Taro silvestre en su área nativa — `plant_wild_taro`
- Bambúes de bosque seco — `PLT#000195`
- Árboles de sal (Shorea robusta), regiones adecuadas — `plant_sal_trees`
- Palmas y dipterocarpáceas regionales — `plant_regional_palms_and_dipterocarps`
- Parientes silvestres de caña de azúcar (Saccharum spp.) — `plant_wild_sugarcane_relatives`
- Taro y otras aráceas regionales — `plant_taro_and_regional_aroids`
- Palmas y pandanus — `plant_palms_and_pandanus`

### Fauna (21 definiciones únicas)

- Jaguar — `animal_jaguar`
- Venado cola blanca, Mesoamérica — `ANM#000175`
- Tapir amazónico o centroamericano, según zona — `ANM#000185`
- Pecarí de collar — `animal_collared_peccary`
- Mono aullador — `animal_howler_monkey`
- Pavo ocelado, Yucatán y zonas vecinas — `animal_ocellated_turkey`
- Guacamayas — `animal_macaws`
- Gorila occidental, África central occidental — `animal_western_gorilla`
- Elefante africano de sabana, mosaicos de bosque seco — `ANM#000176`
- Okapi, cuenca del Congo — `animal_okapi`
- Babuinos — `ANM#000172`
- Antílopes regionales — `ANM#000171`
- Chimpancé, zonas compatibles — `animal_chimpanzee`
- Elefante asiático — `ANM#000177`
- Pavo real azul, subcontinente indio — `animal_indian_peafowl`
- Tigre, en hábitats adecuados — `animal_tiger`
- Gallina roja de la jungla (Gallus gallus) — `animal_red_junglefowl`
- Casuario del sur, Nueva Guinea y norte de Australia — `animal_southern_cassowary`
- Canguros arborícolas de Nueva Guinea — `ANM#000174`
- Aves del paraíso — `animal_birds_of_paradise`
- Cuscús y otros marsupiales arborícolas — `animal_cuscuses_and_other_arboreal_marsupials`

### Recursos geológicos (20 definiciones únicas)

- Arcilla aluvial — `geological_alluvial_clay`
- Caliza — `geological_limestone`
- Oro aluvial — `geological_alluvial_gold`
- Cobre — `geological_copper_bearing_deposit`
- Hierro — `geological_iron_bearing_deposit`
- Oro en veta — `geological_vein_gold`
- Cobre (sulfuros) — `geological_sulfide_copper_ore`
- Hierro (hematita) — `geological_hematite_iron_ore`
- Arcilla — `geological_clay`
- Laterita ferruginosa — `geological_iron_rich_laterite`
- Manganeso — `geological_manganese_bearing_deposit`
- Manganeso (pirolusita) — `geological_pyrolusite_manganese_ore`
- Arcilla fluvial — `geological_fluvial_clay`
- Estaño aluvial (casiterita) — `geological_alluvial_cassiterite`
- Estaño — `geological_tin_bearing_deposit`
- Estaño (casiterita en veta) — `geological_vein_cassiterite_tin_ore`
- Cobre (calcopirita) — `geological_chalcopyrite_copper_ore`
- Roca volcánica — `geological_volcanic_rock`
- Níquel — `geological_nickel_bearing_deposit`
- Níquel (laterita niquelífera) — `geological_nickeliferous_laterite`

## Compatibilidad y cautelas

- Se unificaron 82 apariciones históricas en 64 definiciones únicas (23 flora, 21 fauna y 20 recursos).
- Mantener las referencias de origen para filtrar distribuciones naturales aunque el catálogo se presente sin clasificación regional.
- Algunas entradas heredadas representan bosque tropical seco o mosaicos; su pertenencia definitiva al tipo Selva requiere revisión ecológica posterior, sin eliminar ni reubicar registros ahora.
- Animales salvajes, domesticación y cultivo no son equivalentes; presencia y obtención de productos dependen de mecánicas específicas.
- Las cumbres extremas permanecen infranqueables y no se convierten en selva automáticamente.
