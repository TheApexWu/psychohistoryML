# Psychohistory — Data & Sources Expansion Plan

The notebooks are method-competent but cite **zero** genuine sources (verified: 0 DOI/arxiv links across all of them). This maps real public data + the actual literature onto each track. Every claim goes from "here's what Cox regression is" to "here's how this sits in the real cliodynamics debate — and where it breaks." Provenance tagged; a few links need one confirming click before you cite them.

---

## 1. The data you never used (all public)

| Dataset | Where | License | What it unlocks |
|---|---|---|---|
| **Live Seshat API — ~864 polities** (you used 256) | [seshat-db.com](https://seshat-db.com) · client [`seshat_api`](https://github.com/Seshat-Global-History-Databank/seshat_api) (MIT) | data CC-BY-NC-SA | **3× your N.** Re-run the RF complexity/duration model on 864 polities — is AUC 0.57 a small-N artifact or a real ceiling? That answer *is* the honest-limits story, quantified. |
| **Cliopatria v0.1.3** — geospatial polities + **rulers** 3400 BCE–2024 | [Zenodo 14714684](https://zenodo.org/records/14714684) (307 MB) · [GitHub](https://github.com/Seshat-Global-History-Databank/cliopatria) · [Nat. Sci. Data 2025](https://www.nature.com/articles/s41597-025-04516-9) | **CC-BY-4.0** (verified) | Ruler-tenure survival at real ruler-level scale; and **geometries → neighbor adjacency → test whether your 60% contagion is *spatial* (bordering polities) not just temporal.** A genuinely new analysis. |
| **Military Technology** — 373 polities, 46 warfare binaries | [OSF mkhde](https://osf.io/mkhde/) · [PLOS One 2021](https://doi.org/10.1371/journal.pone.0258161) | open | A whole new **feature family** for the weak track; directly tests the warfare→complexity claim. |
| **Social Complexity CC9** (the PNAS 2018 matrix) | `sc_dataset.12.2017` via [github.com/datasets/seshat](https://github.com/datasets/seshat) | CC-BY-NC-SA | The canonical 9-variable complexity set + published PC1 to benchmark your PCA against. |
| **Moralizing Religion + Beheim reanalysis** | [babeheim/moralizing-gods-reanalysis](https://github.com/babeheim/moralizing-gods-reanalysis) | CC-BY-NC-SA | **The honest-skeptic centerpiece — see §3.** |
| **CrisisDB "Navigating Polycrisis"** — 13 crisis-outcome codes, 150+ cases | [Dryad mkkwh715m](https://datadryad.org/dataset/doi:10.5061/dryad.mkkwh715m) | **CC0** (verified) | Independently-coded operationalization of "violent transition" to **validate your own labels**, + present/absent/**inferred** flags for a missing-data band on your 60/22 Markov. |
| **US Political Violence DB** — 1782→2025 | [peterturchin.com USPVD2010.xlsx](https://peterturchin.com/wp-content/uploads/2017/01/USPVD2010.xlsx) (direct) · live [CrisisDB USPVDB](https://seshat-db.com/crisisdb/uspvdb_download/) | academic-use | **The topical new notebook — see §2c.** |
| **Cline Center Coup d'État** — 1,161 events 1945–2026 | [Illinois Data Bank](https://databank.illinois.edu/datasets/IDB-9651987) (DOI 10.13012/B2IDB-9651987_V10) | CC0/CC-BY | **Out-of-domain replication** of the Markov (a DB Turchin didn't build). |
| **Correlates of War — MID v5.0** 1816–2014 | [correlatesofwar.org](https://correlatesofwar.org/data-sets/mids/) | free academic | Second independent violence-contagion cross-check. |
| **D-PLACE / DRH / eHRAF** | [d-place.org](https://d-place.org) (CC-BY) · [religiondatabase.org](https://religiondatabase.org) · [hraf.yale.edu](https://hraf.yale.edu) | mixed | Cross-cultural triangulation for religion×instability. |

🔴 **License flag:** the Equinox data carries *inconsistent* license statements (Zenodo says AGPL-3.0 / CC-BY-1.0, GitHub LICENSE says CC0, project docs say CC-BY-NC-SA). Treat as **CC-BY-NC-SA + cite**, and don't rehost raw data on the public site — cite and link.

---

## 2. Per-track expansion

### (a) WEAK track `notebooks/` — reframe as "The Limits," and make the limit *rigorous*
- **Scale to 864 polities** via the live API. Report whether OOS AUC moves. Either answer is a finding.
- **Add the 46 military-tech binaries** (OSF mkhde) as a real new feature family; test warfare→complexity.
- **Cite as honest counter-weight, not support:** put **Tosh, Ferguson & Seoighe 2018** ("History by the numbers?", [PNAS comment](https://www.pnas.org/doi/10.1073/pnas.1807023115)) next to your PC1 — concede PCA can't adjudicate causal hypotheses. Put **Slingerland et al. 2020** ("Coding culture", [Evol. Hum. Sci. 2:e29](https://doi.org/10.1017/ehs.2020.30)) as the data-provenance caveat.

### (b) STRONG track `crisisdb/` — validate, stress-test, and replicate out-of-domain
- **Validate your labels:** merge the Dryad "Navigating Polycrisis" 13 crisis-outcome codes onto `power_transitions.csv` — an independent coder's "violent transition."
- **Turn Beheim's weapon on your own numbers:** use the inferred/unknown flags to put a **missing-data sensitivity band** on P(violent|prev violent)=60% vs 22%. Do it *before* a reviewer does.
- **Spatial contagion:** Cliopatria geometries → is the 36% equilibrium spatial or temporal?
- **Out-of-domain replication:** re-estimate the Markov + tenure survival on **Cline Center coups** and **CoW MIDs**. If 60/22 and the equilibrium reappear on databases Turchin never touched → strong confirmation. If not → an honest, publishable negative.
- **The honest ceiling:** cite **Hoyer et al. 2024** ("All Crises are Unhappy in Their Own Way", [OSF](https://doi.org/10.31235/osf.io/rk4gd)) — crisis consequences are "largely uncorrelated and unpredictable." Your own Markov result must be stated *inside* that ceiling.

### (c) NEW notebook `us_political_stress.ipynb` — the topical one
- Pull the live **US Political Violence DB** (1782→2025). Rebuild the annual violence series.
- **Fit the Markov/structural-demographic model on 1782–2010, hold out 2010–2025 as a true out-of-sample test.** This is the honest out-of-sample move the whole reframe is about — and it's topical.
- Reconstruct the **Political Stress Index** using **Ortmans et al. 2017** (UK PSI, [escholarship](https://escholarship.org/uc/item/6qp8x28p), CC-BY) as the recipe.
- Frame with **Turchin 2010** ([Nature 463:608](https://www.nature.com/articles/463608a), "instability may be coming") and **Turchin 2020** ([PMC7430736](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430736/), grading his own 2010 forecast) — you're testing his forecast, not repeating it.

---

## 3. The standout notebook: reproduce the retraction

`moralizing_gods_reproduction.ipynb` — this one alone lifts the whole project from "student ML" to "engages a real scientific controversy":

1. Reproduce **Whitehouse, François, Savage, Turchin et al. 2019**, *"Complex societies precede moralizing gods throughout world history"* — [Nature 568:226](https://doi.org/10.1038/s41586-019-1043-4), **RETRACTED 2021**.
2. Show what **Beheim et al. 2021** ([Nature 595:E29](https://www.nature.com/articles/s41586-021-03655-4)) showed: **61% of the moralizing-gods datapoints are missing**, and recoding missing-as-absent *drove the entire result* — flipping under standard imputation. Their [code+data](https://github.com/babeheim/moralizing-gods-reanalysis) runs end to end.
3. Close with the resolution: **Whitehouse et al. 2022 "retake"** ([RBB 13(2)](https://doi.org/10.1080/2153599X.2022.2074085)) and **"Historians Respond"** ([PDF](https://eprints.lse.ac.uk/107612/1/Historians_Respond_to_Whitehouse_et_al_complete.pdf)).

You reproduce a *Nature* paper, its takedown, and the field's correction — the exact missing-data discipline you then apply to your own CrisisDB numbers in §2b. That through-line ("I hold my own work to the standard that retracted theirs") is the entire portfolio thesis in one arc.

---

## 4. Citation library (group by role in the argument)

**Foundational (cite as the thing you're testing):** Turchin et al. 2018 single-dimension-of-complexity ([PNAS 115(2):E144](https://www.pnas.org/doi/10.1073/pnas.1708800115)) · Turchin, Currie, Turner & Gavrilets 2013 War/space ([PNAS 110:16384](https://www.pnas.org/doi/10.1073/pnas.1308825110)) · Turchin, Whitehouse, Gavrilets et al. 2022 disentangling drivers ([Sci. Adv. 8:eabn3517](https://doi.org/10.1126/sciadv.abn3517)) · Turchin & Nefedov 2009 *Secular Cycles*.

**Structural-demographic / US (the topical notebook):** Turchin 2012 US instability 1780–2010 ([JPR 49(4):577](https://peterturchin.com/wp-content/uploads/2012/06/Turchin_JPR2012.pdf)) · Turchin 2016 *Ages of Discord* · Turchin 2010 Nature · Turchin 2020 retrospective · Ortmans et al. 2017 UK PSI.

**The controversy (your rigor — cite as counter-argument):** Whitehouse 2019 (retracted) · Beheim 2021 critique · Retraction Note ([Nature 595:E9](https://www.nature.com/articles/s41586-021-03656-3)) · Whitehouse 2022 retake · Tosh 2018 · Slingerland 2020 "Coding culture" · Mullins et al. 2018 Axial Age ([ASR 83(3):596](https://doi.org/10.1177/0003122418772567), found little support).

**CrisisDB provenance:** Hoyer et al. 2021 military tech ([PLOS One](https://doi.org/10.1371/journal.pone.0258161)) · Hoyer et al. 2023 Navigating Polycrisis · Hoyer et al. 2024 All Crises are Unhappy.

---

## 5. Confirm before quoting (softer provenance)
- The `github.com/datasets/seshat` `download_oldcsv` links (`mr_dataset`, `axial_dataset`, `agri_dataset`, `sc_dataset`) came via a README snippet, not individually fetched — click each once.
- The 864-polity count is a search snippet, not a curled API count — hit `seshat-db.com/api/core/polities/` and read the real number.
- A few page/issue numbers and the Turchin 2013 *Cliodynamics* DOI are from secondary listings — confirm on the publisher page.
- eHRAF and DRH have restrictive licenses (subscription; DRH is CC-BY-NC-**ND**, no-derivatives) — use for triangulation, don't republish transformed data.
