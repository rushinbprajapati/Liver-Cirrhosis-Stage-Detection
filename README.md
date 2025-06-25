# 🩺 Liver Cirrhosis Stage Detection

A Machine Learning-powered web app built with **Streamlit** to predict the **stage of liver cirrhosis** (Stage 1, 2, or 3) based on a patient's health data. The model is trained on the Mayo Clinic's PBC dataset and provides instant predictions through a user-friendly interface.

---

## 🚀 Features

- Predicts liver cirrhosis stage using clinical inputs
- Built with **Scikit-learn** (Random Forest Classifier)
- Real-time predictions via **Streamlit** web interface
- Easy to deploy and run locally or in the cloud

---

## 🗂️ Project Structure

liver_cirrhosis_app/
│
├── app.py # Streamlit frontend
├── cirrhosis_model.pkl # Trained ML model
├── scaler.pkl # Preprocessing scaler
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📊 Dataset

- **Source:** Mayo Clinic Study of Primary Biliary Cirrhosis (PBC)
- **Features:** Age, sex, bilirubin, albumin, copper, cholesterol, enzymes, etc.
- **Target:** Liver cirrhosis histologic stage (1, 2, 3)

---

## 🛠️ Setup Instructions

### 1. ✅ Clone the Repository or Download ZIP
```bash
git clone https://github.com/yourusername/liver-cirrhosis-app.git
cd liver-cirrhosis-app

    2. ✅ Create and Activate Virtual Environment (Optional but Recommended)
bash

python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows

3. ✅ Install Required Packages
bash

pip install -r requirements.txt

4. ✅ Run the Streamlit App
bash

streamlit run app.py