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

## Phase 3: Reframe Narrative (Pending)

- [ ] "Instability" → "short-duration"
- [ ] "Predicts" → "associated with"
- [ ] Add Limitations section
- [ ] Explain religion contradiction

## Phase 4: Website Overhaul (Pending)

- [ ] Update Research page
- [ ] Add "What This Isn't" section
- [ ] Update chatbot system prompt

## Phase 5: Technical Polish (Pending)

- [ ] requirements.txt
- [ ] Threshold sensitivity analysis
- [ ] Confidence intervals

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
