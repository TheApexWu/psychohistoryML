import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def robust_pca(wide_df: pd.DataFrame,
               n_components: int = 3,
               min_col_cov: float = 0.6,
               min_row_cov: float = 0.6):
    tbl = wide_df.copy()
    tbl = tbl.loc[:, tbl.notna().mean() >= min_col_cov]
    tbl = tbl.loc[tbl.notna().mean(axis=1) >= min_row_cov]

    X = SimpleImputer(strategy="median").fit_transform(tbl)
    X = StandardScaler().fit_transform(X)

    ncomp = int(min(n_components, X.shape[1]))
    pca = PCA(n_components=ncomp).fit(X)
    scores = pd.DataFrame(pca.transform(X), index=tbl.index,
                          columns=[f"PC{i+1}" for i in range(ncomp)])
    loadings = pd.DataFrame(pca.components_.T, index=tbl.columns,
                            columns=[f"PC{i+1}" for i in range(ncomp)])
    return pca, scores, loadings
