# Reference Analytical Solutions

This file documents the validated reference solutions used to score metrics **M3** (boundary conditions) and **M4** (final solution correctness) in the ablation study. Each reference is derived from established literature and verified by independent recomputation. They serve as the *ground truth* against which model outputs are compared.

All cases share the parameter:

$$
\beta = \sqrt[4]{\frac{k}{4\,EI}}
$$

The sign convention is the one stated in `prompts.md` (axis $y$ positive upward, downward load enters the equilibrium equation as a negative force).

---

## C1 — Infinite Winkler beam, centered point load

Reference: Hetényi (1946) §17, Eq. (8); Timoshenko (1956) §1.2.

**Boundary conditions:**

1. $y(x) \to 0$ as $|x| \to \infty$.
2. Symmetry: $y'(0) = 0$.
3. Shear jump at the origin: $V(0^+) - V(0^-) = -P$, equivalently $V(0^+) = -P/2$.

**Final solution (for $x \ge 0$, extended by symmetry):**

$$
y(x) = -\frac{P\,\beta}{2k}\, e^{-\beta|x|}\bigl[\cos(\beta|x|) + \sin(\beta|x|)\bigr]
$$

$$
M(x) = \frac{P}{4\beta}\, e^{-\beta|x|}\bigl[\cos(\beta|x|) - \sin(\beta|x|)\bigr]
$$

$$
V(x) = -\frac{P}{2}\,\mathrm{sgn}(x)\, e^{-\beta|x|}\cos(\beta|x|)
$$

**Diagnostic checks** (used during M4 scoring):
- $y(0) = -\dfrac{P\beta}{2k}$
- $M(0) = \dfrac{P}{4\beta}$
- $V(0^+) - V(0^-) = -P$

---

## C2 — Infinite Winkler beam, off-center point load at $x = a$

Reference: obtained from C1 by translation invariance of the homogeneous problem.

**Boundary conditions:**

1. $y(x) \to 0$ as $|x| \to \infty$.
2. Symmetry of the response about $x = a$: $y'(a) = 0$.
3. Shear jump at $x = a$: $V(a^+) = -P/2$.

**Final solution:**

$$
y(x) = -\frac{P\,\beta}{2k}\, e^{-\beta|x-a|}\bigl[\cos(\beta|x-a|) + \sin(\beta|x-a|)\bigr]
$$

$$
M(x) = \frac{P}{4\beta}\, e^{-\beta|x-a|}\bigl[\cos(\beta|x-a|) - \sin(\beta|x-a|)\bigr]
$$

$$
V(x) = -\frac{P}{2}\,\mathrm{sgn}(x-a)\, e^{-\beta|x-a|}\cos(\beta|x-a|)
$$

**Diagnostic check:** the response must depend on $|x-a|$, **not** on $|x|+a$ or any other spurious combination. A correct derivation either (a) uses the substitution $\xi = x - a$ and reduces the problem to C1, or (b) re-applies all boundary conditions in the original coordinate system without forgetting that the symmetry is about $x = a$.

---

## C3 — Finite Winkler beam, free–free, length $L$, point load at $L/2$

Reference: Hetényi (1946) §19 (medium-length beam with free ends, central load); equivalent treatment in Timoshenko (1956) §3.

**Approach:** by symmetry the problem can be solved on the half-domain $[0, L/2]$ with two boundary conditions at the free end $x = 0$ and two symmetry/load conditions at $x = L/2$.

The general solution on the half-domain is:

$$
y(x) = e^{\beta x}(A \cos\beta x + B \sin\beta x) + e^{-\beta x}(C \cos\beta x + D \sin\beta x)
$$

**Boundary conditions** (4 equations for $A, B, C, D$):

1. $M(0) = EI\,y''(0) = 0$ — moment vanishes at the free end.
2. $V(0) = EI\,y'''(0) = 0$ — shear vanishes at the free end.
3. Symmetry at center: $y'(L/2) = 0$.
4. Shear jump at center: $V(L/2^-) = -P/2$ (from the right half by symmetry, equivalently $EI\,y'''(L/2) = -P/2$).

**Closed-form result:** using the Hetényi auxiliary functions
$F_1(\xi) = \cosh\xi\cos\xi$,
$F_2(\xi) = \tfrac{1}{2}(\cosh\xi\sin\xi + \sinh\xi\cos\xi)$,
$F_3(\xi) = \tfrac{1}{2}\sinh\xi\sin\xi$,
$F_4(\xi) = \tfrac{1}{4}(\cosh\xi\sin\xi - \sinh\xi\cos\xi)$,

the central deflection is

$$
y\!\left(\tfrac{L}{2}\right) = -\frac{P\beta}{2k} \cdot \frac{2 + \cos\beta L + \cosh\beta L}{\sin\beta L + \sinh\beta L}
$$

(see Hetényi 1946, Table I). The full $y(x)$ involves all four constants $A, B, C, D$ obtained from the linear system above and is too lengthy to reproduce in full, but **any correct derivation must yield this central deflection within algebraic equivalence**.

**Diagnostic checks for M4:**
- The four constants must be **non-zero in general** — solutions that set $A = B = 0$ (mistaking the finite beam for an infinite one) score **0**.
- The central deflection formula above must be reproducible from the model's expressions.

---

## C4 — Infinite beam on Pasternak foundation, centered point load

References: Pasternak (1954); Selvadurai (1979) §2.5; Vlasov & Leont'ev (1966).

**Governing ODE:**

$$
EI\,\frac{d^4 y}{dx^4} - k_2\,\frac{d^2 y}{dx^2} + k_1\,y = -P\,\delta(x)
$$

**Characteristic equation** (for the homogeneous problem):

$$
EI\,r^4 - k_2\,r^2 + k_1 = 0 \quad \Longrightarrow \quad r^2 = \frac{k_2 \pm \sqrt{k_2^2 - 4\,EI\,k_1}}{2\,EI}
$$

The qualitative form of the solution depends on the discriminant $\Delta = k_2^2 - 4\,EI\,k_1$:

- **Case A (lightly damped, $\Delta < 0$):** complex conjugate roots of the form $r = \pm \alpha \pm i\gamma$, with

  $$
  \alpha = \sqrt{\tfrac{1}{2}\bigl(\sqrt{k_1/EI} + k_2/(2EI)\bigr)},\qquad
  \gamma = \sqrt{\tfrac{1}{2}\bigl(\sqrt{k_1/EI} - k_2/(2EI)\bigr)}
  $$

  Solution decays oscillatorily, analogous to Winkler.

- **Case B (heavily damped, $\Delta > 0$):** four real roots $\pm r_1, \pm r_2$. Solution is a sum of pure exponentials with no oscillation.

- **Case C (critical, $\Delta = 0$):** repeated roots; solution involves polynomial-times-exponential terms.

**Reference solution for Case A** (the most commonly encountered in the literature):

$$
y(x) = -\frac{P}{4\,\alpha\,\sqrt{EI\,k_1}}\, e^{-\alpha|x|}\!\left[\cos(\gamma|x|) + \frac{\alpha}{\gamma}\sin(\gamma|x|)\right]
$$

Equivalently, factoring $1/\gamma$ inside the bracket:

$$
y(x) = -\frac{P}{4\,\alpha\,\gamma\,\sqrt{EI\,k_1}}\, e^{-\alpha|x|}\!\left[\gamma\cos(\gamma|x|) + \alpha\sin(\gamma|x|)\right]
$$

**Verification** (used during M4 scoring):
- $y(0) = -\dfrac{P}{4\alpha\sqrt{EI\,k_1}}$.
- Using $\alpha^2+\gamma^2 = \sqrt{k_1/EI}$, this is also $y(0) = -\dfrac{P}{4\alpha\,EI(\alpha^2+\gamma^2)}$.
- Limit $k_2\to 0$: $\alpha = \gamma = \beta = \sqrt[4]{k_1/(4EI)}$, giving $y(0) = -\dfrac{P}{8EI\beta^3} = -\dfrac{P\beta}{2k_1}$ — the Winkler reference of C1, as required.

**Derivation sketch:** with $y(x) = e^{-\alpha x}(A\cos\gamma x + B\sin\gamma x)$ for $x \ge 0$, the symmetry condition $y'(0)=0$ gives $B = (\alpha/\gamma)A$, and the third-derivative evaluation produces $y'''(0) = 2\alpha A(\alpha^2+\gamma^2)$. Imposing $-EI\,y'''(0^+) = -P/2$ (with $y'(0)=0$ canceling the Pasternak shear-layer term) yields $A = -P/[4\alpha\,EI(\alpha^2+\gamma^2)] = -P/(4\alpha\sqrt{EI\,k_1})$.

(Equivalent forms exist; cf. Selvadurai 1979.)

**Diagnostic checks for M4:**
- The governing ODE **must** contain the term $-k_2\,y''$. A common failure mode is to ignore this term and "hallucinate" a Winkler-type ODE with a modified $k$. This yields M4 = 0 immediately.
- The discriminant analysis (or equivalent acknowledgment that the roots depend on $k_2^2 - 4\,EI\,k_1$) must appear in the derivation.
- Setting $k_2 = 0$ in the final solution must reduce it back to the Winkler solution of C1. Models that produce expressions which fail this limit score M4 = 0.

---

## Sources

- Hetényi, M. (1946). *Beams on Elastic Foundation*. University of Michigan Press.
- Timoshenko, S. P. (1956). *Strength of Materials, Part II: Advanced Theory and Problems*. Van Nostrand.
- Pasternak, P. L. (1954). *On a new method of analysis of an elastic foundation by means of two foundation constants* [in Russian]. Gosudarstvennoe Izdatelstvo Literaturi po Stroitelstvu i Arkhitekture, Moscow.
- Vlasov, V. Z., & Leont'ev, N. N. (1966). *Beams, Plates and Shells on Elastic Foundations*. Israel Program for Scientific Translations.
- Selvadurai, A. P. S. (1979). *Elastic Analysis of Soil-Foundation Interaction*. Elsevier.
