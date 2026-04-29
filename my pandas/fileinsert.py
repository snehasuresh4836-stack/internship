import pandas as pd
data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
# print(df)
# print(df.info())#summarize
# print(df.head(5))#first 5 records
print(df[["Household_ID","Month"]])#display a column
