# Animals: materials and acquisition

[Complete table of 101 animals](../../data/animals/PRODUCTS.md) · [Full JSON](../../data/animals/animals.catalog.guide.json) · [Every field and example](json/data--animals--animals.catalog.guide.md)

The detailed approach applies to every animal in the current catalog, not just foxes. Each entity retains its gameplay identity and lists useful materials based on anatomy. This selection neither enumerates every tissue/industrial use nor claims that every animal was routinely eaten. Scientific species are not required.

## Simple reference

| Group or case | Main materials | Acquisition or condition |
| --- | --- | --- |
| Terrestrial mammals | Meat, hide, bones and fat | Butchering/skinning a usable carcass. |
| Deer and moose | Those materials plus antlers and useful tendons | Antler-bearing individuals or already shed antlers. |
| Antelopes, bison and ibexes | Meat, hide, bones, fat, horns and tendons | Actual horns; not treated as shed antlers. |
| Birds | Meat, bones, fat, feathers and eggs | Dead source for body tissues; collect shed feathers or existing eggs. |
| Fish | Fish flesh, bones where a bony skeleton exists, usable skin and fatty tissues | Fish preparation; subsequent oil extraction. |
| Crabs and krill | Flesh and shell/exoskeleton | Capture and processing; no vertebrate bones. |
| Mollusks and bivalves | Flesh, shells and conditional pearls | Not every individual contains a pearl; empty shells provide no flesh. |
| Turtles | Flesh, bones, fat, usable skin, carapace and eggs | The carapace is not a shed/regrown resource like hair. |
| Elephants | Body tissues, tusks and tendons | Prepared ivory requires processing suitable tusks. |
| Suitable fiber-bearing animals | Animal fiber | Controlled shearing, combing, shed material or carcass recovery as specified. |
| Managed reindeer and dromedaries | Milk/manure plus carcass materials | Only suitable managed lactating females provide collected milk. |

The complete table records exceptions: baleen only where that anatomy exists; echidna pouch eggs as a biological exception; no collectable eggs for rattlesnakes; giraffes/okapis do not receive the keratin horn resource. Krill capture feasibility and period remain under review without inventing historical techniques.

## Object structure

- `potentialProducts[]`: resource, acquisition methods, availability constraints, processing link where applicable, localized notes and evidence references.
- `acquisitionMethods[]`: flat definitions with `tag`, `name`, `description`, `sourceOutcome`, constraints and disabled runtime.
- `productEvidenceSources[]`: anatomy/general-use references, not yield or category-specific historical-harvest certification.
- `serviceUseCandidates[]`: draft, transport and work candidates separate from materials. Training/suitability are pending; these are not inventory outputs.
- `productCoverage`: 101 animals, 498 material associations, 17 methods and 7 service candidates.

`availabilityConstraints` contains English design tags, not implemented conditions. Availability may depend on the individual, sex, reproductive state, actual material or handling. A record is not a guaranteed bundle of every listed output.

`sourceOutcome` distinguishes:

| Value | Meaning |
| --- | --- |
| `requires_dead_animal` | Material operation needs a dead source. |
| `consumes_animal` | Processing consumes the animal, such as opening shellfish. |
| `preserves_animal` | Method intends to preserve the animal with suitable handling. |
| `collects_discarded_material` | Gather already shed material or present droppings. |
| `removes_egg_without_killing_adult` | Adult survives, but removing a fertilized egg affects possible offspring. |

These describe material handling, not whether hunting and butchering require one or several future UI orders. No new GameState carcass type is introduced in this revision.

## Raw and transformed materials

Hide is not tanned leather; raw fat is not oil; raw tendon is not cord; recovering a tusk does not automatically grant prepared ivory.

`RES#000106` identifies raw tendons; `RES#000105` remains bones. All previous allocations remain stable. The generic shell/carapace ID is retained, with source/composition needed before future recipe evaluation.

Processed outputs use `processingTag` to reference a process guide. Animal, fish and whale oils require both processing and correct provenance. `inputProvenancePolicy` prevents land-animal fat becoming fish oil or arbitrary teeth becoming suitable ivory. A raw-material binding with `requiresProcessing: false` still needs butchering, skinning or its stated acquisition operation.

All 28 process guides still lack quantities, equipment, durations and executable recipes. Do not award all raw fat and oil from the same fat simultaneously, or count the same coat as both extracted fiber and an intact fur-bearing hide.

## Completed scope and remaining work

The initial **animal → material → acquisition method** reference is complete with qualitative constraints. This is neither an implemented production simulation nor approval of every animal service. The current catalog includes many wild forms: sheep, goats and additional domestic gameplay entities belong to the domestication task, rather than claiming nonexistent entities are covered here.

Quantities, durations, body/material consumption, reproduction, regeneration, actual equipment/technology, preservation, food suitability, balance and turn phases remain pending. Runtime remains disabled. Plants are the next block in the [roadmap](../../ROADMAP.md).

## Verification and updates

```sh
python tools/generate_animal_products.py
python tools/generate_json_reference.py
python tools/generate_catalog_diagrams.py
python tools/validate_repository.py
```

The checker covers all material associations, methods, references, translations, anatomy boundaries and processed-output guides. It does not replace an individual biological review or establish historical practice or food suitability. Consulted sources and specific limitations accompany the complete table.
