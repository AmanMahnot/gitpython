# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:59:50 2018

@author: user
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")

df['Survived'].value_counts()

print df["Survived"].value_counts(normalize = True)

df_new=df.groupby(['Sex'])
print df_new["Survived"].value_counts()
print df_new["Survived"].value_counts(normalize = True)