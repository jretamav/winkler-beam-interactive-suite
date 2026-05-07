# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C2 — Viga infinita Winkler con carga puntual descentrada en x = a
- **Modelo:** claude-opus-4-7
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 18:29:43 (CDMX, UTC−6) — inicio. Finalización 18:30:15
- **Tiempo de respuesta:** ~32 segundos
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
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en la posición x = a, donde a es una distancia conocida medida hacia la derecha del origen.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), válidas para todo x perteneciente al intervalo (-infinito, +infinito).
```

---

## Salida del modelo

# Viga infinita sobre fundación elástica de Winkler con carga puntual

## Planteamiento del problema

La ecuación diferencial que gobierna la deflexión de una viga sobre fundación de Winkler es:

$$EI \frac{d^4 y}{dx^4} + k\, y = q(x)$$

Para una carga puntual $P$ descendente aplicada en $x = a$, el término forzante es $q(x) = -P\,\delta(x-a)$ (negativo porque $y$ se mide positivo hacia arriba y $P$ actúa hacia abajo).

## Definición del parámetro característico

Se define la **longitud característica** mediante:

$$\beta = \sqrt[4]{\frac{k}{4EI}}$$

de modo que la ecuación homogénea se escribe como $y^{(4)} + 4\beta^4 y = 0$, cuya solución general involucra los términos $e^{\pm\beta x}\cos(\beta x)$ y $e^{\pm\beta x}\sin(\beta x)$.

## Condiciones del problema

Para la viga **infinita**, se imponen:

1. **Condición de regularidad en el infinito:** $y \to 0$ cuando $|x| \to \infty$, lo que descarta los términos con crecimiento exponencial en cada semi-recta.
2. **Simetría respecto al punto de aplicación:** la deflexión debe ser simétrica respecto a $x = a$, por lo tanto $y'(a) = 0$.
3. **Equilibrio del cortante en $x = a$:** la discontinuidad del cortante debe equilibrar la carga aplicada. Por simetría, cada semi-viga toma la mitad: $V(a^+) - V(a^-) = -P$, lo que conduce a $V(a^+) = -P/2$.

## Solución de la curva elástica

Definiendo la coordenada relativa $\xi = x - a$, la solución que satisface las condiciones anteriores es:

$$\boxed{\,y(x) = -\frac{P\beta}{2k}\, e^{-\beta|x-a|}\bigl[\cos(\beta|x-a|) + \sin(\beta|x-a|)\bigr]\,}$$

El signo negativo indica que la viga se deflecta hacia abajo bajo la carga descendente. La función es par respecto a $x = a$ y decae oscilando exponencialmente al alejarse del punto de aplicación.

**Deflexión máxima** (en $x = a$):

$$y_{\max} = -\frac{P\beta}{2k}$$

## Funciones auxiliares

Para abreviar la presentación, se introducen las funciones clásicas de Hetényi:

$$A(\xi) = e^{-\beta\xi}[\cos(\beta\xi) + \sin(\beta\xi)]$$
$$B(\xi) = e^{-\beta\xi}\sin(\beta\xi)$$
$$C(\xi) = e^{-\beta\xi}[\cos(\beta\xi) - \sin(\beta\xi)]$$
$$D(\xi) = e^{-\beta\xi}\cos(\beta\xi)$$

con las relaciones $A'=-2\beta B$, $B'=\beta C$, $C'=-2\beta D$, $D'=-\beta A$ (para $\xi \geq 0$).

## Momento flexionante

Aplicando la convención $M(x) = -EI\, y''(x)$ y derivando dos veces (usando $|x-a|$ como argumento y notando que el valor absoluto preserva la paridad):

$$\boxed{\,M(x) = \frac{P}{4\beta}\, e^{-\beta|x-a|}\bigl[\cos(\beta|x-a|) - \sin(\beta|x-a|)\bigr]\,}$$

**Momento máximo** (en $x = a$):

$$M_{\max} = \frac{P}{4\beta}$$

## Fuerza cortante

Aplicando $V(x) = dM/dx$. Aquí debe tratarse cuidadosamente la derivada del valor absoluto, que introduce el factor $\operatorname{sgn}(x-a)$:

$$\boxed{\,V(x) = -\frac{P}{2}\,\operatorname{sgn}(x-a)\, e^{-\beta|x-a|}\cos\bigl(\beta|x-a|\bigr)\,}$$

donde $\operatorname{sgn}$ es la función signo. Obsérvese que $V(x)$ presenta una **discontinuidad de salto igual a** $-P$ en $x = a$, consistente con la carga puntual aplicada:

$$V(a^+) - V(a^-) = -\frac{P}{2} - \frac{P}{2} = -P$$

## Resumen de las soluciones

Definiendo $\xi = |x-a|$, las tres ecuaciones se compactan así:

$$y(x) = -\frac{P\beta}{2k}\,A(\xi), \qquad M(x) = \frac{P}{4\beta}\,C(\xi), \qquad V(x) = -\frac{P}{2}\operatorname{sgn}(x-a)\,D(\xi)$$

con $\beta = (k/4EI)^{1/4}$.

## Observaciones físicas

El parámetro $\beta$ tiene unidades de $[\text{longitud}]^{-1}$, y $1/\beta$ representa la longitud característica de decaimiento. Las soluciones muestran que el efecto de la carga se localiza prácticamente en una zona de extensión $\sim \pi/\beta$ alrededor del punto de aplicación: más allá de $x = a \pm \pi/\beta$ los esfuerzos son ya muy pequeños debido al amortiguamiento exponencial, y por eso una viga real de longitud $L \gtrsim \pi/\beta$ se comporta a efectos prácticos como infinita. Las funciones presentan además ceros alternados característicos del comportamiento oscilatorio amortiguado típico de la fundación elástica.

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

- **❗ INCONSISTENCIA INTRA-MODELO:** Claude cambió la convención de signos respecto a su propia versión C1 minimal:
  - **Claude C1 minimal:** declara explícitamente "$y(x)$ es positivo hacia abajo" → $y(0) = +P\beta/(2k)$.
  - **Claude C2 minimal:** declara explícitamente "$y$ se mide positivo hacia arriba" → $y(a) = -P\beta/(2k)$.
  - **Esta inconsistencia entre sesiones es relevante** para la sección 4.5 del manuscrito como evidencia de inestabilidad de convención sin andamiaje, **incluso dentro del mismo modelo**.
- Curiosamente, mantuvo $M = -EI y''$ (que correspondería a $y$ positivo abajo), lo que crea una contradicción interna no resuelta entre la declaración inicial ("$y$ positivo arriba") y la relación constitutiva. A pesar de esto, el resultado final coincide algebraicamente con la referencia.
- **Resultado final $y(x), M(x), V(x)$:** algebraicamente equivalente al manuscrito y a la solución de referencia — incluyendo el signo negativo de $y$.
- **Estrategia metodológica:** evita derivar desde primeros principios; aprovecha la solución conocida de C1 (Hetényi) y aplica traslación $|x| \to |x-a|$. Limpio y eficiente.
- **Salto de cortante calculado correctamente:** $V(a^+) - V(a^-) = -P$, congruente con el manuscrito.
- **Funciones auxiliares de Hetényi** $A, B, C, D$ utilizadas para compactar el resultado, con sus relaciones de derivación enunciadas.
