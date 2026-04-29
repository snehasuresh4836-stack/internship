import pandas as pd
data=pd.read_csv("data2.csv")
df=pd.DataFrame(data)
#print(df)
#print(df[["Last","First"]])#extract first 2 columns
#print(df[df["Salary"]==52000])#filter
print(df.sort_index(axis=1,ascending=False))#sorting,axis=1 menas sort based on column and ascending=true means in order Z->A
print(df.sort_values (by='Salary'))#sort values in a spesific column

