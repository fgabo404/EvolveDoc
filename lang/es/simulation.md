# Ejemplo de simulación de investigación

Estructuras JSON completas, tipos y ejemplos: [referencia de JSON](json-structures.md).

## Propósito

Ejecutar `python simulation/examples/research_progress.py` desde la raíz. Requiere Python 3.10+, sin paquetes externos. Lee la definición real `species_cultivation` y el escenario separado `simulation/examples/research.initial-state.json`.

Dos civilizaciones tienen avances independientes para trigo y maíz. La primera conoce trigo y tiene material accesible; la segunda, maíz. El escenario declara requisitos previos completados: no simula cómo se consiguieron. Trigo/maíz son alias agrícolas ilustrativos, no especies botánicas exactas resueltas.

El escenario asigna 40 puntos por turno a cada intento de investigación de la primera civilización y 25 a cada intento de la segunda. Supone presupuestos independientes para demostrar el avance; no incluye un distribuidor de presupuesto científico total. Los intentos bloqueados no reciben puntos.

## Comportamiento

- Evalúa requisitos y condiciones reales antes de comenzar.
- Después evalúa condiciones de continuación por turno; si fallan, pausa conservando puntos.
- Mantiene registros separados por civilización/especie, limita puntos al costo y guarda `completed` como booleano.
- Avanza cuatro turnos sin cambiar las definiciones. La primera completa trigo en el turno 3; la segunda completa maíz en el turno 4. Los otros intentos siguen bloqueados.
- Verifica los resultados esperados y la serialización JSON. Con `--output`, guarda el estado y vuelve a leerlo para comprobarlo.

```sh
python simulation/examples/research_progress.py
python simulation/examples/research_progress.py --output /tmp/evolve-research-state.json
```

Admite `all`, `any`, requisitos tecnológicos de civilización/especie actual, descubrimiento y acceso a material de la especie. Las condiciones no implementadas producen error en lugar de aprobarse silenciosamente. Las condiciones de continuación vacías se cumplen, como establece la definición actual.

## Límites

No es un motor general, un esquema definitivo de partidas ni la implementación de todos los manejadores agrícolas. No procesa eurekas, producción, efectos de capacidades, condiciones de uso, generación mundial, consumo de recursos, asignación de trabajadores ni evolución biológica. Completar una investigación aquí no produce alimentos ni activa producción operativa automáticamente. Los costos y presupuestos son provisionales. El estado está versionado como ejemplo, sin promesa de compatibilidad con futuras partidas.
