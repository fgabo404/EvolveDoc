# Línea gráfica — lluvia de ideas

**Proyecto:** G-Evolve  
**Fecha de conversación:** 29 de octubre de 2026  
**Estado:** Exploración conceptual / lluvia de ideas. **No es una especificación artística ni técnica definitiva.**

## 1. Dirección visual que estamos explorando

- Referencia artística preferida: **The Escapists 2**, especialmente su estilo de **pixel art moderno, limpio y detallado**, visto desde una perspectiva elevada/cenital.
- Preferencia por una apariencia **minimalista y clara**, capaz de comunicar información del mundo sin excesivo ruido visual.
- La intención es **inspirarse** en la claridad, las proporciones y el enfoque visual de esa referencia, desarrollando una identidad propia para G-Evolve; no reproducir sus recursos gráficos.
- Considerar perspectivas que permitan ver partes laterales de edificios, árboles y otros elementos sin perder la lectura del mapa desde arriba.
- El proyecto es un simulador histórico sistémico con formato 4X, por lo que la legibilidad estratégica es tan importante como el detalle de los objetos.

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

## 10. Ficha de presentación PNG: incorporación pendiente

Se preparó una nueva ficha técnica ilustrada del humano base (29/10/2026), cotejada visualmente contra la lámina «Taparrabo» compartida por el usuario. La imagen resultante es un **PNG de presentación** de 1536 × 1024 px, que contiene una vista ampliada, cuatro orientaciones, esquema de proporciones, anclaje y paleta indicativa.

**El PNG todavía no se ha subido a este repositorio.** Cuando se incorpore, su destino previsto será `assets/characters/human/g-evolve-humano-base-ficha-tecnica-v1.png`. No enlazar archivos inexistentes ni sustituirlo por un SVG. La ficha sigue siendo ilustrativa y no un atlas de sprites.
