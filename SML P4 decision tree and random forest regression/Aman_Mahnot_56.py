# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 12:26:15 2018

@author: user
"""

import pandas as pd
import numpy as np
df=pd.read_fwf("auto.txt",header=None)
df.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]

df["horsepower"] = df["horsepower"].replace(['?'], df.iloc[:,3].value_counts().index[0])
new=max(df["mpg"])
print df["car name"][df["mpg"]==new]


df.iloc[:,3]=pd.to_numeric(df.iloc[:,3])

iv=df.iloc[:,1:8]
dv=df.iloc[:,0]

from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)
 
from sklearn.tree import DecisionTreeRegressor
re=DecisionTreeRegressor()
re.fit(iv_train,dv_train)
print "the score of decision tree is",re.score(iv_test,dv_test)

print "prediction using decision tree is",re.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))

from sklearn.ensemble import RandomForestRegressor
re=RandomForestRegressor(n_estimators=10)
re.fit(iv_train,dv_train)
print "the score of random forest is",re.score(iv_test,dv_test)

print "hence random forest is more accurate in predicting the MPG value"

print "prediction using random forest is",re.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))









