# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:52:22 2018

@author: user
"""

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("tshirts.csv")
iv=df.iloc[:,1:]

from sklearn.cluster import KMeans
wcss=[]
