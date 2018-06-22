# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:18:44 2018

@author: user
"""

import numpy as np 
a = raw_input("enter the values ")
a=a.split(' ')
x = np.array(a,np.int64)
print x

b = x.reshape(3,3) 
print b 