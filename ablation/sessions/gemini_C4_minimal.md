# Bitácora de ejecución — Estudio de ablación

## Metadatos

- **Caso:** C4 — Viga infinita sobre fundación Pasternak con carga puntual centrada
- **Modelo:** gemini-3.1-pro (selector "Pro")
- **Condición:** minimal (sin andamiaje fenomenológico)
- **Fecha y hora de ejecución:** 2026-05-06 18:12:44 (CDMX, UTC−6) — inicio. Finalización 18:13:50
- **Versión exacta del modelo:** Gemini 3.1 Pro
- **Operador:** Jaime Retama Velasco
- **Tipo de chat:** TEMPORAL (verificado)
- **Estado de Memoria/Actividad de Gemini:** Actividad desactivada
- **¿Se requirió pedir "continuar"?:** No
- **Longitud de la respuesta:** larga
- **Verificación de no-contaminación:** usuario neutro

---

## Prompt enviado

```
Resuelve el siguiente problema de mecánica estructural:

Considere una viga prismática elástica, de rigidez a la flexión EI constante, de longitud infinita, apoyada sobre una fundación elástica tipo Pasternak. Esta fundación se caracteriza por dos parámetros independientes: el módulo de reacción vertical k1 (similar al módulo de balasto de Winkler) y el módulo de cortante de la capa de cortante k2 (que acopla horizontalmente las reacciones de los resortes mediante una membrana de cortante virtual). La viga se encuentra sometida a una carga puntual concentrada P, descendente, aplicada en x = 0.

Derive la ecuación diferencial gobernante para la deflexión y(x) y obtén su solución analítica completa, especificando claramente las raíces de la ecuación característica resultante.
```

---

## Salida del modelo

Para resolver este clásico problema de interacción suelo-estructura, procederemos paso a paso: desde el establecimiento de la ecuación diferencial hasta la aplicación de las condiciones de borde para encontrar la solución exacta.

### 1. Ecuación Diferencial Gobernante

Para una viga sometida a flexión, la ecuación diferencial fundamental relaciona la rigidez a la flexión ($EI$) y la deflexión ($y$) con la carga neta aplicada $q(x)$:
$$EI\frac{d^4y}{dx^4}=q_{ext}(x)-p(x)$$

En una fundación tipo Pasternak, la presión de reacción del suelo $p(x)$ consta de dos partes:
1.  La contribución de los resortes independientes (Winkler): $k_1 y(x)$
2.  La contribución de la capa de cortante que acopla los resortes: $-k_2 \frac{d^2y}{dx^2}$

Como la carga puntual $P$ actúa únicamente en $x = 0$, para cualquier punto donde $x \neq 0$, la carga externa $q_{ext}(x)$ es cero. Sustituyendo $p(x)$ en la ecuación de la viga, obtenemos la ecuación diferencial gobernante homogénea para $x \neq 0$:
$$EI\frac{d^4y}{dx^4}-k_2\frac{d^2y}{dx^2}+k_1y=0$$

### 2. Ecuación Característica y sus Raíces

Para resolver esta ecuación diferencial lineal de coeficientes constantes, proponemos una solución de la forma $y(x) = e^{rx}$. Sustituyendo esto en la ecuación gobernante, llegamos a la ecuación característica:
$$EIr^4-k_2r^2+k_1=0$$

Esta es una ecuación bicuadrática. Resolviendo para $r^2$ mediante la fórmula general:
$$r^2=\frac{k_2\pm\sqrt{k_2^2-4EIk_1}}{2EI}$$

En la gran mayoría de los casos físicos reales para suelos, el acoplamiento a cortante es moderado comparado con la rigidez a flexión y el módulo de Winkler, por lo que se cumple que $4EIk_1 > k_2^2$. Esto significa que el discriminante es negativo y las raíces de $r^2$ son complejas conjugadas:
$$r^2=\frac{k_2}{2EI}\pm i\sqrt{\frac{k_1}{EI}-\left(\frac{k_2}{2EI}\right)^2}$$

Extrayendo la raíz cuadrada de $r^2$, obtenemos cuatro raíces complejas para $r$, que podemos expresar en la forma $r = \pm(u \pm iv)$, donde $u$ y $v$ son valores reales positivos dados por:
$$u=\sqrt{\frac{1}{2}\sqrt{\frac{k_1}{EI}}+\frac{k_2}{4EI}}$$
$$v=\sqrt{\frac{1}{2}\sqrt{\frac{k_1}{EI}}-\frac{k_2}{4EI}}$$

### 3. Solución General y Condiciones de Borde

Como la viga es de longitud infinita, evaluaremos el dominio para $x \ge 0$ (aprovechando que el problema es perfectamente simétrico). Para que la deflexión no tienda a infinito cuando $x \to \infty$, debemos descartar las raíces con parte real positiva. Por lo tanto, nos quedamos con las raíces $-u \pm iv$.

La solución general para $x \ge 0$ toma la forma:
$$y(x)=e^{-ux}(C_1\cos vx+C_2\sin vx)$$

Para hallar las constantes $C_1$ y $C_2$, utilizamos las condiciones de borde en el punto de aplicación de la carga ($x = 0$):

**Condición A: Simetría (Pendiente nula)**
Debido a la simetría de la carga, la pendiente bajo la carga debe ser cero:
$$y'(0)=0$$
Derivando la solución y evaluando en $x=0$, obtenemos $-uC_1 + vC_2 = 0$, lo que nos da:
$$C_2=C_1\frac{u}{v}$$

**Condición B: Equilibrio de Cortante**
La fuerza cortante interna total $V_{eff}$ en la viga sobre una fundación Pasternak se define como:
$$V_{eff}(x)=-EIy'''(x)+k_2y'(x)$$
Un corte transversal infinitesimal en $x=0$ debe resistir la mitad de la carga descendente $P$ por equilibrio en la cara derecha ($x=0^+$):
$$V_{eff}(0^+)=-\frac{P}{2}$$
Dado que ya sabemos que $y'(0) = 0$, el término de la capa de cortante se anula en ese punto exacto, simplificando la condición a:
$$-EIy'''(0^+)=-\frac{P}{2} \implies y'''(0^+)=\frac{P}{2EI}$$

Calculando la tercera derivada de $y(x)$ con la relación de $C_2$ ya incluida y evaluando en cero, se obtiene la identidad $y'''(0) = 2C_1u(u^2 + v^2)$.
Sabiendo por la definición de nuestras raíces que $u^2 + v^2 = \sqrt{k_1/EI}$, podemos igualar y despejar $C_1$:
$$2C_1u\sqrt{\frac{k_1}{EI}}=\frac{P}{2EI} \implies C_1=\frac{P}{4u\sqrt{EIk_1}}$$

### 4. Solución Analítica Completa

Sustituyendo $C_1$ y $C_2$ de vuelta en nuestra ecuación y generalizándola para todo el dominio utilizando el valor absoluto $|x|$ (por simetría), la solución analítica completa para la deflexión de la viga es:

$$y(x)=\frac{P}{4u\sqrt{EIk_1}}e^{-u|x|}\left(\cos(v|x|)+\frac{u}{v}\sin(v|x|)\right)$$

*Nota: La deflexión máxima ocurre bajo la carga (en $x=0$) y tiene un valor de $y_{max} = \frac{P}{4u\sqrt{EIk_1}}$. Si hicieras $k_2 = 0$, notarás que $u$ y $v$ se vuelven iguales, y esta solución colapsa exactamente en la solución clásica de una viga sobre fundación elástica de Winkler pura.*

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

- **EDO Pasternak correcta:** $EI y'''' - k_2 y'' + k_1 y = 0$. El término $-k_2 y''$ es la firma de Pasternak.
- **Ecuación característica bicuadrática correcta:** $EI r^4 - k_2 r^2 + k_1 = 0$.
- **Discriminante:** identifica correctamente el caso $4EI k_1 > k_2^2$ (raíces complejas) y descarta los casos $\le$.
- **Raíces:** $r = \pm(u \pm iv)$ con $u, v$ correctas:
  - $u = \sqrt{(1/2)\sqrt{k_1/EI} + k_2/(4EI)}$
  - $v = \sqrt{(1/2)\sqrt{k_1/EI} - k_2/(4EI)}$
- **Cortante efectivo Pasternak:** $V_{eff} = -EI y''' + k_2 y'$ — **correcto y específico de Pasternak**, este término es no-trivial y diferencia esta sesión de un mero "Winkler con $k_1$".
- Adoptó **convención $y$ positivo abajo implícita** (no la declaró explícitamente, pero las relaciones $V = -EI y'''$ y la solución final positiva confirman esta lectura).
- **Verificación del límite Winkler ($k_2 \to 0$):** mencionada explícitamente. Bajo cálculo independiente, la solución se reduce correctamente a la de Winkler con factor $P\beta/(2k_1)$, validando la coherencia algebraica.
- **Resultado sorprendente:** Gemini resolvió Pasternak limpiamente en la condición *minimal*, contrario a la hipótesis inicial. Esto sugiere que el modelo conoce bien Pasternak por su corpus de entrenamiento. La diferencia con el manuscrito es de convención, no de capacidad analítica.
