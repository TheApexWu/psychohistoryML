#!/usr/bin/env python3
"""
Generate all production models from NB06 dataset.
Run this script to create all required .pkl files for deployment.

Usage:
    python generate_models.py

Output:
    production/models/
    ├── scaler.pkl
    ├── linear_regressor.pkl
    ├── random_forest_regressor.pkl
    ├── xgboost_regressor.pkl (optional)
    ├── logistic_classifier.pkl
    ├── random_forest_classifier.pkl
    └── xgboost_classifier.pkl (optional)
"""

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
from sklearn.metrics import (
    r2_score, mean_absolute_error,
    accuracy_score, roc_auc_score, f1_score
)

# Try XGBoost (optional)
try:
    from xgboost import XGBRegressor, XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
    print("⚠️  XGBoost not installed (optional). Install: pip install xgboost")


def load_data():
    """Load NB06 dataset with religion features."""
    print("="*80)
    print("LOADING DATA")
    print("="*80)
    
    # Try to load from models/ or current directory
    possible_paths = [
        'models/equinox_with_religion.csv',
        'equinox_with_religion.csv',
        '../models/equinox_with_religion.csv'
    ]
    
    df = None
    for path in possible_paths:
        if Path(path).exists():
            df = pd.read_csv(path, index_col=0)
            print(f"✓ Loaded: {path}")
            break
    
    if df is None:
        raise FileNotFoundError(
            "Could not find equinox_with_religion.csv\n"
            "Please run this script from your project root directory."
        )
    
    return df


def prepare_features(df):
    """Extract features and targets, drop NaN."""
    print("\n" + "="*80)
    print("PREPARING FEATURES")
    print("="*80)
    
    feature_cols = [
        'PC1_hier', 'PC2_hier', 'PC3_hier', 'PC1_squared', 'PC1_x_PC2',
        'total_warfare_tech', 'weapons_count', 'armor_count', 'cavalry_count',
        'moral_score', 'legit_score', 'ideol_score'
    ]
    
    # Check if all columns exist
    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Clean dataset
    modeling_df = df[feature_cols + ['duration_years', 'collapsed']].dropna().copy()
    
    print(f"Dataset: {len(modeling_df)} polities")
    print(f"Features: {len(feature_cols)}")
    print(f"Collapse rate: {modeling_df['collapsed'].mean():.1%}")
    
    return modeling_df, feature_cols


def split_data(modeling_df, feature_cols):
    """Train-test split."""
    print("\n" + "="*80)
    print("TRAIN-TEST SPLIT")
    print("="*80)
    
    X = modeling_df[feature_cols].values
    y_duration = modeling_df['duration_years'].values
    y_collapse = modeling_df['collapsed'].values
    
    X_train, X_test, y_dur_train, y_dur_test, y_col_train, y_col_test = train_test_split(
        X, y_duration, y_collapse,
        test_size=0.2,
        random_state=42,
        stratify=y_collapse
    )
    
    print(f"Train: {len(X_train)} polities ({len(X_train)/len(X)*100:.1f}%)")
    print(f"Test: {len(X_test)} polities ({len(X_test)/len(X)*100:.1f}%)")
    print(f"Train collapse rate: {y_col_train.mean():.1%}")
    print(f"Test collapse rate: {y_col_test.mean():.1%}")
    
    return X_train, X_test, y_dur_train, y_dur_test, y_col_train, y_col_test


def standardize_features(X_train, X_test):
    """Fit scaler and transform."""
    print("\n" + "="*80)
    print("STANDARDIZING FEATURES")
    print("="*80)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Scaler fitted on {len(X_train)} samples")
    print(f"Mean (first 3): {scaler.mean_[:3]}")
    print(f"Scale (first 3): {scaler.scale_[:3]}")
    
    # Save scaler
    Path("production/models").mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, 'production/models/scaler.pkl')
    print("\n✓ Saved: production/models/scaler.pkl")
    
    return scaler, X_train_scaled, X_test_scaled


def train_regression_models(X_train_scaled, X_test_scaled, y_dur_train, y_dur_test):
    """Train and save all regression models."""
    print("\n" + "="*80)
    print("REGRESSION MODELS (Duration Prediction)")
    print("="*80)
    
    models = {}
    results = []
    
    # 1. Linear Regression
    print("\n1. Linear Regression")
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_dur_train)
    
    train_r2 = r2_score(y_dur_train, lr.predict(X_train_scaled))
    test_r2 = r2_score(y_dur_test, lr.predict(X_test_scaled))
    test_mae = mean_absolute_error(y_dur_test, lr.predict(X_test_scaled))
    
    print(f"   Train R²: {train_r2:.3f}")
    print(f"   Test R²: {test_r2:.3f}")
    print(f"   Test MAE: {test_mae:.1f} years")
    
    joblib.dump(lr, 'production/models/linear_regressor.pkl')
    print("   ✓ Saved: linear_regressor.pkl")
    
    models['linear'] = lr
    results.append({
        'model': 'Linear Regression',
        'train_r2': train_r2,
        'test_r2': test_r2,
        'test_mae': test_mae
    })
    
    # 2. Random Forest
    print("\n2. Random Forest Regressor")
    rfr = RandomForestRegressor(
        n_estimators=100,
        max_depth=7,
        random_state=42,
        n_jobs=-1
    )
    rfr.fit(X_train_scaled, y_dur_train)
    
    train_r2 = r2_score(y_dur_train, rfr.predict(X_train_scaled))
    test_r2 = r2_score(y_dur_test, rfr.predict(X_test_scaled))
    test_mae = mean_absolute_error(y_dur_test, rfr.predict(X_test_scaled))
    
    print(f"   Train R²: {train_r2:.3f}")
    print(f"   Test R²: {test_r2:.3f}")
    print(f"   Test MAE: {test_mae:.1f} years")
    
    joblib.dump(rfr, 'production/models/random_forest_regressor.pkl')
    print("   ✓ Saved: random_forest_regressor.pkl")
    
    models['random_forest'] = rfr
    results.append({
        'model': 'Random Forest',
        'train_r2': train_r2,
        'test_r2': test_r2,
        'test_mae': test_mae
    })
    
    # 3. XGBoost (optional)
    if XGBOOST_AVAILABLE:
        print("\n3. XGBoost Regressor")
        xgbr = XGBRegressor(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            random_state=42
        )
        xgbr.fit(X_train_scaled, y_dur_train)
        
        train_r2 = r2_score(y_dur_train, xgbr.predict(X_train_scaled))
        test_r2 = r2_score(y_dur_test, xgbr.predict(X_test_scaled))
        test_mae = mean_absolute_error(y_dur_test, xgbr.predict(X_test_scaled))
        
        print(f"   Train R²: {train_r2:.3f}")
        print(f"   Test R²: {test_r2:.3f}")
        print(f"   Test MAE: {test_mae:.1f} years")
        
        joblib.dump(xgbr, 'production/models/xgboost_regressor.pkl')
        print("   ✓ Saved: xgboost_regressor.pkl")
        
        models['xgboost'] = xgbr
        results.append({
            'model': 'XGBoost',
            'train_r2': train_r2,
            'test_r2': test_r2,
            'test_mae': test_mae
        })
    
    return models, results


def train_classification_models(X_train_scaled, X_test_scaled, y_col_train, y_col_test):
    """Train and save all classification models."""
    print("\n" + "="*80)
    print("CLASSIFICATION MODELS (Collapse Prediction)")
    print("="*80)
    
    models = {}
    results = []
    
    # 1. Logistic Regression
    print("\n1. Logistic Regression")
    logreg = LogisticRegression(
        max_iter=1000,
        random_state=42,
        class_weight='balanced'
    )
    logreg.fit(X_train_scaled, y_col_train)
    
    train_acc = accuracy_score(y_col_train, logreg.predict(X_train_scaled))
    test_acc = accuracy_score(y_col_test, logreg.predict(X_test_scaled))
    test_auc = roc_auc_score(y_col_test, logreg.predict_proba(X_test_scaled)[:, 1])
    test_f1 = f1_score(y_col_test, logreg.predict(X_test_scaled))
    
    print(f"   Train Acc: {train_acc:.3f}")
    print(f"   Test Acc: {test_acc:.3f}")
    print(f"   Test AUC: {test_auc:.3f}")
    print(f"   Test F1: {test_f1:.3f}")
    
    joblib.dump(logreg, 'production/models/logistic_classifier.pkl')
    print("   ✓ Saved: logistic_classifier.pkl")
    
    models['logistic'] = logreg
    results.append({
        'model': 'Logistic Regression',
        'train_acc': train_acc,
        'test_acc': test_acc,
        'test_auc': test_auc,
        'test_f1': test_f1
    })
    
    # 2. Random Forest
    print("\n2. Random Forest Classifier")
    rfc = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight='balanced',
        n_jobs=-1
    )
    rfc.fit(X_train_scaled, y_col_train)
    
    train_acc = accuracy_score(y_col_train, rfc.predict(X_train_scaled))
    test_acc = accuracy_score(y_col_test, rfc.predict(X_test_scaled))
    test_auc = roc_auc_score(y_col_test, rfc.predict_proba(X_test_scaled)[:, 1])
    test_f1 = f1_score(y_col_test, rfc.predict(X_test_scaled))
    
    print(f"   Train Acc: {train_acc:.3f}")
    print(f"   Test Acc: {test_acc:.3f}")
    print(f"   Test AUC: {test_auc:.3f}")
    print(f"   Test F1: {test_f1:.3f}")
    
    joblib.dump(rfc, 'production/models/random_forest_classifier.pkl')
    print("   ✓ Saved: random_forest_classifier.pkl")
    
    models['random_forest'] = rfc
    results.append({
        'model': 'Random Forest',
        'train_acc': train_acc,
        'test_acc': test_acc,
        'test_auc': test_auc,
        'test_f1': test_f1
    })
    
    # 3. XGBoost (optional)
    if XGBOOST_AVAILABLE:
        print("\n3. XGBoost Classifier")
        scale_pos_weight = (y_col_train == 0).sum() / (y_col_train == 1).sum()
        
        xgbc = XGBClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
            scale_pos_weight=scale_pos_weight
        )
        xgbc.fit(X_train_scaled, y_col_train)
        
        train_acc = accuracy_score(y_col_train, xgbc.predict(X_train_scaled))
        test_acc = accuracy_score(y_col_test, xgbc.predict(X_test_scaled))
        test_auc = roc_auc_score(y_col_test, xgbc.predict_proba(X_test_scaled)[:, 1])
        test_f1 = f1_score(y_col_test, xgbc.predict(X_test_scaled))
        
        print(f"   Train Acc: {train_acc:.3f}")
        print(f"   Test Acc: {test_acc:.3f}")
        print(f"   Test AUC: {test_auc:.3f}")
        print(f"   Test F1: {test_f1:.3f}")
        
        joblib.dump(xgbc, 'production/models/xgboost_classifier.pkl')
        print("   ✓ Saved: xgboost_classifier.pkl")
        
        models['xgboost'] = xgbc
        results.append({
            'model': 'XGBoost',
            'train_acc': train_acc,
            'test_acc': test_acc,
            'test_auc': test_auc,
            'test_f1': test_f1
        })
    
    return models, results


def save_config(feature_cols, train_size, test_size):
    """Save model configuration."""
    print("\n" + "="*80)
    print("SAVING CONFIGURATION")
    print("="*80)
    
    config = {
        'version': '1.0.0',
        'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'dataset': {
            'name': 'Seshat Equinox 2022 + Religion',
            'features': feature_cols,
            'n_features': len(feature_cols)
        },
        'training': {
            'train_size': int(train_size),
            'test_size': int(test_size),
            'test_split': 0.2,
            'random_state': 42
        },
        'models': {
            'regression': [
                'linear_regressor.pkl',
                'random_forest_regressor.pkl',
                'xgboost_regressor.pkl'
            ],
            'classification': [
                'logistic_classifier.pkl',
                'random_forest_classifier.pkl',
                'xgboost_classifier.pkl'
            ]
        },
        'preprocessing': {
            'scaler': 'scaler.pkl',
            'method': 'StandardScaler'
        }
    }
    
    Path("production/configs").mkdir(parents=True, exist_ok=True)
    with open('production/configs/model_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✓ Saved: production/configs/model_config.json")


def verify_models():
    """Verify all models were saved."""
    print("\n" + "="*80)
    print("VERIFICATION")
    print("="*80)
    
    required_files = [
        'scaler.pkl',
        'linear_regressor.pkl',
        'random_forest_regressor.pkl',
        'logistic_classifier.pkl',
        'random_forest_classifier.pkl'
    ]
    
    optional_files = [
        'xgboost_regressor.pkl',
        'xgboost_classifier.pkl'
    ]
    
    print("\nRequired models:")
    for fname in required_files:
        path = Path(f'production/models/{fname}')
        exists = path.exists()
        status = "✓" if exists else "✗"
        size = f"({path.stat().st_size / 1024:.1f} KB)" if exists else ""
        print(f"  {status} {fname} {size}")
    
    print("\nOptional models:")
    for fname in optional_files:
        path = Path(f'production/models/{fname}')
        exists = path.exists()
        status = "✓" if exists else "○"
        size = f"({path.stat().st_size / 1024:.1f} KB)" if exists else "(not installed)"
        print(f"  {status} {fname} {size}")
    
    # Count
    required_count = sum(Path(f'production/models/{f}').exists() for f in required_files)
    optional_count = sum(Path(f'production/models/{f}').exists() for f in optional_files)
    
    print(f"\nTotal: {required_count}/5 required, {optional_count}/2 optional")
    
    if required_count == 5:
        print("\n SUCCESS! All required models saved.")
        return True
    else:
        print(f"\n  Missing {5 - required_count} required models.")
        return False


def main():
    """Main execution."""
    print("\n" + "="*80)
    print(" "*20 + "PRODUCTION MODEL GENERATOR")
    print("="*80)
    
    # Load data
    df = load_data()
    
    # Prepare features
    modeling_df, feature_cols = prepare_features(df)
    
    # Split data
    X_train, X_test, y_dur_train, y_dur_test, y_col_train, y_col_test = split_data(
        modeling_df, feature_cols
    )
    
    # Standardize
    scaler, X_train_scaled, X_test_scaled = standardize_features(X_train, X_test)
    
    # Train regression models
    reg_models, reg_results = train_regression_models(
        X_train_scaled, X_test_scaled, y_dur_train, y_dur_test
    )
    
    # Train classification models
    clf_models, clf_results = train_classification_models(
        X_train_scaled, X_test_scaled, y_col_train, y_col_test
    )
    
    # Save config
    save_config(feature_cols, len(X_train), len(X_test))
    
    # Verify
    success = verify_models()
    
    if success:
        print("\n" + "="*80)
        print("ALL MODELS GENERATED SUCCESSFULLY")
        print("="*80)
        print("\nNext steps:")
        print("1. Test loading: python -c 'import joblib; joblib.load(\"production/models/scaler.pkl\")'")
        print("2. Build simulator: streamlit run app.py")
        print("3. Deploy to production")
    
    return success


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
