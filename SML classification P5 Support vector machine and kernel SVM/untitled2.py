# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:21:47 2018

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('breast_cancer.csv')
df=df.iloc[:,:] = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
iv=df.iloc[:,1:-1].values
dv=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split as t
iv_train,iv_test,dv_train,dv_test=t(iv,dv,test_size=0.2,random_state=0)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iv_train = pca.fit_transform(iv_train)
iv_test = pca.transform(iv_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(iv_train, dv_train)

# Predicting the Test set results
labels_pred = classifier.predict(iv_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, labels_pred)

# Model Score
score = classifier.score(iv_test,dv_test)

print 'pridiction is',classifier.predict(pca.transform([[6,2,5,3,2,7,9,2,4]]))

print "women has Malignant tumor"

from matplotlib.colors import ListedColormap
X_set, y_set = iv_test, dv_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('restult of cancer')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()
