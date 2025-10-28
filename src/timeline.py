import pandas as pd
import numpy as np

def to_year(x):
    if pd.isna(x):
        return np.nan
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).lower()
    digs = "".join(ch for ch in s if ch.isdigit() or ch in "+-")
    if not digs:
        return np.nan
    val = float(digs)
    return -abs(val) if "bce" in s else val

def estimate_timeline(df: pd.DataFrame) -> pd.DataFrame:
    cand_from = [c for c in df.columns if "date" in c.lower() and "from" in c.lower()]
    cand_to   = [c for c in df.columns if "date" in c.lower() and "to" in c.lower()]
    if cand_from and cand_to:
        d = df.copy()
        d["DateFrom_num"] = d[cand_from[0]].map(to_year)
        d["DateTo_num"]   = d[cand_to[0]].map(to_year)
        tl = (d.groupby("PolityKey")
                .agg(start_year_est=("DateFrom_num","min"),
                     end_year_est=("DateTo_num","max"))
                .dropna()
                .reset_index())
    elif "Year" in df.columns:
        tmp = df.groupby("PolityKey")["Year"].agg(["min","max"])
        tl = tmp.rename(columns={"min":"start_year_est","max":"end_year_est"}).reset_index()
    else:
        raise ValueError("No suitable date columns found.")
    tl["duration_years_est"] = tl["end_year_est"] - tl["start_year_est"]
    tl = tl[tl["duration_years_est"] > 0]
    return tl
