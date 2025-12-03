# PsychohistoryML

**Testing whether Asimov's fictional "psychohistory" has any basis in reality—using 10,000 years of historical data.**

This project uses the Seshat Global History Databank to analyze patterns in civilizational stability. The core finding: social complexity correlates with *shorter* duration, not longer—but this relationship is historically bounded and requires context to interpret properly.

*"The fall of Empire, gentlemen, is a massive thing, however, and not easily fought. It is dictated by a rising bureaucracy, a receding initiative, a freezing of caste, a damming of curiosity—a hundred other factors."*  
— Isaac Asimov, *Foundation*

---

## Project Status

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | 2017 Dataset Analysis | Complete |
| 2 | Equinox 2022 Replication |  In Progress |
| 3 | Warfare & Religion Analysis |  Planned |
| 4 | Interactive Explorer |  Planned |

---

## Current Findings

### Phase 1: 2017 Dataset (n=114 polities)

| Task | Model | Metric | Result |
|------|-------|--------|--------|
| Predict duration | Linear Regression | R² | 0.149 |
| Classify instability | Random Forest | ROC-AUC | 0.777 |
| Classify instability | XGBoost | ROC-AUC | **0.848** |

**Key insight**: Classification works much better than regression. We can identify *risk profiles* (like medical diagnostics) but can't predict *exact duration* (too much noise, contingency, missing variables).

### Phase 2: Equinox 2022 Dataset (n=256 polities)

The complexity-instability relationship is **historically bounded**:

| Era | N | β (complexity→duration) | R² | Interpretation |
|-----|---|-------------------------|-----|----------------|
| Ancient (pre-500 BCE) | 77 | -159 | 0.212 | **Strong negative** |
| Classical (500 BCE-500 CE) | 44 | -20 | 0.069 | Weak |
| Medieval (500-1500 CE) | 92 | -11 | 0.027 | No relationship |
| Early Modern (1500+ CE) | 43 | +6 | 0.035 | **Reversed** |

**What this means**: The "complexity curse" isn't universal—it's strongest in ancient state formation and weakens (or reverses) in later periods. Institutional innovations, military technology, and religious developments likely changed the dynamics.

---

## Notebooks

### Completed

| # | Notebook | Dataset | Purpose |
|---|----------|---------|---------|
| 01 | `01_social_complexity_exploration.ipynb` | 2017 | PCA on hierarchy variables, validate Turchin methodology |
| 02 | `02_social_complexity_modeling.ipynb` | 2017 | Regression: complexity → duration (R²=0.15) |
| 03 | `03_instability_prediction.ipynb` | 2017 | Classification: XGBoost AUC=0.848 |
| 04 | `04_equinox_replication.ipynb` | Equinox 2022 | Replicate with larger dataset, diagnose performance |
| 04b | `04b_era_regional_diagnostics.ipynb` | Equinox 2022 | Era stratification, identify where complexity fails |

### Planned

| # | Notebook | Purpose |
|---|----------|---------|
| 05 | `05_warfare_analysis.ipynb` | Add warfare variables, test era×warfare interactions |
| 06 | `06_religion_analysis.ipynb` | Add religion variables, test stabilizing effects |
| 07 | `07_final_model.ipynb` | Ensemble model with full feature set |

### Future Deliverables

| # | Deliverable | Purpose |
|---|-------------|---------|
| — | Interactive Explorer | Streamlit app: adjust variables, see risk predictions |
| — | Ablation Dashboard | Which features matter? Toggle on/off, watch AUC change |
| — | "Which Polity Are You?" | Similarity finder for historical comparisons |

---

## Methodology

### Data Source

**Seshat Global History Databank** ([seshatdatabank.info](https://seshatdatabank.info/))
- 2017 release: 114 polities after filtering
- Equinox 2022 release: 256 polities with warfare and religion variables
- Timeline: ~10,000 BCE to 1900 CE

### Complexity Metrics (PCA on 4 variables)

| Variable | Range | Meaning |
|----------|-------|---------|
| Settlement Hierarchy | 0-7 | Levels of urban organization |
| Administrative Levels | 0-9 | Bureaucratic depth |
| Religious Levels | 0-10 | Religious hierarchy |
| Military Levels | 0-12 | Command structure depth |

PC1 captures ~70% of variance → "general complexity"

### Target Variable

**Instability** = Duration below 33rd percentile (~146 years)

We use "instability" rather than "collapse" because Seshat records when polities ended, not *how*—could be violent collapse, peaceful transition, or absorption.

### Modeling Approach

1. **Baseline**: Logistic regression on PC1-3
2. **Non-linear**: Add PC1², PC1×PC2 interaction terms
3. **Tree models**: Random Forest, XGBoost with class balancing
4. **Stratification**: Era-specific analysis where relationships differ

---

## Honest Limitations

### Sample Size
114-256 polities is small for ML. High variance, wide confidence intervals, can't detect subtle effects reliably.

### Selection Bias
Seshat overrepresents literate, urban, large polities. Complex societies leave better archaeological records—we may detect their endings better than simple societies'.

### Temporal Correlation
Civilizations influence each other (Rome → Byzantium). Random train/test splits may leak information. Era-stratified cross-validation would be more rigorous.

### Causality
Correlation ≠ causation. Does complexity cause instability? Or does impending crisis cause complexity (defensive bureaucratization)? Or common causes?

### Missing Variables
Climate, economics, leadership quality, geography, contingency—all absent from current models.

---

## What This Is (and Isn't)

**IS:**
- Exploration of whether ML can detect historical patterns
- Replication/extension of Turchin et al.'s cliodynamics work
- Open-source learning project with honest methodology

**IS NOT:**
- A claim to have "built psychohistory"
- Predictive model for contemporary societies
- Substitute for historical expertise


---

## Getting Started

```bash
# Clone
git clone https://github.com/TheApexWu/psychohistory-ml.git
cd psychohistory-ml

# Install dependencies
pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter

# Run notebooks
jupyter notebook notebooks/
```

Start with `01_social_complexity_exploration.ipynb` and progress sequentially.

---

## Key Insights

### 1. Complexity is Context-Dependent
The "complexity curse" only appears in ancient polities (R²=0.21). Medieval and early modern societies show no relationship—suggesting institutional innovations buffered complexity costs.

### 2. Non-Linear Effects Matter
PC1² (complexity squared) is consistently important. There may be a "Goldilocks zone" where moderate complexity helps but excessive complexity creates fragility.

### 3. Classification > Regression
Binary outcomes (stable/unstable) are far more predictable than continuous duration. We can identify risk factors without predicting exact outcomes—like medicine, not astrology.

### 4. Era Stratification is Essential
Pooling all eras obscures real heterogeneity. Era-specific models or era×feature interactions are needed.

---

## Academic Context

Builds on:
- **Peter Turchin et al.**: Seshat database, cliodynamics
- **Joseph Tainter**: *The Collapse of Complex Societies* (1988)
- **Oswald Spengler**: Cyclical theories of civilization
- **Jack Goldstone**: Demographic-structural theory

---

## Citation

```bibtex
@misc{psychohistoryml2025,
  author = {Amadeus Wu},
  title = {PsychohistoryML: Analyzing Civilizational Stability with Machine Learning},
  year = {2025},
  url = {https://github.com/TheApexWu/psychohistory-ml}
}
```

---

## License

- **Code**: MIT License
- **Data**: Seshat CC BY-NC-SA 4.0 (research use only)

---

## Contact

- GitHub: [@TheApexWu](https://github.com/TheApexWu)
- Twitter: [@AmadeusWoo](https://twitter.com/AmadeusWoo)
- Substack: [amadeuswu.substack.com](https://amadeuswu.substack.com)

---

*"Seldon knew that his psychohistory could predict only probabilities, and not certainties."* — Asimov
