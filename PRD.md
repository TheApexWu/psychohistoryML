# PRD — Psychohistory Notebook Revamp

The WHAT for churning out the remaining notebooks. No ralph loop yet — this is the spec a loop (or a human) executes against. Two anchor notebooks are already built and set the pattern:
`notebooks/12_moralizing_gods_reproduction.ipynb` and `crisisdb/13_missing_data_self_test.ipynb`.

## The thesis every notebook serves
*Honest computational history: what 10,000 years of data can and can't tell us about instability — held to the standard that retracted a Nature paper.* Turchin/Seshat are the subject under test, not the flag. The arc across the project: **Dynamics** (what patterns exist, strong) → **Mechanism** (meltdown simulates how) → **Limits** (what we can't claim, and why that's the point).

## The refined template (every notebook follows it — this is the "slightly more refined" part)
1. **Markdown intro:** the specific claim/question, the real papers it engages (with DOIs), and — where relevant — the controversy it sits inside. No grand-prophecy language.
2. **Load real data** from `data_external/` or a live API. Never a toy or a re-derived subset when the full set is public.
3. **Explore / grasp** the data honestly (shape, coverage, the missingness).
4. **The analysis, with a control.** Where a prior number exists, *reproduce it exactly first* (assert it), then perturb — the ablation is meaningless unless condition 1 matches. Numbers are computed in-cell, never asserted in prose.
5. **Honest finding + a kept caveat.** State what holds, what doesn't, and the threat you did *not* rule out.
6. **References** — real, linked, grouped by whether cited as support or counter-argument.

## Acceptance criteria (per notebook)
- Executes clean: `jupyter nbconvert --to notebook --execute --inplace <nb>` exits 0.
- Every headline number is produced by a code cell, not written into markdown.
- ≥3 genuine citations with working DOIs/links; at least one cited as a counter-argument.
- Where it reproduces a prior result, a `assert` proves condition 1 matches the original.
- One explicit "what this does NOT show" caveat.
- Figures saved to `figures/`, consistent palette (gold `#c9a55c` warm / `#7a2f2f` deep-red for the "original/contested", muted for "observed/honest").

---

## The lineup

### ✅ Built
- **`notebooks/12_moralizing_gods_reproduction`** — reproduces the retracted Nature 2019 result; shows the 42-point swing from the missing-data coding. The rigor anchor.
- **`crisisdb/13_missing_data_self_test`** — runs the same test on our own 60/22 Markov; it *holds* (37.7%→36.1% gap). The through-line anchor.

### 🔨 To build

**N1 · `crisisdb/14_out_of_domain_replication`** — *does the contagion reappear on data Turchin never built?*
- Data: Cline Center Coup d'État v2.2.2 ([Illinois Data Bank](https://databank.illinois.edu/datasets/IDB-9651987), CC0/CC-BY, 1,161 events 1945–2026); Correlates of War **MID v5.0** ([correlatesofwar.org](https://correlatesofwar.org/data-sets/mids/), free academic, 1816–2014).
- Method: treat coup sequences per country as power-transition sequences; re-estimate P(violent|prev violent) and the stationary distribution. Coups *are* violent transitions → same schema.
- Acceptance: if the ~2.7× multiplier and ~36% equilibrium reappear → out-of-domain confirmation; if not → a stated, honest negative. Either is a result.
- Cite: Peyton et al. Cline codebook (DOI 10.13012/B2IDB-9651987_V10); Palmer et al. 2022 MID5.

**N2 · `notebooks/14_scale_to_864`** — *is AUC 0.57 a small-N artifact or a real ceiling?* (the honest-limits centerpiece)
- Data: live Seshat API — [`seshat_api`](https://github.com/Seshat-Global-History-Databank/seshat_api) (MIT), ~864 polities vs the 256 subset. First confirm the real polity count against `seshat-db.com/api/core/polities/`.
- Method: rebuild the complexity/duration feature matrix on the full set; re-run the RF + temporal holdout from `03_instability_prediction`/`09_survival_analysis`. Report OOS AUC at 256 vs 864.
- Acceptance: report the number both ways with CIs; interpret honestly (a stable ~0.57 across 3× N is a *finding about a ceiling*, not a failure).
- Cite: Turchin et al. 2018 PNAS (CC9); Tosh et al. 2018 PNAS comment (as the counter); Turchin et al. 2020 Equinox release note.

**N3 · `us_political_stress/15_us_structural_demographic`** — *test Turchin's own US forecast out-of-sample.* (the topical one)
- Data: US Political Violence DB — [peterturchin.com USPVD2010.xlsx](https://peterturchin.com/wp-content/uploads/2017/01/USPVD2010.xlsx) + live [CrisisDB USPVDB](https://seshat-db.com/crisisdb/uspvdb_download/) (through 2025).
- Method: rebuild the annual violence series 1780–2025; fit the contagion/structural-demographic model on **1780–2010**, hold out **2010–2025** as a true out-of-sample test. Reconstruct a Political Stress Index using Ortmans et al. 2017's UK recipe on public US series.
- Acceptance: a dated, falsifiable out-of-sample comparison — you are grading Turchin's 2010 forecast, not repeating it.
- Cite: Turchin 2012 JPR; Turchin 2010 Nature 463:608; Turchin 2020 retrospective (PMC7430736); Ortmans et al. 2017 Cliodynamics.

**N4 · `crisisdb/16_navigating_polycrisis_validation`** — *validate our own violence labels against an independent coder.*
- Data: CrisisDB "Navigating Polycrisis" ([Dryad mkkwh715m](https://datadryad.org/dataset/doi:10.5061/dryad.mkkwh715m), CC0, 13 crisis-outcome codes, present/absent/inferred).
- Method: merge the 13 independently-coded outcome variables onto `power_transitions.csv`; check agreement between our `violent` label and their uprising/civil-war/assassination/deposition codes; report a confusion/agreement matrix + a second missing-data band using *their* inferred flags.
- Acceptance: a stated label-validity number; concordance strengthens the contagion result, discordance is disclosed.
- Cite: Hoyer et al. 2023 Navigating Polycrisis (Phil Trans R Soc B 378:20220402); Hoyer et al. 2024.

**N5 · `crisisdb/17_spatial_contagion`** — *is the contagion spatial or purely temporal?* (genuinely new, higher effort)
- Data: Cliopatria v0.1.3 ([Zenodo 14714684](https://zenodo.org/records/14714684), CC-BY-4.0, 307 MB) — polity geometries + rulers.
- Method: build neighbor-adjacency from geometries; test whether a violent transition in polity A raises P(violent) in *bordering* polities B, separating spatial contagion from within-polity temporal autocorrelation.
- Acceptance: a spatial vs temporal decomposition; either result is publishable and new.
- Cite: Cliopatria Nat. Sci. Data 2025 (s41597-025-04516-9).

### Optional enrichment (build only if the above land)
- **`notebooks/16_military_tech_features`** — add the 46 warfare binaries (OSF mkhde, Hoyer et al. 2021 PLOS One) to the complexity model; test warfare→complexity, engaging Turchin et al. 2022 Sci. Adv. and the "does warfare make societies complex" debate.
- **`notebooks/17_axial_age_test`** — the Mullins et al. 2018 ASR Axial Age dataset; a self-contained skeptical vignette (the paper found little support).

---

## Sequence & dependencies
- N1 and N4 need only local + small downloads → build first (fast, high-signal, both strengthen the strong track).
- N2 depends on live-API access working → confirm the API before committing.
- N3 is self-contained and topical → high portfolio value, medium effort.
- N5 is the big new analysis → last, highest effort (307 MB geo data).

## Data hygiene (applies to all)
- Equinox license is inconsistently stated across sources → treat as **CC-BY-NC-SA**, cite, do **not** rehost raw data on the public site; link instead.
- Confirm each `download_oldcsv` link and the 864 count with one live fetch before quoting.
- eHRAF/DRH are restrictive (subscription; DRH is CC-BY-NC-**ND**) → triangulate, don't republish derived tables.
- Keep all downloaded data under `data_external/` (gitignore the large files; commit a `data_external/README.md` with URLs + licenses so the repo is reproducible without rehosting).
