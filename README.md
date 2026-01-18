# Heart Disease Prediction using Machine Learning ❤️🩺

## 📌 Project Overview
Heart disease (cardiovascular disease) is one of the leading causes of mortality worldwide. Early prediction of heart disease plays a critical role in improving treatment outcomes and prevention strategies.

This project presents a **machine learning-based heart disease prediction system** using **supervised learning algorithms** to analyze patient health parameters and predict the likelihood of heart disease. The model is trained on medical data containing important indicators such as **age, blood pressure, cholesterol levels, heart rate**, and other clinical parameters.

---

## 🎯 Problem Statement
Heart disease diagnosis is complex and requires accurate decision-making based on multiple medical parameters. Manual diagnosis is time-consuming and may lead to uncertainty or errors.

This project aims to build a reliable and efficient **machine learning prediction system** that:
- takes patient medical data as input  
- processes the input through trained ML models  
- generates a prediction score indicating the likelihood of heart disease  

The goal is to assist healthcare professionals in **data-driven clinical decision-making**.

---

## 🧠 Machine Learning Models Used
The project uses multiple supervised classification algorithms and compares performance:

- ✅ Logistic Regression  
- ✅ Decision Tree  
- ✅ Random Forest  
- ✅ Support Vector Machine (SVM)

---

## 📚 Literature Survey (Summary)
Machine learning techniques are widely adopted in medical prediction and diagnosis. Heart disease detection is considered a critical task due to its high risk and varying symptoms.

Studies highlight:
- Supervised ML classification helps achieve better prediction accuracy.
- Random Forest models are highly effective in training medical datasets.
- Research by (Arslan, A.K. et al., 2016) suggests SVM and Penalized Logistic Regression (PLR) perform well for stroke prediction, with **SVM showing best performance**.
- Clinical databases like the **Kaggle Heart Disease dataset** provide key patient health indicators for training/testing models.

Dataset contains:
- Total **303 records** and **76 medical attributes**
- Reduced to **14 key attributes** for efficient training and prediction

---

## 📂 Dataset Information
**Source:** Kaggle Heart Disease Dataset  
The dataset includes clinical features used for prediction.

### ✅ Attributes Used (14 Features)
1. **Age** – age in years  
2. **Sex** – (1 = male, 0 = female)  
3. **cp** – chest pain type  
4. **trestbps** – resting blood pressure (mm Hg)  
5. **chol** – serum cholesterol (mg/dl)  
6. **fbs** – fasting blood sugar > 120 mg/dl (1 = true, 0 = false)  
7. **restecg** – resting electrocardiographic results  
8. **thalach** – maximum heart rate achieved  
9. **exang** – exercise induced angina (1 = yes, 0 = no)  
10. **oldpeak** – ST depression induced by exercise relative to rest  
11. **slope** – slope of peak exercise ST segment  
12. **ca** – number of major vessels (0–3) colored by fluoroscopy  
13. **thal** – (3 = normal, 6 = fixed defect, 7 = reversible defect)  
14. **target** – (1 = disease, 0 = no disease)

---

## 🧪 Methodology
1. **Dataset Collection** (Kaggle Heart Disease dataset)
2. **Data Cleaning & Preprocessing**
   - handling missing values (if any)
   - feature selection (14 attributes)
   - scaling/normalization (for models like SVM)
3. **Train-Test Split**
   - dataset split into training & testing sets
4. **Model Training**
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - SVM
5. **Evaluation Metrics**
   - Accuracy
   - Precision
   - Sensitivity (Recall)
   - Specificity

---

## 📊 Evaluation Metrics
The following performance measures are considered to compare models:
- ✅ Accuracy  
- ✅ Precision  
- ✅ Sensitivity / Recall  
- ✅ Specificity  

---

## 🛠️ Tools & Technologies Used
- **Programming Language:** Python  
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn *(optional)*  
- **Dataset:** Kaggle Heart Disease Dataset  
- **Models:** Logistic Regression, Decision Tree, Random Forest, SVM  

---

