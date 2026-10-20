# G-Evolve — Tecnologías y arquitectura del motor (propuesta v0.1)

**Estado:** decisión de prototipo, no implementación terminada. **Plataforma inicial:** PC Windows. **Fecha:** 2026-10-20.

## Objetivo y restricciones
Construir un motor gráfico propio y un generador procedural reproducible para una simulación histórica sistémica tipo 4X. Estilo aprobado: **Hand-Drawn Isometric Hex World with Progressive Elevation**. Terreno geométrico 3D, cámara ortográfica/isométrica; cuadrícula hexagonal siempre visible, relieve claramente legible y pocos elementos por casilla. No sacrificar la simulación por la representación.

## Tecnologías propuestas por componente

| Componente | Tecnología | Uso / motivo | Estado |
|---|---|---|---|
| Aplicación PC | C# y .NET (versión LTS vigente al implementar) | Ejecutable, herramientas y orquestación | Propuesto |
| Ventana, entrada y contexto gráfico | OpenTK | Crear ventana, recibir ratón/teclado y acceder a OpenGL | Propuesto |
| GPU y renderizado | OpenGL moderno + GLSL | Mallas, buffers, shaders, profundidad, selección y líneas de cuadrícula | Propuesto |
| Matemáticas | System.Numerics | Vectores, matrices, transformaciones de cámara | Propuesto |
| Generación procedural | Biblioteca propia en C# | Semillas deterministas, ruido, elevación, humedad, temperatura y asignación de biomas | Por diseñar |
| Mundo hexagonal | Biblioteca propia en C# | Coordenadas axiales/cúbicas, vecinos, distancias y elevación | Por diseñar |
| Simulación | Biblioteca propia en C# | Estados, turnos/ticks, población, recursos y tecnologías sin dependencia gráfica | Posterior |
| Definiciones de datos | JSON + System.Text.Json | Cargar catálogos del repositorio EvolveDoc como definiciones de solo lectura | Propuesto |
| Contratos y validación | Esquemas JSON y validadores del repositorio | Mantener integridad de IDs, vínculos y compatibilidad | Ya existen parcialmente |
| Pruebas | dotnet test y framework de pruebas C# a definir | Reproducibilidad, vecinos, biomas, serialización, invariantes | Propuesto |
| Depuración gráfica | RenderDoc (opcional) | Captura de fotogramas y diagnóstico de GPU | Opcional |
| Control de versiones | Git + GitHub | Código, documentación, revisiones y trazabilidad | Existente |

**No usar por ahora:** Unity, Unreal, navegador, Vulkan o un editor 3D comercial como dependencia del motor. Modeladores externos podrían utilizarse para crear recursos artísticos sin convertirlos en el motor.

## Diagrama de arquitectura lógica

```text
                    G-Evolve PC / Host
                           |
         +-----------------+-----------------+
         |                                   |
    Input + Camera                       UI / Editor
         |                                   |
         +-----------------+-----------------+
                           |
                 Application Controller
                    /             \
                   /               \
         World / Generation       SimulationEngine
             |                         |
      HexGrid + WorldData         GameState mutable
             |                         |
             +------------+------------+
                          |
                  GameDefinitions
                 JSON de solo lectura
                          |
                Catalogs / Schemas
                          |
        EvolveDoc (data/world, flora, fauna,
          minerales, recursos, tecnologías)
                          
   RenderEngine <--- RenderSnapshot <--- WorldData + GameState
       |
   OpenTK / OpenGL / GLSL
       |
      GPU

   Persistencia: Seed + versión del generador + GameState
```

## Módulos y límites

1. **Host/Desktop:** ciclo de aplicación, configuración, tiempo, entrada y ventana.
2. **Core/HexGrid:** coordenadas axiales `(q,r)`, cúbicas derivadas, vecinos, distancias, identificadores y operaciones deterministas. No depende de OpenTK.
3. **World/Generation:** semilla y parámetros → elevaciones → temperatura/humedad → clasificación de biomas → datos iniciales del mundo. Orden explícito y versiones del generador para reproducibilidad. Los recursos/fauna requieren reglas operativas aprobadas; no inventar distribuciones definitivas.
4. **World/Model:** `WorldData` describe el terreno y atributos estáticos por hexágono; estructuras compactas, consulta por coordenadas y carga por regiones.
5. **Simulation:** `GameDefinitions` define posibilidades; `GameState` guarda estado mutable por partida; `SimulationEngine` ejecuta reglas/ticks sin gráficos, manteniendo el contrato ya documentado.
6. **Rendering:** recibe instantáneas de solo lectura y construye mallas de hexágonos con elevación real; cámara ortográfica, líneas hexagonales siempre visibles, iluminación controlada y sombreado ilustrado. No decide reglas de juego.
7. **Interaction/Editor:** picking de hexágonos, inspección de atributos y controles de semilla/mapa. Modificaciones del editor se aplican a datos, nunca directamente a la GPU.
8. **Persistence:** serializa versión de datos/generador, semilla, opciones y estado. No subir partidas ni cachés al repositorio.

## Flujo de generación

```text
Semilla + tamaño + parámetros (prototipo 20x20)
  -> topología y coordenadas hexagonales
  -> alturas continuas/cuánticas por niveles
  -> humedad y temperatura iniciales
  -> clasificación de biomas, según reglas disponibles
  -> WorldData inmutable para el render
  -> generación de mallas por región + grid visible
  -> selección de hexágonos y panel de diagnóstico
```

Los primeros biomas pueden representarse con colores de diagnóstico. **No activar aún** apariciones o producciones de catálogos guía marcados como no ejecutables. Los 7 biomas/27 variantes documentados son referencias, no reglas completas de generación.

## Convenciones gráficas
- Mallas 3D elevadas sobre base hexagonal; evitar grietas entre hexágonos adyacentes mediante bordes compartidos o un tratamiento geométrico deliberado.
- Cámara **ortográfica inclinada**, rotación controlada, zoom y paneo; no confundir con isometría estricta.
- Cuadrícula dibujada como capa visible aun sobre texturas y decoraciones (pasada de líneas/decal con gestión de profundidad para evitar parpadeos).
- Materiales sobrios, contornos suaves, vegetación y fauna escasas; detalle variable con zoom.
- Mantener datos en coordenadas del mundo independientes de la resolución y la cámara.

## Prototipo mínimo (criterios de aceptación)
- [ ] Inicia una ventana de PC y muestra una cuadrícula **20 × 20 hexágonos**.
- [ ] Muestra varios niveles de altura en geometría 3D y una cámara ortográfica inclinada.
- [ ] La cuadrícula es visible en todos los niveles de zoom.
- [ ] Zoom, paneo y selección muestran coordenadas y altura del hexágono.
- [ ] Misma semilla + mismos parámetros + misma versión producen el mismo `WorldData`.
- [ ] El generador funciona y se prueba sin inicializar OpenGL.
- [ ] El renderizador no escribe directamente en `GameState`.
- [ ] Se visualizan biomas preliminares sin afirmar que los catálogos guía ya sean ejecutables.
- [ ] Pruebas de vecinos, determinismo y serialización superadas.

## Organización futura del código (repositorio Evolve, NO mover catálogos de EvolveDoc)

```text
Evolve/
  src/
    GEvolve.Desktop/
    GEvolve.Core/
    GEvolve.World/
    GEvolve.Simulation/
    GEvolve.Rendering.OpenGL/
    GEvolve.Editor/
    GEvolve.Persistence/
  tests/
    GEvolve.Core.Tests/
    GEvolve.World.Tests/
    GEvolve.Simulation.Tests/
  assets/
    shaders/
    textures/
```

**Dependencias:** Desktop compone módulos; Rendering depende de contratos de Core/World pero no al revés; Simulation depende de Core y definiciones, nunca de OpenGL; Editor interactúa por comandos de aplicación.

## Decisiones abiertas
- LTS exacta de .NET, versión de OpenGL y objetivo mínimo de GPU.
- Si elevación por hexágono representa mesetas escalonadas, interpolación o una mezcla; resolver visualmente en el prototipo.
- Algoritmos concretos de ruido, erosión y clima y sus parámetros.
- Formato definitivo de partidas, estrategia de chunks/LOD y medición de rendimiento.
- Recursos, fauna y fórmulas solo después de completar los contratos de simulación.

**Compatibilidad:** documentación de arquitectura, sin cambios a IDs, JSON existentes, balance, reglas ni catálogos. La simulación manual y los pendientes del roadmap continúan vigentes.
