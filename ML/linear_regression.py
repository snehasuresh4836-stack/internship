import numpy as np
from sklearn.linear_model import LinearRegression

# Input data (hours studied)
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

# Output data (scores)
y = np.array([40,45,50,55,65,70,75,85,90,95])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Get slope (m) and intercept (b)
m = model.coef_[0]
b = model.intercept_

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict for 5.5 hours
pred = model.predict([[5.5]])
print(pred)