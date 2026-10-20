# G-Evolve — Technology stack and engine architecture (proposal v0.1)

**Status:** prototype design decision, not a completed implementation. **Initial target:** Windows PC. **Date:** 2026-10-20.

## Goal
Build a dedicated graphics engine and deterministic procedural world generator for a systemic historical 4X-style simulation. Approved appearance: **Hand-Drawn Isometric Hex World with Progressive Elevation**: 3D terrain geometry, tilted orthographic camera, permanently visible hex grid, legible elevation and restrained decoration. Keep simulation independent of rendering.

## Proposed stack

| Part | Technology | Responsibility | Status |
|---|---|---|---|
| Desktop host | C# + .NET (current LTS when implementing) | Application runtime and orchestration | Proposed |
| Window/input/graphics context | OpenTK | Window, keyboard, mouse, OpenGL bindings | Proposed |
| GPU renderer | Modern OpenGL + GLSL | Meshes, shaders, grid lines, selection, depth | Proposed |
| Math | System.Numerics | Vectors, matrices, camera transforms | Proposed |
| Procedural generation | Custom C# library | Seeded elevation, moisture, temperature, biome assignment | To design |
| Hex grid | Custom C# library | Axial/cube coordinates, neighbors, distances, elevation | To design |
| Simulation | Custom C# library | Turns/ticks, populations, resources and research, graphics-free | Later |
| Data definitions | JSON + System.Text.Json | Load read-only definitions from EvolveDoc | Proposed |
| Data contracts | Existing JSON schemas/validators | Validate IDs and relationships | Partially present |
| Testing | dotnet test; test framework TBD | Determinism, neighbors, serialization, invariants | Proposed |
| Graphics debugging | RenderDoc | GPU frame diagnostics | Optional |
| Version control | Git + GitHub | Traceable source and documentation | In place |

Do not introduce Unity, Unreal, browser support, Vulkan, or a commercial 3D editor as the game engine in the initial prototype. External art tools may still be used to author assets.

## Architecture

```text
                     Desktop Host
                  Input / UI / Editor
                         |
                 Application Controller
                     /          \
             World Generator   SimulationEngine
                   |                 |
               WorldData          GameState
                   \                 /
                    GameDefinitions
                         |
                   EvolveDoc JSON
                         |
       RenderSnapshot <- WorldData + GameState
                         |
               OpenGL RenderEngine
                OpenTK / GLSL / GPU

 Save: seed + generator version + settings + GameState
```

## Module responsibilities
1. **Desktop/Host:** application lifecycle, clock, input and window.
2. **Core/HexGrid:** axial `(q,r)` and derived cube coordinates, neighbors, distances, IDs. No OpenTK reference.
3. **World/Generation:** seed and parameters → terrain elevation → preliminary moisture/temperature → biome classification → initial WorldData. Version the algorithm and keep deterministic outputs.
4. **World/Model:** terrain and static per-hex attributes; efficient spatial lookup and chunk access.
5. **Simulation:** preserve existing `GameDefinitions` read-only / `GameState` mutable / `SimulationEngine` rules split; graphics-free.
6. **Rendering:** read-only snapshots → 3D elevated meshes, tilted orthographic camera, clear grid, restrained hand-drawn shading; no game rules.
7. **Interaction/Editor:** hex picking, diagnostic inspector, seed/size controls; edits flow through application commands, not direct GPU writes.
8. **Persistence:** versioned seed, parameters, state; no saves or caches in Git.

## Prototype pipeline and acceptance
```text
seed + 20x20 size + parameters
  -> hex topology -> elevation -> basic moisture/temperature
  -> provisional biomes -> WorldData
  -> per-region meshes + always-visible grid
  -> camera + picking + debug inspector
```

- [ ] Render a **20 × 20** hex world in a Windows desktop window.
- [ ] Real 3D elevation levels with an inclined orthographic camera.
- [ ] Hex grid remains recognizable at supported zoom levels.
- [ ] Pan, zoom, pick a tile and inspect its coordinates/elevation.
- [ ] Same seed, parameters and generator version produce identical WorldData.
- [ ] Generator runs in tests without OpenGL.
- [ ] Renderer does not mutate GameState.
- [ ] Biomes can use diagnostic colors without claiming runtime-ready biome rules.
- [ ] Neighbor, determinism and serialization tests pass.

Terrain meshes must avoid unwanted visible cracks (shared seams or an intentional stepped-edge solution). Draw grid as an overlay/pass with depth treatment to avoid z-fighting. Prefer sparse props and detail scaling with zoom.

**Important:** EvolveDoc's 7 biomes, 27 regional variants and other world guide entries are reference catalogs, not approved production generation rules. Do not activate disabled catalogs, invent distributions, yields or recipes.

## Future code layout (Evolve repository; keep EvolveDoc documentation/catalogs in place)
```text
Evolve/
  src/
    GEvolve.Desktop/
    GEvolve.Core/
    GEvolve.World/
    GEvolve.Simulation/
    GEvolve.Rendering.OpenGL/
    GEvolve.Editor/
    GEvolve.Persistence/
  tests/
    GEvolve.Core.Tests/
    GEvolve.World.Tests/
    GEvolve.Simulation.Tests/
  assets/
    shaders/
    textures/
```

Desktop composes modules. Simulation never depends on OpenGL; Core/World never depend on Rendering. Render snapshots bridge world/state to the renderer.

## Open decisions
Exact .NET LTS and OpenGL version/GPU floor; stepped versus interpolated elevation; noise/erosion/climate algorithms; save format and chunk/LOD strategy. Resource/fauna placement and numerical balance wait for validated simulation rules.

**Compatibility:** architectural documentation only; no existing IDs, JSON catalogs, progression, or gameplay balance changed. Current manual simulation and roadmap remain valid.
