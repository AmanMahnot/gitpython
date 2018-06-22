# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:11:23 2018

@author: user
"""

l=[]
while True:
    a=raw_input("enter the names ,age ,score :")
    if not a:
        break
    x=a.split(',')
    l.append((x[0],int(x[1]),int(x[2])))
l.sort()
print l

