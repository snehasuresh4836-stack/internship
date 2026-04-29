import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("bank.csv")

X = df[["Salary"]]
Y = df["Bonus"]

model = LinearRegression()
model.fit(X, Y)


data = pd.DataFrame([[80000]], columns=["Salary"])
prediction = model.predict(data)

print("Predicted Bonus:", prediction)