# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:39:36 2018

@author: user
"""

a=raw_input("enter the string")
vowels="AaEeIiOoUu "
list1=list(a)
i=0
while i<len(list1):
    if list1[i] in vowels:
        i=i+1
    else:
        list1.insert(i+1,"o"+list1[i])
        i=i+2
b="".join(list1)
print b