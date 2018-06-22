# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:41:39 2018

@author: user
"""

import pandas as pd
i=0

df = pd.read_csv("training_titanic.csv")
df["child"] = 0
df["child"][df["Age"] < 18] = 1

df_new=df.groupby(['child'])
print df_new["Survived"].value_counts()
print df_new["Survived"].value_counts(normalize = True)





