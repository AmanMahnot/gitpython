# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:23:46 2018

@author: user
"""

import pandas as pd
df=pd.read_csv("election_data.csv")
df=df.iloc[:,[4,6]]
df_1 = df[df.duplicated(subset=['Name_of_Candidate','Constituency_no'], keep=False)]

df_2=df[~df.index.isin(df_1.index)]