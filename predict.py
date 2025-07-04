import joblib
import numpy as np

model = joblib.load('models/flood_model.pkl')

def predict_flood(features):
    prediction = model.predict([features])
    return 'Flood Risk' if prediction[0] == 1 else 'No Flood Risk'
