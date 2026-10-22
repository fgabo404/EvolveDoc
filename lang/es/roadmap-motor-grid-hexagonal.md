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
| 4 | Grid de 20 × 20 | 🔄 Código publicado; pendiente de compilación y revisión visual local | Se ven exactamente **400** hexágonos sin superposiciones ni huecos |
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

## Entrega intermedia — mini-grid 3D con relieve de prueba

- Referencia visual: mapa 3D hexagonal con alturas progresivas, contornos visibles y estilo despejado. Los rangos visuales del boceto no son umbrales ecológicos definitivos.
- El usuario verificó localmente el primer prisma 3D girable. Se mantiene **azimut limitado 0°–180°**, inclinación fija para preservar horizonte y zoom con rueda.
- Nueva prueba previa a los 400 hexágonos: **7 celdas contiguas** (centro + seis vecinos), cada una con altura de tapa distinta.
- `GEvolve.Core/HexDemoWorld.cs` define identidades axiales y alturas fijas de demostración. `GEvolve.Desktop/HexRenderer.cs` obtiene centros mediante `HexGeometry` y genera tapa, paredes hasta nivel base y líneas de contorno. `Program.cs` compone datos y cámara.
- Solo se demuestra geometría 3D: **no es todavía generación procedural**, ni biomas, ni relieve ecológico definitivo, ni grid 20x20.
- Repositorio de código: `fgabo404/Evolve`, último commit `b31e2e59cbc8fc14c50c5663946aebf17dcdf1ad`.
- **Pendiente de aceptación local:** cerrar aplicación anterior; `git pull origin master`, `dotnet build`, `dotnet run --project .\\GEvolve.Desktop`; confirmar las siete columnas y el giro limitado.
- **Política de documentación:** usar XML docs para clases/métodos públicos y comentarios técnicos breves sobre decisiones geométricas y renderizado.

## Corrección de compilación de mini-grid

- En la primera ejecución local, `Program.cs` (línea 72) falló con `CS8310` al usar `objetivo + new(...)` sin tipo explícito.
- Corregido a `objetivo + new Vector3(...)` en `fgabo404/Evolve`, commit `c53a5c90b60979656998acee0a78ffbcabb2a95e`.
- Pendiente: usuario confirma nueva compilación y funcionamiento 3D de siete celdas. No marcar el hito como completado todavía.

## Corrección visual mini-grid 3D — encuadre y matrices

- La captura local tras la primera mini-grid mostró geometría desproporcionadamente grande, cortada y sin silueta hexagonal reconocible; **no se aceptó el hito visual**.
- Se corrigió la convención de carga de la matriz OpenTK/GLSL (`GL.UniformMatrix4` con `transpose=false` para las matrices combinadas por filas) en `GEvolve.Desktop/HexRenderer.cs`.
- Cámara ahora usa proyección **ortográfica inclinada** en lugar de perspectiva, con encuadre inicial más abierto y zoom limitado para mantener los siete hexágonos visibles; se conserva el azimut 0°–180° y horizonte fijo.
- Último commit del código: `cd0e2dfcfb5dc7d6735beb21002ed15db9db9b8d`.
- **Pendiente:** el usuario debe ejecutar `git pull`, `dotnet build` y la aplicación para verificar si la forma, los bordes y las alturas son legibles. No avanzar a 400 celdas antes de esa comprobación.

## Grid 20 × 20 preparado (pendiente de ejecución local)

- La última captura aportada por el usuario corresponde todavía a la versión anterior de **7 hexágonos**, no a la cuadrícula 20 × 20.
- Se publicó `HexDemoWorld.CrearCuadricula(20, 20)` con **400 celdas únicas**, alturas reproducibles de demostración y cámara ortográfica con encuadre ampliado.
- El código fue documentado y se incorporaron verificaciones de conteo, unicidad, alturas finitas y reproducibilidad al ejecutable de pruebas.
- Repositorio `fgabo404/Evolve`, rama `master`, último commit `01942a2248f830cb959f56e42e8940474f254976`.
- Falta que el usuario ejecute `git pull origin master`, `dotnet build`, `dotnet run --project .\\GEvolve.Core.Tests`, `dotnet run --project .\\GEvolve.Desktop` y confirme visualización; no considerar la fase terminada antes.

## Variante aprobada de prototipo — mapa radial y grises

**Nueva decisión del usuario:** conservar el motor 3D, pero sustituir la cuadrícula rectangular visible por un mapa con **perímetro hexagonal radial**, construido desde el centro axial `(0,0)`. En prototipo, el radio **11** produce exactamente **397 celdas** mediante `1 + 3R(R+1)`; no confundir con las 400 celdas del hito rectangular original, cuyo código y pruebas permanecen disponibles.

- **Datos:** `HexDemoWorld.CrearRadial(11)` genera coordenadas únicas por anillos, con altura ilustrativa reproducible.
- **Renderizado:** tapas en escala de grises según elevación (oscuro=bajo, claro=alto); paredes también grises, líneas de cuadrícula oscuras y visibles.
- **Cámara:** giro horizontal azimutal limitado a **15°–165°**; inclinación vertical fija **35°**, manteniendo horizonte y zoom.
- **Fuera de alcance:** la forma radial es una vista de prototipo; el mundo final mantiene la topología este-oeste envolvente anteriormente aprobada. No declarar que el planeta final tendrá borde hexagonal.
- **Pruebas:** conteo 397, 66 celdas en anillo exterior, centro único, coordenadas únicas, radios y reproducibilidad; código documentado.
- **Pendiente de aceptación local:** `git pull origin master`, `dotnet build`, `dotnet run --project .\\GEvolve.Core.Tests`, `dotnet run --project .\\GEvolve.Desktop`. No declarar éxito de renderizado sin captura.
- **Último commit código:** `dd1ac7362dc20d15308f712bcdd6a1d05d69978f`.

## Relieve radial descendente y escala de render (actualización)

- Se ajustó el prototipo radial: **elevación máxima en el centro** y descenso monótono por anillos hasta la periferia; cumbre 1.80 y borde 0.15 unidades visuales, sin convertirlos en umbrales definitivos del modelo 0–100.
- Código: `GEvolve.Core/HexDemoWorld.cs` y verificaciones de cima/borde/descenso en `GEvolve.Core.Tests/Program.cs`; último commit `4c0c645440b049dd57af08909a0c9031282b5cb1`.
- Cada hexágono tiene **radio geométrico 1 unidad**: ancho pointy-top `sqrt(3)` unidades, longitud de punta a punta `2` unidades. **No hay tamaño fijo en píxeles**: lo determinan proyección ortográfica, tamaño de ventana, distancia/zoom y orientación de la cámara.
- Con ventana de 720 px y altura ortográfica de `80*0.85=68` unidades al inicio, la escala es ~10.59 px/unidad; ancho horizontal de referencia ~18.3 px antes de proyectar la orientación del plano X/Z. No confundir este dato con un tamaño constante o con la dimensión vertical proyectada.
- Pendiente de `git pull`, compilación y comprobación visual local del usuario.

## Estilo técnico de terreno 3D — sin sombras y contornos negros

- Por aprobación del usuario, las tapas y las paredes de cada prisma usan el **mismo valor de gris** por elevación; no se aplica sombreado lateral ni iluminación por cara.
- Los bordes superiores, las aristas verticales y los bordes inferiores están dibujados en **negro puro** para destacar cada volumen hexagonal.
- Código: `GEvolve.Desktop/HexRenderer.cs`, commit `d08681191d87fd6b0e717649ebbde18d926b1fa1`.
- Pendiente: validación visual y compilación local del usuario.

## Cuadrícula negra visible mediante geometría (corrección)

- Captura del usuario: al solicitar grosor `GL.LineWidth(4f)`, los trazos seguían demasiado finos/entrecortados; resultado rechazado visualmente.
- Reemplazadas las líneas rasterizadas por una tapa hexagonal negra completa y una tapa gris interior reducida. La franja negra resultante tiene grosor de referencia `0.18` **unidades del mundo**, no píxeles; por ello crece o disminuye visualmente con el zoom y no depende del soporte de líneas anchas del driver.
- Se mantienen caras laterales de gris uniforme, relieve elevado en el centro, mapa radial de 397 celdas y cámara con azimut 15°–165°.
- Código `GEvolve.Desktop/HexRenderer.cs`, commit `fa5b2b268c9b3b463bdc879a31ce0c2f480acccf`.
- Pendiente de `git pull origin master`, `dotnet build` y revisión visual de la cuadrícula.

## Corrección de bordes discontinuos (anillo sin solapamiento)

- La captura cercana del usuario muestra contornos negros discontinuos; no se considera aceptado el estilo anterior.
- Se eliminó el esquema de **dos tapas hexagonales completas superpuestas a alturas casi idénticas**, susceptible a errores de profundidad y artefactos.
- Cada celda pasa a construir **seis bandas trapezoidales negras (12 triángulos)** y **seis triángulos interiores grises**, contiguos y coplanares. Se conserva el volumen 3D gris sin sombras.
- Grosor visual de la banda negra: `0.27` unidades radiales del mundo, variable en píxeles según zoom y cámara.
- Revisión a validar en PC mediante `git pull origin master`, `dotnet build` y `dotnet run --project .\\GEvolve.Desktop`.
- Código commit `3168487c3a435d9472f6952fe55889c8eaf44dd4`.

## Cambio de estilo: sin contornos, tapa superior más oscura

- Por decisión del usuario, se eliminan todos los bordes negros, bandas geométricas y cálculo de contornos por shader.
- El prisma mantiene una única malla; sus tapas superiores usan un gris equivalente al **72 % del gris lateral**; las seis paredes quedan en el mismo tono gris lateral, sin iluminación por cara.
- Se eliminan los atributos de borde innecesarios: vértice = posición XYZ + color RGB (6 `float` en vez de 9), reduciendo datos enviados a la GPU.
- Cambios en `GEvolve.Desktop/HexRenderer.cs`, último commit de código `f549cb9096e61c2b060bcd81e8d39080fda3b2f6`.
- Pendiente de compilación y aceptación visual local del usuario.

## Prueba visual de solo dos capas radiales

- A solicitud del usuario, la escena activa ahora usa `HexDemoWorld.CrearRadial(1)`: un hexágono central y seis vecinos, **7 celdas**, dos niveles radiales contando el centro.
- El generador radial de radio 11 y las pruebas permanecen disponibles; únicamente se reduce la escena visible para comprobar la apariencia.
- Se reajustó cámara y zoom para encuadrar estas siete celdas. Se conserva la tapa gris oscura, las caras laterales claras, ausencia de contornos y giro horizontal 15°–165°.
- Commit código: `d8544c7b53fb79d763b5409cf56d328f2f1ecb87`. Pendiente de compilación y validación visual local.

## Ajuste visual solicitado — tapas claras, paredes oscuras y contornos

- Restaurados los bordes negros con shader GLSL (`fwidth`/`smoothstep`) y grosor de referencia de 3 píxeles, sin duplicar prismas ni crear bandas de geometría.
- La superficie superior usa gris base multiplicado por 1.15 (limitado a 1); las paredes usan el gris base multiplicado por 0.70.
- El mapa activo sigue siendo radial de radio 1: centro y seis vecinos (7 celdas).
- Código `GEvolve.Desktop/HexRenderer.cs`, commit `69a59a28fa1a2fc8d57377df7cd0f74563089fb6`.
- Pendiente compilación y validación visual local, especialmente continuidad de los bordes.

## Corrección GLSL tras error de ejecución local

- El usuario confirmó `dotnet build` exitoso, pero la ventana falló durante `HexRenderer.Compilar` con `Error GLSL: (0) : error C0000: syntax error, unexpected $end at token <EOF>`.
- Se simplificó el shader de fragmentos para separar las rutas de tapa y pared con `if/else` explícito y se mejoró el mensaje de excepción para identificar si falla `VertexShader` o `FragmentShader`.
- Código: commit `ced2330da74923d6dda1a1ba70236d81449629a0`. Continúan tapa clara, paredes oscuras, contornos por shader y 7 celdas.
- **Pendiente de validación real en GPU del usuario**; no se declara resuelto hasta comprobar ejecución. Si persiste, inspeccionar shader específico y registro del controlador.

## Ampliación radial y bordes finos

- A solicitud del usuario, grosor de los bordes GLSL reducido de 3 px a **1.5 px**.
- Escena ampliada de radio 1 a **radio 5**: diámetro de 11 celdas en el eje central, **91 hexágonos** en total. Un mapa radial hexagonal con centro único no tiene un diámetro par exacto de 10 celdas.
- Cámara ortográfica reajustada a distancia inicial 22 unidades; zoom adaptado al nuevo tamaño. Se conserva giro horizontal de 15° a 165°, tapas claras y laterales oscuros.
- Commit código final: `acc37e83f776f5fc62fe781da1497a33b73aa010`.
- Pendiente compilación y comprobación visual local.

## Ampliación de prueba a 217 celdas y borde 4f

- Por solicitud del usuario, `GrosorBordePx` vuelve a **4f** (4 píxeles solicitados en el shader GLSL).
- Mapa radial de radio **8**: centro + ocho anillos, diámetro de **17 hexágonos**, **217 celdas** (`1 + 3 * 8 * 9`).
- Encuadre ortográfico actualizado a distancia inicial 38 unidades, zoom entre 18 y 75; se conservan superficies superiores claras, laterales oscuros y giro 15°–165°.
- Código commit `89c0c1a3359be07444ddb23def63606771fa1270`. Pendiente de prueba visual y compilación local.

## Estándar geométrico y estilo sin bordes

- Se centralizó `HexGeometry.RadioEstandar = 1f` en el núcleo. Corresponde al radio **centro–vértice de 1 unidad del mundo**, no píxeles. Para el hexágono pointy-top del proyecto: ancho entre lados = `sqrt(3)` unidades y distancia entre vértices opuestos = `2` unidades. Todos los centros axiales y vértices de render utilizan esa misma constante.
- A petición del usuario, **se eliminan por completo los bordes**, su shader de contorno y los atributos de borde: 6 floats por vértice (posición XYZ y RGB), con menor uso de memoria y ancho de banda.
- Tapa superior gris clara (`gris * 1.15`, máximo 1), paredes gris oscuro (`gris * 0.70`). Se mantiene mapa radial de radio 8 / 217 hexágonos y la cámara existente.
- Código último commit `98bb9844c3002e29d95b9e6ef55f0db4056b8e74`; pendiente validación local de compilación y vista.

## Cámara: giro horizontal completo

- El usuario solicita dar una vuelta completa alrededor del mapa. Se reemplaza la restricción de azimut 15°–165° por giro horizontal **360° continuo y repetible**, normalizando el ángulo módulo 2π.
- La inclinación vertical permanece fija en 35° para mantener el horizonte estable y evitar invertir el terreno.
- El cambio no altera el estándar de medida hexagonal, mapa radial de 217 celdas ni colores sin borde.
- Código `GEvolve.Desktop/Program.cs`, commit `5fe01f8750b34a1a8c0f5f3270a03116b448c6d3`. Pendiente de confirmación local.

## Prototipo explorable — mundo de 100 × 50 hexágonos

- Código publicado en `fgabo404/Evolve`, rama `master`. Commit final `576e59d412b45bd704be222f0bcd5c7aeef6a022`.
- **Generación:** `GEvolve.Core/WorldGenerator.cs` crea 5,000 hexágonos (100 × 50) con coordenadas axiales únicas, máscara de tres continentes e irregularidades por ondas con semilla `2026`. Agua a altura 0.08, tierra más elevada. Biomas/clima/geografía realista no implementados.
- **Renderizado:** `HexRenderer` muestra agua azul y tierra verde en una sola malla; conserva caras superiores más claras y laterales más oscuros, sin contornos. El tamaño estándar sigue siendo radio 1 unidad de mundo.
- **Navegación:** WASD mueve el objetivo sobre XZ siguiendo orientación horizontal de cámara; Shift acelera; botón derecho gira 360°; rueda cambia zoom; Home centra la cámara. La inclinación vertical es fija para conservar horizonte.
- **Alcance:** esta es una primera visualización de 5,000 hexágonos, todavía en una sola malla estática. NO incluye chunks, culling ni envolvente E–O; son los siguientes pasos de optimización/topología sin cambiar el diseño aprobado del mundo final. Los bordes norte/sur no envuelven.
- **Pruebas añadidas:** conteo de 5,000, unicidad, ambos tipos de superficie, alturas válidas y reproducibilidad por semilla.
- **Validación pendiente en PC:** `git pull origin master`, `dotnet build`, `dotnet run --project .\\GEvolve.Core.Tests`, `dotnet run --project .\\GEvolve.Desktop` y captura de pantalla del mapa.

## Navegación continua y zoom limitado

- Cámara: desplazamiento horizontal periódico (este-oeste) por ancho físico de 100 columnas hexagonales. Al cruzar el extremo se retorna al lado opuesto sin detener el movimiento.
- GPU: se dibuja la misma malla en tres posiciones horizontales (original y dos copias desplazadas), sin triplicar almacenamiento de vértices; es un prototipo previo a culling/chunks gráficos.
- Norte-sur: límites polares, sin conexión entre extremos.
- Zoom: rango 8–52 unidades de cámara, inicio 38; giro horizontal 360 grados.
- Revisión pendiente de compilación y validación visual de la costura este-oeste.
- Código: commit `c6bd3e6b30675511af7b7b1b5f209526e2cc64da`.

## Relieve por niveles 0-100

- Clasificación funcional separada de biomas: mar bajo nivel 30 configurable; terreno medio desde nivel del mar hasta 59; alto 60–79; cumbres infranqueables 80–100.
- `WorldCell.Relieve` y `ReglasRelieve.Clasificar` centralizan el estado. `WorldSystem` incorpora crestas de montaña deterministas sobre la masa continental.
- Visualización provisional sin bordes: mar azul, tierras verdes, elevaciones altas gris verdoso y cumbres claras; cada cara lateral sigue más oscura que la superior.
- Continúa la conexión E/O del mundo y los límites N/S. Los rangos ecológicos por bioma, pendientes, paso y erosión permanecen pendientes.
- Código final `59701e0b820bbbf23852ea34fcd45218ccab66ae`. Requiere prueba local de compilación y captura.

## Análisis hexagonal de pendientes y formas de relieve

- Se añadió `GEvolve.Core/AnalizadorRelieve.cs`, que inspecciona hasta seis vecinos por celda usando coordenadas offset odd-r; respeta costura longitudinal E/O y los límites polares N/S.
- `WorldMap.Analisis` expone las pendientes máxima y media, la forma local (llanura, ladera, valle, cresta, cumbre) y el indicador de paso difícil para cada una de las 5,000 celdas.
- La diferencia máxima de altura es >=24 para marcar un paso difícil; las cumbres de nivel 80 o superior también lo son. Estos umbrales son provisionales para balance, no reglas definitivas de movilidad.
- Se preserva el render del terreno, la navegación continua y el zoom limitado. En esta etapa los valles/crestas son clasificación lógica; aún falta su refinamiento visual por erosión y rutas.
- Pruebas incluidas: conteo, valores válidos, reproducibilidad y restricción de cumbres.
- Código commit `367408e09161f0216ee5152ffb03a25572014fee`; pendiente compilar y revisar localmente.

## Mar hexagonal a nivel cero

- Todos los hexágonos oceánicos permanecen en la cuadrícula, sin eliminar celdas.
- La elevación lógica de cada celda oceánica y su altura visual quedan exactamente en 0; forman una superficie marina plana.
- Se mantienen tierra, topología este-oeste y controles de cámara sin cambios.
- Se agrega una prueba que verifica que todas las celdas marinas sean de nivel 0.
- Código commit `3b859897cc92a5c6fae0c396adc50de97b8f809a`.

## Contornos blancos del mar

- Los hexágonos oceánicos continúan a elevación 0 y ahora muestran un contorno superior blanco de un píxel; la tierra sigue sin bordes.
- Las líneas del agua se guardan en un VBO separado y se replican con el mismo desplazamiento horizontal del render E/O.
- Se utiliza un pequeño desplazamiento vertical de 0.003 para evitar z-fighting; no altera la altura lógica del mar.
- Código commit `2b41b7e9d517969fd1cdcad326415060d1d15a60`.

## Mundo 200 × 150 y etiqueta numérica por hexágono

- La escena muestra 200 columnas por 150 filas: 30,000 hexágonos, distribuidos en 300 chunks lógicos de 10 × 10.
- Cada celda del mundo expone el nivel lógico (byte 0–100) al renderizador. Los dígitos vectoriales de siete segmentos se trazan sobre la cara superior: blancos en agua y oscuros en tierra. Se conservan los contornos blancos exclusivos del mar.
- El mar permanece a nivel 0 y muestra la etiqueta 0. El zoom conserva el límite 8–52, el giro 360 grados y la continuidad este-oeste. Se ampliaron los límites norte-sur para abarcar 150 filas.
- Importante: se dibuja todavía la malla completa en tres posiciones horizontales, sin culling visual por chunks; 30,000 celdas pueden exigir optimización de GPU y filtrado de etiquetas a distancia.
- Pruebas esenciales añadidas para 30,000 celdas, 300 regiones, costura E/O y nivel oceánico cero.
- Código commit `096587615c8326785359aefd104bafe29fd9cd3a`. Pendiente verificación local de compilación y rendimiento.

## Elevaciones continuas y costa baja (sin biomas)

- Se corrige el salto de altura: océano = 0; toda tierra emergida puede ocupar niveles 1–100, incluidas costas de 1–10.
- La generación combina una máscara continental de costas sinuosas, crecimiento de altura hacia el interior y crestas montañosas concentradas. Se mantiene la periodicidad este-oeste.
- Clasificación funcional: agua 0; tierra media/baja 1–59; relieve alto 60–79; cumbres impasables 80–100. Los biomas no están integrados.
- El parámetro `NivelMar` permanece en `WorldSettings` por compatibilidad, pero no controla actualmente el corte tierra/agua; la costa se define por la máscara continental y el mar visual/lógico es nivel cero.
- Pruebas añadidas para costas bajas, niveles 60–79, cumbres desde 80 y consistencia de clasificación.
- Código: commit `59f639238060bcffc20c286373a1b3c342e7fb8a`. Pendiente validación de compilación y captura en PC.

## Cámara orbital con mayor libertad

- Botón derecho + movimiento horizontal: giro sin límites, 360° repetibles.
- Botón derecho + movimiento vertical: inclinación variable de 8° a 85° sobre el plano, de vista rasante a casi cenital. No se invierte el horizonte.
- Conserva zoom entre 8 y 52 unidades, desplazamiento WASD, costura E/O y límites polares.
- Código commit `6e7527a5d048851487397dd377c8488485532f5c`; pendiente validación local.

## Ajuste de cámara: evitar ángulo rasante

- Inclinación mínima aumentada de 8° a **25°**; máxima 85°, inicial 35°.
- Sin cambios en giro horizontal 360°, movimiento WASD ni zoom 8–52.
- Código commit `d5380ff12d3223919d1e614f7e3010967ae656e7`.

## Sensibilidad de desplazamiento WASD

- Velocidad base aumentada de 18 a 24 unidades del mundo por segundo (+33 %).
- Shift conserva el multiplicador 2.5; giro, inclinación y zoom sin cambios.
- Código commit `62633a0adf62db8a72505394cf633d575077f120`.

## Generador de tipos de mundo — versión 1

- Configuración aprobada: `TipoMundo.Continentes`, mapa `200 x 150` (30,000 hexágonos), `EdadGeologica.Normal`, `PorcentajeOceanos = 60`, `IntensidadMontanosa = 40`, `Semilla = 2026`.
- Nuevas opciones de `WorldSettings`: tipo de mundo, edad geológica, proporción objetivo de océanos e intensidad montañosa. Se conservan los parámetros anteriores por compatibilidad.
- Patrones disponibles: Continentes, Pangea, Archipiélagos, Mar Interior, Fractal y Aleatorio. Se generan a través de máscaras geográficas reproducibles, no de biomas.
- El motor selecciona exactamente 18,000 celdas marinas (60% de 30,000) por ordenación determinista de la máscara; cada océano tiene nivel 0 y cada tierra elevación 1–100.
- La edad geológica y la intensidad montañosa afectan las crestas; la semilla modifica las formaciones sin estado aleatorio compartido.
- Se preserva la lógica de mapa envolvente este-oeste, límites norte-sur, chunks lógicos, números de altura, contornos blancos oceánicos, cámara y zoom.
- Pruebas incorporadas: configuración, dimensiones, proporción de agua, reproducibilidad, variación de tipo y semilla, límites de elevación y parámetros inválidos.
- Limitaciones: máscaras matemáticas iniciales; no placas tectónicas, clima, biomas, erosión compleja ni renderizado selectivo por chunks. Pendiente compilar y verificar visualmente en PC.
- Código último commit `b80e47af18be7aa4faf0e3e0a8e79428ab858434`.

## Menú principal y configuración de mundo — primera versión

- Menú funcional de estilo pixelado inspirado en la organización de Minecraft, con identidad y gráficos propios de G-Evolve. El menú se dibuja directamente con OpenGL en `GEvolve.Desktop/MenuRenderer.cs`, sin texturas ni fuentes de terceros.
- Pantallas: **Inicio** (Un jugador / Continuar / Salir), **Configurar mundo** y **Pausa** (Continuar / Nuevo mundo / Menú principal).
- Desde configuración se puede cambiar tipo de mundo (Continentes, Pangea, Archipiélagos, Mar interior, Fractal o Aleatorio), edad geológica, porcentaje de océanos, intensidad montañosa, semilla y tamaño (100×50, 200×150, 300×200).
- Perfil inicial aprobado: Continentes, 200×150, Normal, 60 % océanos, 40 % montañas, semilla 2026. La generación ocurre al seleccionar **Generar mundo**, no al iniciar la aplicación.
- Controles del menú: W/S o flechas arriba/abajo para elegir; A/D o flechas izquierda/derecha para cambiar valores; Enter o Espacio para confirmar; Escape para retroceder o pausar. También se admiten clics izquierdos en los botones.
- La cámara y el zoom se reinician al crear un mundo nuevo; durante el juego se conservan WASD, Shift, giro horizontal 360°, inclinación 25°–85°, zoom 8–52 y topología continua E/O.
- Sin nuevas dependencias externas. Compilación e interacción gráfica aún deben comprobarse en PC. No existe todavía guardado de partidas ni multijugador.
- Código commit `7cb11f96d0025d5ec9e9acaba88a93578e41c227`.

## Menú minimalista aprobado (v0.1.0)

- Se sustituye el fondo oscuro/paisaje del menú por gris claro uniforme, sin imágenes ni elementos decorativos saturados.
- Logo G-EVOLVE con acento verde en la G y subtítulo exclusivo de versión `V0.1.0`; se conserva fuente pixelada geométrica y botones rectangulares carbón con realce verde.
- Inicio: Nueva partida, Continuar (solo en sesión), Salir. Nueva partida abre la pantalla Configuración: **Tipo de mundo**, **Tamaño**, **Semilla** y acciones Generar mundo / Volver.
- Tipo de mundo determina los parámetros ocultos mediante `WorldPresets.Aplicar`: Continentes Normal/60% océanos/40% montañas; Pangea Normal/45%/50%; Archipiélagos Normal/75%/35%; Mar Interior Antiguo/40%/30%; Fractal Joven/60%/55%; Aleatorio Normal/60%/40%. Semilla inicial 2026.
- Tamaños 100×50, 200×150 y 300×200; semilla cambia con flechas o clic, no requiere edición de archivos. Tipos aún son prototipos matemáticos sin biomas.
- Se preserva menú de pausa con Esc y el sistema de cámara. Falta confirmar compilación y resultado visual localmente.
- Último commit código `7bfdc499556527b10771272cbde873b83398a9f6`.

## Ajuste visual de Nueva partida — referencia aprobada

- Pantalla Nueva partida: fondo gris claro, encabezado pixelado centrado y líneas horizontales a ambos lados.
- Tres filas oscuras con marcos biselados y doble borde: etiqueta a la izquierda y recuadro de valor independiente a la derecha, con flechas `<` y `>`; texto ajustable para nombres largos.
- Acciones inferiores GENERAR MUNDO (marco verde menta) y VOLVER (marco gris), centradas y más estrechas que los selectores.
- Interacción: al hacer clic en la mitad izquierda/derecha del control de valor, se decrementa/incrementa la opción; las teclas de dirección y Enter conservan su comportamiento previo.
- Sin imágenes externas ni cambios de mecánica de generación, presets, movimiento o cámara.
- Código: `b746c96445150c5f4d806ae2be1a8b528a0c8cb5`. Validación local de compilación y aspecto pendiente.

## Paleta monocromática por elevación

- La tierra cambia a escala continua de grises: nivel 1 negro, nivel 100 blanco, con tonos intermedios según el nivel lógico y laterales ligeramente más oscuros.
- Se ajusta automáticamente el color de las etiquetas numéricas para mantener contraste en terreno oscuro o claro.
- El océano conserva el azul, el nivel 0 y sus contornos blancos. Sin cambios en biomas, relieve lógico ni generación.
- Código commit `12cc28d9f4eea70044394d5dd4735e63f88b7340`.

## Hito: versión inicial v0.1.0 (22 de octubre de 2026)

- Se conserva el estado inicial del motor en la rama inmutable por convención `version-inicial-v0.1.0` del repositorio `fgabo404/Evolve`.
- Commit exacto: `12cc28d9f4eea70044394d5dd4735e63f88b7340`.
- Incluye generación por tipos de mundo, menú pixelado minimalista gris claro, mapa hexagonal, mundo 200×150, alturas 0–100, escala de grises en tierra, océano azul con contornos blancos, números de altura y cámara orbital.
- No mover ni editar la rama del hito; los desarrollos futuros continúan en `master`.
- Se crea una rama de respaldo porque el conector GitHub disponible no expone creación de etiquetas (tags) o releases.
- Pendiente validación de compilación y ejecución local; el hito indica versión inicial del prototipo, no versión final certificada.

## Generación geográfica mejorada posterior a v0.1.0

- Tipos activos: **Pangea**, **Archipiélagos**, **Continentes pequeños** y **Continentes grandes** (predeterminado). Se reemplazan las opciones previas Mar Interior, Fractal y Aleatorio de la interfaz.
- Cada tipo utiliza núcleos de masa independientes, deformación espacial del dominio y ruido suavizado de distintas escalas para crear costas menos geométricas, con golfos, cabos, penínsulas e islas; todavía es un modelo procedural, no una simulación geológica real.
- La función de ruido es periódica de este a oeste, mantiene las costas continuas y reproduce resultados por semilla. El ajuste de proporción oceánica sigue siendo exacto por ordenación determinista.
- Presets ocultos: Pangea 40% agua/50% montañas; Archipiélagos 80%/35%; Continentes pequeños 70%/45%; Continentes grandes 60%/40%. Edad normal en todos.
- Se conservan mar 0, tierra 1–100, rejilla hexagonal, menú minimalista y escala visual de grises. No se integran biomas.
- Se ha preservado la rama de respaldo `version-inicial-v0.1.0` sin modificarla.
- Pendiente: ejecutar `dotnet build` y `dotnet run --project .\\GEvolve.Core.Tests` en PC; esta sesión no tiene instalado el SDK .NET.

## Regeneración dentro del juego

- Botón `REGENERAR MUNDO` superpuesto arriba a la derecha, sin abrir menú ni abandonar la partida.
- Atajo `F5` con la misma función.
- Cada activación incrementa la semilla, conserva tipo/tamaño y presets de generación, libera recursos gráficos anteriores y construye un mundo nuevo. Restablece objetivo de cámara y zoom según el comportamiento existente de `CrearMundo`.
- El HUD muestra la semilla actual y utiliza los botones pixelados que ya existen; sin dependencias nuevas.
- Código: `490a39be3d81078971f5addae709aa5470dbc25a`. Pendiente validación visual y de compilación en PC.

## Relieve basado en costas y corredores montañosos (posterior a versión inicial)

- Se mantiene sin cambios la formación y distribución de masas continentales.
- Después de clasificar océanos se calcula para cada hexágono la distancia mínima a la costa, usando búsqueda en anchura por seis vecinos y envolvimiento este-oeste.
- Las primeras celdas costeras generan cotas bajas; al avanzar al interior aparecen llanuras suavizadas y mesetas amplias según ruido regional determinista.
- Se reemplazan las bandas montañosas sinusoidales por dos corredores curvados y localizados según la semilla, con amplitud controlada por la montañosidad y edad geológica.
- Se mantienen océano 0, tierra 1–100, reglas 60–79 alto y 80–100 impasable, escala de grises, semilla reproducible y cuatro tipos de mundo.
- No se añaden todavía tectónica, erosión hidráulica, ríos ni biomas. Verificación de compilación pendiente en PC.
- Commit del motor: `efd0cc5c97ddb04c3c5116cdb182ad1530f752c6`.

## Biomas visuales provisionales

Se agrego una clasificacion determinista por hexagono usando latitud, humedad procedural, distancia a la costa y elevacion. Incluye veinte clases del catalogo de bosques, desiertos, llanuras, marino, pantanos, tundra y montanas. Cada clase tiene un color provisional, sin texturas, vegetacion, fauna ni recursos. El relieve, menu, tipos de mundo y backup v0.1.0 permanecen intactos. Archivos: GeneradorBiomas.cs, WorldMap.cs, WorldSystem.cs, WorldGenerator.cs, Program.cs y HexRenderer.cs. Pendiente probar compilacion en PC.

## Iteración visual: mundo inspirado en boceto hexagonal (octubre 2026)

- Generador: se suman núcleos pequeños de islas satélite a los cuatro tipos de distribución, conservando la cuota oceánica y semilla determinista.
- Costas: BFS multifuente desde las celdas terrestres calcula distancia de cada hexágono marino a tierra. Anillos 1–2 reciben tonos de arrecife (franja tropical) o litoral/estuario (otras latitudes); más allá se usa océano profundo.
- Biomas terrestres: campo climático de frecuencia espacial reducida, con regiones de humedad más extensas para evitar parches dispersos. Se conserva clasificación por relieve y temperatura.
- Norte y sur: celdas acuáticas y terrestres de latitudes extremas reciben tundra ártica/antártica como representación visual del hielo, sin simular capas físicas de hielo.
- Se mantiene mapa 200×150, envolvimiento horizontal, escala 0–100, cuadrícula y etiquetas numéricas. Árboles 3D, picos modelados y texturas del boceto son todavía **referencias visuales**, no funcionalidades implementadas.
- Pruebas ligeras añadidas para clasificación y franja costera; falta ejecutar y revisar compilación en PC con .NET.
- Instantánea de respaldo version-inicial-v0.1.0 intacta.

## Interfaz: carga y zoom de mundo completo

- Al pulsar Generar mundo o Regenerar mundo se activa la pantalla `CARGANDO MUNDO` / `GENERANDO TERRENO Y BIOMAS` y el cálculo de WorldSystem ocurre en un Task en segundo plano; OpenGL y la construcción de la malla se mantienen en el hilo gráfico.
- Al completarse el cálculo se dibuja el mundo. Los errores vuelven a configuración con mensaje básico.
- El scroll usa un factor multiplicativo de 1.12 por paso y permite alejar la cámara hasta 750 unidades (antes 52) para observar un mapa de hasta 300×200; la distancia máxima de recorte de cámara pasa a 2000.
- Se conservan F5 y el botón regenerar, los controles de cámara, mapa envolvente E/O y la instantánea de respaldo v0.1.0.
- Pendiente verificar compilación y comportamiento visual en PC. Commit `be6fcb1d131f0bef8fd28233ac408f84f8b5e084`.

## Cordilleras conectadas (iteración posterior a v0.1.0)

- Nuevo módulo `GEvolve.Core/GeneradorCordilleras.cs` construye trayectorias terrestres con varios segmentos conectados por semilla. Cada trayectoria serpentea suavemente, tiene centro montañoso, laderas progresivas y se debilita cerca del mar.
- Las montañas ya no se originan mediante dos bandas longitudinales globales. Pangea crea 5 cadenas; Archipiélagos 13 más cortas; Continentes pequeños 10; Continentes grandes 8, con distribución controlada por la semilla.
- Altitudes se combinan con llanuras y mesetas; se conserva mar nivel 0, tierra 1–100 y 80–100 impasable. Los biomas alpino y cumbres se asignan por altura con el clasificador existente.
- Se conservan el diseño UI, la cámara, el zoom amplio, la carga y el respaldo de versión inicial `version-inicial-v0.1.0`.
- Pendiente compilar y comprobar visualmente el resultado en PC; la forma final de cada cadena dependerá del relieve terrestre disponible.

## Generación de masas terrestres por tipo de mundo

Se sustituye la antigua máscara global de masas ovales por `GeneradorMasasTerrestres.Crear(WorldSettings)`, llamado desde `WorldSystem.Generar`. El nuevo módulo utiliza ruido fractal multiescala, deformación de coordenadas y regiones superpuestas con envolvimiento de longitud. Cada modalidad dispone de una distribución distinta de centros, número de regiones y escalas:

- **Pangea:** núcleo dominante y seis regiones anexas, buscando una gran masa continental con penínsulas.
- **Continentes grandes:** cinco regiones amplias distribuidas de forma escalonada.
- **Continentes pequeños:** once regiones medianas.
- **Archipiélagos:** treinta y cinco regiones pequeñas con menor distorsión de costa.

Se mantiene el porcentaje exacto de océanos, la semilla determinista y las etapas posteriores sin cambios: distancias costeras, cordilleras, relieve, biomas y color. La conectividad final real de cada mundo todavía requiere validación topológica con componentes conexas; esta primera integración no garantiza matemáticamente el número final de continentes.

Commit de integración: `1d8de71840d56c6d964ccdb4512e5f16ad162a6d`. Pendiente compilación y revisión visual en PC.

## Correccion de siluetas continentales: sin ovalos ni rejillas

A partir del feedback visual del mapa anterior (masas ovaladas en filas), se sustituyo `GeneradorMasasTerrestres` por una metodologia de **esqueletos ramificados**. Cada grupo continental nace con una espina serpenteante y varios brazos conectados; campos fractales multiescala deforman sus costas con bahias, peninsulas y estrechos. Los centros se distribuyen sin grilla. Los cuatro tipos conservan metodos parametrizados distintos: Pangea (un grupo grande), Continentes grandes (4), Continentes pequenos (9) y Archipielagos (21). Se mantiene el calculo posterior de cuota de oceanos, relieve, cordilleras y biomas, asi como la continuidad este-oeste.

Nota: la cuota de oceano puede separar o conectar grupos despues del umbral; todavia no hay comprobacion matematica de conectividad. Falta verificacion visual/compilacion con .NET en PC. Commit `b870e02278bbe73fa688490d3d3967f33cc77a1b`.

## Generador especializado de archipiélagos

`GeneradorMasasTerrestres.Crear` ahora deriva el tipo Archipiélagos a `GeneradorArchipielagos.Crear`. Inspirado en la estructura geográfica de los arcos insulares de Japón y la combinación de arcos y fragmentos de islas de Indonesia y Filipinas, se crean 6–8 sistemas de arcos curvos por semilla, cada uno de 8–16 islas centrales, con distintas dimensiones, orientaciones e islotes satélite. Los canales provienen de la separación entre islas, con variaciones fractales en las costas. No se simula tectónica física; se usa una abstracción morfológica. Se preservan la cuota de océanos y el mapa cilíndrico mediante el generador general. Los tipos Pangea, Continentes grandes y pequeños no se modifican. Referencias: USGS Open-File Report 2010-1083-D (Japan island arcs) y Hartono/Tjokrosapoetro, Geological Society of Malaysia (Indonesia). Pendiente validación en .NET y observación del tamaño final de islas tras aplicar cuota global de océanos.

## Ajuste de Archipiélagos: cadenas insulares fragmentadas

Se redujo el tamaño de cada isla principal y se limitaron los islotes satélite; los arcos son ahora 7–10 cadenas con 7–13 miembros y canales de penalización entre islas sucesivas. El perfil exclusivo de Archipiélagos utiliza 86 % de océano y montañosidad 25. El cálculo se mantiene determinista y no se alteran los otros tres tipos de mundo. La cuota exacta de agua sigue impuesta por ordenación del campo global; quedan pendientes pruebas visuales y comprobación de conectividad de grandes componentes.
