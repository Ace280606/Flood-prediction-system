import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load data
df = pd.read_csv('../data/weather_data.csv')

# Features and target
X = df.drop('flood', axis=1)
y = df['flood']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs('../models', exist_ok=True)
joblib.dump(model, '../models/flood_model.pkl')
print("Model trained and saved to models/flood_model.pkl")
