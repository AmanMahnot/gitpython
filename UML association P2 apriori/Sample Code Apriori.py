# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:16:33 2017

@author: Kunal

@Topic: Apriori
"""

# Importing the libraries
import pandas as pd
from apyori import apriori

# Data of a week's transaction in a store, 
# each row represents a single customer
data = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
transactions = []
for i in range(7501):
    transactions.append([str(data.values[i,j]) for j in range(20)])

# Training Apriori on the Data
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2,
                min_lift = 3, min_length = 2)

# Visualising the Results
results = list(rules)
