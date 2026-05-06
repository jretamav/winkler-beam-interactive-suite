# Winkler Beam Interactive Suite

An open-source educational toolkit for the analytical study of beams on elastic foundations (Winkler model) through real-time interactive simulation.

This repository accompanies the manuscript *"Generative Artificial Intelligence as a Computational and Pedagogical Assistant: Analytical Derivation and Interactive Simulation of the Winkler Model"* (Retama Velasco, 2026), submitted to *Computer Applications in Engineering Education*.

## Overview

The suite provides three interactive Python scripts that evaluate the **exact analytical solutions** of an infinite beam on a Winkler elastic foundation under three loading scenarios:

| Script | Loading scenario |
|---|---|
| `puntual.py` | Concentrated point load $P$ |
| `momento.py` | Concentrated moment $M_0$ |
| `distribuida.py` | Uniformly distributed load $q$ over a finite length $a$ |

Each script renders the deflection $y(x)$, bending moment $M(x)$ and shear force $V(x)$ in three vertically aligned subplots, and exposes interactive sliders for the flexural rigidity $EI$, the foundation modulus $k$ and the load magnitude. A *TextBox* allows pointwise inspection of the analytical solution at any user-specified coordinate.

## Pedagogical motivation

The classical Winkler model leads to a fourth-order ODE whose closed-form solution involves complex roots and damped trigonometric envelopes. Traditional teaching delegates a disproportionate amount of class time to algebraic manipulation. This suite implements the **exact** analytical solutions in vectorized NumPy form, so students can:

- Validate the qualitative behaviour predicted by theory (deflection bowl, moment concavity, shear discontinuities at point loads).
- Explore the influence of the characteristic parameter $\beta = \sqrt[4]{k/(4EI)}$ on the zone of influence of the load.
- Perform parametric studies in real time without manual tabulation.

## Requirements

- Python 3.9 or newer
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run any of the three scripts directly:

```bash
python puntual.py
python momento.py
python distribuida.py
```

A Matplotlib window opens with the three diagrams, the parameter sliders and the inspection TextBox. Modify any slider to update the curves in real time.

## Validation

The default parameters of each script reproduce the worked examples reported in the accompanying manuscript:

| Parameter | Value |
|---|---|
| Modulus of elasticity (steel) | $E = 200 \times 10^9$ N/m² |
| Section moment of inertia | $I = 1.25 \times 10^{-9}$ m⁴ |
| Foundation linear stiffness | $k = 1000$ N/m² |
| Resulting flexural rigidity | $EI = 250$ N·m² |
| Resulting characteristic parameter | $\beta = 1$ m⁻¹ |

For the point-load case with $P = 1000$ N, the analytical maximum deflection at the origin is $y(0) = -0.5$ m and the maximum bending moment is $M(0) = 250$ N·m, in exact agreement with the values produced by `puntual.py`.

## Sign convention

All scripts follow the sign convention adopted in the manuscript:

- $x$ positive to the right, $y$ positive upward; counter-clockwise moments positive.
- On a differential element, the left face carries an upward shear and a clockwise bending moment; the right face carries a downward shear and a counter-clockwise bending moment.
- Distributed external load $q(x)$ acts downward; foundation reaction acts upward.

## Citation

If you use this software in academic work, please cite both the software and the accompanying article. A `CITATION.cff` file is provided so that GitHub generates a "Cite this repository" entry automatically.

## License

This project is released under the MIT License — see the `LICENSE` file.

## Author

**Jaime Retama Velasco**
Civil Engineering Department, Facultad de Estudios Superiores Aragón
Universidad Nacional Autónoma de México (UNAM)
ORCID: [0000-0001-6451-5597](https://orcid.org/0000-0001-6451-5597)

## Acknowledgements

This work was supported by UNAM through the projects PAPIIT IT101926 and PAPIME PE101626, and by the PRIDE program (Level C). The analytical derivations and the initial code scaffolding were generated under human supervision with the assistance of the Gemini generative AI model, following the methodological framework documented in the accompanying manuscript.
