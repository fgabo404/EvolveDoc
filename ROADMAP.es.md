# Evolve — Pendientes y avances

[English](ROADMAP.md) · [Inicio del proyecto](README.md)

Última actualización: 2026-10-17 (America/Guatemala).

Esta es la lista compartida de trabajo actual, pendientes y avances completados. Consultarla al retomar el proyecto; sirve para personas y herramientas de desarrollo. Los contratos detallados siguen en sus documentos y el historial de cambios en [CHANGELOG.md](CHANGELOG.md).

## Ahora — Enfoque actual

- [ ] Completar **entidad → recurso → forma de obtención** para plantas y animales. Revisar vínculos existentes y completar vacíos. Distinguir recolección, tala, caza, esquila y ordeño, incluyendo si la fuente sobrevive. Todavía no asignar cantidades, tiempos ni regeneración.

Referencias: [categorías de entidades](lang/es/biology.md), [plantas](data/plants/DIAGRAMS.es.md), [animales](data/animals/DIAGRAMS.es.md), [recursos](lang/es/resources.md).

### Decisiones del enfoque actual

Trabajamos una decisión a la vez: presentar opciones, registrar la elección y actualizar datos/documentación y esta lista.

- [x] Zorros: opción C detallada — piel, carne, huesos y grasa animal. Añadido `RES#000105` para huesos.
- [ ] Elegir cómo se obtienen esos materiales: entrega directa tras cazar o una acción posterior de aprovechamiento.
- [ ] Continuar con las demás entidades; la elección de zorros no se aplica a todos los animales.

## Después — Terminar el diseño inicial

- [ ] Definir relaciones silvestres/domésticas útiles con las categorías del juego. Conservar diferencias relevantes entre cultivos; no se exigen especies científicas ni variedades exhaustivas.
- [ ] Completar cadenas de transformación y requisitos de obtención de materiales, incluyendo extracción y refinado de minerales. Las 25 guías actuales relacionan materiales, pero no son recetas terminadas.
- [ ] Definir herramientas, recipientes, recetas e instalaciones necesarias y relacionarlas con recursos y tecnologías. Las referencias externas existentes no equivalen a catálogos completos.
- [ ] Revisar hábitats regionales y reglas de presencia inicial. Distinguir presencia silvestre, animales introducidos y cultivos establecidos; todavía sin emular el mundo.
- [ ] Revisar IDs, referencias faltantes entre catálogos y documentación después de esas decisiones de diseño.

## Más adelante — Simulación y reglas operativas

- [ ] Definir cantidades, unidades, tiempos, regeneración, consumo y balance después del diseño inicial de entidades y recursos.
- [ ] Completar GameState, fases del turno, guardado/carga y compatibilidad.
- [ ] Implementar condiciones tecnológicas, eurekas, efectos y progreso por especie/entidad; la demostración actual solo es un ejemplo.
- [ ] Emular un mundo inicial pequeño sin gráficos, con escenarios reproducibles para comprobar generación y evolución de recursos.
- [ ] Elegir lenguaje y enfoque del motor cuando estén claros los requisitos de simulación.

## Ideas pospuestas — Visibles, fuera del enfoque actual

- [ ] Gráficos, representación del mapa e interfaz, después de la base de simulación.
- [ ] Tiempo atmosférico dinámico, estaciones y desastres climáticos; posible expansión posterior. Las condiciones estáticas del hábitat siguen en el diseño del mundo.
- [ ] Pueblos nómadas, migración y sus relaciones diplomáticas/comerciales; funcionamiento detallado pendiente.
- [ ] Sistemas más amplios de ciudades, economía, diplomacia y guerra; mantener la dirección de simulador histórico con formato 4X.

## Completado — Bases, no funcionamiento final del juego

- [x] Establecer GitHub como referencia principal y organizar documentación bilingüe.
- [x] Separar conceptualmente GameDefinitions, de solo lectura, y GameState, por partida.
- [x] Documentar 23 tecnologías agrícolas planas con textos bilingües, requisitos y eurekas; implementación y balance pendientes.
- [x] Extraer la guía inicial del mundo: 7 biomas, 27 variantes regionales y 485 apariciones originales conservadas.
- [x] Crear guías iniciales de plantas, animales, cultivos, minerales y recursos; son referencias de diseño, no catálogos listos para ejecución.
- [x] Generalizar 33 casos vegetales/animales con 86 alias de IDs retirados; conservar diferencias útiles para jugar. Hay 109 entidades vegetales, 101 animales y 21 grupos agrícolas.
- [x] Definir 104 recursos iniciales, 298 vínculos actuales de origen y 25 guías de transformación. Obtención y procesamiento completos siguen pendientes.
- [x] Añadir referencias de todos los campos JSON actuales, ejemplos, diagramas de catálogos y comprobaciones de consistencia.
- [x] Añadir una pequeña demostración de progreso de investigación sin gráficos; no hay un motor de simulación completo.
- [x] Crear esta lista compartida y enlazar ambos idiomas desde el README.

## Acuerdo de mantenimiento

1. Consultar esta lista antes de continuar; mantener un enfoque actual salvo que el usuario lo cambie explícitamente.
2. Actualizar ambos idiomas en el mismo cambio cuando terminemos trabajo, cambie una decisión o añadamos un pendiente.
3. Marcar una tarea completada solo cuando se termine el alcance indicado. Registrar avances parciales y vacíos restantes explícitamente.
4. Anotar ideas nuevas en Después, Más adelante o Pospuestas, sin sustituir silenciosamente la tarea actual. Las instrucciones del usuario pueden cambiar prioridades.
5. Mantener el detalle útil en su documentación y el historial de cambios terminados en el changelog. No hace falta otro gestor de tareas.
