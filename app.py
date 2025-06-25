import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('cirrhosis_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Liver Cirrhosis Stage Detection")

# Collect input from user
age = st.number_input("Age (in days)", value=20000)
sex = st.selectbox("Sex", ['Male', 'Female'])
bilirubin = st.number_input("Bilirubin (mg/dl)", value=1.0)
albumin = st.number_input("Albumin (gm/dl)", value=3.5)
prothrombin = st.number_input("Prothrombin Time (s)", value=10.0)
ascites = st.selectbox("Ascites", ['No', 'Yes'])
edema = st.selectbox("Edema", ['No', 'Slight', 'Severe'])
status = st.selectbox("Status", ['C', 'CL', 'D'])
drug = st.selectbox("Drug", ['D-penicillamine', 'Placebo'])
hepatomegaly = st.selectbox("Hepatomegaly", ['No', 'Yes'])
spiders = st.selectbox("Spiders", ['No', 'Yes'])
cholesterol = st.number_input("Cholesterol (mg/dl)", value=300.0)
copper = st.number_input("Copper (ug/day)", value=50.0)
alk_phos = st.number_input("Alkaline Phosphatase (U/l)", value=300.0)
sgot = st.number_input("SGOT (U/ml)", value=120.0)
triglycerides = st.number_input("Triglycerides (mg/dl)", value=200.0)
platelets = st.number_input("Platelets (per 1000/ml)", value=250.0)

# Encoding
sex = 1 if sex == 'Male' else 0
ascites = 1 if ascites == 'Yes' else 0
edema = {'No': 0, 'Slight': 1, 'Severe': 2}[edema]
status = {'C': 0, 'CL': 1, 'D': 2}[status]
drug = 0 if drug == 'D-penicillamine' else 1
hepatomegaly = 1 if hepatomegaly == 'Yes' else 0
spiders = 1 if spiders == 'Yes' else 0

# Create feature vector
features = np.array([[0, status, drug, age, sex, ascites, hepatomegaly, spiders, edema,
                      bilirubin, cholesterol, albumin, copper, alk_phos,
                      sgot, triglycerides, platelets, prothrombin]])

# Scale input
features_scaled = scaler.transform(features)

# Predict
if st.button("Predict Stage"):
    stage = model.predict(features_scaled)[0]
    st.success(f"Predicted Liver Cirrhosis Stage: {stage}")

