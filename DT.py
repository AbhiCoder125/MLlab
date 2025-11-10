# Decision Tree Classifier with Parameter Tuning using scikit-learn

import sys
import subprocess

def verify_packages():
    required_packages = ['pandas', 'sklearn', 'matplotlib']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verify and install required packages
verify_packages()

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 20, 50, 23, 37, 48],
    'Income': ['High', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'High', 'Medium'],
    'Student': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'Credit_Rating': ['Fair', 'Excellent', 'Fair', 'Fair', 'Excellent', 'Fair', 'Excellent', 'Fair', 'Excellent', 'Fair'],
    'Buys_Computer': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Step 2: Convert categorical data to numeric using Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

print("Encoded Dataset:\n", df)

# Step 3: Define features (X) and target (y)
X = df.drop('Buys_Computer', axis=1)
y = df['Buys_Computer']

# Step 4: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Create and train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate model performance
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Visualize the Decision Tree
plt.figure(figsize=(10,6))
plot_tree(model, filled=True, feature_names=list(X.columns), class_names=['No', 'Yes'])
plt.title("Decision Tree Classifier")
plt.show()

# Step 9: Parameter Tuning using GridSearchCV

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 3, 4, 5, None],
    'min_samples_split': [2, 3, 4, 5]
}

grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring='accuracy'
)

grid_search.fit(X_train, y_train)

print("\nBest Parameters Found:")
print(grid_search.best_params_)

# Step 10: Evaluate the tuned model
best_model = grid_search.best_estimator_
y_pred_tuned = best_model.predict(X_test)

print("\nTuned Model Accuracy:", accuracy_score(y_test, y_pred_tuned))
print("\nClassification Report after Tuning:\n", classification_report(y_test, y_pred_tuned))

