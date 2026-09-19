# Pre-supersede archive (Nov 2025 – Feb 2026)

Salvaged 19 Sep 2026 from an untracked second clone (`~/Documents/GitHub/psychohistoryML`, 11 commits
behind). **Everything here predates the corrections landed on 9 Sep 2026** — `1b5dff4` (the
complexity→collapse result is a data-coverage artifact), `66ab565` (intra-elite overclaim corrected)
and `67c9c50` (superseded AUC numbers flagged). Treat any number in these files as superseded unless
it is reproduced by the current notebooks.

- `05_source_quality.ipynb` (25 Jan) — data-quality checks on CrisisDB. Makes no result claims
  (checked: zero AUC/prediction assertions), so it is revivable as-is; it fills the gap between
  `04_*` and `13_*` in `crisisdb/`.
- `generate_models.py` (26 Nov) — builds the production .pkl artifacts from the NB06 dataset.
  Deployment tooling, not a finding. Verify it still matches the post-revamp pipeline before use.
- `embedding-model-benchmark-analysis.html` (28 Feb) — benchmark writeup, unverified against the
  corrected notebooks.

**Not committed, deliberately:** ~26MB of derived output that lived only in that clone —
`figures-export/` (20M), `notebooks-export/` (2.6M), `scratch/` (1.8M), `bdiscoringpngs/` (1.0M),
`models-export/` (464K). They render the retracted results and are regenerable from the current
notebooks. Preserved outside git at `~/Archive/stale-clone-psychohistoryML-20260919/`.
