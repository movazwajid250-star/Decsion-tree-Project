
import streamlit as st
import sys
import subprocess

st.title("Dependency Test")
st.write("Python:", sys.version)

result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "scikit-learn"],
    capture_output=True,
    text=True
)

st.write("Package check:")
st.code(result.stdout or result.stderr)

if result.returncode == 0:
    st.success("scikit-learn is installed")
else:
    st.error("scikit-learn is NOT installed")
