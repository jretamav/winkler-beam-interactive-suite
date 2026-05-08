# Prompts del estudio de ablación

Este archivo contiene los **8 prompts únicos** que componen el experimento (4 casos × 2 condiciones), aplicados al modelo **Gemini 3.1 Pro** para un total de 8 sesiones.

**Instrucciones de uso:**

1. Abre una sesión limpia en gemini.google.com.
2. Localiza abajo el bloque correspondiente al caso y condición.
3. Copia desde la línea inmediatamente posterior al encabezado `>>> COPIAR DESDE AQUÍ` hasta la línea inmediatamente anterior al encabezado `<<< HASTA AQUÍ`.
4. Pega como primer mensaje. No añadas nada antes ni después.
5. Espera la respuesta completa del modelo y archívala según el protocolo descrito en `README.md`.

---

## C1 — Viga infinita Winkler con carga puntual centrada

### C1 · Sin andamiaje (minimal)

>>> COPIAR DESDE AQUÍ

Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x).

<<< HASTA AQUÍ

### C1 · Con andamiaje (scaffolded)

>>> COPIAR DESDE AQUÍ

Actúa como un experto en ingeniería estructural y mecánica de sólidos. Antes de resolver el problema que se te planteará al final, adopta y respeta estrictamente las siguientes convenciones físicas y notacionales:

1. SISTEMA GLOBAL DE COORDENADAS: el eje x es positivo hacia la derecha y el eje y es positivo hacia arriba. Por la regla de la mano derecha, todo giro o momento en sentido antihorario es positivo.

2. CONVENCIÓN POR DEFORMACIÓN para un elemento diferencial de longitud dx:
   - En la cara izquierda (en x): el cortante V apunta hacia arriba y el momento flexionante M actúa en sentido horario.
   - En la cara derecha (en x+dx): el cortante V apunta hacia abajo y el momento flexionante M actúa en sentido antihorario.
   - La carga externa distribuida q(x) actúa hacia abajo.
   - La fuerza de reacción del medio elástico actúa hacia arriba.

3. CURVATURA: un momento positivo M genera compresión en la fibra superior y tracción en la fibra inferior (concavidad hacia arriba).

4. REACCIONES: al inicio de la solución del problema, todas las reacciones incógnitas deben tomarse actuando en su sentido positivo conforme al sistema descrito.

5. PROCEDIMIENTO ANALÍTICO: plantea las ecuaciones de equilibrio en un elemento diferencial dx, expande las funciones V(x+dx) y M(x+dx) en series de Taylor truncadas a primer orden, deriva la ecuación diferencial gobernante, resuelve la ecuación característica usando variable compleja cuando proceda, y aplica las condiciones de frontera del problema con coherencia matemática.

6. NOTACIÓN MATEMÁTICA: usa yuxtaposición para multiplicación de variables (qb, Pa, M0L). Para distancias usa literales simples. Reserva L mayúscula para el claro total.

Una vez asimiladas estas convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x).

<<< HASTA AQUÍ

---

## C2 — Viga infinita Winkler con carga puntual descentrada

### C2 · Sin andamiaje (minimal)

>>> COPIAR DESDE AQUÍ

Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en la posición x = a, donde a es una distancia conocida medida hacia la derecha del origen.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), válidas para todo x perteneciente al intervalo (-infinito, +infinito).

<<< HASTA AQUÍ

### C2 · Con andamiaje (scaffolded)

>>> COPIAR DESDE AQUÍ

Actúa como un experto en ingeniería estructural y mecánica de sólidos. Antes de resolver el problema que se te planteará al final, adopta y respeta estrictamente las siguientes convenciones físicas y notacionales:

1. SISTEMA GLOBAL DE COORDENADAS: el eje x es positivo hacia la derecha y el eje y es positivo hacia arriba. Por la regla de la mano derecha, todo giro o momento en sentido antihorario es positivo.

2. CONVENCIÓN POR DEFORMACIÓN para un elemento diferencial de longitud dx:
   - En la cara izquierda (en x): el cortante V apunta hacia arriba y el momento flexionante M actúa en sentido horario.
   - En la cara derecha (en x+dx): el cortante V apunta hacia abajo y el momento flexionante M actúa en sentido antihorario.
   - La carga externa distribuida q(x) actúa hacia abajo.
   - La fuerza de reacción del medio elástico actúa hacia arriba.

3. CURVATURA: un momento positivo M genera compresión en la fibra superior y tracción en la fibra inferior (concavidad hacia arriba).

4. REACCIONES: al inicio de la solución del problema, todas las reacciones incógnitas deben tomarse actuando en su sentido positivo conforme al sistema descrito.

5. PROCEDIMIENTO ANALÍTICO: plantea las ecuaciones de equilibrio en un elemento diferencial dx, expande las funciones V(x+dx) y M(x+dx) en series de Taylor truncadas a primer orden, deriva la ecuación diferencial gobernante, resuelve la ecuación característica usando variable compleja cuando proceda, y aplica las condiciones de frontera del problema con coherencia matemática.

6. NOTACIÓN MATEMÁTICA: usa yuxtaposición para multiplicación de variables (qb, Pa, M0L). Para distancias usa literales simples. Reserva L mayúscula para el claro total.

Una vez asimiladas estas convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en la posición x = a, donde a es una distancia conocida medida hacia la derecha del origen.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), válidas para todo x perteneciente al intervalo (-infinito, +infinito).

<<< HASTA AQUÍ

---

## C3 — Viga finita Winkler con extremos libres y carga puntual al centro

### C3 · Sin andamiaje (minimal)

>>> COPIAR DESDE AQUÍ

Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud finita L, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. Ambos extremos de la viga, en x = 0 y en x = L, son libres (no existen reacciones externas en los extremos). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en el centro de la viga, es decir, en x = L/2.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), aplicando explícitamente las cuatro condiciones de frontera correspondientes a los extremos libres.

<<< HASTA AQUÍ

### C3 · Con andamiaje (scaffolded)

>>> COPIAR DESDE AQUÍ

Actúa como un experto en ingeniería estructural y mecánica de sólidos. Antes de resolver el problema que se te planteará al final, adopta y respeta estrictamente las siguientes convenciones físicas y notacionales:

1. SISTEMA GLOBAL DE COORDENADAS: el eje x es positivo hacia la derecha y el eje y es positivo hacia arriba. Por la regla de la mano derecha, todo giro o momento en sentido antihorario es positivo.

2. CONVENCIÓN POR DEFORMACIÓN para un elemento diferencial de longitud dx:
   - En la cara izquierda (en x): el cortante V apunta hacia arriba y el momento flexionante M actúa en sentido horario.
   - En la cara derecha (en x+dx): el cortante V apunta hacia abajo y el momento flexionante M actúa en sentido antihorario.
   - La carga externa distribuida q(x) actúa hacia abajo.
   - La fuerza de reacción del medio elástico actúa hacia arriba.

3. CURVATURA: un momento positivo M genera compresión en la fibra superior y tracción en la fibra inferior (concavidad hacia arriba).

4. REACCIONES: al inicio de la solución del problema, todas las reacciones incógnitas deben tomarse actuando en su sentido positivo conforme al sistema descrito.

5. PROCEDIMIENTO ANALÍTICO: plantea las ecuaciones de equilibrio en un elemento diferencial dx, expande las funciones V(x+dx) y M(x+dx) en series de Taylor truncadas a primer orden, deriva la ecuación diferencial gobernante, resuelve la ecuación característica usando variable compleja cuando proceda, y aplica las condiciones de frontera del problema con coherencia matemática.

6. NOTACIÓN MATEMÁTICA: usa yuxtaposición para multiplicación de variables (qb, Pa, M0L). Para distancias usa literales simples. Reserva L mayúscula para el claro total.

Una vez asimiladas estas convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud finita L, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. Ambos extremos de la viga, en x = 0 y en x = L, son libres (no existen reacciones externas en los extremos). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en el centro de la viga, es decir, en x = L/2.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), aplicando explícitamente las cuatro condiciones de frontera correspondientes a los extremos libres.

<<< HASTA AQUÍ

---

## C4 — Viga infinita sobre fundación de Pasternak con carga puntual centrada

### C4 · Sin andamiaje (minimal)

>>> COPIAR DESDE AQUÍ

Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre una fundación elástica tipo Pasternak. Esta fundación se caracteriza por dos parámetros independientes: el módulo de reacción vertical k1 (similar al módulo de balasto de Winkler) y el módulo de cortante de la capa de cortante k2 (que acopla horizontalmente las reacciones de los resortes mediante una membrana de cortante virtual). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación diferencial gobernante para la deflexión y(x) y obtén su solución analítica completa, especificando claramente las raíces de la ecuación característica resultante.

<<< HASTA AQUÍ

### C4 · Con andamiaje (scaffolded)

>>> COPIAR DESDE AQUÍ

Actúa como un experto en ingeniería estructural y mecánica de sólidos. Antes de resolver el problema que se te planteará al final, adopta y respeta estrictamente las siguientes convenciones físicas y notacionales:

1. SISTEMA GLOBAL DE COORDENADAS: el eje x es positivo hacia la derecha y el eje y es positivo hacia arriba. Por la regla de la mano derecha, todo giro o momento en sentido antihorario es positivo.

2. CONVENCIÓN POR DEFORMACIÓN para un elemento diferencial de longitud dx:
   - En la cara izquierda (en x): el cortante V apunta hacia arriba y el momento flexionante M actúa en sentido horario.
   - En la cara derecha (en x+dx): el cortante V apunta hacia abajo y el momento flexionante M actúa en sentido antihorario.
   - La carga externa distribuida q(x) actúa hacia abajo.
   - La fuerza de reacción del medio elástico actúa hacia arriba.

3. CURVATURA: un momento positivo M genera compresión en la fibra superior y tracción en la fibra inferior (concavidad hacia arriba).

4. REACCIONES: al inicio de la solución del problema, todas las reacciones incógnitas deben tomarse actuando en su sentido positivo conforme al sistema descrito.

5. PROCEDIMIENTO ANALÍTICO: plantea las ecuaciones de equilibrio en un elemento diferencial dx, expande las funciones V(x+dx) y M(x+dx) en series de Taylor truncadas a primer orden, deriva la ecuación diferencial gobernante, resuelve la ecuación característica usando variable compleja cuando proceda, y aplica las condiciones de frontera del problema con coherencia matemática.

6. NOTACIÓN MATEMÁTICA: usa yuxtaposición para multiplicación de variables (qb, Pa, M0L). Para distancias usa literales simples. Reserva L mayúscula para el claro total.

Una vez asimiladas estas convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre una fundación elástica tipo Pasternak. Esta fundación se caracteriza por dos parámetros independientes: el módulo de reacción vertical k1 (similar al módulo de balasto de Winkler) y el módulo de cortante de la capa de cortante k2 (que acopla horizontalmente las reacciones de los resortes mediante una membrana de cortante virtual). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación diferencial gobernante para la deflexión y(x) y obtén su solución analítica completa, especificando claramente las raíces de la ecuación característica resultante.

<<< HASTA AQUÍ
