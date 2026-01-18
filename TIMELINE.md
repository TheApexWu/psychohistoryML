# PsychohistoryML Project Timeline

Research evolution from initial exploration to CrisisDB integration.

---

## Phase 1: Foundation (Oct 2025)

### Oct 21-22
- Initial commit, README scaffold
- **01_social_complexity_exploration.ipynb**: First pass at Seshat 2017 dataset
  - 28,175 rows → 378 polities with hierarchical complexity
  - Core variables: settlement, admin, religious, military levels

### Oct 27
- **02_social_complexity_modeling.ipynb**: PCA + regression
  - PC1 captures 76% variance ("general complexity")
  - **Key finding**: r = -0.39, p < 0.001 (complexity → shorter duration)
  - R² = 0.149 (weak predictive power for exact duration)
  - Diagnostics: non-normal residuals, heteroscedasticity

---

## Phase 2: Classification Pivot (Nov 2025)

### Nov 12-14
- **03_instability_prediction.ipynb**: Binary classification
  - Target: duration < 33rd percentile (~146 years)
  - Logistic, Random Forest, XGBoost tested
  - **Best**: XGBoost AUC = 0.85
  - **Key insight**: PC1² most important (non-linearity matters)
  - Classification >> regression for this problem

### Nov 14
- Research report folder created (now deprecated)
- README updates with findings

---

## Phase 3: Equinox Migration (Nov 2025)

### Nov 16-18
- Switched from 2017 dataset to **Equinox 2022** (richer variables)
- **04_equinox_replication.ipynb**: Replicate findings on new data
  - 444 polities in Equinox
  - Era clustering discovered (geographic < temporal patterns)

### Nov 26-28
- **05_warfare_integration.ipynb**: Added military tech features
  - AUC: 0.505 → 0.601
- **06_religion_integration.ipynb**: Added religion features
  - AUC: 0.601 → 0.606
- First "three-mechanism" framework (complexity + warfare + religion)

---

## Phase 4: Production Model (Dec 2025)

### Dec 3
- **07_production_deployment.ipynb**: Final model pipeline
  - CV AUC = 0.66 ± 0.06
  - Feature importance: Religion 27%, Complexity 26%, Warfare 19%

### Dec 19-22
- **08_violence_analysis.ipynb**: Violence feature exploration

### Dec 26
- **Critical audit**: Three-agent review identified issues
  - AUC 0.744 was cherry-picked (true = 0.657)
  - 50+ tests without FDR correction
  - Causal language overreach
- **OVERHAUL initiated**

---

## Phase 5: Methodology Overhaul (Dec 2025 - Jan 2026)

### Dec 26
- Phase 1-4 complete in single day:
  - Corrected AUC references (0.744 → 0.66 ± 0.06)
  - Added LOEO AUC = 0.57 (weak temporal generalization)
  - Applied FDR correction (13 → 7 significant findings)
  - Reframed "instability" → "short-duration"
  - Changed "predicts" → "associated with"

### Jan 5
- **10_fdr_correction.ipynb**: Formal statistical correction
  - BH-adjusted p-values for all 34 tests
  - Robust findings: religion effect, era differences, PC1²

### Jan 6-10
- **11_methodology_fixes.ipynb**: Advanced validation
  - Data leakage check: minimal impact (-0.002 AUC)
  - Nested CV: 0.667 ± 0.052
  - **LOEO breakdown**: Ancient 0.71, later eras ~0.47-0.50
  - Weibull survival: ρ = 0.48 (infant mortality pattern)
  - Hazard decreases 70% over first century

---

## Phase 6: CrisisDB Integration (Jan 2026)

### Jan 14
- Obtained power_transitions.csv (3,447 transitions, 264 polities)
- **crisisdb/01_exploration.ipynb**: Initial analysis
  - Violence contagion: 3x multiplier post-violent transition
  - Temporal patterns: 1050 CE peak, Ottoman/Roman concentration
  - 7 figures generated

### Jan 2026 (Current)
- **crisisdb/02_elite_overproduction.ipynb**: Turchin hypothesis test
  - Admin levels vs intra-elite conflict
  - r = 0.362, p < 0.001
  - +5.6 pp per admin level
  - n = 87 polities with merged data

- **crisisdb/03_violence_contagion.ipynb**: ML modeling
  - Markov chain: P(V→V) = 0.60, stationary = 36% violent
  - HMM: hidden regime states (stable/unstable)
  - Logistic regression: AUC = 0.783
  - Lag decay analysis: violence effect decays over transitions

---

## Key Findings Summary

| Analysis | Metric | Value |
|----------|--------|-------|
| Seshat complexity | Correlation | r = -0.39 |
| Duration regression | R² | 0.149 |
| Equinox classifier | CV AUC | 0.66 ± 0.06 |
| Temporal holdout | LOEO AUC | 0.57 |
| CrisisDB violence | Contagion | 3x multiplier |
| Elite overproduction | Correlation | r = 0.36 |
| Violence Markov | Stationary | 36% violent |
| Violence classifier | AUC | 0.783 |

---

## Robust Findings (survive FDR)

1. Religion effect: More institutionalization → shorter duration (HR = 1.58)
2. Era stratification: Ancient patterns don't generalize to later periods
3. Non-linearity: PC1² critical for classification
4. Infant mortality: Polities face highest risk early (ρ = 0.48)
5. Elite overproduction: Admin complexity → intra-elite conflict
6. Violence contagion: Violent transitions cluster temporally

---

## Research Direction

**Past**: Seshat complexity → duration prediction (classification works, regression doesn't)

**Current**: CrisisDB integration for:
- Elite overproduction validation (Turchin alignment)
- Violence dynamics modeling (ML extension)
- Transition mechanism analysis

**Future**:
- Combined Seshat + CrisisDB model
- SHAP interpretability
- Survival analysis with time-varying covariates
- Direct instability measures (vs duration proxy)
