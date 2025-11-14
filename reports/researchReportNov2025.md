# Research Report (Technical Summary) 11/14/2025

This report summarizes my technical workflow, modeling process, and analytical findings for the **PsychohistoryML** research report. Unlike the public-facing GitHub README, this version focuses strictly on the **statistics, machine learning development, and my modeling progress** across the three notebooks.

---

## Objective

My goal was to evaluate whether historical social-complexity metrics contain enough structure to predict **civilizational collapse**. I approached this as a data-science problem, not a narrative or theory-driven project.

The analysis progresses through:

1. **Notebook 01:** Data cleaning, feature extraction, PCA  
2. **Notebook 02:** Regression modeling  
3. **Notebook 03:** Binary classification and risk modeling  

This report reflects the technical insights I gained along the way.

---

## Dataset & Preparation

### Source
- **Seshat Global History Databank (2017 release)**  
- Initial sample: 459 polities  
- Final sample: **114 polities** with reliable complexity metrics and timelines  

### Core Variables
- Settlement hierarchy  
- Administrative hierarchy  
- Religious hierarchy  
- Military hierarchy  

### Cleaning Steps
- Converted BCE/CE strings to numeric years  
- Computed polity duration  
- Filtered out ambiguous timelines  
- Standardized all complexity features  

---

## Notebook 01 — PCA and Complexity Structure

I applied PCA to reduce the four complexity variables into latent components:

- **PC1 (76%) — General complexity**  
- **PC2 (13%) — Religious vs. secular emphasis**  
- **PC3 (6%) — Military vs. administrative specialization**

**Progress Notes**
- Verified strong correlations between raw hierarchical metrics  
- Confirmed that PC1 captures the majority of meaningful variation  
- Exported PC scores for later modeling  

---

## Notebook 02 — Regression Modeling (Low Predictability)

I attempted to predict exact polity duration using linear and polynomial regression.

### Results
- **R² = 0.149** (PC1 only)  
- PC2/PC3 do not meaningfully improve the model  
- Polynomial models overfit and fail to generalize  

### Diagnostics
- Heteroscedastic residuals  
- Heavy-tailed distribution  
- Outliers heavily influence predictions  

### Interpretation
- Duration is mostly driven by **unobserved factors** (warfare, climate, leadership, randomness)  
- Regression is not the right tool for this domain  

**Progress Notes**
- Identified curvature in scatterplots → led to the idea of squaring PC1  
- Determined that classification would capture threshold behavior better  
- Began engineering non-linear features  

---

## Notebook 03 — Classification Modeling (High Predictability)

I reframed the task as predicting **collapse vs. survival**, using the median duration (162 years) as the threshold.

### Models Tested
- Logistic Regression  
- Random Forest  
- XGBoost  

### Performance
| Model | ROC-AUC |
|-------|---------|
| Logistic Regression | ~0.75 |
| Random Forest | ~0.84 |
| XGBoost | **0.85** |

### Feature Importance
Top predictor:  
- **PC1²** — complexity squared, revealing non-linear risk structure  

### Diagnostics
- Balanced confusion matrix  
- ROC curves with bootstrap confidence intervals  
- Calibration curves for probabilistic accuracy  
- Permutation importance confirming dominance of engineered features  
- 5-fold CV demonstrating stable performance (AUC ≈ 0.82 ± 0.09)

**Progress Notes**
- Confirmed threshold-like behavior missing from regression  
- Built risk spectrum plots to visualize probability distributions  
- Implemented full interpretability suite (permutation, bootstrap, calibration)  
- Validated that non-linearity is essential to model performance  

---

## Technical Takeaways

### 1. PCA was essential  
PC1 captured nearly all relevant structural information.

### 2. Regression was not viable  
Duration is too noisy; complexity is not a strong continuous predictor.

### 3. Non-linearity drives collapse prediction  
Engineered features (PC1², interactions) transform the problem.

### 4. Binary classification works  
AUC ≈ 0.85 demonstrates meaningful separability.

### 5. Feature engineering unlocked the signal  
Squared terms, interactions, and standardized PCA scores were key.

---

## Limitations

- **Small sample size** (114 polities)  
- Likely **selection bias** in Seshat  
- Coded variables introduce **measurement uncertainty**  
- Single snapshot per polity (no time dynamics)  
- No causal claims — only statistical patterns  

---

## Next Steps in My Workflow

### 1. Migrate to **Equinox 2022 Dataset**
Richer variables: warfare, religion, climate, institutional checks.

### 2. Add **survival analysis**
- Cox proportional hazards  
- Time-varying covariates  
- Early-warning signals  

### 3. Expand feature pipeline
- Interaction terms  
- Complexity derivatives over time  
- Lagged features  

### 4. Integrate interpretability tools
- SHAP  
- Partial dependence plots  

---

## Summary: What I Accomplished Technically

- Cleaned/standardized a complex historical dataset  
- Derived PCA structure that captured 95% of variation  
- Demonstrated the limits of regression (R² = 0.149)  
- Built a strong collapse classifier (AUC ≈ 0.85)  
- Implemented diagnostics: CV, calibration, permutation, ROC CI  
- Developed a clear roadmap for upgrading the pipeline using richer datasets  
