import pandas as pd

data = {
    'sales': [120, 130, 125, 140, 135, 128, 132, 500, 520, 118,
              122, 127, 129, 131, 134, 136, 138, 121, 119, 600]
}

df = pd.DataFrame(data)
print(df)
q1=df['sales'].quantile(0.25)
q3=df['sales'].quantile(0.75)
iqr=q3-q1
lb=q1-1.5*iqr
ub=q3+1.5*iqr
outliers=df[(df['sales']<lb)|(df['sales']>ub)]
print(q1)
print(q3)
print(iqr)
print(lb)
print(ub)
print(outliers)
