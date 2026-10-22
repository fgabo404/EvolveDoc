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
