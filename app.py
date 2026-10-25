
import streamlit as st
import pickle
import sklearn

st.title("Starbucks Drink Calories Predictor")

st.write("Scikit-learn version:", sklearn.__version__)

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    st.success("Model loaded successfully!")

    if hasattr(model, "feature_names_in_"):
        st.subheader("Model input features")
        st.write(list(model.feature_names_in_))
    elif hasattr(model, "n_features_in_"):
        st.write("Expected number of input features:", model.n_features_in_)
    else:
        st.warning("Model input features could not be detected automatically.")

except Exception as e:
    st.error(f"Model error: {e}")
