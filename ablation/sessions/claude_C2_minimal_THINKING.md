# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C2 — Viga infinita Winkler con carga puntual descentrada en x = a
- **Modelo:** claude-opus-4-7
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 19:48:58 (CDMX, UTC−6) — inicio. Finalización 19:51:15
- **Tiempo de respuesta:** ~2 min 17 s (137 segundos)
- **Versión exacta del modelo:** Claude Opus 4.7
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** Ventana de incógnito + sesión limpia
- **Estado de Memoria de Claude:** desactivada
- **Pensamiento adaptativo (extended thinking):** **ACTIVADO**
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

# Viga infinita sobre fundación elástica de Winkler

## Ecuación de gobierno

Adoptando el convenio en que $y(x)$ es positiva hacia abajo (en el sentido de $P$), $q(x)$ es la carga distribuida positiva hacia abajo, y la reacción del medio elástico vale $ky$ por unidad de longitud (actuando hacia arriba), el equilibrio de un elemento diferencial conduce a la conocida ecuación de la viga sobre fundación elástica:

$$
EI\,\frac{d^{4}y}{dx^{4}} + k\,y \;=\; q(x).
$$

Para una carga puntual $P$ aplicada en $x=a$:

$$
EI\,\frac{d^{4}y}{dx^{4}} + k\,y \;=\; P\,\delta(x-a).
$$

Es conveniente definir el **parámetro característico** (longitud inversa) de la viga sobre fundación:

$$
\boxed{\;\beta \;=\; \sqrt[4]{\dfrac{k}{4\,EI}}\;}\qquad\Longleftrightarrow\qquad 4\,EI\,\beta^{4}=k.
$$

## Solución homogénea y condiciones físicas

Sea $\xi = x-a$ la coordenada local desde el punto de aplicación de la carga. Para $\xi\neq 0$ la ecuación se reduce a

$$
\frac{d^{4}y}{d\xi^{4}} + 4\beta^{4}\,y \;=\; 0,
$$

cuyas raíces características son $\beta(\pm 1\pm i)$. La solución general combina los modos $e^{\pm\beta\xi}\cos\beta\xi$ y $e^{\pm\beta\xi}\sin\beta\xi$.

Dado que la viga es infinita, exigimos **que la deformada se anule en el infinito**: $y\to 0$ cuando $|\xi|\to\infty$. Esto descarta los modos crecientes y deja, por tramos:

$$
y(\xi)=\begin{cases}
e^{-\beta\xi}\bigl(A\cos\beta\xi+B\sin\beta\xi\bigr), & \xi>0,\\[4pt]
e^{+\beta\xi}\bigl(C\cos\beta\xi+D\sin\beta\xi\bigr), & \xi<0.
\end{cases}
$$

El problema es **simétrico** respecto a $\xi=0$ (la geometría, la rigidez del medio y el punto de aplicación de la carga lo son), por lo tanto $y(\xi)=y(-\xi)$ y la pendiente se anula bajo la carga, $y'(0)=0$. Estas condiciones implican $C=A$, $D=-B$, y además $A=B$. La forma simétrica se escribe compactamente como

$$
y(\xi) \;=\; A\,e^{-\beta|\xi|}\bigl(\cos\beta|\xi|+\sin\beta|\xi|\bigr).
$$

## Determinación de la constante: salto de cortante

Integrando la ecuación con la delta entre $\xi=0^{-}$ y $\xi=0^{+}$ se obtiene la condición de salto del cortante (el término $ky$ no contribuye en el límite):

$$
EI\bigl[y'''(0^{+})-y'''(0^{-})\bigr]\;=\;P.
$$

Por la simetría, $y'''$ es una función impar, de modo que $y'''(0^{-})=-y'''(0^{+})$ y por tanto

$$
y'''(0^{+}) \;=\; \frac{P}{2\,EI}.
$$

Derivando $f(\xi)=e^{-\beta\xi}(\cos\beta\xi+\sin\beta\xi)$ tres veces (para $\xi>0$):

$$
f'''(\xi)=4\beta^{3}e^{-\beta\xi}\cos\beta\xi \;\Longrightarrow\; f'''(0^{+})=4\beta^{3}.
$$

Sustituyendo:

$$
A\cdot 4\beta^{3} \;=\; \frac{P}{2EI}\;\Longrightarrow\; A \;=\; \frac{P}{8EI\beta^{3}} \;=\; \frac{P\beta}{2k},
$$

donde se usó $8EI\beta^{3}=2k/\beta$.

## Resultado para la curva elástica

$$
\boxed{\;y(x) \;=\; \dfrac{P\beta}{2k}\;e^{-\beta\,|x-a|}\Bigl[\cos\bigl(\beta|x-a|\bigr)+\sin\bigl(\beta|x-a|\bigr)\Bigr]\;}
$$

válida para todo $x\in(-\infty,+\infty)$. La flecha máxima ocurre bajo la carga: $y_{\max}=y(a)=P\beta/(2k)$.

## Momento flexionante

Con el convenio $M(x)=-EI\,y''(x)$. Usando $f''(\xi)=2\beta^{2}e^{-\beta\xi}(\sin\beta\xi-\cos\beta\xi)$ y la relación $EI/k=1/(4\beta^{4})$:

$$
\boxed{\;M(x) \;=\; \dfrac{P}{4\beta}\;e^{-\beta\,|x-a|}\Bigl[\cos\bigl(\beta|x-a|\bigr)-\sin\bigl(\beta|x-a|\bigr)\Bigr]\;}
$$

El momento es una función **par** respecto a $x=a$, con su máximo justo bajo la carga: $M_{\max}=M(a)=P/(4\beta)$.

## Fuerza cortante

Aplicando $V(x)=dM/dx$ (equivalente a $V=-EI\,y'''$) y notando que la derivada de una función par de $(x-a)$ es impar en $(x-a)$:

$$
\boxed{\;V(x) \;=\; -\dfrac{P}{2}\;\operatorname{sgn}(x-a)\;e^{-\beta\,|x-a|}\cos\bigl(\beta|x-a|\bigr)\;}
$$

La cortante es **antisimétrica** respecto a $x=a$ y presenta el salto característico $V(a^{+})-V(a^{-})=-P$, consistente con la aplicación de la carga concentrada descendente.

## Comentarios físicos

Las tres funciones presentan un **decaimiento exponencial amortiguado y oscilante** controlado por la longitud característica $\ell = 1/\beta = \sqrt[4]{4EI/k}$. Para distancias $|x-a| \gtrsim \pi/\beta$ las amplitudes son ya prácticamente nulas, lo que justifica físicamente la idealización de "viga infinita": en la práctica basta con que la viga real se extienda algunos múltiplos de $\ell$ a cada lado de la carga para que estas expresiones constituyan una excelente aproximación. Además, una verificación inmediata confirma que la integral de la reacción del medio, $\int_{-\infty}^{\infty} k\,y(x)\,dx = P$, recupera el equilibrio global de la viga.

---

## Evaluación según rúbrica (`rubric.md`)

| Métrica | Valor |
|---|---|
| **M1** — Coherencia de signos | 0 |
| **M2** — Coherencia dimensional | 1 |
| **M3** — Aplicación correcta de CB | 1 |
| **M4** — Correctitud de solución final | 1 |
| **M5** — Errores algebraicos contables | 0 |

## Justificación cualitativa de la evaluación

- **M1 = 0:** Claude declara explícitamente "$y(x)$ es positiva hacia abajo". $y(a) = +P\beta/(2k)$ POSITIVO, opuesto a la convención del manuscrito.
- **M2 = 1:** dimensiones consistentes.
- **M3 = 1:** las 3 CB correctas. Uso explícito de la simetría para deducir $y'''(0^+) = P/(2EI)$ desde el salto integrado.
- **M4 = 1:** estructura algebraica idéntica a la referencia (Opción B: signo global no penaliza).
- **M5 = 0:** sin errores algebraicos detectables. Verificación final $\int k\,y\,dx = P$ explícitamente mencionada.

### Comparación con la versión NOTHINKING (`claude_C2_minimal_NOTHINKING.md`)

| Métrica | NOTHINKING | THINKING |
|---|---|---|
| M1 | **1** | **0** ← REVIRTIÓ |
| M2 | 1 | 1 |
| M3 | 1 | 1 |
| M4 | 1 | 1 |
| M5 | 0 | 0 |
| Tiempo | 32 s | 137 s (4×) |

### Hallazgo metodológico

La "anomalía" detectada en la versión NOTHINKING (M1=1 en condición minimal — única excepción de Claude minimal) **desaparece con pensamiento adaptativo activado**. En NOTHINKING Claude declaraba $y$-arriba pero usaba $M = -EI y''$ (combinación inconsistente que casualmente daba el signo correcto del manuscrito). Con pensamiento, Claude **limpia esa inconsistencia interna** y se queda con su default $y$-abajo coherente, perdiendo el M1=1 que tenía por error.

**Implicación:** el pensamiento adaptativo elimina contradicciones internas pero refuerza el default de convención, no lo altera. El default $y$-abajo en Claude minimal es **más robusto** con pensamiento que sin él.
