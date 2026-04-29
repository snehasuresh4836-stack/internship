import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Age": [25,30,35,40,45,50,28,38,42,33],
    "BMI": [22,25,28,30,32,35,24,29,31,27],
    "BloodPressure": [80,85,88,92,95,100,82,90,94,87],
    "Glucose": [90,100,110,120,130,140,95,115,125,105],
    "Disease": [0,0,0,1,1,1,0,1,1,0]
}

df = pd.DataFrame(data)

# Features (X) and Target (Y)
X = df[["Age", "BMI", "BloodPressure", "Glucose"]]
Y = df["Disease"]

# Create model
model = LinearRegression()
# Train model
model.fit(X, Y)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
prediction=model.predict([[42,31,94,125]])
print("Predicted Disease Value:" ,prediction)

if prediction[0] >= 0.5:
    print("Disease = 1")
else:
    print("Disease = 0")