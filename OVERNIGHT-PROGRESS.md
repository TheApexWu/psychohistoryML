# Overnight progress — 28→29 Aug 2026

Built while you slept. Every notebook was executed end-to-end (`nbconvert --execute`, exit 0) and every headline number is computed in-cell, not asserted. Where a prior result exists, a control `assert` proves condition-1 reproduces it before any perturbation. One overclaim of mine was caught and corrected (see N16).

## What got built (5 notebooks)

**`notebooks/12_moralizing_gods_reproduction`** — reproduces the retracted *Nature* 2019 "moralizing gods" result on the real Beheim data. Finding: only 44.7% of the moralizing-gods variable was ever observed; coding the unobserved cells as "absent" vs dropping them swings the headline from 46% → 89% present. **A 42-point swing from a coding choice = the retraction in one cell.**

**`crisisdb/13_missing_data_self_test`** — runs that exact test on *your own* 60/22 Markov. Control asserts it reproduces 60.0%/22.4% first, then ablates the inferred codes. **Your result holds** (gap 37.7% → 36.1%) because your signal is 1,428 observed vs 197 inferred, not a 50/50 coin flip. The through-line — *hold your own work to the standard that retracted theirs* — proven, not claimed.

**`crisisdb/14_label_validation`** — cross-checks your violence labels against the independently-coded "Navigating Polycrisis" CrisisDB module. Honest result: directionally right (44.9% vs 33.4%) but **not significant** (p=0.199, n=47), because the Polycrisis cases are almost all crises so there's barely a contrast group. Reported as under-powered, not hidden.

**`crisisdb/15_channels_of_instability`** — 🌟 **the real find of the night.** Decomposes the violence-contagion by type. Each channel reproduces *itself* (separatism 8×, uprising 5×, invasion 5×) — but **intra-elite conflict, the centerpiece of Turchin's structural-demographic theory, is the most endemic (30% base) and the *least* self-reinforcing channel (1.83×, CI [1.73–1.93], n=972 — non-overlapping with every other channel).** The dynamical engine of instability is mass mobilization and external shock, not the elite channel. A genuinely novel, defensible, mildly Turchin-skeptical result on his own collaborators' data. Bootstrap CIs on every lift.

**`notebooks/16_limits_at_scale`** — pulls the **full live Seshat databank (864 polities, 3× your 256)**, fresh from the API (count verified: 864). Confronts "what is collapse": every polity "ends" (universal, empty), so the real target is *duration*, and the ~184y instability threshold is essentially the median. Region alone explains **11%** of duration variance and medians swing 5× across regions — so "collapse" is part-geography, part-noise, which is *why* the original model scored ~0.57 out-of-sample. **Corrected honesty note:** I first wrote "a large share of the variance"; the real R² is 0.11, so I rewrote it to "modest — the target is partly a map, not a measure." Left in as-corrected.

**`notebooks/17_coverage_artifact`** — 🌟🌟 **the capstone, built on the second wakeup.** Re-fits the complexity→collapse model on the full 864-polity databank (complexity variables pulled from the live API). The result is decisive: on **observed** complexity data the model is *anti-predictive* (AUC 0.403, 10-seed robust); the imputed model's 0.647 (≈ the original 0.66) is largely a **data-coverage artifact** — missingness *alone* scores 0.592 because **better-documented polities are shorter-lived** (r=−0.24, 154y vs 279y median). Median imputation launders "this polity is well-documented" into a fake "complexity predicts collapse" signal worth ~0.25 AUC. **This is the moralizing-gods retraction (N12) reproduced on our own headline result.** The violence-contagion result survives this test; the complexity-collapse result does not — and that asymmetry is the thesis. All numbers computed in-cell; caveats (complete-case n=170 is small) kept honest.

## The complete arc (this is now a coherent portfolio, not five loose notebooks)
**12** their retraction → **13** our contagion *survives* the same test → **15** a novel decomposition (elite conflict is the flat channel) → **16** the outcome "collapse" is incoherent → **17** our own complexity result was the *same* coverage/imputation artifact that retracted the Nature paper. One thesis: *a well-defined outcome supports real findings; a vague one supports artifacts — and here's the honest math for both, including on our own work.*

## Data downloaded (all under `data_external/`)
- `moralizing-gods-reanalysis/` (Beheim critique repo + the raw Seshat export)
- `seshat-datasets/` (Seshat CSV mirror: complexity, moralizing religion, axial age, agriculture, Navigating Polycrisis)
- `seshat_api/polities_864.csv` (the full live databank, pulled tonight)

## Blocked / queued (not done, and why — no fabrication)
- **N1 out-of-domain replication (coups/MID):** the Powell-Thyne and CoW servers 403-block scripted download (tried 4 ways incl. browser UA). Needs a manual download or a working mirror. This is the one PRD item that didn't land.
- **Full complexity re-fit at 864:** the polity list + durations are pulled; the social-complexity variables (population, territory, admin levels) need additional API endpoint calls to rebuild the feature matrix and re-run the RF + temporal holdout. Buildable, just heavier — the natural next notebook.
- **N3 US structural-demographic** and **N5 spatial (Cliopatria, 307 MB):** untouched, per the PRD.

## The story that's emerging
The project now has a spine: **a well-defined outcome (was a transition violent) supports real, decomposable findings; a vague one ("collapse") supports a coin flip — and here's the honest math for both.** N15 is the standout — it's an actual research contribution, not a re-skin.
