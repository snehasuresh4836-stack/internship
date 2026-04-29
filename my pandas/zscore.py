import pandas as pd
data=[10,12,14,15,18,20,22,100]
df=pd.DataFrame(data,columns=['x'])#DataFrame->class
print(df)
mean=df['x'].mean()#find mean
print('mean=',mean)
sd=df['x'].std()#find standard deviation
print('sd=',sd)

#find zscore
df['zscore']=(df['x']-mean)/sd #adding new zscore column and finding z score
print(df)

#outlier finding
outliers=df[df['zscore'].abs()>2]
print(outliers)
