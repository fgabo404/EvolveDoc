# Research simulation example

## Purpose

Run `python simulation/examples/research_progress.py` from the repository root. Python 3.10+ is sufficient; no external packages are required. The example reads the actual `species_cultivation` definition and a separate fixture in `simulation/examples/research.initial-state.json`.

Two civilizations have independent wheat and maize research records. The first has wheat discovery and accessible material; the second has maize. Both have explicitly pre-completed prerequisites in the fixture. This is a scenario setup, not simulation of how those prerequisites were obtained. Wheat/maize are illustrative crop-group aliases, not exact resolved botanical IDs.

The fixture allocates 40 points per turn to each attempted research in civilization one and 25 in civilization two. It assumes independent budgets for this demonstration; there is no global research-budget allocator. Blocked attempts receive no points.

## Behavior

- Evaluate the real prerequisites and start conditions before beginning research.
- Once started, evaluate ongoing conditions each turn; pause without losing accumulated points if they fail.
- Keep each civilization/species research record independent, cap progress at the definition cost and store a `completed` boolean.
- Advance four turns without changing definitions. Wheat completes on turn 3 in civilization one; maize completes on turn 4 in civilization two. The other attempts remain blocked.
- Check expected outcomes and a JSON serialization round trip. With `--output`, write state to the chosen file and read it back to verify.

```sh
python simulation/examples/research_progress.py
python simulation/examples/research_progress.py --output /tmp/evolve-research-state.json
```

The example supports `all`, `any`, civilization/current-species prerequisite completion, species discovery and species material access. Unsupported conditions raise errors instead of being silently accepted. Empty ongoing conditions on this technology succeed, matching the current definition.

## Limits

This is not a general engine, a full save schema or an implementation of all agriculture handlers. It does not process eurekas, production, capability effects, usage conditions, world generation, resource consumption, allocation of workers or biological evolution. Completing research here does not produce food or grant operational production automatically. Numeric costs and budgets are provisional. The state fixture is versioned as an example, not a compatibility promise for future saves.
