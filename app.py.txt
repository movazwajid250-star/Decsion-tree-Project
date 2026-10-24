
import streamlit as st
import pickle
import numpy as np

st.title("Decision Tree Prediction App")

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.write("Apni input features enter karein")

# Example: 4 input features
f1 = st.number_input("Feature 1", value=0.0)
f2 = st.number_input("Feature 2", value=0.0)
f3 = st.number_input("Feature 3", value=0.0)
f4 = st.number_input("Feature 4", value=0.0)

if st.button("Predict"):
    data = np.array([[f1, f2, f3, f4]])
    prediction = model.predict(data)
    st.success(f"Prediction: {prediction[0]}")
