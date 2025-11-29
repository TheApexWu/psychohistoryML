#!/usr/bin/env python3
"""Generate all 7 production models for Notebook 07 deployment."""

import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, mean_absolute_error, accuracy_score, roc_auc_score, f1_score

try:
    from xgboost import XGBRegressor, XGBClassifier
    HAS_XGBOOST = True
except:
    HAS_XGBOOST = False

# Load data
print("="*60)
print("LOADING DATA")
print("="*60)
BASE_DIR = Path(__file__).resolve().parents[1]    # project root
CSV_PATH = BASE_DIR / "notebooks" / "models" / "equinox_with_religion.csv"
df = pd.read_csv(CSV_PATH, index_col=0)
print(f"✓ Loaded {len(df)} polities\n")

# Prepare features
features = [
    'PC1_hier', 'PC2_hier', 'PC3_hier', 'PC1_squared', 'PC1_x_PC2',
    'total_warfare_tech', 'weapons_count', 'armor_count', 'cavalry_count',
    'moral_score', 'legit_score', 'ideol_score'
]

data = df[features + ['duration_years', 'collapsed']].dropna()
X = data[features].values
y_dur = data['duration_years'].values
y_col = data['collapsed'].values

print(f"Dataset: {len(data)} polities, {len(features)} features")
print(f"Collapse rate: {y_col.mean():.1%}\n")

# Split
X_tr, X_te, y_dur_tr, y_dur_te, y_col_tr, y_col_te = train_test_split(
    X, y_dur, y_col, test_size=0.2, random_state=42, stratify=y_col
)
print(f"Train: {len(X_tr)} | Test: {len(X_te)}\n")

# Standardize
scaler = StandardScaler().fit(X_tr)
X_tr_s = scaler.transform(X_tr)
X_te_s = scaler.transform(X_te)

# Create directories
out_dir = BASE_DIR / "production" / "models"
cfg_dir = BASE_DIR / "production" / "configs"
out_dir.mkdir(parents=True, exist_ok=True)
cfg_dir.mkdir(parents=True, exist_ok=True)

# Save scaler
joblib.dump(scaler, out_dir / 'scaler.pkl')
print(f"✓ Saved: scaler.pkl")

# REGRESSION MODELS
print("\n" + "="*60)
print("REGRESSION MODELS (Duration Prediction)")
print("="*60)

# 1. Linear Regression
lr = LinearRegression().fit(X_tr_s, y_dur_tr)
lr_r2 = r2_score(y_dur_te, lr.predict(X_te_s))
lr_mae = mean_absolute_error(y_dur_te, lr.predict(X_te_s))
joblib.dump(lr, out_dir / 'linear_regressor.pkl')
print(f"✓ Linear Regression: R²={lr_r2:.3f}, MAE={lr_mae:.1f}y")

# 2. Random Forest Regressor
rfr = RandomForestRegressor(
    n_estimators=100, max_depth=7, random_state=42, n_jobs=-1
).fit(X_tr_s, y_dur_tr)
rfr_r2 = r2_score(y_dur_te, rfr.predict(X_te_s))
rfr_mae = mean_absolute_error(y_dur_te, rfr.predict(X_te_s))
joblib.dump(rfr, out_dir / 'random_forest_regressor.pkl')
print(f"✓ Random Forest Reg: R²={rfr_r2:.3f}, MAE={rfr_mae:.1f}y")

# 3. XGBoost Regressor (optional)
if HAS_XGBOOST:
    xgbr = XGBRegressor(
        n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42
    ).fit(X_tr_s, y_dur_tr)
    xgbr_r2 = r2_score(y_dur_te, xgbr.predict(X_te_s))
    xgbr_mae = mean_absolute_error(y_dur_te, xgbr.predict(X_te_s))
    joblib.dump(xgbr, out_dir / 'xgboost_regressor.pkl')
    print(f"✓ XGBoost Reg: R²={xgbr_r2:.3f}, MAE={xgbr_mae:.1f}y")
else:
    print(f"○ XGBoost Reg: Not installed (pip install xgboost)")

# CLASSIFICATION MODELS
print("\n" + "="*60)
print("CLASSIFICATION MODELS (Collapse Prediction)")
print("="*60)

# 4. Logistic Regression
log = LogisticRegression(
    max_iter=1000, random_state=42, class_weight='balanced'
).fit(X_tr_s, y_col_tr)
log_auc = roc_auc_score(y_col_te, log.predict_proba(X_te_s)[:, 1])
log_f1 = f1_score(y_col_te, log.predict(X_te_s))
joblib.dump(log, out_dir / 'logistic_classifier.pkl')
print(f"✓ Logistic: AUC={log_auc:.3f}, F1={log_f1:.3f}")

# 5. Random Forest Classifier
rfc = RandomForestClassifier(
    n_estimators=100, max_depth=5, random_state=42, 
    class_weight='balanced', n_jobs=-1
).fit(X_tr_s, y_col_tr)
rfc_auc = roc_auc_score(y_col_te, rfc.predict_proba(X_te_s)[:, 1])
rfc_f1 = f1_score(y_col_te, rfc.predict(X_te_s))
joblib.dump(rfc, out_dir / 'random_forest_classifier.pkl')
print(f"✓ Random Forest Clf: AUC={rfc_auc:.3f}, F1={rfc_f1:.3f}")

# 6. XGBoost Classifier (optional)
if HAS_XGBOOST:
    scale_pos = (y_col_tr == 0).sum() / (y_col_tr == 1).sum()
    xgbc = XGBClassifier(
        n_estimators=100, max_depth=4, learning_rate=0.1,
        random_state=42, scale_pos_weight=scale_pos
    ).fit(X_tr_s, y_col_tr)
    xgbc_auc = roc_auc_score(y_col_te, xgbc.predict_proba(X_te_s)[:, 1])
    xgbc_f1 = f1_score(y_col_te, xgbc.predict(X_te_s))
    joblib.dump(xgbc, out_dir / 'xgboost_classifier.pkl')
    print(f"✓ XGBoost Clf: AUC={xgbc_auc:.3f}, F1={xgbc_f1:.3f}")
else:
    print(f"○ XGBoost Clf: Not installed")

# Save config
config = {
    'version': '1.0.0',
    'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'dataset': {
        'name': 'Seshat Equinox 2022 + Religion',
        'n_polities': len(data),
        'n_features': len(features),
        'features': features
    },
    'training': {
        'train_size': len(X_tr),
        'test_size': len(X_te),
        'test_split': 0.2,
        'random_state': 42
    },
    'champion_models': {
        'regressor': {
            'name': 'random_forest' if rfr_r2 >= lr_r2 else 'linear',
            'test_r2': float(max(rfr_r2, lr_r2)),
            'test_mae': float(rfr_mae if rfr_r2 >= lr_r2 else lr_mae)
        },
        'classifier': {
            'name': 'random_forest' if rfc_auc >= log_auc else 'logistic',
            'test_auc': float(max(rfc_auc, log_auc)),
            'test_f1': float(rfc_f1 if rfc_auc >= log_auc else log_f1)
        }
    }
}

with open(cfg_dir / 'model_config.json', 'w') as f:
    json.dump(config, f, indent=2)

# Verify
print("\n" + "="*60)
print("VERIFICATION")
print("="*60)

required = [
    'scaler.pkl',
    'linear_regressor.pkl', 'random_forest_regressor.pkl',
    'logistic_classifier.pkl', 'random_forest_classifier.pkl'
]
optional = ['xgboost_regressor.pkl', 'xgboost_classifier.pkl']

print("\nRequired models:")
for f in required:
    path = out_dir / f
    print(f"  ✓ {f} ({path.stat().st_size / 1024:.1f} KB)")

print("\nOptional models:")
for f in optional:
    path = out_dir / f
    if path.exists():
        print(f"  ✓ {f} ({path.stat().st_size / 1024:.1f} KB)")
    else:
        print(f"  ○ {f} (not installed)")

total = len(required) + sum((out_dir / f).exists() for f in optional)
print(f"\nTotal: {total}/7 models")
print(f"Location: {out_dir.absolute()}")
print(f"Config: {cfg_dir.absolute()}/model_config.json")

print("\n" + "="*60)
print("READY FOR NOTEBOOK 07")
print("="*60)