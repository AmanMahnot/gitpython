# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:19:39 2018

@author: user
"""

import pandas as pd
df=pd.read_csv("tree_addhealth.csv")
#df= df.apply(lambda x:x.fillna(x.value_counts().index[0]))

iv=df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]]
mf=iv.mode()
for i in range(0,15):
    iv.iloc[:,i] = iv.iloc[:,i].fillna(mf.iloc[0,i])
dv=df.iloc[:,7].values
from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
iv_train=sc.fit_transform(iv_train)
iv_test=sc.fit_transform(iv_test)

from sklearn.tree import DecisionTreeClassifier
c=DecisionTreeClassifier(criterion='entropy',random_state=0)
c.fit(iv_train,dv_train)

c.predict(iv_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(dv_test,c.predict(iv_test))
print "accuracy of model is",c.score(iv_test,dv_test)


############################################################################################################

import pandas as pd
df=pd.read_csv("tree_addhealth.csv")
df= df.apply(lambda x:x.fillna(x.value_counts().index[0]))
iv=df.iloc[:,[0,16]]
dv=df.iloc[:,21]

from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
iv_train=sc.fit_transform(iv_train)
iv_test=sc.fit_transform(iv_test)

from sklearn.tree import DecisionTreeClassifier
c=DecisionTreeClassifier(criterion='entropy',random_state=0)
c.fit(iv_train,dv_train)

c.predict(iv_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(dv_test,c.predict(iv_test))
print "accuracy of model is",c.score(iv_test,dv_test)

#####################################################################################################################


import pandas as pd
df=pd.read_csv("tree_addhealth.csv")
df= df.apply(lambda x:x.fillna(x.value_counts().index[0]))
iv=df.iloc[:,1:6]
dv=df.iloc[:,7]
from sklearn.model_selection import train_test_split
iv_train,iv_test,dv_train,dv_test=train_test_split(iv,dv,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
iv_train=sc.fit_transform(iv_train)
iv_test=sc.fit_transform(iv_test)

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
rfc.fit(iv_train,dv_train)

rfc.predict(iv_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(dv_test,rfc.predict(iv_test))
print "accuracy of model is",rfc.score(iv_test,dv_test)