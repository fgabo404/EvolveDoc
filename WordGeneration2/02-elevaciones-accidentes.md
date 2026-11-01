# Capa 02 — Elevaciones y accidentes geológicos (prototipo)

Estado: **experimental**. Implementación: [lab/relief.py](lab/relief.py). La Capa 01 ([placas iniciales](01-placas-tectonicas.md)) no se modifica.

## Propósito
Transformar límites tectónicos y movimientos relativos en un **campo de relieve potencial** y máscaras de accidentes geológicos. No hay todavía corteza continental/oceánica, nivel del mar ni evolución por millones de años. Por tanto, el resultado **no constituye aún un mapa de tierras emergidas**, ni es una clasificación física definitiva.

## Algoritmo
1. Recibe la topología hexagonal, la matriz de propietarios de placa y la semilla de la primera capa.
2. Asigna direcciones y velocidades planas deterministas (1–8 cm/año), usando un flujo aleatorio separado.
3. Recorre las fronteras reales entre placas y proyecta velocidades relativas sobre normales y tangentes: convergencia, divergencia y cizalla.
4. Propaga la máxima intensidad de cada canal sobre los vecinos hexagonales con atenuación gaussiana y radio experimental de 7 hexágonos.
5. Produce un **índice relativo de elevación** a partir de convergencia, divergencia, cizalla y dos frecuencias de ruido.
6. Marca zonas potenciales de **cordilleras** junto a convergencia, **rifts** junto a divergencia, **fosas candidatas** junto a convergencia fuerte y **centros volcánicos candidatos** en zonas convergentes o extensivas.

Los umbrales son provisionales y requieren calibración visual, estadística y geológica. El índice de altura no está expresado en metros, y una fosa convergente no implica necesariamente fondo oceánico.

## Alcance científico y próximos pasos
- Una colisión continental puede originar cordilleras; una subducción oceánica puede originar fosa y arco volcánico. **No se pueden distinguir sin asignar corteza previamente.**
- Los rifts y el volcanismo no dependen solo de la intensidad cinemática; se necesitan propiedades de corteza, contexto tectónico e historia.
- La erosión, valles fluviales, mesetas, cuencas sedimentarias, volcanes aislados y la acumulación temporal de deformación siguen pendientes.
- La malla sigue siendo 400×267 hexágonos con cierre horizontal; una proyección PNG 3:2 no cambia los vecinos.

## Ejecución
Desde la raíz del repositorio:

```bash
pip install numpy matplotlib
python WordGeneration2/lab/relief.py --png relieve.png
python WordGeneration2/lab/relief.py --seed 356282175 --png relieve_repetible.png
```

No se altera el repositorio de juego Evolve. No se ha validado todavía el algoritmo contra un modelo geológico real.
