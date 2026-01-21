# PsychohistoryML

Exploring patterns in civilizational dynamics using machine learning and 10,000 years of historical data.

This project analyzes the Seshat Global History Databank and CrisisDB to understand factors affecting civilizational stability.

## Status

Two analysis tracks are complete:

**Seshat Analysis (Oct-Dec 2025)**
- 256 polities from Seshat Equinox 2022
- Random Forest CV AUC: 0.66 plus/minus 0.06
- Temporal holdout (LOEO) AUC: 0.57
- Core finding: complexity-duration relationship reverses by era

**CrisisDB Analysis (Jan 2026)**
- 3,447 power transitions from CrisisDB
- Administrative complexity correlates with intra-elite conflict (r=0.36, p<0.001)
- Violence is self-reinforcing: P(violent | prev violent) = 60% vs 22% after peaceful
- Violent accession predicts 2 years shorter median reign

Both are exploratory analyses, not confirmatory hypothesis testing.

## Key Findings

### Seshat: Era-Stratified Effects
The complexity-duration relationship varies across historical periods:
- Ancient (pre-500 BCE): Strong negative correlation (R squared = 0.21)
- Classical-Medieval (500 BCE to 1500 CE): Weak to moderate effects
- Early Modern (1500+ CE): Minimal relationship

### Seshat: Religion Shows Counterintuitive Effects
Total religious institutionalization associates with shorter duration (HR = 1.58, p < 0.001 after FDR). More religion correlates with shorter polity lifespan.

### Seshat: Infant Mortality Pattern
Weibull survival analysis reveals shape parameter rho = 0.48, indicating decreasing hazard over time. Polities face highest collapse risk in their early decades.

### CrisisDB: Elite Overproduction Signal
Each additional administrative level associates with +5.6 percentage points higher intra-elite conflict rate during power transitions. Consistent with Turchin's Structural Demographic Theory.

### CrisisDB: Violence Cascades
Rulers who seize power violently are 2.7x more likely to be removed violently. The system converges to 36% violent transitions at equilibrium.

## Data Sources

**Seshat Global History Databank** (Equinox 2022)
- 256 polities after filtering
- Timeline: 3000 BCE to 1900 CE
- 16 features across complexity, warfare, and religion

**CrisisDB Power Transitions**
- 3,447 transitions from 264 polities
- Merged with Seshat complexity metrics
- Subset with 5+ transitions per polity: 87 polities

## Notebooks

### Seshat Analysis
| Notebook | Purpose |
|----------|---------|
| 04_equinox_replication | Era clustering discovery |
| 05_warfare_integration | Warfare mechanism |
| 06_religion_integration | Religion mechanism |
| 07_production_deployment | Final model |
| 09_survival_analysis | Cox PH survival |
| 10_fdr_correction | Statistical correction |
| 11_methodology_fixes | Data leakage fix, Weibull |

### CrisisDB Analysis
| Notebook | Purpose |
|----------|---------|
| 01_explore | Initial data exploration |
| 02_elite_overproduction | Complexity-conflict correlation |
| 03_violence_contagion | Markov chain analysis |
| 04_ruler_tenure | Reign length by accession type |

## Limitations

- Sample sizes are small (256 and 87 polities for key analyses)
- Selection bias toward well-documented societies
- Correlation does not imply causation
- Temporal holdout shows weak era generalization (AUC 0.57)
- Polity duration is an imperfect proxy for stability

## Getting Started

```bash
git clone https://github.com/TheApexWu/psychohistoryML.git
cd psychohistoryML
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Web Interface

Interactive explorer: https://amadeuswoo.com

- Seshat analysis: /discover, /research
- CrisisDB analysis: /crisisdb

## Acknowledgments

Data from the Seshat Global History Databank and CrisisDB, maintained by the Complexity Science Hub Vienna. Theory builds on Peter Turchin's cliodynamics and Structural Demographic Theory.

## Author

@theapexwu
