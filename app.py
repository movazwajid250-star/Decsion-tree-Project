
import streamlit as st
import sys
import subprocess
from pathlib import Path
import pickle
import joblib

st.title("Decision Tree Model App")

st.write("Python version:", sys.version)

# Check installed packages
result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "scikit-learn"],
    capture_output=True,
    text=True
)

st.subheader("Scikit-learn package check")
st.code(result.stdout or result.stderr)

# Find model file
MODEL_PATH = Path(__file__).parent / "model.pkl"

st.subheader("Model file check")
st.write("File exists:", MODEL_PATH.exists())

if MODEL_PATH.exists():
    st.write("File size:", MODEL_PATH.stat().st_size, "bytes")

    model = None

    # Try joblib first
    try:
        model = joblib.load(MODEL_PATH)
        st.success("Model loaded using joblib!")

    except Exception as e:
        st.warning(f"Joblib loading failed: {e}")

        # Try pickle
        try:
            with open(MODEL_PATH, "rb") as file:
                model = pickle.load(file)

            st.success("Model loaded using pickle!")

        except Exception as e2:
            st.error("Model could not be loaded.")
            st.exception(e2)

    if model is not None:
        st.write("Model type:", type(model).__name__)

else:
    st.error("model.pkl file not found")
