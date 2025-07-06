# app/app.py

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and columns
model = joblib.load('../models/car_price_model.pkl')
model_columns = joblib.load('../models/model_columns.pkl')

st.title("🚗 Car Price Prediction App")

# Input form
company = st.selectbox("Company", ['Maruti', 'Hyundai', 'Ford', 'Toyota', 'Mahindra', 'Honda'])
year = st.number_input("Year of Manufacture", 1995, 2025, step=1)
kms_driven = st.number_input("Kilometers Driven", 0, 1000000, step=1000)
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])

# Predict button
if st.button("Predict Price"):
    # Create input dict
    input_data = {
        'year': year,
        'kms_driven': kms_driven,
        'company_' + company: 1,
        'fuel_type_' + fuel_type: 1
    }

    # Fill missing columns with 0
    input_df = pd.DataFrame([input_data])
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[model_columns]

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹{int(prediction):,}")
