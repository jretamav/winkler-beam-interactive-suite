# Bitácora de ejecución — Estudio de ablación

> ⚠️ **SESIÓN INVALIDADA POR CONTAMINACIÓN DE CONTEXTO.**
>
> Esta ejecución fue realizada en un chat **normal** de gemini.google.com en lugar de un chat **temporal**. El modelo respondió usando contexto personal persistente (trató al usuario como "doctor", referenció "nuestra metodología de cálculo" y "la convención de signos estáticos y de deformación"), lo cual constituye contaminación porque la condición experimental era *minimal* (sin andamiaje). Aunque la Actividad de Gemini estaba formalmente desactivada antes de la ejecución, el chat normal siguió accediendo al perfil personal persistente del usuario.
>
> Sesión válida sustituta: `gemini_C1_minimal.md`, ejecutada en chat **temporal**.
>
> Este archivo se conserva como evidencia metodológica del fenómeno de contaminación, valioso para discusión en la sección 4.5 del manuscrito.

## Metadatos

- **Caso:** C1 — Viga infinita Winkler con carga puntual centrada
- **Modelo:** gemini-3.1-pro (selector "Pro" en gemini.google.com, descripción literal: "Matemáticas y programación avanzadas con 3.1 Pro")
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 [hora local CDMX por confirmar]
- **Versión exacta del modelo:** Gemini 3.1 Pro (vía gemini.google.com con plan Pro del usuario)
- **Operador:** Jaime Retama Velasco
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada antes de la ejecución (verificada por captura de pantalla del usuario)
- **¿Se requirió pedir "continuar"?:** No (respuesta completa en una sola pasada)
- **Longitud de la respuesta:** larga (~3-4 pantallas)

---

## Prompt enviado

```
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x).
```

---

## Salida del modelo

Qué tal, doctor. A continuación presento la derivación analítica para la viga de longitud infinita sobre base elástica, respetando estrictamente la convención de signos estáticos y de deformación que rigen nuestra metodología de cálculo.

### 1. Ecuación Diferencial Gobernadora

Para un elemento diferencial de viga sobre un medio de Winkler, el equilibrio de fuerzas verticales (con el eje $y$ positivo hacia arriba) y momentos nos lleva a las relaciones clásicas. De acuerdo con la convención por deformación definida, donde una carga descendente $q(x)$ es positiva, la reacción del lecho elástico actúa hacia arriba oponiéndose al desplazamiento $y(x)$. Como $y(x)$ es positivo hacia arriba, la presión del resorte es $-ky(x)$.

Sustituyendo esto en la ecuación diferencial de la elástica de Euler-Bernoulli obtenemos:

$$EI \frac{d^4y}{dx^4} = q(x) + ky(x)$$

Dado que la carga concentrada $P$ solo actúa en $x = 0$, para cualquier tramo donde $x \neq 0$, la carga distribuida externa $q(x)$ es nula. Por lo tanto, la ecuación diferencial homogénea es:

$$EI \frac{d^4y}{dx^4} - ky(x) = 0$$
*(Nota: Al considerar la carga $q$ actuando hacia abajo como positiva y la reacción elástica hacia arriba, el equilibrio global requiere que la fuerza neta distribuida sea $-ky$, lo que nos lleva a la forma estándar).*

$$EI \frac{d^4y}{dx^4} + ky = 0$$

Para simplificar la solución, introducimos el parámetro $\beta$ que caracteriza la rigidez relativa entre el medio elástico y la viga:

$$\beta = \sqrt[4]{\frac{k}{4EI}}$$

Sustituyendo $k = 4EI\beta^4$ en la ecuación diferencial, la solución general toma la forma:

$$y(x) = e^{\beta x}(A \cos\beta x + B \sin\beta x) + e^{-\beta x}(C \cos\beta x + D \sin\beta x)$$

### 2. Condiciones de Frontera y Simetría

Debido a que la viga es de longitud infinita y la carga se aplica en $x = 0$, analizaremos el semiespacio derecho ($x \ge 0$).

**Condición en el infinito:**
Cuando $x \to \infty$, el desplazamiento $y(x)$ debe tender a cero. Por lo tanto, los coeficientes de los términos con exponente positivo deben anularse ($A = 0$, $B = 0$). La ecuación se reduce a:

$$y(x) = e^{-\beta x}(C \cos\beta x + D \sin\beta x)$$

**Condición de giro en el origen:**
Por simetría, la tangente a la curva elástica en el punto de aplicación de la carga debe ser horizontal, es decir, $y'(0) = 0$.
Derivando $y(x)$:

$$y'(x) = -\beta e^{-\beta x}(C \cos\beta x + D \sin\beta x) + \beta e^{-\beta x}(-C \sin\beta x + D \cos\beta x)$$

Evaluando en $x = 0$:

$$y'(0) = -\beta C + \beta D = 0 \implies C = D$$

Por lo que la ecuación de la elástica se simplifica a:

$$y(x) = C e^{-\beta x}(\cos\beta x + \sin\beta x)$$

**Condición de cortante en el origen:**
Haciendo un corte infinitesimal a la derecha del origen ($x \to 0^+$), y considerando la convención de signos por deformación (donde en la cara izquierda del segmento derecho un cortante positivo apunta hacia arriba), la carga descendente $P$ se distribuye simétricamente. El segmento derecho debe ejercer una fuerza de $P/2$ hacia arriba para soportar la mitad de la carga, por lo que, por acción y reacción, el cortante interno actuando sobre esa cara izquierda debe apuntar hacia abajo. Así, $V(0^+) = -P/2$.

Sabemos que $V(x) = EI y'''(x)$. Derivando progresivamente:

$$y''(x) = -2\beta^2 C e^{-\beta x}(\cos\beta x - \sin\beta x)$$
$$y'''(x) = 4\beta^3 C e^{-\beta x}\cos\beta x$$

Evaluando el cortante en $x = 0^+$:

$$V(0^+) = EI(4\beta^3 C) = 4EI\beta^3 C$$

Igualando a la condición de frontera:

$$4EI\beta^3 C = -\frac{P}{2}$$
$$C = -\frac{P}{8EI\beta^3}$$

Recordando que $k = 4EI\beta^4$, podemos expresar $8EI\beta^3$ como $2k/\beta$. Sustituyendo esto, encontramos la constante:

$$C = -\frac{P\beta}{2k}$$

### 3. Ecuaciones Analíticas Finales

Habiendo determinado la constante de integración, procedemos a establecer las funciones para el semiespacio $x \ge 0$. Para generalizar a todo el dominio $(-\infty < x < \infty)$, utilizamos el valor absoluto $|x|$ debido a la simetría de la deformación.

**Curva Elástica $y(x)$:**
Sustituyendo la constante $C$, la ecuación de la deformada es negativa (indicando un desplazamiento hacia abajo, acorde a nuestro eje $y$ positivo hacia arriba):

$$y(x) = -\frac{P\beta}{2k} e^{-\beta|x|}(\cos\beta|x| + \sin\beta|x|)$$

**Momento Flexionante $M(x)$:**
Utilizando la relación $M = EI y''$, y sustituyendo el valor de $C$ en la segunda derivada:

$$M(x) = EI \left[ -2\beta^2 \left(-\frac{P\beta}{2k}\right) e^{-\beta|x|}(\cos\beta|x| - \sin\beta|x|) \right]$$
$$M(x) = \frac{PEI\beta^3}{k} e^{-\beta|x|}(\cos\beta|x| - \sin\beta|x|)$$

Sabiendo que $EI/k = 1/(4\beta^4)$, la ecuación final para el momento flector es:

$$M(x) = \frac{P}{4\beta} e^{-\beta|x|}(\cos\beta|x| - \sin\beta|x|)$$
*(El momento máximo ocurre en $x=0$ con un valor positivo de $P/4\beta$, lo cual indica compresión en la fibra superior y tensión en la inferior, congruente con la deformación esperada).*

**Fuerza Cortante $V(x)$:**
Utilizando la relación $V = dM/dx = EI y'''$ para el lado derecho ($x \ge 0$):

$$V(x) = EI \left[ 4\beta^3 \left(-\frac{P\beta}{2k}\right) e^{-\beta x}\cos\beta x \right]$$
$$V(x) = -\frac{2PEI\beta^4}{k} e^{-\beta x}\cos\beta x$$

Dado que $2EI\beta^4/k = 2(k/4)/k = 1/2$, la ecuación para $x \ge 0$ es:

$$V(x) = -\frac{P}{2} e^{-\beta x}\cos\beta x$$

Para englobar todo el dominio y reflejar el salto del cortante en el punto de aplicación de la carga (antisimetría), introducimos la función signo, $\text{sgn}(x)$:

$$V(x) = -\frac{P}{2} \text{sgn}(x) e^{-\beta|x|}\cos\beta|x|$$

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
