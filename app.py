import streamlit as st
from src.predict import predict_flood

st.title("🌊 AI Flood Prediction System")

rainfall = st.slider("Rainfall (mm)", 0, 300, 100)
temperature = st.slider("Temperature (°C)", 10, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 70)
river_level = st.slider("River Level (m)", 0.0, 10.0, 3.0)

if st.button("Predict"):
    features = [rainfall, temperature, humidity, river_level]
    result = predict_flood(features)
    st.subheader(f"🚨 Prediction: {result}")
