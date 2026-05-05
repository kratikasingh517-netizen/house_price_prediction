import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter house details:")

# Inputs
area = st.number_input("Living Area (sq ft)", min_value=500, max_value=5000, step=50)
quality = st.slider("Overall Quality", 1, 10)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, step=1)
garage = st.number_input("Garage Capacity", min_value=0, max_value=5, step=1)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[area, quality, bathrooms, garage]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Price: ₹ {round(prediction[0], 2)}")