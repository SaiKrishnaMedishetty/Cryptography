# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("C:/Users/smedishetty1/Downloads/synthetic_classification_dataset.csv")

# Check for missing values
print(data.isnull().sum())

# Split the data into features and target variable
X = data.drop('Target', axis=1)
y = data['Target']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_pred_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_prob)
    
    return accuracy, precision, recall, f1, roc_auc

# Dictionary to store the results
results = {}

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
results['Logistic Regression'] = evaluate_model(lr, X_test, y_test)

# K-Nearest Neighbors
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
results['K-Nearest Neighbors'] = evaluate_model(knn, X_test, y_test)

# Support Vector Machine
svm = SVC(probability=True)
svm.fit(X_train, y_train)
results['Support Vector Machine'] = evaluate_model(svm, X_test, y_test)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
results['Decision Tree'] = evaluate_model(dt, X_test, y_test)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
results['Random Forest'] = evaluate_model(rf, X_test, y_test)

# Gradient Boosting Machines
gbm = GradientBoostingClassifier()
gbm.fit(X_train, y_train)
results['Gradient Boosting Machines'] = evaluate_model(gbm, X_test, y_test)

# XGBoost
xgb_clf = xgb.XGBClassifier()
xgb_clf.fit(X_train, y_train)
results['XGBoost'] = evaluate_model(xgb_clf, X_test, y_test)

# LightGBM
lgb_clf = lgb.LGBMClassifier()
lgb_clf.fit(X_train, y_train)
results['LightGBM'] = evaluate_model(lgb_clf, X_test, y_test)

# CatBoost
cat_clf = CatBoostClassifier(verbose=0)
cat_clf.fit(X_train, y_train)
results['CatBoost'] = evaluate_model(cat_clf, X_test, y_test)

# Convert results to DataFrame for better visualization
results_df = pd.DataFrame(results, index=['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC-AUC']).T
print(results_df)

# Plot the results
plt.figure(figsize=(12, 8))
sns.barplot(data=results_df)
plt.title('Comparison of Machine Learning Models')
plt.xticks(rotation=45)
plt.show()
