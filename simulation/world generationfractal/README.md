# World generationfractal

**Experimento independiente para G-Evolve**, inspirado en la estructura por etapas del generador de Civilization VI, no copiado del código del juego. No reemplaza el simulador **world generation 2** ni modifica el generador central.

## Ejecutar

Requiere Python 3.10+, NumPy y Matplotlib:

```bash
pip install numpy matplotlib
python world_generation_fractal.py --seed 12345 --world continents --output mundo.png
```

Opciones: `--world` (continents, pangaea, archipelago, fractal), `--seed`, `--width`, `--height`, `--sea-level`, `--world-age` (young, normal, old), `--rainfall` (arid, normal, wet), `--temperature` (cold, normal, hot), `--output`, `--show`.

## Etapas

1. Ruido de valor interpolado de varias octavas (fBm).
2. Máscara continental dependiente de la selección de mundo.
3. Umbral de tierra emergida determinado por el nivel del mar.
4. Campo separado de colinas y montañas.
5. Temperatura latitudinal y humedad aproximada.
6. Clasificación preliminar de biomas y visualización hexagonal con líneas visibles.

## Limitaciones actuales

**No es el generador exacto de Civ VI.** Aún no implementa placas tectónicas físicas, lluvia orográfica, erosión, hidrología, ríos ni controles estrictos de continuidad de continentes. Los parámetros y biomas son experimentales. No se modifican las reglas aprobadas de alturas 0–100, ni se traslada automáticamente al motor central. Más adelante se pueden añadir pruebas de conectividad y un visor interactivo comparable con el generador previo.
