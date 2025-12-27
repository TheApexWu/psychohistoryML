# PsychohistoryML

**Exploring patterns in civilizational dynamics using machine learning and 10,000 years of historical data.**

This project analyzes the Seshat Global History Databank to understand factors affecting civilizational stability. Core finding: **religious and ideological factors are more predictive of instability than traditional complexity measures**, with temporal heterogeneity playing a crucial role.

*"The fall of Empire, gentlemen, is a massive thing, however, and not easily fought. It is dictated by a rising bureaucracy, a receding initiative, a freezing of caste, a damming of curiosity—a hundred other factors."*  
— Isaac Asimov, *Foundation*

---

## Project Status: Complete

**Three-Mechanism Model Achieved:**
- Religion: 27.2% feature importance
- Complexity: 25.8% feature importance
- Warfare: 19.3% feature importance
- **Cross-Validation:** AUC 0.66 ± 0.06 (Random Forest)
- **Temporal Holdout (LOEO):** AUC 0.57 (weak temporal generalization)

*Note: This is exploratory analysis, not confirmatory hypothesis testing.*

---

## Key Findings

### 1. Religion Dominates Prediction
**Ideology score** (12.7%) is the single strongest predictor of civilizational instability, outweighing traditional complexity measures. This challenges assumptions about bureaucratic complexity being the primary driver of civilizational outcomes.

### 2. Era-Stratified Effects
The complexity-duration relationship varies significantly across historical periods:
- **Ancient** (pre-500 BCE): Strong negative correlation (R²=0.21)
- **Classical-Medieval** (500 BCE-1500 CE): Weak to moderate effects
- **Early Modern** (1500+ CE): Minimal relationship

### 3. Realistic Performance Bounds
AUC ~0.67 (CV mean: 0.66 ± 0.06) represents meaningful but appropriately modest predictive power for complex historical phenomena. Temporal holdout (LOEO AUC = 0.57) shows weak generalization across eras, suggesting era-specific patterns rather than universal laws.

---

## Methodology

### Data Source
**Seshat Global History Databank** - Equinox 2022 release
- 256 polities after filtering
- Timeline: ~3000 BCE to 1900 CE
- 16 features across three mechanisms

### Three-Mechanism Framework
1. **Complexity**: Administrative levels, settlement hierarchy, social stratification
2. **Warfare**: Military technology, fortifications, weapons systems  
3. **Religion**: Moral enforcement, ruler legitimacy, ideological frameworks

### Target: Instability Classification
**Instability** = Duration below 33rd percentile (~146 years). Binary classification proves more robust than duration regression for complex historical processes.

---

## Notebooks (Sequential Order)

| # | Notebook | Purpose | Key Result |
|---|----------|---------|------------|
| 04 | `04_equinox_replication.ipynb` | Era clustering discovery | Geographic < Temporal patterns |
| 05 | `05_warfare_integration.ipynb` | Warfare mechanism | AUC 0.505 → 0.601 |
| 06 | `06_religion_integration.ipynb` | Religion mechanism | AUC 0.601 → 0.606 |
| 07 | `07_production_deployment.ipynb` | Final model | AUC ~0.67, production ready |

### Production Models
- **Best Classifier**: Random Forest (CV AUC = 0.66 ± 0.06)
- **Temporal Holdout**: LOEO AUC = 0.57 (limited era generalization)
- **Deployment**: Complete pipeline with scaler and predictor class

---

## Limitations & Cautions

### Sample Size
256 polities enables pattern detection but limits generalizability. Historical machine learning faces inherent small-sample constraints.

### Selection Bias  
Complex societies leave better historical records. Our models may better predict "recordable endings" than actual civilizational dynamics.

### Causality Unknown
Correlation ≠ causation. Do these factors cause instability, or do impending crises drive institutional changes? Causal inference remains challenging.

### Temporal Generalization
Model trained on historical data may not generalize to contemporary societies with fundamentally different institutional structures, technology, and global connectivity.

### Predictive Humility
This work identifies historical correlations, not laws of social physics. Real civilizational dynamics involve contingency, agency, and complexity that resist deterministic modeling.

---

## What This Work Demonstrates

**Achieves:**
- Systematic analysis of large-scale historical patterns
- Validation that machine learning can detect meaningful signals in historical data
- Demonstration that religious/ideological factors merit greater attention in civilizational analysis
- Open methodology with appropriate uncertainty quantification

**Does Not Claim:**
- Ability to predict specific civilizational outcomes
- Discovery of universal laws of social development  
- Relevance to contemporary policy or governance
- Reduction of complex historical processes to simple algorithms

---

## Getting Started

```bash
git clone https://github.com/TheApexWu/psychohistoryML.git
cd psychohistoryML
pip install -r requirements.txt
jupyter notebook notebooks/
```

Start with `04_equinox_replication.ipynb` and proceed sequentially.

---

## Academic Context

Builds on Peter Turchin's cliodynamics, Joseph Tainter's complexity theory, and quantitative approaches to historical analysis. Applies modern machine learning while maintaining historical methodology standards.

---

## Interactive Web App (WIP)

See companion project: [psychohistoryML-web](https://github.com/TheApexWu/psychohistoryML-web) for interactive exploration of the model and historical comparisons.

---

*"Historical patterns exist, but prediction remains probability, not certainty."*
