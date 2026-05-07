# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C2 — Viga infinita Winkler con carga puntual descentrada en x = a
- **Modelo:** gemini-3.1-pro (selector "Pro")
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 17:47:41 (CDMX, UTC−6) — inicio. Finalización ~17:48:30
- **Versión exacta del modelo:** Gemini 3.1 Pro (vía gemini.google.com con plan Pro del usuario)
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** TEMPORAL (verificado)
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada
- **¿Se requirió pedir "continuar"?:** No (respuesta completa en una sola pasada)
- **Longitud de la respuesta:** larga
- **Verificación de no-contaminación:** sin uso de "doctor" ni referencia a metodología previa del usuario

---

## Prompt enviado

```
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en la posición x = a, donde a es una distancia conocida medida hacia la derecha del origen.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), válidas para todo x perteneciente al intervalo (-infinito, +infinito).
```

---

## Salida del modelo

Este es un problema clásico de la teoría de vigas sobre cimentación elástica (modelo de Winkler). Para resolverlo, derivaremos las ecuaciones asumiendo que la deflexión hacia abajo es positiva.

### 1. Ecuación Diferencial Gobernante

Para una viga apoyada sobre un lecho elástico de Winkler, la reacción del medio es proporcional a la deflexión: $q_r(x) = -k y(x)$, donde $k$ es el módulo de balasto (con unidades de fuerza por unidad de longitud al cuadrado, por ejemplo, N/m² o Pa si consideramos el ancho de la viga incluido en $k$).

La ecuación diferencial fundamental de la elástica de la viga es:
$$ EI \frac{d^4y}{dx^4} = q(x) - k y(x) $$

Dado que tenemos una carga puntual $P$ en $x = a$, podemos expresar la carga externa usando la función delta de Dirac, $\delta(x-a)$. Sin embargo, es más sencillo resolver el problema primero para una carga aplicada en el origen ($x = 0$) y luego trasladar la solución a $x = a$.

Para $x \neq 0$ (fuera del punto de aplicación de la carga), la ecuación diferencial homogénea es:
$$ EI \frac{d^4y}{dx^4} + k y = 0 $$

Definimos el **parámetro característico de la viga** (o factor de amortiguamiento espacial) $\beta$ como:
$$ \beta = \sqrt[4]{\frac{k}{4EI}} $$

Sustituyendo esto, la ecuación diferencial se reescribe como:
$$ \frac{d^4y}{dx^4} + 4\beta^4 y = 0 $$

### 2. Solución General y Condiciones de Frontera

La solución general de esta ecuación diferencial lineal de cuarto orden es:
$$ y(x) = e^{\beta x}(C_1 \cos \beta x + C_2 \sin \beta x) + e^{-\beta x}(C_3 \cos \beta x + C_4 \sin \beta x) $$

Para encontrar las constantes, aplicamos las condiciones de frontera para la mitad derecha de la viga ($x \geq 0$):

1.  **Condición en el infinito:** Como la viga es de longitud infinita, la deflexión debe ser cero cuando $x \to \infty$. Esto obliga a que los términos con $e^{\beta x}$ desaparezcan, por lo tanto, $C_1 = 0$ y $C_2 = 0$.
    $$ y(x) = e^{-\beta x}(C_3 \cos \beta x + C_4 \sin \beta x) \quad \text{para } x \geq 0 $$

2.  **Condición de simetría en el origen:** En el punto de aplicación de la carga ($x=0$), la pendiente de la viga debe ser nula debido a la simetría.
    $$ \frac{dy}{dx}\Bigg|_{x=0} = 0 $$
    Derivando $y(x)$ y evaluando en $x=0$, obtenemos:
    $$ y'(0) = \beta(-C_3 + C_4) = 0 \implies C_3 = C_4 = C $$
    Nuestra ecuación se reduce a:
    $$ y(x) = C e^{-\beta x}(\cos \beta x + \sin \beta x) $$

3.  **Condición de cortante en el origen:** Por equilibrio vertical de un segmento infinitesimal en $x=0$, la fuerza cortante $V$ justo a la derecha de la carga debe soportar la mitad de la carga aplicada (la otra mitad se va hacia la izquierda):
    $$ V(0^+) = -EI \frac{d^3y}{dx^3}\Bigg|_{x=0^+} = -\frac{P}{2} $$
    Derivamos $y(x)$ tres veces:
    $$ y'(x) = -2\beta C e^{-\beta x} \sin \beta x $$
    $$ y''(x) = -2\beta^2 C e^{-\beta x} (\cos \beta x - \sin \beta x) $$
    $$ y'''(x) = 4\beta^3 C e^{-\beta x} \cos \beta x $$
    Evaluando en $x=0$:
    $$ y'''(0) = 4\beta^3 C $$
    Sustituyendo en la ecuación de cortante:
    $$ -EI (4\beta^3 C) = -\frac{P}{2} \implies C = \frac{P}{8\beta^3 EI} $$
    Recordando que $\beta^4 = \frac{k}{4EI}$, podemos reescribir $8\beta^3 EI = \frac{2k}{\beta}$, por lo que:
    $$ C = \frac{P\beta}{2k} $$

### 3. Ecuación de la Curva Elástica, $y(x)$

Sustituyendo $C$ de vuelta en nuestra ecuación y reconociendo que por simetría el comportamiento es idéntico para $x < 0$, reemplazamos $x$ por $|x|$.
Luego, para trasladar la carga a la posición $x = a$, simplemente reemplazamos $|x|$ por la distancia relativa $|x - a|$:

$$ y(x) = \frac{P\beta}{2k} e^{-\beta|x-a|} \big( \cos \beta|x-a| + \sin \beta|x-a| \big) $$

### 4. Momento Flexionante, $M(x)$

El momento flexionante se define como $M(x) = -EI \frac{d^2y}{dx^2}$.
Utilizando la segunda derivada que calculamos en el paso anterior (adaptada para $|x-a|$):

$$ y''(x) = -2\beta^2 \left( \frac{P\beta}{2k} \right) e^{-\beta|x-a|} (\cos \beta|x-a| - \sin \beta|x-a|) $$
$$ M(x) = -EI \left[ -\frac{P\beta^3}{k} e^{-\beta|x-a|} (\cos \beta|x-a| - \sin \beta|x-a|) \right] $$

Sabiendo que $\frac{EI}{k} = \frac{1}{4\beta^4}$:

$$ M(x) = \frac{P}{4\beta} e^{-\beta|x-a|} \big( \cos \beta|x-a| - \sin \beta|x-a| \big) $$

### 5. Fuerza Cortante, $V(x)$

La fuerza cortante es la derivada del momento flexionante, $V(x) = \frac{dM}{dx}$.
Al derivar la función que contiene un valor absoluto, aparece una discontinuidad en el punto de aplicación de la carga (justo donde la cortante "salta" de valor debido a la carga puntual $P$). Para representar esto analíticamente para todo $x$, utilizamos la función signo, $\text{sgn}(x-a)$, la cual vale $-1$ si $x<a$ y $+1$ si $x>a$.

Derivando $M(x)$:

$$ V(x) = -\frac{P}{2} \text{sgn}(x-a) e^{-\beta|x-a|} \cos \beta|x-a| $$

---

### Resumen de Soluciones Analíticas

Válidas para cualquier $x \in (-\infty, \infty)$, con $\beta = \sqrt[4]{\frac{k}{4EI}}$:

*   **Deflexión:**
    $$ y(x) = \frac{P\beta}{2k} e^{-\beta|x-a|} \big( \cos \beta|x-a| + \sin \beta|x-a| \big) $$
*   **Momento Flexionante:**
    $$ M(x) = \frac{P}{4\beta} e^{-\beta|x-a|} \big( \cos \beta|x-a| - \sin \beta|x-a| \big) $$
*   **Fuerza Cortante:**
    $$ V(x) = -\frac{P}{2} \text{sgn}(x-a) e^{-\beta|x-a|} \cos \beta|x-a| $$

*(Nota: Los valores máximos ocurren bajo la carga en $x=a$, resultando en $y_{max} = \frac{P\beta}{2k}$ y $M_{max} = \frac{P}{4\beta}$. La cortante bajo la carga está indefinida matemáticamente, pero los límites laterales son $\pm P/2$.)*

---

## Evaluación según rúbrica (`rubric.md`)

> A completar en la fase de análisis. NO LLENAR durante la ejecución.

| Métrica | Valor |
|---|---|
| **M1** — Coherencia de signos | 0 |
| **M2** — Coherencia dimensional | 1 |
| **M3** — Aplicación correcta de CB | 1 |
| **M4** — Correctitud de solución final | 1 |
| **M5** — Errores algebraicos contables | 0 |

## Justificación cualitativa de la evaluación

> A completar en la fase de análisis.

### Observaciones preliminares (no evaluativas, solo para referencia)

- El modelo adoptó **convención de eje $y$ positivo hacia abajo** ("la deflexión hacia abajo es positiva"). Misma elección que en C1 minimal — ambas opuestas a la convención del manuscrito.
- Usó $M = -EI y''$, $V = -EI y'''$ (consistentes con su convención $y$ positivo abajo, opuestos a la del manuscrito).
- **Estrategia de traslación:** resolvió primero en $x = 0$ y luego sustituyó $|x| \to |x-a|$. Aplicación correcta de la invarianza por traslación.
- $y(a) = +P\beta/(2k)$ POSITIVO bajo su convención (correspondería a $-P\beta/(2k)$ bajo la convención del manuscrito).
- $M(a) = +P/(4\beta)$ POSITIVO.
- $V(x)$ con $\text{sgn}(x-a)$ correcto.
