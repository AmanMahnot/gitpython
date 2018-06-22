# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:01:07 2018

@author: user
"""

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris = pca.fit_transform(iris)

explained_variance = pca.explained_variance_ratio_
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(iris)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(iris)

# Visualising the clusters
plt.scatter(iris[y_kmeans == 0, 0], iris[y_kmeans == 0, 1], s = 100, c = 'red', label = 'image 1')
plt.scatter(iris[y_kmeans == 1, 0], iris[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'image 2')
plt.scatter(iris[y_kmeans == 2, 0], iris[y_kmeans == 2, 1], s = 100, c = 'green', label = 'image 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('KMEANS')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

iris.column("w","e","t","y")