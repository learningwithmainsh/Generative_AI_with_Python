# Import required modules
import streamlit as st
import pickle
import numpy as np

# Title
st.title("House Price Predictor")

# User Inputs
area = st.number_input("Enter the area (sq ft):", 500, 10000)
rooms = st.slider("Number of rooms:", 1, 10)

# Load the model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Predict the Price
if st.button("Predict the Price"):
    features = np.array([[area, rooms]])
    prediction = model.predict(features)
    st.subheader(f"Predicted price: ${prediction[0]:,.2f}")