# PsychohistoryML
**Can machine learning predict civilizational collapse? I trained models on 10,000 years of history to find out.**

Inspired by Isaac Asimov's Foundation series, this project uses the Seshat Global History Databank to test whether social complexity patterns can predict which civilizations will collapse versus survive. The results are surprising: high complexity is a risk factor, not a protective one.

---

## Key Findings

- **Classification works**: 85% accuracy (AUC = 0.854) identifying collapse-prone civilizations
- **Regression doesn't**: Only 15% of duration variance explained by complexity (R² = 0.149)
- **Non-linearity dominates**: Complexity squared is the strongest predictor - suggesting tipping points
- **The paradox**: More sophisticated societies tend to be more fragile, not more resilient

**Interpretation**: We can identify *risk factors* (like medical diagnostics) but can't predict *exact outcomes* (like lottery numbers). History is patterned but not deterministic.

---

## What's Inside (so far)

### Completed Analyses

**Notebook 01: Data Exploration** ([`01_social_complexity_exploration.ipynb`](notebooks/01_social_complexity_exploration.ipynb))
- PCA on hierarchical complexity variables (settlement, administrative, religious, military levels)
- Extracted 3 components explaining 95% of variance
- Validates Turchin et al. (2017) "social complexity" axis

**Notebook 02: Regression Analysis** ([`02_social_complexity_modeling.ipynb`](notebooks/02_social_complexity_modeling.ipynb))
- Predicting polity duration from complexity metrics
- Result: R² = 0.149 (weak but significant negative correlation)
- **Finding**: Higher complexity → shorter duration (counterintuitive!)

**Notebook 03: Collapse Prediction** ([`03_collapse_prediction.ipynb`](notebooks/03_collapse_prediction.ipynb))
- Binary classification: collapse (below median duration) vs survival
- Models: Logistic Regression, Random Forest, XGBoost
- Result: **AUC = 0.854** using Random Forest/XGBoost
- **Finding**: Non-linear effects (PC1²) are most important predictor

**Research Report** ([`RESEARCH_REPORT.md`](reports/RESEARCH_REPORT.md))
- Comprehensive write-up answering all research questions from notebooks
- Methods, results, interpretation, limitations
- College-level (not overly academic)

### Coming Soon

- **Equinox 2022 Dataset Migration**: 47K rows with warfare and religion data
- **Interactive Simulator**: Streamlit app for exploring collapse risk
- **Survival Analysis**: Time-to-event modeling with Cox proportional hazards
- **Warfare Predictions**: Can we predict when polities go to war?

---

## Methodology

**Data Source**: [Seshat Global History Databank](https://seshatdatabank.info/) (2017 release)
- 28,175 data points across 459 historical polities
- Systematic coding of social complexity variables
- Timeline: ~3000 BCE to 1800 CE

**Sample**: After filtering, 114 polities with both complexity data and reliable timelines

**Complexity Metrics** (from Seshat):
1. Settlement Hierarchy (1-10): levels of urban organization
2. Administrative Levels (1-10): bureaucratic depth
3. Religious Levels (1-10): religious hierarchy
4. Military Levels (1-10): command structure depth

**Analytical Approach**:
1. PCA to extract underlying complexity dimensions
2. Regression to test complexity-duration relationship
3. Classification to identify collapse-prone profiles
4. Feature engineering (squared terms, interactions) to capture non-linearity

---

## Results Summary

### Model Performance

| Model | Task | Metric | Score |
|-------|------|--------|-------|
| Linear Regression | Predict duration | R² | 0.149 |
| Random Forest | Classify collapse | ROC-AUC | 0.838 |
| XGBoost | Classify collapse | ROC-AUC | **0.854** |

### Feature Importance (Collapse Prediction)

1. **PC1² (24.3%)** - Non-linear complexity effect
2. **PC1 (24.1%)** - General complexity level
3. **PC1 × PC2 (18.4%)** - Interaction: complexity × religious specialization

**What this means**: The relationship isn't linear. There's a "Goldilocks zone" - some complexity helps, but very high complexity becomes a vulnerability.

### Why the Paradox?

**Low R² (regression) + High AUC (classification)**

- Can't predict *exact* duration well (too much noise, contingency)
- Can predict *risk category* well (structural patterns exist)
- Like weather: can forecast "hotter than average" better than exact temperature

---

## Getting Started

### Prerequisites
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter
```

### Run the Analysis
```bash
git clone https://github.com/yourusername/psychohistory-ml.git
cd psychohistory-ml
jupyter notebook notebooks/
```

Start with `01_social_complexity_exploration.ipynb` and progress through the sequence.

### Data
The Seshat dataset is included in `data/` under CC BY-NC-SA 4.0 license (research use only).

---

## Key Insights

### 1. Complexity as Vulnerability
Higher social complexity (more hierarchical layers, more specialization) correlates with *shorter* duration, not longer. Possible explanations:
- Coordination costs grow super-linearly
- More interdependencies → cascading failures
- Rigidity prevents adaptation to shocks
- Elite extraction provokes instability

### 2. Non-Linear Dynamics
The squared term (PC1²) being the strongest predictor suggests *threshold effects*:
- Below threshold: Complexity helps (enables scale)
- Above threshold: Complexity hurts (creates fragility)
- Not a smooth relationship but a tipping point

### 3. Predictability Limits
Only 15% of duration variance is explainable from complexity metrics. The other 85%:
- Warfare (not in 2017 dataset)
- Climate shocks
- Economic factors
- Leadership quality
- Pure randomness

This sets realistic expectations: We can identify risk factors but can't perfectly predict history.

### 4. Classification > Regression
Binary outcomes (collapse vs survival) are much more predictable than continuous ones (exact duration). This is common in complex systems near critical points.

---

## Background

### Inspiration: Asimov's Psychohistory
In Isaac Asimov's *Foundation* series, "psychohistory" is a fictional science combining history, sociology, and statistics to predict the future of large populations. While Asimov's version required quadrillions of people and perfect knowledge, modern data science + historical databases let us test whether any version of this is possible.

**Verdict**: Sort of! We can identify structural risk factors (like identifying heart attack risk) but can't predict exact timelines (like predicting exact day of heart attack).

### Academic Context
This work builds on:
- **Peter Turchin et al. (2017)**: Seshat database and social complexity measurement
- **Joseph Tainter (1988)**: *The Collapse of Complex Societies*
- **Jared Diamond (2005)**: *Collapse: How Societies Choose to Fail or Succeed*

Unlike those works, this takes a pure machine learning approach: let the algorithms find patterns without imposing theoretical priors.

---

## Visualizations

All notebooks generate publication-quality figures:
- Correlation matrices
- PCA biplots
- Regression diagnostics
- ROC curves with confidence intervals
- Confusion matrices
- Feature importance plots
- Calibration curves
- Risk spectra

See `figures/` directory for outputs.

---

## Limitations

**Sample Size**: 114 polities (23 test cases) is small for ML
- High variance across folds
- Can't detect subtle effects
- Confidence intervals are wide

**Selection Bias**: Seshat overrepresents:
- Literate societies (better documentation)
- Urban societies (more archaeological visibility)
- Large polities (empires over chiefdoms)

**Static Snapshots**: We treat each polity as one observation, missing:
- Complexity trajectories over time
- Early warning signals
- Dynamic adaptation patterns

**Missing Variables**: 
- Warfare frequency/intensity (coming in Equinox 2022)
- Climate data
- Economic metrics
- Leadership quality

**Causality**: Correlation ≠ causation (duh!)
- Does complexity cause collapse?
- Or does impending collapse cause complexity (desperate adaptation)?
- Or do both have common causes?

---

## Tech Stack (so far)

- **Python 3.10+**
- **Data**: pandas, numpy
- **ML**: scikit-learn, xgboost
- **Viz**: matplotlib, seaborn
- **Stats**: statsmodels, scipy
- **Notebooks**: Jupyter

---


## Citation

If you use this work, please cite:

```bibtex
@misc{psychohistoryml2025,
  author = {[Your Name]},
  title = {PsychohistoryML: Predicting Civilizational Collapse Using Machine Learning},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/TheApexWu/psychohistory-ml}
}
```

**Data Source**:
```bibtex
@article{turchin2017seshat,
  title={Seshat: The global history databank},
  author={Turchin, Peter and others},
  journal={Cliodynamics},
  volume={6},
  number={1},
  year={2015}
}
```

---

## License

**Code**: MIT License (see [LICENSE](LICENSE))

**Data**: Seshat dataset is CC BY-NC-SA 4.0 (research use only, no commercial use)

**Papers/Reports**: CC BY 4.0 (attribute and share alike)

---

## Contributing

This is a personal research project but feedback welcome! 

- **Found a bug?** Open an issue
- **Have a suggestion?** Start a discussion
- **Want to collaborate?** Reach out at [your email/twitter]

Particularly interested in:
- Alternative modeling approaches
- Additional historical datasets to cross-validate
- Causal inference methodologies
- Survival analysis experts

---

## Acknowledgments

- **Seshat Project**: For creating and maintaining this incredible database
- **Peter Turchin & team**: For pioneering quantitative history
- **Isaac Asimov**: For inspiring generations with psychohistory

---

## Contact

- GitHub: [@TheApexWu](https://github.com/TheApexWu)
- Twitter: [@AmadeusWoo](https://twitter.com/AmadeusWoo)
- Email: amadeuswoo@proton.me

---

*"The fall of Empire, gentlemen, is a massive thing, however, and not easily fought. It is dictated by a rising bureaucracy, a receding initiative, a freezing of caste, a damming of curiosity—a hundred other factors."*  
— Isaac Asimov, *Foundation*
