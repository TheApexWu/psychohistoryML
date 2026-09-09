# PsychohistoryML

**Computational history of political instability — held to the standard that retracts papers.**

This project asks what ten thousand years of historical data can, and cannot, tell us about why polities become unstable. It is deliberately *not* a validation of cliodynamics or structural-demographic theory. It is an attempt to do quantitative history honestly: reproduce the field's central results, test them the way its own critics do, and apply the same test to this project's own findings — including the ones it would rather keep.

The organizing result is an asymmetry. When you subject two of this project's headline findings to the missing-data discipline that retracted a *Nature* paper, **one survives and one does not** — and the difference tells you which quantitative history is real and which is an artifact.

## The two findings

**Violence begets violence — and it holds up.** In the CrisisDB power-transition record, a violent transition of power roughly triples the odds the next one is violent (60% vs 22%). Re-run with every *inferred* code stripped out, keeping only directly-observed events, and the effect barely moves (gap 37.7% → 36.1%). The signal rests on observed data, not on how the blanks were filled. → `crisisdb/13`, `crisisdb/15`

**"Complexity predicts collapse" — and it does not.** The original model here reported that social complexity predicts polity duration at AUC ≈ 0.66. Rebuilt against the live Seshat API (600 of 864 polities merge; 170 have complete complexity data), that number turns out to be largely a **data-coverage artifact**: on observed complexity data the model is anti-predictive (AUC 0.40), while *missingness alone* — how many variables a polity has documented — scores 0.59, because better-documented polities are systematically shorter-lived. Median imputation launders documentation completeness into a fake complexity effect. → `notebooks/17`

The lesson is the one Beheim et al. used to retract Whitehouse et al.'s 2019 *Nature* paper — that the treatment of missing data can determine the conclusion. This project reproduces that retraction (`notebooks/12`) and then turns the same lens on itself.

## The notebooks

Read in order; each is executed end-to-end, and every number is computed in-cell.

| # | Notebook | What it shows |
|---|---|---|
| 12 | `notebooks/12_moralizing_gods_reproduction` | Reproduces the retracted *Nature* 2019 "moralizing gods" result: a 42-point swing from a missing-data coding choice. |
| 13 | `crisisdb/13_missing_data_self_test` | Runs that same test on our own violence-contagion Markov. It survives. |
| 14 | `crisisdb/14_label_validation` | Cross-checks our violence labels against an independent coder. Honest null (under-powered, n=47). |
| 15 | `crisisdb/15_channels_of_instability` | Decomposes contagion by type; a robustness section corrects an over-exciting first draft — external shock is the robustly most self-reinforcing channel. |
| 16 | `notebooks/16_limits_at_scale` | On 864 polities, shows "collapse" is an incoherent target: part geography, part noise. |
| 17 | `notebooks/17_coverage_artifact` | The complexity→collapse result is a coverage/imputation artifact. The capstone. |

Earlier exploratory notebooks (`notebooks/01–11`, `crisisdb/01–04`) are the original analysis this revamp reframes; they are kept for provenance.

## What this project is careful *not* to claim

- It does not predict the future, or any specific society's collapse.
- It does not validate structural-demographic theory. Where it engages Turchin's claims (e.g. elite overproduction), it tests them and reports where they hold and where they don't.
- Its strongest positive result (violence contagion) is descriptive, not causal.
- Every dataset here is expert-coded historical data with real subjectivity and coverage gaps (Slingerland et al. 2020, *Coding culture*); the analyses are built to expose those limits, not paper over them.

## Data & reproduction

All datasets are public and cited inline; large files are gitignored and re-downloadable from the URLs in [`data_external/README.md`](data_external/README.md):

- **Seshat Global History Databank** — social-complexity, religion, and the moralizing-gods data (Equinox release + live API, ~864 polities).
- **CrisisDB** — power transitions, crisis consequences (Navigating Polycrisis), US political violence.
- **Beheim et al. 2021 replication archive** — the moralizing-gods critique, reproduced in `notebooks/12`.

```bash
pip install pandas numpy scikit-learn statsmodels matplotlib
# then run any notebook top to bottom; data URLs are in data_external/README.md
```

## Key references

- Whitehouse, François, Savage, Turchin et al. 2019. *Complex societies precede moralizing gods.* Nature 568:226 (**retracted 2021**).
- Beheim et al. 2021. *Treatment of missing data determined conclusions regarding moralizing gods.* Nature 595:E29.
- Turchin, Currie, Whitehouse et al. 2018. *A single dimension of complexity.* PNAS 115(2):E144.
- Turchin 2016. *Ages of Discord: A Structural-Demographic Analysis of American History.*
- Hoyer, Reddish, François, Turchin et al. 2024. *All Crises are Unhappy in Their Own Way.* Social Science History.

*A well-defined question — was a transition violent — supports real findings. A vague one — did a society collapse — supports artifacts. This project is the honest math for both.*
