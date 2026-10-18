"""Check repository consistency with the Python standard library (not JSON Schema validation)."""
import json
from pathlib import Path
import re
from generate_json_reference import expected_documents
from generate_catalog_diagrams import documents as expected_diagrams
from validate_resources import validate_resources
from validate_biology import validate_biology
from validate_gameplay_categories import validate_categories
from validate_animal_products import validate_animal_products
from generate_biology_reference import documents as expected_biology
from generate_animal_products import documents as expected_animal_products

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def unique(records, label):
    ids = [r["id"] for r in records]
    require(len(ids) == len(set(ids)), f"Duplicate IDs: {label}")
    return set(ids)


def leaves(value):
    if isinstance(value, dict):
        if "technologyId" in value:
            yield value["technologyId"]
        for child in value.values():
            yield from leaves(child)
    elif isinstance(value, list):
        for child in value:
            yield from leaves(child)


def main():
    resource_summary = validate_resources()
    biology_summary = validate_biology()
    category_summary = validate_categories()
    animal_summary = validate_animal_products()
    for relative, expected in {**expected_documents(), **expected_diagrams(), **expected_biology(), **expected_animal_products()}.items():
        document = ROOT / relative
        require(document.exists() and document.read_text(encoding="utf-8") == expected,
                f"Missing or outdated documentation: {relative}. Regenerate JSON references and catalog diagrams.")
    files = list(ROOT.rglob("*.json"))
    for path in files:
        json.loads(path.read_text(encoding="utf-8"))
    world = read("data/world/world.catalog.guide.json")
    plants = read("data/plants/plants.catalog.guide.json")
    animals = read("data/animals/animals.catalog.guide.json")
    minerals = read("data/minerals/minerals.catalog.guide.json")
    for catalog in [world, plants, animals, minerals]:
        require(catalog["runtimePolicy"]["loadAsGameDefinitions"] is False, "Unreviewed guide enabled for runtime")
    for path in world["catalogFiles"].values():
        target = (ROOT / "data/world" / path).resolve()
        require(target.is_relative_to(ROOT) and target.is_file(), f"Missing catalog: {path}")
    species = plants["speciesCandidates"] + animals["speciesCandidates"]
    candidates = species + minerals["geologicalResourceCandidates"]
    ids = unique(candidates, "species and geology")
    biomes = unique(world["biomes"], "biomes")
    variants = {r["id"]: r for r in world["regionalVariants"]}
    unique(world["regionalVariants"], "regional variants")
    for variant in variants.values():
        require(variant["biomeId"] in biomes, "Unresolved variant biome")
    for candidate in species:
        require(all(v in variants for v in candidate["biomeVariantIds"]), "Unresolved species variant")
    occurrences = world["resourceOccurrences"]
    unique(occurrences, "occurrences")
    for occurrence in occurrences:
        require(occurrence["definitionId"] in ids, "Unresolved occurrence definition")
        require(occurrence["biomeId"] in biomes, "Unresolved occurrence biome")
        require(occurrence["variantId"] in variants, "Unresolved occurrence variant")
        require(variants[occurrence["variantId"]]["biomeId"] == occurrence["biomeId"], "Mismatched biome and variant")
        require(occurrence["runtimeEnabled"] is False, "Unreviewed occurrence enabled")
    counts = world["summary"]
    for key, actual in [('biomeCount',len(biomes)),('regionalVariantCount',len(variants)),('plantCandidateCount',len(plants['speciesCandidates'])),('animalCandidateCount',len(animals['speciesCandidates'])),('geologicalCandidateCount',len(minerals['geologicalResourceCandidates'])),('sourceOccurrenceCount',len(occurrences)),('agriculturalCropCandidateCount',len(plants['agriculturalCropCandidates']))]:
        require(counts[key] == actual, f"Summary mismatch: {key}")
    agriculture = read("data/technologies/agriculture.technologies.json")
    technologies = agriculture["technologies"]
    tech_ids = unique(technologies, "technologies")
    require("nodes" not in agriculture and "branches" not in agriculture, "Technology catalog must stay flat")
    orders = [t["order"] for t in technologies]
    require(sorted(orders) == list(range(1, len(technologies)+1)), "Invalid technology ordering")
    external = set(agriculture["externalReferences"]["technologyIds"])
    for reference in leaves(agriculture):
        require(reference in tech_ids | external, f"Undeclared technology: {reference}")
    graph = {t["id"]: set(leaves(t["prerequisites"])) & tech_ids for t in technologies}
    visited, active = set(), set()
    def visit(identifier):
        require(identifier not in active, "Technology prerequisite cycle")
        if identifier in visited:
            return
        active.add(identifier)
        for dependency in graph[identifier]:
            visit(dependency)
        active.remove(identifier)
        visited.add(identifier)
    for identifier in graph:
        visit(identifier)
    for record in candidates + technologies + world["biomes"] + world["regionalVariants"] + plants["agriculturalCropCandidates"]:
        for field in ("name", "description"):
            if field in record:
                require(isinstance(record[field], dict) and all(record[field].get(lang) for lang in ("en", "es")), f"Missing localization: {record['id']}/{field}")
    # Relative Markdown document links only; source-code examples are excluded.
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            require((path.parent / target).exists(), f"Broken document link: {path.relative_to(ROOT)} -> {target}")
    print(f"Validated {len(files)} JSON files, {len(technologies)} flat technologies and {len(occurrences)} linked source occurrences.")
    print(f"Validated {resource_summary['resourceCount']} resources and {resource_summary['sourceBindingCount']} source/product bindings.")
    print(f"Validated {biology_summary['taxonCount']} taxon references, {biology_summary['biologicalFormCount']} forms and {biology_summary['lineageRelationCount']} lineage summaries.")
    print(f"Validated {category_summary['generalizedCategoryCount']} general gameplay categories and {category_summary['retiredIdCount']} retired-ID aliases.")
    print(f"Validated material/method coverage for {animal_summary['animalEntityCount']} animals and {animal_summary['materialLinkCount']} material links.")
    print("External technology imports are declared, not implemented. Live taxonomy verification, source interpretation, ecology, balance and full JSON Schema validation are outside this check.")


if __name__ == "__main__":
    main()
