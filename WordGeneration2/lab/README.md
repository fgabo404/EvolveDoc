# Laboratorio Python — Placas tectónicas

Primera réplica experimental de `TectonicPlateGenerator` (`tectonic-plates-2`) del repositorio `fgabo404/Evolve`.

## Ejecutar

```bash
python WordGeneration2/lab/plates.py --seed 2026 --columns 200 --rows 133
pip install numpy matplotlib
python WordGeneration2/lab/plates.py --seed 2026 --columns 200 --rows 133 --png placas.png
```

La lógica de `SplitMix64`, el ruido periódico, las 16 semillas, los costos, las seis bandas y el crecimiento Dijkstra procede del código C# consultado. Se usa la geometría axial odd-q con cierre este-oeste.

## Estado de fidelidad

**Port experimental, no réplica certificada hexágono por hexágono.** La cola `heapq` de Python utiliza un contador de inserción para resolver prioridades idénticas; la cola `.NET PriorityQueue` no garantiza igual orden en empates. También pueden afectar diferencias flotantes, orden de vecinos y precisión de `Math`. Falta generar un archivo de referencia desde la versión C# e incluir una comparación automática de matrices `PlateByCellId` y hashes SHA-256.

**No simula tiempo ni movimiento tectónico.** Genera solo las placas iniciales, permite comprobar su conectividad e inspeccionar un PNG.

No se ha modificado el repositorio de código Evolve.
