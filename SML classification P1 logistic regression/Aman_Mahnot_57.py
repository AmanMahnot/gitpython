# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 11:05:03 2018

@author: user

Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.
NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

What percentage of total women actually had an affair?
(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
Optional

Build an optimum model, observe all the coefficients.
"""




import pandas as pd 
import numpy as np
df=pd.read_csv("affairs.csv")

iv=df.iloc[:,0:-1]
dv=df.iloc[:,-1]


iv=pd.get_dummies(iv,columns=["occupation"])
iv=iv.iloc[:,0:-1]
iv=pd.get_dummies(iv,columns=["occupation_husb"])
iv=iv.iloc[:,0:-1]

from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(iv_train,dv_train)

abc=pd.DataFrame(lr.predict(iv_test))
print "predicted values are",abc

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(dv_test,lr.predict(iv_test))

abc=pd.DataFrame(lr.predict(iv_test))
print "predicted values are",abc
print "score is",lr.score(iv_test,dv_test)
#abc[0].value_counts(normalize=True)
print "women actually had an affair",float(cm[0,1]+cm[1,1])/float(cm[0,0]+cm[0,1]+cm[1,1]+cm[1,0])

print "the prediction of new women is ",lr.predict(np.array([3,25,3,1,4,16,0,0,0,1,0,0,1,0,0,0]).reshape(1,-1))


import statsmodels.formula.api as sm
iv=np.append(arr=np.ones((6366,1)).astype(int),values=iv,axis=1)

iv_opt=iv[:,[0,1,2,3,4,5,6,7,8]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

iv_opt=iv[:,[0,1,2,3,5,6,7,8]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

iv_opt=iv[:,[0,1,2,3,5,6,7]]
regressor_OLS=sm.OLS(endog=dv,exog=iv_opt).fit()
regressor_OLS.summary()

