# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:11:07 2018

@author: user
"""

import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_csv("crime_data.csv")
iv=df.iloc[:,[1,2,4]].values



from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iv = pca.fit_transform(iv)
explained_variance = pca.explained_variance_ratio_


from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(iv)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(iv)

plt.scatter(iv[y_kmeans == 0, 0], iv[y_kmeans == 0, 1], s = 100, c = 'red', label = 'murder')
plt.scatter(iv[y_kmeans == 1, 0], iv[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'rape')
plt.scatter(iv[y_kmeans == 2, 0], iv[y_kmeans == 2, 1], s = 100, c = 'green', label = 'assault')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('KMEANS')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()