# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C1 — Viga infinita Winkler con carga puntual centrada
- **Modelo:** gemini-3.1-pro (selector "Pro" en gemini.google.com, descripción literal: "Matemáticas y programación avanzadas con 3.1 Pro")
- **Condición:** scaffolded (con andamiaje fenomenológico completo)
- **Fecha y hora de ejecución:** 2026-05-06 17:33:35 (CDMX, UTC−6) — inicio
- **Versión exacta del modelo:** Gemini 3.1 Pro (vía gemini.google.com con plan Pro del usuario)
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** TEMPORAL
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada antes de la ejecución
- **¿Se requirió pedir "continuar"?:** No (respuesta completa en una sola pasada)
- **Longitud de la respuesta:** larga
- **Verificación de no-contaminación:** sin uso de "doctor" ni referencia a metodología previa del usuario

---

## Prompt enviado

```
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

Una vez asimiladas las convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x).
```

---

## Salida del modelo

Como experto en ingeniería estructural y mecánica de sólidos, asumo estrictamente las convenciones físicas, matemáticas y notacionales que has delineado. Procederé con el desarrollo analítico paso a paso para una viga infinita sobre fundación elástica tipo Winkler.

### 1. Equilibrio del Elemento Diferencial

Consideremos un elemento diferencial de viga de longitud $dx$. Aplicamos las convenciones establecidas: el cortante $V(x)$ actúa hacia arriba en la cara izquierda y el cortante $V(x+dx)$ hacia abajo en la cara derecha. El momento flexionante $M(x)$ actúa en sentido horario y $M(x+dx)$ en sentido antihorario.

La reacción del lecho elástico actúa hacia arriba y, dado que la ordenada $y(x)$ es positiva hacia arriba, la fuerza restauradora hacia arriba se expresa como $-ky(x)dx$. La carga externa distribuida $q(x)$ actúa hacia abajo.

**Equilibrio de fuerzas verticales ($\sum F_y = 0$, positivo hacia arriba):**
$$V(x) - V(x+dx) - q(x)dx - ky(x)dx = 0$$

Expandiendo $V(x+dx)$ en serie de Taylor de primer orden:
$$V(x+dx) = V(x) + V'(x)dx$$

Sustituyendo y simplificando:
$$V(x) - (V(x) + V'(x)dx) - q(x)dx - ky(x)dx = 0$$
$$-V'(x) - q(x) - ky(x) = 0 \implies V'(x) = -q(x) - ky(x)$$

**Equilibrio de momentos en el centro del elemento ($\sum M = 0$, positivo antihorario):**
$$-M(x) + M(x+dx) - V(x)\frac{dx}{2} - V(x+dx)\frac{dx}{2} = 0$$

Expandiendo $M(x+dx)$ y $V(x+dx)$ en series de Taylor:
$$-M(x) + (M(x) + M'(x)dx) - V(x)\frac{dx}{2} - (V(x) + V'(x)dx)\frac{dx}{2} = 0$$

Despreciando los diferenciales de segundo orden ($V'(x)dx^2 \approx 0$):
$$M'(x)dx - V(x)dx = 0 \implies M'(x) = V(x)$$

### 2. Ecuación Diferencial Gobernante

Por la convención de curvatura dada, un momento positivo comprime la fibra superior y tracciona la inferior (concavidad hacia arriba, por lo tanto la segunda derivada es positiva):
$$M(x) = EIy''(x)$$

Derivando sucesivamente respecto a $x$:
$$V(x) = M'(x) = EIy'''(x)$$
$$V'(x) = EIy''''(x)$$

Igualando con la ecuación de equilibrio de fuerzas verticales:
$$EIy''''(x) = -ky(x) - q(x) \implies EIy''''(x) + ky(x) = -q(x)$$

Para todo $x \neq 0$, la carga externa $q(x)$ es nula. Obtenemos la ecuación diferencial homogénea:
$$EIy''''(x) + ky(x) = 0$$

### 3. Solución de la Ecuación Característica

Introducimos el parámetro característico de la fundación elástica $\beta$:
$$\beta = \sqrt[4]{\frac{k}{4EI}} \implies 4\beta^4 = \frac{k}{EI}$$

La ecuación diferencial se reescribe como:
$$y''''(x) + 4\beta^4y(x) = 0$$

Proponemos una solución de la forma $y(x) = e^{rx}$, obteniendo la ecuación característica en el plano complejo:
$$r^4 + 4\beta^4 = 0 \implies r^4 = 4\beta^4e^{i\pi}$$

Extrayendo las cuatro raíces complejas:
$$r_n = \sqrt{2}\beta e^{i(\pi + 2n\pi)/4} \quad \text{para} \quad n=0, 1, 2, 3$$
$$r_{1,2,3,4} = \pm \beta \pm i\beta$$

Aplicando la identidad de Euler, la solución general es:
$$y(x) = e^{\beta x}(A\cos\beta x + B\sin\beta x) + e^{-\beta x}(C\cos\beta x + D\sin\beta x)$$

### 4. Condiciones de Frontera

Debido a la simetría estructural respecto a $x = 0$, resolveremos para el dominio $x \ge 0$.

**Condición en el infinito ($x \to \infty$):**
La deformación debe anularse lejos de la carga, por lo tanto $y(\infty) = 0$. Esto obliga a que los coeficientes del término divergente $e^{\beta x}$ sean nulos:
$$A = 0, \quad B = 0$$
$$y(x) = e^{-\beta x}(C\cos\beta x + D\sin\beta x)$$

**Condición de giro nulo en el origen ($x = 0$):**
Por simetría, la tangente a la elástica bajo la carga debe ser horizontal:
$$y'(x) = -\beta e^{-\beta x}(C\cos\beta x + D\sin\beta x) + \beta e^{-\beta x}(-C\sin\beta x + D\cos\beta x)$$
$$y'(0) = -\beta C + \beta D = 0 \implies C = D$$

Por lo tanto, la curva elástica simplificada es:
$$y(x) = Ce^{-\beta x}(\cos\beta x + \sin\beta x)$$

**Condición de equilibrio de cortante bajo la carga ($x = 0$):**
Aislando un elemento diferencial de longitud $2\epsilon$ centrado en $x = 0$, la carga puntual $P$ actúa hacia abajo. Por simetría, el cortante en la cara izquierda es de igual magnitud y signo opuesto al de la cara derecha: $V(-\epsilon) = -V(+\epsilon)$.
$$\sum F_y = 0 \implies V(-\epsilon) - V(+\epsilon) - P = 0 \implies -2V(0^+) - P = 0 \implies V(0^+) = -\frac{P}{2}$$

Calculamos la tercera derivada para hallar el cortante analítico $V(x) = EIy'''(x)$:
$$y'(x) = -2\beta Ce^{-\beta x}\sin\beta x$$
$$y''(x) = 2\beta^2 Ce^{-\beta x}(\sin\beta x - \cos\beta x)$$
$$y'''(x) = 4\beta^3 Ce^{-\beta x}\cos\beta x$$
$$V(x) = 4EI\beta^3 Ce^{-\beta x}\cos\beta x$$

Evaluando en $x = 0^+$:
$$V(0^+) = 4EI\beta^3 C = -\frac{P}{2}$$

Dado que $\beta^4 = \frac{k}{4EI}$, sabemos que $4EI\beta^3 = \frac{k}{\beta}$. Sustituyendo:
$$\frac{k}{\beta} C = -\frac{P}{2} \implies C = -\frac{P\beta}{2k}$$

### 5. Ecuaciones Analíticas Finales

Sustituyendo la constante $C$ en las expresiones previamente derivadas y reconociendo que por simetría las funciones de deformación y momento son pares, mientras que el cortante es impar, las ecuaciones gobernantes para $x \ge 0$ son:

**Curva Elástica (Deflexión):**
$$y(x) = -\frac{P\beta}{2k} e^{-\beta x}(\cos\beta x + \sin\beta x)$$

**Momento Flexionante ($M(x) = EIy''(x)$):**
Sustituyendo $C$ y recordando que $EI = \frac{k}{4\beta^4}$:
$$M(x) = \frac{k}{4\beta^4} \left[ 2\beta^2 \left(-\frac{P\beta}{2k}\right) e^{-\beta x}(\sin\beta x - \cos\beta x) \right]$$
$$M(x) = \frac{P}{4\beta} e^{-\beta x}(\cos\beta x - \sin\beta x)$$

**Fuerza Cortante ($V(x) = EIy'''(x)$):**
$$V(x) = 4EI\beta^3 \left(-\frac{P\beta}{2k}\right) e^{-\beta x}\cos\beta x = -\frac{P}{2} e^{-\beta x}\cos\beta x$$

*(Nota: Para el dominio completo $-\infty < x < \infty$, las ecuaciones se generalizan reemplazando $x$ por el valor absoluto $|x|$ en los argumentos y exponentes, multiplicando la expresión del cortante por la función signo $\text{sgn}(x)$).*

---

## Evaluación según rúbrica (`rubric.md`)

> A completar en la fase de análisis. NO LLENAR durante la ejecución.

| Métrica | Valor |
|---|---|
| **M1** — Coherencia de signos | 1 |
| **M2** — Coherencia dimensional | 1 |
| **M3** — Aplicación correcta de CB | 1 |
| **M4** — Correctitud de solución final | 1 |
| **M5** — Errores algebraicos contables | 0 |

## Justificación cualitativa de la evaluación

> A completar en la fase de análisis.

### Observaciones preliminares (no evaluativas, solo para referencia)

- El modelo **adoptó la convención del andamiaje correctamente** ($y$ positivo arriba, $M = +EI y''$, $V = +EI y'''$).
- $y(0) = -P\beta/(2k)$ NEGATIVO ← **coincide con manuscrito y con la convención prescrita**.
- $M(0) = +P/(4\beta)$ POSITIVO ← coincide con manuscrito.
- Las tres expresiones finales son **algebraicamente idénticas a la solución de referencia** documentada en `reference_solutions.md`.
- Contraste fuerte con la condición *minimal* (que adoptó $y$ positivo abajo).
