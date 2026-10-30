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
- Investigar resolución interna, tamaño de tiles y sprites, paleta, iluminación, animaciones, escala entre ciudades y terrenos, y rendimiento; **ninguno está definido todavía**.
- Validar cómo se integra con los biomas, subtipos y rangos de altura ya documentados **sin alterarlos**.
- Mantener la distinción entre **datos simulados** y **elementos dibujados** para evitar confundir una representación resumida con el estado real.

## 6. Alcance de esta nota

Se documentan **preferencias expresadas e ideas exploratorias** en la conversación del 29/10/2026. No se aprueba todavía un pipeline gráfico, tecnología de renderizado, tamaño de assets, reglas de cámara, sistema de NPCs ni representación definitiva de los ejércitos.

**Próximo trabajo posible:** comparar referencias visuales y elaborar bocetos de un mismo elemento (mercado, bosque y ejército) visto a distintas distancias, antes de tomar decisiones técnicas.


## 7. Personaje humano base — referencia visual seleccionada (29/10/2026)

**Estado: diseño visual base aceptado por el usuario para seguir trabajando, aún no asset de producción.**

Tras comparar varios bocetos, el usuario seleccionó expresamente el personaje de la imagen de referencia que compartió (figura humana pequeña sobre una playa, con cabello castaño oscuro, ojos verticales negros, mejillas rosadas, camisa gris clara y pantalón oscuro). Aprobó el boceto posterior de **un solo personaje en cinco orientaciones** (frente, espalda, perfil izquierdo, perfil derecho y una vista frontal ampliada) como base deseada para G-Evolve.

Rasgos visuales que se deben preservar en próximas iteraciones:
- **Pixel art cenital de apariencia chibi**, con cabeza cuadrada y grande en relación con el cuerpo.
- Ojos oscuros de forma vertical, mejillas levemente rosadas, rostro de pocos píxeles y sin detalle innecesario.
- Cuerpo muy compacto, brazos simples pegados a los costados, piernas cortas y contorno oscuro nítido.
- Proporciones, rostro y silueta compartidos entre todas las profesiones; la vestimenta, los accesorios y el equipo cambiarán sin rediseñar el cuerpo base.
- **Primero trabajar únicamente el personaje base**, separado de terreno y hexágonos; después explorar aldeano, explorador, soldado, etc.

La referencia de estilo sigue siendo **The Escapists 2**, pero los recursos finales deben ser propios de G-Evolve. No confundir este diseño aceptado con las láminas previas de variantes, que no fueron aprobadas como plantilla definitiva.

**Referencia visual:** imagen aportada por el usuario en la conversación del 29/10/2026 y boceto de cinco vistas generado y aprobado en esa misma conversación. Este registro describe el diseño; la imagen binaria no se incorpora aquí todavía.


## 8. Modelo humano base — referencia maestra actualizada

El personaje base aprobado más reciente es **humano con taparrabo marrón, torso descubierto y rostro SIN mejillas rosadas**, con vistas frente/espalda/izquierda/derecha. Sustituye como referencia maestra la versión anterior con rubor. Las variantes de cazador-recolector, agricultor y legionario siguen siendo exploraciones de indumentaria.

**Ficha gráfica y técnica completa:** [Diseño del personaje humano base](diseno-personaje-humano-base.md). Los tamaños nativos, paletas HEX y animaciones siguen pendientes de definición. La imagen del boceto aprobado continúa en la conversación de diseño; el binario todavía no está incorporado a este repositorio.
