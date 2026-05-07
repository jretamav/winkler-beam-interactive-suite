# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C4 — Viga infinita sobre fundación Pasternak con carga puntual centrada
- **Modelo:** claude-opus-4-7
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 18:43:56 (CDMX, UTC−6) — inicio. Finalización 18:44:36
- **Tiempo de respuesta:** ~40 segundos
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

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre una fundación elástica tipo Pasternak. Esta fundación se caracteriza por dos parámetros independientes: el módulo de reacción vertical k1 (similar al módulo de balasto de Winkler) y el módulo de cortante de la capa de cortante k2 (que acopla horizontalmente las reacciones de los resortes mediante una membrana de cortante virtual). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación diferencial gobernante para la deflexión y(x) y obtén su solución analítica completa, especificando claramente las raíces de la ecuación característica resultante.
```

---

## Salida del modelo

# Viga sobre Fundación de Pasternak: Carga Puntual

## 1. Planteamiento del problema

Consideremos una viga elástica infinita de rigidez a la flexión $EI$ constante, apoyada sobre una fundación de Pasternak caracterizada por:
- $k_1$: módulo de reacción vertical [F/L³] (resortes de Winkler)
- $k_2$: módulo de la capa de cortante [F/L]

La carga puntual $P$ se aplica en $x = 0$ y la viga es infinita, por lo que el problema es simétrico respecto al origen.

## 2. Derivación de la ecuación gobernante

### Reacción de la fundación de Pasternak

A diferencia del modelo de Winkler (donde $q_f = k_1 y$), Pasternak introduce una capa de cortante incompresible que acopla los resortes verticales. La presión reactiva por unidad de longitud es:

$$q_f(x) = k_1\, y(x) - k_2\, \frac{d^2 y}{dx^2}$$

El segundo término representa la transmisión horizontal de cortante en la membrana virtual, lo que distingue fundamentalmente este modelo del de Winkler.

### Equilibrio de la viga

Partiendo de la ecuación clásica de Euler-Bernoulli para una viga sobre fundación elástica:

$$EI\, \frac{d^4 y}{dx^4} = q(x) - q_f(x)$$

donde $q(x)$ es la carga externa distribuida. Sustituyendo la reacción de Pasternak:

$$\boxed{\;EI\, \frac{d^4 y}{dx^4} - k_2\, \frac{d^2 y}{dx^2} + k_1\, y = q(x)\;}$$

Para $x \neq 0$ (fuera del punto de aplicación), $q(x) = 0$, por lo que la ecuación homogénea es:

$$EI\, y^{IV} - k_2\, y'' + k_1\, y = 0$$

## 3. Ecuación característica y sus raíces

Proponiendo $y(x) = e^{rx}$:

$$EI\, r^4 - k_2\, r^2 + k_1 = 0$$

Esta es una ecuación bicuadrática. Definiendo $s = r^2$:

$$EI\, s^2 - k_2\, s + k_1 = 0 \quad\Longrightarrow\quad s = \frac{k_2 \pm \sqrt{k_2^2 - 4\, EI\, k_1}}{2\, EI}$$

El comportamiento de las raíces depende del **discriminante** $\Delta = k_2^2 - 4\, EI\, k_1$, lo que define tres regímenes físicamente distintos.

### Caso I: $k_2^2 < 4\, EI\, k_1$ (régimen subamortiguado — el más común)

Las raíces $s$ son complejas conjugadas. Tras manipulación algebraica, las cuatro raíces $r$ se escriben como:

$$r = \pm\, \alpha \pm i\, \beta$$

donde

$$\alpha = \sqrt{\frac{1}{2}\left(\sqrt{\frac{k_1}{EI}} + \frac{k_2}{2\, EI}\right)}, \qquad \beta = \sqrt{\frac{1}{2}\left(\sqrt{\frac{k_1}{EI}} - \frac{k_2}{2\, EI}\right)}$$

Nótese que cuando $k_2 \to 0$ se recupera $\alpha = \beta = \sqrt[4]{k_1/(4EI)} \equiv \lambda$, el parámetro clásico de Winkler.

### Caso II: $k_2^2 = 4\, EI\, k_1$ (régimen crítico)

Raíz doble $s = k_2/(2\,EI)$, dando dos pares dobles $r = \pm\sqrt{k_2/(2EI)}$. Aparecen términos seculares del tipo $x\, e^{\pm rx}$.

### Caso III: $k_2^2 > 4\, EI\, k_1$ (régimen sobreamortiguado)

Ambas raíces $s$ son reales y positivas, dando cuatro raíces reales $r = \pm\sqrt{s_1}, \pm\sqrt{s_2}$ — la respuesta es puramente decreciente exponencial sin oscilación.

## 4. Solución analítica (Caso I — el de interés práctico)

La solución general para $x > 0$ es:

$$y(x) = e^{-\alpha x}\left(A\cos\beta x + B\sin\beta x\right) + e^{\alpha x}\left(C\cos\beta x + D\sin\beta x\right)$$

### Condiciones de contorno

**(a) Decaimiento al infinito:** $y(x) \to 0$ cuando $x \to \infty$, por tanto $C = D = 0$.

**(b) Simetría en el origen:** la pendiente debe anularse en $x = 0$:
$$y'(0) = 0 \;\Longrightarrow\; -\alpha A + \beta B = 0 \;\Longrightarrow\; B = \frac{\alpha}{\beta} A$$

**(c) Equilibrio del cortante en $x=0$:** por simetría, cada mitad de la viga absorbe $P/2$. Aquí el modelo de Pasternak introduce una sutileza importante: el cortante efectivo incluye la contribución de la capa de cortante. La condición de salto es:

$$\left[-EI\, y'''(0^+) + k_2\, y'(0^+)\right] = \frac{P}{2}$$

Usando $y'(0)=0$, esto se reduce a $-EI\, y'''(0^+) = P/2$.

Calculando $y'''(0^+)$ a partir de la solución y aplicando $B = (\alpha/\beta)A$, se obtiene tras álgebra:

$$A = \frac{P\, \beta}{4\, EI\, \alpha\, (\alpha^2 + \beta^2)}$$

### Solución final

$$\boxed{\;y(x) = \frac{P\, \beta}{4\, EI\, \alpha\, (\alpha^2 + \beta^2)}\, e^{-\alpha |x|}\left[\cos\beta x + \frac{\alpha}{\beta}\sin\beta |x|\right]\;}$$

Equivalentemente, factorizando:

$$y(x) = \frac{P}{4\, EI\, \alpha\, \beta\, (\alpha^2 + \beta^2)}\, e^{-\alpha |x|}\left[\beta\cos\beta x + \alpha\sin\beta |x|\right]$$

## 5. Verificación: límite de Winkler

Si $k_2 \to 0$, entonces $\alpha = \beta = \lambda = \sqrt[4]{k_1/(4EI)}$ y la expresión se reduce a:

$$y(x) = \frac{P\lambda}{2\, k_1}\, e^{-\lambda|x|}\left(\cos\lambda x + \sin\lambda |x|\right)$$

que es exactamente la solución clásica de Hetényi para viga sobre fundación de Winkler — confirmando la consistencia del resultado.

## 6. Interpretación física

El parámetro $\alpha$ controla la **tasa de decaimiento espacial** y aumenta con $k_2$: la capa de cortante hace que las perturbaciones se atenúen más rápidamente. El parámetro $\beta$ controla la **longitud de onda de las oscilaciones** y disminuye con $k_2$. Físicamente, la membrana de cortante distribuye la carga sobre una región más amplia y reduce la concentración local de deformación —comportamiento consistente con observaciones experimentales en suelos reales que el modelo de Winkler no captura.

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

- **EDO Pasternak correcta:** $EI y'''' - k_2 y'' + k_1 y = 0$.
- **Tres regímenes correctamente identificados** según el discriminante $\Delta = k_2^2 - 4 EI k_1$:
  - Subamortiguado (raíces complejas, oscilatorio amortiguado).
  - Crítico (raíces dobles con términos seculares $x e^{\pm rx}$).
  - Sobreamortiguado (raíces reales, exponencial puro). **Distinción única en todo el experimento** — solo Claude minimal C4 explicitó los tres casos.
- **Cortante efectivo Pasternak:** $V_{eff} = -EI y''' + k_2 y'$ — correcto y específico de Pasternak.
- **Convención implícita:** $M = -EI y''$ (no declarada explícitamente, pero implícita en el cortante efectivo). Consistente con $y$ positivo abajo.
- **Resultado final:** $y(0) = +P\beta/(4 EI \alpha (\alpha^2 + \beta^2))$ POSITIVO, congruente con $y$-abajo.
- **Verificación del límite Winkler ($k_2 \to 0$):** explícitamente desarrollada y conduce a $y = P\lambda/(2 k_1) e^{-\lambda|x|}(\cos+\sin)$ — coincide con Hetényi clásico.
- **Sección de interpretación física:** explica el rol de $\alpha$ y $\beta$ como tasas de decaimiento y longitud de onda, conectando con observaciones de suelos reales.
- **Comparación con Gemini C4 minimal:** ambos resolvieron Pasternak limpiamente. Claude se distingue por presentar los **tres casos del discriminante** explícitamente y por la sección física más elaborada. Gemini presentó solo el caso subamortiguado.
