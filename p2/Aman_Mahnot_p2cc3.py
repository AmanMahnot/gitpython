# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:48:09 2018

@author: user
"""

a=raw_input("enter the string")
m=a[0]
for i in a[1:]:
    m+="*"+i
print m