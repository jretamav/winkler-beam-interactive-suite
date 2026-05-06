# Cross-Model Ablation Study of the Phenomenological Scaffolding

This folder contains the protocol, prompts, evaluation rubric and raw model outputs of the ablation study designed to validate Research Question 1 (RQ1) of the manuscript:

> *Can Generative AI, when constrained by a strict phenomenological scaffolding, execute the analytical derivation of the Winkler model preserving physical and mathematical rigor and eliminating the traditional algebraic burden?*

## Experimental design

The study evaluates whether the **phenomenological scaffolding** documented in Appendix A of the manuscript actually affects the quality of the analytical derivation produced by a Large Language Model — and whether this effect generalizes across model providers.

### Independent variables

| Factor | Levels |
|---|---|
| Model | Gemini 3 Pro (Google) · Claude Opus 4.7 (Anthropic) |
| Condition | Without scaffolding · With scaffolding |
| Test case | C1 · C2 · C3 · C4 |

### Test cases

| ID | Problem | Rationale |
|---|---|---|
| **C1** | Infinite Winkler beam, centered point load | Canonical baseline (in corpus) |
| **C2** | Infinite Winkler beam, off-center point load at $x = a$ | Requires moving origin (mild generalization) |
| **C3** | Finite Winkler beam, length $L$, free–free, point load at $L/2$ | Four non-trivial boundary conditions |
| **C4** | Infinite Pasternak beam, centered point load | Two-parameter foundation (out of main corpus) |

### Total executions

4 cases × 2 models × 2 conditions = **16 sessions**, each in a fresh chat to prevent context contamination.

### Dependent variables

Five metrics applied to each output:

| Metric | Type | Definition |
|---|---|---|
| **M1** | binary | Sign convention preserved throughout the derivation |
| **M2** | binary | Dimensional consistency in all equations |
| **M3** | binary | Correct identification and application of boundary conditions |
| **M4** | binary | Final analytical solution mathematically equivalent to the reference |
| **M5** | integer | Number of discrete algebraic errors in the derivation |

The full operational rubric is provided in `rubric.md`.

## Protocol

For each of the 16 cells of the experimental design, follow exactly these steps:

1. Open a **new, clean chat session** in the corresponding model's interface (gemini.google.com or claude.ai). Do not reuse a session.
2. Open `prompts.md` and locate the prompt corresponding to the case and condition under evaluation.
3. Copy the **entire prompt** verbatim and paste it as the first message of the session.
4. Wait for the model to complete its full response.
5. Copy the **complete output**, without truncation, and save it together with execution metadata using the template `log_template.md`. Save each session as a separate file inside `sessions/` named:

   ```
   sessions/{model}_{case}_{condition}.md
   ```

   Examples: `sessions/gemini_C1_minimal.md`, `sessions/claude_C3_scaffolded.md`.

6. Do not edit, summarize or correct the model output — verbatim only.

## Evaluation phase

Once the 16 session files are populated, the evaluation is performed by applying `rubric.md` independently to each file and recording the scores in `results.csv` (generated in the analysis phase).

## Reference solutions

The reference analytical solutions used to score M3 and M4 are documented in `reference_solutions.md` and are independently validated against Hetényi (1946) for cases C1, C2 and C3, and against Selvadurai (1979) for case C4.

## Reproducibility

Every artifact in this folder — prompts, rubric, raw outputs, evaluation worksheets — is version-controlled and archived together with the software in the Zenodo release accompanying this study.
