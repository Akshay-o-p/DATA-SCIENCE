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

print(x)
print("\n")

centroid=classifier.cluster_centers_
print(centroid)

