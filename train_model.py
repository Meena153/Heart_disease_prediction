
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pickle

# Load dataset
data = pd.read_csv('heart.csv')

# Features (X) and target (y)
X = data.drop('target', axis=1)
y = data['target']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression Model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
with open('model/heart_model_logreg.pkl', 'wb') as f:
    pickle.dump(logreg, f)

# Decision Tree Model
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
with open('model/heart_model_dt.pkl', 'wb') as f:
    pickle.dump(dt, f)

# Random Forest Model
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
with open('model/heart_model_rf.pkl', 'wb') as f:
    pickle.dump(rf, f)

# SVM Model
svm = SVC(random_state=42)
svm.fit(X_train, y_train)
with open('model/heart_model_svm.pkl', 'wb') as f:
    pickle.dump(svm, f)

print("Models trained and saved successfully!")
