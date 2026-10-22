# G-Evolve — Hoja de ruta técnica: primera cuadrícula hexagonal

**Objetivo del hito:** mostrar una cuadrícula funcional de **20 × 20 hexágonos (400)** en una aplicación Windows construida con motor propio en C# / .NET 10, OpenTK y OpenGL. Este hito **no** incluye relieve, biomas, generación de continentes ni simulación histórica.

**Entorno:** VS Code · .NET 10 LTS · OpenTK 4.9.4 · OpenGL/GLSL · Git.  
**Código local:** `C:\Users\fgabo\Documents\EVOLVE` (carpeta del usuario; repo de documentación distinto: `fgabo404/EvolveDoc`).  
**Estado inicial (21 de octubre de 2026):** ventana 1280 × 720 con fondo azul oscuro y OpenGL inicializado; ejecución mostrada por el usuario. Los demás pasos no están implementados aún.

## Tablero de avance

| Fase | Entregable | Estado | Criterio verificable |
|---|---|---|---|
| 0 | Ventana OpenGL | ✅ Hecho | Aplicación arranca, abre ventana y dibuja fondo sin errores |
| 1 | Núcleo geométrico hexagonal | ✅ Completado: conversiones y pruebas locales superadas | Coordenadas axiales `(q,r)`, vecinos, conversiones a posición y pruebas básicas |
| 2 | Separación de proyectos | ✅ Completado para el hito: Core independiente y Desktop referenciándolo | `GEvolve.Core` independiente de OpenTK y `GEvolve.Desktop` consume sus tipos |
| 3 | Malla base de hexágono | 🔄 En prueba local: primer hexágono y shaders incorporados | Se dibuja **un** hexágono mediante VAO/VBO/EBO + shaders GLSL |
| 4 | Grid de 20 × 20 | ⬜ Pendiente | Se ven exactamente **400** hexágonos sin superposiciones ni huecos |
| 5 | Cámara y encuadre | ⬜ Pendiente | Grid completo visible, redimensionamiento correcto, navegación/zoom básicos |
| 6 | Selección e inspección | ⬜ Pendiente | Clic identifica la celda y muestra `q,r`; celda elegida queda resaltada |
| 7 | Validación y cierre del hito | ⬜ Pendiente | Compila en Debug/Release; invariantes matemáticas y render comprobados |

## Secuencia de desarrollo

### Fase 1 — Matemáticas del hexágono
- Elegir **orientación de vértice superior (pointy-top)** como convención inicial propuesta, modificable antes de programar la malla.
- Usar coordenadas axiales `q,r` y coordenada cúbica implícita `s=-q-r`.
- Implementar los seis vecinos, distancia hexagonal y conversión axial↔mundo.
- Validación: hexágonos vecinos a distancia de una celda; transformación inversa redondea al hexágono correcto.
- Aislar matemáticas de cualquier dependencia gráfica.

### Fase 2 — Estructura
- Añadir `GEvolve.Core` como biblioteca de clases y referenciarla desde `GEvolve.Desktop`.
- Evitar poner geometría del mundo y renderizado directamente en `Program.cs`.
- **No** mover ni reescribir todavía los JSON de `EvolveDoc`.

### Fase 3 — Primer hexágono visible
- Definir vértices, índices y color; crear un shader de vértices y otro de fragmentos.
- Abrir ventana y dibujar una celda; garantizar bordes distinguibles y compatibilidad con el contexto OpenGL creado.
- Limpiar objetos gráficos al cerrar la aplicación.

### Fase 4 — Cuadrícula
- Generar posiciones para `q=0..19`, `r=0..19`.
- Reutilizar malla/recursos en vez de generar lógica duplicada por celda.
- Dibujar relleno sobrio y **contorno hexagonal siempre visible**.
- Mantener identidad estable por celda, independiente del dibujo.
- Validación: 400 hexágonos visibles y contiguos.

### Fase 5 — Cámara
- Proyección ortográfica para el aspecto 2.5D aprobado; terreno aún plano (`z=0`).
- Encuadre automático del grid; paneo, zoom acotado y ajuste al redimensionar.
- Prioridad de lectura visual: contorno de hexágonos → terreno → elementos futuros.

### Fase 6 — Selección
- Convertir posición del cursor en coordenadas del mundo y localizar hexágono.
- Resaltar el seleccionado sin ocultar la cuadrícula y mostrar coordenadas en título o panel temporal.
- Validar esquinas, bordes y clic fuera del mapa.

### Fase 7 — Cierre
- Compilar Debug y Release.
- Probar vecinos/coordenadas en `GEvolve.Core` y selección central/de bordes.
- Registrar capturas del grid y actualizar este tablero con evidencia y commit de código.
- Criterio de **hito alcanzado**: iniciar la app, ver la cuadrícula de 20×20, navegarla y seleccionar cualquier celda.

## Criterios permanentes
- Motor **propio**, no Unity/Unreal.
- Grid siempre visible y legible; escena despejada.
- Datos del mundo independientes del renderizador.
- No iniciar relieve/biomas/fauna antes de cerrar esta meta.
- Pruebas esenciales por etapa; no desplegar suites de regresión innecesarias.
- Actualizar el estado real de este archivo al cerrar cada fase; sin marcar pasos como completos sin evidencia.

## Después de este hito (fuera de alcance)
Relieve progresivo → mundo envolvente este-oeste → continentes/océanos → clima y biomas → distribución de flora, fauna y recursos. Se abordará mediante otra hoja de ruta al completar la cuadrícula.

## Avance registrado — Núcleo hexagonal (21 de octubre de 2026)

- Código subido a `fgabo404/Evolve` (rama `master`), commit `246f6b4`.
- Se creó `GEvolve.Core` (`net10.0`), vinculado a `GEvolve.Desktop`; `dotnet build` completado según evidencia de la terminal.
- `GEvolve.Core/HexCoord.cs` implementa coordenadas axiales `(Q,R)`, coordenada cúbica derivada `S`, seis vecinos y distancia.
- **Pendiente para completar fase 1:** conversión axial↔posición XY con orientación acordada, pruebas de identidad/distancia y retirar `Class1.cs` de plantilla.

## Avance — conversión axial/XY documentada

- Repositorio de código: `fgabo404/Evolve`, rama `master`.
- Añadido `GEvolve.Core/HexGeometry.cs` con XML docs para `APosicion`, `AHexagono`, validación de radio y redondeo cúbico; commit `14dd5d1e1da0e3ced4338d374c1140022ddef004`.
- Eliminado `GEvolve.Core/Class1.cs` de plantilla; commit `accbc079d7f18ef405643b6f139790695b23ccbe`.
- **Estado:** fase 1 todavía en progreso, pendiente de compilación y pruebas locales de inversión/distancia.
- **Política de trabajo acordada:** el asistente modifica código directamente en GitHub, con comentarios y documentación XML para APIs; el usuario ejecuta `git pull`, compila y valida localmente antes de cerrar cada fase. Documentar avances en este roadmap.

## Verificación de fase 1 — pruebas automáticas pendientes de ejecutar

- Evidencia local del usuario: `dotnet build` correcto y ventana OpenGL operativa después de integrar `HexGeometry.cs`.
- Se añadió un ejecutable de verificación independiente `GEvolve.Core.Tests` al repositorio `fgabo404/Evolve` en `master` (código documentado, sin paquetes externos).
- Cubre: coordenada cúbica derivada, seis vecinos únicos, distancia/simetría, conversiones axiales/XY con múltiples radios y validación de entradas incorrectas.
- Comando de aceptación desde la raíz: `dotnet run --project .\\GEvolve.Core.Tests`.
- **Fase 1 todavía pendiente de aceptación:** ejecutar la prueba local y obtener el mensaje de éxito; solo entonces marcar completa. Este proyecto de pruebas aún no está agregado a la solución, pero es ejecutable por su ruta.

## Avance — primer hexágono renderizado (21 de octubre de 2026)

- **Fase 1 aprobada:** el usuario ejecutó `GEvolve.Core.Tests` y obtuvo `OK — Pruebas esenciales de geometría hexagonal superadas`; `dotnet build` también correcto y Git limpio.
- **Fase 2 cubierta en el alcance actual:** biblioteca `GEvolve.Core` independiente del render y referencia desde `GEvolve.Desktop`; no se requiere otro proyecto aún.
- **Fase 3 pendiente de verificación local:** añadidos `GEvolve.Desktop/HexRenderer.cs` y cambios en `Program.cs` para renderizar **un** hexágono verde con borde oscuro mediante VBO/VAO, shaders GLSL y liberación de recursos GPU. Último commit de código: `aaf5d989bac93e6480c35e6daaf8019a422b7c0f`.
- **Validación solicitada:** ejecutar `git pull origin master`, `dotnet build` y `dotnet run --project .\\GEvolve.Desktop`; confirmar imagen de un hexágono en la ventana. No afirmar que la compilación/ejecución ya fue verificada después de este commit.


## Cambio visual solicitado — inspección 3D con cámara orbital

- Aprobado por el usuario tras verificar el primer hexágono plano: el **terreno debe ser verdaderamente 3D y girable**.
- El código en `fgabo404/Evolve` cambia el hexágono plano por un prisma hexagonal con tapa, seis paredes y aristas; añade cámara orbital (arrastre con botón derecho) y zoom (rueda).
- Se conserva la separación entre núcleo matemático `GEvolve.Core` y representación `GEvolve.Desktop`.
- **Prototipo gráfico transitorio:** usa proyección en perspectiva para comprobar volumen; el estilo final aprobado continúa siendo mundo 3D con proyección ortográfica inclinada/isométrica y cuadrícula siempre visible.
- **Pendiente de aceptación:** `git pull origin master`, `dotnet build` y `dotnet run --project .\\GEvolve.Desktop`; comprobar rotación y volumen. No dar la fase por validada hasta la prueba local.
- Código documentado: `GEvolve.Desktop/HexRenderer.cs` y `GEvolve.Desktop/Program.cs`, último commit `ef185e0ef3277c99f3a4fef49c5b52e75e314103`.

## Restricción de cámara aprobada — giro con horizonte estable

- El usuario confirmó el volumen 3D y el funcionamiento del giro.
- A partir de ahora, el **azimut horizontal** de la cámara queda limitado de **0° a 180°**, sin rotación completa de 360°.
- La **inclinación vertical** permanece fija en 35° para no volcar el horizonte, invertir la vista ni mirar desde debajo del terreno. El desplazamiento vertical del mouse no inclina la cámara en este prototipo.
- Se mantiene rueda de zoom y geometría volumétrica hexagonal.
- Implementado en `GEvolve.Desktop/Program.cs` del repositorio de código; commit `16fd75d5e9a69cccde9003fc979f8abaf7004b0b`.
- Pendiente de verificación local con `git pull`, `dotnet build` y prueba de extremos del giro; no dar por probado sin evidencia.
