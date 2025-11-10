# ==========================================
# LASSO & RIDGE REGRESSION - DISEASE RISK
# ==========================================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\DATA_E\MY_PROJECTS\MLlab\Dataset\health_lifestyle_dataset.csv")

print("✅ Dataset Loaded Successfully!")
print(df.head())

# Drop non-informative column if any
if 'id' in df.columns:
    df.drop(columns=['id'], inplace=True)

# Encode categorical columns
label_encoder = LabelEncoder()
if 'gender' in df.columns:
    df['gender'] = label_encoder.fit_transform(df['gender'])  # Male=1, Female=0

# Separate features and target
X = df.drop(columns=['disease_risk'])
y = df['disease_risk']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training & testing data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

#Train Lasso and Ridge Models
lasso = Lasso(alpha=0.1)
ridge = Ridge(alpha=0.1)

lasso.fit(X_train, y_train)
ridge.fit(X_train, y_train)

# Predictions
y_pred_lasso = lasso.predict(X_test)
y_pred_ridge = ridge.predict(X_test)


print("\n📊 Model Performance Comparison:")
print("-" * 50)

# Lasso Evaluation
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso Regression → MSE: {mse_lasso:.4f}, R²: {r2_lasso:.4f}")

# Ridge Evaluation
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"Ridge Regression → MSE: {mse_ridge:.4f}, R²: {r2_ridge:.4f}")

# ------------------------------------------
print("\n🔍 Feature Importance (Lasso):")
for feature, coef in zip(X.columns, lasso.coef_):
    print(f"{feature}: {coef:.4f}")

print("\n🔍 Feature Importance (Ridge):")
for feature, coef in zip(X.columns, ridge.coef_):
    print(f"{feature}: {coef:.4f}")


# Performance Metrics Comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# MSE Comparison
metrics_data = pd.DataFrame({
    'Algorithm': ['Lasso', 'Ridge'],
    'MSE': [mse_lasso, mse_ridge],
    'R²': [r2_lasso, r2_ridge]
})

sns.barplot(x='Algorithm', y='MSE', data=metrics_data, ax=ax1, palette='Set2')
ax1.set_title('Mean Squared Error Comparison')
ax1.set_ylabel('MSE')

# R² Score Comparison
sns.barplot(x='Algorithm', y='R²', data=metrics_data, ax=ax2, palette='Set2')
ax2.set_title('R² Score Comparison')
ax2.set_ylabel('R² Score')

plt.tight_layout()
plt.show()

# Coefficient Comparison
plt.figure(figsize=(12, 6))
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Lasso Coefficients': lasso.coef_,
    'Ridge Coefficients': ridge.coef_
})

coef_df_melted = coef_df.melt(id_vars=['Feature'], 
                             var_name='Algorithm', 
                             value_name='Coefficient')

sns.barplot(x='Feature', y='Coefficient', hue='Algorithm', data=coef_df_melted)
plt.xticks(rotation=45, ha='right')
plt.title('Feature Coefficients: Lasso vs Ridge')
plt.tight_layout()
plt.show()
