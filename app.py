import streamlit as st
import numpy as np
import joblib
import os

# -----------------------------------------
# App Config
# -----------------------------------------
st.set_page_config(
    page_title="Water Potability Predictor",
    page_icon="💧",
    layout="centered",
)

# -----------------------------------------
# Title / Header
# -----------------------------------------
st.markdown(
    """
    <h2 style="text-align:center; color:#1f77b4;">
        💧 Water Potability Prediction App
    </h2>
    <p style="text-align:center; font-size:18px;">
        Enter water quality parameters to check if water is potable.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------
# Load Model
# -----------------------------------------
MODEL_PATH = "models_improved/RandomForest.pkl"   # CHANGE IF REQUIRED
model = joblib.load(MODEL_PATH)

# Sidebar
st.sidebar.title("⚙️ App Settings")
st.sidebar.success(f"Loaded Model: `{os.path.basename(MODEL_PATH)}`")
st.sidebar.write("Modify input parameters on the main screen.")


# -----------------------------------------
# Input Form
# -----------------------------------------
st.markdown("### 🧪 Enter Parameters")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
    solids = st.number_input("Solids (ppm)", 0.0, 60000.0, 20000.0)
    chloramines = st.number_input("Chloramines", 0.0, 15.0, 7.0)

with col2:
    sulfate = st.number_input("Sulfate", 0.0, 600.0, 200.0)
    conductivity = st.number_input("Conductivity", 0.0, 800.0, 300.0)
    organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 10.0)
    trihalomethanes = st.number_input("Trihalomethanes", 0.0, 150.0, 60.0)
    turbidity = st.number_input("Turbidity", 0.0, 10.0, 3.0)


# -----------------------------------------
# Prediction Button
# -----------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Potability", use_container_width=True):
    X = np.array([[ph, hardness, solids, chloramines, sulfate,
                   conductivity, organic_carbon, trihalomethanes, turbidity]])

    pred = model.predict(X)[0]

    if pred == 1:
        st.markdown(
            """
            <div style="padding:20px; border-radius:10px; background:#d4edda; border-left:6px solid #28a745;">
                <h3 style="color:#155724;">✅ Water is POTABLE</h3>
                <p>The water quality meets the safety standard.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="padding:20px; border-radius:10px; background:#f8d7da; border-left:6px solid #dc3545;">
                <h3 style="color:#721c24;">❌ Water is NOT POTABLE</h3>
                <p>The water quality does NOT meet the potability criteria.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
