import streamlit as st
import joblib
import numpy as np

st.title("Instagram Reach Prediction")

try:
    model = joblib.load("instagram_model.pkl")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

try:
    scaler = joblib.load("scaler.pkl")
    st.success("✅ Scaler loaded successfully")
except Exception as e:
    st.error(f"Scaler loading failed: {e}")
    st.stop()