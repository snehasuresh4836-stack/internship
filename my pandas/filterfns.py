import pandas as pd
df=pd.DataFrame({
    "Name":['sneha','nalanda','sinsila'],
    "Mark":[45,None,55]
})
#print(df.fillna(25))
print(df.dropna())#drop the none valued row 