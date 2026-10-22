# G-Evolve — Hoja de ruta técnica: primera cuadrícula hexagonal

**Objetivo del hito:** mostrar una cuadrícula funcional de **20 × 20 hexágonos (400)** en una aplicación Windows construida con motor propio en C# / .NET 10, OpenTK y OpenGL. Este hito **no** incluye relieve, biomas, generación de continentes ni simulación histórica.

**Entorno:** VS Code · .NET 10 LTS · OpenTK 4.9.4 · OpenGL/GLSL · Git.  
**Código local:** `C:\Users\fgabo\Documents\EVOLVE` (carpeta del usuario; repo de documentación distinto: `fgabo404/EvolveDoc`).  
**Estado inicial (21 de octubre de 2026):** ventana 1280 × 720 con fondo azul oscuro y OpenGL inicializado; ejecución mostrada por el usuario. Los demás pasos no están implementados aún.

## Tablero de avance

| Fase | Entregable | Estado | Criterio verificable |
|---|---|---|---|
| 0 | Ventana OpenGL | ✅ Hecho | Aplicación arranca, abre ventana y dibuja fondo sin errores |
| 1 | Núcleo geométrico hexagonal | ⬜ Pendiente | Coordenadas axiales `(q,r)`, vecinos, conversiones a posición y pruebas básicas |
| 2 | Separación de proyectos | ⬜ Pendiente | `GEvolve.Core` independiente de OpenTK y `GEvolve.Desktop` consume sus tipos |
| 3 | Malla base de hexágono | ⬜ Pendiente | Se dibuja **un** hexágono mediante VAO/VBO/EBO + shaders GLSL |
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
