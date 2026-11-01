# WordGeneration2 — Segundo método de generación del mundo

Investigación por capas, separada del generador actual de Evolve. Este directorio guarda las decisiones y alternativas para un simulador geológico evolutivo; nada aquí modifica el juego.

## Índice por capas

- [Laboratorio Python](lab/README.md): réplica experimental de las placas de Evolve, pruebas y visualización.
- [01 — Placas tectónicas](01-placas-tectonicas.md): análisis y propuestas iniciales. **Pendiente de revisión conjunta**, no decisión final de implementar cada punto.

## Acuerdos de trabajo

- Avanzar y documentar una capa a la vez.
- Tomar como base preliminar el generador actual de 16 placas (crecimiento hexagonal multiorigen, Dijkstra y ruido multiescala), sin reescribirlo en esta etapa.
- Diferenciar el comportamiento **verificado del repositorio** de las **propuestas exploratorias**.
- Investigar Pangea, Continentes y Archipiélagos como configuraciones geológicas resultantes.
- No modificar el código principal hasta acordar explícitamente una implementación.

## Próxima conversación

Revisar en detalle los límites de la capa de placas actual y decidir qué comportamiento se conservará en el segundo método.
