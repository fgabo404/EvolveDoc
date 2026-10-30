# G-Evolve — Especificación artística del personaje humano base

**Fecha:** 29 de octubre de 2026  
**Estado:** REFERENCIA VISUAL APROBADA — especificaciones de producción propuestas, sujetas a validación.  
**Alcance:** personaje humano base sin clase, sin armas ni profesión, vestido **únicamente con taparrabo**.  
**Referencia maestra:** última lámina de la conversación del 29/10/2026, denominada *Taparrabo*, **versión sin mejillas rosadas**. Imagen de frente ampliada en el centro y vistas frente, espalda, izquierda y derecha alrededor. Esta imagen es la referencia visual aprobada; el archivo binario aún requiere incorporación al repositorio.

## 1. Identidad del diseño

El humano base de G-Evolve es un personaje **pixel art 2D de escala reducida, lectura cenital elevada y silueta chibi compacta**. Su función es ser el modelo compartido a partir del cual se crean aldeanos, agricultores, cazadores-recolectores, exploradores, soldados y otros oficios sin modificar arbitrariamente anatomía o rostro.

Inspiración visual declarada: *The Escapists 2*. Es una **referencia estética** de lectura y proporciones, no una autorización para reutilizar sprites ni una exigencia de copiar píxel a píxel diseños de terceros. Los assets finales serán propios de G-Evolve.

**Decisión de diseño confirmada:** la última revisión elimina **por completo los píxeles rosados de las mejillas**. Las versiones anteriores con rubor no son el nuevo modelo de referencia.

## 2. Anatomía, silueta y proporciones

### 2.1 Silueta

- **Cabeza:** gran volumen predominantemente cuadrado con esquinas suavizadas por escalones de píxeles; debe seguir siendo el punto focal.
- **Cabello:** masa oscura castaño-violeta que envuelve parte superior y laterales del cráneo; mechones representados como escalones de bloques, sin hebras finas.
- **Rostro:** plano amplio, limpio, tono piel cálido; ojos verticales oscuros, sin boca ni nariz explícitas en el tamaño base.
- **Cuello:** prácticamente omitido; la cabeza se conecta visualmente al torso mediante una banda corta de sombra.
- **Tronco:** corto y estrecho, pecho descubierto, sombreado muy discreto con unos pocos píxeles cálidos.
- **Brazos:** cortos, colocados a cada lado; las manos se sugieren como bloques claros, sin dedos definidos.
- **Piernas:** muy cortas y separadas por un pequeño hueco oscuro; pies simplificados y alineados con la base del sprite.
- **Taparrabo:** prenda marrón de fibras/piel/tela tosca, ceñida a la cintura, con caída frontal pequeña e irregular; es la **única prenda** en la versión base. No añadir pantalones largos, camisa, sandalias ni accesorios.
- **Contorno:** línea exterior oscura continua de grosor aparente uniforme, escalonada en la cuadrícula de píxeles.

### 2.2 Relaciones de escala

Relaciones cualitativas observadas en la lámina aprobada:
- Cabeza visiblemente mayor que torso y piernas juntos, aunque la proporción exacta debe medirse sobre un sprite auténtico.
- Ancho de cabeza superior al del torso.
- Brazos sin prolongarse mucho por debajo de la cadera.
- Pies cortos con sombra inferior compacta.

**No son medidas cerradas:** la lámina actual es una ilustración conceptual escalada, **no** un sprite sheet con celdas verificadas. No se asignan dimensiones nominales 16×16/24×32/32×32 ni coordenadas de píxel como si ya estuvieran aprobadas.

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

La referencia aprobada utiliza:
- **Cabello:** castaño oscuro con sombras violáceas y reflejos marrón-vino.
- **Piel:** melocotón cálido, luces crema/anaranjadas y sombras ocre suaves.
- **Taparrabo:** marrones medios y oscuros; ligera diferencia entre cintura, pliegue central y borde.
- **Contorno:** casi negro con matiz púrpura.
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
- [ ] Sprite nativo editable, con transparencia, tamaño/celda definidos.
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
