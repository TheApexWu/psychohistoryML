from __future__ import annotations
from pathlib import Path
import pandas as pd

def _default_sc_path(root: Path) -> Path:
    # Try common names in data/
    candidates = list((root / "data").glob("sc_dataset*.xlsx"))
    if not candidates:
        raise FileNotFoundError("Could not find sc_dataset*.xlsx in data/")
    return candidates[0]

def load_social_complexity(path: str | Path | None = None, sheet: str = "exportdat_share",  root: Path | None = None) -> pd.DataFrame:
    """
    Load Seshat Social Complexity XLSX from data/.
    If path is None, the first sc_dataset*.xlsx in data/ is used.
    """
    root = root or Path(__file__).resolve().parents[1]
    p = Path(path) if path else _default_sc_path(root)
    df = pd.read_excel(p, sheet_name=sheet, engine="openpyxl")
    if {"NGA", "Polity"}.issubset(df.columns):
        df["PolityKey"] = df["NGA"].astype(str) + " | " + df["Polity"].astype(str)
    return df
