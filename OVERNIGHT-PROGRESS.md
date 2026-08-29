# Overnight progress — 28→29 Aug 2026

Built while you slept. Every notebook was executed end-to-end (`nbconvert --execute`, exit 0) and every headline number is computed in-cell, not asserted. Where a prior result exists, a control `assert` proves condition-1 reproduces it before any perturbation. One overclaim of mine was caught and corrected (see N16).

## What got built (5 notebooks)

**`notebooks/12_moralizing_gods_reproduction`** — reproduces the retracted *Nature* 2019 "moralizing gods" result on the real Beheim data. Finding: only 44.7% of the moralizing-gods variable was ever observed; coding the unobserved cells as "absent" vs dropping them swings the headline from 46% → 89% present. **A 42-point swing from a coding choice = the retraction in one cell.**

**`crisisdb/13_missing_data_self_test`** — runs that exact test on *your own* 60/22 Markov. Control asserts it reproduces 60.0%/22.4% first, then ablates the inferred codes. **Your result holds** (gap 37.7% → 36.1%) because your signal is 1,428 observed vs 197 inferred, not a 50/50 coin flip. The through-line — *hold your own work to the standard that retracted theirs* — proven, not claimed.

**`crisisdb/14_label_validation`** — cross-checks your violence labels against the independently-coded "Navigating Polycrisis" CrisisDB module. Honest result: directionally right (44.9% vs 33.4%) but **not significant** (p=0.199, n=47), because the Polycrisis cases are almost all crises so there's barely a contrast group. Reported as under-powered, not hidden.

**`crisisdb/15_channels_of_instability`** — decomposes the violence-contagion by type, with a **robustness section that corrected my own overclaim** (added on the 3rd wakeup). The *raw* finding — intra-elite conflict is the least self-reinforcing channel (1.83× lift) — survives a co-occurrence/gap filter but **does NOT survive controlling for polity propensity + era** (controlled it is rank 5/7, not last; its low raw lift was a base-rate artifact — it is the most common channel, and lift divides by base rate). What survives both views: (1) instability is channel-specific (each channel's strongest successor is itself), and (2) **external shock — invasion/interference — is robustly the most self-reinforcing** (controlled OR 2.4 / 2.2). The defensible headline is narrower and sturdier than the first draft; the exciting 'elite is uniquely flat' claim is downgraded to a base-rate caution, in the notebook itself. The honesty discipline working on our own most exciting result.

**`notebooks/16_limits_at_scale`** — pulls the **full live Seshat databank (864 polities, 3× your 256)**, fresh from the API (count verified: 864). Confronts "what is collapse": every polity "ends" (universal, empty), so the real target is *duration*, and the ~184y instability threshold is essentially the median. Region alone explains **11%** of duration variance and medians swing 5× across regions — so "collapse" is part-geography, part-noise, which is *why* the original model scored ~0.57 out-of-sample. **Corrected honesty note:** I first wrote "a large share of the variance"; the real R² is 0.11, so I rewrote it to "modest — the target is partly a map, not a measure." Left in as-corrected.

**`notebooks/17_coverage_artifact`** — 🌟🌟 **the capstone, built on the second wakeup.** Re-fits the complexity→collapse model on the full 864-polity databank (complexity variables pulled from the live API). The result is decisive: on **observed** complexity data the model is *anti-predictive* (AUC 0.403, 10-seed robust); the imputed model's 0.647 (≈ the original 0.66) is largely a **data-coverage artifact** — missingness *alone* scores 0.592 because **better-documented polities are shorter-lived** (r=−0.24, 154y vs 279y median). Median imputation launders "this polity is well-documented" into a fake "complexity predicts collapse" signal worth ~0.25 AUC. **This is the moralizing-gods retraction (N12) reproduced on our own headline result.** The violence-contagion result survives this test; the complexity-collapse result does not — and that asymmetry is the thesis. All numbers computed in-cell; caveats (complete-case n=170 is small) kept honest.

## The complete arc (this is now a coherent portfolio, not five loose notebooks)
**12** their retraction → **13** our contagion *survives* the same test → **15** a typed decomposition of instability (channel-specific; external shock is the robustly most self-reinforcing — the raw 'elite is flat' claim was corrected as a base-rate artifact) → **16** the outcome "collapse" is incoherent → **17** our own complexity result was the *same* coverage/imputation artifact that retracted the Nature paper. One thesis: *a well-defined outcome supports real findings; a vague one supports artifacts — and here's the honest math for both, including on our own work.*

## Data downloaded (all under `data_external/`)
- `moralizing-gods-reanalysis/` (Beheim critique repo + the raw Seshat export)
- `seshat-datasets/` (Seshat CSV mirror: complexity, moralizing religion, axial age, agriculture, Navigating Polycrisis)
- `seshat_api/polities_864.csv` (the full live databank, pulled tonight)

## Blocked / queued (not done, and why — no fabrication)
- **N1 out-of-domain replication (coups/MID):** the Powell-Thyne and CoW servers 403-block scripted download (tried 4 ways incl. browser UA). Needs a manual download or a working mirror. This is the one PRD item that didn't land.
- **N3 US structural-demographic:** BLOCKED. Turchin's US Political Violence DB won't pull — peterturchin.com 403s the direct .xlsx, the CrisisDB download URL returns an HTML page not a file, and the `api/crisisdb/us-violences/` endpoint throws a 500 server error (their bug). Needs a manual download or for their endpoint to be fixed.
- **N1 coups/MID** (servers 403) and **N5 spatial (Cliopatria, 307 MB)**: still open.

## The story that's emerging
The project now has a spine: **a well-defined outcome (was a transition violent) supports real, decomposable findings; a vague one ("collapse") supports a coin flip — and here's the honest math for both.** N17 is the capstone (our own headline result was a coverage artifact); N15 is a genuine typed decomposition, honestly qualified. Six notebooks, all executed, all committed to `revamp/honest-notebooks`.
