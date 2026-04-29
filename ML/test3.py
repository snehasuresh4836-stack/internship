from sklearn.neighbors import KNeighborsClassifier
X=[[1.5,7],[2.0,6],[2.5,5],[3.0,6],[3.5,7],[4.0,5],[4.5,6],[5.0,7],[1.0,8],[2.0,8]]
y=['fail','fail','fail','pass','pass','pass','pass','pass','fail','fail']
n1=KNeighborsClassifier(n_neighbors=3)
n1.fit(X,y)
print(n1.predict([[3.2,6]]))