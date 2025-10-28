import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def plot_timeline(df, label_col, start_col, end_col, color_col=None,
                  year_min=None, year_max=None, title="Polity Longevity",
                  out_path: Path | None = None):
    d = df.dropna(subset=[start_col, end_col]).copy()
    if year_min is not None:
        d = d[d[end_col] >= year_min]
    if year_max is not None:
        d = d[d[start_col] <= year_max]
    d = d.sort_values(start_col)

    y = np.arange(len(d))
    fig_h = max(8, 0.28 * len(d))
    fig, ax = plt.subplots(figsize=(12, fig_h))

    if color_col and d[color_col].notna().any():
        vals = d[color_col]
        lo, hi = np.nanpercentile(vals, 5), np.nanpercentile(vals, 95)
        norm = (vals.clip(lo, hi) - lo) / (hi - lo + 1e-9)
        cmap = plt.cm.viridis
        for i, (s, e, c) in enumerate(zip(d[start_col], d[end_col], norm)):
            ax.hlines(i, max(s, year_min or -1e9), min(e, year_max or 1e9),
                      colors=cmap(float(c)), linewidth=2.2)
        sm = plt.cm.ScalarMappable(cmap=cmap); sm.set_array(vals)
        fig.colorbar(sm, ax=ax).set_label(color_col)
    else:
        for i, (s, e) in enumerate(zip(d[start_col], d[end_col])):
            ax.hlines(i, s, e, linewidth=2.2)

    ax.set_yticks(y)
    ax.set_yticklabels(d[label_col], fontsize=8)
    if year_min is not None and year_max is not None:
        ax.set_xlim(year_min, year_max)
    ax.set_xlabel("Year (BCE negative → CE positive)")
    ax.set_title(title)
    plt.tight_layout()
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.show()
