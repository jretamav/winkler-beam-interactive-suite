# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C1 — Viga infinita Winkler con carga puntual centrada
- **Modelo:** gemini-3.1-pro (selector "Pro" en gemini.google.com, descripción literal: "Matemáticas y programación avanzadas con 3.1 Pro")
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 17:29:40 (CDMX, UTC−6)
- **Versión exacta del modelo:** Gemini 3.1 Pro (vía gemini.google.com con plan Pro del usuario)
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** TEMPORAL (verificado para evitar contaminación de contexto persistente)
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada antes de la ejecución
- **¿Se requirió pedir "continuar"?:** No (respuesta completa en una sola pasada)
- **Longitud de la respuesta:** larga (~3-4 pantallas)
- **Verificación de no-contaminación:** sin uso de "doctor" ni referencia a metodología previa del usuario; tono neutro de libro de texto

---

## Prompt enviado

```
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x).
```

---

## Salida del modelo

Este es un problema clásico de mecánica de sólidos y teoría de vigas. Para resolverlo, nos basaremos en la teoría de vigas de Euler-Bernoulli aplicada sobre una cimentación elástica (modelo de Winkler).

Aquí tienes la derivación paso a paso de las ecuaciones analíticas.

### 1. Ecuación Diferencial Gobernadora

Asumimos que la viga tiene un desplazamiento vertical $y(x)$ positivo hacia abajo. La carga concentrada $P$ se aplica en $x = 0$ y actúa hacia abajo.

La presión de reacción del medio elástico hacia arriba, según el modelo de Winkler, es proporcional a la deflexión: $q_{r}(x) = k y(x)$, donde $k$ es el módulo de balasto (con unidades de fuerza por unidad de longitud al cuadrado, por ejemplo, N/m² o Pa si consideramos el ancho de la viga incluido en $k$).

La ecuación diferencial de la curva elástica para una sección de la viga que no tiene cargas aplicadas externamente (es decir, para $x \neq 0$) es:

$$EI \frac{d^4y}{dx^4} = -k y(x)$$

Reorganizando obtenemos la ecuación diferencial homogénea lineal de cuarto orden:

$$EI \frac{d^4y}{dx^4} + k y = 0$$

### 2. Solución General y Parámetro Característico

Para resolver esta ecuación, introducimos un parámetro característico $\beta$, que define la rigidez relativa del sistema viga-suelo y tiene unidades de longitud inversa ($1/m$):

$$\beta = \sqrt[4]{\frac{k}{4EI}}$$

Sustituyendo $k = 4EI\beta^4$ en la ecuación diferencial, la ecuación característica asociada tiene raíces complejas conjugadas. La solución general de la ecuación diferencial es:

$$y(x) = e^{\beta x}(A \cos \beta x + B \sin \beta x) + e^{-\beta x}(C \cos \beta x + D \sin \beta x)$$

### 3. Aplicación de las Condiciones de Frontera

Aprovechando la simetría del problema, analizaremos solo la porción derecha de la viga ($x \ge 0$).

**Condición en el infinito ($x \to \infty$):**
Dado que la viga es de longitud infinita, la deflexión debe desvanecerse muy lejos de la carga.
$$y(\infty) = 0$$
Para que esto se cumpla, el término $e^{\beta x}$ debe eliminarse. Por lo tanto, $A = 0$ y $B = 0$. La ecuación se reduce a:
$$y(x) = e^{-\beta x}(C \cos \beta x + D \sin \beta x) \quad \text{para } x \ge 0$$

**Condición de simetría en el origen ($x = 0$):**
Debido a la simetría de la carga, la pendiente de la viga justo debajo de la carga debe ser cero.
$$\left. \frac{dy}{dx} \right|_{x=0} = 0$$
Derivando $y(x)$:
$$\frac{dy}{dx} = -\beta e^{-\beta x} (C \cos \beta x + D \sin \beta x) + \beta e^{-\beta x} (-C \sin \beta x + D \cos \beta x)$$
$$\frac{dy}{dx} = \beta e^{-\beta x} [ (D - C) \cos \beta x - (C + D) \sin \beta x ]$$
Evaluando en $x = 0$:
$$y'(0) = \beta (D - C) = 0 \implies C = D$$
Sea $C = D = C_0$. La ecuación de deflexión queda:
$$y(x) = C_0 e^{-\beta x}(\cos \beta x + \sin \beta x)$$

**Condición de equilibrio en el origen (Fuerza Cortante):**
La carga puntual $P$ es resistida por la fuerza cortante $V(x)$ a ambos lados del origen. Por simetría, la fuerza cortante justo a la derecha del origen ($x \to 0^+$) debe resistir la mitad de la carga:
$$V(0^+) = -\frac{P}{2}$$
Recordemos que la relación entre cortante y deflexión es $V(x) = -EI \frac{d^3y}{dx^3}$.
Procedemos a derivar hasta la tercera derivada:
$$y'(x) = -2\beta C_0 e^{-\beta x} \sin \beta x$$
$$y''(x) = -2\beta^2 C_0 e^{-\beta x} (\cos \beta x - \sin \beta x)$$
$$y'''(x) = 4\beta^3 C_0 e^{-\beta x} \cos \beta x$$

Sustituyendo en la expresión del cortante y evaluando en $x=0$:
$$V(0) = -EI (4\beta^3 C_0) = -\frac{P}{2}$$
Despejando $C_0$:
$$C_0 = \frac{P}{8\beta^3 EI}$$
Sabiendo que $\beta^4 = \frac{k}{4EI}$, podemos reescribir $EI = \frac{k}{4\beta^4}$. Sustituyendo esto:
$$C_0 = \frac{P}{8\beta^3 \left(\frac{k}{4\beta^4}\right)} = \frac{P \beta}{2k}$$

---

### 4. Ecuaciones Finales Analíticas (para $x \ge 0$)

Sustituyendo el valor de $C_0$ de vuelta, obtenemos las tres ecuaciones fundamentales.

#### A. Curva Elástica (Deflexión) $y(x)$
$$y(x) = \frac{P \beta}{2k} e^{-\beta x} (\cos \beta x + \sin \beta x)$$
*(Esta función describe una onda amortiguada donde la deflexión máxima ocurre en $x = 0$ con un valor de $y_{max} = \frac{P\beta}{2k}$).*

#### B. Momento Flexionante $M(x)$
Usando la convención $M(x) = -EI \frac{d^2y}{dx^2}$:
$$M(x) = -EI \left[ -2\beta^2 \left(\frac{P\beta}{2k}\right) e^{-\beta x} (\cos \beta x - \sin \beta x) \right]$$
Sustituyendo $\frac{EI \beta^3}{k} = \frac{1}{4\beta}$:
$$M(x) = \frac{P}{4\beta} e^{-\beta x} (\cos \beta x - \sin \beta x)$$
*(El momento máximo ocurre en $x = 0$ con un valor de $M_{max} = \frac{P}{4\beta}$).*

#### C. Fuerza Cortante $V(x)$
Usando $V(x) = \frac{dM}{dx} = -EI \frac{d^3y}{dx^3}$:
$$V(x) = -EI \left[ 4\beta^3 \left(\frac{P\beta}{2k}\right) e^{-\beta x} \cos \beta x \right]$$
Sustituyendo nuevamente $\frac{4 EI \beta^4}{k} = 1$:
$$V(x) = -\frac{P}{2} e^{-\beta x} \cos \beta x$$

> **Nota para todo el dominio ($-\infty < x < \infty$):** Dado que el problema es perfectamente simétrico respecto al eje $y$, para encontrar los valores en el lado izquierdo de la viga ($x < 0$), simplemente puedes reemplazar $x$ por su valor absoluto $|x|$ en las ecuaciones de $y(x)$ y $M(x)$. La fuerza cortante $V(x)$ es antisimétrica, por lo que su signo cambia al cruzar el eje central.

---

## Evaluación según rúbrica (`rubric.md`)

> A completar en la fase de análisis. NO LLENAR durante la ejecución.

| Métrica | Valor |
|---|---|
| **M1** — Coherencia de signos | [pendiente] |
| **M2** — Coherencia dimensional | [pendiente] |
| **M3** — Aplicación correcta de CB | [pendiente] |
| **M4** — Correctitud de solución final | [pendiente] |
| **M5** — Errores algebraicos contables | [pendiente] |

## Justificación cualitativa de la evaluación

> A completar en la fase de análisis.

### Observaciones preliminares (no evaluativas, solo para referencia)

- El modelo adoptó **convención de eje $y$ positivo hacia abajo**, opuesta a la convención del manuscrito ($y$ positivo arriba). Implicación a evaluar en M1.
- Usó $M = -EI y''$ y $V = -EI y'''$ (consistentes internamente con su convención $y$ positivo abajo, pero opuestos a las relaciones del manuscrito).
- Solución final internamente coherente, pero **el signo final de $y(0) = +P\beta/(2k)$ es opuesto al del manuscrito**.
