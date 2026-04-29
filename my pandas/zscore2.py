import pandas as pd

data = {
    'sales': [120, 130, 125, 140, 135, 128, 132, 500, 520, 118,
              122, 127, 129, 131, 134, 136, 138, 121, 119, 600]
}

df = pd.DataFrame(data)
print(df)
mean=df['sales'].mean()
print('mean=',mean)
sd=df['sales'].std()
print('sd=',sd)
df['zscore']=(df['sales']-mean)/sd 
print(df)

outliers=df[df['zscore'].abs()>2]
print(outliers)
