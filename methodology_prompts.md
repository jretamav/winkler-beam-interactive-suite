# Methodology prompts (Stages 1, 2 and 4)

This file archives, verbatim, the three canonical prompts that materialize the Human–AI workflow described in the manuscript *"Generative Artificial Intelligence as a Computational and Pedagogical Assistant: Analytical Derivation and Interactive Simulation of the Winkler Model"* (Retama Velasco, 2026).

These prompts are distinct from the eight ablation prompts archived in [`ablation/prompts.md`](ablation/prompts.md). The ablation prompts test the scaffolding hypothesis on four canonical cases; the prompts below define the workflow itself across Stages 1 (parametrization and sign convention), 2 (algebraic execution and LaTeX composition) and 4 (Python ecosystem development). Stage 3 (human structural validation) is, by design, not an LLM prompt and therefore not archived here.

The model used for the workflow execution was **Gemini 3.1 Pro** (Google), default web interface, single fresh chat per stage.

---

## Stage 1 — Parametrization and Sign Convention

```
Actúa como un experto en ingeniería estructural y mecánica de sólidos.
Vamos a realizar la derivación analítica de la ecuación diferencial
gobernante para el Modelo de Winkler. Debes adoptar y respetar
estrictamente las siguientes convenciones físicas:

1. Sistema Global: El eje x es positivo hacia la derecha y el eje y es
positivo hacia arriba. Giro antihorario es positivo.

2. Convención por Deformación: Para un elemento diferencial de longitud
"dx", en la cara izquierda el cortante apunta hacia arriba y el
momento flexionante en sentido horario; en la cara de la derecha, el
cortante apunta hacia abajo y el momento flexionante en el sentido
antihorario. La carga q(x) actúa hacia abajo.

3. Reacciones: Al inicio de la solución de los problemas, las
reacciones incógnitas deben considerarse actuando en su sentido
positivo.

4. Notación Matemática: Utiliza yuxtaposición para variables en
multiplicación (ej. qb, Pa, M0L). Para fracciones en ecuaciones
centradas, utiliza formato apilado. Para distancias, usa literales
simples (a, b, c) para segmentos de viga y reserva L mayúscula para
el claro total (L = a+b).
```

---

## Stage 2 — Analytical Derivation and LaTeX Composition

```
Utilizando las convenciones de signos y el sistema de coordenadas
establecidos previamente, realiza lo siguiente:

1. Planteamiento: Escribe las ecuaciones de equilibrio de fuerzas (sumatoria
en y) y momentos para el elemento diferencial de longitud "dx".

2. Expansión: Aplica una expansión en series de Taylor para las funciones
de cortante V(x+dx) y momento M(x+dx), despreciando los términos de
orden superior a dx.

3. Sustitución: Integra la relación de la base elástica p(x) = k y(x) en
la ecuación de equilibrio de fuerzas. Considera que la carga q(x)
es descendente.

4. Diferenciación: Combina las ecuaciones para obtener la ecuación
diferencial de cuarto orden que gobierna la deflexión y(x) en
función de EI y k.

5. Salida: Genera todo el desarrollo anterior en código LaTeX, utilizando
la notación de yuxtaposición solicitada y asegurando que las
ecuaciones estén centradas y numeradas.
```

---

## Stage 4 — Python Programming and Interactivity

```
Actúa como un programador experto en Python y computación científica.
Genera un script interactivo utilizando NumPy y Matplotlib para
visualizar el comportamiento de la viga de Winkler. Sigue estos
lineamientos técnicos:

1. Vectorización: Utiliza arreglos de NumPy para evaluar las funciones
de deflexión, momento y cortante en un dominio x. Evita el uso de
bucles "for" para los cálculos de los arreglos.

2. Implementación: Programa las funciones analíticas derivadas
previamente para [Caso de Carga: Puntual / Momento / Distribuida],
utilizando las funciones auxiliares A(x), B(x), C(x) y D(x) de
Hetenyi.

3. Interactividad: Incorpora el módulo matplotlib.widgets para crear
controles deslizables (sliders) que permitan modificar en tiempo
real los siguientes parámetros:
- Rigidez a la flexión (EI).
- Constante del lecho elástico (k).
- Magnitud y posición de la carga.

4. Visualización: Crea tres subgráficas alineadas verticalmente para
mostrar: a) Deflexión y(x), b) Momento flexionante M(x) y
c) Fuerza cortante V(x). Asegura que los ejes se actualicen
dinámicamente mediante callbacks.

5. Inspección: Agrega un cuadro de texto (TextBox) para que el usuario
pueda ingresar una coordenada "x" específica y obtener los valores
numéricos exactos en la consola o en el gráfico.
```

---

## Notes

- Stage 3 (human validation of structural behavior) is by design not an LLM prompt; it is the human auditor's responsibility, exercised against the manuscript's results.
- The Stage 4 prompt was issued three times, once for each load case (point load, concentrated moment, uniformly distributed load), with the bracketed placeholder replaced accordingly. The resulting scripts are `puntual.py`, `momento.py` and `distribuida.py` of this repository.
- The manuscript's main text describes the methodology in Section 3; the empirical validation of the Stage 1 scaffolding is reported in Section 9 of the manuscript and archived in [`ablation/`](ablation/).
