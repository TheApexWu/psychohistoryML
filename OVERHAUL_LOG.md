# PsychohistoryML Research Overhaul Log

**Date Initiated**: 2025-12-26
**Reason**: Critical audit identified methodological issues requiring correction

---

## Executive Summary

Three-agent audit revealed:
- **CRITICAL**: AUC 0.744 was cherry-picked (true = 0.657 ± 0.057)
- **HIGH**: 50+ tests without FDR correction, underpowered subgroups
- **MODERATE**: Exploratory analysis framed as confirmatory, causal language overreach

**Overall Grade**: B+ (methodologically sound with important caveats)

---

## Issue Consolidation (All Three Agents)

### Audit Agents:
1. **Cliodynamics Methodology** - Research standards from the field
2. **ML Best Practices** - Small-sample validation strategies
3. **Full Project Audit** - Line-by-line scrutiny of NB01-09

### Critical Findings:

| Severity | Issue | Action Required |
|----------|-------|-----------------|
| CRITICAL | AUC 0.744 → 0.66 ± 0.06 | Update all references |
| CRITICAL | LOEO AUC = 0.566 hidden | Add to all claims |
| CRITICAL | No pre-registration disclaimer | Add exploratory framing |
| HIGH | Multiple comparisons (50+ tests) | Apply FDR correction |
| HIGH | Underpowered subgroups (n<50) | Label as exploratory |
| MODERATE | "Instability" language | Change to "short-duration" |
| MODERATE | Causal language | Change to "associated with" |

---

## Phase 1: Correct the Record ✅ COMPLETE

### Tasks:
- [x] Find all "0.744" references in codebase
- [x] Update to "0.66 ± 0.06" or "~0.67"
- [x] Add LOEO AUC = 0.57 for temporal generalization
- [x] Add exploratory analysis disclaimer

### Files Updated:
- [x] psychohistory-web/src/components/visualizations/AnimatedStats.jsx (lines 62, 133)
- [x] psychohistory-web/src/components/visualizations/AnimatedROC.jsx (line 137)
- [x] psychohistory-web/src/app/research/page.js (lines 105, 120, 268)
- [x] psychohistory-web/src/app/about/page.js (line 163)
- [x] psychohistoryML/README.md (lines 18, 34, 63, 66)
- [x] psychohistory-web/README.md (lines 25, 26)

---

## Phase 2: Statistical Fixes ✅ COMPLETE

### FDR Correction Applied (Benjamini-Hochberg)
- Total tests across project: 34
- Originally significant (p < 0.05): 13
- **After FDR correction: 7**

### Robust Findings (survive FDR):
1. ✓ Religion effect (total_rel): p_fdr < 0.001
2. ✓ Ancient vs later eras survival: p_fdr < 0.001
3. ✓ Complexity×warfare interaction: p_fdr < 0.001
4. ✓ Non-linear complexity (PC1²): p_fdr < 0.001

### Casualties (originally sig, NOT after FDR):
1. ✗ Ancient complexity effect (p=0.046 → p_fdr=0.12)
2. ✗ Medieval religion effect (p=0.042 → p_fdr=0.12)
3. ✗ Ideology sub-score (p=0.039 → p_fdr=0.12)
4. ✗ Moral sub-score (p=0.042 → p_fdr=0.12)

### Files Created:
- [x] notebooks/10_fdr_correction.ipynb
- [x] models/fdr_correction_results.csv

## Phase 3: Reframe Narrative ✅ COMPLETE

### Language Changes:
- [x] "Instability" → "short-duration" (research/page.js)
- [x] "Predicts" → "explains" / "associated with" (DiscoveriesSection.jsx)
- [x] Added FDR context to findings (research/page.js)
- [x] Updated religion finding (now shows HR=1.58 destabilizing, counterintuitive)

### Chatbot System Prompt Updated:
- [x] Rule 3 now "EPISTEMIC HUMILITY" instead of "AGONISTIC STANCE"
- [x] Explicit "EXPLORATORY analysis" framing
- [x] Lists ROBUST vs EXPLORATORY findings with FDR status
- [x] Instructs to say "associated with" not "causes/predicts"

### Files Updated:
- research/page.js (terminology caveat, religion findings)
- DiscoveriesSection.jsx (discovery #1, #4 language)
- layout.tsx (meta description)
- api/chat/route.js (system prompt)

## Phase 4: Website Overhaul ✅ COMPLETE

- [x] Update Research page (FDR context, religion findings)
- [x] Add "What This Isn't" section (4 key disclaimers)
- [x] Update chatbot system prompt (done in Phase 3)
- [x] Simplified home page to HN-style portfolio
- [x] Moved psychohistory content to /discover

## Phase 5: Technical Polish ✅ COMPLETE

- [x] Created requirements.txt with all dependencies
- [x] Documented threshold sensitivity in README
- [x] Added statistical rigor section (FDR, CIs)
- [x] Updated notebooks table (added NB09, NB10)
- [x] Corrected religion finding (HR=1.58 destabilizing)

---

## The Pivot

**OLD**: "ML predicts civilizational collapse with 0.744 AUC"

**NEW**: "Exploratory analysis reveals era-dependent patterns in civilizational duration. Model shows weak temporal generalization (LOEO AUC 0.57), suggesting historical patterns, not universal laws."

---

## Progress Log

### 2025-12-26
- Created overhaul log
- Beginning Phase 1: Correct the Record
- **Phase 1 Complete**: Updated all 0.744 → ~0.67 (CV mean) across 6 files
  - Added LOEO AUC = 0.57 context for temporal generalization
  - Added "exploratory analysis" framing to README files
  - Research page now mentions era-specific patterns vs universal laws
- **Phase 2 Complete**: Applied FDR correction across all 34 tests
  - Only 7/13 "significant" findings survive correction
  - Ancient complexity effect is now EXPLORATORY (p_fdr = 0.12)
  - Religion effect and era differences remain ROBUST
- **Website Simplified**: New HN-style home page created
  - Psychohistory content moved to /discover
  - Home page now personal portfolio style
- **Phase 3 Complete**: Reframed narrative across website
  - "Instability" → "short-duration"
  - "Predicts" → "associated with"
  - Chatbot now distinguishes ROBUST vs EXPLORATORY findings
  - Religion finding corrected (HR=1.58 destabilizing, counterintuitive)
- **Phase 4 Complete**: Added "What This Isn't" section to research page
  - Not prediction, Not causal inference, Not universal laws, Not definitive
  - Emphasizes hypothesis generation over confirmation
- **Phase 5 Complete**: Technical polish
  - Created requirements.txt
  - Added Statistical Rigor section to README (FDR, threshold sensitivity, CIs)
  - Updated notebooks table with NB09, NB10

---

## Phase 6: Methodology Fixes ✅ COMPLETE

**Date**: 2026-01-05

### 6.1 Data Leakage Investigation

**Concern**: Early notebooks fit StandardScaler/PCA on full data before cross-validation, potentially inflating AUC estimates.

**Result**: Minimal impact (-0.002 AUC)
- Leaky approach: 0.696 ± 0.029
- Pipeline approach: 0.698 ± 0.026
- Random Forest is robust to scaling leakage (tree splits are invariant to monotonic transforms)

**Takeaway**: Previous AUC estimates were NOT significantly inflated, but pipeline approach is now standard.

### 6.2 Nested Cross-Validation

Implemented proper nested CV for unbiased performance estimation with hyperparameter tuning.

**Results**:
- Nested CV AUC: 0.667 ± 0.052
- Best params: max_depth=5, min_samples_split=5, n_estimators=100

### 6.3 Leave-One-Era-Out (LOEO) - Detailed Breakdown

**This is the critical finding:**

| Era Held Out | AUC | Interpretation |
|--------------|-----|----------------|
| Ancient (pre-500 BCE) | 0.711 | Model generalizes TO Ancient |
| Classical (500 BCE-500 CE) | 0.464 | Below chance |
| Early Modern (1500+ CE) | 0.479 | Below chance |
| Medieval (500-1500 CE) | 0.496 | Chance level |

**LOEO Mean**: 0.537 ± 0.101
**CV-LOEO Gap**: +0.13

**Interpretation**: The model learns Ancient-era patterns that completely fail to generalize to later periods. This confirms era-specific patterns, not universal laws.

### 6.4 Advanced Survival Analysis

**Weibull AFT Model** (C-index: 0.630):

| Feature | Coefficient | p-value | Interpretation |
|---------|-------------|---------|----------------|
| total_rel (religion) | -0.372 | <0.0005*** | Shorter duration |
| PC1_hier (complexity) | -0.130 | 0.040* | Shorter duration |
| total_warfare_tech | -0.046 | 0.444 | Not significant |
| PC2_hier | +0.015 | 0.720 | Not significant |
| PC3_hier | -0.056 | 0.183 | Not significant |

**Weibull Shape (rho = 0.478)**: Hazard DECREASES over polity lifetime
- "Infant mortality" pattern: Early years most dangerous
- Polities that survive initial period become more stable

**Aalen Additive Model**: Implemented time-varying coefficients to test whether effects change over polity lifetime. Figures saved for visual inspection.

### 6.5 Files Created/Updated

- [x] `notebooks/11_methodology_fixes.ipynb` - Full analysis
- [x] `models/corrected_results.csv` - Summary metrics
- [x] `figures/11_aalen_time_varying.png` - Time-varying effects
- [x] `figures/11_km_by_era_ci.png` - KM curves with confidence intervals

### 6.6 Key Takeaways

1. **Data leakage was NOT a significant issue** - RF robustness saved us
2. **LOEO gap (+0.13) is the real story** - Model doesn't generalize across eras
3. **Religion remains the strongest predictor** (survives all corrections)
4. **Weibull rho < 1** suggests "infant mortality" pattern for polities
5. **Ancient patterns dominate** - model struggles with later periods

---

## Progress Log (Continued)

### 2026-01-05
- **Phase 6 Complete**: Methodology fixes implemented
  - Data leakage: Minimal impact confirmed, pipeline approach now standard
  - Nested CV: Unbiased AUC = 0.667 ± 0.052
  - LOEO breakdown: Ancient 0.711, later eras ~0.47-0.50 (chance)
  - Weibull AFT: Religion -0.372 (p<0.0005), rho=0.478 (infant mortality pattern)
  - Aalen model: Time-varying coefficients implemented
- Created notebook 11_methodology_fixes.ipynb
- Updated OVERHAUL_LOG.md with findings

---

## OVERHAUL COMPLETE
