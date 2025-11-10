# Multiple Linear Regression using scikit-learn (Simplified + Visualization)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create dataset
data = {
    'Area': [1500, 1800, 2400, 3000, 3500],
    'Bedrooms': [3, 4, 3, 5, 4],
    'Age': [10, 15, 20, 8, 12],
    'Price': [400000, 500000, 600000, 650000, 700000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Step 2: Define independent and dependent variables
X = df[['Area', 'Bedrooms', 'Age']]  # Features
Y = df['Price']                      # Target variable

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X, Y)

# Step 4: Display coefficients
print("\nIntercept (b0):", model.intercept_)
print("Coefficients (b1, b2, b3):", model.coef_)

# Step 5: Predict values
Y_pred = model.predict(X)

# Step 6: Compare Actual vs Predicted
comparison = pd.DataFrame({'Actual Price': Y, 'Predicted Price': Y_pred})
print("\nActual vs Predicted Prices:\n", comparison)

# Step 7: Visualization
plt.figure(figsize=(6,4))
plt.scatter(range(len(Y)), Y, color='blue', label='Actual Price')
plt.plot(range(len(Y_pred)), Y_pred, color='red', marker='o', label='Predicted Price')
plt.xlabel('House Index')
plt.ylabel('Price')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.show()

# Step 8: Predict for a new house
new_house = np.array([[2500, 4, 5]])  # Example input
predicted_price = model.predict(new_house)
print("\nPredicted Price for new house (2500 sqft, 4 bedrooms, 5 years old):", predicted_price[0])