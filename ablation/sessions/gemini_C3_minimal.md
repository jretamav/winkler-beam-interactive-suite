# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C3 — Viga finita Winkler, extremos libres, carga puntual al centro (x = L/2)
- **Modelo:** gemini-3.1-pro (selector "Pro")
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 18:04:36 (CDMX, UTC−6) — inicio. Finalización 18:06:05
- **Versión exacta del modelo:** Gemini 3.1 Pro
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** TEMPORAL (verificado)
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada
- **¿Se requirió pedir "continuar"?:** No
- **Longitud de la respuesta:** larga
- **Verificación de no-contaminación:** usuario neutro, sin "doctor"

---

## Prompt enviado

```
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud finita L, apoyada sobre un medio elástico tipo Winkler con módulo de balasto k. Ambos extremos de la viga, en x = 0 y en x = L, son libres (no existen reacciones externas en los extremos). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en el centro de la viga, es decir, en x = L/2.

Derive la ecuación analítica de la curva elástica y(x), del momento flexionante M(x) y de la fuerza cortante V(x), aplicando explícitamente las cuatro condiciones de frontera correspondientes a los extremos libres.
```

---

## Salida del modelo

Para derivar la solución analítica de una viga sobre una fundación elástica de Winkler, el enfoque más elegante y directo es utilizar el **Método de los Parámetros Iniciales** apoyado en las **Funciones de Krylov** (también conocidas como funciones de Maclaurin o Clebsch). Esto nos permite manejar la discontinuidad de la carga puntual y aplicar las condiciones de frontera de forma sistemática.

### 1. Ecuación Diferencial Gobernante

Considerando un sistema de coordenadas donde $x = 0$ está en el extremo izquierdo de la viga y la deflexión $y(x)$ es positiva hacia abajo, la ecuación diferencial de la curva elástica es:

$$EI \frac{d^4y}{dx^4} + ky = q(x)$$

Definimos el parámetro de rigidez del sistema, $\lambda$, como:

$$\lambda = \sqrt[4]{\frac{k}{4EI}}$$

Para una carga puntual descendente $P$ aplicada en $x = L/2$, la ecuación se puede resolver de manera generalizada utilizando la función escalón de Heaviside $H(x - L/2)$.

---

### 2. Funciones de Krylov

Para construir la solución, definimos las cuatro Funciones de Krylov dependientes de una variable adimensional $u = \lambda x$:

$$K_1(u) = \cosh(u) \cos(u)$$
$$K_2(u) = \frac{1}{2}(\cosh(u) \sin(u) + \sinh(u) \cos(u))$$
$$K_3(u) = \frac{1}{2}\sinh(u) \sin(u)$$
$$K_4(u) = \frac{1}{4}(\cosh(u) \sin(u) - \sinh(u) \cos(u))$$

Las derivadas de estas funciones tienen un comportamiento cíclico útil:
*   $K_1' = -4K_4$
*   $K_2' = K_1$
*   $K_3' = K_2$
*   $K_4' = K_3$

---

### 3. Solución General y Condiciones de Frontera en $x = 0$

La ecuación general de la elástica mediante parámetros iniciales es:

$$y(x) = y(0) K_1(\lambda x) + \frac{y'(0)}{\lambda} K_2(\lambda x) + \frac{y''(0)}{\lambda^2} K_3(\lambda x) + \frac{y'''(0)}{\lambda^3} K_4(\lambda x) + y_P(x)$$

Donde $y_P(x)$ es la solución particular por la carga $P$.

Aplicamos explícitamente las **dos primeras condiciones de frontera** en el extremo libre $x = 0$:
1.  **Momento nulo:** $M(0) = -EI y''(0) = 0 \implies y''(0) = 0$
2.  **Cortante nulo:** $V(0) = -EI y'''(0) = 0 \implies y'''(0) = 0$

Esto elimina los términos $K_3$ y $K_4$ de la parte homogénea. Si renombramos las constantes iniciales como $C_1 = y(0)$ y $C_2 = y'(0)/\lambda$, y agregamos el salto provocado por la carga $P$, la ecuación de la elástica se simplifica a:

$$y(x) = C_1 K_1(\lambda x) + C_2 K_2(\lambda x) + \frac{P}{EI \lambda^3} K_4\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right)$$

---

### 4. Derivadas, Momento y Cortante

Derivando $y(x)$ y multiplicando por las rigideces correspondientes, obtenemos las ecuaciones analíticas de Momento Flexionante $M(x)$ y Fuerza Cortante $V(x)$:

**Derivada segunda (asociada al momento):**
$$y''(x) = \lambda^2 \left[ -4C_1 K_3(\lambda x) - 4C_2 K_4(\lambda x) + \frac{P}{EI \lambda^3} K_2\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right) \right]$$

**Derivada tercera (asociada al cortante):**
$$y'''(x) = \lambda^3 \left[ -4C_1 K_2(\lambda x) - 4C_2 K_3(\lambda x) + \frac{P}{EI \lambda^3} K_1\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right) \right]$$

---

### 5. Condiciones de Frontera en $x = L$

Para encontrar $C_1$ y $C_2$, aplicamos las **dos últimas condiciones de frontera** en el extremo libre $x = L$. En este punto, $x > L/2$, por lo que $H(x - L/2) = 1$.

3.  **Momento nulo en el extremo derecho:** $M(L) = 0 \implies y''(L) = 0$
$$-4C_1 K_3(\lambda L) - 4C_2 K_4(\lambda L) + \frac{P}{EI \lambda^3} K_2\left(\lambda \frac{L}{2}\right) = 0$$

4.  **Cortante nulo en el extremo derecho:** $V(L) = 0 \implies y'''(L) = 0$
$$-4C_1 K_2(\lambda L) - 4C_2 K_3(\lambda L) + \frac{P}{EI \lambda^3} K_1\left(\lambda \frac{L}{2}\right) = 0$$

Para simplificar la notación de la solución, definamos un parámetro de carga modificado $P_0 = \frac{P}{4EI \lambda^3}$, y denotemos $K_{iL} = K_i(\lambda L)$ y $K_{iM} = K_i(\lambda L / 2)$. El sistema lineal queda:

$$C_1 K_{3L} + C_2 K_{4L} = P_0 K_{2M}$$
$$C_1 K_{2L} + C_2 K_{3L} = P_0 K_{1M}$$

Resolviendo por la regla de Cramer, donde el determinante del sistema es $\Delta = K_{3L}^2 - K_{2L}K_{4L}$:

$$C_1 = \frac{P_0 (K_{2M} K_{3L} - K_{1M} K_{4L})}{\Delta}$$
$$C_2 = \frac{P_0 (K_{1M} K_{3L} - K_{2M} K_{2L})}{\Delta}$$

---

### 6. Ecuaciones Analíticas Finales

Con las constantes $C_1$ y $C_2$ calculadas, las ecuaciones cerradas que describen la mecánica de la viga en todo su dominio $x \in [0, L]$ son:

**Curva Elástica (Deflexión):**
$$y(x) = C_1 K_1(\lambda x) + C_2 K_2(\lambda x) + \frac{P}{EI \lambda^3} K_4\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right)$$

**Momento Flexionante $M(x) = -EI y''(x)$:**
$$M(x) = 4 EI \lambda^2 \left[ C_1 K_3(\lambda x) + C_2 K_4(\lambda x) \right] - \frac{P}{\lambda} K_2\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right)$$

**Fuerza Cortante $V(x) = -EI y'''(x)$:**
$$V(x) = 4 EI \lambda^3 \left[ C_1 K_2(\lambda x) + C_2 K_3(\lambda x) \right] - P K_1\left(\lambda\left(x - \frac{L}{2}\right)\right) H\left(x - \frac{L}{2}\right)$$

Estas ecuaciones representan la solución exacta y continua a trozos, garantizando que los extremos carezcan de reacciones parásitas y modelando fielmente el salto de cortante de magnitud $P$ en el centro de la viga.

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

- **Enfoque metodológico:** usó el **Método de Parámetros Iniciales con Funciones de Krylov** (Maclaurin/Clebsch). Es un enfoque sofisticado y elegante para vigas finitas, alternativo a la solución por exponenciales de la ecuación característica.
- Adoptó **convención $y$ positivo hacia abajo**, opuesta al manuscrito (consistente con C1 y C2 minimal).
- Usó $M = -EI y''$, $V = -EI y'''$ (consistentes con su convención).
- **Aplicó las 4 condiciones de frontera correctamente:** $M(0)=V(0)=0$ y $M(L)=V(L)=0$.
- **Aplicó las CB en orden óptimo:** primero las de $x=0$ para reducir a 2 constantes, luego las de $x=L$ para resolver sistema 2×2.
- Resolvió el sistema lineal por regla de Cramer.
- Manejo correcto del salto de cortante con función Heaviside $H(x-L/2)$ — añade $K_4(\lambda(x-L/2))$ tras el punto de carga.
- **Anomalía notable:** definió $P_0 = P/(4EI\lambda^3)$ pero las ecuaciones del sistema usan $P/(EI\lambda^3)$ — inconsistencia notacional que requiere verificación cuidadosa al evaluar M5.
- La solución final NO se reduce a una forma cerrada explícita pero sí queda como expresión analítica completa con constantes $C_1, C_2$ determinadas.
