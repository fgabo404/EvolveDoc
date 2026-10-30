# G-Evolve — Especificación artística del personaje humano base

**Fecha:** 29 de octubre de 2026  
**Estado:** REFERENCIA VISUAL APROBADA Y COTEJADA CON LA LÁMINA ORIGINAL RECOMPARTIDA — contrato dimensional v0.1 provisional para prototipado (medidas diseñadas, no extraídas de píxeles del boceto).  
**Alcance:** personaje humano base sin clase, sin armas ni profesión, vestido **únicamente con taparrabo**.  
**Referencia maestra:** última lámina de la conversación del 29/10/2026, denominada *Taparrabo*, **versión sin mejillas rosadas**. Imagen de frente ampliada en el centro y vistas frente, espalda, izquierda y derecha alrededor. Esta imagen es la referencia artística maestra. La lámina se volvió a compartir en la conversación el 29/10/2026; **no hay verificación de un archivo binario correspondiente en este repositorio**.

## 1. Identidad del diseño

El humano base de G-Evolve es un personaje **pixel art 2D de escala reducida, lectura cenital elevada y silueta chibi compacta**. Su función es ser el modelo compartido a partir del cual se crean aldeanos, agricultores, cazadores-recolectores, exploradores, soldados y otros oficios sin modificar arbitrariamente anatomía o rostro.

Inspiración visual declarada: *The Escapists 2*. Es una **referencia estética** de lectura y proporciones, no una autorización para reutilizar sprites ni una exigencia de copiar píxel a píxel diseños de terceros. Los assets finales serán propios de G-Evolve.

**Decisión de diseño confirmada:** la última revisión elimina **por completo los píxeles rosados de las mejillas**. Las versiones anteriores con rubor no son el nuevo modelo de referencia.

## 2. Anatomía, silueta y proporciones

### 2.1 Silueta

- **Cabeza:** gran volumen casi cuadrado, visualmente dominante, con coronilla relativamente plana y esquinas escalonadas; evitar estrecharla, redondearla excesivamente o alargar el rostro.
- **Cabello:** bloque compacto castaño-violáceo oscuro con parte superior bastante limpia y flequillo frontal de pocos escalones anchos; preferir 2–3 masas tonales claras antes que mechones, motas o brillo excesivo.
- **Rostro:** plano amplio y despejado de piel cálida, dos ojos negros verticales sencillos con separación amplia; sin boca, nariz, cejas separadas, reflejos o rubor en el tamaño base.
- **Cuello:** prácticamente omitido; la cabeza se conecta visualmente al torso mediante una banda corta de sombra.
- **Tronco:** corto y estrecho, pecho descubierto, sombreado muy discreto con unos pocos píxeles cálidos.
- **Brazos:** cortos, casi rectos y pegados a los lados del torso; manos como bloques simples, sin dedos ni articulaciones detalladas.
- **Piernas:** muy cortas, de pocos bloques, separadas por un hueco oscuro; pies descalzos cuadrados o ligeramente rectangulares, sin botas ni calzado.
- **Taparrabo:** banda de cintura marrón oscura con faldón corto central, irregular y angular (lectura aproximada de pequeño triángulo escalonado); es la **única prenda**. No añadir pantalones, camisa, sandalias ni accesorios.
- **Contorno:** línea exterior oscura continua de grosor aparente uniforme, escalonada en la cuadrícula de píxeles.

### 2.2 Relaciones de escala

Relaciones cualitativas observadas en la lámina aprobada:
- Cabeza visiblemente mayor que torso y piernas juntos, aunque la proporción exacta debe medirse sobre un sprite auténtico.
- Ancho de cabeza superior al del torso.
- Brazos sin prolongarse mucho por debajo de la cadera.
- Pies cortos con sombra inferior compacta.

**Actualización:** se establece una cuadrícula de trabajo **32×48 px** para prototipado, detallada en la sección 11. Estas son especificaciones **diseñadas a partir de la referencia**, no mediciones exactas del PNG conceptual.

## 3. Rasgos faciales

| Elemento | Regla aprobada o inferida del prototipo |
| --- | --- |
| Ojos | Dos trazos verticales negros, separados simétricamente en la vista frontal |
| Boca | Ausente o no representada; no introducir expresión por defecto |
| Nariz | No visible |
| Mejillas | **Sin rosado, sin puntos de rubor**; usar únicamente el color de piel y sombras naturales |
| Cejas | No se representan como trazos separados |
| Orejas | Pueden insinuarse con un pixel o bloque lateral en perfiles |
| Expresión | Neutral, legible, amistosa sin infantilizar en exceso |

El rostro debe conservar su lectura a escala de mapa. Evitar añadir gradientes, ruido, líneas finas o muchos tonos.

## 4. Paleta, luz y sombreado

La referencia aprobada, verificada visualmente contra la lámina «Taparrabo», utiliza:
- **Cabello:** castaño oscuro con sombra violeta/casi negra y una zona de luz marrón-vino discreta; masas amplias, sin punteado decorativo.
- **Piel:** melocotón cálido bastante uniforme, con sombra ocre mínima en cuello, torso y extremidades; rostro especialmente limpio.
- **Taparrabo:** marrones medios y oscuros; cinturilla contrastada, pequeña caída angular y solo los pliegues necesarios para reconocerla.
- **Contorno:** casi negro con matiz púrpura, continuo y nítido, sin grosor aparente excesivo.
- **Fondo de la lámina:** blanco marfil, **solo para exhibición**, no integra el sprite.

### Propuesta técnica de producción (NO aprobada)

Usar una paleta indexada reducida por material: contorno, sombra, color base y luz; preferir **3–4 valores tonales** por material, con ajustes si se pierde legibilidad. Evitar degradados, blur y antialiasing. Los códigos HEX precisos deberán extraerse y normalizarse durante la fase de arte final, no inventarse a partir de una captura escalada.

Iluminación sugerida: luz ambiental ligeramente superior-izquierda; sombra hacia partes inferiores/derechas, coherente entre orientaciones. La iluminación tampoco está fijada como requisito definitivo.

## 5. Vistas de orientación — contrato gráfico

El prototipo aprobado muestra:
1. **Frente / abajo:** rostro completo, ambos ojos, torso descubierto, taparrabo y separación entre pies.
2. **Espalda / arriba:** cabello como masa posterior, hombros y parte posterior del taparrabo; no dibujar rasgos faciales.
3. **Perfil izquierdo:** un solo ojo vertical, nariz no detallada, silueta de cabello coherente y torso estrecho.
4. **Perfil derecho:** correspondencia anatómica con el izquierdo; mantener la dirección correcta de los accesorios si se agregan después.

Las cuatro direcciones deben conservar **la misma altura aparente, volumen y anclaje de pies**. Un espejo horizontal puede ser una técnica útil para un prototipo, pero el arte final deberá revisarse cuando el vestuario/equipo sea asimétrico.

## 6. Modulación del vestuario y futuros oficios

El personaje humano base será el **soporte común** de las futuras unidades. Los cambios de oficio o época afectan capas visuales y objetos, no la identidad anatómica.

**Capas conceptuales sugeridas** (arquitectura visual aún no implementada):
1. Cuerpo y tono de piel.
2. Cabello y posibles estilos.
3. Prenda inferior base (taparrabo en este prototipo).
4. Indumentaria superior, túnica o armadura.
5. Casco/sombrero y otros accesorios de cabeza.
6. Equipo de manos: herramienta, arma, escudo.
7. Equipo posterior: mochila, carcaj, capa.

Ejemplos de variantes exploradas previamente: cazador-recolector, agricultor primitivo y legionario romano. **Sus láminas previas son estudios**, no reemplazan el modelo humano base aceptado.

## 7. Reglas de pixel art para el artista

- Mantener una **cuadrícula de píxeles consistente** por sprite y escalado **nearest-neighbor** al ampliar.
- Usar grupos de píxeles intencionales: evitar píxeles aislados como ruido decorativo.
- Cerrar y limpiar la silueta para permitir lectura sobre pasto, arena, nieve, bosque y agua.
- Mantener ojos, línea de cabello y taparrabo distinguibles incluso con el sprite reducido.
- Conservar contraste suficiente entre piel, cabello, prenda y fondo.
- No deformar el sprite al cambiar de orientación.
- No incluir rubor rosado en ninguna dirección.
- Priorizar claridad sobre microdetalles anatómicos.
- Evitar que armas/ropa oculten por completo la silueta compartida.
- El borde hexagonal es una **capa de terreno independiente**: no dibujarlo dentro del sprite humano base.

## 8. Guía de implementación (propuesta, no decisión)

**Formatos propuestos:** PNG con transparencia y, para autoría, archivo editable por capas (p. ej. Aseprite o equivalente). La lámina JPG/PNG con rótulos no es un atlas de sprites listo para producción.

**Posicionamiento:** establecer un *pivot* estable en el punto medio de los pies para todas las direcciones y profesiones; permitir que la cabeza sobrepase la mitad superior de un hexágono cuando resulte necesario.

**Animaciones candidatas:** idle, caminar por dirección, trabajar, recolectar, atacar y recibir daño. Ninguna secuencia de fotogramas ni FPS ha sido aprobada todavía.

**Pruebas visuales futuras:** comparar los cuatro ángulos en un único tamaño nativo; verificar lectura en hexágono, contraste sobre distintos biomas y consistencia con zoom regional/estratégico.

## 9. Criterios de aceptación de esta referencia

- [x] Personaje humano base con cabeza grande y cuerpo compacto.
- [x] Cabello oscuro y ojos negros verticales.
- [x] Rostro sin rubor rosado.
- [x] Única indumentaria: taparrabo marrón.
- [x] Presentación conceptual en frente, espalda, izquierda y derecha.
- [x] Referencia visual seleccionada por el usuario.
- [x] Tamaño y distribución de píxeles propuestos y documentados para prototipado (32×48 px).
- [ ] Sprite nativo editable y transparente dibujado conforme a dichas medidas.
- [ ] Paleta HEX normalizada.
- [ ] Sprites animados verificables por frames.
- [ ] Incorporación del archivo PNG original dentro de EvolveDoc.
- [ ] Diseño aprobado de cada oficio a partir de esta base.

## 10. Control de cambios

- **29/10/2026:** se selecciona primero un personaje base similar al pequeño personaje de playa aportado por el usuario.
- **29/10/2026:** se exploran vestimentas de cazador-recolector, agricultor primitivo y legionario romano.
- **29/10/2026:** se genera una variante con solo taparrabo.
- **29/10/2026:** se solicita quitar el rosado de la cara; esta **última variante pasa a ser la referencia artística maestra actual**.
- **29/10/2026:** se redacta esta ficha técnica para consulta y futuras iteraciones.

> **Nota de alcance:** «aprobada» se refiere a la dirección visual de este boceto, no a medidas pixel-perfect, spritesheets finales, animaciones o código de render.


## 11. Contrato dimensional v0.1 — pixel art de producción (29/10/2026)

### 11.1 Naturaleza de las medidas

**Esta sección es una especificación de dibujo implementable**, construida como aproximación al boceto final sin rubor y contrastada visualmente con la lámina que volvió a compartir el usuario. No es un conteo exacto de sus píxeles: el PNG compartido es una lámina ampliada con texto, escala editorial y suavizados propios de la generación de imagen. Para poder producir un atlas consistente se adopta **una resolución nativa de trabajo** y regiones explícitas. La validación posterior puede dar lugar a v0.2, pero toda variante v0.1 debe reutilizar esta misma malla.

- **Canvas lógico por pose:** 32 px de ancho × 48 px de alto, RGBA con transparencia exterior.
- **Sistema de coordenadas:** (0,0) arriba a la izquierda; X crece a la derecha, Y hacia abajo; intervalos indicados **inclusivos**.
- **Bounding box máximo visible:** X=2..29 (28 px), Y=1..46 (46 px); 2 px mínimos de aire lateral antes de accesorios externos, 1 px arriba y abajo.
- **Pivot de suelo:** (16,46), centro horizontal de los pies; las cuatro orientaciones deben compartirlo.
- **Posición de los ojos en la pose frontal:** centros aproximados X=12 y X=20, Y=19–21. Cada ojo: 2×4 px negros, sin reflejos ni rosado.
- **Contorno:** grosor básico 1 píxel nativo; reforzar a 2 solo si una masa o superposición lo requiere, sin dar aspecto de línea gruesa uniforme.
- **Escalado de visualización:** ×2, ×3 o ×4 por vecino más cercano, sin antialiasing. La vista ampliada **no cambia los píxeles nativos**.

### 11.2 Mapa anatómico nominal — frente

| Zona | Rango X (inclusive) | Rango Y (inclusive) | Dimensión de referencia | Observación |
| --- | --- | --- | --- | --- |
| Cabello y cabeza total | 3..28 | 1..26 | 26×26 px | Silueta cuadrada con esquinas escalonadas; incluye cabello y cara |
| Área facial visible | 6..25 | 10..25 | 20×16 px | Plano cálido, limpio; sin mejillas rosadas |
| Torso (sin brazos) | 9..22 | 27..38 | 14×12 px | Pecho desnudo, hombros compactos |
| Brazo izquierdo visual | 4..8 | 29..37 | 5×9 px | Referencia de postura neutra, mano incluida |
| Brazo derecho visual | 23..27 | 29..37 | 5×9 px | Espejado funcional de la pose base |
| Taparrabo | 9..22 | 36..42 | 14×7 px | Bordes marrones escalonados, caída frontal |
| Pierna/pie izquierdo visual | 10..15 | 41..46 | 6×6 px | Diferenciar del taparrabo por tono/sombra |
| Pierna/pie derecho visual | 17..22 | 41..46 | 6×6 px | Hueco central de aproximadamente 1 px |

**Nota:** Las regiones son *cajas de diseño* y se solapan deliberadamente (cabello/cara; torso/taparrabo; taparrabo/piernas). No son rectángulos macizos ni máscaras de colisión. Las formas definitivas se dibujan dentro de esos rangos, sin bloquear el contenido de otras capas.

### 11.3 Proporciones paramétricas de referencia

Se expresan en relación con la **altura visible nominal de 46 px** (Y=1..46) y el ancho visible máximo de 28 px:

| Relación | Cálculo | Valor aproximado |
| --- | --- | --- |
| Altura de cabeza / altura visible | 26/46 | **56.5 %** |
| Altura de torso / altura visible | 12/46 | **26.1 %** |
| Altura de piernas/pies visibles / altura visible | 6/46 | **13.0 %** |
| Ancho cabeza / ancho máximo visible | 26/28 | **92.9 %** |
| Ancho torso / ancho cabeza | 14/26 | **53.8 %** |
| Ancho taparrabo / ancho cabeza | 14/26 | **53.8 %** |
| Ancho de cada brazo / ancho cabeza | 5/26 | **19.2 %** |
| Altura taparrabo / altura visible | 7/46 | **15.2 %** |

Los porcentajes de alturas **no se suman**: hay solapamiento entre capas, cuello implícito y regiones separadas por contornos. La cabeza debe seguir dominando visualmente la silueta.

### 11.4 Reglas de alineación, direcciones y compatibilidad

- **Frente:** ojos visibles, rostro frontal simétrico, taparrabo frontal.
- **Espalda:** misma altura, ancho y pivot; sustituir plano facial por cabello posterior; caída posterior de taparrabo.
- **Izquierda y derecha:** cabeza de altura equiparable, **un** ojo visible, perfil simplificado; mantener el centro de masa y el pie en el mismo pivot. Proporciones X exactas del perfil se ajustarán al dibujar; no escalar el cuerpo arbitrariamente.
- **Variantes de vestuario:** todas parten del *mismo canvas* 32×48 y del mismo pivot; casco, escudo, lanza o mochila pueden requerir una **capa/atlas de equipo con margen extra**, sin redimensionar el cuerpo base.
- **Orden de capas propuesto:** cuerpo → taparrabo/prendas → cabello/casco → accesorios según la dirección; decidir occlusión por escena.
- **Animaciones:** cada fotograma mantiene el canvas 32×48 y pivot (16,46). Si un movimiento exige sobresalir, conservar la referencia de pies y usar atlas de efectos separado.
- **Hexágono:** el hex es una entidad/visualización independiente. El tamaño del hex mundial **no queda definido** por los 32×48 del personaje; para evitar saturación, ajustar zoom/representación de unidades sin deformar sprite.

### 11.5 Criterios verificables del primer sprite real

1. Crear cuatro PNG RGBA (frente, espalda, izquierda, derecha), **32×48 px cada uno**, con canal alfa exterior.
2. Comprobar dimensiones exactas, pivot común (16,46), ausencia de píxeles de rubor y contorno coherente.
3. Comprobar que las regiones de cara, prenda y cabello se reconocen a escala ×1 y ×2.
4. Probar cuatro fondos contrastados, especialmente playa/pasto/bosque/nieve, antes de cerrar los colores.
5. Exportar una hoja 4×1 de **128×48 px** sin padding solo para revisión técnica; una hoja de presentación con rótulos, ilustraciones ampliadas y anotaciones se genera aparte, **sin presentarla como atlas pixel-perfect**.
6. Evaluar el tamaño visual sobre hexágonos con uno y varios personajes representativos; **no** fijar aquí aforo, tamaño de hex ni reglas de simulación.

**Advertencia de trazabilidad:** «medidas de producción propuestas» ≠ «pixelado exacto de la lámina aprobada». El usuario aprobó la **apariencia** del personaje; esta sección materializa dimensiones iniciales razonadas para diseñar sprites reproducibles y podrá cambiar tras inspección visual del primer asset nativo.

## 12. Comprobación con la lámina original «Taparrabo» (29/10/2026)

La imagen original se volvió a compartir en la conversación y confirma **una vista frontal central ampliada y cuatro vistas pequeñas**: frente (arriba izquierda), espalda (arriba derecha), izquierda (abajo izquierda) y derecha (abajo derecha). La vista central **no constituye una quinta orientación**.

### 12.1 Correcciones sobre la primera ficha técnica ilustrativa

| Rasgo | Ajuste para las próximas fichas |
| --- | --- |
| Cabeza | Más cuadrada y dominante; coronilla y mejillas angulares, no cráneo redondeado o estrecho |
| Cabello | Silueta compacta y simple, flequillo de pocos escalones, brillo mucho más reducido |
| Ojos | Dos rectángulos negros verticales sin brillos, centrados en un rostro amplio, despejado y neutro |
| Cuerpo | Torso más bajo y corto; brazos rectos pegados a los costados, piernas y pies mínimos |
| Vestimenta | Únicamente taparrabo marrón pequeño, con banda de cintura y faldón angular; pies descalzos |
| Color y contorno | Tonos planos, sombra moderada y borde casi negro/púrpura; nada de texturas minuciosas ni rubor |
| Espalda y perfiles | Mismo tamaño y volumen; espalda sin rostro y perfiles con solo un ojo visible |

**Prioridad de referencias:** (1) lámina original aprobada «Taparrabo» → (2) reglas artísticas descritas aquí → (3) contrato dimensional v0.1 sujeto a validación. Si una ficha nueva difiere del boceto original, se corrige la ficha, no la identidad aprobada.

### 12.2 Qué no se debe afirmar todavía

- La ficha ilustrada o generada no es un spritesheet producido a escala nativa.
- Las coordenadas y cajas de la sección 11 **siguen siendo propuestas**: no se deben anunciar como mediciones pixel-perfect de la lámina original.
- No están fijados los códigos HEX exactos, la paleta maestra, las animaciones ni los oficios.
- El documento refleja una **imagen visualizada en la conversación**; el PNG maestro aún requiere incorporación verificable a `EvolveDoc`.

**Siguiente validación:** dibujar los cuatro PNG RGBA nativos 32×48 con el pivote común, compararlos uno a uno con la lámina original y ajustar el contrato a v0.2 únicamente después de validar el resultado.
