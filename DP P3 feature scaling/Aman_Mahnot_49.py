# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:57:52 2018

@author: user
"""

import pandas as pd
df=pd.read_csv("Red_wine.csv")



df.iloc[:,0] = df.apply(lambda x:x.fillna(x.value_counts().index[0]))

df.iloc[:,1:]=df.iloc[:,1:].fillna(df.iloc[:,1:].mean())

from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
labelencoder=LabelEncoder()
df.iloc[:,0]=labelencoder.fit_transform(df.iloc[:,0])


onehotencoder = OneHotEncoder(categorical_features=[0])
df=onehotencoder.fit_transform(df).toarray()  


iv=df[:,:-1]
dv=df[:,-1]

from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

sc = StandardScaler()

iv_train=sc.fit_transform(iv_train)
iv_test=sc.fit_transform(iv_test)
dv_train=sc.fit_transform(dv_train.reshape(-1,1))


#dv_test=sc.fit_transform(dv_test)
