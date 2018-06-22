# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:57:06 2018

@author: user
"""

import pandas as pd

df =pd.read_csv("Foodtruck.csv")


iv = df.iloc[:,0:1].values
dv = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test = train_test_split(iv,dv,test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(iv_train,dv_train)


dv_pred=re.predict(iv_test)
score = re.score(iv_test,dv_test)





import matplotlib.pyplot as plt
plt.scatter(iv_train,dv_train,color='red')
plt.plot(iv_train,re.predict(iv_train),color = 'blue')
plt.show()



plt.scatter(iv_test,dv_test,color='red')
plt.plot(iv_train,re.predict(iv_train),color = 'blue')
plt.show()

print re.predict(3.073)
