
import streamlit as st
import sys
import subprocess
from pathlib import Path
import pickle

st.title("Model Deployment Test")

st.write("Python version:", sys.version)

# Check installed scikit-learn version
result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "scikit-learn"],
    capture_output=True,
    text=True
)

st.subheader("Scikit-learn package check")
st.code(result.stdout or result.stderr)

if result.returncode == 0:
    st.success("scikit-learn is installed")
else:
    st.error("scikit-learn is not installed")

# Check model file
MODEL_PATH = Path(__file__).parent / "model.pkl"

st.subheader("Model file check")
st.write("Model file exists:", MODEL_PATH.exists())

if MODEL_PATH.exists():
    st.write("Model file size:", MODEL_PATH.stat().st_size, "bytes")

    try:
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)

        st.success("Model loaded successfully!")
        st.write("Model type:", type(model).__name__)

    except Exception as e:
        st.error("Model loading failed")
        st.exception(e)
else:
    st.error("model.pkl file not found")
