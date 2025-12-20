import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
# data = pd.DataFrame(iris.data, columns=iris.feature_names)
# data['species']=iris.target
# data['species']=data['species'].replace(dict(enumerate(iris.target_names)))
# print(data.head())

X = iris.data[:, [0, 1]]
k = 3
print(X)
np.random.seed(42)
centroids = X[np.random.choice(X.shape[0], k, False)]
print(centroids)

def closest_centroids(X, centroids):
    distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis = 2))
    return np.argmin(distances, axis = 0)

def compute_centroid(X, labels, k):
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])

for _ in range(100):
    labels = closest_centroids(X, centroids)
    new_centroids = compute_centroid(X, labels, k)
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids
print("Final Centroid:\n ", centroids)

plt.figure(figsize=(7, 5))
colors = ['magenta', 'green', 'orange']
for i in range(k):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50, color=colors[i], label=f'Cluster{i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, color='black', marker='X', label='Centroids')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering (Scratch) - Iris Dataset')
plt.legend()
plt.show()