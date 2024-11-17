import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
print(data.head())

x=data.iloc[:,:4]
print(x.head())

classifier = KMeans(n_clusters=3)
classifier.fit(x)
y=classifier.predict(x)

print(y)
print("\n")

centroid=classifier.cluster_centers_
print(centroid)

plt.scatter(x.iloc[:, 0], x.iloc[:, 1], c=y, cmap='viridis', s=50)
plt.scatter(centroid[:, 0], centroid[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("KMeans Clustering on Iris Data")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()
