# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:58:12 2018

@author: Aman
"""

import pandas as pd

df=pd.read_csv("Cars.csv")
y=df.iloc[:,0]
x=df.iloc[:,1:]
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print x_train
print x_test
print y_train
print y_test
x_train.to_csv('x_train.csv',index=False)
x_test.to_csv('x_test.csv',index=False)
y_train.to_csv('y_train.csv',index=False)
y_test.to_csv('y_test.csv',index=False)