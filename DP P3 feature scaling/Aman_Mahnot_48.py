# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:03:07 2018

@author: user
"""

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None,
     usecols=[0,1,2]
    )
df.columns = ['Class label', 'Alcohol', 'Malic acid']


from sklearn.preprocessing import StandardScaler,MinMaxScaler
sc=StandardScaler()
df.iloc[:,[1,2]]=sc.fit_transform(df.iloc[:,[1,2]])


mms=MinMaxScaler()
df1=mms.fit_transform(df)