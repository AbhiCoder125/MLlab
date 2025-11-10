# Simple Linear Regression using scikit-learn

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample Data (Hours Studied vs Marks Scored)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (reshaped for sklearn)
Y = np.array([2, 4, 5, 4, 5])                 # Dependent variable

# Step 1: Create and train the model
model = LinearRegression()
model.fit(X, Y)

# Step 2: Get the slope and intercept
b1 = model.coef_[0]
b0 = model.intercept_
print(f"Calculated coefficients:\nb0 (Intercept) = {b0}\nb1 (Slope) = {b1}")

# Step 3: Predict Y values
Y_pred = model.predict(X)

# Step 4: Plot the results
plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, Y_pred, color="red", label="Regression Line")
plt.xlabel("X - Independent Variable (e.g., Hours Studied)")
plt.ylabel("Y - Dependent Variable (e.g., Marks Scored)")
plt.title("Simple Linear Regression using scikit-learn")
plt.legend()
plt.show()
