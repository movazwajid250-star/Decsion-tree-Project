import sys
import subprocess
import streamlit as st
import sys

st.title("Decision Tree Model")
st.write("Python version:", sys.version)
st.write("Python version:", sys.version)
result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "scikit-learn"],
    capture_output=True,
    text=True
)
st.code(result.stdout or result.stderr)
import streamlit as st
import pickle
import numpy as np
import traceback

st.title("Decision Tree Prediction App")

try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception:
    st.error("Model load nahi ho saka. Asal error:")
    st.code(traceback.format_exc())
    st.stop()

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
