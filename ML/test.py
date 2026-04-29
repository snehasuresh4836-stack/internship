#system predicting where the new datapoint add (0 or 1)
from sklearn.neighbors import KNeighborsClassifier
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
neigh = KNeighborsClassifier(n_neighbors=3)#object creation(neigh), k=3
neigh.fit(X, y)#fit means train the system
print(neigh.predict([[3.9]]))#new data point