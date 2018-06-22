# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 10:17:48 2018

@author: user
"""

import pandas as pd
import numpy as np
df=pd.read_csv("iq_size.csv")

iv=df.iloc[:,1:].values
dv=df.iloc[:,0:1].values


from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
re= LinearRegression()
re.fit(iv_train,dv_train)
re.predict(np.array([90,70,150]).reshape(1,-1))

import statsmodels.formula.api as sm
iv=np.append(arr=np.ones((38,1)).astype(int),values=iv,axis=1)
iv_opt=iv[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

iv_opt=iv[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

iv_opt=iv[:,[1,2]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

iv_opt=iv[:,[1]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

print "brain size is most useful"
