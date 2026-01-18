# Heart Disease Prediction using Machine Learning ❤️🩺

## 📌 Project Overview
Heart disease (cardiovascular disease) is one of the leading causes of mortality worldwide. Early detection plays a crucial role in preventing severe complications and enabling timely treatment.This project implements a **machine learning-based heart disease prediction system** using supervised learning algorithms. The model analyzes patient medical parameters such as **age, blood pressure, cholesterol, heart rate**, etc., and predicts the **likelihood of heart disease**.The system was implemented as a **desktop-based machine learning application**, making it user-friendly and accessible.

---

## 🎯 Objective
- Predict whether a patient is likely to have heart disease using medical parameters.
- Compare multiple supervised ML classifiers and evaluate their performance.
- Identify the best performing model for effective heart disease prediction.
- Support healthcare professionals in early diagnosis through a data-driven tool.

---

## ❓ Problem Statement
Heart disease diagnosis is often a complex process, and symptoms can vary significantly among patients. Manual diagnosis may lead to incorrect assumptions and delayed treatment.  
To address this, the project builds a prediction system using ML models trained on clinical data to improve early detection accuracy.

---

## 📚 Literature Survey Summary
Machine learning has been increasingly used in healthcare for analyzing and predicting medical conditions.
Key insights from existing studies include:
- **Supervised machine learning classification models** offer better diagnosis accuracy.
- Research shows that **SVM and Random Forest** often produce strong predictive performance.
- Heart disease datasets from clinical repositories like the **Kaggle Heart Disease dataset** are commonly used for predictive modeling.
- Model evaluation metrics include **accuracy, precision, sensitivity, and specificity**.

---

## 🗂 Dataset Description
The dataset contains clinical health indicators, including:

### 📌 Attributes Used (14 Features)
1. **Age** — Age in years  
2. **Sex** — (1 = male, 0 = female)  
3. **CP** — Chest pain type  
4. **Trestbps** — Resting blood pressure (mm Hg)  
5. **Chol** — Serum cholesterol (mg/dl)  
6. **Fbs** — Fasting blood sugar > 120 mg/dl (1=true, 0=false)  
7. **Restecg** — Resting electrocardiographic results  
8. **Thalach** — Maximum heart rate achieved  
9. **Exang** — Exercise induced angina (1=yes, 0=no)  
10. **Oldpeak** — ST depression induced by exercise  
11. **Slope** — Slope of peak exercise ST segment  
12. **CA** — Number of major vessels (0–3)  
13. **Thal** — 3=normal, 6=fixed defect, 7=reversible defect  
14. **Target** — 1 = heart disease, 0 = no heart disease  

📌 Original dataset: **303 records with 76 attributes**, reduced to **14 key features** for better performance and efficiency.

---

## 🧠 Machine Learning Algorithms Used
This project uses 4 supervised learning algorithms:

- ✅ Logistic Regression  
- ✅ Decision Tree  
- ✅ Random Forest  
- ✅ Support Vector Machine (SVM)

---

## 🧪 Methodology
1. Data Collection (Kaggle Heart Disease Dataset)
2. Data Cleaning & Preprocessing
3. Feature Selection (Reduced dataset to 14 important features)
4. Train-Test Split
5. Model Training (4 classifiers)
6. Evaluation (Accuracy comparison)
7. Deployment (Desktop-based application)

---

## 📊 Model Evaluation
Each algorithm was evaluated primarily using:
- Accuracy

📌 Key Finding:
- **Random Forest produced higher accuracy compared to Logistic Regression**
- Best performing model was selected for prediction use.

---

## 🛠 Tools & Technologies Used
- **Python**
- **Machine Learning (Scikit-learn)**
- **Pandas / NumPy** (Data preprocessing)
- **Matplotlib / Seaborn** (optional visualizations)
- **Desktop Application Interface** (Python-based)

---

## 🚀 Future Enhancements
- Add more performance metrics: Precision, Recall, F1-score, ROC-AUC
- Hyperparameter tuning using GridSearchCV/RandomSearchCV
- Deploy as a Web App (Streamlit / Flask)
- Integrate real-time patient form input and report generation
- Add explainability using SHAP / LIME

---
## ✅ Conclusion
This project demonstrates the practical application of traditional machine learning algorithms for predicting heart disease based on real-world medical data.

- Built a supervised ML prediction model using 4 classifiers.
- Trained and evaluated each model for performance.
- Identified the best model (Random Forest performed better in accuracy).
- Implemented the system as a desktop-based application for user-friendly access.

This tool can support early diagnosis and assist healthcare decision-making through data-driven predictions.

---
