
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Beverage Nutrition Predictor", page_icon="☕")

st.title("☕ Beverage Nutrition Predictor")
st.write("Starbucks beverage nutrition data using Decision Tree")

MODEL_PATH = Path(__file__).parent / "model.pkl"

try:
    model = joblib.load(MODEL_PATH)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# Inspect model inputs
st.subheader("Model Information")

if hasattr(model, "feature_names_in_"):
    features = list(model.feature_names_in_)
    st.write("Model input features:", features)
else:
    st.warning(
        "Model does not contain feature names. "
        "We need the original training code to confirm input order."
    )
    st.write("Expected number of features:", model.n_features_in_)
    st.stop()

st.write("Number of features:", len(features))

# These are the columns from your dataset
numeric_features = [
    "Calories",
    " Total Fat (g)",
    "Trans Fat (g) ",
    "Saturated Fat (g)",
    " Sodium (mg)",
    " Total Carbohydrates (g) ",
    "Cholesterol (mg)",
    " Dietary Fibre (g)",
    " Sugars (g)",
    " Protein (g) ",
    "Vitamin A (% DV) ",
    "Vitamin C (% DV)",
    " Calcium (% DV) ",
    "Iron (% DV) ",
    "Caffeine (mg)",
]

beverage_categories = [
    "Coffee",
    "Classic Espresso Drinks",
    "Signature Espresso Drinks",
    "Tazo Tea Drinks",
    "Shaken Iced Beverages",
    "Frappuccino Blended Coffee",
    "Frappuccino Light Blended Coffee",
    "Frappuccino Blended Crème",
]

beverage_names = [
    "Brewed Coffee",
    "Caffè Latte",
    "Cappuccino",
    "Caramel Macchiato",
    "Mocha",
    "White Chocolate Mocha",
    "Espresso",
    "Other",
]

beverage_preps = [
    "Short",
    "Tall",
    "Grande",
    "Venti",
    "Short Nonfat Milk",
    "2% Milk",
    "Whole Milk",
    "Soymilk",
    "Other",
]

st.subheader("Enter Beverage Information")

with st.form("prediction_form"):
    values = {}

    for feature in features:
        if feature == "Beverage_category":
            values[feature] = st.selectbox(
                feature, beverage_categories
            )
        elif feature == "Beverage":
            values[feature] = st.selectbox(
                feature, beverage_names
            )
        elif feature == "Beverage_prep":
            values[feature] = st.selectbox(
                feature, beverage_preps
            )
        else:
            values[feature] = st.number_input(
                feature,
                min_value=0.0,
                value=0.0,
                step=1.0
            )

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        input_df = pd.DataFrame([values], columns=features)
        prediction = model.predict(input_df)

        st.subheader("Prediction Result")
        st.success(f"Predicted value: {prediction[0]:.2f}")

    except Exception as e:
        st.error("Prediction failed")
        st.exception(e)
