# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:07:14 2018

@author: user
"""

import pandas as pd

df=pd.read_csv("Loan.csv")
df = df.drop("Loan_ID",axis=1)
x=df.iloc[:,0:-1].values
y=df.iloc[:,-1].values

'''new=pd.DataFrame(df).select_dtypes(include=[object])
string_col= list(new)
for i in string_col:
'''

import pandas as pd

loan = pd.read_csv("Loan.csv")

str_col_names = list(pd.DataFrame(loan).select_dtypes(include=[object]))

for i in str_col_names:
    loan[i] = loan[i].astype('category')
    loan[i] = loan[i].cat.codes

iv = loan.iloc[:, :-1]
dv = loan.iloc[:, -1]

iv = pd.get_dummies(iv, columns=["Property_Area"])

r, c = loan.shape

split_limit = r - int(r*20/100)

iv_train = iv.iloc[:split_limit, :]
iv_test = iv.iloc[split_limit:, :]
dv_train = dv.iloc[:split_limit]
dv_test = dv.iloc[split_limit:]

