# Statistical & ML Concepts Reference

Quick reference for methods used across PsychohistoryML analysis.

---

## Correlation

**Pearson's r**: Linear association between two variables.

$$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}$$

| r value | Interpretation |
|---------|----------------|
| +1 | Perfect positive |
| 0 | No relationship |
| -1 | Perfect negative |

**Effect sizes (Cohen)**:
- < 0.1: negligible
- 0.1-0.3: small
- 0.3-0.5: medium
- > 0.5: large

**Spearman's rho**: Rank-based. Robust to outliers and non-linear monotonic relationships.

---

## Principal Component Analysis (PCA)

Dimensionality reduction — finds orthogonal axes of maximum variance.

**Steps**:
1. Standardize data (z-score)
2. Compute covariance matrix
3. Find eigenvectors (directions) and eigenvalues (variance)
4. Project data onto top k eigenvectors

**Loadings**: Correlation between original variables and components.

**Result** (Seshat):
- PC1 (76%): General complexity (all hierarchies load positive)
- PC2 (13%): Religious vs secular emphasis
- PC3 (6%): Military vs administrative specialization

**When to use**:
- Correlated features → combine into fewer dimensions
- Reduce multicollinearity in regression
- Exploratory structure discovery

---

## Linear Regression

$$Y = \beta_0 + \beta_1 X + \varepsilon$$

- beta_0: intercept (Y when X=0)
- beta_1: slope (change in Y per unit X)
- epsilon: error term (residuals)

**R-squared**: Variance explained (0-1)

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

**Adjusted R-squared**: Penalizes adding predictors

$$R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$$

**Result**: R² = 0.149 (complexity explains 15% of duration variance)

---

## Regression Diagnostics

### Assumption Tests

**1. Normality (Shapiro-Wilk)**
- H0: Residuals are normal
- p < 0.05: Non-normal residuals
- Result: W = 0.78, p < 0.001 (violated)

**2. Homoscedasticity (Breusch-Pagan)**
- H0: Constant variance of residuals
- p < 0.05: Heteroscedasticity present
- Result: p = 0.094 (ok)

**3. Autocorrelation (Durbin-Watson)**
- DW in [1.5, 2.5]: No autocorrelation
- Result: DW = 1.98 (ok)

### Diagnostic Plots
- **Residuals vs Fitted**: Should be random scatter (no patterns)
- **Q-Q Plot**: Points should follow diagonal (normality)
- **Scale-Location**: Horizontal line (constant variance)

---

## Polynomial Regression

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \ldots + \varepsilon$$

**When to use**: Curved relationships in residual plots.

**Cross-validate**: Higher degrees often overfit on small samples.

**Result**: Degree 1 best by CV (higher degrees overfit).

---

## Markov Chains

Models sequences where next state depends **only on current state**.

$$P(X_{t+1} = j \mid X_t = i) = p_{ij}$$

### Transition Matrix

```
            -> Peaceful  -> Violent
Peaceful    [   0.78       0.22  ]
Violent     [   0.40       0.60  ]
```

**Reading it**:
- Rows = current state
- Columns = next state
- Each row sums to 1

**Result**:
- P(V->V) = 0.60 — violence is sticky
- P(P->V) = 0.22 — baseline rate

### Stationary Distribution

Long-run equilibrium. Solve pi = piP (left eigenvector for eigenvalue 1).

**Result**: pi = [0.64, 0.36]
- System spends 36% of time violent

---

## Hidden Markov Model (HMM)

Hidden state not directly observable:

```
Hidden:    Stable <-> Unstable
              |         |
Observed:  Peaceful   Violent
```

**Components**:
1. Transition matrix (hidden -> hidden)
2. Emission matrix (hidden -> observed)
3. Initial distribution

**Use**: Infer regime state from observations.

---

## Hawkes Process

Self-exciting point process — events trigger more events.

$$\lambda(t) = \mu + \sum_{t_i < t} \alpha \cdot e^{-\beta(t - t_i)}$$

- mu: baseline rate
- alpha: excitation per event
- beta: decay rate

**Intuition**: Violence raises "temperature", effect decays over time.

---

## Logistic Regression

Binary classification.

$$P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \ldots)}}$$

Coefficients = log-odds change per unit X.

**Interpretation**: exp(beta) = odds ratio

---

## Classification Metrics

### Confusion Matrix

```
                  Predicted
                  0      1
Actual    0      TN     FP
          1      FN     TP
```

**Metrics**:
- Accuracy: (TP + TN) / Total
- Precision: TP / (TP + FP) — "of predicted positives, how many correct?"
- Recall: TP / (TP + FN) — "of actual positives, how many caught?"
- F1: 2 * (Precision * Recall) / (Precision + Recall)

---

## ROC & AUC

**ROC**: True Positive Rate vs False Positive Rate at all thresholds.

**AUC** (Area Under Curve):
- 0.5: random
- 0.7-0.8: acceptable
- 0.8-0.9: good
- > 0.9: excellent

**Results**:
- Seshat classifier: AUC = 0.66 +/- 0.06
- CrisisDB violence: AUC = 0.783

---

## Cross-Validation

Estimate performance on unseen data.

**K-fold**:
1. Split into K parts
2. Train on K-1, test on 1
3. Repeat K times, average

**Nested CV**: Inner loop for hyperparameters, outer for unbiased estimate.

**Leave-One-Era-Out (LOEO)**: Temporal holdout — tests generalization across eras.

**Result**: CV AUC = 0.66, LOEO AUC = 0.57 (weak temporal generalization).

---

## Survival Analysis

Time-to-event modeling when some observations are censored.

### Kaplan-Meier

Non-parametric survival curve.

$$\hat{S}(t) = \prod_{t_i \leq t} \left(1 - \frac{d_i}{n_i}\right)$$

### Cox Proportional Hazards

$$h(t) = h_0(t) \exp(\beta_1 X_1 + \ldots)$$

- h_0(t): baseline hazard
- exp(beta): hazard ratio (HR)

**Interpretation**: HR = 1.58 means 58% higher risk.

**C-index**: Concordance (like AUC for survival).

### Weibull AFT

Parametric survival with shape parameter.

$$S(t) = \exp\left(-\left(\frac{t}{\lambda}\right)^\rho\right)$$

- rho < 1: Decreasing hazard (infant mortality)
- rho = 1: Constant hazard (exponential)
- rho > 1: Increasing hazard (wear-out)

**Result**: rho = 0.48 (polities face highest risk early).

---

## Multiple Testing Correction

**Problem**: 50 tests at alpha=0.05 → expect ~2.5 false positives.

### Benjamini-Hochberg (FDR)

Controls False Discovery Rate.

1. Sort p-values
2. p_adjusted = p * (n / rank)
3. Reject if p_adj < alpha

**Result**: 13 "significant" → 7 after FDR.

---

## p-values & Significance

p = probability of result if null hypothesis true.

| p-value | Interpretation |
|---------|----------------|
| < 0.05 | significant (*) |
| < 0.01 | highly significant (**) |
| < 0.001 | very highly significant (***) |

**Caution**: Statistical significance != practical significance.

---

## Confidence Intervals

95% CI = range where true value likely lies.

$$CI = \hat{\beta} \pm 1.96 \times SE$$

Narrower = more precise.

---

## Feature Importance

### Gini Importance (Tree-based)
Average decrease in impurity from splits on that feature.

### Permutation Importance
Drop in performance when feature values are shuffled.

**Result**: PC1² most important (non-linearity matters).

---

## Effect Size vs Statistical Significance

- **p-value**: Could this be chance? (depends on n)
- **Effect size**: How big is it? (independent of n)

With large n, tiny effects become "significant".
With small n, large effects may not reach significance.

Always report both.

---

## Mann-Whitney U Test

Non-parametric alternative to the independent samples t-test.

**When to use**:
- Comparing two groups (violent vs peaceful accession)
- Data is skewed or ordinal (reign lengths are right-skewed)
- Don't want to assume normality

**How it works**:
1. Pool all observations and rank them (1 = smallest)
2. Sum ranks for each group
3. Compare: does one group consistently rank higher?

$$U = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1$$

Where R₁ = sum of ranks in group 1.

**Intuition**: If violent accessions consistently have shorter reigns, their ranks will be lower. U quantifies this.

**Result (Notebook 04)**:
- Violent accession: median 8 years
- Peaceful accession: median 10 years
- p < 0.0001 (one-tailed)

**Why not t-test?** T-test compares means and assumes normality. With reign lengths:
- Mean is inflated by long-ruling outliers
- Distribution has long right tail
- Median is more representative of "typical" reign

---

## One-Tailed vs Two-Tailed Tests

**Two-tailed**: Testing if groups differ in *either* direction.
- H₀: μ₁ = μ₂
- H₁: μ₁ ≠ μ₂

**One-tailed**: Testing a *directional* hypothesis.
- H₀: μ₁ ≥ μ₂
- H₁: μ₁ < μ₂

**When to use one-tailed**:
- You have a specific directional prediction *before* seeing data
- "Violent accession leads to shorter reigns" is directional

**Calculation**: One-tailed p = two-tailed p / 2

**Caution**: Only use if direction was predicted a priori. Don't peek at data first.

---

## Chi-Square Test of Independence

Tests whether two categorical variables are associated.

**Setup**: 2x2 contingency table

```
                    Violent Exit    Peaceful Exit
Violent Entry           264             910
Peaceful Entry          132            1330
```

**Question**: Is entry violence associated with exit violence, or are they independent?

**How it works**:
1. Calculate expected counts if independent: E = (row total × col total) / grand total
2. Compare observed vs expected: χ² = Σ (O - E)² / E
3. Larger χ² = bigger deviation from independence

$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Result (Notebook 04)**:
- χ² = 91.3, p < 0.0001
- Violent entry → 22.5% violent exit
- Peaceful entry → 9.0% violent exit
- Strong association: violence begets violence

---

## Empirical Survival Curves

Non-parametric estimate of "proportion still in power at time t".

**Calculation**:
$$\hat{S}(t) = \frac{\text{rulers with reign} \geq t}{\text{total rulers}}$$

**Interpretation**: At year 10, S(10) = 0.45 means 45% of rulers were still in power after 10 years.

**Comparing curves**: If violent accession curve drops faster, violent rulers are removed sooner.

**Result (Notebook 04)**:
- Violent curve consistently below peaceful curve
- Gap visible from year 1 onwards
- Both converge toward 0 by year 50

**Note**: This is simpler than Kaplan-Meier (no censoring adjustment). Works here because we observe full reign lengths for most rulers.

---

## Median vs Mean for Skewed Data

**Mean**: Sum / count. Sensitive to outliers.

**Median**: Middle value when sorted. Robust to outliers.

**Example** (reign lengths):
- Reigns: [2, 5, 8, 10, 12, 15, 94]
- Mean: 20.9 years (inflated by 94-year outlier)
- Median: 10 years (more representative)

**Rule of thumb**:
- Symmetric data → mean ≈ median, use either
- Right-skewed → mean > median, prefer median
- Left-skewed → mean < median, prefer median

**Reign lengths are right-skewed**: Most rulers reign ~10 years, few reign 50+. Median (8 vs 10 years) is more meaningful than mean (12.4 vs 15.6 years).

---

## Contingency Table Notation

Standard 2×2 layout:

```
                 Outcome=1    Outcome=0    Total
Exposure=1          a            b         a+b
Exposure=0          c            d         c+d
Total             a+c          b+d          n
```

**Derived measures**:
- Risk in exposed: a / (a+b)
- Risk in unexposed: c / (c+d)
- Risk ratio: [a/(a+b)] / [c/(c+d)]
- Odds ratio: (a×d) / (b×c)

**Result (Notebook 04)**:
- Risk of violent exit | violent entry = 264/1174 = 22.5%
- Risk of violent exit | peaceful entry = 132/1462 = 9.0%
- Risk ratio = 2.5× (violent entry → 2.5× more likely violent exit)
