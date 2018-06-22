# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:39:23 2018

@author: user
"""

import pandas as pd
df = pd.read_csv("Bahubali2_vs_Dangal.csv")


b_iv=df.iloc[:,0:1].values
b_dv=df.iloc[:,1:2].values

d_iv=df.iloc[:,0:1].values
d_dv=df.iloc[:,2:3].values


from sklearn.model_selection import train_test_split
b_iv_train,b_iv_test,b_dv_train,b_dv_test=train_test_split(b_iv,b_dv,test_size = 0.2,random_state=0)
d_iv_train,d_iv_test,d_dv_train,d_dv_test=train_test_split(d_iv,d_dv,test_size = 0.2,random_state=0)

from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(b_iv_train,b_dv_train)
b_dv_pred=re.predict(b_iv_test)
b_score = re.score(b_iv_test,b_dv_test)
print "bahubali 10th day collection",re.predict(10)




re.fit(d_iv_train,d_dv_train)
d_dv_pred=re.predict(d_iv_test)
d_score = re.score(d_iv_test,d_dv_test)
print "dangal 10th day collection",re.predict(10)