import streamlit as st
import pickle
import numpy as np

# Load all the models

logreg_model = pickle.load(open('model/heart_model_logreg.pkl', 'rb'))
dt_model = pickle.load(open('model/heart_model_dt.pkl', 'rb'))
rf_model = pickle.load(open('model/heart_model_rf.pkl', 'rb'))
svm_model = pickle.load(open('model/heart_model_svm.pkl', 'rb'))

# Streamlit page title
st.title("Heart Disease Prediction")

# Input fields for user data
age = st.number_input("Age", min_value=1, max_value=120)
sex = st.selectbox("Sex", options=["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0)
chol = st.number_input("Cholesterol (mg/dl)", min_value=0)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
restecg = st.selectbox("Resting Electrocardiographic results", options=[0, 1, 2])
thalach = st.number_input("Max Heart Rate", min_value=50, max_value=250)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1])
oldpeak = st.number_input("ST Depression", min_value=0.0)
slope = st.selectbox("Slope (0-2)", options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", options=[0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1/2/3)", options=[1, 2, 3])

# Model selection dropdown
model_choice = st.selectbox("Select Model", options=["Logistic Regression", "Decision Tree", "Random Forest", "SVM"])

# Button to make prediction
if st.button("Predict"):
    # Convert inputs to appropriate format for prediction
    sex = 1 if sex == "Male" else 0
    inputs = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
        # Make prediction based on selected model
    if model_choice == "Logistic Regression":
        prediction = logreg_model.predict(inputs)
    elif model_choice == "Decision Tree":
        prediction = dt_model.predict(inputs)
    elif model_choice == "Random Forest":
        prediction = rf_model.predict(inputs)
    elif model_choice == "SVM":
        prediction = svm_model.predict(inputs)

    # Display result
    if prediction[0] == 1:
        st.write("The patient **has heart disease** 😟")
    else:
        st.write("The patient **does not have heart disease** 😊")
        
    