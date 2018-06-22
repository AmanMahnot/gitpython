# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:04:00 2018

@author: user
"""

import pandas as pd
df1=pd.read_csv("weather-faridabad.csv")
df1=df1.iloc[:,1:]
df2=pd.read_csv("weather-ghaziabad.csv")
df2=df2.iloc[:,1:]
df3=pd.read_csv("weather-sonipat.csv")
df3=df3.iloc[:,1:]
df4=pd.read_csv("weather-delhi.csv")
df4=df4.iloc[:,1:]

new_df1 = df1.merge(df2, on='Time')
new_df2 = new_df1.merge(df3,on='Time')
df= new_df2.merge(df4,on='Time')

features=df.iloc[:,[0,1,2,3,4,5,7,8,9,10,11,13,14,15,16,17]]
labels=df.iloc[:,19:-1]


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
for i in range(1,16):
    features.iloc[:,i]=labelencoder.fit_transform(features.iloc[:,i])
for i in range(0,5):
    labels.iloc[:,i]=labelencoder.fit_transform(labels.iloc[:,i])

features['Time']=features['Time'].replace(":","", regex=True)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.linear_model import LinearRegression
re=LinearRegression()
re.fit(features_train,labels_train)
label_predict=re.predict(features_train)
score = re.score(features_test,labels_test)















from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = re, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())

