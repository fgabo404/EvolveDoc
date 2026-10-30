# Línea gráfica — dirección visual de G-Evolve

**Proyecto:** G-Evolve  
**Origen:** exploración del 29 de octubre de 2026; decisión de referencia visual del **30 de octubre de 2026**.  
**Estado:** **dirección artística de referencia seleccionada** para el juego a partir del video aportado por el usuario. Las reglas de producción, tamaños nativos, paletas definitivas y animaciones concretas siguen en fase de prototipado.

## 1. Dirección visual seleccionada

**Referencia principal desde el 30/10/2026:** el **video de jugabilidad compartido por el usuario** (secuencia breve con entorno de isla, agua, arena, palmeras, rocas, personaje, interfaz y acciones de interacción). Se adopta su **lenguaje gráfico general y sensación de fluidez** como guía estética para G-Evolve, **sin copiar sprites, mapas, interfaz ni recursos de terceros**.

- **Pixel art 2D moderno, orgánico y legible**, con masas de color y siluetas claras; más riqueza ambiental que una representación puramente minimalista, pero sin ruido decorativo.
- **Perspectiva cenital elevada**: se ven superficies de suelo y parte de los laterales de rocas, vegetación y construcciones; mantener lectura estratégica desde arriba.
- **Terreno con costas irregulares y transiciones naturales** entre arena, suelo, vegetación y agua; evitar que las cuadrículas o el hexágono estructural aparezcan como bordes rígidos en cada textura.
- **Volumen e iluminación sutiles**: sombreados escalonados, sombras de contacto, pequeñas luces y profundidad de agua. Mantener píxeles definidos y no aplicar desenfoque global al arte.
- **Naturaleza rica pero ordenada**: árboles, rocas, agua y vegetación se reconocen inmediatamente, con variación local y animación discreta cuando corresponda.
- **Movimiento con sensación continua**: interpolar la posición de objetos y cámara entre estados simulados, aunque las animaciones de sprites se compongan de pocos fotogramas.
- **Interfaz con personalidad pixel art**, compacta y jerarquizada, sin sacrificar legibilidad de datos de un juego 4X.

La referencia histórica a **The Escapists 2** sigue siendo útil como inspiración secundaria para la claridad y las proporciones chibi del humano base, **pero el video pasa a guiar la ambientación general, animación percibida y acabado del mundo**. La identidad final y sus assets serán originales de G-Evolve.

**Compatibilidad con el diseño existente:** mantener la referencia aprobada del personaje «Taparrabo» (cabeza grande y cuadrada, torso corto, cuatro orientaciones), sin rediseñarlo por defecto. La integración visual entre personajes, fondos y edificios deberá validarse con bocetos conjuntos. El mundo **no tiene que ser tropical**: este lenguaje gráfico se trasladará a cada bioma histórico/geográfico correspondiente.

## 2. Zoom con cambios de representación

**Idea central:** la representación de un mismo elemento cambia según la distancia de la cámara. No se trata de crear objetos diferentes en la simulación, sino de mostrar versiones visuales adecuadas al nivel de acercamiento.

### Posibles escalas de visualización

| Escala conceptual | Qué debería destacar | Ejemplos |
| --- | --- | --- |
| Estratégica (lejos) | Continentes, biomas, masas de agua, fronteras y ubicaciones de asentamientos | Un mercado aparece como un símbolo sencillo, si corresponde mostrarlo a esa escala. |
| Regional (distancia intermedia) | Poblaciones, rutas, recursos, bosques y edificios reconocibles | El mercado aparece como una construcción simplificada con identificación «Mercado». |
| Detallada (cerca) | Elementos físicos y ambiente local | El mercado puede mostrar puestos, mercancías, entradas, caminos y detalles del entorno. |

Estas **tres escalas son una propuesta de diseño**, no cantidades de zoom fijadas ni un requisito de implementación. Se prefiere explorar una transición progresiva, sin saltos visuales abruptos.

### Ejemplos adicionales

- **Bosque:** área o patrón legible a gran distancia → grupos de árboles → árboles individuales al acercarse.
- **Ciudad:** marca/representación general → edificios y trazado urbano reconocibles → detalles de construcciones y espacios.
- **Terreno:** colores y siluetas que distingan biomas → rasgos más específicos → texturas y detalles pequeños.
- **Elevaciones:** conservar la lectura del relieve en todas las escalas; aún sin decidir cómo representar técnicamente cada rango de altura.

## 3. Ejércitos y unidades militares

- **Interés expreso:** al acercar la cámara a un ejército, que se puedan observar **varias unidades militares desplegadas o representadas en grupo**.
- **Representación simbólica, no individual exacta:** si un ejército contiene 100 unidades en la simulación, **no es necesario dibujar 100 soldados**. Se mostraría un conjunto visual representativo.
- Posibilidad a explorar: un símbolo o ficha estratégica al alejarnos, una formación simplificada a distancia media y varios personajes/soldados pixelados al acercarnos.
- La cantidad de sprites mostrados **no debe interpretarse como la cantidad real de unidades**; la fuerza, composición y tamaño verdaderos deben permanecer en los datos de la simulación y poder consultarse por la interfaz.
- Quedan por investigar el tipo de formación, cómo cambia por época histórica, la variedad de tropas, su escala y las animaciones.

## 4. Habitantes y vida cotidiana: pendiente

La idea de mostrar **NPCs caminando por ciudades o trabajando** (por ejemplo, comerciantes o civiles) se conversó, pero **se deja expresamente pendiente**. No debe registrarse como requisito aprobado.

Esta reserva **no afecta la propuesta de representación visual de ejércitos**: el usuario sí expresó interés en que sus integrantes aparezcan de forma representativa al acercar la cámara.

## 5. Criterios y dudas por resolver

- Conservar una lectura clara de biomas, construcciones y recursos tanto al acercar como al alejar la cámara.
- Evaluar niveles de detalle (LOD) visual y semántico: simplificar o sustituir la forma de representación según el zoom.
- Procurar que las capas visuales no obliguen a representar todos los objetos con máximo detalle al mismo tiempo.
- Investigar resolución interna, tamaño de tiles, paleta, iluminación, animaciones, escala entre ciudades y terrenos, y rendimiento; **solo existe una propuesta de canvas 32×48 px y pivote (16,46) para el humano base, no un estándar global definitivo**.
- Validar cómo se integra con los biomas, subtipos y rangos de altura ya documentados **sin alterarlos**.
- Mantener la distinción entre **datos simulados** y **elementos dibujados** para evitar confundir una representación resumida con el estado real.

## 6. Alcance de esta nota

Se documentan **preferencias expresadas e ideas exploratorias** en la conversación del 29/10/2026. No se aprueba todavía un pipeline gráfico, tecnología de renderizado, tamaño de assets, reglas de cámara, sistema de NPCs ni representación definitiva de los ejércitos.

**Próximo trabajo posible:** comparar referencias visuales y elaborar bocetos de un mismo elemento (mercado, bosque y ejército) visto a distintas distancias, antes de tomar decisiones técnicas.


## 7. Historial de exploración del personaje humano base (no vigente)

En la conversación del 29/10/2026 se estudiaron figuras con camisa, pantalón y mejillas rosadas. Estas versiones ayudaron a explorar la apariencia chibi y la legibilidad, pero **han sido reemplazadas**. No deben usarse como plantilla para nuevos sprites.

También se exploraron personajes de distintas profesiones. Los bocetos de cazador-recolector, agricultor y legionario son **estudios de vestuario sin aprobación como assets definitivos**.

## 8. Referencia maestra vigente: humano con taparrabo

**Estado:** identidad visual del humano base aprobada y cotejada de nuevo con la lámina «Taparrabo» compartida por el usuario el 29/10/2026. La lámina contiene **cuatro orientaciones (frente, espalda, izquierda y derecha) y una vista frontal ampliada**, no cinco direcciones.

El personaje maestro tiene:

- Silueta **chibi muy compacta** y cabeza grande, casi cuadrada, con esquinas escalonadas.
- Cabello oscuro castaño con matices violáceos, dibujado como **una masa sencilla**, no en mechones finos ni con textura ruidosa. Flequillo de escalones claros.
- Cara ancha y plana, ojos verticales negros; **sin rubor, boca, nariz dibujada ni cejas separadas** en el sprite base.
- Torso descubierto y pequeño, brazos cortos y rectos junto al cuerpo, piernas y pies diminutos.
- **Taparrabo marrón como única prenda**, con cintura oscura y caída frontal pequeña y angular.
- Contorno casi negro con leve matiz púrpura; colores planos y sombreado por grupos deliberados de píxeles.
- Cuatro vistas con proporciones coherentes, centro de pies común y sin alterar la anatomía entre oficios.

**Referencia técnica:** [Diseño del personaje humano base](diseno-personaje-humano-base.md), que distingue el **aspecto aprobado** de la **malla provisional de prototipado (32×48 px y pivote 16,46)**. Estas medidas no son un conteo extraído del boceto ilustrado.

El archivo binario original de la lámina compartida en la conversación todavía **no ha sido verificado dentro de este repositorio**. La descripción no sustituye el archivo maestro y no debe confundirse con un spritesheet nativo.

## 9. Consistencia al producir nuevas láminas

1. Priorizar la **lámina «Taparrabo»** sobre bocetos antiguos o reinterpretaciones posteriores; una ficha técnica nueva es una adaptación, no reemplaza la fuente aprobada.
2. En fichas de diseño, separar los personajes de presentación ampliados de los sprites nativos 32×48 px.
3. Mantener iguales cabeza, ojos, cabello, tronco, extremidades y anclaje en todas las orientaciones; cambiar vestuario/equipo solo para oficios futuros.
4. No añadir mejillas rosas, pelo excesivamente detallado, ropa adicional, botas, expresiones o accesorios a la versión base.
5. Conservar pendiente la paleta HEX exacta, sprites transparentes verificables, animaciones, integración con hexágonos y parámetros definitivos del motor.

## 10. Ficha técnica gráfica del humano base: imagen seleccionada (subida pendiente)

El usuario seleccionó la ficha técnica ilustrada del humano base (30/10/2026) como **referencia gráfica documental del personaje**, cotejada visualmente contra la lámina «Taparrabo» compartida anteriormente. La imagen resultante es un **PNG de presentación** de 1536 × 1024 px, que contiene una vista ampliada, cuatro orientaciones, esquema de proporciones, anclaje y paleta indicativa.

**El PNG todavía no se ha subido a este repositorio.** Cuando se incorpore, su destino previsto será `assets/characters/human/g-evolve-humano-base-ficha-tecnica-v1.png`. No enlazar archivos inexistentes ni sustituirlo por un SVG. La ficha sigue siendo ilustrativa y no un atlas de sprites.


## 11. Referencia audiovisual y fluidez (decisión del 30/10/2026)

**Evidencia original:** video MP4 adjunto por el usuario en la conversación del 30/10/2026; **el archivo de video no está incorporado a EvolveDoc**. Observaciones verificadas visualmente: agua con varias tonalidades, costa orgánica, zona de isla con vegetación y palmeras, rocas, personaje pequeño en vista elevada, interfaz pixel art y acciones de interacción. No inferir a partir del video un motor, sistema de cámara, velocidad de simulación, resolución nativa o cantidad de frames por animación.

### 11.1 Principios gráficos que tomamos como guía

| Elemento | Lenguaje visual deseado | Observación para Evolve |
| --- | --- | --- |
| Agua | Variación tonal y vida visual sutil | Cambios de color/ondas que no distraigan de unidades y recursos |
| Costas y suelo | Perfiles escalonados y naturales, sin geometría rígida a la vista | Los hexágonos siguen existiendo para la simulación, pero su retícula se puede ocultar en el render |
| Vegetación | Siluetas reconocibles, paleta rica, agrupación orgánica | Adaptar especies y densidades a los biomas reales y sus catálogos |
| Rocas y recursos | Volúmenes y contrastes claros con sombra de contacto | Representar mineral explotable de acuerdo con datos y escala de zoom |
| Personajes | Sprite compacto, nítido y anclado al suelo | Conservar modelo «Taparrabo» aprobado y sus orientaciones |
| Interacciones | Reacción visual rápida, estados fáciles de reconocer | Activación de animación de trabajo, efectos pequeños y cambio al terminar |
| Interfaz | Paneles pixel art coherentes, texto y recursos bien diferenciados | No ocultar información estratégica ni inventarios por decoración |

### 11.2 Cómo producir la sensación de fluidez (guía, no valores aprobados)

- **Lógica y render separados:** la simulación determina posiciones, estados y acciones; el render interpola posiciones visibles y reproduce animaciones.
- **Movimiento continuo:** personajes o embarcaciones pueden avanzar entre puntos sin saltos visuales; mantener sincronización con la ruta real.
- **Sprites animados:** dibujar secuencias cortas (quieto, caminar, trabajar, recolectar, golpear) y ajustar el timing observando el juego, no solo incrementando los frames.
- **Animación ambiental:** agua, vegetación y efectos de interacción discretos; priorizar lo visible a la escala actual.
- **Cámara:** desplazamiento y zoom suaves, con atención a evitar shimmer y pérdida de nitidez de píxel; comparar interpolación con movimiento alineado a píxeles.
- **Capas de detalle (LOD):** a escala estratégica, mostrar iconos y patrones; a escala cercana, desplegar sprites y microanimaciones; la cantidad dibujada no equivale necesariamente al número de entidades simuladas.

**Parámetros de prueba posibles, todavía no aprobados:** render cercano a 60 FPS cuando el dispositivo lo permita, caminata a 8–12 imágenes/segundo de animación y ciclo de 4–6 poses. Son puntos de partida para experimentar, **no una especificación de producción ni una medición del video**.

### 11.3 Criterios para la primera prueba visual

1. Dibujar un escenario pequeño con costa, agua, vegetación, piedra y una figura humana del modelo aprobado.
2. Representar un desplazamiento breve con animación de pasos y movimiento interpolado; al llegar, reproducir idle.
3. Incluir una acción de recolección/minería con efectos simples y respuesta visual inmediata.
4. Mostrar tres encuadres del mismo lugar (cercano, regional y estratégico), sin obligar a dibujar todos los objetos en el zoom alejado.
5. Validar lectura de recursos, siluetas y contraste sobre distintos biomas, no solo una isla tropical.

**Prioridad para futuras decisiones artísticas:** (1) identidad original aprobada del humano base para anatomía; (2) video para acabado ambiental y sensación de movimiento; (3) reglas de legibilidad/zoom del simulador 4X; (4) propuestas técnicas por validar.

**Referencia del PNG seleccionado:** SHA-256 `a9b6c4ee88e43ae3728ccce7213ee31d170fcf1b5dbabaae97f302d3d5846f53`. No sustituirlo por SVG ni convertir la lámina de presentación en spritesheet. La selección de esta ficha no implica aprobar los diseños exploratorios de otras profesiones.
