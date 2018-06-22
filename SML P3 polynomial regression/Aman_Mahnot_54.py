# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 11:24:47 2018

@author: user
"""

import pandas as pd
df=pd.read_csv("bluegills.csv")
age_5 = df["length"][df["age"]==5]
iv=df.iloc[:,0:1].values
dv= df.iloc[:,1:2].values


from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(iv_train,dv_train)


import matplotlib.pyplot as plt
plt.scatter(iv_train,dv_train,color="red")
plt.plot(iv_train,re.predict(iv_train),color = 'blue')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
po=PolynomialFeatures(degree=6)
iv_pol=po.fit_transform(iv_train)

re2=LinearRegression()
re2.fit(iv_pol,dv_train)


plt.scatter(iv_train,dv_train,color="red")
plt.plot(iv_train,re2.predict(po.fit_transform(iv_train)),color = 'blue')
plt.show()

print "prediction through linear regression",re.predict(5)[0]
print "prediction through polynomial regression",re2.predict(po.fit_transform(5))
print "the length of a bluegill fish best related to its age by polynomial regression"