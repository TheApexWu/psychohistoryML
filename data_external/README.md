# Data sources

Every dataset used here is public. Large files are gitignored; the two small CSVs
below are committed so `notebooks/17` runs from a clean clone.

## Committed in this directory

`seshat_api/polities_864.csv`, `seshat_api/sc_features_864.csv`
Pulled from the live Seshat API, https://seshat-db.com, via the MIT-licensed client
https://github.com/Seshat-Global-History-Databank/seshat_api. 864 polity records and
the social-complexity variables for them, 84 KB total. Seshat data is CC-BY-NC-SA.

Cite: Turchin, Currie, Whitehouse et al. (2018), "Quantitative historical analysis
uncovers a single dimension of complexity that structures global variation in human
social organization," PNAS 115(2):E144-E151.

## Gitignored — download these to re-run the rest

- Beheim et al. (2021) replication archive, used by `notebooks/12`:
  https://github.com/babeheim/moralizing-gods-reanalysis (CC-BY-NC-SA)
- Seshat Equinox release: https://github.com/datasets/seshat (CC-BY-NC-SA)
- CrisisDB "Navigating Polycrisis":
  https://datadryad.org/dataset/doi:10.5061/dryad.mkkwh715m (CC0)

The Equinox release carries inconsistent license statements across Zenodo, its GitHub
LICENSE file and the project docs. Treated here as CC-BY-NC-SA: cited and linked,
never rehosted.
