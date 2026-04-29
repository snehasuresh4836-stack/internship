import pandas as pd
data={'age':[15,15,16,17,17,18,18,20,30]}
df=pd.DataFrame(data)#converting to dataframe
q1=df['age'].quantile(0.25)#first quartile
q3=df['age'].quantile(0.75)#second quartile
iqr=q3-q1#find interquartile rangr
lb=q1-1.5*iqr#lowerbound
ub=q3+1.5*iqr#upperbound
outliers=df[(df['age']<lb)|(df['age']>ub)]#find outliers

print('q1=',q1)
print('q3=',q3)
print('iqr=',iqr)
print('lowerbound=',lb)
print('upperbound=',ub)
print('\noutliers=',outliers)