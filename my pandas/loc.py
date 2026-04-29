import pandas as pd
df=pd.DataFrame({
    'Name':['Anu','Ammu','Anju'],
    'Age':[20,21,22]
})
# print(df.loc[1,'Name'])#[1:row,Name:column label]
# print(df.iloc[1,0])#[1:row,0:column index]
print(df.loc[0:1, ['Name', 'Age']])

