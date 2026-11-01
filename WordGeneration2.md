# WordGeneration2 — Generación de mundo por simulación tectónica

> Documento exploratorio independiente. No sustituye el método actual de Evolve ni implica cambios en el código del juego.

## Objetivo

Investigar un segundo generador procedural capaz de producir tres tipos de mundo — **Pangea**, **Continentes** y **Archipiélagos** — mediante procesos tectónicos plausibles, no por el simple dibujo de siluetas terrestres.

**Principio rector:** primero se generan placas tectónicas y materiales de corteza; la disposición final de océanos, continentes e islas debe resultar de su evolución. Un tipo de mundo configura condiciones y criterios de selección, pero no obliga a dibujar directamente una forma predeterminada.

## Etapa 01 — Generación inicial de placas tectónicas

### 1. Separar conceptos

- **Placa tectónica:** pieza móvil y relativamente rígida de litosfera.
- **Corteza:** material transportado por la placa; puede ser continental u oceánico.
- **Continente:** acumulación de corteza continental emergida o sumergida, que puede abarcar porciones de varias placas.
- **Isla:** masa emergida, continental o volcánica; no equivale necesariamente a una placa.
- **Límite tectónico:** contacto entre placas que puede cambiar con el tiempo.

**Regla importante:** ni una placa equivale a un continente ni un continente debe coincidir con una placa.

### 2. Representación del planeta

Se propone modelar una **superficie planetaria cerrada (esfera)** y dividirla en celdas o polígonos de área aproximadamente uniforme. En caso de que Evolve decida utilizar un mapa rectangular con unión horizontal, deberá definirse cómo representar los polos o qué aproximación geométrica se permite: un cilindro periódico no reproduce exactamente una esfera.

Cada celda guarda: identificador de placa, tipo de corteza, edad de corteza, espesor o flotabilidad relativa (cuando se definan), elevación inicial y trazas geológicas. La topología debe permitir localizar vecinas y bordes sin discontinuidades artificiales.

### 3. Crear centros iniciales de placas

1. Elegir de modo determinista, a partir de la semilla, el **número objetivo de placas**. No fijar un número universal: hacerlo configurable por tamaño del planeta y resolución.
2. Distribuir los centros sobre la esfera con **muestreo espacial aproximadamente uniforme**, pero con variación controlada para obtener placas grandes, medianas y pequeñas.
3. Asignar a cada centro un **peso de crecimiento** para producir una distribución desigual de áreas.
4. Expandir regiones mediante **Voronoi geodésico ponderado** o crecimiento por grafo; evitar formas exclusivamente radiales o circulares.
5. Introducir perturbaciones multiescala suaves en los bordes y luego corregir cuellos de botella, islotes de una celda y regiones desconectadas.
6. Conservar una placa como una región continua al inicio (salvo que posteriormente se justifiquen casos excepcionales en el modelo).

> Voronoi es aquí una técnica de partición inicial, **no** una simulación tectónica. La dinámica aparece al mover las placas y transformar sus límites.

### 4. Diversidad de tamaños y formas

Buscar una mezcla de pocas placas extensas, varias intermedias y algunas microplacas; definir proporciones ajustables y no porcentajes fijos por ahora. Las formas deben ser irregulares y conectadas, con bordes de escalas distintas. Evitar tanto polígonos perfectos como costas excesivamente dentadas: **los límites de placas no son costas**.

### 5. Asignar propiedades físicas iniciales

A cada placa:
- ID estable;
- área, geometría y vecinas;
- polo de Euler y velocidad angular (movimiento sobre la esfera);
- categoría descriptiva según composición dominante, **sin** prohibir placas mixtas;
- proporción inicial de corteza continental/oceánica;
- parámetros simplificados de densidad/flotabilidad, cuando corresponda.

A cada región de corteza:
- tipo continental u oceánico;
- edad inicial;
- espesor/flotabilidad relativa;
- identificador de bloque o fragmento continental, si aplica.

La distribución inicial de corteza continental debe generarse **por bloques** que pueden cruzar o no límites de placa; no pintar toda una placa como tierra por defecto.

### 6. Dar movimiento a las placas

Asignar movimientos mediante polos de Euler; la velocidad superficial de cada punto resulta de la rotación de su placa. Calcular la velocidad relativa a lo largo de cada borde y descomponerla en:
- normal convergente → colisión o subducción potencial;
- normal divergente → rift o dorsal potencial;
- tangencial → falla transformante/cizalla.

**No asignar aleatoriamente “convergente/divergente” a cada borde**: el tipo de interacción debe derivarse del movimiento relativo, y podría variar a lo largo de un mismo límite. En esta etapa solo se preparan los movimientos; las consecuencias geológicas se diseñarán después.

### 7. Comprobaciones mínimas

- La totalidad de la superficie pertenece a exactamente una placa.
- Cada placa inicial es conectada y tiene área válida.
- No hay huecos ni superposiciones en la malla.
- Los bordes son compartidos de forma consistente por placas vecinas.
- No aparecen discontinuidades artificiales en la unión del mapa.
- Misma semilla + parámetros + versión del algoritmo = mismos resultados.
- Distribución de tamaños y longitudes de borde razonablemente variada.
- Comprobar que existen suficientes contactos potenciales de convergencia, divergencia y transformantes para una evolución interesante; **sin forzar cada tipo en cada placa**.

### 8. Qué cambia según el tipo de mundo

En esta primera etapa **el algoritmo de generación de placas es el mismo para todos**. Las diferencias pueden aparecer después en la cantidad y distribución de corteza continental inicial, la historia tectónica, el momento temporal de observación y los criterios de aceptación del resultado.

| Mundo | Objetivo geográfico final | Mecanismos que conviene explorar |
| --- | --- | --- |
| **Pangea** | Una masa continental principal | Ensamblaje y suturas de bloques continentales |
| **Continentes** | Varias grandes masas separadas | Rifting, dispersión, colisiones regionales y océanos abiertos |
| **Archipiélagos** | Predominio oceánico y numerosas islas | Arcos insulares, fragmentación, microcontinentes y puntos calientes |

**Advertencia:** no se consigue un archipiélago solamente aumentando el número de placas, ni Pangea reduciéndolo.

### 9. Secuencia conceptual propuesta

```text
Semilla + configuración planetaria
        ↓
Superficie y malla
        ↓
Centros y tamaños de placas
        ↓
Partición inicial y bordes irregulares
        ↓
Distribución de corteza continental y oceánica
        ↓
Polos de Euler y velocidades
        ↓
Cálculo de contactos e interacciones
        ↓
Estado tectónico inicial listo para evolucionar
```

### 10. Decisiones pendientes para la siguiente conversación

1. ¿Simularemos una esfera completa o una aproximación de mapa plano con unión horizontal?
2. ¿Qué rango de placas y microplacas queremos por tamaño de planeta?
3. ¿La corteza inicial será distribuida aleatoriamente por bloques o partiremos de configuraciones de corteza geológicamente motivadas?
4. ¿Durante cuántos millones de años evolucionará el sistema y con qué pasos adaptativos?
5. ¿Cómo se crean, fusionan, fragmentan y consumen placas conforme evoluciona el planeta?

**Alcance de esta versión:** solo diseño de la **etapa 01: placas iniciales**. No se implementan todavía movimiento evolutivo, subducción, formación de continentes, relieve, erosión, clima ni biomas.
