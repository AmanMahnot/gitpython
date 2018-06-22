# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:38:44 2018

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("banknotes.csv")

iv=df.iloc[:,1:-1].values
dv=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split,cross_val_score
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(iv_train,dv_train)



# Predicting the Test set results
labels_pred = classifier.predict(iv_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(dv_test, labels_pred)

accuracy=cross_val_score(estimator=classifier,X=iv_train,y=dv_train,cv=10)
print("accuracy is",accuracy.mean())
print("standard deviation is",accuracy.std())