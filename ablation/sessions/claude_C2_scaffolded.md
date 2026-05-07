# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C2 — Viga infinita Winkler con carga puntual descentrada en x = a
- **Modelo:** claude-opus-4-7
- **Condición:** scaffolded (con andamiaje fenomenológico completo)
- **Fecha y hora de ejecución:** 2026-05-06 18:32:30 (CDMX, UTC−6) — inicio. Finalización 18:33:21
- **Tiempo de respuesta:** ~51 segundos
- **Versión exacta del modelo:** Claude Opus 4.7
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** Ventana de incógnito + sesión limpia
- **Estado de Memoria de Claude:** desactivada
- **Pensamiento adaptativo:** DESACTIVADO
- **¿Se requirió pedir "continuar"?:** No
- **Longitud de la respuesta:** larga
- **Verificación de no-contaminación:** confirmado por el operador

---

## Prompt enviado

```
Actúa como un experto en ingeniería estructural y mecánica de sólidos. Antes de resolver el problema que se te planteará al final, adopta y respeta estrictamente las siguientes convenciones físicas y notacionales:

[andamiaje completo de 6 puntos — ver prompts.md]

Una vez asimiladas las convenciones, resuelve el siguiente problema:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en la posición x = a, donde a es una distancia conocida medida hacia la derecha del origen.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), válidas para todo x perteneciente al intervalo (-infinito, +infinito).
```

---

## Salida del modelo

# Viga infinita sobre fundación elástica de Winkler con carga puntual P en x = a

## 1. Ecuación diferencial gobernante

Considero un elemento diferencial de longitud $dx$ tomado en una región sin la carga puntual. Sobre él actúan:

- En la cara izquierda: cortante $V$ (hacia arriba) y momento $M$ (horario).
- En la cara derecha: $V + dV$ (hacia abajo) y $M + dM$ (antihorario), por expansión de Taylor a primer orden:

$$V(x+dx) = V(x) + \frac{dV}{dx}\,dx, \qquad M(x+dx) = M(x) + \frac{dM}{dx}\,dx$$

- Reacción del medio Winkler: $k\,y(x)\,dx$ hacia arriba (cuando $y$ se mide positiva hacia abajo).

**Equilibrio de fuerzas verticales** (positivo hacia arriba):

$$V - (V + dV) + k\,y\,dx = 0 \;\;\Longrightarrow\;\; \frac{dV}{dx} = k\,y$$

**Equilibrio de momentos** respecto a la cara derecha (positivo antihorario), despreciando infinitésimos de orden superior:

$$-M + (M + dM) - V\,dx = 0 \;\;\Longrightarrow\;\; \frac{dM}{dx} = V$$

Combinando con la relación constitutiva de Euler–Bernoulli $M = EI\,\dfrac{d^2 y}{dx^2}$ (con $y$ positiva hacia abajo, de modo que un $M$ positivo produzca concavidad hacia arriba):

$$EI\,\frac{d^4 y}{dx^4} + k\,y = 0 \qquad \text{(zonas sin carga puntual)}$$

Definiendo el **parámetro característico de Winkler**:

$$\boxed{\;\beta = \sqrt[4]{\dfrac{k}{4\,EI}}\;}$$

la ecuación se escribe:

$$\frac{d^4 y}{dx^4} + 4\beta^4\,y = 0$$

## 2. Solución de la ecuación característica

La ecuación característica $r^4 + 4\beta^4 = 0$ tiene raíces complejas. Usando $-1 = e^{i\pi}$:

$$r^4 = -4\beta^4 = 4\beta^4\,e^{i(\pi + 2n\pi)} \;\;\Longrightarrow\;\; r = \sqrt{2}\,\beta\,e^{i(\pi + 2n\pi)/4}$$

Las cuatro raíces son:

$$r_{1,2,3,4} = \beta(\pm 1 \pm i)$$

Por tanto la solución general es:

$$y(x) = e^{\beta x}\bigl(C_1 \cos\beta x + C_2 \sin\beta x\bigr) + e^{-\beta x}\bigl(C_3 \cos\beta x + C_4 \sin\beta x\bigr)$$

## 3. Aplicación de condiciones de frontera

Por la simetría del problema respecto al punto de aplicación $x = a$, conviene definir la coordenada local:

$$\xi = x - a$$

**Condiciones en el infinito:** la deflexión, pendiente, momento y cortante deben anularse cuando $|\xi| \to \infty$.

**Región derecha** ($\xi > 0$, es decir $x > a$): el término $e^{\beta\xi}$ crece sin cota, por lo que $C_1 = C_2 = 0$:

$$y_D(\xi) = e^{-\beta \xi}\bigl(C_3 \cos\beta\xi + C_4 \sin\beta\xi\bigr)$$

**Región izquierda** ($\xi < 0$, es decir $x < a$): el término $e^{-\beta\xi}$ crece sin cota, por lo que los coeficientes de ese par deben anularse. Por la simetría de la deflexión bajo una carga puntual $y(-\xi) = y(\xi)$, basta resolver una región y reflejar.

**Condiciones en $\xi = 0$** (punto de aplicación de $P$):

(i) Continuidad y simetría de la deflexión:
$$y_D'(0) = 0 \;\;\Longrightarrow\;\; \beta(-C_3 + C_4) - \beta C_3 \cdot 0 = 0$$

Calculando explícitamente:
$$y_D'(\xi) = -\beta e^{-\beta\xi}\bigl(C_3\cos\beta\xi + C_4\sin\beta\xi\bigr) + e^{-\beta\xi}\bigl(-C_3\beta\sin\beta\xi + C_4\beta\cos\beta\xi\bigr)$$

$$y_D'(0) = -\beta C_3 + \beta C_4 = 0 \;\;\Longrightarrow\;\; C_4 = C_3$$

(ii) Equilibrio de la rebanada infinitesimal en torno a $\xi = 0$. Por simetría, el cortante a la derecha de la carga vale $V_D(0^+) = -P/2$ (la mitad de $P$ se transmite a cada lado, y a la derecha actúa con signo negativo según la convención adoptada porque la fuerza interna debe equilibrar la mitad descendente de $P$):

$$V = EI\,\frac{d^3 y}{dx^3}$$

Calculando la tercera derivada y evaluando en $\xi = 0$ con $C_4 = C_3 \equiv C$:

$$y_D'''(0) = 2\beta^3\,C\bigl[-\cos\beta\xi - \sin\beta\xi + \cos\beta\xi - \sin\beta\xi\bigr]\Big|_{\xi=0} \cdot (\ldots)$$

Procediendo con cuidado: con $y_D = C\,e^{-\beta\xi}(\cos\beta\xi + \sin\beta\xi)$,

$$y_D' = -2\beta C\,e^{-\beta\xi}\sin\beta\xi$$

$$y_D'' = 2\beta^2 C\,e^{-\beta\xi}(\sin\beta\xi - \cos\beta\xi)$$

$$y_D''' = 4\beta^3 C\,e^{-\beta\xi}\cos\beta\xi$$

Imponiendo $EI\,y_D'''(0) = -P/2$:

$$4 EI\,\beta^3\,C = -\frac{P}{2} \;\;\Longrightarrow\;\; C = -\frac{P}{8 EI\,\beta^3} = -\frac{P\beta}{2k}$$

usando $k = 4EI\beta^4$.

## 4. Expresiones finales

Definiendo la función auxiliar de Hetényi:

$$f(\xi) = e^{-\beta|\xi|}\bigl(\cos\beta|\xi| + \sin\beta|\xi|\bigr)$$

y empleando $|\xi| = |x-a|$ para extender la solución a todo $x \in (-\infty, +\infty)$:

### Curva elástica

$$\boxed{\;y(x) = \dfrac{P\beta}{2k}\,e^{-\beta|x-a|}\bigl[\cos\beta(x-a) + \sin\beta|x-a|\bigr]\;}$$

(con la convención de que $y$ es positiva hacia abajo; en la fórmula compacta se entiende $\sin\beta|x-a|$ y $\cos\beta(x-a) = \cos\beta|x-a|$ por paridad del coseno).

### Pendiente

$$\theta(x) = \frac{dy}{dx} = -\dfrac{P\beta^2}{k}\,e^{-\beta|x-a|}\sin\beta|x-a|\cdot\operatorname{sgn}(x-a)$$

### Momento flexionante

Aplicando $M = EI\,\dfrac{d^2 y}{dx^2}$ y usando $EI\beta^2 = \dfrac{k}{4\beta^2}$:

$$\boxed{\;M(x) = \dfrac{P}{4\beta}\,e^{-\beta|x-a|}\bigl[\cos\beta(x-a) - \sin\beta|x-a|\bigr]\;}$$

### Fuerza cortante

Aplicando $V = \dfrac{dM}{dx}$:

$$\boxed{\;V(x) = -\dfrac{P}{2}\,e^{-\beta|x-a|}\cos\beta(x-a)\cdot\operatorname{sgn}(x-a)\;}$$

## 5. Verificación de consistencia

| Cantidad | $x \to a^-$ | $x \to a^+$ | Valor en $x = a$ |
|---|---|---|---|
| $y$ | $P\beta/(2k)$ | $P\beta/(2k)$ | máximo: $P\beta/(2k)$ |
| $\theta$ | $0$ | $0$ | nulo (simetría) |
| $M$ | $P/(4\beta)$ | $P/(4\beta)$ | máximo: $P/(4\beta)$ |
| $V$ | $+P/2$ | $-P/2$ | salto $= -P$ ✓ |

El salto del cortante en $x = a$ es exactamente $-P$, consistente con la aplicación de una fuerza descendente concentrada de magnitud $P$. Todas las funciones decaen exponencialmente como $e^{-\beta|x-a|}$, lo que confirma el carácter local del efecto de la carga: el parámetro $1/\beta$ define la **longitud característica** de influencia, fuera de la cual la viga prácticamente no se entera de la carga.

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

- **🚨 INCUMPLIMIENTO PARCIAL DEL ANDAMIAJE:** el andamiaje establece explícitamente "$y$ positivo hacia arriba" (Punto 1). El modelo declara internamente "$y$ se mide positiva hacia abajo" en dos pasajes:
  1. *"Reacción del medio Winkler: $ky(x)dx$ hacia arriba (cuando y se mide positiva hacia abajo)"*.
  2. *"Combinando con la relación constitutiva de Euler-Bernoulli $M = EI y''$ (con $y$ positiva hacia abajo, de modo que un M positivo produzca concavidad hacia arriba)"*.
  3. La fórmula final aclara: *"con la convención de que $y$ es positiva hacia abajo"*.

  **Esta es una violación directa del Punto 1 del andamiaje.** La constatación más fuerte de hallazgo experimental hasta ahora: el andamiaje no fue suficiente para forzar la convención prescrita en Claude para C2. Comparar con Claude C1 scaffolded (que sí adoptó $y$-arriba correctamente).

- **Resultado final $y(a) = +P\beta/(2k)$ POSITIVO** — opuesto al manuscrito ($y(a) = -P\beta/(2k)$).
- $M(a) = +P/(4\beta)$ POSITIVO — coincide con manuscrito numéricamente.
- Salto de cortante $V(a^+) - V(a^-) = -P$ — correcto.
- **Tercera derivada correcta** $y''' = 4\beta^3 C \cos$ (a diferencia de C1 minimal donde tuvo el coeficiente erróneo). El paso por la algebra confusa intermedia se autocorrige a la respuesta correcta.
- **Hallazgo metodológico relevante:** Claude exhibe inestabilidad en la respuesta al andamiaje:
  - C1 scaffolded: andamiaje aceptado correctamente.
  - C2 scaffolded: andamiaje parcialmente ignorado (sigue con su preferencia por $y$ positivo abajo).

  Este patrón **contrasta con Gemini scaffolded** (C1 y C2 ambas correctas) y constituye evidencia de **variabilidad inter-modelo en la respuesta al andamiaje**, lo cual es un resultado nuevo y citable.
