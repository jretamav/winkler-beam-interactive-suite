# Rúbrica de evaluación

Esta rúbrica se aplica de forma uniforme a las 16 sesiones del experimento. Cada sesión recibe cinco puntuaciones independientes (M1 a M5).

## M1 — Coherencia de convención de signos *(binaria, 0 ó 1)*

**Asigna 1 si:**
- A lo largo de toda la derivación, la convención de signos adoptada (o asumida) al inicio se preserva sin inversiones implícitas.
- El signo final de las funciones $y(x)$, $M(x)$ y $V(x)$ coincide con el comportamiento físico esperado del problema (deflexión negativa bajo carga descendente con eje $y$ positivo hacia arriba; concavidad hacia arriba bajo el punto de carga; etc.).

**Asigna 0 si:**
- En algún paso intermedio, una derivada se calcula bajo una asunción de signos y se utiliza luego bajo otra asunción contradictoria.
- El signo final de cualquiera de las tres funciones es opuesto al esperado físicamente.
- El modelo cambia el sentido del eje $y$ a mitad de la derivación sin justificación.

## M2 — Coherencia dimensional *(binaria, 0 ó 1)*

Inspecciona tres ecuaciones representativas de la derivación:

1. La ecuación diferencial gobernante.
2. La solución general homogénea.
3. La expresión final de $y(x)$.

**Asigna 1 si:** todos los términos aditivos en cada una de esas tres ecuaciones tienen unidades consistentes.

**Asigna 0 si:** algún término rompe la homogeneidad dimensional, por ejemplo:
- Sumar un término con unidades de $[L]$ con uno de $[L^2]$.
- Olvidar dividir entre $EI$ donde corresponde, dejando un término con dimensiones inconsistentes.
- Confundir la dimensión de $k$ (constante de balasto $\times$ ancho) con la del módulo de balasto puro $k_0$.

## M3 — Aplicación correcta de condiciones de frontera *(binaria, 0 ó 1)*

**Asigna 1 si:**
- El conjunto de condiciones de frontera identificadas corresponde correctamente al problema planteado:
  - **C1, C2, C4:** finitud en el infinito ($y \to 0$ cuando $|x| \to \infty$); simetría o salto de cortante en el punto de carga.
  - **C3:** $M(0) = M(L) = 0$ y $V(0) = V(L) = 0$ (cuatro CB en una viga finita libre-libre).
- Cada CB se aplica algebraicamente al término o constante correcto y produce un sistema lineal coherente.

**Asigna 0 si:**
- Se inventa una CB inexistente (por ejemplo, asumir $y(0) = 0$ en C1).
- Se omite una CB necesaria.
- Se aplica una CB a la ecuación o variable equivocada.
- El sistema lineal resultante es inconsistente o degenerado por error.

## M4 — Correctitud de la solución analítica final *(binaria, 0 ó 1)*

Compara la expresión final de $y(x)$ con la solución de referencia documentada en `reference_solutions.md`.

**Asigna 1 si:** la expresión final es matemáticamente equivalente a la referencia (las diferencias son únicamente de forma algebraica: factorización, identidades trigonométricas, etc.).

**Asigna 0 si:**
- La expresión final difiere por un factor constante incorrecto.
- Faltan o sobran términos.
- El argumento de las funciones trigonométricas o exponenciales es incorrecto.
- La estructura funcional difiere (por ejemplo, falta el envolvente exponencial $e^{-\beta|x|}$).

## M5 — Errores algebraicos contables *(entero, conteo)*

Cuenta cada error algebraico **discreto y verificable** detectado en la derivación. Una misma ocurrencia se cuenta una sola vez. Categorías a considerar:

- **Signo:** un signo incorrecto en una derivada, integral o sustitución.
- **Término omitido:** un término que debería estar presente y no aparece.
- **Término espurio:** un término que aparece sin justificación matemática.
- **Identidad mal aplicada:** uso incorrecto de una identidad trigonométrica, una expansión en serie, o una propiedad de exponentes.
- **Sustitución:** sustitución de una variable o valor incorrecto.
- **Álgebra elemental:** error aritmético en la simplificación.

Reporta el conteo total como entero no negativo (0, 1, 2, …).

**Nota:** errores que se propagan derivados de un único error inicial se cuentan **solo una vez** (el original). Los errores subsecuentes algebraicamente consistentes con el original no se penalizan adicionalmente, para no inflar artificialmente el conteo.

---

## Cómo registrar los resultados

Para cada uno de los 16 archivos de sesión en `sessions/`, abre la plantilla `log_template.md`, lee la salida del modelo, aplica la rúbrica anterior y registra los cinco valores. Acumula los 16 resultados en un archivo `results.csv` con la siguiente estructura:

```csv
case,model,condition,M1,M2,M3,M4,M5
C1,gemini,minimal,1,1,0,0,3
C1,gemini,scaffolded,1,1,1,1,0
...
```
