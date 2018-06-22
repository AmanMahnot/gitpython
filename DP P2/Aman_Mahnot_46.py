# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:11:12 2018

@author: user
"""

import pandas as pd
df=pd.read_csv("Loan.csv")
df = df.drop("Loan_ID",axis=1)
x=df.iloc[:,0:-1].values
y=df.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
for i in [0,1,2,3,4,10]:
    x[:,i]=labelencoder.fit_transform(x[:,i])

onehotencoder = OneHotEncoder(categorical_features=[10])
x=onehotencoder.fit_transform(x).toarray()  

y=labelencoder.fit_transform(y)
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
