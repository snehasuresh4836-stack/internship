import pandas as pd
df=pd.DataFrame({
    "Fruits":['Apple','Orange','Mango','Grapes'],
    "Stock":[100,50,450,200],
    "price":[10000,5000,4500,2000]
})
#print(df)
#print(df["price"].max())#maximum price
#print(df["price"].min())#minimum price
print(df.describe())
