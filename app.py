import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config( page_title="Insurance Premium Predictor", page_icon="💰", layout="wide" )



# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Insurance Premium Predictor")

st.title("Insurance Premium Predictor")

st.write("Enter your details below:")



# Inputs

st.markdown("### Personal Details")

col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 18, 100)
    height = st.number_input("Height (cm)", 100, 220)
    weight = st.number_input("Weight (kg)", 30, 150)

with col2:
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    bp = st.selectbox("Blood Pressure Problems", ["No", "Yes"])
    chronic = st.selectbox("Chronic Diseases", ["No", "Yes"])

st.markdown("### Medical History")

col3, col4 = st.columns(2)
with col3:
    transplants = st.selectbox("Any Transplants", ["No", "Yes"])
    allergies = st.selectbox("Known Allergies", ["No", "Yes"])

with col4:
    cancer = st.selectbox("Cancer History in Family", ["No", "Yes"])
    surgeries = st.slider("Number of Major Surgeries", 0, 5)

# Convert Yes/No to 0/1
if st.button("Predict Premium"):

    # Convert Yes/No to 0/1
    diabetes = 1 if diabetes == "Yes" else 0
    bp = 1 if bp == "Yes" else 0
    transplants = 1 if transplants == "Yes" else 0
    chronic = 1 if chronic == "Yes" else 0
    allergies = 1 if allergies == "Yes" else 0
    cancer = 1 if cancer == "Yes" else 0

    # BMI calculation
    bmi = weight / ((height / 100) ** 2)

    # Create DataFrame (correct format)
    input_data = pd.DataFrame([{
        'Age': age,
        'Diabetes': diabetes,
        'BloodPressureProblems': bp,
        'AnyTransplants': transplants,
        'AnyChronicDiseases': chronic,
        'Height': height,
        'Weight': weight,
        'KnownAllergies': allergies,
        'HistoryOfCancerInFamily': cancer,
        'NumberOfMajorSurgeries': surgeries,
        'BMI': bmi
    }])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Prediction interval
    lower = prediction - 4000
    upper = prediction + 4000

   #OUTPUT#

    st.markdown("## Prediction Result")

    col5, col6 = st.columns(2)

    with col5:
        st.metric("Estimated Premium", f"Rs {int(prediction)}")

    with col6:
        st.metric("Expected Range", f"Rs {int(lower)} - Rs {int(upper)}")
