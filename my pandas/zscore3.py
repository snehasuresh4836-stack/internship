import pandas as pd

data = {
    'marks': [45, 50, 52, 48, 49, 51, 47, 46, 53, 54,
              50, 49, 48, 47, 46, 52, 51, 50, 49, 95]
}

df = pd.DataFrame(data)
print(df)
mean=df['marks'].mean()
print('mean=',mean)
sd=df['marks'].std()
print('sd=',sd)
df['zscore']=(df['marks']-mean)/sd 
print(df)

outliers=df[df['zscore'].abs()>2]
print(outliers)
