"""Educational subset of the agriculture contract; not a general simulation engine."""
import argparse
from copy import deepcopy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def eligible(expression, civilization, species_id):
    if "all" in expression:
        return all(eligible(c, civilization, species_id) for c in expression["all"])
    if "any" in expression:
        return any(eligible(c, civilization, species_id) for c in expression["any"])
    condition_type = expression["type"]
    if condition_type == "technology_completed":
        scope = expression["scope"]
        if scope not in {"civilization", "current_species"}:
            raise ValueError(f"Unsupported example scope: {scope}")
        target_species = None if scope == "civilization" else species_id
        return any(r["technologyId"] == expression["technologyId"]
                   and r["speciesId"] == target_species and r["completed"]
                   for r in civilization["research"])
    target = expression.get("speciesId", "$speciesId")
    target = species_id if target == "$speciesId" else target
    if condition_type == "species_discovered":
        return target in civilization["discoveredSpeciesIds"]
    if condition_type == "species_material_accessible":
        return target in civilization["accessibleMaterialSpeciesIds"]
    raise ValueError(f"Unsupported example condition: {condition_type}")


def advance_turn(state, definition):
    state["turn"] += 1
    for civilization in state["civilizations"]:
        for research in civilization["research"]:
            if research["technologyId"] != definition["id"] or research["completed"]:
                continue
            species_id = research["speciesId"]
            if not research["started"]:
                can_start = eligible(definition["prerequisites"], civilization, species_id)
                can_start &= eligible(definition["research"]["startConditions"], civilization, species_id)
                if not can_start:
                    research["status"] = "blocked"
                    continue
                research["started"] = True
            if not eligible(definition["research"]["ongoingConditions"], civilization, species_id):
                research["status"] = "paused"
                continue
            research["points"] = min(definition["research"]["cost"],
                                     research["points"] + research["pointsPerTurn"])
            research["completed"] = research["points"] >= definition["research"]["cost"]
            research["status"] = "completed" if research["completed"] else "researching"
    return state


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional save destination; generated state is not source data.")
    args = parser.parse_args()
    definitions = json.loads((ROOT / "data/technologies/agriculture.technologies.json").read_text())
    original_definitions = deepcopy(definitions)
    definition = next(t for t in definitions["technologies"] if t["id"] == "species_cultivation")
    state = json.loads((ROOT / "simulation/examples/research.initial-state.json").read_text())
    assert definition["scope"] == "species" and definition["research"]["mode"] == "points"
    for _ in range(4):
        advance_turn(state, definition)
        for civilization in state["civilizations"]:
            for research in civilization["research"]:
                if research["technologyId"] == definition["id"]:
                    print(f'Turn {state["turn"]}: {civilization["id"]} / {research["speciesId"]}: '
                          f'{research["points"]}/{definition["research"]["cost"]} ({research["status"]})')
    records = [r for c in state["civilizations"] for r in c["research"] if r["technologyId"] == definition["id"]]
    assert [r["completed"] for r in records] == [True, False, False, True]
    assert [r["points"] for r in records] == [100, 0, 0, 100]
    assert definitions == original_definitions, "Definitions must remain unchanged."
    assert json.loads(json.dumps(state)) == state, "State must survive a JSON round trip."
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(state, indent=2) + "\n")
        assert json.loads(args.output.read_text()) == state
        print(f"Saved and reloaded: {args.output}")
    print("Example checks passed: isolated progress, access gates, cost cap, immutable definitions and JSON round trip.")


if __name__ == "__main__":
    run()
