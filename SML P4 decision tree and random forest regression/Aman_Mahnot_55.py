# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:22:32 2018

@author: user
"""

import pandas as pd
import numpy as np
df=pd.read_csv("PastHires.csv")
iv=df.iloc[:,0:6]
dv=df.iloc[:,6:7]
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for i in range(1,6):
    iv.iloc[:,i]=labelencoder.fit_transform(iv.iloc[:,i])
dv=labelencoder.fit_transform(dv)
from sklearn.tree import DecisionTreeRegressor
re=DecisionTreeRegressor()
re.fit(iv,dv)




from sklearn.ensemble import RandomForestRegressor
re=RandomForestRegressor(n_estimators=10)
re.fit(iv,dv)
pre=re.predict(np.array([10,1,4,0,1,0]).reshape(1,-1))
pre1=re.predict(np.array([10,1,4,1,0,1]).reshape(1,-1))