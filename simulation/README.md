# Simulation examples

Educational scenarios accompany the documentation. This directory is not a production simulation engine.

Los escenarios sirven para comprobar conceptos del diseño. Esta carpeta no contiene el motor definitivo.

- [English explanation](../lang/en/simulation.md)
- [Explicación en español](../lang/es/simulation.md)
- [Research example](examples/research_progress.py)
- [Initial fixture](examples/research.initial-state.json)

From the repository root / Desde la raíz:

```sh
python simulation/examples/research_progress.py
python simulation/examples/research_progress.py --output /tmp/evolve-research-state.json
```

Generated `output/` and `saves/` directories are ignored by Git. Only intentional examples belong in version control.
