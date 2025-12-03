
import joblib
import numpy as np
import pandas as pd

class PsychohistoryMLPredictor:
    """Production model for civilizational survival prediction."""
    
    def __init__(self, model_dir="production/models"):
        self.scaler = joblib.load(f"{model_dir}/scaler.pkl")
        self.classifier = joblib.load(f"{model_dir}/best_classifier.pkl")
        self.regressor = joblib.load(f"{model_dir}/best_regressor.pkl")
        
        # Feature names for reference
        self.features = ['PC1_hier', 'PC2_hier', 'PC3_hier', 'PC1_squared', 'PC1_x_PC2', 'total_warfare_tech', 'weapons_count', 'armor_count', 'cavalry_count', 'fortification_count', 'material_count', 'advanced_tech_count', 'moral_score', 'legit_score', 'ideol_score', 'total_rel']
        
    def predict_instability(self, X):
        """Predict probability of civilizational instability."""
        X_scaled = self.scaler.transform(X)
        return self.classifier.predict_proba(X_scaled)[:, 1]
    
    def predict_duration(self, X):
        """Predict civilizational duration in years."""
        X_scaled = self.scaler.transform(X)
        return self.regressor.predict(X_scaled)
    
    def predict_both(self, X):
        """Predict both instability probability and duration."""
        return {
            'instability_prob': self.predict_instability(X),
            'predicted_duration': self.predict_duration(X)
        }

# Example usage:
# predictor = PsychohistoryMLPredictor()
# sample_data = np.array([[0.5, -0.2, 0.1, 0.0, 0.0, 5.0, 3.0, 2.0, 1.0, 8.0, 1.0, 3.0, 12.0]])
# predictions = predictor.predict_both(sample_data)
