# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:51:10 2018

@author: user
"""

import pandas as pd
import numpy as np
#Read csv file
df= pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
a= np.array(df['price'])
print 'min is:',np.min(a)
print 'max is:',np.max(a)
print 'avg is:',np.mean(a)
print 'std is:',np.std(a)