# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:57:56 2018

@author: user
"""
dict1 = {'a':0, 'b':0, 'c':0}
inp = input("Enter values for a,b,c: ")
j = 0
for i in dict1.keys():
    dict1[i] = inp[j]
    j = j + 1

def fix_teen(n):
    if n in range(13,20):
        if n==15 or n==16:
            return n
        else:
            return 0
    else:
        return n
a=sum(map(fix_teen, dict1.values()))
print "Sum =",a