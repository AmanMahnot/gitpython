# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:11:56 2018

@author: user
"""

import pandas as pd


c= pd.read_csv("Automobile.csv")

df=c['make'].value_counts()

df=pd.DataFrame({'make':df.index,'values':df.values})

import matplotlib.pyplot as plt
labels = df.iloc[:10,0]
sizes = df.iloc[:10,-1]
e=[0.2,0,0,0,0,0,0,0,0,0]
ax1 = plt.subplot()
ax1.pie(sizes,e, labels=labels, autopct='%1.2f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()