import pandas as pd

data = {
    'marks': [45, 50, 52, 48, 49, 51, 47, 46, 53, 54,
              50, 49, 48, 47, 46, 52, 51, 50, 49, 95]
}

df = pd.DataFrame(data)
print(df)
q1=df['marks'].quantile(0.25)
q3=df['marks'].quantile(0.75)
iqr=q3-q1
lb=q1-1.5*iqr
ub=q3+1.5*iqr
outliers=df[(df['marks']<lb)|(df['marks']>ub)]
print(q1)
print(q3)
print(iqr)
print(lb)
print(ub)
print(outliers)
