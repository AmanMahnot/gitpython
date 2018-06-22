# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:15:54 2018

@author: user
"""

import pandas as pd 
df=pd.read_csv("Automobile.csv")


datatypes="data types are",df.dtypes
print datatypes


new_df=pd.DataFrame(df).select_dtypes(include=[object])
string_col=list(new_df)

df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))


from sklearn.preprocessing import Imputer,LabelEncoder ,OneHotEncoder

labelencoder = LabelEncoder()
for i in string_col:
    df[i]=labelencoder.fit_transform(df[i])


onehotencoder = OneHotEncoder(categorical_features=[6,7])
df=onehotencoder.fit_transform(df).toarray()